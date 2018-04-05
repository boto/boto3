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
from tests import unittest, mock

from botocore.model import ServiceModel, OperationModel

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.dynamodb.transform import ParameterTransformer
from boto3.dynamodb.transform import TransformationInjector
from boto3.dynamodb.transform import DynamoDBHighLevelResource
from boto3.dynamodb.transform import register_high_level_interface
from boto3.dynamodb.transform import copy_dynamodb_params
from boto3.dynamodb.conditions import Attr, Key


class BaseTransformationTest(unittest.TestCase):
    def setUp(self):
        self.target_shape = 'MyShape'
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
                'SampleOperationInputOutput': {
                    'type': 'structure',
                    'members': {}
                },
                'String': {
                    'type': 'string'
                }
            }
        }

    def build_models(self):
        self.service_model = ServiceModel(self.json_model)
        self.operation_model = OperationModel(
            self.json_model['operations']['SampleOperation'],
            self.service_model
        )

    def add_input_shape(self, shape):
        self.add_shape(shape)
        params_shape = self.json_model['shapes']['SampleOperationInputOutput']
        shape_name = list(shape.keys())[0]
        params_shape['members'][shape_name] = {'shape': shape_name}

    def add_shape(self, shape):
        shape_name = list(shape.keys())[0]
        self.json_model['shapes'][shape_name] = shape[shape_name]


