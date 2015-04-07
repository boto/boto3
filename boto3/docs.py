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
        'blob': 'bytes',
        'character': 'string',
        'double': 'float',
        'long': 'integer',
        'map': 'dict',
        'structure': 'dict',
        'timestamp': 'datetime',
    }.get(type_name, type_name)


def py_default(type_name):
    """
    Get the Python default value for a given model type, useful
    for generated examples.

        >>> py_default('string')
        '\'string\''
        >>> py_default('list')
        '[...]'
        >>> py_default('unknown')
        '...'

    :rtype: string
    """
    return {
        'double': '123.0',
        'long': '123',
        'integer': '123',
        'string': "'string'",
        'blob': "b'bytes'",
        'list': '[...]',
        'map': '{...}',
        'structure': '{...}',
        'timestamp': 'datetime(2015, 1, 1)',
    }.get(type_name, '...')


def html_to_rst(html, indent=0, indent_first=False):
    """
    Use bcdoc to convert html to rst.

    :type html: string
    :param html: Input HTML to be converted
    :type indent: int
    :param indent: Number of spaces to indent each line
    :type indent_first: boolean
    :param indent_first: Whether to indent the first line
    :rtype: string
    """
    doc = ReSTDocument()

    # TODO: Remove me, temp workaround to fix doc building
    # because of smart quotes that aren't currently supported.
    html = html.replace(u'\u2019', "'")
    html = html.replace(u'\u2014', '-')

    doc.include_doc_string(html)
    rst = doc.getvalue().decode('utf-8')

    if indent:
        rst = '\n'.join([(' ' * indent) + line for line in rst.splitlines()])

        if not indent_first:
            rst = rst.strip()

    return rst


def docs_for(service_name, session=None, resource_filename=None):
    """
    Generate reference documentation (low and high level) for a service
    by name. This generates docs for the latest available version.

    :type service_name: string
    :param service_name: The service short-name, like 'ec2'
    :type session: botocore.session.Session
    :param session: Existing pre-setup session or ``None``.
    :type resource_filename: string
    :param resource_filename: Full path to the service's resource JSON
                              description file. If unset, then this is
                              loaded from the default location.
    :rtype: string
    """
    if session is None:
        session = botocore.session.get_session()

    service_model = session.get_service_model(service_name)

    print('Processing {0}-{1}'.format(service_name, service_model.api_version))

    # The following creates an official name of 'Amazon Simple Storage
    # Service (S3)' our of 'Amazon Simple Storage Service' and 'Amazon S3'.
    # It tries to be smart, so for `Amazon DynamoDB' and 'DynamoDB' we would
    # get an official name of 'Amazon DynamoDB'.
    official_name = service_model.metadata.get('serviceFullName')
    short_name = service_model.metadata.get('serviceAbbreviation', '')
    if short_name.startswith('Amazon'):
        short_name = short_name[7:]
    if short_name.startswith('AWS'):
        short_name = short_name[4:]
    if short_name and short_name.lower() not in official_name.lower():
        official_name += ' ({0})'.format(short_name)

    docs = '{0}\n{1}\n\n'.format(official_name, '=' * len(official_name))

    docs += '.. contents:: Table of Contents\n   :depth: 2\n\n'

    # TODO: Get this information from the model somehow in the future.
    #       For now creating and introspecing a client is a quick and
    #       dirty way to access waiters/paginators.
    client = session.create_client(service_name, aws_access_key_id='dummy',
                                   aws_secret_access_key='dummy',
                                   region_name='us-east-1')

    docs += document_client(service_name, official_name, service_model,
                            client)
    docs += document_client_waiter(session, official_name, service_name,
                                   service_model, client)

    if resource_filename is None:
        resource_filename = (os.path.dirname(__file__) + '/data/resources/'
                             '{0}-{1}.resources.json').format(
                                service_name, service_model.api_version)
    # We can't use a set here because dicts aren't hashable!
    models = {}
    if os.path.exists(resource_filename):
        data = json.load(open(resource_filename))
        model = ResourceModel(service_name, data['service'], data['resources'])

        for collection_model in model.collections:
            collection_model.parent_name = model.name
            models[collection_model.name] = {
                'type': 'collection',
                'model': collection_model
            }

        docs += document_resource(service_name, official_name, model,
                                  service_model, session)

        # First, collect all the models...
        for name, model in sorted(data['resources'].items(),
                                  key=lambda i:i[0]):
            resource_model = ResourceModel(name, model, data['resources'])

            shape = None
            if resource_model.shape:
                shape = service_model.shape_for(resource_model.shape)
            resource_model.load_rename_map(shape)

            if name not in models:
                models[name] = {'type': 'resource', 'model': resource_model}

            for collection_model in resource_model.collections:
                collection_model.parent_name = xform_name(resource_model.name)

                cname = collection_model.name + 'CollectionManager'
                if cname not in models:
                    models[cname] = {'type': 'collection',
                                     'model': collection_model}

        # Then render them out in alphabetical order.
        for name, item in sorted(models.items()):
            model = item['model']
            if item['type'] == 'resource':
                docs += document_resource(service_name, official_name,
                                          model, service_model, session)
            elif item['type'] == 'collection':
                docs += document_collection(
                    service_name, official_name, model,
                    model.resource.model, service_model)

    return docs

