.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


#################
Amazon S3 buckets
#################

An Amazon S3 bucket is a storage location to hold files. S3 files are referred 
to as objects.

This section describes how to use the AWS SDK for Python to perform common 
operations on S3 buckets.


Create an Amazon S3 bucket
==========================

The name of an Amazon S3 bucket must be unique across all regions of the AWS 
platform. The bucket can be located in a specific region to minimize latency
or to address regulatory requirements.

.. note::
    The ``LocationConstraint`` value is used to specify the region where a bucket
    will be created. S3 requires ``LocationConstraint`` to be specified when creating
    buckets using a client in regions other than ``us-east-1``. When no region is
    specified, ``us-east-1`` is used by default. The example below ensures the S3
    client is created in the same region as the bucket to avoid a
    ``IllegalLocationConstraintException`` error.

.. code-block:: python

    import logging
    import boto3
    from botocore.exceptions import ClientError


    def create_bucket(bucket_name, region='us-east-1'):
        """Create an S3 bucket in a specified region

        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else False
        """

        # Create bucket
        try:
            bucket_config = {}
            s3_client = boto3.client('s3', region_name=region)
            if region != 'us-east-1':
                bucket_config['CreateBucketConfiguration'] = {'LocationConstraint': region}

            s3_client.create_bucket(Bucket=bucket_name, **bucket_config)
        except ClientError as e:
            logging.error(e)
            return False
        return True

List existing buckets
=====================

List all the existing buckets for the AWS account.

.. code-block:: python

    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
