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
        """
        if version is None:
            version = get_latest_version(service)

        path = os.path.join(RESOURCE_ROOT,
                           '{0}-{1}.resources.json'.format(service, version))

        logger.info('Loading %s:%s from %s', service, name, path)
        model = json.load(open(path), object_pairs_hook=OrderedDict)

        if name is None:
            cls = self._load(service, service, model.get('service', {}),
                               model.get('resources', {}), version)
        else:
            cls = self._load(service, name,
                               model.get('resources', {}).get(name, {}),
                               {}, version)

        return cls

    def _load(self, service_name, resource_name, model, resource_defs, version):
        """
        Loads a resource from a model, creating a new ServiceResource subclass
        with the correct properties and methods, named based on the service
        and resource name, e.g. EC2InstanceResource.
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
        for name, resource_def in resource_defs.items():
            cls = self.create_class(service_name, name=name, version=version)
            attrs[name] = self._create_class_partial(cls)

        # Create the name based on the requested service and resource
        name = resource_name + 'Resource'
        if service_name != resource_name:
            name = service_name + name

        if not isinstance(name, str):
            # Python 2 requires string type names
            name = name.encode('utf-8')

        return type(name, (ServiceResource,), attrs)

    def _create_class_partial(factory_self, resource_cls):
        """
        Creates a new method which acts as a functools.partial, passing
        along the instance's low-level `client` to the new resource
        class' constructor.
        """
        # We need a new method here because we want access to the
        # instance's client.
        def create_resource(self, *args, **kwargs):
            return partial(resource_cls, client=self.client)(*args, **kwargs)

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
