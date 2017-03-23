.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-allocate-address:   

###########################
Allocate an Elastic Address
###########################

An *Elastic IP address* is a static IPv4 address designed for dynamic cloud computing. An Elastic IP 
address is associated with your AWS account. With an Elastic IP address, you can mask the failure of 
an instance or software by rapidly remapping the address to another instance in your account. 

The example below shows how to:
 
* Acquire an Elastic IP address using 
  `allocate_address <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.allocate_address>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Acquire an Elastic IP address for either the EC2-Classic platform or a VPC
--------------------------------------------------------------------------------------------------------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError

    ec2 = boto3.client('ec2')

    try:
        allocation = ec2.allocate_address(Domain='vpc')
        response = ec2.associate_address(AllocationId=allocation['AllocationId'],
                                         InstanceId='INSTANCE_ID')
        print(response)
    except ClientError as e:
        print(e)
