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
import sys
from collections import namedtuple


ServiceContext = namedtuple(
    'ServiceContext',
    ['service_name', 'service_model', 'service_waiter_model',
     'resource_json_definitions']
)


def import_module(name):
    """Import module given a name.

    Does not support relative imports.

    """
    __import__(name)
    return sys.modules[name]


def lazy_call(full_name):
    def _handler(**kwargs):
        module, function_name = full_name.rsplit('.', 1)
        module = import_module(module)
        return getattr(module, function_name)(**kwargs)
    return _handler


def inject_attribute(class_attributes, name, value):
    if name in class_attributes:
        raise RuntimeError(
            'Cannot inject class attribute "%s", attribute '
            'already exists in class dict.' % name)
    else:
        class_attributes[name] = value


class LazyLoadedWaiterModel(object):
    """A lazily loaded waiter model

    This does not load the service waiter model until an attempt is made
    to retrieve the waiter model for a specific waiter. This is helpful
    in docstring generation where we do not need to actually need to grab
    the waiter-2.json until it is accessed through a ``get_waiter`` call
    when the docstring is generated/accessed.
    """
    def __init__(self, bc_session, service_name, api_version):
        self._session = bc_session
        self._service_name = service_name
        self._api_version = api_version

    def get_waiter(self, waiter_name):
        return self._session.get_waiter_model(
            self._service_name, self._api_version).get_waiter(waiter_name)
