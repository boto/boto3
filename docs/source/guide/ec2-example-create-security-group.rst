.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-create-security-groups:   

######################
Create Security Groups
######################

A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. 
For more information, see `Amazon EC2 Security Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`_ 
in the *Amazon Elastic Compute Cloud User Guide* and `Security Groups for Your VPC <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`_ 
in the *Amazon Virtual Private Cloud User Guide*.

The example below shows how to:
 
* Create a Security Group using 
  `create_security_group <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.create_security_group>`_.

* Add an ingress rule to a security group using 
  `authorize_security_group_ingress <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Create a Security Group and Add an Ingress Rule
-----------------------------------------------------------------------------

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
