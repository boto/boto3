.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
##################
Access permissions
##################

This section demonstrates how to manage the access permissions for an S3 
bucket or object by using an access control list (ACL).


Get a bucket access control list
================================

The example retrieves the current access control list of an S3 bucket.
 
.. code-block:: python

    import boto3

    # Retrieve a bucket's ACL
    s3 = boto3.client('s3')
    result = s3.get_bucket_acl(Bucket='my-bucket')
    print(result)
