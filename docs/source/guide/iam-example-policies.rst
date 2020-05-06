.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-iam-examples-policies:

#########################
Working with IAM policies
#########################

This Python example shows you how to create and get IAM policies and attach and detach IAM policies from roles.

The scenario
============

You grant permissions to a user by creating a policy, which is a document that lists the actions 
that a user can perform and the resources those actions can affect. Any actions or resources that are 
not explicitly allowed are denied by default. Policies can be created and attached to users, groups 
of users, roles assumed by users, and resources.

In this example, Python code used to manage policies in IAM. The code uses the 
Amazon Web Services (AWS) SDK for Python to create and delete policies as well as attaching and 
detaching role policies using these methods of the IAM client class:

* `create_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_policy>`_.

* `get_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_policy>`_.

* `attach_role_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.attach_role_policy>`_.

* `detach_role_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.detach_role_policy>`_.
    
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

For more information about IAM policies, see `Overview of Access Management: Permissions and Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html>`_ 
in the IAM User Guide.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.

Create an IAM policy
====================

Create a new managed policy for your AWS account.

This operation creates a policy version with a version identifier of :code:`v1` and sets :code:`v1` 
as the policy's default version. For more information about policy versions, see 
`Versioning for Managed Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html>`_ 
in the *IAM User Guide*.

The example below shows how to:
 
* Create a new managed policy using 
  `create_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_policy>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Example
-------

.. code-block:: python

    import json

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Create a policy
    my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "logs:CreateLogGroup",
                "Resource": "RESOURCE_ARN"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:DeleteItem",
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:Scan",
                    "dynamodb:UpdateItem"
                ],
                "Resource": "RESOURCE_ARN"
            }
        ]
    }
    response = iam.create_policy(
      PolicyName='myDynamoDBPolicy',
      PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)

Get an IAM policy
=================

Get information about the specified managed policy, including the policy's default version and 
the total number of IAM users, groups, and roles to which the policy is attached. To get the 
list of the specific users, groups, and roles that the policy is attached to, use the 
:code:`list_entities_for_policy` API. This API returns metadata about the policy. To get the actual policy 
document for a specific version of the policy, use :code:`get_policy_version` API.

This API gets information about managed policies. To get information about an inline policy 
that is embedded with an IAM user, group, or role, use the :code:`get_user_policy`, :code:`get_group_policy`, 
or :code:`get_role_policy` API.

The example below shows how to:
 
* Get information about a managed policy using 
  `get_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_policy>`_.
 
Example
-------

.. code-block:: python

    import boto3


    # Create IAM client
    iam = boto3.client('iam')

    # Get a policy
    response = iam.get_policy(
        PolicyArn='arn:aws:iam::aws:policy/AWSLambdaExecute'
    )
    print(response['Policy'])



Attach a managed role policy
============================

When you attach a managed policy to a role, the managed policy becomes part of the role's permission 
(access) policy. You cannot use a managed policy as the role's trust policy. The role's trust policy 
is created at the same time as the role, using :code:`create_role`. You can update a role's trust policy using 
:code:`update_assume_role_policy`.

Use this API to attach a managed policy to a role. To embed an inline policy in a role, use :code:`put_role_policy`.

The example below shows how to:
 
* Attach a managed policy to an IAM role. using 
  `attach_role_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.attach_role_policy>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Attach a role policy
    iam.attach_role_policy(
        PolicyArn='arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess',
        RoleName='AmazonDynamoDBFullAccess'
    )



Detach a managed role policy
============================

Detach the specified managed policy from the specified role.

A role can also have inline policies embedded with it. To delete an inline policy, use the 
:code:`delete_role_policy` API. For information about policies, see 
`Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`_ 
in the *IAM User Guide*.

The example below shows how to:
 
* Detach a managed role policy using 
  `detach_role_policy <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.detach_role_policy>`_.
 
Example
-------

.. code-block:: python

    import boto3

    # Create IAM client
    iam = boto3.client('iam')

    # Detach a role policy
    iam.detach_role_policy(
        PolicyArn='arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess',
        RoleName='AmazonDynamoDBFullAccess'
    )

