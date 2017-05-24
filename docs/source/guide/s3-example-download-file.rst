.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-boto3-s3-download-file:

####################################
Downloading a File from an S3 Bucket
####################################

.. meta::
   :description: Use the AWS SDK for Python (aka Boto) to download a file from an S3 bucket.
   :keywords: download file, s3, bucket

This example shows how to download a file from an S3 bucket, using :py:meth:`S3.Bucket.download_file`.

Prerequisites
=============

To set up and run this example, you must first:

* Configure your AWS credentials, as described in :doc:`quickstart`.
* Create an S3 bucket and upload a file to the bucket.
* Replace the ``BUCKET_NAME`` and ``KEY`` values in the code snippet with the name of your bucket and the key for the uploaded file.

Downloading a File
==================

The example below tries to download an S3 object to a file. If the service returns a 404 error, it prints an error message indicating that the object doesn't exist.

.. code-block:: python

    import boto3
    import botocore

    BUCKET_NAME = 'my-bucket' # replace with your bucket name
    KEY = 'my_image_in_s3.jpg' # replace with your object key

    s3 = boto3.resource('s3')

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
    raise

More Info
=========

* :py:meth:`S3.Bucket.download_file`
* :ref:`s3_guide`
