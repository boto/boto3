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
import copy

import pytest

from boto3.dynamodb.conditions import (
    And,
    Attr,
    AttributeExists,
    AttributeNotExists,
    AttributeType,
    BeginsWith,
    Between,
    ConditionExpressionBuilder,
    Contains,
    Equals,
    GreaterThan,
    GreaterThanEquals,
    In,
    Key,
    LessThan,
    LessThanEquals,
    Not,
    NotEquals,
    Or,
    Size,
)
from boto3.exceptions import (
    DynamoDBNeedsConditionError,
    DynamoDBNeedsKeyConditionError,
    DynamoDBOperationNotSupportedError,
)
from tests import unittest


class TestK(unittest.TestCase):
    def setUp(self):
        self.attr = Key('mykey')
        self.attr2 = Key('myotherkey')
        self.value = 'foo'
        self.value2 = 'foo2'

    def test_and(self):
        with pytest.raises(DynamoDBOperationNotSupportedError, match=r'AND'):
            self.attr & self.attr2

    def test_or(self):
        with pytest.raises(DynamoDBOperationNotSupportedError, match=r'OR'):
            self.attr | self.attr2

    def test_not(self):
        with pytest.raises(DynamoDBOperationNotSupportedError, match=r'NOT'):
            ~self.attr

    def test_eq(self):
        assert self.attr.eq(self.value) == Equals(self.attr, self.value)

    def test_lt(self):
        assert self.attr.lt(self.value) == LessThan(self.attr, self.value)

    def test_lte(self):
        assert self.attr.lte(self.value) == LessThanEquals(
            self.attr, self.value
        )

    def test_gt(self):
        assert self.attr.gt(self.value) == GreaterThan(self.attr, self.value)

    def test_gte(self):
        assert self.attr.gte(self.value) == GreaterThanEquals(
            self.attr, self.value
        )

    def test_begins_with(self):
        assert self.attr.begins_with(self.value) == BeginsWith(
            self.attr, self.value
        )

    def test_between(self):
        assert self.attr.between(self.value, self.value2) == Between(
            self.attr, self.value, self.value2
        )

    def test_attribute_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        assert self.attr is not attr_copy
        assert self.attr == attr_copy

    def test_eq_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.eq(self.value)
        comp2 = attr_copy.eq(self.value)
        assert comp == comp2

    def test_eq_inequality(self):
        attr_copy = copy.deepcopy(self.attr)
        assert self.attr.eq(self.value) != attr_copy.eq(self.value2)

    def test_lt_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.lt(self.value)
        comp2 = attr_copy.lt(self.value)
        assert comp == comp2

    def test_lte_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.lte(self.value)
        comp2 = attr_copy.lte(self.value)
        assert comp == comp2

    def test_gt_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.gt(self.value)
        comp2 = attr_copy.gt(self.value)
        assert comp == comp2

    def test_gte_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.gte(self.value)
        comp2 = attr_copy.gte(self.value)
        assert comp == comp2

    def test_begins_with_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.begins_with(self.value)
        comp2 = attr_copy.begins_with(self.value)
        assert comp == comp2

    def test_between_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.between(self.value, self.value2)
        comp2 = attr_copy.between(self.value, self.value2)
        assert comp == comp2


class TestA(TestK):
    def setUp(self):
        self.attr = Attr('mykey')
        self.attr2 = Attr('myotherkey')
        self.value = 'foo'
        self.value2 = 'foo2'

    def test_ne(self):
        assert self.attr.ne(self.value) == NotEquals(self.attr, self.value)

    def test_is_in(self):
        assert self.attr.is_in([self.value]) == In(self.attr, [self.value])

    def test_exists(self):
        assert self.attr.exists() == AttributeExists(self.attr)

    def test_not_exists(self):
        assert self.attr.not_exists() == AttributeNotExists(self.attr)

    def test_contains(self):
        assert self.attr.contains(self.value) == Contains(
            self.attr, self.value
        )

    def test_size(self):
        assert self.attr.size() == Size(self.attr)

    def test_attribute_type(self):
        assert self.attr.attribute_type(self.value) == AttributeType(
            self.attr, self.value
        )

    def test_ne_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.ne(self.value)
        comp2 = attr_copy.ne(self.value)
        assert comp == comp2

    def test_is_in_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.is_in([self.value])
        comp2 = attr_copy.is_in([self.value])
        assert comp == comp2

    def test_exists_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.exists()
        comp2 = attr_copy.exists()
        assert comp == comp2

    def test_not_exists_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.not_exists()
        comp2 = attr_copy.not_exists()
        assert comp == comp2

    def test_contains_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.contains(self.value)
        comp2 = attr_copy.contains(self.value)
        assert comp == comp2

    def test_size_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.size()
        comp2 = attr_copy.size()
        assert comp == comp2

    def test_attribute_type_equality(self):
        attr_copy = copy.deepcopy(self.attr)
        comp = self.attr.attribute_type(self.value)
        comp2 = attr_copy.attribute_type(self.value)
        assert comp == comp2


