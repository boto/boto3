# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
import os
import threading
import math
import time
import random
import tempfile
import shutil
import hashlib

from tests import unittest, unique_id
from botocore.vendored import six

import boto3.session
import boto3.s3.transfer


urlopen = six.moves.urllib.request.urlopen


def assert_files_equal(first, second):
    if os.path.getsize(first) != os.path.getsize(second):
        raise AssertionError("Files are not equal: %s, %s" % (first, second))
    first_md5 = md5_checksum(first)
    second_md5 = md5_checksum(second)
    if first_md5 != second_md5:
        raise AssertionError(
            "Files are not equal: %s(md5=%s) != %s(md5=%s)" % (
                first, first_md5, second, second_md5))


def md5_checksum(filename):
    checksum = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            checksum.update(chunk)
    return checksum.hexdigest()


class FileCreator(object):
    def __init__(self):
        self.rootdir = tempfile.mkdtemp()

    def remove_all(self):
        shutil.rmtree(self.rootdir)

    def create_file(self, filename, contents, mtime=None, mode='w'):
        """Creates a file in a tmpdir

        ``filename`` should be a relative path, e.g. "foo/bar/baz.txt"
        It will be translated into a full path in a tmp dir.

        If the ``mtime`` argument is provided, then the file's
        mtime will be set to the provided value (must be an epoch time).
        Otherwise the mtime is left untouched.

        ``mode`` is the mode the file should be opened either as ``w`` or
        `wb``.

        Returns the full path to the file.

        """
        full_path = os.path.join(self.rootdir, filename)
        if not os.path.isdir(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))
        with open(full_path, mode) as f:
            f.write(contents)
        current_time = os.path.getmtime(full_path)
        # Subtract a few years off the last modification date.
        os.utime(full_path, (current_time, current_time - 100000000))
        if mtime is not None:
            os.utime(full_path, (mtime, mtime))
        return full_path

    def create_file_with_size(self, filename, filesize):
        filename = self.create_file(filename, contents='')
        chunksize = 8192
        with open(filename, 'wb') as f:
            for i in range(int(math.ceil(filesize / float(chunksize)))):
                f.write(b'a' * chunksize)
        return filename

    def append_file(self, filename, contents):
        """Append contents to a file

        ``filename`` should be a relative path, e.g. "foo/bar/baz.txt"
        It will be translated into a full path in a tmp dir.

        Returns the full path to the file.
        """
        full_path = os.path.join(self.rootdir, filename)
        if not os.path.isdir(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))
        with open(full_path, 'a') as f:
            f.write(contents)
        return full_path

    def full_path(self, filename):
        """Translate relative path to full path in temp dir.

        f.full_path('foo/bar.txt') -> /tmp/asdfasd/foo/bar.txt
        """
        return os.path.join(self.rootdir, filename)


class TestS3Resource(unittest.TestCase):
    def setUp(self):
        self.region = 'us-west-2'
        self.session = boto3.session.Session(region_name=self.region)
        self.s3 = self.session.resource('s3')
        self.bucket_name = unique_id('boto3-test')

    def create_bucket_resource(self, bucket_name, region=None):
        if region is None:
            region = self.region
        kwargs = {'Bucket': bucket_name}
        if region != 'us-east-1':
            kwargs['CreateBucketConfiguration'] = {
                'LocationConstraint': region
            }
        bucket = self.s3.create_bucket(**kwargs)
        self.addCleanup(bucket.delete)
        return bucket

    def test_s3(self):
        client = self.s3.meta.client

        # Create a bucket (resource action with a resource response)
        bucket = self.create_bucket_resource(self.bucket_name)
        waiter = client.get_waiter('bucket_exists')
        waiter.wait(Bucket=self.bucket_name)

        # Create an object
        obj = bucket.Object('test.txt')
        obj.put(
            Body='hello, world')
        waiter = client.get_waiter('object_exists')
        waiter.wait(Bucket=self.bucket_name, Key='test.txt')
        self.addCleanup(obj.delete)

        # List objects and make sure ours is present
        self.assertIn('test.txt', [o.key for o in bucket.objects.all()])

        # Lazy-loaded attribute
        self.assertEqual(12, obj.content_length)

        # Load a similar attribute from the collection response
        self.assertEqual(12, list(bucket.objects.all())[0].size)

        # Perform a resource action with a low-level response
        self.assertEqual(b'hello, world',
                         obj.get()['Body'].read())

    def test_s3_resource_waiter(self):
        # Create a bucket
        bucket = self.create_bucket_resource(self.bucket_name)
        # Wait till the bucket exists
        bucket.wait_until_exists()
        # Confirm the bucket exists by finding it in a list of all of our
        # buckets
        self.assertIn(self.bucket_name,
                      [b.name for b in self.s3.buckets.all()])

        # Create an object
        obj = bucket.Object('test.txt')
        obj.put(
            Body='hello, world')
        self.addCleanup(obj.delete)

        # Wait till the bucket exists
        obj.wait_until_exists()

        # List objects and make sure ours is present
        self.assertIn('test.txt', [o.key for o in bucket.objects.all()])

    def test_can_create_object_directly(self):
        obj = self.s3.Object(self.bucket_name, 'test.txt')

        self.assertEqual(obj.bucket_name, self.bucket_name)
        self.assertEqual(obj.key, 'test.txt')

    def test_s3_multipart(self):
        # Create the bucket
        bucket = self.create_bucket_resource(self.bucket_name)
        bucket.wait_until_exists()

        # Create the multipart upload
        mpu = bucket.Object('mp-test.txt').initiate_multipart_upload()
        self.addCleanup(mpu.abort)

        # Create and upload a part
        part = mpu.Part(1)
        response = part.upload(Body='hello, world!')

        # Complete the upload, which requires info on all of the parts
        part_info = {
            'Parts': [
                {
                    'PartNumber': 1,
                    'ETag': response['ETag']
                }
            ]
        }

        mpu.complete(MultipartUpload=part_info)
        self.addCleanup(bucket.Object('mp-test.txt').delete)

        contents = bucket.Object('mp-test.txt').get()['Body'].read()
        self.assertEqual(contents, b'hello, world!')


