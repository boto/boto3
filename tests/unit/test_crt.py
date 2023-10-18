# Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import boto3
import s3transfer
from botocore.compat import HAS_CRT

from tests import mock, requires_crt

if HAS_CRT:
    import boto3.crt


USW2_S3_CLIENT = boto3.client('s3', region_name='us-west-2')
USE1_S3_CLIENT = boto3.client('s3', region_name='us-east-1')


@requires_crt()
def test_create_crt_transfer_manager_with_lock_in_use():
    with mock.patch('boto3.crt.acquire_crt_s3_process_lock') as lock:
        lock.return_value = None

        # Verify we can't create a second CRT client
        tm = boto3.crt.create_crt_transfer_manager(USW2_S3_CLIENT, None)
        assert tm is None


@requires_crt()
def test_create_crt_transfer_manager():
    tm = boto3.crt.create_crt_transfer_manager(USW2_S3_CLIENT, None)
    assert isinstance(tm, s3transfer.crt.CRTTransferManager)


@requires_crt()
def test_crt_singleton_is_returned_every_call():
    first_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, None)
    second_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, None)

    assert isinstance(first_s3_client, boto3.crt.CRTS3Client)
    assert first_s3_client is second_s3_client
    assert first_s3_client.crt_client is second_s3_client.crt_client


@requires_crt()
def test_create_crt_transfer_manager_w_client_in_wrong_region():
    """Ensure we don't return the crt transfer manager if client is in
    different region. The CRT isn't able to handle region redirects and
    will consistently fail.

    We can remove this test once we have this fixed on the CRT side.
    """
    usw2_s3_client = boto3.crt.create_crt_transfer_manager(
        USW2_S3_CLIENT, None
    )
    assert isinstance(usw2_s3_client, boto3.crt.CRTTransferManager)

    use1_s3_client = boto3.crt.create_crt_transfer_manager(
        USE1_S3_CLIENT, None
    )
    assert use1_s3_client is None
