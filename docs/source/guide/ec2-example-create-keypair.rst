.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-create-keypair:   

################
Create a Keypair
################

Creates a 2048-bit RSA key pair with the specified name. Amazon EC2 stores the public key and displays 
the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded 
PKCS#8 private key. If a key with the specified name already exists, Amazon EC2 returns an error.

The example below shows how to:
 
* Create a 2048-bit RSA key pair with a specified name using 
  `create_key_pair <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.create_key_pair>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Create an RSA Keypair
---------------------------------------------------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError


    ec2 = boto3.client('ec2')
    response = ec2.create_key_pair(KeyName='KEY_PAIR_NAME')
    print(response)
