# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import logging

from botocore import xform_name

from .params import create_request_parameters
from .response import ResourceHandler


logger = logging.getLogger(__name__)


class ResourceCollection(object):
    """
    Represents a collection of resources, which can be iterated through,
    optionally with filtering. Collections automatically handle pagination
    for you.

    See :ref:`guide_collections` for a high-level overview of collections,
    including when remote service requests are performed.

    :type definition: dict
    :param definition: Collection definition
    :type parent: ServiceResource
    :param parent: The collection's parent resource
    :type py_operation_name: string
    :param py_operation_name: Snake-cased operation name
    :type handler: :py:class:`~boto3.resources.response.ResourceHandler`
    :param handler: The resource response handler used to create resource
                    instances

    :ivar parent: The collection's parent resource
    :ivar params: A dict of key value pairs to send as parameters to the
                  underlying service operation

    """
    def __init__(self, definition, parent, py_operation_name, handler,
                 **kwargs):
        self.definition = definition
        self.parent = parent
        self.py_operation_name = py_operation_name
        self.handler = handler
        self.params = kwargs

    def __repr__(self):
        return '{0}({1}, {2})'.format(
            self.__class__.__name__,
            self.parent,
            '{0}.{1}'.format(
                self.parent.meta['service_name'],
                self.definition.get('resource', {}).get('type')
            )
        )

    def __iter__(self):
        """
        A generator which yields resource instances after doing the
        appropriate service operation calls and handling any pagination
        on your behalf.
        """
        client = self.parent.meta['client']
        cleaned_params = self.params.copy()
        limit = cleaned_params.pop('limit', None)
        page_size = cleaned_params.pop('page_size', None)

        params = create_request_parameters(self.parent,
            self.definition.get('request', {}))
        params.update(cleaned_params)

        # Is this a paginated operation? If so, we need to get an
        # iterator for the various pages. If not, then we simply
        # call the operation and return the result as a single
        # page in a list. For non-paginated results, we just ignore
        # the page size parameter.
        if client.can_paginate(self.py_operation_name):
            paginator = client.get_paginator(self.py_operation_name)
            pages = paginator.paginate(limit=limit,
                page_size=page_size, **params)
        else:
            logger.info('Calling %s:%s with %r',
                        self.parent.meta['service_name'],
                        self.py_operation_name, params)
            pages = [getattr(client, self.py_operation_name)(**params)]

        # Now that we have a page iterator or single page of results
        # we start processing and yielding individual items.
        count = 0
        for page in pages:
            for item in self.handler(self.parent, params, page):
                yield item

                # If the limit is set and has been reached, then
                # we stop processing items here.
                count += 1
                if limit is not None and count >= limit:
                    return

    def __getitem__(self, k):
        """
        Enable array indexing and slicing, for example:

            >>> collection.all()[2]
            Item2
            >>> collection.all()[:5]
            [Item1, Item2, Item3, Item4, Item5]
        """
        return list(self)[k]

    def _clone(self, **kwargs):
        """
        Create a clone of this collection. This is used by the methods
        below to provide a chainable interface that returns copies
        rather than the original. This allows things like:

            >>> base = collection.filter(Param1=1)
            >>> query1 = base.filter(Param2=2)
            >>> query2 = base.filter(Param3=3)
            >>> query1.params
            {'Param1': 1, 'Param2': 2}
            >>> query2.params
            {'Param1': 1, 'Param3': 3}

        :rtype: :py:class:`ResourceCollection`
        :return: A clone of this resource collection
        """
        params = self.params.copy()
        params.update(kwargs)
        clone = self.__class__(self.definition, self.parent,
                               self.py_operation_name, self.handler,
                               **params)
        return clone

    def all(self, **kwargs):
        """
        Get all items from the collection, optionally with a custom
        page size and item count limit. Any other keyword arguments
        are passed along as parameters to the underlying service
        operation, typically used to filter the results.

        This method returns an iterable generator which yields
        individual resource instances. Example use::

            # Iterate through items
            >>> for queue in sqs.queues.all():
            ...     print(queue.url)
            'https://url1'
            'https://url2'

            # Convert to list
            >>> queues = list(sqs.queues.all())
            >>> len(queues)
            2

        The ``filter`` method is an alias for ``all``.

        :type limit: int
        :param limit: Return no more than this many items
        :type page_size: int
        :param page_size: Fetch this many items per request
        :rtype: :py:class:`ResourceCollection`
        """
        return self._clone(**kwargs)

    filter = all

    def limit(self, count):
        """
        Return at most this many resources.

        :type count: int
        :param count: Return no more than this many items
        :rtype: :py:class:`ResourceCollection`
        """
        return self._clone(limit=count)

    def page_size(self, count):
        """
        Fetch at most this many resources per service request.

        :type count: int
        :param count: Fetch this many items per request
        :rtype: :py:class:`ResourceCollection`
        """
        return self._clone(page_size=count)


class CollectionManager(object):
    """
    A collection manager provides access to resource collection instances,
    which can be iterated and filtered. The manager exposes some
    convenience functions that are also found on resource collections,
    such as :py:meth:`~ResourceCollection.all` and
    :py:meth:`~ResourceCollection.filter`.

    Get all items::

        >>> for bucket in s3.buckets.all():
        ...     print(bucket.name)

    Get only some items via filtering::

        >>> for queue in sqs.queues.filter(QueueNamePrefix='AWS'):
        ...     print(queue.url)

    A collection manager is not iterable. You **must** call one of the
    methods that return a :py:class:`ResourceCollection` before trying
    to iterate, slice, or convert to a list.

    See :ref:`guide_collections` for a high-level overview of collections,
    including when remote service requests are performed.

    :type collection_def: dict
    :param collection_def: Collection definition
    :type parent: ServiceResource
    :param parent: The collection's parent resource
    :type factory: ResourceFactory
    :param factory: The resource factory to create new resources
    :type resource_defs: dict
    :param resource_defs: Service resource definitions.
    :type service_model: :ref:`botocore.model.ServiceModel`
    :param service_model: The Botocore service model

    :ivar parent: The collection's parent resource   
    """
    def __init__(self, collection_def, parent, factory, resource_defs,
                 service_model):
        self.definition = collection_def
        operation_name = self.definition['request']['operation']
        self.py_operation_name = xform_name(operation_name)
        self.parent = parent

        search_path = collection_def.get('path', '')
        response_resource_def = collection_def.get('resource')
        self.handler = ResourceHandler(search_path, factory, resource_defs,
            service_model, response_resource_def, operation_name)

    def __repr__(self):
        return '{0}({1}, {2})'.format(
            self.__class__.__name__,
            self.parent,
            '{0}.{1}'.format(
                self.parent.meta['service_name'],
                self.definition.get('resource', {}).get('type')
            )
        )

    def iterator(self, **kwargs):
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        return ResourceCollection(self.definition, self.parent,
                                  self.py_operation_name, self.handler,
                                  **kwargs)

    # Set up some methods to proxy ResourceCollection methods
    def all(self, **kwargs):
        return self.iterator(**kwargs)
    all.__doc__ = ResourceCollection.all.__doc__
    filter = all

    def limit(self, count):
        return self.iterator(limit=count)
    limit.__doc__ = ResourceCollection.limit.__doc__

    def page_size(self, count):
        return self.iterator(page_size=count)
    page_size.__doc__ = ResourceCollection.page_size.__doc__
