.. Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
.. SPDX-License-Identifier: Apache-2.0

.. _guide_session:

Session
=======

Overview
---------

A session manages state about a particular configuration. By default, a session is created for you when needed. However, it's possible and recommended that in some scenarios you maintain your own session. Sessions typically store the following:

* Credentials
* AWS Region
* Other configurations related to your profile


Default session
----------------

Boto3 acts as a proxy to the default session. This is created automatically when you create a low-level client or resource client::

    import boto3

    # Using the default session
    sqs = boto3.client('sqs')
    s3 = boto3.resource('s3')


Custom session
---------------

You can also manage your own session and create low-level clients or resource clients from it::


    import boto3
    import boto3.session

    # Create your own session
    my_session = boto3.session.Session()

    # Now we can create low-level clients or resource clients from our custom session
    sqs = my_session.client('sqs')
    s3 = my_session.resource('s3')


Session configurations
------------------------

You can configure each session with specific credentials, AWS Region information, or profiles. The most common configurations you might use are:

* ``aws_access_key_id`` - A specific AWS access key ID.
* ``aws_secret_access_key`` - A specific AWS secret access key.
* ``region_name`` - The AWS Region where you want to create new connections.
* ``profile_name`` - The profile to use when creating your session.


.. note::
    Only set the ``profile_name`` parameter when a specific profile is required for your session. To use the default profile, don’t set the ``profile_name`` parameter at all. If the ``profile_name`` parameter isn't set *and* there is no default profile, an empty config dictionary will be used.

    For a detailed list of per-session configurations, see the `Session core reference <https://docs.aws.amazon.com/boto3/latest/reference/core/session.html>`_.


.. _guide_session_multithreading:

Multithreading or multiprocessing with sessions
-----------------------------------------------

``Session`` objects are not thread safe and should not be shared across
threads or processes. Clients created from a session are thread safe (with the
caveats in :ref:`guide_clients_multithreading`), and once a client has been
created it does not call back into its session. That gives you two safe
patterns for using Boto3 from multiple threads:

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

Cost of creating many sessions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first time a session creates a client for a service, Boto3 reads that
service's JSON model files from disk and caches them in that session. Later
clients for the same service from the same session reuse the cache, but the
cache is not shared between sessions. Each new session rereads the files and
holds its own copy of the model data in memory, so a session per thread or per
task repeats that cost every time. When you can, create one session and reuse
it (pattern 1 above).

Some workloads need a separate session for each set of credentials, for
example iterating over every account in an AWS Organization and assuming a
role in each one. Each of those sessions holds its own copy of the model data
for every service it creates a client for, and in memory-constrained
environments this adds up quickly. Create only as many sessions as you need
at one time. A session's model data is freed only after both the session and
every client created from it have gone out of scope.
