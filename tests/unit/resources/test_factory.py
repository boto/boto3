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

from botocore.model import DenormalizedStructureBuilder, ServiceModel
from boto3.exceptions import ResourceLoadException
from boto3.resources.base import ServiceResource
from boto3.resources.collection import CollectionManager
from boto3.resources.factory import ResourceFactory
from boto3.resources.action import WaiterAction
from tests import BaseTestCase, mock


class BaseTestResourceFactory(BaseTestCase):
    def setUp(self):
        super(BaseTestResourceFactory, self).setUp()
        self.factory = ResourceFactory()
        self.load = self.factory.load_from_definition


class TestResourceFactory(BaseTestResourceFactory):
    def test_get_service_returns_resource_class(self):
        TestResource = self.load('test', 'test', {}, {}, None)

        self.assertIn(ServiceResource, TestResource.__bases__,
            'Did not return a ServiceResource subclass for service')

    def test_get_resource_returns_resource_class(self):
        QueueResource = self.load('test', 'Queue', {}, {}, None)

        self.assertIn(ServiceResource, QueueResource.__bases__,
            'Did not return a ServiceResource subclass for resource')

    def test_factory_sets_service_name(self):
        QueueResource = self.load('test', 'Queue', {}, {}, None)

        self.assertEqual(QueueResource.meta.service_name, 'test',
            'Service name not set')

    def test_factory_sets_identifiers(self):
        model = {
            'identifiers': [
                {'name': 'QueueUrl'},
                {'name': 'ReceiptHandle'},
            ],
        }

        MessageResource = self.load('test', 'Message', model, {}, None)

        self.assertIn('queue_url', MessageResource.meta.identifiers,
            'Missing queue_url identifier from model')
        self.assertIn('receipt_handle', MessageResource.meta.identifiers,
            'Missing receipt_handle identifier from model')

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

        resource = self.load('test', 'Message', model, defs, None)('url', 'handle')

        # Class name
        self.assertIn('test.Message', repr(resource))

        # Identifier names and values
        self.assertIn('queue_url', repr(resource))
        self.assertIn("'url'", repr(resource))
        self.assertIn('receipt_handle', repr(resource))
        self.assertIn("'handle'", repr(resource))

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

        TestResource = self.load('test', 'test', model, defs, None)

        self.assertTrue(hasattr(TestResource, 'Queue'),
            'Missing Queue class from model')
        self.assertTrue(hasattr(TestResource, 'Message'),
            'Missing Message class from model')

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

        TestResource = self.load('test', 'test', model, {}, service_model)

        self.assertTrue(hasattr(TestResource, 'e_tag'),
            'ETag shape member not available on resource')
        self.assertTrue(hasattr(TestResource, 'last_modified'),
            'LastModified shape member not available on resource')

    def test_factory_renames_on_clobber_identifier(self):
        model = {
            'identifiers': [
                {'name': 'Meta'}
            ]
        }

        # Each resource has a ``meta`` defined, so this identifier
        # must be renamed.
        cls = self.load('test', 'test', model, {}, None)

        self.assertTrue(hasattr(cls, 'meta_identifier'))

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
        with self.assertRaises(ValueError) as cm:
            self.load('test', 'test', model, {}, None)

        self.assertIn('test', str(cm.exception))
        self.assertIn('action', str(cm.exception))

    def test_can_instantiate_service_resource(self):
        TestResource = self.load('test', 'test', {}, {}, None)
        resource = TestResource()

        self.assertIsInstance(resource, ServiceResource,
            'Object is not an instance of ServiceResource')

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

        queue = self.load('test', 'Queue', model, defs, None)('url')

        self.assertTrue(not hasattr(queue, 'Queue'))
        self.assertTrue(not hasattr(queue, 'Message'))

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

        queue = self.load('test', 'Queue', model, defs, None)('url')

        # Let's create a message and only give it a receipt handle
        # The required queue_url identifier should be set from the
        # queue itself.
        message = queue.Message('receipt')

        self.assertEqual(message.queue_url, 'url',
            'Wrong queue URL set on the message resource instance')
        self.assertEqual(message.receipt_handle, 'receipt',
            'Wrong receipt handle set on the message resource instance')

    def test_resource_meta_unique(self):
        queue_cls = self.load('test', 'Queue', {}, {}, None)

        queue1 = queue_cls()
        queue2 = queue_cls()

        self.assertEqual(queue1.meta, queue2.meta,
            'Queue meta copies not equal after creation')

        queue1.meta.data = {'id': 'foo'}
        queue2.meta.data = {'id': 'bar'}

        self.assertNotEqual(queue_cls.meta, queue1.meta,
            'Modified queue instance data should not modify the class data')
        self.assertNotEqual(queue1.meta, queue2.meta,
            'Queue data should be unique to queue instance')
        self.assertNotEqual(queue1.meta, 'bad-value')

    def test_resource_meta_repr(self):
        queue_cls = self.load('test', 'Queue', {}, {}, None)
        queue = queue_cls()
        self.assertEqual(repr(queue.meta),
                         'ResourceMeta(\'test\', identifiers=[])')

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

        queue = self.load('test', 'Queue', model, {}, None)()
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

        queue = self.load('test', 'Queue', model, {}, None)()

        # Simulate loaded data
        queue.meta.data = {'some': 'data'}

        # Perform a call
        queue.get_message_status()

        # Cached data should be cleared
        self.assertIsNone(queue.meta.data)

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

        queue = self.load('test', 'Queue', model, {}, None)()

        # Simulate loaded data
        queue.meta.data = {'some': 'data'}

        # Perform a call
        queue.get_message_status()

        # Cached data should not be cleared
        self.assertEqual(queue.meta.data, {'some': 'data'})

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

        resource = self.load('test', 'test', model, {}, service_model)('url')

        # Accessing an identifier should not call load, even if it's in
        # the shape members.
        resource.url
        action.assert_not_called()

        # Accessing a property should call load
        self.assertEqual(resource.e_tag, 'tag',
            'ETag property returned wrong value')
        action.assert_called_once()

        # Both params should have been loaded into the data bag
        self.assertIn('ETag', resource.meta.data)
        self.assertIn('LastModified', resource.meta.data)

        # Accessing another property should use cached value
        # instead of making a second call.
        self.assertEqual(resource.last_modified, 'never',
            'LastModified property returned wrong value')
        action.assert_called_once()

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

        resource = self.load('test', 'test', model, {}, service_model)('url')

        with self.assertRaises(ResourceLoadException):
            resource.last_modified

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

        resource = self.load('test', 'Instance', model, defs,
                             service_model)('group-id')

        # Load the resource with no data
        resource.meta.data = {}

        self.assertTrue(
            hasattr(resource, 'subnet'),
            'Resource should have a subnet reference')
        self.assertIsNone(
            resource.subnet,
            'Missing identifier, should return None')
        self.assertIsNone(resource.vpcs)

        # Load the resource with data to instantiate a reference
        resource.meta.data = {
            'SubnetId': 'abc123',
            'Vpcs': [
                {'Id': 'vpc1'},
                {'Id': 'vpc2'}
            ]
        }

        self.assertIsInstance(resource.subnet, ServiceResource)
        self.assertEqual(resource.subnet.id, 'abc123')

        vpcs = resource.vpcs
        self.assertIsInstance(vpcs, list)
        self.assertEqual(len(vpcs), 2)
        self.assertEqual(vpcs[0].id, 'vpc1')
        self.assertEqual(vpcs[1].id, 'vpc2')

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

        resource = self.load('test', 'test', model, defs, service_model)()

        self.assertTrue(hasattr(resource, 'queues'),
            'Resource should expose queues collection')
        self.assertIsInstance(resource.queues, CollectionManager,
            'Queues collection should be a collection manager')

    def test_resource_loads_waiters(self):
        model = {
            "waiters": {
                "Exists": {
                "waiterName": "BucketExists",
                "params": [
                    {"target": "Bucket", "source": "identifier",
                     "name": "Name"}]
                }
            }
        }

        defs = {
            'Bucket': {}
        }
        service_model = ServiceModel({})

        resource = self.load('test', 'test', model, defs, service_model)()

        self.assertTrue(hasattr(resource, 'wait_until_exists'),
            'Resource should expose resource waiter: wait_until_exists')

    @mock.patch('boto3.resources.factory.WaiterAction')
    def test_resource_waiter_calls_waiter_method(self, waiter_action_cls):
        model = {
            "waiters": {
                "Exists": {
                "waiterName": "BucketExists",
                "params": [
                    {"target": "Bucket", "source": "identifier",
                     "name": "Name"}]
                }
            }
        }

        defs = {
            'Bucket': {}
        }
        service_model = ServiceModel({})

        waiter_action = waiter_action_cls.return_value
        resource = self.load('test', 'test', model, defs, service_model)()

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
        resource = self.load('test', 'test', self.model, self.defs, None)()
        q = resource.Queue('test')

        self.assertIsInstance(q, ServiceResource,
            'Dangling resource instance not a ServiceResource')

    def test_dangling_resource_create_with_kwarg(self):
        resource = self.load('test', 'test', self.model, self.defs, None)()
        q = resource.Queue(url='test')

        self.assertIsInstance(q, ServiceResource,
            'Dangling resource created with kwargs is not a ServiceResource')

    def test_dangling_resource_shares_client(self):
        resource = self.load('test', 'test', self.model, self.defs, None)()
        q = resource.Queue('test')

        self.assertEqual(resource.meta.client, q.meta.client,
            'Client was not shared to dangling resource instance')

    def test_dangling_resource_requires_identifier(self):
        resource = self.load('test', 'test', self.model, self.defs, None)()

        with self.assertRaises(ValueError):
            resource.Queue()

    def test_dangling_resource_raises_for_unknown_arg(self):
        resource = self.load('test', 'test', self.model, self.defs, None)()

        with self.assertRaises(ValueError):
            resource.Queue(url='foo', bar='baz')

    def test_dangling_resource_equality(self):
        resource = self.load('test', 'test', self.model, self.defs, None)()

        q1 = resource.Queue('url')
        q2 = resource.Queue('url')

        self.assertEqual(q1, q2)

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

        resource = self.load('test', 'test', self.model, self.defs, None)()

        q1 = resource.Queue('url')
        q2 = resource.Queue('different')
        m = q1.Message('handle')

        self.assertNotEqual(q1, q2)
        self.assertNotEqual(q1, m)

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

        cls = self.load('test', 'Instance', self.model, self.defs,
                        service_model)
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
        self.assertIsNotNone(interface.meta.data)
        self.assertEqual(interface.public_ip, '127.0.0.1')


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
        resource = self.load('test', 'test', self.model, self.defs, None)()

        self.assertTrue(hasattr(resource, 'QueueObject'))

    def test_contains_all_subresources(self):
        resource = self.load('test', 'test', self.model, self.defs, None)()

        self.assertIn('QueueObject', dir(resource))
        self.assertIn('PriorityQueue', dir(resource))
        self.assertIn('Message', dir(resource))

    def test_subresource_missing_all_subresources(self):
        resource = self.load('test', 'test', self.model, self.defs, None)()
        message = resource.Message('url', 'handle')

        self.assertNotIn('QueueObject', dir(message))
        self.assertNotIn('PriorityQueue', dir(message))
        self.assertNotIn('Queue', dir(message))
        self.assertNotIn('Message', dir(message))
