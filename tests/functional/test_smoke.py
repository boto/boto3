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
import pytest

from boto3.session import Session
import botocore.session


boto3_session = Session(
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy',
            region_name='us-east-1'
)


@pytest.mark.parametrize(
    "resource_name", boto3_session.get_available_resources()
)
def test_create_resource(resource_name):
    """Verify we can create all existing resources."""
    resource = boto3_session.resource(resource_name)
    # Verifying we have a "meta" attr is just an arbitrary
    # sanity check.
    assert hasattr(resource, 'meta')


@pytest.mark.parametrize(
    "service_name", boto3_session.get_available_services()
)
def test_create_client(service_name):
    client = boto3_session.client(service_name)
    assert hasattr(client, 'meta')


@pytest.mark.parametrize(
    "resource_name", boto3_session.get_available_resources()
)
def test_api_versions_synced_with_botocore(resource_name):
    botocore_session = botocore.session.get_session()
    resource = boto3_session.resource(resource_name)
    boto3_api_version = resource.meta.client.meta.service_model.api_version
    client = botocore_session.create_client(resource_name,
                                            region_name='us-east-1',
                                            aws_access_key_id='foo',
                                            aws_secret_access_key='bar')
    botocore_api_version = client.meta.service_model.api_version
    if botocore_api_version != boto3_api_version:
        raise AssertionError(
            "Different latest API versions found for %s: "
            "%s (botocore), %s (boto3)\n" % (resource_name,
                                             botocore_api_version,
                                             boto3_api_version))
