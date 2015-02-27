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

from botocore.model import DenormalizedStructureBuilder

from boto3.resources.model import ResourceModel, Action, Collection, Waiter
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
                            {'target': 'FrobId', 'source': 'identifier',
                             'name': 'Id'}
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
        self.assertEqual(action.request.params[0].source, 'identifier')
        self.assertEqual(action.request.params[0].name, 'Id')
        self.assertEqual(action.path, 'Container.Frobs[]')

    def test_resource_action_response_resource(self):
        model = ResourceModel('test', {
            'actions': {
                'GetFrobs': {
                    'resource': {
                        'type': 'Frob',
                        'path': 'Container.Frobs[]'
                    }
                }
            }
        }, {
            'Frob': {}
        })

        action = model.actions[0]
        self.assertEqual(action.resource.type, 'Frob')
        self.assertEqual(action.resource.path, 'Container.Frobs[]')
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

    def test_resource_batch_action(self):
        model = ResourceModel('test', {
            'batchActions': {
                'Delete': {
                    'request': {
                        'operation': 'DeleteObjects',
                        'params': [
                            {'target': 'Bucket', 'sourceType': 'identifier',
                             'source': 'BucketName'}
                        ]
                    }
                }
            }
        }, {})

        self.assertIsInstance(model.batch_actions, list)

        action = model.batch_actions[0]
        self.assertIsInstance(action, Action)
        self.assertEqual(action.request.operation, 'DeleteObjects')
        self.assertEqual(action.request.params[0].target, 'Bucket')

    def test_sub_resources(self):
        model = ResourceModel('test', {
            'has': {
                'RedFrob': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {'target': 'Id', 'source': 'input'}
                        ]
                    }
                },
                'GreenFrob': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {'target': 'Id', 'source': 'input'}
                        ]
                    }
                }
            }
        }, {
            'Frob': {}
        })

        self.assertIsInstance(model.subresources, list)
        self.assertEqual(len(model.subresources), 2)

        action = model.subresources[0]
        resource = action.resource

        self.assertIn(action.name, ['RedFrob', 'GreenFrob'])
        self.assertEqual(resource.identifiers[0].target, 'Id')
        self.assertEqual(resource.identifiers[0].source, 'input')
        self.assertEqual(resource.type, 'Frob')

    def test_resource_references(self):
        model_def = {
            'has': {
                'Frob': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {'target':'Id', 'source':'data',
                             'path':'FrobId'}
                        ]
                    }
                }
            }
        }
        resource_defs = {
            'Frob': {}
        }
        model = ResourceModel('test', model_def, resource_defs)

        self.assertIsInstance(model.references, list)
        self.assertEqual(len(model.references), 1)

        ref = model.references[0]
        self.assertEqual(ref.name, 'frob')
        self.assertEqual(ref.resource.type, 'Frob')
        self.assertEqual(ref.resource.identifiers[0].target, 'Id')
        self.assertEqual(ref.resource.identifiers[0].source, 'data')
        self.assertEqual(ref.resource.identifiers[0].path, 'FrobId')

    def test_resource_collections(self):
        model = ResourceModel('test', {
            'hasMany': {
                'Frobs': {
                    'request': {
                        'operation': 'GetFrobList'
                    },
                    'resource': {
                        'type': 'Frob',
                        'path': 'FrobList[]'
                    }
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
        self.assertEqual(model.collections[0].resource.path, 'FrobList[]')

    def test_waiter(self):
        model = ResourceModel('test', {
            'waiters': {
                'Exists': {
                    'waiterName': 'ObjectExists',
                    'params': [
                        {'target': 'Bucket', 'sourceType': 'identifier',
                         'source': 'BucketName'}
                    ]
                }
            }
        }, {})

        self.assertIsInstance(model.waiters, list)

        waiter = model.waiters[0]
        self.assertIsInstance(waiter, Waiter)
        self.assertEqual(waiter.name, 'wait_until_exists')
        self.assertEqual(waiter.waiter_name, 'ObjectExists')
        self.assertEqual(waiter.params[0].target, 'Bucket')

class TestRenaming(BaseTestCase):
    def test_multiple(self):
        # This tests a bunch of different renames working together
        model = ResourceModel('test', {
            'identifiers': [{'name': 'Foo'}],
            'actions': {
                'Foo': {}
            },
            'has': {
                'Foo': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {'target':'Id', 'source':'data',
                             'path': 'FrobId'}
                        ]
                    }
                }
            },
            'hasMany': {
                'Foo': {}
            },
            'waiters': {
                'Foo': {}
            }
        }, {
            'Frob': {}
        })

        shape = DenormalizedStructureBuilder().with_members({
            'Foo': {
                'type': 'string',
            },
            'Bar': {
                'type': 'string'
            }
        }).build_model()

        model.load_rename_map(shape)

        self.assertEqual(model.identifiers[0].name, 'foo')
        self.assertEqual(model.actions[0].name, 'foo_action')
        self.assertEqual(model.references[0].name, 'foo_reference')
        self.assertEqual(model.collections[0].name, 'foo_collection')
        self.assertEqual(model.waiters[0].name, 'wait_until_foo')

        # If an identifier and an attribute share the same name, then
        # the attribute is essentially hidden.
        self.assertNotIn('foo_attribute', model.get_attributes(shape))

        # Other attributes need to be there, though
        self.assertIn('bar', model.get_attributes(shape))

    # The rest of the tests below ensure the correct order of precedence
    # for the various categories of attributes/properties/methods on the
    # resource model.
    def test_meta_beats_identifier(self):
        model = ResourceModel('test', {
            'identifiers': [{'name': 'Meta'}]
        }, {})

        model.load_rename_map()

        self.assertEqual(model.identifiers[0].name, 'meta_identifier')

    def test_load_beats_identifier(self):
        model = ResourceModel('test', {
            'identifiers': [{'name': 'Load'}],
            'load': {
                'request': {
                    'operation': 'GetFrobs'
                }
            }
        }, {})

        model.load_rename_map()

        self.assertTrue(model.load)
        self.assertEqual(model.identifiers[0].name, 'load_identifier')

    def test_identifier_beats_action(self):
        model = ResourceModel('test', {
            'identifiers': [{'name': 'foo'}],
            'actions': {
                'Foo': {
                    'request': {
                        'operation': 'GetFoo'
                    }
                }
            }
        }, {})

        model.load_rename_map()

        self.assertEqual(model.identifiers[0].name, 'foo')
        self.assertEqual(model.actions[0].name, 'foo_action')

    def test_action_beats_reference(self):
        model = ResourceModel('test', {
            'actions': {
                'Foo': {
                    'request': {
                        'operation': 'GetFoo'
                    }
                }
            },
            'has': {
                'Foo': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {'target':'Id', 'source':'data',
                             'path': 'FrobId'}
                        ]
                    }
                }
            }
        }, {'Frob': {}})

        model.load_rename_map()

        self.assertEqual(model.actions[0].name, 'foo')
        self.assertEqual(model.references[0].name, 'foo_reference')

    def test_reference_beats_collection(self):
        model = ResourceModel('test', {
            'has': {
                'Foo': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {'target':'Id', 'source':'data',
                             'path': 'FrobId'}
                        ]
                    }
                }
            },
            'hasMany': {
                'Foo': {
                    'resource': {
                        'type': 'Frob'
                    }
                }
            }
        }, {'Frob': {}})

        model.load_rename_map()

        self.assertEqual(model.references[0].name, 'foo')
        self.assertEqual(model.collections[0].name, 'foo_collection')

    def test_collection_beats_waiter(self):
        model = ResourceModel('test', {
            'hasMany': {
                'WaitUntilFoo': {
                    'resource': {
                        'type': 'Frob'
                    }
                }
            },
            'waiters': {
                'Foo': {}
            }
        }, {'Frob': {}})

        model.load_rename_map()

        self.assertEqual(model.collections[0].name, 'wait_until_foo')
        self.assertEqual(model.waiters[0].name, 'wait_until_foo_waiter')

    def test_waiter_beats_attribute(self):
        model = ResourceModel('test', {
            'waiters': {
                'Foo': {}
            }
        }, {'Frob': {}})

        shape = DenormalizedStructureBuilder().with_members({
            'WaitUntilFoo': {
                'type': 'string',
            }
        }).build_model()

        model.load_rename_map(shape)

        self.assertEqual(model.waiters[0].name, 'wait_until_foo')
        self.assertIn('wait_until_foo_attribute', model.get_attributes(shape))
