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
import tempfile
import shutil
import hashlib
import string
import datetime
import logging

from tests import unittest, unique_id
from botocore.compat import six
from botocore.client import Config

import boto3.session
import boto3.s3.transfer


urlopen = six.moves.urllib.request.urlopen
LOG = logging.getLogger('boto3.tests.integration')


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


def random_bucket_name(prefix='boto3-transfer', num_chars=10):
    base = string.ascii_lowercase + string.digits
    random_bytes = bytearray(os.urandom(num_chars))
    return prefix + ''.join([base[b % len(base)] for b in random_bytes])


_SHARED_BUCKET = random_bucket_name()
_DEFAULT_REGION = 'us-west-2'


def setup_module():
    s3 = boto3.client('s3')
    waiter = s3.get_waiter('bucket_exists')
    params = {
        'Bucket': _SHARED_BUCKET,
        'CreateBucketConfiguration': {
            'LocationConstraint': _DEFAULT_REGION,
        }
    }
    try:
        s3.create_bucket(**params)
    except Exception as e:
        # A create_bucket can fail for a number of reasons.
        # We're going to defer to the waiter below to make the
        # final call as to whether or not the bucket exists.
        LOG.debug("create_bucket() raised an exception: %s", e, exc_info=True)
    waiter.wait(Bucket=_SHARED_BUCKET)


def clear_out_bucket(bucket, region, delete_bucket=False):
    s3 = boto3.client('s3', region_name=region)
    page = s3.get_paginator('list_objects')
    # Use pages paired with batch delete_objects().
    for page in page.paginate(Bucket=bucket):
        keys = [{'Key': obj['Key']} for obj in page.get('Contents', [])]
        if keys:
            s3.delete_objects(Bucket=bucket, Delete={'Objects': keys})
    if delete_bucket:
        try:
            s3.delete_bucket(Bucket=bucket)
        except Exception as e:
            # We can sometimes get exceptions when trying to
            # delete a bucket.  We'll let the waiter make
            # the final call as to whether the bucket was able
            # to be deleted.
            LOG.debug("delete_bucket() raised an exception: %s",
                      e, exc_info=True)
            waiter = s3.get_waiter('bucket_not_exists')
            waiter.wait(Bucket=bucket)


def teardown_module():
    clear_out_bucket(_SHARED_BUCKET, _DEFAULT_REGION, delete_bucket=True)


