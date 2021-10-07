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

from boto3.exceptions import ResourceLoadException
from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.model import Request
from boto3.resources.params import (
    create_request_parameters, build_param_structure
)
from tests import BaseTestCase, mock


class TestServiceActionParams(BaseTestCase):
    def test_service_action_params_identifier(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'WarehouseUrl',
                    'source': 'identifier',
                    'name': 'Url'
                }
            ]
        })

        parent = mock.Mock()
        parent.url = 'w-url'

        params = create_request_parameters(parent, request_model)

        assert params['WarehouseUrl'] == 'w-url'

    def test_service_action_params_data_member(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'WarehouseUrl',
                    'source': 'data',
                    'path': 'SomeMember'
                }
            ]
        })

        parent = mock.Mock()
        parent.meta = ResourceMeta('test', data={
            'SomeMember': 'w-url'
        })

        params = create_request_parameters(parent, request_model)

        assert params['WarehouseUrl'] == 'w-url'

    def test_service_action_params_data_member_missing(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'WarehouseUrl',
                    'source': 'data',
                    'path': 'SomeMember'
                }
            ]
        })

        parent = mock.Mock()

        def load_data():
            parent.meta.data = {
                'SomeMember': 'w-url'
            }

        parent.load.side_effect = load_data
        parent.meta = ResourceMeta('test')

        params = create_request_parameters(parent, request_model)

        parent.load.assert_called_with()
        assert params['WarehouseUrl'] == 'w-url'

    def test_service_action_params_data_member_missing_no_load(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'WarehouseUrl',
                    'source': 'data',
                    'path': 'SomeMember'
                }
            ]
        })

        # This mock has no ``load`` method.
        parent = mock.Mock(spec=ServiceResource)
        parent.meta = ResourceMeta('test', data=None)

        with pytest.raises(ResourceLoadException):
            create_request_parameters(parent, request_model)

    def test_service_action_params_constants(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'Param1',
                    'source': 'string',
                    'value': 'param1'
                },
                {
                    'target': 'Param2',
                    'source': 'integer',
                    'value': 123
                },
                {
                    'target': 'Param3',
                    'source': 'boolean',
                    'value': True
                }
            ]
        })

        params = create_request_parameters(None, request_model)

        assert params['Param1'] == 'param1'
        assert params['Param2'] == 123
        assert params['Param3'] is True

    def test_service_action_params_input(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {'target': 'Param1', 'source': 'input'}
            ]
        })

        params = create_request_parameters(None, request_model)
        assert params == {}

        params['param1'] = 'myinput'
        params = create_request_parameters(None, request_model, params=params)
        assert params == {'param1': 'myinput'}

    def test_service_action_params_invalid(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'Param1',
                    'source': 'invalid'
                }
            ]
        })

        with pytest.raises(NotImplementedError):
            create_request_parameters(None, request_model)

    def test_service_action_params_list(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'WarehouseUrls[0]',
                    'source': 'string',
                    'value': 'w-url'
                }
            ]
        })

        params = create_request_parameters(None, request_model)

        assert isinstance(params['WarehouseUrls'], list)
        assert len(params['WarehouseUrls']) == 1
        assert 'w-url' in params['WarehouseUrls']

    def test_service_action_params_reuse(self):
        request_model = Request({
            'operation': 'GetFrobs',
            'params': [
                {
                    'target': 'Delete.Objects[].Key',
                    'source': 'data',
                    'path': 'Key'
                }
            ]
        })

        item1 = mock.Mock()
        item1.meta = ResourceMeta('test', data={
            'Key': 'item1'
        })

        item2 = mock.Mock()
        item2.meta = ResourceMeta('test', data={
            'Key': 'item2'
        })

        # Here we create params and then re-use it to build up a more
        # complex structure over multiple calls.
        params = create_request_parameters(item1, request_model)
        create_request_parameters(item2, request_model, params=params)

        assert params == {
            'Delete': {
                'Objects': [
                    {'Key': 'item1'},
                    {'Key': 'item2'}
                ]
            }
        }


class TestStructBuilder(BaseTestCase):
    def test_simple_value(self):
        params = {}
        build_param_structure(params, 'foo', 'bar')
        assert params['foo'] == 'bar'

    def test_nested_dict(self):
        params = {}
        build_param_structure(params, 'foo.bar.baz', 123)
        assert params['foo']['bar']['baz'] == 123

    def test_nested_list(self):
        params = {}
        build_param_structure(params, 'foo.bar[0]', 'test')
        assert params['foo']['bar'][0] == 'test'

    def test_strange_offset(self):
        params = {}
        build_param_structure(params, 'foo[2]', 'test')
        assert params['foo'] == [{}, {}, 'test']

    def test_nested_list_dict(self):
        params = {}
        build_param_structure(params, 'foo.bar[0].baz', 123)
        assert params['foo']['bar'][0]['baz'] == 123

    def test_modify_existing(self):
        params = {
            'foo': [
                {'key': 'abc'}
            ]
        }
        build_param_structure(params, 'foo[0].secret', 123)
        assert params['foo'][0]['key'] == 'abc'
        assert params['foo'][0]['secret'] == 123

    def test_append_no_index(self):
        params = {}
        build_param_structure(params, 'foo[]', 123)
        assert params['foo'] == [123]

        build_param_structure(params, 'foo[]', 456)
        assert params['foo'] == [123, 456]

    def test_provided_index_with_wildcard(self):
        params = {}
        index = 0
        build_param_structure(params, 'foo[*].bar', 123, index)
        build_param_structure(params, 'foo[*].baz', 456, index)
        assert params['foo'][index] == {'bar': 123, 'baz': 456}

        index = 1
        build_param_structure(params, 'foo[*].bar', 789, index)
        build_param_structure(params, 'foo[*].baz', 123, index)
        assert params['foo'] == [
            {'bar': 123, 'baz': 456},
            {'bar': 789, 'baz': 123}
        ]
