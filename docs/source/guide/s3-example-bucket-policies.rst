.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


###############
Bucket policies
###############

An S3 bucket can have an optional policy that grants access permissions to 
other AWS accounts or AWS Identity and Access Management (IAM) users. Bucket 
policies are defined using the same JSON format as a resource-based IAM policy.


Retrieve a bucket policy
========================

Retrieve a bucket's policy by calling the AWS SDK for Python 
``get_bucket_policy`` method. The method accepts a parameter that specifies 
the bucket name.

.. code-block:: python

    import boto3

    # Retrieve the policy of the specified bucket
    s3 = boto3.client('s3')
    result = s3.get_bucket_policy(Bucket='BUCKET_NAME')
    print(result['Policy'])


Set a bucket policy
===================

A bucket's policy can be set by calling the ``put_bucket_policy`` method.

The policy is defined in the same JSON format as an IAM policy. The policy 
defined in the example below enables any user to retrieve any object 
stored in the bucket identified by the ``bucket_name`` variable.


.. code-block:: python

    import json

    # Create a bucket policy
    bucket_name = 'BUCKET_NAME'
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
    }

    # Convert the policy from JSON dict to string
    bucket_policy = json.dumps(bucket_policy)

    # Set the new policy
    s3 = boto3.client('s3')
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)


Delete a bucket policy
======================

A bucket's policy can be deleted by calling the ``delete_bucket_policy`` method.

.. code-block:: python

    # Delete a bucket's policy
    s3 = boto3.client('s3')
    s3.delete_bucket_policy(Bucket='BUCKET_NAME')
