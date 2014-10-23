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

from botocore import xform_name


def create_request_parameters(parent, request_model):
    """
    Handle request parameters that can be filled in from identifiers,
    resource data members or constants.

    :type parent: ServiceResource
    :param parent: The resource instance to which this action is attached.
    :type request_model: :py:class:`~boto3.resources.model.Request`
    :param request_model: The action request model.
    :rtype: dict
    :return: Pre-filled parameters to be sent to the request operation.
    """
    params = {}

    for param in request_model.params:
        source = param.source
        source_type = param.source_type
        target = param.target

        if source_type in ['identifier', 'dataMember']:
            # Resource identifier, e.g. queue.url
            # If this is a dataMember then it may incur a load
            # action before returning the value.
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
