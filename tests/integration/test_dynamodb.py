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
import copy
from decimal import Decimal

import boto3.session
from boto3.dynamodb.types import Binary
from boto3.dynamodb.conditions import Attr, Key
from tests import unittest, unique_id


class BaseDynamoDBTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session = boto3.session.Session(region_name='us-west-2')
        cls.dynamodb = cls.session.resource('dynamodb')
        cls.table_name = unique_id('boto3db')
        cls.item_data = {
            'MyHashKey': 'mykey',
            'MyNull': None,
            'MyBool': True,
            'MyString': 'mystring',
            'MyNumber': Decimal('1.25'),
            'MyBinary': Binary(b'\x01'),
            'MyStringSet': set(['foo']),
            'MyNumberSet': set([Decimal('1.25')]),
            'MyBinarySet': set([Binary(b'\x01')]),
            'MyList': ['foo'],
            'MyMap': {'foo': 'bar'}
        }
        cls.table = cls.dynamodb.create_table(
            TableName=cls.table_name,
            ProvisionedThroughput={"ReadCapacityUnits": 5,
                                   "WriteCapacityUnits": 5},
            KeySchema=[{"AttributeName": "MyHashKey", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "MyHashKey",
                                   "AttributeType": "S"}])
        waiter = cls.dynamodb.meta.client.get_waiter('table_exists')
        waiter.wait(TableName=cls.table_name)

    @classmethod
    def tearDownClass(cls):
        cls.table.delete()


class TestDynamoDBTypes(BaseDynamoDBTest):
    def test_put_get_item(self):
        self.table.put_item(Item=copy.deepcopy(self.item_data))
        self.addCleanup(self.table.delete_item, Key={'MyHashKey': 'mykey'})
        response = self.table.get_item(Key={'MyHashKey': 'mykey'})
        self.assertEqual(response['Item'], self.item_data)


class TestDynamoDBConditions(BaseDynamoDBTest):
    @classmethod
    def setUpClass(cls):
        super(TestDynamoDBConditions, cls).setUpClass()
        cls.table.put_item(Item=copy.deepcopy(cls.item_data))

    @classmethod
    def tearDownClass(cls):
        cls.table.delete_item(Key={'MyHashKey': 'mykey'})
        super(TestDynamoDBConditions, cls).setUpClass()

    def test_filter_expression(self):
        response = self.table.scan(
            FilterExpression=Attr('MyHashKey').eq('mykey'))
        self.assertEqual(response['Count'], 1)

    def test_key_condition_expression(self):
        response = self.table.query(
            KeyConditionExpression=Key('MyHashKey').eq('mykey'))
        self.assertEqual(response['Count'], 1)

    def test_key_condition_with_filter_condition_expression(self):
        response = self.table.query(
            KeyConditionExpression=Key('MyHashKey').eq('mykey'),
            FilterExpression=Attr('MyString').eq('mystring'))
        self.assertEqual(response['Count'], 1)

    def test_condition_less_than(self):
        response = self.table.scan(
            FilterExpression=Attr('MyNumber').lt(Decimal('1.26')))
        self.assertEqual(response['Count'], 1)

    def test_condition_less_than_equal(self):
        response = self.table.scan(
            FilterExpression=Attr('MyNumber').lte(Decimal('1.26')))
        self.assertEqual(response['Count'], 1)

    def test_condition_greater_than(self):
        response = self.table.scan(
            FilterExpression=Attr('MyNumber').gt(Decimal('1.24')))
        self.assertEqual(response['Count'], 1)

    def test_condition_greater_than_equal(self):
        response = self.table.scan(
            FilterExpression=Attr('MyNumber').gte(Decimal('1.24')))
        self.assertEqual(response['Count'], 1)

    def test_condition_begins_with(self):
        response = self.table.scan(
            FilterExpression=Attr('MyString').begins_with('my'))
        self.assertEqual(response['Count'], 1)

    def test_condition_between(self):
        response = self.table.scan(
            FilterExpression=Attr('MyNumber').between(
                Decimal('1.24'), Decimal('1.26')))
        self.assertEqual(response['Count'], 1)

    def test_condition_not_equal(self):
        response = self.table.scan(
            FilterExpression=Attr('MyHashKey').ne('notmykey'))
        self.assertEqual(response['Count'], 1)

    def test_condition_in(self):
        response = self.table.scan(
            FilterExpression=Attr('MyHashKey').is_in(['notmykey', 'mykey']))
        self.assertEqual(response['Count'], 1)

    def test_condition_exists(self):
        response = self.table.scan(
            FilterExpression=Attr('MyString').exists())
        self.assertEqual(response['Count'], 1)

    def test_condition_not_exists(self):
        response = self.table.scan(
            FilterExpression=Attr('MyFakeKey').not_exists())
        self.assertEqual(response['Count'], 1)

    def test_condition_contains(self):
        response = self.table.scan(
            FilterExpression=Attr('MyString').contains('my'))
        self.assertEqual(response['Count'], 1)

    def test_condition_size(self):
        response = self.table.scan(
            FilterExpression=Attr('MyString').size().eq(len('mystring')))
        self.assertEqual(response['Count'], 1)

    def test_condition_attribute_type(self):
        response = self.table.scan(
            FilterExpression=Attr('MyMap').attribute_type('M'))
        self.assertEqual(response['Count'], 1)

    def test_condition_and(self):
        response = self.table.scan(
            FilterExpression=(Attr('MyHashKey').eq('mykey') &
                              Attr('MyString').eq('mystring')))
        self.assertEqual(response['Count'], 1)

    def test_condition_or(self):
        response = self.table.scan(
            FilterExpression=(Attr('MyHashKey').eq('mykey2') |
                              Attr('MyString').eq('mystring')))
        self.assertEqual(response['Count'], 1)

    def test_condition_not(self):
        response = self.table.scan(
            FilterExpression=(~Attr('MyHashKey').eq('mykey2')))
        self.assertEqual(response['Count'], 1)

    def test_condition_in_map(self):
        response = self.table.scan(
            FilterExpression=Attr('MyMap.foo').eq('bar'))
        self.assertEqual(response['Count'], 1)

    def test_condition_in_list(self):
        response = self.table.scan(
            FilterExpression=Attr('MyList[0]').eq('foo'))
        self.assertEqual(response['Count'], 1)
