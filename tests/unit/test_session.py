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

from boto3.session import Session
from tests import unittest


class SessionTest(unittest.TestCase):
    def test_access_key_can_be_accessed(self):
        session = Session(access_key='foo')
        self.assertEqual(session.access_key, 'foo')

    def test_create_connection(self):
        session = Session()
        # TODO: Once implemented, write this test!
        with self.assertRaises(NotImplementedError):
            session.connect('s3')
