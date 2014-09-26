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

from boto3.resources.action import ServiceAction
from boto3.resources.base import ServiceResource
from boto3.exceptions import ResourceLoadException
from boto3.resources.factory import ResourceFactory
from tests import BaseTestCase, mock


class TestServiceActionParams(BaseTestCase):
    def test_service_action_params_identifier(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': [
                    {
                        'target': 'WarehouseUrl',
                        'sourceType': 'identifier',
                        'source': 'Url'
                    }
                ]
            }
        }

        parent = mock.Mock()
        parent.url = 'w-url'

        action = ServiceAction(None, action_def, {}, None)
        params = action.create_request_parameters(parent, action_def['request'])

        self.assertEqual(params['WarehouseUrl'], 'w-url',
            'Parameter not set from resource identifier')

    def test_service_action_params_data_member(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': [
                    {
                        'target': 'WarehouseUrl',
                        'sourceType': 'dataMember',
                        'source': 'some_member'
                    }
                ]
            }
        }

        parent = mock.Mock()
        parent.some_member = 'w-url'

        action = ServiceAction(None, action_def, {}, None)
        params = action.create_request_parameters(parent, action_def['request'])

        self.assertEqual(params['WarehouseUrl'], 'w-url',
            'Parameter not set from resource property')

    def test_service_action_params_constants(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': [
                    {
                        'target': 'Param1',
                        'sourceType': 'string',
                        'source': 'param1'
                    },
                    {
                        'target': 'Param2',
                        'sourceType': 'integer',
                        'source': 123
                    },
                    {
                        'target': 'Param3',
                        'sourceType': 'boolean',
                        'source': True
                    }
                ]
            }
        }

        action = ServiceAction(None, action_def, {}, None)
        params = action.create_request_parameters(None, action_def['request'])

        self.assertEqual(params['Param1'], 'param1',
            'Parameter not set from string constant')
        self.assertEqual(params['Param2'], 123,
            'Parameter not set from integer constant')
        self.assertEqual(params['Param3'], True,
            'Parameter not set from boolean constant')

    def test_service_action_params_invalid(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': [
                    {
                        'target': 'Param1',
                        'sourceType': 'invalid',
                        'source': 'param1'
                    }
                ]
            }
        }

        action = ServiceAction(None, action_def, {}, None)

        with self.assertRaises(NotImplementedError):
            action.create_request_parameters(None, action_def['request'])

    def test_action_params_list(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': [
                    {
                        'target': 'WarehouseUrls[0]',
                        'sourceType': 'string',
                        'source': 'w-url'
                    }
                ]
            }
        }

        action = ServiceAction(None, action_def, {}, None)
        params = action.create_request_parameters(None, action_def['request'])

        self.assertIsInstance(params['WarehouseUrls'], list,
            'Parameter did not create a list')
        self.assertEqual(len(params['WarehouseUrls']), 1,
            'Parameter list should only have a single item')
        self.assertIn('w-url', params['WarehouseUrls'],
            'Parameter not in expected list')


