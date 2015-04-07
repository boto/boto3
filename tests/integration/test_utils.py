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


from boto3 import utils
import boto3.session


class TestUtils(unittest.TestCase):
    def test_runtime_error_raised_when_shadowing_client_method(self):
        botocore_session = botocore.session.get_session()
        session = boto3.session.Session(region_name='us-west-2',
                                        botocore_session=botocore_session)

        def shadows_put_object(class_attributes, **kwargs):
            utils.inject_attribute(class_attributes, 'put_object', 'invalid')

        botocore_session.register('creating-client-class', shadows_put_object)

        with self.assertRaises(RuntimeError):
            # This should raise an exception because we're trying to
            # shadow the put_object client method in the
            # shadows_put_object handler above.
            session.client('s3')
