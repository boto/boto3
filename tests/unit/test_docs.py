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

from botocore.model import DenormalizedStructureBuilder, ServiceModel

from boto3.docs import py_type_name, document_structure
from tests import mock, BaseTestCase


class TestPythonTypeName(BaseTestCase):
    def test_structure(self):
        self.assertEqual('dict', py_type_name('structure'))

    def test_list(self):
        self.assertEqual('list', py_type_name('list'))

    def test_map(self):
        self.assertEqual('dict', py_type_name('map'))

    def test_string(self):
        self.assertEqual('string', py_type_name('string'))

    def test_character(self):
        self.assertEqual('string', py_type_name('character'))

    def test_blob(self):
        self.assertEqual('bytes', py_type_name('blob'))

    def test_timestamp(self):
        self.assertEqual('datetime', py_type_name('timestamp'))

    def test_integer(self):
        self.assertEqual('integer', py_type_name('integer'))

    def test_long(self):
        self.assertEqual('integer', py_type_name('long'))

    def test_float(self):
        self.assertEqual('float', py_type_name('float'))

    def test_double(self):
        self.assertEqual('float', py_type_name('double'))


class TestDocumentStructure(BaseTestCase):
    def test_nested_structure(self):
        # Internally this doesn't use an OrderedDict so we can't
        # test the full output, but we can test whether the
        # parameters are all included as expected with the correct
        # types.
        shape = DenormalizedStructureBuilder().with_members({
            'Param1': {
                'type': 'list',
                'member': {
                    'type': 'structure',
                    'members': {
                        'Param2': {
                            'type': 'string'
                        },
                        'Param3': {
                            'type': 'float'
                        }
                    }
                }
            },
            'Param4': {
                'type': 'blob'
            }
        }).build_model()

        doc = document_structure('Test', shape)

        self.assertIn("'Param1': [", doc)
        self.assertIn("'Param2': STRING", doc)
        self.assertIn("'Param3': FLOAT", doc)
        self.assertIn("'Param4': BYTES", doc)
