.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ses-template:   

###############################################
Creating custom email templates with Amazon SES
###############################################

.. meta::
   :description: Use the Amazon SES API to create and use email templates.
   :keywords: SES Python

Amazon Simple Email Service (SES) enables you to send emails that are 
personalized for each recipient by using templates. Templates include 
a subject line and the text and HTML parts of the email body. The subject 
and body sections can also contain unique values that are personalized for 
each recipient.

For more information, see `Sending Personalized Email Using the Amazon SES 
API <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html>`__.

The following examples show how to:

* Create an email template using `create_template() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_template>`_.
* List all email templates using `list_templates() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_templates>`_.
* Retrieve an email template using `get_template() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_template>`_.
* Update an email template using `update_template() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_template>`_.
* Remove an email template using `delete_template() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_template>`_.
* Send a templated email using `send_templated_email() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_templated_email>`_.

Prerequisite tasks
==================

To set up and run this example, you must first complete these tasks:

* Configure your AWS credentials, as described in :doc:`quickstart`.

Create an email template
========================

To create a template to send personalized email messages, use the 
`CreateTemplate <https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateTemplate.html>`_ 
operation. The template can be used by any account authorized to send 
messages in the AWS Region to which the template is added.

.. note::
    SES doesn't validate your HTML, so be sure that ``HtmlPart`` is 
    valid before sending an email.
    
Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.create_template(
      Template = {
        'TemplateName' : 'TEMPLATE_NAME',
        'SubjectPart'  : 'SUBJECT_LINE',
        'TextPart'     : 'TEXT_CONTENT',
        'HtmlPart'     : 'HTML_CONTENT'
      }
    )


    print(response)

Get an email template
=====================

To view the content for an existing email template including the subject line, HTML body, and plain text, use the `GetTemplate <https://docs.aws.amazon.com/ses/latest/APIReference/API_GetTemplate.html>`_ operation. Only TemplateName is required.

Example
-------

.. code-block:: python

    import boto3
    
    # Create SES client
    ses = boto3.client('ses')

    response = ses.get_template(
      TemplateName = 'TEMPLATE_NAME'
    )

    print(response)

List all email templates
========================

To retrieve a list of all email templates that are associated with your AWS account in the current AWS Region, use the `ListTemplates <https://docs.aws.amazon.com/ses/latest/APIReference/API_ListTemplates.html>`_ operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.list_templates(
      MaxItems=10
    )

    print(response)


Update an email template
========================

To change the content for a specific email template including the subject line, HTML body, and plain text, use the `UpdateTemplate <https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateTemplate.html>`_ operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.update_template(
      Template={
        'TemplateName': 'TEMPLATE_NAME',
        'SubjectPart' : 'SUBJECT_LINE',
        'TextPart'    : 'TEXT_CONTENT',
        'HtmlPart'    : 'HTML_CONTENT'
      }
    )
    
    print(response)
   
Send an email with a template
=============================

To use a template to send an email to recipients, use the `SendTemplatedEmail <https://docs.aws.amazon.com/ses/latest/APIReference/API_SendTemplatedEmail.html>`__ operation.


Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.send_templated_email(
      Source='EMAIL_ADDRESS',
      Destination={
        'ToAddresses': [
          'EMAIL_ADDRESS',
        ],
        'CcAddresses': [
          'EMAIL_ADDRESS',
        ]
      },
      ReplyToAddresses=[
        'EMAIL_ADDRESS',
      ],
      Template='TEMPLATE_NAME',
      TemplateData='{ \"REPLACEMENT_TAG_NAME\":\"REPLACEMENT_VALUE\" }'
    )

    print(response)