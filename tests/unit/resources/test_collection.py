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
from tests import BaseTestCase, mock


class TestResourceCollection(BaseTestCase):
    def setUp(self):
        super(TestResourceCollection, self).setUp()
   
    def get_collection(self, paginated=False):
        collection_def = {
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
        response = {
            'Frobs': [
                {'Id': 'one'},
                {'Id': 'two'},
                {'Id': 'three'},
                {'Id': 'four'}
            ]
        }
        pages = [
            {'Frobs': [{'Id': 'one'}, {'Id': 'two'}]},
            {'Frobs': [{'Id': 'three'}, {'Id': 'four'}]}
        ]
        client = mock.Mock()
        client.get_frobs.return_value = response
        client.can_paginate.return_value = paginated
        client.get_paginator.return_value.paginate.return_value = pages
        meta = {
            'client': client,
            'service_name': 'test'
        }
        parent = mock.Mock()
        parent.meta = meta
        factory = ResourceFactory()
        resource_defs = {
            'Frob': {
                'identifiers': [
                    {'name': 'Id'}
                ]
            }
        }
        service_model = ServiceModel({})
        collection = CollectionManager(collection_def, parent, factory,
            resource_defs, service_model)
        return client, collection

    def test_repr(self):
        client, collection = self.get_collection()

        self.assertIn('CollectionManager', repr(collection))

    def test_iteration_manager(self):
        client, collection = self.get_collection()
        with self.assertRaises(TypeError):
            list(collection)

    def test_iteration_non_paginated(self):
        client, collection = self.get_collection()
        item_count = len(list(collection.all()))
        self.assertEqual(item_count, 4)

    def test_limit_param_non_paginated(self):
        client, collection = self.get_collection()
        item_count = len(list(collection.all(limit=2)))
        self.assertEqual(item_count, 2)

    def test_limit_method_non_paginated(self):
        client, collection = self.get_collection()
        item_count = len(list(collection.limit(2)))
        self.assertEqual(item_count, 2)

    def test_filters_non_paginated(self):
        client, collection = self.get_collection()

        list(collection.filter(limit=2, Param1='foo', Param2=3))

        # Note - limit is not passed through to the low-level call
        client.get_frobs.assert_called_with(Param1='foo', Param2=3)

    def test_iteration_paginated(self):
        client, collection = self.get_collection(paginated=True)
        item_count = len(list(collection.all()))
        self.assertEqual(item_count, 4)

        # Low-level pagination should have been called
        client.get_paginator.assert_called_with('get_frobs')
        paginator = client.get_paginator.return_value
        paginator.paginate.assert_called_with(page_size=None, max_items=None)

    def test_limit_param_paginated(self):
        client, collection = self.get_collection(paginated=True)
        item_count = len(list(collection.all(limit=2)))
        self.assertEqual(item_count, 2)

    def test_limit_method_paginated(self):
        client, collection = self.get_collection(paginated=True)
        item_count = len(list(collection.limit(2)))
        self.assertEqual(item_count, 2)

    def test_filters_paginated(self):
        client, collection = self.get_collection(paginated=True)

        list(collection.filter(limit=2, Param1='foo', Param2=3))

        paginator = client.get_paginator.return_value
        paginator.paginate.assert_called_with(
            page_size=None, max_items=2, Param1='foo', Param2=3)

    def test_page_size_param(self):
        client, collection = self.get_collection(paginated=True)
        list(collection.all(page_size=1))
        paginator = client.get_paginator.return_value
        paginator.paginate.assert_called_with(page_size=1, max_items=None)

    def test_page_size_method(self):
        client, collection = self.get_collection(paginated=True)
        list(collection.page_size(1))
        paginator = client.get_paginator.return_value
        paginator.paginate.assert_called_with(page_size=1, max_items=None)

    def test_chaining(self):
        client, collection = self.get_collection()

        items = list(collection.filter().all().all())

        self.assertEqual(len(items), 4)

    def test_chaining_copies_parameters(self):
        client, collection = self.get_collection(paginated=True)

        list(collection.all().filter(CustomArg=1).limit(3).page_size(3))

        paginator = client.get_paginator.return_value
        paginator.paginate.assert_called_with(page_size=3,
            max_items=3, CustomArg=1)

    def test_chained_repr(self):
        client, collection = self.get_collection()

        self.assertIn('ResourceCollection', repr(collection.all()))
