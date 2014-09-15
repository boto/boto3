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

import botocore.session

from .resources import ResourceFactory


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
    :type region: string
    :param region: Default region when creating new connections
    :type botocore_session: botocore.session.Session
    :param botocore_session: Use this Botocore session instead of creating
                             a new default one.
    """
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None,
                 aws_session_token=None, region=None, botocore_session=None):
        if botocore_session is not None:
            self._session = botocore_session
        else:
            # Create a new default session
            self._session = botocore.session.Session()

        if aws_access_key_id or aws_secret_access_key or aws_session_token:
            self._session.set_credentials(aws_access_key_id,
                aws_secret_access_key, aws_session_token)

        if region is not None:
            self._session.set_config_variable('region', region)

        self.resource_factory = ResourceFactory()

    def __repr__(self):
        return '<boto3.Session({0}:{1})'.format(
            self._session.get_config_variable('region'),
            self._session.get_credentials().access_key)

    def get_available_services(self):
        """
        Get a list of available services that can be loaded as low-level
        clients via ``session.client(name)``.

        :rtype: list
        :return: List of service names
        """
        return self._session.get_available_services()

    def get_available_resources(self):
        """
        Get a list of available services that can be loaded as resource
        clients via ``session.resource(name)``.

        :rtype: list
        :return: List of service names
        """
        # TODO: Implement me!
        return []

    def client(self, service):
        """
        Create a low-level service client by name using the default session.

        :type service: string
        :param service: The name of a service, e.g. 's3' or 'ec2'

        :return: Service client instance
        """
        # TODO: Create a service client in botocore and return it
        # return self._session.create_client(service_name=service,
        #                                       region_name=self.region)
        raise NotImplementedError()

    def resource(self, service):
        """
        Create a resource service client by name using the default session.

        :type service: string
        :param service: The name of a service, e.g. 's3' or 'ec2'

        :return: Resource client instance
        """
        client = self.client(service)
        cls = self.resource_factory.create_class(service)
        return cls(client=client)
