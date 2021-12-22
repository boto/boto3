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
import pytest
import botocore.session
from botocore import xform_name
from botocore.exceptions import DataNotFoundError

import boto3
from boto3.docs.service import ServiceDocumenter


@pytest.fixture
def botocore_session():
    return botocore.session.get_session()


@pytest.fixture
def boto3_session():
    return boto3.Session(region_name='us-east-1')


def all_services():
    session = boto3.Session(region_name='us-east-1')
    for service_name in session.get_available_services():
        yield service_name


@pytest.fixture
def available_resources():
    session = boto3.Session(region_name='us-east-1')
    return session.get_available_resources()


@pytest.mark.parametrize('service_name', all_services())
def test_documentation(
    boto3_session, botocore_session, available_resources, service_name
):
    generated_docs = ServiceDocumenter(
        service_name, session=boto3_session).document_service()
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
            generated_docs, service_name, client,
            sorted(paginator_model._paginator_config)
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
        contents = contents[(beginning + len(line)):]


def _assert_has_title(generated_docs, client):
    title = client.__class__.__name__
    ref_lines = [
        '*' * len(title),
        title,
        '*' * len(title)
    ]
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
        '  These are the available methods:',
        '  *   :py:meth:`~%s.Client.get_paginator`' % class_name,
        '  *   :py:meth:`~%s.Client.get_waiter`' % class_name,
        '  .. py:method:: get_paginator(operation_name)',
        '  .. py:method:: get_waiter(waiter_name)',
    ]
    _assert_contains_lines_in_order(ref_lines, generated_docs)


def _assert_has_paginator_documentation(generated_docs, service_name, client,
                                        paginator_names):
    ref_lines = [
        '==========',
        'Paginators',
        '==========',
        'The available paginators are:'
    ]
    for paginator_name in paginator_names:
        ref_lines.append(
            '* :py:class:`%s.Paginator.%s`' % (
                client.__class__.__name__, paginator_name))

    for paginator_name in paginator_names:
        ref_lines.append(
            '.. py:class:: %s.Paginator.%s' % (
                client.__class__.__name__, paginator_name))
        ref_lines.append(
            '  .. py:method:: paginate(')

    _assert_contains_lines_in_order(ref_lines, generated_docs)


def _assert_has_waiter_documentation(generated_docs, service_name, client,
                                     waiter_model):
    ref_lines = [
        '=======',
        'Waiters',
        '=======',
        'The available waiters are:'
    ]
    for waiter_name in waiter_model.waiter_names:
        ref_lines.append(
            '* :py:class:`%s.Waiter.%s`' % (
                client.__class__.__name__, waiter_name))

    for waiter_name in waiter_model.waiter_names:
        ref_lines.append(
            '.. py:class:: %s.Waiter.%s' % (
                client.__class__.__name__, waiter_name))
        ref_lines.append(
            '    waiter = client.get_waiter(\'%s\')' % xform_name(waiter_name))
        ref_lines.append(
            '  .. py:method:: wait(')

    _assert_contains_lines_in_order(ref_lines, generated_docs)


def _assert_has_resource_documentation(generated_docs, service_name, resource):
    ref_lines = [
        '================',
        'Service Resource',
        '================',
        '.. py:class:: %s.ServiceResource' % (
            resource.meta.client.__class__.__name__),
        '  A resource representing',
        '    import boto3',
        '    %s = boto3.resource(\'%s\')' % (service_name, service_name),
    ]
    _assert_contains_lines_in_order(ref_lines, generated_docs)
