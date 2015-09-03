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

from boto3.docs.subresource import SubResourceDocumenter


class TestSubResourceDocumenter(BaseDocsTest):
    def test_document_sub_resources(self):
        sub_resource_documentor = SubResourceDocumenter(self.resource)
        sub_resource_documentor.document_sub_resources(self.doc_structure)
        self.assert_contains_lines_in_order([
            '.. py:method:: Sample(name)',
            '  Creates a Sample resource.::',
            "    sample = myservice.Sample('name')",
            '  :type name: string',
            "  :param name: The Sample's name identifier.",
            '  :rtype: :py:class:`MyService.Sample`',
            '  :returns: A Sample resource',
        ])
