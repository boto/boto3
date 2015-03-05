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

from boto3 import __version__
from boto3.exceptions import NoVersionFound
from boto3.session import Session
from tests import mock, BaseTestCase


def test_create_all_resources():
    """
    This generator yields test functions for each available
    resource via its service name. Individual tests can fail
    indepdendently to let you know which services are not
    working and why.
    """
    session = Session(aws_access_key_id='dummy',
                      aws_secret_access_key='dummy',
                      region_name='us-east-1')
    for service_name in session.get_available_resources():
        yield _test_create_resource, session, service_name

def _test_create_resource(session, service_name):
    # Instantiate a resource and make sure no exceptions are thrown.
    session.resource(service_name)


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

        self.assertEqual(bc_session.profile, 'foo')

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

    @mock.patch('os.path.isdir', return_value=True)
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=[
        'sqs-2012-11-05.resources.json', 's3-2006-03-01.resources.json'])
    def test_get_available_resources(self, list_mock, exist_mock, dir_mock):
        session = Session()
        self.loader.get_search_paths.return_value = ['search-path']

        names = session.get_available_resources()
        self.assertEqual(sorted(names), ['s3', 'sqs'])

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
            verify=None, region_name='us-west-2', api_version=None)

    @mock.patch('os.path.isdir', return_value=True)
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=['sqs-2012-11-05.resources.json'])
    def test_create_resource(self, list_mock, exist_mock, dir_mock):
        session = Session()
        session.client = mock.Mock()
        load_mock = mock.Mock()
        session.resource_factory.load_from_definition = load_mock
        cls = load_mock.return_value

        self.loader.get_search_paths.return_value = ['search-path']

        sqs = session.resource('sqs', verify=False)

        self.assertTrue(session.client.called,
            'No low-level client was created')
        self.assertTrue(load_mock.called,
            'Resource factory did not look up class')
        self.assertTrue(cls.called,
            'Resource instance was not created')
        self.assertEqual(sqs, cls.return_value,
            'Returned instance is not an instance of the looked up resource '
            'class from the factory')

    @mock.patch('os.path.isdir', return_value=True)
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=['sqs-2012-11-05.resources.json'])
    def test_create_resource_with_args(self, list_mock, exist_mock, dir_mock):
        session = Session()
        session.client = mock.Mock()
        session.resource_factory.load_from_definition = mock.Mock()

        self.loader.get_search_paths.return_value = ['search-path']

        session.resource('sqs', verify=False)

        session.client.assert_called_with(
            'sqs', aws_secret_access_key=None, aws_access_key_id=None,
            endpoint_url=None, use_ssl=True, aws_session_token=None,
            verify=False, region_name=None, api_version=None)

    @mock.patch('os.path.isdir', return_value=True)
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir',
                return_value=['sqs-2012-11-05.resources.json',
                              'sqs-2013-11-05.resources.json',
                              'sqs-2014-11-05.resources.json'])
    def test_create_resource_latest_version(self, list_mock, exist_mock,
                                            dir_mock):
        session = Session()
        session.client = mock.Mock()
        load_mock = mock.Mock()
        session.resource_factory.load_from_definition = load_mock

        self.loader.get_search_paths.return_value = ['search-path']

        session.resource('sqs')

        self.loader.load_data.assert_called_with('sqs-2014-11-05.resources')

    @mock.patch('os.path.isdir', return_value=True)
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=['s3-2006-03-01.resources.json'])
    def test_bad_resource_name(self, list_mock, exist_mock, dir_mock):
        session = Session()
        session.client = mock.Mock()
        load_mock = mock.Mock()
        session.resource_factory.load_from_definition = load_mock

        self.loader.get_search_paths.return_value = ['search-path']

        with self.assertRaises(NoVersionFound):
            # S3 is defined but not SQS!
            session.resource('sqs')

    # We make ``isdir`` return ``False``, then ``True`` because we
    # want the first path to be a file, and the second a directory.
    # This allows us to test both code paths while searching for
    # a value, otherwise the ``exists`` check is never performed.
    @mock.patch('os.path.isdir', side_effect=[False, True])
    @mock.patch('os.path.exists', return_value=False)
    def test_no_search_path_resources(self, exist_mock, dir_mock):
        session = Session()
        session.client = mock.Mock()
        load_mock = mock.Mock()
        session.resource_factory.load_from_definition = load_mock

        self.loader.get_search_paths.return_value = [
            'search-path1', 'search-path2']

        with self.assertRaises(NoVersionFound):
            # No resources are defined anywhere
            session.resource('sqs')
