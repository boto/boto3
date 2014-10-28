# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is
# distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from boto3.resources.model import ResourceModel, Action, SubResourceList,\
                                  Collection
from tests import BaseTestCase


class TestModels(BaseTestCase):
    def test_resource_name(self):
        model = ResourceModel('test', {}, {})

        self.assertEqual(model.name, 'test')

    def test_resource_shape(self):
        model = ResourceModel('test', {
            'shape': 'Frob'
        }, {})

        self.assertEqual(model.shape, 'Frob')

    def test_resource_identifiers(self):
        model = ResourceModel('test', {
            'identifiers': [
                {'name': 'one'},
                {'name': 'two'}
            ]
        }, {})

        self.assertEqual(model.identifiers[0].name, 'one')
        self.assertEqual(model.identifiers[1].name, 'two')

    def test_resource_action_raw(self):
        model = ResourceModel('test', {
            'actions': {
                'GetFrobs': {
                    'request': {
                        'operation': 'GetFrobsOperation',
                        'params': [
                            {'target': 'FrobId', 'sourceType': 'identifier',
                             'source': 'Id'}
                        ]
                    },
                    'path': 'Container.Frobs[]'
                }
            }
        }, {})

        self.assertIsInstance(model.actions, list)
        self.assertEqual(len(model.actions), 1)

        action = model.actions[0]
        self.assertIsInstance(action, Action)
        self.assertEqual(action.request.operation, 'GetFrobsOperation')
        self.assertIsInstance(action.request.params, list)
        self.assertEqual(len(action.request.params), 1)
        self.assertEqual(action.request.params[0].target, 'FrobId')
        self.assertEqual(action.request.params[0].source_type, 'identifier')
        self.assertEqual(action.request.params[0].source, 'Id')
        self.assertEqual(action.path, 'Container.Frobs[]')

    def test_resource_action_response_resource(self):
        model = ResourceModel('test', {
            'actions': {
                'GetFrobs': {
                    'resource': {
                        'type': 'Frob'
                    }
                }
            }
        }, {
            'Frob': {}
        })

        action = model.actions[0]
        self.assertEqual(action.resource.type, 'Frob')
        self.assertIsInstance(action.resource.model, ResourceModel)
        self.assertEqual(action.resource.model.name, 'Frob')

    def test_resource_load_action(self):
        model = ResourceModel('test', {
            'load': {
                'request': {
                    'operation': 'GetFrobInfo'
                },
                'path': '$'
            }
        }, {})

        self.assertIsInstance(model.load, Action)
        self.assertEqual(model.load.request.operation, 'GetFrobInfo')
        self.assertEqual(model.load.path, '$')

    def test_sub_resources(self):
        model = ResourceModel('test', {
            'subResources': {
                'identifiers': {
                    'FrobId': 'Id'
                },
                'resources': ['Frob']
            }
        }, {
            'Frob': {}
        })

        self.assertIsInstance(model.sub_resources, SubResourceList)
        self.assertEqual(model.sub_resources.identifiers['FrobId'], 'Id')
        self.assertEqual(model.sub_resources.resource_names[0], 'Frob')

        resource = model.sub_resources.resources[0]
        self.assertEqual(resource.name, 'Frob')

    def test_resource_references(self):
        model_def = {
            'hasOne': {
                'Frob': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {'target':'Id', 'sourceType':'dataMember',
                             'source':'FrobId'}
                        ]
                    },
                }
            },
            'hasSome': {
                'Frobs': {
                    'resource': {
                        'type': 'Frob'
                    }
                }
            }
        }
        resource_defs = {
            'Frob': {}
        }
        model = ResourceModel('test', model_def, resource_defs)

        self.assertIsInstance(model.references, list)
        self.assertEqual(len(model.references), 2)

        ref = model.references[0]
        self.assertEqual(ref.name, 'Frob')
        self.assertEqual(ref.resource.type, 'Frob')
        self.assertEqual(ref.resource.identifiers[0].target, 'Id')
        self.assertEqual(ref.resource.identifiers[0].source_type,
                         'dataMember')
        self.assertEqual(ref.resource.identifiers[0].source, 'FrobId')

        ref2 = model.references[1]
        self.assertEqual(ref2.name, 'Frobs')
        self.assertEqual(ref2.resource.type, 'Frob')
        self.assertEqual(len(ref2.resource.identifiers), 0)

    def test_resource_collections(self):
        model = ResourceModel('test', {
            'hasMany': {
                'Frobs': {
                    'request': {
                        'operation': 'GetFrobList'
                    },
                    'resource': {
                        'type': 'Frob'
                    },
                    'path': 'FrobList[]'
                }
            }
        }, {
            'Frob': {}
        })

        self.assertIsInstance(model.collections, list)
        self.assertEqual(len(model.collections), 1)
        self.assertIsInstance(model.collections[0], Collection)
        self.assertEqual(model.collections[0].request.operation, 'GetFrobList')
        self.assertEqual(model.collections[0].resource.type, 'Frob')
        self.assertEqual(model.collections[0].resource.model.name, 'Frob')
        self.assertEqual(model.collections[0].path, 'FrobList[]')
