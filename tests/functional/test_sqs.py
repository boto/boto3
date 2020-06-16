# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from tests import unittest


class TestSQSMethodInjection(unittest.TestCase):
    def test_queue_resource_has_batch_sender_method(self):
        session = boto3.session.Session(
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy',
            region_name='us-east-1')
        queue = session.resource('sqs').Queue('foo')
        self.assertTrue(hasattr(queue, 'batch_sender'),
                        'batch_sender() was not injected onto SQS Queue resource.')
