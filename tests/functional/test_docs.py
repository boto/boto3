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

import boto3
from boto3.docs import docs_for


def test_resource_docs_generated():
    service_with_resources = boto3.Session().get_available_resources()
    session = botocore.session.get_session()
    for service_name in service_with_resources:
        yield _assert_has_resource_documentation, service_name, session


def _assert_has_resource_documentation(service_name, session):
    generated_docs = docs_for(service_name, session)
    service_documentation_bits = [
        # Nothing too specific.  Just documentation that should be
        # in the generated docs if the resource docs were generated.
        # Things will likely never change as the resource docs
        # evolve.
        'Service Resource',
        'A resource representing',
    ]
    for part in service_documentation_bits:
        if part not in generated_docs:
            raise AssertionError(
                "Missing resource documentation for: %s" % service_name)


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
