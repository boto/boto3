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

from boto3.session import Session
import botocore.session

boto3_session = None


def create_session():
    global boto3_session
    if boto3_session is None:
        boto3_session = Session(
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy',
            region_name='us-east-1'
        )

    return boto3_session


def _all_resources():
    session = create_session()
    for service_name in session.get_available_resources():
        yield session, service_name


def _all_clients():
    session = create_session()
    for service_name in session.get_available_services():
        yield session, service_name


def _all_api_version_args():
    botocore_session = botocore.session.get_session()
    boto3_session = create_session()
    for service_name in boto3_session.get_available_resources():
        yield (service_name, botocore_session, boto3_session)


@pytest.mark.parametrize('resource_args', _all_resources())
def test_can_create_all_resources(resource_args):
    """Verify we can create all existing resources."""
    session, service_name = resource_args
    resource = session.resource(service_name)
    # Verifying we have a "meta" attr is just an arbitrary
    # sanity check.
    assert hasattr(resource, 'meta')


@pytest.mark.parametrize('client_args', _all_clients())
def test_can_create_all_clients(client_args):
    """Verify we can create all existing clients."""
    session, service_name = client_args
    client = session.client(service_name)
    assert hasattr(client, 'meta')


@pytest.mark.parametrize('api_version_args', _all_api_version_args())
def test_api_versions_synced_with_botocore(api_version_args):
    """Verify both boto3 and botocore clients stay in sync."""
    service_name, botocore_session, boto3_session = api_version_args
    resource = boto3_session.resource(service_name)
    boto3_api_version = resource.meta.client.meta.service_model.api_version
    client = botocore_session.create_client(
        service_name,
        region_name='us-east-1',
        aws_access_key_id='foo',
        aws_secret_access_key='bar'
    )
    botocore_api_version = client.meta.service_model.api_version
    err = (
        f"Different latest API versions found for {service_name}: "
        f"{botocore_api_version} (botocore), {boto3_api_version} (boto3)\n"
    )
    assert botocore_api_version == boto3_api_version, err
