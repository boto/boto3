# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from importlib.resources import path
from unittest.mock import patch

import boto3.session
from tests import unittest


class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = boto3.session.Session(region_name='us-west-2')

    def test_events_attribute(self):
        # Create some function to register.
        def my_handler(my_list, **kwargs):
            return my_list.append('my_handler called')

        # Register the handler to the event.
        self.session.events.register('myevent', my_handler)

        initial_list = []
        # Emit the event.
        self.session.events.emit('myevent', my_list=initial_list)
        # Ensure that the registered handler was called.
        assert initial_list == ['my_handler called']

    def test_can_access_region_property(self):
        session = boto3.session.Session(region_name='us-west-1')
        assert session.region_name == 'us-west-1'

    def test_get_available_partitions(self):
        partitions = self.session.get_available_partitions()
        assert isinstance(partitions, list)
        assert partitions

    def test_get_available_regions(self):
        regions = self.session.get_available_regions('s3')
        assert isinstance(regions, list)
        assert regions

    def test_loader_search_path(self):
        with patch.object(boto3.session, '__file__', None):
            session = boto3.session.Session()
            with path(boto3, "data") as data_path:
                assert str(data_path) in session._loader.search_paths
