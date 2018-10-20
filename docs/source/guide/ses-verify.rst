.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ses-verify:   

############################################
Verifying Email Identities in Amazon SES
############################################

.. meta::
   :description: Use Amazon SES API to verify email addresses and domains.
   :keywords: Amazon SES code examples for Python, approve emails recipients with Python

When you first start using your Amazon Simple Email Service (SES) account, all senders and recipients must be verified in the same AWS Region that you
will be sending emails to. For more information about sending emails, see `Sending Email with Amazon SES <http://aws.amazon.com/documentation/ses/sending-email.html>`__.

The following examples show how to:

* Verify an email address using `verify_email_identity() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.verify_email_identity.html>`__.
* Verify an email domain using `verify_domain_identity() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.verify_domain_identity.html>`__.
* List all email addresses using `list_identities() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.listidentities.html>`__.
* List all email domains using `list_identities() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_identities.html>`__.
* Remove an email address using `delete_identity() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_identity.html>`__.
* Remove an email domain using `delete_identity() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_identity.html>`__.
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code.html>`__.

Prerequisite Tasks
==================

To set up and run this example, you must first complete these tasks:

* Configure your AWS credentials, as described in :doc:`quickstart`.

Verifying Email addresses
=========================
SES can send email only from verified email addresses or domains. By verifying an email address, you demonstrate that you're the owner of that address and want to allow SES to send email from that address.

When you run the following code example, SES sends an email to the address you specified. When you (or the recipient of the email) click the link in the email, the address is verified.

To add an email address to your SES account, use the `VerifyEmailIdentity <https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailIdentity.html>`__ operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.verify_email_identity(
      EmailAddress = 'EMAIL_ADDRESS'
    )

    print(response)


Verify an Email Domain
======================

SES can send email only from verified email addresses or domains. By verifying a domain, you demonstrate that you're the owner of that domain. When you verify a domain, you allow SES to send email from any address on that domain.

When you run the following code example, SES provides you with a verification token. You have to add the token to your domain's DNS configuration. For more information, see `Verifying a Domain with Amazon SES <http://aws.amazon.com/documentation/ses/verify-domain-procedure.html>`_.

To add a sending domain to your SES account, use the `VerifyDomainIdentity <https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainIdentity.html>`_ operation.

Example
-------

.. code-block:: python

    mport boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.verify_domain_identity(
      Domain='DOMAIN_NAME'
    )

    print(response)

List Email Addresses
====================

To retrieve a list of email addresses submitted in the current AWS Region, regardless of verification status, use the `ListIdentities <https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html>`__ operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.list_identities(
      IdentityType = 'EmailAddress',
      MaxItems=10
    )

    print(response)

List Email Domains
==================

To retrieve a list of email domains submitted in the current AWS Region, regardless of verification status use the `ListIdentities <https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html>`__ operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.list_identities(
      IdentityType = 'Domain',
      MaxItems=10
    )

    print(response)



Delete an Email Address
=======================

To delete a verified email address from the list of verified identities, use the `DeleteIdentity <https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentity.html>`__ operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.delete_identity(
      Identity = 'EMAIL_ADDRESS'
    )

    print(response)

Delete an Email Domain
======================

To delete a verified email domain from the list of verified identities, use the `DeleteIdentity <https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentity.html>`__ operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.delete_identity(
      Identity = 'DOMAIN_NAME'
    )

    print(response)
