.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-s3-access-permissions:   

############################################
Managing Amazon S3 Bucket Access Permissions
############################################

This Python example shows you how to get or set the access control list for an Amazon S3 bucket.

The Scenario
============

In this example, a Python code is used to display the bucket access control list (ACL) for a selected 
bucket. The code uses the AWS SDK for Python to manage Amazon S3 bucket access permissions using this 
method of the Amazon S3 client class:

* `get_bucket_acl <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_bucket_acl>`_.

For more information about access control lists for Amazon S3 buckets, see 
`Managing Access with ACLs <http://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html>`_ 
in the *Amazon Simple Storage Service Developer Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite Tasks
==================

To set up and run this example, you must first complete this task:

* Configure your AWS credentials, as described in :doc:`quickstart`.

Get a Specified Bucket Access Control (ACL) List
================================================

Access control lists (ACLs) are one of the resource-based access policy option you can use to manage 
access to your buckets and objects. You can use ACLs to grant basic read/write permissions to other 
AWS accounts.

The example below shows how to:
 
* Get the bucket ACL for a specified bucket using 
  `get_bucket_acl <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_bucket_acl>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call to S3 to retrieve the policy for the given bucket
    result = s3.get_bucket_acl(Bucket='my-bucket')
    print(result)

