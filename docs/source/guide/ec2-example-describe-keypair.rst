.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-describe-keypairs:   

#################
Describe Keypairs
#################

Amazon EC2 uses public–key cryptography to encrypt and decrypt login information. Public–key 
cryptography uses a public key to encrypt a piece of data, such as a password, then the recipient 
uses the private key to decrypt the data. The public and private keys are known as a key pair. 

The example below shows how to:
 
* Describe keypairs using 
  `describe_key_pairs <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_key_pairs>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Describe Keypairs
-----------------------------------------------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError


    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()
    print(response)
