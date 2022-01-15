.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-secrets-manager:   

###################
AWS Secrets Manager
###################

This Python example shows you how to retrieve the decrypted secret value from an AWS Secrets Manager secret. The secret could be created using either the Secrets Manager console or the CLI/SDK. 

The code uses the AWS SDK for Python to retrieve a decrypted secret value.

For more information about using an Amazon Secrets Manager, see 
`Tutorial: Storing and Retrieving a Secret <https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html>`_ 
in the *AWS Secrets Manager Developer Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
==================

To set up and run this example, you must first set up the following:

* Configure your AWS credentials, as described in :doc:`quickstart`.
* Create a secret with the AWS Secrets Manager, as described in the `AWS Secrets Manager Developer Guide <https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html>`_

Retrieve the secret value
=============================================

The following example shows how to:
 
* Retrieve a secret value using 
  `get_secret_value <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_secret_value>`_.
 
Example
-------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError


    def get_secret():
        secret_name = "MySecretName"
        region_name = "us-west-2"

        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name,
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                print("The requested secret " + secret_name + " was not found")
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                print("The request was invalid due to:", e)
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                print("The request had invalid params:", e)
            elif e.response['Error']['Code'] == 'DecryptionFailure':
                print("The requested secret can't be decrypted using the provided KMS key:", e)
            elif e.response['Error']['Code'] == 'InternalServiceError':
                print("An error occurred on service side:", e)
        else:
            # Secrets Manager decrypts the secret value using the associated KMS CMK
            # Depending on whether the secret was a string or binary, only one of these fields will be populated
            if 'SecretString' in get_secret_value_response:
                text_secret_data = get_secret_value_response['SecretString']
            else:
                binary_secret_data = get_secret_value_response['SecretBinary']
                
            # Your code goes here. 

     
