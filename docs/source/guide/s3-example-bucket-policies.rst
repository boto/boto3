.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-s3-bucket-policies:   

######################################
Working with Amazon S3 Bucket Policies
######################################

This Python example shows you how to:

* Get the bucket policy of an Amazon S3 bucket.

* Add or update the bucket policy of an Amazon S3 bucket.

* Delete the bucket policy of an Amazon S3 bucket.

The Scenario
============

In this example, Python code is used to get, set, or delete a bucket policy on an Amazon S3 bucket. 
The code uses the AWS SDK for Python to configure policy for a selected Amazon S3 bucket using these 
methods of the Amazon S3 client class:

* `get_bucket_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_bucket_policy>`_.

* `put_bucket_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_policy>`_.

* `delete_bucket_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_bucket_policy>`_

For more information about bucket policies for Amazon S3 buckets, see 
`Using Bucket Policies and User Policies <http://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html>`_ 
in the *Amazon Simple Storage Service Developer Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite Tasks
==================

To set up and run this example, you must first complete this task:

* Configure your AWS credentials, as described in :doc:`quickstart`.

Get the Current Bucket Policy
=============================

The example below shows how to:
 
* Get the bucket ACL for a specified bucket using 
  `get_bucket_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_bucket_policy>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call to S3 to retrieve the policy for the given bucket
    result = s3.get_bucket_policy(Bucket='my-bucket')
    print(result)

    

    
Set a Simple Bucket Policy
==========================

The example below shows how to:
 
* Set the bucket policy for a specified bucket using 
  `put_bucket_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_policy>`_.
 
Example
-------

.. code-block:: python

    import boto3
    import json

    # Create an S3 client
    s3 = boto3.client('s3')

    bucket_name = 'my-bucket'

    # Create the bucket policy
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': "arn:aws:s3:::%s/*" % bucket_name
        }]
    }

    # Convert the policy to a JSON string
    bucket_policy = json.dumps(bucket_policy)

    # Set the new policy on the given bucket
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

 
Delete a Bucket Policy
======================

The example below shows how to:
 
* Delete a bucket policy for a specified bucket using 
  `delete_bucket_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_bucket_policy>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call S3 to delete the policy for the given bucket
    s3.delete_bucket_policy(Bucket='my-bucket')
