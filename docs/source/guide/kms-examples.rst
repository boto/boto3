.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

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
