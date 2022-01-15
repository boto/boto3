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
import pytest

from botocore.model import DenormalizedStructureBuilder, ServiceModel
from tests import BaseTestCase, mock

from boto3.exceptions import ResourceLoadException
from boto3.utils import ServiceContext
from boto3.resources.base import ServiceResource
from boto3.resources.collection import CollectionManager
from boto3.resources.factory import ResourceFactory


class BaseTestResourceFactory(BaseTestCase):
    def setUp(self):
        super(BaseTestResourceFactory, self).setUp()
        self.emitter = mock.Mock()
        self.factory = ResourceFactory(self.emitter)

    def load(self, resource_name, resource_json_definition=None,
             resource_json_definitions=None, service_model=None):
        if resource_json_definition is None:
            resource_json_definition = {}
        if resource_json_definitions is None:
            resource_json_definitions = {}
        service_context = ServiceContext(
            service_name='test',
            resource_json_definitions=resource_json_definitions,
            service_model=service_model,
            service_waiter_model=None
        )

        return self.factory.load_from_definition(
            resource_name=resource_name,
            single_resource_json_definition=resource_json_definition,
            service_context=service_context
        )


class TestResourceFactory(BaseTestResourceFactory):
    def test_get_service_returns_resource_class(self):
        TestResource = self.load('test')
        assert ServiceResource in TestResource.__bases__

    def test_get_resource_returns_resource_class(self):
        QueueResource = self.load('Queue')
        assert ServiceResource in QueueResource.__bases__

    def test_factory_sets_service_name(self):
        QueueResource = self.load('Queue')
        assert QueueResource.meta.service_name == 'test'

    def test_factory_sets_identifiers(self):
        model = {
            'identifiers': [
                {'name': 'QueueUrl'},
                {'name': 'ReceiptHandle'},
            ],
        }

        MessageResource = self.load('Message', model)

        assert 'queue_url' in MessageResource.meta.identifiers
        assert 'receipt_handle' in MessageResource.meta.identifiers

    def test_identifiers_in_repr(self):
        model = {
            'identifiers': [
                {'name': 'QueueUrl'},
                {'name': 'ReceiptHandle'},
            ],
        }
        defs = {
            'Message': model
        }

        resource = self.load('Message', model, defs)('url', 'handle')

        # Class name
        assert 'test.Message' in repr(resource)

        # Identifier names and values
        assert 'queue_url' in repr(resource)
        assert "'url'" in repr(resource)
        assert 'receipt_handle' in repr(resource)
        assert "'handle'" in repr(resource)

    def test_factory_creates_dangling_resources(self):
        model = {
            'has': {
                'Queue': {
                    'resource': {
                        'type': 'Queue',
                        'identifiers': [
                            {'target': 'Url', 'source': 'input'}
                        ]
                    }
                },
                'Message': {
                    'resource': {
                        'type': 'Message',
                        'identifiers': [
                            {'target': 'QueueUrl', 'source': 'input'},
                            {'target': 'Handle', 'source': 'input'}
                        ]
                    }
                }
            }
        }
        defs = {
            'Queue': {},
            'Message': {}
        }

        TestResource = self.load('test', model, defs)

        assert hasattr(TestResource, 'Queue')
        assert hasattr(TestResource, 'Message')

    def test_factory_creates_properties(self):
        model = {
            'shape': 'TestShape',
            'load': {
                'request': {
                    'operation': 'DescribeTest',
                }
            }
        }
        shape = DenormalizedStructureBuilder().with_members({
            'ETag': {
                'type': 'string',
            },
            'LastModified': {
                'type': 'string'
            }
        }).build_model()
        service_model = mock.Mock()
        service_model.shape_for.return_value = shape

        TestResource = self.load('test', model, service_model=service_model)

        assert hasattr(TestResource, 'e_tag')
        assert hasattr(TestResource, 'last_modified')

    def test_factory_renames_on_clobber_identifier(self):
        model = {
            'identifiers': [
                {'name': 'Meta'}
            ]
        }

        # Each resource has a ``meta`` defined, so this identifier
        # must be renamed.
        cls = self.load('test', model)

        assert hasattr(cls, 'meta_identifier')

    def test_factory_fails_on_clobber_action(self):
        model = {
            'identifiers': [
                {'name': 'Test'},
                {'name': 'TestAction'}
            ],
            'actions': {
                'Test': {
                    'request': {
                        'operation': 'GetTest'
                    }
                }
            }
        }

        # This fails because the resource has an identifier
        # that would be clobbered by the action name.
        with pytest.raises(ValueError) as cm:
            self.load('test', model)

            assert 'test' in str(cm.exception)
            assert 'action' in str(cm.exception)

    def test_can_instantiate_service_resource(self):
        TestResource = self.load('test')
        resource = TestResource()

        assert isinstance(resource, ServiceResource)

    def test_non_service_resource_missing_defs(self):
        # Only services should get dangling defs
        defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            },
            'Message': {
                'identifiers': [
                    {'name': 'QueueUrl'},
                    {'name': 'ReceiptHandle'}
                ]
            }
        }

        model = defs['Queue']

        queue = self.load('Queue', model, defs)('url')

        assert not hasattr(queue, 'Queue')
        assert not hasattr(queue, 'Message')

    def test_subresource_requires_only_identifier(self):
        defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ],
                'has': {
                    'Message': {
                        'resource': {
                            'type': 'Message',
                            'identifiers': [
                                {'target': 'QueueUrl', 'source': 'identifier',
                                 'name': 'Url'},
                                {'target': 'ReceiptHandle', 'source': 'input'}
                            ]
                        }
                    }
                }
            },
            'Message': {
                'identifiers': [
                    {'name': 'QueueUrl'},
                    {'name': 'ReceiptHandle'}
                ]
            }
        }

        model = defs['Queue']

        queue = self.load('Queue', model, defs)('url')

        # Let's create a message and only give it a receipt handle
        # The required queue_url identifier should be set from the
        # queue itself.
        message = queue.Message('receipt')

        assert message.queue_url == 'url'
        assert message.receipt_handle == 'receipt'

    def test_resource_meta_unique(self):
        queue_cls = self.load('Queue')

        queue1 = queue_cls()
        queue2 = queue_cls()

        assert queue1.meta == queue2.meta

        queue1.meta.data = {'id': 'foo'}
        queue2.meta.data = {'id': 'bar'}

        assert queue_cls.meta != queue1.meta
        assert queue1.meta != queue2.meta
        assert queue1.meta != 'bad-value'

    def test_resource_meta_repr(self):
        queue_cls = self.load('Queue')
        queue = queue_cls()
        assert repr(queue.meta) == 'ResourceMeta(\'test\', identifiers=[])'

    @mock.patch('boto3.resources.factory.ServiceAction')
    def test_resource_calls_action(self, action_cls):
        model = {
            'actions': {
                'GetMessageStatus': {
                    'request': {
                        'operation': 'DescribeMessageStatus'
                    }
                }
            }
        }

        action = action_cls.return_value

        queue = self.load('Queue', model)()
        queue.get_message_status('arg1', arg2=2)

        action.assert_called_with(queue, 'arg1', arg2=2)

    @mock.patch('boto3.resources.factory.ServiceAction')
    def test_resource_action_clears_data(self, action_cls):
        model = {
            'load': {
                'request': {
                    'operation': 'DescribeQueue'
                }
            },
            'actions': {
                'GetMessageStatus': {
                    'request': {
                        'operation': 'DescribeMessageStatus'
                    }
                }
            }
        }

        queue = self.load('Queue', model)()

        # Simulate loaded data
        queue.meta.data = {'some': 'data'}

        # Perform a call
        queue.get_message_status()

        # Cached data should be cleared
        assert queue.meta.data is None

    @mock.patch('boto3.resources.factory.ServiceAction')
    def test_resource_action_leaves_data(self, action_cls):
        # This model has NO load method. Cached data should
        # never be cleared since it cannot be reloaded!
        model = {
            'actions': {
                'GetMessageStatus': {
                    'request': {
                        'operation': 'DescribeMessageStatus'
                    }
                }
            }
        }

        queue = self.load('Queue', model)()

        # Simulate loaded data
        queue.meta.data = {'some': 'data'}

        # Perform a call
        queue.get_message_status()

        # Cached data should not be cleared
        assert queue.meta.data == {'some': 'data'}

    @mock.patch('boto3.resources.factory.ServiceAction')
    def test_resource_lazy_loads_properties(self, action_cls):
        model = {
            'shape': 'TestShape',
            'identifiers': [
                {'name': 'Url'}
            ],
            'load': {
                'request': {
                    'operation': 'DescribeTest',
                }
            }
        }
        shape = DenormalizedStructureBuilder().with_members({
            'ETag': {
                'type': 'string',
                'shape_name': 'ETag'
            },
            'LastModified': {
                'type': 'string',
                'shape_name': 'LastModified'
            },
            'Url': {
                'type': 'string',
                'shape_name': 'Url'
            }
        }).build_model()
        service_model = mock.Mock()
        service_model.shape_for.return_value = shape

        action = action_cls.return_value
        action.return_value = {'ETag': 'tag', 'LastModified': 'never'}

        resource = self.load(
            'test', model, service_model=service_model)('url')

        # Accessing an identifier should not call load, even if it's in
        # the shape members.
        resource.url
        action.assert_not_called()

        # Accessing a property should call load
        assert resource.e_tag == 'tag'
        assert action.call_count == 1

        # Both params should have been loaded into the data bag
        assert 'ETag' in resource.meta.data
        assert 'LastModified' in resource.meta.data

        # Accessing another property should use cached value
        # instead of making a second call.
        assert resource.last_modified == 'never'
        assert action.call_count == 1

    @mock.patch('boto3.resources.factory.ServiceAction')
    def test_resource_lazy_properties_missing_load(self, action_cls):
        model = {
            'shape': 'TestShape',
            'identifiers': [
                {'name': 'Url'}
            ]
            # Note the lack of a `load` method. These resources
            # are usually loaded via a call on a parent resource.
        }
        shape = DenormalizedStructureBuilder().with_members({
            'ETag': {
                'type': 'string',
            },
            'LastModified': {
                'type': 'string'
            },
            'Url': {
                'type': 'string'
            }
        }).build_model()
        service_model = mock.Mock()
        service_model.shape_for.return_value = shape

        action = action_cls.return_value
        action.return_value = {'ETag': 'tag', 'LastModified': 'never'}

        resource = self.load(
            'test', model, service_model=service_model)('url')

        with pytest.raises(ResourceLoadException):
            resource.last_modified

    @mock.patch('boto3.resources.factory.ServiceAction')
    def test_resource_aliases_identifiers(self, action_cls):
        model = {
            'shape': 'TestShape',
            'identifiers': [
                {'name': 'id', 'memberName': 'foo_id'}
            ]
        }
        shape = DenormalizedStructureBuilder().with_members({
            'foo_id': {
                'type': 'string',
            },
            'bar': {
                'type': 'string'
            },
        }).build_model()
        service_model = mock.Mock()
        service_model.shape_for.return_value = shape

        shape_id = 'baz'
        resource = self.load(
            'test', model, service_model=service_model)(shape_id)

        try:
            assert resource.id == shape_id
            assert resource.foo_id == shape_id
        except ResourceLoadException:
            self.fail("Load attempted on identifier alias.")

    def test_resource_loads_references(self):
        model = {
            'shape': 'InstanceShape',
            'identifiers': [{'name': 'GroupId'}],
            'has': {
                'Subnet': {
                    'resource': {
                        'type': 'Subnet',
                        'identifiers': [
                            {'target': 'Id', 'source': 'data',
                             'path': 'SubnetId'}
                        ]
                    }
                },
                'Vpcs': {
                    'resource': {
                        'type': 'Vpc',
                        'identifiers': [
                            {'target': 'Id', 'source': 'data',
                             'path': 'Vpcs[].Id'}
                        ]
                    }
                }
            }
        }
        defs = {
            'Subnet': {
                'identifiers': [{'name': 'Id'}]
            },
            'Vpc': {
                'identifiers': [{'name': 'Id'}]
            }
        }
        service_model = ServiceModel({
            'shapes': {
                'InstanceShape': {
                    'type': 'structure',
                    'members': {
                        'SubnetId': {
                            'shape': 'String'
                        }
                    }
                },
                'String': {
                    'type': 'string'
                }
            }
        })

        resource = self.load('Instance', model, defs,
                             service_model)('group-id')

        # Load the resource with no data
        resource.meta.data = {}

        assert hasattr(resource, 'subnet')
        assert resource.subnet is None
        assert resource.vpcs is None

        # Load the resource with data to instantiate a reference
        resource.meta.data = {
            'SubnetId': 'abc123',
            'Vpcs': [
                {'Id': 'vpc1'},
                {'Id': 'vpc2'}
            ]
        }

        assert isinstance(resource.subnet, ServiceResource)
        assert resource.subnet.id == 'abc123'

        vpcs = resource.vpcs
        assert isinstance(vpcs, list)
        assert len(vpcs) == 2
        assert vpcs[0].id == 'vpc1'
        assert vpcs[1].id == 'vpc2'

    @mock.patch('boto3.resources.model.Collection')
    def test_resource_loads_collections(self, mock_model):
        model = {
            'hasMany': {
                u'Queues': {
                    'request': {
                        'operation': 'ListQueues'
                    },
                    'resource': {
                        'type': 'Queue'
                    }
                }
            }
        }
        defs = {
            'Queue': {}
        }
        service_model = ServiceModel({})
        mock_model.return_value.name = 'queues'

        resource = self.load('test', model, defs, service_model)()

        # Resource must expose queues collection
        assert hasattr(resource, 'queues')
        assert isinstance(resource.queues, CollectionManager)

    def test_resource_loads_waiters(self):
        model = {
            "waiters": {
                "Exists": {
                    "waiterName": "BucketExists",
                    "params": [
                        {
                            "target": "Bucket",
                            "source": "identifier",
                            "name": "Name"
                        }
                    ]
                }
            }
        }

        defs = {
            'Bucket': {}
        }
        service_model = ServiceModel({})

        resource = self.load('test', model, defs, service_model)()

        assert hasattr(resource, 'wait_until_exists')

    @mock.patch('boto3.resources.factory.WaiterAction')
    def test_resource_waiter_calls_waiter_method(self, waiter_action_cls):
        model = {
            "waiters": {
                "Exists": {
                    "waiterName": "BucketExists",
                    "params": [
                        {
                            "target": "Bucket",
                            "source": "identifier",
                            "name": "Name"
                        }
                    ]
                }
            }
        }

        defs = {
            'Bucket': {}
        }
        service_model = ServiceModel({})

        waiter_action = waiter_action_cls.return_value
        resource = self.load('test', model, defs, service_model)()

        resource.wait_until_exists('arg1', arg2=2)
        waiter_action.assert_called_with(resource, 'arg1', arg2=2)


