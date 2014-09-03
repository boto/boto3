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


class Session(object):
    """
    A session stores configuration state and allows you to create service
    clients and resources.
    """
    def __init__(self, access_key=None, secret_key=None, security_token=None,
                 region=None):
        self._bc_session = botocore.session.Session()

        if access_key or secret_key or security_token:
            self._bc_session.set_credentials(access_key, secret_key,
                                             security_token)

    def __repr__(self):
        return '<boto3.session.Session({0})'.format(self.access_key)

    @property
    def access_key(self):
        """
        The current session's access key
        """
        return self._bc_session.get_credentials().access_key

    def connect(self, service, **kwargs):
        """
        Create a low-level service client by name using the default session.

        :type service: string
        :param service: The name of a service, e.g. 's3' or 'ec2'

        :return: Service client instance
        """
        # TODO: Create a service client and return it
        raise NotImplementedError()
