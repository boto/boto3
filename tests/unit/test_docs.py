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

import os

from botocore.compat import json, OrderedDict
from botocore.model import DenormalizedStructureBuilder, ServiceModel
from botocore.session import get_session

from boto3.docs import py_type_name, document_param_response, docs_for
from tests import mock, unittest, BaseTestCase


ROOT = os.path.dirname(__file__)


def load_json(data):
    """
    Load a string of JSON data using OrderedDict for object
    pairs.
    """
    return json.loads(data, object_pairs_hook=OrderedDict)


def fix_whitespace(data):
    """
    Return a string without extra leading whitespace. For example:

                    {
                        "foo": 1
                    }

    Becomes:

        {
            "foo": 1
        }

    """
    if data and data[0] == '\n':
        data = data[1:]
    spaces = len(data) - len(data.lstrip())
    return '\n'.join([line[spaces:] for line in data.split('\n')])


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


class TestDocumentService(unittest.TestCase):
    """
    End-to-end tests of the documentation functionality that uses a dummy
    service and resource JSON description. The tests check for specific
    values in the output.
    """
    def setUp(self):
        self.session = get_session()

        loader = self.session.get_component('data_loader')
        loader.data_path = os.path.join(ROOT, 'data')

        self.docs = docs_for(
            'todo', session=self.session,
            resource_filename=os.path.join(ROOT, 'data', 'resources',
                                           'todo-2015-04-01.resources.json'))

        self.resource_docs = ''
        if 'Service Resource' in self.docs:
            self.resource_docs = self.docs.split('Service Resource')[-1]

    def assert_after(self, marker, expected, actual):
        """
        Assert that the expected value occurs after a text marker in
        the actual value.
        """
        pos = actual.find(marker)
        self.assertIn(expected, actual[pos:])

    def test_removed_html(self):
        self.assertNotIn('<p>', self.docs)
        self.assertNotIn('<ul>', self.docs)
        self.assertNotIn('<i>', self.docs)

    def test_page_title(self):
        # The service full name and abbreviated name are both
        # important!
        self.assertIn('AWS ToDo Sample API for Tasks (ToDo Tasks)',
                      self.docs)

    def test_client_description(self):
        self.assertIn('A low-level client representing AWS ToDo Sample API',
                      self.docs)

    def test_client_example(self):
        self.assertIn('todo = boto3.client(\'todo\')', self.docs)

    def test_client_method(self):
        self.assertIn('.. py:method:: create_to_do(Title=None)', self.docs)

    def test_client_method_description(self):
        self.assertIn('Create a new to-do item.', self.docs)

    def test_client_method_example(self):
        self.assertIn('response = client.create_to_do(Title=\'string\')',
                      self.docs)

    def test_client_method_parameters(self):
        self.assertIn(':param string Title: *Required*', self.docs)
        self.assertIn('The title of the to-do item.', self.docs)

    def test_client_method_return(self):
        self.assertIn(':rtype: dict', self.docs)
        self.assertIn(':return:', self.docs)
        self.assertIn('\'Id\': STRING', self.docs)
        self.assertIn('\'Title\': STRING', self.docs)

    def test_waiter_description(self):
        self.assertIn('to_do_ready', self.docs)
        self.assertIn('.. py:method:: wait(Id=None)', self.docs)
        self.assertIn('This polls :py:meth:`todo.Client.get_to_do` every 20 '
                      'seconds until a successful state is reached. An error '
                      'is returned after 25 failed checks.', self.docs)

    def test_waiter_example(self):
        self.assertIn('client.get_waiter(\'to_do_ready\').wait('
                      'Id=\'string\')', self.docs)

    def test_resource_description(self):
        self.assertIn('py:class:: todo.Service()', self.resource_docs)
        self.assertIn('A resource representing AWS ToDo Sample API',
                      self.resource_docs)

    def test_resource_example(self):
        self.assertIn('todo = boto3.resource(\'todo\')', self.resource_docs)

    def test_resource_action_description(self):
        self.assertIn('.. py:method:: create_to_do(Title=None)',
                      self.resource_docs)
        self.assertIn('This method calls :py:meth:`todo.Client.create_to_do`.',
                      self.resource_docs)

    def test_resource_action_return(self):
        self.assertIn(':rtype: :py:class:`todo.ToDo`', self.resource_docs)

    def test_resource_collection_description(self):
        self.assertIn('.. py:attribute:: to_dos', self.resource_docs)
        self.assertIn('A collection of :py:class:`todo.ToDo` instances. This '
                      'collection uses the :py:meth:`todo.Client.describe_to_'
                      'dos` operation to get items.', self.resource_docs)

    def test_resource_has_description(self):
        self.assertIn('py:class:: todo.ToDo(id)', self.resource_docs)
        self.assertIn('A resource representing an AWS ToDo Sample API for '
                      'Tasks (ToDo Tasks) ToDo', self.resource_docs)

    def test_resource_has_example(self):
        self.assertIn('to_do = todo.ToDo(\'id\')', self.resource_docs)

    def test_resource_identifier(self):
        self.assertIn('.. py:attribute:: id', self.resource_docs)
        self.assertIn('(``string``, **identifier**) The ToDo\'s id identifier.'
                      ' This attribute **must** be set for the actions below '
                      'to work.', self.resource_docs)

    def test_resource_attribute(self):
        self.assertIn('.. py:attribute:: title', self.resource_docs)
        self.assertIn('(``string``) The title of the to-do item.',
                      self.resource_docs)

    def test_resource_waiter_description(self):
        self.assertIn('.. py:method:: wait_until_ready()', self.resource_docs)
        self.assertIn('Waits until this ToDo is ready.', self.resource_docs)
        self.assertIn('This method calls ``wait()`` on :py:meth:`todo.'
                      'Client.get_waiter` using `to_do_ready`_ .',
                      self.resource_docs)

    def test_resource_waiter_example(self):
        self.assertIn('to_do.wait_until_ready()', self.resource_docs)

    def test_resource_reference(self):
        self.assertIn('.. py:attribute:: my_self', self.resource_docs)
        self.assertIn('(:py:class:`todo.ToDo`) The related ToDo if set, '
                      'otherwise ``None``.', self.resource_docs)

class TestDocumentStructure(BaseTestCase):
    def test_nested_structure(self):
        shape = DenormalizedStructureBuilder().with_members(
                load_json('''{
                    "Param1": {
                        "type": "list",
                        "member": {
                            "type": "structure",
                            "members": {
                                "Param2": {
                                    "type": "string"
                                },
                                "Param3": {
                                    "type": "float"
                                }
                            }
                        }
                    },
                    "Param4": {
                        "type": "blob"
                    },
                    "Param5": {
                        "type": "list",
                        "member": {
                            "type": "string"
                        }
                    },
                    "Param6": {
                        "type": "map",
                        "key": {
                            "type": "string"
                        },
                        "value": {
                            "type": "integer"
                        }
                    }
                }''')).build_model()

        expected = fix_whitespace('''
        {
            'Param1': [
                {
                    'Param2': STRING,
                    'Param3': FLOAT
                },
                ...
            ],
            'Param4': BYTES,
            'Param5': [
                STRING,
                ...
            ],
            'Param6': {
                STRING: INTEGER
            }
        }
        ''')

        doc = document_param_response('Test', shape)

        self.assertEqual(doc, expected)
