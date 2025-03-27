# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from boto3.dynamodb.table import BatchWriter
from tests import mock, unittest


class BaseTransformationTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.client = mock.Mock()
        self.client.batch_write_item.return_value = {'UnprocessedItems': {}}
        self.table_name = 'tablename'
        self.flush_amount = 2
        self.batch_writer = BatchWriter(
            self.table_name, self.client, self.flush_amount
        )

    def assert_batch_write_calls_are(self, expected_batch_writes):
        assert self.client.batch_write_item.call_count == len(
            expected_batch_writes
        )
        batch_write_calls = [
            args[1] for args in self.client.batch_write_item.call_args_list
        ]
        assert batch_write_calls == expected_batch_writes

    def test_batch_write_does_not_immediately_write(self):
        self.batch_writer.put_item(Item={'Hash': 'foo'})
        assert not self.client.batch_write_item.called

    def test_batch_write_flushes_at_flush_amount(self):
        self.batch_writer.put_item(Item={'Hash': 'foo1'})
        self.batch_writer.put_item(Item={'Hash': 'foo2'})
        expected = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            }
        }
        self.assert_batch_write_calls_are([expected])

    def test_multiple_flushes_reset_items_to_put(self):
        self.batch_writer.put_item(Item={'Hash': 'foo1'})
        self.batch_writer.put_item(Item={'Hash': 'foo2'})
        self.batch_writer.put_item(Item={'Hash': 'foo3'})
        self.batch_writer.put_item(Item={'Hash': 'foo4'})
        # We should have two batch calls, one for foo1,foo2 and
        # one for foo3,foo4.
        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            }
        }
        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo4'}}},
                ]
            }
        }
        self.assert_batch_write_calls_are([first_batch, second_batch])

    def test_can_handle_puts_and_deletes(self):
        self.batch_writer.put_item(Item={'Hash': 'foo1'})
        self.batch_writer.delete_item(Key={'Hash': 'foo2'})
        expected = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'DeleteRequest': {'Key': {'Hash': 'foo2'}}},
                ]
            }
        }
        self.assert_batch_write_calls_are([expected])

    def test_multiple_batch_calls_with_mixed_deletes(self):
        self.batch_writer.put_item(Item={'Hash': 'foo1'})
        self.batch_writer.delete_item(Key={'Hash': 'foo2'})
        self.batch_writer.delete_item(Key={'Hash': 'foo3'})
        self.batch_writer.put_item(Item={'Hash': 'foo4'})
        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'DeleteRequest': {'Key': {'Hash': 'foo2'}}},
                ]
            }
        }
        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {'DeleteRequest': {'Key': {'Hash': 'foo3'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo4'}}},
                ]
            }
        }
        self.assert_batch_write_calls_are([first_batch, second_batch])

    def test_unprocessed_items_added_to_next_batch(self):
        self.client.batch_write_item.side_effect = [
            {
                'UnprocessedItems': {
                    self.table_name: [
                        {'PutRequest': {'Item': {'Hash': 'foo2'}}}
                    ],
                },
            },
            # Then the last response shows that everything went through
            {'UnprocessedItems': {}},
        ]
        self.batch_writer.put_item(Item={'Hash': 'foo1'})
        self.batch_writer.put_item(Item={'Hash': 'foo2'})
        self.batch_writer.put_item(Item={'Hash': 'foo3'})

        # We should have sent two batch requests consisting of 2
        # 2 requests.  foo1,foo2 and foo2,foo3.
        # foo2 is sent twice because the first response has it listed
        # as an unprocessed item which means it needs to be part
        # of the next batch.
        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            }
        }
        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                ]
            }
        }
        self.assert_batch_write_calls_are([first_batch, second_batch])

    def test_all_items_flushed_on_exit(self):
        with self.batch_writer as b:
            b.put_item(Item={'Hash': 'foo1'})
        self.assert_batch_write_calls_are(
            [
                {
                    'RequestItems': {
                        self.table_name: [
                            {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                        ]
                    },
                },
            ]
        )

    def test_never_send_more_than_max_batch_size(self):
        # Suppose the server sends backs a response that indicates that
        # all the items were unprocessed.
        self.client.batch_write_item.side_effect = [
            {
                'UnprocessedItems': {
                    self.table_name: [
                        {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                        {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                    ],
                },
            },
            {
                'UnprocessedItems': {
                    self.table_name: [
                        {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                    ],
                },
            },
            {'UnprocessedItems': {}},
        ]
        with BatchWriter(self.table_name, self.client, flush_amount=2) as b:
            b.put_item(Item={'Hash': 'foo1'})
            b.put_item(Item={'Hash': 'foo2'})
            b.put_item(Item={'Hash': 'foo3'})

        # Note how we're never sending more than flush_amount=2.
        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            }
        }
        # Even when the server sends us unprocessed items of 2 elements,
        # we'll still only send 2 at a time, in order.
        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            }
        }
        # And then we still see one more unprocessed item so
        # we need to send another batch.
        third_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            }
        }
        self.assert_batch_write_calls_are(
            [first_batch, second_batch, third_batch]
        )

    def test_repeated_flushing_on_exit(self):
        # We're going to simulate unprocessed_items
        # returning multiple unprocessed items across calls.
        self.client.batch_write_item.side_effect = [
            {
                'UnprocessedItems': {
                    self.table_name: [
                        {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                        {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                    ],
                },
            },
            {
                'UnprocessedItems': {
                    self.table_name: [
                        {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                    ],
                },
            },
            {'UnprocessedItems': {}},
        ]
        with BatchWriter(self.table_name, self.client, flush_amount=4) as b:
            b.put_item(Item={'Hash': 'foo1'})
            b.put_item(Item={'Hash': 'foo2'})
            b.put_item(Item={'Hash': 'foo3'})
        # So when we exit, we expect three calls.
        # First we try the normal batch write with 3 items:
        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                ]
            }
        }
        # Then we see two unprocessed items so we send another batch.
        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                ]
            }
        }
        # And then we still see one more unprocessed item so
        # we need to send another batch.
        third_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                ]
            }
        }
        self.assert_batch_write_calls_are(
            [first_batch, second_batch, third_batch]
        )

    def test_auto_dedup_for_dup_requests(self):
        with BatchWriter(
            self.table_name,
            self.client,
            flush_amount=5,
            overwrite_by_pkeys=["pkey", "skey"],
        ) as b:
            # dup 1
            b.put_item(
                Item={'pkey': 'foo1', 'skey': 'bar1', 'other': 'other1'}
            )
            b.put_item(
                Item={'pkey': 'foo1', 'skey': 'bar1', 'other': 'other2'}
            )
            # dup 2
            b.delete_item(
                Key={
                    'pkey': 'foo1',
                    'skey': 'bar2',
                }
            )
            b.put_item(
                Item={'pkey': 'foo1', 'skey': 'bar2', 'other': 'other3'}
            )
            # dup 3
            b.put_item(
                Item={'pkey': 'foo2', 'skey': 'bar2', 'other': 'other3'}
            )
            b.delete_item(
                Key={
                    'pkey': 'foo2',
                    'skey': 'bar2',
                }
            )
            # dup 4
            b.delete_item(
                Key={
                    'pkey': 'foo2',
                    'skey': 'bar3',
                }
            )
            b.delete_item(
                Key={
                    'pkey': 'foo2',
                    'skey': 'bar3',
                }
            )
            # 5
            b.delete_item(
                Key={
                    'pkey': 'foo3',
                    'skey': 'bar3',
                }
            )
            # 2nd batch
            b.put_item(
                Item={'pkey': 'foo1', 'skey': 'bar1', 'other': 'other1'}
            )
            b.put_item(
                Item={'pkey': 'foo1', 'skey': 'bar1', 'other': 'other2'}
            )

        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {
                        'PutRequest': {
                            'Item': {
                                'pkey': 'foo1',
                                'skey': 'bar1',
                                'other': 'other2',
                            }
                        }
                    },
                    {
                        'PutRequest': {
                            'Item': {
                                'pkey': 'foo1',
                                'skey': 'bar2',
                                'other': 'other3',
                            }
                        }
                    },
                    {
                        'DeleteRequest': {
                            'Key': {
                                'pkey': 'foo2',
                                'skey': 'bar2',
                            }
                        }
                    },
                    {
                        'DeleteRequest': {
                            'Key': {
                                'pkey': 'foo2',
                                'skey': 'bar3',
                            }
                        }
                    },
                    {
                        'DeleteRequest': {
                            'Key': {
                                'pkey': 'foo3',
                                'skey': 'bar3',
                            }
                        }
                    },
                ]
            }
        }
        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {
                        'PutRequest': {
                            'Item': {
                                'pkey': 'foo1',
                                'skey': 'bar1',
                                'other': 'other2',
                            }
                        }
                    },
                ]
            }
        }
        self.assert_batch_write_calls_are([first_batch, second_batch])

    def test_added_unsent_request_not_flushed_put(self):
        # If n requests that get sent fail to process where n = flush_amount
        # and at least one more request gets created before the second attempt,
        # then previously if n requests were successful on the next run and
        # returned an empty dict, _item_buffer would be emptied before sending
        # the next batch of n requests
        self.client.batch_write_item.side_effect = [
            {
                'UnprocessedItems': {
                    self.table_name: [
                        {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                        {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                    ],
                },
            },
            {
                'UnprocessedItems': {},
            },
            {
                'UnprocessedItems': {},
            },
        ]
        self.batch_writer.put_item({'Hash': 'foo1'})
        self.batch_writer.put_item({'Hash': 'foo2'})
        self.batch_writer.put_item({'Hash': 'foo3'})
        self.assertIn(
            {'PutRequest': {'Item': {'Hash': 'foo3'}}},
            self.batch_writer._items_buffer,
        )
        batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            }
        }
        final_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo4'}}},
                ]
            }
        }
        # same batch sent twice since all failed on first try
        # and flush_items = 2
        self.assert_batch_write_calls_are([batch, batch])
        # test that the next two items get sent
        self.batch_writer.put_item({'Hash': 'foo4'})
        self.assert_batch_write_calls_are([batch, batch, final_batch])
        # the buffer should be empty now
        self.assertEqual(self.batch_writer._items_buffer, [])

    def test_added_unsent_request_not_flushed_delete(self):
        # If n requests that get sent fail to process where n = flush_amount
        # and at least one more request gets created before the second attempt,
        # then previously if n requests were successful on the next run and
        # returned an empty dict, _item_buffer would be emptied before sending
        # the next batch of n requests
        self.client.batch_write_item.side_effect = [
            {
                'UnprocessedItems': {
                    self.table_name: [
                        {'DeleteRequest': {'Key': {'Hash': 'foo1'}}},
                        {'DeleteRequest': {'Key': {'Hash': 'foo2'}}},
                    ],
                },
            },
            {
                'UnprocessedItems': {},
            },
            {
                'UnprocessedItems': {},
            },
        ]
        self.batch_writer.delete_item({'Hash': 'foo1'})
        self.batch_writer.delete_item({'Hash': 'foo2'})
        self.batch_writer.delete_item({'Hash': 'foo3'})
        self.assertIn(
            {'DeleteRequest': {'Key': {'Hash': 'foo3'}}},
            self.batch_writer._items_buffer,
        )
        batch = {
            'RequestItems': {
                self.table_name: [
                    {'DeleteRequest': {'Key': {'Hash': 'foo1'}}},
                    {'DeleteRequest': {'Key': {'Hash': 'foo2'}}},
                ]
            }
        }
        final_batch = {
            'RequestItems': {
                self.table_name: [
                    {'DeleteRequest': {'Key': {'Hash': 'foo3'}}},
                    {'DeleteRequest': {'Key': {'Hash': 'foo4'}}},
                ]
            }
        }
        # same batch sent twice since all failed on first try
        # and flush_items = 2
        self.assert_batch_write_calls_are([batch, batch])
        # test that the next two items get sent
        self.batch_writer.delete_item({'Hash': 'foo4'})
        self.assert_batch_write_calls_are([batch, batch, final_batch])
        # the buffer should be empty now
        self.assertEqual(self.batch_writer._items_buffer, [])

    def test_consumed_capacity_agg_total(self):
        self.client.batch_write_item.side_effect = [
            {
                'ConsumedCapacity': [
                    {
                        'TableName': self.table_name,
                        'CapacityUnits': 5.0,
                    }
                ],
                'UnprocessedItems': {},
            },
            {
                'ConsumedCapacity': [
                    {
                        'TableName': self.table_name,
                        'CapacityUnits': 5.0,
                    }
                ],
                'UnprocessedItems': {},
            },
        ]

        # ReturnConsumedCapacity=TOTAL
        with BatchWriter(
            self.table_name,
            self.client,
            flush_amount=2,
            return_consumed_capacity='TOTAL',
        ) as b:
            b.put_item(Item={'Hash': 'foo1'})
            b.put_item(Item={'Hash': 'foo2'})
            b.put_item(Item={'Hash': 'foo3'})
            b.put_item(Item={'Hash': 'foo4'})

        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            },
            'ReturnConsumedCapacity': 'TOTAL',
        }

        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo4'}}},
                ]
            },
            'ReturnConsumedCapacity': 'TOTAL',
        }
        self.assert_batch_write_calls_are([first_batch, second_batch])

        self.assertEqual(
            b.consumed_capacity,
            [
                {
                    'TableName': self.table_name,
                    'CapacityUnits': 10.0,
                }
            ],
        )

    def test_consumed_capacity_agg_none(self):
        with BatchWriter(
            self.table_name,
            self.client,
            flush_amount=2,
            return_consumed_capacity='NONE',
        ) as b:
            b.put_item(Item={'Hash': 'foo1'})
            b.put_item(Item={'Hash': 'foo2'})
            b.put_item(Item={'Hash': 'foo3'})
            b.put_item(Item={'Hash': 'foo4'})

        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            },
            'ReturnConsumedCapacity': 'NONE',
        }

        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo4'}}},
                ]
            },
            'ReturnConsumedCapacity': 'NONE',
        }
        self.assert_batch_write_calls_are([first_batch, second_batch])

        self.assertIs(b.consumed_capacity, None)

    def test_consumed_capacity_agg_indexes(self):
        # Operation is on a table so there will be no split
        self.client.batch_write_item.side_effect = [
            {
                'ConsumedCapacity': [
                    {
                        'TableName': self.table_name,
                        'CapacityUnits': 45.0,
                        'ReadCapacityUnits': 18.0,
                        'WriteCapacityUnits': 27.0,
                        'Table': {
                            'CapacityUnits': 5.0,
                            'ReadCapacityUnits': 2.0,
                            'WriteCapacityUnits': 3.0,
                        },
                        'LocalSecondaryIndexes': {
                            'FirstLSI': {
                                'CapacityUnits': 10.0,
                                'ReadCapacityUnits': 4.0,
                                'WriteCapacityUnits': 6.0,
                            },
                            'SecondLSI': {
                                'CapacityUnits': 20.0,
                                'ReadCapacityUnits': 8.0,
                                'WriteCapacityUnits': 12.0,
                            },
                        },
                        'GlobalSecondaryIndexes': {
                            'FirstGSI': {
                                'CapacityUnits': 10.0,
                                'ReadCapacityUnits': 4.0,
                                'WriteCapacityUnits': 6.0,
                            },
                        },
                    }
                ],
                'UnprocessedItems': {},
            },
            {
                'ConsumedCapacity': [
                    {
                        'TableName': self.table_name,
                        'CapacityUnits': 55.0,
                        'ReadCapacityUnits': 22.0,
                        'WriteCapacityUnits': 33.0,
                        'Table': {
                            'CapacityUnits': 5.0,
                            'ReadCapacityUnits': 2.0,
                            'WriteCapacityUnits': 3.0,
                        },
                        'LocalSecondaryIndexes': {
                            'SecondLSI': {
                                'CapacityUnits': 20.0,
                                'ReadCapacityUnits': 8.0,
                                'WriteCapacityUnits': 12.0,
                            },
                            'ThirdLSI': {
                                'CapacityUnits': 30.0,
                                'ReadCapacityUnits': 12.0,
                                'WriteCapacityUnits': 18.0,
                            },
                        },
                    }
                ],
                'UnprocessedItems': {},
            },
            {
                'ConsumedCapacity': [
                    {
                        'TableName': self.table_name,
                        'CapacityUnits': 55.0,
                        'ReadCapacityUnits': 22.0,
                        'WriteCapacityUnits': 33.0,
                        'Table': {
                            'CapacityUnits': 5.0,
                            'ReadCapacityUnits': 2.0,
                            'WriteCapacityUnits': 3.0,
                        },
                        'LocalSecondaryIndexes': {
                            'FourthLSI': {
                                'CapacityUnits': 40.0,
                                'ReadCapacityUnits': 16.0,
                                'WriteCapacityUnits': 24.0,
                            }
                        },
                        'GlobalSecondaryIndexes': {
                            'FirstGSI': {
                                'CapacityUnits': 10.0,
                                'ReadCapacityUnits': 4.0,
                                'WriteCapacityUnits': 6.0,
                            },
                        },
                    }
                ],
                'UnprocessedItems': {},
            },
        ]

        with BatchWriter(
            self.table_name,
            self.client,
            flush_amount=2,
            return_consumed_capacity='INDEXES',
        ) as b:
            b.put_item(Item={'Hash': 'foo1'})
            b.put_item(Item={'Hash': 'foo2'})
            b.put_item(Item={'Hash': 'foo3'})
            b.put_item(Item={'Hash': 'foo4'})
            b.put_item(Item={'Hash': 'foo5'})
            b.put_item(Item={'Hash': 'foo6'})

        first_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo1'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo2'}}},
                ]
            },
            'ReturnConsumedCapacity': 'INDEXES',
        }

        second_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo3'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo4'}}},
                ]
            },
            'ReturnConsumedCapacity': 'INDEXES',
        }

        third_batch = {
            'RequestItems': {
                self.table_name: [
                    {'PutRequest': {'Item': {'Hash': 'foo5'}}},
                    {'PutRequest': {'Item': {'Hash': 'foo6'}}},
                ]
            },
            'ReturnConsumedCapacity': 'INDEXES',
        }
        self.assert_batch_write_calls_are(
            [first_batch, second_batch, third_batch]
        )

        self.assertEqual(
            b.consumed_capacity,
            [
                {
                    'TableName': self.table_name,
                    'CapacityUnits': 155.0,
                    'ReadCapacityUnits': 62.0,
                    'WriteCapacityUnits': 93.0,
                    'Table': {
                        'CapacityUnits': 15.0,
                        'ReadCapacityUnits': 6.0,
                        'WriteCapacityUnits': 9.0,
                    },
                    'LocalSecondaryIndexes': {
                        'FirstLSI': {
                            'CapacityUnits': 10.0,
                            'ReadCapacityUnits': 4.0,
                            'WriteCapacityUnits': 6.0,
                        },
                        'SecondLSI': {
                            'CapacityUnits': 40.0,
                            'ReadCapacityUnits': 16.0,
                            'WriteCapacityUnits': 24.0,
                        },
                        'ThirdLSI': {
                            'CapacityUnits': 30.0,
                            'ReadCapacityUnits': 12.0,
                            'WriteCapacityUnits': 18.0,
                        },
                        'FourthLSI': {
                            'CapacityUnits': 40.0,
                            'ReadCapacityUnits': 16.0,
                            'WriteCapacityUnits': 24.0,
                        },
                    },
                    'GlobalSecondaryIndexes': {
                        'FirstGSI': {
                            'CapacityUnits': 20.0,
                            'ReadCapacityUnits': 8.0,
                            'WriteCapacityUnits': 12.0,
                        },
                    },
                }
            ],
        )
