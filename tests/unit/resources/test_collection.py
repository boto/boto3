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

from botocore.model import ServiceModel
from boto3.resources.collection import CollectionManager
from boto3.resources.factory import ResourceFactory
from boto3.resources.model import Collection
from tests import BaseTestCase, mock


class TestResourceCollection(BaseTestCase):
    def setUp(self):
        super(TestResourceCollection, self).setUp()

        # Minimal definition so things like repr work
        self.collection_def = {
            'request': {
                'operation': 'TestOperation'
            },
            'resource': {
                'type': 'Frob'
            }
        }
        self.client = mock.Mock()
        self.client.can_paginate.return_value = False
        meta = {
            'client': self.client,
            'service_name': 'test'
        }
        self.parent = mock.Mock()
        self.parent.meta = meta
        self.factory = ResourceFactory()
        self.service_model = ServiceModel({})
   
    def get_collection(self):
        resource_defs = {
            'Frob': {
                'identifiers': []
            }
        }

        # Build up a resource def identifier list based on what
        # the collection is expecting to be required from its
        # definition. This saves a bunch of repetitive typing
        # and lets you just define a collection in the tests
        # below. Any identifiers you expect to be availabe in
        # the resource definition will automatically be there.
        resource_def = self.collection_def.get('resource', {})
        for identifier in resource_def.get('identifiers', []):
            resource_defs['Frob']['identifiers'].append(
                {'name': identifier['target']})

        collection_model = Collection(
            'test', self.collection_def, resource_defs)

        collection = CollectionManager(
            collection_model, self.parent, self.factory,
            resource_defs, self.service_model)
        return collection

    def test_repr(self):
        collection = self.get_collection()
        self.assertIn('CollectionManager', repr(collection))

    def test_iteration_manager(self):
        # A collection manager is not iterable. You must first call
        # .all or .filter or another method to get an iterable.
        collection = self.get_collection()
        with self.assertRaises(TypeError):
            list(collection)

    def test_iteration_non_paginated(self):
        self.collection_def = {
            'request': {
                'operation': 'GetFrobs'
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {
                        'target': 'Id',
                        'sourceType': 'responsePath',
                        'source': 'Frobs[].Id'
                    }
                ]
            }
        }
        self.client.get_frobs.return_value = {
            'Frobs': [
                {'Id': 'one'},
                {'Id': 'two'},
                {'Id': 'three'},
                {'Id': 'four'}
            ]
        }
        collection = self.get_collection()
        items = list(collection.all())
        self.assertEqual(len(items), 4)
        self.assertEqual(items[0].id, 'one')
        self.assertEqual(items[1].id, 'two')
        self.assertEqual(items[2].id, 'three')
        self.assertEqual(items[3].id, 'four')

    def test_limit_param_non_paginated(self):
        self.collection_def = {
            'request': {
                'operation': 'GetFrobs'
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {
                        'target': 'Id',
                        'sourceType': 'responsePath',
                        'source': 'Frobs[].Id'
                    }
                ]
            }
        }
        self.client.get_frobs.return_value = {
            'Frobs': [
                {'Id': 'one'},
                {'Id': 'two'},
                {'Id': 'three'},
                {'Id': 'four'}
            ]
        }
        collection = self.get_collection()
        items = list(collection.all(limit=2))
        self.assertEqual(len(items), 2)

        # Only the first two should be present
        self.assertEqual(items[0].id, 'one')
        self.assertEqual(items[1].id, 'two')

    def test_limit_method_non_paginated(self):
        self.collection_def = {
            'request': {
                'operation': 'GetFrobs'
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {
                        'target': 'Id',
                        'sourceType': 'responsePath',
                        'source': 'Frobs[].Id'
                    }
                ]
            }
        }
        self.client.get_frobs.return_value = {
            'Frobs': [
                {'Id': 'one'},
                {'Id': 'two'},
                {'Id': 'three'},
                {'Id': 'four'}
            ]
        }
        collection = self.get_collection()
        items = list(collection.limit(2))
        self.assertEqual(len(items), 2)

        # Only the first two should be present
        self.assertEqual(items[0].id, 'one')
        self.assertEqual(items[1].id, 'two')

    @mock.patch('boto3.resources.collection.ResourceHandler')
    def test_filters_non_paginated(self, handler):
        self.collection_def = {
            'request': {
                'operation': 'GetFrobs'
            },
            'resource': {
                'type': 'Frob',
                'identifiers': []
            }
        }
        self.client.get_frobs.return_value = {}
        handler.return_value.return_value = []
        collection = self.get_collection()

        list(collection.filter(limit=2, Param1='foo', Param2=3))

        # Note - limit is not passed through to the low-level call
        self.client.get_frobs.assert_called_with(Param1='foo', Param2=3)

    def test_iteration_paginated(self):
        self.collection_def = {
            'request': {
                'operation': 'GetFrobs'
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {
                        'target': 'Id',
                        'sourceType': 'responsePath',
                        'source': 'Frobs[].Id'
                    }
                ]
            }
        }
        self.client.can_paginate.return_value = True
        self.client.get_paginator.return_value.paginate.return_value = [
            {
                'Frobs': [
                    {'Id': 'one'},
                    {'Id': 'two'}
                ]
            }, {
                'Frobs': [
                    {'Id': 'three'},
                    {'Id': 'four'}
                ]
            }
        ]
        collection = self.get_collection()
        items = list(collection.all())
        self.assertEqual(len(items), 4)
        self.assertEqual(items[0].id, 'one')
        self.assertEqual(items[1].id, 'two')
        self.assertEqual(items[2].id, 'three')
        self.assertEqual(items[3].id, 'four')

        # Low-level pagination should have been called
        self.client.get_paginator.assert_called_with('get_frobs')
        paginator = self.client.get_paginator.return_value
        paginator.paginate.assert_called_with(page_size=None, max_items=None)

    def test_limit_param_paginated(self):
        self.collection_def = {
            'request': {
                'operation': 'GetFrobs'
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {
                        'target': 'Id',
                        'sourceType': 'responsePath',
                        'source': 'Frobs[].Id'
                    }
                ]
            }
        }
        self.client.can_paginate.return_value = True
        self.client.get_paginator.return_value.paginate.return_value = [
            {
                'Frobs': [
                    {'Id': 'one'},
                    {'Id': 'two'}
                ]
            }, {
                'Frobs': [
                    {'Id': 'three'},
                    {'Id': 'four'}
                ]
            }
        ]
        collection = self.get_collection()
        items = list(collection.all(limit=2))
        self.assertEqual(len(items), 2)

        # Only the first two should be present
        self.assertEqual(items[0].id, 'one')
        self.assertEqual(items[1].id, 'two')

    def test_limit_method_paginated(self):
        self.collection_def = {
            'request': {
                'operation': 'GetFrobs'
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {
                        'target': 'Id',
                        'sourceType': 'responsePath',
                        'source': 'Frobs[].Id'
                    }
                ]
            }
        }
        self.client.can_paginate.return_value = True
        self.client.get_paginator.return_value.paginate.return_value = [
            {
                'Frobs': [
                    {'Id': 'one'},
                    {'Id': 'two'}
                ]
            }, {
                'Frobs': [
                    {'Id': 'three'},
                    {'Id': 'four'}
                ]
            }
        ]
        collection = self.get_collection()
        items = list(collection.all(limit=2))
        self.assertEqual(len(items), 2)

        # Only the first two should be present
        self.assertEqual(items[0].id, 'one')
        self.assertEqual(items[1].id, 'two')

    @mock.patch('boto3.resources.collection.ResourceHandler')
    def test_filters_paginated(self, handler):
        self.client.can_paginate.return_value = True
        self.client.get_paginator.return_value.paginate.return_value = []
        handler.return_value.return_value = []
        collection = self.get_collection()

        list(collection.filter(limit=2, Param1='foo', Param2=3))

        paginator = self.client.get_paginator.return_value
        paginator.paginate.assert_called_with(
            page_size=None, max_items=2, Param1='foo', Param2=3)

    @mock.patch('boto3.resources.collection.ResourceHandler')
    def test_page_size_param(self, handler):
        self.client.can_paginate.return_value = True
        self.client.get_paginator.return_value.paginate.return_value = []
        handler.return_value.return_value = []
        collection = self.get_collection()

        list(collection.all(page_size=1))

        paginator = self.client.get_paginator.return_value
        paginator.paginate.assert_called_with(page_size=1, max_items=None)

    @mock.patch('boto3.resources.collection.ResourceHandler')
    def test_page_size_method(self, handler):
        self.client.can_paginate.return_value = True
        self.client.get_paginator.return_value.paginate.return_value = []
        handler.return_value.return_value = []
        collection = self.get_collection()

        list(collection.page_size(1))

        paginator = self.client.get_paginator.return_value
        paginator.paginate.assert_called_with(page_size=1, max_items=None)

    def test_chaining(self):
        self.collection_def = {
            'request': {
                'operation': 'GetFrobs'
            },
            'resource': {
                'type': 'Frob',
                'identifiers': [
                    {
                        'target': 'Id',
                        'sourceType': 'responsePath',
                        'source': 'Frobs[].Id'
                    }
                ]
            }
        }
        self.client.get_frobs.return_value = {
            'Frobs': [
                {'Id': 'one'},
                {'Id': 'two'},
                {'Id': 'three'},
                {'Id': 'four'}
            ]
        }
        collection = self.get_collection()

        items = list(collection.filter().all().all())

        self.assertEqual(len(items), 4)
        self.assertEqual(items[0].id, 'one')
        self.assertEqual(items[1].id, 'two')
        self.assertEqual(items[2].id, 'three')
        self.assertEqual(items[3].id, 'four')

    @mock.patch('boto3.resources.collection.ResourceHandler')
    def test_chaining_copies_parameters(self, handler):
        self.client.can_paginate.return_value = True
        self.client.get_paginator.return_value.paginate.return_value = []
        handler.return_value.return_value = []
        collection = self.get_collection()

        list(collection.all().filter(CustomArg=1).limit(3).page_size(3))

        paginator = self.client.get_paginator.return_value
        paginator.paginate.assert_called_with(
            page_size=3, max_items=3, CustomArg=1)

    def test_chained_repr(self):
        collection = self.get_collection()

        self.assertIn('ResourceCollection', repr(collection.all()))
