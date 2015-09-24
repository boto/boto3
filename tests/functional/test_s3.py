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
