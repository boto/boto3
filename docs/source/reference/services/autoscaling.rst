

***********
AutoScaling
***********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: AutoScaling.Client

  A low-level client representing Auto Scaling::

    
    import boto3
    
    client = boto3.client('autoscaling')

  
  These are the available methods:
  
  *   :py:meth:`~AutoScaling.Client.attach_instances`

  
  *   :py:meth:`~AutoScaling.Client.attach_load_balancer_target_groups`

  
  *   :py:meth:`~AutoScaling.Client.attach_load_balancers`

  
  *   :py:meth:`~AutoScaling.Client.can_paginate`

  
  *   :py:meth:`~AutoScaling.Client.complete_lifecycle_action`

  
  *   :py:meth:`~AutoScaling.Client.create_auto_scaling_group`

  
  *   :py:meth:`~AutoScaling.Client.create_launch_configuration`

  
  *   :py:meth:`~AutoScaling.Client.create_or_update_tags`

  
  *   :py:meth:`~AutoScaling.Client.delete_auto_scaling_group`

  
  *   :py:meth:`~AutoScaling.Client.delete_launch_configuration`

  
  *   :py:meth:`~AutoScaling.Client.delete_lifecycle_hook`

  
  *   :py:meth:`~AutoScaling.Client.delete_notification_configuration`

  
  *   :py:meth:`~AutoScaling.Client.delete_policy`

  
  *   :py:meth:`~AutoScaling.Client.delete_scheduled_action`

  
  *   :py:meth:`~AutoScaling.Client.delete_tags`

  
  *   :py:meth:`~AutoScaling.Client.describe_account_limits`

  
  *   :py:meth:`~AutoScaling.Client.describe_adjustment_types`

  
  *   :py:meth:`~AutoScaling.Client.describe_auto_scaling_groups`

  
  *   :py:meth:`~AutoScaling.Client.describe_auto_scaling_instances`

  
  *   :py:meth:`~AutoScaling.Client.describe_auto_scaling_notification_types`

  
  *   :py:meth:`~AutoScaling.Client.describe_launch_configurations`

  
  *   :py:meth:`~AutoScaling.Client.describe_lifecycle_hook_types`

  
  *   :py:meth:`~AutoScaling.Client.describe_lifecycle_hooks`

  
  *   :py:meth:`~AutoScaling.Client.describe_load_balancer_target_groups`

  
  *   :py:meth:`~AutoScaling.Client.describe_load_balancers`

  
  *   :py:meth:`~AutoScaling.Client.describe_metric_collection_types`

  
  *   :py:meth:`~AutoScaling.Client.describe_notification_configurations`

  
  *   :py:meth:`~AutoScaling.Client.describe_policies`

  
  *   :py:meth:`~AutoScaling.Client.describe_scaling_activities`

  
  *   :py:meth:`~AutoScaling.Client.describe_scaling_process_types`

  
  *   :py:meth:`~AutoScaling.Client.describe_scheduled_actions`

  
  *   :py:meth:`~AutoScaling.Client.describe_tags`

  
  *   :py:meth:`~AutoScaling.Client.describe_termination_policy_types`

  
  *   :py:meth:`~AutoScaling.Client.detach_instances`

  
  *   :py:meth:`~AutoScaling.Client.detach_load_balancer_target_groups`

  
  *   :py:meth:`~AutoScaling.Client.detach_load_balancers`

  
  *   :py:meth:`~AutoScaling.Client.disable_metrics_collection`

  
  *   :py:meth:`~AutoScaling.Client.enable_metrics_collection`

  
  *   :py:meth:`~AutoScaling.Client.enter_standby`

  
  *   :py:meth:`~AutoScaling.Client.execute_policy`

  
  *   :py:meth:`~AutoScaling.Client.exit_standby`

  
  *   :py:meth:`~AutoScaling.Client.generate_presigned_url`

  
  *   :py:meth:`~AutoScaling.Client.get_paginator`

  
  *   :py:meth:`~AutoScaling.Client.get_waiter`

  
  *   :py:meth:`~AutoScaling.Client.put_lifecycle_hook`

  
  *   :py:meth:`~AutoScaling.Client.put_notification_configuration`

  
  *   :py:meth:`~AutoScaling.Client.put_scaling_policy`

  
  *   :py:meth:`~AutoScaling.Client.put_scheduled_update_group_action`

  
  *   :py:meth:`~AutoScaling.Client.record_lifecycle_action_heartbeat`

  
  *   :py:meth:`~AutoScaling.Client.resume_processes`

  
  *   :py:meth:`~AutoScaling.Client.set_desired_capacity`

  
  *   :py:meth:`~AutoScaling.Client.set_instance_health`

  
  *   :py:meth:`~AutoScaling.Client.set_instance_protection`

  
  *   :py:meth:`~AutoScaling.Client.suspend_processes`

  
  *   :py:meth:`~AutoScaling.Client.terminate_instance_in_auto_scaling_group`

  
  *   :py:meth:`~AutoScaling.Client.update_auto_scaling_group`

  

  .. py:method:: attach_instances(**kwargs)

    

    Attaches one or more EC2 instances to the specified Auto Scaling group.

     

    When you attach instances, Auto Scaling increases the desired capacity of the group by the number of instances being attached. If the number of instances being attached plus the desired capacity of the group exceeds the maximum size of the group, the operation fails.

     

    If there is a Classic Load Balancer attached to your Auto Scaling group, the instances are also registered with the load balancer. If there are target groups attached to your Auto Scaling group, the instances are also registered with the target groups.

     

    For more information, see `Attach EC2 Instances to Your Auto Scaling Group <http://docs.aws.amazon.com/autoscaling/latest/userguide/attach-instance-asg.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/AttachInstances>`_    


    **Request Syntax** 
    ::

      response = client.attach_instances(
          InstanceIds=[
              'string',
          ],
          AutoScalingGroupName='string'
      )
    :type InstanceIds: list
    :param InstanceIds: 

      One or more instance IDs.

      

    
      - *(string) --* 

      
  
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    
    :returns: None

    **Examples** 

    This example attaches the specified instance to the specified Auto Scaling group.
    ::

      response = client.attach_instances(
          AutoScalingGroupName='my-auto-scaling-group',
          InstanceIds=[
              'i-93633f9b',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: attach_load_balancer_target_groups(**kwargs)

    

    Attaches one or more target groups to the specified Auto Scaling group.

     

    To describe the target groups for an Auto Scaling group, use  DescribeLoadBalancerTargetGroups . To detach the target group from the Auto Scaling group, use  DetachLoadBalancerTargetGroups .

     

    For more information, see `Attach a Load Balancer to Your Auto Scaling Group <http://docs.aws.amazon.com/autoscaling/latest/userguide/attach-load-balancer-asg.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups>`_    


    **Request Syntax** 
    ::

      response = client.attach_load_balancer_target_groups(
          AutoScalingGroupName='string',
          TargetGroupARNs=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type TargetGroupARNs: list
    :param TargetGroupARNs: **[REQUIRED]** 

      The Amazon Resource Names (ARN) of the target groups.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example attaches the specified target group to the specified Auto Scaling group.
    ::

      response = client.attach_load_balancer_target_groups(
          AutoScalingGroupName='my-auto-scaling-group',
          TargetGroupARNs=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: attach_load_balancers(**kwargs)

    

    Attaches one or more Classic Load Balancers to the specified Auto Scaling group.

     

    To attach an Application Load Balancer instead, see  AttachLoadBalancerTargetGroups .

     

    To describe the load balancers for an Auto Scaling group, use  DescribeLoadBalancers . To detach the load balancer from the Auto Scaling group, use  DetachLoadBalancers .

     

    For more information, see `Attach a Load Balancer to Your Auto Scaling Group <http://docs.aws.amazon.com/autoscaling/latest/userguide/attach-load-balancer-asg.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/AttachLoadBalancers>`_    


    **Request Syntax** 
    ::

      response = client.attach_load_balancers(
          AutoScalingGroupName='string',
          LoadBalancerNames=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: **[REQUIRED]** 

      One or more load balancer names.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example attaches the specified load balancer to the specified Auto Scaling group.
    ::

      response = client.attach_load_balancers(
          AutoScalingGroupName='my-auto-scaling-group',
          LoadBalancerNames=[
              'my-load-balancer',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: can_paginate(operation_name)

        
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name.  This is the same name
        as the method name on the client.  For example, if the
        method name is ``create_foo``, and you'd normally invoke the
        operation as ``client.create_foo(**kwargs)``, if the
        ``create_foo`` operation can be paginated, you can use the
        call ``client.get_paginator("create_foo")``.
    
    :return: ``True`` if the operation can be paginated,
        ``False`` otherwise.


  .. py:method:: complete_lifecycle_action(**kwargs)

    

    Completes the lifecycle action for the specified token or instance with the specified result.

     

    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:

     

     
    * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Auto Scaling launches or terminates instances. 
     
    * (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Auto Scaling to publish lifecycle notifications to the target. 
     
    * Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate. 
     
    * If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state. 
     
    * **If you finish before the timeout period ends, complete the lifecycle action.**   
     

     

    For more information, see `Auto Scaling Lifecycle <http://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroupLifecycle.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/CompleteLifecycleAction>`_    


    **Request Syntax** 
    ::

      response = client.complete_lifecycle_action(
          LifecycleHookName='string',
          AutoScalingGroupName='string',
          LifecycleActionToken='string',
          LifecycleActionResult='string',
          InstanceId='string'
      )
    :type LifecycleHookName: string
    :param LifecycleHookName: **[REQUIRED]** 

      The name of the lifecycle hook.

      

    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type LifecycleActionToken: string
    :param LifecycleActionToken: 

      A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.

      

    
    :type LifecycleActionResult: string
    :param LifecycleActionResult: **[REQUIRED]** 

      The action for the group to take. This parameter can be either ``CONTINUE`` or ``ABANDON`` .

      

    
    :type InstanceId: string
    :param InstanceId: 

      The ID of the instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example notifies Auto Scaling that the specified lifecycle action is complete so that it can finish launching or terminating the instance.
    ::

      response = client.complete_lifecycle_action(
          AutoScalingGroupName='my-auto-scaling-group',
          LifecycleActionResult='CONTINUE',
          LifecycleActionToken='bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635',
          LifecycleHookName='my-lifecycle-hook',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_auto_scaling_group(**kwargs)

    

    Creates an Auto Scaling group with the specified name and attributes.

     

    If you exceed your maximum limit of Auto Scaling groups, which by default is 20 per region, the call fails. For information about viewing and updating this limit, see  DescribeAccountLimits .

     

    For more information, see `Auto Scaling Groups <http://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroup.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/CreateAutoScalingGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_auto_scaling_group(
          AutoScalingGroupName='string',
          LaunchConfigurationName='string',
          LaunchTemplate={
              'LaunchTemplateId': 'string',
              'LaunchTemplateName': 'string',
              'Version': 'string'
          },
          InstanceId='string',
          MinSize=123,
          MaxSize=123,
          DesiredCapacity=123,
          DefaultCooldown=123,
          AvailabilityZones=[
              'string',
          ],
          LoadBalancerNames=[
              'string',
          ],
          TargetGroupARNs=[
              'string',
          ],
          HealthCheckType='string',
          HealthCheckGracePeriod=123,
          PlacementGroup='string',
          VPCZoneIdentifier='string',
          TerminationPolicies=[
              'string',
          ],
          NewInstancesProtectedFromScaleIn=True|False,
          LifecycleHookSpecificationList=[
              {
                  'LifecycleHookName': 'string',
                  'LifecycleTransition': 'string',
                  'NotificationMetadata': 'string',
                  'HeartbeatTimeout': 123,
                  'DefaultResult': 'string',
                  'NotificationTargetARN': 'string',
                  'RoleARN': 'string'
              },
          ],
          Tags=[
              {
                  'ResourceId': 'string',
                  'ResourceType': 'string',
                  'Key': 'string',
                  'Value': 'string',
                  'PropagateAtLaunch': True|False
              },
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group. This name must be unique within the scope of your AWS account.

      

    
    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: 

      The name of the launch configuration. You must specify one of the following: a launch configuration, a launch template, or an EC2 instance.

      

    
    :type LaunchTemplate: dict
    :param LaunchTemplate: 

      The launch template to use to launch instances. You must specify one of the following: a launch template, a launch configuration, or an EC2 instance.

      

    
      - **LaunchTemplateId** *(string) --* 

        The ID of the launch template. You must specify either a template ID or a template name.

        

      
      - **LaunchTemplateName** *(string) --* 

        The name of the launch template. You must specify either a template name or a template ID.

        

      
      - **Version** *(string) --* 

        The version number. By default, the default version of the launch template is used.

        

      
    
    :type InstanceId: string
    :param InstanceId: 

      The ID of the instance used to create a launch configuration for the group. You must specify one of the following: an EC2 instance, a launch configuration, or a launch template.

       

      When you specify an ID of an instance, Auto Scaling creates a new launch configuration and associates it with the group. This launch configuration derives its attributes from the specified instance, with the exception of the block device mapping.

       

      For more information, see `Create an Auto Scaling Group Using an EC2 Instance <http://docs.aws.amazon.com/autoscaling/latest/userguide/create-asg-from-instance.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type MinSize: integer
    :param MinSize: **[REQUIRED]** 

      The minimum size of the group.

      

    
    :type MaxSize: integer
    :param MaxSize: **[REQUIRED]** 

      The maximum size of the group.

      

    
    :type DesiredCapacity: integer
    :param DesiredCapacity: 

      The number of EC2 instances that should be running in the group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity, the default is the minimum size of the group.

      

    
    :type DefaultCooldown: integer
    :param DefaultCooldown: 

      The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default is 300.

       

      For more information, see `Auto Scaling Cooldowns <http://docs.aws.amazon.com/autoscaling/latest/userguide/Cooldown.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type AvailabilityZones: list
    :param AvailabilityZones: 

      One or more Availability Zones for the group. This parameter is optional if you specify one or more subnets.

      

    
      - *(string) --* 

      
  
    :type LoadBalancerNames: list
    :param LoadBalancerNames: 

      One or more Classic Load Balancers. To specify an Application Load Balancer, use ``TargetGroupARNs`` instead.

       

      For more information, see `Using a Load Balancer With an Auto Scaling Group <http://docs.aws.amazon.com/autoscaling/latest/userguide/create-asg-from-instance.html>`__ in the *Auto Scaling User Guide* .

      

    
      - *(string) --* 

      
  
    :type TargetGroupARNs: list
    :param TargetGroupARNs: 

      The Amazon Resource Names (ARN) of the target groups.

      

    
      - *(string) --* 

      
  
    :type HealthCheckType: string
    :param HealthCheckType: 

      The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` .

       

      By default, health checks use Amazon EC2 instance status checks to determine the health of an instance. For more information, see `Health Checks <http://docs.aws.amazon.com/autoscaling/latest/userguide/healthcheck.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type HealthCheckGracePeriod: integer
    :param HealthCheckGracePeriod: 

      The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service. During this time, any health check failures for the instance are ignored. The default is 0.

       

      This parameter is required if you are adding an ``ELB`` health check.

       

      For more information, see `Health Checks <http://docs.aws.amazon.com/autoscaling/latest/userguide/healthcheck.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type PlacementGroup: string
    :param PlacementGroup: 

      The name of the placement group into which you'll launch your instances, if any. For more information, see `Placement Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
    :type VPCZoneIdentifier: string
    :param VPCZoneIdentifier: 

      A comma-separated list of subnet identifiers for your virtual private cloud (VPC).

       

      If you specify subnets and Availability Zones with this call, ensure that the subnets' Availability Zones match the Availability Zones specified.

       

      For more information, see `Launching Auto Scaling Instances in a VPC <http://docs.aws.amazon.com/autoscaling/latest/userguide/asg-in-vpc.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type TerminationPolicies: list
    :param TerminationPolicies: 

      One or more termination policies used to select the instance to terminate. These policies are executed in the order that they are listed.

       

      For more information, see `Controlling Which Instances Auto Scaling Terminates During Scale In <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-termination.html>`__ in the *Auto Scaling User Guide* .

      

    
      - *(string) --* 

      
  
    :type NewInstancesProtectedFromScaleIn: boolean
    :param NewInstancesProtectedFromScaleIn: 

      Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.

      

    
    :type LifecycleHookSpecificationList: list
    :param LifecycleHookSpecificationList: 

      One or more lifecycle hooks.

      

    
      - *(dict) --* 

        Describes a lifecycle hook, which tells Auto Scaling that you want to perform an action whenever it launches instances or whenever it terminates instances.

         

        For more information, see `Auto Scaling Lifecycle Hooks <http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html>`__ in the *Auto Scaling User Guide* .

        

      
        - **LifecycleHookName** *(string) --* **[REQUIRED]** 

          The name of the lifecycle hook.

          

        
        - **LifecycleTransition** *(string) --* **[REQUIRED]** 

          The state of the EC2 instance to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see  DescribeLifecycleHookTypes .

          

        
        - **NotificationMetadata** *(string) --* 

          Additional information that you want to include any time Auto Scaling sends a message to the notification target.

          

        
        - **HeartbeatTimeout** *(integer) --* 

          The maximum time, in seconds, that can elapse before the lifecycle hook times out. If the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling  RecordLifecycleActionHeartbeat .

          

        
        - **DefaultResult** *(string) --* 

          Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are ``CONTINUE`` and ``ABANDON`` .

          

        
        - **NotificationTargetARN** *(string) --* 

          The ARN of the target that Auto Scaling sends notifications to when an instance is in the transition state for the lifecycle hook. The notification target can be either an SQS queue or an SNS topic.

          

        
        - **RoleARN** *(string) --* 

          The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

          

        
      
  
    :type Tags: list
    :param Tags: 

      One or more tags.

       

      For more information, see `Tagging Auto Scaling Groups and Instances <http://docs.aws.amazon.com/autoscaling/latest/userguide/autoscaling-tagging.html>`__ in the *Auto Scaling User Guide* .

      

    
      - *(dict) --* 

        Describes a tag for an Auto Scaling group.

        

      
        - **ResourceId** *(string) --* 

          The name of the group.

          

        
        - **ResourceType** *(string) --* 

          The type of resource. The only supported value is ``auto-scaling-group`` .

          

        
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* 

          The tag value.

          

        
        - **PropagateAtLaunch** *(boolean) --* 

          Determines whether the tag is added to new instances as they are launched in the group.

          

        
      
  
    
    :returns: None

    **Examples** 

    This example creates an Auto Scaling group.
    ::

      response = client.create_auto_scaling_group(
          AutoScalingGroupName='my-auto-scaling-group',
          LaunchConfigurationName='my-launch-config',
          MaxSize=3,
          MinSize=1,
          VPCZoneIdentifier='subnet-4176792c',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example creates an Auto Scaling group and attaches the specified Classic Load Balancer.
    ::

      response = client.create_auto_scaling_group(
          AutoScalingGroupName='my-auto-scaling-group',
          AvailabilityZones=[
              'us-west-2c',
          ],
          HealthCheckGracePeriod=120,
          HealthCheckType='ELB',
          LaunchConfigurationName='my-launch-config',
          LoadBalancerNames=[
              'my-load-balancer',
          ],
          MaxSize=3,
          MinSize=1,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example creates an Auto Scaling group and attaches the specified target group.
    ::

      response = client.create_auto_scaling_group(
          AutoScalingGroupName='my-auto-scaling-group',
          HealthCheckGracePeriod=120,
          HealthCheckType='ELB',
          LaunchConfigurationName='my-launch-config',
          MaxSize=3,
          MinSize=1,
          TargetGroupARNs=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
          ],
          VPCZoneIdentifier='subnet-4176792c, subnet-65ea5f08',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_launch_configuration(**kwargs)

    

    Creates a launch configuration.

     

    If you exceed your maximum limit of launch configurations, which by default is 100 per region, the call fails. For information about viewing and updating this limit, see  DescribeAccountLimits .

     

    For more information, see `Launch Configurations <http://docs.aws.amazon.com/autoscaling/latest/userguide/LaunchConfiguration.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/CreateLaunchConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.create_launch_configuration(
          LaunchConfigurationName='string',
          ImageId='string',
          KeyName='string',
          SecurityGroups=[
              'string',
          ],
          ClassicLinkVPCId='string',
          ClassicLinkVPCSecurityGroups=[
              'string',
          ],
          UserData='string',
          InstanceId='string',
          InstanceType='string',
          KernelId='string',
          RamdiskId='string',
          BlockDeviceMappings=[
              {
                  'VirtualName': 'string',
                  'DeviceName': 'string',
                  'Ebs': {
                      'SnapshotId': 'string',
                      'VolumeSize': 123,
                      'VolumeType': 'string',
                      'DeleteOnTermination': True|False,
                      'Iops': 123,
                      'Encrypted': True|False
                  },
                  'NoDevice': True|False
              },
          ],
          InstanceMonitoring={
              'Enabled': True|False
          },
          SpotPrice='string',
          IamInstanceProfile='string',
          EbsOptimized=True|False,
          AssociatePublicIpAddress=True|False,
          PlacementTenancy='string'
      )
    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: **[REQUIRED]** 

      The name of the launch configuration. This name must be unique within the scope of your AWS account.

      

    
    :type ImageId: string
    :param ImageId: 

      The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances.

       

      If you do not specify ``InstanceId`` , you must specify ``ImageId`` .

       

      For more information, see `Finding an AMI <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
    :type KeyName: string
    :param KeyName: 

      The name of the key pair. For more information, see `Amazon EC2 Key Pairs <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
    :type SecurityGroups: list
    :param SecurityGroups: 

      One or more security groups with which to associate the instances.

       

      If your instances are launched in EC2-Classic, you can either specify security group names or the security group IDs. For more information about security groups for EC2-Classic, see `Amazon EC2 Security Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

       

      If your instances are launched into a VPC, specify security group IDs. For more information, see `Security Groups for Your VPC <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ in the *Amazon Virtual Private Cloud User Guide* .

      

    
      - *(string) --* 

      
  
    :type ClassicLinkVPCId: string
    :param ClassicLinkVPCId: 

      The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. This parameter is supported only if you are launching EC2-Classic instances. For more information, see `ClassicLink <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
    :type ClassicLinkVPCSecurityGroups: list
    :param ClassicLinkVPCSecurityGroups: 

      The IDs of one or more security groups for the specified ClassicLink-enabled VPC. This parameter is required if you specify a ClassicLink-enabled VPC, and is not supported otherwise. For more information, see `ClassicLink <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
      - *(string) --* 

      
  
    :type UserData: string
    :param UserData: 

      The user data to make available to the launched EC2 instances. For more information, see `Instance Metadata and User Data <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

            **This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.**


    
    :type InstanceId: string
    :param InstanceId: 

      The ID of the instance to use to create the launch configuration. The new launch configuration derives attributes from the instance, with the exception of the block device mapping.

       

      If you do not specify ``InstanceId`` , you must specify both ``ImageId`` and ``InstanceType`` .

       

      To create a launch configuration with a block device mapping or override any other instance attributes, specify them as part of the same request.

       

      For more information, see `Create a Launch Configuration Using an EC2 Instance <http://docs.aws.amazon.com/autoscaling/latest/userguide/create-lc-with-instanceID.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type InstanceType: string
    :param InstanceType: 

      The instance type of the EC2 instance.

       

      If you do not specify ``InstanceId`` , you must specify ``InstanceType`` .

       

      For information about available instance types, see `Available Instance Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__ in the *Amazon Elastic Compute Cloud User Guide.*  

      

    
    :type KernelId: string
    :param KernelId: 

      The ID of the kernel associated with the AMI.

      

    
    :type RamdiskId: string
    :param RamdiskId: 

      The ID of the RAM disk associated with the AMI.

      

    
    :type BlockDeviceMappings: list
    :param BlockDeviceMappings: 

      One or more mappings that specify how block devices are exposed to the instance. For more information, see `Block Device Mapping <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
      - *(dict) --* 

        Describes a block device mapping.

        

      
        - **VirtualName** *(string) --* 

          The name of the virtual device (for example, ``ephemeral0`` ).

          

        
        - **DeviceName** *(string) --* **[REQUIRED]** 

          The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).

          

        
        - **Ebs** *(dict) --* 

          The information about the Amazon EBS volume.

          

        
          - **SnapshotId** *(string) --* 

            The ID of the snapshot.

            

          
          - **VolumeSize** *(integer) --* 

            The volume size, in GiB. For ``standard`` volumes, specify a value from 1 to 1,024. For ``io1`` volumes, specify a value from 4 to 16,384. For ``gp2`` volumes, specify a value from 1 to 16,384. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.

             

            Default: If you create a volume from a snapshot and you don't specify a volume size, the default is the snapshot size.

            

          
          - **VolumeType** *(string) --* 

            The volume type. For more information, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

             

            Valid values: ``standard`` | ``io1`` | ``gp2``  

             

            Default: ``standard``  

            

          
          - **DeleteOnTermination** *(boolean) --* 

            Indicates whether the volume is deleted on instance termination.

             

            Default: ``true``  

            

          
          - **Iops** *(integer) --* 

            The number of I/O operations per second (IOPS) to provision for the volume.

             

            Constraint: Required when the volume type is ``io1`` .

            

          
          - **Encrypted** *(boolean) --* 

            Indicates whether the volume should be encrypted. Encrypted EBS volumes must be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or an unencrypted volume from an encrypted snapshot. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

            

          
        
        - **NoDevice** *(boolean) --* 

          Suppresses a device mapping.

           

          If this parameter is true for the root device, the instance might fail the EC2 health check. Auto Scaling launches a replacement instance if the instance fails the health check.

          

        
      
  
    :type InstanceMonitoring: dict
    :param InstanceMonitoring: 

      Enables detailed monitoring (``true`` ) or basic monitoring (``false`` ) for the Auto Scaling instances. The default is ``true`` .

      

    
      - **Enabled** *(boolean) --* 

        If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

        

      
    
    :type SpotPrice: string
    :param SpotPrice: 

      The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. For more information, see `Launching Spot Instances in Your Auto Scaling Group <http://docs.aws.amazon.com/autoscaling/latest/userguide/US-SpotInstances.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type IamInstanceProfile: string
    :param IamInstanceProfile: 

      The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.

       

      EC2 instances launched with an IAM role will automatically have AWS security credentials available. You can use IAM roles with Auto Scaling to automatically enable applications running on your EC2 instances to securely access other AWS resources. For more information, see `Launch Auto Scaling Instances with an IAM Role <http://docs.aws.amazon.com/autoscaling/latest/userguide/us-iam-role.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type EbsOptimized: boolean
    :param EbsOptimized: 

      Indicates whether the instance is optimized for Amazon EBS I/O. By default, the instance is not optimized for EBS I/O. The optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization is not available with all instance types. Additional usage charges apply. For more information, see `Amazon EBS-Optimized Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
    :type AssociatePublicIpAddress: boolean
    :param AssociatePublicIpAddress: 

      Used for groups that launch instances into a virtual private cloud (VPC). Specifies whether to assign a public IP address to each instance. For more information, see `Launching Auto Scaling Instances in a VPC <http://docs.aws.amazon.com/autoscaling/latest/userguide/asg-in-vpc.html>`__ in the *Auto Scaling User Guide* .

       

      If you specify this parameter, be sure to specify at least one subnet when you create your group.

       

      Default: If the instance is launched into a default subnet, the default is ``true`` . If the instance is launched into a nondefault subnet, the default is ``false`` . For more information, see `Supported Platforms <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
    :type PlacementTenancy: string
    :param PlacementTenancy: 

      The tenancy of the instance. An instance with a tenancy of ``dedicated`` runs on single-tenant hardware and can only be launched into a VPC.

       

      You must set the value of this parameter to ``dedicated`` if want to launch Dedicated Instances into a shared tenancy VPC (VPC with instance placement tenancy attribute set to ``default`` ).

       

      If you specify this parameter, be sure to specify at least one subnet when you create your group.

       

      For more information, see `Launching Auto Scaling Instances in a VPC <http://docs.aws.amazon.com/autoscaling/latest/userguide/asg-in-vpc.html>`__ in the *Auto Scaling User Guide* .

       

      Valid values: ``default`` | ``dedicated``  

      

    
    
    :returns: None

    **Examples** 

    This example creates a launch configuration.
    ::

      response = client.create_launch_configuration(
          IamInstanceProfile='my-iam-role',
          ImageId='ami-12345678',
          InstanceType='m3.medium',
          LaunchConfigurationName='my-launch-config',
          SecurityGroups=[
              'sg-eb2af88e',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_or_update_tags(**kwargs)

    

    Creates or updates tags for the specified Auto Scaling group.

     

    When you specify a tag with a key that already exists, the operation overwrites the previous tag definition, and you do not get an error message.

     

    For more information, see `Tagging Auto Scaling Groups and Instances <http://docs.aws.amazon.com/autoscaling/latest/userguide/autoscaling-tagging.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/CreateOrUpdateTags>`_    


    **Request Syntax** 
    ::

      response = client.create_or_update_tags(
          Tags=[
              {
                  'ResourceId': 'string',
                  'ResourceType': 'string',
                  'Key': 'string',
                  'Value': 'string',
                  'PropagateAtLaunch': True|False
              },
          ]
      )
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      One or more tags.

      

    
      - *(dict) --* 

        Describes a tag for an Auto Scaling group.

        

      
        - **ResourceId** *(string) --* 

          The name of the group.

          

        
        - **ResourceType** *(string) --* 

          The type of resource. The only supported value is ``auto-scaling-group`` .

          

        
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* 

          The tag value.

          

        
        - **PropagateAtLaunch** *(boolean) --* 

          Determines whether the tag is added to new instances as they are launched in the group.

          

        
      
  
    
    :returns: None

    **Examples** 

    This example adds two tags to the specified Auto Scaling group.
    ::

      response = client.create_or_update_tags(
          Tags=[
              {
                  'Key': 'Role',
                  'PropagateAtLaunch': True,
                  'ResourceId': 'my-auto-scaling-group',
                  'ResourceType': 'auto-scaling-group',
                  'Value': 'WebServer',
              },
              {
                  'Key': 'Dept',
                  'PropagateAtLaunch': True,
                  'ResourceId': 'my-auto-scaling-group',
                  'ResourceType': 'auto-scaling-group',
                  'Value': 'Research',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_auto_scaling_group(**kwargs)

    

    Deletes the specified Auto Scaling group.

     

    If the group has instances or scaling activities in progress, you must specify the option to force the deletion in order for it to succeed.

     

    If the group has policies, deleting the group deletes the policies, the underlying alarm actions, and any alarm that no longer has an associated action.

     

    To remove instances from the Auto Scaling group before deleting it, call  DetachInstances with the list of instances and the option to decrement the desired capacity so that Auto Scaling does not launch replacement instances.

     

    To terminate all instances before deleting the Auto Scaling group, call  UpdateAutoScalingGroup and set the minimum size and desired capacity of the Auto Scaling group to zero.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteAutoScalingGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_auto_scaling_group(
          AutoScalingGroupName='string',
          ForceDelete=True|False
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type ForceDelete: boolean
    :param ForceDelete: 

      Specifies that the group will be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This parameter also deletes any lifecycle actions associated with the group.

      

    
    
    :returns: None

    **Examples** 

    This example deletes the specified Auto Scaling group.
    ::

      response = client.delete_auto_scaling_group(
          AutoScalingGroupName='my-auto-scaling-group',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example deletes the specified Auto Scaling group and all its instances.
    ::

      response = client.delete_auto_scaling_group(
          AutoScalingGroupName='my-auto-scaling-group',
          ForceDelete=True,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_launch_configuration(**kwargs)

    

    Deletes the specified launch configuration.

     

    The launch configuration must not be attached to an Auto Scaling group. When this call completes, the launch configuration is no longer available for use.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteLaunchConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.delete_launch_configuration(
          LaunchConfigurationName='string'
      )
    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: **[REQUIRED]** 

      The name of the launch configuration.

      

    
    
    :returns: None

    **Examples** 

    This example deletes the specified launch configuration.
    ::

      response = client.delete_launch_configuration(
          LaunchConfigurationName='my-launch-config',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_lifecycle_hook(**kwargs)

    

    Deletes the specified lifecycle hook.

     

    If there are any outstanding lifecycle actions, they are completed first (``ABANDON`` for launching instances, ``CONTINUE`` for terminating instances).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteLifecycleHook>`_    


    **Request Syntax** 
    ::

      response = client.delete_lifecycle_hook(
          LifecycleHookName='string',
          AutoScalingGroupName='string'
      )
    :type LifecycleHookName: string
    :param LifecycleHookName: **[REQUIRED]** 

      The name of the lifecycle hook.

      

    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deletes the specified lifecycle hook.
    ::

      response = client.delete_lifecycle_hook(
          AutoScalingGroupName='my-auto-scaling-group',
          LifecycleHookName='my-lifecycle-hook',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_notification_configuration(**kwargs)

    

    Deletes the specified notification.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteNotificationConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.delete_notification_configuration(
          AutoScalingGroupName='string',
          TopicARN='string'
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type TopicARN: string
    :param TopicARN: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.

      

    
    
    :returns: None

    **Examples** 

    This example deletes the specified notification from the specified Auto Scaling group.
    ::

      response = client.delete_notification_configuration(
          AutoScalingGroupName='my-auto-scaling-group',
          TopicARN='arn:aws:sns:us-west-2:123456789012:my-sns-topic',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_policy(**kwargs)

    

    Deletes the specified Auto Scaling policy.

     

    Deleting a policy deletes the underlying alarm action, but does not delete the alarm, even if it no longer has an associated action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeletePolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_policy(
          AutoScalingGroupName='string',
          PolicyName='string'
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: 

      The name of the Auto Scaling group.

      

    
    :type PolicyName: string
    :param PolicyName: **[REQUIRED]** 

      The name or Amazon Resource Name (ARN) of the policy.

      

    
    
    :returns: None

    **Examples** 

    This example deletes the specified Auto Scaling policy.
    ::

      response = client.delete_policy(
          AutoScalingGroupName='my-auto-scaling-group',
          PolicyName='ScaleIn',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_scheduled_action(**kwargs)

    

    Deletes the specified scheduled action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteScheduledAction>`_    


    **Request Syntax** 
    ::

      response = client.delete_scheduled_action(
          AutoScalingGroupName='string',
          ScheduledActionName='string'
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type ScheduledActionName: string
    :param ScheduledActionName: **[REQUIRED]** 

      The name of the action to delete.

      

    
    
    :returns: None

    **Examples** 

    This example deletes the specified scheduled action from the specified Auto Scaling group.
    ::

      response = client.delete_scheduled_action(
          AutoScalingGroupName='my-auto-scaling-group',
          ScheduledActionName='my-scheduled-action',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_tags(**kwargs)

    

    Deletes the specified tags.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteTags>`_    


    **Request Syntax** 
    ::

      response = client.delete_tags(
          Tags=[
              {
                  'ResourceId': 'string',
                  'ResourceType': 'string',
                  'Key': 'string',
                  'Value': 'string',
                  'PropagateAtLaunch': True|False
              },
          ]
      )
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      One or more tags.

      

    
      - *(dict) --* 

        Describes a tag for an Auto Scaling group.

        

      
        - **ResourceId** *(string) --* 

          The name of the group.

          

        
        - **ResourceType** *(string) --* 

          The type of resource. The only supported value is ``auto-scaling-group`` .

          

        
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* 

          The tag value.

          

        
        - **PropagateAtLaunch** *(boolean) --* 

          Determines whether the tag is added to new instances as they are launched in the group.

          

        
      
  
    
    :returns: None

    **Examples** 

    This example deletes the specified tag from the specified Auto Scaling group.
    ::

      response = client.delete_tags(
          Tags=[
              {
                  'Key': 'Dept',
                  'ResourceId': 'my-auto-scaling-group',
                  'ResourceType': 'auto-scaling-group',
                  'Value': 'Research',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_account_limits()

    

    Describes the current Auto Scaling resource limits for your AWS account.

     

    For information about requesting an increase in these limits, see `AWS Service Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>`__ in the *Amazon Web Services General Reference* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAccountLimits>`_    


    **Request Syntax** 

    ::

      response = client.describe_account_limits()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MaxNumberOfAutoScalingGroups': 123,
            'MaxNumberOfLaunchConfigurations': 123,
            'NumberOfAutoScalingGroups': 123,
            'NumberOfLaunchConfigurations': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **MaxNumberOfAutoScalingGroups** *(integer) --* 

          The maximum number of groups allowed for your AWS account. The default limit is 20 per region.

          
        

        - **MaxNumberOfLaunchConfigurations** *(integer) --* 

          The maximum number of launch configurations allowed for your AWS account. The default limit is 100 per region.

          
        

        - **NumberOfAutoScalingGroups** *(integer) --* 

          The current number of groups for your AWS account.

          
        

        - **NumberOfLaunchConfigurations** *(integer) --* 

          The current number of launch configurations for your AWS account.

          
    

    **Examples** 

    This example describes the Auto Scaling limits for your AWS account.
    ::

      response = client.describe_account_limits(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'MaxNumberOfAutoScalingGroups': 20,
          'MaxNumberOfLaunchConfigurations': 100,
          'NumberOfAutoScalingGroups': 3,
          'NumberOfLaunchConfigurations': 5,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_adjustment_types()

    

    Describes the policy adjustment types for use with  PutScalingPolicy .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAdjustmentTypes>`_    


    **Request Syntax** 

    ::

      response = client.describe_adjustment_types()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AdjustmentTypes': [
                {
                    'AdjustmentType': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AdjustmentTypes** *(list) --* 

          The policy adjustment types.

          
          

          - *(dict) --* 

            Describes a policy adjustment type.

             

            For more information, see `Dynamic Scaling <http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html>`__ in the *Auto Scaling User Guide* .

            
            

            - **AdjustmentType** *(string) --* 

              The policy adjustment type. The valid values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .

              
        
      
    

    **Examples** 

    This example describes the available adjustment types.
    ::

      response = client.describe_adjustment_types(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AdjustmentTypes': [
              {
                  'AdjustmentType': 'ChangeInCapacity',
              },
              {
                  'AdjustmentType': 'ExactCapcity',
              },
              {
                  'AdjustmentType': 'PercentChangeInCapacity',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_auto_scaling_groups(**kwargs)

    

    Describes one or more Auto Scaling groups.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_auto_scaling_groups(
          AutoScalingGroupNames=[
              'string',
          ],
          NextToken='string',
          MaxRecords=123
      )
    :type AutoScalingGroupNames: list
    :param AutoScalingGroupNames: 

      The names of the Auto Scaling groups. If you omit this parameter, all Auto Scaling groups are described.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutoScalingGroups': [
                {
                    'AutoScalingGroupName': 'string',
                    'AutoScalingGroupARN': 'string',
                    'LaunchConfigurationName': 'string',
                    'LaunchTemplate': {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'Version': 'string'
                    },
                    'MinSize': 123,
                    'MaxSize': 123,
                    'DesiredCapacity': 123,
                    'DefaultCooldown': 123,
                    'AvailabilityZones': [
                        'string',
                    ],
                    'LoadBalancerNames': [
                        'string',
                    ],
                    'TargetGroupARNs': [
                        'string',
                    ],
                    'HealthCheckType': 'string',
                    'HealthCheckGracePeriod': 123,
                    'Instances': [
                        {
                            'InstanceId': 'string',
                            'AvailabilityZone': 'string',
                            'LifecycleState': 'Pending'|'Pending:Wait'|'Pending:Proceed'|'Quarantined'|'InService'|'Terminating'|'Terminating:Wait'|'Terminating:Proceed'|'Terminated'|'Detaching'|'Detached'|'EnteringStandby'|'Standby',
                            'HealthStatus': 'string',
                            'LaunchConfigurationName': 'string',
                            'LaunchTemplate': {
                                'LaunchTemplateId': 'string',
                                'LaunchTemplateName': 'string',
                                'Version': 'string'
                            },
                            'ProtectedFromScaleIn': True|False
                        },
                    ],
                    'CreatedTime': datetime(2015, 1, 1),
                    'SuspendedProcesses': [
                        {
                            'ProcessName': 'string',
                            'SuspensionReason': 'string'
                        },
                    ],
                    'PlacementGroup': 'string',
                    'VPCZoneIdentifier': 'string',
                    'EnabledMetrics': [
                        {
                            'Metric': 'string',
                            'Granularity': 'string'
                        },
                    ],
                    'Status': 'string',
                    'Tags': [
                        {
                            'ResourceId': 'string',
                            'ResourceType': 'string',
                            'Key': 'string',
                            'Value': 'string',
                            'PropagateAtLaunch': True|False
                        },
                    ],
                    'TerminationPolicies': [
                        'string',
                    ],
                    'NewInstancesProtectedFromScaleIn': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AutoScalingGroups** *(list) --* 

          The groups.

          
          

          - *(dict) --* 

            Describes an Auto Scaling group.

            
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **AutoScalingGroupARN** *(string) --* 

              The Amazon Resource Name (ARN) of the Auto Scaling group.

              
            

            - **LaunchConfigurationName** *(string) --* 

              The name of the associated launch configuration.

              
            

            - **LaunchTemplate** *(dict) --* 

              The launch template for the group.

              
              

              - **LaunchTemplateId** *(string) --* 

                The ID of the launch template. You must specify either a template ID or a template name.

                
              

              - **LaunchTemplateName** *(string) --* 

                The name of the launch template. You must specify either a template name or a template ID.

                
              

              - **Version** *(string) --* 

                The version number. By default, the default version of the launch template is used.

                
          
            

            - **MinSize** *(integer) --* 

              The minimum size of the group.

              
            

            - **MaxSize** *(integer) --* 

              The maximum size of the group.

              
            

            - **DesiredCapacity** *(integer) --* 

              The desired size of the group.

              
            

            - **DefaultCooldown** *(integer) --* 

              The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.

              
            

            - **AvailabilityZones** *(list) --* 

              One or more Availability Zones for the group.

              
              

              - *(string) --* 
          
            

            - **LoadBalancerNames** *(list) --* 

              One or more load balancers associated with the group.

              
              

              - *(string) --* 
          
            

            - **TargetGroupARNs** *(list) --* 

              The Amazon Resource Names (ARN) of the target groups for your load balancer.

              
              

              - *(string) --* 
          
            

            - **HealthCheckType** *(string) --* 

              The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` .

              
            

            - **HealthCheckGracePeriod** *(integer) --* 

              The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service.

              
            

            - **Instances** *(list) --* 

              The EC2 instances associated with the group.

              
              

              - *(dict) --* 

                Describes an EC2 instance.

                
                

                - **InstanceId** *(string) --* 

                  The ID of the instance.

                  
                

                - **AvailabilityZone** *(string) --* 

                  The Availability Zone in which the instance is running.

                  
                

                - **LifecycleState** *(string) --* 

                  A description of the current lifecycle state. Note that the ``Quarantined`` state is not used.

                  
                

                - **HealthStatus** *(string) --* 

                  The last reported health status of the instance. "Healthy" means that the instance is healthy and should remain in service. "Unhealthy" means that the instance is unhealthy and Auto Scaling should terminate and replace it.

                  
                

                - **LaunchConfigurationName** *(string) --* 

                  The launch configuration associated with the instance.

                  
                

                - **LaunchTemplate** *(dict) --* 

                  The launch template for the instance.

                  
                  

                  - **LaunchTemplateId** *(string) --* 

                    The ID of the launch template. You must specify either a template ID or a template name.

                    
                  

                  - **LaunchTemplateName** *(string) --* 

                    The name of the launch template. You must specify either a template name or a template ID.

                    
                  

                  - **Version** *(string) --* 

                    The version number. By default, the default version of the launch template is used.

                    
              
                

                - **ProtectedFromScaleIn** *(boolean) --* 

                  Indicates whether the instance is protected from termination by Auto Scaling when scaling in.

                  
            
          
            

            - **CreatedTime** *(datetime) --* 

              The date and time the group was created.

              
            

            - **SuspendedProcesses** *(list) --* 

              The suspended processes associated with the group.

              
              

              - *(dict) --* 

                Describes an Auto Scaling process that has been suspended. For more information, see  ProcessType .

                
                

                - **ProcessName** *(string) --* 

                  The name of the suspended process.

                  
                

                - **SuspensionReason** *(string) --* 

                  The reason that the process was suspended.

                  
            
          
            

            - **PlacementGroup** *(string) --* 

              The name of the placement group into which you'll launch your instances, if any. For more information, see `Placement Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

              
            

            - **VPCZoneIdentifier** *(string) --* 

              One or more subnet IDs, if applicable, separated by commas.

               

              If you specify ``VPCZoneIdentifier`` and ``AvailabilityZones`` , ensure that the Availability Zones of the subnets match the values for ``AvailabilityZones`` .

              
            

            - **EnabledMetrics** *(list) --* 

              The metrics enabled for the group.

              
              

              - *(dict) --* 

                Describes an enabled metric.

                
                

                - **Metric** *(string) --* 

                  One of the following metrics:

                   

                   
                  * ``GroupMinSize``   
                   
                  * ``GroupMaxSize``   
                   
                  * ``GroupDesiredCapacity``   
                   
                  * ``GroupInServiceInstances``   
                   
                  * ``GroupPendingInstances``   
                   
                  * ``GroupStandbyInstances``   
                   
                  * ``GroupTerminatingInstances``   
                   
                  * ``GroupTotalInstances``   
                   

                  
                

                - **Granularity** *(string) --* 

                  The granularity of the metric. The only valid value is ``1Minute`` .

                  
            
          
            

            - **Status** *(string) --* 

              The current state of the group when  DeleteAutoScalingGroup is in progress.

              
            

            - **Tags** *(list) --* 

              The tags for the group.

              
              

              - *(dict) --* 

                Describes a tag for an Auto Scaling group.

                
                

                - **ResourceId** *(string) --* 

                  The name of the group.

                  
                

                - **ResourceType** *(string) --* 

                  The type of resource. The only supported value is ``auto-scaling-group`` .

                  
                

                - **Key** *(string) --* 

                  The tag key.

                  
                

                - **Value** *(string) --* 

                  The tag value.

                  
                

                - **PropagateAtLaunch** *(boolean) --* 

                  Determines whether the tag is added to new instances as they are launched in the group.

                  
            
          
            

            - **TerminationPolicies** *(list) --* 

              The termination policies for the group.

              
              

              - *(string) --* 
          
            

            - **NewInstancesProtectedFromScaleIn** *(boolean) --* 

              Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the specified Auto Scaling group.
    ::

      response = client.describe_auto_scaling_groups(
          AutoScalingGroupNames=[
              'my-auto-scaling-group',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AutoScalingGroups': [
              {
                  'AutoScalingGroupARN': 'arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:930d940e-891e-4781-a11a-7b0acd480f03:autoScalingGroupName/my-auto-scaling-group',
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'AvailabilityZones': [
                      'us-west-2c',
                  ],
                  'CreatedTime': datetime(2013, 8, 19, 20, 53, 25, 0, 231, 0),
                  'DefaultCooldown': 300,
                  'DesiredCapacity': 1,
                  'EnabledMetrics': [
                  ],
                  'HealthCheckGracePeriod': 300,
                  'HealthCheckType': 'EC2',
                  'Instances': [
                      {
                          'AvailabilityZone': 'us-west-2c',
                          'HealthStatus': 'Healthy',
                          'InstanceId': 'i-4ba0837f',
                          'LaunchConfigurationName': 'my-launch-config',
                          'LifecycleState': 'InService',
                      },
                  ],
                  'LaunchConfigurationName': 'my-launch-config',
                  'LoadBalancerNames': [
                  ],
                  'MaxSize': 1,
                  'MinSize': 0,
                  'NewInstancesProtectedFromScaleIn': False,
                  'SuspendedProcesses': [
                  ],
                  'Tags': [
                  ],
                  'TerminationPolicies': [
                      'Default',
                  ],
                  'VPCZoneIdentifier': 'subnet-12345678',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_auto_scaling_instances(**kwargs)

    

    Describes one or more Auto Scaling instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingInstances>`_    


    **Request Syntax** 
    ::

      response = client.describe_auto_scaling_instances(
          InstanceIds=[
              'string',
          ],
          MaxRecords=123,
          NextToken='string'
      )
    :type InstanceIds: list
    :param InstanceIds: 

      The instances to describe; up to 50 instance IDs. If you omit this parameter, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.

      

    
      - *(string) --* 

      
  
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutoScalingInstances': [
                {
                    'InstanceId': 'string',
                    'AutoScalingGroupName': 'string',
                    'AvailabilityZone': 'string',
                    'LifecycleState': 'string',
                    'HealthStatus': 'string',
                    'LaunchConfigurationName': 'string',
                    'LaunchTemplate': {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'Version': 'string'
                    },
                    'ProtectedFromScaleIn': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AutoScalingInstances** *(list) --* 

          The instances.

          
          

          - *(dict) --* 

            Describes an EC2 instance associated with an Auto Scaling group.

            
            

            - **InstanceId** *(string) --* 

              The ID of the instance.

              
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group for the instance.

              
            

            - **AvailabilityZone** *(string) --* 

              The Availability Zone for the instance.

              
            

            - **LifecycleState** *(string) --* 

              The lifecycle state for the instance. For more information, see `Auto Scaling Lifecycle <http://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroupLifecycle.html>`__ in the *Auto Scaling User Guide* .

              
            

            - **HealthStatus** *(string) --* 

              The last reported health status of this instance. "Healthy" means that the instance is healthy and should remain in service. "Unhealthy" means that the instance is unhealthy and Auto Scaling should terminate and replace it.

              
            

            - **LaunchConfigurationName** *(string) --* 

              The launch configuration used to launch the instance. This value is not available if you attached the instance to the Auto Scaling group.

              
            

            - **LaunchTemplate** *(dict) --* 

              The launch template for the instance.

              
              

              - **LaunchTemplateId** *(string) --* 

                The ID of the launch template. You must specify either a template ID or a template name.

                
              

              - **LaunchTemplateName** *(string) --* 

                The name of the launch template. You must specify either a template name or a template ID.

                
              

              - **Version** *(string) --* 

                The version number. By default, the default version of the launch template is used.

                
          
            

            - **ProtectedFromScaleIn** *(boolean) --* 

              Indicates whether the instance is protected from termination by Auto Scaling when scaling in.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the specified Auto Scaling instance.
    ::

      response = client.describe_auto_scaling_instances(
          InstanceIds=[
              'i-4ba0837f',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AutoScalingInstances': [
              {
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'AvailabilityZone': 'us-west-2c',
                  'HealthStatus': 'HEALTHY',
                  'InstanceId': 'i-4ba0837f',
                  'LaunchConfigurationName': 'my-launch-config',
                  'LifecycleState': 'InService',
                  'ProtectedFromScaleIn': False,
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_auto_scaling_notification_types()

    

    Describes the notification types that are supported by Auto Scaling.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes>`_    


    **Request Syntax** 

    ::

      response = client.describe_auto_scaling_notification_types()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutoScalingNotificationTypes': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AutoScalingNotificationTypes** *(list) --* 

          The notification types.

          
          

          - *(string) --* 
      
    

    **Examples** 

    This example describes the available notification types.
    ::

      response = client.describe_auto_scaling_notification_types(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AutoScalingNotificationTypes': [
              'autoscaling:EC2_INSTANCE_LAUNCH',
              'autoscaling:EC2_INSTANCE_LAUNCH_ERROR',
              'autoscaling:EC2_INSTANCE_TERMINATE',
              'autoscaling:EC2_INSTANCE_TERMINATE_ERROR',
              'autoscaling:TEST_NOTIFICATION',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_launch_configurations(**kwargs)

    

    Describes one or more launch configurations.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLaunchConfigurations>`_    


    **Request Syntax** 
    ::

      response = client.describe_launch_configurations(
          LaunchConfigurationNames=[
              'string',
          ],
          NextToken='string',
          MaxRecords=123
      )
    :type LaunchConfigurationNames: list
    :param LaunchConfigurationNames: 

      The launch configuration names. If you omit this parameter, all launch configurations are described.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LaunchConfigurations': [
                {
                    'LaunchConfigurationName': 'string',
                    'LaunchConfigurationARN': 'string',
                    'ImageId': 'string',
                    'KeyName': 'string',
                    'SecurityGroups': [
                        'string',
                    ],
                    'ClassicLinkVPCId': 'string',
                    'ClassicLinkVPCSecurityGroups': [
                        'string',
                    ],
                    'UserData': 'string',
                    'InstanceType': 'string',
                    'KernelId': 'string',
                    'RamdiskId': 'string',
                    'BlockDeviceMappings': [
                        {
                            'VirtualName': 'string',
                            'DeviceName': 'string',
                            'Ebs': {
                                'SnapshotId': 'string',
                                'VolumeSize': 123,
                                'VolumeType': 'string',
                                'DeleteOnTermination': True|False,
                                'Iops': 123,
                                'Encrypted': True|False
                            },
                            'NoDevice': True|False
                        },
                    ],
                    'InstanceMonitoring': {
                        'Enabled': True|False
                    },
                    'SpotPrice': 'string',
                    'IamInstanceProfile': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'EbsOptimized': True|False,
                    'AssociatePublicIpAddress': True|False,
                    'PlacementTenancy': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LaunchConfigurations** *(list) --* 

          The launch configurations.

          
          

          - *(dict) --* 

            Describes a launch configuration.

            
            

            - **LaunchConfigurationName** *(string) --* 

              The name of the launch configuration.

              
            

            - **LaunchConfigurationARN** *(string) --* 

              The Amazon Resource Name (ARN) of the launch configuration.

              
            

            - **ImageId** *(string) --* 

              The ID of the Amazon Machine Image (AMI).

              
            

            - **KeyName** *(string) --* 

              The name of the key pair.

              
            

            - **SecurityGroups** *(list) --* 

              The security groups to associate with the instances.

              
              

              - *(string) --* 
          
            

            - **ClassicLinkVPCId** *(string) --* 

              The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. This parameter can only be used if you are launching EC2-Classic instances. For more information, see `ClassicLink <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

              
            

            - **ClassicLinkVPCSecurityGroups** *(list) --* 

              The IDs of one or more security groups for the VPC specified in ``ClassicLinkVPCId`` . This parameter is required if you specify a ClassicLink-enabled VPC, and cannot be used otherwise. For more information, see `ClassicLink <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

              
              

              - *(string) --* 
          
            

            - **UserData** *(string) --* 

              The user data available to the instances.

              
            

            - **InstanceType** *(string) --* 

              The instance type for the instances.

              
            

            - **KernelId** *(string) --* 

              The ID of the kernel associated with the AMI.

              
            

            - **RamdiskId** *(string) --* 

              The ID of the RAM disk associated with the AMI.

              
            

            - **BlockDeviceMappings** *(list) --* 

              A block device mapping, which specifies the block devices for the instance.

              
              

              - *(dict) --* 

                Describes a block device mapping.

                
                

                - **VirtualName** *(string) --* 

                  The name of the virtual device (for example, ``ephemeral0`` ).

                  
                

                - **DeviceName** *(string) --* 

                  The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).

                  
                

                - **Ebs** *(dict) --* 

                  The information about the Amazon EBS volume.

                  
                  

                  - **SnapshotId** *(string) --* 

                    The ID of the snapshot.

                    
                  

                  - **VolumeSize** *(integer) --* 

                    The volume size, in GiB. For ``standard`` volumes, specify a value from 1 to 1,024. For ``io1`` volumes, specify a value from 4 to 16,384. For ``gp2`` volumes, specify a value from 1 to 16,384. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.

                     

                    Default: If you create a volume from a snapshot and you don't specify a volume size, the default is the snapshot size.

                    
                  

                  - **VolumeType** *(string) --* 

                    The volume type. For more information, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

                     

                    Valid values: ``standard`` | ``io1`` | ``gp2``  

                     

                    Default: ``standard``  

                    
                  

                  - **DeleteOnTermination** *(boolean) --* 

                    Indicates whether the volume is deleted on instance termination.

                     

                    Default: ``true``  

                    
                  

                  - **Iops** *(integer) --* 

                    The number of I/O operations per second (IOPS) to provision for the volume.

                     

                    Constraint: Required when the volume type is ``io1`` .

                    
                  

                  - **Encrypted** *(boolean) --* 

                    Indicates whether the volume should be encrypted. Encrypted EBS volumes must be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or an unencrypted volume from an encrypted snapshot. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

                    
              
                

                - **NoDevice** *(boolean) --* 

                  Suppresses a device mapping.

                   

                  If this parameter is true for the root device, the instance might fail the EC2 health check. Auto Scaling launches a replacement instance if the instance fails the health check.

                  
            
          
            

            - **InstanceMonitoring** *(dict) --* 

              Controls whether instances in this group are launched with detailed (``true`` ) or basic (``false`` ) monitoring.

              
              

              - **Enabled** *(boolean) --* 

                If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

                
          
            

            - **SpotPrice** *(string) --* 

              The price to bid when launching Spot Instances.

              
            

            - **IamInstanceProfile** *(string) --* 

              The name or Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.

              
            

            - **CreatedTime** *(datetime) --* 

              The creation date and time for the launch configuration.

              
            

            - **EbsOptimized** *(boolean) --* 

              Controls whether the instance is optimized for EBS I/O (``true`` ) or not (``false`` ).

              
            

            - **AssociatePublicIpAddress** *(boolean) --* 

              [EC2-VPC] Indicates whether to assign a public IP address to each instance.

              
            

            - **PlacementTenancy** *(string) --* 

              The tenancy of the instance, either ``default`` or ``dedicated`` . An instance with ``dedicated`` tenancy runs in an isolated, single-tenant hardware and can only be launched into a VPC.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the specified launch configuration.
    ::

      response = client.describe_launch_configurations(
          LaunchConfigurationNames=[
              'my-launch-config',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'LaunchConfigurations': [
              {
                  'AssociatePublicIpAddress': True,
                  'BlockDeviceMappings': [
                  ],
                  'CreatedTime': datetime(2014, 5, 7, 17, 39, 28, 2, 127, 0),
                  'EbsOptimized': False,
                  'ImageId': 'ami-043a5034',
                  'InstanceMonitoring': {
                      'Enabled': True,
                  },
                  'InstanceType': 't1.micro',
                  'LaunchConfigurationARN': 'arn:aws:autoscaling:us-west-2:123456789012:launchConfiguration:98d3b196-4cf9-4e88-8ca1-8547c24ced8b:launchConfigurationName/my-launch-config',
                  'LaunchConfigurationName': 'my-launch-config',
                  'SecurityGroups': [
                      'sg-67ef0308',
                  ],
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_lifecycle_hook_types()

    

    Describes the available types of lifecycle hooks.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLifecycleHookTypes>`_    


    **Request Syntax** 

    ::

      response = client.describe_lifecycle_hook_types()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LifecycleHookTypes': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LifecycleHookTypes** *(list) --* 

          The lifecycle hook types.

          
          

          - *(string) --* 
      
    

    **Examples** 

    This example describes the available lifecycle hook types.
    ::

      response = client.describe_lifecycle_hook_types(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'LifecycleHookTypes': [
              'autoscaling:EC2_INSTANCE_LAUNCHING',
              'autoscaling:EC2_INSTANCE_TERMINATING',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_lifecycle_hooks(**kwargs)

    

    Describes the lifecycle hooks for the specified Auto Scaling group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLifecycleHooks>`_    


    **Request Syntax** 
    ::

      response = client.describe_lifecycle_hooks(
          AutoScalingGroupName='string',
          LifecycleHookNames=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type LifecycleHookNames: list
    :param LifecycleHookNames: 

      The names of one or more lifecycle hooks. If you omit this parameter, all lifecycle hooks are described.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LifecycleHooks': [
                {
                    'LifecycleHookName': 'string',
                    'AutoScalingGroupName': 'string',
                    'LifecycleTransition': 'string',
                    'NotificationTargetARN': 'string',
                    'RoleARN': 'string',
                    'NotificationMetadata': 'string',
                    'HeartbeatTimeout': 123,
                    'GlobalTimeout': 123,
                    'DefaultResult': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LifecycleHooks** *(list) --* 

          The lifecycle hooks for the specified group.

          
          

          - *(dict) --* 

            Describes a lifecycle hook, which tells Auto Scaling that you want to perform an action whenever it launches instances or whenever it terminates instances.

             

            For more information, see `Auto Scaling Lifecycle Hooks <http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html>`__ in the *Auto Scaling User Guide* .

            
            

            - **LifecycleHookName** *(string) --* 

              The name of the lifecycle hook.

              
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group for the lifecycle hook.

              
            

            - **LifecycleTransition** *(string) --* 

              The state of the EC2 instance to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see  DescribeLifecycleHookTypes .

              
            

            - **NotificationTargetARN** *(string) --* 

              The ARN of the target that Auto Scaling sends notifications to when an instance is in the transition state for the lifecycle hook. The notification target can be either an SQS queue or an SNS topic.

              
            

            - **RoleARN** *(string) --* 

              The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

              
            

            - **NotificationMetadata** *(string) --* 

              Additional information that you want to include any time Auto Scaling sends a message to the notification target.

              
            

            - **HeartbeatTimeout** *(integer) --* 

              The maximum time, in seconds, that can elapse before the lifecycle hook times out. If the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling  RecordLifecycleActionHeartbeat .

              
            

            - **GlobalTimeout** *(integer) --* 

              The maximum time, in seconds, that an instance can remain in a ``Pending:Wait`` or ``Terminating:Wait`` state. The maximum is 172800 seconds (48 hours) or 100 times ``HeartbeatTimeout`` , whichever is smaller.

              
            

            - **DefaultResult** *(string) --* 

              Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are ``CONTINUE`` and ``ABANDON`` . The default value is ``CONTINUE`` .

              
        
      
    

    **Examples** 

    This example describes the lifecycle hooks for the specified Auto Scaling group.
    ::

      response = client.describe_lifecycle_hooks(
          AutoScalingGroupName='my-auto-scaling-group',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'LifecycleHooks': [
              {
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'DefaultResult': 'ABANDON',
                  'GlobalTimeout': 172800,
                  'HeartbeatTimeout': 3600,
                  'LifecycleHookName': 'my-lifecycle-hook',
                  'LifecycleTransition': 'autoscaling:EC2_INSTANCE_LAUNCHING',
                  'NotificationTargetARN': 'arn:aws:sns:us-west-2:123456789012:my-sns-topic',
                  'RoleARN': 'arn:aws:iam::123456789012:role/my-auto-scaling-role',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_load_balancer_target_groups(**kwargs)

    

    Describes the target groups for the specified Auto Scaling group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLoadBalancerTargetGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_load_balancer_target_groups(
          AutoScalingGroupName='string',
          NextToken='string',
          MaxRecords=123
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LoadBalancerTargetGroups': [
                {
                    'LoadBalancerTargetGroupARN': 'string',
                    'State': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LoadBalancerTargetGroups** *(list) --* 

          Information about the target groups.

          
          

          - *(dict) --* 

            Describes the state of a target group.

             

            If you attach a target group to an existing Auto Scaling group, the initial state is ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are registered with the target group. If ELB health checks are enabled, the state transitions to ``InService`` after at least one Auto Scaling instance passes the health check. If EC2 health checks are enabled instead, the target group remains in the ``Added`` state.

            
            

            - **LoadBalancerTargetGroupARN** *(string) --* 

              The Amazon Resource Name (ARN) of the target group.

              
            

            - **State** *(string) --* 

              The state of the target group.

               

               
              * ``Adding`` - The Auto Scaling instances are being registered with the target group. 
               
              * ``Added`` - All Auto Scaling instances are registered with the target group. 
               
              * ``InService`` - At least one Auto Scaling instance passed an ELB health check. 
               
              * ``Removing`` - The Auto Scaling instances are being deregistered from the target group. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances. 
               
              * ``Removed`` - All Auto Scaling instances are deregistered from the target group. 
               

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the target groups attached to the specified Auto Scaling group.
    ::

      response = client.describe_load_balancer_target_groups(
          AutoScalingGroupName='my-auto-scaling-group',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'LoadBalancerTargetGroups': [
              {
                  'LoadBalancerTargetGroupARN': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                  'State': 'Added',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_load_balancers(**kwargs)

    

    Describes the load balancers for the specified Auto Scaling group.

     

    Note that this operation describes only Classic Load Balancers. If you have Application Load Balancers, use  DescribeLoadBalancerTargetGroups instead.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLoadBalancers>`_    


    **Request Syntax** 
    ::

      response = client.describe_load_balancers(
          AutoScalingGroupName='string',
          NextToken='string',
          MaxRecords=123
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LoadBalancers': [
                {
                    'LoadBalancerName': 'string',
                    'State': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LoadBalancers** *(list) --* 

          The load balancers.

          
          

          - *(dict) --* 

            Describes the state of a Classic Load Balancer.

             

            If you specify a load balancer when creating the Auto Scaling group, the state of the load balancer is ``InService`` .

             

            If you attach a load balancer to an existing Auto Scaling group, the initial state is ``Adding`` . The state transitions to ``Added`` after all instances in the group are registered with the load balancer. If ELB health checks are enabled for the load balancer, the state transitions to ``InService`` after at least one instance in the group passes the health check. If EC2 health checks are enabled instead, the load balancer remains in the ``Added`` state.

            
            

            - **LoadBalancerName** *(string) --* 

              The name of the load balancer.

              
            

            - **State** *(string) --* 

              One of the following load balancer states:

               

               
              * ``Adding`` - The instances in the group are being registered with the load balancer. 
               
              * ``Added`` - All instances in the group are registered with the load balancer. 
               
              * ``InService`` - At least one instance in the group passed an ELB health check. 
               
              * ``Removing`` - The instances in the group are being deregistered from the load balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances. 
               
              * ``Removed`` - All instances in the group are deregistered from the load balancer. 
               

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the load balancers attached to the specified Auto Scaling group.
    ::

      response = client.describe_load_balancers(
          AutoScalingGroupName='my-auto-scaling-group',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'LoadBalancers': [
              {
                  'LoadBalancerName': 'my-load-balancer',
                  'State': 'Added',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_metric_collection_types()

    

    Describes the available CloudWatch metrics for Auto Scaling.

     

    Note that the ``GroupStandbyInstances`` metric is not returned by default. You must explicitly request this metric when calling  EnableMetricsCollection .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeMetricCollectionTypes>`_    


    **Request Syntax** 

    ::

      response = client.describe_metric_collection_types()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Metrics': [
                {
                    'Metric': 'string'
                },
            ],
            'Granularities': [
                {
                    'Granularity': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Metrics** *(list) --* 

          One or more metrics.

          
          

          - *(dict) --* 

            Describes a metric.

            
            

            - **Metric** *(string) --* 

              One of the following metrics:

               

               
              * ``GroupMinSize``   
               
              * ``GroupMaxSize``   
               
              * ``GroupDesiredCapacity``   
               
              * ``GroupInServiceInstances``   
               
              * ``GroupPendingInstances``   
               
              * ``GroupStandbyInstances``   
               
              * ``GroupTerminatingInstances``   
               
              * ``GroupTotalInstances``   
               

              
        
      
        

        - **Granularities** *(list) --* 

          The granularities for the metrics.

          
          

          - *(dict) --* 

            Describes a granularity of a metric.

            
            

            - **Granularity** *(string) --* 

              The granularity. The only valid value is ``1Minute`` .

              
        
      
    

    **Examples** 

    This example describes the available metric collection types.
    ::

      response = client.describe_metric_collection_types(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Granularities': [
              {
                  'Granularity': '1Minute',
              },
          ],
          'Metrics': [
              {
                  'Metric': 'GroupMinSize',
              },
              {
                  'Metric': 'GroupMaxSize',
              },
              {
                  'Metric': 'GroupDesiredCapacity',
              },
              {
                  'Metric': 'GroupInServiceInstances',
              },
              {
                  'Metric': 'GroupPendingInstances',
              },
              {
                  'Metric': 'GroupTerminatingInstances',
              },
              {
                  'Metric': 'GroupStandbyInstances',
              },
              {
                  'Metric': 'GroupTotalInstances',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_notification_configurations(**kwargs)

    

    Describes the notification actions associated with the specified Auto Scaling group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeNotificationConfigurations>`_    


    **Request Syntax** 
    ::

      response = client.describe_notification_configurations(
          AutoScalingGroupNames=[
              'string',
          ],
          NextToken='string',
          MaxRecords=123
      )
    :type AutoScalingGroupNames: list
    :param AutoScalingGroupNames: 

      The name of the Auto Scaling group.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NotificationConfigurations': [
                {
                    'AutoScalingGroupName': 'string',
                    'TopicARN': 'string',
                    'NotificationType': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NotificationConfigurations** *(list) --* 

          The notification configurations.

          
          

          - *(dict) --* 

            Describes a notification.

            
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **TopicARN** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.

              
            

            - **NotificationType** *(string) --* 

              One of the following event notification types:

               

               
              * ``autoscaling:EC2_INSTANCE_LAUNCH``   
               
              * ``autoscaling:EC2_INSTANCE_LAUNCH_ERROR``   
               
              * ``autoscaling:EC2_INSTANCE_TERMINATE``   
               
              * ``autoscaling:EC2_INSTANCE_TERMINATE_ERROR``   
               
              * ``autoscaling:TEST_NOTIFICATION``   
               

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the notification configurations for the specified Auto Scaling group.
    ::

      response = client.describe_notification_configurations(
          AutoScalingGroupNames=[
              'my-auto-scaling-group',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'NotificationConfigurations': [
              {
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'NotificationType': 'autoscaling:TEST_NOTIFICATION',
                  'TopicARN': 'arn:aws:sns:us-west-2:123456789012:my-sns-topic-2',
              },
              {
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'NotificationType': 'autoscaling:TEST_NOTIFICATION',
                  'TopicARN': 'arn:aws:sns:us-west-2:123456789012:my-sns-topic',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_policies(**kwargs)

    

    Describes the policies for the specified Auto Scaling group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribePolicies>`_    


    **Request Syntax** 
    ::

      response = client.describe_policies(
          AutoScalingGroupName='string',
          PolicyNames=[
              'string',
          ],
          PolicyTypes=[
              'string',
          ],
          NextToken='string',
          MaxRecords=123
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: 

      The name of the Auto Scaling group.

      

    
    :type PolicyNames: list
    :param PolicyNames: 

      The names of one or more policies. If you omit this parameter, all policies are described. If an group name is provided, the results are limited to that group. This list is limited to 50 items. If you specify an unknown policy name, it is ignored with no error.

      

    
      - *(string) --* 

      
  
    :type PolicyTypes: list
    :param PolicyTypes: 

      One or more policy types. Valid values are ``SimpleScaling`` and ``StepScaling`` .

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to be returned with each call. The default value is 50 and the maximum value is 100.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ScalingPolicies': [
                {
                    'AutoScalingGroupName': 'string',
                    'PolicyName': 'string',
                    'PolicyARN': 'string',
                    'PolicyType': 'string',
                    'AdjustmentType': 'string',
                    'MinAdjustmentStep': 123,
                    'MinAdjustmentMagnitude': 123,
                    'ScalingAdjustment': 123,
                    'Cooldown': 123,
                    'StepAdjustments': [
                        {
                            'MetricIntervalLowerBound': 123.0,
                            'MetricIntervalUpperBound': 123.0,
                            'ScalingAdjustment': 123
                        },
                    ],
                    'MetricAggregationType': 'string',
                    'EstimatedInstanceWarmup': 123,
                    'Alarms': [
                        {
                            'AlarmName': 'string',
                            'AlarmARN': 'string'
                        },
                    ],
                    'TargetTrackingConfiguration': {
                        'PredefinedMetricSpecification': {
                            'PredefinedMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'ALBRequestCountPerTarget',
                            'ResourceLabel': 'string'
                        },
                        'CustomizedMetricSpecification': {
                            'MetricName': 'string',
                            'Namespace': 'string',
                            'Dimensions': [
                                {
                                    'Name': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                            'Unit': 'string'
                        },
                        'TargetValue': 123.0,
                        'DisableScaleIn': True|False
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ScalingPolicies** *(list) --* 

          The scaling policies.

          
          

          - *(dict) --* 

            Describes a scaling policy.

            
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **PolicyName** *(string) --* 

              The name of the scaling policy.

              
            

            - **PolicyARN** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

              
            

            - **PolicyType** *(string) --* 

              The policy type. Valid values are ``SimpleScaling`` and ``StepScaling`` .

              
            

            - **AdjustmentType** *(string) --* 

              The adjustment type, which specifies how ``ScalingAdjustment`` is interpreted. Valid values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .

              
            

            - **MinAdjustmentStep** *(integer) --* 

              Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.

              
            

            - **MinAdjustmentMagnitude** *(integer) --* 

              The minimum number of instances to scale. If the value of ``AdjustmentType`` is ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the Auto Scaling group by at least this many instances. Otherwise, the error is ``ValidationError`` .

              
            

            - **ScalingAdjustment** *(integer) --* 

              The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.

              
            

            - **Cooldown** *(integer) --* 

              The amount of time, in seconds, after a scaling activity completes before any further dynamic scaling activities can start.

              
            

            - **StepAdjustments** *(list) --* 

              A set of adjustments that enable you to scale based on the size of the alarm breach.

              
              

              - *(dict) --* 

                Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you've defined for the alarm.

                 

                For the following examples, suppose that you have an alarm with a breach threshold of 50:

                 

                 
                * If you want the adjustment to be triggered when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10. 
                 
                * If you want the adjustment to be triggered when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0. 
                 

                 

                There are a few rules for the step adjustments for your step policy:

                 

                 
                * The ranges of your step adjustments can't overlap or have a gap. 
                 
                * At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound. 
                 
                * At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound. 
                 
                * The upper and lower bound can't be null in the same step adjustment. 
                 

                
                

                - **MetricIntervalLowerBound** *(float) --* 

                  The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.

                  
                

                - **MetricIntervalUpperBound** *(float) --* 

                  The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.

                   

                  The upper bound must be greater than the lower bound.

                  
                

                - **ScalingAdjustment** *(integer) --* 

                  The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.

                  
            
          
            

            - **MetricAggregationType** *(string) --* 

              The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` , ``Maximum`` , and ``Average`` .

              
            

            - **EstimatedInstanceWarmup** *(integer) --* 

              The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.

              
            

            - **Alarms** *(list) --* 

              The CloudWatch alarms related to the policy.

              
              

              - *(dict) --* 

                Describes an alarm.

                
                

                - **AlarmName** *(string) --* 

                  The name of the alarm.

                  
                

                - **AlarmARN** *(string) --* 

                  The Amazon Resource Name (ARN) of the alarm.

                  
            
          
            

            - **TargetTrackingConfiguration** *(dict) --* 

              A target tracking policy.

              
              

              - **PredefinedMetricSpecification** *(dict) --* 

                A predefined metric. You can specify either a predefined metric or a customized metric.

                
                

                - **PredefinedMetricType** *(string) --* 

                  The metric type.

                  
                

                - **ResourceLabel** *(string) --* 

                  Identifies the resource associated with the metric type. The following predefined metrics are available:

                   

                   
                  * ``ASGAverageCPUUtilization`` - average CPU utilization of the Auto Scaling group 
                   
                  * ``ASGAverageNetworkIn`` - average number of bytes received on all network interfaces by the Auto Scaling group 
                   
                  * ``ASGAverageNetworkOut`` - average number of bytes sent out on all network interfaces by the Auto Scaling group 
                   
                  * ``ALBRequestCountPerTarget`` - number of requests completed per target in an Application Load Balancer target group 
                   

                   

                  For predefined metric types ``ASGAverageCPUUtilization`` , ``ASGAverageNetworkIn`` , and ``ASGAverageNetworkOut`` , the parameter must not be specified as the resource associated with the metric type is the Auto Scaling group. For predefined metric type ``ALBRequestCountPerTarget`` , the parameter must be specified in the format: ``app/*load-balancer-name* /*load-balancer-id* /targetgroup/*target-group-name* /*target-group-id* `` , where ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load balancer ARN, and ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the target group ARN. The target group must be attached to the Auto Scaling group.

                  
            
              

              - **CustomizedMetricSpecification** *(dict) --* 

                A customized metric.

                
                

                - **MetricName** *(string) --* 

                  The name of the metric.

                  
                

                - **Namespace** *(string) --* 

                  The namespace of the metric.

                  
                

                - **Dimensions** *(list) --* 

                  The dimensions of the metric.

                  
                  

                  - *(dict) --* 

                    Describes the dimension of a metric.

                    
                    

                    - **Name** *(string) --* 

                      The name of the dimension.

                      
                    

                    - **Value** *(string) --* 

                      The value of the dimension.

                      
                
              
                

                - **Statistic** *(string) --* 

                  The statistic of the metric.

                  
                

                - **Unit** *(string) --* 

                  The unit of the metric.

                  
            
              

              - **TargetValue** *(float) --* 

                The target value for the metric.

                
              

              - **DisableScaleIn** *(boolean) --* 

                Indicates whether scale in by the target tracking policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking policy won't remove instances from the Auto Scaling group. Otherwise, scale in is enabled and the target tracking policy can remove instances from the Auto Scaling group. The default value is ``false`` .

                
          
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the policies for the specified Auto Scaling group.
    ::

      response = client.describe_policies(
          AutoScalingGroupName='my-auto-scaling-group',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ScalingPolicies': [
              {
                  'AdjustmentType': 'ChangeInCapacity',
                  'Alarms': [
                  ],
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'PolicyARN': 'arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:2233f3d7-6290-403b-b632-93c553560106:autoScalingGroupName/my-auto-scaling-group:policyName/ScaleIn',
                  'PolicyName': 'ScaleIn',
                  'ScalingAdjustment': -1,
              },
              {
                  'AdjustmentType': 'PercentChangeInCapacity',
                  'Alarms': [
                  ],
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'Cooldown': 60,
                  'MinAdjustmentStep': 2,
                  'PolicyARN': 'arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:2b435159-cf77-4e89-8c0e-d63b497baad7:autoScalingGroupName/my-auto-scaling-group:policyName/ScalePercentChange',
                  'PolicyName': 'ScalePercentChange',
                  'ScalingAdjustment': 25,
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_scaling_activities(**kwargs)

    

    Describes one or more scaling activities for the specified Auto Scaling group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScalingActivities>`_    


    **Request Syntax** 
    ::

      response = client.describe_scaling_activities(
          ActivityIds=[
              'string',
          ],
          AutoScalingGroupName='string',
          MaxRecords=123,
          NextToken='string'
      )
    :type ActivityIds: list
    :param ActivityIds: 

      The activity IDs of the desired scaling activities. If you omit this parameter, all activities for the past six weeks are described. If you specify an Auto Scaling group, the results are limited to that group. The list of requested activities cannot contain more than 50 items. If unknown activities are requested, they are ignored with no error.

      

    
      - *(string) --* 

      
  
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: 

      The name of the Auto Scaling group.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 100.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Activities': [
                {
                    'ActivityId': 'string',
                    'AutoScalingGroupName': 'string',
                    'Description': 'string',
                    'Cause': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                    'StatusMessage': 'string',
                    'Progress': 123,
                    'Details': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Activities** *(list) --* 

          The scaling activities. Activities are sorted by start time. Activities still in progress are described first.

          
          

          - *(dict) --* 

            Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

            
            

            - **ActivityId** *(string) --* 

              The ID of the activity.

              
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **Description** *(string) --* 

              A friendly, more verbose description of the activity.

              
            

            - **Cause** *(string) --* 

              The reason the activity began.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the activity.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the activity.

              
            

            - **StatusCode** *(string) --* 

              The current status of the activity.

              
            

            - **StatusMessage** *(string) --* 

              A friendly, more verbose description of the activity status.

              
            

            - **Progress** *(integer) --* 

              A value between 0 and 100 that indicates the progress of the activity.

              
            

            - **Details** *(string) --* 

              The details about the activity.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the scaling activities for the specified Auto Scaling group.
    ::

      response = client.describe_scaling_activities(
          AutoScalingGroupName='my-auto-scaling-group',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Activities': [
              {
                  'ActivityId': 'f9f2d65b-f1f2-43e7-b46d-d86756459699',
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'Cause': 'At 2013-08-19T20:53:25Z a user request created an AutoScalingGroup changing the desired capacity from 0 to 1.  At 2013-08-19T20:53:29Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 1.',
                  'Description': 'Launching a new EC2 instance: i-4ba0837f',
                  'Details': 'details',
                  'EndTime': datetime(2013, 8, 19, 20, 54, 2, 0, 231, 0),
                  'Progress': 100,
                  'StartTime': datetime(2013, 8, 19, 20, 53, 29, 0, 231, 0),
                  'StatusCode': 'Successful',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_scaling_process_types()

    

    Describes the scaling process types for use with  ResumeProcesses and  SuspendProcesses .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScalingProcessTypes>`_    


    **Request Syntax** 

    ::

      response = client.describe_scaling_process_types()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Processes': [
                {
                    'ProcessName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Processes** *(list) --* 

          The names of the process types.

          
          

          - *(dict) --* 

            Describes a process type.

             

            For more information, see `Auto Scaling Processes <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-suspend-resume-processes.html#process-types>`__ in the *Auto Scaling User Guide* .

            
            

            - **ProcessName** *(string) --* 

              One of the following processes:

               

               
              * ``Launch``   
               
              * ``Terminate``   
               
              * ``AddToLoadBalancer``   
               
              * ``AlarmNotification``   
               
              * ``AZRebalance``   
               
              * ``HealthCheck``   
               
              * ``ReplaceUnhealthy``   
               
              * ``ScheduledActions``   
               

              
        
      
    

    **Examples** 

    This example describes the Auto Scaling process types.
    ::

      response = client.describe_scaling_process_types(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Processes': [
              {
                  'ProcessName': 'AZRebalance',
              },
              {
                  'ProcessName': 'AddToLoadBalancer',
              },
              {
                  'ProcessName': 'AlarmNotification',
              },
              {
                  'ProcessName': 'HealthCheck',
              },
              {
                  'ProcessName': 'Launch',
              },
              {
                  'ProcessName': 'ReplaceUnhealthy',
              },
              {
                  'ProcessName': 'ScheduledActions',
              },
              {
                  'ProcessName': 'Terminate',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_scheduled_actions(**kwargs)

    

    Describes the actions scheduled for your Auto Scaling group that haven't run. To describe the actions that have already run, use  DescribeScalingActivities .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScheduledActions>`_    


    **Request Syntax** 
    ::

      response = client.describe_scheduled_actions(
          AutoScalingGroupName='string',
          ScheduledActionNames=[
              'string',
          ],
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          NextToken='string',
          MaxRecords=123
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: 

      The name of the Auto Scaling group.

      

    
    :type ScheduledActionNames: list
    :param ScheduledActionNames: 

      Describes one or more scheduled actions. If you omit this parameter, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.

       

      You can describe up to a maximum of 50 instances with a single call. If there are more items to return, the call returns a token. To get the next set of items, repeat the call with the returned token.

      

    
      - *(string) --* 

      
  
    :type StartTime: datetime
    :param StartTime: 

      The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.

      

    
    :type EndTime: datetime
    :param EndTime: 

      The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ScheduledUpdateGroupActions': [
                {
                    'AutoScalingGroupName': 'string',
                    'ScheduledActionName': 'string',
                    'ScheduledActionARN': 'string',
                    'Time': datetime(2015, 1, 1),
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'Recurrence': 'string',
                    'MinSize': 123,
                    'MaxSize': 123,
                    'DesiredCapacity': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ScheduledUpdateGroupActions** *(list) --* 

          The scheduled actions.

          
          

          - *(dict) --* 

            Describes a scheduled update to an Auto Scaling group.

            
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **ScheduledActionName** *(string) --* 

              The name of the scheduled action.

              
            

            - **ScheduledActionARN** *(string) --* 

              The Amazon Resource Name (ARN) of the scheduled action.

              
            

            - **Time** *(datetime) --* 

              This parameter is deprecated.

              
            

            - **StartTime** *(datetime) --* 

              The date and time that the action is scheduled to begin. This date and time can be up to one month in the future.

               

              When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the boundaries of when the recurring action will start and stop.

              
            

            - **EndTime** *(datetime) --* 

              The date and time that the action is scheduled to end. This date and time can be up to one month in the future.

              
            

            - **Recurrence** *(string) --* 

              The recurring schedule for the action.

              
            

            - **MinSize** *(integer) --* 

              The minimum size of the group.

              
            

            - **MaxSize** *(integer) --* 

              The maximum size of the group.

              
            

            - **DesiredCapacity** *(integer) --* 

              The number of instances you prefer to maintain in the group.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the scheduled actions for the specified Auto Scaling group.
    ::

      response = client.describe_scheduled_actions(
          AutoScalingGroupName='my-auto-scaling-group',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ScheduledUpdateGroupActions': [
              {
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'DesiredCapacity': 4,
                  'MaxSize': 6,
                  'MinSize': 2,
                  'Recurrence': '30 0 1 12 0',
                  'ScheduledActionARN': 'arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-auto-scaling-group:scheduledActionName/my-scheduled-action',
                  'ScheduledActionName': 'my-scheduled-action',
                  'StartTime': datetime(2016, 12, 1, 0, 30, 0, 3, 336, 0),
                  'Time': datetime(2016, 12, 1, 0, 30, 0, 3, 336, 0),
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_tags(**kwargs)

    

    Describes the specified tags.

     

    You can use filters to limit the results. For example, you can query for the tags for a specific Auto Scaling group. You can specify multiple values for a filter. A tag must match at least one of the specified values for it to be included in the results.

     

    You can also specify multiple filters. The result includes information for a particular tag only if it matches all the filters. If there's no match, no special message is returned.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeTags>`_    


    **Request Syntax** 
    ::

      response = client.describe_tags(
          Filters=[
              {
                  'Name': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          NextToken='string',
          MaxRecords=123
      )
    :type Filters: list
    :param Filters: 

      A filter used to scope the tags to return.

      

    
      - *(dict) --* 

        Describes a filter.

        

      
        - **Name** *(string) --* 

          The name of the filter. The valid values are: ``"auto-scaling-group"`` , ``"key"`` , ``"value"`` , and ``"propagate-at-launch"`` .

          

        
        - **Values** *(list) --* 

          The value of the filter.

          

        
          - *(string) --* 

          
      
      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tags': [
                {
                    'ResourceId': 'string',
                    'ResourceType': 'string',
                    'Key': 'string',
                    'Value': 'string',
                    'PropagateAtLaunch': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Tags** *(list) --* 

          One or more tags.

          
          

          - *(dict) --* 

            Describes a tag for an Auto Scaling group.

            
            

            - **ResourceId** *(string) --* 

              The name of the group.

              
            

            - **ResourceType** *(string) --* 

              The type of resource. The only supported value is ``auto-scaling-group`` .

              
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The tag value.

              
            

            - **PropagateAtLaunch** *(boolean) --* 

              Determines whether the tag is added to new instances as they are launched in the group.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

    **Examples** 

    This example describes the tags for the specified Auto Scaling group.
    ::

      response = client.describe_tags(
          Filters=[
              {
                  'Name': 'auto-scaling-group',
                  'Values': [
                      'my-auto-scaling-group',
                  ],
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Tags': [
              {
                  'Key': 'Dept',
                  'PropagateAtLaunch': True,
                  'ResourceId': 'my-auto-scaling-group',
                  'ResourceType': 'auto-scaling-group',
                  'Value': 'Research',
              },
              {
                  'Key': 'Role',
                  'PropagateAtLaunch': True,
                  'ResourceId': 'my-auto-scaling-group',
                  'ResourceType': 'auto-scaling-group',
                  'Value': 'WebServer',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_termination_policy_types()

    

    Describes the termination policies supported by Auto Scaling.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeTerminationPolicyTypes>`_    


    **Request Syntax** 

    ::

      response = client.describe_termination_policy_types()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TerminationPolicyTypes': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TerminationPolicyTypes** *(list) --* 

          The termination policies supported by Auto Scaling (``OldestInstance`` , ``OldestLaunchConfiguration`` , ``NewestInstance`` , ``ClosestToNextInstanceHour`` , and ``Default`` ).

          
          

          - *(string) --* 
      
    

    **Examples** 

    This example describes the available termination policy types.
    ::

      response = client.describe_termination_policy_types(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'TerminationPolicyTypes': [
              'ClosestToNextInstanceHour',
              'Default',
              'NewestInstance',
              'OldestInstance',
              'OldestLaunchConfiguration',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: detach_instances(**kwargs)

    

    Removes one or more instances from the specified Auto Scaling group.

     

    After the instances are detached, you can manage them independent of the Auto Scaling group.

     

    If you do not specify the option to decrement the desired capacity, Auto Scaling launches instances to replace the ones that are detached.

     

    If there is a Classic Load Balancer attached to the Auto Scaling group, the instances are deregistered from the load balancer. If there are target groups attached to the Auto Scaling group, the instances are deregistered from the target groups.

     

    For more information, see `Detach EC2 Instances from Your Auto Scaling Group <http://docs.aws.amazon.com/autoscaling/latest/userguide/detach-instance-asg.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DetachInstances>`_    


    **Request Syntax** 
    ::

      response = client.detach_instances(
          InstanceIds=[
              'string',
          ],
          AutoScalingGroupName='string',
          ShouldDecrementDesiredCapacity=True|False
      )
    :type InstanceIds: list
    :param InstanceIds: 

      One or more instance IDs.

      

    
      - *(string) --* 

      
  
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: **[REQUIRED]** 

      If ``True`` , the Auto Scaling group decrements the desired capacity value by the number of instances detached.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Activities': [
                {
                    'ActivityId': 'string',
                    'AutoScalingGroupName': 'string',
                    'Description': 'string',
                    'Cause': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                    'StatusMessage': 'string',
                    'Progress': 123,
                    'Details': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Activities** *(list) --* 

          The activities related to detaching the instances from the Auto Scaling group.

          
          

          - *(dict) --* 

            Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

            
            

            - **ActivityId** *(string) --* 

              The ID of the activity.

              
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **Description** *(string) --* 

              A friendly, more verbose description of the activity.

              
            

            - **Cause** *(string) --* 

              The reason the activity began.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the activity.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the activity.

              
            

            - **StatusCode** *(string) --* 

              The current status of the activity.

              
            

            - **StatusMessage** *(string) --* 

              A friendly, more verbose description of the activity status.

              
            

            - **Progress** *(integer) --* 

              A value between 0 and 100 that indicates the progress of the activity.

              
            

            - **Details** *(string) --* 

              The details about the activity.

              
        
      
    

    **Examples** 

    This example detaches the specified instance from the specified Auto Scaling group.
    ::

      response = client.detach_instances(
          AutoScalingGroupName='my-auto-scaling-group',
          InstanceIds=[
              'i-93633f9b',
          ],
          ShouldDecrementDesiredCapacity=True,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Activities': [
              {
                  'ActivityId': '5091cb52-547a-47ce-a236-c9ccbc2cb2c9',
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'Cause': 'At 2015-04-12T15:02:16Z instance i-93633f9b was detached in response to a user request, shrinking the capacity from 2 to 1.',
                  'Description': 'Detaching EC2 instance: i-93633f9b',
                  'Details': 'details',
                  'Progress': 50,
                  'StartTime': datetime(2015, 4, 12, 15, 2, 16, 6, 102, 0),
                  'StatusCode': 'InProgress',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: detach_load_balancer_target_groups(**kwargs)

    

    Detaches one or more target groups from the specified Auto Scaling group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups>`_    


    **Request Syntax** 
    ::

      response = client.detach_load_balancer_target_groups(
          AutoScalingGroupName='string',
          TargetGroupARNs=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type TargetGroupARNs: list
    :param TargetGroupARNs: **[REQUIRED]** 

      The Amazon Resource Names (ARN) of the target groups.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example detaches the specified target group from the specified Auto Scaling group
    ::

      response = client.detach_load_balancer_target_groups(
          AutoScalingGroupName='my-auto-scaling-group',
          TargetGroupARNs=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: detach_load_balancers(**kwargs)

    

    Detaches one or more Classic Load Balancers from the specified Auto Scaling group.

     

    Note that this operation detaches only Classic Load Balancers. If you have Application Load Balancers, use  DetachLoadBalancerTargetGroups instead.

     

    When you detach a load balancer, it enters the ``Removing`` state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the load balancer using  DescribeLoadBalancers . Note that the instances remain running.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DetachLoadBalancers>`_    


    **Request Syntax** 
    ::

      response = client.detach_load_balancers(
          AutoScalingGroupName='string',
          LoadBalancerNames=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: **[REQUIRED]** 

      One or more load balancer names.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example detaches the specified load balancer from the specified Auto Scaling group.
    ::

      response = client.detach_load_balancers(
          AutoScalingGroupName='my-auto-scaling-group',
          LoadBalancerNames=[
              'my-load-balancer',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: disable_metrics_collection(**kwargs)

    

    Disables group metrics for the specified Auto Scaling group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DisableMetricsCollection>`_    


    **Request Syntax** 
    ::

      response = client.disable_metrics_collection(
          AutoScalingGroupName='string',
          Metrics=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type Metrics: list
    :param Metrics: 

      One or more of the following metrics. If you omit this parameter, all metrics are disabled.

       

       
      * ``GroupMinSize``   
       
      * ``GroupMaxSize``   
       
      * ``GroupDesiredCapacity``   
       
      * ``GroupInServiceInstances``   
       
      * ``GroupPendingInstances``   
       
      * ``GroupStandbyInstances``   
       
      * ``GroupTerminatingInstances``   
       
      * ``GroupTotalInstances``   
       

      

    
      - *(string) --* 

      
  
    
    :returns: None

    **Examples** 

    This example disables collecting data for the GroupDesiredCapacity metric for the specified Auto Scaling group.
    ::

      response = client.disable_metrics_collection(
          AutoScalingGroupName='my-auto-scaling-group',
          Metrics=[
              'GroupDesiredCapacity',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: enable_metrics_collection(**kwargs)

    

    Enables group metrics for the specified Auto Scaling group. For more information, see `Monitoring Your Auto Scaling Groups and Instances <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/EnableMetricsCollection>`_    


    **Request Syntax** 
    ::

      response = client.enable_metrics_collection(
          AutoScalingGroupName='string',
          Metrics=[
              'string',
          ],
          Granularity='string'
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type Metrics: list
    :param Metrics: 

      One or more of the following metrics. If you omit this parameter, all metrics are enabled.

       

       
      * ``GroupMinSize``   
       
      * ``GroupMaxSize``   
       
      * ``GroupDesiredCapacity``   
       
      * ``GroupInServiceInstances``   
       
      * ``GroupPendingInstances``   
       
      * ``GroupStandbyInstances``   
       
      * ``GroupTerminatingInstances``   
       
      * ``GroupTotalInstances``   
       

      

    
      - *(string) --* 

      
  
    :type Granularity: string
    :param Granularity: **[REQUIRED]** 

      The granularity to associate with the metrics to collect. The only valid value is ``1Minute`` .

      

    
    
    :returns: None

    **Examples** 

    This example enables data collection for the specified Auto Scaling group.
    ::

      response = client.enable_metrics_collection(
          AutoScalingGroupName='my-auto-scaling-group',
          Granularity='1Minute',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: enter_standby(**kwargs)

    

    Moves the specified instances into the standby state.

     

    For more information, see `Temporarily Removing Instances from Your Auto Scaling Group <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-enter-exit-standby.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/EnterStandby>`_    


    **Request Syntax** 
    ::

      response = client.enter_standby(
          InstanceIds=[
              'string',
          ],
          AutoScalingGroupName='string',
          ShouldDecrementDesiredCapacity=True|False
      )
    :type InstanceIds: list
    :param InstanceIds: 

      One or more instances to move into ``Standby`` mode. You must specify at least one instance ID.

      

    
      - *(string) --* 

      
  
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: **[REQUIRED]** 

      Specifies whether the instances moved to ``Standby`` mode count as part of the Auto Scaling group's desired capacity. If set, the desired capacity for the Auto Scaling group decrements by the number of instances moved to ``Standby`` mode.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Activities': [
                {
                    'ActivityId': 'string',
                    'AutoScalingGroupName': 'string',
                    'Description': 'string',
                    'Cause': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                    'StatusMessage': 'string',
                    'Progress': 123,
                    'Details': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Activities** *(list) --* 

          The activities related to moving instances into ``Standby`` mode.

          
          

          - *(dict) --* 

            Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

            
            

            - **ActivityId** *(string) --* 

              The ID of the activity.

              
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **Description** *(string) --* 

              A friendly, more verbose description of the activity.

              
            

            - **Cause** *(string) --* 

              The reason the activity began.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the activity.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the activity.

              
            

            - **StatusCode** *(string) --* 

              The current status of the activity.

              
            

            - **StatusMessage** *(string) --* 

              A friendly, more verbose description of the activity status.

              
            

            - **Progress** *(integer) --* 

              A value between 0 and 100 that indicates the progress of the activity.

              
            

            - **Details** *(string) --* 

              The details about the activity.

              
        
      
    

    **Examples** 

    This example puts the specified instance into standby mode.
    ::

      response = client.enter_standby(
          AutoScalingGroupName='my-auto-scaling-group',
          InstanceIds=[
              'i-93633f9b',
          ],
          ShouldDecrementDesiredCapacity=True,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Activities': [
              {
                  'ActivityId': 'ffa056b4-6ed3-41ba-ae7c-249dfae6eba1',
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'Cause': 'At 2015-04-12T15:10:23Z instance i-93633f9b was moved to standby in response to a user request, shrinking the capacity from 2 to 1.',
                  'Description': 'Moving EC2 instance to Standby: i-93633f9b',
                  'Details': 'details',
                  'Progress': 50,
                  'StartTime': datetime(2015, 4, 12, 15, 10, 23, 6, 102, 0),
                  'StatusCode': 'InProgress',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: execute_policy(**kwargs)

    

    Executes the specified policy.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/ExecutePolicy>`_    


    **Request Syntax** 
    ::

      response = client.execute_policy(
          AutoScalingGroupName='string',
          PolicyName='string',
          HonorCooldown=True|False,
          MetricValue=123.0,
          BreachThreshold=123.0
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: 

      The name of the Auto Scaling group.

      

    
    :type PolicyName: string
    :param PolicyName: **[REQUIRED]** 

      The name or ARN of the policy.

      

    
    :type HonorCooldown: boolean
    :param HonorCooldown: 

      If this parameter is true, Auto Scaling waits for the cooldown period to complete before executing the policy. Otherwise, Auto Scaling executes the policy without waiting for the cooldown period to complete.

       

      This parameter is not supported if the policy type is ``StepScaling`` .

       

      For more information, see `Auto Scaling Cooldowns <http://docs.aws.amazon.com/autoscaling/latest/userguide/Cooldown.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type MetricValue: float
    :param MetricValue: 

      The metric value to compare to ``BreachThreshold`` . This enables you to execute a policy of type ``StepScaling`` and determine which step adjustment to use. For example, if the breach threshold is 50 and you want to use a step adjustment with a lower bound of 0 and an upper bound of 10, you can set the metric value to 59.

       

      If you specify a metric value that doesn't correspond to a step adjustment for the policy, the call returns an error.

       

      This parameter is required if the policy type is ``StepScaling`` and not supported otherwise.

      

    
    :type BreachThreshold: float
    :param BreachThreshold: 

      The breach threshold for the alarm.

       

      This parameter is required if the policy type is ``StepScaling`` and not supported otherwise.

      

    
    
    :returns: None

    **Examples** 

    This example executes the specified Auto Scaling policy for the specified Auto Scaling group.
    ::

      response = client.execute_policy(
          AutoScalingGroupName='my-auto-scaling-group',
          HonorCooldown=True,
          PolicyName='ScaleIn',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: exit_standby(**kwargs)

    

    Moves the specified instances out of the standby state.

     

    For more information, see `Temporarily Removing Instances from Your Auto Scaling Group <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-enter-exit-standby.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/ExitStandby>`_    


    **Request Syntax** 
    ::

      response = client.exit_standby(
          InstanceIds=[
              'string',
          ],
          AutoScalingGroupName='string'
      )
    :type InstanceIds: list
    :param InstanceIds: 

      One or more instance IDs. You must specify at least one instance ID.

      

    
      - *(string) --* 

      
  
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Activities': [
                {
                    'ActivityId': 'string',
                    'AutoScalingGroupName': 'string',
                    'Description': 'string',
                    'Cause': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                    'StatusMessage': 'string',
                    'Progress': 123,
                    'Details': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Activities** *(list) --* 

          The activities related to moving instances out of ``Standby`` mode.

          
          

          - *(dict) --* 

            Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

            
            

            - **ActivityId** *(string) --* 

              The ID of the activity.

              
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **Description** *(string) --* 

              A friendly, more verbose description of the activity.

              
            

            - **Cause** *(string) --* 

              The reason the activity began.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the activity.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the activity.

              
            

            - **StatusCode** *(string) --* 

              The current status of the activity.

              
            

            - **StatusMessage** *(string) --* 

              A friendly, more verbose description of the activity status.

              
            

            - **Progress** *(integer) --* 

              A value between 0 and 100 that indicates the progress of the activity.

              
            

            - **Details** *(string) --* 

              The details about the activity.

              
        
      
    

    **Examples** 

    This example moves the specified instance out of standby mode.
    ::

      response = client.exit_standby(
          AutoScalingGroupName='my-auto-scaling-group',
          InstanceIds=[
              'i-93633f9b',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Activities': [
              {
                  'ActivityId': '142928e1-a2dc-453a-9b24-b85ad6735928',
                  'AutoScalingGroupName': 'my-auto-scaling-group',
                  'Cause': 'At 2015-04-12T15:14:29Z instance i-93633f9b was moved out of standby in response to a user request, increasing the capacity from 1 to 2.',
                  'Description': 'Moving EC2 instance out of Standby: i-93633f9b',
                  'Details': 'details',
                  'Progress': 30,
                  'StartTime': datetime(2015, 4, 12, 15, 14, 29, 6, 102, 0),
                  'StatusCode': 'PreInService',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: generate_presigned_url(ClientMethod, Params=None, ExpiresIn=3600, HttpMethod=None)

        
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for
    
    :type Params: dict
    :param Params: The parameters normally passed to
        ``ClientMethod``.
    
    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
        for. By default it expires in an hour (3600 seconds)
    
    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
        default, the http method is whatever is used in the method's model.
    
    :returns: The presigned url


  .. py:method:: get_paginator(operation_name)

        
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name.  This is the same name
        as the method name on the client.  For example, if the
        method name is ``create_foo``, and you'd normally invoke the
        operation as ``client.create_foo(**kwargs)``, if the
        ``create_foo`` operation can be paginated, you can use the
        call ``client.get_paginator("create_foo")``.
    
    :raise OperationNotPageableError: Raised if the operation is not
        pageable.  You can use the ``client.can_paginate`` method to
        check if an operation is pageable.
    
    :rtype: L{botocore.paginate.Paginator}
    :return: A paginator object.


  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: put_lifecycle_hook(**kwargs)

    

    Creates or updates a lifecycle hook for the specified Auto Scaling Group.

     

    A lifecycle hook tells Auto Scaling that you want to perform an action on an instance that is not actively in service; for example, either when the instance launches or before the instance terminates.

     

    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:

     

     
    * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Auto Scaling launches or terminates instances. 
     
    * (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Auto Scaling to publish lifecycle notifications to the target. 
     
    * **Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.**   
     
    * If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state. 
     
    * If you finish before the timeout period ends, complete the lifecycle action. 
     

     

    For more information, see `Auto Scaling Lifecycle Hooks <http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html>`__ in the *Auto Scaling User Guide* .

     

    If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails. For information about updating this limit, see `AWS Service Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>`__ in the *Amazon Web Services General Reference* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutLifecycleHook>`_    


    **Request Syntax** 
    ::

      response = client.put_lifecycle_hook(
          LifecycleHookName='string',
          AutoScalingGroupName='string',
          LifecycleTransition='string',
          RoleARN='string',
          NotificationTargetARN='string',
          NotificationMetadata='string',
          HeartbeatTimeout=123,
          DefaultResult='string'
      )
    :type LifecycleHookName: string
    :param LifecycleHookName: **[REQUIRED]** 

      The name of the lifecycle hook.

      

    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type LifecycleTransition: string
    :param LifecycleTransition: 

      The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see  DescribeLifecycleHookTypes .

       

      This parameter is required for new lifecycle hooks, but optional when updating existing hooks.

      

    
    :type RoleARN: string
    :param RoleARN: 

      The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

       

      This parameter is required for new lifecycle hooks, but optional when updating existing hooks.

      

    
    :type NotificationTargetARN: string
    :param NotificationTargetARN: 

      The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This target can be either an SQS queue or an SNS topic. If you specify an empty string, this overrides the current ARN.

       

      This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key/value pair format when sending notifications to an Amazon SNS topic.

       

      When you specify a notification target, Auto Scaling sends it a test message. Test messages contains the following additional key/value pair: ``"Event": "autoscaling:TEST_NOTIFICATION"`` .

      

    
    :type NotificationMetadata: string
    :param NotificationMetadata: 

      Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.

      

    
    :type HeartbeatTimeout: integer
    :param HeartbeatTimeout: 

      The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default is 3600 seconds (1 hour).

       

      If the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling  RecordLifecycleActionHeartbeat .

      

    
    :type DefaultResult: string
    :param DefaultResult: 

      Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. This parameter can be either ``CONTINUE`` or ``ABANDON`` . The default value is ``ABANDON`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example creates a lifecycle hook.
    ::

      response = client.put_lifecycle_hook(
          AutoScalingGroupName='my-auto-scaling-group',
          LifecycleHookName='my-lifecycle-hook',
          LifecycleTransition='autoscaling:EC2_INSTANCE_LAUNCHING',
          NotificationTargetARN='arn:aws:sns:us-west-2:123456789012:my-sns-topic --role-arn',
          RoleARN='arn:aws:iam::123456789012:role/my-auto-scaling-role',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: put_notification_configuration(**kwargs)

    

    Configures an Auto Scaling group to send notifications when specified events take place. Subscribers to the specified topic can have messages delivered to an endpoint such as a web server or an email address.

     

    This configuration overwrites any existing configuration.

     

    For more information see `Getting SNS Notifications When Your Auto Scaling Group Scales <http://docs.aws.amazon.com/autoscaling/latest/userguide/ASGettingNotifications.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutNotificationConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.put_notification_configuration(
          AutoScalingGroupName='string',
          TopicARN='string',
          NotificationTypes=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type TopicARN: string
    :param TopicARN: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.

      

    
    :type NotificationTypes: list
    :param NotificationTypes: **[REQUIRED]** 

      The type of event that will cause the notification to be sent. For details about notification types supported by Auto Scaling, see  DescribeAutoScalingNotificationTypes .

      

    
      - *(string) --* 

      
  
    
    :returns: None

    **Examples** 

    This example adds the specified notification to the specified Auto Scaling group.
    ::

      response = client.put_notification_configuration(
          AutoScalingGroupName='my-auto-scaling-group',
          NotificationTypes=[
              'autoscaling:TEST_NOTIFICATION',
          ],
          TopicARN='arn:aws:sns:us-west-2:123456789012:my-sns-topic',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: put_scaling_policy(**kwargs)

    

    Creates or updates a policy for an Auto Scaling group. To update an existing policy, use the existing policy name and set the parameters you want to change. Any existing parameter not changed in an update to an existing policy is not changed in this update request.

     

    If you exceed your maximum limit of step adjustments, which by default is 20 per region, the call fails. For information about updating this limit, see `AWS Service Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>`__ in the *Amazon Web Services General Reference* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutScalingPolicy>`_    


    **Request Syntax** 
    ::

      response = client.put_scaling_policy(
          AutoScalingGroupName='string',
          PolicyName='string',
          PolicyType='string',
          AdjustmentType='string',
          MinAdjustmentStep=123,
          MinAdjustmentMagnitude=123,
          ScalingAdjustment=123,
          Cooldown=123,
          MetricAggregationType='string',
          StepAdjustments=[
              {
                  'MetricIntervalLowerBound': 123.0,
                  'MetricIntervalUpperBound': 123.0,
                  'ScalingAdjustment': 123
              },
          ],
          EstimatedInstanceWarmup=123,
          TargetTrackingConfiguration={
              'PredefinedMetricSpecification': {
                  'PredefinedMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'ALBRequestCountPerTarget',
                  'ResourceLabel': 'string'
              },
              'CustomizedMetricSpecification': {
                  'MetricName': 'string',
                  'Namespace': 'string',
                  'Dimensions': [
                      {
                          'Name': 'string',
                          'Value': 'string'
                      },
                  ],
                  'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                  'Unit': 'string'
              },
              'TargetValue': 123.0,
              'DisableScaleIn': True|False
          }
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type PolicyName: string
    :param PolicyName: **[REQUIRED]** 

      The name of the policy.

      

    
    :type PolicyType: string
    :param PolicyType: 

      The policy type. The valid values are ``SimpleScaling`` , ``StepScaling`` , and ``TargetTrackingScaling`` . If the policy type is null, the value is treated as ``SimpleScaling`` .

      

    
    :type AdjustmentType: string
    :param AdjustmentType: 

      The adjustment type. The valid values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .

       

      This parameter is supported if the policy type is ``SimpleScaling`` or ``StepScaling`` .

       

      For more information, see `Dynamic Scaling <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-scale-based-on-demand.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type MinAdjustmentStep: integer
    :param MinAdjustmentStep: 

      Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.

      

    
    :type MinAdjustmentMagnitude: integer
    :param MinAdjustmentMagnitude: 

      The minimum number of instances to scale. If the value of ``AdjustmentType`` is ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the Auto Scaling group by at least this many instances. Otherwise, the error is ``ValidationError`` .

       

      This parameter is supported if the policy type is ``SimpleScaling`` or ``StepScaling`` .

      

    
    :type ScalingAdjustment: integer
    :param ScalingAdjustment: 

      The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.

       

      This parameter is required if the policy type is ``SimpleScaling`` and not supported otherwise.

      

    
    :type Cooldown: integer
    :param Cooldown: 

      The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start. If this parameter is not specified, the default cooldown period for the group applies.

       

      This parameter is supported if the policy type is ``SimpleScaling`` .

       

      For more information, see `Auto Scaling Cooldowns <http://docs.aws.amazon.com/autoscaling/latest/userguide/Cooldown.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type MetricAggregationType: string
    :param MetricAggregationType: 

      The aggregation type for the CloudWatch metrics. The valid values are ``Minimum`` , ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated as ``Average`` .

       

      This parameter is supported if the policy type is ``StepScaling`` .

      

    
    :type StepAdjustments: list
    :param StepAdjustments: 

      A set of adjustments that enable you to scale based on the size of the alarm breach.

       

      This parameter is required if the policy type is ``StepScaling`` and not supported otherwise.

      

    
      - *(dict) --* 

        Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you've defined for the alarm.

         

        For the following examples, suppose that you have an alarm with a breach threshold of 50:

         

         
        * If you want the adjustment to be triggered when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10. 
         
        * If you want the adjustment to be triggered when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0. 
         

         

        There are a few rules for the step adjustments for your step policy:

         

         
        * The ranges of your step adjustments can't overlap or have a gap. 
         
        * At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound. 
         
        * At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound. 
         
        * The upper and lower bound can't be null in the same step adjustment. 
         

        

      
        - **MetricIntervalLowerBound** *(float) --* 

          The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.

          

        
        - **MetricIntervalUpperBound** *(float) --* 

          The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.

           

          The upper bound must be greater than the lower bound.

          

        
        - **ScalingAdjustment** *(integer) --* **[REQUIRED]** 

          The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.

          

        
      
  
    :type EstimatedInstanceWarmup: integer
    :param EstimatedInstanceWarmup: 

      The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. The default is to use the value specified for the default cooldown period for the group.

       

      This parameter is supported if the policy type is ``StepScaling`` or ``TargetTrackingScaling`` .

      

    
    :type TargetTrackingConfiguration: dict
    :param TargetTrackingConfiguration: 

      A target tracking policy.

       

      This parameter is required if the policy type is ``TargetTrackingScaling`` and not supported otherwise.

      

    
      - **PredefinedMetricSpecification** *(dict) --* 

        A predefined metric. You can specify either a predefined metric or a customized metric.

        

      
        - **PredefinedMetricType** *(string) --* **[REQUIRED]** 

          The metric type.

          

        
        - **ResourceLabel** *(string) --* 

          Identifies the resource associated with the metric type. The following predefined metrics are available:

           

           
          * ``ASGAverageCPUUtilization`` - average CPU utilization of the Auto Scaling group 
           
          * ``ASGAverageNetworkIn`` - average number of bytes received on all network interfaces by the Auto Scaling group 
           
          * ``ASGAverageNetworkOut`` - average number of bytes sent out on all network interfaces by the Auto Scaling group 
           
          * ``ALBRequestCountPerTarget`` - number of requests completed per target in an Application Load Balancer target group 
           

           

          For predefined metric types ``ASGAverageCPUUtilization`` , ``ASGAverageNetworkIn`` , and ``ASGAverageNetworkOut`` , the parameter must not be specified as the resource associated with the metric type is the Auto Scaling group. For predefined metric type ``ALBRequestCountPerTarget`` , the parameter must be specified in the format: ``app/*load-balancer-name* /*load-balancer-id* /targetgroup/*target-group-name* /*target-group-id* `` , where ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load balancer ARN, and ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the target group ARN. The target group must be attached to the Auto Scaling group.

          

        
      
      - **CustomizedMetricSpecification** *(dict) --* 

        A customized metric.

        

      
        - **MetricName** *(string) --* **[REQUIRED]** 

          The name of the metric.

          

        
        - **Namespace** *(string) --* **[REQUIRED]** 

          The namespace of the metric.

          

        
        - **Dimensions** *(list) --* 

          The dimensions of the metric.

          

        
          - *(dict) --* 

            Describes the dimension of a metric.

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the dimension.

              

            
            - **Value** *(string) --* **[REQUIRED]** 

              The value of the dimension.

              

            
          
      
        - **Statistic** *(string) --* **[REQUIRED]** 

          The statistic of the metric.

          

        
        - **Unit** *(string) --* 

          The unit of the metric.

          

        
      
      - **TargetValue** *(float) --* **[REQUIRED]** 

        The target value for the metric.

        

      
      - **DisableScaleIn** *(boolean) --* 

        Indicates whether scale in by the target tracking policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking policy won't remove instances from the Auto Scaling group. Otherwise, scale in is enabled and the target tracking policy can remove instances from the Auto Scaling group. The default value is ``false`` .

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PolicyARN': 'string',
            'Alarms': [
                {
                    'AlarmName': 'string',
                    'AlarmARN': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of PutScalingPolicy.

        
        

        - **PolicyARN** *(string) --* 

          The Amazon Resource Name (ARN) of the policy.

          
        

        - **Alarms** *(list) --* 

          The CloudWatch alarms created for the target tracking policy.

          
          

          - *(dict) --* 

            Describes an alarm.

            
            

            - **AlarmName** *(string) --* 

              The name of the alarm.

              
            

            - **AlarmARN** *(string) --* 

              The Amazon Resource Name (ARN) of the alarm.

              
        
      
    

    **Examples** 

    This example adds the specified policy to the specified Auto Scaling group.
    ::

      response = client.put_scaling_policy(
          AdjustmentType='ChangeInCapacity',
          AutoScalingGroupName='my-auto-scaling-group',
          PolicyName='ScaleIn',
          ScalingAdjustment=-1,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'PolicyARN': 'arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:2233f3d7-6290-403b-b632-93c553560106:autoScalingGroupName/my-auto-scaling-group:policyName/ScaleIn',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: put_scheduled_update_group_action(**kwargs)

    

    Creates or updates a scheduled scaling action for an Auto Scaling group. When updating a scheduled scaling action, if you leave a parameter unspecified, the corresponding value remains unchanged.

     

    For more information, see `Scheduled Scaling <http://docs.aws.amazon.com/autoscaling/latest/userguide/schedule_time.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutScheduledUpdateGroupAction>`_    


    **Request Syntax** 
    ::

      response = client.put_scheduled_update_group_action(
          AutoScalingGroupName='string',
          ScheduledActionName='string',
          Time=datetime(2015, 1, 1),
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          Recurrence='string',
          MinSize=123,
          MaxSize=123,
          DesiredCapacity=123
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type ScheduledActionName: string
    :param ScheduledActionName: **[REQUIRED]** 

      The name of this scaling action.

      

    
    :type Time: datetime
    :param Time: 

      This parameter is deprecated.

      

    
    :type StartTime: datetime
    :param StartTime: 

      The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, ``2014-06-01T00:00:00Z`` ).

       

      If you specify ``Recurrence`` and ``StartTime`` , Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.

       

      If you try to schedule your action in the past, Auto Scaling returns an error message.

      

    
    :type EndTime: datetime
    :param EndTime: 

      The time for the recurring schedule to end. Auto Scaling does not perform the action after this time.

      

    
    :type Recurrence: string
    :param Recurrence: 

      The recurring schedule for this action, in Unix cron syntax format. For more information, see `Cron <http://en.wikipedia.org/wiki/Cron>`__ in Wikipedia.

      

    
    :type MinSize: integer
    :param MinSize: 

      The minimum size for the Auto Scaling group.

      

    
    :type MaxSize: integer
    :param MaxSize: 

      The maximum size for the Auto Scaling group.

      

    
    :type DesiredCapacity: integer
    :param DesiredCapacity: 

      The number of EC2 instances that should be running in the group.

      

    
    
    :returns: None

    **Examples** 

    This example adds the specified scheduled action to the specified Auto Scaling group.
    ::

      response = client.put_scheduled_update_group_action(
          AutoScalingGroupName='my-auto-scaling-group',
          DesiredCapacity=4,
          EndTime=datetime(2014, 5, 12, 8, 0, 0, 0, 132, 0),
          MaxSize=6,
          MinSize=2,
          ScheduledActionName='my-scheduled-action',
          StartTime=datetime(2014, 5, 12, 8, 0, 0, 0, 132, 0),
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: record_lifecycle_action_heartbeat(**kwargs)

    

    Records a heartbeat for the lifecycle action associated with the specified token or instance. This extends the timeout by the length of time defined using  PutLifecycleHook .

     

    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:

     

     
    * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Auto Scaling launches or terminates instances. 
     
    * (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Auto Scaling to publish lifecycle notifications to the target. 
     
    * Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate. 
     
    * **If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state.**   
     
    * If you finish before the timeout period ends, complete the lifecycle action. 
     

     

    For more information, see `Auto Scaling Lifecycle <http://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroupLifecycle.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/RecordLifecycleActionHeartbeat>`_    


    **Request Syntax** 
    ::

      response = client.record_lifecycle_action_heartbeat(
          LifecycleHookName='string',
          AutoScalingGroupName='string',
          LifecycleActionToken='string',
          InstanceId='string'
      )
    :type LifecycleHookName: string
    :param LifecycleHookName: **[REQUIRED]** 

      The name of the lifecycle hook.

      

    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type LifecycleActionToken: string
    :param LifecycleActionToken: 

      A token that uniquely identifies a specific lifecycle action associated with an instance. Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.

      

    
    :type InstanceId: string
    :param InstanceId: 

      The ID of the instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example records a lifecycle action heartbeat to keep the instance in a pending state.
    ::

      response = client.record_lifecycle_action_heartbeat(
          AutoScalingGroupName='my-auto-scaling-group',
          LifecycleActionToken='bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635',
          LifecycleHookName='my-lifecycle-hook',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: resume_processes(**kwargs)

    

    Resumes the specified suspended Auto Scaling processes, or all suspended process, for the specified Auto Scaling group.

     

    For more information, see `Suspending and Resuming Auto Scaling Processes <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-suspend-resume-processes.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/ResumeProcesses>`_    


    **Request Syntax** 
    ::

      response = client.resume_processes(
          AutoScalingGroupName='string',
          ScalingProcesses=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type ScalingProcesses: list
    :param ScalingProcesses: 

      One or more of the following processes. If you omit this parameter, all processes are specified.

       

       
      * ``Launch``   
       
      * ``Terminate``   
       
      * ``HealthCheck``   
       
      * ``ReplaceUnhealthy``   
       
      * ``AZRebalance``   
       
      * ``AlarmNotification``   
       
      * ``ScheduledActions``   
       
      * ``AddToLoadBalancer``   
       

      

    
      - *(string) --* 

      
  
    
    :returns: None

    **Examples** 

    This example resumes the specified suspended scaling process for the specified Auto Scaling group.
    ::

      response = client.resume_processes(
          AutoScalingGroupName='my-auto-scaling-group',
          ScalingProcesses=[
              'AlarmNotification',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_desired_capacity(**kwargs)

    

    Sets the size of the specified Auto Scaling group.

     

    For more information about desired capacity, see `What Is Auto Scaling? <http://docs.aws.amazon.com/autoscaling/latest/userguide/WhatIsAutoScaling.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/SetDesiredCapacity>`_    


    **Request Syntax** 
    ::

      response = client.set_desired_capacity(
          AutoScalingGroupName='string',
          DesiredCapacity=123,
          HonorCooldown=True|False
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type DesiredCapacity: integer
    :param DesiredCapacity: **[REQUIRED]** 

      The number of EC2 instances that should be running in the Auto Scaling group.

      

    
    :type HonorCooldown: boolean
    :param HonorCooldown: 

      By default, ``SetDesiredCapacity`` overrides any cooldown period associated with the Auto Scaling group. Specify ``True`` to make Auto Scaling to wait for the cool-down period associated with the Auto Scaling group to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity.

      

    
    
    :returns: None

    **Examples** 

    This example sets the desired capacity for the specified Auto Scaling group.
    ::

      response = client.set_desired_capacity(
          AutoScalingGroupName='my-auto-scaling-group',
          DesiredCapacity=2,
          HonorCooldown=True,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_instance_health(**kwargs)

    

    Sets the health status of the specified instance.

     

    For more information, see `Health Checks <http://docs.aws.amazon.com/autoscaling/latest/userguide/healthcheck.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/SetInstanceHealth>`_    


    **Request Syntax** 
    ::

      response = client.set_instance_health(
          InstanceId='string',
          HealthStatus='string',
          ShouldRespectGracePeriod=True|False
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The ID of the instance.

      

    
    :type HealthStatus: string
    :param HealthStatus: **[REQUIRED]** 

      The health status of the instance. Set to ``Healthy`` if you want the instance to remain in service. Set to ``Unhealthy`` if you want the instance to be out of service. Auto Scaling will terminate and replace the unhealthy instance.

      

    
    :type ShouldRespectGracePeriod: boolean
    :param ShouldRespectGracePeriod: 

      If the Auto Scaling group of the specified instance has a ``HealthCheckGracePeriod`` specified for the group, by default, this call will respect the grace period. Set this to ``False`` , if you do not want the call to respect the grace period associated with the group.

       

      For more information, see the description of the health check grace period for  CreateAutoScalingGroup .

      

    
    
    :returns: None

    **Examples** 

    This example sets the health status of the specified instance to Unhealthy.
    ::

      response = client.set_instance_health(
          HealthStatus='Unhealthy',
          InstanceId='i-93633f9b',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_instance_protection(**kwargs)

    

    Updates the instance protection settings of the specified instances.

     

    For more information, see `Instance Protection <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-termination.html#instance-protection>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/SetInstanceProtection>`_    


    **Request Syntax** 
    ::

      response = client.set_instance_protection(
          InstanceIds=[
              'string',
          ],
          AutoScalingGroupName='string',
          ProtectedFromScaleIn=True|False
      )
    :type InstanceIds: list
    :param InstanceIds: **[REQUIRED]** 

      One or more instance IDs.

      

    
      - *(string) --* 

      
  
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type ProtectedFromScaleIn: boolean
    :param ProtectedFromScaleIn: **[REQUIRED]** 

      Indicates whether the instance is protected from termination by Auto Scaling when scaling in.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example enables instance protection for the specified instance.
    ::

      response = client.set_instance_protection(
          AutoScalingGroupName='my-auto-scaling-group',
          InstanceIds=[
              'i-93633f9b',
          ],
          ProtectedFromScaleIn=True,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example disables instance protection for the specified instance.
    ::

      response = client.set_instance_protection(
          AutoScalingGroupName='my-auto-scaling-group',
          InstanceIds=[
              'i-93633f9b',
          ],
          ProtectedFromScaleIn=False,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: suspend_processes(**kwargs)

    

    Suspends the specified Auto Scaling processes, or all processes, for the specified Auto Scaling group.

     

    Note that if you suspend either the ``Launch`` or ``Terminate`` process types, it can prevent other process types from functioning properly.

     

    To resume processes that have been suspended, use  ResumeProcesses .

     

    For more information, see `Suspending and Resuming Auto Scaling Processes <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-suspend-resume-processes.html>`__ in the *Auto Scaling User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/SuspendProcesses>`_    


    **Request Syntax** 
    ::

      response = client.suspend_processes(
          AutoScalingGroupName='string',
          ScalingProcesses=[
              'string',
          ]
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type ScalingProcesses: list
    :param ScalingProcesses: 

      One or more of the following processes. If you omit this parameter, all processes are specified.

       

       
      * ``Launch``   
       
      * ``Terminate``   
       
      * ``HealthCheck``   
       
      * ``ReplaceUnhealthy``   
       
      * ``AZRebalance``   
       
      * ``AlarmNotification``   
       
      * ``ScheduledActions``   
       
      * ``AddToLoadBalancer``   
       

      

    
      - *(string) --* 

      
  
    
    :returns: None

    **Examples** 

    This example suspends the specified scaling process for the specified Auto Scaling group.
    ::

      response = client.suspend_processes(
          AutoScalingGroupName='my-auto-scaling-group',
          ScalingProcesses=[
              'AlarmNotification',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: terminate_instance_in_auto_scaling_group(**kwargs)

    

    Terminates the specified instance and optionally adjusts the desired group size.

     

    This call simply makes a termination request. The instance is not terminated immediately.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup>`_    


    **Request Syntax** 
    ::

      response = client.terminate_instance_in_auto_scaling_group(
          InstanceId='string',
          ShouldDecrementDesiredCapacity=True|False
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The ID of the instance.

      

    
    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: **[REQUIRED]** 

      If ``true`` , terminating the instance also decrements the size of the Auto Scaling group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Activity': {
                'ActivityId': 'string',
                'AutoScalingGroupName': 'string',
                'Description': 'string',
                'Cause': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                'StatusMessage': 'string',
                'Progress': 123,
                'Details': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Activity** *(dict) --* 

          A scaling activity.

          
          

          - **ActivityId** *(string) --* 

            The ID of the activity.

            
          

          - **AutoScalingGroupName** *(string) --* 

            The name of the Auto Scaling group.

            
          

          - **Description** *(string) --* 

            A friendly, more verbose description of the activity.

            
          

          - **Cause** *(string) --* 

            The reason the activity began.

            
          

          - **StartTime** *(datetime) --* 

            The start time of the activity.

            
          

          - **EndTime** *(datetime) --* 

            The end time of the activity.

            
          

          - **StatusCode** *(string) --* 

            The current status of the activity.

            
          

          - **StatusMessage** *(string) --* 

            A friendly, more verbose description of the activity status.

            
          

          - **Progress** *(integer) --* 

            A value between 0 and 100 that indicates the progress of the activity.

            
          

          - **Details** *(string) --* 

            The details about the activity.

            
      
    

    **Examples** 

    This example terminates the specified instance from the specified Auto Scaling group without updating the size of the group. Auto Scaling launches a replacement instance after the specified instance terminates.
    ::

      response = client.terminate_instance_in_auto_scaling_group(
          InstanceId='i-93633f9b',
          ShouldDecrementDesiredCapacity=False,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_auto_scaling_group(**kwargs)

    

    Updates the configuration for the specified Auto Scaling group.

     

    The new settings take effect on any scaling activities after this call returns. Scaling activities that are currently in progress aren't affected.

     

    To update an Auto Scaling group with a launch configuration with ``InstanceMonitoring`` set to ``false`` , you must first disable the collection of group metrics. Otherwise, you will get an error. If you have previously enabled the collection of group metrics, you can disable it using  DisableMetricsCollection .

     

    Note the following:

     

     
    * If you specify a new value for ``MinSize`` without specifying a value for ``DesiredCapacity`` , and the new ``MinSize`` is larger than the current size of the group, we implicitly call  SetDesiredCapacity to set the size of the group to the new value of ``MinSize`` . 
     
    * If you specify a new value for ``MaxSize`` without specifying a value for ``DesiredCapacity`` , and the new ``MaxSize`` is smaller than the current size of the group, we implicitly call  SetDesiredCapacity to set the size of the group to the new value of ``MaxSize`` . 
     
    * All other optional parameters are left unchanged if not specified. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/UpdateAutoScalingGroup>`_    


    **Request Syntax** 
    ::

      response = client.update_auto_scaling_group(
          AutoScalingGroupName='string',
          LaunchConfigurationName='string',
          LaunchTemplate={
              'LaunchTemplateId': 'string',
              'LaunchTemplateName': 'string',
              'Version': 'string'
          },
          MinSize=123,
          MaxSize=123,
          DesiredCapacity=123,
          DefaultCooldown=123,
          AvailabilityZones=[
              'string',
          ],
          HealthCheckType='string',
          HealthCheckGracePeriod=123,
          PlacementGroup='string',
          VPCZoneIdentifier='string',
          TerminationPolicies=[
              'string',
          ],
          NewInstancesProtectedFromScaleIn=True|False
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: **[REQUIRED]** 

      The name of the Auto Scaling group.

      

    
    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: 

      The name of the launch configuration. You must specify either a launch configuration or a launch template.

      

    
    :type LaunchTemplate: dict
    :param LaunchTemplate: 

      The launch template to use to specify the updates. You must specify a launch configuration or a launch template.

      

    
      - **LaunchTemplateId** *(string) --* 

        The ID of the launch template. You must specify either a template ID or a template name.

        

      
      - **LaunchTemplateName** *(string) --* 

        The name of the launch template. You must specify either a template name or a template ID.

        

      
      - **Version** *(string) --* 

        The version number. By default, the default version of the launch template is used.

        

      
    
    :type MinSize: integer
    :param MinSize: 

      The minimum size of the Auto Scaling group.

      

    
    :type MaxSize: integer
    :param MaxSize: 

      The maximum size of the Auto Scaling group.

      

    
    :type DesiredCapacity: integer
    :param DesiredCapacity: 

      The number of EC2 instances that should be running in the Auto Scaling group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.

      

    
    :type DefaultCooldown: integer
    :param DefaultCooldown: 

      The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default is 300.

       

      For more information, see `Auto Scaling Cooldowns <http://docs.aws.amazon.com/autoscaling/latest/userguide/Cooldown.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type AvailabilityZones: list
    :param AvailabilityZones: 

      One or more Availability Zones for the group.

      

    
      - *(string) --* 

      
  
    :type HealthCheckType: string
    :param HealthCheckType: 

      The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` .

      

    
    :type HealthCheckGracePeriod: integer
    :param HealthCheckGracePeriod: 

      The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service. The default is 0.

       

      For more information, see `Health Checks <http://docs.aws.amazon.com/autoscaling/latest/userguide/healthcheck.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type PlacementGroup: string
    :param PlacementGroup: 

      The name of the placement group into which you'll launch your instances, if any. For more information, see `Placement Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

      

    
    :type VPCZoneIdentifier: string
    :param VPCZoneIdentifier: 

      The ID of the subnet, if you are launching into a VPC. You can specify several subnets in a comma-separated list.

       

      When you specify ``VPCZoneIdentifier`` with ``AvailabilityZones`` , ensure that the subnets' Availability Zones match the values you specify for ``AvailabilityZones`` .

       

      For more information, see `Launching Auto Scaling Instances in a VPC <http://docs.aws.amazon.com/autoscaling/latest/userguide/asg-in-vpc.html>`__ in the *Auto Scaling User Guide* .

      

    
    :type TerminationPolicies: list
    :param TerminationPolicies: 

      A standalone termination policy or a list of termination policies used to select the instance to terminate. The policies are executed in the order that they are listed.

       

      For more information, see `Controlling Which Instances Auto Scaling Terminates During Scale In <http://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-termination.html>`__ in the *Auto Scaling User Guide* .

      

    
      - *(string) --* 

      
  
    :type NewInstancesProtectedFromScaleIn: boolean
    :param NewInstancesProtectedFromScaleIn: 

      Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.

      

    
    
    :returns: None

    **Examples** 

    This example updates the launch configuration of the specified Auto Scaling group.
    ::

      response = client.update_auto_scaling_group(
          AutoScalingGroupName='my-auto-scaling-group',
          LaunchConfigurationName='new-launch-config',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example updates the minimum size and maximum size of the specified Auto Scaling group.
    ::

      response = client.update_auto_scaling_group(
          AutoScalingGroupName='my-auto-scaling-group',
          MaxSize=3,
          MinSize=1,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example enables instance protection for the specified Auto Scaling group.
    ::

      response = client.update_auto_scaling_group(
          AutoScalingGroupName='my-auto-scaling-group',
          NewInstancesProtectedFromScaleIn=True,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:

* :py:class:`AutoScaling.Paginator.DescribeAutoScalingGroups`


* :py:class:`AutoScaling.Paginator.DescribeAutoScalingInstances`


* :py:class:`AutoScaling.Paginator.DescribeLaunchConfigurations`


* :py:class:`AutoScaling.Paginator.DescribeNotificationConfigurations`


* :py:class:`AutoScaling.Paginator.DescribePolicies`


* :py:class:`AutoScaling.Paginator.DescribeScalingActivities`


* :py:class:`AutoScaling.Paginator.DescribeScheduledActions`


* :py:class:`AutoScaling.Paginator.DescribeTags`



.. py:class:: AutoScaling.Paginator.DescribeAutoScalingGroups

  ::

    
    paginator = client.get_paginator('describe_auto_scaling_groups')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_auto_scaling_groups`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingGroups>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          AutoScalingGroupNames=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type AutoScalingGroupNames: list
    :param AutoScalingGroupNames: 

      The names of the Auto Scaling groups. If you omit this parameter, all Auto Scaling groups are described.

      

    
      - *(string) --* 

      
  
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutoScalingGroups': [
                {
                    'AutoScalingGroupName': 'string',
                    'AutoScalingGroupARN': 'string',
                    'LaunchConfigurationName': 'string',
                    'LaunchTemplate': {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'Version': 'string'
                    },
                    'MinSize': 123,
                    'MaxSize': 123,
                    'DesiredCapacity': 123,
                    'DefaultCooldown': 123,
                    'AvailabilityZones': [
                        'string',
                    ],
                    'LoadBalancerNames': [
                        'string',
                    ],
                    'TargetGroupARNs': [
                        'string',
                    ],
                    'HealthCheckType': 'string',
                    'HealthCheckGracePeriod': 123,
                    'Instances': [
                        {
                            'InstanceId': 'string',
                            'AvailabilityZone': 'string',
                            'LifecycleState': 'Pending'|'Pending:Wait'|'Pending:Proceed'|'Quarantined'|'InService'|'Terminating'|'Terminating:Wait'|'Terminating:Proceed'|'Terminated'|'Detaching'|'Detached'|'EnteringStandby'|'Standby',
                            'HealthStatus': 'string',
                            'LaunchConfigurationName': 'string',
                            'LaunchTemplate': {
                                'LaunchTemplateId': 'string',
                                'LaunchTemplateName': 'string',
                                'Version': 'string'
                            },
                            'ProtectedFromScaleIn': True|False
                        },
                    ],
                    'CreatedTime': datetime(2015, 1, 1),
                    'SuspendedProcesses': [
                        {
                            'ProcessName': 'string',
                            'SuspensionReason': 'string'
                        },
                    ],
                    'PlacementGroup': 'string',
                    'VPCZoneIdentifier': 'string',
                    'EnabledMetrics': [
                        {
                            'Metric': 'string',
                            'Granularity': 'string'
                        },
                    ],
                    'Status': 'string',
                    'Tags': [
                        {
                            'ResourceId': 'string',
                            'ResourceType': 'string',
                            'Key': 'string',
                            'Value': 'string',
                            'PropagateAtLaunch': True|False
                        },
                    ],
                    'TerminationPolicies': [
                        'string',
                    ],
                    'NewInstancesProtectedFromScaleIn': True|False
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AutoScalingGroups** *(list) --* 

          The groups.

          
          

          - *(dict) --* 

            Describes an Auto Scaling group.

            
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **AutoScalingGroupARN** *(string) --* 

              The Amazon Resource Name (ARN) of the Auto Scaling group.

              
            

            - **LaunchConfigurationName** *(string) --* 

              The name of the associated launch configuration.

              
            

            - **LaunchTemplate** *(dict) --* 

              The launch template for the group.

              
              

              - **LaunchTemplateId** *(string) --* 

                The ID of the launch template. You must specify either a template ID or a template name.

                
              

              - **LaunchTemplateName** *(string) --* 

                The name of the launch template. You must specify either a template name or a template ID.

                
              

              - **Version** *(string) --* 

                The version number. By default, the default version of the launch template is used.

                
          
            

            - **MinSize** *(integer) --* 

              The minimum size of the group.

              
            

            - **MaxSize** *(integer) --* 

              The maximum size of the group.

              
            

            - **DesiredCapacity** *(integer) --* 

              The desired size of the group.

              
            

            - **DefaultCooldown** *(integer) --* 

              The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.

              
            

            - **AvailabilityZones** *(list) --* 

              One or more Availability Zones for the group.

              
              

              - *(string) --* 
          
            

            - **LoadBalancerNames** *(list) --* 

              One or more load balancers associated with the group.

              
              

              - *(string) --* 
          
            

            - **TargetGroupARNs** *(list) --* 

              The Amazon Resource Names (ARN) of the target groups for your load balancer.

              
              

              - *(string) --* 
          
            

            - **HealthCheckType** *(string) --* 

              The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` .

              
            

            - **HealthCheckGracePeriod** *(integer) --* 

              The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service.

              
            

            - **Instances** *(list) --* 

              The EC2 instances associated with the group.

              
              

              - *(dict) --* 

                Describes an EC2 instance.

                
                

                - **InstanceId** *(string) --* 

                  The ID of the instance.

                  
                

                - **AvailabilityZone** *(string) --* 

                  The Availability Zone in which the instance is running.

                  
                

                - **LifecycleState** *(string) --* 

                  A description of the current lifecycle state. Note that the ``Quarantined`` state is not used.

                  
                

                - **HealthStatus** *(string) --* 

                  The last reported health status of the instance. "Healthy" means that the instance is healthy and should remain in service. "Unhealthy" means that the instance is unhealthy and Auto Scaling should terminate and replace it.

                  
                

                - **LaunchConfigurationName** *(string) --* 

                  The launch configuration associated with the instance.

                  
                

                - **LaunchTemplate** *(dict) --* 

                  The launch template for the instance.

                  
                  

                  - **LaunchTemplateId** *(string) --* 

                    The ID of the launch template. You must specify either a template ID or a template name.

                    
                  

                  - **LaunchTemplateName** *(string) --* 

                    The name of the launch template. You must specify either a template name or a template ID.

                    
                  

                  - **Version** *(string) --* 

                    The version number. By default, the default version of the launch template is used.

                    
              
                

                - **ProtectedFromScaleIn** *(boolean) --* 

                  Indicates whether the instance is protected from termination by Auto Scaling when scaling in.

                  
            
          
            

            - **CreatedTime** *(datetime) --* 

              The date and time the group was created.

              
            

            - **SuspendedProcesses** *(list) --* 

              The suspended processes associated with the group.

              
              

              - *(dict) --* 

                Describes an Auto Scaling process that has been suspended. For more information, see  ProcessType .

                
                

                - **ProcessName** *(string) --* 

                  The name of the suspended process.

                  
                

                - **SuspensionReason** *(string) --* 

                  The reason that the process was suspended.

                  
            
          
            

            - **PlacementGroup** *(string) --* 

              The name of the placement group into which you'll launch your instances, if any. For more information, see `Placement Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

              
            

            - **VPCZoneIdentifier** *(string) --* 

              One or more subnet IDs, if applicable, separated by commas.

               

              If you specify ``VPCZoneIdentifier`` and ``AvailabilityZones`` , ensure that the Availability Zones of the subnets match the values for ``AvailabilityZones`` .

              
            

            - **EnabledMetrics** *(list) --* 

              The metrics enabled for the group.

              
              

              - *(dict) --* 

                Describes an enabled metric.

                
                

                - **Metric** *(string) --* 

                  One of the following metrics:

                   

                   
                  * ``GroupMinSize``   
                   
                  * ``GroupMaxSize``   
                   
                  * ``GroupDesiredCapacity``   
                   
                  * ``GroupInServiceInstances``   
                   
                  * ``GroupPendingInstances``   
                   
                  * ``GroupStandbyInstances``   
                   
                  * ``GroupTerminatingInstances``   
                   
                  * ``GroupTotalInstances``   
                   

                  
                

                - **Granularity** *(string) --* 

                  The granularity of the metric. The only valid value is ``1Minute`` .

                  
            
          
            

            - **Status** *(string) --* 

              The current state of the group when  DeleteAutoScalingGroup is in progress.

              
            

            - **Tags** *(list) --* 

              The tags for the group.

              
              

              - *(dict) --* 

                Describes a tag for an Auto Scaling group.

                
                

                - **ResourceId** *(string) --* 

                  The name of the group.

                  
                

                - **ResourceType** *(string) --* 

                  The type of resource. The only supported value is ``auto-scaling-group`` .

                  
                

                - **Key** *(string) --* 

                  The tag key.

                  
                

                - **Value** *(string) --* 

                  The tag value.

                  
                

                - **PropagateAtLaunch** *(boolean) --* 

                  Determines whether the tag is added to new instances as they are launched in the group.

                  
            
          
            

            - **TerminationPolicies** *(list) --* 

              The termination policies for the group.

              
              

              - *(string) --* 
          
            

            - **NewInstancesProtectedFromScaleIn** *(boolean) --* 

              Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.

              
        
      
    

.. py:class:: AutoScaling.Paginator.DescribeAutoScalingInstances

  ::

    
    paginator = client.get_paginator('describe_auto_scaling_instances')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_auto_scaling_instances`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingInstances>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          InstanceIds=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type InstanceIds: list
    :param InstanceIds: 

      The instances to describe; up to 50 instance IDs. If you omit this parameter, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.

      

    
      - *(string) --* 

      
  
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutoScalingInstances': [
                {
                    'InstanceId': 'string',
                    'AutoScalingGroupName': 'string',
                    'AvailabilityZone': 'string',
                    'LifecycleState': 'string',
                    'HealthStatus': 'string',
                    'LaunchConfigurationName': 'string',
                    'LaunchTemplate': {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'Version': 'string'
                    },
                    'ProtectedFromScaleIn': True|False
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AutoScalingInstances** *(list) --* 

          The instances.

          
          

          - *(dict) --* 

            Describes an EC2 instance associated with an Auto Scaling group.

            
            

            - **InstanceId** *(string) --* 

              The ID of the instance.

              
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group for the instance.

              
            

            - **AvailabilityZone** *(string) --* 

              The Availability Zone for the instance.

              
            

            - **LifecycleState** *(string) --* 

              The lifecycle state for the instance. For more information, see `Auto Scaling Lifecycle <http://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroupLifecycle.html>`__ in the *Auto Scaling User Guide* .

              
            

            - **HealthStatus** *(string) --* 

              The last reported health status of this instance. "Healthy" means that the instance is healthy and should remain in service. "Unhealthy" means that the instance is unhealthy and Auto Scaling should terminate and replace it.

              
            

            - **LaunchConfigurationName** *(string) --* 

              The launch configuration used to launch the instance. This value is not available if you attached the instance to the Auto Scaling group.

              
            

            - **LaunchTemplate** *(dict) --* 

              The launch template for the instance.

              
              

              - **LaunchTemplateId** *(string) --* 

                The ID of the launch template. You must specify either a template ID or a template name.

                
              

              - **LaunchTemplateName** *(string) --* 

                The name of the launch template. You must specify either a template name or a template ID.

                
              

              - **Version** *(string) --* 

                The version number. By default, the default version of the launch template is used.

                
          
            

            - **ProtectedFromScaleIn** *(boolean) --* 

              Indicates whether the instance is protected from termination by Auto Scaling when scaling in.

              
        
      
    

.. py:class:: AutoScaling.Paginator.DescribeLaunchConfigurations

  ::

    
    paginator = client.get_paginator('describe_launch_configurations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_launch_configurations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLaunchConfigurations>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          LaunchConfigurationNames=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type LaunchConfigurationNames: list
    :param LaunchConfigurationNames: 

      The launch configuration names. If you omit this parameter, all launch configurations are described.

      

    
      - *(string) --* 

      
  
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LaunchConfigurations': [
                {
                    'LaunchConfigurationName': 'string',
                    'LaunchConfigurationARN': 'string',
                    'ImageId': 'string',
                    'KeyName': 'string',
                    'SecurityGroups': [
                        'string',
                    ],
                    'ClassicLinkVPCId': 'string',
                    'ClassicLinkVPCSecurityGroups': [
                        'string',
                    ],
                    'UserData': 'string',
                    'InstanceType': 'string',
                    'KernelId': 'string',
                    'RamdiskId': 'string',
                    'BlockDeviceMappings': [
                        {
                            'VirtualName': 'string',
                            'DeviceName': 'string',
                            'Ebs': {
                                'SnapshotId': 'string',
                                'VolumeSize': 123,
                                'VolumeType': 'string',
                                'DeleteOnTermination': True|False,
                                'Iops': 123,
                                'Encrypted': True|False
                            },
                            'NoDevice': True|False
                        },
                    ],
                    'InstanceMonitoring': {
                        'Enabled': True|False
                    },
                    'SpotPrice': 'string',
                    'IamInstanceProfile': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'EbsOptimized': True|False,
                    'AssociatePublicIpAddress': True|False,
                    'PlacementTenancy': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LaunchConfigurations** *(list) --* 

          The launch configurations.

          
          

          - *(dict) --* 

            Describes a launch configuration.

            
            

            - **LaunchConfigurationName** *(string) --* 

              The name of the launch configuration.

              
            

            - **LaunchConfigurationARN** *(string) --* 

              The Amazon Resource Name (ARN) of the launch configuration.

              
            

            - **ImageId** *(string) --* 

              The ID of the Amazon Machine Image (AMI).

              
            

            - **KeyName** *(string) --* 

              The name of the key pair.

              
            

            - **SecurityGroups** *(list) --* 

              The security groups to associate with the instances.

              
              

              - *(string) --* 
          
            

            - **ClassicLinkVPCId** *(string) --* 

              The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. This parameter can only be used if you are launching EC2-Classic instances. For more information, see `ClassicLink <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

              
            

            - **ClassicLinkVPCSecurityGroups** *(list) --* 

              The IDs of one or more security groups for the VPC specified in ``ClassicLinkVPCId`` . This parameter is required if you specify a ClassicLink-enabled VPC, and cannot be used otherwise. For more information, see `ClassicLink <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

              
              

              - *(string) --* 
          
            

            - **UserData** *(string) --* 

              The user data available to the instances.

              
            

            - **InstanceType** *(string) --* 

              The instance type for the instances.

              
            

            - **KernelId** *(string) --* 

              The ID of the kernel associated with the AMI.

              
            

            - **RamdiskId** *(string) --* 

              The ID of the RAM disk associated with the AMI.

              
            

            - **BlockDeviceMappings** *(list) --* 

              A block device mapping, which specifies the block devices for the instance.

              
              

              - *(dict) --* 

                Describes a block device mapping.

                
                

                - **VirtualName** *(string) --* 

                  The name of the virtual device (for example, ``ephemeral0`` ).

                  
                

                - **DeviceName** *(string) --* 

                  The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).

                  
                

                - **Ebs** *(dict) --* 

                  The information about the Amazon EBS volume.

                  
                  

                  - **SnapshotId** *(string) --* 

                    The ID of the snapshot.

                    
                  

                  - **VolumeSize** *(integer) --* 

                    The volume size, in GiB. For ``standard`` volumes, specify a value from 1 to 1,024. For ``io1`` volumes, specify a value from 4 to 16,384. For ``gp2`` volumes, specify a value from 1 to 16,384. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.

                     

                    Default: If you create a volume from a snapshot and you don't specify a volume size, the default is the snapshot size.

                    
                  

                  - **VolumeType** *(string) --* 

                    The volume type. For more information, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

                     

                    Valid values: ``standard`` | ``io1`` | ``gp2``  

                     

                    Default: ``standard``  

                    
                  

                  - **DeleteOnTermination** *(boolean) --* 

                    Indicates whether the volume is deleted on instance termination.

                     

                    Default: ``true``  

                    
                  

                  - **Iops** *(integer) --* 

                    The number of I/O operations per second (IOPS) to provision for the volume.

                     

                    Constraint: Required when the volume type is ``io1`` .

                    
                  

                  - **Encrypted** *(boolean) --* 

                    Indicates whether the volume should be encrypted. Encrypted EBS volumes must be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or an unencrypted volume from an encrypted snapshot. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .

                    
              
                

                - **NoDevice** *(boolean) --* 

                  Suppresses a device mapping.

                   

                  If this parameter is true for the root device, the instance might fail the EC2 health check. Auto Scaling launches a replacement instance if the instance fails the health check.

                  
            
          
            

            - **InstanceMonitoring** *(dict) --* 

              Controls whether instances in this group are launched with detailed (``true`` ) or basic (``false`` ) monitoring.

              
              

              - **Enabled** *(boolean) --* 

                If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

                
          
            

            - **SpotPrice** *(string) --* 

              The price to bid when launching Spot Instances.

              
            

            - **IamInstanceProfile** *(string) --* 

              The name or Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.

              
            

            - **CreatedTime** *(datetime) --* 

              The creation date and time for the launch configuration.

              
            

            - **EbsOptimized** *(boolean) --* 

              Controls whether the instance is optimized for EBS I/O (``true`` ) or not (``false`` ).

              
            

            - **AssociatePublicIpAddress** *(boolean) --* 

              [EC2-VPC] Indicates whether to assign a public IP address to each instance.

              
            

            - **PlacementTenancy** *(string) --* 

              The tenancy of the instance, either ``default`` or ``dedicated`` . An instance with ``dedicated`` tenancy runs in an isolated, single-tenant hardware and can only be launched into a VPC.

              
        
      
    

.. py:class:: AutoScaling.Paginator.DescribeNotificationConfigurations

  ::

    
    paginator = client.get_paginator('describe_notification_configurations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_notification_configurations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeNotificationConfigurations>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          AutoScalingGroupNames=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type AutoScalingGroupNames: list
    :param AutoScalingGroupNames: 

      The name of the Auto Scaling group.

      

    
      - *(string) --* 

      
  
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NotificationConfigurations': [
                {
                    'AutoScalingGroupName': 'string',
                    'TopicARN': 'string',
                    'NotificationType': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NotificationConfigurations** *(list) --* 

          The notification configurations.

          
          

          - *(dict) --* 

            Describes a notification.

            
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **TopicARN** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.

              
            

            - **NotificationType** *(string) --* 

              One of the following event notification types:

               

               
              * ``autoscaling:EC2_INSTANCE_LAUNCH``   
               
              * ``autoscaling:EC2_INSTANCE_LAUNCH_ERROR``   
               
              * ``autoscaling:EC2_INSTANCE_TERMINATE``   
               
              * ``autoscaling:EC2_INSTANCE_TERMINATE_ERROR``   
               
              * ``autoscaling:TEST_NOTIFICATION``   
               

              
        
      
    

.. py:class:: AutoScaling.Paginator.DescribePolicies

  ::

    
    paginator = client.get_paginator('describe_policies')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_policies`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribePolicies>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          AutoScalingGroupName='string',
          PolicyNames=[
              'string',
          ],
          PolicyTypes=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: 

      The name of the Auto Scaling group.

      

    
    :type PolicyNames: list
    :param PolicyNames: 

      The names of one or more policies. If you omit this parameter, all policies are described. If an group name is provided, the results are limited to that group. This list is limited to 50 items. If you specify an unknown policy name, it is ignored with no error.

      

    
      - *(string) --* 

      
  
    :type PolicyTypes: list
    :param PolicyTypes: 

      One or more policy types. Valid values are ``SimpleScaling`` and ``StepScaling`` .

      

    
      - *(string) --* 

      
  
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ScalingPolicies': [
                {
                    'AutoScalingGroupName': 'string',
                    'PolicyName': 'string',
                    'PolicyARN': 'string',
                    'PolicyType': 'string',
                    'AdjustmentType': 'string',
                    'MinAdjustmentStep': 123,
                    'MinAdjustmentMagnitude': 123,
                    'ScalingAdjustment': 123,
                    'Cooldown': 123,
                    'StepAdjustments': [
                        {
                            'MetricIntervalLowerBound': 123.0,
                            'MetricIntervalUpperBound': 123.0,
                            'ScalingAdjustment': 123
                        },
                    ],
                    'MetricAggregationType': 'string',
                    'EstimatedInstanceWarmup': 123,
                    'Alarms': [
                        {
                            'AlarmName': 'string',
                            'AlarmARN': 'string'
                        },
                    ],
                    'TargetTrackingConfiguration': {
                        'PredefinedMetricSpecification': {
                            'PredefinedMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'ALBRequestCountPerTarget',
                            'ResourceLabel': 'string'
                        },
                        'CustomizedMetricSpecification': {
                            'MetricName': 'string',
                            'Namespace': 'string',
                            'Dimensions': [
                                {
                                    'Name': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                            'Unit': 'string'
                        },
                        'TargetValue': 123.0,
                        'DisableScaleIn': True|False
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ScalingPolicies** *(list) --* 

          The scaling policies.

          
          

          - *(dict) --* 

            Describes a scaling policy.

            
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **PolicyName** *(string) --* 

              The name of the scaling policy.

              
            

            - **PolicyARN** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

              
            

            - **PolicyType** *(string) --* 

              The policy type. Valid values are ``SimpleScaling`` and ``StepScaling`` .

              
            

            - **AdjustmentType** *(string) --* 

              The adjustment type, which specifies how ``ScalingAdjustment`` is interpreted. Valid values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .

              
            

            - **MinAdjustmentStep** *(integer) --* 

              Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.

              
            

            - **MinAdjustmentMagnitude** *(integer) --* 

              The minimum number of instances to scale. If the value of ``AdjustmentType`` is ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the Auto Scaling group by at least this many instances. Otherwise, the error is ``ValidationError`` .

              
            

            - **ScalingAdjustment** *(integer) --* 

              The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.

              
            

            - **Cooldown** *(integer) --* 

              The amount of time, in seconds, after a scaling activity completes before any further dynamic scaling activities can start.

              
            

            - **StepAdjustments** *(list) --* 

              A set of adjustments that enable you to scale based on the size of the alarm breach.

              
              

              - *(dict) --* 

                Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you've defined for the alarm.

                 

                For the following examples, suppose that you have an alarm with a breach threshold of 50:

                 

                 
                * If you want the adjustment to be triggered when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10. 
                 
                * If you want the adjustment to be triggered when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0. 
                 

                 

                There are a few rules for the step adjustments for your step policy:

                 

                 
                * The ranges of your step adjustments can't overlap or have a gap. 
                 
                * At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound. 
                 
                * At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound. 
                 
                * The upper and lower bound can't be null in the same step adjustment. 
                 

                
                

                - **MetricIntervalLowerBound** *(float) --* 

                  The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.

                  
                

                - **MetricIntervalUpperBound** *(float) --* 

                  The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.

                   

                  The upper bound must be greater than the lower bound.

                  
                

                - **ScalingAdjustment** *(integer) --* 

                  The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.

                  
            
          
            

            - **MetricAggregationType** *(string) --* 

              The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` , ``Maximum`` , and ``Average`` .

              
            

            - **EstimatedInstanceWarmup** *(integer) --* 

              The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.

              
            

            - **Alarms** *(list) --* 

              The CloudWatch alarms related to the policy.

              
              

              - *(dict) --* 

                Describes an alarm.

                
                

                - **AlarmName** *(string) --* 

                  The name of the alarm.

                  
                

                - **AlarmARN** *(string) --* 

                  The Amazon Resource Name (ARN) of the alarm.

                  
            
          
            

            - **TargetTrackingConfiguration** *(dict) --* 

              A target tracking policy.

              
              

              - **PredefinedMetricSpecification** *(dict) --* 

                A predefined metric. You can specify either a predefined metric or a customized metric.

                
                

                - **PredefinedMetricType** *(string) --* 

                  The metric type.

                  
                

                - **ResourceLabel** *(string) --* 

                  Identifies the resource associated with the metric type. The following predefined metrics are available:

                   

                   
                  * ``ASGAverageCPUUtilization`` - average CPU utilization of the Auto Scaling group 
                   
                  * ``ASGAverageNetworkIn`` - average number of bytes received on all network interfaces by the Auto Scaling group 
                   
                  * ``ASGAverageNetworkOut`` - average number of bytes sent out on all network interfaces by the Auto Scaling group 
                   
                  * ``ALBRequestCountPerTarget`` - number of requests completed per target in an Application Load Balancer target group 
                   

                   

                  For predefined metric types ``ASGAverageCPUUtilization`` , ``ASGAverageNetworkIn`` , and ``ASGAverageNetworkOut`` , the parameter must not be specified as the resource associated with the metric type is the Auto Scaling group. For predefined metric type ``ALBRequestCountPerTarget`` , the parameter must be specified in the format: ``app/*load-balancer-name* /*load-balancer-id* /targetgroup/*target-group-name* /*target-group-id* `` , where ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load balancer ARN, and ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the target group ARN. The target group must be attached to the Auto Scaling group.

                  
            
              

              - **CustomizedMetricSpecification** *(dict) --* 

                A customized metric.

                
                

                - **MetricName** *(string) --* 

                  The name of the metric.

                  
                

                - **Namespace** *(string) --* 

                  The namespace of the metric.

                  
                

                - **Dimensions** *(list) --* 

                  The dimensions of the metric.

                  
                  

                  - *(dict) --* 

                    Describes the dimension of a metric.

                    
                    

                    - **Name** *(string) --* 

                      The name of the dimension.

                      
                    

                    - **Value** *(string) --* 

                      The value of the dimension.

                      
                
              
                

                - **Statistic** *(string) --* 

                  The statistic of the metric.

                  
                

                - **Unit** *(string) --* 

                  The unit of the metric.

                  
            
              

              - **TargetValue** *(float) --* 

                The target value for the metric.

                
              

              - **DisableScaleIn** *(boolean) --* 

                Indicates whether scale in by the target tracking policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking policy won't remove instances from the Auto Scaling group. Otherwise, scale in is enabled and the target tracking policy can remove instances from the Auto Scaling group. The default value is ``false`` .

                
          
        
      
    

.. py:class:: AutoScaling.Paginator.DescribeScalingActivities

  ::

    
    paginator = client.get_paginator('describe_scaling_activities')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_scaling_activities`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScalingActivities>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ActivityIds=[
              'string',
          ],
          AutoScalingGroupName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ActivityIds: list
    :param ActivityIds: 

      The activity IDs of the desired scaling activities. If you omit this parameter, all activities for the past six weeks are described. If you specify an Auto Scaling group, the results are limited to that group. The list of requested activities cannot contain more than 50 items. If unknown activities are requested, they are ignored with no error.

      

    
      - *(string) --* 

      
  
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: 

      The name of the Auto Scaling group.

      

    
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Activities': [
                {
                    'ActivityId': 'string',
                    'AutoScalingGroupName': 'string',
                    'Description': 'string',
                    'Cause': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                    'StatusMessage': 'string',
                    'Progress': 123,
                    'Details': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Activities** *(list) --* 

          The scaling activities. Activities are sorted by start time. Activities still in progress are described first.

          
          

          - *(dict) --* 

            Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

            
            

            - **ActivityId** *(string) --* 

              The ID of the activity.

              
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **Description** *(string) --* 

              A friendly, more verbose description of the activity.

              
            

            - **Cause** *(string) --* 

              The reason the activity began.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the activity.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the activity.

              
            

            - **StatusCode** *(string) --* 

              The current status of the activity.

              
            

            - **StatusMessage** *(string) --* 

              A friendly, more verbose description of the activity status.

              
            

            - **Progress** *(integer) --* 

              A value between 0 and 100 that indicates the progress of the activity.

              
            

            - **Details** *(string) --* 

              The details about the activity.

              
        
      
    

.. py:class:: AutoScaling.Paginator.DescribeScheduledActions

  ::

    
    paginator = client.get_paginator('describe_scheduled_actions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_scheduled_actions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScheduledActions>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          AutoScalingGroupName='string',
          ScheduledActionNames=[
              'string',
          ],
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: 

      The name of the Auto Scaling group.

      

    
    :type ScheduledActionNames: list
    :param ScheduledActionNames: 

      Describes one or more scheduled actions. If you omit this parameter, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.

       

      You can describe up to a maximum of 50 instances with a single call. If there are more items to return, the call returns a token. To get the next set of items, repeat the call with the returned token.

      

    
      - *(string) --* 

      
  
    :type StartTime: datetime
    :param StartTime: 

      The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.

      

    
    :type EndTime: datetime
    :param EndTime: 

      The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.

      

    
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ScheduledUpdateGroupActions': [
                {
                    'AutoScalingGroupName': 'string',
                    'ScheduledActionName': 'string',
                    'ScheduledActionARN': 'string',
                    'Time': datetime(2015, 1, 1),
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'Recurrence': 'string',
                    'MinSize': 123,
                    'MaxSize': 123,
                    'DesiredCapacity': 123
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ScheduledUpdateGroupActions** *(list) --* 

          The scheduled actions.

          
          

          - *(dict) --* 

            Describes a scheduled update to an Auto Scaling group.

            
            

            - **AutoScalingGroupName** *(string) --* 

              The name of the Auto Scaling group.

              
            

            - **ScheduledActionName** *(string) --* 

              The name of the scheduled action.

              
            

            - **ScheduledActionARN** *(string) --* 

              The Amazon Resource Name (ARN) of the scheduled action.

              
            

            - **Time** *(datetime) --* 

              This parameter is deprecated.

              
            

            - **StartTime** *(datetime) --* 

              The date and time that the action is scheduled to begin. This date and time can be up to one month in the future.

               

              When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the boundaries of when the recurring action will start and stop.

              
            

            - **EndTime** *(datetime) --* 

              The date and time that the action is scheduled to end. This date and time can be up to one month in the future.

              
            

            - **Recurrence** *(string) --* 

              The recurring schedule for the action.

              
            

            - **MinSize** *(integer) --* 

              The minimum size of the group.

              
            

            - **MaxSize** *(integer) --* 

              The maximum size of the group.

              
            

            - **DesiredCapacity** *(integer) --* 

              The number of instances you prefer to maintain in the group.

              
        
      
    

.. py:class:: AutoScaling.Paginator.DescribeTags

  ::

    
    paginator = client.get_paginator('describe_tags')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_tags`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeTags>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Filters=[
              {
                  'Name': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type Filters: list
    :param Filters: 

      A filter used to scope the tags to return.

      

    
      - *(dict) --* 

        Describes a filter.

        

      
        - **Name** *(string) --* 

          The name of the filter. The valid values are: ``"auto-scaling-group"`` , ``"key"`` , ``"value"`` , and ``"propagate-at-launch"`` .

          

        
        - **Values** *(list) --* 

          The value of the filter.

          

        
          - *(string) --* 

          
      
      
  
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tags': [
                {
                    'ResourceId': 'string',
                    'ResourceType': 'string',
                    'Key': 'string',
                    'Value': 'string',
                    'PropagateAtLaunch': True|False
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Tags** *(list) --* 

          One or more tags.

          
          

          - *(dict) --* 

            Describes a tag for an Auto Scaling group.

            
            

            - **ResourceId** *(string) --* 

              The name of the group.

              
            

            - **ResourceType** *(string) --* 

              The type of resource. The only supported value is ``auto-scaling-group`` .

              
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The tag value.

              
            

            - **PropagateAtLaunch** *(boolean) --* 

              Determines whether the tag is added to new instances as they are launched in the group.

              
        
      
    