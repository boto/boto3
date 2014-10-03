.. _guide_tutorial:

Tutorial
========
`Simple Queue Service (SQS) <http://aws.amazon.com/documentation/sqs/>`_
allows you to queue and then process messages. This tutorial covers how to
create a new queue, get and use an existing queue, push new messages onto the
queue, and process messages from the queue by using
:ref:`guide_resources` and :ref:`guide_collections`.

Creating a Queue
----------------
Queues are created with a name. You may also optionally set queue
attributes, such as the number of seconds to wait before an item may be
processed. The examples below will use the queue name ``test``.
Before creating a queue, you must first get the SQS service resource::

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Create the queue. This returns an SQS.Queue instance
    queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': 5})

    # You can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get['DelaySeconds'])

Reference: :py:meth:`sqs.ServiceResource.create_queue`

.. warning::

   The code above may throw an exception if you already have a queue named
   ``test``.

Using an Existing Queue
-----------------------
It is possible to look up a queue by its name. If the queue does not exist,
then an exception will be thrown::

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName='test')

    # You can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))

It is also possible to list all of our existing queues::

    # Print out each queue name, which is part of its ARN
    for queue in sqs.queues.all():
        print(queue.url)

.. note::

   To get the name from a queue, you must use its ARN, which is available
   in the queue's ``attributes`` attribute. Using
   ``queue.attributes['QueueArn'].split(':')[-1]`` will return its name.

Reference: :py:meth:`sqs.ServiceResource.get_queue_by_name`,
:py:attr:`sqs.ServiceResource.queues`

Sending Messages
----------------
Sending a message adds it to the end of the queue::

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='test')

    # Create a new message
    response = queue.send_message(MessageBody='world')

    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))

You can also create messages with custom attributes::

    queue.send_message(MessageBody='boto3', MessageAttributes={
        'Author': {
            'StringValue': 'Daniel',
            'DataType': 'string'
        }
    })

Messages can also be sent in batches. For example, sending the two messages
described above in a single request would look like the following::

    response = queue.send_messages(Entries=[
        {
            'Id': '1',
            'MessageBody': 'world'
        },
        {
            'Id': '2',
            'MessageBody': 'boto3',
            'MessageAttributes': {
                'Author': {
                    'StringValue': 'Daniel',
                    'DataType': 'string'
                }
            }
        }
    ])

    # Print out any failures
    print(response.get('Failed'))

In this case, the response contains lists of ``Successful`` and ``Failed``
messages, so you can retry failures if needed.

Reference: :py:meth:`sqs.Queue.send_message`,
:py:meth:`sqs.Queue.send_messages`

Processing Messages
-------------------
Messages are processed in batches::

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='test')

    # Process messages by printing out body and optional author name
    for message in queue.receive_messages(MessageAttributeNames=['Author']):
        # Get the custom author message attribute if it was set
        author_text = ''
        if message.message_attributes is not None:
            author_name = message.message_attributes.get('Author')
            if author_name:
                author_text = ' ({0})'.format(author_name)

        # Print out the body and author (if set)
        print('Hello, {0}!{1}'.format(message.body, author_name))

        # Let the queue know that the message is processed
        message.delete()

Given *only* the messages that were sent in a batch with
:py:meth:`~sqs.Queue.send_messages` in the previous section, the above code
will print out::

    Hello, world!
    Hello, boto3! (Daniel)

Reference: :py:meth:`sqs.Queue.receive_messages`,
:py:meth:`sqs.Message.delete`
