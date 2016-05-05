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
from tests.functional.docs import BaseDocsFunctionalTests

from boto3.session import Session
from boto3.docs.service import ServiceDocumenter


class TestDynamoDBCustomizations(BaseDocsFunctionalTests):
    def setUp(self):
        self.documenter = ServiceDocumenter(
            'dynamodb', session=Session(region_name='us-east-1'))
        self.generated_contents = self.documenter.document_service()
        self.generated_contents = self.generated_contents.decode('utf-8')

    def test_batch_writer_is_documented(self):
        self.assert_contains_lines_in_order([
            '.. py:class:: DynamoDB.Table(name)',
            '  *   :py:meth:`batch_writer()`',
            '  .. py:method:: batch_writer(overwrite_by_pkeys=None)'],
            self.generated_contents
        )

    def test_document_interface_is_documented(self):
        contents = self.get_class_document_block(
            'DynamoDB.Table', self.generated_contents)

        # Take an arbitrary method that uses the customization.
        method_contents = self.get_method_document_block('put_item', contents)

        # Make sure the request syntax is as expected.
        request_syntax_contents = self.get_request_syntax_document_block(
            method_contents)
        self.assert_contains_lines_in_order([
            'response = table.put_item(',
            'Item={',
            ('\'string\': \'string\'|123|Binary(b\'bytes\')'
             '|True|None|set([\'string\'])|set([123])|'
             'set([Binary(b\'bytes\')])|[]|{}'),
            '},',
            'Expected={',
            '\'string\': {',
            ('\'Value\': \'string\'|123'
             '|Binary(b\'bytes\')|True|None|set([\'string\'])'
             '|set([123])|set([Binary(b\'bytes\')])|[]|{},'),
            '\'AttributeValueList\': [',
            ('\'string\'|123|Binary(b\'bytes\')'
             '|True|None|set([\'string\'])|set([123])|'
             'set([Binary(b\'bytes\')])|[]|{},')],
            request_syntax_contents)

        # Make sure the response syntax is as expected.
        response_syntax_contents = self.get_response_syntax_document_block(
            method_contents)
        self.assert_contains_lines_in_order([
            '{',
            '\'Attributes\': {',
            ('\'string\': \'string\'|123|'
             'Binary(b\'bytes\')|True|None|set([\'string\'])|'
             'set([123])|set([Binary(b\'bytes\')])|[]|{}'),
            '},'],
            response_syntax_contents)

        # Make sure the request parameter is documented correctly.
        request_param_contents = self.get_request_parameter_document_block(
            'Item', method_contents)
        self.assert_contains_lines_in_order([
            ':type Item: dict',
            ':param Item: **[REQUIRED]**',
            '- *(string) --*',
            ('- *(valid DynamoDB type) --* - The value of the '
             'attribute. The valid value types are listed in the '
             ':ref:`DynamoDB Reference Guide<ref_valid_dynamodb_types>`.')],
            request_param_contents
        )

        # Make sure the response parameter is documented correctly.
        response_param_contents = self.get_response_parameter_document_block(
            'Attributes', method_contents)
        self.assert_contains_lines_in_order([
            '- **Attributes** *(dict) --*',
            '- *(string) --*',
            ('- *(valid DynamoDB type) --* - The value of '
             'the attribute. The valid value types are listed in the '
             ':ref:`DynamoDB Reference Guide<ref_valid_dynamodb_types>`.')],
            response_param_contents)

    def test_conditions_is_documented(self):
        contents = self.get_class_document_block(
            'DynamoDB.Table', self.generated_contents)

        # Take an arbitrary method that uses the customization.
        method_contents = self.get_method_document_block('query', contents)

        # Make sure the request syntax is as expected.
        request_syntax_contents = self.get_request_syntax_document_block(
            method_contents)
        self.assert_contains_lines_in_order([
            'response = table.query(',
            ('FilterExpression=Attr(\'myattribute\').'
             'eq(\'myvalue\'),'),
            ('KeyConditionExpression=Key(\'mykey\')'
             '.eq(\'myvalue\'),')],
            request_syntax_contents)

        # Make sure the request parameter is documented correctly.
        self.assert_contains_lines_in_order([
            (':type FilterExpression: condition from '
             ':py:class:`boto3.dynamodb.conditions.Attr` method'),
            (':param FilterExpression: The condition(s) an '
             'attribute(s) must meet. Valid conditions are listed in '
             'the :ref:`DynamoDB Reference Guide<ref_dynamodb_conditions>`.'),
            (':type KeyConditionExpression: condition from '
             ':py:class:`boto3.dynamodb.conditions.Key` method'),
            (':param KeyConditionExpression: The condition(s) a '
             'key(s) must meet. Valid conditions are listed in the '
             ':ref:`DynamoDB Reference Guide<ref_dynamodb_conditions>`.')],
            method_contents)
