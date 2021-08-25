.. Copyright 2010-2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

##################
AWS PrivateLink for Amazon S3
##################

This section demonstrates how to configure an S3 client to use an interface
VPC endpoint.


Configuring the client endpoint URL
================================

When configuring an S3 client to use an interface VPC endpoint it's important
to note that only the resource type specified in the endpoint can be addressed
using that client. Accessing both buckets and access points requires
instantiating two clients, one for each resource type.

The following example configures an S3 client to access S3 buckets via an
interface VPC endpoint. This client cannot be used to address S3 access points.

.. code-block:: python

    import boto3

    s3_client = boto3.client(
        service_name='s3',
        endpoint_url='https://bucket.vpce-abc123-abcdefgh.s3.us-east-1.vpce.amazonaws.com'
    )

The following example configures an S3 client to access S3 access points via an
interface VPC endpoint. This client cannot be used to address S3 buckets.

.. code-block:: python

    import boto3

    s3_client = boto3.client(
        service_name='s3',
        endpoint_url='https://accesspoint.vpce-abc123-abcdefgh.s3.us-east-1.vpce.amazonaws.com'
    )

The following example configures an S3 Control client to use an interface VPC
endpoint.

.. code-block:: python

    import boto3

    control_client = boto3.client(
        service_name='s3control',
        endpoint_url='https://control.vpce-abc123-abcdefgh.s3.us-east-1.vpce.amazonaws.com'
    )
