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
from botocore.hooks import HierarchicalEmitter

from tests.unit.docs import BaseDocsTest
from boto3.docs.attr import document_attribute


class TestDocumentAttribute(BaseDocsTest):
    def setUp(self):
        super(TestDocumentAttribute, self).setUp()
        self.add_shape({
            'NestedStruct': {
                'type': 'structure',
                'members': {
                    'NestedStrAttr': {
                        'shape': 'String',
                        'documentation': 'Documents a nested string attribute'
                    }
                }
            }
        })
        self.add_shape({
            'ResourceShape': {
                'type': 'structure',
                'members': {
                    'StringAttr': {
                        'shape': 'String',
                        'documentation': 'Documents a string attribute'
                    },
                    'NestedAttr': {
                        'shape': 'NestedStruct',
                        'documentation': 'Documents a nested attribute'
                    }
                }
            }
        })
        self.setup_client_and_resource()

        self.event_emitter = HierarchicalEmitter()
        self.service_name = 'myservice'
        self.resource_name = 'myresource'
        self.service_model = self.client.meta.service_model

    def test_document_attr_scalar(self):
        shape_model = self.service_model.shape_for('ResourceShape')
        attr_name = 'StringAttr'
        document_attribute(
            self.doc_structure, self.service_name, self.resource_name,
            attr_name, self.event_emitter, shape_model.members[attr_name])
        self.assert_contains_lines_in_order([
            '.. py:attribute:: StringAttr',
            '  - *(string) --* Documents a string attribute'
        ])

    def test_document_attr_structure(self):
        shape_model = self.service_model.shape_for('ResourceShape')
        attr_name = 'NestedAttr'
        document_attribute(
            self.doc_structure, self.service_name, self.resource_name,
            attr_name, self.event_emitter, shape_model.members[attr_name])
        self.assert_contains_lines_in_order([
            '.. py:attribute:: NestedAttr',
            '  - *(dict) --* Documents a nested attribute',
            ('    - **NestedStrAttr** *(string) --* Documents a nested '
             'string attribute')
        ])
