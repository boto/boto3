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
import os
import tempfile
import shutil
import socket
from tests import unittest
from contextlib import closing

import mock
from botocore.vendored import six
from botocore.client import BaseClient
from concurrent import futures

from boto3.exceptions import RetriesExceededError
from boto3.s3.transfer import ReadFileChunk, StreamReaderProgress
from boto3.s3.transfer import S3Transfer
from boto3.s3.transfer import OSUtils, TransferConfig
from boto3.s3.transfer import MultipartDownloader, MultipartUploader


class InMemoryOSLayer(OSUtils):
    def __init__(self, filemap):
        self._filemap = filemap

    def get_file_size(self, filename):
        return len(self._filemap[filename])

    def open_file_chunk_reader(self, filename, start_byte, size, callback):
        return closing(six.BytesIO(self._filemap[filename]))

    def open(self, filename, mode):
        if 'wb' in mode:
            fileobj = six.BytesIO()
            self._filemap = fileobj
            return closing(fileobj)
        else:
            return closing(self._filemap[filename])


class SequentialExecutor(object):
    def __init__(self, max_workers):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    # The real map() interface actually takes *args, but we specifically do
    # _not_ use this interface.
    def map(self, function, args):
        results = []
        for arg in args:
            results.append(function(arg))
        return results

    def submit(self, function):
        future = futures.Future()
        future.set_result(function())
        return future


