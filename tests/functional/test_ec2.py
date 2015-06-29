# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is
# distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from tests import unittest

import mock

import boto3.session


class TestCreateTagsInjection(unittest.TestCase):
    def test_create_tags_injected_to_resource(self):
        session = boto3.session.Session(region_name='us-west-2')
        with mock.patch('boto3.ec2.createtags.create_tags') as mock_method:
            resource = session.resource('ec2')
            self.assertTrue(hasattr(resource, 'create_tags'),
                            'EC2 resource does not have create_tags method.')
            self.assertIs(resource.create_tags, mock_method,
                          'custom create_tags method was not injected onto '
                          'EC2 service resource')
