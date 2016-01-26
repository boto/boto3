# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from boto3.utils import inject_attribute
from boto3.resources.model import Action
from boto3.docs.docstring import ActionDocstring


def inject_delete_tags(class_attributes, service_context, emitter, **kwargs):
    action_model = {
        'request': {
            'operation': 'DeleteTags',
            'params': [{
                'target': 'Resources[0]',
                'source': 'identifier',
                'name': 'Id'
            }]
        }
    }
    action = Action('delete_tags', action_model, {})

    delete_tags_action = delete_tags
    delete_tags_action.__doc__ = ActionDocstring(
        resource_name='Instance',
        event_emitter=emitter,
        action_model=action,
        service_model=service_context.service_model,
        include_signature=False
    )

    inject_attribute(class_attributes, 'delete_tags', delete_tags_action)


def delete_tags(self, **kwargs):
    kwargs['Resources'] = [self.id]
    return self.meta.client.delete_tags(**kwargs)
