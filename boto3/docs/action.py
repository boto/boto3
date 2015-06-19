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
from botocore.model import OperationModel
from botocore.docs.method import document_model_driven_method
from botocore.docs.method import document_custom_method

from boto3.docs.base import BaseDocumenter
from boto3.docs.method import document_model_driven_resource_method
from boto3.docs.utils import get_resource_ignore_params
from boto3.docs.utils import get_resource_public_actions
from boto3.docs.utils import add_resource_type_overview


class ActionDocumenter(BaseDocumenter):
    def document_actions(self, section):
        modeled_actions_list = self._resource_model.actions
        modeled_actions = {}
        for modeled_action in modeled_actions_list:
            modeled_actions[modeled_action.name] = modeled_action
        resource_actions = get_resource_public_actions(
            self._resource.__class__)
        self.member_map['actions'] = sorted(resource_actions)
        add_resource_type_overview(
            section=section,
            resource_type='Actions',
            description=(
                'Actions call operations on resources.  They may '
                'automatically handle the passing in of arguments set '
                'from identifiers and some attributes.'),
            intro_link='actions_intro')
        for action_name in sorted(resource_actions):
            action_section = section.add_new_section(action_name)
            if action_name in ['load', 'reload'] and self._resource_model.load:
                self._document_load_reload_action(
                    action_section, action_name, self._resource_model.load)
            elif action_name in modeled_actions:
                self._document_modeled_action(
                    action_section, modeled_actions[action_name])
            else:
                document_custom_method(
                    section, action_name, resource_actions[action_name])

    def _document_modeled_action(self, section, action):
        operation_model = self._service_model.operation_model(
            action.request.operation)

        ignore_params = get_resource_ignore_params(action.request.params)

        example_return_value = 'response'
        if action.resource:
            example_return_value = xform_name(action.resource.type)
        resource_name = xform_name(self._resource_name)
        if self.represents_service_resource:
            resource_name = self._resource_name
        example_prefix = '%s = %s.%s' % (
            example_return_value, resource_name, action.name)
        document_model_driven_resource_method(
            section=section, method_name=action.name,
            operation_model=operation_model,
            event_emitter=self._resource.meta.client.meta.events,
            method_description=operation_model.documentation,
            example_prefix=example_prefix,
            exclude_input=ignore_params,
            resource_action_model=action
        )

    def _document_load_reload_action(self, action_section, action_name,
                                     load_model):
        description = (
            'Calls  :py:meth:`%s.Client.%s` to update the attributes of the'
            ' %s resource' % (
                self._service_name, xform_name(load_model.request.operation),
                self._resource_name)
        )
        resource_name = xform_name(self._resource_name)
        if self.represents_service_resource:
            resource_name = self._resource_name
        example_prefix = '%s.%s' % (resource_name, action_name)
        document_model_driven_method(
            section=action_section, method_name=action_name,
            operation_model=OperationModel({}, self._service_model),
            event_emitter=self._resource.meta.client.meta.events,
            method_description=description,
            example_prefix=example_prefix
        )
