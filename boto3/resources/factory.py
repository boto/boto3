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
from functools import partial

from .action import ServiceAction
from .action import WaiterAction
from .base import ResourceMeta, ServiceResource
from .collection import CollectionFactory
from .model import ResourceModel
from .response import build_identifiers, ResourceHandler
from ..exceptions import ResourceLoadException


logger = logging.getLogger(__name__)


class ResourceFactory(object):
    """
    A factory to create new :py:class:`~boto3.resources.base.ServiceResource`
    classes from a :py:class:`~boto3.resources.model.ResourceModel`. There are
    two types of lookups that can be done: one on the service itself (e.g. an
    SQS resource) and another on models contained within the service (e.g. an
    SQS Queue resource).
    """
    def __init__(self):
        self._collection_factory = CollectionFactory()

    def load_from_definition(self, service_name, resource_name, model,
                             resource_defs, service_model):
        """
        Loads a resource from a model, creating a new
        :py:class:`~boto3.resources.base.ServiceResource` subclass
        with the correct properties and methods, named based on the service
        and resource name, e.g. EC2.Instance.

        :type service_name: string
        :param service_name: Name of the service to look up
        :type resource_name: string
        :param resource_name: Name of the resource to look up. For services,
                              this should match the ``service_name``.
        :type model: dict
        :param model: The service or resource definition.
        :type resource_defs: dict
        :param resource_defs: The service's resource definitions, used to load
                              subresources (e.g. ``sqs.Queue``).
        :type service_model: ``botocore.model.ServiceModel``
        :param service_model: The Botocore service model, required only if the
                              resource shape contains members. This is used to
                              expose lazy-loaded attributes on the resource.
        :rtype: Subclass of :py:class:`~boto3.resources.base.ServiceResource`
        :return: The service or resource class.
        """
        # Set some basic info
        meta = ResourceMeta(service_name)
        attrs = {
            'meta': meta,
        }

        logger.debug('Loading %s:%s', service_name, resource_name)

        resource_model = ResourceModel(resource_name, model, resource_defs)

        shape = None
        if resource_model.shape:
            shape = service_model.shape_for(resource_model.shape)
        resource_model.load_rename_map(shape)

        self._load_identifiers(attrs, meta, resource_model)
        self._load_actions(attrs, resource_model, resource_defs,
                           service_model)
        self._load_attributes(attrs, meta, resource_model, service_model)
        self._load_collections(attrs, resource_model, resource_defs,
                               service_model)
        self._load_has_relations(attrs, service_name, resource_name,
                                 resource_model, resource_defs, service_model)
        self._load_waiters(attrs, resource_model)

        # Create the name based on the requested service and resource
        cls_name = resource_name
        if service_name != resource_name:
            cls_name = service_name + '.' + cls_name

        return type(str(cls_name), (ServiceResource,), attrs)

    def _load_identifiers(self, attrs, meta, model):
        """
        Populate required identifiers. These are arguments without which
        the resource cannot be used. Identifiers become arguments for
        operations on the resource.
        """
        for identifier in model.identifiers:
            meta.identifiers.append(identifier.name)
            attrs[identifier.name] = None

    def _load_actions(self, attrs, model, resource_defs, service_model):
        """
        Actions on the resource become methods, with the ``load`` method
        being a special case which sets internal data for attributes, and
        ``reload`` is an alias for ``load``.
        """
        if model.load:
            attrs['load'] = self._create_action(
                model.load, resource_defs, service_model, is_load=True)
            attrs['reload'] = attrs['load']

        for action in model.actions:
            attrs[action.name] = self._create_action(action, resource_defs,
                                                     service_model)

    def _load_attributes(self, attrs, meta, model, service_model):
        """
        Load resource attributes based on the resource shape. The shape
        name is referenced in the resource JSON, but the shape itself
        is defined in the Botocore service JSON, hence the need for
        access to the ``service_model``.
        """
        if model.shape:
            shape = service_model.shape_for(model.shape)

            attributes = model.get_attributes(shape)
            for name, (orig_name, member) in attributes.items():
                attrs[name] = self._create_autoload_property(orig_name, name)

    def _load_collections(self, attrs, model, resource_defs, service_model):
        """
        Load resource collections from the model. Each collection becomes
        a :py:class:`~boto3.resources.collection.CollectionManager` instance
        on the resource instance, which allows you to iterate and filter
        through the collection's items.
        """
        for collection_model in model.collections:
            attrs[collection_model.name] = self._create_collection(
                attrs['meta'].service_name, model.name,
                collection_model, resource_defs, service_model)

    def _load_has_relations(self, attrs, service_name, resource_name,
                            model, resource_defs, service_model):
        """
        Load related resources, which are defined via a ``has``
        relationship but conceptually come in two forms:

        1. A reference, which is a related resource instance and can be
           ``None``, such as an EC2 instance's ``vpc``.
        2. A subresource, which is a resource constructor that will always
           return a resource instance which shares identifiers/data with
           this resource, such as ``s3.Bucket('name').Object('key')``.
        """
        for reference in model.references:
            # This is a dangling reference, i.e. we have all
            # the data we need to create the resource, so
            # this instance becomes an attribute on the class.
            attrs[reference.name] = self._create_reference(
                reference.resource.type, reference,
                service_name, resource_name, model, resource_defs,
                service_model)

        for subresource in model.subresources:
            # This is a sub-resource class you can create
            # by passing in an identifier, e.g. s3.Bucket(name).
            name = subresource.resource.type
            attrs[subresource.name] = self._create_class_partial(
                name, subresource, service_name, resource_name, model,
                resource_defs, service_model)


    def _load_waiters(self, attrs, model):
        """
        Load resource waiters from the model. Each waiter allows you to
        wait until a resource reaches a specific state by polling the state
        of the resource.
        """
        for waiter in model.waiters:
            attrs[waiter.name] = self._create_waiter(waiter)

    def _create_autoload_property(factory_self, name, snake_cased):
        """
        Creates a new property on the resource to lazy-load its value
        via the resource's ``load`` method (if it exists).
        """
        # The property loader will check to see if this resource has already
        # been loaded and return the cached value if possible. If not, then
        # it first checks to see if it CAN be loaded (raise if not), then
        # calls the load before returning the value.
        def property_loader(self):
            if self.meta.data is None:
                if hasattr(self, 'load'):
                    self.load()
                else:
                    raise ResourceLoadException(
                        '{0} has no load method'.format(self.__class__.__name__))

            return self.meta.data.get(name)

        property_loader.__name__ = str(snake_cased)
        property_loader.__doc__ = 'TODO'
        return property(property_loader)

    def _create_waiter(factory_self, waiter_model):
        """
        Creates a new wait method for each resource where both a waiter and
        resource model is defined.
        """
        waiter = WaiterAction(waiter_model,
                              waiter_resource_name=waiter_model.name)
        def do_waiter(self, *args, **kwargs):
            waiter(self, *args, **kwargs)

        do_waiter.__name__ = str(waiter_model.name)
        do_waiter.__doc__ = 'TODO'
        return do_waiter

    def _create_collection(factory_self, service_name, resource_name,
                           collection_model, resource_defs, service_model):
        """
        Creates a new property on the resource to lazy-load a collection.
        """
        cls = factory_self._collection_factory.load_from_definition(
            service_name, resource_name, collection_model.name,
            collection_model, resource_defs)

        def get_collection(self):
            return cls(collection_model, self, factory_self,
                       resource_defs, service_model)

        get_collection.__name__ = str(collection_model.name)
        get_collection.__doc__ = 'TODO'
        return property(get_collection)

    def _create_reference(factory_self, name, reference, service_name,
                          resource_name, model, resource_defs, service_model):
        """
        Creates a new property on the resource to lazy-load a reference.
        """
        # References are essentially an action with no request
        # or response, so we can re-use the response handlers to
        # build up resources from identifiers and data members.
        handler = ResourceHandler(reference.resource.path, factory_self,
                                  resource_defs, service_model,
                                  reference.resource)

        # Are there any identifiers that need access to data members?
        # This is important when building the resource below since
        # it requires the data to be loaded.
        needs_data = any(i.source == 'data' for i in
                         reference.resource.identifiers)

        def get_reference(self):
            # We need to lazy-evaluate the reference to handle circular
            # references between resources. We do this by loading the class
            # when first accessed.
            # This is using a *response handler* so we need to make sure
            # our data is loaded (if possible) and pass that data into
            # the handler as if it were a response. This allows references
            # to have their data loaded properly.
            if needs_data and self.meta.data is None and hasattr(self, 'load'):
                self.load()
            return handler(self, {}, self.meta.data)

        get_reference.__name__ = str(reference.name)
        get_reference.__doc__ = 'TODO'
        return property(get_reference)

    def _create_class_partial(factory_self, name, subresource,
                              service_name, resource_name, model,
                              resource_defs, service_model):
        """
        Creates a new method which acts as a functools.partial, passing
        along the instance's low-level `client` to the new resource
        class' constructor.
        """
        # We need a new method here because we want access to the
        # instance's client.
        def create_resource(self, *args, **kwargs):
            positional_args = []

            # We lazy-load the class to handle circular references.
            resource_cls = factory_self.load_from_definition(
                service_name, name, resource_defs.get(name, {}),
                resource_defs, service_model)

            # Assumes that identifiers are in order, which lets you do
            # e.g. ``sqs.Queue('foo').Message('bar')`` to create a new message
            # linked with the ``foo`` queue and which has a ``bar`` receipt
            # handle. If we did kwargs here then future positional arguments
            # would lead to failure.
            identifiers = subresource.resource.identifiers
            if identifiers is not None:
                for identifier, value in build_identifiers(identifiers, self):
                    positional_args.append(value)

            return partial(resource_cls, *positional_args,
                client=self.meta.client)(*args, **kwargs)

        create_resource.__name__ = str(name)
        create_resource.__doc__ = 'TODO'
        return create_resource

    def _create_action(factory_self, action_model, resource_defs,
                       service_model, is_load=False):
        """
        Creates a new method which makes a request to the underlying
        AWS service.
        """
        # Create the action in in this closure but before the ``do_action``
        # method below is invoked, which allows instances of the resource
        # to share the ServiceAction instance.
        action = ServiceAction(action_model, factory=factory_self,
            resource_defs=resource_defs, service_model=service_model)

        # A resource's ``load`` method is special because it sets
        # values on the resource instead of returning the response.
        if is_load:
            # We need a new method here because we want access to the
            # instance via ``self``.
            def do_action(self, *args, **kwargs):
                response = action(self, *args, **kwargs)
                self.meta.data = response
        else:
            # We need a new method here because we want access to the
            # instance via ``self``.
            def do_action(self, *args, **kwargs):
                response = action(self, *args, **kwargs)

                if hasattr(self, 'load'):
                    # Clear cached data. It will be reloaded the next
                    # time that an attribute is accessed.
                    # TODO: Make this configurable in the future?
                    self.meta.data = None

                return response

        do_action.__name__ = str(action_model.name)
        do_action.__doc__ = 'TODO'
        return do_action
