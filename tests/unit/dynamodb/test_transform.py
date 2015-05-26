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
import copy
from tests import unittest, mock

from botocore.model import ServiceModel, OperationModel

from boto3.resources.base import ResourceMeta
from boto3.dynamodb.transform import ParameterTransformer
from boto3.dynamodb.transform import TransformationInjector
from boto3.dynamodb.transform import DynamoDBHighLevelResource
from boto3.dynamodb.transform import register_high_level_interface
from boto3.dynamodb.conditions import Attr, Key


class BaseTransformationTest(unittest.TestCase):
    def setUp(self):
        self.target_shape_name = 'MyShape'
        self.original_value = 'orginal'
        self.transformed_value = 'transformed'
        self.transformer = ParameterTransformer()
        self.json_model = {}
        self.nested_json_model = {}
        self.setup_models()
        self.build_models()

    def setup_models(self):
        self.json_model = {
            'operations': {
                'SampleOperation': {
                    'name': 'SampleOperation',
                    'input': {'shape': 'SampleOperationInputOutput'},
                    'output': {'shape': 'SampleOperationInputOutput'}
                }
            },
            'shapes': {
                self.target_shape_name: {
                    'type': 'string'
                },
                'List': {
                    'type': 'list',
                    'member': {'shape': self.target_shape_name}
                },
                'Map': {
                    'type': 'map',
                    'key': {'shape': 'Name'},
                    'value': {'shape': self.target_shape_name}
                },
                'Structure': {
                    'type': 'structure',
                    'members': {
                        'Member': {'shape': self.target_shape_name}
                    }
                },
                'SampleOperationInputOutput': {
                    'type': 'structure',
                    'members': {
                        'Structure': {'shape': 'Structure'},
                        'Map': {'shape': 'Map'},
                        'List': {'shape': 'List'},
                    }
                },
                'Name': {
                    'type': 'string'
                }
            }
        }

        # Create a more complicated model to test the ability to recurse
        # through a structure.
        self.nested_json_model = copy.deepcopy(self.json_model)
        shapes = self.nested_json_model['shapes']
        shapes['SampleOperationInputOutput']['members'] = {
            'Structure': {'shape': 'WrapperStructure'},
            'Map': {'shape': 'WrapperMap'},
            'List': {'shape': 'WrapperList'}
        }
        shapes['WrapperStructure'] = {
            'type': 'structure',
            'members': {'Structure': {'shape': 'Structure'}}
        }
        shapes['WrapperMap'] = {
            'type': 'map',
            'key': {'shape': 'Name'},
            'value': {'shape': 'Map'}
        }
        shapes['WrapperList'] = {
            'type': 'list',
            'member': {'shape': 'List'}
        }

    def build_models(self):
        self.service_model = ServiceModel(self.json_model)
        self.operation_model = OperationModel(
            self.json_model['operations']['SampleOperation'],
            self.service_model
        )

        self.nested_service_model = ServiceModel(self.nested_json_model)
        self.nested_operation_model = OperationModel(
            self.nested_json_model['operations']['SampleOperation'],
            self.nested_service_model
        )


