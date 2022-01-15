.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-iam-managing-access-keys:   

########################
Managing IAM access keys
########################

This Python example shows you how to manage the access keys of your users.

The scenario
============

Users need their own access keys to make programmatic calls to AWS from the Amazon Web Services (AWS) 
SDK for Python. To fill this need, you can create, modify, view, or rotate access keys 
(access key IDs and secret access keys) for IAM users. By default, when you create an access key, its
status is Active, which means the user can use the access key for API calls.

In this example, Python code is used to manage access keys in IAM. The code uses the AWS SDK for Python 
to manage IAM access keys using these methods of the IAM client class:

* `create_access_key <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_access_key>`_.

* `paginate(UserName='IAM_USER_NAME') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.paginate>`_.

* `get_access_key_last_used <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_access_key_last_used>`_.

* `update_access_key <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_access_key>`_.

* `delete_access_key <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_access_key>`_.


For more information about IAM access keys, see `Managing Access Keys <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html>`_ 
in the *IAM User Guide*. 

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.

Create access keys for a user
=============================

Create a new AWS secret access key and corresponding AWS access key ID for the specified user. The 
default status for new keys is :code:`Active`.

The example below shows how to:
 
* Create a new AWS access key using 
  `create_access_key <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_access_key>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Create an access key
    response = iam.create_access_key(
        UserName='IAM_USER_NAME'
    )

    print(response['AccessKey'])

List a user's access keys
=========================

List information about the access key IDs associated with the specified IAM user. If there are none, 
the action returns an empty list.

If the UserName field is not specified, the UserName is determined implicitly based on the AWS access 
key ID used to sign the request. Because this action works for access keys under the AWS account, 
you can use this action to manage root credentials even if the AWS account has no associated users.

The example below shows how to:
 
* List a user's access keys using 
  `paginate(UserName='IAM_USER_NAME') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.paginate>`_.
  
For more information about paginators see, :doc:`paginators`

Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # List access keys through the pagination interface.
    paginator = iam.get_paginator('list_access_keys')
    for response in paginator.paginate(UserName='IAM_USER_NAME'):
        print(response)


Get the access key last used
============================

Get information about when the specified access key was last used. The information includes the 
date and time of last use, along with the AWS service and region that were specified in the last request 
made with that key.

The example below shows how to:
 
* Get the access key last used using 
  `get_access_key_last_used <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_access_key_last_used>`_.

Example
-------

.. code-block:: python

    import boto3


    # Create IAM client
    iam = boto3.client('iam')

    # Get last use of access key
    response = iam.get_access_key_last_used(
        AccessKeyId='ACCESS_KEY_ID'
    )

    print(response['AccessKeyLastUsed'])


 
Update access key status
========================

Change the status of the specified access key from Active to Inactive, or vice versa. This action 
can be used to disable a user's key as part of a key rotation work flow.

The example below shows how to:
 
* Change the status of an access key to :code:`Active` using 
  `update_access_key <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_access_key>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Update access key to be active
    iam.update_access_key(
        AccessKeyId='ACCESS_KEY_ID',
        Status='Active',
        UserName='IAM_USER_NAME'
    )

    
Delete an access key
====================

Delete the access key pair associated with the specified IAM user.

If you do not specify a user name, IAM determines the user name implicitly based on the AWS access 
key ID signing the request. Because this action works for access keys under the AWS account, you can 
use this action to manage root credentials even if the AWS account has no associated users.

The example below shows how to:
 
* Delete an access key using 
  `delete_access_key <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_access_key>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Delete access key
    iam.delete_access_key(
        AccessKeyId='ACCESS_KEY_ID',
        UserName='IAM_USER_NAME'
    )


 