class TestResourceFactoryDanglingResource(BaseTestResourceFactory):
    def setUp(self):
        super(TestResourceFactoryDanglingResource, self).setUp()

        self.model = {
            'has': {
                'Queue': {
                    'resource': {
                        'type': 'Queue',
                        'identifiers': [
                            {'target': 'Url', 'source': 'input'}
                        ]
                    }
                }
            }
        }

        self.defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            }
        }

    def test_dangling_resources_create_resource_instance(self):
        resource = self.load('test', self.model, self.defs)()
        q = resource.Queue('test')

        assert isinstance(q, ServiceResource)

    def test_hash_resource_equal(self):
        resource = self.load('test', self.model, self.defs)()
        p = resource.Queue('test')
        q = resource.Queue('test')

        assert p == q
        assert hash(p) == hash(q)

    def test_hash_resource_not_equal(self):
        resource = self.load('test', self.model, self.defs)()
        p = resource.Queue('test1')
        q = resource.Queue('test2')

        assert p != q
        assert hash(p) != hash(q)

    def test_dangling_resource_create_with_kwarg(self):
        resource = self.load('test', self.model, self.defs)()
        q = resource.Queue(url='test')

        assert isinstance(q, ServiceResource)

    def test_dangling_resource_shares_client(self):
        resource = self.load('test', self.model, self.defs)()
        q = resource.Queue('test')

        assert resource.meta.client == q.meta.client

    def test_dangling_resource_requires_identifier(self):
        resource = self.load('test', self.model, self.defs)()

        with pytest.raises(ValueError):
            resource.Queue()

    def test_dangling_resource_raises_for_unknown_arg(self):
        resource = self.load('test', self.model, self.defs)()

        with pytest.raises(ValueError):
            resource.Queue(url='foo', bar='baz')

    def test_dangling_resource_identifier_is_immutable(self):
        resource = self.load('test', self.model, self.defs)()
        queue = resource.Queue('url')
        # We should not be able to change the identifier's value
        with pytest.raises(AttributeError):
            queue.url = 'foo'

    def test_dangling_resource_equality(self):
        resource = self.load('test', self.model, self.defs)()

        q1 = resource.Queue('url')
        q2 = resource.Queue('url')

        assert q1 == q2

    def test_dangling_resource_inequality(self):
        self.defs = {
            'Queue': {
                'identifiers': [{'name': 'Url'}],
                'has': {
                    'Message': {
                        'resource': {
                            'type': 'Message',
                            'identifiers': [
                                {'target': 'QueueUrl', 'source': 'identifier',
                                 'name': 'Url'},
                                {'target': 'Handle', 'source': 'input'}
                            ]
                        }
                    }
                }
            },
            'Message': {
                'identifiers': [{'name': 'QueueUrl'}, {'name': 'Handle'}]
            }
        }

        resource = self.load('test', self.model, self.defs)()

        q1 = resource.Queue('url')
        q2 = resource.Queue('different')
        m = q1.Message('handle')

        assert q1 != q2
        assert q1 != m

    def test_dangling_resource_loads_data(self):
        # Given a loadable resource instance that contains a reference
        # to another resource which has a resource data path, the
        # referenced resource should be loaded with all of the data
        # contained at that path. This allows loading references
        # which would otherwise not be loadable (missing load method)
        # and prevents extra load calls for others when we already
        # have the data available.
        self.defs = {
            'Instance': {
                'identifiers': [{'name': 'Id'}],
                'has': {
                    'NetworkInterface': {
                        'resource': {
                            'type': 'NetworkInterface',
                            'identifiers': [
                                {'target': 'Id', 'source': 'data',
                                 'path': 'NetworkInterface.Id'}
                            ],
                            'path': 'NetworkInterface'
                        }
                    }
                }
            },
            'NetworkInterface': {
                'identifiers': [{'name': 'Id'}],
                'shape': 'NetworkInterfaceShape'
            }
        }
        self.model = self.defs['Instance']
        shape = DenormalizedStructureBuilder().with_members({
            'Id': {
                'type': 'string',
            },
            'PublicIp': {
                'type': 'string'
            }
        }).build_model()
        service_model = mock.Mock()
        service_model.shape_for.return_value = shape

        cls = self.load('Instance', self.model, self.defs, service_model)
        instance = cls('instance-id')

        # Set some data as if we had completed a load action.
        def set_meta_data():
            instance.meta.data = {
                'NetworkInterface': {
                    'Id': 'network-interface-id',
                    'PublicIp': '127.0.0.1'
                }
            }
        instance.load = mock.Mock(side_effect=set_meta_data)

        # Now, get the reference and make sure it has its data
        # set as expected.
        interface = instance.network_interface
        assert interface.meta.data is not None
        assert interface.public_ip == '127.0.0.1'


