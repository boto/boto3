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
from collections import Mapping
import functools

from boto3.dynamodb.types import TypeSerializer, TypeDeserializer
from boto3.dynamodb.conditions import ConditionBase
from boto3.dynamodb.conditions import ConditionExpressionBuilder


def register_high_level_interface(base_classes, **kwargs):
    # This assumes the base class is the base resource object
    resource_base_class = base_classes[0]

    class DynamoDBHighLevelResource(resource_base_class):
        def __init__(self, *args, **kwargs):
            super(DynamoDBHighLevelResource, self).__init__(*args, **kwargs)
            # Apply the handler that generates condition expressions including
            # placeholders.

            self.meta.client.meta.events.register(
                'before-parameter-build.dynamodb',
                transform_condition_expressions,
                unique_id='dynamodb-condition-expression')

            # Apply the handler that serializes the request from python
            # types to dynamodb types.
            self.meta.client.meta.events.register(
                'before-parameter-build.dynamodb',
                transform_attribute_value_input,
                unique_id='dynamodb-attr-value-input')

            # Apply the handler that deserializes the response from dynamodb
            # types to python types.
            self.meta.client.meta.events.register(
                'after-call.dynamodb', transform_attribute_value_output,
                unique_id='dynamodb-attr-value-output')

    base_classes[0] = DynamoDBHighLevelResource


def transform_condition_expressions(params, model, **kwargs):
    transformer = ParameterTransformer()
    condition_builder = ConditionExpressionBuilder()

    def inject_condition_expression(value, transformer, condition_builder,
                                    original_params, model, placeholder_names,
                                    placeholder_values,
                                    is_key_condition=False):
        if isinstance(value, ConditionBase):
            # Create a conditional expression string with placeholders
            # for the provided condition.
            expr, attr_names, attr_values = condition_builder.build_expression(
                value, is_key_condition=is_key_condition)

            placeholder_names.update(attr_names)
            placeholder_values.update(attr_values)

            return expr
        # Use the user provided value if it is not a ConditonBase object.
        return value

    generated_names = {}
    generated_values = {}

    # Apply transformation for conditon and key conditon expression parameters.
    cond_exp_transformation = functools.partial(
        inject_condition_expression, transformer=transformer,
        condition_builder=condition_builder, original_params=params,
        model=model, placeholder_names=generated_names,
        placeholder_values=generated_values, is_key_condition=False)
    transformer.transform(
        params, model.input_shape, cond_exp_transformation,
        'ConditionExpression')

    key_exp_transformation = functools.partial(
        inject_condition_expression, transformer=transformer,
        condition_builder=condition_builder, original_params=params,
        model=model, placeholder_names=generated_names,
        placeholder_values=generated_values, is_key_condition=True)
    transformer.transform(
        params, model.input_shape, key_exp_transformation, 'KeyExpression')

    expr_attr_names_input = 'ExpressionAttributeNames'
    expr_attr_values_input = 'ExpressionAttributeValues'

    # Now that all of the condition expression transformation are done,
    # update the placeholder dictionaries in the request.
    if expr_attr_names_input in params:
        params[expr_attr_names_input].update(generated_names)
    else:
        if generated_names:
            params[expr_attr_names_input] = generated_names

    if expr_attr_values_input in params:
        params[expr_attr_values_input].update(generated_values)
    else:
        if generated_values:
            params[expr_attr_values_input] = generated_values


def transform_attribute_value_input(params, model, **kwargs):
    serializer = TypeSerializer()
    transformer = ParameterTransformer()
    transformer.transform(
        params, model.input_shape, serializer.serialize, 'AttributeValue')


def transform_attribute_value_output(parsed, model, **kwargs):
    deserializer = TypeDeserializer()
    transformer = ParameterTransformer()
    transformer.transform(
        parsed, model.output_shape, deserializer.deserialize, 'AttributeValue')


class ParameterTransformer(object):
    """Transforms the input to and output from botocore based on shape"""

    def transform(self, params, model, transformation, target_shape):
        """Transforms the dynamodb input to or output from botocore

        It applies a specified transformation whenever a specific shape name
        is encountered while traversing the parameters in the dictionary.

        :param params: The parameters structure to transform.
        :param model: The operation model.
        :param transformation: The function to apply the parameter
        :param target_shape: The name of the shape to apply the
            transformation to
        """
        self._transform_parameters(
            model, params, transformation, target_shape)

    def _transform_parameters(self, model, params, transformation,
                              target_shape):
        type_name = model.type_name
        if type_name in ['structure', 'map', 'list']:
            getattr(self, '_transform_%s' % type_name)(
                model, params, transformation, target_shape)

    def _transform_structure(self, model, params, transformation,
                             target_shape):
        if not isinstance(params, Mapping):
            return
        for param in params:
            if param in model.members:
                member_model = model.members[param]
                member_shape = member_model.name
                if member_shape == target_shape:
                    params[param] = transformation(params[param])
                else:
                    self._transform_parameters(
                        member_model, params[param], transformation,
                        target_shape)

    def _transform_map(self, model, params, transformation, target_shape):
        if not isinstance(params, Mapping):
            return
        value_model = model.value
        value_shape = value_model.name
        for key, value in params.items():
            if value_shape == target_shape:
                params[key] = transformation(value)
            else:
                self._transform_parameters(
                    value_model, params[key], transformation, target_shape)

    def _transform_list(self, model, params, transformation, target_shape):
        if not isinstance(params, list):
            return
        member_model = model.member
        member_shape = member_model.name
        for i, item in enumerate(params):
            if member_shape == target_shape:
                params[i] = transformation(item)
            else:
                self._transform_parameters(
                    member_model, params[i], transformation, target_shape)
