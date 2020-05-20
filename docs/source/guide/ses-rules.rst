.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-boto3-ses-rules:  


####################################################
Creating and managing email rules with the SES API 
####################################################

.. meta::
   :description: Use the Amazon SES API to manage email rules.
   :keywords: SES Python

In addition to sending emails, you can also receive email with Amazon Simple 
Email Service (SES). Receipt rules enable you to specify what SES does with 
email it receives for the email addresses or domains you own. A rule can send 
email to other AWS services including but not limited to Amazon S3, Amazon 
SNS, or AWS Lambda.

For more information, see `Managing Receipt Rule Sets for Amazon SES Email 
Receiving <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html>`_ 
and `Managing Receipt Rules for Amazon SES Email 
Receiving <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html>`_.

The following examples show how to:

* Create a receipt rule set using `create_receipt_rule_set()  <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_receipt_rule_set>`_.
* Create a receipt rule using `create_receipt_rule() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_receipt_rule>`_.
* Remove a receipt rule using `delete_receipt_rule() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_receipt_rule>`_.
* Remove a receipt rule set using `delete_receipt_rule_set() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_receipt_rule_set>`_.


Prerequisite tasks
==================

To set up and run this example, you must first complete these tasks:

* Configure your AWS credentials, as described in :doc:`quickstart`.


Create a receipt rule set
==========================

A receipt rule set contains a collection of receipt rules. You must have at 
least one receipt rule set associated with your account before you can create 
a receipt rule. To create a receipt rule set, provide a unique RuleSetName and 
use the 
`CreateReceiptRuleSet <https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRuleSet.html>`_ 
operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.create_receipt_rule_set(
      RuleSetName = 'RULE_SET_NAME',
    )

    print(response)


Create a receipt rule
=====================

Control your incoming email by adding a receipt rule to an existing 
receipt rule set. This example shows you how to create a receipt rule that 
sends incoming messages to an Amazon S3 bucket, but you can also send 
messages to Amazon SNS and AWS Lambda. To create a receipt rule, provide a 
rule and the RuleSetName to the 
`CreateReceiptRule <https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRule.html>`_ 
operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.create_receipt_rule(
      RuleSetName   = 'RULE_SET_NAME',
      Rule          = {
        'Name'      : 'RULE_NAME',
        'Enabled'   : True,
        'TlsPolicy' : 'Optional',
        'Recipients': [
          'EMAIL_ADDRESS',
        ],
        'Actions'   : [
          {
            'S3Action'         : {
              'BucketName'     : 'S3_BUCKET_NAME',
              'ObjectKeyPrefix': 'SES_email'
            }
          }
        ],
      }
    )

    print(response)


Delete a receipt rule set
==========================

Remove a specified receipt rule set that isn't currently disabled. This also 
deletes all of the receipt rules it contains. To delete a receipt rule set, 
provide the RuleSetName to the 
`DeleteReceiptRuleSet <https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRuleSet.html>`_ 
operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.delete_receipt_rule(
      RuleName='RULE_NAME',
      RuleSetName='RULE_SET_NAME'
    )

    print(response)


Delete a receipt rule
=====================

To delete a specified receipt rule, provide the RuleName and RuleSetName to the 
`DeleteReceiptRule <https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRule.html>`_ 
operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.delete_receipt_rule_set(
      RuleSetName = 'RULE_SET_NAME'
    )

    print(response)
