.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-cw-creating-alarms:   

####################################
Creating alarms in Amazon CloudWatch
####################################

This Python example shows you how to:

* Get basic information about your CloudWatch alarms

* Create and delete a CloudWatch alarm

The scenario
============

An alarm watches a single metric over a time period you specify, and performs one or more actions 
based on the value of the metric relative to a given threshold over a number of time periods.

In this example, Python code is used to create alarms in CloudWatch. The code 
uses the AWS SDK for Python to create alarms using these methods of the AWS.CloudWatch client class:

* `paginate(StateValue='INSUFFICIENT_DATA') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.paginate>`_.

* `put_metric_alarm <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm>`_.

* `delete_alarms <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.delete_alarms>`_.

For more information about CloudWatch alarms, see `Creating Amazon CloudWatch Alarms <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html>`_ 
in the *Amazon CloudWatch User Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.

Describe alarms
===============

The example below shows how to:
 
* List metric alarms for insufficient data using 
  `paginate(StateValue='INSUFFICIENT_DATA') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.paginate>`_.
 
For more information about paginators see, :doc:`paginators`
 
Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # List alarms of insufficient data through the pagination interface
    paginator = cloudwatch.get_paginator('describe_alarms')
    for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
        print(response['MetricAlarms'])
 
Create an alarm for a CloudWatch Metric alarm
=============================================

Create or update an alarm and associate it with the specified metric alarm. Optionally, this operation 
can associate one or more Amazon SNS resources with the alarm.

When this operation creates an alarm, the alarm state is immediately set to :code:`INSUFFICIENT_DATA`. 
The alarm is evaluated and its state is set appropriately. Any actions associated with the state are 
then executed.

When you update an existing alarm, its state is left unchanged, but the update completely overwrites 
the previous configuration of the alarm.

The example below shows how to:
 
* Create or update a metric alarm using 
  `put_metric_alarm <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # Create alarm
    cloudwatch.put_metric_alarm(
        AlarmName='Web_Server_CPU_Utilization',
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Period=60,
        Statistic='Average',
        Threshold=70.0,
        ActionsEnabled=False,
        AlarmDescription='Alarm when server CPU exceeds 70%',
        Dimensions=[
            {
              'Name': 'InstanceId',
              'Value': 'INSTANCE_ID'
            },
        ],
        Unit='Seconds'
    )

 
Delete an alarm
===============

Delete the specified alarms. In the event of an error, no alarms are deleted.

The example below shows how to:
 
* Delete a metric alarm using 
  `delete_alarms <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.delete_alarms>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # Delete alarm
    cloudwatch.delete_alarms(
      AlarmNames=['Web_Server_CPU_Utilization'],
    )

 
