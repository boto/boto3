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
