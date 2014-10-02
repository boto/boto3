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

from boto3.resources.params import create_request_parameters
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

        params = create_request_parameters(parent, action_def['request'])

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

        params = create_request_parameters(parent, action_def['request'])

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

        params = create_request_parameters(None, action_def['request'])

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

        with self.assertRaises(NotImplementedError):
            create_request_parameters(None, action_def['request'])

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

        params = create_request_parameters(None, action_def['request'])

        self.assertIsInstance(params['WarehouseUrls'], list,
            'Parameter did not create a list')
        self.assertEqual(len(params['WarehouseUrls']), 1,
            'Parameter list should only have a single item')
        self.assertIn('w-url', params['WarehouseUrls'],
            'Parameter not in expected list')