class TestServiceResourceSubresources(BaseTestResourceFactory):
    def setUp(self):
        super(TestServiceResourceSubresources, self).setUp()

        self.model = {
            'has': {
                'QueueObject': {
                    'resource': {
                        'type': 'Queue',
                        'identifiers': [
                            {'target': 'Url', 'source': 'input'}
                        ]
                    }
                },
                'PriorityQueue': {
                    'resource': {
                        'type': 'Queue',
                        'identifiers': [
                            {'target': 'Url', 'source': 'input'}
                        ]
                    }
                }
            }
        }

        self.defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            },
            'Message': {
                'identifiers': [
                    {'name': 'QueueUrl'},
                    {'name': 'ReceiptHandle'}
                ]
            }
        }

    def test_subresource_custom_name(self):
        resource = self.load('test', self.model, self.defs)()

        assert hasattr(resource, 'QueueObject')

    def test_contains_all_subresources(self):
        resource = self.load('test', self.model, self.defs)()

        assert 'QueueObject' in dir(resource)
        assert 'PriorityQueue' in dir(resource)
        assert 'Message' in dir(resource)

    def test_get_available_subresources(self):
        resource = self.load('test', self.model, self.defs)()
        assert hasattr(resource, 'get_available_subresources')
        subresources = sorted(resource.get_available_subresources())
        expected = sorted(['PriorityQueue', 'Message', 'QueueObject'])
        assert subresources == expected

    def test_subresource_missing_all_subresources(self):
        resource = self.load('test', self.model, self.defs)()
        message = resource.Message('url', 'handle')

        assert 'QueueObject' not in dir(message)
        assert 'PriorityQueue' not in dir(message)
        assert 'Queue' not in dir(message)
        assert 'Message' not in dir(message)

    def test_event_emitted_when_class_created(self):
        self.load('test', self.model, self.defs)
        assert self.emitter.emit.called
        call_args = self.emitter.emit.call_args
        # Verify the correct event name emitted.
        assert call_args[0][0] == 'creating-resource-class.test.ServiceResource'

        # Verify we send out the class attributes dict.
        actual_class_attrs = sorted(call_args[1]['class_attributes'])
        assert actual_class_attrs == [
            'Message', 'PriorityQueue', 'QueueObject',
            'get_available_subresources', 'meta']

        base_classes = sorted(call_args[1]['base_classes'])
        assert base_classes == [ServiceResource]
