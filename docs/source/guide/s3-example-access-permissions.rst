.. Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
.. SPDX-License-Identifier: Apache-2.0

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
    result = s3.get_bucket_acl(Bucket='amzn-s3-demo-bucket')
    print(result)
