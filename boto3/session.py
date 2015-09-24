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

import botocore.session
from botocore.client import Config

import boto3
import boto3.utils

from .resources.factory import ResourceFactory


class Session(object):
    """
    A session stores configuration state and allows you to create service
    clients and resources.

    :type aws_access_key_id: string
    :param aws_access_key_id: AWS access key ID
    :type aws_secret_access_key: string
    :param aws_secret_access_key: AWS secret access key
    :type aws_session_token: string
    :param aws_session_token: AWS temporary session token
    :type region_name: string
    :param region_name: Default region when creating new connections
    :type botocore_session: botocore.session.Session
    :param botocore_session: Use this Botocore session instead of creating
                             a new default one.
    :type profile_name: string
    :param profile_name: The name of a profile to use. If not given, then
                         the default profile is used.
    """
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None,
                 aws_session_token=None, region_name=None,
                 botocore_session=None, profile_name=None):
        if botocore_session is not None:
            self._session = botocore_session
        else:
            # Create a new default session
            self._session = botocore.session.get_session()

        # Setup custom user-agent string if it isn't already customized
        if self._session.user_agent_name == 'Botocore':
            botocore_info = 'Botocore/{0}'.format(
                self._session.user_agent_version)
            if self._session.user_agent_extra:
                self._session.user_agent_extra += ' ' + botocore_info
            else:
                self._session.user_agent_extra = botocore_info
            self._session.user_agent_name = 'Boto3'
            self._session.user_agent_version = boto3.__version__

        if profile_name is not None:
            self._session.set_config_variable('profile', profile_name)

        if aws_access_key_id or aws_secret_access_key or aws_session_token:
            self._session.set_credentials(aws_access_key_id,
                aws_secret_access_key, aws_session_token)

        if region_name is not None:
            self._session.set_config_variable('region', region_name)

        self.resource_factory = ResourceFactory(
            self._session.get_component('event_emitter'))
        self._setup_loader()
        self._register_default_handlers()

    def __repr__(self):
        return 'Session(region={0})'.format(
            repr(self._session.get_config_variable('region')))

    @property
    def profile_name(self):
        """
        The **read-only** profile name.
        """
        return self._session.profile or 'default'

    @property
    def events(self):
        """
        The event emitter for a session
        """
        return self._session.get_component('event_emitter')

    def _setup_loader(self):
        """
        Setup loader paths so that we can load resources.
        """
        self._loader = self._session.get_component('data_loader')
        self._loader.search_paths.append(
             os.path.join(os.path.dirname(__file__), 'data'))

    def get_available_services(self):
        """
        Get a list of available services that can be loaded as low-level
        clients via :py:meth:`Session.client`.

        :rtype: list
        :return: List of service names
        """
        return self._session.get_available_services()

    def get_available_resources(self):
        """
        Get a list of available services that can be loaded as resource
        clients via :py:meth:`Session.resource`.

        :rtype: list
        :return: List of service names
        """
        return self._loader.list_available_services(type_name='resources-1')

    def client(self, service_name, region_name=None, api_version=None,
               use_ssl=True, verify=None, endpoint_url=None,
               aws_access_key_id=None, aws_secret_access_key=None,
               aws_session_token=None, config=None):
        """
        Create a low-level service client by name.

        :type service_name: string
        :param service_name: The name of a service, e.g. 's3' or 'ec2'. You
            can get a list of available services via
            :py:meth:`get_available_services`.

        :type region_name: string
        :param region_name: The name of the region associated with the client.
            A client is associated with a single region.

        :type api_version: string
        :param api_version: The API version to use.  By default, botocore will
            use the latest API version when creating a client.  You only need
            to specify this parameter if you want to use a previous API version
            of the client.

        :type use_ssl: boolean
        :param use_ssl: Whether or not to use SSL.  By default, SSL is used.  Note that
            not all services support non-ssl connections.

        :type verify: boolean/string
        :param verify: Whether or not to verify SSL certificates.  By default SSL certificates
            are verified.  You can provide the following values:

            * False - do not validate SSL certificates.  SSL will still be
              used (unless use_ssl is False), but SSL certificates
              will not be verified.
            * path/to/cert/bundle.pem - A filename of the CA cert bundle to
              uses.  You can specify this argument if you want to use a different
              CA cert bundle than the one used by botocore.

        :type endpoint_url: string
        :param endpoint_url: The complete URL to use for the constructed client.
            Normally, botocore will automatically construct the appropriate URL
            to use when communicating with a service.  You can specify a
            complete URL (including the "http/https" scheme) to override this
            behavior.  If this value is provided, then ``use_ssl`` is ignored.

        :type aws_access_key_id: string
        :param aws_access_key_id: The access key to use when creating
            the client.  This is entirely optional, and if not provided,
            the credentials configured for the session will automatically
            be used.  You only need to provide this argument if you want
            to override the credentials used for this specific client.

        :type aws_secret_access_key: string
        :param aws_secret_access_key: The secret key to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type aws_session_token: string
        :param aws_session_token: The session token to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type config: botocore.client.Config
        :param config: Advanced client configuration options. If region_name
            is specified in the client config, its value will take precedence
            over environment variables and configuration values, but not over
            a region_name value passed explicitly to the method.

        :return: Service client instance

        """
        return self._session.create_client(
            service_name, region_name=region_name, api_version=api_version,
            use_ssl=use_ssl, verify=verify, endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token, config=config)

    def resource(self, service_name, region_name=None, api_version=None,
               use_ssl=True, verify=None, endpoint_url=None,
               aws_access_key_id=None, aws_secret_access_key=None,
               aws_session_token=None):
        """
        Create a resource service client by name.

        :type service_name: string
        :param service_name: The name of a service, e.g. 's3' or 'ec2'. You
            can get a list of available services via
            :py:meth:`get_available_resources`.

        :type region_name: string
        :param region_name: The name of the region associated with the client.
            A client is associated with a single region.

        :type api_version: string
        :param api_version: The API version to use.  By default, botocore will
            use the latest API version when creating a client.  You only need
            to specify this parameter if you want to use a previous API version
            of the client.

        :type use_ssl: boolean
        :param use_ssl: Whether or not to use SSL.  By default, SSL is used.  Note that
            not all services support non-ssl connections.

        :type verify: boolean/string
        :param verify: Whether or not to verify SSL certificates.  By default SSL certificates
            are verified.  You can provide the following values:

            * False - do not validate SSL certificates.  SSL will still be
              used (unless use_ssl is False), but SSL certificates
              will not be verified.
            * path/to/cert/bundle.pem - A filename of the CA cert bundle to
              uses.  You can specify this argument if you want to use a different
              CA cert bundle than the one used by botocore.

        :type endpoint_url: string
        :param endpoint_url: The complete URL to use for the constructed client.
            Normally, botocore will automatically construct the appropriate URL
            to use when communicating with a service.  You can specify a
            complete URL (including the "http/https" scheme) to override this
            behavior.  If this value is provided, then ``use_ssl`` is ignored.

        :type aws_access_key_id: string
        :param aws_access_key_id: The access key to use when creating
            the client.  This is entirely optional, and if not provided,
            the credentials configured for the session will automatically
            be used.  You only need to provide this argument if you want
            to override the credentials used for this specific client.

        :type aws_secret_access_key: string
        :param aws_secret_access_key: The secret key to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type aws_session_token: string
        :param aws_session_token: The session token to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :return: Subclass of :py:class:`~boto3.resources.base.ServiceResource`
        """
        if api_version is None:
            api_version = self._loader.determine_latest_version(
                service_name, 'resources-1')
        resource_model = self._loader.load_service_model(
            service_name, 'resources-1', api_version)
        # Creating a new resource instance requires the low-level client
        # and service model, the resource version and resource JSON data.
        # We pass these to the factory and get back a class, which is
        # instantiated on top of the low-level client.
        config = Config(user_agent_extra='Resource')
        client = self.client(
            service_name, region_name=region_name, api_version=api_version,
            use_ssl=use_ssl, verify=verify, endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token, config=config)
        service_model = client.meta.service_model
        cls = self.resource_factory.load_from_definition(
            service_name, service_name, resource_model['service'],
            resource_model['resources'], service_model)
        return cls(client=client)

    def _register_default_handlers(self):

        # S3 customizations
        self._session.register(
            'creating-client-class.s3',
            boto3.utils.lazy_call(
                'boto3.s3.inject.inject_s3_transfer_methods'))
        self._session.register(
            'creating-resource-class.s3.Bucket',
            boto3.utils.lazy_call(
                'boto3.s3.inject.inject_bucket_methods'))
        self._session.register(
            'creating-resource-class.s3.Object',
            boto3.utils.lazy_call(
                'boto3.s3.inject.inject_object_methods'))

        # DynamoDb customizations
        self._session.register(
            'creating-resource-class.dynamodb',
            boto3.utils.lazy_call(
                'boto3.dynamodb.transform.register_high_level_interface'),
            unique_id='high-level-dynamodb')
        self._session.register(
            'creating-resource-class.dynamodb.Table',
            boto3.utils.lazy_call(
                'boto3.dynamodb.table.register_table_methods'),
            unique_id='high-level-dynamodb-table')

        # EC2 Customizations
        self._session.register(
            'creating-resource-class.ec2.ServiceResource',
            boto3.utils.lazy_call(
                'boto3.ec2.createtags.inject_create_tags'))
