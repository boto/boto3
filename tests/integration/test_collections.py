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

import boto3.session

from boto3.resources.collection import CollectionManager


# A map of services to regions that cannot use us-west-2
# for the integration tests.
REGION_MAP = {
    'opsworks': 'us-east-1'
}

# A list of collections to ignore. They require parameters
# or are very slow to run.
BLACKLIST = {
    'ec2': ['images'],
    'iam': ['signing_certificates'],
    'sqs': ['dead_letter_source_queues']
}


def test_all_collections():
    # This generator yields test functions for every collection
    # on every available resource, except those which have
    # been blacklisted.
    session = boto3.session.Session()
    for service_name in session.get_available_resources():
        resource = session.resource(
            service_name,
            region_name=REGION_MAP.get(service_name, 'us-west-2'))

        for key in dir(resource):
            if key in BLACKLIST.get(service_name, []):
                continue

            value = getattr(resource, key)
            if isinstance(value, CollectionManager):
                yield _test_collection, service_name, key, value

def _test_collection(service_name, collection_name, collection):
    # Create a list of the first page of items. This tests that
    # a remote request can be made, the response parsed, and that
    # resources are successfully created.
    list(collection.limit(1))
