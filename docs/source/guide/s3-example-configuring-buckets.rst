.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


#########################
Bucket CORS configuration
#########################

Cross Origin Resource Sharing (CORS) enables client web applications in one 
domain to access resources in another domain. An S3 bucket can be configured 
to enable cross-origin requests. The configuration defines rules that specify 
the allowed origins, HTTP methods (GET, PUT, etc.), and other elements.


Retrieve a bucket CORS configuration
====================================

Retrieve a bucket's CORS configuration by calling the AWS SDK for Python 
``get_bucket_cors`` method.

.. code-block:: python

    import logging
    import boto3
    from botocore.exceptions import ClientError


    def get_bucket_cors(bucket_name):
        """Retrieve the CORS configuration rules of an Amazon S3 bucket

        :param bucket_name: string
        :return: List of the bucket's CORS configuration rules. If no CORS
        configuration exists, return empty list. If error, return None.
        """

        # Retrieve the CORS configuration
        s3 = boto3.client('s3')
        try:
            response = s3.get_bucket_cors(Bucket=bucket_name)
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchCORSConfiguration':
                return []
            else:
                # AllAccessDisabled error == bucket not found
                logging.error(e)
                return None
        return response['CORSRules']


Set a bucket CORS configuration
===============================

A bucket's CORS configuration can be set by calling the ``put_bucket_cors`` 
method.

.. code-block:: python

    # Define the configuration rules
    cors_configuration = {
        'CORSRules': [{
            'AllowedHeaders': ['Authorization'],
            'AllowedMethods': ['GET', 'PUT'],
            'AllowedOrigins': ['*'],
            'ExposeHeaders': ['GET', 'PUT'],
            'MaxAgeSeconds': 3000
        }]
    }

    # Set the CORS configuration
    s3 = boto3.client('s3')
    s3.put_bucket_cors(Bucket='BUCKET_NAME',
                       CORSConfiguration=cors_configuration)
