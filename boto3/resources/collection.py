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

import copy
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

    :type model: :py:class:`~boto3.resources.model.Collection`
    :param model: Collection model
    :type parent: :py:class:`~boto3.resources.base.ServiceResource`
    :param parent: The collection's parent resource
    :type handler: :py:class:`~boto3.resources.response.ResourceHandler`
    :param handler: The resource response handler used to create resource
                    instances
    """
    def __init__(self, model, parent, handler, **kwargs):
        self._model = model
        self._parent = parent
        self._py_operation_name = xform_name(
            model.request.operation)
        self._handler = handler
        self._params = kwargs

    def __repr__(self):
        return '{0}({1}, {2})'.format(
            self.__class__.__name__,
            self._parent,
            '{0}.{1}'.format(
                self._parent.meta['service_name'],
                self._model.resource.type
            )
        )

    def __iter__(self):
        """
        A generator which yields resource instances after doing the
        appropriate service operation calls and handling any pagination
        on your behalf.
        """
        client = self._parent.meta['client']
        cleaned_params = self._params.copy()
        limit = cleaned_params.pop('limit', None)
        page_size = cleaned_params.pop('page_size', None)

        params = create_request_parameters(
            self._parent, self._model.request)
        params.update(cleaned_params)

        # Is this a paginated operation? If so, we need to get an
        # iterator for the various pages. If not, then we simply
        # call the operation and return the result as a single
        # page in a list. For non-paginated results, we just ignore
        # the page size parameter.
        if client.can_paginate(self._py_operation_name):
            logger.info('Calling paginated %s:%s with %r',
                        self._parent.meta['service_name'],
                        self._py_operation_name, params)
            paginator = client.get_paginator(self._py_operation_name)
            pages = paginator.paginate(
                max_items=limit, page_size=page_size, **params)
        else:
            logger.info('Calling %s:%s with %r',
                        self._parent.meta['service_name'],
                        self._py_operation_name, params)
            pages = [getattr(client, self._py_operation_name)(**params)]

        # Now that we have a page iterator or single page of results
        # we start processing and yielding individual items.
        count = 0
        for page in pages:
            for item in self._handler(self._parent, params, page):
                yield item

                # If the limit is set and has been reached, then
                # we stop processing items here.
                count += 1
                if limit is not None and count >= limit:
                    return

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
        params = copy.deepcopy(self._params)
        params.update(kwargs)
        clone = self.__class__(self._model, self._parent,
                               self._handler, **params)
        return clone

    def all(self, limit=None, page_size=None):
        """
        Get all items from the collection, optionally with a custom
        page size and item count limit.

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

        :type limit: int
        :param limit: Return no more than this many items
        :type page_size: int
        :param page_size: Fetch this many items per request
        :rtype: :py:class:`ResourceCollection`
        """
        return self._clone(limit=limit, page_size=page_size)

    def filter(self, **kwargs):
        """
        Get items from the collection, passing keyword arguments along
        as parameters to the underlying service operation, which are
        typically used to filter the results.

        This method returns an iterable generator which yields
        individual resource instances. Example use::

            # Iterate through items
            >>> for queue in sqs.queues.filter(Param='foo'):
            ...     print(queue.url)
            'https://url1'
            'https://url2'

            # Convert to list
            >>> queues = list(sqs.queues.filter(Param='foo'))
            >>> len(queues)
            2

        :rtype: :py:class:`ResourceCollection`
        """
        return self._clone(**kwargs)

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

    :type model: :py:class:`~boto3.resources.model.Collection`
    :param model: Collection model
    :type parent: :py:class:`~boto3.resources.base.ServiceResource`
    :param parent: The collection's parent resource
    :type factory: :py:class:`~boto3.resources.factory.ResourceFactory`
    :param factory: The resource factory to create new resources
    :type resource_defs: dict
    :param resource_defs: Service resource definitions.
    :type service_model: :ref:`botocore.model.ServiceModel`
    :param service_model: The Botocore service model
    """
    def __init__(self, model, parent, factory, resource_defs,
                 service_model):
        self._model = model
        operation_name = self._model.request.operation
        self._parent = parent

        search_path = model.path
        self._handler = ResourceHandler(search_path, factory, resource_defs,
            service_model, model.resource, operation_name)

    def __repr__(self):
        return '{0}({1}, {2})'.format(
            self.__class__.__name__,
            self._parent,
            '{0}.{1}'.format(
                self._parent.meta['service_name'],
                self._model.resource.type
            )
        )

    def iterator(self, **kwargs):
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        return ResourceCollection(self._model, self._parent,
                                  self._handler, **kwargs)

    # Set up some methods to proxy ResourceCollection methods
    def all(self, limit=None, page_size=None):
        return self.iterator(limit=limit, page_size=page_size)
    all.__doc__ = ResourceCollection.all.__doc__

    def filter(self, **kwargs):
        return self.iterator(**kwargs)
    filter.__doc__ = ResourceCollection.filter.__doc__

    def limit(self, count):
        return self.iterator(limit=count)
    limit.__doc__ = ResourceCollection.limit.__doc__

    def page_size(self, count):
        return self.iterator(page_size=count)
    page_size.__doc__ = ResourceCollection.page_size.__doc__
