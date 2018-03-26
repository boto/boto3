.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-boto-kms-example-re-encrypt-data:

#########################
Re-encrypting a Data Blob
#########################

The following example uses the AWS SDK for Python
`re_encrypt <https://boto3.readthedocs.io/en/latest/reference/services/kms.html#KMS.Client.re_encrypt>`_ method,
which implements the
`ReEncrypt <http://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html>`_ operation,
to decrypt encrypted data and then immediately re-encrypt data under a new customer master key (CMK).
The operations are performed entirely on the server side within AWS KMS,
so they never expose your plaintext outside of AWS KMS.
The example displays a readable version of the resulting re-encrypted blob.

.. code-block:: python

   import boto3

   blob = '\x01\x02\x02\...'

   # Replace the fictitious key ARN with a valid key ID

   destinationKeyId = 'arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321'

   client = boto3.client('kms')

   response = client.re_encrypt(
       CiphertextBlob=blob,
       DestinationKeyId=destinationKeyId,
   )

   print(response)

Choose :code:`Copy` to save the code locally.
See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/python/example_code/kms/kms-python-example-re-encrypt-data.py>`_
on GitHub.
