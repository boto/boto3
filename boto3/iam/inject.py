# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
    Call iam.client.list_access_keys to get the status
    """
    response = self.meta.client.list_access_keys(UserName=self.user_name)
    for access_key_dict in response['AccessKeyMetadata']:
        if access_key_dict['AccessKeyId'] == self.id:
            new_response = access_key_dict
            break
    self.meta.data = new_response 
