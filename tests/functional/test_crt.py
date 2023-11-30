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

from contextlib import ContextDecorator

import pytest
from botocore.compat import HAS_CRT
from botocore.credentials import Credentials

from boto3.s3.transfer import (
    TransferConfig,
    create_transfer_manager,
    has_minimum_crt_version,
)
from tests import mock, requires_crt

if HAS_CRT:
    from s3transfer.crt import CRTTransferManager


class MockOptimizedInstance(ContextDecorator):
    """Helper class to simulate a CRT optimized EC2 instance."""

    DEFAULT_LOCK_MOCK = mock.Mock()

    def __init__(self, lock=DEFAULT_LOCK_MOCK, optimized=True):
        self.acquire_process_lock = mock.patch(
            'boto3.crt.acquire_crt_s3_process_lock'
        )
        self.acquire_process_lock.return_value = lock
        self.is_optimized = mock.patch('awscrt.s3.is_optimized_for_system')
        self.is_optimized.return_value = optimized

    def __enter__(self, *args, **kwargs):
        self.acquire_process_lock.start()
        self.is_optimized.start()

    def __exit__(self, *args, **kwargs):
        self.acquire_process_lock.stop()
        self.is_optimized.stop()


def create_mock_client(region_name='us-west-2'):
    client = mock.Mock()
    client.meta.region_name = region_name
    client._get_credentials.return_value = Credentials(
        'access', 'secret', 'token'
    )
    return client


class TestS3TransferWithCRT:
    @requires_crt()
    @MockOptimizedInstance()
    def test_create_transfer_manager_on_optimized_instance(self):
        client = create_mock_client()
        config = TransferConfig()
        transfer_manager = create_transfer_manager(client, config)
        assert isinstance(transfer_manager, CRTTransferManager)

    @requires_crt()
    def test_minimum_crt_version(self):
        assert has_minimum_crt_version((0, 16, 12)) is True

    @pytest.mark.parametrize(
        "bad_version",
        (
            None,
            "0.1.0-dev",
            "0.20",
            object(),
        ),
    )
    @requires_crt()
    def test_minimum_crt_version_bad_crt_version(self, bad_version):
        with mock.patch("awscrt.__version__") as vers:
            vers.return_value = bad_version

            assert has_minimum_crt_version((0, 16, 12)) is False
