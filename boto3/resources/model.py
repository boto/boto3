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
            params.append(
                Parameter(item['target'], item['sourceType'], item['source']))

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
    def __init__(self, target, source_type, source):
        #: (``string``) The destination parameter name
        self.target = target
        #: (``string``) Where the source is defined
        self.source_type = source_type
        #: (``string``) The source name
        self.source = source


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
                Parameter(item['target'], item['sourceType'], item['source']))

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


class SubResourceList(object):
    """
    A list of information about sub-resources. It includes access
    to identifiers as well as resource names and models.

    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    def __init__(self, definition, resource_defs):
        self._definition = definition
        self._resource_defs = resource_defs

        #: (``dict``) Identifier key:value pairs
        self.identifiers = definition.get('identifiers', {})
        #: (``list``) A list of resource names
        self.resource_names = definition.get('resources', [])

    @property
    def resources(self):
        """
        Get a list of resource models contained in this sub-resource
        entry.

        :type: list(:py:class:`ResourceModel`)
        """
        resources = []

        for name in self.resource_names:
            resources.append(
                ResourceModel(name, self._resource_defs.get(name, {}),
                              self._resource_defs))

        return resources


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
        #: (:py:class:`SubResourceList`) Sub-resource information or ``None``
        self.sub_resources = None
        if 'subResources' in definition:
            self.sub_resources = SubResourceList(
                definition.get('subResources', {}), resource_defs)

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

    @property
    def references(self):
        """
        Get a list of reference resources.

        :type: list(:py:class:`ResponseResource`)
        """
        references = []

        for key in ['belongsTo']:
            for name, definition in self._definition.get(key, {}).items():
                references.append(
                    Action(name, definition, self._resource_defs))

        return references

    @property
    def reverse_references(self):
        """
        Get a list of reverse reference resources. E.g. an S3 object has
        a ``bucket_name`` identifier that can be used to instantiate a
        bucket resource instance.
        """
        references = []

        # First, we search for possible reverse references based on the
        # defined sub-resources in each resource. If the name of this
        # resource is present, then we are a child. Next, we use the
        # identifiers to construct a reference definition, append it
        # to the list of references and return.

        for name, definition in self._resource_defs.items():
            sub_resources = definition.get('subResources', {})
            resource_names = sub_resources.get('resources', [])

            if self.name in resource_names:
                logger.debug('Discovered reverse reference from {0}'
                             ' to {1}'.format(self.name, name))

                identifiers = sub_resources.get('identifiers', {})

                has_one_def = {
                    'resource': {
                        'type': name,
                        'identifiers': []
                    }
                }

                for target, source in identifiers.items():
                    has_one_def['resource']['identifiers'].append(
                        {'target': target, 'sourceType': 'identifier',
                         'source': source})

                references.append(
                    Action(name, has_one_def, self._resource_defs))

        return references

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
