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
from boto3.docs.service import ServiceDocumenter
from boto3.session import Session
from tests.functional.docs import BaseDocsFunctionalTests


class TestDynamoDBCustomizations(BaseDocsFunctionalTests):
    def setUp(self):
        super().setUp()
        self.documenter = ServiceDocumenter(
            'dynamodb',
            session=Session(region_name='us-east-1'),
            root_docs_path=self.root_services_path,
        )
        self.generated_contents = self.documenter.document_service()
        self.generated_contents = self.generated_contents.decode('utf-8')

    def test_batch_writer_is_documented(self):
        self.assert_contains_lines_in_order(
            [
                '=========',
                'Resources',
                '=========',
                'The available resources are:',
                '  dynamodb/table/index',
            ],
            self.generated_contents,
        )
        self.assert_contains_lines_in_order(
            [
                '.. py:class:: DynamoDB.Table(name)',
                '  batch_writer',
            ],
            self.get_nested_file_contents('dynamodb', 'table', 'index'),
        )
        self.assert_contains_lines_in_order(
            [
                '************\nbatch_writer\n************',
                '.. py:method:: DynamoDB.Table.batch_writer(overwrite_by_pkeys=None)',
            ],
            self.get_nested_file_contents('dynamodb', 'table', 'batch_writer'),
        )

    def test_document_interface_is_documented(self):
        put_item_content = self.get_nested_file_contents(
            'dynamodb', 'table', 'put_item'
        )
        self.assert_contains_lines_in_order(
            [
                '********',
                'put_item',
                '********',
                '.. py:method:: DynamoDB.Table.put_item(**kwargs)',
                # Make sure the request syntax is as expected.
                'response = table.put_item(',
                'Item={',
                (
                    '\'string\': \'string\'|123|Binary(b\'bytes\')'
                    '|True|None|set([\'string\'])|set([123])|'
                    'set([Binary(b\'bytes\')])|[]|{}'
                ),
                '},',
                'Expected={',
                '\'string\': {',
                (
                    '\'Value\': \'string\'|123'
                    '|Binary(b\'bytes\')|True|None|set([\'string\'])'
                    '|set([123])|set([Binary(b\'bytes\')])|[]|{},'
                ),
                '\'AttributeValueList\': [',
                (
                    '\'string\'|123|Binary(b\'bytes\')'
                    '|True|None|set([\'string\'])|set([123])|'
                    'set([Binary(b\'bytes\')])|[]|{},'
                ),
                # Make sure the request parameter is documented correctly.
                ':type Item: dict',
                ':param Item: **[REQUIRED]**',
                '- *(string) --*',
                (
                    '- *(valid DynamoDB type) -- *- The value of the '
                    'attribute. The valid value types are listed in the '
                    ':ref:`DynamoDB Reference Guide<ref_valid_dynamodb_types>`.'
                ),
                # Make sure the response syntax is as expected.
                '{',
                '\'Attributes\': {',
                (
                    '\'string\': \'string\'|123|'
                    'Binary(b\'bytes\')|True|None|set([\'string\'])|'
                    'set([123])|set([Binary(b\'bytes\')])|[]|{}'
                ),
                '},',
                # Make sure the response parameter is documented correctly.
                '- **Attributes** *(dict) --*',
                '- *(string) --*',
                (
                    '- *(valid DynamoDB type) -- *- The value of '
                    'the attribute. The valid value types are listed in the '
                    ':ref:`DynamoDB Reference Guide<ref_valid_dynamodb_types>`.'
                ),
            ],
            put_item_content,
        )

    def test_conditions_is_documented(self):
        query_contents = self.get_nested_file_contents(
            'dynamodb', 'table', 'query'
        )
        self.assert_contains_lines_in_order(
            [
                # Make sure the request syntax is as expected.
                'response = table.query(',
                ('FilterExpression=Attr(\'myattribute\').' 'eq(\'myvalue\'),'),
                ('KeyConditionExpression=Key(\'mykey\')' '.eq(\'myvalue\'),'),
                # Make sure the request parameter is documented correctly.
                (
                    ':type FilterExpression: condition from '
                    ':py:class:`boto3.dynamodb.conditions.Attr` method'
                ),
                (
                    ':param FilterExpression: The condition(s) an '
                    'attribute(s) must meet. Valid conditions are listed in '
                    'the :ref:`DynamoDB Reference Guide<ref_dynamodb_conditions>`.'
                ),
                (
                    ':type KeyConditionExpression: condition from '
                    ':py:class:`boto3.dynamodb.conditions.Key` method'
                ),
                (
                    ':param KeyConditionExpression: The condition(s) a '
                    'key(s) must meet. Valid conditions are listed in the '
                    ':ref:`DynamoDB Reference Guide<ref_dynamodb_conditions>`.'
                ),
            ],
            query_contents,
        )
