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

import boto3.session

from tests import unittest, unique_id


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
        response = part.upload(b'hello, world!')

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
