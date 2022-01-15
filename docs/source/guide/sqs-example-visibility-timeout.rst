.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-sqs-visibility-timeout:   

#########################################
Managing visibility timeout in Amazon SQS
#########################################

This Python example shows you how to specify the time interval during which messages received by a 
queue are not visible.

The scenario
============

In this example, Python code is used to manage visibility timeout. The code uses the SDK for Python 
to manage visibility timeout by using this method of the AWS.SQS client class:

* `set_queue_attributes <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.set_queue_attributes>`_.

For more information about Amazon SQS visibility timeout, see 
`Visibility Timeout <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>`_ 
in the *Amazon Simple Queue Service Developer Guide*.

Prerequisite tasks
==================

To set up and run this example, you must first complete these tasks:

* Create an Amazon SQS queue. For an example of creating an Amazon SQS 
  queue, see :ref:`aws-boto3-sqs-create-queue`.

* Send a message to the queue. For an example of sending a message to a 
  queue, see :ref:`aws-boto3-sqs-send-message`.

Change the visibility timeout
=============================

The example below shows how to:
 
* Change the visibility timeout using 
  `set_queue_attributes <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.set_queue_attributes>`_.
  
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
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    # Change visibility timeout of message from queue
    sqs.change_message_visibility(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle,
        VisibilityTimeout=20
    )
    print('Received and changed visibility timeout of message: %s' % message)
