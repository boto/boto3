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

from boto3 import utils

def inject_access_key_methods(class_attributes, **kwargs):
    utils.inject_attribute(class_attributes, 'load', access_key_load)

def access_key_load(self, *args, **kwargs):
    """
    Call s3.client.list_access_keys to get the status
    """
    response = self.meta.client.list_access_keys(UserName= self.user_name)
    for access_key in response['AccessKeyMetadata']:
        if access_key['AccessKeyId'] == self.id:
            response = access_key
    self.meta.data = response 