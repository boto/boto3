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
from boto3.docs.resource import ResourceDocumenter, ServiceResourceDocumenter
from tests.unit.docs import BaseDocsTest


class TestResourceDocumenter(BaseDocsTest):
    def test_document_resource(self):
        resource = self.resource.Sample('mysample')
        resource_documenter = ResourceDocumenter(
            resource, self.botocore_session, self.root_services_path
        )
        resource_documenter.document_resource(self.doc_structure)
        self.assert_contains_lines_in_order(
            [
                '======',
                'Sample',
                '======',
                '.. py:class:: MyService.Sample(name)',
                '  A resource representing an AWS MyService Sample::',
                '    import boto3',
                "    myservice = boto3.resource('myservice')",
                "    sample = myservice.Sample('name')",
                'Identifiers',
                "These are the resource's available identifiers:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  myservice/Sample/name',
                'Attributes',
                "These are the resource's available attributes:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  myservice/Sample/bar',
                '  myservice/Sample/foo',
                'Actions',
                "These are the resource's available actions:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  myservice/Sample/load',
                '  myservice/Sample/operate',
                '  myservice/Sample/reload',
                'Waiters',
                "These are the resource's available waiters:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  myservice/Sample/wait_until_complete',
            ]
        )
        self.assert_contains_lines_in_order(
            [
                'name',
                '.. py:attribute:: name',
            ],
            self.get_nested_service_contents('myservice', 'Sample', 'name'),
        )
        self.assert_contains_lines_in_order(
            [
                'bar',
                '.. py:attribute:: bar',
                '  - *(string) --* Documents Bar',
            ],
            self.get_nested_service_contents('myservice', 'Sample', 'bar'),
        )
        self.assert_contains_lines_in_order(
            [
                'load',
                '.. py:method:: load()',
            ],
            self.get_nested_service_contents('myservice', 'Sample', 'load'),
        )
        self.assert_contains_lines_in_order(
            [
                'wait_until_complete',
                '.. py:method:: wait_until_complete(**kwargs)',
            ],
            self.get_nested_service_contents(
                'myservice', 'Sample', 'wait_until_complete'
            ),
        )


class TestServiceResourceDocumenter(BaseDocsTest):
    def test_document_resource(self):
        resource_documenter = ServiceResourceDocumenter(
            self.resource, self.botocore_session, self.root_services_path
        )
        resource_documenter.document_resource(self.doc_structure)
        self.assert_contains_lines_in_order(
            [
                '================',
                'Service Resource',
                '================',
                '.. py:class:: MyService.ServiceResource()',
                '  A resource representing AWS MyService::',
                '    import boto3',
                "    myservice = boto3.resource('myservice')",
                'Actions',
                "These are the resource's available actions:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  myservice/ServiceResource/sample_operation',
                'Sub-resources',
                "These are the resource's available sub-resources:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  myservice/ServiceResource/Sample',
                'Collections',
                "These are the resource's available collections:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  myservice/ServiceResource/samples',
            ]
        )
        self.assert_contains_lines_in_order(
            [
                'sample_operation',
                '.. py:method:: sample_operation(**kwargs)',
            ],
            self.get_nested_service_contents(
                'myservice', 'ServiceResource', 'sample_operation'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'Sample',
                '.. py:method:: Sample(name)',
            ],
            self.get_nested_service_contents(
                'myservice', 'ServiceResource', 'Sample'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'samples',
                '.. py:attribute:: samples',
                '  .. py:method:: all()',
                '  .. py:method:: filter(**kwargs)',
                '  .. py:method:: limit(**kwargs)',
                '  .. py:method:: page_size(**kwargs)',
            ],
            self.get_nested_service_contents(
                'myservice', 'ServiceResource', 'samples'
            ),
        )
