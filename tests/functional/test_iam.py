# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import botocore
from botocore.stub import Stubber

import boto3.session

class TestiamAccessKey(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(
            aws_access_key_id='foo', aws_secret_access_key='bar',
            region_name='us-west-2')
        self.iam = self.session.resource('iam')
        self.access_key = self.iam.AccessKey('username', 'access_key_id_value')

    def test_access_key_load(self):
        stubber = Stubber(self.iam.meta.client)
        stubber.activate()
        stubber.add_response(
            method='list_access_keys',
            service_response={
                'AccessKeyMetadata':[
                    {'AccessKeyId':'access_key_id_value' , 'Status': 'Active'},
                    {'AccessKeyId':'access_key_id_value2' , 'Status': 'Inactive'}
                ]
            }
        )
        self.assertEqual(self.access_key.status, 'Active')
        stubber.deactivate()

    def test_has_load(self):
        self.assertTrue(hasattr(self.access_key, 'load'),
                        'load() was not injected onto ObjectSummary resource.')
