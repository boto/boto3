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
import io

import botocore
import botocore.stub
import pytest
from botocore.config import Config
from botocore.httpchecksum import DEFAULT_CHECKSUM_ALGORITHM
from botocore.stub import Stubber

import boto3.session
from boto3.s3.transfer import TransferConfig
from tests import unittest


class TestS3MethodInjection(unittest.TestCase):
    def test_transfer_methods_injected_to_client(self):
        session = boto3.session.Session(region_name='us-west-2')
        client = session.client('s3')
        assert hasattr(client, 'upload_file')
        assert hasattr(client, 'download_file')
        assert hasattr(client, 'copy')

    def test_bucket_resource_has_load_method(self):
        session = boto3.session.Session(region_name='us-west-2')
        bucket = session.resource('s3').Bucket('fakebucket')
        assert hasattr(bucket, 'load')

    def test_transfer_methods_injected_to_bucket(self):
        bucket = boto3.resource('s3').Bucket('my_bucket')
        assert hasattr(bucket, 'upload_file')
        assert hasattr(bucket, 'download_file')
        assert hasattr(bucket, 'copy')

    def test_transfer_methods_injected_to_object(self):
        obj = boto3.resource('s3').Object('my_bucket', 'my_key')
        assert hasattr(obj, 'upload_file')
        assert hasattr(obj, 'download_file')
        assert hasattr(obj, 'copy')


