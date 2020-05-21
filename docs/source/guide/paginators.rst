Paginators
==========

Some AWS operations return results that are incomplete and require subsequent
requests in order to attain the entire result set. The process of sending
subsequent requests to continue where a previous request left off is called
*pagination*. For example, the ``list_objects`` operation of Amazon S3
returns up to 1000 objects at a time, and you must send subsequent requests
with the appropriate ``Marker`` in order to retrieve the next *page* of
results.

*Paginators* are a feature of boto3 that act as an abstraction over the
process of iterating over an entire result set of a truncated API operation.


Creating paginators
-------------------

Paginators are created via the ``get_paginator()`` method of a boto3
client. The ``get_paginator()`` method accepts an operation name and returns
a reusable ``Paginator`` object. You then call the ``paginate`` method of the
Paginator, passing in any relevant operation parameters to apply to the
underlying API operation. The ``paginate`` method then returns an iterable
``PageIterator``::

    import boto3

    # Create a client
    client = boto3.client('s3', region_name='us-west-2')

    # Create a reusable Paginator
    paginator = client.get_paginator('list_objects')

    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(Bucket='my-bucket')

    for page in page_iterator:
        print(page['Contents'])


Customizing page iterators
~~~~~~~~~~~~~~~~~~~~~~~~~~

You must call the ``paginate`` method of a Paginator in order to iterate over
the pages of API operation results. The ``paginate`` method accepts a
``PaginationConfig`` named argument that can be used to customize the
pagination::

    paginator = client.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket='my-bucket',
                                       PaginationConfig={'MaxItems': 10})

``MaxItems``
    Limits the maximum number of total returned items returned while
    paginating.

``StartingToken``
    Can be used to modify the starting marker or token of a paginator. This
    argument if useful for resuming pagination from a previous token or
    starting pagination at a known position.

``PageSize``
    Controls the number of items returned per page of each result.

    .. note::

        Services may choose to return more or fewer items than specified in the
        ``PageSize`` argument depending on the service, the operation, or the
        resource you are paginating.


Filtering results
-----------------

Many Paginators can be filtered server-side with options that are passed
through to each underlying API call. For example,
:py:meth:`S3.Paginator.list_objects.paginate` accepts a ``Prefix`` parameter
used to filter the paginated results by prefix server-side before sending them
to the client::

    import boto3
    
    client = boto3.client('s3', region_name='us-west-2')
    paginator = client.get_paginator('list_objects')
    operation_parameters = {'Bucket': 'my-bucket',
                            'Prefix': 'foo/baz'}
    page_iterator = paginator.paginate(**operation_parameters)
    for page in page_iterator:
        print(page['Contents'])


Filtering results with JMESPath
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`JMESPath <http://jmespath.org>`_ is a query language for JSON that can be used
directly on paginated results. You can filter results client-side using
JMESPath expressions that are applied to each page of results through the
``search`` method of a ``PageIterator``.

.. code-block:: python

    import boto3
    
    client = boto3.client('s3', region_name='us-west-2')
    paginator = client.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket='my-bucket')
    filtered_iterator = page_iterator.search("Contents[?Size > `100`][]")
    for key_data in filtered_iterator:
        print(key_data)

When filtering with JMESPath expressions, each page of results that is yielded
by the paginator is mapped through the JMESPath expression. If a JMESPath
expression returns a single value that is not an array, that value is yielded
directly. If the result of applying the JMESPath expression to a page of
results is a list, then each value of the list is yielded individually
(essentially implementing a flat map). For example, in the above expression,
each key that has a ``Size`` greater than `100` is yielded by the
``filtered_iterator``.
