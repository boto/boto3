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
from tests.unit.docs import BaseDocsTest

from boto3.docs.waiter import WaiterResourceDocumenter


class TestWaiterResourceDocumenter(BaseDocsTest):
    def test_document_resource_waiters(self):
        service_waiter_model = self.botocore_session.get_waiter_model(
            'myservice')
        subresource = self.resource.Sample('mysample')
        waiter_documenter = WaiterResourceDocumenter(
            subresource, service_waiter_model)
        waiter_documenter.document_resource_waiters(self.doc_structure)
        self.assert_contains_lines_in_order([
            '.. py:method:: wait_until_complete(**kwargs)',
            ('  Waits until this Sample is complete. This method calls '
             ':py:meth:`MyService.Waiter.sample_operation_complete.wait` '
             'which polls. :py:meth:`MyService.Client.sample_operation` '
             'every 15 seconds until a successful state is reached. An '
             'error is returned after 40 failed checks.'),
            '  **Request Syntax** ',
            '  ::',
            '    sample.wait_until_complete(',
            "        Bar='string'",
            '    )',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :returns: None'
        ])
