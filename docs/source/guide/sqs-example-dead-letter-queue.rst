.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-sqs-dead-letter-queue:   

######################################
Using dead-letter queues in Amazon SQS
######################################

This Python example shows you how to use a queue to receive and hold messages from other queues that 
the queues can't process.

The scenario
============

A dead letter queue is one that other (source) queues can target for messages that can't be processed
successfully. You can set aside and isolate these messages in the dead letter queue to determine why 
their processing did not succeed. You must individually configure each source queue that sends messages 
to a dead letter queue. Multiple queues can target a single dead letter queue.

In this example, Python code is used to route messages to a dead letter queue. The code uses the 
SDK for Python to use dead letter queues using this method of the AWS.SQS client class:

* `set_queue_attributes <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.set_queue_attributes>`_.

For more information about Amazon SQS dead letter queues, see 
`Using Amazon SQS Dead Letter Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html>`_ 
in the *Amazon Simple Queue Service Developer Guide*.

Prerequisite tasks
==================

To set up and run this example, you must first complete these tasks:

* Create an Amazon SQS queue to serve as a dead letter queue. For an example 
  of creating an Amazon SQS queue, see :ref:`aws-boto3-sqs-create-queue`.

Configure source queues
=======================

After you create a queue to act as a dead letter queue, you must configure the other queues that route 
unprocessed messages to the dead letter queue. To do this, specify a redrive policy that identifies 
the queue to use as a dead letter queue and the maximum number of receives by individual messages 
before they are routed to the dead letter queue.

The example below shows how to:
 
* Configure a source queue using 
  `set_queue_attributes <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.set_queue_attributes>`_.
 

Example
-------
  
.. code-block:: python
 
    import json

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    queue_url = 'SOURCE_QUEUE_URL'
    dead_letter_queue_arn = 'DEAD_LETTER_QUEUE_ARN'

    redrive_policy = {
        'deadLetterTargetArn': dead_letter_queue_arn,
        'maxReceiveCount': '10'
    }


    # Configure queue to send messages to dead letter queue
    sqs.set_queue_attributes(
        QueueUrl=queue_url,
        Attributes={
            'RedrivePolicy': json.dumps(redrive_policy)
        }
    )
    