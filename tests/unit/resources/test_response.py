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

from tests import BaseTestCase, mock
from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.model import ResponseResource, Parameter
from boto3.resources.factory import ResourceFactory
from boto3.resources.response import build_identifiers, build_empty_response,\
                                     RawHandler, ResourceHandler


class TestBuildIdentifiers(BaseTestCase):
    def test_build_identifier_from_res_path_scalar(self):
        identifiers = [Parameter(target='Id', source='response',
                                 path='Container.Frob.Id')]

        parent = mock.Mock()
        params = {}
        response = {
            'Container': {
                'Frob': {
                    'Id': 'response-path'
                }
            }
        }

        values = build_identifiers(identifiers, parent, params, response)

        self.assertEqual(values[0][1], 'response-path',
            'Identifier loaded from responsePath scalar not set')

    def test_build_identifier_from_res_path_list(self):
        identifiers = [Parameter(target='Id', source='response',
                       path='Container.Frobs[].Id')]

        parent = mock.Mock()
        params = {}
        response = {
            'Container': {
                'Frobs': [
                    {
                        'Id': 'response-path'
                    }
                ]
            }
        }

        values = build_identifiers(identifiers, parent, params, response)

        self.assertEqual(values[0][1], ['response-path'],
            'Identifier loaded from responsePath list not set')

    def test_build_identifier_from_parent_identifier(self):
        identifiers = [Parameter(target='Id', source='identifier',
                       name='Id')]

        parent = mock.Mock()
        parent.id = 'identifier'
        params = {}
        response = {
            'Container': {
                'Frobs': []
            }
        }

        values = build_identifiers(identifiers, parent, params, response)

        self.assertEqual(values[0][1], 'identifier',
            'Identifier loaded from parent identifier not set')

    def test_build_identifier_from_parent_data_member(self):
        identifiers = [Parameter(target='Id', source='data',
                       path='Member')]

        parent = mock.Mock()
        parent.meta = ResourceMeta('test', data={
            'Member': 'data-member'
        })
        params = {}
        response = {
            'Container': {
                'Frobs': []
            }
        }

        values = build_identifiers(identifiers, parent, params, response)

        self.assertEqual(values[0][1], 'data-member',
            'Identifier loaded from parent data member not set')

    def test_build_identifier_from_req_param(self):
        identifiers = [Parameter(target='Id', source='requestParameter',
                       path='Param')]

        parent = mock.Mock()
        params = {
            'Param': 'request-param'
        }
        response = {
            'Container': {
                'Frobs': []
            }
        }

        values = build_identifiers(identifiers, parent, params, response)

        self.assertEqual(values[0][1], 'request-param',
            'Identifier loaded from request parameter not set')

    def test_build_identifier_from_invalid_source_type(self):
        identifiers = [Parameter(target='Id', source='invalid')]

        parent = mock.Mock()
        params = {}
        response = {
            'Container': {
                'Frobs': []
            }
        }

        with self.assertRaises(NotImplementedError):
            build_identifiers(identifiers, parent, params, response)


class TestBuildEmptyResponse(BaseTestCase):
    def setUp(self):
        super(TestBuildEmptyResponse, self).setUp()

        self.search_path = ''
        self.operation_name = 'GetFrobs'

        self.output_shape = mock.Mock()

        operation_model = mock.Mock()
        operation_model.output_shape = self.output_shape

        self.service_model = mock.Mock()
        self.service_model.operation_model.return_value = operation_model

    def get_response(self):
        return build_empty_response(self.search_path, self.operation_name,
                                    self.service_model)

    def test_empty_structure(self):
        self.output_shape.type_name = 'structure'

        response = self.get_response()

        self.assertIsInstance(response, dict,
            'Structure should default to empty dictionary')
        self.assertFalse(response.items(),
            'Dictionary should be empty')

    def test_empty_list(self):
        self.output_shape.type_name = 'list'

        response = self.get_response()

        self.assertIsInstance(response, list,
            'List should default to empty list')
        self.assertFalse(len(response),
            'List should be empty')

    def test_empty_map(self):
        self.output_shape.type_name = 'map'

        response = self.get_response()

        self.assertIsInstance(response, dict,
            'Map should default to empty dictionary')
        self.assertFalse(response.items(),
            'Dictionary should be empty')

    def test_empty_string(self):
        self.output_shape.type_name = 'string'

        response = self.get_response()

        self.assertIsNone(response,
            'String should default to None')

    def test_empty_integer(self):
        self.output_shape.type_name = 'integer'

        response = self.get_response()

        self.assertIsNone(response,
            'Integer should default to None')

    def test_empty_unkown_returns_none(self):
        self.output_shape.type_name = 'invalid'

        response = self.get_response()

        self.assertIsNone(response,
            'Unknown types should default to None')

    def test_path_structure(self):
        self.search_path = 'Container.Frob'

        frob = mock.Mock()
        frob.type_name = 'integer'

        container = mock.Mock()
        container.type_name = 'structure'
        container.members = {
            'Frob': frob
        }

        self.output_shape.type_name = 'structure'
        self.output_shape.members = {
            'Container': container
        }

        response = self.get_response()

        self.assertEqual(response, None)

    def test_path_list(self):
        self.search_path = 'Container[1].Frob'

        frob = mock.Mock()
        frob.type_name = 'integer'

        container = mock.Mock()
        container.type_name = 'list'
        container.member = frob

        self.output_shape.type_name = 'structure'
        self.output_shape.members = {
            'Container': container
        }

        response = self.get_response()

        self.assertEqual(response, None)

    def test_path_invalid(self):
        self.search_path = 'Container.Invalid'

        container = mock.Mock()
        container.type_name = 'invalid'

        self.output_shape.type_name = 'structure'
        self.output_shape.members = {
            'Container': container
        }

        with self.assertRaises(NotImplementedError):
            self.get_response()


