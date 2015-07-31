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

from boto3.resources.model import Parameter
from boto3.docs.utils import get_resource_ignore_params


class TestGetResourceIgnoreParams(unittest.TestCase):
    def test_target_is_single_resource(self):
        param = Parameter('InstanceId', 'response')
        ignore_params = get_resource_ignore_params([param])
        self.assertEqual(ignore_params, ['InstanceId'])

    def test_target_is_multiple_resources(self):
        param = Parameter('InstanceIds[]', 'response')
        ignore_params = get_resource_ignore_params([param])
        self.assertEqual(ignore_params, ['InstanceIds'])

    def test_target_is_element_of_multiple_resources(self):
        param = Parameter('InstanceIds[0]', 'response')
        ignore_params = get_resource_ignore_params([param])
        self.assertEqual(ignore_params, ['InstanceIds'])

    def test_target_is_nested_param(self):
        param = Parameter('Filters[0].Name', 'response')
        ignore_params = get_resource_ignore_params([param])
        self.assertEqual(ignore_params, ['Filters'])

        param = Parameter('Filters[0].Values[0]', 'response')
        ignore_params = get_resource_ignore_params([param])
        self.assertEqual(ignore_params, ['Filters'])
