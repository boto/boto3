# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from boto3.docs.service import ServiceDocumenter
from boto3.session import Session
from tests.functional.docs import BaseDocsFunctionalTests


class TestCloudWatchMetricPutActionOverrides(BaseDocsFunctionalTests):
    def setUp(self):
        super().setUp()
        self.documenter = ServiceDocumenter(
            'cloudwatch',
            session=Session(region_name='us-east-1'),
            root_docs_path=self.root_services_path,
        )
        self.generated_contents = self.documenter.document_service()
        self.generated_contents = self.generated_contents.decode('utf-8')

    def test_put_action_overrides(self):
        put_action_contents = self.get_nested_file_contents(
            "cloudwatch", "metric", "put_data"
        )
        self.assert_contains_lines_in_order(
            [
                ".. warning::",
                "Please note that this method does not function as expected. It is",
                "recommended to use the :py:meth:`put_metric_data`",
                ":doc:`client method <../../cloudwatch/client/put_metric_data>` instead.",
                "If you would still like to use this method, please make sure that",
                "``MetricData[].MetricName`` is equal to the metric resource's ``name`` attribute.",
            ],
            put_action_contents,
        )

    def test_put_action_override_not_present_in_other_action(self):
        put_alarm_contents = self.get_nested_file_contents(
            "cloudwatch", "metric", "put_alarm"
        )
        lines = [
            ".. warning::",
            "Please note that this method does not function as expected. It is",
            "recommended to use the :py:meth:`put_metric_data`",
            ":doc:`client method <../../cloudwatch/client/put_metric_data>` instead.",
            "If you would still like to use this method, please make sure that",
            "``MetricData[].MetricName`` is equal to the metric resource's ``name`` attribute.",
        ]
        for line in lines:
            self.assertNotIn(line, put_alarm_contents)
