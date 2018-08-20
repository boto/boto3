.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-sqs-long-polling:   

###################################
Enabling Long Polling in Amazon SQS
###################################

This Python example shows you how to enable long polling in Amazon SQS in one of these ways:

* For a newly created queue

* For an existing queue

* Upon receipt of a message

The Scenario
============

Long polling reduces the number of empty responses by allowing Amazon SQS to wait a specified time 
for a message to become available in the queue before sending a response. Also, long polling eliminates 
false empty responses by querying all of the servers instead of a sampling of servers. To enable long 
polling, you must specify a non-zero wait time for received messages. You can do this by setting the 
:code:`ReceiveMessageWaitTimeSeconds` parameter of a queue or by setting the :code:`WaitTimeSeconds` 
parameter on a message when it is received.

In this example, Python code is used to enable long polling. The code uses the AWS SDK for Python to 
enable long polling using these methods of the AWS.SQS client class:

* `create_queue <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.create_queue>`_

* `set_queue_attributes <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.set_queue_attributes>`_.

* `receive_message <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.receive_message>`_.

For more information about Amazon SQS long polling, see 
`Long Polling <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html>`_ 
in the *Amazon Simple Queue Service Developer Guide*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite Tasks
==================

To set up and run this example, you must first complete these tasks:

* Configure your AWS credentials, as described in :doc:`quickstart`.

Enable Long Polling When Creating a Queue
=========================================

The example below shows how to:
 
* Create a queue and enable long polling using 
  `create_queue <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.create_queue>`_.
 

Example
-------

.. code-block:: python

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # Create a SQS queue with long polling enabled
    response = sqs.create_queue(
        QueueName='SQS_QUEUE_NAME',
        Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
    )

    print(response['QueueUrl'])


Enable Long Polling on an Existing Queue
========================================

The example below shows how to:
 
* Enable long polling on an existing queue using 
  `set_queue_attributes <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.set_queue_attributes>`_.
 

Example
-------

.. code:: python

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    queue_url = 'SQS_QUEUE_URL'

    # Enable long polling on an existing SQS queue
    sqs.set_queue_attributes(
        QueueUrl=queue_url,
        Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
    )

Enable Long Polling on Message Receipt
======================================

Get one or more messages (up to 10), from the specified queue. Using the WaitTimeSeconds 
parameter enables long-poll support. For more information, see 
`Amazon SQS Long Polling <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html>`_ 
in the *Amazon SQS Developer Guide*.

The example below shows how to:
 
* Enable a long poll for message on provided SQS queue using 
  `receive_message <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.receive_message>`_.
 

Example
-------

.. code-block:: python/example_code

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    queue_url = 'SQS_QUEUE_URL'

    # Long poll for message on provided SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        WaitTimeSeconds=20
    )

    print(response)
