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
from tests.functional.docs import BaseDocsFunctionalTests

from boto3.session import Session
from boto3.docs.service import ServiceDocumenter


class TestS3Customizations(BaseDocsFunctionalTests):
    def setUp(self):
        self.documenter = ServiceDocumenter(
            's3', session=Session(region_name='us-east-1'))
        self.generated_contents = self.documenter.document_service()
        self.generated_contents = self.generated_contents.decode('utf-8')

    def test_file_transfer_methods_are_documented(self):
        self.assert_contains_lines_in_order([
            '.. py:class:: S3.Client',
            '  *   :py:meth:`~S3.Client.download_file`',
            '  *   :py:meth:`~S3.Client.upload_file`',
            '  .. py:method:: download_file(',
            '  .. py:method:: upload_file('],
            self.generated_contents
        )