class FileCreator(object):
    def __init__(self):
        self.rootdir = tempfile.mkdtemp()

    def remove_all(self):
        shutil.rmtree(self.rootdir)

    def create_file(self, filename, contents, mode='w'):
        """Creates a file in a tmpdir

        ``filename`` should be a relative path, e.g. "foo/bar/baz.txt"
        It will be translated into a full path in a tmp dir.

        ``mode`` is the mode the file should be opened either as ``w`` or
        `wb``.

        Returns the full path to the file.

        """
        full_path = os.path.join(self.rootdir, filename)
        if not os.path.isdir(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))
        with open(full_path, mode) as f:
            f.write(contents)
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
        self.region = _DEFAULT_REGION
        self.bucket_name = _SHARED_BUCKET
        clear_out_bucket(self.bucket_name, self.region)
        self.session = boto3.session.Session(region_name=self.region)
        self.s3 = self.session.resource('s3')
        self.bucket = self.s3.Bucket(self.bucket_name)

    def create_bucket_resource(self, bucket_name=None, region=None):
        if bucket_name is None:
            bucket_name = random_bucket_name()

        if region is None:
            region = self.region

        kwargs = {'Bucket': bucket_name}

        if region != 'us-east-1':
            kwargs['CreateBucketConfiguration'] = {
                'LocationConstraint': region
            }
        bucket = self.s3.create_bucket(**kwargs)
        self.addCleanup(bucket.delete)

        for _ in range(3):
            bucket.wait_until_exists()
        return bucket

    def test_s3(self):
        client = self.s3.meta.client

        # Create an object
        obj = self.bucket.Object('test.txt')
        obj.put(
            Body='hello, world')
        waiter = client.get_waiter('object_exists')
        waiter.wait(Bucket=self.bucket_name, Key='test.txt')
        self.addCleanup(obj.delete)

        # List objects and make sure ours is present
        self.assertIn('test.txt', [o.key for o in self.bucket.objects.all()])

        # Lazy-loaded attribute
        self.assertEqual(12, obj.content_length)

        # Load a similar attribute from the collection response
        self.assertEqual(12, list(self.bucket.objects.all())[0].size)

        # Perform a resource action with a low-level response
        self.assertEqual(b'hello, world',
                         obj.get()['Body'].read())

    def test_s3_resource_waiter(self):
        # Create a bucket
        bucket_name = random_bucket_name()
        bucket = self.create_bucket_resource(bucket_name)
        # Wait till the bucket exists
        bucket.wait_until_exists()
        # Confirm the bucket exists by finding it in a list of all of our
        # buckets
        self.assertIn(bucket_name,
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
        # Create the multipart upload
        mpu = self.bucket.Object('mp-test.txt').initiate_multipart_upload()
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
        self.addCleanup(self.bucket.Object('mp-test.txt').delete)

        contents = self.bucket.Object('mp-test.txt').get()['Body'].read()
        self.assertEqual(contents, b'hello, world!')

    def test_s3_batch_delete(self):
        bucket = self.create_bucket_resource()
        bucket.Versioning().enable()

        # Create several versions of an object
        obj = self.bucket.Object('test.txt')
        for i in range(10):
            obj.put(Body="Version %s" % i)

        # Delete all the versions of the object
            bucket.object_versions.all().delete()

        versions = list(bucket.object_versions.all())
        self.assertEqual(len(versions), 0)


class TestS3Transfers(unittest.TestCase):
    """Tests for the high level boto3.s3.transfer module."""
    def setUp(self):
        self.region = _DEFAULT_REGION
        self.bucket_name = _SHARED_BUCKET
        clear_out_bucket(self.bucket_name, self.region)
        self.session = boto3.session.Session(region_name=self.region)
        self.client = self.session.client('s3', self.region)
        self.files = FileCreator()
        self.progress = 0

    def tearDown(self):
        self.files.remove_all()

    def delete_object(self, key):
        self.client.delete_object(
            Bucket=self.bucket_name,
            Key=key)

    def object_exists(self, key):
        waiter = self.client.get_waiter('object_exists')
        waiter.wait(Bucket=self.bucket_name, Key=key)
        return True

    def wait_until_object_exists(self, key_name, extra_params=None,
                                 min_successes=3):
        waiter = self.client.get_waiter('object_exists')
        params = {'Bucket': self.bucket_name, 'Key': key_name}
        if extra_params is not None:
            params.update(extra_params)
        for _ in range(min_successes):
            waiter.wait(**params)

    def create_s3_transfer(self, config=None):
        return boto3.s3.transfer.S3Transfer(self.client,
                                            config=config)

    def assert_has_public_read_acl(self, response):
        grants = response['Grants']
        public_read = [g['Grantee'].get('URI', '') for g in grants
                       if g['Permission'] == 'READ']
        self.assertIn('groups/global/AllUsers', public_read[0])

    def test_copy(self):
        self.client.put_object(
            Bucket=self.bucket_name, Key='foo', Body='beach')
        self.addCleanup(self.delete_object, 'foo')

        self.client.copy(
            CopySource={'Bucket': self.bucket_name, 'Key': 'foo'},
            Bucket=self.bucket_name, Key='bar'
        )
        self.addCleanup(self.delete_object, 'bar')

        self.object_exists('bar')

    def test_upload_fileobj(self):
        fileobj = six.BytesIO(b'foo')
        self.client.upload_fileobj(
            Fileobj=fileobj, Bucket=self.bucket_name, Key='foo')
        self.addCleanup(self.delete_object, 'foo')

        self.object_exists('foo')

    def test_upload_fileobj_progress(self):
        # This has to be an integration test because the fileobj will never
        # actually be read from when using the stubber and therefore the
        # progress callbacks will not be invoked.
        chunksize = 5 * (1024 ** 2)
        config = boto3.s3.transfer.TransferConfig(
            multipart_chunksize=chunksize,
            multipart_threshold=chunksize,
            max_concurrency=1
        )
        fileobj = six.BytesIO(b'0' * (chunksize * 3))

        def progress_callback(amount):
            self.progress += amount

        self.client.upload_fileobj(
            Fileobj=fileobj, Bucket=self.bucket_name, Key='foo',
            Config=config, Callback=progress_callback)
        self.addCleanup(self.delete_object, 'foo')

        self.object_exists('foo')
        self.assertEqual(self.progress, chunksize * 3)

    def test_download_fileobj(self):
        fileobj = six.BytesIO()
        self.client.put_object(
            Bucket=self.bucket_name, Key='foo', Body=b'beach')
        self.addCleanup(self.delete_object, 'foo')

        self.wait_until_object_exists('foo')
        self.client.download_fileobj(
            Bucket=self.bucket_name, Key='foo', Fileobj=fileobj)

        self.assertEqual(fileobj.getvalue(), b'beach')

    def test_upload_below_threshold(self):
        config = boto3.s3.transfer.TransferConfig(
            multipart_threshold=2 * 1024 * 1024)
        transfer = self.create_s3_transfer(config)
        filename = self.files.create_file_with_size(
            'foo.txt', filesize=1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             'foo.txt')
        self.addCleanup(self.delete_object, 'foo.txt')

        self.assertTrue(self.object_exists('foo.txt'))

    def test_upload_above_threshold(self):
        config = boto3.s3.transfer.TransferConfig(
            multipart_threshold=2 * 1024 * 1024)
        transfer = self.create_s3_transfer(config)
        filename = self.files.create_file_with_size(
            '20mb.txt', filesize=20 * 1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             '20mb.txt')
        self.addCleanup(self.delete_object, '20mb.txt')
        self.assertTrue(self.object_exists('20mb.txt'))

    def test_upload_file_above_threshold_with_acl(self):
        config = boto3.s3.transfer.TransferConfig(
            multipart_threshold=5 * 1024 * 1024)
        transfer = self.create_s3_transfer(config)
        filename = self.files.create_file_with_size(
            '6mb.txt', filesize=6 * 1024 * 1024)
        extra_args = {'ACL': 'public-read'}
        transfer.upload_file(filename, self.bucket_name,
                             '6mb.txt', extra_args=extra_args)
        self.addCleanup(self.delete_object, '6mb.txt')

        self.assertTrue(self.object_exists('6mb.txt'))
        response = self.client.get_object_acl(
            Bucket=self.bucket_name, Key='6mb.txt')
        self.assert_has_public_read_acl(response)

    def test_upload_file_above_threshold_with_ssec(self):
        key_bytes = os.urandom(32)
        extra_args = {
            'SSECustomerKey': key_bytes,
            'SSECustomerAlgorithm': 'AES256',
        }
        config = boto3.s3.transfer.TransferConfig(
            multipart_threshold=5 * 1024 * 1024)
        transfer = self.create_s3_transfer(config)
        filename = self.files.create_file_with_size(
            '6mb.txt', filesize=6 * 1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             '6mb.txt', extra_args=extra_args)
        self.addCleanup(self.delete_object, '6mb.txt')
        # A head object will fail if it has a customer key
        # associated with it and it's not provided in the HeadObject
        # request so we can use this to verify our functionality.
        response = self.client.head_object(
            Bucket=self.bucket_name,
            Key='6mb.txt', **extra_args)
        self.assertEqual(response['SSECustomerAlgorithm'], 'AES256')

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

    def test_callback_called_once_with_sigv4(self):
        # Verify #98, where the callback was being invoked
        # twice when using signature version 4.
        self.amount_seen = 0
        lock = threading.Lock()
        def progress_callback(amount):
            with lock:
                self.amount_seen += amount

        client = self.session.client(
            's3', self.region,
            config=Config(signature_version='s3v4'))
        transfer = boto3.s3.transfer.S3Transfer(client)
        filename = self.files.create_file_with_size(
            '10mb.txt', filesize=10 * 1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             '10mb.txt', callback=progress_callback)
        self.addCleanup(self.delete_object, '10mb.txt')

        self.assertEqual(self.amount_seen, 10 * 1024 * 1024)

    def test_can_send_extra_params_on_upload(self):
        transfer = self.create_s3_transfer()
        filename = self.files.create_file_with_size('foo.txt', filesize=1024)
        transfer.upload_file(filename, self.bucket_name,
                             'foo.txt', extra_args={'ACL': 'public-read'})
        self.addCleanup(self.delete_object, 'foo.txt')

        response = self.client.get_object_acl(
            Bucket=self.bucket_name, Key='foo.txt')
        self.assert_has_public_read_acl(response)

    def test_can_configure_threshold(self):
        config = boto3.s3.transfer.TransferConfig(
            multipart_threshold=6 * 1024 * 1024
        )
        transfer = self.create_s3_transfer(config)
        filename = self.files.create_file_with_size(
            'foo.txt', filesize=8 * 1024 * 1024)
        transfer.upload_file(filename, self.bucket_name,
                             'foo.txt')
        self.addCleanup(self.delete_object, 'foo.txt')

        self.assertTrue(self.object_exists('foo.txt'))

    def test_can_send_extra_params_on_download(self):
        # We're picking the customer provided sse feature
        # of S3 to test the extra_args functionality of
        # S3.
        key_bytes = os.urandom(32)
        extra_args = {
            'SSECustomerKey': key_bytes,
            'SSECustomerAlgorithm': 'AES256',
        }
        self.client.put_object(Bucket=self.bucket_name,
                               Key='foo.txt',
                               Body=b'hello world',
                               **extra_args)
        self.addCleanup(self.delete_object, 'foo.txt')
        transfer = self.create_s3_transfer()

        download_path = os.path.join(self.files.rootdir, 'downloaded.txt')
        self.wait_until_object_exists('foo.txt', extra_params=extra_args)
        transfer.download_file(self.bucket_name, 'foo.txt',
                               download_path, extra_args=extra_args)
        with open(download_path, 'rb') as f:
            self.assertEqual(f.read(), b'hello world')

    def test_progress_callback_on_download(self):
        self.amount_seen = 0
        lock = threading.Lock()

        def progress_callback(amount):
            with lock:
                self.amount_seen += amount

        transfer = self.create_s3_transfer()
        filename = self.files.create_file_with_size(
            '20mb.txt', filesize=20 * 1024 * 1024)
        with open(filename, 'rb') as f:
            self.client.put_object(Bucket=self.bucket_name,
                                   Key='20mb.txt', Body=f)
        self.addCleanup(self.delete_object, '20mb.txt')

        download_path = os.path.join(self.files.rootdir, 'downloaded.txt')
        transfer.download_file(self.bucket_name, '20mb.txt',
                               download_path, callback=progress_callback)

        self.assertEqual(self.amount_seen, 20 * 1024 * 1024)

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
        self.wait_until_object_exists('foo.txt')
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
        self.wait_until_object_exists('foo.txt')
        transfer.download_file(self.bucket_name, 'foo.txt',
                               download_path)
        assert_files_equal(filename, download_path)

    def test_download_file_with_directory_not_exist(self):
        transfer = self.create_s3_transfer()
        self.client.put_object(Bucket=self.bucket_name,
                                Key='foo.txt',
                                Body=b'foo')
        self.addCleanup(self.delete_object, 'foo.txt')
        download_path = os.path.join(self.files.rootdir, 'a', 'b', 'c',
                                     'downloaded.txt')
        self.wait_until_object_exists('foo.txt')
        with self.assertRaises(IOError):
            transfer.download_file(self.bucket_name, 'foo.txt', download_path)

    def test_download_large_file_directory_not_exist(self):
        transfer = self.create_s3_transfer()

        filename = self.files.create_file_with_size(
            'foo.txt', filesize=20 * 1024 * 1024)
        with open(filename, 'rb') as f:
            self.client.put_object(Bucket=self.bucket_name,
                                   Key='foo.txt',
                                   Body=f)
            self.addCleanup(self.delete_object, 'foo.txt')
        download_path = os.path.join(self.files.rootdir, 'a', 'b', 'c',
                                     'downloaded.txt')
        self.wait_until_object_exists('foo.txt')
        with self.assertRaises(IOError):
            transfer.download_file(self.bucket_name, 'foo.txt', download_path)

    def test_transfer_methods_through_client(self):
        # This is really just a sanity check to ensure that the interface
        # from the clients work.  We're not exhaustively testing through
        # this client interface.
        filename = self.files.create_file_with_size(
            'foo.txt', filesize=1024 * 1024)
        self.client.upload_file(Filename=filename,
                                Bucket=self.bucket_name,
                                Key='foo.txt')
        self.addCleanup(self.delete_object, 'foo.txt')

        download_path = os.path.join(self.files.rootdir, 'downloaded.txt')
        self.wait_until_object_exists('foo.txt')
        self.client.download_file(Bucket=self.bucket_name,
                                  Key='foo.txt',
                                  Filename=download_path)
        assert_files_equal(filename, download_path)

    def test_transfer_methods_do_not_use_threads(self):
        # This is just a smoke test to make sure that
        # setting use_threads to False has no issues transferring files as
        # the non-threaded implementation is ran under the same integration
        # and functional tests in s3transfer as the normal threaded
        # implementation
        #
        # The methods used are arbitrary other than one of the methods
        # use ``boto3.s3.transfer.S3Transfer`` and the other should be
        # using ``s3transfer.manager.TransferManager`` directly
        content = b'my content'
        filename = self.files.create_file('myfile', content.decode('utf-8'))
        key = 'foo'
        config = boto3.s3.transfer.TransferConfig(use_threads=False)

        self.client.upload_file(
            Bucket=self.bucket_name, Key=key, Filename=filename,
            Config=config)
        self.addCleanup(self.delete_object, key)
        self.assertTrue(self.object_exists(key))

        fileobj = six.BytesIO()
        self.client.download_fileobj(
            Bucket=self.bucket_name, Key='foo', Fileobj=fileobj, Config=config)
        self.assertEqual(fileobj.getvalue(), content)

    def test_transfer_methods_through_bucket(self):
        # This is just a sanity check to ensure that the bucket interface work.
        key = 'bucket.txt'
        bucket = self.session.resource('s3').Bucket(self.bucket_name)
        filename = self.files.create_file_with_size(key, 1024*1024)
        bucket.upload_file(Filename=filename, Key=key)
        self.addCleanup(self.delete_object, key)
        download_path = os.path.join(self.files.rootdir, unique_id('foo'))
        bucket.download_file(Key=key, Filename=download_path)
        assert_files_equal(filename, download_path)

    def test_transfer_methods_through_object(self):
        # This is just a sanity check to ensure that the object interface work.
        key = 'object.txt'
        obj = self.session.resource('s3').Object(self.bucket_name, key)
        filename = self.files.create_file_with_size(key, 1024*1024)
        obj.upload_file(Filename=filename)
        self.addCleanup(self.delete_object, key)
        download_path = os.path.join(self.files.rootdir, unique_id('foo'))
        obj.download_file(Filename=download_path)
        assert_files_equal(filename, download_path)


class TestCustomS3BucketLoad(unittest.TestCase):
    def setUp(self):
        self.region = _DEFAULT_REGION
        self.bucket_name = _SHARED_BUCKET
        clear_out_bucket(self.bucket_name, self.region)
        self.session = boto3.session.Session(region_name=self.region)
        self.s3 = self.session.resource('s3')

    def test_can_access_buckets_creation_date(self):
        bucket = self.s3.Bucket(self.bucket_name)
        self.assertIsInstance(bucket.creation_date, datetime.datetime)