class TestServiceActionCall(BaseTestCase):
    def test_service_action_creates_params(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            }
        }

        resource = mock.Mock()
        resource.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }

        action = ServiceAction(None, action_def, {}, None)
        action.create_request_parameters = mock.Mock()
        action.create_request_parameters.return_value = {}

        action(resource, foo=1)

        self.assertTrue(action.create_request_parameters.called,
            'Parameters for operation not created')

    def test_service_action_calls_operation(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            }
        }

        resource = mock.Mock()
        resource.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }
        operation = resource.meta['client'].get_frobs
        operation.return_value = 'response'

        action = ServiceAction(None, action_def, {}, None)
        action.create_request_parameters = mock.Mock()
        action.create_request_parameters.return_value = {
            'bar': 'baz'
        }

        response = action(resource, foo=1)

        operation.assert_called_with(foo=1, bar='baz')
        self.assertEqual(response, 'response',
            'Unexpected low-level response data returned')

    def test_service_action_creates_resource_from_res_path(self):
        factory = ResourceFactory()
        resource = mock.Mock()
        resource.meta = {'service_name': 'test'}

        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {'target': 'Id', 'sourceType': 'responsePath',
                     'source': 'Container.Frobs[].Id'},
                ]
            },
            'path': 'Container.Frobs[]'
        }
        resource_def = action_def['resource']
        resource_defs = {
            'Frob': {
                'identifiers': [
                    {'name': 'Id'}
                ]
            }
        }

        params = {}
        response = {
            'Container': {
                'Frobs': [
                    {'Id': 'response-path'}
                ]
            }
        }

        action = ServiceAction(factory, action_def, resource_defs, None)
        response_resources = action.create_response_resource(resource,
            params, resource_def, response)

        self.assertEqual(len(response_resources), 1,
            'Too many resources were created')
        self.assertEqual(response_resources[0].id, 'response-path',
            'Identifier loaded from responsePath not set')

    def test_service_action_creates_resource_from_identifier(self):
        factory = ResourceFactory()
        resource = mock.Mock()
        resource.meta = {'service_name': 'test'}
        resource.id = 'identifier'

        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {'target': 'Id', 'sourceType': 'identifier',
                     'source': 'Id'}
                ]
            },
            'path': 'Container.Frobs[]'
        }
        resource_def = action_def['resource']
        resource_defs = {
            'Frob': {
                'identifiers': [
                    {'name': 'Id'}
                ]
            }
        }

        params = {}
        response = {
            'Container': {
                'Frobs': [
                    {}
                ]
            }
        }

        action = ServiceAction(factory, action_def, resource_defs, None)
        response_resources = action.create_response_resource(resource,
            params, resource_def, response)

        self.assertEqual(len(response_resources), 1,
            'Too many resources were created')
        self.assertEqual(response_resources[0].id, 'identifier',
            'Identifier loaded from parent identifier not set')

    def test_service_action_creates_resource_from_data_member(self):
        factory = ResourceFactory()
        resource = mock.Mock()
        resource.meta = {'service_name': 'test'}
        resource.id = 'data-member'

        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {'target': 'Id', 'sourceType': 'dataMember',
                     'source': 'Id'}
                ]
            },
            'path': 'Container.Frobs[]'
        }
        resource_def = action_def['resource']
        resource_defs = {
            'Frob': {
                'identifiers': [
                    {'name': 'Id'},
                ]
            }
        }

        params = {}
        response = {
            'Container': {
                'Frobs': [
                    {}
                ]
            }
        }

        action = ServiceAction(factory, action_def, resource_defs, None)
        response_resources = action.create_response_resource(resource,
            params, resource_def, response)

        self.assertEqual(len(response_resources), 1,
            'Too many resources were created')
        self.assertEqual(response_resources[0].id, 'data-member',
            'Identifier loaded from parent property not set')

    def test_service_action_creates_resource_from_req_param(self):
        factory = ResourceFactory()
        resource = mock.Mock()
        resource.meta = {'service_name': 'test'}

        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {'target': 'Id', 'sourceType': 'requestParameter',
                     'source': 'Id'}
                ]
            },
            'path': 'Container.Frobs[]'
        }
        resource_def = action_def['resource']
        resource_defs = {
            'Frob': {
                'identifiers': [
                    {'name': 'Id'}
                ]
            }
        }

        params = {
            'Id': 'request-parameter'
        }
        response = {
            'Container': {
                'Frobs': [
                    {}
                ]
            }
        }

        action = ServiceAction(factory, action_def, resource_defs, None)
        response_resources = action.create_response_resource(resource,
            params, resource_def, response)

        self.assertEqual(len(response_resources), 1,
            'Too many resources were created')
        self.assertEqual(response_resources[0].id, 'request-parameter',
            'Identifier loaded from request parameter not set')

    def test_service_action_resource_invalid_source_type(self):
        factory = ResourceFactory()
        resource = mock.Mock()
        resource.meta = {'service_name': 'test'}
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {'target': 'Id1', 'sourceType': 'bad', 'source': 'Id1'},
                ]
            }
        }
        resource_def = action_def['resource']
        resource_defs = {
            'Frob': {
                'identifiers': [
                    {'name': 'Id1'}
                ]
            }
        }
        params = {}
        response = {}

        action = ServiceAction(factory, action_def, resource_defs, None)

        with self.assertRaises(NotImplementedError):
            action.create_response_resource(resource, params, resource_def,
                                            response)

    def test_service_action_creates_single_resource(self):
        # This is different from the examples above because only a single
        # resource is represented in the response. The ``path`` creates
        # a single response dict rather than a list, so only one resource
        # instance should ever be returned.
        factory = ResourceFactory()
        resource = mock.Mock()
        resource.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }

        action_def = {
            'request': {
                'operation': 'GetFrob',
                'params': []
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {'target': 'Id', 'sourceType': 'responsePath',
                     'source': 'Container.Id'},
                ]
            },
            'path': 'Container'
        }
        resource_defs = {
            'Frob': {
                'identifiers': [
                    {'name': 'Id'}
                ]
            }
        }

        params = {}
        response = {
            'Container': {
                'Id': 'a-frob'
            }
        }

        resource.meta['client'].get_frob.return_value = response

        action = ServiceAction(factory, action_def, resource_defs, None)
        response_resource = action(resource, **params)

        self.assertIsInstance(response_resource, ServiceResource,
            'A single resource instance was not returned')
        self.assertEqual(response_resource.id, 'a-frob',
            'Identifier loaded from request parameter not set')

class TestResourceFactory(BaseTestCase):
    def setUp(self):
        super(TestResourceFactory, self).setUp()
        self.factory = ResourceFactory()
        self.load = self.factory.load_from_definition

        # Don't do version lookups on the filesystem, instead always return
        # a set date and mock calls to ``open`` when required.
        self.version_patch = mock.patch(
            'boto3.resources.factory.get_latest_version')
        self.version_mock = self.version_patch.start()
        self.version_mock.return_value = '2014-01-01'

    def tearDown(self):
        super(TestResourceFactory, self).tearDown()
        self.version_patch.stop()

    def test_create_service_calls_load(self):
        self.factory.load_from_definition = mock.Mock()
        with mock.patch('boto3.resources.factory.open',
                        mock.mock_open(read_data='{}'), create=True):
            self.factory.create_class('test')

            self.assertTrue(self.factory.load_from_definition.called,
                'Class was not loaded from definition')
            self.factory.load_from_definition.assert_called_with(
                'test', 'test', {}, {}, None)

    def test_create_resource_calls_load(self):
        self.factory.load_from_definition = mock.Mock()
        with mock.patch('boto3.resources.factory.open',
                        mock.mock_open(read_data='{}'), create=True):
            self.factory.create_class('test', 'Queue')

            self.assertTrue(self.factory.load_from_definition.called,
                'Class was not loaded from definition')
            self.factory.load_from_definition.assert_called_with(
                'test', 'Queue', {}, {}, None)

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

    def test_factory_fails_on_clobber_identifier(self):
        model = {
            'identifiers': [
                {'name': 'Meta'}
            ]
        }

        # This fails because each resource has a `meta` defined.
        with self.assertRaises(ValueError):
            self.load('test', 'test', model, {}, None)

    def test_factory_fails_on_clobber_action(self):
        model = {
            'identifiers': [
                {'name': 'Test'}
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
        with self.assertRaises(ValueError):
            self.load('test', 'test', model, {}, None)

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
