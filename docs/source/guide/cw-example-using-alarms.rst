.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-cw-using-alarms:   

########################################
Using alarm actions in Amazon CloudWatch
########################################

This Python example shows you how to:

* Create a CloudWatch alarm and enable actions

* Disable a CloudWatch alarm action

The scenario
============

Using alarm actions, you can create alarms that automatically stop, terminate, reboot, or recover 
your Amazon EC2 instances. You can use the stop or terminate actions when you no longer need an EC2 
instance to be running. You can use the reboot and recover actions to automatically reboot those instances.

In this example, Python code is used to define an alarm action in CloudWatch that 
triggers the reboot of an Amazon EC2 instance. The code uses the AWS SDK for Python to manage
Amazon EC2 instances using these methods of the CloudWatch client class:

* `put_metric_alarm <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm>`_.

* `disable_alarm_actions <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.disable_alarm_actions>`_.


For more information about CloudWatch alarm actions, see 
`Create Alarms to Stop, Terminate, Reboot, or Recover an Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingAlarmActions.html>`_ 
in the *Amazon CloudWatch User Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

* Configure your AWS credentials, as described in :doc:`quickstart`.

* Create an IAM role whose policy grants permission to describe, reboot, stop, or terminate an Amazon 
  EC2 instance. For more information about creating an IAM role, see 
  `Creating a Role to Delegate Permissions to an AWS Service <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html>`_
  in the *IAM User Guide*. 
  
  Use the following role policy when creating the IAM role.

 .. code-block::  python

        {
           "Version": "2012-10-17",
           "Statement": [
              {
                 "Effect": "Allow",
                 "Action": [
                    "cloudwatch:Describe*",
                    "ec2:Describe*",
                    "ec2:RebootInstances",
                    "ec2:StopInstances*",
                    "ec2:TerminateInstances"
                 ],
                 "Resource": [
                    "*"
                 ]
              }
           ]
        }
 
Create and enable actions on an alarm
=====================================

Create or update an alarm and associate it with the specified metric. Optionally, this operation 
can associate one or more Amazon SNS resources with the alarm.

When this operation creates an alarm, the alarm state is immediately set to :code:`INSUFFICIENT_DATA`. 
The alarm is evaluated and its state is set appropriately. Any actions associated with the state are 
then executed.

When you update an existing alarm, its state is left unchanged, but the update completely overwrites 
the previous configuration of the alarm.

The example below shows how to:
 
* Create an alarm and enable actions using 
  `put_metric_alarm <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm>`_.
 
Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # Create alarm with actions enabled
    cloudwatch.put_metric_alarm(
        AlarmName='Web_Server_CPU_Utilization',
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Period=60,
        Statistic='Average',
        Threshold=70.0,
        ActionsEnabled=True,
        AlarmActions=[
          'arn:aws:swf:us-west-2:{CUSTOMER_ACCOUNT}:action/actions/AWS_EC2.InstanceId.Reboot/1.0'
        ],
        AlarmDescription='Alarm when server CPU exceeds 70%',
        Dimensions=[
            {
              'Name': 'InstanceId',
              'Value': 'INSTANCE_ID'
            },
        ],
        Unit='Seconds'
    )

Disable actions on an alarm
===========================

Disable the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions 
do not execute when the alarm state changes.

The example below shows how to:
 
* Disable metric alarm actions using 
  `disable_alarm_actions <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.disable_alarm_actions>`_.
 
Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # Disable alarm
    cloudwatch.disable_alarm_actions(
      AlarmNames=['Web_Server_CPU_Utilization'],
    )

 
