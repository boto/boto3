# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is
# distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import mock

from botocore.exceptions import ClientError
from botocore.compat import six

from boto3.s3 import inject
from tests import unittest


class TestInjectTransferMethods(unittest.TestCase):
    def test_inject_upload_download_file_to_client(self):
        class_attributes = {}
        inject.inject_s3_transfer_methods(class_attributes=class_attributes)
        self.assertIn('upload_file', class_attributes)
        self.assertIn('download_file', class_attributes)

    def test_upload_file_proxies_to_transfer_object(self):
        with mock.patch('boto3.s3.inject.S3Transfer') as transfer:
            inject.upload_file(mock.sentinel.CLIENT,
                               Filename='filename',
                               Bucket='bucket', Key='key')
            transfer_in_context_manager = \
                transfer.return_value.__enter__.return_value
            transfer_in_context_manager.upload_file.assert_called_with(
                filename='filename', bucket='bucket', key='key',
                extra_args=None, callback=None)

    def test_download_file_proxies_to_transfer_object(self):
        with mock.patch('boto3.s3.inject.S3Transfer') as transfer:
            inject.download_file(
                mock.sentinel.CLIENT,
                Bucket='bucket', Key='key',
                Filename='filename')
            transfer_in_context_manager = \
                transfer.return_value.__enter__.return_value
            transfer_in_context_manager.download_file.assert_called_with(
                bucket='bucket', key='key', filename='filename',
                extra_args=None, callback=None)


class TestBucketLoad(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock()
        self.resource = mock.Mock()
        self.resource.meta.client = self.client

    def test_bucket_load_finds_bucket(self):
        self.resource.name = 'MyBucket'
        self.client.list_buckets.return_value = {
            'Buckets': [
                {'Name': 'NotMyBucket', 'CreationDate': 1},
                {'Name': self.resource.name, 'CreationDate': 2},
            ],
        }

        inject.bucket_load(self.resource)
        self.assertEqual(
            self.resource.meta.data,
            {'Name': self.resource.name, 'CreationDate': 2})

    def test_bucket_load_doesnt_find_bucket(self):
        self.resource.name = 'MyBucket'
        self.client.list_buckets.return_value = {
            'Buckets': [
                {'Name': 'NotMyBucket', 'CreationDate': 1},
                {'Name': 'NotMine2', 'CreationDate': 2},
            ],
        }
        inject.bucket_load(self.resource)
        self.assertEqual(self.resource.meta.data, {})

    def test_bucket_load_encounters_access_exception(self):
        self.client.list_buckets.side_effect = ClientError(
            {'Error':
             {'Code': 'AccessDenied',
              'Message': 'Access Denied'}},
            'ListBuckets')
        inject.bucket_load(self.resource)
        self.assertEqual(self.resource.meta.data, {})

    def test_bucket_load_encounters_other_exception(self):
        self.client.list_buckets.side_effect = ClientError(
            {'Error':
             {'Code': 'ExpiredToken',
              'Message': 'The provided token has expired.'}},
            'ListBuckets')
        with self.assertRaises(ClientError):
            inject.bucket_load(self.resource)

class TestBucketTransferMethods(unittest.TestCase):

    def setUp(self):
        self.bucket = mock.Mock(name='my_bucket')
        self.copy_source = {'Bucket': 'foo', 'Key': 'bar'}

    def test_upload_file_proxies_to_meta_client(self):
        inject.bucket_upload_file(self.bucket, Filename='foo', Key='key')
        self.bucket.meta.client.upload_file.assert_called_with(
            Filename='foo', Bucket=self.bucket.name, Key='key',
            ExtraArgs=None, Callback=None, Config=None)

    def test_download_file_proxies_to_meta_client(self):
        inject.bucket_download_file(self.bucket, Key='key', Filename='foo')
        self.bucket.meta.client.download_file.assert_called_with(
            Bucket=self.bucket.name, Key='key', Filename='foo',
            ExtraArgs=None, Callback=None, Config=None)

    def test_copy(self):
        inject.bucket_copy(self.bucket, self.copy_source, Key='key')
        self.bucket.meta.client.copy.assert_called_with(
            CopySource=self.copy_source, Bucket=self.bucket.name, Key='key',
            ExtraArgs=None, Callback=None, SourceClient=None, Config=None)

    def test_upload_fileobj(self):
        fileobj = six.BytesIO(b'foo')
        inject.bucket_upload_fileobj(self.bucket, Key='key', Fileobj=fileobj)
        self.bucket.meta.client.upload_fileobj.assert_called_with(
            Bucket=self.bucket.name, Fileobj=fileobj, Key='key',
            ExtraArgs=None, Callback=None, Config=None)

    def test_download_fileobj(self):
        obj = six.BytesIO()
        inject.bucket_download_fileobj(self.bucket, Key='key', Fileobj=obj)
        self.bucket.meta.client.download_fileobj.assert_called_with(
            Bucket=self.bucket.name, Key='key', Fileobj=obj, ExtraArgs=None,
            Callback=None, Config=None)


class TestObjectTransferMethods(unittest.TestCase):

    def setUp(self):
        self.obj = mock.Mock(bucket_name='my_bucket', key='my_key')
        self.copy_source = {'Bucket': 'foo', 'Key': 'bar'}

    def test_upload_file_proxies_to_meta_client(self):
        inject.object_upload_file(self.obj, Filename='foo')
        self.obj.meta.client.upload_file.assert_called_with(
            Filename='foo', Bucket=self.obj.bucket_name, Key=self.obj.key,
            ExtraArgs=None, Callback=None, Config=None)

    def test_download_file_proxies_to_meta_client(self):
        inject.object_download_file(self.obj, Filename='foo')
        self.obj.meta.client.download_file.assert_called_with(
            Bucket=self.obj.bucket_name, Key=self.obj.key, Filename='foo',
            ExtraArgs=None, Callback=None, Config=None)

    def test_copy(self):
        inject.object_copy(self.obj, self.copy_source)
        self.obj.meta.client.copy.assert_called_with(
            CopySource=self.copy_source, Bucket=self.obj.bucket_name,
            Key=self.obj.key, ExtraArgs=None, Callback=None,
            SourceClient=None, Config=None)

    def test_upload_fileobj(self):
        fileobj = six.BytesIO(b'foo')
        inject.object_upload_fileobj(self.obj, Fileobj=fileobj)
        self.obj.meta.client.upload_fileobj.assert_called_with(
            Bucket=self.obj.bucket_name, Fileobj=fileobj, Key=self.obj.key,
            ExtraArgs=None, Callback=None, Config=None)

    def test_download_fileobj(self):
        fileobj = six.BytesIO()
        inject.object_download_fileobj(self.obj, Fileobj=fileobj)
        self.obj.meta.client.download_fileobj.assert_called_with(
            Bucket=self.obj.bucket_name, Key=self.obj.key, Fileobj=fileobj,
            ExtraArgs=None, Callback=None, Config=None)


class TestObejctSummaryLoad(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock()
        self.resource = mock.Mock()
        self.resource.meta.client = self.client
        self.head_object_response = {
            'ContentLength': 5, 'ETag': 'my-etag'
        }
        self.client.head_object.return_value = self.head_object_response

    def test_object_summary_load(self):
        inject.object_summary_load(self.resource)
        self.assertEqual(
            self.resource.meta.data, {'Size': 5, 'ETag': 'my-etag'})

    def test_can_handle_missing_content_length(self):
        self.head_object_response.pop('ContentLength')
        inject.object_summary_load(self.resource)
        self.assertEqual(self.resource.meta.data, {'ETag': 'my-etag'})
