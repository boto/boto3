.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-delete-security-group:   

#######################
Delete a Security Group
#######################

A security group acts as a virtual firewall that controls the traffic for one or more instances. 
When you launch an instance, you associate one or more security groups with the instance.

If you attempt to delete a security group that is associated with an instance, or is referenced by 
another security group, the operation fails with :code:`InvalidGroup.InUse` in EC2-Classic or :code:`DependencyViolation` 
in EC2-VPC.

The example below shows how to:
 
* Delete a security group using 
  `delete_security_group <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.delete_security_group>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Delete a Security Group
-----------------------------------------------------

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
