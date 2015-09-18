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
import types
from tests import unittest
import mock

from boto3 import utils


class FakeModule(object):
    @staticmethod
    def entry_point(**kwargs):
        return kwargs


class TestUtils(unittest.TestCase):
    def test_lazy_call(self):
        with mock.patch('boto3.utils.import_module') as importer:
            importer.return_value = FakeModule
            lazy_function = utils.lazy_call(
                'fakemodule.FakeModule.entry_point')
            self.assertEqual(lazy_function(a=1, b=2), {'a': 1, 'b': 2})

    def test_import_module(self):
        module = utils.import_module('boto3.s3.transfer')
        self.assertEqual(module.__name__, 'boto3.s3.transfer')
        self.assertIsInstance(module, types.ModuleType)

    def test_inject_attributes_with_no_shadowing(self):
        class_attributes = {}
        utils.inject_attribute(class_attributes, 'foo', 'bar')
        self.assertEqual(class_attributes['foo'], 'bar')

    def test_shadowing_existing_var_raises_exception(self):
        class_attributes = {'foo': 'preexisting'}
        with self.assertRaises(RuntimeError):
            utils.inject_attribute(class_attributes, 'foo', 'bar')


class TestLazyLoadedWaiterModel(unittest.TestCase):
    def test_get_waiter_model_is_lazy(self):
        session = mock.Mock()
        waiter_model = utils.LazyLoadedWaiterModel(
            session, 'myservice', '2014-01-01')
        self.assertFalse(session.get_waiter_model.called)
        waiter_model.get_waiter('Foo')
        self.assertTrue(session.get_waiter_model.called)
        session.get_waiter_model.return_value.get_waiter.assert_called_with(
            'Foo')
