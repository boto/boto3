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
from botocore.docs.method import document_model_driven_method

from boto3.docs.base import BaseDocumenter
from boto3.docs.utils import get_resource_ignore_params
from boto3.docs.utils import add_resource_type_overview


class WaiterResourceDocumenter(BaseDocumenter):
    def __init__(self, resource, service_waiter_model):
        super(WaiterResourceDocumenter, self).__init__(resource)
        self._service_waiter_model = service_waiter_model

    def document_resource_waiters(self, section):
        waiters = self._resource.meta.resource_model.waiters
        add_resource_type_overview(
            section=section,
            resource_type='Waiters',
            description=(
                'Waiters provide an interface to wait for a resource'
                ' to reach a specific state.'),
            intro_link='waiters_intro')
        waiter_list = []
        self.member_map['waiters'] = waiter_list
        for waiter in waiters:
            waiter_section = section.add_new_section(waiter.name)
            waiter_list.append(waiter.name)
            waiter_model = self._service_waiter_model.get_waiter(
                waiter.waiter_name)
            operation_model = self._service_model.operation_model(
                waiter_model.operation)

            ignore_params = get_resource_ignore_params(waiter.params)
            description = (
                'Waits until this %s is %s. This method calls '
                ':py:meth:`%s.Waiter.%s.wait` which polls. '
                ':py:meth:`%s.Client.%s` every %s seconds until '
                'a successful state is reached. An error is returned '
                'after %s failed checks.' % (
                    self._resource_name, ' '.join(waiter.name.split('_')[2:]),
                    self._service_docs_name, xform_name(waiter.waiter_name),
                    self._service_docs_name,
                    xform_name(waiter_model.operation),
                    waiter_model.delay, waiter_model.max_attempts))
            example_prefix = '%s.%s' % (
                xform_name(self._resource_name), waiter.name)
            document_model_driven_method(
                section=waiter_section, method_name=waiter.name,
                operation_model=operation_model,
                event_emitter=self._resource.meta.client.meta.events,
                example_prefix=example_prefix,
                method_description=description,
                exclude_input=ignore_params
            )
            if 'return' in waiter_section.available_sections:
                # Waiters do not return anything so we should remove
                # any sections that may document the underlying return
                # value of the client method.
                return_section = waiter_section.get_section('return')
                return_section.clear_text()
                return_section.remove_all_sections()
                return_section.write(':returns: None')
