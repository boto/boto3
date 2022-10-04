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
from tests import unittest


class BaseDocsFunctionalTests(unittest.TestCase):
    def assert_contains_lines_in_order(self, lines, contents):
        for line in lines:
            assert line in contents
            beginning = contents.find(line)
            contents = contents[(beginning + len(line)) :]

    def get_class_document_block(self, class_name, contents):
        start_class_document = '.. py:class:: %s' % class_name
        start_index = contents.find(start_class_document)
        assert start_index != -1, 'Class is not found in contents'
        contents = contents[start_index:]
        end_index = contents.find('  .. py:class::', len(start_class_document))
        return contents[:end_index]

    def get_method_document_block(self, method_name, contents):
        start_method_document = '  .. py:method:: %s(' % method_name
        start_index = contents.find(start_method_document)
        assert start_index != -1, 'Method is not found in contents'
        contents = contents[start_index:]
        end_index = contents.find(
            '  .. py:method::', len(start_method_document)
        )
        return contents[:end_index]

    def get_request_syntax_document_block(self, contents):
        start_marker = '**Request Syntax**'
        start_index = contents.find(start_marker)
        assert start_index != -1, 'There is no request syntax section'
        contents = contents[start_index:]
        end_index = contents.find(':type', len(start_marker))
        return contents[:end_index]

    def get_response_syntax_document_block(self, contents):
        start_marker = '**Response Syntax**'
        start_index = contents.find(start_marker)
        assert start_index != -1, 'There is no response syntax section'
        contents = contents[start_index:]
        end_index = contents.find('**Response Structure**', len(start_marker))
        return contents[:end_index]

    def get_request_parameter_document_block(self, param_name, contents):
        start_param_document = ':type %s:' % param_name
        start_index = contents.find(start_param_document)
        assert start_index != -1, 'Param is not found in contents'
        contents = contents[start_index:]
        end_index = contents.find(':type', len(start_param_document))
        return contents[:end_index]

    def get_response_parameter_document_block(self, param_name, contents):
        start_param_document = '**Response Structure**'
        start_index = contents.find(start_param_document)
        assert start_index != -1, 'There is no response structure'

        start_param_document = '- **%s**' % param_name
        start_index = contents.find(start_param_document)
        assert start_index != -1, 'Param is not found in contents'
        contents = contents[start_index:]
        end_index = contents.find('- **', len(start_param_document))
        return contents[:end_index]
