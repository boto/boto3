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
The models defined in this file represent the resource JSON description
format and provide a layer of abstraction from the raw JSON. The advantages
of this are:

* Pythonic interface (e.g. ``action.request.operation``)
* Consumers need not change for minor JSON changes (e.g. renamed field)

These models are used both by the resource factory to generate resource
classes as well as by the documentation generator.
"""

import logging


logger = logging.getLogger(__name__)


class Identifier(object):
    """
    A resource identifier, given by its name.

    :type name: string
    :param name: The name of the identifier
    """
    def __init__(self, name):
        #: (``string``) The name of the identifier
        self.name = name


class Action(object):
    """
    A service operation action.

    :type name: string
    :param name: The name of the action
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    def __init__(self, name, definition, resource_defs):
        self._definition = definition

        #: (``string``) The name of the action
        self.name = name
        #: (:py:class:`Request`) This action's request or ``None``
        self.request = None
        if 'request' in definition:
            self.request = Request(definition.get('request', {}))
        #: (:py:class:`ResponseResource`) This action's resource or ``None``
        self.resource = None
        if 'resource' in definition:
            self.resource = ResponseResource(definition.get('resource', {}),
                                             resource_defs)
        #: (``string``) The JMESPath search path or ``None``
        self.path = definition.get('path')



class DefinitionWithParams(object):
    """
    An item which has parameters exposed via the ``params`` property.
    A request has an operation and parameters, while a waiter has
    a name, a low-level waiter name and parameters.

    :type definition: dict
    :param definition: The JSON definition
    """
    def __init__(self, definition):
        self._definition = definition

    @property
    def params(self):
        """
        Get a list of auto-filled parameters for this request.

        :type: list(:py:class:`Parameter`)
        """
        params = []

        for item in self._definition.get('params', []):
            params.append(Parameter(**item))

        return params


class Parameter(object):
    """
    An auto-filled parameter which has a source and target. For example,
    the ``QueueUrl`` may be auto-filled from a resource's ``url`` identifier
    when making calls to ``queue.receive_messages``.

    :type target: string
    :param target: The destination parameter name, e.g. ``QueueUrl``
    :type source_type: string
    :param source_type: Where the source is defined.
    :type source: string
    :param source: The source name, e.g. ``Url``
    """
    def __init__(self, target, source, name=None, path=None, value=None,
                 **kwargs):
        #: (``string``) The destination parameter name
        self.target = target
        #: (``string``) Where the source is defined
        self.source = source
        #: (``string``) The name of the source, if given
        self.name = name
        #: (``string``) The JMESPath query of the source
        self.path = path
        #: (``string|int|float|bool``) The source constant value
        self.value = value

        # Complain if we encounter any unknown values.
        if kwargs:
            logger.warning('Unknown parameter options found: %s', kwargs)


class Request(DefinitionWithParams):
    """
    A service operation action request.

    :type definition: dict
    :param definition: The JSON definition
    """
    def __init__(self, definition):
        super(Request, self).__init__(definition)

        #: (``string``) The name of the low-level service operation
        self.operation = definition.get('operation')


class Waiter(DefinitionWithParams):
    """
    An event waiter specification.

    :type name: string
    :param name: Name of the waiter
    :type definition: dict
    :param definition: The JSON definition
    """
    def __init__(self, name, definition):
        super(Waiter, self).__init__(definition)

        #: (``string``) The name of this waiter
        self.name = name

        #: (``string``) The name of the waiter in the resource
        self.resource_waiter_name = 'WaitUntil' + name

        #: (``string``) The name of the underlying event waiter
        self.waiter_name = definition.get('waiterName')


