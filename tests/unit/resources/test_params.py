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

from boto3.resources.model import Request
from boto3.resources.params import create_request_parameters, \
                                   build_param_structure
from tests import BaseTestCase, mock

class TestServiceActionParams(BaseTestCase):
    def test_service_action_params_identifier(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'WarehouseUrl',
                    'sourceType': 'identifier',
                    'source': 'Url'
                }
            ]
        })

        parent = mock.Mock()
        parent.url = 'w-url'

        params = create_request_parameters(parent, request_model)

        self.assertEqual(params['WarehouseUrl'], 'w-url',
            'Parameter not set from resource identifier')

    def test_service_action_params_data_member(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'WarehouseUrl',
                    'sourceType': 'dataMember',
                    'source': 'some_member'
                }
            ]
        })

        parent = mock.Mock()
        parent.some_member = 'w-url'

        params = create_request_parameters(parent, request_model)

        self.assertEqual(params['WarehouseUrl'], 'w-url',
            'Parameter not set from resource property')

    def test_service_action_params_constants(self):
        request_model = Request({
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
        })

        params = create_request_parameters(None, request_model)

        self.assertEqual(params['Param1'], 'param1',
            'Parameter not set from string constant')
        self.assertEqual(params['Param2'], 123,
            'Parameter not set from integer constant')
        self.assertEqual(params['Param3'], True,
            'Parameter not set from boolean constant')

    def test_service_action_params_invalid(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'Param1',
                    'sourceType': 'invalid',
                    'source': 'param1'
                }
            ]
        })

        with self.assertRaises(NotImplementedError):
            create_request_parameters(None, request_model)

    def test_service_action_params_list(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'WarehouseUrls[0]',
                    'sourceType': 'string',
                    'source': 'w-url'
                }
            ]
        })

        params = create_request_parameters(None, request_model)

        self.assertIsInstance(params['WarehouseUrls'], list,
            'Parameter did not create a list')
        self.assertEqual(len(params['WarehouseUrls']), 1,
            'Parameter list should only have a single item')
        self.assertIn('w-url', params['WarehouseUrls'],
            'Parameter not in expected list')

    def test_service_action_params_reuse(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'Delete.Objects[].Key',
                    'sourceType': 'dataMember',
                    'source': 'Key'
                }
            ]
        })

        item1 = mock.Mock()
        item1.key = 'item1'

        item2 = mock.Mock()
        item2.key = 'item2'

        # Here we create params and then re-use it to build up a more
        # complex structure over multiple calls.
        params = create_request_parameters(item1, request_model)
        create_request_parameters(item2, request_model, params=params)

        self.assertEqual(params, {
            'Delete': {
                'Objects': [
                    {'Key': 'item1'},
                    {'Key': 'item2'}
                ]
            }
        })


class TestStructBuilder(BaseTestCase):
    def test_simple_value(self):
        params = {}
        build_param_structure(params, 'foo', 'bar')
        self.assertEqual(params['foo'], 'bar')

    def test_nested_dict(self):
        params = {}
        build_param_structure(params, 'foo.bar.baz', 123)
        self.assertEqual(params['foo']['bar']['baz'], 123)

    def test_nested_list(self):
        params = {}
        build_param_structure(params, 'foo.bar[0]', 'test')
        self.assertEqual(params['foo']['bar'][0], 'test')

    def test_strange_offset(self):
        params = {}
        build_param_structure(params, 'foo[2]', 'test')
        self.assertEqual(params['foo'], [{}, {}, 'test'])

    def test_nested_list_dict(self):
        params = {}
        build_param_structure(params, 'foo.bar[0].baz', 123)
        self.assertEqual(params['foo']['bar'][0]['baz'], 123)

    def test_modify_existing(self):
        params = {
            'foo': [
                {'key': 'abc'}
            ]
        }
        build_param_structure(params, 'foo[0].secret', 123)
        self.assertEqual(params['foo'][0]['key'], 'abc')
        self.assertEqual(params['foo'][0]['secret'], 123)

    def test_append_no_index(self):
        params = {}
        build_param_structure(params, 'foo[]', 123)
        self.assertEqual(params['foo'], [123])

        build_param_structure(params, 'foo[]', 456)
        self.assertEqual(params['foo'], [123, 456])
