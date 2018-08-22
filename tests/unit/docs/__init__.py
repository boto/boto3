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
import os
import json
import tempfile
import shutil
from tests import unittest

import botocore.session
from botocore.compat import OrderedDict
from botocore.loaders import Loader
from botocore.docs.bcdoc.restdoc import DocumentStructure

from boto3.session import Session


class BaseDocsTest(unittest.TestCase):
    def setUp(self):
        self.root_dir = tempfile.mkdtemp()
        self.version_dirs = os.path.join(
            self.root_dir, 'myservice', '2014-01-01')
        os.makedirs(self.version_dirs)

        self.model_file = os.path.join(self.version_dirs, 'service-2.json')
        self.waiter_model_file = os.path.join(
            self.version_dirs, 'waiters-2.json')
        self.paginator_model_file = os.path.join(
            self.version_dirs, 'paginators-1.json')
        self.resource_model_file = os.path.join(
            self.version_dirs, 'resources-1.json')
        self.example_model_file = os.path.join(
            self.version_dirs, 'examples-1.json')

        self.json_model = {}
        self.waiter_json_model = {}
        self.paginator_json_model = {}
        self.resource_json_model = {}
        self._setup_models()

        self.doc_name = 'MyDoc'
        self.doc_structure = DocumentStructure(self.doc_name)

        self.setup_client_and_resource()

    def tearDown(self):
        shutil.rmtree(self.root_dir)

    def setup_client_and_resource(self):
        self._write_models()
        self.loader = Loader(extra_search_paths=[self.root_dir])
        self.botocore_session = botocore.session.get_session()
        self.botocore_session.register_component('data_loader', self.loader)
        self.session = Session(
            botocore_session=self.botocore_session, region_name='us-east-1')
        self.client = self.session.client('myservice', 'us-east-1')
        self.resource = self.session.resource('myservice', 'us-east-1')

    def _setup_models(self):
        self.json_model = {
            'metadata': {
                'apiVersion': '2014-01-01',
                'endpointPrefix': 'myservice',
                'signatureVersion': 'v4',
                'serviceFullName': 'AWS MyService',
                'protocol': 'query',
                'serviceId': 'MyService',
            },
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
                    'members': OrderedDict([
                        ('Foo', {
                            'shape': 'String',
                            'documentation': 'Documents Foo'}),
                        ('Bar', {
                            'shape': 'String',
                            'documentation': 'Documents Bar'}),
                    ])
                },
                'String': {
                    'type': 'string'
                }
            }
        }

        self.example_json_model = {
            "version": 1,
            "examples": {
                "SampleOperation": [{
                    "id": "sample-id",
                    "title": "sample-title",
                    "description": "Sample Description.",
                    "input": OrderedDict([
                        ("Foo", "bar"),
                    ]),
                    "comments": {
                        "input": {
                            "Foo": "biz"
                        },
                    }
                }]
            }
        }

        self.waiter_json_model = {
            "version": 2,
            "waiters": {
                "SampleOperationComplete": {
                    "delay": 15,
                    "operation": "SampleOperation",
                    "maxAttempts": 40,
                    "acceptors": [
                        {"expected": "complete",
                         "matcher": "pathAll",
                         "state": "success",
                         "argument": "Biz"},
                        {"expected": "failed",
                         "matcher": "pathAny",
                         "state": "failure",
                         "argument": "Biz"}
                    ]
                }
            }
        }

        self.paginator_json_model = {
            "pagination": {
                "SampleOperation": {
                    "input_token": "NextResult",
                    "output_token": "NextResult",
                    "limit_key": "MaxResults",
                    "result_key": "Biz"
                }
            }
        }

        self.resource_json_model = {
            "service": {
                "actions": OrderedDict([
                    ("SampleOperation", {
                        "request": {"operation": "SampleOperation"}
                    }),
                    ("SampleListReturnOperation", {
                        "request": {"operation": "SampleOperation"},
                        "resource": {
                            "type": "Sample",
                            "identifiers": [
                                {"target": "Name", "source": "response",
                                 "path": "Samples[].Name"}
                            ],
                            "path": "Samples[]"
                        }
                    })
                ]),
                "has": {
                    "Sample": {
                        "resource": {
                            "type": "Sample",
                            "identifiers": [
                                {"target": "Name", "source": "input"}
                            ]
                        }
                    }
                },
                "hasMany": {
                    "Samples": {
                        "request": {"operation": "SampleOperation"},
                        "resource": {
                            "type": "Sample",
                            "identifiers": [
                                {"target": "Name", "source": "response",
                                 "path": "Samples[].Foo"}
                            ]
                        }
                    }
                }
            },
            "resources": {
                "Sample": {
                    "identifiers": [
                        {"name": "Name", "memberName": "Foo"}
                    ],
                    "shape": "SampleOperationInputOutput",
                    "load": {
                        "request": {
                            "operation": "SampleOperation",
                            "params": [
                                {"target": "Foo", "source": "identifier",
                                 "name": "Name"}
                            ]
                        }
                    },
                    "actions": {
                        "Operate": {
                            "request": {
                                "operation": "SampleOperation",
                                "params": [
                                    {"target": "Foo", "source": "identifier",
                                     "name": "Name"}
                                ]
                            }
                        }
                    },
                    "batchActions": {
                        "Operate": {
                            "request": {
                                "operation": "SampleOperation",
                                "params": [
                                    {"target": "Samples[].Foo",
                                     "source": "identifier", "name": "Name"}
                                ]
                            }
                        }
                    },
                    "has": {
                        "RelatedSample": {
                            "resource": {
                                "type": "Sample",
                                "identifiers": [
                                    {"target": "Name", "source": "data",
                                     "path": "Foo"}
                                ]
                            }
                        }
                    },
                    "waiters": {
                        "Complete": {
                            "waiterName": "SampleOperationComplete",
                            "params": [
                                {"target": "Foo", "source": "identifier",
                                 "name": "Name"}
                            ]
                        }
                    }
                }
            }
        }

    def _write_models(self):
        with open(self.resource_model_file, 'w') as f:
            json.dump(self.resource_json_model, f)

        with open(self.waiter_model_file, 'w') as f:
            json.dump(self.waiter_json_model, f)

        with open(self.paginator_model_file, 'w') as f:
            json.dump(self.paginator_json_model, f)

        with open(self.model_file, 'w') as f:
            json.dump(self.json_model, f)

        with open(self.example_model_file, 'w') as f:
            json.dump(self.example_json_model, f)

    def add_shape(self, shape):
        shape_name = list(shape.keys())[0]
        self.json_model['shapes'][shape_name] = shape[shape_name]

    def add_shape_to_params(self, param_name, shape_name, documentation=None,
                            is_required=False):
        params_shape = self.json_model['shapes']['SampleOperationInputOutput']
        member = {'shape': shape_name}
        if documentation is not None:
            member['documentation'] = documentation
        params_shape['members'][param_name] = member

        if is_required:
            required_list = params_shape.get('required', [])
            required_list.append(param_name)
            params_shape['required'] = required_list

    def assert_contains_lines_in_order(self, lines, contents=None):
        if contents is None:
            contents = self.doc_structure.flush_structure().decode('utf-8')
        for line in lines:
            self.assertIn(line, contents)
            beginning = contents.find(line)
            contents = contents[(beginning + len(line)):]

    def assert_not_contains_lines(self, lines):
        contents = self.doc_structure.flush_structure().decode('utf-8')
        for line in lines:
            self.assertNotIn(line, contents)
