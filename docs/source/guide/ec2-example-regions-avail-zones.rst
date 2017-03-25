.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto-ec2-example-regions-zones:

##################################################
Describe Amazon EC2 Regions and Availability Zones
##################################################

Amazon EC2 is hosted in multiple locations worldwide. These locations are composed of regions and 
Availability Zones. Each region is a separate geographic area. Each region has multiple, isolated 
locations known as Availability Zones. Amazon EC2 provides the ability to place instances and data 
in multiple locations.

The Scenario
============

In this example, Python code is used to retrieve details about regions and Availability Zones. The code uses the 
AWS SDK for Python to get the daa by using these methods of :code:`boto3.client('ec2')` client class:
 
* Describe regions 

* Describe AvailabilityZones 
 
For more information about regions and Availability Zones, see 
`Regions and Availability Zones <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html>`_ 
in the *Amazon EC2 User Guide for Linux Instances* or 
`Regions and Availability Zones <https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/concepts.html>`_ 
in the *Amazon EC2 User Guide for Windows Instances*.

All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.

Prerequisite Task
=================

To set up and run this example, you must first configure your AWS credentials, as described in :doc:`quickstart`.

Describing Regions and Availability Zones
=========================================

Amazon EC2 is hosted in multiple locations world-wide. These locations are composed of regions and 
Availability Zones. Each region is a separate geographic area. Each region has multiple, isolated 
locations known as Availability Zones. Amazon EC2 provides you the ability to place resources, such 
as instances, and data in multiple locations.

The example below shows how to:
 
* Describe regions using 
  `describe_regions <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_regions>`_.

* Describe AvailabilityZones using 
  `describe_availability_zones <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_availability_zones>`_.
 
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
