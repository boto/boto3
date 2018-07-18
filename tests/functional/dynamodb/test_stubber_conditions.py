# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from botocore.stub import Stubber

import boto3
from boto3.dynamodb.conditions import Attr, Key
from tests import unittest


class TestStubberSupportsFilterExpressions(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.resource = boto3.resource('dynamodb', 'us-east-1')

    def test_table_query_can_be_stubbed_with_expressions(self):
        table = self.resource.Table('mytable')

        stubber = Stubber(table.meta.client)
        stubber.add_response('query', dict(Items=list()), expected_params=dict(
                TableName='mytable',
                KeyConditionExpression=Key('mykey').eq('testkey'),
                FilterExpression=Attr('myattr').eq('foo') & (Attr('myattr2').lte('buzz') | Attr('myattr2').gte('fizz'))
        ))

        with stubber:
            response = table.query(KeyConditionExpression=Key('mykey').eq('testkey'),
                                   FilterExpression=Attr('myattr').eq('foo') & (Attr('myattr2').lte('buzz') | Attr('myattr2').gte('fizz')))

        self.assertEqual(list(), response['Items'])
        stubber.assert_no_pending_responses()

    def test_table_scan_can_be_stubbed_with_expressions(self):
        table = self.resource.Table('mytable')

        stubber = Stubber(table.meta.client)
        stubber.add_response('scan', dict(Items=list()), expected_params=dict(
                TableName='mytable',
                FilterExpression=Attr('myattr').eq('foo') & (Attr('myattr2').lte('buzz') | Attr('myattr2').gte('fizz'))
        ))

        with stubber:
            response = table.scan(FilterExpression=Attr('myattr').eq('foo') & (Attr('myattr2').lte('buzz') | Attr('myattr2').gte('fizz')))

        self.assertEqual(list(), response['Items'])
        stubber.assert_no_pending_responses()
