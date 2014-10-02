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

Filtering
---------
Some collections support extra arguments to filter the returned data set,
which are passed into the underlying service operation. Use the
:py:meth:`~boto3.resources.collection.Collection.filter` method to filter
the results::

    # S3 list all keys
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        for obj in bucket.objects.filter(Prefix='/photos'):
            print('{0}:{1}'.format(bucket.name, obj.key))

.. warning::

   Behind the scenes, the above example will call ``ListBuckets``,
   ``ListObjects``, and ``HeadObject`` many times. If you have a large
   number of S3 objects then this could incur a significant cost.

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
