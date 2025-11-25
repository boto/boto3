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
    from awscrt.s3 import CrossProcessLock as CrossProcessLockClass
    from s3transfer.crt import BotocoreCRTCredentialsWrapper

    import boto3.crt


@pytest.fixture
def mock_crt_process_lock(monkeypatch):
    # The process lock is cached at the module layer whenever the
    # cross process lock is successfully acquired. This patch ensures that
    # test cases will start off with no previously cached process lock and
    # if a cross process is instantiated/acquired it will be the mock that
    # can be used for controlling lock behavior.
    if HAS_CRT:
        monkeypatch.setattr('s3transfer.crt.CRT_S3_PROCESS_LOCK', None)
        with mock.patch('awscrt.s3.CrossProcessLock', spec=True) as mock_lock:
            yield mock_lock
    else:
        # We cannot mock or use the lock without CRT support.
        yield None


@pytest.fixture
def mock_crt_client_singleton(monkeypatch):
    # Clear CRT state for each test
    if HAS_CRT:
        monkeypatch.setattr('boto3.crt.CRT_S3_CLIENT', None)
    yield None


@pytest.fixture
def mock_serializer_singleton(monkeypatch):
    # Clear CRT state for each test
    if HAS_CRT:
        monkeypatch.setattr('boto3.crt.BOTOCORE_CRT_SERIALIZER', None)
    yield None


def create_test_client(
    service_name='s3', region_name="us-east-1", endpoint_url=None
):
    return boto3.client(
        service_name,
        region_name=region_name,
        aws_access_key_id="access",
        aws_secret_access_key="secret",
        aws_session_token="token",
        endpoint_url=endpoint_url,
    )


USW2_S3_CLIENT = create_test_client(region_name="us-west-2")
USE1_S3_CLIENT = create_test_client(region_name="us-east-1")


class TestCRTTransferManager:
    @requires_crt()
    def test_create_crt_transfer_manager_with_lock_in_use(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
        mock_crt_process_lock.return_value.acquire.side_effect = RuntimeError

        # Verify we can't create a second CRT client
        tm = boto3.crt.create_crt_transfer_manager(USW2_S3_CLIENT, None)
        assert tm is None

    @requires_crt()
    def test_create_crt_transfer_manager(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
        tm = boto3.crt.create_crt_transfer_manager(USW2_S3_CLIENT, None)
        assert isinstance(tm, s3transfer.crt.CRTTransferManager)

    @requires_crt()
    def test_crt_singleton_is_returned_every_call(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
        first_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, None)
        second_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, None)

        assert isinstance(first_s3_client, boto3.crt.CRTS3Client)
        assert first_s3_client is second_s3_client
        assert first_s3_client.crt_client is second_s3_client.crt_client

    @requires_crt()
    def test_create_crt_transfer_manager_w_client_in_wrong_region(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
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
            # Token normalization: None and empty string should be treated as equivalent
            (
                ("access", "secret", None),
                ("access", "secret", ""),
                True,
            ),
            (
                ("access", "secret", ""),
                ("access", "secret", None),
                True,
            ),
            (
                ("access", "secret", None),
                ("access", "secret", None),
                True,
            ),
            (
                ("access", "secret", ""),
                ("access", "secret", ""),
                True,
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
    def test_get_crt_s3_client(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
        config = TransferConfig()
        crt_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, config)
        assert isinstance(crt_s3_client, boto3.crt.CRTS3Client)
        assert isinstance(crt_s3_client.process_lock, CrossProcessLockClass)
        assert crt_s3_client.region == "us-west-2"
        assert isinstance(
            crt_s3_client.cred_provider, BotocoreCRTCredentialsWrapper
        )

    @requires_crt()
    def test_get_crt_s3_client_w_wrong_region(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
        config = TransferConfig()
        crt_s3_client = boto3.crt.get_crt_s3_client(USW2_S3_CLIENT, config)
        assert isinstance(crt_s3_client, boto3.crt.CRTS3Client)

        # Ensure we don't create additional CRT clients
        use1_crt_s3_client = boto3.crt.get_crt_s3_client(
            USE1_S3_CLIENT, config
        )
        assert use1_crt_s3_client is crt_s3_client
        assert use1_crt_s3_client.region == "us-west-2"

    @requires_crt()
    def test_create_crt_transfer_manager_with_custom_endpoint(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
        """Test that custom endpoints are properly passed through to the serializer"""
        custom_endpoint = "https://custom-s3.example.com"
        custom_client = create_test_client(
            region_name="us-west-2", endpoint_url=custom_endpoint
        )

        tm = boto3.crt.create_crt_transfer_manager(custom_client, None)
        assert isinstance(tm, s3transfer.crt.CRTTransferManager)

        # Verify the serializer was created with the custom endpoint
        serializer = boto3.crt.BOTOCORE_CRT_SERIALIZER
        assert serializer is not None
        # Check that the client_kwargs passed to the serializer includes the endpoint_url
        assert hasattr(serializer, '_client')
        # The serializer's internal client should have the custom endpoint
        assert serializer._client.meta.endpoint_url == custom_endpoint

    @requires_crt()
    def test_create_crt_request_serializer_with_custom_endpoint(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
        """Test that _create_crt_request_serializer properly handles custom endpoints"""
        from botocore.session import Session

        custom_endpoint = "https://custom-s3.example.com"
        session = Session()

        serializer = boto3.crt._create_crt_request_serializer(
            session, "us-west-2", endpoint_url=custom_endpoint
        )

        # Verify serializer was created and has the custom endpoint in its client
        assert serializer is not None
        assert hasattr(serializer, '_client')
        assert serializer._client.meta.endpoint_url == custom_endpoint
        # Verify path-style addressing is configured for custom endpoints
        assert serializer._client.meta.config.s3['addressing_style'] == 'path'

    @requires_crt()
    def test_create_crt_request_serializer_without_custom_endpoint(
        self,
        mock_crt_process_lock,
        mock_crt_client_singleton,
        mock_serializer_singleton,
    ):
        """Test that _create_crt_request_serializer works without custom endpoint (default behavior)"""
        from botocore.session import Session

        session = Session()

        serializer = boto3.crt._create_crt_request_serializer(
            session, "us-west-2", endpoint_url=None
        )

        # Verify serializer was created
        assert serializer is not None
        assert hasattr(serializer, '_client')
