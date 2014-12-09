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

from botocore.model import ServiceModel, StructureShape
from boto3.exceptions import ResourceLoadException
from boto3.resources.base import ServiceResource
from boto3.resources.collection import CollectionManager
from boto3.resources.factory import ResourceFactory
from boto3.resources.action import WaiterAction
from tests import BaseTestCase, mock


class TestResourceFactory(BaseTestCase):
    def setUp(self):
        super(TestResourceFactory, self).setUp()
        self.factory = ResourceFactory()
        self.load = self.factory.load_from_definition

    def tearDown(self):
        super(TestResourceFactory, self).tearDown()

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

        self.assertEqual(QueueResource.meta['service_name'], 'test',
            'Service name not set')

    def test_factory_sets_identifiers(self):
        model = {
            'identifiers': [
                {'name': 'QueueUrl'},
                {'name': 'ReceiptHandle'},
            ],
        }

        MessageResource = self.load('test', 'Message', model, {}, None)

        self.assertTrue('identifiers' in MessageResource.meta,
            'Class has no identifiers')
        self.assertIn('queue_url', MessageResource.meta['identifiers'],
            'Missing queue_url identifier from model')
        self.assertIn('receipt_handle', MessageResource.meta['identifiers'],
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
        defs = {
            'Queue': {},
            'Message': {}
        }

        TestResource = self.load('test', 'test', {}, defs, None)

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
        shape = mock.Mock()
        shape.members = {
            'ETag': None,
            'LastModified': None,
        }
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

    def test_dangling_resources_create_resource_instance(self):
        defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            }
        }

        resource = self.load('test', 'test', {}, defs, None)()
        q = resource.Queue('test')

        self.assertIsInstance(q, ServiceResource,
            'Dangling resource instance not a ServiceResource')

    def test_dangling_resource_create_with_kwarg(self):
        defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            }
        }

        resource = self.load('test', 'test', {}, defs, None)()
        q = resource.Queue(url='test')

        self.assertIsInstance(q, ServiceResource,
            'Dangling resource created with kwargs is not a ServiceResource')

    def test_dangling_resource_shares_client(self):
        defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            }
        }

        resource = self.load('test', 'test', {}, defs, None)()
        q = resource.Queue('test')

        self.assertEqual(resource.meta['client'], q.meta['client'],
            'Client was not shared to dangling resource instance')

    def test_dangling_resource_requires_identifier(self):
        defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            }
        }

        resource = self.load('test', 'test', {}, defs, None)()

        with self.assertRaises(ValueError):
            resource.Queue()

    def test_dangling_resource_raises_for_unknown_arg(self):
        defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            }
        }

        resource = self.load('test', 'test', {}, defs, None)()

        with self.assertRaises(ValueError):
            resource.Queue(url='foo', bar='baz')

    def test_dangling_resource_equality(self):
        defs = {
            'Queue': {
                'identifiers': [{'name': 'Url'}]
            }
        }

        resource = self.load('test', 'test', {}, defs, None)()

        q1 = resource.Queue('url')
        q2 = resource.Queue('url')

        self.assertEqual(q1, q2)

    def test_dangling_resource_inequality(self):
        defs = {
            'Queue': {
                'identifiers': [{'name': 'Url'}]
            },
            'Message': {
                'identifiers': [{'name': 'QueueUrl'}, {'name': 'Handle'}]
            }
        }

        resource = self.load('test', 'test', {}, defs, None)()

        q1 = resource.Queue('url')
        q2 = resource.Queue('different')
        m = resource.Message('url', 'handle')

        self.assertNotEqual(q1, q2)
        self.assertNotEqual(q1, m)

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
                'subResources': {
                    'resources': ['Message'],
                    'identifiers': {'Url': 'QueueUrl'}
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

        queue1.meta['data'] = {'id': 'foo'}
        queue2.meta['data'] = {'id': 'bar'}

        self.assertNotEqual(queue_cls.meta, queue1.meta,
            'Modified queue instance data should not modify the class data')
        self.assertNotEqual(queue1.meta, queue2.meta,
            'Queue data should be unique to queue instance')

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
        queue.meta['data'] = {'some': 'data'}

        # Perform a call
        queue.get_message_status()

        # Cached data should be cleared
        self.assertIsNone(queue.meta['data'])

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
        queue.meta['data'] = {'some': 'data'}

        # Perform a call
        queue.get_message_status()

        # Cached data should not be cleared
        self.assertEqual(queue.meta['data'], {'some': 'data'})

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
        shape = mock.Mock()
        shape.members = {
            'Url': None,
            'ETag': None,
            'LastModified': None,
        }
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
        self.assertIn('ETag', resource.meta['data'])
        self.assertIn('LastModified', resource.meta['data'])

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
        shape = mock.Mock()
        shape.members = {
            'Url': None,
            'ETag': None,
            'LastModified': None,
        }
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
            'belongsTo': {
                'Subnet': {
                    'resource': {
                        'type': 'Subnet',
                        'identifiers': [
                            {'target': 'Id', 'sourceType': 'dataMember',
                             'source': 'SubnetId'}
                        ]
                    }
                }
            }
        }
        defs = {
            'Group': {
                'identifiers': [{'name': 'Id'}],
                'subResources': {
                    'identifiers': {'Id': 'GroupId'},
                    'resources': ['Instance']
                }
            },
            'Subnet': {
                'identifiers': [{'name': 'Id'}]
            }
        }
        service_model = ServiceModel({
            'shapes': {
                'InstanceShape': {
                    'type': 'structure',
                    'members': {
                        'GroupId': {
                            'shape': 'String'
                        },
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
        resource.meta['data'] = {}

        self.assertTrue(hasattr(resource, 'subnet'),
                        'Resource should have a subnet reference')
        self.assertIsNone(resource.subnet,
                          'Missing identifier, should return None')
        self.assertTrue(hasattr(resource, 'group'),
                        'Resource should have a group reverse ref')

        # Load the resource with data to instantiate a reference
        resource.meta['data'] = {'SubnetId': 'abc123'}
        self.assertIsInstance(resource.subnet, ServiceResource)
        self.assertEqual(resource.subnet.id, 'abc123')

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
        mock_model.return_value.name = 'Queues'

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
                    {"target": "Bucket", "sourceType": "identifier",
                     "source": "Name"}]
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
                    {"target": "Bucket", "sourceType": "identifier",
                     "source": "Name"}]
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
