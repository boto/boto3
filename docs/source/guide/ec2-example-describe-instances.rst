.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-describe-instances:   

##################
Describe Instances
##################

An EC2 instance is a virtual server in Amazon's Elastic Compute Cloud (EC2) for running applications 
on the Amazon Web Services (AWS) infrastructure.

The example below shows how to:
 
* Describe one or more EC2 instances using 
  `describe_instances <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_instances>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Describe Instances
------------------------------------------------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError


    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)