def document_client(service_name, official_name, service_model, client):
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

    wdoc = ''
    if client.waiter_names:
        # This gets included in alphabetical order below!
        wdoc += '   .. py:method:: get_waiter(name)\n\n'
        wdoc += '      Get a waiter by name. Available waiters:\n\n'
        for waiter in client.waiter_names:
            wdoc += '      * `{0}`_\n'.format(waiter)
        wdoc += '\n'

    waiter_included = False
    for operation_name in service_model.operation_names:
        if not waiter_included and xform_name(operation_name) > 'get_waiter':
            docs += wdoc
            waiter_included = True

        operation = service_model.operation_model(operation_name)
        docs += document_operation(
            operation, service_name,
            paginated=client.can_paginate(xform_name(operation_name)),
            example_instance='client', example_response='response')

    return docs

def document_client_waiter(session, official_name, service_name,
                           service_model, client):
    waiter_spec_doc = ''
    if client.waiter_names:
        waiter_spec_doc = 'Waiter\n------\n\n'
        service_waiter_model = session.get_waiter_model(service_name)
        for waiter in service_waiter_model.waiter_names:
            snake_cased = xform_name(waiter)
            waiter_spec_doc += '{0}\n{1}\n\n'.format(snake_cased,
                '~' * len(snake_cased))
            waiter_model = service_waiter_model.get_waiter(waiter)
            operation_model = service_model.operation_model(
                waiter_model.operation)
            description = (
                '      This polls :py:meth:`{0}.Client.{1}` every {2} '
                'seconds until a successful state is reached. An error is '
                'returned after {3} failed checks.'.format(
                    service_name, xform_name(waiter_model.operation),
                    waiter_model.delay, waiter_model.max_attempts)
            )
            waiter_spec_doc += document_operation(
                operation_model=operation_model, service_name=service_name,
                operation_name='wait', rtype=None, description=description,
                example_instance='client.get_waiter(\'{0}\')'.format(
                    snake_cased))
        waiter_spec_doc += '\n'

    return waiter_spec_doc

def document_resource(service_name, official_name, resource_model,
                      service_model, session):
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

            attributes = resource_model.get_attributes(shape)
            for name, (orig_name, member) in sorted(attributes.items()):
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

    if resource_model.subresources:
        docs += ('   .. rst-class:: admonition-title\n\n   Sub-resources\n\n'
                 '   Sub-resources are methods that create a new instance of a'
                 ' child resource. This resource\'s identifiers get passed'
                 ' along to the child.\n\n')

        preset = len(resource_model.identifiers)

        if resource_model.subresources:
            for subresource in sorted(resource_model.subresources,
                                      key=lambda i: i.name):
                identifiers = [
                    xform_name(i.target) for i in \
                    subresource.resource.identifiers if i.source == 'input']
                docs += '   .. py:method:: {0}({1})\n\n'.format(
                    subresource.name,
                    ', '.join(identifiers))
                docs += ('      Create a :py:class:`{0}.{1}`'
                         ' instance.\n\n').format(service_name,
                                                  subresource.resource.type)

        docs += '\n\n'

    if resource_model.references:
        docs += ('   .. rst-class:: admonition-title\n\n   References\n\n'
                 '   References are related resource instances that have'
                 ' a belongs-to relationship.\n\n')
        for ref in sorted(resource_model.references, key=lambda i: i.name):
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
                     '(:py:class:`{1}.{2}CollectionManager`)'
                     ' A collection of :py:class:`{3}.{4}` instances. This'
                     ' collection uses the :py:meth:`{5}.Client.{6}` operation'
                     ' to get items.\n\n').format(
                        xform_name(collection.name), service_name,
                        collection.name, service_name,
                        collection.resource.type, service_name,
                        xform_name(collection.request.operation))

    if resource_model.waiters:
        docs += ('   .. rst-class:: admonition-title\n\n   Waiters\n\n'
                 '   Waiters provide an interface to wait for a resource'
                 ' to reach a specific state.\n\n')
        service_waiter_model = session.get_waiter_model(service_name)
        for waiter in sorted(resource_model.waiters,
                             key=lambda i: i.name):
            docs += document_waiter(waiter, service_name, resource_model,
                                    service_model, service_waiter_model)

    return docs

