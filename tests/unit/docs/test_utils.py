# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import importlib
import sys
import types

import botocore.docs.utils

import boto3.docs.utils
from boto3.docs.utils import get_resource_ignore_params
from boto3.resources.model import Parameter
from tests import mock, unittest


class TestGetResourceIgnoreParams(unittest.TestCase):
    def test_target_is_single_resource(self):
        param = Parameter('InstanceId', 'response')
        ignore_params = get_resource_ignore_params([param])
        assert ignore_params == ['InstanceId']

    def test_target_is_multiple_resources(self):
        param = Parameter('InstanceIds[]', 'response')
        ignore_params = get_resource_ignore_params([param])
        assert ignore_params == ['InstanceIds']

    def test_target_is_element_of_multiple_resources(self):
        param = Parameter('InstanceIds[0]', 'response')
        ignore_params = get_resource_ignore_params([param])
        assert ignore_params == ['InstanceIds']

    def test_target_is_nested_param(self):
        param = Parameter('Filters[0].Name', 'response')
        ignore_params = get_resource_ignore_params([param])
        assert ignore_params == ['Filters']

        param = Parameter('Filters[0].Values[0]', 'response')
        ignore_params = get_resource_ignore_params([param])
        assert ignore_params == ['Filters']


class TestDocumentModifiedShapeImport(unittest.TestCase):
    def tearDown(self):
        # Restore the module state for the rest of the test suite.
        importlib.reload(boto3.docs.utils)

    def test_import_with_document_modified_shape(self):
        importlib.reload(boto3.docs.utils)
        assert (
            boto3.docs.utils.DocumentModifiedShape
            is botocore.docs.utils.DocumentModifiedShape
        )

    def test_import_without_document_modified_shape(self):
        # Simulate a botocore version whose docs.utils module does not
        # provide DocumentModifiedShape.
        old_botocore_docs_utils = types.ModuleType('botocore.docs.utils')
        with mock.patch.dict(
            sys.modules, {'botocore.docs.utils': old_botocore_docs_utils}
        ):
            importlib.reload(boto3.docs.utils)
            assert boto3.docs.utils.DocumentModifiedShape is None
