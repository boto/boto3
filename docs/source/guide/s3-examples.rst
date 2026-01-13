.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-boto3-s3-examples:

##################
Amazon S3 examples
##################

.. meta::
   :description:
   :keywords: s3 python

Amazon Simple Storage Service (Amazon S3) is an object storage service that 
offers scalability, data availability, security, and performance.

This section demonstrates how to use the AWS SDK for Python to access Amazon S3 
services.

.. note::
   Boto3 clients and resources have an option to use a custom endpoint using the ``endpoint_url`` parameter as shown in the `Session Reference <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html>`_ guide.
   This overrides the default endpoint the client or resource will use.
   Use caution when configuring this parameter as it can cause unintended behavior including S3 redirect issues.
   See `Service-specific endpoints <https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html>`_ page in the *AWS SDK reference guide* for more information.

**Examples**

.. toctree::
   :maxdepth: 1

   s3-example-creating-buckets
   s3-uploading-files
   s3-example-download-file
   s3
   s3-presigned-urls
   s3-example-bucket-policies
   s3-example-access-permissions
   s3-example-static-web-host
   s3-example-configuring-buckets
   s3-example-mrap
   s3-example-privatelink
