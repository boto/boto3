.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto-ec2-example-key-pairs:

#################################
Working with Amazon EC2 key pairs
#################################

This Python example shows you how to:

* Get information about your key pairs

* Create a key pair to access an Amazon EC2 instance

* Delete an existing key pair

The scenario
============

Amazon EC2 uses public–key cryptography to encrypt and decrypt login information. Public–key cryptography 
uses a public key to encrypt data, then the recipient uses the private key to decrypt the data. The 
public and private keys are known as a key pair.

In this example, Python code is used to perform several Amazon EC2 key pair management 
operations. The code uses the AWS SDK for Python to manage IAM access keys using these methods of the EC2 client class:

* `describe_key_pairs <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_key_pairs>`_.

* `create_key_pair <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_key_pair>`_.

* `delete_key_pair <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_key_pair>`_.

For more information about the Amazon EC2 key pairs, see `Amazon EC2 Key Pairs <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`_ 
in the *Amazon EC2 User Guide for Linux Instances* 
or `Amazon EC2 Key Pairs and Windows Instances <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-key-pairs.html>`_
in the *Amazon EC2 User Guide for Windows Instances*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.
    
Describe key pairs
==================

Describe one or more of your key pairs.

The example below shows how to:
 
* Describe keypairs using 
  `describe_key_pairs <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_key_pairs>`_.
 
Example
-------

.. code-block:: python

    import boto3
    
    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()
    print(response)


Create a key pair
=================

Create a 2048-bit RSA key pair with the specified name. Amazon EC2 stores the public key and displays 
the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded 
PKCS#8 private key. If a key with the specified name already exists, Amazon EC2 returns an error.

The example below shows how to:
 
* Create a 2048-bit RSA key pair with a specified name using 
  `create_key_pair <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_key_pair>`_.
  
Example
-------

.. code-block:: python

    import boto3
    
    ec2 = boto3.client('ec2')
    response = ec2.create_key_pair(KeyName='KEY_PAIR_NAME')
    print(response)


Delete a key pair
=================

Delete the specified key pair, by removing the public key from Amazon EC2.

The example below shows how to:
 
* Delete a key pair by removing the public key from Amazon EC2 using 
  `delete_key_pair <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_key_pair>`_.
 
Example
-------

.. code-block:: python

    import boto3

    ec2 = boto3.client('ec2')
    response = ec2.delete_key_pair(KeyName='KEY_PAIR_NAME')
    print(response)

    