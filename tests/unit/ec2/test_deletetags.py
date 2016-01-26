# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
import unittest
import mock

from boto3.ec2.deletetags import delete_tags


class TestDeleteTags(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock()
        self.resource = mock.Mock()
        self.resource.meta.client = self.client
        self.instance_id = 'instance_id'
        self.resource.id = self.instance_id

    def test_delete_tags(self):
        tags = {
            'Tags': [
                {'Key': 'key1', 'Value': 'value1'},
                {'Key': 'key2', 'Value': 'value2'},
                {'Key': 'key3', 'Value': 'value3'}
            ]
        }

        delete_tags(self.resource, **tags)

        kwargs = tags
        kwargs['Resources'] = [self.instance_id]
        self.client.delete_tags.assert_called_with(**kwargs)
