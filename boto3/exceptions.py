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

class ResourceLoadException(Exception):
    pass


class NoVersionFound(Exception):
    pass


class UnknownAPIVersionError(Exception):
    def __init__(self, service_name, bad_api_version,
                 available_api_versions):
        msg = (
            "The '%s' resource does not an API version of: %s\n"
            "Valid API versions are: %s"
            % (service_name, bad_api_version, available_api_versions)
        )
        super(UnknownAPIVersionError, self).__init__(msg)


class ResourceNotExistsError(Exception):
    """Raised when you attempt to create a resource that does not exist."""
    def __init__(self, service_name, available_services, has_low_level_client):
        msg = (
            "The '%s' resource does not exist.\n"
            "The available resources are:\n"
            "   - %s\n" % (service_name, '\n   - '.join(available_services))
        )
        if has_low_level_client:
            msg += (
                "\nConsider using a boto3.client('%s') instead "
                "of a resource for '%s'" % (service_name, service_name))
        super(ResourceNotExistsError, self).__init__(msg)


class RetriesExceededError(Exception):
    def __init__(self, last_exception, msg='Max Retries Exceeded'):
        super(RetriesExceededError, self).__init__(msg)
        self.last_exception = last_exception


class S3TransferFailedError(Exception):
    pass


class S3UploadFailedError(Exception):
    pass


class DynamoDBOperationNotSupportedError(Exception):
    """Raised for operantions that are not supported for an operand"""
    def __init__(self, operation, value):
        msg = (
            '%s operation cannot be applied to value %s of type %s directly. '
            'Must use AttributeBase object methods (i.e. Attr().eq()). to '
            'generate ConditionBase instances first.' %
            (operation, value, type(value)))
        Exception.__init__(self, msg)

# FIXME: Backward compatibility
DynanmoDBOperationNotSupportedError = DynamoDBOperationNotSupportedError

class DynamoDBNeedsConditionError(Exception):
    """Raised when input is not a condition"""
    def __init__(self, value):
        msg = (
            'Expecting a ConditionBase object. Got %s of type %s. '
            'Use AttributeBase object methods (i.e. Attr().eq()). to '
            'generate ConditionBase instances.' % (value, type(value)))
        Exception.__init__(self, msg)


class DynamoDBNeedsKeyConditionError(Exception):
    pass
