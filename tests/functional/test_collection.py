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
from tests import unittest

from boto3.session import Session
from boto3.resources.collection import ResourceCollection


class TestCollection(unittest.TestCase):
    def setUp(self):
        self.session = Session(
            aws_access_key_id='dummy', aws_secret_access_key='dummy',
            region_name='us-east-1')
        # Pick an arbitrary resource.
        self.ec2_resource = self.session.resource('ec2')

    def test_can_use_collection_methods(self):
        self.assertIsInstance(
            self.ec2_resource.instances.all(), ResourceCollection)

    def test_can_chain_methods(self):
        self.assertIsInstance(
            self.ec2_resource.instances.all().page_size(5), ResourceCollection)
