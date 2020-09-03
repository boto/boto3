.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto-ec2-example-security-group:

##########################################
Working with security groups in Amazon EC2
##########################################

This Python example shows you how to:

* Get information about your security groups

* Create a security group to access an Amazon EC2 instance

* Delete an existing security group

The scenario
============

An Amazon EC2 security group acts as a virtual firewall that controls the traffic for one or more instances. 
You add rules to each security group to allow traffic to or from its associated instances. You can 
modify the rules for a security group at any time; the new rules are automatically applied to all 
instances that are associated with the security group.

In this example, Python code is used to perform several Amazon EC2 operations involving security groups. 
The code uses the AWS SDK for Python to manage IAM access keys using these methods of the EC2 
client class:

* `describe_security_groups <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_groups>`_.

* `authorize_security_group_ingress <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress>`_.

* `create_security_group <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_security_group>`_.

* `delete_security_group <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_security_group>`_.

For more information about the Amazon EC2 security groups, see 
`Amazon EC2 Amazon Security Groups for Linux Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`_ 
in the *Amazon EC2 User Guide for Linux Instances* or 
`Amazon EC2 Security Groups for Windows Instances <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/using-network-security.html>`_ 
in the *Amazon EC2 User Guide for Windows Instances*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
==================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.

Describe security groups
=======================
Describe one or more of your security groups.

A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. 
For more information, see `Amazon EC2 Security Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`_ 
in the *Amazon Elastic Compute Cloud User Guide* and 
`Security Groups for Your VPC <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`_ 
in the *Amazon Virtual Private Cloud User Guide*.

The example below shows how to:
 
* Describe a Security Group using 
  `describe_security_groups <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_groups>`_.

Example
-------

.. code:: python

    import boto3
    from botocore.exceptions import ClientError

    ec2 = boto3.client('ec2')

    try:
        response = ec2.describe_security_groups(GroupIds=['SECURITY_GROUP_ID'])
        print(response)
    except ClientError as e:
        print(e)

Create a security group and rules
=================================

* Create a security group.

* Add one or more ingress rules to a security group.

  Rule changes are propagated to instances within the security group as quickly as possible. However, 
  a small delay might occur.

The example below shows how to:
 
* Create a Security Group using 
  `create_security_group <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_security_group>`_.

* Add an ingress rule to a security group using 
  `authorize_security_group_ingress <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress>`_.
 
Example
-------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError

    ec2 = boto3.client('ec2')

    response = ec2.describe_vpcs()
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

    try:
        response = ec2.create_security_group(GroupName='SECURITY_GROUP_NAME',
                                             Description='DESCRIPTION',
                                             VpcId=vpc_id)
        security_group_id = response['GroupId']
        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ])
        print('Ingress Successfully Set %s' % data)
    except ClientError as e:
        print(e)

Delete a security group
=======================

If you attempt to delete a security group that is associated with an instance, or is referenced by 
another security group, the operation fails with :code:`InvalidGroup.InUse` in EC2-Classic or :code:`DependencyViolation` 
in EC2-VPC.

The example below shows how to:
 
* Delete a security group using 
  `delete_security_group <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_security_group>`_.
 
Example
-------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError

    # Create EC2 client
    ec2 = boto3.client('ec2')

    # Delete security group
    try:
        response = ec2.delete_security_group(GroupId='SECURITY_GROUP_ID')
        print('Security Group Deleted')
    except ClientError as e:
        print(e)

 