.. Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
.. SPDX-License-Identifier: Apache-2.0

.. _guide_clients:

Low-level clients
=================
Clients provide a low-level interface to AWS whose methods map close to 1:1
with service APIs. All service operations are supported by clients. Clients
are generated from a JSON service definition file.

Creating clients
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
    sqs = sqs_resource.meta.client

Service operations
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

Handling responses
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

Waiters
-------
Waiters use a client's service operations to poll the status of an AWS resource
and suspend execution until the AWS resource reaches the state that the
waiter is polling for or a failure occurs while polling.
Using clients, you can learn the name of each waiter that a client has access
to::

    import boto3

    s3 = boto3.client('s3')
    sqs = boto3.client('sqs')

    # List all of the possible waiters for both clients
    print("s3 waiters:")
    s3.waiter_names

    print("sqs waiters:")
    sqs.waiter_names

Note if a client does not have any waiters, it will return an empty list when
accessing its ``waiter_names`` attribute::

    s3 waiters:
    [u'bucket_exists', u'bucket_not_exists', u'object_exists', u'object_not_exists']
    sqs waiters:
    []

Using a client's ``get_waiter()`` method, you can obtain a specific waiter
from its list of possible waiters::

    # Retrieve waiter instance that will wait till a specified
    # S3 bucket exists
    s3_bucket_exists_waiter = s3.get_waiter('bucket_exists')

Then to actually start waiting, you must call the waiter's ``wait()`` method
with the method's appropriate parameters passed in::

    # Begin waiting for the S3 bucket, amzn-s3-demo-bucket, to exist
    s3_bucket_exists_waiter.wait(Bucket='amzn-s3-demo-bucket')

.. _guide_clients_multithreading:

Multithreading or multiprocessing with clients
----------------------------------------------

Unlike Resources and Sessions, clients **are** generally *thread-safe*.
There are some caveats, defined below, to be aware of though.

Caveats
~~~~~~~

**Multi-Processing:** While clients are *thread-safe*, they cannot be
shared across processes due to their networking implementation. Doing so
may lead to incorrect response ordering when calling services.

**Shared Metadata:** Clients expose metadata to the end user through a
few attributes (namely ``meta``, ``exceptions`` and ``waiter_names``).
These are safe to read but any mutations should not be considered
thread-safe.

**Custom** \ `Botocore Events`_\ **:** Botocore (the library Boto3 is
built on) allows advanced users to provide their own custom event hooks
which may interact with boto3’s client. The majority of users will not
need to use these interfaces, but those that do should no longer
consider their clients thread-safe without careful review.

.. note::
    ``boto3.client('<service_name>')`` is an alias for creating a client with a
    shared default session. Invoking ``boto3.client()`` inside of a concurrent
    context may result in response ordering issues or interpreter failures
    from underlying SSL modules.

Creating clients for use in threads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Session`` that creates a client is not thread safe, so what matters is
where you call ``session.client()``. Once a client has been created it does not
call back into its session and can be used from any thread. There are two safe
patterns:

1. **Create one session outside the threads and pass its clients to the
   threads.** The threads share the clients and never touch the session. This
   is the recommended pattern::

    import boto3.session
    from concurrent.futures import ThreadPoolExecutor

    def do_s3_task(client, task_definition):
        # Put your thread-safe code here
        ...

    def my_workflow():
        # Create a session outside the threads and use it to make our client.
        session = boto3.session.Session()
        s3_client = session.client('s3')

        # Define some work to be done, this can be anything
        my_tasks = [ ... ]

        # Dispatch work tasks with our s3_client. The client is thread safe
        # and is shared by all the workers.
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(do_s3_task, s3_client, task) for task in my_tasks]

2. **Create both the session and the client inside each thread.** Nothing is
   shared between threads, but every thread rereads the service model files::

    import boto3.session
    import threading

    class MyTask(threading.Thread):
        def run(self):
            # Here we create a new session per thread
            session = boto3.session.Session()

            # Next, we create a client using our thread's session object
            s3 = session.client('s3')

            # Put your thread-safe code here
            ...

Do not mix the two. Creating a session in one thread and then calling
``session.client()`` from other threads at the same time uses the session
concurrently, which is not safe.

With multiple processes, create both the session and the clients inside each
process. Neither sessions nor clients can be shared across processes.

The first time a session creates a client for a service, Boto3 reads that
service's JSON model files from disk and caches them in that session. The cache
is not shared between sessions, so with the second pattern every thread repeats
the read and holds its own copy of the model data. This is why the first
pattern is recommended. See :ref:`guide_session_multithreading` for details.

.. _Botocore Events: https://docs.aws.amazon.com/botocore/latest/topics/events.html
