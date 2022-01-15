.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


##############################################
Using an Amazon S3 bucket as a static web host
##############################################

An S3 bucket can be configured to host a static website.


Retrieve a website configuration
================================

Retrieve a bucket's website configuration by calling the AWS SDK for Python 
``get_bucket_website`` method.

.. code-block:: python

    import boto3

    # Retrieve the website configuration
    s3 = boto3.client('s3')
    result = s3.get_bucket_website(Bucket='BUCKET_NAME')
 

Set a website configuration
===========================

A bucket's website configuration can be set by calling the 
``put_bucket_website`` method.


.. code-block:: python

    # Define the website configuration
    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
    }

    # Set the website configuration
    s3 = boto3.client('s3')
    s3.put_bucket_website(Bucket='BUCKET_NAME',
                          WebsiteConfiguration=website_configuration)


Delete a website configuration
==============================

A bucket's website configuration can be deleted by calling the 
``delete_bucket_website`` method.

.. code-block:: python

    # Delete the website configuration
    s3 = boto3.client('s3')
    s3.delete_bucket_website(Bucket='BUCKET_NAME')
