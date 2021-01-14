# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
import mock

from botocore.exceptions import ClientError
from boto3.iam import inject
from tests import unittest

class TestAccessKeyload(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock()
        self.resource = mock.Mock()
        self.resource.meta.client = self.client
        self.list_access_keys_response = {
            'AccessKeyMetadata':[{'AccessKeyId': self.resource.id, 'Status': 'Active'}]
        }
        self.client.list_access_keys.return_value = self.list_access_keys_response

    def test_access_key_load(self):
        inject.access_key_load(self.resource)
        self.assertEqual(
            self.resource.meta.data, {'AccessKeyId': self.resource.id, 'Status': 'Active'})

