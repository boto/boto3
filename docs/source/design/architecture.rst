.. _design_arch:

Architecture
============

Overview
--------
Boto 3 consists of several main concepts:

* Session
* Clients
* Resources & collections
* High-level abstractions

Session
-------
A session manages state about a particular configuration. By default a
session is created for you when needed, however it is possible and
recommended to maintain your own session(s) in some scenarios. Session
objects provide an interface to the concepts described below. The ``boto3``
module acts as a proxy to the default session. Example session use::

    # Using the default session
    sqs = boto3.client('sqs')

    # Creating your own session
    session = boto3.session.Session()
    sqs = session.client('sqs')

Clients
-------
Clients provide a low-level interface to AWS and map close to 1:1 with
service APIs. All service operations are supported by clients. Clients are
generated from a JSON service definition file.

Example of client use::

    import boto3

    # Create a low-level client with the service name
    sqs = boto3.client('sqs')

    # Make a call using the low-level client
    response = sqs.send_message(QueueUrl='...', MessageBody='...')

As can be seen above, the method arguments map directly to the associated
`SQS API <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html>`_.
The method names have been snake-cased for better looking Python code.

Resources & collections
-----------------------
Resources provide an object-oriented interface to AWS, which sits atop of
service clients. Collections provide an iterable interface to groups of
resources. Together, they provide a more traditional Python interface to AWS
and a more natural way to interact with the services.

Resources & collections are generated from a JSON resource definition file.
Example of resource use::

    import boto3

    # Create a service resource with the service name
    sqs = boto3.resource('sqs')

    # Get a queue resource and send it a new message
    queue = sqs.get_queue_by_name(QueueName='test')
    queue.send_message(MessageBody='hello world')

.. note::

   Resources & collections are the preferred method of interacting with Boto 3
   in the absence of high level abstractions. For more information, look at
   :ref:`design_resources`.

High-level abstractions
-----------------------
High-level abstractions are hand-coded customizations to provide more
advanced or more convenient functionality to SDK users. High level
abstractions are created on a case-by-case basis.
