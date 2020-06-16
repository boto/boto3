# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from botocore.errorfactory import ClientError
from botocore.exceptions import MissingParametersError

from boto3.sqs.queue import BatchSender, QueueResource
from tests import unittest, mock


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock()
        self.meta = mock.Mock(client=self.client)
        self.queue_url = 'queue_url'
        self.queue = QueueResource()
        self.queue.meta = self.meta
        self.queue.url = self.queue_url

    def test_create_batch_sender_with_defaults(self):
        batch_sender = self.queue.batch_sender()
        self.assertEquals(BatchSender._DEFAULT_OVERWRITE_BY_ID, batch_sender._overwrite_by_id)
        self.assertEquals(self.queue_url, batch_sender._queue_url)
        self.assertEquals(self.client, batch_sender._client)
        self.assertEquals(BatchSender._DEFAULT_FLUSH_AMOUNT, batch_sender._flush_amount)
        self.assertEquals(BatchSender._DEFAULT_MAX_SEND_ATTEMPTS, batch_sender._max_send_attempts)
        self.assertEquals(BatchSender._DEFAULT_MAX_BACKOFF_SLEEP_SECS, batch_sender._max_backoff_sleep_secs)

    def test_create_batch_sender_with_overrides(self):
        batch_sender = self.queue.batch_sender(overwrite_by_id=True, flush_amount=7, max_send_attempts=23,
                                               max_backoff_sleep_secs=42)
        self.assertTrue(batch_sender._overwrite_by_id)
        self.assertEquals(self.queue_url, batch_sender._queue_url)
        self.assertEquals(self.client, batch_sender._client)
        self.assertEquals(7, batch_sender._flush_amount)
        self.assertEquals(23, batch_sender._max_send_attempts)
        self.assertEquals(42, batch_sender._max_backoff_sleep_secs)


