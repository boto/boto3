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


def inject_create_tags(event_name, class_attributes, **kwargs):
    """This injects a custom create_tags method onto the ec2 service resource

    This is needed because the resource model is not able to express
    creating multiple tag resources based on the fact you can apply a set
    of tags to multiple ec2 resources.
    """
    class_attributes['create_tags'] = create_tags


def create_tags(self, **kwargs):
    """
    Adds or overwrites the specified tags for the specified Amazon EC2
    resource or resources. Each resource can have a maximum of 50 tags.
    Each tag consists of a key and optional value. Tag keys must be unique
    per resource.

    For more information about tags, see
    `Tagging Your Resources <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__
    in the *Amazon Elastic Compute Cloud User Guide* . For more information about
    creating IAM policies that control users' access to resources based on tags, see
    `Supported Resource-Level Permissions for Amazon EC2 API Actions
    <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__
    in the *Amazon Elastic Compute Cloud User Guide* .

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_

    **Request Syntax**
    ::

      response = client.create_tags(
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
    :param Tags: **[REQUIRED]**

      The tags. The ``value`` parameter is required, but if you don't want the tag to
      have a value, specify the parameter with no value, and we set the value to an
      empty string.

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
    # Call the client method
    self.meta.client.create_tags(**kwargs)
    resources = kwargs.get('Resources', [])
    tags = kwargs.get('Tags', [])
    tag_resources = []

    # Generate all of the tag resources that just were created with the
    # preceding client call.
    for resource in resources:
        for tag in tags:
            # Add each tag from the tag set for each resource to the list
            # that is returned by the method.
            tag_resource = self.Tag(resource, tag['Key'], tag['Value'])
            tag_resources.append(tag_resource)
    return tag_resources