class TestInputOutputTransformer(BaseTransformationTest):
    def setUp(self):
        super(TestInputOutputTransformer, self).setUp()
        self.transformation = lambda params: self.transformed_value
        self.add_shape({self.target_shape: {'type': 'string'}})

    def test_transform_structure(self):
        input_params = {
            'Structure': {
                'TransformMe': self.original_value,
                'LeaveAlone': self.original_value,
            }
        }
        input_shape = {
            'Structure': {
                'type': 'structure',
                'members': {
                    'TransformMe': {'shape': self.target_shape},
                    'LeaveAlone': {'shape': 'String'}
                }
            }
        }

        self.add_input_shape(input_shape)
        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation,
            target_shape=self.target_shape)
        self.assertEqual(
            input_params,
            {'Structure': {
                'TransformMe': self.transformed_value,
                'LeaveAlone': self.original_value}}
        )

    def test_transform_map(self):
        input_params = {
            'TransformMe': {'foo': self.original_value},
            'LeaveAlone': {'foo': self.original_value}
        }

        targeted_input_shape = {
            'TransformMe': {
                'type': 'map',
                'key': {'shape': 'String'},
                'value': {'shape': self.target_shape}
            }
        }

        untargeted_input_shape = {
            'LeaveAlone': {
                'type': 'map',
                'key': {'shape': 'String'},
                'value': {'shape': 'String'}
            }
        }

        self.add_input_shape(targeted_input_shape)
        self.add_input_shape(untargeted_input_shape)

        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation,
            target_shape=self.target_shape)
        self.assertEqual(
            input_params,
            {'TransformMe': {'foo': self.transformed_value},
             'LeaveAlone': {'foo': self.original_value}}
        )

    def test_transform_list(self):
        input_params = {
            'TransformMe': [
                self.original_value, self.original_value
            ],
            'LeaveAlone': [
                self.original_value, self.original_value
            ]
        }

        targeted_input_shape = {
            'TransformMe': {
                'type': 'list',
                'member': {'shape': self.target_shape}
            }
        }

        untargeted_input_shape = {
            'LeaveAlone': {
                'type': 'list',
                'member': {'shape': 'String'}
            }
        }

        self.add_input_shape(targeted_input_shape)
        self.add_input_shape(untargeted_input_shape)

        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation, target_shape=self.target_shape)
        self.assertEqual(
            input_params,
            {'TransformMe': [self.transformed_value, self.transformed_value],
             'LeaveAlone': [self.original_value, self.original_value]}
        )

    def test_transform_nested_structure(self):
        input_params = {
            'WrapperStructure': {
                'Structure': {
                    'TransformMe': self.original_value,
                    'LeaveAlone': self.original_value
                }
            }
        }

        structure_shape = {
            'Structure': {
                'type': 'structure',
                'members': {
                    'TransformMe': {'shape': self.target_shape},
                    'LeaveAlone': {'shape': 'String'}
                }
            }
        }

        input_shape = {
            'WrapperStructure': {
                'type': 'structure',
                'members': {'Structure': {'shape': 'Structure'}}}
        }
        self.add_shape(structure_shape)
        self.add_input_shape(input_shape)

        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation,
            target_shape=self.target_shape)
        self.assertEqual(
            input_params,
            {'WrapperStructure': {
                'Structure': {'TransformMe': self.transformed_value,
                              'LeaveAlone': self.original_value}}}
        )

    def test_transform_nested_map(self):
        input_params = {
            'TargetedWrapperMap': {
                'foo': {
                    'bar': self.original_value
                }
            },
            'UntargetedWrapperMap': {
                'foo': {
                    'bar': self.original_value
                }
            }

        }

        targeted_map_shape = {
            'TransformMeMap': {
                'type': 'map',
                'key': {'shape': 'String'},
                'value': {'shape': self.target_shape}
            }
        }

        targeted_wrapper_shape = {
            'TargetedWrapperMap': {
                'type': 'map',
                'key': {'shape': 'Name'},
                'value': {'shape': 'TransformMeMap'}}
        }

        self.add_shape(targeted_map_shape)
        self.add_input_shape(targeted_wrapper_shape)

        untargeted_map_shape = {
            'LeaveAloneMap': {
                'type': 'map',
                'key': {'shape': 'String'},
                'value': {'shape': 'String'}
            }
        }

        untargeted_wrapper_shape = {
            'UntargetedWrapperMap': {
                'type': 'map',
                'key': {'shape': 'Name'},
                'value': {'shape': 'LeaveAloneMap'}}
        }

        self.add_shape(untargeted_map_shape)
        self.add_input_shape(untargeted_wrapper_shape)

        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation, target_shape=self.target_shape)
        self.assertEqual(
            input_params,
            {'TargetedWrapperMap': {'foo': {'bar': self.transformed_value}},
             'UntargetedWrapperMap': {'foo': {'bar': self.original_value}}}
        )

    def test_transform_nested_list(self):
        input_params = {
            'TargetedWrapperList': [
                [self.original_value, self.original_value]
            ],
            'UntargetedWrapperList': [
                [self.original_value, self.original_value]
            ]
        }

        targeted_list_shape = {
            'TransformMe': {
                'type': 'list',
                'member': {'shape': self.target_shape}
            }
        }

        targeted_wrapper_shape = {
            'TargetedWrapperList': {
                'type': 'list',
                'member': {'shape': 'TransformMe'}}
        }

        self.add_shape(targeted_list_shape)
        self.add_input_shape(targeted_wrapper_shape)

        untargeted_list_shape = {
            'LeaveAlone': {
                'type': 'list',
                'member': {'shape': 'String'}
            }
        }

        untargeted_wrapper_shape = {
            'UntargetedWrapperList': {
                'type': 'list',
                'member': {'shape': 'LeaveAlone'}}
        }

        self.add_shape(untargeted_list_shape)
        self.add_input_shape(untargeted_wrapper_shape)

        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation,
            target_shape=self.target_shape)
        self.assertEqual(
            input_params,
            {'TargetedWrapperList': [[
                self.transformed_value, self.transformed_value]],
             'UntargetedWrapperList': [[
                 self.original_value, self.original_value]]}
        )

    def test_transform_incorrect_type_for_structure(self):
        input_params = {
            'Structure': 'foo'
        }

        input_shape = {
            'Structure': {
                'type': 'structure',
                'members': {
                    'TransformMe': {'shape': self.target_shape},
                }
            }
        }

        self.add_input_shape(input_shape)

        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation,
            target_shape=self.target_shape)
        self.assertEqual(input_params, {'Structure': 'foo'})

    def test_transform_incorrect_type_for_map(self):
        input_params = {
            'Map': 'foo'
        }

        input_shape = {
            'Map': {
                'type': 'map',
                'key': {'shape': 'String'},
                'value': {'shape': self.target_shape}
            }
        }

        self.add_input_shape(input_shape)

        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation,
            target_shape=self.target_shape)
        self.assertEqual(input_params, {'Map': 'foo'})

    def test_transform_incorrect_type_for_list(self):
        input_params = {
            'List': 'foo'
        }

        input_shape = {
            'List': {
                'type': 'list',
                'member': {'shape': self.target_shape}
            }
        }

        self.add_input_shape(input_shape)

        self.transformer.transform(
            params=input_params, model=self.operation_model.input_shape,
            transformation=self.transformation, target_shape=self.target_shape)
        self.assertEqual(input_params, {'List': 'foo'})


class BaseTransformAttributeValueTest(BaseTransformationTest):
    def setUp(self):
        self.target_shape = 'AttributeValue'
        self.setup_models()
        self.build_models()
        self.python_value = 'mystring'
        self.dynamodb_value = {'S': self.python_value}
        self.injector = TransformationInjector()
        self.add_shape({self.target_shape: {'type': 'string'}})


