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
from decimal import Decimal

import boto3.session
from boto3.compat import collections_abc
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
        self.table.put_item(Item=self.item_data)
        self.addCleanup(self.table.delete_item, Key={'MyHashKey': 'mykey'})
        response = self.table.get_item(Key={'MyHashKey': 'mykey'},
                                       ConsistentRead=True)
        self.assertEqual(response['Item'], self.item_data)


class TestDynamoDBConditions(BaseDynamoDBTest):
    @classmethod
    def setUpClass(cls):
        super(TestDynamoDBConditions, cls).setUpClass()
        cls.table.put_item(Item=cls.item_data)

    @classmethod
    def tearDownClass(cls):
        cls.table.delete_item(Key={'MyHashKey': 'mykey'})
        super(TestDynamoDBConditions, cls).tearDownClass()

    def scan(self, filter_expression):
        return self.table.scan(FilterExpression=filter_expression,
                               ConsistentRead=True)

    def query(self, key_condition_expression, filter_expression=None):
        kwargs = {
            'KeyConditionExpression': key_condition_expression,
            'ConsistentRead': True
        }
        if filter_expression is not None:
            kwargs['FilterExpression'] = filter_expression
        return self.table.query(**kwargs)

    def test_filter_expression(self):
        r = self.scan(
            filter_expression=Attr('MyHashKey').eq('mykey'))
        self.assertEqual(r['Items'][0]['MyHashKey'], 'mykey')

    def test_key_condition_expression(self):
        r = self.query(
            key_condition_expression=Key('MyHashKey').eq('mykey'))
        self.assertEqual(r['Items'][0]['MyHashKey'], 'mykey')

    def test_key_condition_with_filter_condition_expression(self):
        r = self.query(
            key_condition_expression=Key('MyHashKey').eq('mykey'),
            filter_expression=Attr('MyString').eq('mystring'))
        self.assertEqual(r['Items'][0]['MyString'], 'mystring')

    def test_condition_less_than(self):
        r = self.scan(
            filter_expression=Attr('MyNumber').lt(Decimal('1.26')))
        self.assertTrue(r['Items'][0]['MyNumber'] < Decimal('1.26'))

    def test_condition_less_than_equal(self):
        r = self.scan(
            filter_expression=Attr('MyNumber').lte(Decimal('1.26')))
        self.assertTrue(r['Items'][0]['MyNumber'] <= Decimal('1.26'))

    def test_condition_greater_than(self):
        r = self.scan(
            filter_expression=Attr('MyNumber').gt(Decimal('1.24')))
        self.assertTrue(r['Items'][0]['MyNumber'] > Decimal('1.24'))

    def test_condition_greater_than_equal(self):
        r = self.scan(
            filter_expression=Attr('MyNumber').gte(Decimal('1.24')))
        self.assertTrue(r['Items'][0]['MyNumber'] >= Decimal('1.24'))

    def test_condition_begins_with(self):
        r = self.scan(
            filter_expression=Attr('MyString').begins_with('my'))
        self.assertTrue(r['Items'][0]['MyString'].startswith('my'))

    def test_condition_between(self):
        r = self.scan(
            filter_expression=Attr('MyNumber').between(
                Decimal('1.24'), Decimal('1.26')))
        self.assertTrue(r['Items'][0]['MyNumber'] > Decimal('1.24'))
        self.assertTrue(r['Items'][0]['MyNumber'] < Decimal('1.26'))

    def test_condition_not_equal(self):
        r = self.scan(
            filter_expression=Attr('MyHashKey').ne('notmykey'))
        self.assertNotEqual(r['Items'][0]['MyHashKey'], 'notmykey')

    def test_condition_in(self):
        r = self.scan(
            filter_expression=Attr('MyHashKey').is_in(['notmykey', 'mykey']))
        self.assertIn(r['Items'][0]['MyHashKey'], ['notmykey', 'mykey'])

    def test_condition_exists(self):
        r = self.scan(
            filter_expression=Attr('MyString').exists())
        self.assertIn('MyString', r['Items'][0])

    def test_condition_not_exists(self):
        r = self.scan(
            filter_expression=Attr('MyFakeKey').not_exists())
        self.assertNotIn('MyFakeKey', r['Items'][0])

    def test_condition_contains(self):
        r = self.scan(
            filter_expression=Attr('MyString').contains('my'))
        self.assertIn('my', r['Items'][0]['MyString'])

    def test_condition_size(self):
        r = self.scan(
            filter_expression=Attr('MyString').size().eq(len('mystring')))
        self.assertEqual(len(r['Items'][0]['MyString']), len('mystring'))

    def test_condition_attribute_type(self):
        r = self.scan(
            filter_expression=Attr('MyMap').attribute_type('M'))
        self.assertIsInstance(r['Items'][0]['MyMap'], collections_abc.Mapping)

    def test_condition_and(self):
        r = self.scan(
            filter_expression=(Attr('MyHashKey').eq('mykey') &
                               Attr('MyString').eq('mystring')))
        item = r['Items'][0]
        self.assertTrue(
            item['MyHashKey'] == 'mykey' and item['MyString'] == 'mystring')

    def test_condition_or(self):
        r = self.scan(
            filter_expression=(Attr('MyHashKey').eq('mykey2') |
                               Attr('MyString').eq('mystring')))
        item = r['Items'][0]
        self.assertTrue(
            item['MyHashKey'] == 'mykey2' or item['MyString'] == 'mystring')

    def test_condition_not(self):
        r = self.scan(
            filter_expression=(~Attr('MyHashKey').eq('mykey2')))
        item = r['Items'][0]
        self.assertTrue(item['MyHashKey'] != 'mykey2')

    def test_condition_in_map(self):
        r = self.scan(
            filter_expression=Attr('MyMap.foo').eq('bar'))
        self.assertEqual(r['Items'][0]['MyMap']['foo'], 'bar')

    def test_condition_in_list(self):
        r = self.scan(
            filter_expression=Attr('MyList[0]').eq('foo'))
        self.assertEqual(r['Items'][0]['MyList'][0], 'foo')


class TestDynamodbBatchWrite(BaseDynamoDBTest):
    def test_batch_write_items(self):
        num_elements = 1000
        items = []
        for i in range(num_elements):
            items.append({'MyHashKey': 'foo%s' % i,
                          'OtherKey': 'bar%s' % i})
        with self.table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

        # Verify all the items were added to dynamodb.
        for obj in self.table.scan(ConsistentRead=True)['Items']:
            self.assertIn(obj, items)
