.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-starting-and-stopping-instances:   

###############################
Starting and Stopping Instances
###############################

Instances that use Amazon EBS volumes as their root devices can be quickly stopped and started. When 
an instance is stopped, the compute resources are released and you are not billed for hourly instance 
usage. However, your root partition Amazon EBS volume remains, continues to persist your data, and 
you are charged for Amazon EBS volume usage. You can restart your instance at any time. Each time 
you transition an instance from stopped to started, Amazon EC2 charges a full instance hour, even 
if transitions happen multiple times within a single hour.

The example below shows how to:
 
* Start an Amazon EBS-backed AMI that you've previously stopped using 
  `start_instances <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.start_instances>`_.

* Stop an Amazon EBS-backed instance using 
  `stop_instances <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.stop_instances>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Start and Stop an EC2 Instance
------------------------------------------------------------

.. code-block:: python

    import sys
    import boto3
    from botocore.exceptions import ClientError

    instance_id = sys.argv[3]
    action = sys.argv[2].upper()

    ec2 = boto3.client('ec2')


    if action == 'ON':
        # Do a dryrun first to verify permissions
        try:
            ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

        # Dry run succeeded, run start_instances without dryrun
        try:
            response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)
    else:
        # Do a dryrun first to verify permissions
        try:
            ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

        # Dry run succeeded, call stop_instances witout dryrun
        try:
            response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)
