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
from tests import unittest

from botocore.stub import Stubber

import boto3.session
from boto3.s3.transfer import TransferConfig


class TestS3MethodInjection(unittest.TestCase):
    def test_transfer_methods_injected_to_client(self):
        session = boto3.session.Session(region_name='us-west-2')
        client = session.client('s3')
        self.assertTrue(hasattr(client, 'upload_file'),
                        'upload_file was not injected onto S3 client')
        self.assertTrue(hasattr(client, 'download_file'),
                        'download_file was not injected onto S3 client')
        self.assertTrue(hasattr(client, 'copy'),
                        'copy was not injected onto S3 client')

    def test_bucket_resource_has_load_method(self):
        session = boto3.session.Session(region_name='us-west-2')
        bucket = session.resource('s3').Bucket('fakebucket')
        self.assertTrue(hasattr(bucket, 'load'),
                        'load() was not injected onto S3 Bucket resource.')

    def test_transfer_methods_injected_to_bucket(self):
        bucket = boto3.resource('s3').Bucket('my_bucket')
        self.assertTrue(hasattr(bucket, 'upload_file'),
                        'upload_file was not injected onto S3 bucket')
        self.assertTrue(hasattr(bucket, 'download_file'),
                        'download_file was not injected onto S3 bucket')
        self.assertTrue(hasattr(bucket, 'copy'),
                        'copy was not injected onto S3 bucket')

    def test_transfer_methods_injected_to_object(self):
        obj = boto3.resource('s3').Object('my_bucket', 'my_key')
        self.assertTrue(hasattr(obj, 'upload_file'),
                        'upload_file was not injected onto S3 object')
        self.assertTrue(hasattr(obj, 'download_file'),
                        'download_file was not injected onto S3 object')
        self.assertTrue(hasattr(obj, 'copy'),
                        'copy was not injected onto S3 object')


