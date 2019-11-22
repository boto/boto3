# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from boto3.resources.action import CustomModeledAction


def inject_delete_tags(event_emitter, **kwargs):
    action_model = {
        'request': {
            'operation': 'DeleteTags',
            'params': [{
                'target': 'Resources[0]',
                'source': 'identifier',
                'name': 'Id'
            }]
        }
    }
    action = CustomModeledAction(
        'delete_tags', action_model, delete_tags, event_emitter)
    action.inject(**kwargs)


def delete_tags(self, **kwargs):
    """
    Deletes the specified set of tags from the specified set of resources.

    To list the current tags, use DescribeTags . For more information about tags, see
    `Tagging Your Resources <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__
    in the *Amazon Elastic Compute Cloud User Guide* .

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_

    **Request Syntax**
    ::

      response = client.delete_tags(
          DryRun=True|False,
          Resources=[
              'string',
          ],
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )

    :type DryRun: boolean
    :param DryRun:

      Checks whether you have the required permissions for the action,
      without actually making the request, and provides an error response.
      If you have the required permissions, the error response
      is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .

    :type Resources: list
    :param Resources: **[REQUIRED]**

      The IDs of the resources, separated by spaces.

      Constraints: Up to 1000 resource IDs. We recommend breaking up this
      request into smaller batches.

      - *(string) --*

    :type Tags: list
    :param Tags:

      The tags to delete. Specify a tag key and an optional tag value to delete
      specific tags. If you specify a tag key without a tag value, we delete any
      tag with this key regardless of its value. If you specify a tag key with
      an empty string as the tag value, we delete the tag only if its value is
      an empty string.

      If you omit this parameter, we delete all user-defined tags for the specified
      resources. We do not delete AWS-generated tags (tags that have the ``aws:`` prefix).

      - *(dict) --*-

        Describes a tag.

        - **Key** *(string) --*

          The key of the tag.

          Constraints: Tag keys are case-sensitive and accept a maximum of 127
          Unicode characters. May not begin with ``aws:`` .

        - **Value** *(string) --*

          The value of the tag.

          Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.


    """
    kwargs['Resources'] = [self.id]
    return self.meta.client.delete_tags(**kwargs)
