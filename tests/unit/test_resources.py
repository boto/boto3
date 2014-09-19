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

from boto3.resources import ServiceAction, ServiceResource, ResourceFactory
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

        action = ServiceAction(None, action_def, {})
        params = action.create_request_parameters(parent, action_def['request'])

        self.assertEqual(params['WarehouseUrl'], 'w-url')

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

        action = ServiceAction(None, action_def, {})
        params = action.create_request_parameters(parent, action_def['request'])

        self.assertEqual(params['WarehouseUrl'], 'w-url')

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

        action = ServiceAction(None, action_def, {})
        params = action.create_request_parameters(None, action_def['request'])

        self.assertEqual(params['Param1'], 'param1')
        self.assertEqual(params['Param2'], 123)
        self.assertEqual(params['Param3'], True)

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

        action = ServiceAction(None, action_def, {})

        with self.assertRaises(NotImplementedError):
            action.create_request_parameters(None, action_def['request'])


class TestServiceActionCall(BaseTestCase):
    def test_service_action_creates_params(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            }
        }

        resource = mock.Mock()

        action = ServiceAction(None, action_def, {})
        action.create_request_parameters = mock.Mock()
        action.create_request_parameters.return_value = {}

        action(resource, foo=1)

        self.assertTrue(action.create_request_parameters.called)

    def test_service_action_calls_operation(self):
        action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            }
        }

        resource = mock.Mock()
        operation = resource.client.get_frobs
        operation.return_value = 'response'

        action = ServiceAction(None, action_def, {})
        action.create_request_parameters = mock.Mock()
        action.create_request_parameters.return_value = {
            'bar': 'baz'
        }

        response = action(resource, foo=1)

        self.assertTrue(operation.called)
        operation.assert_called_with(foo=1, bar='baz')
        self.assertEqual(response, 'response')


class TestResourceFactory(BaseTestCase):
    def setUp(self):
        super(TestResourceFactory, self).setUp()
        self.factory = ResourceFactory()
        self.load = self.factory.load_from_definition

        # Don't do version lookups on the filesystem, instead always return
        # a set date and mock calls to ``open`` when required.
        self.version_patch = mock.patch('boto3.resources.get_latest_version')
        self.version_mock = self.version_patch.start()
        self.version_mock.return_value = '2014-01-01'

    def tearDown(self):
        super(TestResourceFactory, self).tearDown()
        self.version_patch.stop()

    def test_create_service_calls_load(self):
        self.factory.load_from_definition = mock.Mock()
        with mock.patch('boto3.resources.open',
                        mock.mock_open(read_data='{}'), create=True):
            self.factory.create_class('test')

            self.assertTrue(self.factory.load_from_definition.called,
                'Class was not loaded from definition')
            self.factory.load_from_definition.assert_called_with(
                'test', 'test', {}, {})

    def test_create_resource_calls_load(self):
        self.factory.load_from_definition = mock.Mock()
        with mock.patch('boto3.resources.open',
                        mock.mock_open(read_data='{}'), create=True):
            self.factory.create_class('test', 'Queue')

            self.assertTrue(self.factory.load_from_definition.called,
                'Class was not loaded from definition')
            self.factory.load_from_definition.assert_called_with(
                'test', 'Queue', {}, {})

    def test_get_service_returns_resource_class(self):
        TestResource = self.load('test', 'test', {}, {})

        self.assertIn(ServiceResource, TestResource.__bases__,
            'Did not return a ServiceResource subclass for service')

    def test_get_resource_returns_resource_class(self):
        QueueResource = self.load('test', 'Queue', {}, {})

        self.assertIn(ServiceResource, QueueResource.__bases__,
            'Did not return a ServiceResource subclass for resource')

    def test_factory_sets_service_name(self):
        QueueResource = self.load('test', 'Queue', {}, {})

        self.assertEqual(QueueResource.service_name, 'test',
            'Service name not set')

    def test_factory_sets_identifiers(self):
        model = {
            'identifiers': [
                {'name': 'QueueUrl'},
                {'name': 'ReceiptHandle'},
            ],
        }

        MessageResource = self.load('test', 'Message', model, {})

        self.assertTrue(hasattr(MessageResource, 'identifiers'),
            'Class has no identifiers')
        self.assertIn('queue_url', MessageResource.identifiers,
            'Missing queue_url identifier from model')
        self.assertIn('receipt_handle', MessageResource.identifiers,
            'Missing receipt_handle identifier from model')

    def test_factory_creates_dangling_resources(self):
        defs = {
            'Queue': {},
            'Message': {}
        }

        TestResource = self.load('test', 'test', {}, defs)

        self.assertTrue(hasattr(TestResource, 'Queue'),
            'Missing Queue class from model')
        self.assertTrue(hasattr(TestResource, 'Message'),
            'Missing Message class from model')

    def test_can_instantiate_service_resource(self):
        TestResource = self.load('test', 'test', {}, {})
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

        resource = self.load('test', 'test', {}, defs)()
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

        resource = self.load('test', 'test', {}, defs)()
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

        resource = self.load('test', 'test', {}, defs)()
        q = resource.Queue('test')

        self.assertEqual(resource.client, q.client,
            'Client was not shared to dangling resource instance')

    def test_dangling_resource_requires_identifier(self):
        defs = {
            'Queue': {
                'identifiers': [
                    {'name': 'Url'}
                ]
            }
        }

        resource = self.load('test', 'test', {}, defs)()

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

        queue = self.load('test', 'Queue', model, defs)('url')

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

        queue = self.load('test', 'Queue', model, defs)('url')

        # Let's create a message and only give it a receipt handle
        # The required queue_url identifier should be set from the
        # queue itself.
        message = queue.Message('receipt')

        self.assertEqual(message.queue_url, 'url',
            'Wrong queue URL set on the message resource instance')
        self.assertEqual(message.receipt_handle, 'receipt',
            'Wrong receipt handle set on the message resource instance')