class TestCopy(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(
            aws_access_key_id='foo', aws_secret_access_key='bar',
            region_name='us-west-2')
        self.s3 = self.session.resource('s3')
        self.stubber = Stubber(self.s3.meta.client)
        self.copy_source = {'Bucket': 'foo', 'Key': 'bar'}
        self.bucket = 'mybucket'
        self.key = 'mykey'
        self.upload_id = 'uploadid'
        self.etag = '"example0etag"'
        self.progress = 0
        self.progress_times_called = 0

    def stub_single_part_copy(self):
        self.stub_head()
        self.stub_copy_object()

    def stub_multipart_copy(self, part_size, num_parts):
        # Set the HEAD to return the total size
        total_size = part_size * num_parts
        self.stub_head(content_length=total_size)

        # Add the response and assert params for CreateMultipartUpload
        create_upload_response = {
            "Bucket": self.bucket,
            "Key": self.key,
            "UploadId": self.upload_id
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
        }
        self.stubber.add_response(
            method='create_multipart_upload',
            service_response=create_upload_response,
            expected_params=expected_params)

        # Add the responses for each UploadPartCopy
        parts = []
        for i in range(num_parts):
            # Fill in the parts
            part_number = i + 1
            copy_range = "bytes=%s-%s" % (
                i * part_size,
                i * part_size + (part_size - 1)
            )
            self.stub_copy_part(part_number=part_number, copy_range=copy_range)
            parts.append({'ETag': self.etag, 'PartNumber': part_number})

        # Add the response for completing the upload
        complete_upload_response = {
            "Location": "us-west-2",
            "Bucket": self.bucket,
            "Key": self.key,
            "ETag": self.etag
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
            "MultipartUpload": {
                "Parts": parts
            },
            "UploadId": self.upload_id
        }

        self.stubber.add_response(
            method='complete_multipart_upload',
            service_response=complete_upload_response,
            expected_params=expected_params)

    def stub_head(self, content_length=4):
        head_response = {
            'AcceptRanges': 'bytes',
            'ContentLength': content_length,
            'ContentType': 'binary/octet-stream',
            'ETag': self.etag,
            'Metadata': {},
            'ResponseMetadata': {
                'HTTPStatusCode': 200,
            }
        }

        self.stubber.add_response(
            method='head_object', service_response=head_response,
            expected_params=self.copy_source)

    def stub_copy_object(self):
        copy_response = {
            'CopyObjectResult': {
                'ETag': self.etag
            },
            'ResponseMetadata': {
                'HTTPStatusCode': 200
            }
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
            "CopySource": self.copy_source
        }
        self.stubber.add_response(
            method='copy_object', service_response=copy_response,
            expected_params=expected_params)

    def stub_copy_part(self, part_number, copy_range):
        copy_part_response = {
            "CopyPartResult": {
                "ETag": self.etag
            },
            'ResponseMetadata': {
                'HTTPStatusCode': 200
            }
        }
        expected_params = {
            "Bucket": self.bucket,
            "Key": self.key,
            "CopySource": self.copy_source,
            "UploadId": self.upload_id,
            "PartNumber": part_number,
            "CopySourceRange": copy_range
        }
        self.stubber.add_response(
            method='upload_part_copy', service_response=copy_part_response,
            expected_params=expected_params)

    def test_client_copy(self):
        self.stub_single_part_copy()
        with self.stubber:
            response = self.s3.meta.client.copy(
                self.copy_source, self.bucket, self.key)
        # The response will be none on a successful transfer.
        self.assertIsNone(response)

    def test_bucket_copy(self):
        self.stub_single_part_copy()
        bucket = self.s3.Bucket(self.bucket)
        with self.stubber:
            response = bucket.copy(self.copy_source, self.key)
        # The response will be none on a successful transfer.
        self.assertIsNone(response)

    def test_object_copy(self):
        self.stub_single_part_copy()
        obj = self.s3.Object(self.bucket, self.key)
        with self.stubber:
            response = obj.copy(self.copy_source)
        self.assertIsNone(response)

    def test_copy_progress(self):
        self.stub_multipart_copy(5, 11)
        transfer_config = TransferConfig(
            multipart_chunksize=5, multipart_threshold=1,
            max_concurrency=1)

        def progress_callback(amount):
            self.progress += amount
            self.progress_times_called += 1

        with self.stubber:
            self.s3.meta.client.copy(
                Bucket=self.bucket, Key=self.key, CopySource=self.copy_source,
                Config=transfer_config, Callback=progress_callback)

        # Assert that the progress callback was called the correct number of
        # times with the correct amounts.
        self.assertEqual(self.progress_times_called, 11)
        self.assertEqual(self.progress, 55)


class TestS3ObjectSummary(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(
            aws_access_key_id='foo', aws_secret_access_key='bar',
            region_name='us-west-2')
        self.s3 = self.session.resource('s3')
        self.obj_summary = self.s3.ObjectSummary('my_bucket', 'my_key')
        self.obj_summary_size = 12
        self.stubber = Stubber(self.s3.meta.client)
        self.stubber.activate()
        self.stubber.add_response(
            method='head_object',
            service_response={
                'ContentLength': self.obj_summary_size, 'ETag': 'my-etag',
                'ContentType': 'binary'
            },
            expected_params={
                'Bucket': 'my_bucket',
                'Key': 'my_key'
            }
        )

    def tearDown(self):
        self.stubber.deactivate()

    def test_has_load(self):
        self.assertTrue(hasattr(self.obj_summary, 'load'),
                        'load() was not injected onto ObjectSummary resource.')

    def test_autoloads_correctly(self):
        # In HeadObject the parameter returned is ContentLength, this
        # should get mapped to Size of ListObject since the resource uses
        # the shape returned to by ListObjects.
        self.assertEqual(self.obj_summary.size, self.obj_summary_size)

    def test_cannot_access_other_non_related_parameters(self):
        # Even though an HeadObject was used to load this, it should
        # only expose the attributes from its shape defined in ListObjects.
        self.assertFalse(hasattr(self.obj_summary, 'content_length'))
