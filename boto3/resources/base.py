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

import boto3


class ServiceResource(object):
    """
    A base class for resources.

    :type client: botocore.client
    :param client: A low-level Botocore client instance
    """
    def __init__(self, *args, **kwargs):
        # Create a default client if none was passed
        if kwargs.get('client') is not None:
            self.client = kwargs.get('client')
        else:
            self.client = boto3.client(self.service_name)

        # Allow setting identifiers as positional arguments in the order
        # in which they were defined in the ResourceJSON.
        for i, value in enumerate(args):
            setattr(self, self.identifiers[i], value)

        # Allow setting identifiers via keyword arguments. Here we need
        # extra logic to ignore other keyword arguments like ``client``.
        for name, value in kwargs.items():
            if name == 'client':
                continue

            if name not in self.identifiers:
                raise ValueError('Unknown keyword argument: {0}'.format(name))

            setattr(self, name, value)

        # Validate that all identifiers have been set.
        for identifier in self.identifiers:
            if getattr(self, identifier) is None:
                raise ValueError(
                    'Required parameter {0} not set'.format(identifier))

    def __str__(self):
        return "{0}: {1} in {2}".format(
            self.__class__.__name__,
            self.service_name,
            self.client.endpoint.region_name,
        )
