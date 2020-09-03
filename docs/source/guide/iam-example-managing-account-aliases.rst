.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-iam-managing-account-aliases:   

############################
Managing IAM account aliases
############################

This Python example shows you how to manage aliases for your AWS account ID.

The scenario
============

If you want the URL for your sign-in page to contain your company name or other friendly identifier 
instead of your AWS account ID, you can create an alias for your AWS account ID. If you create an 
AWS account alias, your sign-in page URL changes to incorporate the alias.

In this example, Python code is used to create and manage IAM account aliases. The code uses the 
AWS SDK for Python to manage IAM access keys using these methods of the IAM client class:

* `create_account_alias <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_account_alias>`_.

* `get_paginator('list_account_aliases') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_paginator>`_.

* `delete_account_alias <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_account_alias>`_.

For more information about IAM account aliases, see `Your AWS Account ID and Its Alias <http://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html>`_ 
in the *IAM User Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.

Create an account alias
=======================

Create an alias for your AWS account. For information about using an AWS account alias, see 
`Using an Alias for Your AWS Account ID <http://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html>`_ 
in the *IAM User Guide*.

The example below shows how to:
 
* Create an account alias using 
  `create_account_alias <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_account_alias>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Create an account alias
    iam.create_account_alias(
        AccountAlias='ALIAS'
    )

List an account alias
=====================

List the account alias associated with the AWS account (Note: you can have only one). For information 
about using an AWS account alias, see `Using an Alias for Your AWS Account ID <http://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html>`_ 
in the *IAM User Guide*. 

The example below shows how to:
 
* List account aliases using 
  `get_paginator('list_account_aliases') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_paginator>`_.
 
For more information about paginators see, :doc:`paginators`
 
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # List account aliases through the pagination interface
    paginator = iam.get_paginator('list_account_aliases')
    for response in paginator.paginate():
        print(response['AccountAliases'])

Delete an account alias
=========================

Delete the specified AWS account alias. For information about using an AWS account alias, see 
`Using an Alias for Your AWS Account ID <http://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html>`_ 
in the *IAM User Guide*.

The example below shows how to:
 
* Delete an account alias using 
  `delete_account_alias <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_account_alias>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Delete an account alias
    iam.delete_account_alias(
        AccountAlias='ALIAS'
    )
