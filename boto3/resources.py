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
import os
from functools import partial

import jmespath
from botocore import xform_name

import boto3
from .compat import json, OrderedDict


# Where to find the resource objects
RESOURCE_ROOT = os.path.join(
    os.path.dirname(__file__),
    'data',
    'resources'
)


logger = logging.getLogger(__name__)


def get_latest_version(name):
    """
    Get the latest version number given a service name.

    :type name: string
    :param name: Service name, e.g. 'sqs'
    :rtype: string
    :return: Service version, e.g. 2012-11-05
    """
    entries = os.listdir(RESOURCE_ROOT)
    entries = [i for i in entries if i.startswith(name + '-')]
    return sorted(entries, reverse=True)[0][len(name) + 1:len(name) + 11]


class ServiceAction(object):
    """
    A class representing a callable action on a resource, for example
    ``sqs.get_queue_by_name(...)`` or ``s3.Bucket('foo').delete()``.
    The action may construct parameters from existing resource identifiers
    and may return either a raw response or a new resource instance.

    TODO: Move this to its own file

    :type factory: ResourceFactory
    :param factory: The factory that created the resource class to which
                    this action is attached.
    :type action_def: dict
    :param action_def: The action definition.
    :type resource_defs: dict
    :param resource_defs: Service resource definitions.
    """
    def __init__(self, factory, action_def, resource_defs):
        self.factory = factory
        self.action_def = action_def
        self.resource_defs = resource_defs

    def create_request_parameters(self, parent, request_def):
        """
        Handle request parameters that can be filled in from identifiers,
        resource data members or constants.

        :type parent: ServiceResource
        :param parent: The resource instance to which this action is attached.
        :type request_def: dict
        :param request_def: The action request definition.
        :rtype: dict
        :return: Pre-filled parameters to be sent to the request operation.
        """
        params = {}

        for param in request_def.get('params', []):
            source = param.get('source', '')
            source_type = param.get('sourceType', '')
            target = param.get('target', '')

            if source_type in ['identifier', 'dataMember']:
                # Resource identifier, e.g. queue.url
                params[target] = getattr(parent, xform_name(source))
            elif source_type in ['string', 'integer', 'boolean']:
                # These are hard-coded values in the definition
                params[target] = source
            else:
                raise NotImplementedError(
                    'Unsupported source type: {0}'.format(source_type))

        return params

    def __call__(self, parent, *args, **kwargs):
        """
        Perform the action's request operation after building operation
        parameters and build any defined resources from the response.

        :type parent: ServiceResource
        :param parent: The resource instance to which this action is attached.
        :rtype: dict or ServiceResource or list(ServiceResource)
        :return: The response, either as a raw dict or resource instance(s).
        """
        request_def = self.action_def.get('request', {})
        operation_name = xform_name(request_def.get('operation', ''))

        # First, build predefined params and then update with the
        # user-supplied kwargs, which allows overriding the pre-built
        # params if needed.
        params = self.create_request_parameters(parent, request_def)
        params.update(kwargs)

        logger.info('Calling %s:%s with %r', parent.service_name,
            operation_name, params)

        response = getattr(parent.client, operation_name)(**params)

        logger.debug('Response: %r', response)

        return response


class ServiceResource(object):
    """
    A base class for resources.

    :type client: botocore.client
    :param client: A low-level Botocore client instance
    """
    def __init__(self, *args, **kwargs):
        # Create a default client if none was passed
        if kwargs.get('client') is not None:
            self.client = kwargs.get('client')
        else:
            self.client = boto3.client(self.service_name)

        # Allow setting identifiers as positional arguments in the order
        # in which they were defined in the ResourceJSON.
        for i, value in enumerate(args):
            setattr(self, self.identifiers[i], value)

        # Allow setting identifiers via keyword arguments. Here we need
        # extra logic to ignore other keyword arguments like ``client``.
        for name, value in kwargs.items():
            if name == 'client':
                continue

            if name not in self.identifiers:
                raise ValueError('Unknown keyword argument: {0}'.format(name))

            setattr(self, name, value)

        # Validate that all identifiers have been set.
        for identifier in self.identifiers:
            if getattr(self, identifier) is None:
                raise ValueError(
                    'Required parameter {0} not set'.format(identifier))

    def __str__(self):
        return "{0}: {1} in {2}".format(
            self.__class__.__name__,
            self.service_name,
            self.client.endpoint.region_name,
        )


