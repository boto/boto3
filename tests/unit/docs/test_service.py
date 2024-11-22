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
import os

import boto3
from boto3.docs.service import ServiceDocumenter
from tests import mock
from tests.unit.docs import BaseDocsTest


class TestServiceDocumenter(BaseDocsTest):
    def test_document_service(self):
        service_documenter = ServiceDocumenter(
            'myservice', self.session, self.root_services_path
        )
        contents = service_documenter.document_service().decode('utf-8')
        lines = [
            '*********',
            'MyService',
            '*********',
            '======',
            'Client',
            '======',
            '.. py:class:: MyService.Client',
            'These are the available methods:',
            '  myservice/client/sample_operation',
            '==========',
            'Paginators',
            '==========',
            'The available paginators are:',
            '  myservice/paginator/SampleOperation',
            '=======',
            'Waiters',
            '=======',
            'The available waiters are:',
            '  myservice/waiter/SampleOperationComplete',
            '=========',
            'Resources',
            '=========',
            'Resources are available in boto3 via the ',
            '``resource`` method. For more detailed instructions ',
            'and examples on the usage of resources, see the ',
            'resources ',
            'The available resources are:',
            '  myservice/service-resource/index',
            '  myservice/sample/index',
        ]
        self.assert_contains_lines_in_order(lines, contents)
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
                '  sample_operation',
                'Sub-resources',
                "These are the resource's available sub-resources:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  Sample',
                'Collections',
                "These are the resource's available collections:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  samples',
            ],
            self.get_nested_service_contents(
                'myservice', 'service-resource', 'index'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                '======',
                'Sample',
                '======',
                '.. py:class:: MyService.Sample(name)',
                "These are the resource's available identifiers:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  name',
                "These are the resource's available attributes:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  bar',
                '  foo',
                "These are the resource's available actions:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  load',
                '  operate',
                '  reload',
                "These are the resource's available waiters:",
                '.. toctree::',
                '  :maxdepth: 1',
                '  :titlesonly:',
                '  wait_until_complete',
            ],
            self.get_nested_service_contents('myservice', 'sample', 'index'),
        )
        self.assert_contains_lines_in_order(
            [
                'sample_operation',
                '.. py:method:: MyService.Client.sample_operation(**kwargs)',
                '  **Examples**',
                '  Sample Description.',
                '  ::',
                '    response = client.sample_operation(',
            ],
            self.get_nested_service_contents(
                'myservice', 'client', 'sample_operation'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'SampleOperation',
                '.. py:class:: MyService.Paginator.SampleOperation',
                '  .. py:method:: paginate(**kwargs)',
            ],
            self.get_nested_service_contents(
                'myservice', 'paginator', 'SampleOperation'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'SampleOperationComplete',
                '.. py:class:: MyService.Waiter.SampleOperationComplete',
                '  .. py:method:: wait(**kwargs)',
            ],
            self.get_nested_service_contents(
                'myservice', 'waiter', 'SampleOperationComplete'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'sample_operation',
                '.. py:method:: MyService.ServiceResource.sample_operation(**kwargs)',
            ],
            self.get_nested_service_contents(
                'myservice', 'service-resource', 'sample_operation'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'Sample',
                '.. py:method:: MyService.ServiceResource.Sample(name)',
            ],
            self.get_nested_service_contents(
                'myservice', 'service-resource', 'Sample'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'samples',
                '.. py:attribute:: MyService.ServiceResource.samples',
                '  .. py:method:: all()',
                '  .. py:method:: filter(**kwargs)',
                '  .. py:method:: limit(**kwargs)',
                '  .. py:method:: page_size(**kwargs)',
            ],
            self.get_nested_service_contents(
                'myservice', 'service-resource', 'samples'
            ),
        )
        self.assert_contains_lines_in_order(
            [
                'name',
                '.. py:attribute:: MyService.Sample.name',
            ],
            self.get_nested_service_contents('myservice', 'sample', 'name'),
        )
        self.assert_contains_lines_in_order(
            [
                'name',
                '.. py:attribute:: MyService.Sample.name',
            ],
            self.get_nested_service_contents('myservice', 'sample', 'name'),
        )
        self.assert_contains_lines_in_order(
            [
                'bar',
                '.. py:attribute:: MyService.Sample.bar',
            ],
            self.get_nested_service_contents('myservice', 'sample', 'bar'),
        )
        self.assert_contains_lines_in_order(
            [
                'load',
                '.. py:method:: MyService.Sample.load()',
            ],
            self.get_nested_service_contents('myservice', 'sample', 'load'),
        )
        self.assert_contains_lines_in_order(
            [
                'wait_until_complete',
                '.. py:method:: MyService.Sample.wait_until_complete(**kwargs)',
            ],
            self.get_nested_service_contents(
                'myservice', 'sample', 'wait_until_complete'
            ),
        )

    def test_document_service_no_resource(self):
        os.remove(self.resource_model_file)
        service_documenter = ServiceDocumenter(
            'myservice', self.session, self.root_services_path
        )
        contents = service_documenter.document_service().decode('utf-8')
        assert 'Service Resource' not in contents

    def test_document_service_no_paginators(self):
        # Delete the resource model so that the resource is not documented
        # as it may try to look at the paginator model during documentation.
        os.remove(self.resource_model_file)
        os.remove(self.paginator_model_file)
        service_documenter = ServiceDocumenter(
            'myservice', self.session, self.root_services_path
        )
        contents = service_documenter.document_service().decode('utf-8')
        assert 'Paginators' not in contents

    def test_document_service_no_waiter(self):
        # Delete the resource model so that the resource is not documented
        # as it may try to look at the waiter model during documentation.
        os.remove(self.resource_model_file)
        os.remove(self.waiter_model_file)
        service_documenter = ServiceDocumenter(
            'myservice', self.session, self.root_services_path
        )
        contents = service_documenter.document_service().decode('utf-8')
        assert 'Waiters' not in contents

    def test_creates_correct_path_to_examples_based_on_service_name(self):
        path = os.sep.join(
            [os.path.dirname(boto3.__file__), 'examples', 'myservice.rst']
        )
        path = os.path.realpath(path)
        with mock.patch('os.path.isfile') as isfile:
            isfile.return_value = False
            s = ServiceDocumenter(
                'myservice', self.session, self.root_services_path
            )
            s.document_service()
            assert isfile.call_args_list[-1] == mock.call(path)

    def test_injects_examples_when_found(self):
        examples_path = os.sep.join(
            [os.path.dirname(__file__), '..', 'data', 'examples']
        )
        service_documenter = ServiceDocumenter(
            'myservice', self.session, self.root_services_path
        )
        service_documenter.EXAMPLE_PATH = examples_path
        contents = service_documenter.document_service().decode('utf-8')
        assert 'This is an example' in contents
        assert 'This is for another service' not in contents

    def test_service_with_context_params(self):
        self.json_model['clientContextParams'] = {
            'MyContextParam': {
                'documentation': 'This is my context param',
                'type': 'boolean',
            }
        }
        self.setup_client_and_resource()
        service_documenter = ServiceDocumenter(
            'myservice', self.session, self.root_services_path
        )
        contents = service_documenter.document_service().decode('utf-8')
        lines = [
            "=========================",
            "Client Context Parameters",
            "=========================",
            "* ``my_context_param`` (boolean) - This is my context param",
        ]
        self.assert_contains_lines_in_order(lines, contents)
