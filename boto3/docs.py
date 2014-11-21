# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

"""
This module is used to generate both high and low-level reference
documentation for services. Currently, it does this by inspecting
the service and resource models, as well as instantiating dummy
clients to introspect some values. It is likely to change
significantly in the future!

Currently this is not used for docstrings, just for the Sphinx
documentation. RST is generated which Sphinx turns into HTML.

The generated output can be found here:

    http://boto3.readthedocs.org/en/latest/

"""

import json
import os

import botocore.session

from botocore import xform_name
from bcdoc.restdoc import ReSTDocument

import boto3

from .resources.model import ResourceModel


def py_type_name(type_name):
    """
    Get the Python type name for a given model type.

        >>> py_type_name('list')
        'list'
        >>> py_type_name('structure')
        'dict'

    :rtype: string
    """
    return {
        'character': 'string',
        'double': 'float',
        'long': 'integer',
        'map': 'dict',
        'structure': 'dict',
        'timestamp': 'datetime',
    }.get(type_name, type_name)


def html_to_rst(html, indent=0, indentFirst=False):
    """
    Use bcdoc to convert html to rst.

    :type html: string
    :param html: Input HTML to be converted
    :type indent: int
    :param indent: Number of spaces to indent each line
    :type indentFirst: boolean
    :param indentFirst: Whether to indent the first line
    :rtype: string
    """
    doc = ReSTDocument()

    # TODO: Remove me, temp workaround to fix doc building
    # because of smart quotes that aren't currently supported.
    html = html.replace(u'\u2019', "'")

    doc.include_doc_string(html)
    rst = doc.getvalue().decode('utf-8')

    if indent:
        rst = '\n'.join([(' ' * indent) + line for line in rst.splitlines()])

        if not indentFirst:
            rst = rst.strip()

    return rst


def docs_for(service_name):
    """
    Generate reference documentation (low and high level) for a service
    by name. This generates docs for the latest available version.

    :type service_name: string
    :param service_name: The service short-name, like 'ec2'
    :rtype: string
    """
    session = botocore.session.get_session()
    service_model = session.get_service_model(service_name)

    print('Processing {0}-{1}'.format(service_name, service_model.api_version))

    official_name = service_model.metadata.get('serviceFullName')

    docs = '{0}\n{1}\n\n'.format(official_name, '=' * len(official_name))

    docs += '.. contents:: Table of Contents\n\n'

    docs += document_client(service_name, official_name, service_model)

    filename = (os.path.dirname(__file__) + '/data/resources/'
                '{0}-{1}.resources.json').format(service_name,
                                                 service_model.api_version)
    if os.path.exists(filename):
        data = json.load(open(filename))
        model = ResourceModel(service_name, data['service'], data['resources'])

        docs += document_resource(service_name, official_name, model,
                                  service_model)

        for name, model in sorted(data['resources'].items(),
                                  key=lambda i:i[0]):
            resource_model = ResourceModel(name, model, data['resources'])
            docs += document_resource(service_name, official_name,
                                      resource_model, service_model)

    return docs

def document_client(service_name, official_name, service_model):
    """
    Generate low-level client documentation for a service. This generates
    documentation for all available operations.
    """
    docs = 'Client\n------\n\n'
    docs += '.. py:class:: {0}.Client\n\n'.format(service_name)
    docs += '   A low-level client representing {0}::\n\n'.format(
        official_name)
    docs += '       import boto3\n\n'
    docs += '       {service} = boto3.client(\'{service}\')\n\n'.format(
        service=service_name)

    # TODO: Get this information from the model somehow in the future.
    #       For now creating and introspecing a client is a quick and
    #       dirty way to access waiters/paginators.
    client = boto3.client(service_name, aws_access_key_id='dummy',
                          aws_secret_access_key='dummy',
                          region_name='us-east-1')

    wdoc = ''
    if client.waiter_names:
        # This gets included in alphabetical order below!
        wdoc += '   .. py:method:: get_waiter(name)\n\n'
        wdoc += '      Get a waiter by name. Available waiters:\n\n'
        for waiter in client.waiter_names:
            wdoc += '      * {0}\n'.format(waiter)
        wdoc += '\n'

    waiter_included = False
    for operation_name in service_model.operation_names:
        if not waiter_included and xform_name(operation_name) > 'get_waiter':
            docs += wdoc
            waiter_included = True

        operation = service_model.operation_model(operation_name)
        docs += document_operation(
            operation, service_name,
            paginated=client.can_paginate(xform_name(operation_name)))

    return docs

