.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-iam-examples-managing-users:   

******************
Managing IAM users
******************

This Python example shows you how to create a user, list users, update a user name and delete a user.

The scenario
============

In this example Python code is used to create and manage users in IAM. The code uses the 
Amazon Web Services (AWS) SDK for Python to manage users using these methods of the 
IAM client class:

* `create_user <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_user>`_

* `get_paginator('list_users') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_paginator>`_.

* `update_user <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_user>`_.

* `delete_user <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_user>`_.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
    
For more information about IAM users, see `IAM Users <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html>`_ 
in the *IAM User Guide*.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.
    
Create a user
=============

Create a new IAM user for your AWS account.

For information about limitations on the number of IAM users you can create, see 
`Limitations on IAM Entities <http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html>`_ 
in the *IAM User Guide*.

The example below shows how to:
 
* Create a new IAM user using 
  `create_user <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_user>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Create user
    response = iam.create_user(
        UserName='IAM_USER_NAME'
    )

    print(response)

List users in your account
==========================

List the IAM users.

The example below shows how to:
 
* List the IAM users using 
  `get_paginator('list_users') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_paginator>`_.
  
For more information about paginators see, :doc:`paginators`
 
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # List users with the pagination interface
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        print(response)

Update a user's name
====================

Update the name and/or the path of the specified IAM user.

To change a user's name or path, you must use the AWS CLI, Tools for Windows PowerShell, or AWS API. 
There is no option in the console to rename a user. For information about the permissions that you 
need in order to rename a user, see 
`Delegating Permissions to Administer IAM Users, Groups, and Credentials <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_renaming>`_ 
in the *IAM User Guide*. 

The example below shows how to:
 
* Update an IAM user name using 
  `update_user <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_user>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Update a user name
    iam.update_user(
        UserName='IAM_USER_NAME',
        NewUserName='NEW_IAM_USER_NAME'
    )

 
Delete a user
=============

Delete the specified IAM user. The user must not belong to any groups or have any access keys, signing 
certificates, or attached policies.

The example below shows how to:
 
* Delete an IAM user name using 
  `delete_user <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_user>`_.

Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Delete a user
    iam.delete_user(
        UserName='IAM_USER_NAME'
    )
     