def document_collection(service_name, official_name, collection_model,
                        resource_model, service_model):
    """
    Generate reference documentation about a collection and any
    batch actions it might have.
    """
    title = collection_model.name + 'Collection'
    docs = '{0}\n{1}\n\n'.format(title, '-' * len(title))
    docs += '.. py:class:: {0}.{1}CollectionManager()\n\n'.format(
        service_name, collection_model.name)
    docs += ('   A collection of :py:class:`{0}.{1}` resources for {2}. See'
             '   the'
             '   :py:class:`~boto3.resources.collection.CollectionManager`'
             '   base class for additional methods.\n\n'
             '   This collection uses the :py:meth:`{3}.Client.{4}`'
             '   operation to get items, and its parameters can be'
             '   used as filters::\n\n').format(
                service_name, resource_model.name, official_name,
                service_name, xform_name(collection_model.request.operation))
    docs += ('       for {0} in {1}.{2}.all():\n'
             '           print({0})\n\n').format(
                xform_name(collection_model.resource.type),
                collection_model.parent_name,
                xform_name(collection_model.name),
                xform_name(collection_model.resource.type))

    if collection_model.batch_actions:
        docs += ('   .. rst-class:: admonition-title\n\n   Batch Actions\n\n'
                 '   Batch actions provide a way to manipulate groups of'
                 '   resources in a single service operation call.\n\n')
    for action in sorted(collection_model.batch_actions, key=lambda i:i.name):
        docs += document_action(action, service_name, resource_model,
                                service_model)

    return docs

def document_waiter(waiter, service_name, resource_model, service_model,
                    service_waiter_model):
    """
    Document a resource waiter, including the low-level client waiter
    and parameters.
    """
    try:
        waiter_model = service_waiter_model.get_waiter(waiter.waiter_name)
    except:
        print('Cannot get waiter ' + waiter.waiter_name)
        return ''

    try:
        operation_model = service_model.operation_model(waiter_model.operation)
    except:
        print('Cannot get operation ' + action.request.operation +
              ' for waiter ' + waiter.waiter_name)
        return ''
    description = ('      Waits until this {0} is {1}.\n'
                   '      This method calls ``wait()`` on'
                   ' :py:meth:`{2}.Client.get_waiter` using `{3}`_ .').format(
                        resource_model.name,
                        ' '.join(waiter.name.split('_')[2:]),
                        service_name,
                        xform_name(waiter.waiter_name))

    # Here we split because we only care about top-level parameter names
    ignore_params = [p.target.split('.')[0].strip('[]') for p in waiter.params]

    return document_operation(
        operation_model=operation_model, service_name=service_name,
        operation_name=xform_name(waiter.name),
        description=description,
        example_instance = xform_name(resource_model.name),
        ignore_params=ignore_params, rtype=None)

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

    # Here we split because we only care about top-level parameter names
    ignore_params = [p.target.split('.')[0].strip('[]')
                     for p in action.request.params]

    rtype = 'dict'
    if action_type == 'action':
        description = ('      This method calls'
                       ' :py:meth:`{0}.Client.{1}`.').format(
                            service_name,
                            xform_name(action.request.operation))
        example_response = 'response'
        if action.resource:
            rtype = ':py:class:`{0}.{1}`'.format(
                service_name, action.resource.type)
            example_response = xform_name(action.resource.type)

            # Is the response plural? If so we are returning a list!
            if action.path and '[]' in action.path:
                rtype = 'list({0})'.format(rtype)

    return document_operation(
        operation_model, service_name, operation_name=xform_name(action.name),
        description=description, ignore_params=ignore_params, rtype=rtype,
        example_instance=xform_name(resource_model.name),
        example_response=example_response)

