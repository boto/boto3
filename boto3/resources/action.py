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
from .response import RawHandler, ResourceHandler


logger = logging.getLogger(__name__)


class ServiceAction(object):
    """
    A class representing a callable action on a resource, for example
    ``sqs.get_queue_by_name(...)`` or ``s3.Bucket('foo').delete()``.
    The action may construct parameters from existing resource identifiers
    and may return either a raw response or a new resource instance.

    :type action_def: dict
    :param action_def: The action definition.
    :type factory: ResourceFactory
    :param factory: The factory that created the resource class to which
                    this action is attached.
    :type resource_defs: dict
    :param resource_defs: Service resource definitions.
    :type service_model: :ref:`botocore.model.ServiceModel`
    :param service_model: The Botocore service model
    """
    def __init__(self, action_def, factory=None, resource_defs=None,
                 service_model=None):
        self.action_def = action_def

        search_path = action_def.get('path')

        # In the simplest case we just return the response, but if a
        # resource is defined, then we must create these before returning.
        response_resource_def = action_def.get('resource', {})
        if response_resource_def:
            self.response_handler = ResourceHandler(search_path, factory,
                resource_defs, service_model, response_resource_def,
                action_def.get('request', {}).get('operation'))
        else:
            self.response_handler = RawHandler(search_path)

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
        params = create_request_parameters(parent, request_def)
        params.update(kwargs)

        logger.info('Calling %s:%s with %r', parent.meta['service_name'],
            operation_name, params)

        response = getattr(parent.meta['client'], operation_name)(**params)

        logger.debug('Response: %r', response)

        return self.response_handler(parent, params, response)
