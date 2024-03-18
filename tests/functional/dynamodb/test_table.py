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
import json

from botocore.stub import Stubber

import boto3
from tests import unittest


class TestTableResourceCustomizations(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.resource = boto3.resource('dynamodb', 'us-east-1')
        self.table = self.resource.Table('mytable')

    def test_resource_has_batch_writer_added(self):
        assert hasattr(self.table, 'batch_writer')

    def test_operation_without_output(self):
        stubber = Stubber(self.table.meta.client)
        stubber.add_response('tag_resource', {})
        arn = 'arn:aws:dynamodb:us-west-2:123456789:table/mytable'

        with stubber:
            self.table.meta.client.tag_resource(
                ResourceArn=arn, Tags=[{'Key': 'project', 'Value': 'val'}]
            )

        stubber.assert_no_pending_responses()

    def test_batch_write_does_not_double_serialize(self):
        # If multiple items reference the same Python object, the
        # object does not get double-serialized.
        # https://github.com/boto/boto3/issues/3474

        used_twice = {'pkey': 'foo1', 'otherfield': {'foo': 1, 'bar': 2}}
        batch_writer = self.table.batch_writer()

        # The default Stubber compares the request payload to the
        # "expected_params" before automatic serialization happens. This custom
        # event handler uses the same technique as the Stubber to record the
        # serialized request body, but later in the request lifecycle.
        class LateStubber:
            def __init__(self, client):
                self.intercepted_request_body = None
                client.meta.events.register_first(
                    'before-call.*.*',
                    self.late_request_interceptor,
                )

            def late_request_interceptor(self, event_name, params, **kwargs):
                if self.intercepted_request_body is not None:
                    raise AssertionError(
                        'LateStubber was called more than once, but only one '
                        'request is expected'
                    )
                body_str = params.get('body', b'').decode('utf-8')
                try:
                    self.intercepted_request_body = json.loads(body_str)
                except Exception:
                    raise AssertionError(
                        'Expected JSON request body, but failed to JSON decode'
                    )

        late_stubber = LateStubber(self.table.meta.client)

        with Stubber(self.table.meta.client) as stubber:
            stubber.add_response(
                'batch_write_item',
                service_response={'UnprocessedItems': {}},
            )
            batch_writer.put_item(Item=used_twice)
            batch_writer.put_item(Item=used_twice)
            batch_writer._flush()

        expected_request_body = {
            'RequestItems': {
                'mytable': [
                    {
                        'PutRequest': {
                            'Item': {
                                'pkey': {'S': 'foo1'},
                                'otherfield': {
                                    'M': {'foo': {'N': '1'}, 'bar': {'N': '2'}}
                                },
                            }
                        }
                    },
                    {
                        'PutRequest': {
                            'Item': {
                                'pkey': {'S': 'foo1'},
                                'otherfield': {
                                    'M': {'foo': {'N': '1'}, 'bar': {'N': '2'}}
                                },
                            }
                        }
                    },
                ]
            }
        }

        assert late_stubber.intercepted_request_body == expected_request_body
