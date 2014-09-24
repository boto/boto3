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

import jmespath
from botocore import xform_name


logger = logging.getLogger(__name__)


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
    :type service_model: `botocore.model.ServiceModel`
    :param service_model: The Botocore service model
    """
    def __init__(self, factory, action_def, resource_defs, service_model):
        self.factory = factory
        self.action_def = action_def
        self.resource_defs = resource_defs
        self.service_model = service_model

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
                value = getattr(parent, xform_name(source))
            elif source_type in ['string', 'integer', 'boolean']:
                # These are hard-coded values in the definition
                value = source
            else:
                raise NotImplementedError(
                    'Unsupported source type: {0}'.format(source_type))

            # Basic reverse jmespath support for lists
            # TODO: I believe this may get added into jmespath eventually?
            # TODO: support foo.bar.baz and foo.bar[0].baz
            # jmespath.create_structure(params, target, value)
            if target.endswith('[]'):
                params[target[:-2]] = [value]
            elif target.endswith('[0]'):
                params[target[:-3]] = [value]
            else:
                params[target] = value

        return params

    def create_response_resource(self, parent, params, resource_def, response):
        """
        Creates a new resource or list of new resources from the low-level
        response based on the given response resource definition.

        :type parent: ServiceResource
        :param parent: The resource instance to which this action is attached.
        :type params: dict
        :param params: Request parameters sent to the service.
        :type resource_def: dict
        :param resource_def: Response resource definition.
        :type response: dict
        :param response: Low-level operation response.
        :rtype: ServiceResource or list(ServiceResource)
        :return: New resource instance(s).
        """
        resource_name = resource_def.get('type', '')
        resource_cls = self.factory.load_from_definition(
            parent.meta['service_name'], resource_name,
            self.resource_defs.get(resource_name), self.resource_defs,
            self.service_model)

        raw_response = response
        search_response = response
        path = self.action_def.get('path', None)
        if path:
            search_response = jmespath.search(path, raw_response)

        # First, we parse all the identifiers, then create the individual
        # response resources using them. Any identifiers that are lists
        # will have one item consumed from the front of the list for each
        # resource that is instantiated. Items which are not a list will
        # be set as the same value on each new resource instance.
        identifiers = {}
        for identifier in resource_def.get('identifiers', []):
            source = identifier.get('source', '')
            source_type = identifier.get('sourceType')
            target = identifier.get('target')

            if source_type == 'responsePath':
                value = jmespath.search(source, raw_response)
                identifiers[xform_name(target)] = value
            elif source_type in ['identifier', 'dataMember']:
                value = getattr(parent, xform_name(source))
                identifiers[xform_name(target)] = value
            elif source_type == 'requestParameter':
                value = params[source]
                identifiers[xform_name(target)] = value
            else:
                raise NotImplementedError(
                    'Unsupported source type: {0}'.format(source_type))

        if isinstance(search_response, list):
            response = []
            for response_item in search_response:
                response.append(self.handle_response_item(resource_cls,
                    parent, identifiers))
        else:
            response = self.handle_response_item(resource_cls,
                parent, identifiers)

        return response

    def handle_response_item(self, resource_cls, parent, identifiers):
        """
        Handles the creation of a single response item by setting
        parameters and creating the appropriate resource instance.

        :type resource_cls: ServiceResource subclass
        :param resource_cls: The resource class to instantiate.
        :type parent: ServiceResource
        :param parent: The resource instance to which this action is attached.
        :type identifiers: dict
        :param identifiers: Map of identifier names to value or values.
        :rtype: ServiceResource
        :return: New resource instance.
        """
        kwargs = {
            'client': parent.meta.get('client'),
        }

        for name, value in identifiers.items():
            # If value is a list, then consume the next item
            if isinstance(value, list):
                value = value.pop(0)

            kwargs[name] = value

        return resource_cls(**kwargs)

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

        logger.info('Calling %s:%s with %r', parent.meta['service_name'],
            operation_name, params)

        response = getattr(parent.meta['client'], operation_name)(**params)

        logger.debug('Response: %r', response)

        # In the simplest case we just return the response, but if a
        # resource is defined, then we must create these before returning.
        response_resource_def = self.action_def.get('resource', {})
        if response_resource_def:
            response = self.create_response_resource(parent, params,
                response_resource_def, response)

        return response
