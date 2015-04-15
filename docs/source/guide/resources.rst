.. _guide_resources:

Resources
=========

Overview
--------
Resources represent an object-oriented interface to Amazon Web Services (AWS).
They provide a higher-level abstraction than the raw, low-level calls made by
service clients. To use resources, you invoke the
:py:meth:`~boto3.session.Session.resource` method of a
:py:class:`~boto3.session.Session` and pass in a service name::

    # Get resources from the default session
    sqs = boto3.resource('sqs')
    s3 = boto3.resource('s3')

Every resource instance has a number of attributes and methods. These can
conceptually be split up into identifiers, attributes, actions, references,
sub-resources, and collections. Each of these is described in further detail
below and in the following section.

Resources themselves can also be conceptually split into service resources
(like ``sqs``, ``s3``, ``ec2``, etc) and individual resources (like
``sqs.Queue`` or ``s3.Bucket``). Service resources *do not* have
identifiers or attributes. The two share the same components otherwise.

Identifiers & Attributes
------------------------
An identifier is a unique value that is used to call actions on the resource.
Resources **must** have at least one identifier, except for the top-level
service resources (e.g. ``sqs`` or ``s3``). An identifier is set at instance
creation-time, and failing to provide all necessary identifiers during
instantiation will result in an exception. Examples of identifiers::

    # SQS Queue (url is an identifier)
    queue = sqs.Queue(url='http://...')
    print(queue.url)

    # S3 Object (bucket_name and key are identifiers)
    obj = s3.Object(bucket_name='boto3', key='test.py')
    print(obj.bucket_name)
    print(obj.key)

    # Raises exception, missing identifier: key!
    obj = s3.Object(bucket_name='boto3')

Identifiers may also be passed as positional arguments::

    # SQS Queue
    queue = sqs.Queue('http://...')

    # S3 Object
    obj = s3.Object('boto3', 'test.py')

    # Raises exception, missing key!
    obj = s3.Object('boto3')

Identifiers also play a role in resource instance equality. For two
instances of a resource to be considered equal, their identifiers must
be equal::

    >>> bucket1 = s3.Bucket('boto3')
    >>> bucket2 = s3.Bucket('boto3')
    >>> bucket3 = s3.Bucket('some-other-bucket')

    >>> bucket1 == bucket2
    True
    >>> bucket1 == bucket3
    False

.. note::

   Only identifiers are taken into account for instance equality. Region,
   account ID and other data members are not considered. When using temporary
   credentials or multiple regions in your code please keep this in mind.

Resources may also have attributes, which are *lazy-loaded* properties on the
instance. They may be set at creation time from the response of an action on
another resource, or they may be set when accessed or via an explicit call to
the ``load`` or ``reload`` action. Examples of attributes::

    # SQS Message
    message.body

    # S3 Object
    obj.last_modified
    obj.md5

.. warning::

   Attributes may incur a load action when first accessed. If latency is
   a concern, then manually calling ``load`` will allow you to control
   exactly when the load action (and thus latency) is invoked. The
   documentation for each resource explicitly lists its attributes.

   Additionally, attributes may be reloaded after an action has been
   performed on the resource. For example, if the ``last_modified``
   attribute of an S3 object is loaded and then a ``put`` action is
   called, then the next time you access ``last_modified`` it will
   reload the object's metadata.

Actions
-------
An action is a method which makes a call to the service. Actions may return a
low-level response, a new resource instance or a list of new resource
instances. Actions automatically set the resource identifiers as parameters,
but allow you to pass additional parameters via keyword arguments. Examples
of actions::

    # SQS Queue
    messages = queue.receive_messages()

    # SQS Message
    for message in messages:
        message.delete()

    # S3 Object
    obj = s3.Object(bucket_name='boto3', key='test.py')
    response = obj.get()
    data = response['Body'].read()

Examples of sending additional parameters::

    # SQS Service
    queue = sqs.get_queue_by_name(QueueName='test')

    # SQS Queue
    queue.send_message(MessageBody='hello')

.. note::

   Parameters **must** be passed as keyword arguments. They will not work
   as positional arguments.

References
----------
A reference is an attribute which may be ``None`` or a related resource
instance. The resource instance does not share identifiers with its
reference resource, that is, it is not a strict parent to child relationship.
In relational terms, these can be considered many-to-one or one-to-one.
Examples of references::

    # EC2 Instance
    instance.subnet
    instance.vpc

In the above example, an EC2 instance may have exactly one associated
subnet, and may have exactly one associated VPC. The subnet does not
require the instance ID to exist, hence it is not a parent to child
relationship.

Sub-resources
-------------
A sub-resource is similar to a reference, but is a related class rather than
an instance. Sub-resources, when instantiated, share identifiers with their
parent. It is a strict parent-child relationship. In relational terms, these
can be considered one-to-many. Examples of sub-resources::

    # SQS
    queue = sqs.Queue(url='...')
    message = queue.Message(receipt_handle='...')
    print(queue.url == message.queue_url)
    print(message.receipt_handle)

    # S3
    obj = bucket.Object(key='new_file.txt')
    print(obj.bucket_name)
    print(obj.key)

Because an SQS message cannot exist without a queue, and an S3 object cannot
exist without a bucket, these are parent to child relationships.

Waiters
-------
A waiter is similiar to an action. A waiter will poll the status of a
resource and suspend execution until the resource reaches the state that is
being polling for or a failure occurs while polling.
Waiters automatically set the resource
identifiers as parameters, but allow you to pass additional parameters via
keyword arguments. Examples of waiters include::

    # S3: Wait for a bucket to exist.
    bucket.wait_until_exists()

    # EC2: Wait for an instance to reach the running state.
    instance.wait_until_running()


Multithreading
--------------
It is recommended to create a resource instance for each thread in a multithreaded application rather than sharing a single instance among the threads. For example::

    import boto3
    import boto3.session
    import threading

    class MyTask(threading.Thread):
        def run(self):
            session = boto3.session.Session()
            s3 = session.resource('s3')
            # ... do some work with S3 ...

In the example above, each thread would have its own Boto 3 session and its own instance of the S3 resource. This is a good idea because resources contain shared data when loaded and calling actions, accessing properties, or manually loading or reloading the resource can modify this data.