def document_resource(service_name, official_name, resource_model,
                      service_model):
    """
    Generate reference documentation from a resource model.
    """
    model_name = resource_model.name
    title = model_name
    is_service_resource = False
    if model_name == service_name:
        model_name = 'Service'
        title = 'Service Resource'
        is_service_resource = True
    docs = '{0}\n{1}\n\n'.format(title, '-' * len(title))
    docs += '.. py:class:: {0}.{1}({2})\n\n'.format(
        service_name, model_name, ', '.join(
            [xform_name(i.name) for i in resource_model.identifiers]))

    if is_service_resource:
        docs += ('   A resource representing {0}::\n\n').format(official_name)
        docs += '       import boto3\n\n'
        docs += '       {service} = boto3.resource(\'{service}\')\n\n'.format(
            service=service_name)
    else:
        identifiers = ', '.join(
            ["'{0}'".format(xform_name(i.name)) for i in
             resource_model.identifiers])
        docs += ('   A resource representing an {0} {1}::\n\n').format(
            official_name, model_name)
        docs += '       import boto3\n\n'
        docs += ('       {service} = boto3.resource(\'{service}\')\n'
                 '       {var} = {service}.{model}({identifiers})\n\n').format(
                    var=xform_name(model_name), service=service_name,
                    model=model_name, identifiers=identifiers)

    if not is_service_resource:
        docs += ('   .. rst-class:: admonition-title\n\n   Attributes &'
                 'Identifiers\n\n   Attributes & identifiers provide access'
                 ' to the properties of a resource. Attributes are lazy-'
                 'loaded the first time one is accessed via the'
                 ' :py:meth:`load` method, if it exists.\n\n'
                 '   Identifiers:\n\n')

        for identifier in sorted(resource_model.identifiers,
                                 key=lambda i:i.name):
            docs += ('   .. py:attribute:: {0}\n\n      (``string``,'
                     ' **identifier**) The {1}\'s {2} identifier. This'
                     ' attribute **must** be set for the actions below to'
                     ' work.\n\n'.format(
                        xform_name(identifier.name), resource_model.name,
                        identifier.name))

        docs += '\n\n'

        if resource_model.shape:
            docs += '   Attributes:\n\n'
            shape = service_model.shape_for(resource_model.shape)

            for name, member in sorted(shape.members.items()):
                docs += ('   .. py:attribute:: {0}\n\n      (``{1}``)'
                         ' {2}\n\n').format(
                    xform_name(name), py_type_name(member.type_name),
                    html_to_rst(member.documentation, indent=6))

    docs += ('   .. rst-class:: admonition-title\n\n   Actions\n\n   Actions'
             ' call operations on resources, automatically handling the'
             ' passing in of arguments set from identifiers and some'
             ' attributes.\n\n')
    for action in sorted(resource_model.actions, key=lambda i:i.name):
        docs += document_action(action, service_name, resource_model,
                                service_model)

    if resource_model.sub_resources or is_service_resource:
        docs += ('   .. rst-class:: admonition-title\n\n   Sub-resources\n\n'
                 '   Sub-resources are methods that create a new instance of a'
                 ' child resource. This resource\'s identifiers get passed'
                 ' along to the child.\n\n')

        preset = len(resource_model.identifiers)

        if resource_model.sub_resources:
            for resource in sorted(resource_model.sub_resources.resources,
                                   key=lambda i: i.name):
                docs += '   .. py:method:: {0}({1})\n\n'.format(
                    resource.name,
                    ', '.join([xform_name(i.name) for i in \
                               resource.identifiers[preset:]]))
                docs += ('      Create a :py:class:`{0}.{1}`'
                         ' instance.\n\n').format(service_name, resource.name)

        if is_service_resource:
            # TODO: expose service-level subresources via the model
            for name, resource_def in sorted(resource_model._resource_defs.items()):
                docs += '   .. py:method:: {0}({1})\n\n'.format(
                    name,
                    ', '.join([xform_name(i['name']) for i in \
                               resource_def['identifiers'][preset:]]))
                docs += ('      Create a :py:class:`{0}.{1}`'
                         ' instance.\n\n').format(service_name, name)

        docs += '\n\n'

    refs = resource_model.references + resource_model.reverse_references
    if sorted(refs, key=lambda i: i.name):
        docs += ('   .. rst-class:: admonition-title\n\n   References\n\n'
                 '   References are related resource instances that have'
                 ' a belongs-to relationship.\n\n')
        for ref in refs:
            docs += ('   .. py:attribute:: {0}\n\n      '
                     '(:py:class:`{1}.{2}`) The related {3} if set,'
                     ' otherwise ``None``.\n\n').format(
                        xform_name(ref.name), service_name,
                        ref.resource.type, ref.resource.type)

    if resource_model.collections:
        docs += ('   .. rst-class:: admonition-title\n\n   Collections\n\n'
                 '   Collections provide an interface to iterate and'
                 ' manipulate groups of resources.\n\n')
        for collection in sorted(resource_model.collections,
                                 key=lambda i: i.name):
            docs += ('   .. py:attribute:: {0}\n\n      '
                     '(:py:class:`~boto3.resources.collection.CollectionManager`)'
                     ' A collection of :py:class:`{1}.{2}` instances. This'
                     ' collection uses the :py:meth:`{3}.Client.{4}` operation'
                     ' to get items.\n\n').format(
                        xform_name(collection.name), service_name,
                        collection.resource.type, service_name,
                        xform_name(collection.request.operation))

    return docs

