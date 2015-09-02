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
from botocore.docs.docstring import LazyLoadedDocstring

from boto3.docs.action import document_action
from boto3.docs.action import document_load_reload_action
from boto3.docs.subresource import document_sub_resource


class ActionDocstring(LazyLoadedDocstring):
    def __init__(self, *args, **kwargs):
        super(ActionDocstring, self).__init__(*args, **kwargs)
        self._docstring_writer = document_action


class LoadReloadDocstring(LazyLoadedDocstring):
    def __init__(self, *args, **kwargs):
        super(LoadReloadDocstring, self).__init__(*args, **kwargs)
        self._docstring_writer = document_load_reload_action


class SubResourceDocstring(LazyLoadedDocstring):
    def __init__(self, *args, **kwargs):
        super(SubResourceDocstring, self).__init__(*args, **kwargs)
        self._docstring_writer = document_sub_resource