class BaseTransferTest(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(
            aws_access_key_id='foo',
            aws_secret_access_key='bar',
            region_name='us-west-2',
        )
        self.s3 = self.session.resource('s3')
        self.stubber = Stubber(self.s3.meta.client)
        self.bucket = 'mybucket'
        self.key = 'mykey'
        self.upload_id = 'uploadid'
        self.etag = '"example0etag"'
        self.progress = 0
        self.progress_times_called = 0

    def stub_head(self, content_length=4, expected_params=None):
        head_response = {
            'AcceptRanges': 'bytes',
            'ContentLength': content_length,
            'ContentType': 'binary/octet-stream',
            'ETag': self.etag,
            'Metadata': {},
            'ResponseMetadata': {
                'HTTPStatusCode': 200,
            },
        }

        if expected_params is None:
            expected_params = {'Bucket': self.bucket, 'Key': self.key}

        self.stubber.add_response(
            method='head_object',
            service_response=head_response,
            expected_params=expected_params,
        )

    def stub_create_multipart_upload(
        self,
        extra_expected_params=None,
    ):
        # Add the response and assert params for CreateMultipartUpload
        create_upload_response = {
            "Bucket": self.bucket,
            "Key": self.key,
            "UploadId": self.upload_id,
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
        }
        if extra_expected_params:
            expected_params.update(extra_expected_params)
        self.stubber.add_response(
            method='create_multipart_upload',
            service_response=create_upload_response,
            expected_params=expected_params,
        )

    def stub_complete_multipart_upload(
        self, parts, extra_expected_params=None
    ):
        complete_upload_response = {
            "Location": "us-west-2",
            "Bucket": self.bucket,
            "Key": self.key,
            "ETag": self.etag,
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
            "MultipartUpload": {"Parts": parts},
            "UploadId": self.upload_id,
        }
        if extra_expected_params:
            expected_params.update(extra_expected_params)

        self.stubber.add_response(
            method='complete_multipart_upload',
            service_response=complete_upload_response,
            expected_params=expected_params,
        )


class TestCopy(BaseTransferTest):
    def setUp(self):
        super().setUp()
        self.copy_source = {'Bucket': 'foo', 'Key': 'bar'}

    def stub_single_part_copy(self):
        self.stub_head(expected_params=self.copy_source)
        self.stub_copy_object()

    def stub_multipart_copy(self, part_size, num_parts):
        # Set the HEAD to return the total size
        total_size = part_size * num_parts
        self.stub_head(
            content_length=total_size, expected_params=self.copy_source
        )

        self.stub_create_multipart_upload()

        # Add the responses for each UploadPartCopy
        parts = []
        for i in range(num_parts):
            # Fill in the parts
            part_number = i + 1
            copy_range = (
                f"bytes={i * part_size}-{i * part_size + (part_size - 1)}"
            )
            self.stub_copy_part(part_number=part_number, copy_range=copy_range)
            parts.append({'ETag': self.etag, 'PartNumber': part_number})

        self.stub_complete_multipart_upload(parts)

    def stub_copy_object(self):
        copy_response = {
            'CopyObjectResult': {'ETag': self.etag},
            'ResponseMetadata': {'HTTPStatusCode': 200},
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
            "CopySource": self.copy_source,
        }
        self.stubber.add_response(
            method='copy_object',
            service_response=copy_response,
            expected_params=expected_params,
        )

    def stub_copy_part(self, part_number, copy_range):
        copy_part_response = {
            "CopyPartResult": {"ETag": self.etag},
            'ResponseMetadata': {'HTTPStatusCode': 200},
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
            "CopySource": self.copy_source,
            "UploadId": self.upload_id,
            "PartNumber": part_number,
            "CopySourceRange": copy_range,
        }
        self.stubber.add_response(
            method='upload_part_copy',
            service_response=copy_part_response,
            expected_params=expected_params,
        )

    def test_client_copy(self):
        self.stub_single_part_copy()
        with self.stubber:
            response = self.s3.meta.client.copy(
                self.copy_source, self.bucket, self.key
            )
        # The response will be none on a successful transfer.
        assert response is None

    def test_bucket_copy(self):
        self.stub_single_part_copy()
        bucket = self.s3.Bucket(self.bucket)
        with self.stubber:
            response = bucket.copy(self.copy_source, self.key)
        # The response will be none on a successful transfer.
        assert response is None

    def test_object_copy(self):
        self.stub_single_part_copy()
        obj = self.s3.Object(self.bucket, self.key)
        with self.stubber:
            response = obj.copy(self.copy_source)
        assert response is None

    def test_copy_progress(self):
        chunksize = 8 * (1024**2)
        self.stub_multipart_copy(chunksize, 3)
        transfer_config = TransferConfig(
            multipart_chunksize=chunksize,
            multipart_threshold=1,
            max_concurrency=1,
        )

        def progress_callback(amount):
            self.progress += amount
            self.progress_times_called += 1

        with self.stubber:
            self.s3.meta.client.copy(
                Bucket=self.bucket,
                Key=self.key,
                CopySource=self.copy_source,
                Config=transfer_config,
                Callback=progress_callback,
            )

        # Assert that the progress callback was called the correct number of
        # times with the correct amounts.
        assert self.progress_times_called == 3
        assert self.progress == chunksize * 3


class TestUploadFileobj(BaseTransferTest):
    def setUp(self):
        super().setUp()
        self.contents = io.BytesIO(b'foo\n')

    def stub_put_object(self):
        put_object_response = {
            "ETag": self.etag,
            "ResponseMetadata": {"HTTPStatusCode": 200},
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
            "Body": botocore.stub.ANY,
            "ChecksumAlgorithm": DEFAULT_CHECKSUM_ALGORITHM,
        }
        self.stubber.add_response(
            method='put_object',
            service_response=put_object_response,
            expected_params=expected_params,
        )

    def stub_upload_part(self, part_number):
        upload_part_response = {
            'ETag': self.etag,
            'ResponseMetadata': {'HTTPStatusCode': 200},
            'ChecksumCRC32': f'sum{part_number}==',
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
            "Body": botocore.stub.ANY,
            "PartNumber": part_number,
            "UploadId": self.upload_id,
            'ChecksumAlgorithm': 'CRC32',
        }
        self.stubber.add_response(
            method='upload_part',
            service_response=upload_part_response,
            expected_params=expected_params,
        )

    def stub_multipart_upload(self, num_parts):
        self.stub_create_multipart_upload(
            extra_expected_params={
                "ChecksumAlgorithm": DEFAULT_CHECKSUM_ALGORITHM,
            }
        )

        # Add the responses for each UploadPartCopy
        parts = []
        for i in range(num_parts):
            # Fill in the parts
            part_number = i + 1
            self.stub_upload_part(part_number=part_number)
            parts.append(
                {
                    'ETag': self.etag,
                    'PartNumber': part_number,
                    'ChecksumCRC32': f'sum{part_number}==',
                }
            )

        self.stub_complete_multipart_upload(parts)

    def test_client_upload(self):
        self.stub_put_object()
        with self.stubber:
            # The stubber will assert that all the right parameters are called.
            self.s3.meta.client.upload_fileobj(
                Fileobj=self.contents, Bucket=self.bucket, Key=self.key
            )

        self.stubber.assert_no_pending_responses()

    def test_raises_value_error_on_invalid_fileobj(self):
        with self.stubber:
            with pytest.raises(ValueError):
                self.s3.meta.client.upload_fileobj(
                    Fileobj='foo', Bucket=self.bucket, Key=self.key
                )

    def test_bucket_upload(self):
        self.stub_put_object()
        bucket = self.s3.Bucket(self.bucket)
        with self.stubber:
            # The stubber will assert that all the right parameters are called.
            bucket.upload_fileobj(Fileobj=self.contents, Key=self.key)

        self.stubber.assert_no_pending_responses()

    def test_object_upload(self):
        self.stub_put_object()
        obj = self.s3.Object(self.bucket, self.key)
        with self.stubber:
            # The stubber will assert that all the right parameters are called.
            obj.upload_fileobj(Fileobj=self.contents)

        self.stubber.assert_no_pending_responses()

    def test_multipart_upload(self):
        chunksize = 8 * (1024**2)
        contents = io.BytesIO(b'0' * (chunksize * 3))
        self.stub_multipart_upload(num_parts=3)
        transfer_config = TransferConfig(
            multipart_chunksize=chunksize,
            multipart_threshold=1,
            max_concurrency=1,
        )

        with self.stubber:
            # The stubber will assert that all the right parameters are called.
            self.s3.meta.client.upload_fileobj(
                Fileobj=contents,
                Bucket=self.bucket,
                Key=self.key,
                Config=transfer_config,
            )

        self.stubber.assert_no_pending_responses()


class TestDownloadFileobj(BaseTransferTest):
    def setUp(self):
        super().setUp()
        self.contents = b'foo'
        self.fileobj = io.BytesIO()

    def stub_single_part_download(self):
        self.stub_head(content_length=len(self.contents))
        self.stub_get_object(self.contents)

    def stub_get_object(self, full_contents, start_byte=0, end_byte=None):
        """
        Stubs out the get_object operation.

        :param full_contents: The FULL contents of the object
        :param start_byte: The first byte to grab.
        :param end_byte: The last byte to grab.
        """
        get_object_response = {}
        expected_params = {}
        contents = full_contents
        end_byte_range = end_byte

        # If the start byte is set and the end byte is not, the end byte is
        # the last byte.
        if start_byte != 0 and end_byte is None:
            end_byte = len(full_contents) - 1

        # The range on get object where the the end byte is the last byte
        # should set the input range as e.g. Range='bytes=3-'
        if end_byte == len(full_contents) - 1:
            end_byte_range = ''

        # If this is a ranged get, ContentRange needs to be returned,
        # contents needs to be pruned, and Range needs to be an expected param.
        if end_byte is not None:
            contents = full_contents[start_byte : end_byte + 1]
            part_range = f'bytes={start_byte}-{end_byte_range}'
            content_range = (
                f'bytes={start_byte}-{end_byte}/{len(full_contents)}'
            )
            get_object_response['ContentRange'] = content_range
            expected_params['Range'] = part_range

        get_object_response.update(
            {
                "AcceptRanges": "bytes",
                "ETag": self.etag,
                "ContentLength": len(contents),
                "ContentType": "binary/octet-stream",
                "Body": io.BytesIO(contents),
                "ResponseMetadata": {"HTTPStatusCode": 200},
            }
        )
        expected_params.update({"Bucket": self.bucket, "Key": self.key})

        self.stubber.add_response(
            method='get_object',
            service_response=get_object_response,
            expected_params=expected_params,
        )

    def stub_multipart_download(self, contents, part_size, num_parts):
        self.stub_head(content_length=len(contents))

        for i in range(num_parts):
            start_byte = i * part_size
            end_byte = (i + 1) * part_size - 1
            self.stub_get_object(
                full_contents=contents,
                start_byte=start_byte,
                end_byte=end_byte,
            )

    def test_client_download(self):
        self.stub_single_part_download()
        with self.stubber:
            self.s3.meta.client.download_fileobj(
                Bucket=self.bucket, Key=self.key, Fileobj=self.fileobj
            )

        assert self.fileobj.getvalue() == self.contents
        self.stubber.assert_no_pending_responses()

    def test_raises_value_error_on_invalid_fileobj(self):
        with self.stubber:
            with pytest.raises(ValueError):
                self.s3.meta.client.download_fileobj(
                    Bucket=self.bucket, Key=self.key, Fileobj='foo'
                )

    def test_bucket_download(self):
        self.stub_single_part_download()
        bucket = self.s3.Bucket(self.bucket)
        with self.stubber:
            bucket.download_fileobj(Key=self.key, Fileobj=self.fileobj)

        assert self.fileobj.getvalue() == self.contents
        self.stubber.assert_no_pending_responses()

    def test_object_download(self):
        self.stub_single_part_download()
        obj = self.s3.Object(self.bucket, self.key)
        with self.stubber:
            obj.download_fileobj(Fileobj=self.fileobj)

        assert self.fileobj.getvalue() == self.contents
        self.stubber.assert_no_pending_responses()

    def test_multipart_download(self):
        self.contents = b'A' * 55
        self.stub_multipart_download(
            contents=self.contents, part_size=5, num_parts=11
        )
        transfer_config = TransferConfig(
            multipart_chunksize=5, multipart_threshold=1, max_concurrency=1
        )

        with self.stubber:
            self.s3.meta.client.download_fileobj(
                Bucket=self.bucket,
                Key=self.key,
                Fileobj=self.fileobj,
                Config=transfer_config,
            )

        assert self.fileobj.getvalue() == self.contents
        self.stubber.assert_no_pending_responses()

    def test_download_progress(self):
        self.contents = b'A' * 55
        self.stub_multipart_download(
            contents=self.contents, part_size=5, num_parts=11
        )
        transfer_config = TransferConfig(
            multipart_chunksize=5, multipart_threshold=1, max_concurrency=1
        )

        def progress_callback(amount):
            self.progress += amount
            self.progress_times_called += 1

        with self.stubber:
            self.s3.meta.client.download_fileobj(
                Bucket=self.bucket,
                Key=self.key,
                Fileobj=self.fileobj,
                Config=transfer_config,
                Callback=progress_callback,
            )

        # Assert that the progress callback was called the correct number of
        # times with the correct amounts.
        assert self.progress_times_called == 11
        assert self.progress == 55
        self.stubber.assert_no_pending_responses()


class TestS3ObjectSummary(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(
            aws_access_key_id='foo',
            aws_secret_access_key='bar',
            region_name='us-west-2',
        )
        self.s3 = self.session.resource('s3')
        self.obj_summary = self.s3.ObjectSummary('my_bucket', 'my_key')
        self.obj_summary_size = 12
        self.stubber = Stubber(self.s3.meta.client)
        self.stubber.activate()
        self.stubber.add_response(
            method='head_object',
            service_response={
                'ContentLength': self.obj_summary_size,
                'ETag': 'my-etag',
                'ContentType': 'binary',
            },
            expected_params={'Bucket': 'my_bucket', 'Key': 'my_key'},
        )

    def tearDown(self):
        self.stubber.deactivate()

    def test_has_load(self):
        # Validate load was injected onto ObjectSummary.
        assert hasattr(self.obj_summary, 'load')

    def test_autoloads_correctly(self):
        # In HeadObject the parameter returned is ContentLength, this
        # should get mapped to Size of ListObject since the resource uses
        # the shape returned to by ListObjects.
        assert self.obj_summary.size == self.obj_summary_size

    def test_cannot_access_other_non_related_parameters(self):
        # Even though an HeadObject was used to load this, it should
        # only expose the attributes from its shape defined in ListObjects.
        assert not hasattr(self.obj_summary, 'content_length')


class TestServiceResource(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session()

    def test_unsigned_signature_version_is_not_corrupted(self):
        config = Config(signature_version=botocore.UNSIGNED)
        resource = self.session.resource('s3', config=config)
        sig_version = resource.meta.client.meta.config.signature_version
        assert sig_version is botocore.UNSIGNED