def document_action(action, service_name, resource_model, service_model,
                    action_type='action'):
    """
    Document a resource action, including the low-level client operation
    and parameters.
    """
    try:
        operation_model = service_model.operation_model(
            action.request.operation)
    except:
        print('Cannot get operation ' + action.request.operation)
        return ''

    ignore_params = [p.target for p in action.request.params]

    rtype = 'dict'
    if action_type == 'action':
        description = ('      This method calls'
                       ' :py:meth:`{0}.Client.{1}`.').format(
                            service_name,
                            xform_name(action.request.operation))
        if action.resource:
            rtype = ':py:class:`{0}.{1}`'.format(
                service_name, action.resource.type)

            # Is the response plural? If so we are returning a list!
            if action.path and '[]' in action.path:
                rtype = 'list({0})'.format(rtype)

    return document_operation(
        operation_model, service_name, operation_name=xform_name(action.name),
        description=description, ignore_params=ignore_params, rtype=rtype)

def document_operation(operation_model, service_name, operation_name=None,
                       description=None, ignore_params=None, rtype='dict',
                       paginated=False):
    """
    Document an operation. The description can be overridden and certain
    params hidden to support documenting resource actions.
    """
    params = {}
    if operation_model.input_shape:
        try:
            params = operation_model.input_shape.members
        except AttributeError:
            print('Cannot find input shape for ' + operation_model.name)

    if ignore_params is None:
        ignore_params = []

    required = []
    if operation_model.input_shape:
        required = operation_model.input_shape.required_members
    required_params = [k for k in params.keys() if k in required and \
                       k not in ignore_params]
    optional_params = [k for k in params.keys() if k not in required and \
                       k not in ignore_params]
    param_desc = ', '.join([
        ', '.join(required_params),
        ', '.join(['{0}=None'.format(k) for k in optional_params])
    ])

    if operation_name is None:
        operation_name = xform_name(operation_model.name)

    if description is None:
        description = html_to_rst(
            operation_model._operation_model.get('documentation', ''),
            indent=6, indentFirst=True)

    docs = '   .. py:method:: {0}({1})\n\n{2}\n\n'.format(
                operation_name, param_desc, description)

    if paginated:
        docs += '      This operation can be paginated.\n\n'

    for key, value in params.items():
        # Skip identifiers as these are automatically set!
        if key in ignore_params:
            continue
        param_type = py_type_name(value.type_name)
        docs += ('      :param {0} {1}: {2}\n'.format(
            param_type, key, html_to_rst(value.documentation, indent=9)))

    docs += '\n\n      :rtype: {0}\n\n'.format(rtype)

    return docs
