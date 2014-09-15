# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import os

import boto3.resources
from boto3.resources import ServiceResource, ResourceFactory
from tests import BaseTestCase


class TestResourceFactory(BaseTestCase):
    def setUp(self):
        super(TestResourceFactory, self).setUp()
        self.factory = ResourceFactory()
        boto3.resources.RESOURCE_ROOT = os.path.join(
            os.path.dirname(__file__),
            'data'
        )

    def test_get_service_returns_resource_class(self):
        TestResource = self.factory.create_class('test')

        self.assertIn(ServiceResource, TestResource.__bases__,
            'Did not return a ServiceResource subclass for service')

    def test_get_resource_returns_resource_class(self):
        Queue = self.factory.create_class('test', 'Queue')

        self.assertIn(ServiceResource, Queue.__bases__,
            'Did not return a ServiceResource subclass for resource')

    def test_factory_sets_service_name(self):
        Queue = self.factory.create_class('test', 'Queue')

        self.assertEqual(Queue.service_name, 'test',
            'Service name not set')

    def test_factory_sets_identifiers(self):
        Message = self.factory.create_class('test', 'Message')

        self.assertTrue(hasattr(Message, 'identifiers'),
            'Class has no identifiers')
        self.assertIn('queue_url', Message.identifiers,
            'Missing queue_url identifier from model')
        self.assertIn('receipt_handle', Message.identifiers,
            'Missing receipt_handle identifier from model')

    def test_factory_creates_dangling_resources(self):
        TestResource = self.factory.create_class('test')

        self.assertTrue(hasattr(TestResource, 'Queue'),
            'Missing Queue class from model')
        self.assertTrue(hasattr(TestResource, 'Message'),
            'Missing Message class from model')

    def test_can_instantiate_service_resource(self):
        TestResource = self.factory.create_class('test')
        resource = TestResource()

        self.assertIsInstance(resource, ServiceResource,
            'Object is not an instance of ServiceResource')

    def test_dangling_resources_create_resource_instance(self):
        resource = self.factory.create_class('test')()
        q = resource.Queue('test')

        self.assertIsInstance(q, ServiceResource,
            'Dangling resource instance not a ServiceResource')

    def test_dangling_resource_create_with_kwarg(self):
        resource = self.factory.create_class('test')()
        q = resource.Queue(url='test')

        self.assertIsInstance(q, ServiceResource,
            'Dangling resource created with kwargs is not a ServiceResource')

    def test_dangling_resource_shares_client(self):
        resource = self.factory.create_class('test')()
        q = resource.Queue('test')

        self.assertEqual(resource.client, q.client,
            'Client was not shared to dangling resource instance')

    def test_dangling_resource_requires_identifier(self):
        resource = self.factory.create_class('test')()

        with self.assertRaises(ValueError):
            resource.Queue()
