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
from tests import mock, unittest


class TestSession(unittest.TestCase):
    def setUp(self):
        self.bc_session_patch = mock.patch('botocore.session.Session', autospec=True)
        self.BCSession = self.bc_session_patch.start()

    def tearDown(self):
        self.bc_session_patch.stop()

    def test_arguments_not_required(self):
        Session()

        self.assertTrue(self.BCSession.called,
            'Botocore session was not created!')

    def test_credentials_can_be_set(self):
        bc_session = self.BCSession.return_value

        # Set values in constructor
        Session(aws_access_key_id='key',
                aws_secret_access_key='secret',
                aws_session_token='token')

        self.assertTrue(self.BCSession.called,
            'Botocore session was not created!')
        self.assertTrue(bc_session.set_credentials.called,
            'Botocore session set_credentials not called from constructor!')
        bc_session.set_credentials.assert_called_with(
            'key', 'secret', 'token')

    def test_custom_session(self):
        bc_session = self.BCSession()
        self.BCSession.reset_mock()

        Session(botocore_session=bc_session)

        # No new session was created
        self.assertFalse(self.BCSession.called)

    def test_get_available_services(self):
        bc_session = self.BCSession.return_value

        session = Session()
        session.get_available_services()

        self.assertTrue(bc_session.get_available_services.called,
            'Botocore session get_available_services not called!')

    @unittest.skip(True)
    def test_get_available_resources(self):
        # TODO: Once implemented, write this test!
        # session = Session()
        # session.get_available_resources()
        pass

    @unittest.skip(True)
    def test_create_client(self):
        # TODO: Once implemented, write this test!
        # session = Session()
        # session.client('sqs')
        pass

    @unittest.skip(True)
    def test_create_resource(self):
        # TODO: Once implemented, write this test!
        # session = Session()
        # session.resource('sqs')
        pass
