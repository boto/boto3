.. Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
.. SPDX-License-Identifier: Apache-2.0

.. _aws-boto3-kms-examples:

#############################################
AWS Key Management Service (AWS KMS) examples
#############################################

.. meta::
   :description: Python examples that use the AWS Key Management Service (AWS KMS)
   :keywords: KMS

Encrypting valuable data is a common security practice. The encryption process 
typically uses one or more keys, sometimes referred to as data keys and master 
keys. A data key is used to encrypt the data. A master key manages one or 
more data keys. To prevent the data from being decrypted by unauthorized 
users, both keys must be protected, often by being encrypted themselves. 
The AWS Key Management Service (AWS KMS) can assist in this key management.

**Examples**

.. toctree::
   :maxdepth: 1

   kms-example-encrypt-decrypt-file
