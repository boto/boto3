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

from boto3.docs.resource import ResourceDocumenter
from boto3.docs.resource import ServiceResourceDocumenter


class TestResourceDocumenter(BaseDocsTest):
    def test_document_resource(self):
        resource = self.resource.Sample('mysample')
        resource_documenter = ResourceDocumenter(
            resource, self.botocore_session)
        resource_documenter.document_resource(self.doc_structure)
        self.assert_contains_lines_in_order([
            '======',
            'Sample',
            '======',
            '.. py:class:: MyService.Sample(name)',
            '  A resource representing an AWS MyService Sample::',
            '    import boto3',
            "    myservice = boto3.resource('myservice')",
            "    sample = myservice.Sample('name')",
            "  These are the resource's available identifiers:",
            '  *   :py:attr:`name`',
            "  These are the resource's available attributes:",
            '  *   :py:attr:`bar`',
            '  *   :py:attr:`foo`',
            "  These are the resource's available actions:",
            '  *   :py:meth:`load()`',
            '  *   :py:meth:`operate()`',
            '  *   :py:meth:`reload()`',
            "  These are the resource's available waiters:",
            '  *   :py:meth:`wait_until_complete()`',
            '  .. rst-class:: admonition-title',
            '  Identifiers',
            '  .. py:attribute:: name',
            '  .. rst-class:: admonition-title',
            '  Attributes',
            '  .. py:attribute:: bar',
            '    - *(string) --* Documents Bar',
            '  .. py:attribute:: foo',
            '    - *(string) --* Documents Foo',
            '  .. rst-class:: admonition-title',
            '  Actions',
            '  .. py:method:: load()',
            '  .. py:method:: operate(**kwargs)',
            '  .. py:method:: reload()',
            '  .. rst-class:: admonition-title',
            '  Waiters',
            '  .. py:method:: wait_until_complete(**kwargs)',
        ])


class TestServiceResourceDocumenter(BaseDocsTest):
    def test_document_resource(self):
        resource_documenter = ServiceResourceDocumenter(
            self.resource, self.botocore_session)
        resource_documenter.document_resource(self.doc_structure)
        self.assert_contains_lines_in_order([
            '================',
            'Service Resource',
            '================',
            '.. py:class:: MyService.ServiceResource()',
            '  A resource representing AWS MyService::',
            '    import boto3',
            "    myservice = boto3.resource('myservice')",
            "  These are the resource's available actions:",
            '  *   :py:meth:`sample_operation()`',
            "  These are the resource's available sub-resources:",
            '  *   :py:meth:`Sample()`',
            "  These are the resource's available collections:",
            '  *   :py:attr:`samples`',
            '  .. rst-class:: admonition-title',
            '  Actions',
            '  .. py:method:: sample_operation(**kwargs)',
            '  .. rst-class:: admonition-title',
            '  Sub-resources',
            '  .. py:method:: Sample(name)',
            '  .. rst-class:: admonition-title',
            '  Collections',
            '  .. py:attribute:: samples',
            '    .. py:method:: all()',
            '    .. py:method:: filter(**kwargs)',
            '    .. py:method:: limit(**kwargs)',
            '    .. py:method:: page_size(**kwargs)',
        ])
