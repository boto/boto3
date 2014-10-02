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
from boto3.resources.base import ServiceResource
from boto3.resources.factory import ResourceFactory
from boto3.resources.response import build_identifiers, RawHandler,\
                                     ResourceHandler


class TestBuildIdentifiers(BaseTestCase):
    def test_build_identifier_from_res_path_scalar(self):
        identifier_defs = [{
            'target': 'Id',
            'sourceType': 'responsePath',
            'source': 'Container.Frob.Id'
        }]

        parent = mock.Mock()
        params = {}
        response = {
            'Container': {
                'Frob': {
                    'Id': 'response-path'
                }
            }
        }

        values = build_identifiers(identifier_defs, parent, params, response)

        self.assertEqual(values['id'], 'response-path',
            'Identifier loaded from responsePath scalar not set')

    def test_build_identifier_from_res_path_list(self):
        identifier_defs = [{
            'target': 'Id',
            'sourceType': 'responsePath',
            'source': 'Container.Frobs[].Id'
        }]

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

        values = build_identifiers(identifier_defs, parent, params, response)

        self.assertEqual(values['id'], ['response-path'],
            'Identifier loaded from responsePath list not set')

    def test_build_identifier_from_parent_identifier(self):
        identifier_defs = [{
            'target': 'Id',
            'sourceType': 'identifier',
            'source': 'Id'
        }]

        parent = mock.Mock()
        parent.id = 'identifier'
        params = {}
        response = {
            'Container': {
                'Frobs': []
            }
        }

        values = build_identifiers(identifier_defs, parent, params, response)

        self.assertEqual(values['id'], 'identifier',
            'Identifier loaded from parent identifier not set')

    def test_build_identifier_from_parent_data_member(self):
        identifier_defs = [{
            'target': 'Id',
            'sourceType': 'dataMember',
            'source': 'Member'
        }]

        parent = mock.Mock()
        parent.member = 'data-member'
        params = {}
        response = {
            'Container': {
                'Frobs': []
            }
        }

        values = build_identifiers(identifier_defs, parent, params, response)

        self.assertEqual(values['id'], 'data-member',
            'Identifier loaded from parent data member not set')

    def test_build_identifier_from_req_param(self):
        identifier_defs = [{
            'target': 'Id',
            'sourceType': 'requestParameter',
            'source': 'Param'
        }]

        parent = mock.Mock()
        params = {
            'Param': 'request-param'
        }
        response = {
            'Container': {
                'Frobs': []
            }
        }

        values = build_identifiers(identifier_defs, parent, params, response)

        self.assertEqual(values['id'], 'request-param',
            'Identifier loaded from request parameter not set')

    def test_build_identifier_from_invalid_source_type(self):
        identifier_defs = [{
            'target': 'Id',
            'sourceType': 'invalid',
            'source': 'abc'
        }]

        parent = mock.Mock()
        params = {}
        response = {
            'Container': {
                'Frobs': []
            }
        }

        with self.assertRaises(NotImplementedError):
            build_identifiers(identifier_defs, parent, params, response)


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
    def _get_resource_scalar(self, search_path, response):
        request_resource_def = {
            'type': 'Frob',
            'identifiers': [
                {'target': 'Id', 'sourceType': 'responsePath',
                 'source': 'Container.Id'},
            ]
        }
        factory = ResourceFactory()
        resource_defs = {
            'Frob': {
                'shape': 'Frob',
                'identifiers': [
                    {'name': 'Id'}
                ]
            }
        }
        service_model = mock.Mock()
        shape = mock.Mock()
        shape.members = {}
        service_model.shape_for.return_value = shape
        parent = mock.Mock()
        parent.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }
        params = {}

        handler = ResourceHandler(search_path, factory, resource_defs,
            service_model, request_resource_def)
        return handler(parent, params, response)

    def test_create_resource_scalar(self):
        search_path = 'Container'
        response = {
            'Container': {
                'Id': 'a-frob',
                'OtherValue': 'other',
            }
        }
        resource = self._get_resource_scalar(search_path, response)

        self.assertIsInstance(resource, ServiceResource,
            'No resource instance returned from handler')

    def test_missing_data_scalar_returns_none(self):
        search_path = 'Container'
        response = {
            'something': 'irrelevant'
        }

        resource = self._get_resource_scalar(search_path, response)

        self.assertIsNone(resource,
            'Data returned even though response path was empty')

    def _get_resource_list(self, search_path, response):
        request_resource_def = {
            'type': 'Frob',
            'identifiers': [
                {'target': 'Id', 'sourceType': 'responsePath',
                 'source': 'Container.Frobs[].Id'},
            ]
        }
        factory = ResourceFactory()
        resource_defs = {
            'Frob': {
                'shape': 'Frob',
                'identifiers': [
                    {'name': 'Id'}
                ]
            }
        }
        service_model = mock.Mock()
        shape = mock.Mock()
        shape.members = {}
        service_model.shape_for.return_value = shape
        parent = mock.Mock()
        parent.meta = {
            'service_name': 'test',
            'client': mock.Mock(),
        }
        params = {}

        handler = ResourceHandler(search_path, factory, resource_defs,
            service_model, request_resource_def)
        return handler(parent, params, response)

    def test_create_resource_list(self):
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

        resources = self._get_resource_list(search_path, response)

        self.assertIsInstance(resources, list,
            'No list returned from handler')
        self.assertEqual(len(resources), 2,
            'Exactly two frobs should be returned')
        self.assertIsInstance(resources[0], ServiceResource,
            'List items are not resource instances')

    def test_missing_data_list_returns_none(self):
        search_path = 'Container.Frobs[]'
        response = {
            'something': 'irrelevant'
        }

        resources = self._get_resource_list(search_path, response)

        self.assertIsNone(resources,
            'Data returned even though response was path empty')

    def test_empty_list_passes_through(self):
        search_path = 'Container.Frobs[]'
        response = {
            'Container': {
                'Frobs': []
            }
        }

        resources = self._get_resource_list(search_path, response)

        self.assertIsInstance(resources, list,
            'No list returned from handler')
        self.assertEqual(len(resources), 0,
            'Exactly zero frobs should be returned')
