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
