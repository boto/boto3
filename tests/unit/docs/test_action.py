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
from boto3.docs.action import ActionDocumenter
from tests.unit.docs import BaseDocsTest


class TestActionDocumenter(BaseDocsTest):
    def test_document_service_resource_actions(self):
        action_documenter = ActionDocumenter(
            self.resource, self.root_services_path
        )
        action_documenter.document_actions(self.doc_structure)
        self.assert_contains_lines_in_order(
            [
                '-------\nActions\n-------',
                'Actions call operations on resources.  They may',
                'automatically handle the passing in of arguments set',
                'from identifiers and some attributes.',
                'For more information about actions refer to the ',
            ]
        )
        self.assert_contains_lines_in_order(
            [
                'sample_operation',
                '.. py:method:: MyService.ServiceResource.sample_operation(**kwargs)',
                '  **Request Syntax**',
                '  ::',
                '    response = myservice.sample_operation(',
                '        Foo=\'string\',',
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
                '          \'Foo\': \'string\',',
                '          \'Bar\': \'string\'',
                '      }',
                '    **Response Structure**',
                '    - *(dict) --*',
                '      - **Foo** *(string) --* Documents Foo',
                '      - **Bar** *(string) --* Documents Bar',
            ],
            self.get_nested_service_contents(
                'myservice', 'service-resource', 'sample_operation'
            ),
        )

    def test_document_nonservice_resource_actions(self):
        subresource = self.resource.Sample('mysample')
        action_documenter = ActionDocumenter(
            subresource, self.root_services_path
        )
        action_documenter.document_actions(self.doc_structure)
        self.assert_contains_lines_in_order(
            [
                '-------\nActions\n-------',
                'Actions call operations on resources.  They may',
                'automatically handle the passing in of arguments set',
                'from identifiers and some attributes.',
                'For more information about actions refer to the ',
            ]
        )
        self.assert_contains_lines_in_order(
            [
                'load',
                '.. py:method:: MyService.Sample.load()',
                (
                    '  Calls :py:meth:`MyService.Client.sample_operation` to update '
                    'the attributes of the Sample resource'
                ),
                '  **Request Syntax**',
                '  ::',
                '    sample.load()',
                '  :returns: None',
            ],
            self.get_nested_service_contents('myservice', 'sample', 'load'),
        )
        self.assert_contains_lines_in_order(
            [
                'operate',
                '.. py:method:: MyService.Sample.operate(**kwargs)',
                '  **Request Syntax**',
                '  ::',
                '    response = sample.operate(',
                "        Bar='string'",
                '    )',
                '  :type Bar: string',
                '  :param Bar: Documents Bar',
                '  :rtype: dict',
                '  :returns: ',
                '    ',
                '    **Response Syntax**',
                '    ::',
                '      {',
                "          'Foo': 'string',",
                "          'Bar': 'string'",
                '      }',
                '    **Response Structure**',
                '    - *(dict) --* ',
                '      - **Foo** *(string) --* Documents Foo',
                '      - **Bar** *(string) --* Documents Bar',
            ],
            self.get_nested_service_contents('myservice', 'sample', 'operate'),
        )
        self.assert_contains_lines_in_order(
            [
                'reload',
                '.. py:method:: MyService.Sample.reload()',
                (
                    '  Calls :py:meth:`MyService.Client.sample_operation` to update '
                    'the attributes of the Sample resource'
                ),
                '  **Request Syntax**',
                '  ::',
                '    sample.reload()',
                '  :returns: None',
            ],
            self.get_nested_service_contents('myservice', 'sample', 'reload'),
        )
        self.assert_contains_lines_in_order(
            [
                'get_available_subresources',
                '.. py:method:: MyService.Sample.get_available_subresources()',
                'Returns a list of all the available sub-resources for this',
                ':returns: A list containing the name of each sub-resource for this',
                ':rtype: list of str',
            ],
            self.get_nested_service_contents(
                'myservice', 'sample', 'get_available_subresources'
            ),
        )
