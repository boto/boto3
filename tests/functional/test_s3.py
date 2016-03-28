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


class TestS3MethodInjection(unittest.TestCase):
    def test_transfer_methods_injected_to_client(self):
        session = boto3.session.Session(region_name='us-west-2')
        client = session.client('s3')
        self.assertTrue(hasattr(client, 'upload_file'),
                        'upload_file was not injected onto S3 client')
        self.assertTrue(hasattr(client, 'download_file'),
                        'download_file was not injected onto S3 client')

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

    def test_transfer_methods_injected_to_object(self):
        obj = boto3.resource('s3').Object('my_bucket', 'my_key')
        self.assertTrue(hasattr(obj, 'upload_file'),
                        'upload_file was not injected onto S3 object')
        self.assertTrue(hasattr(obj, 'download_file'),
                        'download_file was not injected onto S3 object')


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
