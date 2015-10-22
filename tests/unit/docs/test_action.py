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
from tests.unit.docs import BaseDocsTest

from boto3.docs.action import ActionDocumenter


class TestActionDocumenter(BaseDocsTest):
    def test_document_service_resource_actions(self):
        action_documenter = ActionDocumenter(self.resource)
        action_documenter.document_actions(self.doc_structure)
        self.assert_contains_lines_in_order([
            '.. py:method:: sample_operation(**kwargs)',
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
            '      - **Bar** *(string) --* Documents Bar'
        ])

    def test_document_nonservice_resource_actions(self):
        subresource = self.resource.Sample('mysample')
        action_documenter = ActionDocumenter(subresource)
        action_documenter.document_actions(self.doc_structure)
        self.assert_contains_lines_in_order([
            '.. py:method:: load()',
            ('  Calls :py:meth:`MyService.Client.sample_operation` to update '
             'the attributes of the Sample resource'),
            '  **Request Syntax** ',
            '  ::',
            '    sample.load()',
            '  :returns: None',
            '.. py:method:: operate(**kwargs)',
            '  **Request Syntax** ',
            '  ::',
            '    response = sample.operate(',
            "        Bar='string'",
            '    )',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :rtype: dict',
            '  :returns: ',
            '    ',
            '    **Response Syntax** ',
            '    ::',
            '      {',
            "          'Foo': 'string',",
            "          'Bar': 'string'",
            '      }',
            '    **Response Structure** ',
            '    - *(dict) --* ',
            '      - **Foo** *(string) --* Documents Foo',
            '      - **Bar** *(string) --* Documents Bar',
            '.. py:method:: reload()',
            ('  Calls :py:meth:`MyService.Client.sample_operation` to update '
             'the attributes of the Sample resource'),
            '  **Request Syntax** ',
            '  ::',
            '    sample.reload()',
            '  :returns: None'
        ])
