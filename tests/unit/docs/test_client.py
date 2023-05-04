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
from boto3.docs.client import Boto3ClientDocumenter
from tests.unit.docs import BaseDocsTest


class TestBoto3ClientDocumenter(BaseDocsTest):
    def setUp(self):
        super().setUp()
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
                '  .. raw:: html',
                '    <h3>Request Syntax</h3>',
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
                '    .. raw:: html',
                '      <h3>Response Syntax</h3>',
                '    ::',
                '      {',
                '          \'Foo\': \'string\'',
                '          \'Bar\': \'string\'',
                '      }',
                '    .. raw:: html',
                '      <h3>Response Structure</h3>',
                '    - *(dict) --*',
                '      - **Foo** *(string) --*',
                '      - **Bar** *(string) --*',
            ],
            self.get_nested_service_contents(
                'myservice', 'client', 'sample_operation'
            ),
        )
