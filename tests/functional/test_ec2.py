# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
import unittest

import boto3.session
from botocore.stub import Stubber


class TestInstanceDeleteTags(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(region_name='us-west-2')
        self.service_resource = self.session.resource('ec2')
        self.instance_resource = self.service_resource.Instance('i-abc123')

    def test_delete_tags_injected(self):
        self.assertTrue(hasattr(self.instance_resource, 'delete_tags'),
                        'delete_tags was not injected onto Instance resource.')

    def test_delete_tags(self):
        stubber = Stubber(self.instance_resource.meta.client)
        stubber.add_response('delete_tags', {})
        stubber.activate()
        response = self.instance_resource.delete_tags(Tags=[{'Key': 'foo'}])
        stubber.assert_no_pending_responses()
        self.assertEqual(response, {})
        stubber.deactivate()

    def test_mutating_filters(self):
        stubber = Stubber(self.service_resource.meta.client)
        instance_filters = [
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
        running_instances = self.service_resource.instances.filter(
            Filters=instance_filters
        )

        # This should not impact the already-created filter.
        instance_filters.append(
            {'Name': 'instance-type', 'Values': ['c4.large']}
        )

        stubber.add_response(
            method='describe_instances',
            service_response={
                'Reservations': []
            },
            expected_params={
                'Filters': [{
                    'Name': 'instance-state-name',
                    'Values': ['running']
                }]
            }
        )

        with stubber:
            list(running_instances)

        stubber.assert_no_pending_responses()