class TestOSUtils(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_get_file_size(self):
        with mock.patch('os.path.getsize') as m:
            OSUtils().get_file_size('myfile')
            m.assert_called_with('myfile')

    def test_open_file_chunk_reader(self):
        with mock.patch('boto3.s3.transfer.ReadFileChunk') as m:
            OSUtils().open_file_chunk_reader('myfile', 0, 100, None)
            m.from_filename.assert_called_with('myfile', 0, 100, None)

    def test_open_file(self):
        fileobj = OSUtils().open(os.path.join(self.tempdir, 'foo'), 'w')
        self.assertTrue(hasattr(fileobj, 'write'))


class TestReadFileChunk(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_read_entire_chunk(self):
        filename = os.path.join(self.tempdir, 'foo')
        with open(filename, 'wb') as f:
            f.write(b'onetwothreefourfivesixseveneightnineten')
        chunk = ReadFileChunk.from_filename(
            filename, start_byte=0, chunk_size=3)
        self.assertEqual(chunk.read(), b'one')
        self.assertEqual(chunk.read(), b'')

    def test_read_with_amount_size(self):
        filename = os.path.join(self.tempdir, 'foo')
        with open(filename, 'wb') as f:
            f.write(b'onetwothreefourfivesixseveneightnineten')
        chunk = ReadFileChunk.from_filename(
            filename, start_byte=11, chunk_size=4)
        self.assertEqual(chunk.read(1), b'f')
        self.assertEqual(chunk.read(1), b'o')
        self.assertEqual(chunk.read(1), b'u')
        self.assertEqual(chunk.read(1), b'r')
        self.assertEqual(chunk.read(1), b'')

    def test_reset_stream_emulation(self):
        filename = os.path.join(self.tempdir, 'foo')
        with open(filename, 'wb') as f:
            f.write(b'onetwothreefourfivesixseveneightnineten')
        chunk = ReadFileChunk.from_filename(
            filename, start_byte=11, chunk_size=4)
        self.assertEqual(chunk.read(), b'four')
        chunk.seek(0)
        self.assertEqual(chunk.read(), b'four')

    def test_read_past_end_of_file(self):
        filename = os.path.join(self.tempdir, 'foo')
        with open(filename, 'wb') as f:
            f.write(b'onetwothreefourfivesixseveneightnineten')
        chunk = ReadFileChunk.from_filename(
            filename, start_byte=36, chunk_size=100000)
        self.assertEqual(chunk.read(), b'ten')
        self.assertEqual(chunk.read(), b'')
        self.assertEqual(len(chunk), 3)

    def test_tell_and_seek(self):
        filename = os.path.join(self.tempdir, 'foo')
        with open(filename, 'wb') as f:
            f.write(b'onetwothreefourfivesixseveneightnineten')
        chunk = ReadFileChunk.from_filename(
            filename, start_byte=36, chunk_size=100000)
        self.assertEqual(chunk.tell(), 0)
        self.assertEqual(chunk.read(), b'ten')
        self.assertEqual(chunk.tell(), 3)
        chunk.seek(0)
        self.assertEqual(chunk.tell(), 0)

    def test_callback_is_invoked_on_read(self):
        filename = os.path.join(self.tempdir, 'foo')
        with open(filename, 'wb') as f:
            f.write(b'abc')
        amounts_seen = []
        def callback(amount):
            amounts_seen.append(amount)
        chunk = ReadFileChunk.from_filename(
            filename, start_byte=0, chunk_size=3, callback=callback)
        chunk.read(1)
        chunk.read(1)
        chunk.read(1)

        self.assertEqual(amounts_seen, [1, 1, 1])

    def test_file_chunk_supports_context_manager(self):
        filename = os.path.join(self.tempdir, 'foo')
        with open(filename, 'wb') as f:
            f.write(b'abc')
        with ReadFileChunk.from_filename(filename,
                                         start_byte=0,
                                         chunk_size=2) as chunk:
            val = chunk.read()
            self.assertEqual(val, b'ab')

    def test_iter_is_always_empty(self):
        # This tests the workaround for the httplib bug (see
        # the source for more info).
        filename = os.path.join(self.tempdir, 'foo')
        f = open(filename, 'wb').close()
        chunk = ReadFileChunk.from_filename(
            filename, start_byte=0, chunk_size=10)
        self.assertEqual(list(chunk), [])


class TestStreamReaderProgress(unittest.TestCase):

    def test_proxies_to_wrapped_stream(self):
        original_stream = six.StringIO('foobarbaz')
        wrapped = StreamReaderProgress(original_stream)
        self.assertEqual(wrapped.read(), 'foobarbaz')

    def test_callback_invoked(self):
        amounts_seen = []
        def callback(amount):
            amounts_seen.append(amount)
        original_stream = six.StringIO('foobarbaz')
        wrapped = StreamReaderProgress(original_stream, callback)
        self.assertEqual(wrapped.read(), 'foobarbaz')
        self.assertEqual(amounts_seen, [9])


class TestMultipartUploader(unittest.TestCase):
    def test_multipart_upload_uses_correct_client_calls(self):
        client = mock.Mock()
        uploader = MultipartUploader(client, TransferConfig(),
                                     InMemoryOSLayer({'filename': b'foobar'}), SequentialExecutor)
        client.create_multipart_upload.return_value = {'UploadId': 'upload_id'}
        client.upload_part.return_value = {'ETag': 'first'}

        uploader.upload_file('filename', 'bucket', 'key', None, {})


        # We need to check both the sequence of calls (create/upload/complete)
        # as well as the params passed between the calls, including
        # 1. The upload_id was plumbed through
        # 2. The collected etags were added to the complete call.
        client.create_multipart_upload.assert_called_with(
            Bucket='bucket', Key='key')
        # Should be two parts.
        client.upload_part.assert_called_with(
            Body=mock.ANY, Bucket='bucket',
            UploadId='upload_id', Key='key', PartNumber=1)
        client.complete_multipart_upload.assert_called_with(
            MultipartUpload={'Parts': [{'PartNumber': 1, 'ETag': 'first'}]},
            Bucket='bucket',
            UploadId='upload_id',
            Key='key')


class TestMultipartDownloader(unittest.TestCase):
    def test_multipart_download_uses_correct_client_calls(self):
        client = mock.Mock()
        response_body = b'foobarbaz'
        client.get_object.return_value = {'Body': six.BytesIO(response_body)}


        downloader = MultipartDownloader(client, TransferConfig(),
                                         InMemoryOSLayer({}),
                                         SequentialExecutor)
        downloader.download_file('bucket', 'key', 'filename',
                                 len(response_body), {})

        client.get_object.assert_called_with(
            Range='bytes=0-',
            Bucket='bucket',
            Key='key'
        )

    def test_multipart_download_with_multiple_parts(self):
        client = mock.Mock()
        response_body = b'foobarbaz'
        client.get_object.return_value = {'Body': six.BytesIO(response_body)}
        # For testing purposes, we're testing with a multipart threshold
        # of 4 bytes and a chunksize of 4 bytes.  Given b'foobarbaz',
        # this should result in 3 calls.  In python slices this would be:
        # r[0:4], r[4:8], r[8:9].  But the Range param will be slightly
        # different because they use inclusive ranges.
        config = TransferConfig(multipart_threshold=4,
                                multipart_chunksize=4)

        downloader = MultipartDownloader(client, config,
                                         InMemoryOSLayer({}),
                                         SequentialExecutor)
        downloader.download_file('bucket', 'key', 'filename',
                                 len(response_body), {})

        # We're storing these in **extra because the assertEqual
        # below is really about verifying we have the correct value
        # for the Range param.
        extra = {'Bucket': 'bucket', 'Key': 'key'}
        self.assertEqual(client.get_object.call_args_list,
                         # Note these are inclusive ranges.
                         [mock.call(Range='bytes=0-3', **extra),
                          mock.call(Range='bytes=4-7', **extra),
                          mock.call(Range='bytes=8-', **extra)])

    def test_retry_on_failures_from_stream_reads(self):
        # If we get an exception during a call to the response body's .read()
        # method, we should retry the request.
        pass


class TestS3Transfer(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock()

    def test_upload_below_multipart_threshold_uses_put_object(self):
        below_multipart_threshold = 10
        fake_files = {
            'smallfile': b'foobar',
        }
        osutil = InMemoryOSLayer(fake_files)
        transfer = S3Transfer(self.client, osutil=osutil)
        transfer.upload_file('smallfile', 'bucket', 'key')
        self.client.put_object.assert_called_with(
            Bucket='bucket', Key='key', Body=mock.ANY
        )

    def test_extra_args_on_uploaded_passed_to_api_call(self):
        below_multipart_threshold = 10
        extra_args = {'ACL': 'public-read'}
        fake_files = {
            'smallfile': b'hello world'
        }
        osutil = InMemoryOSLayer(fake_files)
        transfer = S3Transfer(self.client, osutil=osutil)
        transfer.upload_file('smallfile', 'bucket', 'key',
                             extra_args=extra_args)
        self.client.put_object.assert_called_with(
            Bucket='bucket', Key='key', Body=mock.ANY,
            ACL='public-read'
        )

    def test_uses_multipart_upload_when_over_threshold(self):
        with mock.patch('boto3.s3.transfer.MultipartUploader') as uploader:
            fake_files = {
                'smallfile': b'foobar',
            }
            osutil = InMemoryOSLayer(fake_files)
            config = TransferConfig(multipart_threshold=2,
                                    multipart_chunksize=2)
            transfer = S3Transfer(self.client, osutil=osutil, config=config)
            transfer.upload_file('smallfile', 'bucket', 'key')

            uploader.return_value.upload_file.assert_called_with(
                'smallfile', 'bucket', 'key', None, {})

    def test_uses_multipart_download_when_over_threshold(self):
        with mock.patch('boto3.s3.transfer.MultipartDownloader') as downloader:
            osutil = InMemoryOSLayer({})
            over_multipart_threshold = 100 * 1024 * 1024
            transfer = S3Transfer(self.client, osutil=osutil)
            callback = mock.sentinel.CALLBACK
            self.client.head_object.return_value = {
                'ContentLength': over_multipart_threshold,
            }
            transfer.download_file('bucket', 'key', 'filename',
                                   callback=callback)

            downloader.return_value.download_file.assert_called_with(
                'bucket', 'key', 'filename', over_multipart_threshold,
                {}, callback)

    def test_download_file_with_invalid_extra_args(self):
        below_threshold = 20
        osutil = InMemoryOSLayer({})
        transfer = S3Transfer(self.client, osutil=osutil)
        self.client.head_object.return_value = {
            'ContentLength': below_threshold}
        with self.assertRaises(ValueError):
            transfer.download_file('bucket', 'key', '/tmp/smallfile',
                                extra_args={'BadValue': 'foo'})

    def test_download_file_fowards_extra_args(self):
        extra_args = {
            'SSECustomerKey': 'foo',
            'SSECustomerAlgorithm': 'AES256',
        }
        below_threshold = 20
        osutil = InMemoryOSLayer({'smallfile': b'hello world'})
        transfer = S3Transfer(self.client, osutil=osutil)
        self.client.head_object.return_value = {
            'ContentLength': below_threshold}
        self.client.get_object.return_value = {
            'Body': six.BytesIO(b'foobar')
        }
        transfer.download_file('bucket', 'key', '/tmp/smallfile',
                               extra_args=extra_args)

        # Note that we need to invoke the HeadObject call
        # and the PutObject call with the extra_args.
        # This is necessary.  Trying to HeadObject an SSE object
        # will return a 400 if you don't provide the required
        # params.
        self.client.get_object.assert_called_with(
            Bucket='bucket', Key='key', SSECustomerAlgorithm='AES256',
            SSECustomerKey='foo')

    def test_get_object_stream_is_retried_and_succeeds(self):
        below_threshold = 20
        osutil = InMemoryOSLayer({'smallfile': b'hello world'})
        transfer = S3Transfer(self.client, osutil=osutil)
        self.client.head_object.return_value = {
            'ContentLength': below_threshold}
        self.client.get_object.side_effect = [
            # First request fails.
            socket.error("fake error"),
            # Second succeeds.
            {'Body': six.BytesIO(b'foobar')}
        ]
        transfer.download_file('bucket', 'key', '/tmp/smallfile')

        self.assertEqual(self.client.get_object.call_count, 2)

    def test_get_object_stream_uses_all_retries_and_errors_out(self):
        below_threshold = 20
        osutil = InMemoryOSLayer({'smallfile': b'hello world'})
        transfer = S3Transfer(self.client, osutil=osutil)
        self.client.head_object.return_value = {
            'ContentLength': below_threshold}
        # Here we're raising an exception every single time, which
        # will exhaust our retry count and propogate a
        # RetriesExceededError.
        self.client.get_object.side_effect = socket.error("fake error")
        with self.assertRaises(RetriesExceededError):
            transfer.download_file('bucket', 'key', '/tmp/smallfile')

        self.assertEqual(self.client.get_object.call_count, 5)

    def test_download_below_multipart_threshold(self):
        below_threshold = 20
        osutil = InMemoryOSLayer({'smallfile': b'hello world'})
        transfer = S3Transfer(self.client, osutil=osutil)
        self.client.head_object.return_value = {
            'ContentLength': below_threshold}
        self.client.get_object.return_value = {
            'Body': six.BytesIO(b'foobar')
        }
        transfer.download_file('bucket', 'key', '/tmp/smallfile')

        self.client.get_object.assert_called_with(Bucket='bucket', Key='key')

    def test_can_create_with_just_client(self):
        transfer = S3Transfer(client=mock.Mock())
        self.assertIsInstance(transfer, S3Transfer)