class ResponseResource(object):
    """
    A resource response to create after performing an action.

    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    def __init__(self, definition, resource_defs):
        self._definition = definition
        self._resource_defs = resource_defs

        #: (``string``) The name of the response resource type
        self.type = definition.get('type')

        #: (``string``) The JMESPath search query or ``None``
        self.path = definition.get('path')

    @property
    def identifiers(self):
        """
        A list of resource identifiers.

        :type: list(:py:class:`Identifier`)
        """
        identifiers = []

        for item in self._definition.get('identifiers', []):
            identifiers.append(
                Parameter(**item))

        return identifiers

    @property
    def model(self):
        """
        Get the resource model for the response resource.

        :type: :py:class:`ResourceModel`
        """
        return ResourceModel(self.type, self._resource_defs[self.type],
                             self._resource_defs)


class Collection(Action):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    @property
    def batch_actions(self):
        """
        Get a list of batch actions supported by the resource type
        contained in this action. This is a shortcut for accessing
        the same information through the resource model.

        :rtype: list(:py:class:`Action`)
        """
        return self.resource.model.batch_actions


class ResourceModel(object):
    """
    A model representing a resource, defined via a JSON description
    format. A resource has identifiers, attributes, actions,
    sub-resources, references and collections. For more information
    on resources, see :ref:`guide_resources`.

    :type name: string
    :param name: The name of this resource, e.g. ``sqs`` or ``Queue``
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    def __init__(self, name, definition, resource_defs):
        self._definition = definition
        self._resource_defs = resource_defs

        #: (``string``) The name of this resource
        self.name = name
        #: (``string``) The service shape name for this resource or ``None``
        self.shape = definition.get('shape')

    @property
    def identifiers(self):
        """
        Get a list of resource identifiers.

        :type: list(:py:class:`Identifier`)
        """
        identifiers = []

        for item in self._definition.get('identifiers', []):
            identifiers.append(Identifier(item['name']))

        return identifiers

    @property
    def load(self):
        """
        Get the load action for this resource, if it is defined.

        :type: :py:class:`Action` or ``None``
        """
        action = self._definition.get('load')

        if action is not None:
            action = Action('load', action, self._resource_defs)

        return action

    @property
    def actions(self):
        """
        Get a list of actions for this resource.

        :type: list(:py:class:`Action`)
        """
        actions = []

        for name, item in self._definition.get('actions', {}).items():
            actions.append(Action(name, item, self._resource_defs))

        return actions

    @property
    def batch_actions(self):
        """
        Get a list of batch actions for this resource.

        :type: list(:py:class:`Action`)
        """
        actions = []

        for name, item in self._definition.get('batchActions', {}).items():
            actions.append(Action(name, item, self._resource_defs))

        return actions

    def _get_has_definition(self):
        """
        Get a ``has`` relationship definition from a model, where the
        service resource model is treated special in that it contains
        a relationship to every resource defined for the service. This
        allows things like ``s3.Object('bucket-name', 'key')`` to
        work even though the JSON doesn't define it explicitly.

        :rtype: dict
        :return: Mapping of names to subresource and reference
                 definitions.
        """
        if self.name not in self._resource_defs:
            # This is the service resource, so let us expose all of
            # the defined resources as subresources.
            definition = {}

            for name, resource_def in self._resource_defs.items():
                # It's possible for the service to have renamed a
                # resource or to have defined multiple names that
                # point to the same resource type, so we need to
                # take that into account.
                found = False
                has_items = self._definition.get('has', {}).items()
                for has_name, has_def in has_items:
                    if has_def.get('resource', {}).get('type') == name:
                        definition[has_name] = has_def
                        found = True

                if not found:
                    # Create a relationship definition and attach it
                    # to the model, such that all identifiers must be
                    # supplied by the user. It will look something like:
                    #
                    # {
                    #   'resource': {
                    #     'type': 'ResourceName',
                    #     'identifiers': [
                    #       {'target': 'Name1', 'source': 'input'},
                    #       {'target': 'Name2', 'source': 'input'},
                    #       ...
                    #     ]
                    #   }
                    # }
                    #
                    fake_has = {
                        'resource': {
                            'type': name,
                            'identifiers': []
                        }
                    }

                    for identifier in resource_def.get('identifiers', []):
                        fake_has['resource']['identifiers'].append({
                            'target': identifier['name'], 'source': 'input'
                        })

                    definition[name] = fake_has
        else:
            definition = self._definition.get('has', {})

        return definition

    def _get_related_resources(self, subresources):
        """
        Get a list of sub-resources or references.

        :type subresources: bool
        :param subresources: ``True`` to get sub-resources, ``False`` to
                             get references.
        :rtype: list(:py:class:`ResponseResource`)
        """
        resources = []

        for name, definition in self._get_has_definition().items():
            action = Action(name, definition, self._resource_defs)

            data_required = False
            for identifier in action.resource.identifiers:
                if identifier.source == 'data':
                    data_required = True
                    break

            if subresources and not data_required:
                resources.append(action)
            elif not subresources and data_required:
                resources.append(action)

        return resources

    @property
    def subresources(self):
        """
        Get a list of sub-resources.

        :type: list(:py:class`ResponseResource`)
        """
        return self._get_related_resources(True)

    @property
    def references(self):
        """
        Get a list of reference resources.

        :type: list(:py:class:`ResponseResource`)
        """
        return self._get_related_resources(False)

    @property
    def collections(self):
        """
        Get a list of collections for this resource.

        :type: list(:py:class:`Collection`)
        """
        collections = []

        for name, item in self._definition.get('hasMany', {}).items():
            collections.append(Collection(name, item, self._resource_defs))

        return collections

    @property
    def waiters(self):
        """
        Get a list of waiters for this resource.

        :type: list(:py:class:`Waiter`)
        """
        waiters = []

        for name, item in self._definition.get('waiters', {}).items():
            waiters.append(Waiter(name, item))

        return waiters
