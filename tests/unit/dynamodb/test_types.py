# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is
# distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from decimal import Decimal

import pytest

from tests import unittest

from boto3.dynamodb.types import Binary, TypeSerializer, TypeDeserializer


class TestBinary(unittest.TestCase):
    def test_bytes_input(self):
        data = Binary(b'\x01')
        assert b'\x01' == data
        assert b'\x01' == data.value

    def test_non_ascii_bytes_input(self):
        # Binary data that is out of ASCII range
        data = Binary(b'\x88')
        assert b'\x88' == data
        assert b'\x88' == data.value

    def test_bytearray_input(self):
        data = Binary(bytearray([1]))
        assert b'\x01' == data
        assert b'\x01' == data.value

    def test_unicode_throws_error(self):
        with pytest.raises(TypeError):
            Binary(u'\u00e9')

    def test_integer_throws_error(self):
        with pytest.raises(TypeError):
            Binary(1)

    def test_not_equal(self):
        assert Binary(b'\x01') != b'\x02'

    def test_str(self):
        assert Binary(b'\x01').__str__() == b'\x01'

    def test_bytes(self):
        self.assertEqual(bytes(Binary(b'\x01')), b'\x01')

    def test_repr(self):
        assert 'Binary' in repr(Binary(b'1'))


class TestSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = TypeSerializer()

    def test_serialize_unsupported_type(self):
        with pytest.raises(TypeError, match=r'Unsupported type'):
            self.serializer.serialize(object())

    def test_serialize_null(self):
        assert self.serializer.serialize(None) == {'NULL': True}

    def test_serialize_boolean(self):
        assert self.serializer.serialize(False) == {'BOOL': False}

    def test_serialize_integer(self):
        assert self.serializer.serialize(1) == {'N': '1'}

    def test_serialize_decimal(self):
        assert self.serializer.serialize(Decimal('1.25')) == {'N': '1.25'}

    def test_serialize_float_error(self):
        error_msg = r'Float types are not supported. Use Decimal types instead'
        with pytest.raises(TypeError, match=error_msg):
            self.serializer.serialize(1.25)

    def test_serialize_NaN_error(self):
        with pytest.raises(TypeError, match=r'Infinity and NaN not supported'):
            self.serializer.serialize(Decimal('NaN'))

    def test_serialize_string(self):
        assert self.serializer.serialize('foo') == {'S': 'foo'}

    def test_serialize_binary(self):
        assert self.serializer.serialize(Binary(b'\x01')) == {'B': b'\x01'}

    def test_serialize_bytearray(self):
        assert self.serializer.serialize(bytearray([1])) == {'B': b'\x01'}

    def test_serialize_bytes(self):
        assert self.serializer.serialize(b'\x01') == {'B': b'\x01'}

    def test_serialize_number_set(self):
        serialized_value = self.serializer.serialize(set([1, 2, 3]))
        assert len(serialized_value) == 1
        assert 'NS' in serialized_value
        self.assertCountEqual(serialized_value['NS'], ['1', '2', '3'])

    def test_serialize_string_set(self):
        serialized_value = self.serializer.serialize(set(['foo', 'bar']))
        assert len(serialized_value) == 1
        assert 'SS' in serialized_value
        self.assertCountEqual(serialized_value['SS'], ['foo', 'bar'])

    def test_serialize_binary_set(self):
        serialized_value = self.serializer.serialize(
            set([Binary(b'\x01'), Binary(b'\x02')]))
        assert len(serialized_value) == 1
        assert 'BS' in serialized_value
        self.assertCountEqual(serialized_value['BS'], [b'\x01', b'\x02'])

    def test_serialize_list(self):
        serialized_value = self.serializer.serialize(['foo', 1, [1]])
        assert len(serialized_value) == 1
        assert 'L' in serialized_value
        self.assertCountEqual(
            serialized_value['L'],
            [{'S': 'foo'}, {'N': '1'}, {'L': [{'N': '1'}]}]
        )

    def test_serialize_tuple(self):
        serialized_value = self.serializer.serialize(('foo', 1, (1,)))
        self.assertEqual(len(serialized_value), 1)
        self.assertIn('L', serialized_value)
        self.assertCountEqual(
            serialized_value['L'],
            [{'S': 'foo'}, {'N': '1'}, {'L': [{'N': '1'}]}]
        )

    def test_serialize_map(self):
        serialized_value = self.serializer.serialize(
            {'foo': 'bar', 'baz': {'biz': 1}}
        )
        assert serialized_value == {
            'M': {
                'foo': {'S': 'bar'},
                'baz': {'M': {'biz': {'N': '1'}}}
            }
        }


class TestDeserializer(unittest.TestCase):
    def setUp(self):
        self.deserializer = TypeDeserializer()

    def test_deserialize_invalid_type(self):
        with pytest.raises(TypeError, match=r'FOO is not supported'):
            self.deserializer.deserialize({'FOO': 'bar'})

    def test_deserialize_empty_structure(self):
        with pytest.raises(TypeError, match=r'Value must be a nonempty'):
            self.assertEqual(self.deserializer.deserialize({}), {})

    def test_deserialize_null(self):
        assert self.deserializer.deserialize({"NULL": True}) is None

    def test_deserialize_boolean(self):
        assert self.deserializer.deserialize({"BOOL": False}) is False

    def test_deserialize_integer(self):
        assert self.deserializer.deserialize({'N': '1'}) == Decimal('1')

    def test_deserialize_decimal(self):
        assert self.deserializer.deserialize({'N': '1.25'}) == Decimal('1.25')

    def test_deserialize_string(self):
        assert self.deserializer.deserialize({'S': 'foo'}) == 'foo'

    def test_deserialize_binary(self):
        assert self.deserializer.deserialize({'B': b'\x00'}) == Binary(b'\x00')

    def test_deserialize_number_set(self):
        assert self.deserializer.deserialize(
            {'NS': ['1', '1.25']}) == set([Decimal('1'), Decimal('1.25')])

    def test_deserialize_string_set(self):
        assert self.deserializer.deserialize(
            {'SS': ['foo', 'bar']}) == set(['foo', 'bar'])

    def test_deserialize_binary_set(self):
        assert self.deserializer.deserialize(
            {'BS': [b'\x00', b'\x01']}) == set([Binary(b'\x00'), Binary(b'\x01')])

    def test_deserialize_list(self):
        assert self.deserializer.deserialize(
            {'L': [{'N': '1'}, {'S': 'foo'}, {'L': [{'N': '1.25'}]}]}
        ) == [Decimal('1'), 'foo', [Decimal('1.25')]]

    def test_deserialize_map(self):
        assert self.deserializer.deserialize(
            {'M': {'foo': {'S': 'mystring'}, 'bar': {'M': {'baz': {'N': '1'}}}}}
        ) == {'foo': 'mystring', 'bar': {'baz': Decimal('1')}}
