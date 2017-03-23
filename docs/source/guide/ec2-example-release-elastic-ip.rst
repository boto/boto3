.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-describe-regions:   

##########################
Release Elastic IP Address
##########################

After releasing an Elastic IP address, it is released to the IP address pool and might be unavailable 
to you. Be sure to update your DNS records and any servers or devices that communicate with the address. 
If you attempt to release an Elastic IP address that you already released, you'll get an :code:`AuthFailure` 
error if the address is already allocated to another AWS account.

The example below shows how to:
 
* Release the specified Elastic IP address using 
  `release_address <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.release_address>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Release an IP Address
---------------------------------------------------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError


    ec2 = boto3.client('ec2')

    try:
        response = ec2.release_address(AllocationId='ALLOCATION_ID')
        print('Address released')
    except ClientError as e:
        print(e)
