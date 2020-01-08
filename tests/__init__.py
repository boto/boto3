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

import random
import sys
import time

from botocore.compat import six


import unittest


# Python 3 includes mocking, while 2 requires an extra module.
if sys.version_info[0] == 2:
    import mock
else:
    from unittest import mock


# In python 3, order matters when calling assertEqual to
# compare lists and dictionaries with lists. Therefore,
# assertItemsEqual needs to be used but it is renamed to
# assertCountEqual in python 3.
if six.PY2:
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


def unique_id(name):
    """
    Generate a unique ID that includes the given name,
    a timestamp and a random number. This helps when running
    integration tests in parallel that must create remote
    resources.
    """
    return '{0}-{1}-{2}'.format(name, int(time.time()),
                                random.randint(0, 10000))


class BaseTestCase(unittest.TestCase):
    """
    A base test case which mocks out the low-level session to prevent
    any actual calls to Botocore.
    """
    def setUp(self):
        self.bc_session_patch = mock.patch('botocore.session.Session')
        self.bc_session_cls = self.bc_session_patch.start()

        loader = self.bc_session_cls.return_value.get_component.return_value
        loader.data_path = ''
        self.loader = loader

        # We also need to patch the global default session.
        # Otherwise it could be a cached real session came from previous
        # "functional" or "integration" tests.
        patch_global_session = mock.patch('boto3.DEFAULT_SESSION')
        patch_global_session.start()
        self.addCleanup(patch_global_session.stop)

    def tearDown(self):
        self.bc_session_patch.stop()
