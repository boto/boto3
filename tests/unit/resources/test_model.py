# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://aws.amazon.com/apache2.0/
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

        assert model.name == 'test'

    def test_resource_shape(self):
        model = ResourceModel('test', {
            'shape': 'Frob'
        }, {})

        assert model.shape == 'Frob'

    def test_resource_identifiers(self):
        model = ResourceModel('test', {
            'identifiers': [
                {'name': 'one'},
                {'name': 'two', 'memberName': 'three'}
            ]
        }, {})

        assert model.identifiers[0].name == 'one'
        assert model.identifiers[1].name == 'two'
        assert model.identifiers[1].member_name == 'three'

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

        assert isinstance(model.actions, list)
        assert len(model.actions) == 1

        action = model.actions[0]
        assert isinstance(action, Action)
        assert action.request.operation == 'GetFrobsOperation'
        assert isinstance(action.request.params, list)
        assert len(action.request.params) == 1
        assert action.request.params[0].target == 'FrobId'
        assert action.request.params[0].source == 'identifier'
        assert action.request.params[0].name == 'Id'
        assert action.path == 'Container.Frobs[]'

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
        assert action.resource.type == 'Frob'
        assert action.resource.path == 'Container.Frobs[]'
        assert isinstance(action.resource.model, ResourceModel)
        assert action.resource.model.name == 'Frob'

    def test_resource_load_action(self):
        model = ResourceModel('test', {
            'load': {
                'request': {
                    'operation': 'GetFrobInfo'
                },
                'path': '$'
            }
        }, {})

        assert isinstance(model.load, Action)
        assert model.load.request.operation == 'GetFrobInfo'
        assert model.load.path == '$'

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

        assert isinstance(model.batch_actions, list)

        action = model.batch_actions[0]
        assert isinstance(action, Action)
        assert action.request.operation == 'DeleteObjects'
        assert action.request.params[0].target == 'Bucket'

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

        assert isinstance(model.subresources, list)
        assert len(model.subresources) == 2

        action = model.subresources[0]
        resource = action.resource

        assert action.name in ['RedFrob', 'GreenFrob']
        assert resource.identifiers[0].target == 'Id'
        assert resource.identifiers[0].source == 'input'
        assert resource.type == 'Frob'

    def test_resource_references(self):
        model_def = {
            'has': {
                'Frob': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {
                                'target': 'Id',
                                'source': 'data',
                                'path': 'FrobId'
                            }
                        ]
                    }
                }
            }
        }
        resource_defs = {
            'Frob': {}
        }
        model = ResourceModel('test', model_def, resource_defs)

        assert isinstance(model.references, list)
        assert len(model.references) == 1

        ref = model.references[0]
        assert ref.name == 'frob'
        assert ref.resource.type == 'Frob'
        assert ref.resource.identifiers[0].target == 'Id'
        assert ref.resource.identifiers[0].source == 'data'
        assert ref.resource.identifiers[0].path == 'FrobId'

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

        assert isinstance(model.collections, list)
        assert len(model.collections) == 1
        assert isinstance(model.collections[0], Collection)
        assert model.collections[0].request.operation == 'GetFrobList'
        assert model.collections[0].resource.type == 'Frob'
        assert model.collections[0].resource.model.name == 'Frob'
        assert model.collections[0].resource.path == 'FrobList[]'

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

        assert isinstance(model.waiters, list)

        waiter = model.waiters[0]
        assert isinstance(waiter, Waiter)
        assert waiter.name == 'wait_until_exists'
        assert waiter.waiter_name == 'ObjectExists'
        assert waiter.params[0].target == 'Bucket'


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
                            {
                                'target': 'Id',
                                'source': 'data',
                                'path': 'FrobId'
                            }
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

        assert model.identifiers[0].name == 'foo'
        assert model.actions[0].name == 'foo_action'
        assert model.references[0].name == 'foo_reference'
        assert model.collections[0].name == 'foo_collection'
        assert model.waiters[0].name == 'wait_until_foo'

        # If an identifier and an attribute share the same name, then
        # the attribute is essentially hidden.
        assert 'foo_attribute' not in model.get_attributes(shape)

        # Other attributes need to be there, though
        assert 'bar' in model.get_attributes(shape)

    # The rest of the tests below ensure the correct order of precedence
    # for the various categories of attributes/properties/methods on the
    # resource model.
    def test_meta_beats_identifier(self):
        model = ResourceModel('test', {
            'identifiers': [{'name': 'Meta'}]
        }, {})

        model.load_rename_map()

        assert model.identifiers[0].name == 'meta_identifier'

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

        assert model.load
        assert model.identifiers[0].name == 'load_identifier'

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

        assert model.identifiers[0].name == 'foo'
        assert model.actions[0].name == 'foo_action'

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
                            {
                                'target': 'Id',
                                'source': 'data',
                                'path': 'FrobId'
                            }
                        ]
                    }
                }
            }
        }, {'Frob': {}})

        model.load_rename_map()

        assert model.actions[0].name == 'foo'
        assert model.references[0].name == 'foo_reference'

    def test_reference_beats_collection(self):
        model = ResourceModel('test', {
            'has': {
                'Foo': {
                    'resource': {
                        'type': 'Frob',
                        'identifiers': [
                            {
                                'target': 'Id',
                                'source': 'data',
                                'path': 'FrobId'
                            }
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

        assert model.references[0].name == 'foo'
        assert model.collections[0].name == 'foo_collection'

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

        assert model.collections[0].name == 'wait_until_foo'
        assert model.waiters[0].name == 'wait_until_foo_waiter'

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

        assert model.waiters[0].name == 'wait_until_foo'
        assert 'wait_until_foo_attribute' in model.get_attributes(shape)
