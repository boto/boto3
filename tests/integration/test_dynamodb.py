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

import boto3.session

from tests import unittest, unique_id


class TestDynamoDBResource(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(region_name='us-west-2')
        self.ddb = self.session.resource('dynamodb')

    def test_has_tables_attr(self):
        self.assertTrue(hasattr(self.ddb, 'tables'))

    def tes_can_list_tables(self):
        # Smoke test to verify we can list() the tables
        # collection.
        self.assertIsInstance(list(self.ddb.tables.all()), list)
