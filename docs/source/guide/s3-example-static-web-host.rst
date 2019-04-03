.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-s3-static-web-host:   

##############################################
Using an Amazon S3 Bucket as a Static Web Host
##############################################

This Python example shows you how to set up an Amazon S3 bucket as a static web host.
The Scenario

In this example, Python code is used to configure any of your buckets to act as a static web host. 
The code uses the AWS SDK for Python to configure a selected Amazon S3 bucket using these methods 
of the Amazon S3 client class:

* `get_bucket_website <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_bucket_website>`_

* `put_bucket_website <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_website>`_

* `delete_bucket_website <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_bucket_website>`_

For more information about using an Amazon S3 bucket as a static web host, see 
`Hosting a Static Website on Amazon S3 <http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html>`_ 
in the *Amazon Simple Storage Service Developer Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite Tasks
==================

To set up and run this example, you must first complete this task:

* Configure your AWS credentials, as described in :doc:`quickstart`.

Get the Current Bucket Website Configuration
=============================================

The example below shows how to:
 
* Get the bucket website configuration using 
  `get_bucket_website <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_bucket_website>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call to S3 to retrieve the policy for the given bucket
    result = s3.get_bucket_website(Bucket='my-bucket')
 
Set a Bucket Website Configuration
==================================

The example below shows how to:
 
* Set a bucket website configuration using 
  `put_bucket_website <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_website>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Create the configuration for the website
    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
    }

    # Set the new policy on the selected bucket
    s3.put_bucket_website(
        Bucket='my-bucket',
        WebsiteConfiguration=website_configuration
    )

 
Delete a Bucket Website Configuration
=====================================

The example below shows how to:
 
* Delete a bucket website configuration using 
  `delete_bucket_website <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_bucket_website>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call S3 to delete the website policy for the given bucket
    s3.delete_bucket_website(Bucket='my-bucket')

 