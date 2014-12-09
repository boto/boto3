.. _guide_collections:

Collections
===========

Overview
--------
A collection provides an iterable interface to a group of resources.
Collections behave similarly to
`Django QuerySets <https://docs.djangoproject.com/en/1.7/ref/models/querysets/>`_
and expose a similar API. A collection seamlessly handles pagination for
you, making it possible to easily iterate over all items from all pages of
data. Example of a collection::

    # SQS list all queues
    sqs = boto3.resource('sqs')
    for queue in sqs.queues.all():
        print(queue.url)

When Collections Make Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Collections can be created and manipulated without any request being made
to the underlying service. A collection makes a remote service request under
the following conditions:

* **Iteration**::

      for bucket in s3.buckets.all():
          print(bucket.name)

* **Conversion to list()**::

      buckets = list(s3.buckets.all())

* **Batch actions (see below)**::

      s3.Bucket('my-bucket').objects.delete()

Filtering
---------
Some collections support extra arguments to filter the returned data set,
which are passed into the underlying service operation. Use the
:py:meth:`~boto3.resources.collection.Collection.filter` method to filter
the results::

    # S3 list all keys with the prefix '/photos'
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        for obj in bucket.objects.filter(Prefix='/photos'):
            print('{0}:{1}'.format(bucket.name, obj.key))

.. warning::

   Behind the scenes, the above example will call ``ListBuckets``,
   ``ListObjects``, and ``HeadObject`` many times. If you have a large
   number of S3 objects then this could incur a significant cost.

Chainability
------------
Collection methods are chainable. They return copies of the collection
rather than modifying the collection, including a deep copy of any
associated operation parameters. For example, this allows you
to build up multiple collections from a base which they all have
in common::

    # EC2 find instances
    ec2 = boto3.resource('ec2')
    base = ec2.instances.filter(InstanceIds=['id1', 'id2', 'id3'])

    filters = [{
        'name': 'tenancy',
        'value': 'dedicated'
    }]
    filtered1 = base.filter(Filters=filters)

    # Note, this does NOT modify the filters in ``filtered1``!
    filters.append({'name': 'instance-type', 'value': 't1.micro'})
    filtered2 = base.filter(Filters=filters)

    print('All instances:')
    for instance in base:
        print(instance.id)

    print('Dedicated instances:')
    for instance in filtered1:
        print(instance.id)

    print('Dedicated micro instances:')
    for instance in filtered2:
        print(instance.id)

Limiting Results
----------------
It is possible to limit the number of items returned from a collection
by using either the
:py:meth:`~boto3.resources.collection.ResourceCollection.limit` method or
keyword argument::

    # S3 iterate over first ten buckets
    for bucket in s3.buckets.limit(10):
        print(bucket.name)

    # Keyword argument example
    for bucket in s3.buckets.filter(limit=10):
        print(bucket.name)

In both cases, up to 10 items total will be returned. If you do not
have 10 buckets, then all of your buckets will be returned.

Controlling Page Size
---------------------
Collections automatically handle paging through results, but you may want
to control the number of items returned from a single service operation
call. You can do so using the
:py:meth:`~boto3.resources.collection.ResourceCollection.page_size` method
or keyword argument::

    # S3 iterate over all objects 100 at a time
    for obj in bucket.objects.page_size(100):
        print(obj.key)

    # Keyword argument example
    for obj in bucket.objects.all(page_size=100):
        print(obj.key)

By default, S3 will return 1000 objects at a time, so the above code
would let you process the items in smaller batches, which could be
beneficial for slow or unreliable internet connections.

Batch Actions
-------------
Some collections support batch actions, which are actions that operate
on an entire page of results at a time. They will automatically handle
pagination::

    # S3 delete everything in `my-bucket`
    s3 = boto3.resource('s3')
    s3.buckets('my-bucket').objects.delete()

.. danger::

   The above example will **completely erase all data** in the ``my-bucket``
   bucket! Please be careful with batch actions.
