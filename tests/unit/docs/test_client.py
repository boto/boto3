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
from botocore.docs.client import ClientExceptionsDocumenter

from boto3.docs.client import Boto3ClientDocumenter
from tests.unit.docs import BaseDocsTest


class TestBoto3ClientDocumenter(BaseDocsTest):
    def setUp(self):
        super().setUp()
        exception_shape = {
            'SomeException': {
                'exception': True,
                'type': 'structure',
                'members': {'Message': {'shape': 'String'}},
            }
        }
        self.add_shape(exception_shape)
        self.add_shape_to_errors('SomeException')
        self.setup_client_and_resource()
        self.client_documenter = Boto3ClientDocumenter(
            self.client, self.root_services_path
        )

    def test_document_client(self):
        self.client_documenter.document_client(self.doc_structure)
        self.assert_contains_lines_in_order(
            [
                '======',
                'Client',
                '======',
                '.. py:class:: MyService.Client',
                '  A low-level client representing AWS MyService',
                '  ::',
                '    import boto3',
                '    client = boto3.client(\'myservice\')',
                'These are the available methods:',
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  myservice/client/can_paginate',
                '  myservice/client/get_paginator',
                '  myservice/client/get_waiter',
                '  myservice/client/sample_operation',
            ]
        )
        self.assert_contains_lines_in_order(
            [
                'can_paginate',
                '.. py:method:: MyService.Client.can_paginate(operation_name)',
            ],
            self.get_nested_service_contents(
                'myservice', 'client', 'can_paginate'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'get_paginator',
                '.. py:method:: MyService.Client.get_paginator(operation_name)',
            ],
            self.get_nested_service_contents(
                'myservice', 'client', 'get_paginator'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'get_waiter',
                '.. py:method:: MyService.Client.get_waiter(waiter_name)',
            ],
            self.get_nested_service_contents(
                'myservice', 'client', 'get_waiter'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'sample_operation',
                '.. py:method:: MyService.Client.sample_operation(**kwargs)',
                '  **Request Syntax**',
                '  ::',
                '    response = client.sample_operation(',
                '        Foo=\'string\'',
                '        Bar=\'string\'',
                '    )',
                '  :type Foo: string',
                '  :param Foo: Documents Foo',
                '  :type Bar: string',
                '  :param Bar: Documents Bar',
                '  :rtype: dict',
                '  :returns:',
                '    **Response Syntax**',
                '    ::',
                '      {',
                '          \'Foo\': \'string\'',
                '          \'Bar\': \'string\'',
                '      }',
                '    **Response Structure**',
                '    - *(dict) --*',
                '      - **Foo** *(string) --*',
                '      - **Bar** *(string) --*',
                '**Exceptions**',
                '*   :py:class:`MyService.Client.exceptions.SomeException`',
            ],
            self.get_nested_service_contents(
                'myservice', 'client', 'sample_operation'
            ),
        )


class TestClientExceptionsDocumenter(BaseDocsTest):
    def setup_documenter(self):
        self.setup_client_and_resource()
        self.exceptions_documenter = ClientExceptionsDocumenter(
            self.client, self.root_services_path
        )

    def test_no_modeled_exceptions(self):
        self.setup_documenter()
        self.exceptions_documenter.document_exceptions(self.doc_structure)
        self.assert_contains_lines_in_order(
            [
                '=================',
                'Client Exceptions',
                '=================',
                'Client exceptions are available',
                'This client has no modeled exception classes.',
            ]
        )

    def test_modeled_exceptions(self):
        exception_shape = {
            'SomeException': {
                'exception': True,
                'type': 'structure',
                'members': {'Message': {'shape': 'String'}},
            }
        }
        self.add_shape(exception_shape)
        self.setup_documenter()
        self.exceptions_documenter.document_exceptions(self.doc_structure)
        self.assert_contains_lines_in_order(
            [
                '=================',
                'Client Exceptions',
                '=================',
                'Client exceptions are available',
                'The available client exceptions are:',
                '.. toctree::',
                ':maxdepth: 1',
                ':titlesonly:',
                '  myservice/client/exceptions/SomeException',
            ]
        )
        self.assert_contains_lines_in_order(
            [
                '.. py:class:: MyService.Client.exceptions.SomeException',
                '**Example**',
                '::',
                'except client.exceptions.SomeException as e:',
                '.. py:attribute:: response',
                '**Syntax**',
                '{',
                "'Message': 'string',",
                "'Error': {",
                "'Code': 'string',",
                "'Message': 'string'",
                '}',
                '}',
                '**Structure**',
                '- *(dict) --*',
                '- **Message** *(string) --* ',
                '- **Error** *(dict) --* ',
                '- **Code** *(string) --* ',
                '- **Message** *(string) --* ',
            ],
            self.get_nested_service_contents(
                'myservice', 'client/exceptions', 'SomeException'
            ),
        )
