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

from botocore import xform_name

from .action import ServiceAction
from .base import ServiceResource
from .collection import CollectionFactory
from .model import ResourceModel
from .response import all_not_none, build_identifiers
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
        meta = {
            'service_name': service_name,
            'identifiers': [],
            'data': None,
        }
        attrs = {
            'meta': meta,
        }

        logger.debug('Loading %s:%s', service_name, resource_name)

        resource_model = ResourceModel(resource_name, model, resource_defs)

        self._load_identifiers(attrs, meta, resource_model)
        self._load_subresources(attrs, service_name, resource_name,
                                resource_model, resource_defs, service_model)
        self._load_actions(attrs, resource_model, resource_defs,
                           service_model)
        self._load_attributes(attrs, meta, resource_model, service_model)
        self._load_collections(attrs, resource_model, resource_defs,
                               service_model)
        self._load_references(attrs, service_name, resource_name,
                              resource_model, resource_defs, service_model)

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
            snake_cased = xform_name(identifier.name)
            snake_cased = self._check_allowed_name(
                attrs, snake_cased, 'identifier', model.name)
            meta['identifiers'].append(snake_cased)
            attrs[snake_cased] = None

    def _load_subresources(self, attrs, service_name, resource_name,
                           model, resource_defs, service_model):
        """
        Creates subresource classes which hang off the instance. Each
        subresource is a bound partial method that returns a resource
        instance which shares the client and identifiers of the parent.
        """
        # Create dangling classes, e.g. SQS.Queue, SQS.Message
        if service_name == resource_name:
            # This is a service, so dangle all the resource_defs as if
            # they were subresources of the service itself.
            for name, resource_def in resource_defs.items():
                cls = self.load_from_definition(
                    service_name, name, resource_defs.get(name, {}),
                    resource_defs, service_model)
                attrs[name] = self._create_class_partial(cls)

        # For non-services, subresources are explicitly listed
        if model.sub_resources:
            identifiers = model.sub_resources.identifiers
            for name in model.sub_resources.resource_names:
                cls = self.load_from_definition(
                    service_name, name, resource_defs.get(name, {}),
                    resource_defs, service_model)
                attrs[name] = self._create_class_partial(
                    cls, identifiers=identifiers)

    def _load_actions(self, attrs, model, resource_defs, service_model):
        """
        Actions on the resource become methods, with the ``load`` method
        being a special case which sets internal data for attributes, and
        ``reload`` is an alias for ``load``.
        """
        if model.load:
            attrs['load'] = self._create_action(
                'load', model.load, resource_defs, service_model,
                is_load=True)
            attrs['reload'] = attrs['load']

        for action in model.actions:
            snake_cased = xform_name(action.name)
            snake_cased = self._check_allowed_name(
                attrs, snake_cased, 'action', model.name)
            attrs[snake_cased] = self._create_action(snake_cased,
                action, resource_defs, service_model)

    def _load_attributes(self, attrs, meta, model, service_model):
        """
        Load resource attributes based on the resource shape. The shape
        name is referenced in the resource JSON, but the shape itself
        is defined in the Botocore service JSON, hence the need for
        access to the ``service_model``.
        """
        if model.shape:
            shape = service_model.shape_for(model.shape)

            for name, member in shape.members.items():
                snake_cased = xform_name(name)
                if snake_cased in meta['identifiers']:
                    # Skip identifiers, these are set through other means
                    continue

                snake_cased = self._check_allowed_name(
                    attrs, snake_cased, 'attribute', model.name)
                attrs[snake_cased] = self._create_autoload_property(name,
                    snake_cased)

    def _load_collections(self, attrs, model, resource_defs, service_model):
        """
        Load resource collections from the model. Each collection becomes
        a :py:class:`~boto3.resources.collection.CollectionManager` instance
        on the resource instance, which allows you to iterate and filter
        through the collection's items.
        """
        for collection_model in model.collections:
            snake_cased = xform_name(collection_model.name)
            snake_cased = self._check_allowed_name(
                attrs, snake_cased, 'collection', model.name)

            attrs[snake_cased] = self._create_collection(
                attrs['meta']['service_name'], model.name, snake_cased,
                collection_model, resource_defs, service_model)

    def _load_references(self, attrs, service_name, resource_name,
                         model, resource_defs, service_model):
        """
        Load references, which are related resource instances. For example,
        an EC2 instance would have a ``vpc`` reference, which is an instance
        of an EC2 VPC resource.
        """
        for reference in model.references:
            snake_cased = xform_name(reference.resource.type)
            snake_cased = self._check_allowed_name(
                attrs, snake_cased, 'reference', model.name)
            attrs[snake_cased] = self._create_reference(
                reference.resource.type, snake_cased, reference, service_name,
                resource_name, model, resource_defs, service_model)

        for reference in model.reverse_references:
            snake_cased = xform_name(reference.resource.type)
            snake_cased = self._check_allowed_name(
                attrs, snake_cased, 'reference', model.name)
            attrs[snake_cased] = self._create_reference(
                reference.resource.type, snake_cased, reference, service_name,
                resource_name, model, resource_defs, service_model)

    def _check_allowed_name(self, attrs, name, category, resource_name):
        """
        Determine if a given name is allowed on the instance, and if not,
        then raise an exception. This prevents public attributes of the
        class from being clobbered, e.g. since we define ``Resource.meta``,
        no identifier may be named ``meta``. Another example: no action
        named ``queue_items`` may be added after an identifier of the same
        name has been added.

        One attempt is made in the event of a collision to remedy the
        situation. The ``category`` is appended to the name and the
        check is performed again. For example, if an action named
        ``get_frobs`` fails the test, then we try ``get_frobs_action``
        after logging a warning.

        :raises: ValueError
        """
        if name in attrs:
            logger.warning('%s `%s` would clobber existing %s'
                           ' resource attribute, going to try'
                           ' %s instead...', category, name,
                           resource_name, name + '_' + category)
            # TODO: Move this logic into the model and strictly
            #       define the loading order of categories. This
            #       will make documentation much simpler.
            name = name + '_' + category

        if name in attrs:
            raise ValueError('{0} `{1}` would clobber existing '
                             '{2} resource attribute'.format(
                                category, name, resource_name))

        return name

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
            if self.meta['data'] is None:
                if hasattr(self, 'load'):
                    self.load()
                else:
                    raise ResourceLoadException(
                        '{0} has no load method'.format(self.__class__.__name__))

            return self.meta['data'].get(name)

        property_loader.__name__ = str(snake_cased)
        property_loader.__doc__ = 'TODO'
        return property(property_loader)

    def _create_collection(factory_self, service_name, resource_name,
                           snake_cased, collection_model,
                           resource_defs, service_model):
        """
        Creates a new property on the resource to lazy-load a collection.
        """
        cls = factory_self._collection_factory.load_from_definition(
            service_name, resource_name, collection_model.name,
            collection_model, resource_defs)

        def get_collection(self):
            return cls(collection_model, self, factory_self,
                       resource_defs, service_model)

        get_collection.__name__ = str(snake_cased)
        get_collection.__doc__ = 'TODO'
        return property(get_collection)

    def _create_reference(factory_self, name, snake_cased, reference,
                          service_name, resource_name, model, resource_defs,
                          service_model):
        """
        Creates a new property on the resource to lazy-load a reference.
        """
        def get_reference(self):
            # We need to lazy-evaluate the reference to handle circular
            # references between resources. We do this by loading the class
            # when first accessed.
            # First, though, we need to see if we have the required
            # identifiers to instantiate the resource reference.
            identifiers = build_identifiers(
                reference.resource.identifiers, self, {}, {})
            resource = None
            if all_not_none(identifiers.values()):
                # Identifiers are present, so now we can create the resource
                # instance using them.
                resource_type = reference.resource.type
                cls = factory_self.load_from_definition(
                    service_name, name, resource_defs.get(resource_type),
                    resource_defs, service_model)
                resource = cls(**identifiers)
            return resource

        get_reference.__name__ = str(snake_cased)
        get_reference.__doc__ = 'TODO'
        return property(get_reference)

    def _create_class_partial(factory_self, resource_cls, identifiers=None):
        """
        Creates a new method which acts as a functools.partial, passing
        along the instance's low-level `client` to the new resource
        class' constructor.
        """
        # We need a new method here because we want access to the
        # instance's client.
        def create_resource(self, *args, **kwargs):
            pargs = []

            # Assumes that identifiers are in order, which lets you do
            # e.g. ``sqs.Queue('foo').Message('bar')`` to create a new message
            # linked with the ``foo`` queue and which has a ``bar`` receipt
            # handle. If we did kwargs here then future positional arguments
            # would lead to failure.
            if identifiers is not None:
                for key, value in identifiers.items():
                    pargs.append(getattr(self, xform_name(key)))

            return partial(resource_cls, *pargs,
                client=self.meta.get('client'))(*args, **kwargs)

        # Generate documentation about required and optional params
        doc = 'Create a new instance of {0}\n\nRequired identifiers:\n'

        for identifier in resource_cls.meta['identifiers']:
            doc += ':type {0}: string\n'.format(identifier)
            doc += ':param {0}: {0} identifier\n'.format(identifier)

        doc += '\nOptional params:\n'
        doc += ':type client: botocore.client\n'
        doc += ':param client: Low-level Botocore client instance\n'

        doc += '\n:rtype: {0}\n'.format(resource_cls)
        doc += ':return: A new resource instance'

        create_resource.__name__ = str(resource_cls.__name__)
        create_resource.__doc__ = doc.format(resource_cls)
        return create_resource

    def _create_action(factory_self, snake_cased, action_model, resource_defs,
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
                self.meta['data'] = response
        else:
            # We need a new method here because we want access to the
            # instance via ``self``.
            def do_action(self, *args, **kwargs):
                response = action(self, *args, **kwargs)

                if hasattr(self, 'load'):
                    # Clear cached data. It will be reloaded the next
                    # time that an attribute is accessed.
                    # TODO: Make this configurable in the future?
                    self.meta['data'] = None

                return response

        do_action.__name__ = str(snake_cased)
        do_action.__doc__ = 'TODO'
        return do_action
