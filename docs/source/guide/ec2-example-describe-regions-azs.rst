.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-describe-regions:   

######################################
Describe Regions and AvailabilityZones
######################################

Amazon EC2 is hosted in multiple locations world-wide. These locations are composed of regions and 
Availability Zones. Each region is a separate geographic area. Each region has multiple, isolated 
locations known as Availability Zones. Amazon EC2 provides you the ability to place resources, such 
as instances, and data in multiple locations.

The example below shows how to:
 
* Describe regions using 
  `describe_regions <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_regions>`_.

* Describe AvailabilityZones using 
  `describe_availability_zones <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_availability_zones>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Describe EC2 Regions and AvailabilityZones
------------------------------------------------------------------------

.. code-block:: python

        import boto3

        ec2 = boto3.client('ec2')

        # Retrieves all regions/endpoints that work with EC2
        response = ec2.describe_regions()
        print('Regions:', response['Regions'])

        # Retrieves availability zones only for region of the ec2 object
        response = ec2.describe_availability_zones()
        print('Availability Zones:', response['AvailabilityZones'])
