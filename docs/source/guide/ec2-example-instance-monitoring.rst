.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-ec2-examples-monitor-instances:   

###############################
Monitor and Unmonitor Instances
###############################

Enables and disables detailed monitoring for a running instance. If detailed monitoring is not enabled, 
basic monitoring is enabled. For more information, see 
`Monitoring Your Instances and Volumes <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html>`_ 
in the *Amazon Elastic Compute Cloud User Guide*.

The example below shows how to:
 
* Enable detailed monitoring for a running instance using 
  `monitor_instances <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.monitor_instances>`_.

* Disable detailed monitoring for a running instance using 
  `unmonitor_instances <https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.unmonitor_instances>`_.
 
All the example code for the Amazon Web Services (AWS) SDK for Python is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code>`_.
 
Credentials
-----------
 
Before running the example code, configure your AWS credentials, as described in :doc:`/guide/credentials`.
 
Execute the Following Code to Enable and Disable Monitoring for an EC2 Instance
-------------------------------------------------------------------------------

.. code-block:: python

    import sys
    import boto3


    ec2 = boto3.client('ec2')
    if sys.argv[2] == 'ON':
        response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
    else:
        response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
    print(response)
