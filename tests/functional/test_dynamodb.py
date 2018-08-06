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
import json
from tests import unittest, mock

from botocore.awsrequest import AWSResponse

from boto3.session import Session
from boto3.dynamodb.conditions import Attr


class TestDynamoDB(unittest.TestCase):
    def setUp(self):
        self.http_response = AWSResponse(None, 200, {}, None)
        self.parsed_response = {}
        self.make_request_patch = mock.patch(
            'botocore.endpoint.Endpoint.make_request')
        self.make_request_mock = self.make_request_patch.start()
        self.make_request_mock.return_value = (
            self.http_response, self.parsed_response)
        self.session = Session(
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy',
            region_name='us-east-1')

    def tearDown(self):
        self.make_request_patch.stop()

    def test_resource(self):
        dynamodb = self.session.resource('dynamodb')
        table = dynamodb.Table('MyTable')
        # Make sure it uses the high level interface
        table.scan(FilterExpression=Attr('mykey').eq('myvalue'))
        request = self.make_request_mock.call_args_list[0][0][1]
        request_params = json.loads(request['body'].decode('utf-8'))
        self.assertEqual(
            request_params,
            {'TableName': 'MyTable',
             'FilterExpression': '#n0 = :v0',
             'ExpressionAttributeNames': {'#n0': 'mykey'},
             'ExpressionAttributeValues': {':v0': {'S': 'myvalue'}}}
        )

    def test_client(self):
        dynamodb = self.session.client('dynamodb')
        # Make sure the client still uses the botocore level interface
        dynamodb.scan(
            TableName='MyTable',
            FilterExpression='#n0 = :v0',
            ExpressionAttributeNames={'#n0': 'mykey'},
            ExpressionAttributeValues={':v0': {'S': 'myvalue'}}
        )
        request = self.make_request_mock.call_args_list[0][0][1]
        request_params = json.loads(request['body'].decode('utf-8'))
        self.assertEqual(
            request_params,
            {'TableName': 'MyTable',
             'FilterExpression': '#n0 = :v0',
             'ExpressionAttributeNames': {'#n0': 'mykey'},
             'ExpressionAttributeValues': {':v0': {'S': 'myvalue'}}}
        )
