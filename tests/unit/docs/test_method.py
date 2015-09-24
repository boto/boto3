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
from botocore.hooks import HierarchicalEmitter
from botocore.docs.utils import DocumentedShape

from tests.unit.docs import BaseDocsTest
from boto3.resources.model import ResponseResource
from boto3.docs.method import document_model_driven_resource_method


class TestDocumentModelDrivenResourceMethod(BaseDocsTest):
    def setUp(self):
        super(TestDocumentModelDrivenResourceMethod, self).setUp()
        self.event_emitter = HierarchicalEmitter()
        self.service_model = self.client.meta.service_model
        self.operation_model = self.service_model.operation_model(
            'SampleOperation')
        self.service_resource_model = self.resource.meta.resource_model

    def test_default(self):
        document_model_driven_resource_method(
            self.doc_structure, 'foo', self.operation_model,
            event_emitter=self.event_emitter,
            method_description='This describes the foo method.',
            example_prefix='response = myservice.foo',
            resource_action_model=self.service_resource_model.actions[0]
        )
        self.assert_contains_lines_in_order([
            '.. py:method:: foo(**kwargs)',
            '  This describes the foo method.',
            '  **Request Syntax** ',
            '  ::',
            '    response = myservice.foo(',
            "        Foo='string',",
            "        Bar='string'",
            '    )',
            '  :type Foo: string',
            '  :param Foo: Documents Foo',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :rtype: dict',
            '  :returns: ',
            '    **Response Syntax** ',
            '    ::',
            '      {',
            "          'Foo': 'string',",
            "          'Bar': 'string'",
            '      }',
            '    **Response Structure** ',
            '    - *(dict) --* ',
            '      - **Foo** *(string) --* Documents Foo',
            '      - **Bar** *(string) --* Documents Bar'
        ])

    def test_returns_resource(self):
        resource_action = self.service_resource_model.actions[0]
        # Override the return type of the action to be a resource
        # instead of the regular dictionary.
        resource_action.resource = ResponseResource(
            {'type': 'Sample',
             'identifiers': [{
                 'target': 'Name', 'source': 'requestParameter',
                 'path': 'Foo'}]},
            self.resource_json_model)
        document_model_driven_resource_method(
            self.doc_structure, 'foo', self.operation_model,
            event_emitter=self.event_emitter,
            method_description='This describes the foo method.',
            example_prefix='sample = myservice.foo',
            resource_action_model=resource_action
        )
        self.assert_contains_lines_in_order([
            '.. py:method:: foo(**kwargs)',
            '  This describes the foo method.',
            '  **Request Syntax** ',
            '  ::',
            '    sample = myservice.foo(',
            "        Foo='string',",
            "        Bar='string'",
            '    )',
            '  :type Foo: string',
            '  :param Foo: Documents Foo',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :rtype: :py:class:`myservice.Sample`',
            '  :returns: Sample resource'
        ])

    def test_returns_list_of_resource(self):
        resource_action = self.service_resource_model.actions[1]
        document_model_driven_resource_method(
            self.doc_structure, 'foo', self.operation_model,
            event_emitter=self.event_emitter,
            method_description='This describes the foo method.',
            example_prefix='samples = myservice.foo',
            resource_action_model=resource_action
        )
        self.assert_contains_lines_in_order([
            '.. py:method:: foo(**kwargs)',
            '  This describes the foo method.',
            '  **Request Syntax** ',
            '  ::',
            '    samples = myservice.foo(',
            "        Foo='string',",
            "        Bar='string'",
            '    )',
            '  :type Foo: string',
            '  :param Foo: Documents Foo',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :rtype: list(:py:class:`myservice.Sample`)',
            '  :returns: A list of Sample resource'
        ])

    def test_include_input(self):
        include_params = [
            DocumentedShape(
                name='Biz', type_name='string', documentation='biz docs')
        ]
        document_model_driven_resource_method(
            self.doc_structure, 'foo', self.operation_model,
            event_emitter=self.event_emitter,
            method_description='This describes the foo method.',
            example_prefix='response = myservice.foo',
            include_input=include_params,
            resource_action_model=self.service_resource_model.actions[0]
        )
        self.assert_contains_lines_in_order([
            '.. py:method:: foo(**kwargs)',
            '  This describes the foo method.',
            '  **Request Syntax** ',
            '  ::',
            '    response = myservice.foo(',
            "        Foo='string',",
            "        Bar='string',",
            "        Biz='string'",
            '    )',
            '  :type Foo: string',
            '  :param Foo: Documents Foo',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :type Biz: string',
            '  :param Biz: biz docs',
            '  :rtype: dict',
            '  :returns: ',
            '    **Response Syntax** ',
            '    ::',
            '      {',
            "          'Foo': 'string',",
            "          'Bar': 'string'",
            '      }',
            '    **Response Structure** ',
            '    - *(dict) --* ',
            '      - **Foo** *(string) --* Documents Foo',
            '      - **Bar** *(string) --* Documents Bar'
        ])

    def test_include_output(self):
        include_params = [
            DocumentedShape(
                name='Biz', type_name='string', documentation='biz docs')
        ]
        document_model_driven_resource_method(
            self.doc_structure, 'foo', self.operation_model,
            event_emitter=self.event_emitter,
            method_description='This describes the foo method.',
            example_prefix='response = myservice.foo',
            include_output=include_params,
            resource_action_model=self.service_resource_model.actions[0]
        )
        self.assert_contains_lines_in_order([
            '.. py:method:: foo(**kwargs)',
            '  This describes the foo method.',
            '  **Request Syntax** ',
            '  ::',
            '    response = myservice.foo(',
            "        Foo='string',",
            "        Bar='string'",
            '    )',
            '  :type Foo: string',
            '  :param Foo: Documents Foo',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :rtype: dict',
            '  :returns: ',
            '    **Response Syntax** ',
            '    ::',
            '      {',
            "          'Foo': 'string',",
            "          'Bar': 'string',",
            "          'Biz': 'string'",
            '      }',
            '    **Response Structure** ',
            '    - *(dict) --* ',
            '      - **Foo** *(string) --* Documents Foo',
            '      - **Bar** *(string) --* Documents Bar',
            '      - **Biz** *(string) --* biz docs'
        ])

    def test_exclude_input(self):
        document_model_driven_resource_method(
            self.doc_structure, 'foo', self.operation_model,
            event_emitter=self.event_emitter,
            method_description='This describes the foo method.',
            example_prefix='response = myservice.foo',
            exclude_input=['Bar'],
            resource_action_model=self.service_resource_model.actions[0]
        )
        self.assert_contains_lines_in_order([
            '.. py:method:: foo(**kwargs)',
            '  This describes the foo method.',
            '  **Request Syntax** ',
            '  ::',
            '    response = myservice.foo(',
            "        Foo='string',",
            '    )',
            '  :type Foo: string',
            '  :param Foo: Documents Foo',
            '  :rtype: dict',
            '  :returns: ',
            '    **Response Syntax** ',
            '    ::',
            '      {',
            "          'Foo': 'string',",
            "          'Bar': 'string'",
            '      }',
            '    **Response Structure** ',
            '    - *(dict) --* ',
            '      - **Foo** *(string) --* Documents Foo',
            '      - **Bar** *(string) --* Documents Bar'
        ])
        self.assert_not_contains_lines([
            ':param Bar: string',
            'Bar=\'string\''
        ])

    def test_exclude_output(self):
        document_model_driven_resource_method(
            self.doc_structure, 'foo', self.operation_model,
            event_emitter=self.event_emitter,
            method_description='This describes the foo method.',
            example_prefix='response = myservice.foo',
            exclude_output=['Bar'],
            resource_action_model=self.service_resource_model.actions[0]
        )
        self.assert_contains_lines_in_order([
            '.. py:method:: foo(**kwargs)',
            '  This describes the foo method.',
            '  **Request Syntax** ',
            '  ::',
            '    response = myservice.foo(',
            "        Foo='string',",
            "        Bar='string'",
            '    )',
            '  :type Foo: string',
            '  :param Foo: Documents Foo',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :rtype: dict',
            '  :returns: ',
            '    **Response Syntax** ',
            '    ::',
            '      {',
            "          'Foo': 'string'",
            '      }',
            '    **Response Structure** ',
            '    - *(dict) --* ',
            '      - **Foo** *(string) --* Documents Foo',
        ])
        self.assert_not_contains_lines([
            '\'Bar\': \'string\'',
            '- **Bar** *(string) --*',
        ])
