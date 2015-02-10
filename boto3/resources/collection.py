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

from .action import BatchAction
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
                self._parent.meta.service_name,
                self._model.resource.type
            )
        )

    def __iter__(self):
        """
        A generator which yields resource instances after doing the
        appropriate service operation calls and handling any pagination
        on your behalf.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for obj in bucket.objects.all():
            ...     print(obj.key)
            'key1'
            'key2'

        """
        limit = self._params.get('limit', None)

        count = 0
        for page in self.pages():
            for item in page:
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

    def pages(self):
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        client = self._parent.meta.client
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
                        self._parent.meta.service_name,
                        self._py_operation_name, params)
            paginator = client.get_paginator(self._py_operation_name)
            pages = paginator.paginate(
                max_items=limit, page_size=page_size, **params)
        else:
            logger.info('Calling %s:%s with %r',
                        self._parent.meta.service_name,
                        self._py_operation_name, params)
            pages = [getattr(client, self._py_operation_name)(**params)]

        # Now that we have a page iterator or single page of results
        # we start processing and yielding individual items.
        count = 0
        for page in pages:
            page_items = []
            for item in self._handler(self._parent, params, page):
                page_items.append(item)

                # If the limit is set and has been reached, then
                # we stop processing items here.
                count += 1
                if limit is not None and count >= limit:
                    break

            yield page_items

            # Stop reading pages if we've reached out limit
            if limit is not None and count >= limit:
                break

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

            >>> for bucket in s3.buckets.limit(5):
            ...     print(bucket.name)
            'bucket1'
            'bucket2'
            'bucket3'
            'bucket4'
            'bucket5'

        :type count: int
        :param count: Return no more than this many items
        :rtype: :py:class:`ResourceCollection`
        """
        return self._clone(limit=count)

    def page_size(self, count):
        """
        Fetch at most this many resources per service request.

            >>> for obj in s3.Bucket('boto3').objects.page_size(100):
            ...     print(obj.key)

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

    Get whole pages of items:

        >>> for page in s3.Bucket('boto3').objects.pages():
        ...     for obj in page:
        ...         print(obj.key)

    A collection manager is not iterable. You **must** call one of the
    methods that return a :py:class:`ResourceCollection` before trying
    to iterate, slice, or convert to a list.

    See the :ref:`guide_collections` guide for a high-level overview
    of collections, including when remote service requests are performed.

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
    # The class to use when creating an iterator
    _collection_cls = ResourceCollection

    def __init__(self, model, parent, factory, resource_defs,
                 service_model):
        self._model = model
        operation_name = self._model.request.operation
        self._parent = parent

        search_path = model.resource.path
        self._handler = ResourceHandler(search_path, factory, resource_defs,
            service_model, model.resource, operation_name)

    def __repr__(self):
        return '{0}({1}, {2})'.format(
            self.__class__.__name__,
            self._parent,
            '{0}.{1}'.format(
                self._parent.meta.service_name,
                self._model.resource.type
            )
        )

    def iterator(self, **kwargs):
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        return self._collection_cls(self._model, self._parent,
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

    def pages(self):
        return self.iterator().pages()
    pages.__doc__ = ResourceCollection.pages.__doc__


class CollectionFactory(object):
    """
    A factory to create new
    :py:class:`CollectionManager` and :py:class:`ResourceCollection`
    subclasses from a :py:class:`~boto3.resources.model.Collection`
    model. These subclasses include methods to perform batch operations.
    """
    def load_from_definition(self, service_name, resource_name,
                             collection_name, model, resource_defs):
        """
        Loads a collection from a model, creating a new
        :py:class:`CollectionManager` subclass
        with the correct properties and methods, named based on the service
        and resource name, e.g. ec2.InstanceCollectionManager. It also
        creates a new :py:class:`ResourceCollection` subclass which is used
        by the new manager class.

        :type service_name: string
        :param service_name: Name of the service to look up
        :type resource_name: string
        :param resource_name: Name of the resource to look up. For services,
                              this should match the ``service_name``.
        :type model: dict
        :param model: The collection definition.
        :type resource_defs: dict
        :param resource_defs: The service's resource definitions, used to load
                              collection resources (e.g. ``sqs.Queue``).
        :rtype: Subclass of
                :py:class:`CollectionManager`
        :return: The collection class.
        """
        attrs = {}

        self._load_batch_actions(attrs, model)

        if service_name == resource_name:
            cls_name = '{0}.{1}Collection'.format(
                service_name, collection_name)
        else:
            cls_name = '{0}.{1}.{2}Collection'.format(
                service_name, resource_name, collection_name)

        collection_cls = type(str(cls_name), (ResourceCollection,),
                              attrs)

        attrs['_collection_cls'] = collection_cls
        cls_name += 'Manager'

        return type(str(cls_name), (CollectionManager,), attrs)

    def _load_batch_actions(self, attrs, model):
        """
        Batch actions on the collection become methods on both
        the collection manager and iterators.
        """
        for action_model in model.batch_actions:
            snake_cased = xform_name(action_model.name)
            attrs[snake_cased] = self._create_batch_action(
                snake_cased, action_model)

    def _create_batch_action(factory_self, snake_cased, action_model):
        """
        Creates a new method which makes a batch operation request
        to the underlying service API.
        """
        action = BatchAction(action_model)

        def batch_action(self, *args, **kwargs):
            return action(self, *args, **kwargs)

        batch_action.__name__ = str(snake_cased)
        batch_action.__doc__ = 'TODO'
        return batch_action
