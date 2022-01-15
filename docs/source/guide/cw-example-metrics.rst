.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-cw-metrics:   

######################################
Getting metrics from Amazon CloudWatch
######################################

This Python example shows you how to:

* Get a list of published CloudWatch metrics

* Publish data points to CloudWatch metrics

The scenario
============

Metrics are data about the performance of your systems. You can enable detailed monitoring of some 
resources, such as your Amazon CloudWatch instances, or your own application metrics.

In this example, Python code is used to get and send CloudWatch metrics data. 
The code uses the AWS SDK for Python to get metrics from CloudWatch
using these methods of the CloudWatch client class:

* `paginate('list_metrics') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.paginate>`_.

* `put_metric_data <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data>`_.

For more information about CloudWatch metrics, see `Using Amazon CloudWatch Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html>`_ in the 
*Amazon CloudWatch User Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.


List metrics
===============

List the metric alarm events uploaded to CloudWatch Logs. 

The example below shows how to:
 
* List metric alarms of incoming log events using 
  `paginate('list_metrics') <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.paginate>`_.
 
For more information about paginators see, :doc:`paginators`

Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # List metrics through the pagination interface
    paginator = cloudwatch.get_paginator('list_metrics')
    for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
                                       MetricName='IncomingLogEvents',
                                       Namespace='AWS/Logs'):
        print(response['Metrics'])

 
Publish custom metrics
======================

Publish metric data points to Amazon CloudWatch. Amazon CloudWatch associates the data points with 
the specified metric. If the specified metric does not exist, Amazon CloudWatch creates the metric. 
When Amazon CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear 
in calls to ListMetrics.

The example below shows how to:
 
* Publish custom metrics using 
  `put_metric_data <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data>`_.
 

Example
-------
  
.. code-block:: python

    import boto3

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # Put custom metrics
    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName': 'PAGES_VISITED',
                'Dimensions': [
                    {
                        'Name': 'UNIQUE_PAGES',
                        'Value': 'URLS'
                    },
                ],
                'Unit': 'None',
                'Value': 1.0
            },
        ],
        Namespace='SITE/TRAFFIC'
    )
     
