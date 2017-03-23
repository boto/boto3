.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-reboot-instances:   

################
Reboot Instances
################

Requests a reboot of one or more instances. This operation is asynchronous; it only queues a request 
to reboot the specified instances. The operation succeeds if the instances are valid and belong to 
you. Requests to reboot terminated instances are ignored.

The example below shows how to:
 
* Request a reboot of one or more instances using 
  `reboot_instances <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.reboot_instances>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Reboot an EC2 Instance
----------------------------------------------------

.. code-block:: python


    import boto3
    from botocore.exceptions import ClientError


    ec2 = boto3.client('ec2')

    try:
        ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            print("You don't have permission to reboot instances.")
            raise

    try:
        response = ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=False)
        print('Success', response)
    except ClientError as e:
        print('Error', e)
