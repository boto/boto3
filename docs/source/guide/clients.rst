.. _guide_clients:

Low-level Clients
=================
Clients provide a low-level interface to AWS whose methods map close to 1:1
with service APIs. All service operations are supported by clients. Clients
are generated from a JSON service definition file.

Creating Clients
----------------
Clients are created in a similar fashion to resources::

    import boto3

    # Create a low-level client with the service name
    sqs = boto3.client('sqs')

It is also possible to access the low-level client from an existing
resource::

    # Create the resource
    sqs_resource = boto3.resource('sqs')

    # Get the client from the resource
    sqs = sqs_resource.meta['client']

Service Operations
------------------
Service operations map to client methods of the same name and provide
access to the same operation parameters via keyword arguments::

    # Make a call using the low-level client
    response = sqs.send_message(QueueUrl='...', MessageBody='...')

As can be seen above, the method arguments map directly to the associated
`SQS API <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html>`_.

.. note::

   The method names have been snake-cased for better looking Python code.

   Parameters **must** be sent as keyword arguments. They will not work
   as positional arguments.

Handling Responses
------------------
Responses are returned as python dictionaries. It is up to you to traverse
or otherwise process the response for the data you need, keeping in mind
that responses may not always include all of the expected data. In the
example below, ``response.get('QueueUrls', [])`` is used to ensure that a
list is always returned, even when the response has no key ``'QueueUrls'``::

    # List all your queues
    response = sqs.list_queues()
    for url in response.get('QueueUrls', []):
        print(url)

The ``response`` in the example above looks something like this:

.. code-block:: json

   {
       "QueueUrls": [
           "http://url1",
           "http://url2",
           "http://url3"
       ]
   }
