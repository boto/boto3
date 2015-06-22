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
from botocore import xform_name
from botocore.docs.method import get_instance_public_methods
from botocore.docs.utils import DocumentedShape

from boto3.docs.base import BaseDocumenter
from boto3.docs.utils import get_resource_ignore_params
from boto3.docs.method import document_model_driven_resource_method
from boto3.docs.utils import add_resource_type_overview


class CollectionDocumenter(BaseDocumenter):
    def document_collections(self, section):
        collections = self._resource.meta.resource_model.collections
        collections_list = []
        add_resource_type_overview(
            section=section,
            resource_type='Collections',
            description=(
                'Collections provide an interface to iterate over and '
                'manipulate groups of resources. '),
            intro_link='guide_collections')
        self.member_map['collections'] = collections_list
        for collection in collections:
            collection_section = section.add_new_section(collection.name)
            collections_list.append(collection.name)
            self._document_collection(collection_section, collection)

    def _document_collection(self, section, collection):
        section.style.start_sphinx_py_attr(collection.name)
        methods = get_instance_public_methods(
            getattr(self._resource, collection.name))
        batch_actions = {}
        for batch_action in collection.batch_actions:
            batch_actions[batch_action.name] = batch_action

        for method in sorted(methods):
            method_section = section.add_new_section(method)
            if method in batch_actions:
                self._document_batch_action(
                    method_section, batch_actions[method], collection)
            else:
                self._document_custom_action(
                    method_section, method, collection)

    def _document_batch_action(self, section, action, collection):
        operation_model = self._service_model.operation_model(
            action.request.operation)
        ignore_params = get_resource_ignore_params(action.request.params)

        example_return_value = 'response'
        if action.resource:
            example_return_value = xform_name(action.resource.type)
        resource_name = xform_name(self._resource_name)
        if self.represents_service_resource:
            resource_name = self._resource_name
        example_prefix = '%s = %s.%s.%s' % (
            example_return_value, resource_name,
            collection.name, action.name
        )
        document_model_driven_resource_method(
            section=section, method_name=action.name,
            operation_model=operation_model,
            event_emitter=self._resource.meta.client.meta.events,
            method_description=operation_model.documentation,
            example_prefix=example_prefix,
            exclude_input=ignore_params,
            resource_action_model=action
        )

    def _document_custom_action(self, section, action_name, collection):
        operation_model = self._service_model.operation_model(
            collection.request.operation)

        underlying_operation_members = []
        if operation_model.input_shape:
            underlying_operation_members = operation_model.input_shape.members

        resource_name = xform_name(self._resource_name)
        if self.represents_service_resource:
            resource_name = self._resource_name

        custom_action_info_dict = {
            'all': {
                'method_description': (
                    'Creates an iterable of all %s resources '
                    'in the collection.' % collection.resource.type),
                'example_prefix': '%s_iterator = %s.%s.all' % (
                    xform_name(collection.resource.type),
                    resource_name, collection.name),
                'exclude_input': underlying_operation_members
            },
            'filter': {
                'method_description': (
                    'Creates an iterable of all %s resources '
                    'in the collection filtered by kwargs passed to '
                    'method.' % collection.resource.type),
                'example_prefix': '%s_iterator = %s.%s.filter' % (
                    xform_name(collection.resource.type),
                    resource_name, collection.name),
                'exclude_input': get_resource_ignore_params(
                    collection.request.params)
            },
            'limit': {
                'method_description': (
                    'Creates an iterable up to a specified amount of '
                    '%s resources in the collection.' %
                    collection.resource.type),
                'example_prefix': '%s_iterator = %s.%s.limit' % (
                    xform_name(collection.resource.type),
                    resource_name, collection.name),
                'include_input': [
                    DocumentedShape(
                        name='count', type_name='integer',
                        documentation=(
                            'The limit to the number of resources '
                            'in the iterable.'))],
                'exclude_input': underlying_operation_members
            },
            'page_size': {
                'method_description': (
                    'Creates an iterable of all %s resources '
                    'in the collection, but limits the number of '
                    'items returned by each service call by the specified '
                    'amount.' % collection.resource.type),
                'example_prefix': '%s_iterator = %s.%s.page_size' % (
                    xform_name(collection.resource.type),
                    resource_name, collection.name),
                'include_input': [
                    DocumentedShape(
                        name='count', type_name='integer',
                        documentation=(
                            'The number of items returned by each '
                            'service call'))],
                'exclude_input': underlying_operation_members
            }
        }
        if action_name in custom_action_info_dict:
            action_info = custom_action_info_dict[action_name]
            document_model_driven_resource_method(
                section=section, method_name=action_name,
                operation_model=operation_model,
                event_emitter=self._resource.meta.client.meta.events,
                resource_action_model=collection,
                **action_info
            )
