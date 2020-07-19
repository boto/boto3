.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-cw-subscription-filters:   

####################################################
Using subscription filters in Amazon CloudWatch Logs
####################################################

This Python example shows you how to create and delete filters for log events in CloudWatch Logs.

The scenario
============

Subscriptions provide access to a real-time feed of log events from CloudWatch Logs and deliver that 
feed to other services, such as an Amazon Kinesis stream or AWS Lambda, for custom processing, 
analysis, or loading to other systems. A subscription filter defines the pattern to use for filtering 
which log events are delivered to your AWS resource.

In this example, Python code is used to list, create, and delete a subscription 
filter in CloudWatch Logs. The destination for the log events is a Lambda function. 
The code uses the AWS SDK for Python to manage subscription filters using these methods of the
CloudWatchLogs client class:

* `get_paginator('describe_subscription_filters') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.get_paginator>`_.

* `put_subscription_filter <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_subscription_filter>`_.

* `delete_subscription_filter <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_subscription_filter>`_.

For more information about CloudWatch Logs subscriptions, see 
Real-time `Processing of Log Data with Subscriptions <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html>`_ 
in the Amazon CloudWatch Logs User Guide.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
==================

* Configure your AWS credentials, as described in :doc:`quickstart`.

* Create a Lambda function as the destination for log events. You will need to use the ARN of this 
  function. For more information about setting up a Lambda function, see 
  `Subscription Filters with AWS Lambda <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html#LambdaFunctionExample>`_ 
  in the *Amazon CloudWatch Logs User Guide*.

* Create an IAM role whose policy grants permission to invoke the Lambda function you created and 
  grants full access to CloudWatch Logs or apply the following policy to the execution role you create 
  for the Lambda function. For more information about creating an IAM role, see 
  Creating a Role to `Delegate Permissions to an AWS Service <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html>`_ 
  in the *IAM User Guide*.

  Use the following role policy when creating the IAM role.

 .. code-block::  python
   
        {
           "Version": "2012-10-17",
           "Statement": [
              {
                 "Effect": "Allow",
                 "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                 ],
                 "Resource": "arn:aws:logs:*:*:*"
              },
              {
                 "Effect": "Allow",
                 "Action": [
                    "lambda:InvokeFunction"
                 ],
                 "Resource": [
                    "*"
                 ]
              }
           ]
        }
 
List existing subscription filters
==================================

List the subscription filters for the specified log group.

The example below shows how to:
 
* List subscription filters using 
  `get_paginator('describe_subscription_filters') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.get_paginator>`_.
  
For more information about paginators see, :doc:`paginators`

Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatchLogs client
    cloudwatch_logs = boto3.client('logs')

    # List subscription filters through the pagination interface
    paginator = cloudwatch_logs.get_paginator('describe_subscription_filters')
    for response in paginator.paginate(logGroupName='GROUP_NAME'):
        print(response['subscriptionFilters'])



 
Create a subscription filter
============================

Create or update a subscription filter and associate it with the specified log group.

The example below shows how to:
 
* Create a subscription filter using 
  `put_subscription_filter <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_subscription_filter>`_.
 
Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatchLogs client
    cloudwatch_logs = boto3.client('logs')

    # Create a subscription filter
    cloudwatch_logs.put_subscription_filter(
        destinationArn='LAMBDA_FUNCTION_ARN',
        filterName='FILTER_NAME',
        filterPattern='ERROR',
        logGroupName='LOG_GROUP',
    )

 
Delete a subscription filter
============================

The example below shows how to:
 
* Delete a subscription filter. using 
  `delete_subscription_filter <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_subscription_filter>`_.
  
Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatchLogs client
    cloudwatch_logs = boto3.client('logs')

    # Delete a subscription filter
    cloudwatch_logs.delete_subscription_filter(
        filterName='FILTER_NAME',
        logGroupName='LOG_GROUP',
    )


 
