# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from tests import unittest, unique_id
import botocore.session

import boto3.session


class TestUserAgentCustomizations(unittest.TestCase):
    def setUp(self):
        self.botocore_session = botocore.session.get_session()
        self.session = boto3.session.Session(
            region_name='us-west-2', botocore_session=self.botocore_session)
        self.actual_user_agent = None
        self.botocore_session.register('request-created',
                                       self.record_user_agent)

    def record_user_agent(self, request, **kwargs):
        self.actual_user_agent = request.headers['User-Agent']

    def test_client_user_agent(self):
        client = self.session.client('s3')
        client.list_buckets()
        self.assertIn('Boto3', self.actual_user_agent)
        self.assertIn('Botocore', self.actual_user_agent)
        self.assertIn('Python', self.actual_user_agent)
        # We should *not* have any mention of resource
        # when using clients directly.
        self.assertNotIn('Resource', self.actual_user_agent)

    def test_resource_user_agent_has_customization(self):
        resource = self.session.resource('s3')
        list(resource.buckets.all())
        # We should have customized the user agent for
        # resource calls with "Resource".
        self.assertTrue(self.actual_user_agent.endswith(' Resource'))