def document_operation(operation_model, service_name, operation_name=None,
                       description=None, ignore_params=None, rtype='dict',
                       paginated=False, example_instance=None,
                       example_response=None):
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
        ', '.join(['{0}=None'.format(k) for k in required_params]),
        ', '.join(['{0}=None'.format(k) for k in optional_params])
    ]).strip(', ')

    if operation_name is None:
        operation_name = xform_name(operation_model.name)

    if description is None:
        description = html_to_rst(
            operation_model._operation_model.get('documentation', ''),
            indent=6, indent_first=True)

    docs = '   .. py:method:: {0}({1})\n\n{2}\n\n'.format(
                operation_name, param_desc, description)

    if paginated:
        docs += '      This operation can be paginated.\n\n'

    if example_instance:
        dummy_params = []
        for key, value in params.items():
            if key in ignore_params:
                continue
            if key in required_params:
                default = py_default(value.type_name)
                dummy_params.append('{0}={1}'.format(
                    key, default))
        docs +=  '      Example::\n\n          '
        if example_response is not None:
            docs += '{0} = '.format(example_response)
        docs += '{0}.{1}({2})\n\n'.format(example_instance, operation_name,
            ', '.join(dummy_params))

    for key, value in params.items():
        # Skip identifiers as these are automatically set!
        if key in ignore_params:
            continue
        param_type = py_type_name(value.type_name)

        # Convert the description from HTML to RST (to later be converted
        # into HTML... don't ask). If the parameter is a nested structure
        # then we also describe its members.
        param_desc = html_to_rst(
            value.documentation, indent=9, indent_first=True)
        if param_type in ['list', 'dict']:
            param_desc = ('\n         Structure description::\n\n' +
                          '            ' + key + ' = ' +
                          document_param_response(
                            key, value, indent=12, indent_first=False) +
                          '\n' + param_desc)
        required = key in required_params and 'Required' or 'Optional'
        docs += ('      :param {0} {1}: *{2}* - {3}\n'.format(
            param_type, key, required, param_desc))
    if rtype is not None:
        docs += '      :rtype: {0}\n\n'.format(rtype)

    # Only document the return structure if it isn't a resource. Usually
    # this means either a list or structure.
    output_shape = operation_model.output_shape
    if rtype in ['list', 'dict'] and output_shape is not None:
        docs += ('      :return:\n         Structure description::\n\n' +
                 document_param_response(None, output_shape, indent=12) + '\n')

    return docs


def document_param_response(name, shape, indent=0, indent_first=True,
                            parent_type=None, eol='\n'):
    """
    Document a nested structure (list or dict) parameter or return value as
    a snippet of Python code with dummy placeholders. For example:

        {
            'Param1': [
                STRING,
                ...
            ],
            'Param2': BOOLEAN,
            'Param3': {
                'Param4': FLOAT,
                'Param5': INTEGER
            }
        }

    :type name: string
    :param name: The shape name.
    :type shape: botocore.model.Shape
    :param shape: The shape structure.
    :type indent: integer
    :param indent: The number of spaces to indent each line.
    :type indent_first: boolean
    :param indent_first: Whether to indent the first line.
    :type parent_type: string
    :param parent_type: The type name of the parent, which determines
                        whether a name is printed for nested members.
    :type eol: string
    :param eol: The end-of-line string to use when finishing a member.
    :rtype: string
    """
    param_name = "'{name}': "
    docs = ''
    spaces = ' ' * indent

    # Add spaces if the first line is indented.
    if indent_first:
        docs += spaces

    if shape.type_name == 'structure':
        # Only include the name if the parent is also a structure.
        if parent_type == 'structure':
            docs += param_name.format(name=name)

        docs += render_structure(shape, spaces, indent, eol)
    elif shape.type_name == 'list':
        # Only include the name if the parent is a structure.
        if parent_type == 'structure':
            docs += param_name.format(name=name)

        docs += render_list(shape, spaces, indent, eol)
    elif shape.type_name == 'map':
        if parent_type == 'structure':
            docs += param_name.format(name=name)

        docs += render_map(shape, spaces, indent, eol)
    else:
        # It's not a structure or list, so document the type. Here we
        # try to use the equivalent Python type name for clarity.
        if name is not None:
            docs += param_name.format(name=name)

        docs += py_type_name(shape.type_name).upper() + eol

    return docs


def render_structure(shape, spaces, indent, eol):
    """
    Render out a ``structure`` type. This renders info about each
    member in the shape::

        {
            'MemberName': 'Value'
        }

    """
    docs = '{\n'

    # Go through each member and recursively process them.
    for i, member_name in enumerate(shape.members):
        # Individual members get a trailing comma only if they
        # are not the last item.
        member_eol = '\n'
        if i < len(shape.members) - 1:
            member_eol = ',' + member_eol

        docs += document_param_response(
            member_name, shape.members[member_name],
            indent=indent + 4, parent_type=shape.type_name,
            eol=member_eol)
    docs += spaces + '}' + eol

    return docs


def render_list(shape, spaces, indent, eol):
    """
    Render out a ``list`` type. This renders info about the member
    type of the list and adds an ellipsis to indicate it can contain
    many items::

        [
            'STRING',
            ...
        ]

    """
    docs = '[\n'

    # Lists have only a single member. Here we document it, plus add
    # an ellipsis to signify that more of the same member type can be
    # added in a list.
    docs += document_param_response(
        None, shape.member, indent=indent + 4, eol=',\n')
    docs += spaces + '    ...\n'
    docs += spaces + ']' + eol

    return docs


def render_map(shape, spaces, indent, eol):
    """
    Render out a ``structure`` type. This renders info about each
    member in the shape::

        {
            'Key': 'Value'
        }

    """
    docs = '{\n'

    # Document the types for the keys and values.
    docs += (spaces + '    ' + py_type_name(shape.key.type_name).upper()
             + ': ' + py_type_name(shape.value.type_name).upper() + '\n')
    docs += spaces + '}' + eol

    return docs
