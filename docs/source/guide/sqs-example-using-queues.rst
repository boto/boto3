.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-sqs-using-queues:   

##########################
Using queues in Amazon SQS
##########################

This Python example shows you how to:

* Get a list of all of your message queues

* Obtain the URL for a particular queue

* Create and delete queues

The scenario
============

In this example, Python code is used to work with queues. The code uses the AWS SDK for Python to use 
queues using these methods of the AWS.SQS client class:

* `list_queues <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_queues>`_.

* `create_queue <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.create_queue>`_.

* `get_queue_url <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.get_queue_url>`_.

* `delete_queue <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_queue>`_.

For more information about Amazon SQS messages, see 
`How Queues Work <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-how-it-works.html>`_ 
in the *Amazon Simple Queue Service Developer Guide*.

List your queues
================

The example below shows how to:
 
* List queues using 
  `list_queues <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_queues>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # List SQS queues
    response = sqs.list_queues()

    print(response['QueueUrls'])

.. _aws-boto3-sqs-create-queue:

Create a queue
==============

The example below shows how to:
 
* Create a queue using 
  `create_queue <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.create_queue>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # Create a SQS queue
    response = sqs.create_queue(
        QueueName='SQS_QUEUE_NAME',
        Attributes={
            'DelaySeconds': '60',
            'MessageRetentionPeriod': '86400'
        }
    )

    print(response['QueueUrl'])

Get the URL for a queue
=======================

The example below shows how to:
 
* Get the URL for a queue using 
  `get_queue_url <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.get_queue_url>`_.
  
Example
-------

.. code-block:: python

    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # Get URL for SQS queue
    response = sqs.get_queue_url(QueueName='SQS_QUEUE_NAME')

    print(response['QueueUrl'])

Delete a queue
==============

The example below shows how to:
 
* Delete a queue using 
  `delete_queue <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_queue>`_.
  
Example
-------

  .. code-block:: python
  
    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # Delete SQS queue
    sqs.delete_queue(QueueUrl='SQS_QUEUE_URL')
