.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-managing-instances:   

#############################
Managing Amazon EC2 instances
#############################

This Python example shows you how to:

* Get basic information about your Amazon EC2 instances

* Start and stop detailed monitoring of an Amazon EC2 instance

* Start and stop an Amazon EC2 instance

* Reboot an Amazon EC2 instance

The scenario
============

In this example, Python code is used perform several basic instance management operations. The code uses the 
AWS SDK for Python to manage the instances by using these methods of the EC2 client class:

* `describe_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances>`_.

* `monitor_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.monitor_instances>`_.

* `unmonitor_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unmonitor_instances>`_.

* `start_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_instances>`_.

* `stop_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.stop_instances>`_.

* `reboot_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reboot_instances>`_.

For more information about the lifecycle of Amazon EC2 instances, see 
`Instance Lifecycle <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`_ 
in the *Amazon EC2 User Guide for Linux Instances* or `Instance Lifecycle <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-lifecycle.html>`_ 
in the *Amazon EC2 User Guide for Windows Instances*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.
    
Describe instances
==================

An EC2 instance is a virtual server in Amazon's Elastic Compute Cloud (EC2) for running applications 
on the Amazon Web Services (AWS) infrastructure.

The example below shows how to:
 
* Describe one or more EC2 instances using 
  `describe_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Example
-------

.. code-block:: python

    import boto3
    
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)


Monitor and unmonitor instances
===============================

Enable or disable detailed monitoring for a running instance. If detailed monitoring is not enabled, 
basic monitoring is enabled. For more information, see 
`Monitoring Your Instances and Volumes <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html>`_ 
in the *Amazon Elastic Compute Cloud User Guide*.

The example below shows how to:
 
* Enable detailed monitoring for a running instance using 
  `monitor_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.monitor_instances>`_.

* Disable detailed monitoring for a running instance using 
  `unmonitor_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unmonitor_instances>`_.
  
Example
-------

.. code-block:: python

    import sys
    import boto3


    ec2 = boto3.client('ec2')
    if sys.argv[1] == 'ON':
        response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
    else:
        response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
    print(response)


Start and stop instances
========================

Instances that use Amazon EBS volumes as their root devices can be quickly stopped and started. When 
an instance is stopped, the compute resources are released and you are not billed for hourly instance 
usage. However, your root partition Amazon EBS volume remains, continues to persist your data, and 
you are charged for Amazon EBS volume usage. You can restart your instance at any time. Each time 
you transition an instance from stopped to started, Amazon EC2 charges a full instance hour, even 
if transitions happen multiple times within a single hour.

The example below shows how to:
 
* Start an Amazon EBS-backed AMI that you've previously stopped using 
  `start_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_instances>`_.

* Stop an Amazon EBS-backed instance using 
  `stop_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.stop_instances>`_.
 
Example
-------

.. code-block:: python

    import sys
    import boto3
    from botocore.exceptions import ClientError

    instance_id = sys.argv[2]
    action = sys.argv[1].upper()

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

        # Dry run succeeded, call stop_instances without dryrun
        try:
            response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)


Reboot instances
================
Request a reboot of one or more instances. This operation is asynchronous; it only queues a request 
to reboot the specified instances. The operation succeeds if the instances are valid and belong to 
you. Requests to reboot terminated instances are ignored.

The example below shows how to:
 
* Request a reboot of one or more instances using 
  `reboot_instances <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reboot_instances>`_.
 
Example
-------

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