class TestInputOutputTransformer(BaseTransformationTest):
    def setUp(self):
        super(TestInputOutputTransformer, self).setUp()
        self.transformation = lambda params: self.transformed_value

    def test_transform_structure(self):
        input_params = {
            'Structure': {
                'Member': self.original_value
            }
        }
        self.transformer.transform(
            input_params, self.operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(
            input_params,
            {'Structure': {'Member': self.transformed_value}}
        )

    def test_transform_map(self):
        input_params = {
            'Map': {
                'foo': self.original_value
            }
        }
        self.transformer.transform(
            input_params, self.operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(
            input_params,
            {'Map': {'foo': self.transformed_value}}
        )

    def test_transform_list(self):
        input_params = {
            'List': [
                self.original_value, self.original_value
            ]
        }
        self.transformer.transform(
            input_params, self.operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(
            input_params,
            {'List': [self.transformed_value, self.transformed_value]}
        )

    def test_transform_nested_structure(self):
        input_params = {
            'Structure': {
                'Structure': {
                    'Member': self.original_value
                }
            }
        }
        self.transformer.transform(
            input_params, self.nested_operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(
            input_params,
            {'Structure': {
                'Structure': {'Member': self.transformed_value}}}
        )

    def test_transform_nested_map(self):
        input_params = {
            'Map': {
                'foo': {
                    'bar': self.original_value
                }
            }
        }
        self.transformer.transform(
            input_params, self.nested_operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(
            input_params,
            {'Map': {'foo': {'bar': self.transformed_value}}}
        )

    def test_transform_nested_list(self):
        input_params = {
            'List': [
                [self.original_value, self.original_value]
            ]
        }
        self.transformer.transform(
            input_params, self.nested_operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(
            input_params,
            {'List': [[self.transformed_value, self.transformed_value]]}
        )

    def test_transform_incorrect_type_for_structure(self):
        input_params = {
            'Structure': 'foo'
        }
        self.transformer.transform(
            input_params, self.operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(input_params, {'Structure': 'foo'})

    def test_transform_incorrect_type_for_map(self):
        input_params = {
            'Map': 'foo'
        }
        self.transformer.transform(
            input_params, self.operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(input_params, {'Map': 'foo'})

    def test_transform_incorrect_type_for_list(self):
        input_params = {
            'List': 'foo'
        }
        self.transformer.transform(
            input_params, self.operation_model.input_shape,
            self.transformation, self.target_shape_name)
        self.assertEqual(input_params, {'List': 'foo'})


class BaseTransformAttributeValueTest(BaseTransformationTest):
    def setUp(self):
        self.target_shape_name = 'AttributeValue'
        self.setup_models()
        self.build_models()
        self.python_value = 'mystring'
        self.dynamodb_value = {'S': self.python_value}
        self.injector = TransformationInjector()


class TestTransformAttributeValueInput(BaseTransformAttributeValueTest):
    def test_handler(self):
        input_params = {
            'Structure': {
                'Member': self.python_value
            }
        }
        self.injector.inject_attribute_value_input(
            input_params, self.operation_model)
        self.assertEqual(
            input_params,
            {'Structure': {'Member': self.dynamodb_value}}
        )


class TestTransformAttributeValueOutput(BaseTransformAttributeValueTest):
    def test_handler(self):
        parsed = {
            'Structure': {
                'Member': self.dynamodb_value
            }
        }
        self.injector.inject_attribute_value_output(
            parsed, self.operation_model)
        self.assertEqual(
            parsed,
            {'Structure': {'Member': self.python_value}}
        )


class TestTransformConditionExpression(BaseTransformationTest):
    def setUp(self):
        super(TestTransformConditionExpression, self).setUp()
        shapes = self.json_model['shapes']
        shapes['ConditionExpression'] = {'type': 'string'}
        shapes['KeyExpression'] = {'type': 'string'}
        input_members = shapes['SampleOperationInputOutput']['members']
        input_members['KeyCondition'] = {'shape': 'KeyExpression'}
        input_members['AttrCondition'] = {'shape': 'ConditionExpression'}
        self.injector = TransformationInjector()
        self.build_models()

    def test_non_condition_input(self):
        params = {
            'KeyCondition': 'foo',
            'AttrCondition': 'bar'
        }
        self.injector.inject_condition_expressions(
            params, self.operation_model)
        self.assertEqual(
            params, {'KeyCondition': 'foo', 'AttrCondition': 'bar'})

    def test_single_attr_condition_expression(self):
        params = {
            'AttrCondition': Attr('foo').eq('bar')
        }
        self.injector.inject_condition_expressions(
            params, self.operation_model)
        self.assertEqual(
            params,
            {'AttrCondition': '#n0 = :v0',
             'ExpressionAttributeNames': {'#n0': 'foo'},
             'ExpressionAttributeValues': {':v0': 'bar'}}
        )

    def test_single_key_conditon_expression(self):
        params = {
            'KeyCondition': Key('foo').eq('bar')
        }
        self.injector.inject_condition_expressions(
            params, self.operation_model)
        self.assertEqual(
            params,
            {'KeyCondition': '#n0 = :v0',
             'ExpressionAttributeNames': {'#n0': 'foo'},
             'ExpressionAttributeValues': {':v0': 'bar'}}
        )

    def test_key_and_attr_conditon_expression(self):
        params = {
            'KeyCondition': Key('foo').eq('bar'),
            'AttrCondition': Attr('biz').eq('baz')
        }
        self.injector.inject_condition_expressions(
            params, self.operation_model)
        self.assertEqual(
            params,
            {'KeyCondition': '#n1 = :v1',
             'AttrCondition': '#n0 = :v0',
             'ExpressionAttributeNames': {'#n0': 'biz', '#n1': 'foo'},
             'ExpressionAttributeValues': {':v0': 'baz', ':v1': 'bar'}}
        )

    def test_key_and_attr_conditon_expression_with_placeholders(self):
        params = {
            'KeyCondition': Key('foo').eq('bar'),
            'AttrCondition': Attr('biz').eq('baz'),
            'ExpressionAttributeNames': {'#a': 'b'},
            'ExpressionAttributeValues': {':c': 'd'}
        }
        self.injector.inject_condition_expressions(
            params, self.operation_model)
        self.assertEqual(
            params,
            {'KeyCondition': '#n1 = :v1',
             'AttrCondition': '#n0 = :v0',
             'ExpressionAttributeNames': {
                 '#n0': 'biz', '#n1': 'foo', '#a': 'b'},
             'ExpressionAttributeValues': {
                 ':v0': 'baz', ':v1': 'bar', ':c': 'd'}}
        )


class TestDynamoDBHighLevelResource(unittest.TestCase):
    def setUp(self):
        self.events = mock.Mock()
        self.client = mock.Mock()
        self.client.meta.events = self.events
        self.meta = ResourceMeta('dynamodb')

    def test_instantiation(self):
        # Instantiate the class.
        dynamodb_class = type(
            'dynamodb', (DynamoDBHighLevelResource,), {'meta': self.meta})
        with mock.patch('boto3.dynamodb.transform.TransformationInjector') \
                as mock_injector:
            dynamodb_class(client=self.client)

        # It should have fired the following events upon instantiation.
        event_call_args = self.events.register.call_args_list
        self.assertEqual(
            event_call_args,
            [mock.call(
                'before-parameter-build.dynamodb',
                mock_injector.return_value.inject_condition_expressions,
                unique_id='dynamodb-condition-expression'),
             mock.call(
                'before-parameter-build.dynamodb',
                mock_injector.return_value.inject_attribute_value_input,
                unique_id='dynamodb-attr-value-input'),
             mock.call(
                'after-call.dynamodb',
                mock_injector.return_value.inject_attribute_value_output,
                unique_id='dynamodb-attr-value-output')]
        )


class TestRegisterHighLevelInterface(unittest.TestCase):
    def test_register(self):
        base_classes = [object]
        register_high_level_interface(base_classes)

        # Check that the base classes are as expected
        self.assertEqual(base_classes, [DynamoDBHighLevelResource])
