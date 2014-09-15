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

from boto3.resources import ServiceResource, ResourceFactory
from tests import BaseTestCase


class TestResourceFactory(BaseTestCase):
    def setUp(self):
        super(TestResourceFactory, self).setUp()
        self.factory = ResourceFactory()

    def test_get_service_returns_resource_class(self):
        SQS = self.factory.create_class('sqs')

        self.assertIn(ServiceResource, SQS.__bases__,
            'Did not return a ServiceResource subclass for service')

    def test_get_resource_returns_resource_class(self):
        Queue = self.factory.create_class('sqs', 'Queue')

        self.assertIn(ServiceResource, Queue.__bases__,
            'Did not return a ServiceResource subclass for resource')

    def test_factory_sets_service_name(self):
        Queue = self.factory.create_class('sqs', 'Queue')

        self.assertEqual(Queue.service_name, 'sqs',
            'Service name not set')

    def test_factory_sets_identifiers(self):
        Message = self.factory.create_class('sqs', 'Message')

        self.assertTrue(hasattr(Message, 'identifiers'),
            'Class has no identifiers')
        self.assertIn('queue_url', Message.identifiers,
            'Missing queue_url identifier from model')
        self.assertIn('receipt_handle', Message.identifiers,
            'Missing receipt_handle identifier from model')

    def test_factory_creates_dangling_resources(self):
        SQS = self.factory.create_class('sqs')

        self.assertTrue(hasattr(SQS, 'Queue'),
            'Missing Queue class from model')
        self.assertTrue(hasattr(SQS, 'Message'),
            'Missing Message class from model')

    def test_can_instantiate_service_resource(self):
        SQS = self.factory.create_class('sqs')
        sqs = SQS()

        self.assertIsInstance(sqs, ServiceResource,
            'Object is not an instance of ServiceResource')

    def test_dangling_resources_create_resource_instance(self):
        sqs = self.factory.create_class('sqs')()
        q = sqs.Queue('test')

        self.assertIsInstance(q, ServiceResource,
            'Dangling resource instance not a ServiceResource')

    def test_dangling_resource_create_with_kwarg(self):
        sqs = self.factory.create_class('sqs')()
        q = sqs.Queue(url='test')

        self.assertIsInstance(q, ServiceResource,
            'Dangling resource created with kwargs is not a ServiceResource')

    def test_dangling_resource_shares_client(self):
        sqs = self.factory.create_class('sqs')()
        q = sqs.Queue('test')

        self.assertEqual(sqs.client, q.client,
            'Client was not shared to dangling resource instance')

    def test_dangling_resource_requires_identifier(self):
        sqs = self.factory.create_class('sqs')()

        with self.assertRaises(ValueError):
            sqs.Queue()
