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
from boto3.s3.transfer import S3Transfer
from boto3 import utils


def inject_s3_transfer_methods(class_attributes, **kwargs):
    utils.inject_attribute(class_attributes, 'upload_file', upload_file)
    utils.inject_attribute(class_attributes, 'download_file', download_file)


def upload_file(self, Filename, Bucket, Key, ExtraArgs=None,
                Callback=None, Config=None):
    transfer = S3Transfer(self, Config)
    return transfer.upload_file(
        filename=Filename, bucket=Bucket, key=Key,
        extra_args=ExtraArgs, callback=Callback)


def download_file(self, Bucket, Key, Filename, ExtraArgs=None,
                  Callback=None, Config=None):
    transfer = S3Transfer(self, Config)
    return transfer.download_file(
        bucket=Bucket, key=Key, filename=Filename,
        extra_args=ExtraArgs, callback=Callback)
