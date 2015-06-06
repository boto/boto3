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

import botocore.session
from boto3.docs import docs_for


class TestDocs(unittest.TestCase):
    def setUp(self):
        self.session = botocore.session.get_session()

    def test_resource_docs_generated(self):
        docs_str = docs_for('s3', self.session)
        self.assertIn('Service Resource', docs_str)
        self.assertIn('A resource representing Amazon Simple Storage Service',
                      docs_str)

    def test_client_docs_generated(self):
        docs_str = docs_for('s3', self.session)
        self.assertIn('s3.Client', docs_str)
        self.assertIn(
            'A low-level client representing Amazon Simple Storage Service',
            docs_str)

    def test_waiter_docs_generated(self):
        docs_str = docs_for('s3', self.session)
        self.assertIn('Waiter', docs_str)
        self.assertIn('bucket_exists', docs_str)
