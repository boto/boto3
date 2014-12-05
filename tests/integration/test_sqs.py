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

import boto3.session

from tests import unittest, unique_id


class TestSQSResource(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(region_name='us-west-2')
        self.sqs = self.session.resource('sqs')
        self.queue_name = unique_id('boto3-test')

    def test_s3(self):
        # Create a new resource
        queue = self.sqs.create_queue(QueueName=self.queue_name)
        self.addCleanup(queue.delete)

        # Call an action
        queue.send_message(MessageBody='test')

        # Get pre-populated resources and access attributes
        messages = queue.receive_messages(WaitTimeSeconds=1)

        self.assertEqual(len(messages), 1)
        self.addCleanup(messages[0].delete)

        self.assertEqual(queue.url, messages[0].queue_url)
        self.assertEqual('test', messages[0].body)
