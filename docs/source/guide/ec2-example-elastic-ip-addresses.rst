.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto-ec2-example-elastic-ip-addresses:

########################################
Using Elastic IP addresses in Amazon EC2
########################################

This Python example shows you how to:

* Get descriptions of your Elastic IP addresses

* Allocate an Elastic IP address

* Release an Elastic IP address

The scenario
============

An Elastic IP address is a static IP address designed for dynamic cloud computing. An Elastic IP 
address is associated with your AWS account. It is a public IP address, which is reachable from the 
Internet. If your instance does not have a public IP address, you can associate an Elastic IP address 
with your instance to enable communication with the Internet.

In this example, Python code performs several Amazon EC2 operations involving Elastic IP addresses. 
The code uses the AWS SDK for Python to manage IAM access keys using these methods of the EC2
client class:

* `describe_addresses <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_addresses>`_.

* `allocate_address <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.allocate_address>`_.

* `release_address <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.release_address>`_.

For more information about Elastic IP addresses in Amazon EC2, see 
`Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`_ 
in the *Amazon EC2 User Guide for Linux Instances* or 
`Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-ip-addresses-eip.html>`_ in the *Amazon EC2 User Guide for Windows Instances*.
Prerequisite Tasks

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite tasks
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.

Describe Elastic IP addresses
=============================

An Elastic IP address is a static IPv4 address designed for dynamic cloud computing. An Elastic IP 
address is associated with your AWS account. With an Elastic IP address, you can mask the failure of 
an instance or software by rapidly remapping the address to another instance in your account. 

The example below shows how to:
 
* Describe Elastic IP addresses using 
  `describe_addresses <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_addresses>`_.
 
Example
-------

.. code-block:: python

    import boto3


    ec2 = boto3.client('ec2')
    filters = [
        {'Name': 'domain', 'Values': ['vpc']}
    ]
    response = ec2.describe_addresses(Filters=filters)
    print(response)

Allocate and associate an Elastic IP address with an Amazon EC2 instance
========================================================================

An *Elastic IP address* is a static IPv4 address designed for dynamic cloud computing. An Elastic IP 
address is associated with your AWS account. With an Elastic IP address, you can mask the failure of 
an instance or software by rapidly remapping the address to another instance in your account. 

The example below shows how to:
 
* Acquire an Elastic IP address using 
  `allocate_address <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.allocate_address>`_.
 
Example
-------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError

    ec2 = boto3.client('ec2')

    try:
        allocation = ec2.allocate_address(Domain='vpc')
        response = ec2.associate_address(AllocationId=allocation['AllocationId'],
                                         InstanceId='INSTANCE_ID')
        print(response)
    except ClientError as e:
        print(e)


 
Release an Elastic IP address
=============================

After releasing an Elastic IP address, it is released to the IP address pool and might be unavailable 
to you. Be sure to update your DNS records and any servers or devices that communicate with the address. 
If you attempt to release an Elastic IP address that you already released, you'll get an :code:`AuthFailure` 
error if the address is already allocated to another AWS account.

The example below shows how to:
 
* Release the specified Elastic IP address using 
  `release_address <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.release_address>`_.
 
Example
-------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError


    ec2 = boto3.client('ec2')

    try:
        response = ec2.release_address(AllocationId='ALLOCATION_ID')
        print('Address released')
    except ClientError as e:
        print(e)

