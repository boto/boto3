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
import botocore.exceptions
import pytest
import s3transfer
from botocore.compat import HAS_CRT
from botocore.credentials import Credentials

import boto3
from boto3.s3.transfer import TransferConfig
from tests import mock, requires_crt

if HAS_CRT:
    import awscrt.s3
    from s3transfer.crt import BotocoreCRTCredentialsWrapper

    import boto3.crt


def create_test_client(service_name='s3', region_name="us-east-1"):
    return boto3.client(
        service_name,
        region_name=region_name,
        aws_access_key_id="access",
        aws_secret_access_key="secret",
        aws_session_token="token",
    )


USW2_S3_CLIENT = create_test_client(region_name="us-west-2")
USE1_S3_CLIENT = create_test_client(region_name="us-east-1")


class TestCRTTransferManager:
    @requires_crt()
    def test_create_crt_transfer_manager_with_lock_in_use(self):
        with mock.patch('boto3.crt.acquire_crt_s3_process_lock') as lock:
            lock.return_value = None

            # Verify we can't create a second CRT client
            tm = boto3.crt.create_crt_transfer_manager(USW2_S3_CLIENT, None)
            assert tm is None

    @requires_crt()
    def test_create_crt_transfer_manager(self):
        tm = boto3.crt.create_crt_transfer_manager(USW2_S3_CLIENT, None)
        assert isinstance(tm, s3transfer.crt.CRTTransferManager)

    @requires_crt()
    def test_crt_singleton_is_returned_every_call(self):
        first_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, None)
        second_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, None)

        assert isinstance(first_s3_client, boto3.crt.CRTS3Client)
        assert first_s3_client is second_s3_client
        assert first_s3_client.crt_client is second_s3_client.crt_client

    @requires_crt()
    def test_create_crt_transfer_manager_w_client_in_wrong_region(self):
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

    @pytest.mark.parametrize(
        "boto3_tuple,crt_tuple,matching",
        (
            (
                ("access", "secret", "token"),
                ("access", "secret", "token"),
                True,
            ),
            (
                ("access", "secret", "token"),
                ("noaccess", "secret", "token"),
                False,
            ),
            (
                ("access", "secret", "token"),
                ("access", "nosecret", "token"),
                False,
            ),
            (
                ("access", "secret", "token"),
                ("access", "secret", "notoken"),
                False,
            ),
        ),
    )
    @requires_crt()
    def test_compare_identities(self, boto3_tuple, crt_tuple, matching):
        boto3_creds = Credentials(*boto3_tuple)
        crt_creds = Credentials(*crt_tuple)
        crt_creds_wrapper = BotocoreCRTCredentialsWrapper(crt_creds)
        assert (
            boto3.crt.compare_identity(boto3_creds, crt_creds_wrapper)
            is matching
        )

    @requires_crt()
    def test_compare_idenities_no_credentials(self):
        def no_credentials():
            raise botocore.exceptions.NoCredentialsError()

        boto3_creds = Credentials("access", "secret", "token")
        crt_creds_wrapper = no_credentials
        assert (
            boto3.crt.compare_identity(boto3_creds, crt_creds_wrapper) is False
        )

    @requires_crt()
    def test_get_crt_s3_client(self):
        config = TransferConfig()
        crt_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, config)
        assert isinstance(crt_s3_client, boto3.crt.CRTS3Client)
        assert isinstance(
            crt_s3_client.process_lock, awscrt.s3.CrossProcessLock
        )
        assert crt_s3_client.region == "us-west-2"
        assert isinstance(
            crt_s3_client.cred_provider, BotocoreCRTCredentialsWrapper
        )

    @requires_crt()
    def test_get_crt_s3_client_w_wrong_region(self):
        config = TransferConfig()
        crt_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, config)
        assert isinstance(crt_s3_client, boto3.crt.CRTS3Client)

        # Ensure we don't create additional CRT clients
        use1_crt_s3_client = boto3.crt.get_crt_s3_client(
            USE1_S3_CLIENT, config
        )
        assert use1_crt_s3_client is crt_s3_client
        assert use1_crt_s3_client.region == "us-west-2"
