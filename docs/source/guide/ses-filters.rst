.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ses-filters:  


###################################
Managing email filters with SES API 
###################################

.. meta::
   :description: Use the Amazon SES API to manage email filters.
   :keywords: SES Python

In addition to sending emails, you can also receive email with Amazon Simple 
Email Service (SES). An IP address filter enables you to optionally specify 
whether to accept or reject mail that originates from an IP address or range 
of IP addresses. For more information, see `Managing IP Address Filters for 
Amazon SES Email 
Receiving <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-ip-filters.html>`__.

The following examples show how to:

* Create an email filter using 
  `create_receipt_filter() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_receipt_filter>`__.
* List all email filters using 
  `list_receipt_filters() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_receipt_filters>`__.
* Remove an email filter using 
  `delete_receipt_filter() <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_receipt_filter>`__.


Prerequisite tasks
==================

To set up and run this example, you must first complete these tasks:

* Configure your AWS credentials, as described in :doc:`quickstart`.


Create an email filter
======================

To allow or block emails from a specific IP address, use the 
`CreateReceiptFilter <https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptFilter.html>`__ 
operation. Provide the IP address or range of addresses and a unique name to 
identify this filter.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    # Create receipt filter
    response = ses.create_receipt_filter(
      Filter = {
        'NAME'     : 'NAME',
        'IpFilter' : {
          'Cidr'   : 'IP_ADDRESS_OR_RANGE',
          'Policy' : 'Allow' 
        }
      }
    )

    print(response)


List all email filters
======================

To list the IP address filters associated with your AWS account in the current 
AWS Region, use the 
`ListReceiptFilters <https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptFilters.html>`__ 
operation.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.list_receipt_filters()

    print(response)


Delete an email filter
======================

To remove an existing filter for a specific IP address use the 
`DeleteReceiptFilter <https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptFilter.html>`__ 
operation. Provide the unique filter name to identify the receipt filter to 
delete.

If you need to change the range of addresses that are filtered, you can delete 
a receipt filter and create a new one.

Example
-------

.. code-block:: python

    import boto3

    # Create SES client
    ses = boto3.client('ses')

    response = ses.delete_receipt_filter(
      FilterName = 'NAME'
    )

    print(response)
