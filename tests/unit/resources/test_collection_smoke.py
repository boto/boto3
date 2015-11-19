# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
import botocore.session
from botocore import xform_name
from nose.tools import assert_false

from boto3.session import Session
from boto3.resources.model import ResourceModel


# A list of names that are common names of a pagination parameter.
# Note that this list is not comprehensive. It may have to be updated
# in the future, but this covers a lot of the pagination parameters.
COMMON_PAGINATION_PARAM_NAMES = [
    'nextToken',
    'NextToken',
    'marker',
    'Marker',
    'NextMarker',
    'nextPageToken',
    'NextPageToken',
]


def operation_looks_paginated(operation_model):
    """Checks whether an operation looks like it can be paginated

    :type operation_model: botocore.model.OperationModel
    :param operation_model: The model for a particular operation

    :returns: True if determines it can be paginated. False otherwise.
    """
    has_input_param = _shape_has_pagination_param(operation_model.input_shape)
    has_output_param = _shape_has_pagination_param(
        operation_model.output_shape)
    # If there is a parameter in either the input or output that
    # is used in pagination, mark the operation as paginateable.
    return (has_input_param and has_output_param)


def _shape_has_pagination_param(shape):
    if shape:
        members = shape.members
        # Go through the list of common names that may be a pagination
        # parameter name
        for param in COMMON_PAGINATION_PARAM_NAMES:
            # Go through all of the shapes members.
            for member in members:
                # See if the name is the member name. If it is, mark
                # it as a pagination parameter.
                if param == member:
                    return True
    return False


def test_all_collections_have_paginators_if_needed():
    # If a collection relies on an operation that is paginated, it
    # will require a paginator to iterate through all of the resources
    # with the all() method. If there is no paginator, it will only
    # make it through the first page of results. So we need to make sure
    # if a collection looks like it uses a paginated operation then there
    # should be a paginator applied to it.
    botocore_session = botocore.session.get_session()
    session = Session(botocore_session=botocore_session)
    loader = botocore_session.get_component('data_loader')
    for service_name in session.get_available_resources():
        client = session.client(service_name, region_name='us-east-1')
        json_resource_model = loader.load_service_model(
            service_name, 'resources-1')
        resource_defs = json_resource_model['resources']
        resource_models = []
        # Get the service resource model
        service_resource_model = ResourceModel(
            service_name, json_resource_model['service'], resource_defs)
        resource_models.append(service_resource_model)
        # Generate all of the resource models for a service
        for resource_name, resource_defintion in resource_defs.items():
            resource_models.append(ResourceModel(
                resource_name, resource_defintion, resource_defs))
        for resource_model in resource_models:
            # Iterate over all of the collections for each resource model
            # and ensure that the collection has a paginator if it needs one.
            for collection_model in resource_model.collections:
                yield (
                    _assert_collection_has_paginator_if_needed, client,
                    service_name, resource_name, collection_model)


def _assert_collection_has_paginator_if_needed(
        client, service_name, resource_name, collection_model):
    underlying_operation_name = collection_model.request.operation
    # See if the operation can be paginated from the client.
    can_paginate_operation = client.can_paginate(
        xform_name(underlying_operation_name))
    # See if the operation looks paginated.
    looks_paginated = operation_looks_paginated(
        client.meta.service_model.operation_model(underlying_operation_name))
    # Make sure that if the operation looks paginated then there is
    # a paginator for the client to use for the collection.
    if not can_paginate_operation:
        assert_false(
            looks_paginated,
            'Collection %s on resource %s of service %s uses the operation '
            '%s, but the operation has no paginator even though it looks '
            'paginated.' % (
                collection_model.name, resource_name, service_name,
                underlying_operation_name))
