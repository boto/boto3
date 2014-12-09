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

import re

from botocore import xform_name


INDEX_RE = re.compile('\[(.*)\]$')


def create_request_parameters(parent, request_model, params=None):
    """
    Handle request parameters that can be filled in from identifiers,
    resource data members or constants.

    By passing ``params``, you can invoke this method multiple times and
    build up a parameter dict over time, which is particularly useful
    for reverse JMESPath expressions that append to lists.

    :type parent: ServiceResource
    :param parent: The resource instance to which this action is attached.
    :type request_model: :py:class:`~boto3.resources.model.Request`
    :param request_model: The action request model.
    :type params: dict
    :param params: If set, then add to this existing dict. It is both
                   edited in-place and returned.
    :rtype: dict
    :return: Pre-filled parameters to be sent to the request operation.
    """
    if params is None:
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

        build_param_structure(params, target, value)

    return params

def build_param_structure(params, target, value):
    """
    This method provides a basic reverse JMESPath implementation that
    lets you go from a JMESPath-like string to a possibly deeply nested
    object. The ``params`` are mutated in-place, so subsequent calls
    can modify the same element by its index.

        >>> build_param_structure(params, 'test[0]', 1)
        >>> print(params)
        {'test': [1]}

        >>> build_param_structure(params, 'foo.bar[0].baz', 'hello world')
        >>> print(params)
        {'test': [1], 'foo': {'bar': [{'baz': 'hello, world'}]}}

    """
    pos = params
    parts = target.split('.')

    # First, split into parts like 'foo', 'bar[0]', 'baz' and process
    # each piece. It can either be a list or a dict, depending on if
    # an index like `[0]` is present. We detect this via a regular
    # expression, and keep track of where we are in params via the
    # pos variable, walking down to the last item. Once there, we
    # set the value.
    for i, part in enumerate(parts):
        # Is it indexing an array?
        result = INDEX_RE.search(part)
        if result:
            if result.group(1):
                # We have an explicit index
                index = int(result.group(1))

                # Strip index off part name
                part = part[:-len(str(index) + '[]')]
            else:
                # Index will be set after we know the proper part
                # name and that it's a list instance.
                index = None
                part = part[:-2]

            if part not in pos or not isinstance(pos[part], list):
                pos[part] = []

            # This means we should append, e.g. 'foo[]'
            if index is None:
                index = len(pos[part])

            while len(pos[part]) <= index:
                # Assume it's a dict until we set the final value below
                pos[part].append({})

            # Last item? Set the value, otherwise set the new position
            if i == len(parts) - 1:
                pos[part][index] = value
            else:
                # The new pos is the *item* in the array, not the array!
                pos = pos[part][index]
        else:
            if part not in pos:
                pos[part] = {}

            # Last item? Set the value, otherwise set the new position
            if i == len(parts) - 1:
                pos[part] = value
            else:
                pos = pos[part]
