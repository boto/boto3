.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-s3-configuring-buckets:   

#############################
Configuring Amazon S3 Buckets
#############################

This Python example shows you how to configure the cross-origin resource sharing (CORS) permissions for a bucket.

The Scenario
============

In this example, Python code is used to list your Amazon S3 buckets and to configure CORS and bucket logging. 
The Python code uses the AWS SDK for Python to configure a selected Amazon S3 bucket using these 
methods of the Amazon S3 client class:

* `get_bucket_cors <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_bucket_cors>`_

* `put_bucket_cors <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_cors>`_.

For more information about using CORS configuration with an Amazon S3 bucket, see 
`Cross-Origin Resource Sharing (CORS) <http://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html>`_ 
in the *Amazon Simple Storage Service Developer Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite Tasks
==================

To set up and run this example, you must first complete this task:

* Configure your AWS credentials, as described in :doc:`quickstart`.

Get a Bucket CORS Configuration
===============================

The example below shows how to:
 
* Get a CORS configuration for a specified bucket using 
  `get_bucket_cors <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_bucket_cors>`_.
 
.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call S3 to get CORS configuration for selected bucket
    result = s3.get_bucket_cors(Bucket='my-bucket')

Set a Bucket CORS Configuration
===============================

The example below shows how to:
 
* Set a CORS configuration for a specified bucket using 
  `put_bucket_cors <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_cors>`_.
 
.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Create the CORS configuration
    cors_configuration = {
        'CORSRules': [{
            'AllowedHeaders': ['Authorization'],
            'AllowedMethods': ['GET', 'PUT'],
            'AllowedOrigins': ['*'],
            'ExposeHeaders': ['GET', 'PUT'],
            'MaxAgeSeconds': 3000
        }]
    }

    # Set the new CORS configuration on the selected bucket
    s3.put_bucket_cors(Bucket='my-bucket', CORSConfiguration=cors_configuration)

