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

from botocore import loaders
from botocore.exceptions import DataNotFoundError
from botocore.client import Config

from boto3 import __version__
from boto3.exceptions import NoVersionFound
from boto3.session import Session
from tests import mock, BaseTestCase


class TestSession(BaseTestCase):
    def test_repr(self):
        bc_session = self.bc_session_cls.return_value
        bc_session.get_credentials.return_value.access_key = 'abc123'
        bc_session.get_config_variable.return_value = 'us-west-2'

        session = Session('abc123', region_name='us-west-2')

        self.assertEqual(repr(session), 'Session(region=\'us-west-2\')')

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

    def test_profile_can_be_set(self):
        bc_session = self.bc_session_cls.return_value

        session = Session(profile_name='foo')

        bc_session.set_config_variable.assert_called_with(
            'profile', 'foo')
        bc_session.profile = 'foo'

        # We should also be able to read the value
        self.assertEqual(session.profile_name, 'foo')

    def test_profile_default(self):
        self.bc_session_cls.return_value.profile = None

        session = Session()

        self.assertEqual(session.profile_name, 'default')

    def test_custom_session(self):
        bc_session = self.bc_session_cls()
        self.bc_session_cls.reset_mock()

        Session(botocore_session=bc_session)

        # No new session was created
        self.assertFalse(self.bc_session_cls.called)

    def test_user_agent(self):
        # Here we get the underlying Botocore session, create a Boto 3
        # session, and ensure that the user-agent is modified as expected
        bc_session = self.bc_session_cls.return_value
        bc_session.user_agent_name = 'Botocore'
        bc_session.user_agent_version = '0.68.0'
        bc_session.user_agent_extra = ''

        Session(botocore_session=bc_session)

        self.assertEqual(bc_session.user_agent_name, 'Boto3')
        self.assertEqual(bc_session.user_agent_version, __version__)
        self.assertEqual(bc_session.user_agent_extra, 'Botocore/0.68.0')

    def test_user_agent_extra(self):
        # This test is the same as above, but includes custom extra content
        # which must still be in the final modified user-agent.
        bc_session = self.bc_session_cls.return_value
        bc_session.user_agent_name = 'Botocore'
        bc_session.user_agent_version = '0.68.0'
        bc_session.user_agent_extra = 'foo'

        Session(botocore_session=bc_session)

        self.assertEqual(bc_session.user_agent_extra, 'foo Botocore/0.68.0')

    def test_custom_user_agent(self):
        # This test ensures that a customized user-agent is left untouched.
        bc_session = self.bc_session_cls.return_value
        bc_session.user_agent_name = 'Custom'
        bc_session.user_agent_version = '1.0'
        bc_session.user_agent_extra = ''

        Session(botocore_session=bc_session)

        self.assertEqual(bc_session.user_agent_name, 'Custom')
        self.assertEqual(bc_session.user_agent_version, '1.0')
        self.assertEqual(bc_session.user_agent_extra, '')

    def test_get_available_services(self):
        bc_session = self.bc_session_cls.return_value

        session = Session()
        session.get_available_services()

        self.assertTrue(bc_session.get_available_services.called,
            'Botocore session get_available_services not called')

    def test_get_available_resources(self):
        mock_bc_session = mock.Mock()
        loader = mock.Mock(spec=loaders.Loader)
        loader.list_available_services.return_value = ['foo', 'bar']
        mock_bc_session.get_component.return_value = loader
        session = Session(botocore_session=mock_bc_session)

        names = session.get_available_resources()
        self.assertEqual(names, ['foo', 'bar'])

    def test_create_client(self):
        session = Session(region_name='us-east-1')
        client = session.client('sqs', region_name='us-west-2')

        self.assertTrue(client,
            'No low-level client was returned')

    def test_create_client_with_args(self):
        bc_session = self.bc_session_cls.return_value

        session = Session(region_name='us-east-1')
        session.client('sqs', region_name='us-west-2')

        bc_session.create_client.assert_called_with(
            'sqs', aws_secret_access_key=None, aws_access_key_id=None,
            endpoint_url=None, use_ssl=True, aws_session_token=None,
            verify=None, region_name='us-west-2', api_version=None,
            config=None)

    def test_create_resource_with_args(self):
        mock_bc_session = mock.Mock()
        loader = mock.Mock(spec=loaders.Loader)
        loader.determine_latest_version.return_value = '2014-11-02'
        loader.load_service_model.return_value = {'resources': [], 'service': []}
        mock_bc_session.get_component.return_value = loader
        session = Session(botocore_session=mock_bc_session)
        session.resource_factory.load_from_definition = mock.Mock()
        session.client = mock.Mock()

        session.resource('sqs', verify=False)

        session.client.assert_called_with(
            'sqs', aws_secret_access_key=None, aws_access_key_id=None,
            endpoint_url=None, use_ssl=True, aws_session_token=None,
            verify=False, region_name=None, api_version='2014-11-02',
            config=mock.ANY)
        client_config = session.client.call_args[1]['config']
        self.assertEqual(client_config.user_agent_extra, 'Resource')
        self.assertEqual(client_config.signature_version, None)

    def test_create_resource_with_config(self):
        mock_bc_session = mock.Mock()
        loader = mock.Mock(spec=loaders.Loader)
        loader.determine_latest_version.return_value = '2014-11-02'
        loader.load_service_model.return_value = {'resources': [], 'service': []}
        mock_bc_session.get_component.return_value = loader
        session = Session(botocore_session=mock_bc_session)
        session.resource_factory.load_from_definition = mock.Mock()
        session.client = mock.Mock()
        config = Config(signature_version='v4')

        session.resource('sqs', config=config)

        session.client.assert_called_with(
            'sqs', aws_secret_access_key=None, aws_access_key_id=None,
            endpoint_url=None, use_ssl=True, aws_session_token=None,
            verify=None, region_name=None, api_version='2014-11-02',
            config=mock.ANY)
        client_config = session.client.call_args[1]['config']
        self.assertEqual(client_config.user_agent_extra, 'Resource')
        self.assertEqual(client_config.signature_version, 'v4')

    def test_create_resource_with_config_override_user_agent_extra(self):
        mock_bc_session = mock.Mock()
        loader = mock.Mock(spec=loaders.Loader)
        loader.determine_latest_version.return_value = '2014-11-02'
        loader.load_service_model.return_value = {'resources': [], 'service': []}
        mock_bc_session.get_component.return_value = loader
        session = Session(botocore_session=mock_bc_session)
        session.resource_factory.load_from_definition = mock.Mock()
        session.client = mock.Mock()
        config = Config(signature_version='v4', user_agent_extra='foo')

        session.resource('sqs', config=config)

        session.client.assert_called_with(
            'sqs', aws_secret_access_key=None, aws_access_key_id=None,
            endpoint_url=None, use_ssl=True, aws_session_token=None,
            verify=None, region_name=None, api_version='2014-11-02',
            config=mock.ANY)
        client_config = session.client.call_args[1]['config']
        self.assertEqual(client_config.user_agent_extra, 'foo')
        self.assertEqual(client_config.signature_version, 'v4')

    def test_create_resource_latest_version(self):
        mock_bc_session = mock.Mock()
        loader = mock.Mock(spec=loaders.Loader)
        loader.determine_latest_version.return_value = '2014-11-02'
        loader.load_service_model.return_value = {'resources': [], 'service': []}
        mock_bc_session.get_component.return_value = loader
        session = Session(botocore_session=mock_bc_session)
        session.resource_factory.load_from_definition = mock.Mock()

        session.resource('sqs')

        loader.load_service_model.assert_called_with(
            'sqs', 'resources-1', '2014-11-02')

    def test_bad_resource_name(self):
        mock_bc_session = mock.Mock()
        loader = mock.Mock(spec=loaders.Loader)
        loader.determine_latest_version.side_effect = DataNotFoundError(
            data_path='foo')
        mock_bc_session.get_component.return_value = loader

        session = Session(botocore_session=mock_bc_session)
        with self.assertRaises(DataNotFoundError):
            session.resource('sqs')

    def test_can_reach_events(self):
        mock_bc_session = self.bc_session_cls()
        session = Session(botocore_session=mock_bc_session)
        session.events
        mock_bc_session.get_component.assert_called_with('event_emitter')