class TestRawHandler(BaseTestCase):
    def test_raw_handler_response(self):
        parent = mock.Mock()
        params = {}
        response = {
            'Id': 'foo'
        }

        handler = RawHandler(search_path=None)
        parsed_response = handler(parent, params, response)

        self.assertEqual(parsed_response, response,
            'Raw response not passed through unmodified')

    def test_raw_handler_response_path(self):
        parent = mock.Mock()
        params = {}
        frob = {
            'Id': 'foo'
        }
        response = {
            'Container': {
                'Frob': frob
            }
        }

        handler = RawHandler(search_path='Container.Frob')
        parsed_response = handler(parent, params, response)

        self.assertEqual(parsed_response, frob,
            'Search path not processed correctly')


class TestResourceHandler(BaseTestCase):
    def setUp(self):
        super(TestResourceHandler, self).setUp()
        self.identifier_path = ''
        self.factory = ResourceFactory()
        self.resource_defs = {
            'Frob': {
                'shape': 'Frob',
                'identifiers': [
                    {'name': 'Id'}
                ]
            }
        }
        self.service_model = mock.Mock()
        shape = mock.Mock()
        shape.members = {}
        self.service_model.shape_for.return_value = shape

        frobs = mock.Mock()
        frobs.type_name = 'list'
        container = mock.Mock()
        container.type_name = 'structure'
        container.members = {
            'Frobs': frobs
        }
        self.output_shape = mock.Mock()
        self.output_shape.type_name = 'structure'
        self.output_shape.members = {
            'Container': container
        }
        operation_model = mock.Mock()
        operation_model.output_shape = self.output_shape
        self.service_model.operation_model.return_value = operation_model

        self.parent = mock.Mock()
        self.parent.meta = ResourceMeta('test', client=mock.Mock())
        self.params = {}

    def get_resource(self, search_path, response):
        request_resource_def = {
            'type': 'Frob',
            'identifiers': [
                {'target': 'Id', 'source': 'response',
                 'path': self.identifier_path},
            ]
        }
        resource_model = ResponseResource(
            request_resource_def, self.resource_defs)

        handler = ResourceHandler(search_path, self.factory,
            self.resource_defs, self.service_model, resource_model,
            'GetFrobs')
        return handler(self.parent, self.params, response)

    def test_create_resource_scalar(self):
        self.identifier_path = 'Container.Id'
        search_path = 'Container'
        response = {
            'Container': {
                'Id': 'a-frob',
                'OtherValue': 'other',
            }
        }
        resource = self.get_resource(search_path, response)

        self.assertIsInstance(resource, ServiceResource,
            'No resource instance returned from handler')

    @mock.patch('boto3.resources.response.build_empty_response')
    def test_missing_data_scalar_builds_empty_response(self, build_mock):
        self.identifier_path = 'Container.Id'
        search_path = 'Container'
        response = {
            'something': 'irrelevant'
        }

        resources = self.get_resource(search_path, response)

        self.assertTrue(build_mock.called,
            'build_empty_response was never called')
        self.assertEqual(resources, build_mock.return_value,
            'build_empty_response return value was not returned')

    def test_create_resource_list(self):
        self.identifier_path = 'Container.Frobs[].Id'
        search_path = 'Container.Frobs[]'
        response = {
            'Container': {
                'Frobs': [
                    {
                        'Id': 'a-frob',
                        'OtherValue': 'other',
                    },
                    {
                        'Id': 'another-frob',
                        'OtherValue': 'foo',
                    }
                ]
            }
        }

        resources = self.get_resource(search_path, response)

        self.assertIsInstance(resources, list,
            'No list returned from handler')
        self.assertEqual(len(resources), 2,
            'Exactly two frobs should be returned')
        self.assertIsInstance(resources[0], ServiceResource,
            'List items are not resource instances')

    def test_create_resource_list_no_search_path(self):
        self.identifier_path = '[].Id'
        search_path = ''
        response = [
            {
                'Id': 'a-frob',
                'OtherValue': 'other'
            }
        ]

        resources = self.get_resource(search_path, response)

        self.assertIsInstance(resources, list,
            'No list returned from handler')
        self.assertEqual(len(resources), 1,
            'Exactly one frob should be returned')
        self.assertIsInstance(resources[0], ServiceResource,
            'List items are not resource instances')

    @mock.patch('boto3.resources.response.build_empty_response')
    def test_missing_data_list_builds_empty_response(self, build_mock):
        self.identifier_path = 'Container.Frobs[].Id'
        search_path = 'Container.Frobs[]'
        response = {
            'something': 'irrelevant'
        }

        resources = self.get_resource(search_path, response)

        self.assertTrue(build_mock.called,
            'build_empty_response was never called')
        self.assertEqual(resources, build_mock.return_value,
            'build_empty_response return value was not returned')
