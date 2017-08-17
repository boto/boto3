.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-boto-kms-example-create-key:

##############
Creating a CMK
##############

The following example uses the AWS SDK for Python
`create_key <https://boto3.readthedocs.io/en/latest/reference/services/kms.html#KMS.Client.create_key>`_
method,
which implements the
`CreateKey <http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`_ operation,
to create a customer master key (CMK).
Since the example only encrypts a small amount of data,
a CMK is fine for our purposes.
For larger amounts of data,
use the CMK to encrypt a data encryption key (DEK).

Example
-------

.. code-block:: python

   import boto3

   client = boto3.client('kms')

   response = client.create_key()

   print(response['KeyMetadata']['Arn'])

Choose :code:`Copy` to save the code locally.
See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/python/example_code/kms/kms-python-example-create-key.py>`_
on GitHub.
