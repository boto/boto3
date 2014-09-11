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

import sys


# The unittest module got a significant overhaul
# in 2.7, so if we're in 2.6 we can use the backported
# version unittest2.
if sys.version_info[:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


# Python 3 includes mocking, while 2 requires an extra module.
if sys.version_info[0] == 2:
    import mock
else:
    from unittest import mock


class BaseTestCase(unittest.TestCase):
    """
    A base test case which mocks out the low-level session to prevent
    any actual calls to Botocore.
    """
    def setUp(self):
        self.bc_session_patch = mock.patch('botocore.session.Session',
                                           autospec=True)
        self.bc_session_cls = self.bc_session_patch.start()

    def tearDown(self):
        self.bc_session_patch.stop()