class TestTransformAttributeValueInput(BaseTransformAttributeValueTest):
    def test_handler(self):
        input_params = {
            'Structure': {
                'TransformMe': self.python_value,
                'LeaveAlone': 'unchanged'
            }
        }
        input_shape = {
            'Structure': {
                'type': 'structure',
                'members': {
                    'TransformMe': {'shape': self.target_shape},
                    'LeaveAlone': {'shape': 'String'}
                }
            }
        }

        self.add_input_shape(input_shape)

        self.injector.inject_attribute_value_input(
            params=input_params, model=self.operation_model)
        self.assertEqual(
            input_params,
            {'Structure': {
                'TransformMe': self.dynamodb_value,
                'LeaveAlone': 'unchanged'}}
        )


class TestTransformAttributeValueOutput(BaseTransformAttributeValueTest):
    def test_handler(self):
        parsed = {
            'Structure': {
                'TransformMe': self.dynamodb_value,
                'LeaveAlone': 'unchanged'
            }
        }
        input_shape = {
            'Structure': {
                'type': 'structure',
                'members': {
                    'TransformMe': {'shape': self.target_shape},
                    'LeaveAlone': {'shape': 'String'}
                }
            }
        }

        self.add_input_shape(input_shape)
        self.injector.inject_attribute_value_output(
            parsed=parsed, model=self.operation_model)
        self.assertEqual(
            parsed,
            {'Structure': {
                'TransformMe': self.python_value,
                'LeaveAlone': 'unchanged'}}
        )


    def test_no_output(self):
        service_model = ServiceModel({
            'operations': {
                'SampleOperation': {
                    'name': 'SampleOperation',
                    'input': {'shape': 'SampleOperationInputOutput'},
                }
            },
            'shapes': {
                'SampleOperationInput': {
                    'type': 'structure',
                    'members': {}
                },
                'String': {
                    'type': 'string'
                }
            }
        })
        operation_model = service_model.operation_model('SampleOperation')

        parsed = {}
        self.injector.inject_attribute_value_output(
            parsed=parsed, model=operation_model)
        self.assertEqual(parsed, {})



class TestTransformConditionExpression(BaseTransformationTest):
    def setUp(self):
        super(TestTransformConditionExpression, self).setUp()
        self.add_shape({'ConditionExpression': {'type': 'string'}})
        self.add_shape({'KeyExpression': {'type': 'string'}})

        shapes = self.json_model['shapes']
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


class TestCopyDynamoDBParams(unittest.TestCase):
    def test_copy_dynamodb_params(self):
        params = {'foo': 'bar'}
        new_params = copy_dynamodb_params(params)
        self.assertEqual(params, new_params)
        self.assertIsNot(new_params, params)


class TestDynamoDBHighLevelResource(unittest.TestCase):
    def setUp(self):
        self.events = mock.Mock()
        self.client = mock.Mock()
        self.client.meta.events = self.events
        self.meta = ResourceMeta('dynamodb')

    def test_instantiation(self):
        # Instantiate the class.
        dynamodb_class = type(
            'dynamodb', (DynamoDBHighLevelResource, ServiceResource),
            {'meta': self.meta})
        with mock.patch('boto3.dynamodb.transform.TransformationInjector') \
                as mock_injector:
            with mock.patch(
                'boto3.dynamodb.transform.DocumentModifiedShape.'
                'replace_documentation_for_matching_shape') \
                    as mock_modify_documentation_method:
                dynamodb_class(client=self.client)

        # It should have fired the following events upon instantiation.
        event_call_args = self.events.register.call_args_list
        self.assertEqual(
            event_call_args,
            [mock.call(
                'provide-client-params.dynamodb',
                copy_dynamodb_params,
                unique_id='dynamodb-create-params-copy'),
             mock.call(
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
                unique_id='dynamodb-attr-value-output'),
             mock.call(
                'docs.*.dynamodb.*.complete-section',
                mock_modify_documentation_method,
                unique_id='dynamodb-attr-value-docs'),
             mock.call(
                'docs.*.dynamodb.*.complete-section',
                mock_modify_documentation_method,
                unique_id='dynamodb-key-expression-docs'),
             mock.call(
                'docs.*.dynamodb.*.complete-section',
                mock_modify_documentation_method,
                unique_id='dynamodb-cond-expression-docs')]
        )


class TestRegisterHighLevelInterface(unittest.TestCase):
    def test_register(self):
        base_classes = [object]
        register_high_level_interface(base_classes)

        # Check that the base classes are as expected
        self.assertEqual(base_classes, [DynamoDBHighLevelResource, object])
