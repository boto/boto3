.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-sqs-messages:   

############################################
Sending and receiving messages in Amazon SQS
############################################

This Python example shows you how to send, receive, and delete messages in a queue.

The scenario
============

In this example, Python code is used to send and receive messages. The code uses the AWS SDK for Python 
to send and receive messages by using these methods of the AWS.SQS client class:

* `send_message <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message>`_.

* `receive_message <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.receive_message>`_.

* `delete_message <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_message>`_.

For more information about Amazon SQS messages, see 
`Sending a Message to an Amazon SQS Queue <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-send-message.html>`_ 
and `Receiving and Deleting a Message from an Amazon SQS Queue <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-receive-delete-message.html>`_ 
in the *Amazon Simple Queue Service Developer Guide*.

Prerequisite tasks
==================

To set up and run this example, you must first complete these tasks:

* Create an Amazon SQS queue. For an example of creating an Amazon SQS 
  queue, see :ref:`aws-boto3-sqs-create-queue`.

.. _aws-boto3-sqs-send-message:

Send a message to a queue
=========================

The example below shows how to:
 
* Send a message to a queue using 
  `send_message <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    queue_url = 'SQS_QUEUE_URL'

    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )

    print(response['MessageId'])


Receive and delete messages from a queue
========================================

The example below shows how to:
 
* Receive a message from a queue using 
  `receive_message <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.receive_message>`_.
  
* Delete a message from a queue using 
  `delete_message <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_message>`_.

Example
-------

.. code-block:: python

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    queue_url = 'SQS_QUEUE_URL'

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print('Received and deleted message: %s' % message)