class ResourceFactory(object):
    """
    A factory to create new ``ServiceResource`` classes from a ResourceJSON
    description. There are two types of lookups that can be done: one on the
    service itself (e.g. an SQS resource) and another on models contained
    within the service (e.g. an SQS Queue resource).

        >>> factory = ResourceFactory()
        >>> S3Resource = factory.create_class('s3')
        >>> S3BucketResource = factory.create_class('s3', name='Bucket')
        >>> SQSResource = factory.create_class('sqs')
        >>> SQSQueueResource = factory.create_class('sqs', name='Queue')

    """
    def create_class(self, service, name=None, version=None):
        """
        Create a new resource class for a service or service resource.

        :type service: string
        :param service: Name of the service to look up
        :type name: string
        :param name: Name of the resource to look up. If not given, then the
                     service resource itself is returned.
        :type version: string
        :param version: The service version to load. A value of ``None`` will
                        load the latest available version.
        :rtype: Subclass of ``ServiceResource``
        :return: The service or resource class.
        """
        if version is None:
            version = get_latest_version(service)

        path = os.path.join(RESOURCE_ROOT,
                           '{0}-{1}.resources.json'.format(service, version))

        logger.info('Loading %s:%s from %s', service, name, path)
        model = json.load(open(path), object_pairs_hook=OrderedDict)

        resource_defs = model.get('resources', {})

        if name is None:
            cls = self.load_from_definition(service, service,
                model.get('service', {}), resource_defs)
        else:
            cls = self.load_from_definition(service, name,
                resource_defs.get(name, {}), resource_defs)

        return cls

    def load_from_definition(self, service_name, resource_name, model,
                             resource_defs):
        """
        Loads a resource from a model, creating a new ServiceResource subclass
        with the correct properties and methods, named based on the service
        and resource name, e.g. EC2InstanceResource.

        :type service: string
        :param service: Name of the service to look up
        :type resource_name: string
        :param resource_name: Name of the resource to look up. For services,
                              this should match the ``service_name``.
        :type model: dict
        :param model: The service or resource definition.
        :type resource_defs: dict
        :param resource_defs: The service's resource definitions, used to load
                              subresources (e.g. ``sqs.Queue``).
        :rtype: Subclass of ``ServiceResource``
        :return: The service or resource class.
        """
        # Set some basic info
        attrs = {
            'service_name': service_name,
            'model': model,
            'identifiers': [],
        }

        # Populate required identifiers. These are arguments without which
        # the resource cannot be used. Identifiers become arguments for
        # operations on the resource.
        for identifier in model.get('identifiers', []):
            snake_cased = xform_name(identifier['name'])
            attrs['identifiers'].append(snake_cased)
            attrs[snake_cased] = None

        # Create dangling classes, e.g. SQS.Queue, SQS.Message
        if service_name == resource_name:
            # This is a service, so dangle all the resource_defs as if
            # they were subresources of the service itself.
            for name, resource_def in resource_defs.items():
                cls = self.load_from_definition(service_name, name,
                    resource_defs.get(name), resource_defs)
                attrs[name] = self._create_class_partial(cls)

        # For non-services, subresources are explicitly listed
        sub_resources = model.get('subResources', {})
        if sub_resources:
            identifiers = sub_resources.get('identifiers', {})
            for name in sub_resources.get('resources'):
                klass = self.load_from_definition(service_name, name,
                    resource_defs.get(name), resource_defs)
                attrs[name] = self._create_class_partial(klass,
                    identifiers=identifiers)

        for name, action in model.get('actions', {}).items():
            snake_cased = xform_name(name)
            attrs[snake_cased] = self._create_action(service_name,
                name, snake_cased, action, resource_defs)

        # Create the name based on the requested service and resource
        name = resource_name + 'Resource'
        if service_name != resource_name:
            name = service_name + name

        if not isinstance(name, str):
            # Python 2 requires string type names
            name = name.encode('utf-8')

        return type(name, (ServiceResource,), attrs)

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

            return partial(resource_cls, *pargs, client=self.client)(*args,
                                                                     **kwargs)

        # Generate documentation about required and optional params
        doc = 'Create a new instance of {0}\n\nRequired identifiers:\n'

        for identifier in resource_cls.identifiers:
            doc += ':type {0}: string\n'.format(identifier)
            doc += ':param {0}: {0} identifier\n'.format(identifier)

        doc += '\nOptional params:\n'
        doc += ':type client: botocore.client\n'
        doc += ':param client: Low-level Botocore client instance\n'

        doc += '\n:rtype: {0}\n'.format(resource_cls)
        doc += ':return: A new resource instance'

        create_resource.__name__ = resource_cls.__name__
        create_resource.__doc__ = doc.format(resource_cls)
        return create_resource

    def _create_action(factory_self, service_name, action_name,
                       snake_cased, action_def, resource_defs):
        """
        Creates a new method which makes a request to the underlying
        AWS service.
        """
        # Create the action in in this closure but before the ``do_action``
        # method below is invoked, which allows instances of the resource
        # to share the ServiceAction instance.
        action = ServiceAction(factory_self, action_def, resource_defs)

        # We need a new method here because we want access to the
        # instance via ``self``.
        def do_action(self, *args, **kwargs):
            return action(self, *args, **kwargs)

        if not isinstance(snake_cased, str):
            snake_cased = snake_cased.encode('utf-8')

        do_action.__name__ = snake_cased
        do_action.__doc__ = 'TODO'
        return do_action
