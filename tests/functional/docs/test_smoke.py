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
import shutil
import tempfile

import botocore.session
import pytest
from botocore import xform_name
from botocore.exceptions import DataNotFoundError

import boto3
from boto3.docs.service import ServiceDocumenter

DOCS_ROOT_DIR = None
ROOT_SERVICES_PATH = None


@pytest.fixture
def botocore_session():
    return botocore.session.get_session()


@pytest.fixture
def boto3_session():
    return boto3.Session(region_name='us-east-1')


def all_services():
    # Create temporary directory before testing.
    global DOCS_ROOT_DIR, ROOT_SERVICES_PATH
    DOCS_ROOT_DIR = tempfile.mkdtemp()
    ROOT_SERVICES_PATH = os.path.join(
        tempfile.mkdtemp(), 'reference', 'services'
    )
    session = boto3.Session(region_name='us-east-1')
    yield from session.get_available_services()
    # Clean up temporary directory after testing.
    shutil.rmtree(DOCS_ROOT_DIR)


@pytest.fixture
def available_resources():
    session = boto3.Session(region_name='us-east-1')
    return session.get_available_resources()


@pytest.mark.parametrize('service_name', all_services())
def test_documentation(
    boto3_session, botocore_session, available_resources, service_name
):
    generated_docs = ServiceDocumenter(
        service_name, session=boto3_session, root_docs_path=ROOT_SERVICES_PATH
    ).document_service()
    generated_docs = generated_docs.decode('utf-8')
    client = boto3.client(service_name, 'us-east-1')

    # Check that all of the services have the appropriate title
    _assert_has_title(generated_docs, client)

    # Check that all services have the client documented.
    _assert_has_client_documentation(generated_docs, service_name, client)

    # If the service has resources, make sure the service resource
    # is at least documented.
    if service_name in available_resources:

        resource = boto3.resource(service_name, 'us-east-1')
        _assert_has_resource_documentation(
            generated_docs, service_name, resource
        )

    # If the client can paginate, make sure the paginators are documented.
    try:
        paginator_model = botocore_session.get_paginator_model(service_name)
        _assert_has_paginator_documentation(
            generated_docs,
            service_name,
            client,
            sorted(paginator_model._paginator_config),
        )
    except DataNotFoundError:
        pass

    # If the client has waiters, make sure the waiters are documented.
    if client.waiter_names:
        waiter_model = botocore_session.get_waiter_model(service_name)
        _assert_has_waiter_documentation(
            generated_docs, service_name, client, waiter_model
        )


def _assert_contains_lines_in_order(lines, contents):
    for line in lines:
        assert line in contents
        beginning = contents.find(line)
        contents = contents[(beginning + len(line)) :]


def _assert_has_title(generated_docs, client):
    title = client.__class__.__name__
    ref_lines = ['*' * len(title), title, '*' * len(title)]
    _assert_contains_lines_in_order(ref_lines, generated_docs)


def _assert_has_client_documentation(generated_docs, service_name, client):
    class_name = client.__class__.__name__
    ref_lines = [
        '======',
        'Client',
        '======',
        '.. py:class:: %s.Client' % class_name,
        '  A low-level client representing',
        '    import boto3',
        '    client = boto3.client(\'%s\')' % service_name,
        'These are the available methods:',
        '  %s/Client/get_paginator' % service_name,
        '  %s/Client/get_waiter' % service_name,
    ]
    _assert_contains_lines_in_order(ref_lines, generated_docs)
    for method_name in ['get_paginator', 'get_waiter']:
        _assert_contains_lines_in_order(
            [
                f'{method_name}',
                f'.. py:method:: {method_name}(',
            ],
            get_nested_file_contents(service_name, 'Client', method_name),
        )


def _assert_has_paginator_documentation(
    generated_docs, service_name, client, paginator_names
):
    ref_lines = [
        '==========',
        'Paginators',
        '==========',
        'The available paginators are:',
    ]
    for paginator_name in paginator_names:
        ref_lines.append(f'  {service_name}/Paginator/{paginator_name}')

    for paginator_name in paginator_names:
        _assert_contains_lines_in_order(
            [
                '.. py:class:: {}.Paginator.{}'.format(
                    client.__class__.__name__, paginator_name
                ),
                '  .. py:method:: paginate(',
            ],
            get_nested_file_contents(
                service_name, 'Paginator', paginator_name
            ),
        )

    _assert_contains_lines_in_order(ref_lines, generated_docs)


def _assert_has_waiter_documentation(
    generated_docs, service_name, client, waiter_model
):
    ref_lines = ['=======', 'Waiters', '=======', 'The available waiters are:']
    for waiter_name in waiter_model.waiter_names:
        ref_lines.append(f'  {service_name}/Waiter/{waiter_name}')

    for waiter_name in waiter_model.waiter_names:
        _assert_contains_lines_in_order(
            [
                '.. py:class:: {}.Waiter.{}'.format(
                    client.__class__.__name__, waiter_name
                ),
                '    waiter = client.get_waiter(\'%s\')'
                % xform_name(waiter_name),
                '  .. py:method:: wait(',
            ],
            get_nested_file_contents(service_name, 'Waiter', waiter_name),
        )

    _assert_contains_lines_in_order(ref_lines, generated_docs)


def _assert_has_resource_documentation(generated_docs, service_name, resource):
    ref_lines = [
        '================',
        'Service Resource',
        '================',
        '.. py:class:: %s.ServiceResource'
        % (resource.meta.client.__class__.__name__),
        '  A resource representing',
        '    import boto3',
        f'    {service_name} = boto3.resource(\'{service_name}\')',
    ]
    _assert_contains_lines_in_order(ref_lines, generated_docs)


def get_nested_file_contents(service_name, sub_folder, file_name):
    service_file_path = os.path.join(
        ROOT_SERVICES_PATH,
        service_name,
        sub_folder,
        f'{file_name}.rst',
    )
    with open(service_file_path, 'rb') as f:
        return f.read().decode('utf-8')
