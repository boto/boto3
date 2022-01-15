.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-cw-events:   

##########################################
Sending events to Amazon CloudWatch Events
##########################################

This Python example shows you how to:

* Create and update a rule used to trigger an event

* Define one or more targets to respond to an event

* Send events that are matched to targets for handling

The scenario
============

CloudWatch Events delivers a near real-time stream of system events that describe changes in 
Amazon Web Services (AWS) resources to any of various targets. Using simple rules, you can match 
events and route them to one or more target functions or streams.

In this example, Python code is used to send events to CloudWatch Events. The code uses the
AWS SDK for Python to manage instances using these methods of the CloudWatchEvents client class:

* `put_rule <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#CloudWatchEvents.Client.put_rule>`_.

* `put_targets <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#CloudWatchEvents.Client.put_targets>`_.

* `put_events <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#CloudWatchEvents.Client.put_events>`_.

For more information about CloudWatch Events, see 
`Adding Events with PutEvents <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/AddEventsPutEvents.html>`_ 
in the *Amazon CloudWatch Events User Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

* Configure your AWS credentials, as described in :doc:`quickstart`.

* Create a Lambda function using the **hello-world** blueprint to serve as the target for events. To 
  learn how, see `Step 1: Create an AWS Lambda function <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/LogEC2InstanceState.html>`_ 
  in the *Amazon CloudWatch Events User Guide*.

* Create an IAM role whose policy grants permission to CloudWatch Events and that includes :code:`events.amazonaws.com` 
  as a trusted entity. For more information about creating an IAM role, see 
  `Creating a Role to Delegate Permissions to an AWS Service <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html>`_ 
  in the *IAM User Guide*.
  
  Use the following role policy when creating the IAM role.

 .. code-block:: python
  
        {
           "Version": "2012-10-17",
           "Statement": [
              {
                 "Sid": "CloudWatchEventsFullAccess",
                 "Effect": "Allow",
                 "Action": "events:*",
                 "Resource": "*"
              },
              {
                 "Sid": "IAMPassRoleForCloudWatchEvents",
                 "Effect": "Allow",
                 "Action": "iam:PassRole",
                 "Resource": "arn:aws:iam::*:role/AWS_Events_Invoke_Targets"
              }      
           ]
        }

Use the following trust relationship when creating the IAM role.

 .. code-block:: python
 
        {
           "Version": "2012-10-17",
           "Statement": [
              {
                 "Effect": "Allow",
                 "Principal": {
                    "Service": "events.amazonaws.com"
                 },
                 "Action": "sts:AssumeRole"
              }      
           ]
        }


Create a scheduled rule
=======================

Create or update the specified rule. Rules are enabled by default, or based on value of the state. 
You can disable a rule using `DisableRule <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#CloudWatchEvents.Client.disable_rule>`_.

The example below shows how to:
 
* Create a CloudWatch Events rule using 
  `put_rule <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#CloudWatchEvents.Client.put_rule>`_.
 

Example
-------
  
.. code-block:: python

    import boto3


    # Create CloudWatchEvents client
    cloudwatch_events = boto3.client('events')

    # Put an event rule
    response = cloudwatch_events.put_rule(
        Name='DEMO_EVENT',
        RoleArn='IAM_ROLE_ARN',
        ScheduleExpression='rate(5 minutes)',
        State='ENABLED'
    )
    print(response['RuleArn'])

 
Add an AWS Lambda function target
=================================

Add the specified targets to the specified rule, or update the targets if they are already 
associated with the rule.

The example below shows how to:
 
* Add a target to a rule using 
  `put_targets <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#CloudWatchEvents.Client.put_targets>`_.
 

Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatchEvents client
    cloudwatch_events = boto3.client('events')

    # Put target for rule
    response = cloudwatch_events.put_targets(
        Rule='DEMO_EVENT',
        Targets=[
            {
                'Arn': 'LAMBDA_FUNCTION_ARN',
                'Id': 'myCloudWatchEventsTarget',
            }
        ]
    )
    print(response)

 
Send events
===========

Send custom events to Amazon CloudWatch Events so that they can be matched to rules.

The example below shows how to:
 
* Send a custom event to CloudWatch Events using 
  `put_events <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#CloudWatchEvents.Client.put_events>`_.
 
Example
-------
  
.. code-block:: python

    import json

    import boto3


    # Create CloudWatchEvents client
    cloudwatch_events = boto3.client('events')

    # Put an event
    response = cloudwatch_events.put_events(
        Entries=[
            {
                'Detail': json.dumps({'key1': 'value1', 'key2': 'value2'}),
                'DetailType': 'appRequestSubmitted',
                'Resources': [
                    'RESOURCE_ARN',
                ],
                'Source': 'com.company.myapp'
            }
        ]
    )
    print(response['Entries'])

 
