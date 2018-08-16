.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-s3-creating-buckets:   

####################################
Creating and Using Amazon S3 Buckets
####################################

This Python example shows you how to:

* Obtain and display a list of Amazon S3 buckets in your account.

* Create an Amazon S3 bucket.

* Upload an object to a specified bucket.

The Scenario
============

In this example, Python code is used to obtain a list of existing Amazon S3 buckets, create a bucket, 
and upload a file to a specified bucket. The code uses the AWS SDK for Python to get information from 
and upload files to an Amazon S3 bucket using these methods of the Amazon S3 client class:

* `list_buckets <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets>`_

* `create_bucket <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket>`_

* `upload_file <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_file>`_

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite Tasks
==================

To set up and run this example, you must first complete this task:

* Configure your AWS credentials, as described in :doc:`quickstart`.

Display a List of Amazon S3 Buckets
===================================

List all the buckets owned by the authenticated sender of the request.

The example below shows how to:
 
* List buckets using 
  `list_buckets <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets>`_.
 

Example
-------

.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call S3 to list current buckets
    response = s3.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list
    print("Bucket List: %s" % buckets)
    

Create an Amazon S3 Bucket
==========================

The example below shows how to:
 
* Create a new bucket using 
  `create_bucket <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket>`_.
 

Example
-------

.. code-block:: python

    import boto3

    s3 = boto3.client('s3')
    s3.create_bucket(Bucket='my-bucket')

    
Upload a File to an Amazon S3 Bucket
====================================

The example below shows how to:
 
* Upload a file to a bucket using 
  `upload_file <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_file>`_.
 

Example
-------

.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    filename = 'file.txt'
    bucket_name = 'my-bucket'

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(filename, bucket_name, filename)
    