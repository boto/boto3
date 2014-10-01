.. _design_resources:

Resources Design
================

Overview
--------
Resources represent an object-oriented interface to Amazon Web Services (AWS).
They provide a higher-level abstraction than the raw, low-level calls made by
service clients. To use resources, you invoke the
:py:meth:`~boto3.session.Session.resource` method of a
:py:class:`~boto3.session.Session` and pass in a service name::

    >>> s3 = boto3.resource('s3')

Every resource instance has a number of attributes and methods. These can
conceptually be split up into identifiers, attributes, actions, references,
sub-resources, and collections. Each of these is described in further detail
below.

Resources themselves can also be conceptually split into service resources
(like ``sqs``, ``s3``, ``ec2``, etc) and individual resources (like
``sqs.Queue`` or ``s3.Bucket``). Service resources *do not* to have
identifiers or attributes.

Identifiers & Attributes
------------------------
An identifier is a unique value that is used to call actions on the resource.
Resources **must** have at least one identifier, except for the top-level
service resources (e.g. ``sqs`` or ``s3``). An identifier is set at instance
creation-time, and failing to provide all necessary identifiers during
instantiation will result in an exception. Examples of identifiers::

    # SQS Queue
    queue = sqs.Queue(url='http://...')
    print(queue.url)

    # S3 Object
    obj = s3.Object(bucket_name='boto3', key='test.py')
    print(obj.bucket_name)
    print(obj.key)

    # Raises exception, missing key!
    obj = s3.Object(bucket_name='boto3')

Identifiers may also be passed as positional arguments::

    # SQS Queue
    queue = sqs.Queue('http://...')

    # S3 Object
    obj = s3.Object('boto3', 'test.py')

    # Raises exception, missing key!
    obj = s3.Object('boto3')

Resources may also have attributes, which are *lazy-loaded* properties on the
instance. They may be set at creation time from the response of an action on
another resource, or they may be set when accessed or via an explicit call to
the ``load`` or ``reload`` action. Examples of attributes::

    # SQS Message
    message.body

    # S3 Object
    obj.last_modified
    obj.md5

Actions
-------
An action is a method which makes a call to the service. Actions may return a
low-level response, a new resource instance or a list of new resource
instances. Actions automatically set the resource identifiers as parameters,
but allow you to pass additional parameters via keyword arguments. Examples
of actions::

    # SQS Service
    queue = sqs.get_queue_by_name(QueueName='test')

    # SQS Queue
    messages = queue.receive_messages()

    # SQS Message
    for message in messages:
        message.delete()

    # S3 Object
    obj = s3.Object(bucket_name='boto3', key='test.py')
    response = obj.get()
    data = response['Body'].read()

References & Sub-resources
--------------------------
A reference is an attribute which may be ``None`` or a related resource
instance. The resource instance does not share identifiers, that is, it is
not a strict parent to child relationship. In relational terms, these can
be considered many-to-one or one-to-one. Examples of references::

    # EC2 Instance
    instance.subnet
    instance.vpc

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

Collections
-----------
A collection provides an iterable interface to a group of resources.
Collections behave similarly to
`Django QuerySets <https://docs.djangoproject.com/en/1.7/ref/models/querysets/>`_
and expose a similar API. A collection seamlessly handles pagination for
you. Examples of collections::

    # SQS
    for queue in sqs.queues.all():
        print(queue.url)

    # S3
    for bucket in s3.buckets.all():
        for obj in bucket.objects.filter(Prefix='/photos'):
            print('{0}:{1}'.format(bucket.name, obj.key))

.. warning::

   Behind the scenes, the above example will call ``ListBuckets``,
   ``ListObjects``, and ``HeadObject`` many times. If you have a large
   number of S3 objects then this could incur a significant cost.

Implementation
--------------
Resource classes are generated at runtime using a factory that is attached
to a session. Each time a resource is requested, the factory is asked to
provide its class. The factory uses a resource base class and the resource
definition JSON to construct and return the new class, which is then
instantiated with the required arguments and returned to the user.

Resource Factory
~~~~~~~~~~~~~~~~
The :py:class:`resource factory <boto3.resources.factory.ResourceFactory>`
follows these basic steps:

1. Check for and return existing cached class if possible
2. Gather and set identifiers
3. Gather and set attributes (from shape introspection)
4. Gather and set actions
5. Gather and set references & sub-resources
6. Gather and set collections
7. Create a new class type and return it

Resource Base
~~~~~~~~~~~~~
The :py:class:`resource base class <boto3.resources.base.ServiceResource>`
contains basic shared logic between all resources, such as requiring
identifiers to be set at instantiation time.

Resource Actions
~~~~~~~~~~~~~~~~
The :py:class:`resource action <boto3.resources.action.ServiceAction>` is a
callable class that performs an operation on a service. It handles
automatically setting some parameters, for example  ``QueueUrl`` is not
required to be set by the user for any actions on an SQS queue resource. It
will also create new resource instances from the response if possible. It
follows these basic steps:

1. Generate known request parameters
2. Merge user-specified request parameters
3. Call service operation
4. Handle response

The response may be handled in one of three ways:

* Return the raw response
* Search and return via JMESPath
* Create one or more resource instances from the response and return
