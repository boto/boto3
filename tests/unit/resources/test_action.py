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
from boto3.resources.model import Action
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
        resource.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }

        action = ServiceAction(self.action)

        action(resource, foo=1)

        self.assertTrue(params_mock.called,
            'Parameters for operation not created')

    @mock.patch('boto3.resources.action.create_request_parameters',
                return_value={'bar': 'baz'})
    def test_service_action_calls_operation(self, params_mock):
        resource = mock.Mock()
        resource.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }
        operation = resource.meta['client'].get_frobs
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
        resource.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }
        operation = resource.meta['client'].get_frobs
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
        resource.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }
        operation = resource.meta['client'].get_frobs
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