class BatchSenderTest(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock()
        self.client.send_message_batch.return_value = {'Successful': [], 'Failed': []}
        self.queue_url = 'queue_url'
        self.flush_amount = 2
        self.batch_sender = BatchSender(self.queue_url, self.client,
                                        overwrite_by_id=True,
                                        flush_amount=self.flush_amount,
                                        max_send_attempts=2,
                                        max_backoff_sleep_secs=0.0000001)

    def test_send_message_does_not_immediately_send(self):
        self.batch_sender.send_message(Id='1', MessageBody=b'')
        self.assertFalse(self.client.send_message_batch.called)
        self.assertFalse(self.client.send_messages.called)

    def test_send_message_flushes_at_flush_amount(self):
        self.batch_sender.send_message(Id='1', MessageBody=b'')
        self.batch_sender.send_message(Id='2', MessageBody=b'')
        expected = [{"QueueUrl": "queue_url",
                     "Entries": [{'Id': '1', 'MessageBody': b''},
                                 {'Id': '2', 'MessageBody': b''}]}]
        self.assert_send_message_batch_calls_are(expected)
        self.assert_messages_buffer_empty()

    def test_multiple_flushes_reset_messages_to_send(self):
        self.batch_sender.send_message(Id='1', MessageBody=b'')
        self.batch_sender.send_message(Id='2', MessageBody=b'')
        self.batch_sender.send_message(Id='3', MessageBody=b'')
        self.batch_sender.send_message(Id='4', MessageBody=b'')

        first_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '1', 'MessageBody': b''},
                                   {'Id': '2', 'MessageBody': b''}]}
        second_batch = {"QueueUrl": "queue_url",
                        "Entries": [{'Id': '3', 'MessageBody': b''},
                                    {'Id': '4', 'MessageBody': b''}]}
        self.assert_send_message_batch_calls_are([first_batch, second_batch])
        self.assert_messages_buffer_empty()

    def test_flush_resends_batch_on_repeatedly_fully_unprocessed_batch(self):
        self.client.send_message_batch.side_effect = [
            {
                'Failed': [{"Id": "1", "SenderFault": False},
                           {"Id": "2", "SenderFault": False}]
            },
            {
                'Failed': [{"Id": "1", "SenderFault": False},
                           {"Id": "2", "SenderFault": False}]
            },
            {
                'Failed': []
            },
            {
                'Failed': []
            }
        ]
        with self.batch_sender:
            self.batch_sender.send_message(Id='1', MessageBody=b'')
            self.batch_sender.send_message(Id='2', MessageBody=b'')
            self.batch_sender.send_message(Id='3', MessageBody=b'')

        first_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '1', 'MessageBody': b''},
                                   {'Id': '2', 'MessageBody': b''}]}
        second_batch = {"QueueUrl": "queue_url",
                        "Entries": [{'Id': '3', 'MessageBody': b''}]}
        self.assert_send_message_batch_calls_are([first_batch, first_batch, first_batch, second_batch])
        self.assert_messages_buffer_empty()

    def test_fails_on_failed_send_because_of_sender_fault(self):
        self.client.send_message_batch.side_effect = [
            {
                'Failed': [{"Id": "1", "SenderFault": True, "Code": "Code"},
                           {"Id": "2", "SenderFault": False, "Code": "Code"}]
            }
        ]
        with self.assertRaises(ClientError) as context:
            self.batch_sender.send_message(Id='1', MessageBody=b'')
            self.batch_sender.send_message(Id='2', MessageBody=b'')

            self.assertEqual(context.exception, "Code")
        self.assert_messages_buffer_is([{"Id": '2', "MessageBody": b''}])

    def test_unprocessed_items_added_to_next_batch(self):
        # Suppose the server sends backs a response that indicates that
        # one item was unprocessed.
        self.client.send_message_batch.side_effect = [
            {
                'Failed': [{"Id": "2", "SenderFault": False}]
            },
            # Then everything went through
            {},
            {}
        ]
        with self.batch_sender:
            self.batch_sender.send_message(Id='1', MessageBody=b'')
            self.batch_sender.send_message(Id='2', MessageBody=b'')
            self.batch_sender.send_message(Id='3', MessageBody=b'')
            self.batch_sender.send_message(Id='4', MessageBody=b'')

        first_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '1', 'MessageBody': b''},
                                   {'Id': '2', 'MessageBody': b''}]}
        second_batch = {"QueueUrl": "queue_url",
                        "Entries": [{'Id': '2', 'MessageBody': b''},
                                    {'Id': '3', 'MessageBody': b''}]}
        third_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '4', 'MessageBody': b''}]}
        self.assert_send_message_batch_calls_are([first_batch, second_batch, third_batch])
        self.assert_messages_buffer_empty()

    def test_all_messages_sent_on_exit(self):
        with self.batch_sender as b:
            b.send_message(Id='1', MessageBody=b'')
        self.assert_send_message_batch_calls_are([{"QueueUrl": "queue_url",
                                                   "Entries": [{'Id': '1', 'MessageBody': b''}]}])
        self.assert_messages_buffer_empty()

    def test_never_send_more_than_max_batch_size(self):
        # Suppose the server sends backs a response that indicates that
        # all the items were unprocessed.
        self.client.send_message_batch.side_effect = [
            {
                'Failed': [{"Id": "1", "SenderFault": False},
                           {"Id": "2", "SenderFault": False}]
            },
            {},
            # Then the last response shows that everything went through
            {}
        ]
        with BatchSender(self.queue_url, self.client, flush_amount=2) as b:
            b.send_message(Id='1', MessageBody=b'')
            b.send_message(Id='2', MessageBody=b'')
            b.send_message(Id='3', MessageBody=b'')

        # Note how we're never sending more than flush_amount=2.
        first_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '1', 'MessageBody': b''},
                                   {'Id': '2', 'MessageBody': b''}]}
        # Even when the server sends us unprocessed items of 2 elements,
        # we'll still only send 2 at a time, in order.
        second_batch = {"QueueUrl": "queue_url",
                        "Entries": [{'Id': '1', 'MessageBody': b''},
                                    {'Id': '2', 'MessageBody': b''}]}
        # And then we still see one more unprocessed item so
        # we need to send another batch.
        third_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '3', 'MessageBody': b''}]}
        self.assert_send_message_batch_calls_are([first_batch, second_batch,
                                                  third_batch])
        self.assert_messages_buffer_empty()

    def test_repeated_flushing_on_exit(self):
        # We're going to simulate failed items
        # returning multiple failed items across calls.
        self.client.send_message_batch.side_effect = [
            {
                'Failed': [
                    {"Id": "2", "SenderFault": False}
                ],
            },
            {
                'Failed': [
                    {"Id": "2", "SenderFault": False}
                ],
            },
            {}
        ]
        with BatchSender(self.queue_url, self.client, overwrite_by_id=False, flush_amount=2) as b:
            b.send_message(Id='1', MessageBody=b'')
            b.send_message(Id='2', MessageBody=b'')
        # So when we exit, we expect three calls.
        # First we try the normal batch write with 3 items:
        first_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '1', 'MessageBody': b''},
                                   {'Id': '2', 'MessageBody': b''}]}
        second_batch = {"QueueUrl": "queue_url",
                        "Entries": [{'Id': '2', 'MessageBody': b''}]}
        third_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '2', 'MessageBody': b''}]}
        self.assert_send_message_batch_calls_are([first_batch, second_batch,
                                                  third_batch])
        self.assert_messages_buffer_empty()

    def test_auto_dedup_for_dup_requests_at_the_beginning(self):
        with BatchSender(self.queue_url, self.client,
                         flush_amount=2, overwrite_by_id=True) as b:
            b.send_message(Id='1', MessageBody=b'first')
            b.send_message(Id='1', MessageBody=b'second')
            b.send_message(Id='1', MessageBody=b'third')
            b.send_message(Id='2', MessageBody=b'')

        first_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '1', 'MessageBody': b'third'},
                                   {'Id': '2', 'MessageBody': b''}]}
        self.assert_send_message_batch_calls_are([first_batch])
        self.assert_messages_buffer_empty()

    def test_auto_dedup_for_dup_requests_at_the_end_with_flush_in_between(self):
        with BatchSender(self.queue_url, self.client,
                         flush_amount=2, overwrite_by_id=True) as b:
            b.send_message(Id='1', MessageBody=b'')
            b.send_message(Id='2', MessageBody=b'first')
            b.send_message(Id='2', MessageBody=b'second')
            b.send_message(Id='2', MessageBody=b'third')

        first_batch = {"QueueUrl": "queue_url",
                       "Entries": [{'Id': '1', 'MessageBody': b''},
                                   {'Id': '2', 'MessageBody': b'first'}]}
        second_batch = {"QueueUrl": "queue_url",
                        "Entries": [{'Id': '2', 'MessageBody': b'third'}]}
        self.assert_send_message_batch_calls_are([first_batch, second_batch])
        self.assert_messages_buffer_empty()

    def test_fails_on_missing_id(self):
        with self.assertRaises(MissingParametersError) as context:
            self.batch_sender.send_message()

        self.assertEqual(str(context.exception), "The following required parameters are missing for Message: Id")
        self.assert_messages_buffer_empty()

    def test_flush_aborts_on_repeated_failure(self):
        # We're going to simulate failed items
        # returning multiple failed items across calls.
        self.client.send_message_batch.side_effect = [
            {
                'Failed': [
                    {"Id": "1", "SenderFault": False, "Code": "Code"}
                ],
            },
            {
                'Failed': [
                    {"Id": "1", "SenderFault": False, "Code": "Code"}
                ],
            },
            {
                'Failed': [
                    {"Id": "1", "SenderFault": False, "Code": "Code"}
                ],
            }
        ]
        with self.assertRaises(ClientError):
            self.batch_sender.send_message(Id='1', MessageBody=b'')
            self.batch_sender.flush()
        self.assert_messages_buffer_is([{"Id": '1', "MessageBody": b''}])

    def assert_send_message_batch_calls_are(self, expected_calls):
        self.assertEqual(self.client.send_message_batch.call_count,
                         len(expected_calls))
        calls = [c[1] for c in self.client.send_message_batch.call_args_list]
        self.assertEqual(expected_calls, calls)

    def assert_messages_buffer_empty(self):
        self.assertEquals([], self.batch_sender._messages_buffer)

    def assert_messages_buffer_is(self, expected_messages_buffer):
        self.assertEquals(expected_messages_buffer, self.batch_sender._messages_buffer)
