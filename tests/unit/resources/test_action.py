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

from boto3.resources.action import BatchAction, ServiceAction, WaiterAction
from boto3.resources.base import ResourceMeta
from boto3.resources.model import Action, Waiter
from tests import BaseTestCase, mock


class TestServiceActionCall(BaseTestCase):
    def setUp(self):
        super(TestServiceActionCall, self).setUp()

        self.action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            }
        }

    @property
    def action(self):
        return Action('test', self.action_def, {})

    @mock.patch('boto3.resources.action.create_request_parameters',
                return_value={})
    def test_service_action_creates_params(self, params_mock):
        resource = mock.Mock()
        resource.meta = ResourceMeta('test', client=mock.Mock())

        action = ServiceAction(self.action)

        action(resource, foo=1)

        self.assertTrue(params_mock.called,
            'Parameters for operation not created')

    @mock.patch('boto3.resources.action.create_request_parameters',
                return_value={'bar': 'baz'})
    def test_service_action_calls_operation(self, params_mock):
        resource = mock.Mock()
        resource.meta = ResourceMeta('test', client=mock.Mock())
        operation = resource.meta.client.get_frobs
        operation.return_value = 'response'

        action = ServiceAction(self.action)

        response = action(resource, foo=1)

        operation.assert_called_with(foo=1, bar='baz')
        self.assertEqual(response, 'response',
            'Unexpected low-level response data returned')

    @mock.patch('boto3.resources.action.create_request_parameters',
                return_value={})
    @mock.patch('boto3.resources.action.RawHandler')
    def test_service_action_calls_raw_handler(self, handler_mock, params_mock):
        resource = mock.Mock()
        resource.meta = ResourceMeta('test', client=mock.Mock())
        operation = resource.meta.client.get_frobs
        operation.return_value = 'response'

        action = ServiceAction(self.action)

        handler_mock.return_value.return_value = 'response'

        action(resource)

        handler_mock.assert_called_with(None)
        handler_mock.return_value.assert_called_with(resource, {}, 'response')

    @mock.patch('boto3.resources.action.create_request_parameters',
                return_value={})
    @mock.patch('boto3.resources.action.ResourceHandler')
    def test_service_action_calls_resource_handler(self, handler_mock, params_mock):
        self.action_def['resource'] = {
            'type': 'Frob',
            'path': 'Container'
        }

        resource = mock.Mock()
        resource.meta = ResourceMeta('test', client=mock.Mock())
        operation = resource.meta.client.get_frobs
        operation.return_value = 'response'

        factory = mock.Mock()
        resource_defs = {}
        service_model = mock.Mock()

        action_model = self.action

        action = ServiceAction(action_model, factory=factory,
            resource_defs=resource_defs, service_model=service_model)

        handler_mock.return_value.return_value = 'response'

        action(resource)

        handler_mock.assert_called_with('Container', factory, resource_defs,
            service_model, action_model.resource,
            self.action_def['request']['operation'])
        handler_mock.return_value.assert_called_with(resource, {}, 'response')


class TestWaiterActionCall(BaseTestCase):
    def setUp(self):
        super(TestWaiterActionCall, self).setUp()
        self.waiter_resource_name = 'wait_until_exists'
        self.waiter_def = {
            "waiterName": "FrobExists",
            "params": [
                {"target": "Frob", "sourceType": "identifier",
                 "source": "Name"}]
        }

    @property
    def waiter(self):
        return Waiter('test', self.waiter_def)

    @mock.patch('boto3.resources.action.create_request_parameters',
                return_value={})
    def test_service_waiter_creates_params(self, params_mock):
        resource = mock.Mock()
        resource.meta = ResourceMeta('test', client=mock.Mock())

        action = WaiterAction(self.waiter, self.waiter_resource_name)

        action(resource, foo=1)

        self.assertTrue(params_mock.called,
            'Parameters for operation not created')

    @mock.patch('boto3.resources.action.create_request_parameters',
                return_value={'bar': 'baz'})
    def test_service_action_calls_operation(self, params_mock):
        resource = mock.Mock()
        resource.meta = ResourceMeta('test', client=mock.Mock())
        get_waiter = resource.meta.client.get_waiter
        mock_waiter = mock.Mock()
        get_waiter.return_value = mock_waiter

        action = WaiterAction(self.waiter, self.waiter_resource_name)

        action(resource, foo=1)

        get_waiter.assert_called_with('frob_exists')
        mock_waiter.wait.assert_called_with(foo=1, bar='baz')


class TestBatchActionCall(BaseTestCase):
    def setUp(self):
        super(TestBatchActionCall, self).setUp()

        self.action_def = {
            'request': {
                'operation': 'GetFrobs',
                'params': []
            }
        }

    @property
    def model(self):
        return Action('test', self.action_def, {})

    def test_batch_action_gets_pages_from_collection(self):
        collection = mock.Mock()
        collection.pages.return_value = []
        action = BatchAction(self.model)

        action(collection)

        collection.pages.assert_called_with()

    def test_batch_action_creates_parameters_from_items(self):
        self.action_def['request']['params'] = [
            {'target': 'Bucket', 'source': 'data', 'path': 'BucketName'},
            {'target': 'Delete.Objects[].Key', 'source': 'data',
             'path': 'Key'}
        ]

        client = mock.Mock()

        item1 = mock.Mock()
        item1.meta = ResourceMeta('test', client=client, data={
            'BucketName': 'bucket',
            'Key': 'item1'
        })

        item2 = mock.Mock()
        item2.meta = ResourceMeta('test', client=client, data={
            'BucketName': 'bucket',
            'Key': 'item2'
        })

        collection = mock.Mock()
        collection.pages.return_value = [[item1, item2]]

        action = BatchAction(self.model)
        action(collection)

        client.get_frobs.assert_called_with(Bucket='bucket', Delete={
            'Objects': [
                {'Key': 'item1'},
                {'Key': 'item2'}
            ]
        })

    @mock.patch('boto3.resources.action.create_request_parameters',
                return_value={})
    def test_batch_action_skips_operation(self, crp_mock):
        # In this test we have an item from the collection, but no
        # parameters are set up. Because of this, we do NOT call
        # the batch operation.
        client = mock.Mock()

        item = mock.Mock()
        item.meta = ResourceMeta('test', client=client)

        collection = mock.Mock()
        collection.pages.return_value = [[item]]

        model = self.model
        action = BatchAction(model)
        action(collection)

        crp_mock.assert_called_with(item, model.request, params={})
        client.get_frobs.assert_not_called()

    @mock.patch('boto3.resources.action.create_request_parameters')
    def test_batch_action_calls_operation(self, crp_mock):
        # In this test we have an item and parameters, so the call
        # to the batch operation should be made.
        def side_effect(resource, model, params=None):
            params['foo'] = 'bar'

        crp_mock.side_effect = side_effect

        client = mock.Mock()

        item = mock.Mock()
        item.meta = ResourceMeta('test', client=client)

        collection = mock.Mock()
        collection.pages.return_value = [[item]]

        model = self.model
        action = BatchAction(model)
        action(collection)

        # Here the call is made with params={}, but they are edited
        # in-place so we need to compare to the final edited value.
        crp_mock.assert_called_with(item, model.request,
                                    params={'foo': 'bar'})
        client.get_frobs.assert_called_with(foo='bar')
