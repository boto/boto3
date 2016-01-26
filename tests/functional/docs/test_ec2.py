# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from tests.functional.docs import BaseDocsFunctionalTests

from boto3.session import Session
from boto3.docs.service import ServiceDocumenter


class TestInstanceDeleteTags(BaseDocsFunctionalTests):
    def setUp(self):
        self.documenter = ServiceDocumenter(
            'ec2', session=Session(region_name='us-east-1'))
        self.generated_contents = self.documenter.document_service()
        self.generated_contents = self.generated_contents.decode('utf-8')

    def test_delete_tags_method_is_documented(self):
        contents = self.get_class_document_block(
                'EC2.Instance', self.generated_contents)
        method_contents = self.get_method_document_block(
                'delete_tags', contents)
        self.assert_contains_lines_in_order([
            'response = instance.delete_tags(',
            'DryRun=True|False,',
            'Tags=[',
        ], method_contents)
