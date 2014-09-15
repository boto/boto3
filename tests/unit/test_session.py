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

from boto3.session import Session
from boto3.resources import ServiceResource
from tests import mock, unittest, BaseTestCase


class TestSession(BaseTestCase):
    def test_arguments_not_required(self):
        Session()

        self.assertTrue(self.bc_session_cls.called,
            'Botocore session was not created')

    def test_credentials_can_be_set(self):
        bc_session = self.bc_session_cls.return_value

        # Set values in constructor
        Session(aws_access_key_id='key',
                aws_secret_access_key='secret',
                aws_session_token='token')

        self.assertTrue(self.bc_session_cls.called,
            'Botocore session was not created')
        self.assertTrue(bc_session.set_credentials.called,
            'Botocore session set_credentials not called from constructor')
        bc_session.set_credentials.assert_called_with(
            'key', 'secret', 'token')

    def test_custom_session(self):
        bc_session = self.bc_session_cls()
        self.bc_session_cls.reset_mock()

        Session(botocore_session=bc_session)

        # No new session was created
        self.assertFalse(self.bc_session_cls.called)

    def test_get_available_services(self):
        bc_session = self.bc_session_cls.return_value

        session = Session()
        session.get_available_services()

        self.assertTrue(bc_session.get_available_services.called,
            'Botocore session get_available_services not called')

    def test_get_available_resources(self):
        session = Session()
        resources = session.get_available_resources()
        self.assertIsInstance(resources, list)

    @unittest.skip(True)
    def test_create_client(self):
        # TODO: Once implemented, write this test!
        # session = Session()
        # session.client('sqs')
        pass

    def test_create_resource(self):
        session = Session()
        session.client = mock.Mock()
        session.resource_factory.create_class = mock.Mock()
        cls = session.resource_factory.create_class.return_value

        sqs = session.resource('sqs')

        self.assertTrue(session.client.called,
            'No low-level client was created')
        self.assertTrue(session.resource_factory.create_class.called,
            'Resource factory did not look up class')
        self.assertTrue(cls.called,
            'Resource instance was not created')
        self.assertEqual(sqs, cls.return_value,
            'Returned instance is not an instance of the looked up resource '
            'class from the factory')
