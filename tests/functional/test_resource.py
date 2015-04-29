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
import boto3

import botocore.session
from tests import unittest


def identity(self, x):
    return x


class TestResourceCustomization(unittest.TestCase):
    def setUp(self):
        self.botocore_session = botocore.session.get_session()

    def add_new_method(self, name):
        def handler(class_attributes, **kwargs):
            class_attributes[name] = identity
        return handler

    def test_can_inject_method_onto_resource(self):
        session = boto3.Session(botocore_session=self.botocore_session)
        self.botocore_session.register('creating-resource-class.s3',
                                       self.add_new_method(name='my_method'))
        resource = session.resource('s3')
        self.assertTrue(hasattr(resource, 'my_method'))
        self.assertEqual(resource.my_method('anything'), 'anything')
