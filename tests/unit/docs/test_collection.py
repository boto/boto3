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
from tests.unit.docs import BaseDocsTest

from boto3.docs.collection import CollectionDocumenter


class TestCollectionDocumenter(BaseDocsTest):
    def test_document_collections(self):
        collection_documenter = CollectionDocumenter(self.resource)
        collection_documenter.document_collections(self.doc_structure)
        self.assert_contains_lines_in_order([
            '.. py:attribute:: samples',
            '  A collection of Sample resources.'
             'A Sample Collection will include all resources by default, '
             'and extreme caution should be taken when performing actions '
             'on all resources.',
            '  .. py:method:: all()',
            ('    Creates an iterable of all Sample resources in the '
             'collection.'),
            '    **Request Syntax** ',
            '    ::',
            '      sample_iterator = myservice.samples.all()',
            '    :rtype: list(:py:class:`myservice.Sample`)',
            '    :returns: A list of Sample resources',
            '  .. py:method:: filter(**kwargs)',
            ('    Creates an iterable of all Sample resources in '
             'the collection filtered by kwargs passed to method.'
             'A Sample collection will include all resources by default '
             'if no filters are provided, and extreme caution should be '
             'taken when performing actions on all resources'),
            '    **Request Syntax** ',
            '    ::',
            '      sample_iterator = myservice.samples.filter(',
            "          Foo='string',",
            "          Bar='string'",
            '      )',
            '    :type Foo: string',
            '    :param Foo: Documents Foo',
            '    :type Bar: string',
            '    :param Bar: Documents Bar',
            '    :rtype: list(:py:class:`myservice.Sample`)',
            '    :returns: A list of Sample resources',
            '  .. py:method:: limit(**kwargs)',
            ('    Creates an iterable up to a specified amount of '
             'Sample resources in the collection.'),
            '    **Request Syntax** ',
            '    ::',
            '      sample_iterator = myservice.samples.limit(',
            '          count=123',
            '      )',
            '    :type count: integer',
            ('    :param count: The limit to the number of resources '
             'in the iterable.'),
            '    :rtype: list(:py:class:`myservice.Sample`)',
            '    :returns: A list of Sample resources',
            '  .. py:method:: operate(**kwargs)',
            '    **Request Syntax** ',
            '      response = myservice.samples.operate(',
            "          Foo='string',",
            "          Bar='string'",
            '      )',
            '    :type Foo: string',
            '    :param Foo: Documents Foo',
            '    :type Bar: string',
            '    :param Bar: Documents Bar',
            '    :rtype: dict',
            '    :returns: ',
            '      **Response Syntax** ',
            '      ::',
            '        {',
            "            'Foo': 'string',",
            "            'Bar': 'string'",
            '        }',
            '      **Response Structure** ',
            '      - *(dict) --* ',
            '        - **Foo** *(string) --* Documents Foo',
            '        - **Bar** *(string) --* Documents Bar',
            '  .. py:method:: page_size(**kwargs)',
            ('    Creates an iterable of all Sample resources in the '
             'collection, but limits the number of items returned by '
             'each service call by the specified amount.'),
            '    **Request Syntax** ',
            '    ::',
            '',
            '      sample_iterator = myservice.samples.page_size(',
            '          count=123',
            '      )',
            '    :type count: integer',
            ('    :param count: The number of items returned by '
             'each service call'),
            '    :rtype: list(:py:class:`myservice.Sample`)',
            '    :returns: A list of Sample resources',
            '    '
        ])