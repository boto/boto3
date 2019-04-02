.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


#################
Amazon S3 Buckets
#################

An Amazon S3 bucket is a storage location to hold files. S3 files are referred 
to as objects.

This section describes how to use the AWS SDK for Python to perform common 
operations on S3 buckets.


Create an Amazon S3 Bucket
==========================

The name of an Amazon S3 bucket must be unique across all regions of the AWS 
platform.

.. code-block:: python

    import logging
    import boto3
    from botocore.exceptions import ClientError


    def create_bucket(bucket_name):
    """ Create an Amazon S3 bucket

    :param bucket_name: Unique string name
    :return: True if bucket is created, else False
    """

    s3 = boto3.client('s3')
    try
        s3.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


List Existing Buckets
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