class TestS3Transfers(unittest.TestCase):
    """Tests for the high level boto3.s3.transfer module."""

    @classmethod
    def setUpClass(cls):
        cls.region = 'us-west-2'
        cls.session = boto3.session.Session(region_name=cls.region)
        cls.client = cls.session.client('s3', cls.region)
        cls.bucket_name = 'boto3-integ-transfer-%s-%s' % (
            int(time.time()), random.randint(1, 100))
        cls.client.create_bucket(
            Bucket=cls.bucket_name,
            CreateBucketConfiguration={'LocationConstraint': cls.region})

    def setUp(self):
        self.files = FileCreator()

    def tearDown(self):
        self.files.remove_all()

    @classmethod
    def tearDownClass(cls):
        cls.client.delete_bucket(Bucket=cls.bucket_name)

    def delete_object(self, key):
        self.client.delete_object(
            Bucket=self.bucket_name,
            Key=key)

    def object_exists(self, key):
        self.client.head_object(Bucket=self.bucket_name,
                                Key=key)
        return True

    def create_s3_transfer(self):
        return boto3.s3.transfer.S3Transfer(self.client)

    def test_upload_below_threshold(self):
        transfer = self.create_s3_transfer()
        filename = self.files.create_file_with_size(
            'foo.txt', filesize=1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             'foo.txt')
        self.addCleanup(self.delete_object, 'foo.txt')

        self.assertTrue(self.object_exists('foo.txt'))

    def test_upload_above_threshold(self):
        transfer = self.create_s3_transfer()
        filename = self.files.create_file_with_size(
            '20mb.txt', filesize=20 * 1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             '20mb.txt')
        self.addCleanup(self.delete_object, '20mb.txt')
        self.assertTrue(self.object_exists('20mb.txt'))

    def test_progress_callback_on_upload(self):
        self.amount_seen = 0
        lock = threading.Lock()

        def progress_callback(amount):
            with lock:
                self.amount_seen += amount

        transfer = self.create_s3_transfer()
        filename = self.files.create_file_with_size(
            '20mb.txt', filesize=20 * 1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             '20mb.txt', callback=progress_callback)
        self.addCleanup(self.delete_object, '20mb.txt')

        # The callback should have been called enough times such that
        # the total amount of bytes we've seen (via the "amount"
        # arg to the callback function) should be the size
        # of the file we uploaded.
        self.assertEqual(self.amount_seen, 20 * 1024 * 1024)

    def test_can_send_extra_params_on_upload(self):
        pass

    def test_can_configure_threshold(self):
        config = boto3.s3.transfer.TransferConfig(
            multipart_threshold=6 * 1024 * 1024
        )
        transfer = boto3.s3.transfer.S3Transfer(self.client, config)
        filename = self.files.create_file_with_size(
            'foo.txt', filesize=8 * 1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             'foo.txt')
        self.addCleanup(self.delete_object, 'foo.txt')

        self.assertTrue(self.object_exists('foo.txt'))

    def test_can_send_extra_params_on_download(self):
        transfer = self.create_s3_transfer()
        extra_args = {'ACL': 'public-read'}
        filename = self.files.create_file_with_size(
            'foo.txt', filesize=1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             'foo.txt', extra_args=extra_args)
        self.addCleanup(self.delete_object, 'foo.txt')

        self.assertTrue(self.object_exists('foo.txt'))
        # TODO: Verify we can download the object
        # I'd like to create an anonymous client in boto3, but that doesn't
        # appear possible.

    def test_progress_callback_on_download(self):
        pass

    def test_download_below_threshold(self):
        transfer = self.create_s3_transfer()

        filename = self.files.create_file_with_size(
            'foo.txt', filesize=1024 * 1024)
        with open(filename, 'rb') as f:
            self.client.put_object(Bucket=self.bucket_name,
                                   Key='foo.txt',
                                   Body=f)
            self.addCleanup(self.delete_object, 'foo.txt')

        download_path = os.path.join(self.files.rootdir, 'downloaded.txt')
        transfer.download_file(self.bucket_name, 'foo.txt',
                               download_path)
        assert_files_equal(filename, download_path)

    def test_download_above_threshold(self):
        transfer = self.create_s3_transfer()

        filename = self.files.create_file_with_size(
            'foo.txt', filesize=20 * 1024 * 1024)
        with open(filename, 'rb') as f:
            self.client.put_object(Bucket=self.bucket_name,
                                   Key='foo.txt',
                                   Body=f)
            self.addCleanup(self.delete_object, 'foo.txt')

        download_path = os.path.join(self.files.rootdir, 'downloaded.txt')
        transfer.download_file(self.bucket_name, 'foo.txt',
                               download_path)
        assert_files_equal(filename, download_path)
