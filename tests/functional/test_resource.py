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
from boto3.exceptions import ResourceNotExistsError

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


class TestSessionErrorMessages(unittest.TestCase):
    def test_has_good_error_message_when_no_resource(self):
        bad_resource_name = 'doesnotexist'
        err_regex = (
            '%s.*resource does not exist.' % bad_resource_name
        )
        with self.assertRaisesRegexp(ResourceNotExistsError, err_regex):
            boto3.resource(bad_resource_name)


class TestGetAvailableSubresources(unittest.TestCase):
    def test_s3_available_subresources_exists(self):
        s3 = boto3.resource('s3')
        self.assertTrue(hasattr(s3, 'get_available_subresources'))