class TestConditions(unittest.TestCase):
    def setUp(self):
        self.value = Attr('mykey')
        self.value2 = 'foo'

    def build_and_assert_expression(
        self, condition, reference_expression_dict
    ):
        expression_dict = condition.get_expression()
        assert expression_dict == reference_expression_dict

    def test_equal_operator(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = Equals(self.value, self.value2)
        assert cond1 == cond2

    def test_equal_operator_type(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = NotEquals(self.value, self.value2)
        assert cond1 != cond2

    def test_equal_operator_value(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = Equals(self.value, self.value)
        assert cond1 != cond2

    def test_not_equal_operator(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = NotEquals(self.value, self.value)
        assert cond1 != cond2

    def test_and_operator(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = Equals(self.value, self.value2)
        assert cond1 & cond2 == And(cond1, cond2)

    def test_and_operator_throws_excepetion(self):
        cond1 = Equals(self.value, self.value2)
        with pytest.raises(DynamoDBOperationNotSupportedError, match=r'AND'):
            cond1 & self.value2

    def test_or_operator(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = Equals(self.value, self.value2)
        assert cond1 | cond2 == Or(cond1, cond2)

    def test_or_operator_throws_excepetion(self):
        cond1 = Equals(self.value, self.value2)
        with pytest.raises(DynamoDBOperationNotSupportedError, match=r'OR'):
            cond1 | self.value2

    def test_not_operator(self):
        cond1 = Equals(self.value, self.value2)
        assert ~cond1 == Not(cond1)

    def test_eq(self):
        self.build_and_assert_expression(
            Equals(self.value, self.value2),
            {
                'format': '{0} {operator} {1}',
                'operator': '=',
                'values': (self.value, self.value2),
            },
        )

    def test_eq_repr(self):
        actual_repr = str(Equals(self.value, self.value2))
        assert actual_repr == 'mykey = foo'

    def test_ne(self):
        self.build_and_assert_expression(
            NotEquals(self.value, self.value2),
            {
                'format': '{0} {operator} {1}',
                'operator': '<>',
                'values': (self.value, self.value2),
            },
        )

    def test_ne_repr(self):
        actual_repr = str(NotEquals(self.value, self.value2))
        assert actual_repr == 'mykey <> foo'

    def test_lt(self):
        self.build_and_assert_expression(
            LessThan(self.value, self.value2),
            {
                'format': '{0} {operator} {1}',
                'operator': '<',
                'values': (self.value, self.value2),
            },
        )

    def test_lt_repr(self):
        actual_repr = str(LessThan(self.value, self.value2))
        assert actual_repr == 'mykey < foo'

    def test_lte(self):
        self.build_and_assert_expression(
            LessThanEquals(self.value, self.value2),
            {
                'format': '{0} {operator} {1}',
                'operator': '<=',
                'values': (self.value, self.value2),
            },
        )

    def test_lte_repr(self):
        actual_repr = str(LessThanEquals(self.value, self.value2))
        assert actual_repr == 'mykey <= foo'

    def test_gt(self):
        self.build_and_assert_expression(
            GreaterThan(self.value, self.value2),
            {
                'format': '{0} {operator} {1}',
                'operator': '>',
                'values': (self.value, self.value2),
            },
        )

    def test_gt_repr(self):
        actual_repr = str(GreaterThan(self.value, self.value2))
        assert actual_repr == 'mykey > foo'

    def test_gte(self):
        self.build_and_assert_expression(
            GreaterThanEquals(self.value, self.value2),
            {
                'format': '{0} {operator} {1}',
                'operator': '>=',
                'values': (self.value, self.value2),
            },
        )

    def test_gte_repr(self):
        actual_repr = str(GreaterThanEquals(self.value, self.value2))
        assert actual_repr == 'mykey >= foo'

    def test_in(self):
        cond = In(self.value, (self.value2))
        self.build_and_assert_expression(
            cond,
            {
                'format': '{0} {operator} {1}',
                'operator': 'IN',
                'values': (self.value, (self.value2)),
            },
        )
        assert cond.has_grouped_values

    def test_in_repr(self):
        actual_repr = str(In(self.value, self.value2))
        assert actual_repr == 'mykey IN foo'

    def test_bet(self):
        self.build_and_assert_expression(
            Between(self.value, self.value2, 'foo2'),
            {
                'format': '{0} {operator} {1} AND {2}',
                'operator': 'BETWEEN',
                'values': (self.value, self.value2, 'foo2'),
            },
        )

    def test_bet_repr(self):
        actual_repr = str(Between(self.value, self.value2, 'foo2'))
        assert actual_repr == 'mykey BETWEEN foo AND foo2'

    def test_beg(self):
        self.build_and_assert_expression(
            BeginsWith(self.value, self.value2),
            {
                'format': '{operator}({0}, {1})',
                'operator': 'begins_with',
                'values': (self.value, self.value2),
            },
        )

    def test_beg_repr(self):
        actual_repr = str(BeginsWith(self.value, self.value2))
        assert actual_repr == 'begins_with(mykey, foo)'

    def test_cont(self):
        self.build_and_assert_expression(
            Contains(self.value, self.value2),
            {
                'format': '{operator}({0}, {1})',
                'operator': 'contains',
                'values': (self.value, self.value2),
            },
        )

    def test_cont_repr(self):
        actual_repr = str(Contains(self.value, self.value2))
        assert actual_repr == 'contains(mykey, foo)'

    def test_ae(self):
        self.build_and_assert_expression(
            AttributeExists(self.value),
            {
                'format': '{operator}({0})',
                'operator': 'attribute_exists',
                'values': (self.value,),
            },
        )

    def test_ae_repr(self):
        actual_repr = str(AttributeExists(self.value))
        assert actual_repr == 'attribute_exists(mykey)'

    def test_ane(self):
        self.build_and_assert_expression(
            AttributeNotExists(self.value),
            {
                'format': '{operator}({0})',
                'operator': 'attribute_not_exists',
                'values': (self.value,),
            },
        )

    def test_ane_repr(self):
        actual_repr = str(AttributeNotExists(self.value))
        assert actual_repr == 'attribute_not_exists(mykey)'

    def test_size(self):
        self.build_and_assert_expression(
            Size(self.value),
            {
                'format': '{operator}({0})',
                'operator': 'size',
                'values': (self.value,),
            },
        )

    def test_size_repr(self):
        actual_repr = str(Size(self.value))
        assert actual_repr == 'size(mykey)'

    def test_size_can_use_attr_methods(self):
        size = Size(self.value)
        self.build_and_assert_expression(
            size.eq(self.value),
            {
                'format': '{0} {operator} {1}',
                'operator': '=',
                'values': (size, self.value),
            },
        )

    def test_size_eq_repr(self):
        actual_repr = str(Size(self.value).eq(self.value2))
        assert actual_repr == 'size(mykey) = foo'

    def test_size_can_use_and(self):
        size = Size(self.value)
        ae = AttributeExists(self.value)
        self.build_and_assert_expression(
            size & ae,
            {
                'format': '({0} {operator} {1})',
                'operator': 'AND',
                'values': (size, ae),
            },
        )

    def test_size_and_ae_repr(self):
        actual_repr = str(Size(self.value) & AttributeExists(self.value))
        assert actual_repr == '(size(mykey) AND attribute_exists(mykey))'

    def test_attribute_type(self):
        self.build_and_assert_expression(
            AttributeType(self.value, self.value2),
            {
                'format': '{operator}({0}, {1})',
                'operator': 'attribute_type',
                'values': (self.value, self.value2),
            },
        )

    def test_attribute_type_repr(self):
        actual_repr = str(AttributeType(self.value, self.value2))
        assert actual_repr == 'attribute_type(mykey, foo)'

    def test_and(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = Equals(self.value, self.value2)
        and_cond = And(cond1, cond2)
        self.build_and_assert_expression(
            and_cond,
            {
                'format': '({0} {operator} {1})',
                'operator': 'AND',
                'values': (cond1, cond2),
            },
        )

    def test_and_repr(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = Equals(self.value, self.value2)
        actual_repr = str(And(cond1, cond2))
        assert actual_repr == '(mykey = foo AND mykey = foo)'

    def test_or(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = Equals(self.value, self.value2)
        or_cond = Or(cond1, cond2)
        self.build_and_assert_expression(
            or_cond,
            {
                'format': '({0} {operator} {1})',
                'operator': 'OR',
                'values': (cond1, cond2),
            },
        )

    def test_or_repr(self):
        cond1 = Equals(self.value, self.value2)
        cond2 = Equals(self.value, self.value2)
        actual_repr = str(Or(cond1, cond2))
        assert actual_repr == '(mykey = foo OR mykey = foo)'

    def test_not(self):
        cond = Equals(self.value, self.value2)
        not_cond = Not(cond)
        self.build_and_assert_expression(
            not_cond,
            {
                'format': '({operator} {0})',
                'operator': 'NOT',
                'values': (cond,),
            },
        )

    def test_not_repr(self):
        cond = Equals(self.value, self.value2)
        actual_repr = str(Not(cond))
        assert actual_repr == '(NOT mykey = foo)'


class TestConditionExpressionBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = ConditionExpressionBuilder()

    def assert_condition_expression_build(
        self,
        condition,
        ref_string,
        ref_names,
        ref_values,
        is_key_condition=False,
    ):
        exp_string, names, values = self.builder.build_expression(
            condition, is_key_condition=is_key_condition
        )
        assert exp_string == ref_string
        assert names == ref_names
        assert values == ref_values

    def test_bad_input(self):
        a = Attr('myattr')
        with pytest.raises(DynamoDBNeedsConditionError):
            self.builder.build_expression(a)

    def test_build_expression_eq(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.eq('foo'), '#n0 = :v0', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

    def test_reset(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.eq('foo'), '#n0 = :v0', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

        self.assert_condition_expression_build(
            a.eq('foo'), '#n1 = :v1', {'#n1': 'myattr'}, {':v1': 'foo'}
        )

        self.builder.reset()
        self.assert_condition_expression_build(
            a.eq('foo'), '#n0 = :v0', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

    def test_build_expression_lt(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.lt('foo'), '#n0 < :v0', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

    def test_build_expression_lte(self):
        a1 = Attr('myattr')
        self.assert_condition_expression_build(
            a1.lte('foo'), '#n0 <= :v0', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

    def test_build_expression_gt(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.gt('foo'), '#n0 > :v0', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

    def test_build_expression_gte(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.gte('foo'), '#n0 >= :v0', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

    def test_build_expression_begins_with(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.begins_with('foo'),
            'begins_with(#n0, :v0)',
            {'#n0': 'myattr'},
            {':v0': 'foo'},
        )

    def test_build_expression_between(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.between('foo', 'foo2'),
            '#n0 BETWEEN :v0 AND :v1',
            {'#n0': 'myattr'},
            {':v0': 'foo', ':v1': 'foo2'},
        )

    def test_build_expression_ne(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.ne('foo'), '#n0 <> :v0', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

    def test_build_expression_in(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.is_in([1, 2, 3]),
            '#n0 IN (:v0, :v1, :v2)',
            {'#n0': 'myattr'},
            {':v0': 1, ':v1': 2, ':v2': 3},
        )

    def test_build_expression_exists(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.exists(), 'attribute_exists(#n0)', {'#n0': 'myattr'}, {}
        )

    def test_build_expression_not_exists(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.not_exists(), 'attribute_not_exists(#n0)', {'#n0': 'myattr'}, {}
        )

    def test_build_contains(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.contains('foo'),
            'contains(#n0, :v0)',
            {'#n0': 'myattr'},
            {':v0': 'foo'},
        )

    def test_build_size(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.size(), 'size(#n0)', {'#n0': 'myattr'}, {}
        )

    def test_build_size_with_other_conditons(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.size().eq(5), 'size(#n0) = :v0', {'#n0': 'myattr'}, {':v0': 5}
        )

    def test_build_attribute_type(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            a.attribute_type('foo'),
            'attribute_type(#n0, :v0)',
            {'#n0': 'myattr'},
            {':v0': 'foo'},
        )

    def test_build_and(self):
        a = Attr('myattr')
        a2 = Attr('myattr2')
        self.assert_condition_expression_build(
            a.eq('foo') & a2.eq('bar'),
            '(#n0 = :v0 AND #n1 = :v1)',
            {'#n0': 'myattr', '#n1': 'myattr2'},
            {':v0': 'foo', ':v1': 'bar'},
        )

    def test_build_or(self):
        a = Attr('myattr')
        a2 = Attr('myattr2')
        self.assert_condition_expression_build(
            a.eq('foo') | a2.eq('bar'),
            '(#n0 = :v0 OR #n1 = :v1)',
            {'#n0': 'myattr', '#n1': 'myattr2'},
            {':v0': 'foo', ':v1': 'bar'},
        )

    def test_build_not(self):
        a = Attr('myattr')
        self.assert_condition_expression_build(
            ~a.eq('foo'), '(NOT #n0 = :v0)', {'#n0': 'myattr'}, {':v0': 'foo'}
        )

    def test_build_attribute_with_attr_value(self):
        a = Attr('myattr')
        value = Attr('myreference')
        self.assert_condition_expression_build(
            a.eq(value),
            '#n0 = #n1',
            {'#n0': 'myattr', '#n1': 'myreference'},
            {},
        )

    def test_build_with_is_key_condition(self):
        k = Key('myattr')
        self.assert_condition_expression_build(
            k.eq('foo'),
            '#n0 = :v0',
            {'#n0': 'myattr'},
            {':v0': 'foo'},
            is_key_condition=True,
        )

    def test_build_with_is_key_condition_throws_error(self):
        a = Attr('myattr')
        with pytest.raises(DynamoDBNeedsKeyConditionError):
            self.builder.build_expression(a.eq('foo'), is_key_condition=True)

    def test_build_attr_map(self):
        a = Attr('MyMap.MyKey')
        self.assert_condition_expression_build(
            a.eq('foo'),
            '#n0.#n1 = :v0',
            {'#n0': 'MyMap', '#n1': 'MyKey'},
            {':v0': 'foo'},
        )

    def test_build_attr_list(self):
        a = Attr('MyList[0]')
        self.assert_condition_expression_build(
            a.eq('foo'), '#n0[0] = :v0', {'#n0': 'MyList'}, {':v0': 'foo'}
        )

    def test_build_nested_attr_map_list(self):
        a = Attr('MyMap.MyList[2].MyElement')
        self.assert_condition_expression_build(
            a.eq('foo'),
            '#n0.#n1[2].#n2 = :v0',
            {'#n0': 'MyMap', '#n1': 'MyList', '#n2': 'MyElement'},
            {':v0': 'foo'},
        )

    def test_build_double_nested_and_or(self):
        a = Attr('myattr')
        a2 = Attr('myattr2')
        self.assert_condition_expression_build(
            (a.eq('foo') & a2.eq('foo2')) | (a.eq('bar') & a2.eq('bar2')),
            '((#n0 = :v0 AND #n1 = :v1) OR (#n2 = :v2 AND #n3 = :v3))',
            {
                '#n0': 'myattr',
                '#n1': 'myattr2',
                '#n2': 'myattr',
                '#n3': 'myattr2',
            },
            {':v0': 'foo', ':v1': 'foo2', ':v2': 'bar', ':v3': 'bar2'},
        )
