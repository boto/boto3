

.. _https://docs.docker.com/engine/reference/commandline/run/: https://docs.docker.com/engine/reference/commandline/run/


***
ECS
***

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ECS.Client

  A low-level client representing Amazon EC2 Container Service (ECS)::

    
    import boto3
    
    client = boto3.client('ecs')

  
  These are the available methods:
  
  *   :py:meth:`~ECS.Client.can_paginate`

  
  *   :py:meth:`~ECS.Client.create_cluster`

  
  *   :py:meth:`~ECS.Client.create_service`

  
  *   :py:meth:`~ECS.Client.delete_attributes`

  
  *   :py:meth:`~ECS.Client.delete_cluster`

  
  *   :py:meth:`~ECS.Client.delete_service`

  
  *   :py:meth:`~ECS.Client.deregister_container_instance`

  
  *   :py:meth:`~ECS.Client.deregister_task_definition`

  
  *   :py:meth:`~ECS.Client.describe_clusters`

  
  *   :py:meth:`~ECS.Client.describe_container_instances`

  
  *   :py:meth:`~ECS.Client.describe_services`

  
  *   :py:meth:`~ECS.Client.describe_task_definition`

  
  *   :py:meth:`~ECS.Client.describe_tasks`

  
  *   :py:meth:`~ECS.Client.discover_poll_endpoint`

  
  *   :py:meth:`~ECS.Client.generate_presigned_url`

  
  *   :py:meth:`~ECS.Client.get_paginator`

  
  *   :py:meth:`~ECS.Client.get_waiter`

  
  *   :py:meth:`~ECS.Client.list_attributes`

  
  *   :py:meth:`~ECS.Client.list_clusters`

  
  *   :py:meth:`~ECS.Client.list_container_instances`

  
  *   :py:meth:`~ECS.Client.list_services`

  
  *   :py:meth:`~ECS.Client.list_task_definition_families`

  
  *   :py:meth:`~ECS.Client.list_task_definitions`

  
  *   :py:meth:`~ECS.Client.list_tasks`

  
  *   :py:meth:`~ECS.Client.put_attributes`

  
  *   :py:meth:`~ECS.Client.register_container_instance`

  
  *   :py:meth:`~ECS.Client.register_task_definition`

  
  *   :py:meth:`~ECS.Client.run_task`

  
  *   :py:meth:`~ECS.Client.start_task`

  
  *   :py:meth:`~ECS.Client.stop_task`

  
  *   :py:meth:`~ECS.Client.submit_container_state_change`

  
  *   :py:meth:`~ECS.Client.submit_task_state_change`

  
  *   :py:meth:`~ECS.Client.update_container_agent`

  
  *   :py:meth:`~ECS.Client.update_container_instances_state`

  
  *   :py:meth:`~ECS.Client.update_service`

  

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


  .. py:method:: create_cluster(**kwargs)

    

    Creates a new Amazon ECS cluster. By default, your account receives a ``default`` cluster when you launch your first container instance. However, you can create your own cluster with a unique name with the ``CreateCluster`` action.

     

    .. note::

       

      When you call the  CreateCluster API operation, Amazon ECS attempts to create the service-linked role for your account so that required resources in other AWS services can be managed on your behalf. However, if the IAM user that makes the call does not have permissions to create the service-linked role, it is not created. For more information, see `Using Service-Linked Roles for Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/CreateCluster>`_    


    **Request Syntax** 
    ::

      response = client.create_cluster(
          clusterName='string'
      )
    :type clusterName: string
    :param clusterName: 

      The name of your cluster. If you do not specify a name for your cluster, you create a cluster named ``default`` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'cluster': {
                'clusterArn': 'string',
                'clusterName': 'string',
                'status': 'string',
                'registeredContainerInstancesCount': 123,
                'runningTasksCount': 123,
                'pendingTasksCount': 123,
                'activeServicesCount': 123,
                'statistics': [
                    {
                        'name': 'string',
                        'value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **cluster** *(dict) --* 

          The full description of your new cluster.

          
          

          - **clusterArn** *(string) --* 

            The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the cluster, the AWS account ID of the cluster owner, the ``cluster`` namespace, and then the cluster name. For example, ``arn:aws:ecs:*region* :*012345678910* :cluster/*test* `` ..

            
          

          - **clusterName** *(string) --* 

            A user-generated string that you use to identify your cluster.

            
          

          - **status** *(string) --* 

            The status of the cluster. The valid values are ``ACTIVE`` or ``INACTIVE`` . ``ACTIVE`` indicates that you can register container instances with the cluster and the associated instances can accept tasks.

            
          

          - **registeredContainerInstancesCount** *(integer) --* 

            The number of container instances registered into the cluster.

            
          

          - **runningTasksCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``RUNNING`` state.

            
          

          - **pendingTasksCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``PENDING`` state.

            
          

          - **activeServicesCount** *(integer) --* 

            The number of services that are running on the cluster in an ``ACTIVE`` state. You can view these services with  ListServices .

            
          

          - **statistics** *(list) --* 

            Additional information about your clusters that are separated by launch type, including:

             

             
            * runningEC2TasksCount 
             
            * RunningFargateTasksCount 
             
            * pendingEC2TasksCount 
             
            * pendingFargateTasksCount 
             
            * activeEC2ServiceCount 
             
            * activeFargateServiceCount 
             
            * drainingEC2ServiceCount 
             
            * drainingFargateServiceCount 
             

            
            

            - *(dict) --* 

              A key and value pair object.

              
              

              - **name** *(string) --* 

                The name of the key value pair. For environment variables, this is the name of the environment variable.

                
              

              - **value** *(string) --* 

                The value of the key value pair. For environment variables, this is the value of the environment variable.

                
          
        
      
    

    **Examples** 

    This example creates a cluster in your default region.
    ::

      response = client.create_cluster(
          clusterName='my_cluster',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'cluster': {
              'activeServicesCount': 0,
              'clusterArn': 'arn:aws:ecs:us-east-1:012345678910:cluster/my_cluster',
              'clusterName': 'my_cluster',
              'pendingTasksCount': 0,
              'registeredContainerInstancesCount': 0,
              'runningTasksCount': 0,
              'status': 'ACTIVE',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_service(**kwargs)

    

    Runs and maintains a desired number of tasks from a specified task definition. If the number of tasks running in a service drops below ``desiredCount`` , Amazon ECS spawns another copy of the task in the specified cluster. To update an existing service, see  UpdateService .

     

    In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind a load balancer. The load balancer distributes traffic across the tasks that are associated with the service. For more information, see `Service Load Balancing <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

     

    You can optionally specify a deployment configuration for your service. During a deployment, the service scheduler uses the ``minimumHealthyPercent`` and ``maximumPercent`` parameters to determine the deployment strategy. The deployment is triggered by changing the task definition or the desired count of a service with an  UpdateService operation.

     

    The ``minimumHealthyPercent`` represents a lower limit on the number of your service's tasks that must remain in the ``RUNNING`` state during a deployment, as a percentage of the ``desiredCount`` (rounded up to the nearest integer). This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a ``desiredCount`` of four tasks and a ``minimumHealthyPercent`` of 50%, the scheduler can stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that *do not* use a load balancer are considered healthy if they are in the ``RUNNING`` state. Tasks for services that *do* use a load balancer are considered healthy if they are in the ``RUNNING`` state and the container instance they are hosted on is reported as healthy by the load balancer. The default value for ``minimumHealthyPercent`` is 50% in the console and 100% for the AWS CLI, the AWS SDKs, and the APIs.

     

    The ``maximumPercent`` parameter represents an upper limit on the number of your service's tasks that are allowed in the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the ``desiredCount`` (rounded down to the nearest integer). This parameter enables you to define the deployment batch size. For example, if your service has a ``desiredCount`` of four tasks and a ``maximumPercent`` value of 200%, the scheduler can start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for ``maximumPercent`` is 200%.

     

    When the service scheduler launches new tasks, it determines task placement in your cluster using the following logic:

     

     
    * Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes). 
     
    * By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy) with the ``placementStrategy`` parameter): 

       
      * Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement. 
       
      * Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service. 
       

     
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/CreateService>`_    


    **Request Syntax** 
    ::

      response = client.create_service(
          cluster='string',
          serviceName='string',
          taskDefinition='string',
          loadBalancers=[
              {
                  'targetGroupArn': 'string',
                  'loadBalancerName': 'string',
                  'containerName': 'string',
                  'containerPort': 123
              },
          ],
          desiredCount=123,
          clientToken='string',
          launchType='EC2'|'FARGATE',
          platformVersion='string',
          role='string',
          deploymentConfiguration={
              'maximumPercent': 123,
              'minimumHealthyPercent': 123
          },
          placementConstraints=[
              {
                  'type': 'distinctInstance'|'memberOf',
                  'expression': 'string'
              },
          ],
          placementStrategy=[
              {
                  'type': 'random'|'spread'|'binpack',
                  'field': 'string'
              },
          ],
          networkConfiguration={
              'awsvpcConfiguration': {
                  'subnets': [
                      'string',
                  ],
                  'securityGroups': [
                      'string',
                  ],
                  'assignPublicIp': 'ENABLED'|'DISABLED'
              }
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster on which to run your service. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type serviceName: string
    :param serviceName: **[REQUIRED]** 

      The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a region or across multiple regions.

      

    
    :type taskDefinition: string
    :param taskDefinition: **[REQUIRED]** 

      The ``family`` and ``revision`` (``family:revision`` ) or full ARN of the task definition to run in your service. If a ``revision`` is not specified, the latest ``ACTIVE`` revision is used.

      

    
    :type loadBalancers: list
    :param loadBalancers: 

      A load balancer object representing the load balancer to use with your service. Currently, you are limited to one load balancer or target group per service. After you create a service, the load balancer name or target group ARN, container name, and container port specified in the service definition are immutable.

       

      For Classic Load Balancers, this object must contain the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer. When a task from this service is placed on a container instance, the container instance is registered with the load balancer specified here.

       

      For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name (as it appears in a container definition), and the container port to access from the load balancer. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group specified here.

      

    
      - *(dict) --* 

        Details on a load balancer that is used with a service.

        

      
        - **targetGroupArn** *(string) --* 

          The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group associated with a service.

          

        
        - **loadBalancerName** *(string) --* 

          The name of a load balancer.

          

        
        - **containerName** *(string) --* 

          The name of the container (as it appears in a container definition) to associate with the load balancer.

          

        
        - **containerPort** *(integer) --* 

          The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.

          

        
      
  
    :type desiredCount: integer
    :param desiredCount: **[REQUIRED]** 

      The number of instantiations of the specified task definition to place and keep running on your cluster.

      

    
    :type clientToken: string
    :param clientToken: 

      Unique, case-sensitive identifier you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.

      

    
    :type launchType: string
    :param launchType: 

      The launch type on which to run your service.

      

    
    :type platformVersion: string
    :param platformVersion: 

      The platform version on which to run your service. If one is not specified, the latest version is used by default.

      

    
    :type role: string
    :param role: 

      The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition does not use the ``awsvpc`` network mode. If you specify the ``role`` parameter, you must also specify a load balancer object with the ``loadBalancers`` parameter.

       

      .. warning::

         

        If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here. The service-linked role is required if your task definition uses the ``awsvpc`` network mode, in which case you should not specify a role here. For more information, see `Using Service-Linked Roles for Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

         

       

      If your specified role has a path other than ``/`` , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` then you would specify ``/foo/bar`` as the role name. For more information, see `Friendly Names and Paths <http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`__ in the *IAM User Guide* .

      

    
    :type deploymentConfiguration: dict
    :param deploymentConfiguration: 

      Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.

      

    
      - **maximumPercent** *(integer) --* 

        The upper limit (as a percentage of the service's ``desiredCount`` ) of the number of tasks that are allowed in the ``RUNNING`` or ``PENDING`` state in a service during a deployment. The maximum number of tasks during a deployment is the ``desiredCount`` multiplied by ``maximumPercent`` /100, rounded down to the nearest integer value.

        

      
      - **minimumHealthyPercent** *(integer) --* 

        The lower limit (as a percentage of the service's ``desiredCount`` ) of the number of running tasks that must remain in the ``RUNNING`` state in a service during a deployment. The minimum number of healthy tasks during a deployment is the ``desiredCount`` multiplied by ``minimumHealthyPercent`` /100, rounded up to the nearest integer value.

        

      
    
    :type placementConstraints: list
    :param placementConstraints: 

      An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints per task (this limit includes constraints in the task definition and those specified at run time). 

      

    
      - *(dict) --* 

        An object representing a constraint on task placement. For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

        

      
        - **type** *(string) --* 

          The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.

          

        
        - **expression** *(string) --* 

          A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

          

        
      
  
    :type placementStrategy: list
    :param placementStrategy: 

      The placement strategy objects to use for tasks in your service. You can specify a maximum of five strategy rules per service.

      

    
      - *(dict) --* 

        The task placement strategy for a task or service. For more information, see `Task Placement Strategies <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

        

      
        - **type** *(string) --* 

          The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

          

        
        - **field** *(string) --* 

          The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.

          

        
      
  
    :type networkConfiguration: dict
    :param networkConfiguration: 

      The network configuration for the service. This parameter is required for task definitions that use the ``awsvpc`` network mode to receive their own Elastic Network Interface, and it is not supported for other network modes. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

      

    
      - **awsvpcConfiguration** *(dict) --* 

        The VPC subnets and security groups associated with a task.

        

      
        - **subnets** *(list) --* **[REQUIRED]** 

          The subnets associated with the task or service.

          

        
          - *(string) --* 

          
      
        - **securityGroups** *(list) --* 

          The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

          

        
          - *(string) --* 

          
      
        - **assignPublicIp** *(string) --* 

          Specifies whether or not the task's elastic network interface receives a public IP address.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'service': {
                'serviceArn': 'string',
                'serviceName': 'string',
                'clusterArn': 'string',
                'loadBalancers': [
                    {
                        'targetGroupArn': 'string',
                        'loadBalancerName': 'string',
                        'containerName': 'string',
                        'containerPort': 123
                    },
                ],
                'status': 'string',
                'desiredCount': 123,
                'runningCount': 123,
                'pendingCount': 123,
                'launchType': 'EC2'|'FARGATE',
                'platformVersion': 'string',
                'taskDefinition': 'string',
                'deploymentConfiguration': {
                    'maximumPercent': 123,
                    'minimumHealthyPercent': 123
                },
                'deployments': [
                    {
                        'id': 'string',
                        'status': 'string',
                        'taskDefinition': 'string',
                        'desiredCount': 123,
                        'pendingCount': 123,
                        'runningCount': 123,
                        'createdAt': datetime(2015, 1, 1),
                        'updatedAt': datetime(2015, 1, 1),
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'networkConfiguration': {
                            'awsvpcConfiguration': {
                                'subnets': [
                                    'string',
                                ],
                                'securityGroups': [
                                    'string',
                                ],
                                'assignPublicIp': 'ENABLED'|'DISABLED'
                            }
                        }
                    },
                ],
                'roleArn': 'string',
                'events': [
                    {
                        'id': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'message': 'string'
                    },
                ],
                'createdAt': datetime(2015, 1, 1),
                'placementConstraints': [
                    {
                        'type': 'distinctInstance'|'memberOf',
                        'expression': 'string'
                    },
                ],
                'placementStrategy': [
                    {
                        'type': 'random'|'spread'|'binpack',
                        'field': 'string'
                    },
                ],
                'networkConfiguration': {
                    'awsvpcConfiguration': {
                        'subnets': [
                            'string',
                        ],
                        'securityGroups': [
                            'string',
                        ],
                        'assignPublicIp': 'ENABLED'|'DISABLED'
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **service** *(dict) --* 

          The full description of your service following the create call.

          
          

          - **serviceArn** *(string) --* 

            The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the service, the AWS account ID of the service owner, the ``service`` namespace, and then the service name. For example, ``arn:aws:ecs:*region* :*012345678910* :service/*my-service* `` .

            
          

          - **serviceName** *(string) --* 

            The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a region or across multiple regions.

            
          

          - **clusterArn** *(string) --* 

            The Amazon Resource Name (ARN) of the cluster that hosts the service.

            
          

          - **loadBalancers** *(list) --* 

            A list of Elastic Load Balancing load balancer objects, containing the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer.

            
            

            - *(dict) --* 

              Details on a load balancer that is used with a service.

              
              

              - **targetGroupArn** *(string) --* 

                The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group associated with a service.

                
              

              - **loadBalancerName** *(string) --* 

                The name of a load balancer.

                
              

              - **containerName** *(string) --* 

                The name of the container (as it appears in a container definition) to associate with the load balancer.

                
              

              - **containerPort** *(integer) --* 

                The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.

                
          
        
          

          - **status** *(string) --* 

            The status of the service. The valid values are ``ACTIVE`` , ``DRAINING`` , or ``INACTIVE`` .

            
          

          - **desiredCount** *(integer) --* 

            The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .

            
          

          - **runningCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``RUNNING`` state.

            
          

          - **pendingCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``PENDING`` state.

            
          

          - **launchType** *(string) --* 

            The launch type on which your service is running.

            
          

          - **platformVersion** *(string) --* 

            The platform version on which your task is running. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **taskDefinition** *(string) --* 

            The task definition to use for tasks in the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .

            
          

          - **deploymentConfiguration** *(dict) --* 

            Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.

            
            

            - **maximumPercent** *(integer) --* 

              The upper limit (as a percentage of the service's ``desiredCount`` ) of the number of tasks that are allowed in the ``RUNNING`` or ``PENDING`` state in a service during a deployment. The maximum number of tasks during a deployment is the ``desiredCount`` multiplied by ``maximumPercent`` /100, rounded down to the nearest integer value.

              
            

            - **minimumHealthyPercent** *(integer) --* 

              The lower limit (as a percentage of the service's ``desiredCount`` ) of the number of running tasks that must remain in the ``RUNNING`` state in a service during a deployment. The minimum number of healthy tasks during a deployment is the ``desiredCount`` multiplied by ``minimumHealthyPercent`` /100, rounded up to the nearest integer value.

              
        
          

          - **deployments** *(list) --* 

            The current state of deployments for the service.

            
            

            - *(dict) --* 

              The details of an Amazon ECS service deployment.

              
              

              - **id** *(string) --* 

                The ID of the deployment.

                
              

              - **status** *(string) --* 

                The status of the deployment. Valid values are ``PRIMARY`` (for the most recent deployment), ``ACTIVE`` (for previous deployments that still have tasks running, but are being replaced with the ``PRIMARY`` deployment), and ``INACTIVE`` (for deployments that have been completely replaced).

                
              

              - **taskDefinition** *(string) --* 

                The most recent task definition that was specified for the service to use.

                
              

              - **desiredCount** *(integer) --* 

                The most recent desired count of tasks that was specified for the service to deploy or maintain.

                
              

              - **pendingCount** *(integer) --* 

                The number of tasks in the deployment that are in the ``PENDING`` status.

                
              

              - **runningCount** *(integer) --* 

                The number of tasks in the deployment that are in the ``RUNNING`` status.

                
              

              - **createdAt** *(datetime) --* 

                The Unix time stamp for when the service was created.

                
              

              - **updatedAt** *(datetime) --* 

                The Unix time stamp for when the service was last updated.

                
              

              - **launchType** *(string) --* 

                The launch type on which your service is running.

                
              

              - **platformVersion** *(string) --* 

                The platform version on which your service is running.

                
              

              - **networkConfiguration** *(dict) --* 

                The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

                
                

                - **awsvpcConfiguration** *(dict) --* 

                  The VPC subnets and security groups associated with a task.

                  
                  

                  - **subnets** *(list) --* 

                    The subnets associated with the task or service.

                    
                    

                    - *(string) --* 
                
                  

                  - **securityGroups** *(list) --* 

                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

                    
                    

                    - *(string) --* 
                
                  

                  - **assignPublicIp** *(string) --* 

                    Specifies whether or not the task's elastic network interface receives a public IP address.

                    
              
            
          
        
          

          - **roleArn** *(string) --* 

            The ARN of the IAM role associated with the service that allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.

            
          

          - **events** *(list) --* 

            The event stream for your service. A maximum of 100 of the latest events are displayed.

            
            

            - *(dict) --* 

              Details on an event associated with a service.

              
              

              - **id** *(string) --* 

                The ID string of the event.

                
              

              - **createdAt** *(datetime) --* 

                The Unix time stamp for when the event was triggered.

                
              

              - **message** *(string) --* 

                The event message.

                
          
        
          

          - **createdAt** *(datetime) --* 

            The Unix time stamp for when the service was created.

            
          

          - **placementConstraints** *(list) --* 

            The placement constraints for the tasks in the service.

            
            

            - *(dict) --* 

              An object representing a constraint on task placement. For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.

                
              

              - **expression** *(string) --* 

                A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
          
        
          

          - **placementStrategy** *(list) --* 

            The placement strategy that determines how tasks for the service are placed.

            
            

            - *(dict) --* 

              The task placement strategy for a task or service. For more information, see `Task Placement Strategies <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

                
              

              - **field** *(string) --* 

                The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.

                
          
        
          

          - **networkConfiguration** *(dict) --* 

            The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

            
            

            - **awsvpcConfiguration** *(dict) --* 

              The VPC subnets and security groups associated with a task.

              
              

              - **subnets** *(list) --* 

                The subnets associated with the task or service.

                
                

                - *(string) --* 
            
              

              - **securityGroups** *(list) --* 

                The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

                
                

                - *(string) --* 
            
              

              - **assignPublicIp** *(string) --* 

                Specifies whether or not the task's elastic network interface receives a public IP address.

                
          
        
      
    

    **Examples** 

    This example creates a service in your default region called ``ecs-simple-service``. The service uses the ``hello_world`` task definition and it maintains 10 copies of that task.
    ::

      response = client.create_service(
          desiredCount=10,
          serviceName='ecs-simple-service',
          taskDefinition='hello_world',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'service': {
              'clusterArn': 'arn:aws:ecs:us-east-1:012345678910:cluster/default',
              'createdAt': datetime(2016, 8, 29, 16, 13, 47, 0, 242, 0),
              'deploymentConfiguration': {
                  'maximumPercent': 200,
                  'minimumHealthyPercent': 100,
              },
              'deployments': [
                  {
                      'createdAt': datetime(2016, 8, 29, 16, 13, 47, 0, 242, 0),
                      'desiredCount': 10,
                      'id': 'ecs-svc/9223370564342348388',
                      'pendingCount': 0,
                      'runningCount': 0,
                      'status': 'PRIMARY',
                      'taskDefinition': 'arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:6',
                      'updatedAt': datetime(2016, 8, 29, 16, 13, 47, 0, 242, 0),
                  },
                  {
                      'createdAt': datetime(2016, 8, 29, 15, 52, 44, 0, 242, 0),
                      'desiredCount': 0,
                      'id': 'ecs-svc/9223370564343611322',
                      'pendingCount': 0,
                      'runningCount': 0,
                      'status': 'ACTIVE',
                      'taskDefinition': 'arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:6',
                      'updatedAt': datetime(2016, 8, 29, 16, 11, 38, 0, 242, 0),
                  },
              ],
              'desiredCount': 10,
              'events': [
              ],
              'loadBalancers': [
              ],
              'pendingCount': 0,
              'runningCount': 0,
              'serviceArn': 'arn:aws:ecs:us-east-1:012345678910:service/ecs-simple-service',
              'serviceName': 'ecs-simple-service',
              'status': 'ACTIVE',
              'taskDefinition': 'arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:6',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example creates a service in your default region called ``ecs-simple-service-elb``. The service uses the ``ecs-demo`` task definition and it maintains 10 copies of that task. You must reference an existing load balancer in the same region by its name.
    ::

      response = client.create_service(
          desiredCount=10,
          loadBalancers=[
              {
                  'containerName': 'simple-app',
                  'containerPort': 80,
                  'loadBalancerName': 'EC2Contai-EcsElast-15DCDAURT3ZO2',
              },
          ],
          role='ecsServiceRole',
          serviceName='ecs-simple-service-elb',
          taskDefinition='console-sample-app-static',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'service': {
              'clusterArn': 'arn:aws:ecs:us-east-1:012345678910:cluster/default',
              'createdAt': datetime(2016, 8, 29, 16, 2, 54, 0, 242, 0),
              'deploymentConfiguration': {
                  'maximumPercent': 200,
                  'minimumHealthyPercent': 100,
              },
              'deployments': [
                  {
                      'createdAt': datetime(2016, 8, 29, 16, 2, 54, 0, 242, 0),
                      'desiredCount': 10,
                      'id': 'ecs-svc/9223370564343000923',
                      'pendingCount': 0,
                      'runningCount': 0,
                      'status': 'PRIMARY',
                      'taskDefinition': 'arn:aws:ecs:us-east-1:012345678910:task-definition/console-sample-app-static:6',
                      'updatedAt': datetime(2016, 8, 29, 16, 2, 54, 0, 242, 0),
                  },
              ],
              'desiredCount': 10,
              'events': [
              ],
              'loadBalancers': [
                  {
                      'containerName': 'simple-app',
                      'containerPort': 80,
                      'loadBalancerName': 'EC2Contai-EcsElast-15DCDAURT3ZO2',
                  },
              ],
              'pendingCount': 0,
              'roleArn': 'arn:aws:iam::012345678910:role/ecsServiceRole',
              'runningCount': 0,
              'serviceArn': 'arn:aws:ecs:us-east-1:012345678910:service/ecs-simple-service-elb',
              'serviceName': 'ecs-simple-service-elb',
              'status': 'ACTIVE',
              'taskDefinition': 'arn:aws:ecs:us-east-1:012345678910:task-definition/console-sample-app-static:6',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_attributes(**kwargs)

    

    Deletes one or more custom attributes from an Amazon ECS resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeleteAttributes>`_    


    **Request Syntax** 
    ::

      response = client.delete_attributes(
          cluster='string',
          attributes=[
              {
                  'name': 'string',
                  'value': 'string',
                  'targetType': 'container-instance',
                  'targetId': 'string'
              },
          ]
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to delete attributes. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type attributes: list
    :param attributes: **[REQUIRED]** 

      The attributes to delete from your resource. You can specify up to 10 attributes per request. For custom attributes, specify the attribute name and target ID, but do not specify the value. If you specify the target ID using the short form, you must also specify the target type.

      

    
      - *(dict) --* 

        An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

        

      
        - **name** *(string) --* **[REQUIRED]** 

          The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

          

        
        - **value** *(string) --* 

          The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

          

        
        - **targetType** *(string) --* 

          The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

          

        
        - **targetId** *(string) --* 

          The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'attributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **attributes** *(list) --* 

          A list of attribute objects that were successfully deleted from your resource.

          
          

          - *(dict) --* 

            An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - **name** *(string) --* 

              The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

              
            

            - **value** *(string) --* 

              The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

              
            

            - **targetType** *(string) --* 

              The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

              
            

            - **targetId** *(string) --* 

              The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

              
        
      
    

  .. py:method:: delete_cluster(**kwargs)

    

    Deletes the specified cluster. You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with  ListContainerInstances and deregister them with  DeregisterContainerInstance .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeleteCluster>`_    


    **Request Syntax** 
    ::

      response = client.delete_cluster(
          cluster='string'
      )
    :type cluster: string
    :param cluster: **[REQUIRED]** 

      The short name or full Amazon Resource Name (ARN) of the cluster to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'cluster': {
                'clusterArn': 'string',
                'clusterName': 'string',
                'status': 'string',
                'registeredContainerInstancesCount': 123,
                'runningTasksCount': 123,
                'pendingTasksCount': 123,
                'activeServicesCount': 123,
                'statistics': [
                    {
                        'name': 'string',
                        'value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **cluster** *(dict) --* 

          The full description of the deleted cluster.

          
          

          - **clusterArn** *(string) --* 

            The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the cluster, the AWS account ID of the cluster owner, the ``cluster`` namespace, and then the cluster name. For example, ``arn:aws:ecs:*region* :*012345678910* :cluster/*test* `` ..

            
          

          - **clusterName** *(string) --* 

            A user-generated string that you use to identify your cluster.

            
          

          - **status** *(string) --* 

            The status of the cluster. The valid values are ``ACTIVE`` or ``INACTIVE`` . ``ACTIVE`` indicates that you can register container instances with the cluster and the associated instances can accept tasks.

            
          

          - **registeredContainerInstancesCount** *(integer) --* 

            The number of container instances registered into the cluster.

            
          

          - **runningTasksCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``RUNNING`` state.

            
          

          - **pendingTasksCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``PENDING`` state.

            
          

          - **activeServicesCount** *(integer) --* 

            The number of services that are running on the cluster in an ``ACTIVE`` state. You can view these services with  ListServices .

            
          

          - **statistics** *(list) --* 

            Additional information about your clusters that are separated by launch type, including:

             

             
            * runningEC2TasksCount 
             
            * RunningFargateTasksCount 
             
            * pendingEC2TasksCount 
             
            * pendingFargateTasksCount 
             
            * activeEC2ServiceCount 
             
            * activeFargateServiceCount 
             
            * drainingEC2ServiceCount 
             
            * drainingFargateServiceCount 
             

            
            

            - *(dict) --* 

              A key and value pair object.

              
              

              - **name** *(string) --* 

                The name of the key value pair. For environment variables, this is the name of the environment variable.

                
              

              - **value** *(string) --* 

                The value of the key value pair. For environment variables, this is the value of the environment variable.

                
          
        
      
    

    **Examples** 

    This example deletes an empty cluster in your default region.
    ::

      response = client.delete_cluster(
          cluster='my_cluster',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'cluster': {
              'activeServicesCount': 0,
              'clusterArn': 'arn:aws:ecs:us-east-1:012345678910:cluster/my_cluster',
              'clusterName': 'my_cluster',
              'pendingTasksCount': 0,
              'registeredContainerInstancesCount': 0,
              'runningTasksCount': 0,
              'status': 'INACTIVE',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_service(**kwargs)

    

    Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you cannot delete it, and you must update the service to a desired task count of zero. For more information, see  UpdateService .

     

    .. note::

       

      When you delete a service, if there are still running tasks that require cleanup, the service status moves from ``ACTIVE`` to ``DRAINING`` , and the service is no longer visible in the console or in  ListServices API operations. After the tasks have stopped, then the service status moves from ``DRAINING`` to ``INACTIVE`` . Services in the ``DRAINING`` or ``INACTIVE`` status can still be viewed with  DescribeServices API operations. However, in the future, ``INACTIVE`` services may be cleaned up and purged from Amazon ECS record keeping, and  DescribeServices API operations on those services return a ``ServiceNotFoundException`` error.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeleteService>`_    


    **Request Syntax** 
    ::

      response = client.delete_service(
          cluster='string',
          service='string'
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type service: string
    :param service: **[REQUIRED]** 

      The name of the service to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'service': {
                'serviceArn': 'string',
                'serviceName': 'string',
                'clusterArn': 'string',
                'loadBalancers': [
                    {
                        'targetGroupArn': 'string',
                        'loadBalancerName': 'string',
                        'containerName': 'string',
                        'containerPort': 123
                    },
                ],
                'status': 'string',
                'desiredCount': 123,
                'runningCount': 123,
                'pendingCount': 123,
                'launchType': 'EC2'|'FARGATE',
                'platformVersion': 'string',
                'taskDefinition': 'string',
                'deploymentConfiguration': {
                    'maximumPercent': 123,
                    'minimumHealthyPercent': 123
                },
                'deployments': [
                    {
                        'id': 'string',
                        'status': 'string',
                        'taskDefinition': 'string',
                        'desiredCount': 123,
                        'pendingCount': 123,
                        'runningCount': 123,
                        'createdAt': datetime(2015, 1, 1),
                        'updatedAt': datetime(2015, 1, 1),
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'networkConfiguration': {
                            'awsvpcConfiguration': {
                                'subnets': [
                                    'string',
                                ],
                                'securityGroups': [
                                    'string',
                                ],
                                'assignPublicIp': 'ENABLED'|'DISABLED'
                            }
                        }
                    },
                ],
                'roleArn': 'string',
                'events': [
                    {
                        'id': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'message': 'string'
                    },
                ],
                'createdAt': datetime(2015, 1, 1),
                'placementConstraints': [
                    {
                        'type': 'distinctInstance'|'memberOf',
                        'expression': 'string'
                    },
                ],
                'placementStrategy': [
                    {
                        'type': 'random'|'spread'|'binpack',
                        'field': 'string'
                    },
                ],
                'networkConfiguration': {
                    'awsvpcConfiguration': {
                        'subnets': [
                            'string',
                        ],
                        'securityGroups': [
                            'string',
                        ],
                        'assignPublicIp': 'ENABLED'|'DISABLED'
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **service** *(dict) --* 

          The full description of the deleted service.

          
          

          - **serviceArn** *(string) --* 

            The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the service, the AWS account ID of the service owner, the ``service`` namespace, and then the service name. For example, ``arn:aws:ecs:*region* :*012345678910* :service/*my-service* `` .

            
          

          - **serviceName** *(string) --* 

            The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a region or across multiple regions.

            
          

          - **clusterArn** *(string) --* 

            The Amazon Resource Name (ARN) of the cluster that hosts the service.

            
          

          - **loadBalancers** *(list) --* 

            A list of Elastic Load Balancing load balancer objects, containing the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer.

            
            

            - *(dict) --* 

              Details on a load balancer that is used with a service.

              
              

              - **targetGroupArn** *(string) --* 

                The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group associated with a service.

                
              

              - **loadBalancerName** *(string) --* 

                The name of a load balancer.

                
              

              - **containerName** *(string) --* 

                The name of the container (as it appears in a container definition) to associate with the load balancer.

                
              

              - **containerPort** *(integer) --* 

                The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.

                
          
        
          

          - **status** *(string) --* 

            The status of the service. The valid values are ``ACTIVE`` , ``DRAINING`` , or ``INACTIVE`` .

            
          

          - **desiredCount** *(integer) --* 

            The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .

            
          

          - **runningCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``RUNNING`` state.

            
          

          - **pendingCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``PENDING`` state.

            
          

          - **launchType** *(string) --* 

            The launch type on which your service is running.

            
          

          - **platformVersion** *(string) --* 

            The platform version on which your task is running. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **taskDefinition** *(string) --* 

            The task definition to use for tasks in the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .

            
          

          - **deploymentConfiguration** *(dict) --* 

            Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.

            
            

            - **maximumPercent** *(integer) --* 

              The upper limit (as a percentage of the service's ``desiredCount`` ) of the number of tasks that are allowed in the ``RUNNING`` or ``PENDING`` state in a service during a deployment. The maximum number of tasks during a deployment is the ``desiredCount`` multiplied by ``maximumPercent`` /100, rounded down to the nearest integer value.

              
            

            - **minimumHealthyPercent** *(integer) --* 

              The lower limit (as a percentage of the service's ``desiredCount`` ) of the number of running tasks that must remain in the ``RUNNING`` state in a service during a deployment. The minimum number of healthy tasks during a deployment is the ``desiredCount`` multiplied by ``minimumHealthyPercent`` /100, rounded up to the nearest integer value.

              
        
          

          - **deployments** *(list) --* 

            The current state of deployments for the service.

            
            

            - *(dict) --* 

              The details of an Amazon ECS service deployment.

              
              

              - **id** *(string) --* 

                The ID of the deployment.

                
              

              - **status** *(string) --* 

                The status of the deployment. Valid values are ``PRIMARY`` (for the most recent deployment), ``ACTIVE`` (for previous deployments that still have tasks running, but are being replaced with the ``PRIMARY`` deployment), and ``INACTIVE`` (for deployments that have been completely replaced).

                
              

              - **taskDefinition** *(string) --* 

                The most recent task definition that was specified for the service to use.

                
              

              - **desiredCount** *(integer) --* 

                The most recent desired count of tasks that was specified for the service to deploy or maintain.

                
              

              - **pendingCount** *(integer) --* 

                The number of tasks in the deployment that are in the ``PENDING`` status.

                
              

              - **runningCount** *(integer) --* 

                The number of tasks in the deployment that are in the ``RUNNING`` status.

                
              

              - **createdAt** *(datetime) --* 

                The Unix time stamp for when the service was created.

                
              

              - **updatedAt** *(datetime) --* 

                The Unix time stamp for when the service was last updated.

                
              

              - **launchType** *(string) --* 

                The launch type on which your service is running.

                
              

              - **platformVersion** *(string) --* 

                The platform version on which your service is running.

                
              

              - **networkConfiguration** *(dict) --* 

                The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

                
                

                - **awsvpcConfiguration** *(dict) --* 

                  The VPC subnets and security groups associated with a task.

                  
                  

                  - **subnets** *(list) --* 

                    The subnets associated with the task or service.

                    
                    

                    - *(string) --* 
                
                  

                  - **securityGroups** *(list) --* 

                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

                    
                    

                    - *(string) --* 
                
                  

                  - **assignPublicIp** *(string) --* 

                    Specifies whether or not the task's elastic network interface receives a public IP address.

                    
              
            
          
        
          

          - **roleArn** *(string) --* 

            The ARN of the IAM role associated with the service that allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.

            
          

          - **events** *(list) --* 

            The event stream for your service. A maximum of 100 of the latest events are displayed.

            
            

            - *(dict) --* 

              Details on an event associated with a service.

              
              

              - **id** *(string) --* 

                The ID string of the event.

                
              

              - **createdAt** *(datetime) --* 

                The Unix time stamp for when the event was triggered.

                
              

              - **message** *(string) --* 

                The event message.

                
          
        
          

          - **createdAt** *(datetime) --* 

            The Unix time stamp for when the service was created.

            
          

          - **placementConstraints** *(list) --* 

            The placement constraints for the tasks in the service.

            
            

            - *(dict) --* 

              An object representing a constraint on task placement. For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.

                
              

              - **expression** *(string) --* 

                A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
          
        
          

          - **placementStrategy** *(list) --* 

            The placement strategy that determines how tasks for the service are placed.

            
            

            - *(dict) --* 

              The task placement strategy for a task or service. For more information, see `Task Placement Strategies <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

                
              

              - **field** *(string) --* 

                The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.

                
          
        
          

          - **networkConfiguration** *(dict) --* 

            The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

            
            

            - **awsvpcConfiguration** *(dict) --* 

              The VPC subnets and security groups associated with a task.

              
              

              - **subnets** *(list) --* 

                The subnets associated with the task or service.

                
                

                - *(string) --* 
            
              

              - **securityGroups** *(list) --* 

                The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

                
                

                - *(string) --* 
            
              

              - **assignPublicIp** *(string) --* 

                Specifies whether or not the task's elastic network interface receives a public IP address.

                
          
        
      
    

    **Examples** 

    This example deletes the my-http-service service. The service must have a desired count and running count of 0 before you can delete it.
    ::

      response = client.delete_service(
          service='my-http-service',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: deregister_container_instance(**kwargs)

    

    Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks.

     

    If you intend to use the container instance for some other purpose after deregistration, you should stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources.

     

    Deregistering a container instance removes the instance from a cluster, but it does not terminate the EC2 instance; if you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.

     

    .. note::

       

      If you terminate a running container instance, Amazon ECS automatically deregisters the instance from your cluster (stopped container instances or instances with disconnected agents are not automatically deregistered when terminated).

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeregisterContainerInstance>`_    


    **Request Syntax** 
    ::

      response = client.deregister_container_instance(
          cluster='string',
          containerInstance='string',
          force=True|False
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to deregister. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type containerInstance: string
    :param containerInstance: **[REQUIRED]** 

      The container instance ID or full ARN of the container instance to deregister. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .

      

    
    :type force: boolean
    :param force: 

      Forces the deregistration of the container instance. If you have tasks running on the container instance when you deregister it with the ``force`` option, these tasks remain running until you terminate the instance or the tasks stop through some other means, but they are orphaned (no longer monitored or accounted for by Amazon ECS). If an orphaned task on your container instance is part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a different container instance if possible. 

       

      Any containers in orphaned service tasks that are registered with a Classic Load Balancer or an Application Load Balancer target group are deregistered. They begin connection draining according to the settings on the load balancer or target group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'containerInstance': {
                'containerInstanceArn': 'string',
                'ec2InstanceId': 'string',
                'version': 123,
                'versionInfo': {
                    'agentVersion': 'string',
                    'agentHash': 'string',
                    'dockerVersion': 'string'
                },
                'remainingResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'registeredResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'status': 'string',
                'agentConnected': True|False,
                'runningTasksCount': 123,
                'pendingTasksCount': 123,
                'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                'attributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'registeredAt': datetime(2015, 1, 1),
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **containerInstance** *(dict) --* 

          The container instance that was deregistered.

          
          

          - **containerInstanceArn** *(string) --* 

            The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .

            
          

          - **ec2InstanceId** *(string) --* 

            The EC2 instance ID of the container instance.

            
          

          - **version** *(integer) --* 

            The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.

            
          

          - **versionInfo** *(dict) --* 

            The version information for the Amazon ECS container agent and Docker daemon running on the container instance.

            
            

            - **agentVersion** *(string) --* 

              The version number of the Amazon ECS container agent.

              
            

            - **agentHash** *(string) --* 

              The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.

              
            

            - **dockerVersion** *(string) --* 

              The Docker version running on the container instance.

              
        
          

          - **remainingResources** *(list) --* 

            For most resource types, this parameter describes the remaining resources of the container instance that are available for new tasks. For port resource types, this parameter describes the ports that are reserved by the Amazon ECS container agent and any containers that have reserved port mappings; any port that is not specified here is available for new tasks.

            
            

            - *(dict) --* 

              Describes the resources available for a container instance.

              
              

              - **name** *(string) --* 

                The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                
              

              - **type** *(string) --* 

                The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                
              

              - **doubleValue** *(float) --* 

                When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                
              

              - **longValue** *(integer) --* 

                When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                
              

              - **integerValue** *(integer) --* 

                When the ``integerValue`` type is set, the value of the resource must be an integer.

                
              

              - **stringSetValue** *(list) --* 

                When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                
                

                - *(string) --* 
            
          
        
          

          - **registeredResources** *(list) --* 

            For most resource types, this parameter describes the registered resources on the container instance that are in use by current tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.

            
            

            - *(dict) --* 

              Describes the resources available for a container instance.

              
              

              - **name** *(string) --* 

                The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                
              

              - **type** *(string) --* 

                The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                
              

              - **doubleValue** *(float) --* 

                When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                
              

              - **longValue** *(integer) --* 

                When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                
              

              - **integerValue** *(integer) --* 

                When the ``integerValue`` type is set, the value of the resource must be an integer.

                
              

              - **stringSetValue** *(list) --* 

                When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                
                

                - *(string) --* 
            
          
        
          

          - **status** *(string) --* 

            The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **agentConnected** *(boolean) --* 

            This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Instances without a connected agent can't accept placement requests.

            
          

          - **runningTasksCount** *(integer) --* 

            The number of tasks on the container instance that are in the ``RUNNING`` status.

            
          

          - **pendingTasksCount** *(integer) --* 

            The number of tasks on the container instance that are in the ``PENDING`` status.

            
          

          - **agentUpdateStatus** *(string) --* 

            The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .

            
          

          - **attributes** *(list) --* 

            The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.

            
            

            - *(dict) --* 

              An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **name** *(string) --* 

                The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

                
              

              - **value** *(string) --* 

                The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

                
              

              - **targetType** *(string) --* 

                The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

                
              

              - **targetId** *(string) --* 

                The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

                
          
        
          

          - **registeredAt** *(datetime) --* 

            The Unix time stamp for when the container instance was registered.

            
          

          - **attachments** *(list) --* 

            The Elastic Network Interfaces associated with the container instance.

            
            

            - *(dict) --* 

              An object representing a container instance or task attachment.

              
              

              - **id** *(string) --* 

                The unique identifier for the attachment.

                
              

              - **type** *(string) --* 

                The type of the attachment, such as an ``ElasticNetworkInterface`` .

                
              

              - **status** *(string) --* 

                The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                
              

              - **details** *(list) --* 

                Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                
                

                - *(dict) --* 

                  A key and value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key value pair. For environment variables, this is the value of the environment variable.

                    
              
            
          
        
      
    

    **Examples** 

    This example deregisters a container instance from the specified cluster in your default region. If there are still tasks running on the container instance, you must either stop those tasks before deregistering, or use the force option.
    ::

      response = client.deregister_container_instance(
          cluster='default',
          containerInstance='container_instance_UUID',
          force=True,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: deregister_task_definition(**kwargs)

    

    Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as ``INACTIVE`` . Existing tasks and services that reference an ``INACTIVE`` task definition continue to run without disruption. Existing services that reference an ``INACTIVE`` task definition can still scale up or down by modifying the service's desired count.

     

    You cannot use an ``INACTIVE`` task definition to run new tasks or create new services, and you cannot update an existing service to reference an ``INACTIVE`` task definition (although there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect).

     

    .. note::

       

      At this time, ``INACTIVE`` task definitions remain discoverable in your account indefinitely; however, this behavior is subject to change in the future, so you should not rely on ``INACTIVE`` task definitions persisting beyond the lifecycle of any associated tasks and services.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeregisterTaskDefinition>`_    


    **Request Syntax** 
    ::

      response = client.deregister_task_definition(
          taskDefinition='string'
      )
    :type taskDefinition: string
    :param taskDefinition: **[REQUIRED]** 

      The ``family`` and ``revision`` (``family:revision`` ) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a ``revision`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskDefinition': {
                'taskDefinitionArn': 'string',
                'containerDefinitions': [
                    {
                        'name': 'string',
                        'image': 'string',
                        'cpu': 123,
                        'memory': 123,
                        'memoryReservation': 123,
                        'links': [
                            'string',
                        ],
                        'portMappings': [
                            {
                                'containerPort': 123,
                                'hostPort': 123,
                                'protocol': 'tcp'|'udp'
                            },
                        ],
                        'essential': True|False,
                        'entryPoint': [
                            'string',
                        ],
                        'command': [
                            'string',
                        ],
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'mountPoints': [
                            {
                                'sourceVolume': 'string',
                                'containerPath': 'string',
                                'readOnly': True|False
                            },
                        ],
                        'volumesFrom': [
                            {
                                'sourceContainer': 'string',
                                'readOnly': True|False
                            },
                        ],
                        'linuxParameters': {
                            'capabilities': {
                                'add': [
                                    'string',
                                ],
                                'drop': [
                                    'string',
                                ]
                            },
                            'devices': [
                                {
                                    'hostPath': 'string',
                                    'containerPath': 'string',
                                    'permissions': [
                                        'read'|'write'|'mknod',
                                    ]
                                },
                            ],
                            'initProcessEnabled': True|False
                        },
                        'hostname': 'string',
                        'user': 'string',
                        'workingDirectory': 'string',
                        'disableNetworking': True|False,
                        'privileged': True|False,
                        'readonlyRootFilesystem': True|False,
                        'dnsServers': [
                            'string',
                        ],
                        'dnsSearchDomains': [
                            'string',
                        ],
                        'extraHosts': [
                            {
                                'hostname': 'string',
                                'ipAddress': 'string'
                            },
                        ],
                        'dockerSecurityOptions': [
                            'string',
                        ],
                        'dockerLabels': {
                            'string': 'string'
                        },
                        'ulimits': [
                            {
                                'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                                'softLimit': 123,
                                'hardLimit': 123
                            },
                        ],
                        'logConfiguration': {
                            'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                            'options': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'family': 'string',
                'taskRoleArn': 'string',
                'executionRoleArn': 'string',
                'networkMode': 'bridge'|'host'|'awsvpc'|'none',
                'revision': 123,
                'volumes': [
                    {
                        'name': 'string',
                        'host': {
                            'sourcePath': 'string'
                        }
                    },
                ],
                'status': 'ACTIVE'|'INACTIVE',
                'requiresAttributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'placementConstraints': [
                    {
                        'type': 'memberOf',
                        'expression': 'string'
                    },
                ],
                'compatibilities': [
                    'EC2'|'FARGATE',
                ],
                'requiresCompatibilities': [
                    'EC2'|'FARGATE',
                ],
                'cpu': 'string',
                'memory': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskDefinition** *(dict) --* 

          The full description of the deregistered task.

          
          

          - **taskDefinitionArn** *(string) --* 

            The full Amazon Resource Name (ARN) of the task definition.

            
          

          - **containerDefinitions** *(list) --* 

            A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see `Amazon ECS Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(dict) --* 

              Container definitions are used in task definitions to describe the different containers that are launched as part of a task.

              
              

              - **name** *(string) --* 

                The name of a container. If you are linking multiple containers together in a task definition, the ``name`` of one container can be entered in the ``links`` of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to ``name`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--name`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . 

                
              

              - **image** *(string) --* 

                The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` *repository-url* /*image* :*tag* `` or `` *repository-url* /*image* @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                 
                * Images in Amazon ECR repositories can be specified by either using the full ``registry/repository:tag`` or ``registry/repository@digest`` . For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`` .  
                 
                * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                 
                * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                 
                * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                 

                
              

              - **cpu** *(integer) --* 

                The number of ``cpu`` units reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level ``cpu`` value.

                 

                .. note::

                   

                  You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the `Amazon EC2 Instances <http://aws.amazon.com/ec2/instance-types/>`__ detail page by 1,024.

                   

                 

                For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.

                 

                Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.

                 

                On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see `CPU share constraint <https://docs.docker.com/engine/reference/run/#cpu-share-constraint>`__ in the Docker documentation. The minimum valid CPU share value that the Linux kernel will allow is 2; however, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:

                 

                 
                * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to 2 CPU shares. 
                 
                * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2. 
                 

                 

                On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.

                
              

              - **memory** *(integer) --* 

                The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                If your containers will be part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task ``memory`` value.

                 

                For containers that will be part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of ``memory`` is used.

                 

                The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 

                
              

              - **memoryReservation** *(integer) --* 

                The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit; however, your container can consume more memory when it needs to, up to either the hard limit specified with the ``memory`` parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to ``MemoryReservation`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--memory-reservation`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                You must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of ``memory`` is used.

                 

                For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a ``memoryReservation`` of 128 MiB, and a ``memory`` hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.

                
              

              - **links** *(list) --* 

                The ``link`` parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to ``bridge`` . The ``name:internalName`` construct is analogous to ``name:alias`` in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to `https\://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>`__ . This parameter maps to ``Links`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--link`` option to ` ``docker run`` https://docs.docker.com/engine/reference/commandline/run/`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                 

                .. warning::

                   

                  Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.

                   

                
                

                - *(string) --* 
            
              

              - **portMappings** *(list) --* 

                The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.

                 

                For task definitions that use the ``awsvpc`` network mode, you should only specify the ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .

                 

                Port mappings on Windows use the ``NetNAT`` gateway address rather than ``localhost`` . There is no loopback for port mappings on Windows, so you cannot access a container's mapped port from the host itself. 

                 

                This parameter maps to ``PortBindings`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--publish`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . If the network mode of a task definition is set to ``none`` , then you can't specify port mappings. If the network mode of a task definition is set to ``host`` , then host ports must either be undefined or they must match the container port in the port mapping.

                 

                .. note::

                   

                  After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the **Network Bindings** section of a container description for a selected task in the Amazon ECS console, or the ``networkBindings`` section  DescribeTasks responses.

                   

                
                

                - *(dict) --* 

                  Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.

                   

                  If using containers in a task with the Fargate launch type, exposed ports should be specified using ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .

                   

                  After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

                  
                  

                  - **containerPort** *(integer) --* 

                    The port number on the container that is bound to the user-specified or automatically assigned host port.

                     

                    If using containers in a task with the Fargate launch type, exposed ports should be specified using ``containerPort`` .

                     

                    If using containers in a task with the EC2 launch type and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range (for more information, see ``hostPort`` ). Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.

                    
                  

                  - **hostPort** *(integer) --* 

                    The port number on the container instance to reserve for your container.

                     

                    If using containers in a task with the Fargate launch type, the ``hostPort`` can either be left blank or needs to be the same value as the ``containerPort`` .

                     

                    If using containers in a task with the EC2 launch type, you can specify a non-reserved host port for your container port mapping, or you can omit the ``hostPort`` (or set it to ``0`` ) while specifying a ``containerPort`` and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.

                     

                    The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under ``/proc/sys/net/ipv4/ip_local_port_range`` ; if this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. You should not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.

                     

                    .. note::

                       

                      The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.

                       

                     

                    The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678 and 51679. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the ``remainingResources`` of  DescribeContainerInstances output, and a container instance may have up to 100 reserved ports at a time, including the default reserved ports (automatically assigned ports do not count toward the 100 reserved ports limit).

                    
                  

                  - **protocol** *(string) --* 

                    The protocol used for the port mapping. Valid values are ``tcp`` and ``udp`` . The default is ``tcp`` .

                    
              
            
              

              - **essential** *(boolean) --* 

                If the ``essential`` parameter of a container is marked as ``true`` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the ``essential`` parameter of a container is marked as ``false`` , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.

                 

                All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see `Application Architecture <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
              

              - **entryPoint** *(list) --* 

                .. warning::

                   

                  Early versions of the Amazon ECS container agent do not properly handle ``entryPoint`` parameters. If you have problems using ``entryPoint`` , update your container agent or enter your commands and arguments as ``command`` array items instead.

                   

                 

                The entry point that is passed to the container. This parameter maps to ``Entrypoint`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--entrypoint`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#entrypoint <https://docs.docker.com/engine/reference/builder/#entrypoint>`__ .

                
                

                - *(string) --* 
            
              

              - **command** *(list) --* 

                The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

                
                

                - *(string) --* 
            
              

              - **environment** *(list) --* 

                The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. warning::

                   

                  We do not recommend using plaintext environment variables for sensitive information, such as credential data.

                   

                
                

                - *(dict) --* 

                  A key and value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key value pair. For environment variables, this is the value of the environment variable.

                    
              
            
              

              - **mountPoints** *(list) --* 

                The mount points for data volumes in your container.

                 

                This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.

                
                

                - *(dict) --* 

                  Details on a volume mount point that is used in a container definition.

                  
                  

                  - **sourceVolume** *(string) --* 

                    The name of the volume to mount.

                    
                  

                  - **containerPath** *(string) --* 

                    The path on the container to mount the host volume at.

                    
                  

                  - **readOnly** *(boolean) --* 

                    If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .

                    
              
            
              

              - **volumesFrom** *(list) --* 

                Data volumes to mount from another container. This parameter maps to ``VolumesFrom`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--volumes-from`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
                

                - *(dict) --* 

                  Details on a data volume from another container in the same task definition.

                  
                  

                  - **sourceContainer** *(string) --* 

                    The name of another container within the same task definition to mount volumes from.

                    
                  

                  - **readOnly** *(boolean) --* 

                    If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .

                    
              
            
              

              - **linuxParameters** *(dict) --* 

                Linux-specific modifications that are applied to the container, such as Linux  KernelCapabilities .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.

                   

                
                

                - **capabilities** *(dict) --* 

                  The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.

                  
                  

                  - **add** *(list) --* 

                    The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to ``CapAdd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cap-add`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                     

                    Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  

                    
                    

                    - *(string) --* 
                
                  

                  - **drop** *(list) --* 

                    The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to ``CapDrop`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cap-drop`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                     

                    Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  

                    
                    

                    - *(string) --* 
                
              
                

                - **devices** *(list) --* 

                  Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                  
                  

                  - *(dict) --* 

                    An object representing a container instance host device.

                    
                    

                    - **hostPath** *(string) --* 

                      The path for the device on the host container instance.

                      
                    

                    - **containerPath** *(string) --* 

                      The path inside the container at which to expose the host device.

                      
                    

                    - **permissions** *(list) --* 

                      The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

                      
                      

                      - *(string) --* 
                  
                
              
                

                - **initProcessEnabled** *(boolean) --* 

                  Run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
            
              

              - **hostname** *(string) --* 

                The hostname to use for your container. This parameter maps to ``Hostname`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--hostname`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
              

              - **user** *(string) --* 

                The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **workingDirectory** *(string) --* 

                The working directory in which to run commands inside the container. This parameter maps to ``WorkingDir`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--workdir`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
              

              - **disableNetworking** *(boolean) --* 

                When this parameter is true, networking is disabled within the container. This parameter maps to ``NetworkDisabled`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **privileged** *(boolean) --* 

                When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.

                   

                
              

              - **readonlyRootFilesystem** *(boolean) --* 

                When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--read-only`` option to ``docker run`` .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **dnsServers** *(list) --* 

                A list of DNS servers that are presented to the container. This parameter maps to ``Dns`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--dns`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **dnsSearchDomains** *(list) --* 

                A list of DNS search domains that are presented to the container. This parameter maps to ``DnsSearch`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--dns-search`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **extraHosts** *(list) --* 

                A list of hostnames and IP address mappings to append to the ``/etc/hosts`` file on the container. If using the Fargate launch type, this may be used to list non-Fargate hosts you want the container to talk to. This parameter maps to ``ExtraHosts`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--add-host`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(dict) --* 

                  Hostnames and IP address entries that are added to the ``/etc/hosts`` file of a container via the ``extraHosts`` parameter of its  ContainerDefinition . 

                  
                  

                  - **hostname** *(string) --* 

                    The hostname to use in the ``/etc/hosts`` entry.

                    
                  

                  - **ipAddress** *(string) --* 

                    The IP address to use in the ``/etc/hosts`` entry.

                    
              
            
              

              - **dockerSecurityOptions** *(list) --* 

                A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.

                 

                This parameter maps to ``SecurityOpt`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--security-opt`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  The Amazon ECS container agent running on a container instance must register with the ``ECS_SELINUX_CAPABLE=true`` or ``ECS_APPARMOR_CAPABLE=true`` environment variables before containers placed on that instance can use these security options. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **dockerLabels** *(dict) --* 

                A key/value map of labels to add to the container. This parameter maps to ``Labels`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--label`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **ulimits** *(list) --* 

                A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(dict) --* 

                  The ``ulimit`` settings to pass to the container.

                  
                  

                  - **name** *(string) --* 

                    The ``type`` of the ``ulimit`` .

                    
                  

                  - **softLimit** *(integer) --* 

                    The soft limit for the ulimit type.

                    
                  

                  - **hardLimit** *(integer) --* 

                    The hard limit for the ulimit type.

                    
              
            
              

              - **logConfiguration** *(dict) --* 

                The log configuration specification for the container.

                 

                If using the Fargate launch type, the only supported value is ``awslogs`` .

                 

                This parameter maps to ``LogConfig`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--log-driver`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . By default, containers use the same logging driver that the Docker daemon uses; however the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.docker.com/engine/admin/logging/overview/>`__ in the Docker documentation.

                 

                .. note::

                   

                  Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.

                   

                 

                This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                 

                .. note::

                   

                  The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                
                

                - **logDriver** *(string) --* 

                  The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default. If using the Fargate launch type, the only supported value is ``awslogs`` . For more information about using the ``awslogs`` driver, see `Using the awslogs Log Driver <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                  .. note::

                     

                    If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is `available on GitHub <https://github.com/aws/amazon-ecs-agent>`__ and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.

                     

                   

                  This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
                

                - **options** *(dict) --* 

                  The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
          
        
          

          - **family** *(string) --* 

            The family of your task definition, used as the definition name.

            
          

          - **taskRoleArn** *(string) --* 

            The ARN of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

             

            IAM roles for tasks on Windows require that the ``-EnableTaskIAMRole`` option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code in order to take advantage of the feature. For more information, see `Windows IAM Roles for Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **executionRoleArn** *(string) --* 

            The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

            
          

          - **networkMode** *(string) --* 

            The Docker networking mode to use for the containers in the task. The valid values are ``none`` , ``bridge`` , ``awsvpc`` , and ``host`` . The default Docker network mode is ``bridge`` . If using the Fargate launch type, the ``awsvpc`` network mode is required. If using the EC2 launch type, any network mode can be used. If the network mode is set to ``none`` , you can't specify port mappings in your container definitions, and the task's containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.

             

            With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings. 

             

            If the network mode is ``awsvpc`` , the task is allocated an Elastic Network Interface, and you must specify a  NetworkConfiguration when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

             

            .. note::

               

              Currently, only the Amazon ECS-optimized AMI, other Amazon Linux variants with the ``ecs-init`` package, or AWS Fargate infrastructure support the ``awsvpc`` network mode. 

               

             

            If the network mode is ``host`` , you can't run multiple instantiations of the same task on a single container instance when port mappings are used.

             

            Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. If you use the console to register a task definition with Windows containers, you must choose the ``<default>`` network mode object. 

             

            For more information, see `Network settings <https://docs.docker.com/engine/reference/run/#network-settings>`__ in the *Docker run reference* .

            
          

          - **revision** *(integer) --* 

            The revision of the task in a particular family. The revision is a version number of a task definition in a family. When you register a task definition for the first time, the revision is ``1`` ; each time you register a new revision of a task definition in the same family, the revision value always increases by one (even if you have deregistered previous revisions in this family).

            
          

          - **volumes** *(list) --* 

            The list of volumes in a task.

             

            If you are using the Fargate launch type, the ``host`` and ``sourcePath`` parameters are not supported.

             

            For more information about volume definition parameters and defaults, see `Amazon ECS Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(dict) --* 

              A data volume used in a task definition.

              
              

              - **name** *(string) --* 

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

                
              

              - **host** *(dict) --* 

                The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume, but the data is not guaranteed to persist after the containers associated with it stop running.

                 

                Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount ``C:\my\path:C:\my\path`` and ``D:\:D:\`` , but not ``D:\my\path:C:\my\path`` or ``D:\:C:\my\path`` .

                
                

                - **sourcePath** *(string) --* 

                  The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

                   

                  If you are using the Fargate launch type, the ``sourcePath`` parameter is not supported.

                  
            
          
        
          

          - **status** *(string) --* 

            The status of the task definition.

            
          

          - **requiresAttributes** *(list) --* 

            The container instance attributes required by your task. This field is not valid if using the Fargate launch type for your task.

            
            

            - *(dict) --* 

              An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **name** *(string) --* 

                The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

                
              

              - **value** *(string) --* 

                The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

                
              

              - **targetType** *(string) --* 

                The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

                
              

              - **targetId** *(string) --* 

                The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

                
          
        
          

          - **placementConstraints** *(list) --* 

            An array of placement constraint objects to use for tasks. This field is not valid if using the Fargate launch type for your task.

            
            

            - *(dict) --* 

              An object representing a constraint on task placement in the task definition.

               

              If you are using the Fargate launch type, task placement contraints are not supported.

               

              For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of constraint. The ``DistinctInstance`` constraint ensures that each task in a particular group is running on a different container instance. The ``MemberOf`` constraint restricts selection to be from a group of valid candidates.

                
              

              - **expression** *(string) --* 

                A cluster query language expression to apply to the constraint. For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
          
        
          

          - **compatibilities** *(list) --* 

            The launch type to use with your task. For more information, see `Amazon ECS Launch Types <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(string) --* 
        
          

          - **requiresCompatibilities** *(list) --* 

            The launch type the task is using.

            
            

            - *(string) --* 
        
          

          - **cpu** *(string) --* 

            The number of ``cpu`` units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:

             

             
            * 256 (.25 vCPU) - Available ``memory`` values: 512MB, 1GB, 2GB 
             
            * 512 (.5 vCPU) - Available ``memory`` values: 1GB, 2GB, 3GB, 4GB 
             
            * 1024 (1 vCPU) - Available ``memory`` values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 
             
            * 2048 (2 vCPU) - Available ``memory`` values: Between 4GB and 16GB in 1GB increments 
             
            * 4096 (4 vCPU) - Available ``memory`` values: Between 8GB and 30GB in 1GB increments 
             

            
          

          - **memory** *(string) --* 

            The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:

             

             
            * 512MB, 1GB, 2GB - Available ``cpu`` values: 256 (.25 vCPU) 
             
            * 1GB, 2GB, 3GB, 4GB - Available ``cpu`` values: 512 (.5 vCPU) 
             
            * 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available ``cpu`` values: 1024 (1 vCPU) 
             
            * Between 4GB and 16GB in 1GB increments - Available ``cpu`` values: 2048 (2 vCPU) 
             
            * Between 8GB and 30GB in 1GB increments - Available ``cpu`` values: 4096 (4 vCPU) 
             

            
      
    

  .. py:method:: describe_clusters(**kwargs)

    

    Describes one or more of your clusters.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeClusters>`_    


    **Request Syntax** 
    ::

      response = client.describe_clusters(
          clusters=[
              'string',
          ],
          include=[
              'STATISTICS',
          ]
      )
    :type clusters: list
    :param clusters: 

      A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.

      

    
      - *(string) --* 

      
  
    :type include: list
    :param include: 

      Additional information about your clusters to be separated by launch type, including:

       

       
      * runningEC2TasksCount 
       
      * RunningFargateTasksCount 
       
      * pendingEC2TasksCount 
       
      * pendingFargateTasksCount 
       
      * activeEC2ServiceCount 
       
      * activeFargateServiceCount 
       
      * drainingEC2ServiceCount 
       
      * drainingFargateServiceCount 
       

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'clusters': [
                {
                    'clusterArn': 'string',
                    'clusterName': 'string',
                    'status': 'string',
                    'registeredContainerInstancesCount': 123,
                    'runningTasksCount': 123,
                    'pendingTasksCount': 123,
                    'activeServicesCount': 123,
                    'statistics': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'failures': [
                {
                    'arn': 'string',
                    'reason': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **clusters** *(list) --* 

          The list of clusters.

          
          

          - *(dict) --* 

            A regional grouping of one or more container instances on which you can run task requests. Each account receives a default cluster the first time you use the Amazon ECS service, but you may also create other clusters. Clusters may contain more than one instance type simultaneously.

            
            

            - **clusterArn** *(string) --* 

              The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the cluster, the AWS account ID of the cluster owner, the ``cluster`` namespace, and then the cluster name. For example, ``arn:aws:ecs:*region* :*012345678910* :cluster/*test* `` ..

              
            

            - **clusterName** *(string) --* 

              A user-generated string that you use to identify your cluster.

              
            

            - **status** *(string) --* 

              The status of the cluster. The valid values are ``ACTIVE`` or ``INACTIVE`` . ``ACTIVE`` indicates that you can register container instances with the cluster and the associated instances can accept tasks.

              
            

            - **registeredContainerInstancesCount** *(integer) --* 

              The number of container instances registered into the cluster.

              
            

            - **runningTasksCount** *(integer) --* 

              The number of tasks in the cluster that are in the ``RUNNING`` state.

              
            

            - **pendingTasksCount** *(integer) --* 

              The number of tasks in the cluster that are in the ``PENDING`` state.

              
            

            - **activeServicesCount** *(integer) --* 

              The number of services that are running on the cluster in an ``ACTIVE`` state. You can view these services with  ListServices .

              
            

            - **statistics** *(list) --* 

              Additional information about your clusters that are separated by launch type, including:

               

               
              * runningEC2TasksCount 
               
              * RunningFargateTasksCount 
               
              * pendingEC2TasksCount 
               
              * pendingFargateTasksCount 
               
              * activeEC2ServiceCount 
               
              * activeFargateServiceCount 
               
              * drainingEC2ServiceCount 
               
              * drainingFargateServiceCount 
               

              
              

              - *(dict) --* 

                A key and value pair object.

                
                

                - **name** *(string) --* 

                  The name of the key value pair. For environment variables, this is the name of the environment variable.

                  
                

                - **value** *(string) --* 

                  The value of the key value pair. For environment variables, this is the value of the environment variable.

                  
            
          
        
      
        

        - **failures** *(list) --* 

          Any failures associated with the call.

          
          

          - *(dict) --* 

            A failed resource.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the failed resource.

              
            

            - **reason** *(string) --* 

              The reason for the failure.

              
        
      
    

    **Examples** 

    This example provides a description of the specified cluster in your default region.
    ::

      response = client.describe_clusters(
          clusters=[
              'default',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'clusters': [
              {
                  'clusterArn': 'arn:aws:ecs:us-east-1:aws_account_id:cluster/default',
                  'clusterName': 'default',
                  'status': 'ACTIVE',
              },
          ],
          'failures': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_container_instances(**kwargs)

    

    Describes Amazon Elastic Container Service container instances. Returns metadata about registered and remaining resources on each container instance requested.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeContainerInstances>`_    


    **Request Syntax** 
    ::

      response = client.describe_container_instances(
          cluster='string',
          containerInstances=[
              'string',
          ]
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type containerInstances: list
    :param containerInstances: **[REQUIRED]** 

      A list of container instance IDs or full ARN entries.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'containerInstances': [
                {
                    'containerInstanceArn': 'string',
                    'ec2InstanceId': 'string',
                    'version': 123,
                    'versionInfo': {
                        'agentVersion': 'string',
                        'agentHash': 'string',
                        'dockerVersion': 'string'
                    },
                    'remainingResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'registeredResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'status': 'string',
                    'agentConnected': True|False,
                    'runningTasksCount': 123,
                    'pendingTasksCount': 123,
                    'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                    'attributes': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'targetType': 'container-instance',
                            'targetId': 'string'
                        },
                    ],
                    'registeredAt': datetime(2015, 1, 1),
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                },
            ],
            'failures': [
                {
                    'arn': 'string',
                    'reason': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **containerInstances** *(list) --* 

          The list of container instances.

          
          

          - *(dict) --* 

            An EC2 instance that is running the Amazon ECS agent and has been registered with a cluster.

            
            

            - **containerInstanceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .

              
            

            - **ec2InstanceId** *(string) --* 

              The EC2 instance ID of the container instance.

              
            

            - **version** *(integer) --* 

              The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.

              
            

            - **versionInfo** *(dict) --* 

              The version information for the Amazon ECS container agent and Docker daemon running on the container instance.

              
              

              - **agentVersion** *(string) --* 

                The version number of the Amazon ECS container agent.

                
              

              - **agentHash** *(string) --* 

                The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.

                
              

              - **dockerVersion** *(string) --* 

                The Docker version running on the container instance.

                
          
            

            - **remainingResources** *(list) --* 

              For most resource types, this parameter describes the remaining resources of the container instance that are available for new tasks. For port resource types, this parameter describes the ports that are reserved by the Amazon ECS container agent and any containers that have reserved port mappings; any port that is not specified here is available for new tasks.

              
              

              - *(dict) --* 

                Describes the resources available for a container instance.

                
                

                - **name** *(string) --* 

                  The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                  
                

                - **type** *(string) --* 

                  The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                  
                

                - **doubleValue** *(float) --* 

                  When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                  
                

                - **longValue** *(integer) --* 

                  When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                  
                

                - **integerValue** *(integer) --* 

                  When the ``integerValue`` type is set, the value of the resource must be an integer.

                  
                

                - **stringSetValue** *(list) --* 

                  When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                  
                  

                  - *(string) --* 
              
            
          
            

            - **registeredResources** *(list) --* 

              For most resource types, this parameter describes the registered resources on the container instance that are in use by current tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.

              
              

              - *(dict) --* 

                Describes the resources available for a container instance.

                
                

                - **name** *(string) --* 

                  The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                  
                

                - **type** *(string) --* 

                  The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                  
                

                - **doubleValue** *(float) --* 

                  When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                  
                

                - **longValue** *(integer) --* 

                  When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                  
                

                - **integerValue** *(integer) --* 

                  When the ``integerValue`` type is set, the value of the resource must be an integer.

                  
                

                - **stringSetValue** *(list) --* 

                  When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                  
                  

                  - *(string) --* 
              
            
          
            

            - **status** *(string) --* 

              The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
            

            - **agentConnected** *(boolean) --* 

              This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Instances without a connected agent can't accept placement requests.

              
            

            - **runningTasksCount** *(integer) --* 

              The number of tasks on the container instance that are in the ``RUNNING`` status.

              
            

            - **pendingTasksCount** *(integer) --* 

              The number of tasks on the container instance that are in the ``PENDING`` status.

              
            

            - **agentUpdateStatus** *(string) --* 

              The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .

              
            

            - **attributes** *(list) --* 

              The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.

              
              

              - *(dict) --* 

                An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
                

                - **name** *(string) --* 

                  The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

                  
                

                - **value** *(string) --* 

                  The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

                  
                

                - **targetType** *(string) --* 

                  The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

                  
                

                - **targetId** *(string) --* 

                  The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

                  
            
          
            

            - **registeredAt** *(datetime) --* 

              The Unix time stamp for when the container instance was registered.

              
            

            - **attachments** *(list) --* 

              The Elastic Network Interfaces associated with the container instance.

              
              

              - *(dict) --* 

                An object representing a container instance or task attachment.

                
                

                - **id** *(string) --* 

                  The unique identifier for the attachment.

                  
                

                - **type** *(string) --* 

                  The type of the attachment, such as an ``ElasticNetworkInterface`` .

                  
                

                - **status** *(string) --* 

                  The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                  
                

                - **details** *(list) --* 

                  Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                  
                  

                  - *(dict) --* 

                    A key and value pair object.

                    
                    

                    - **name** *(string) --* 

                      The name of the key value pair. For environment variables, this is the name of the environment variable.

                      
                    

                    - **value** *(string) --* 

                      The value of the key value pair. For environment variables, this is the value of the environment variable.

                      
                
              
            
          
        
      
        

        - **failures** *(list) --* 

          Any failures associated with the call.

          
          

          - *(dict) --* 

            A failed resource.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the failed resource.

              
            

            - **reason** *(string) --* 

              The reason for the failure.

              
        
      
    

    **Examples** 

    This example provides a description of the specified container instance in your default region, using the container instance UUID as an identifier.
    ::

      response = client.describe_container_instances(
          cluster='default',
          containerInstances=[
              'f2756532-8f13-4d53-87c9-aed50dc94cd7',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'containerInstances': [
              {
                  'agentConnected': True,
                  'containerInstanceArn': 'arn:aws:ecs:us-east-1:012345678910:container-instance/f2756532-8f13-4d53-87c9-aed50dc94cd7',
                  'ec2InstanceId': 'i-807f3249',
                  'pendingTasksCount': 0,
                  'registeredResources': [
                      {
                          'name': 'CPU',
                          'type': 'INTEGER',
                          'doubleValue': 0.0,
                          'integerValue': 2048,
                          'longValue': 0,
                      },
                      {
                          'name': 'MEMORY',
                          'type': 'INTEGER',
                          'doubleValue': 0.0,
                          'integerValue': 3768,
                          'longValue': 0,
                      },
                      {
                          'name': 'PORTS',
                          'type': 'STRINGSET',
                          'doubleValue': 0.0,
                          'integerValue': 0,
                          'longValue': 0,
                          'stringSetValue': [
                              '2376',
                              '22',
                              '51678',
                              '2375',
                          ],
                      },
                  ],
                  'remainingResources': [
                      {
                          'name': 'CPU',
                          'type': 'INTEGER',
                          'doubleValue': 0.0,
                          'integerValue': 1948,
                          'longValue': 0,
                      },
                      {
                          'name': 'MEMORY',
                          'type': 'INTEGER',
                          'doubleValue': 0.0,
                          'integerValue': 3668,
                          'longValue': 0,
                      },
                      {
                          'name': 'PORTS',
                          'type': 'STRINGSET',
                          'doubleValue': 0.0,
                          'integerValue': 0,
                          'longValue': 0,
                          'stringSetValue': [
                              '2376',
                              '22',
                              '80',
                              '51678',
                              '2375',
                          ],
                      },
                  ],
                  'runningTasksCount': 1,
                  'status': 'ACTIVE',
              },
          ],
          'failures': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_services(**kwargs)

    

    Describes the specified services running in your cluster.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeServices>`_    


    **Request Syntax** 
    ::

      response = client.describe_services(
          cluster='string',
          services=[
              'string',
          ]
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type services: list
    :param services: **[REQUIRED]** 

      A list of services to describe. You may specify up to 10 services to describe in a single operation.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'services': [
                {
                    'serviceArn': 'string',
                    'serviceName': 'string',
                    'clusterArn': 'string',
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'status': 'string',
                    'desiredCount': 123,
                    'runningCount': 123,
                    'pendingCount': 123,
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'taskDefinition': 'string',
                    'deploymentConfiguration': {
                        'maximumPercent': 123,
                        'minimumHealthyPercent': 123
                    },
                    'deployments': [
                        {
                            'id': 'string',
                            'status': 'string',
                            'taskDefinition': 'string',
                            'desiredCount': 123,
                            'pendingCount': 123,
                            'runningCount': 123,
                            'createdAt': datetime(2015, 1, 1),
                            'updatedAt': datetime(2015, 1, 1),
                            'launchType': 'EC2'|'FARGATE',
                            'platformVersion': 'string',
                            'networkConfiguration': {
                                'awsvpcConfiguration': {
                                    'subnets': [
                                        'string',
                                    ],
                                    'securityGroups': [
                                        'string',
                                    ],
                                    'assignPublicIp': 'ENABLED'|'DISABLED'
                                }
                            }
                        },
                    ],
                    'roleArn': 'string',
                    'events': [
                        {
                            'id': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'message': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'placementConstraints': [
                        {
                            'type': 'distinctInstance'|'memberOf',
                            'expression': 'string'
                        },
                    ],
                    'placementStrategy': [
                        {
                            'type': 'random'|'spread'|'binpack',
                            'field': 'string'
                        },
                    ],
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    }
                },
            ],
            'failures': [
                {
                    'arn': 'string',
                    'reason': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **services** *(list) --* 

          The list of services described.

          
          

          - *(dict) --* 

            Details on a service within a cluster

            
            

            - **serviceArn** *(string) --* 

              The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the service, the AWS account ID of the service owner, the ``service`` namespace, and then the service name. For example, ``arn:aws:ecs:*region* :*012345678910* :service/*my-service* `` .

              
            

            - **serviceName** *(string) --* 

              The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a region or across multiple regions.

              
            

            - **clusterArn** *(string) --* 

              The Amazon Resource Name (ARN) of the cluster that hosts the service.

              
            

            - **loadBalancers** *(list) --* 

              A list of Elastic Load Balancing load balancer objects, containing the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer.

              
              

              - *(dict) --* 

                Details on a load balancer that is used with a service.

                
                

                - **targetGroupArn** *(string) --* 

                  The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group associated with a service.

                  
                

                - **loadBalancerName** *(string) --* 

                  The name of a load balancer.

                  
                

                - **containerName** *(string) --* 

                  The name of the container (as it appears in a container definition) to associate with the load balancer.

                  
                

                - **containerPort** *(integer) --* 

                  The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.

                  
            
          
            

            - **status** *(string) --* 

              The status of the service. The valid values are ``ACTIVE`` , ``DRAINING`` , or ``INACTIVE`` .

              
            

            - **desiredCount** *(integer) --* 

              The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .

              
            

            - **runningCount** *(integer) --* 

              The number of tasks in the cluster that are in the ``RUNNING`` state.

              
            

            - **pendingCount** *(integer) --* 

              The number of tasks in the cluster that are in the ``PENDING`` state.

              
            

            - **launchType** *(string) --* 

              The launch type on which your service is running.

              
            

            - **platformVersion** *(string) --* 

              The platform version on which your task is running. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
            

            - **taskDefinition** *(string) --* 

              The task definition to use for tasks in the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .

              
            

            - **deploymentConfiguration** *(dict) --* 

              Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.

              
              

              - **maximumPercent** *(integer) --* 

                The upper limit (as a percentage of the service's ``desiredCount`` ) of the number of tasks that are allowed in the ``RUNNING`` or ``PENDING`` state in a service during a deployment. The maximum number of tasks during a deployment is the ``desiredCount`` multiplied by ``maximumPercent`` /100, rounded down to the nearest integer value.

                
              

              - **minimumHealthyPercent** *(integer) --* 

                The lower limit (as a percentage of the service's ``desiredCount`` ) of the number of running tasks that must remain in the ``RUNNING`` state in a service during a deployment. The minimum number of healthy tasks during a deployment is the ``desiredCount`` multiplied by ``minimumHealthyPercent`` /100, rounded up to the nearest integer value.

                
          
            

            - **deployments** *(list) --* 

              The current state of deployments for the service.

              
              

              - *(dict) --* 

                The details of an Amazon ECS service deployment.

                
                

                - **id** *(string) --* 

                  The ID of the deployment.

                  
                

                - **status** *(string) --* 

                  The status of the deployment. Valid values are ``PRIMARY`` (for the most recent deployment), ``ACTIVE`` (for previous deployments that still have tasks running, but are being replaced with the ``PRIMARY`` deployment), and ``INACTIVE`` (for deployments that have been completely replaced).

                  
                

                - **taskDefinition** *(string) --* 

                  The most recent task definition that was specified for the service to use.

                  
                

                - **desiredCount** *(integer) --* 

                  The most recent desired count of tasks that was specified for the service to deploy or maintain.

                  
                

                - **pendingCount** *(integer) --* 

                  The number of tasks in the deployment that are in the ``PENDING`` status.

                  
                

                - **runningCount** *(integer) --* 

                  The number of tasks in the deployment that are in the ``RUNNING`` status.

                  
                

                - **createdAt** *(datetime) --* 

                  The Unix time stamp for when the service was created.

                  
                

                - **updatedAt** *(datetime) --* 

                  The Unix time stamp for when the service was last updated.

                  
                

                - **launchType** *(string) --* 

                  The launch type on which your service is running.

                  
                

                - **platformVersion** *(string) --* 

                  The platform version on which your service is running.

                  
                

                - **networkConfiguration** *(dict) --* 

                  The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

                  
                  

                  - **awsvpcConfiguration** *(dict) --* 

                    The VPC subnets and security groups associated with a task.

                    
                    

                    - **subnets** *(list) --* 

                      The subnets associated with the task or service.

                      
                      

                      - *(string) --* 
                  
                    

                    - **securityGroups** *(list) --* 

                      The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

                      
                      

                      - *(string) --* 
                  
                    

                    - **assignPublicIp** *(string) --* 

                      Specifies whether or not the task's elastic network interface receives a public IP address.

                      
                
              
            
          
            

            - **roleArn** *(string) --* 

              The ARN of the IAM role associated with the service that allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.

              
            

            - **events** *(list) --* 

              The event stream for your service. A maximum of 100 of the latest events are displayed.

              
              

              - *(dict) --* 

                Details on an event associated with a service.

                
                

                - **id** *(string) --* 

                  The ID string of the event.

                  
                

                - **createdAt** *(datetime) --* 

                  The Unix time stamp for when the event was triggered.

                  
                

                - **message** *(string) --* 

                  The event message.

                  
            
          
            

            - **createdAt** *(datetime) --* 

              The Unix time stamp for when the service was created.

              
            

            - **placementConstraints** *(list) --* 

              The placement constraints for the tasks in the service.

              
              

              - *(dict) --* 

                An object representing a constraint on task placement. For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
                

                - **type** *(string) --* 

                  The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.

                  
                

                - **expression** *(string) --* 

                  A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                  
            
          
            

            - **placementStrategy** *(list) --* 

              The placement strategy that determines how tasks for the service are placed.

              
              

              - *(dict) --* 

                The task placement strategy for a task or service. For more information, see `Task Placement Strategies <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
                

                - **type** *(string) --* 

                  The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

                  
                

                - **field** *(string) --* 

                  The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.

                  
            
          
            

            - **networkConfiguration** *(dict) --* 

              The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

              
              

              - **awsvpcConfiguration** *(dict) --* 

                The VPC subnets and security groups associated with a task.

                
                

                - **subnets** *(list) --* 

                  The subnets associated with the task or service.

                  
                  

                  - *(string) --* 
              
                

                - **securityGroups** *(list) --* 

                  The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

                  
                  

                  - *(string) --* 
              
                

                - **assignPublicIp** *(string) --* 

                  Specifies whether or not the task's elastic network interface receives a public IP address.

                  
            
          
        
      
        

        - **failures** *(list) --* 

          Any failures associated with the call.

          
          

          - *(dict) --* 

            A failed resource.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the failed resource.

              
            

            - **reason** *(string) --* 

              The reason for the failure.

              
        
      
    

    **Examples** 

    This example provides descriptive information about the service named ``ecs-simple-service``.
    ::

      response = client.describe_services(
          services=[
              'ecs-simple-service',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'failures': [
          ],
          'services': [
              {
                  'clusterArn': 'arn:aws:ecs:us-east-1:012345678910:cluster/default',
                  'createdAt': datetime(2016, 8, 29, 16, 25, 52, 0, 242, 0),
                  'deploymentConfiguration': {
                      'maximumPercent': 200,
                      'minimumHealthyPercent': 100,
                  },
                  'deployments': [
                      {
                          'createdAt': datetime(2016, 8, 29, 16, 25, 52, 0, 242, 0),
                          'desiredCount': 1,
                          'id': 'ecs-svc/9223370564341623665',
                          'pendingCount': 0,
                          'runningCount': 0,
                          'status': 'PRIMARY',
                          'taskDefinition': 'arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:6',
                          'updatedAt': datetime(2016, 8, 29, 16, 25, 52, 0, 242, 0),
                      },
                  ],
                  'desiredCount': 1,
                  'events': [
                      {
                          'createdAt': datetime(2016, 8, 29, 16, 25, 58, 0, 242, 0),
                          'id': '38c285e5-d335-4b68-8b15-e46dedc8e88d',
                          # In this example, there is a service event that shows unavailable cluster resources.
                          'message': '(service ecs-simple-service) was unable to place a task because no container instance met all of its requirements. The closest matching (container-instance 3f4de1c5-ffdd-4954-af7e-75b4be0c8841) is already using a port required by your task. For more information, see the Troubleshooting section of the Amazon ECS Developer Guide.',
                      },
                  ],
                  'loadBalancers': [
                  ],
                  'pendingCount': 0,
                  'runningCount': 0,
                  'serviceArn': 'arn:aws:ecs:us-east-1:012345678910:service/ecs-simple-service',
                  'serviceName': 'ecs-simple-service',
                  'status': 'ACTIVE',
                  'taskDefinition': 'arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:6',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_task_definition(**kwargs)

    

    Describes a task definition. You can specify a ``family`` and ``revision`` to find information about a specific task definition, or you can simply specify the family to find the latest ``ACTIVE`` revision in that family.

     

    .. note::

       

      You can only describe ``INACTIVE`` task definitions while an active task or service references them.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTaskDefinition>`_    


    **Request Syntax** 
    ::

      response = client.describe_task_definition(
          taskDefinition='string'
      )
    :type taskDefinition: string
    :param taskDefinition: **[REQUIRED]** 

      The ``family`` for the latest ``ACTIVE`` revision, ``family`` and ``revision`` (``family:revision`` ) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskDefinition': {
                'taskDefinitionArn': 'string',
                'containerDefinitions': [
                    {
                        'name': 'string',
                        'image': 'string',
                        'cpu': 123,
                        'memory': 123,
                        'memoryReservation': 123,
                        'links': [
                            'string',
                        ],
                        'portMappings': [
                            {
                                'containerPort': 123,
                                'hostPort': 123,
                                'protocol': 'tcp'|'udp'
                            },
                        ],
                        'essential': True|False,
                        'entryPoint': [
                            'string',
                        ],
                        'command': [
                            'string',
                        ],
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'mountPoints': [
                            {
                                'sourceVolume': 'string',
                                'containerPath': 'string',
                                'readOnly': True|False
                            },
                        ],
                        'volumesFrom': [
                            {
                                'sourceContainer': 'string',
                                'readOnly': True|False
                            },
                        ],
                        'linuxParameters': {
                            'capabilities': {
                                'add': [
                                    'string',
                                ],
                                'drop': [
                                    'string',
                                ]
                            },
                            'devices': [
                                {
                                    'hostPath': 'string',
                                    'containerPath': 'string',
                                    'permissions': [
                                        'read'|'write'|'mknod',
                                    ]
                                },
                            ],
                            'initProcessEnabled': True|False
                        },
                        'hostname': 'string',
                        'user': 'string',
                        'workingDirectory': 'string',
                        'disableNetworking': True|False,
                        'privileged': True|False,
                        'readonlyRootFilesystem': True|False,
                        'dnsServers': [
                            'string',
                        ],
                        'dnsSearchDomains': [
                            'string',
                        ],
                        'extraHosts': [
                            {
                                'hostname': 'string',
                                'ipAddress': 'string'
                            },
                        ],
                        'dockerSecurityOptions': [
                            'string',
                        ],
                        'dockerLabels': {
                            'string': 'string'
                        },
                        'ulimits': [
                            {
                                'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                                'softLimit': 123,
                                'hardLimit': 123
                            },
                        ],
                        'logConfiguration': {
                            'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                            'options': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'family': 'string',
                'taskRoleArn': 'string',
                'executionRoleArn': 'string',
                'networkMode': 'bridge'|'host'|'awsvpc'|'none',
                'revision': 123,
                'volumes': [
                    {
                        'name': 'string',
                        'host': {
                            'sourcePath': 'string'
                        }
                    },
                ],
                'status': 'ACTIVE'|'INACTIVE',
                'requiresAttributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'placementConstraints': [
                    {
                        'type': 'memberOf',
                        'expression': 'string'
                    },
                ],
                'compatibilities': [
                    'EC2'|'FARGATE',
                ],
                'requiresCompatibilities': [
                    'EC2'|'FARGATE',
                ],
                'cpu': 'string',
                'memory': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskDefinition** *(dict) --* 

          The full task definition description.

          
          

          - **taskDefinitionArn** *(string) --* 

            The full Amazon Resource Name (ARN) of the task definition.

            
          

          - **containerDefinitions** *(list) --* 

            A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see `Amazon ECS Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(dict) --* 

              Container definitions are used in task definitions to describe the different containers that are launched as part of a task.

              
              

              - **name** *(string) --* 

                The name of a container. If you are linking multiple containers together in a task definition, the ``name`` of one container can be entered in the ``links`` of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to ``name`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--name`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . 

                
              

              - **image** *(string) --* 

                The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` *repository-url* /*image* :*tag* `` or `` *repository-url* /*image* @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                 
                * Images in Amazon ECR repositories can be specified by either using the full ``registry/repository:tag`` or ``registry/repository@digest`` . For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`` .  
                 
                * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                 
                * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                 
                * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                 

                
              

              - **cpu** *(integer) --* 

                The number of ``cpu`` units reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level ``cpu`` value.

                 

                .. note::

                   

                  You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the `Amazon EC2 Instances <http://aws.amazon.com/ec2/instance-types/>`__ detail page by 1,024.

                   

                 

                For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.

                 

                Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.

                 

                On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see `CPU share constraint <https://docs.docker.com/engine/reference/run/#cpu-share-constraint>`__ in the Docker documentation. The minimum valid CPU share value that the Linux kernel will allow is 2; however, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:

                 

                 
                * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to 2 CPU shares. 
                 
                * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2. 
                 

                 

                On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.

                
              

              - **memory** *(integer) --* 

                The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                If your containers will be part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task ``memory`` value.

                 

                For containers that will be part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of ``memory`` is used.

                 

                The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 

                
              

              - **memoryReservation** *(integer) --* 

                The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit; however, your container can consume more memory when it needs to, up to either the hard limit specified with the ``memory`` parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to ``MemoryReservation`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--memory-reservation`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                You must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of ``memory`` is used.

                 

                For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a ``memoryReservation`` of 128 MiB, and a ``memory`` hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.

                
              

              - **links** *(list) --* 

                The ``link`` parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to ``bridge`` . The ``name:internalName`` construct is analogous to ``name:alias`` in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to `https\://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>`__ . This parameter maps to ``Links`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--link`` option to ` ``docker run`` https://docs.docker.com/engine/reference/commandline/run/`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                 

                .. warning::

                   

                  Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.

                   

                
                

                - *(string) --* 
            
              

              - **portMappings** *(list) --* 

                The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.

                 

                For task definitions that use the ``awsvpc`` network mode, you should only specify the ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .

                 

                Port mappings on Windows use the ``NetNAT`` gateway address rather than ``localhost`` . There is no loopback for port mappings on Windows, so you cannot access a container's mapped port from the host itself. 

                 

                This parameter maps to ``PortBindings`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--publish`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . If the network mode of a task definition is set to ``none`` , then you can't specify port mappings. If the network mode of a task definition is set to ``host`` , then host ports must either be undefined or they must match the container port in the port mapping.

                 

                .. note::

                   

                  After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the **Network Bindings** section of a container description for a selected task in the Amazon ECS console, or the ``networkBindings`` section  DescribeTasks responses.

                   

                
                

                - *(dict) --* 

                  Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.

                   

                  If using containers in a task with the Fargate launch type, exposed ports should be specified using ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .

                   

                  After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

                  
                  

                  - **containerPort** *(integer) --* 

                    The port number on the container that is bound to the user-specified or automatically assigned host port.

                     

                    If using containers in a task with the Fargate launch type, exposed ports should be specified using ``containerPort`` .

                     

                    If using containers in a task with the EC2 launch type and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range (for more information, see ``hostPort`` ). Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.

                    
                  

                  - **hostPort** *(integer) --* 

                    The port number on the container instance to reserve for your container.

                     

                    If using containers in a task with the Fargate launch type, the ``hostPort`` can either be left blank or needs to be the same value as the ``containerPort`` .

                     

                    If using containers in a task with the EC2 launch type, you can specify a non-reserved host port for your container port mapping, or you can omit the ``hostPort`` (or set it to ``0`` ) while specifying a ``containerPort`` and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.

                     

                    The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under ``/proc/sys/net/ipv4/ip_local_port_range`` ; if this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. You should not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.

                     

                    .. note::

                       

                      The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.

                       

                     

                    The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678 and 51679. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the ``remainingResources`` of  DescribeContainerInstances output, and a container instance may have up to 100 reserved ports at a time, including the default reserved ports (automatically assigned ports do not count toward the 100 reserved ports limit).

                    
                  

                  - **protocol** *(string) --* 

                    The protocol used for the port mapping. Valid values are ``tcp`` and ``udp`` . The default is ``tcp`` .

                    
              
            
              

              - **essential** *(boolean) --* 

                If the ``essential`` parameter of a container is marked as ``true`` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the ``essential`` parameter of a container is marked as ``false`` , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.

                 

                All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see `Application Architecture <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
              

              - **entryPoint** *(list) --* 

                .. warning::

                   

                  Early versions of the Amazon ECS container agent do not properly handle ``entryPoint`` parameters. If you have problems using ``entryPoint`` , update your container agent or enter your commands and arguments as ``command`` array items instead.

                   

                 

                The entry point that is passed to the container. This parameter maps to ``Entrypoint`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--entrypoint`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#entrypoint <https://docs.docker.com/engine/reference/builder/#entrypoint>`__ .

                
                

                - *(string) --* 
            
              

              - **command** *(list) --* 

                The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

                
                

                - *(string) --* 
            
              

              - **environment** *(list) --* 

                The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. warning::

                   

                  We do not recommend using plaintext environment variables for sensitive information, such as credential data.

                   

                
                

                - *(dict) --* 

                  A key and value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key value pair. For environment variables, this is the value of the environment variable.

                    
              
            
              

              - **mountPoints** *(list) --* 

                The mount points for data volumes in your container.

                 

                This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.

                
                

                - *(dict) --* 

                  Details on a volume mount point that is used in a container definition.

                  
                  

                  - **sourceVolume** *(string) --* 

                    The name of the volume to mount.

                    
                  

                  - **containerPath** *(string) --* 

                    The path on the container to mount the host volume at.

                    
                  

                  - **readOnly** *(boolean) --* 

                    If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .

                    
              
            
              

              - **volumesFrom** *(list) --* 

                Data volumes to mount from another container. This parameter maps to ``VolumesFrom`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--volumes-from`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
                

                - *(dict) --* 

                  Details on a data volume from another container in the same task definition.

                  
                  

                  - **sourceContainer** *(string) --* 

                    The name of another container within the same task definition to mount volumes from.

                    
                  

                  - **readOnly** *(boolean) --* 

                    If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .

                    
              
            
              

              - **linuxParameters** *(dict) --* 

                Linux-specific modifications that are applied to the container, such as Linux  KernelCapabilities .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.

                   

                
                

                - **capabilities** *(dict) --* 

                  The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.

                  
                  

                  - **add** *(list) --* 

                    The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to ``CapAdd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cap-add`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                     

                    Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  

                    
                    

                    - *(string) --* 
                
                  

                  - **drop** *(list) --* 

                    The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to ``CapDrop`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cap-drop`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                     

                    Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  

                    
                    

                    - *(string) --* 
                
              
                

                - **devices** *(list) --* 

                  Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                  
                  

                  - *(dict) --* 

                    An object representing a container instance host device.

                    
                    

                    - **hostPath** *(string) --* 

                      The path for the device on the host container instance.

                      
                    

                    - **containerPath** *(string) --* 

                      The path inside the container at which to expose the host device.

                      
                    

                    - **permissions** *(list) --* 

                      The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

                      
                      

                      - *(string) --* 
                  
                
              
                

                - **initProcessEnabled** *(boolean) --* 

                  Run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
            
              

              - **hostname** *(string) --* 

                The hostname to use for your container. This parameter maps to ``Hostname`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--hostname`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
              

              - **user** *(string) --* 

                The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **workingDirectory** *(string) --* 

                The working directory in which to run commands inside the container. This parameter maps to ``WorkingDir`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--workdir`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
              

              - **disableNetworking** *(boolean) --* 

                When this parameter is true, networking is disabled within the container. This parameter maps to ``NetworkDisabled`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **privileged** *(boolean) --* 

                When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.

                   

                
              

              - **readonlyRootFilesystem** *(boolean) --* 

                When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--read-only`` option to ``docker run`` .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **dnsServers** *(list) --* 

                A list of DNS servers that are presented to the container. This parameter maps to ``Dns`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--dns`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **dnsSearchDomains** *(list) --* 

                A list of DNS search domains that are presented to the container. This parameter maps to ``DnsSearch`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--dns-search`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **extraHosts** *(list) --* 

                A list of hostnames and IP address mappings to append to the ``/etc/hosts`` file on the container. If using the Fargate launch type, this may be used to list non-Fargate hosts you want the container to talk to. This parameter maps to ``ExtraHosts`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--add-host`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(dict) --* 

                  Hostnames and IP address entries that are added to the ``/etc/hosts`` file of a container via the ``extraHosts`` parameter of its  ContainerDefinition . 

                  
                  

                  - **hostname** *(string) --* 

                    The hostname to use in the ``/etc/hosts`` entry.

                    
                  

                  - **ipAddress** *(string) --* 

                    The IP address to use in the ``/etc/hosts`` entry.

                    
              
            
              

              - **dockerSecurityOptions** *(list) --* 

                A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.

                 

                This parameter maps to ``SecurityOpt`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--security-opt`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  The Amazon ECS container agent running on a container instance must register with the ``ECS_SELINUX_CAPABLE=true`` or ``ECS_APPARMOR_CAPABLE=true`` environment variables before containers placed on that instance can use these security options. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **dockerLabels** *(dict) --* 

                A key/value map of labels to add to the container. This parameter maps to ``Labels`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--label`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **ulimits** *(list) --* 

                A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(dict) --* 

                  The ``ulimit`` settings to pass to the container.

                  
                  

                  - **name** *(string) --* 

                    The ``type`` of the ``ulimit`` .

                    
                  

                  - **softLimit** *(integer) --* 

                    The soft limit for the ulimit type.

                    
                  

                  - **hardLimit** *(integer) --* 

                    The hard limit for the ulimit type.

                    
              
            
              

              - **logConfiguration** *(dict) --* 

                The log configuration specification for the container.

                 

                If using the Fargate launch type, the only supported value is ``awslogs`` .

                 

                This parameter maps to ``LogConfig`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--log-driver`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . By default, containers use the same logging driver that the Docker daemon uses; however the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.docker.com/engine/admin/logging/overview/>`__ in the Docker documentation.

                 

                .. note::

                   

                  Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.

                   

                 

                This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                 

                .. note::

                   

                  The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                
                

                - **logDriver** *(string) --* 

                  The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default. If using the Fargate launch type, the only supported value is ``awslogs`` . For more information about using the ``awslogs`` driver, see `Using the awslogs Log Driver <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                  .. note::

                     

                    If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is `available on GitHub <https://github.com/aws/amazon-ecs-agent>`__ and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.

                     

                   

                  This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
                

                - **options** *(dict) --* 

                  The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
          
        
          

          - **family** *(string) --* 

            The family of your task definition, used as the definition name.

            
          

          - **taskRoleArn** *(string) --* 

            The ARN of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

             

            IAM roles for tasks on Windows require that the ``-EnableTaskIAMRole`` option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code in order to take advantage of the feature. For more information, see `Windows IAM Roles for Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **executionRoleArn** *(string) --* 

            The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

            
          

          - **networkMode** *(string) --* 

            The Docker networking mode to use for the containers in the task. The valid values are ``none`` , ``bridge`` , ``awsvpc`` , and ``host`` . The default Docker network mode is ``bridge`` . If using the Fargate launch type, the ``awsvpc`` network mode is required. If using the EC2 launch type, any network mode can be used. If the network mode is set to ``none`` , you can't specify port mappings in your container definitions, and the task's containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.

             

            With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings. 

             

            If the network mode is ``awsvpc`` , the task is allocated an Elastic Network Interface, and you must specify a  NetworkConfiguration when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

             

            .. note::

               

              Currently, only the Amazon ECS-optimized AMI, other Amazon Linux variants with the ``ecs-init`` package, or AWS Fargate infrastructure support the ``awsvpc`` network mode. 

               

             

            If the network mode is ``host`` , you can't run multiple instantiations of the same task on a single container instance when port mappings are used.

             

            Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. If you use the console to register a task definition with Windows containers, you must choose the ``<default>`` network mode object. 

             

            For more information, see `Network settings <https://docs.docker.com/engine/reference/run/#network-settings>`__ in the *Docker run reference* .

            
          

          - **revision** *(integer) --* 

            The revision of the task in a particular family. The revision is a version number of a task definition in a family. When you register a task definition for the first time, the revision is ``1`` ; each time you register a new revision of a task definition in the same family, the revision value always increases by one (even if you have deregistered previous revisions in this family).

            
          

          - **volumes** *(list) --* 

            The list of volumes in a task.

             

            If you are using the Fargate launch type, the ``host`` and ``sourcePath`` parameters are not supported.

             

            For more information about volume definition parameters and defaults, see `Amazon ECS Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(dict) --* 

              A data volume used in a task definition.

              
              

              - **name** *(string) --* 

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

                
              

              - **host** *(dict) --* 

                The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume, but the data is not guaranteed to persist after the containers associated with it stop running.

                 

                Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount ``C:\my\path:C:\my\path`` and ``D:\:D:\`` , but not ``D:\my\path:C:\my\path`` or ``D:\:C:\my\path`` .

                
                

                - **sourcePath** *(string) --* 

                  The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

                   

                  If you are using the Fargate launch type, the ``sourcePath`` parameter is not supported.

                  
            
          
        
          

          - **status** *(string) --* 

            The status of the task definition.

            
          

          - **requiresAttributes** *(list) --* 

            The container instance attributes required by your task. This field is not valid if using the Fargate launch type for your task.

            
            

            - *(dict) --* 

              An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **name** *(string) --* 

                The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

                
              

              - **value** *(string) --* 

                The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

                
              

              - **targetType** *(string) --* 

                The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

                
              

              - **targetId** *(string) --* 

                The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

                
          
        
          

          - **placementConstraints** *(list) --* 

            An array of placement constraint objects to use for tasks. This field is not valid if using the Fargate launch type for your task.

            
            

            - *(dict) --* 

              An object representing a constraint on task placement in the task definition.

               

              If you are using the Fargate launch type, task placement contraints are not supported.

               

              For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of constraint. The ``DistinctInstance`` constraint ensures that each task in a particular group is running on a different container instance. The ``MemberOf`` constraint restricts selection to be from a group of valid candidates.

                
              

              - **expression** *(string) --* 

                A cluster query language expression to apply to the constraint. For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
          
        
          

          - **compatibilities** *(list) --* 

            The launch type to use with your task. For more information, see `Amazon ECS Launch Types <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(string) --* 
        
          

          - **requiresCompatibilities** *(list) --* 

            The launch type the task is using.

            
            

            - *(string) --* 
        
          

          - **cpu** *(string) --* 

            The number of ``cpu`` units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:

             

             
            * 256 (.25 vCPU) - Available ``memory`` values: 512MB, 1GB, 2GB 
             
            * 512 (.5 vCPU) - Available ``memory`` values: 1GB, 2GB, 3GB, 4GB 
             
            * 1024 (1 vCPU) - Available ``memory`` values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 
             
            * 2048 (2 vCPU) - Available ``memory`` values: Between 4GB and 16GB in 1GB increments 
             
            * 4096 (4 vCPU) - Available ``memory`` values: Between 8GB and 30GB in 1GB increments 
             

            
          

          - **memory** *(string) --* 

            The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:

             

             
            * 512MB, 1GB, 2GB - Available ``cpu`` values: 256 (.25 vCPU) 
             
            * 1GB, 2GB, 3GB, 4GB - Available ``cpu`` values: 512 (.5 vCPU) 
             
            * 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available ``cpu`` values: 1024 (1 vCPU) 
             
            * Between 4GB and 16GB in 1GB increments - Available ``cpu`` values: 2048 (2 vCPU) 
             
            * Between 8GB and 30GB in 1GB increments - Available ``cpu`` values: 4096 (4 vCPU) 
             

            
      
    

    **Examples** 

    This example provides a description of the specified task definition.
    ::

      response = client.describe_task_definition(
          taskDefinition='hello_world:8',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'taskDefinition': {
              'containerDefinitions': [
                  {
                      'name': 'wordpress',
                      'cpu': 10,
                      'environment': [
                      ],
                      'essential': True,
                      'image': 'wordpress',
                      'links': [
                          'mysql',
                      ],
                      'memory': 500,
                      'mountPoints': [
                      ],
                      'portMappings': [
                          {
                              'containerPort': 80,
                              'hostPort': 80,
                          },
                      ],
                      'volumesFrom': [
                      ],
                  },
                  {
                      'name': 'mysql',
                      'cpu': 10,
                      'environment': [
                          {
                              'name': 'MYSQL_ROOT_PASSWORD',
                              'value': 'password',
                          },
                      ],
                      'essential': True,
                      'image': 'mysql',
                      'memory': 500,
                      'mountPoints': [
                      ],
                      'portMappings': [
                      ],
                      'volumesFrom': [
                      ],
                  },
              ],
              'family': 'hello_world',
              'revision': 8,
              'taskDefinitionArn': 'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/hello_world:8',
              'volumes': [
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_tasks(**kwargs)

    

    Describes a specified task or tasks.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTasks>`_    


    **Request Syntax** 
    ::

      response = client.describe_tasks(
          cluster='string',
          tasks=[
              'string',
          ]
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to describe. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type tasks: list
    :param tasks: **[REQUIRED]** 

      A list of up to 100 task IDs or full ARN entries.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tasks': [
                {
                    'taskArn': 'string',
                    'clusterArn': 'string',
                    'taskDefinitionArn': 'string',
                    'containerInstanceArn': 'string',
                    'overrides': {
                        'containerOverrides': [
                            {
                                'name': 'string',
                                'command': [
                                    'string',
                                ],
                                'environment': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'cpu': 123,
                                'memory': 123,
                                'memoryReservation': 123
                            },
                        ],
                        'taskRoleArn': 'string',
                        'executionRoleArn': 'string'
                    },
                    'lastStatus': 'string',
                    'desiredStatus': 'string',
                    'cpu': 'string',
                    'memory': 'string',
                    'containers': [
                        {
                            'containerArn': 'string',
                            'taskArn': 'string',
                            'name': 'string',
                            'lastStatus': 'string',
                            'exitCode': 123,
                            'reason': 'string',
                            'networkBindings': [
                                {
                                    'bindIP': 'string',
                                    'containerPort': 123,
                                    'hostPort': 123,
                                    'protocol': 'tcp'|'udp'
                                },
                            ],
                            'networkInterfaces': [
                                {
                                    'attachmentId': 'string',
                                    'privateIpv4Address': 'string',
                                    'ipv6Address': 'string'
                                },
                            ]
                        },
                    ],
                    'startedBy': 'string',
                    'version': 123,
                    'stoppedReason': 'string',
                    'connectivity': 'CONNECTED'|'DISCONNECTED',
                    'connectivityAt': datetime(2015, 1, 1),
                    'pullStartedAt': datetime(2015, 1, 1),
                    'pullStoppedAt': datetime(2015, 1, 1),
                    'executionStoppedAt': datetime(2015, 1, 1),
                    'createdAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'stoppingAt': datetime(2015, 1, 1),
                    'stoppedAt': datetime(2015, 1, 1),
                    'group': 'string',
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                },
            ],
            'failures': [
                {
                    'arn': 'string',
                    'reason': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tasks** *(list) --* 

          The list of tasks.

          
          

          - *(dict) --* 

            Details on a task in a cluster.

            
            

            - **taskArn** *(string) --* 

              The Amazon Resource Name (ARN) of the task.

              
            

            - **clusterArn** *(string) --* 

              The ARN of the cluster that hosts the task.

              
            

            - **taskDefinitionArn** *(string) --* 

              The ARN of the task definition that creates the task.

              
            

            - **containerInstanceArn** *(string) --* 

              The ARN of the container instances that host the task.

              
            

            - **overrides** *(dict) --* 

              One or more container overrides.

              
              

              - **containerOverrides** *(list) --* 

                One or more container overrides sent to a task.

                
                

                - *(dict) --* 

                  The overrides that should be sent to a container.

                  
                  

                  - **name** *(string) --* 

                    The name of the container that receives the override. This parameter is required if any override is specified.

                    
                  

                  - **command** *(list) --* 

                    The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

                    
                    

                    - *(string) --* 
                
                  

                  - **environment** *(list) --* 

                    The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

                    
                    

                    - *(dict) --* 

                      A key and value pair object.

                      
                      

                      - **name** *(string) --* 

                        The name of the key value pair. For environment variables, this is the name of the environment variable.

                        
                      

                      - **value** *(string) --* 

                        The value of the key value pair. For environment variables, this is the value of the environment variable.

                        
                  
                
                  

                  - **cpu** *(integer) --* 

                    The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

                    
                  

                  - **memory** *(integer) --* 

                    The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

                    
                  

                  - **memoryReservation** *(integer) --* 

                    The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

                    
              
            
              

              - **taskRoleArn** *(string) --* 

                The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

                
              

              - **executionRoleArn** *(string) --* 

                The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

                
          
            

            - **lastStatus** *(string) --* 

              The last known status of the task.

              
            

            - **desiredStatus** *(string) --* 

              The desired status of the task.

              
            

            - **cpu** *(string) --* 

              The number of ``cpu`` units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:

               

               
              * 256 (.25 vCPU) - Available ``memory`` values: 512MB, 1GB, 2GB 
               
              * 512 (.5 vCPU) - Available ``memory`` values: 1GB, 2GB, 3GB, 4GB 
               
              * 1024 (1 vCPU) - Available ``memory`` values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 
               
              * 2048 (2 vCPU) - Available ``memory`` values: Between 4GB and 16GB in 1GB increments 
               
              * 4096 (4 vCPU) - Available ``memory`` values: Between 8GB and 30GB in 1GB increments 
               

              
            

            - **memory** *(string) --* 

              The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:

               

               
              * 512MB, 1GB, 2GB - Available ``cpu`` values: 256 (.25 vCPU) 
               
              * 1GB, 2GB, 3GB, 4GB - Available ``cpu`` values: 512 (.5 vCPU) 
               
              * 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available ``cpu`` values: 1024 (1 vCPU) 
               
              * Between 4GB and 16GB in 1GB increments - Available ``cpu`` values: 2048 (2 vCPU) 
               
              * Between 8GB and 30GB in 1GB increments - Available ``cpu`` values: 4096 (4 vCPU) 
               

              
            

            - **containers** *(list) --* 

              The containers associated with the task.

              
              

              - *(dict) --* 

                A Docker container that is part of a task.

                
                

                - **containerArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the container.

                  
                

                - **taskArn** *(string) --* 

                  The ARN of the task.

                  
                

                - **name** *(string) --* 

                  The name of the container.

                  
                

                - **lastStatus** *(string) --* 

                  The last known status of the container.

                  
                

                - **exitCode** *(integer) --* 

                  The exit code returned from the container.

                  
                

                - **reason** *(string) --* 

                  A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

                  
                

                - **networkBindings** *(list) --* 

                  The network bindings associated with the container.

                  
                  

                  - *(dict) --* 

                    Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

                    
                    

                    - **bindIP** *(string) --* 

                      The IP address that the container is bound to on the container instance.

                      
                    

                    - **containerPort** *(integer) --* 

                      The port number on the container that is used with the network binding.

                      
                    

                    - **hostPort** *(integer) --* 

                      The port number on the host that is used with the network binding.

                      
                    

                    - **protocol** *(string) --* 

                      The protocol used for the network binding.

                      
                
              
                

                - **networkInterfaces** *(list) --* 

                  The network interfaces associated with the container.

                  
                  

                  - *(dict) --* 

                    An object representing the Elastic Network Interface for tasks that use the ``awsvpc`` network mode.

                    
                    

                    - **attachmentId** *(string) --* 

                      The attachment ID for the network interface.

                      
                    

                    - **privateIpv4Address** *(string) --* 

                      The private IPv4 address for the network interface.

                      
                    

                    - **ipv6Address** *(string) --* 

                      The private IPv6 address for the network interface.

                      
                
              
            
          
            

            - **startedBy** *(string) --* 

              The tag specified when a task is started. If the task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.

              
            

            - **version** *(integer) --* 

              The version counter for the task. Every time a task experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the task (inside the ``detail`` object) to verify that the version in your event stream is current.

              
            

            - **stoppedReason** *(string) --* 

              The reason the task was stopped.

              
            

            - **connectivity** *(string) --* 

              The connectivity status of a task.

              
            

            - **connectivityAt** *(datetime) --* 

              The Unix time stamp for when the task last went into ``CONNECTED`` status.

              
            

            - **pullStartedAt** *(datetime) --* 

              The Unix time stamp for when the container image pull began.

              
            

            - **pullStoppedAt** *(datetime) --* 

              The Unix time stamp for when the container image pull completed.

              
            

            - **executionStoppedAt** *(datetime) --* 

              The Unix timestamp for when the task execution stopped.

              
            

            - **createdAt** *(datetime) --* 

              The Unix time stamp for when the task was created (the task entered the ``PENDING`` state).

              
            

            - **startedAt** *(datetime) --* 

              The Unix time stamp for when the task started (the task transitioned from the ``PENDING`` state to the ``RUNNING`` state).

              
            

            - **stoppingAt** *(datetime) --* 

              The Unix time stamp for when the task will stop (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).

              
            

            - **stoppedAt** *(datetime) --* 

              The Unix time stamp for when the task was stopped (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).

              
            

            - **group** *(string) --* 

              The name of the task group associated with the task.

              
            

            - **launchType** *(string) --* 

              The launch type on which your task is running.

              
            

            - **platformVersion** *(string) --* 

              The platform version on which your task is running. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
            

            - **attachments** *(list) --* 

              The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network mode.

              
              

              - *(dict) --* 

                An object representing a container instance or task attachment.

                
                

                - **id** *(string) --* 

                  The unique identifier for the attachment.

                  
                

                - **type** *(string) --* 

                  The type of the attachment, such as an ``ElasticNetworkInterface`` .

                  
                

                - **status** *(string) --* 

                  The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                  
                

                - **details** *(list) --* 

                  Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                  
                  

                  - *(dict) --* 

                    A key and value pair object.

                    
                    

                    - **name** *(string) --* 

                      The name of the key value pair. For environment variables, this is the name of the environment variable.

                      
                    

                    - **value** *(string) --* 

                      The value of the key value pair. For environment variables, this is the value of the environment variable.

                      
                
              
            
          
        
      
        

        - **failures** *(list) --* 

          Any failures associated with the call.

          
          

          - *(dict) --* 

            A failed resource.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the failed resource.

              
            

            - **reason** *(string) --* 

              The reason for the failure.

              
        
      
    

    **Examples** 

    This example provides a description of the specified task, using the task UUID as an identifier.
    ::

      response = client.describe_tasks(
          tasks=[
              'c5cba4eb-5dad-405e-96db-71ef8eefe6a8',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'failures': [
          ],
          'tasks': [
              {
                  'clusterArn': 'arn:aws:ecs:<region>:<aws_account_id>:cluster/default',
                  'containerInstanceArn': 'arn:aws:ecs:<region>:<aws_account_id>:container-instance/18f9eda5-27d7-4c19-b133-45adc516e8fb',
                  'containers': [
                      {
                          'name': 'ecs-demo',
                          'containerArn': 'arn:aws:ecs:<region>:<aws_account_id>:container/7c01765b-c588-45b3-8290-4ba38bd6c5a6',
                          'lastStatus': 'RUNNING',
                          'networkBindings': [
                              {
                                  'bindIP': '0.0.0.0',
                                  'containerPort': 80,
                                  'hostPort': 80,
                              },
                          ],
                          'taskArn': 'arn:aws:ecs:<region>:<aws_account_id>:task/c5cba4eb-5dad-405e-96db-71ef8eefe6a8',
                      },
                  ],
                  'desiredStatus': 'RUNNING',
                  'lastStatus': 'RUNNING',
                  'overrides': {
                      'containerOverrides': [
                          {
                              'name': 'ecs-demo',
                          },
                      ],
                  },
                  'startedBy': 'ecs-svc/9223370608528463088',
                  'taskArn': 'arn:aws:ecs:<region>:<aws_account_id>:task/c5cba4eb-5dad-405e-96db-71ef8eefe6a8',
                  'taskDefinitionArn': 'arn:aws:ecs:<region>:<aws_account_id>:task-definition/amazon-ecs-sample:1',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: discover_poll_endpoint(**kwargs)

    

    .. note::

       

      This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

       

     

    Returns an endpoint for the Amazon ECS agent to poll for updates.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DiscoverPollEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.discover_poll_endpoint(
          containerInstance='string',
          cluster='string'
      )
    :type containerInstance: string
    :param containerInstance: 

      The container instance ID or full ARN of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .

      

    
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that the container instance belongs to.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'endpoint': 'string',
            'telemetryEndpoint': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **endpoint** *(string) --* 

          The endpoint for the Amazon ECS agent to poll.

          
        

        - **telemetryEndpoint** *(string) --* 

          The telemetry endpoint for the Amazon ECS agent.

          
    

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

        


  .. py:method:: list_attributes(**kwargs)

    

    Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, ``ListAttributes`` returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value, for example, to see which container instances in a cluster are running a Linux AMI (``ecs.os-type=linux`` ). 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListAttributes>`_    


    **Request Syntax** 
    ::

      response = client.list_attributes(
          cluster='string',
          targetType='container-instance',
          attributeName='string',
          attributeValue='string',
          nextToken='string',
          maxResults=123
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type targetType: string
    :param targetType: **[REQUIRED]** 

      The type of the target with which to list attributes.

      

    
    :type attributeName: string
    :param attributeName: 

      The name of the attribute with which to filter the results. 

      

    
    :type attributeValue: string
    :param attributeValue: 

      The value of the attribute with which to filter results. You must also specify an attribute name to use this parameter.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``ListAttributes`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of cluster results returned by ``ListAttributes`` in paginated output. When this parameter is used, ``ListAttributes`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListAttributes`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListAttributes`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'attributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **attributes** *(list) --* 

          A list of attribute objects that meet the criteria of the request.

          
          

          - *(dict) --* 

            An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - **name** *(string) --* 

              The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

              
            

            - **value** *(string) --* 

              The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

              
            

            - **targetType** *(string) --* 

              The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

              
            

            - **targetId** *(string) --* 

              The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

              
        
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``ListAttributes`` request. When the results of a ``ListAttributes`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

  .. py:method:: list_clusters(**kwargs)

    

    Returns a list of existing clusters.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListClusters>`_    


    **Request Syntax** 
    ::

      response = client.list_clusters(
          nextToken='string',
          maxResults=123
      )
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``ListClusters`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of cluster results returned by ``ListClusters`` in paginated output. When this parameter is used, ``ListClusters`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListClusters`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListClusters`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'clusterArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **clusterArns** *(list) --* 

          The list of full Amazon Resource Name (ARN) entries for each cluster associated with your account.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``ListClusters`` request. When the results of a ``ListClusters`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example lists all of your available clusters in your default region.
    ::

      response = client.list_clusters(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'clusterArns': [
              'arn:aws:ecs:us-east-1:<aws_account_id>:cluster/test',
              'arn:aws:ecs:us-east-1:<aws_account_id>:cluster/default',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_container_instances(**kwargs)

    

    Returns a list of container instances in a specified cluster. You can filter the results of a ``ListContainerInstances`` operation with cluster query language statements inside the ``filter`` parameter. For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListContainerInstances>`_    


    **Request Syntax** 
    ::

      response = client.list_container_instances(
          cluster='string',
          filter='string',
          nextToken='string',
          maxResults=123,
          status='ACTIVE'|'DRAINING'
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type filter: string
    :param filter: 

      You can filter the results of a ``ListContainerInstances`` operation with cluster query language statements. For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``ListContainerInstances`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of container instance results returned by ``ListContainerInstances`` in paginated output. When this parameter is used, ``ListContainerInstances`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListContainerInstances`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListContainerInstances`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    :type status: string
    :param status: 

      Filters the container instances by status. For example, if you specify the ``DRAINING`` status, the results include only container instances that have been set to ``DRAINING`` using  UpdateContainerInstancesState . If you do not specify this parameter, the default is to include container instances set to ``ACTIVE`` and ``DRAINING`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'containerInstanceArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **containerInstanceArns** *(list) --* 

          The list of container instances with full ARN entries for each container instance associated with the specified cluster.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``ListContainerInstances`` request. When the results of a ``ListContainerInstances`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example lists all of your available container instances in the specified cluster in your default region.
    ::

      response = client.list_container_instances(
          cluster='default',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'containerInstanceArns': [
              'arn:aws:ecs:us-east-1:<aws_account_id>:container-instance/f6bbb147-5370-4ace-8c73-c7181ded911f',
              'arn:aws:ecs:us-east-1:<aws_account_id>:container-instance/ffe3d344-77e2-476c-a4d0-bf560ad50acb',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_services(**kwargs)

    

    Lists the services that are running in a specified cluster.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListServices>`_    


    **Request Syntax** 
    ::

      response = client.list_services(
          cluster='string',
          nextToken='string',
          maxResults=123,
          launchType='EC2'|'FARGATE'
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the services to list. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``ListServices`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of service results returned by ``ListServices`` in paginated output. When this parameter is used, ``ListServices`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListServices`` request with the returned ``nextToken`` value. This value can be between 1 and 10. If this parameter is not used, then ``ListServices`` returns up to 10 results and a ``nextToken`` value if applicable.

      

    
    :type launchType: string
    :param launchType: 

      The launch type for services you want to list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'serviceArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **serviceArns** *(list) --* 

          The list of full ARN entries for each service associated with the specified cluster.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``ListServices`` request. When the results of a ``ListServices`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example lists the services running in the default cluster for an account.
    ::

      response = client.list_services(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'serviceArns': [
              'arn:aws:ecs:us-east-1:012345678910:service/my-http-service',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_task_definition_families(**kwargs)

    

    Returns a list of task definition families that are registered to your account (which may include task definition families that no longer have any ``ACTIVE`` task definition revisions).

     

    You can filter out task definition families that do not contain any ``ACTIVE`` task definition revisions by setting the ``status`` parameter to ``ACTIVE`` . You can also filter the results with the ``familyPrefix`` parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTaskDefinitionFamilies>`_    


    **Request Syntax** 
    ::

      response = client.list_task_definition_families(
          familyPrefix='string',
          status='ACTIVE'|'INACTIVE'|'ALL',
          nextToken='string',
          maxResults=123
      )
    :type familyPrefix: string
    :param familyPrefix: 

      The ``familyPrefix`` is a string that is used to filter the results of ``ListTaskDefinitionFamilies`` . If you specify a ``familyPrefix`` , only task definition family names that begin with the ``familyPrefix`` string are returned.

      

    
    :type status: string
    :param status: 

      The task definition family status with which to filter the ``ListTaskDefinitionFamilies`` results. By default, both ``ACTIVE`` and ``INACTIVE`` task definition families are listed. If this parameter is set to ``ACTIVE`` , only task definition families that have an ``ACTIVE`` task definition revision are returned. If this parameter is set to ``INACTIVE`` , only task definition families that do not have any ``ACTIVE`` task definition revisions are returned. If you paginate the resulting output, be sure to keep the ``status`` value constant in each subsequent request.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``ListTaskDefinitionFamilies`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of task definition family results returned by ``ListTaskDefinitionFamilies`` in paginated output. When this parameter is used, ``ListTaskDefinitions`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListTaskDefinitionFamilies`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListTaskDefinitionFamilies`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'families': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **families** *(list) --* 

          The list of task definition family names that match the ``ListTaskDefinitionFamilies`` request.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``ListTaskDefinitionFamilies`` request. When the results of a ``ListTaskDefinitionFamilies`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example lists all of your registered task definition families.
    ::

      response = client.list_task_definition_families(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'families': [
              'node-js-app',
              'web-timer',
              'hpcc',
              'hpcc-c4-8xlarge',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example lists the task definition revisions that start with "hpcc".
    ::

      response = client.list_task_definition_families(
          familyPrefix='hpcc',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'families': [
              'hpcc',
              'hpcc-c4-8xlarge',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_task_definitions(**kwargs)

    

    Returns a list of task definitions that are registered to your account. You can filter the results by family name with the ``familyPrefix`` parameter or by status with the ``status`` parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTaskDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.list_task_definitions(
          familyPrefix='string',
          status='ACTIVE'|'INACTIVE',
          sort='ASC'|'DESC',
          nextToken='string',
          maxResults=123
      )
    :type familyPrefix: string
    :param familyPrefix: 

      The full family name with which to filter the ``ListTaskDefinitions`` results. Specifying a ``familyPrefix`` limits the listed task definitions to task definition revisions that belong to that family.

      

    
    :type status: string
    :param status: 

      The task definition status with which to filter the ``ListTaskDefinitions`` results. By default, only ``ACTIVE`` task definitions are listed. By setting this parameter to ``INACTIVE`` , you can view task definitions that are ``INACTIVE`` as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the ``status`` value constant in each subsequent request.

      

    
    :type sort: string
    :param sort: 

      The order in which to sort the results. Valid values are ``ASC`` and ``DESC`` . By default (``ASC`` ), task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to ``DESC`` reverses the sort order on family name and revision so that the newest task definitions in a family are listed first.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``ListTaskDefinitions`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of task definition results returned by ``ListTaskDefinitions`` in paginated output. When this parameter is used, ``ListTaskDefinitions`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListTaskDefinitions`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListTaskDefinitions`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskDefinitionArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskDefinitionArns** *(list) --* 

          The list of task definition Amazon Resource Name (ARN) entries for the ``ListTaskDefinitions`` request.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``ListTaskDefinitions`` request. When the results of a ``ListTaskDefinitions`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example lists all of your registered task definitions.
    ::

      response = client.list_task_definitions(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'taskDefinitionArns': [
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/sleep300:2',
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/sleep360:1',
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/wordpress:3',
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/wordpress:4',
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/wordpress:5',
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/wordpress:6',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example lists the task definition revisions of a specified family.
    ::

      response = client.list_task_definitions(
          familyPrefix='wordpress',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'taskDefinitionArns': [
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/wordpress:3',
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/wordpress:4',
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/wordpress:5',
              'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/wordpress:6',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_tasks(**kwargs)

    

    Returns a list of tasks for a specified cluster. You can filter the results by family name, by a particular container instance, or by the desired status of the task with the ``family`` , ``containerInstance`` , and ``desiredStatus`` parameters.

     

    Recently stopped tasks might appear in the returned results. Currently, stopped tasks appear in the returned results for at least one hour. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTasks>`_    


    **Request Syntax** 
    ::

      response = client.list_tasks(
          cluster='string',
          containerInstance='string',
          family='string',
          nextToken='string',
          maxResults=123,
          startedBy='string',
          serviceName='string',
          desiredStatus='RUNNING'|'PENDING'|'STOPPED',
          launchType='EC2'|'FARGATE'
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the tasks to list. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type containerInstance: string
    :param containerInstance: 

      The container instance ID or full ARN of the container instance with which to filter the ``ListTasks`` results. Specifying a ``containerInstance`` limits the results to tasks that belong to that container instance.

      

    
    :type family: string
    :param family: 

      The name of the family with which to filter the ``ListTasks`` results. Specifying a ``family`` limits the results to tasks that belong to that family.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``ListTasks`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of task results returned by ``ListTasks`` in paginated output. When this parameter is used, ``ListTasks`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListTasks`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListTasks`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    :type startedBy: string
    :param startedBy: 

      The ``startedBy`` value with which to filter the task results. Specifying a ``startedBy`` value limits the results to tasks that were started with that value.

      

    
    :type serviceName: string
    :param serviceName: 

      The name of the service with which to filter the ``ListTasks`` results. Specifying a ``serviceName`` limits the results to tasks that belong to that service.

      

    
    :type desiredStatus: string
    :param desiredStatus: 

      The task desired status with which to filter the ``ListTasks`` results. Specifying a ``desiredStatus`` of ``STOPPED`` limits the results to tasks that Amazon ECS has set the desired status to ``STOPPED`` , which can be useful for debugging tasks that are not starting properly or have died or finished. The default status filter is ``RUNNING`` , which shows tasks that Amazon ECS has set the desired status to ``RUNNING`` .

       

      .. note::

         

        Although you can filter results based on a desired status of ``PENDING`` , this does not return any results because Amazon ECS never sets the desired status of a task to that value (only a task's ``lastStatus`` may have a value of ``PENDING`` ).

         

      

    
    :type launchType: string
    :param launchType: 

      The launch type for services you want to list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskArns** *(list) --* 

          The list of task ARN entries for the ``ListTasks`` request.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``ListTasks`` request. When the results of a ``ListTasks`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example lists all of the tasks in a cluster.
    ::

      response = client.list_tasks(
          cluster='default',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'taskArns': [
              'arn:aws:ecs:us-east-1:012345678910:task/0cc43cdb-3bee-4407-9c26-c0e6ea5bee84',
              'arn:aws:ecs:us-east-1:012345678910:task/6b809ef6-c67e-4467-921f-ee261c15a0a1',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example lists the tasks of a specified container instance. Specifying a ``containerInstance`` value limits  the  results  to  tasks  that belong to that container instance.
    ::

      response = client.list_tasks(
          cluster='default',
          containerInstance='f6bbb147-5370-4ace-8c73-c7181ded911f',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'taskArns': [
              'arn:aws:ecs:us-east-1:012345678910:task/0cc43cdb-3bee-4407-9c26-c0e6ea5bee84',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: put_attributes(**kwargs)

    

    Create or update an attribute on an Amazon ECS resource. If the attribute does not exist, it is created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use  DeleteAttributes . For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/PutAttributes>`_    


    **Request Syntax** 
    ::

      response = client.put_attributes(
          cluster='string',
          attributes=[
              {
                  'name': 'string',
                  'value': 'string',
                  'targetType': 'container-instance',
                  'targetId': 'string'
              },
          ]
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type attributes: list
    :param attributes: **[REQUIRED]** 

      The attributes to apply to your resource. You can specify up to 10 custom attributes per resource. You can specify up to 10 attributes in a single call.

      

    
      - *(dict) --* 

        An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

        

      
        - **name** *(string) --* **[REQUIRED]** 

          The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

          

        
        - **value** *(string) --* 

          The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

          

        
        - **targetType** *(string) --* 

          The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

          

        
        - **targetId** *(string) --* 

          The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'attributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **attributes** *(list) --* 

          The attributes applied to your resource.

          
          

          - *(dict) --* 

            An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - **name** *(string) --* 

              The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

              
            

            - **value** *(string) --* 

              The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

              
            

            - **targetType** *(string) --* 

              The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

              
            

            - **targetId** *(string) --* 

              The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

              
        
      
    

  .. py:method:: register_container_instance(**kwargs)

    

    .. note::

       

      This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

       

     

    Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/RegisterContainerInstance>`_    


    **Request Syntax** 
    ::

      response = client.register_container_instance(
          cluster='string',
          instanceIdentityDocument='string',
          instanceIdentityDocumentSignature='string',
          totalResources=[
              {
                  'name': 'string',
                  'type': 'string',
                  'doubleValue': 123.0,
                  'longValue': 123,
                  'integerValue': 123,
                  'stringSetValue': [
                      'string',
                  ]
              },
          ],
          versionInfo={
              'agentVersion': 'string',
              'agentHash': 'string',
              'dockerVersion': 'string'
          },
          containerInstanceArn='string',
          attributes=[
              {
                  'name': 'string',
                  'value': 'string',
                  'targetType': 'container-instance',
                  'targetId': 'string'
              },
          ]
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster with which to register your container instance. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type instanceIdentityDocument: string
    :param instanceIdentityDocument: 

      The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: ``curl http://169.254.169.254/latest/dynamic/instance-identity/document/``  

      

    
    :type instanceIdentityDocumentSignature: string
    :param instanceIdentityDocumentSignature: 

      The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: ``curl http://169.254.169.254/latest/dynamic/instance-identity/signature/``  

      

    
    :type totalResources: list
    :param totalResources: 

      The resources available on the instance.

      

    
      - *(dict) --* 

        Describes the resources available for a container instance.

        

      
        - **name** *(string) --* 

          The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

          

        
        - **type** *(string) --* 

          The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

          

        
        - **doubleValue** *(float) --* 

          When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

          

        
        - **longValue** *(integer) --* 

          When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

          

        
        - **integerValue** *(integer) --* 

          When the ``integerValue`` type is set, the value of the resource must be an integer.

          

        
        - **stringSetValue** *(list) --* 

          When the ``stringSetValue`` type is set, the value of the resource must be a string type.

          

        
          - *(string) --* 

          
      
      
  
    :type versionInfo: dict
    :param versionInfo: 

      The version information for the Amazon ECS container agent and Docker daemon running on the container instance.

      

    
      - **agentVersion** *(string) --* 

        The version number of the Amazon ECS container agent.

        

      
      - **agentHash** *(string) --* 

        The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.

        

      
      - **dockerVersion** *(string) --* 

        The Docker version running on the container instance.

        

      
    
    :type containerInstanceArn: string
    :param containerInstanceArn: 

      The ARN of the container instance (if it was previously registered).

      

    
    :type attributes: list
    :param attributes: 

      The container instance attributes that this container instance supports.

      

    
      - *(dict) --* 

        An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

        

      
        - **name** *(string) --* **[REQUIRED]** 

          The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

          

        
        - **value** *(string) --* 

          The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

          

        
        - **targetType** *(string) --* 

          The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

          

        
        - **targetId** *(string) --* 

          The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'containerInstance': {
                'containerInstanceArn': 'string',
                'ec2InstanceId': 'string',
                'version': 123,
                'versionInfo': {
                    'agentVersion': 'string',
                    'agentHash': 'string',
                    'dockerVersion': 'string'
                },
                'remainingResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'registeredResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'status': 'string',
                'agentConnected': True|False,
                'runningTasksCount': 123,
                'pendingTasksCount': 123,
                'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                'attributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'registeredAt': datetime(2015, 1, 1),
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **containerInstance** *(dict) --* 

          The container instance that was registered.

          
          

          - **containerInstanceArn** *(string) --* 

            The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .

            
          

          - **ec2InstanceId** *(string) --* 

            The EC2 instance ID of the container instance.

            
          

          - **version** *(integer) --* 

            The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.

            
          

          - **versionInfo** *(dict) --* 

            The version information for the Amazon ECS container agent and Docker daemon running on the container instance.

            
            

            - **agentVersion** *(string) --* 

              The version number of the Amazon ECS container agent.

              
            

            - **agentHash** *(string) --* 

              The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.

              
            

            - **dockerVersion** *(string) --* 

              The Docker version running on the container instance.

              
        
          

          - **remainingResources** *(list) --* 

            For most resource types, this parameter describes the remaining resources of the container instance that are available for new tasks. For port resource types, this parameter describes the ports that are reserved by the Amazon ECS container agent and any containers that have reserved port mappings; any port that is not specified here is available for new tasks.

            
            

            - *(dict) --* 

              Describes the resources available for a container instance.

              
              

              - **name** *(string) --* 

                The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                
              

              - **type** *(string) --* 

                The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                
              

              - **doubleValue** *(float) --* 

                When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                
              

              - **longValue** *(integer) --* 

                When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                
              

              - **integerValue** *(integer) --* 

                When the ``integerValue`` type is set, the value of the resource must be an integer.

                
              

              - **stringSetValue** *(list) --* 

                When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                
                

                - *(string) --* 
            
          
        
          

          - **registeredResources** *(list) --* 

            For most resource types, this parameter describes the registered resources on the container instance that are in use by current tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.

            
            

            - *(dict) --* 

              Describes the resources available for a container instance.

              
              

              - **name** *(string) --* 

                The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                
              

              - **type** *(string) --* 

                The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                
              

              - **doubleValue** *(float) --* 

                When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                
              

              - **longValue** *(integer) --* 

                When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                
              

              - **integerValue** *(integer) --* 

                When the ``integerValue`` type is set, the value of the resource must be an integer.

                
              

              - **stringSetValue** *(list) --* 

                When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                
                

                - *(string) --* 
            
          
        
          

          - **status** *(string) --* 

            The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **agentConnected** *(boolean) --* 

            This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Instances without a connected agent can't accept placement requests.

            
          

          - **runningTasksCount** *(integer) --* 

            The number of tasks on the container instance that are in the ``RUNNING`` status.

            
          

          - **pendingTasksCount** *(integer) --* 

            The number of tasks on the container instance that are in the ``PENDING`` status.

            
          

          - **agentUpdateStatus** *(string) --* 

            The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .

            
          

          - **attributes** *(list) --* 

            The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.

            
            

            - *(dict) --* 

              An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **name** *(string) --* 

                The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

                
              

              - **value** *(string) --* 

                The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

                
              

              - **targetType** *(string) --* 

                The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

                
              

              - **targetId** *(string) --* 

                The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

                
          
        
          

          - **registeredAt** *(datetime) --* 

            The Unix time stamp for when the container instance was registered.

            
          

          - **attachments** *(list) --* 

            The Elastic Network Interfaces associated with the container instance.

            
            

            - *(dict) --* 

              An object representing a container instance or task attachment.

              
              

              - **id** *(string) --* 

                The unique identifier for the attachment.

                
              

              - **type** *(string) --* 

                The type of the attachment, such as an ``ElasticNetworkInterface`` .

                
              

              - **status** *(string) --* 

                The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                
              

              - **details** *(list) --* 

                Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                
                

                - *(dict) --* 

                  A key and value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key value pair. For environment variables, this is the value of the environment variable.

                    
              
            
          
        
      
    

  .. py:method:: register_task_definition(**kwargs)

    

    Registers a new task definition from the supplied ``family`` and ``containerDefinitions`` . Optionally, you can add data volumes to your containers with the ``volumes`` parameter. For more information about task definition parameters and defaults, see `Amazon ECS Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

     

    You can specify an IAM role for your task with the ``taskRoleArn`` parameter. When you specify an IAM role for a task, its containers can then use the latest versions of the AWS CLI or SDKs to make API requests to the AWS services that are specified in the IAM policy associated with the role. For more information, see `IAM Roles for Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

     

    You can specify a Docker networking mode for the containers in your task definition with the ``networkMode`` parameter. The available network modes correspond to those described in `Network settings <https://docs.docker.com/engine/reference/run/#/network-settings>`__ in the Docker run reference. If you specify the ``awsvpc`` network mode, the task is allocated an Elastic Network Interface, and you must specify a  NetworkConfiguration when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/RegisterTaskDefinition>`_    


    **Request Syntax** 
    ::

      response = client.register_task_definition(
          family='string',
          taskRoleArn='string',
          executionRoleArn='string',
          networkMode='bridge'|'host'|'awsvpc'|'none',
          containerDefinitions=[
              {
                  'name': 'string',
                  'image': 'string',
                  'cpu': 123,
                  'memory': 123,
                  'memoryReservation': 123,
                  'links': [
                      'string',
                  ],
                  'portMappings': [
                      {
                          'containerPort': 123,
                          'hostPort': 123,
                          'protocol': 'tcp'|'udp'
                      },
                  ],
                  'essential': True|False,
                  'entryPoint': [
                      'string',
                  ],
                  'command': [
                      'string',
                  ],
                  'environment': [
                      {
                          'name': 'string',
                          'value': 'string'
                      },
                  ],
                  'mountPoints': [
                      {
                          'sourceVolume': 'string',
                          'containerPath': 'string',
                          'readOnly': True|False
                      },
                  ],
                  'volumesFrom': [
                      {
                          'sourceContainer': 'string',
                          'readOnly': True|False
                      },
                  ],
                  'linuxParameters': {
                      'capabilities': {
                          'add': [
                              'string',
                          ],
                          'drop': [
                              'string',
                          ]
                      },
                      'devices': [
                          {
                              'hostPath': 'string',
                              'containerPath': 'string',
                              'permissions': [
                                  'read'|'write'|'mknod',
                              ]
                          },
                      ],
                      'initProcessEnabled': True|False
                  },
                  'hostname': 'string',
                  'user': 'string',
                  'workingDirectory': 'string',
                  'disableNetworking': True|False,
                  'privileged': True|False,
                  'readonlyRootFilesystem': True|False,
                  'dnsServers': [
                      'string',
                  ],
                  'dnsSearchDomains': [
                      'string',
                  ],
                  'extraHosts': [
                      {
                          'hostname': 'string',
                          'ipAddress': 'string'
                      },
                  ],
                  'dockerSecurityOptions': [
                      'string',
                  ],
                  'dockerLabels': {
                      'string': 'string'
                  },
                  'ulimits': [
                      {
                          'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                          'softLimit': 123,
                          'hardLimit': 123
                      },
                  ],
                  'logConfiguration': {
                      'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                      'options': {
                          'string': 'string'
                      }
                  }
              },
          ],
          volumes=[
              {
                  'name': 'string',
                  'host': {
                      'sourcePath': 'string'
                  }
              },
          ],
          placementConstraints=[
              {
                  'type': 'memberOf',
                  'expression': 'string'
              },
          ],
          requiresCompatibilities=[
              'EC2'|'FARGATE',
          ],
          cpu='string',
          memory='string'
      )
    :type family: string
    :param family: **[REQUIRED]** 

      You must specify a ``family`` for a task definition, which allows you to track multiple versions of the same task definition. The ``family`` is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

      

    
    :type taskRoleArn: string
    :param taskRoleArn: 

      The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see `IAM Roles for Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

      

    
    :type executionRoleArn: string
    :param executionRoleArn: 

      The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

      

    
    :type networkMode: string
    :param networkMode: 

      The Docker networking mode to use for the containers in the task. The valid values are ``none`` , ``bridge`` , ``awsvpc`` , and ``host`` . The default Docker network mode is ``bridge`` . If using the Fargate launch type, the ``awsvpc`` network mode is required. If using the EC2 launch type, any network mode can be used. If the network mode is set to ``none`` , you can't specify port mappings in your container definitions, and the task's containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.

       

      With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings. 

       

      If the network mode is ``awsvpc`` , the task is allocated an Elastic Network Interface, and you must specify a  NetworkConfiguration when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

       

      If the network mode is ``host`` , you can't run multiple instantiations of the same task on a single container instance when port mappings are used.

       

      Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode.

       

      For more information, see `Network settings <https://docs.docker.com/engine/reference/run/#network-settings>`__ in the *Docker run reference* .

      

    
    :type containerDefinitions: list
    :param containerDefinitions: **[REQUIRED]** 

      A list of container definitions in JSON format that describe the different containers that make up your task.

      

    
      - *(dict) --* 

        Container definitions are used in task definitions to describe the different containers that are launched as part of a task.

        

      
        - **name** *(string) --* 

          The name of a container. If you are linking multiple containers together in a task definition, the ``name`` of one container can be entered in the ``links`` of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to ``name`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--name`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . 

          

        
        - **image** *(string) --* 

          The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` *repository-url* /*image* :*tag* `` or `` *repository-url* /*image* @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

           
          * Images in Amazon ECR repositories can be specified by either using the full ``registry/repository:tag`` or ``registry/repository@digest`` . For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`` .  
           
          * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
           
          * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
           
          * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
           

          

        
        - **cpu** *(integer) --* 

          The number of ``cpu`` units reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level ``cpu`` value.

           

          .. note::

             

            You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the `Amazon EC2 Instances <http://aws.amazon.com/ec2/instance-types/>`__ detail page by 1,024.

             

           

          For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.

           

          Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.

           

          On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see `CPU share constraint <https://docs.docker.com/engine/reference/run/#cpu-share-constraint>`__ in the Docker documentation. The minimum valid CPU share value that the Linux kernel will allow is 2; however, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:

           

           
          * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to 2 CPU shares. 
           
          * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2. 
           

           

          On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.

          

        
        - **memory** *(integer) --* 

          The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          If your containers will be part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task ``memory`` value.

           

          For containers that will be part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of ``memory`` is used.

           

          The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 

          

        
        - **memoryReservation** *(integer) --* 

          The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit; however, your container can consume more memory when it needs to, up to either the hard limit specified with the ``memory`` parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to ``MemoryReservation`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--memory-reservation`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          You must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of ``memory`` is used.

           

          For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a ``memoryReservation`` of 128 MiB, and a ``memory`` hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.

          

        
        - **links** *(list) --* 

          The ``link`` parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to ``bridge`` . The ``name:internalName`` construct is analogous to ``name:alias`` in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to `https\://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>`__ . This parameter maps to ``Links`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--link`` option to ` ``docker run`` https://docs.docker.com/engine/reference/commandline/run/`__ .

           

          .. note::

             

            This parameter is not supported for Windows containers.

             

           

          .. warning::

             

            Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.

             

          

        
          - *(string) --* 

          
      
        - **portMappings** *(list) --* 

          The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.

           

          For task definitions that use the ``awsvpc`` network mode, you should only specify the ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .

           

          Port mappings on Windows use the ``NetNAT`` gateway address rather than ``localhost`` . There is no loopback for port mappings on Windows, so you cannot access a container's mapped port from the host itself. 

           

          This parameter maps to ``PortBindings`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--publish`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . If the network mode of a task definition is set to ``none`` , then you can't specify port mappings. If the network mode of a task definition is set to ``host`` , then host ports must either be undefined or they must match the container port in the port mapping.

           

          .. note::

             

            After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the **Network Bindings** section of a container description for a selected task in the Amazon ECS console, or the ``networkBindings`` section  DescribeTasks responses.

             

          

        
          - *(dict) --* 

            Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.

             

            If using containers in a task with the Fargate launch type, exposed ports should be specified using ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .

             

            After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

            

          
            - **containerPort** *(integer) --* 

              The port number on the container that is bound to the user-specified or automatically assigned host port.

               

              If using containers in a task with the Fargate launch type, exposed ports should be specified using ``containerPort`` .

               

              If using containers in a task with the EC2 launch type and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range (for more information, see ``hostPort`` ). Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.

              

            
            - **hostPort** *(integer) --* 

              The port number on the container instance to reserve for your container.

               

              If using containers in a task with the Fargate launch type, the ``hostPort`` can either be left blank or needs to be the same value as the ``containerPort`` .

               

              If using containers in a task with the EC2 launch type, you can specify a non-reserved host port for your container port mapping, or you can omit the ``hostPort`` (or set it to ``0`` ) while specifying a ``containerPort`` and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.

               

              The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under ``/proc/sys/net/ipv4/ip_local_port_range`` ; if this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. You should not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.

               

              .. note::

                 

                The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.

                 

               

              The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678 and 51679. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the ``remainingResources`` of  DescribeContainerInstances output, and a container instance may have up to 100 reserved ports at a time, including the default reserved ports (automatically assigned ports do not count toward the 100 reserved ports limit).

              

            
            - **protocol** *(string) --* 

              The protocol used for the port mapping. Valid values are ``tcp`` and ``udp`` . The default is ``tcp`` .

              

            
          
      
        - **essential** *(boolean) --* 

          If the ``essential`` parameter of a container is marked as ``true`` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the ``essential`` parameter of a container is marked as ``false`` , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.

           

          All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see `Application Architecture <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

          

        
        - **entryPoint** *(list) --* 

          .. warning::

             

            Early versions of the Amazon ECS container agent do not properly handle ``entryPoint`` parameters. If you have problems using ``entryPoint`` , update your container agent or enter your commands and arguments as ``command`` array items instead.

             

           

          The entry point that is passed to the container. This parameter maps to ``Entrypoint`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--entrypoint`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#entrypoint <https://docs.docker.com/engine/reference/builder/#entrypoint>`__ .

          

        
          - *(string) --* 

          
      
        - **command** *(list) --* 

          The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

          

        
          - *(string) --* 

          
      
        - **environment** *(list) --* 

          The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          .. warning::

             

            We do not recommend using plaintext environment variables for sensitive information, such as credential data.

             

          

        
          - *(dict) --* 

            A key and value pair object.

            

          
            - **name** *(string) --* 

              The name of the key value pair. For environment variables, this is the name of the environment variable.

              

            
            - **value** *(string) --* 

              The value of the key value pair. For environment variables, this is the value of the environment variable.

              

            
          
      
        - **mountPoints** *(list) --* 

          The mount points for data volumes in your container.

           

          This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.

          

        
          - *(dict) --* 

            Details on a volume mount point that is used in a container definition.

            

          
            - **sourceVolume** *(string) --* 

              The name of the volume to mount.

              

            
            - **containerPath** *(string) --* 

              The path on the container to mount the host volume at.

              

            
            - **readOnly** *(boolean) --* 

              If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .

              

            
          
      
        - **volumesFrom** *(list) --* 

          Data volumes to mount from another container. This parameter maps to ``VolumesFrom`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--volumes-from`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

          

        
          - *(dict) --* 

            Details on a data volume from another container in the same task definition.

            

          
            - **sourceContainer** *(string) --* 

              The name of another container within the same task definition to mount volumes from.

              

            
            - **readOnly** *(boolean) --* 

              If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .

              

            
          
      
        - **linuxParameters** *(dict) --* 

          Linux-specific modifications that are applied to the container, such as Linux  KernelCapabilities .

           

          .. note::

             

            This parameter is not supported for Windows containers or tasks using the Fargate launch type.

             

          

        
          - **capabilities** *(dict) --* 

            The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.

            

          
            - **add** *(list) --* 

              The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to ``CapAdd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cap-add`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

               

              Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  

              

            
              - *(string) --* 

              
          
            - **drop** *(list) --* 

              The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to ``CapDrop`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cap-drop`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

               

              Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  

              

            
              - *(string) --* 

              
          
          
          - **devices** *(list) --* 

            Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            

          
            - *(dict) --* 

              An object representing a container instance host device.

              

            
              - **hostPath** *(string) --* **[REQUIRED]** 

                The path for the device on the host container instance.

                

              
              - **containerPath** *(string) --* 

                The path inside the container at which to expose the host device.

                

              
              - **permissions** *(list) --* 

                The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

                

              
                - *(string) --* 

                
            
            
        
          - **initProcessEnabled** *(boolean) --* 

            Run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

            

          
        
        - **hostname** *(string) --* 

          The hostname to use for your container. This parameter maps to ``Hostname`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--hostname`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

          

        
        - **user** *(string) --* 

          The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          .. note::

             

            This parameter is not supported for Windows containers.

             

          

        
        - **workingDirectory** *(string) --* 

          The working directory in which to run commands inside the container. This parameter maps to ``WorkingDir`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--workdir`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

          

        
        - **disableNetworking** *(boolean) --* 

          When this parameter is true, networking is disabled within the container. This parameter maps to ``NetworkDisabled`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ .

           

          .. note::

             

            This parameter is not supported for Windows containers.

             

          

        
        - **privileged** *(boolean) --* 

          When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          .. note::

             

            This parameter is not supported for Windows containers or tasks using the Fargate launch type.

             

          

        
        - **readonlyRootFilesystem** *(boolean) --* 

          When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--read-only`` option to ``docker run`` .

           

          .. note::

             

            This parameter is not supported for Windows containers.

             

          

        
        - **dnsServers** *(list) --* 

          A list of DNS servers that are presented to the container. This parameter maps to ``Dns`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--dns`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          .. note::

             

            This parameter is not supported for Windows containers.

             

          

        
          - *(string) --* 

          
      
        - **dnsSearchDomains** *(list) --* 

          A list of DNS search domains that are presented to the container. This parameter maps to ``DnsSearch`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--dns-search`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          .. note::

             

            This parameter is not supported for Windows containers.

             

          

        
          - *(string) --* 

          
      
        - **extraHosts** *(list) --* 

          A list of hostnames and IP address mappings to append to the ``/etc/hosts`` file on the container. If using the Fargate launch type, this may be used to list non-Fargate hosts you want the container to talk to. This parameter maps to ``ExtraHosts`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--add-host`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          .. note::

             

            This parameter is not supported for Windows containers.

             

          

        
          - *(dict) --* 

            Hostnames and IP address entries that are added to the ``/etc/hosts`` file of a container via the ``extraHosts`` parameter of its  ContainerDefinition . 

            

          
            - **hostname** *(string) --* **[REQUIRED]** 

              The hostname to use in the ``/etc/hosts`` entry.

              

            
            - **ipAddress** *(string) --* **[REQUIRED]** 

              The IP address to use in the ``/etc/hosts`` entry.

              

            
          
      
        - **dockerSecurityOptions** *(list) --* 

          A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.

           

          This parameter maps to ``SecurityOpt`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--security-opt`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

           

          .. note::

             

            The Amazon ECS container agent running on a container instance must register with the ``ECS_SELINUX_CAPABLE=true`` or ``ECS_APPARMOR_CAPABLE=true`` environment variables before containers placed on that instance can use these security options. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

             

            This parameter is not supported for Windows containers.

             

          

        
          - *(string) --* 

          
      
        - **dockerLabels** *(dict) --* 

          A key/value map of labels to add to the container. This parameter maps to ``Labels`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--label`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
        - **ulimits** *(list) --* 

          A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

           

          .. note::

             

            This parameter is not supported for Windows containers.

             

          

        
          - *(dict) --* 

            The ``ulimit`` settings to pass to the container.

            

          
            - **name** *(string) --* **[REQUIRED]** 

              The ``type`` of the ``ulimit`` .

              

            
            - **softLimit** *(integer) --* **[REQUIRED]** 

              The soft limit for the ulimit type.

              

            
            - **hardLimit** *(integer) --* **[REQUIRED]** 

              The hard limit for the ulimit type.

              

            
          
      
        - **logConfiguration** *(dict) --* 

          The log configuration specification for the container.

           

          If using the Fargate launch type, the only supported value is ``awslogs`` .

           

          This parameter maps to ``LogConfig`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--log-driver`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . By default, containers use the same logging driver that the Docker daemon uses; however the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.docker.com/engine/admin/logging/overview/>`__ in the Docker documentation.

           

          .. note::

             

            Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.

             

           

          This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

           

          .. note::

             

            The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

             

          

        
          - **logDriver** *(string) --* **[REQUIRED]** 

            The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default. If using the Fargate launch type, the only supported value is ``awslogs`` . For more information about using the ``awslogs`` driver, see `Using the awslogs Log Driver <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

             

            .. note::

               

              If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is `available on GitHub <https://github.com/aws/amazon-ecs-agent>`__ and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.

               

             

            This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

            

          
          - **options** *(dict) --* 

            The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
      
  
    :type volumes: list
    :param volumes: 

      A list of volume definitions in JSON format that containers in your task may use.

      

    
      - *(dict) --* 

        A data volume used in a task definition.

        

      
        - **name** *(string) --* 

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

          

        
        - **host** *(dict) --* 

          The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume, but the data is not guaranteed to persist after the containers associated with it stop running.

           

          Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount ``C:\my\path:C:\my\path`` and ``D:\:D:\`` , but not ``D:\my\path:C:\my\path`` or ``D:\:C:\my\path`` .

          

        
          - **sourcePath** *(string) --* 

            The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

             

            If you are using the Fargate launch type, the ``sourcePath`` parameter is not supported.

            

          
        
      
  
    :type placementConstraints: list
    :param placementConstraints: 

      An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints per task (this limit includes constraints in the task definition and those specified at run time).

      

    
      - *(dict) --* 

        An object representing a constraint on task placement in the task definition.

         

        If you are using the Fargate launch type, task placement contraints are not supported.

         

        For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

        

      
        - **type** *(string) --* 

          The type of constraint. The ``DistinctInstance`` constraint ensures that each task in a particular group is running on a different container instance. The ``MemberOf`` constraint restricts selection to be from a group of valid candidates.

          

        
        - **expression** *(string) --* 

          A cluster query language expression to apply to the constraint. For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

          

        
      
  
    :type requiresCompatibilities: list
    :param requiresCompatibilities: 

      The launch type required by the task. If no value is specified, it defaults to ``EC2`` .

      

    
      - *(string) --* 

      
  
    :type cpu: string
    :param cpu: 

      The number of ``cpu`` units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:

       

       
      * 256 (.25 vCPU) - Available ``memory`` values: 512MB, 1GB, 2GB 
       
      * 512 (.5 vCPU) - Available ``memory`` values: 1GB, 2GB, 3GB, 4GB 
       
      * 1024 (1 vCPU) - Available ``memory`` values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 
       
      * 2048 (2 vCPU) - Available ``memory`` values: Between 4GB and 16GB in 1GB increments 
       
      * 4096 (4 vCPU) - Available ``memory`` values: Between 8GB and 30GB in 1GB increments 
       

      

    
    :type memory: string
    :param memory: 

      The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:

       

       
      * 512MB, 1GB, 2GB - Available ``cpu`` values: 256 (.25 vCPU) 
       
      * 1GB, 2GB, 3GB, 4GB - Available ``cpu`` values: 512 (.5 vCPU) 
       
      * 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available ``cpu`` values: 1024 (1 vCPU) 
       
      * Between 4GB and 16GB in 1GB increments - Available ``cpu`` values: 2048 (2 vCPU) 
       
      * Between 8GB and 30GB in 1GB increments - Available ``cpu`` values: 4096 (4 vCPU) 
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskDefinition': {
                'taskDefinitionArn': 'string',
                'containerDefinitions': [
                    {
                        'name': 'string',
                        'image': 'string',
                        'cpu': 123,
                        'memory': 123,
                        'memoryReservation': 123,
                        'links': [
                            'string',
                        ],
                        'portMappings': [
                            {
                                'containerPort': 123,
                                'hostPort': 123,
                                'protocol': 'tcp'|'udp'
                            },
                        ],
                        'essential': True|False,
                        'entryPoint': [
                            'string',
                        ],
                        'command': [
                            'string',
                        ],
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'mountPoints': [
                            {
                                'sourceVolume': 'string',
                                'containerPath': 'string',
                                'readOnly': True|False
                            },
                        ],
                        'volumesFrom': [
                            {
                                'sourceContainer': 'string',
                                'readOnly': True|False
                            },
                        ],
                        'linuxParameters': {
                            'capabilities': {
                                'add': [
                                    'string',
                                ],
                                'drop': [
                                    'string',
                                ]
                            },
                            'devices': [
                                {
                                    'hostPath': 'string',
                                    'containerPath': 'string',
                                    'permissions': [
                                        'read'|'write'|'mknod',
                                    ]
                                },
                            ],
                            'initProcessEnabled': True|False
                        },
                        'hostname': 'string',
                        'user': 'string',
                        'workingDirectory': 'string',
                        'disableNetworking': True|False,
                        'privileged': True|False,
                        'readonlyRootFilesystem': True|False,
                        'dnsServers': [
                            'string',
                        ],
                        'dnsSearchDomains': [
                            'string',
                        ],
                        'extraHosts': [
                            {
                                'hostname': 'string',
                                'ipAddress': 'string'
                            },
                        ],
                        'dockerSecurityOptions': [
                            'string',
                        ],
                        'dockerLabels': {
                            'string': 'string'
                        },
                        'ulimits': [
                            {
                                'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                                'softLimit': 123,
                                'hardLimit': 123
                            },
                        ],
                        'logConfiguration': {
                            'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                            'options': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'family': 'string',
                'taskRoleArn': 'string',
                'executionRoleArn': 'string',
                'networkMode': 'bridge'|'host'|'awsvpc'|'none',
                'revision': 123,
                'volumes': [
                    {
                        'name': 'string',
                        'host': {
                            'sourcePath': 'string'
                        }
                    },
                ],
                'status': 'ACTIVE'|'INACTIVE',
                'requiresAttributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'placementConstraints': [
                    {
                        'type': 'memberOf',
                        'expression': 'string'
                    },
                ],
                'compatibilities': [
                    'EC2'|'FARGATE',
                ],
                'requiresCompatibilities': [
                    'EC2'|'FARGATE',
                ],
                'cpu': 'string',
                'memory': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskDefinition** *(dict) --* 

          The full description of the registered task definition.

          
          

          - **taskDefinitionArn** *(string) --* 

            The full Amazon Resource Name (ARN) of the task definition.

            
          

          - **containerDefinitions** *(list) --* 

            A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see `Amazon ECS Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(dict) --* 

              Container definitions are used in task definitions to describe the different containers that are launched as part of a task.

              
              

              - **name** *(string) --* 

                The name of a container. If you are linking multiple containers together in a task definition, the ``name`` of one container can be entered in the ``links`` of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to ``name`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--name`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . 

                
              

              - **image** *(string) --* 

                The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` *repository-url* /*image* :*tag* `` or `` *repository-url* /*image* @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                 
                * Images in Amazon ECR repositories can be specified by either using the full ``registry/repository:tag`` or ``registry/repository@digest`` . For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`` .  
                 
                * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                 
                * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                 
                * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                 

                
              

              - **cpu** *(integer) --* 

                The number of ``cpu`` units reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level ``cpu`` value.

                 

                .. note::

                   

                  You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the `Amazon EC2 Instances <http://aws.amazon.com/ec2/instance-types/>`__ detail page by 1,024.

                   

                 

                For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.

                 

                Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.

                 

                On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see `CPU share constraint <https://docs.docker.com/engine/reference/run/#cpu-share-constraint>`__ in the Docker documentation. The minimum valid CPU share value that the Linux kernel will allow is 2; however, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:

                 

                 
                * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to 2 CPU shares. 
                 
                * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2. 
                 

                 

                On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.

                
              

              - **memory** *(integer) --* 

                The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                If your containers will be part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task ``memory`` value.

                 

                For containers that will be part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of ``memory`` is used.

                 

                The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 

                
              

              - **memoryReservation** *(integer) --* 

                The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit; however, your container can consume more memory when it needs to, up to either the hard limit specified with the ``memory`` parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to ``MemoryReservation`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--memory-reservation`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                You must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of ``memory`` is used.

                 

                For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a ``memoryReservation`` of 128 MiB, and a ``memory`` hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.

                
              

              - **links** *(list) --* 

                The ``link`` parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to ``bridge`` . The ``name:internalName`` construct is analogous to ``name:alias`` in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to `https\://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>`__ . This parameter maps to ``Links`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--link`` option to ` ``docker run`` https://docs.docker.com/engine/reference/commandline/run/`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                 

                .. warning::

                   

                  Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.

                   

                
                

                - *(string) --* 
            
              

              - **portMappings** *(list) --* 

                The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.

                 

                For task definitions that use the ``awsvpc`` network mode, you should only specify the ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .

                 

                Port mappings on Windows use the ``NetNAT`` gateway address rather than ``localhost`` . There is no loopback for port mappings on Windows, so you cannot access a container's mapped port from the host itself. 

                 

                This parameter maps to ``PortBindings`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--publish`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . If the network mode of a task definition is set to ``none`` , then you can't specify port mappings. If the network mode of a task definition is set to ``host`` , then host ports must either be undefined or they must match the container port in the port mapping.

                 

                .. note::

                   

                  After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the **Network Bindings** section of a container description for a selected task in the Amazon ECS console, or the ``networkBindings`` section  DescribeTasks responses.

                   

                
                

                - *(dict) --* 

                  Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.

                   

                  If using containers in a task with the Fargate launch type, exposed ports should be specified using ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .

                   

                  After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

                  
                  

                  - **containerPort** *(integer) --* 

                    The port number on the container that is bound to the user-specified or automatically assigned host port.

                     

                    If using containers in a task with the Fargate launch type, exposed ports should be specified using ``containerPort`` .

                     

                    If using containers in a task with the EC2 launch type and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range (for more information, see ``hostPort`` ). Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.

                    
                  

                  - **hostPort** *(integer) --* 

                    The port number on the container instance to reserve for your container.

                     

                    If using containers in a task with the Fargate launch type, the ``hostPort`` can either be left blank or needs to be the same value as the ``containerPort`` .

                     

                    If using containers in a task with the EC2 launch type, you can specify a non-reserved host port for your container port mapping, or you can omit the ``hostPort`` (or set it to ``0`` ) while specifying a ``containerPort`` and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.

                     

                    The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under ``/proc/sys/net/ipv4/ip_local_port_range`` ; if this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. You should not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.

                     

                    .. note::

                       

                      The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.

                       

                     

                    The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678 and 51679. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the ``remainingResources`` of  DescribeContainerInstances output, and a container instance may have up to 100 reserved ports at a time, including the default reserved ports (automatically assigned ports do not count toward the 100 reserved ports limit).

                    
                  

                  - **protocol** *(string) --* 

                    The protocol used for the port mapping. Valid values are ``tcp`` and ``udp`` . The default is ``tcp`` .

                    
              
            
              

              - **essential** *(boolean) --* 

                If the ``essential`` parameter of a container is marked as ``true`` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the ``essential`` parameter of a container is marked as ``false`` , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.

                 

                All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see `Application Architecture <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
              

              - **entryPoint** *(list) --* 

                .. warning::

                   

                  Early versions of the Amazon ECS container agent do not properly handle ``entryPoint`` parameters. If you have problems using ``entryPoint`` , update your container agent or enter your commands and arguments as ``command`` array items instead.

                   

                 

                The entry point that is passed to the container. This parameter maps to ``Entrypoint`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--entrypoint`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#entrypoint <https://docs.docker.com/engine/reference/builder/#entrypoint>`__ .

                
                

                - *(string) --* 
            
              

              - **command** *(list) --* 

                The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

                
                

                - *(string) --* 
            
              

              - **environment** *(list) --* 

                The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. warning::

                   

                  We do not recommend using plaintext environment variables for sensitive information, such as credential data.

                   

                
                

                - *(dict) --* 

                  A key and value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key value pair. For environment variables, this is the value of the environment variable.

                    
              
            
              

              - **mountPoints** *(list) --* 

                The mount points for data volumes in your container.

                 

                This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.

                
                

                - *(dict) --* 

                  Details on a volume mount point that is used in a container definition.

                  
                  

                  - **sourceVolume** *(string) --* 

                    The name of the volume to mount.

                    
                  

                  - **containerPath** *(string) --* 

                    The path on the container to mount the host volume at.

                    
                  

                  - **readOnly** *(boolean) --* 

                    If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .

                    
              
            
              

              - **volumesFrom** *(list) --* 

                Data volumes to mount from another container. This parameter maps to ``VolumesFrom`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--volumes-from`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
                

                - *(dict) --* 

                  Details on a data volume from another container in the same task definition.

                  
                  

                  - **sourceContainer** *(string) --* 

                    The name of another container within the same task definition to mount volumes from.

                    
                  

                  - **readOnly** *(boolean) --* 

                    If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .

                    
              
            
              

              - **linuxParameters** *(dict) --* 

                Linux-specific modifications that are applied to the container, such as Linux  KernelCapabilities .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.

                   

                
                

                - **capabilities** *(dict) --* 

                  The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.

                  
                  

                  - **add** *(list) --* 

                    The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to ``CapAdd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cap-add`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                     

                    Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  

                    
                    

                    - *(string) --* 
                
                  

                  - **drop** *(list) --* 

                    The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to ``CapDrop`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--cap-drop`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                     

                    Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  

                    
                    

                    - *(string) --* 
                
              
                

                - **devices** *(list) --* 

                  Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                  
                  

                  - *(dict) --* 

                    An object representing a container instance host device.

                    
                    

                    - **hostPath** *(string) --* 

                      The path for the device on the host container instance.

                      
                    

                    - **containerPath** *(string) --* 

                      The path inside the container at which to expose the host device.

                      
                    

                    - **permissions** *(list) --* 

                      The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

                      
                      

                      - *(string) --* 
                  
                
              
                

                - **initProcessEnabled** *(boolean) --* 

                  Run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
            
              

              - **hostname** *(string) --* 

                The hostname to use for your container. This parameter maps to ``Hostname`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--hostname`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
              

              - **user** *(string) --* 

                The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **workingDirectory** *(string) --* 

                The working directory in which to run commands inside the container. This parameter maps to ``WorkingDir`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--workdir`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
              

              - **disableNetworking** *(boolean) --* 

                When this parameter is true, networking is disabled within the container. This parameter maps to ``NetworkDisabled`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **privileged** *(boolean) --* 

                When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.

                   

                
              

              - **readonlyRootFilesystem** *(boolean) --* 

                When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--read-only`` option to ``docker run`` .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
              

              - **dnsServers** *(list) --* 

                A list of DNS servers that are presented to the container. This parameter maps to ``Dns`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--dns`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **dnsSearchDomains** *(list) --* 

                A list of DNS search domains that are presented to the container. This parameter maps to ``DnsSearch`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--dns-search`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **extraHosts** *(list) --* 

                A list of hostnames and IP address mappings to append to the ``/etc/hosts`` file on the container. If using the Fargate launch type, this may be used to list non-Fargate hosts you want the container to talk to. This parameter maps to ``ExtraHosts`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--add-host`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(dict) --* 

                  Hostnames and IP address entries that are added to the ``/etc/hosts`` file of a container via the ``extraHosts`` parameter of its  ContainerDefinition . 

                  
                  

                  - **hostname** *(string) --* 

                    The hostname to use in the ``/etc/hosts`` entry.

                    
                  

                  - **ipAddress** *(string) --* 

                    The IP address to use in the ``/etc/hosts`` entry.

                    
              
            
              

              - **dockerSecurityOptions** *(list) --* 

                A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.

                 

                This parameter maps to ``SecurityOpt`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--security-opt`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. note::

                   

                  The Amazon ECS container agent running on a container instance must register with the ``ECS_SELINUX_CAPABLE=true`` or ``ECS_APPARMOR_CAPABLE=true`` environment variables before containers placed on that instance can use these security options. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(string) --* 
            
              

              - **dockerLabels** *(dict) --* 

                A key/value map of labels to add to the container. This parameter maps to ``Labels`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--label`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **ulimits** *(list) --* 

                A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                 

                .. note::

                   

                  This parameter is not supported for Windows containers.

                   

                
                

                - *(dict) --* 

                  The ``ulimit`` settings to pass to the container.

                  
                  

                  - **name** *(string) --* 

                    The ``type`` of the ``ulimit`` .

                    
                  

                  - **softLimit** *(integer) --* 

                    The soft limit for the ulimit type.

                    
                  

                  - **hardLimit** *(integer) --* 

                    The hard limit for the ulimit type.

                    
              
            
              

              - **logConfiguration** *(dict) --* 

                The log configuration specification for the container.

                 

                If using the Fargate launch type, the only supported value is ``awslogs`` .

                 

                This parameter maps to ``LogConfig`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.27/>`__ and the ``--log-driver`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . By default, containers use the same logging driver that the Docker daemon uses; however the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.docker.com/engine/admin/logging/overview/>`__ in the Docker documentation.

                 

                .. note::

                   

                  Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.

                   

                 

                This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                 

                .. note::

                   

                  The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                
                

                - **logDriver** *(string) --* 

                  The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default. If using the Fargate launch type, the only supported value is ``awslogs`` . For more information about using the ``awslogs`` driver, see `Using the awslogs Log Driver <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                   

                  .. note::

                     

                    If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is `available on GitHub <https://github.com/aws/amazon-ecs-agent>`__ and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.

                     

                   

                  This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
                

                - **options** *(dict) --* 

                  The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``  

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
          
        
          

          - **family** *(string) --* 

            The family of your task definition, used as the definition name.

            
          

          - **taskRoleArn** *(string) --* 

            The ARN of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

             

            IAM roles for tasks on Windows require that the ``-EnableTaskIAMRole`` option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code in order to take advantage of the feature. For more information, see `Windows IAM Roles for Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **executionRoleArn** *(string) --* 

            The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

            
          

          - **networkMode** *(string) --* 

            The Docker networking mode to use for the containers in the task. The valid values are ``none`` , ``bridge`` , ``awsvpc`` , and ``host`` . The default Docker network mode is ``bridge`` . If using the Fargate launch type, the ``awsvpc`` network mode is required. If using the EC2 launch type, any network mode can be used. If the network mode is set to ``none`` , you can't specify port mappings in your container definitions, and the task's containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.

             

            With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings. 

             

            If the network mode is ``awsvpc`` , the task is allocated an Elastic Network Interface, and you must specify a  NetworkConfiguration when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

             

            .. note::

               

              Currently, only the Amazon ECS-optimized AMI, other Amazon Linux variants with the ``ecs-init`` package, or AWS Fargate infrastructure support the ``awsvpc`` network mode. 

               

             

            If the network mode is ``host`` , you can't run multiple instantiations of the same task on a single container instance when port mappings are used.

             

            Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. If you use the console to register a task definition with Windows containers, you must choose the ``<default>`` network mode object. 

             

            For more information, see `Network settings <https://docs.docker.com/engine/reference/run/#network-settings>`__ in the *Docker run reference* .

            
          

          - **revision** *(integer) --* 

            The revision of the task in a particular family. The revision is a version number of a task definition in a family. When you register a task definition for the first time, the revision is ``1`` ; each time you register a new revision of a task definition in the same family, the revision value always increases by one (even if you have deregistered previous revisions in this family).

            
          

          - **volumes** *(list) --* 

            The list of volumes in a task.

             

            If you are using the Fargate launch type, the ``host`` and ``sourcePath`` parameters are not supported.

             

            For more information about volume definition parameters and defaults, see `Amazon ECS Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(dict) --* 

              A data volume used in a task definition.

              
              

              - **name** *(string) --* 

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

                
              

              - **host** *(dict) --* 

                The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume, but the data is not guaranteed to persist after the containers associated with it stop running.

                 

                Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount ``C:\my\path:C:\my\path`` and ``D:\:D:\`` , but not ``D:\my\path:C:\my\path`` or ``D:\:C:\my\path`` .

                
                

                - **sourcePath** *(string) --* 

                  The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

                   

                  If you are using the Fargate launch type, the ``sourcePath`` parameter is not supported.

                  
            
          
        
          

          - **status** *(string) --* 

            The status of the task definition.

            
          

          - **requiresAttributes** *(list) --* 

            The container instance attributes required by your task. This field is not valid if using the Fargate launch type for your task.

            
            

            - *(dict) --* 

              An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **name** *(string) --* 

                The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

                
              

              - **value** *(string) --* 

                The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

                
              

              - **targetType** *(string) --* 

                The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

                
              

              - **targetId** *(string) --* 

                The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

                
          
        
          

          - **placementConstraints** *(list) --* 

            An array of placement constraint objects to use for tasks. This field is not valid if using the Fargate launch type for your task.

            
            

            - *(dict) --* 

              An object representing a constraint on task placement in the task definition.

               

              If you are using the Fargate launch type, task placement contraints are not supported.

               

              For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of constraint. The ``DistinctInstance`` constraint ensures that each task in a particular group is running on a different container instance. The ``MemberOf`` constraint restricts selection to be from a group of valid candidates.

                
              

              - **expression** *(string) --* 

                A cluster query language expression to apply to the constraint. For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
          
        
          

          - **compatibilities** *(list) --* 

            The launch type to use with your task. For more information, see `Amazon ECS Launch Types <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
            

            - *(string) --* 
        
          

          - **requiresCompatibilities** *(list) --* 

            The launch type the task is using.

            
            

            - *(string) --* 
        
          

          - **cpu** *(string) --* 

            The number of ``cpu`` units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:

             

             
            * 256 (.25 vCPU) - Available ``memory`` values: 512MB, 1GB, 2GB 
             
            * 512 (.5 vCPU) - Available ``memory`` values: 1GB, 2GB, 3GB, 4GB 
             
            * 1024 (1 vCPU) - Available ``memory`` values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 
             
            * 2048 (2 vCPU) - Available ``memory`` values: Between 4GB and 16GB in 1GB increments 
             
            * 4096 (4 vCPU) - Available ``memory`` values: Between 8GB and 30GB in 1GB increments 
             

            
          

          - **memory** *(string) --* 

            The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:

             

             
            * 512MB, 1GB, 2GB - Available ``cpu`` values: 256 (.25 vCPU) 
             
            * 1GB, 2GB, 3GB, 4GB - Available ``cpu`` values: 512 (.5 vCPU) 
             
            * 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available ``cpu`` values: 1024 (1 vCPU) 
             
            * Between 4GB and 16GB in 1GB increments - Available ``cpu`` values: 2048 (2 vCPU) 
             
            * Between 8GB and 30GB in 1GB increments - Available ``cpu`` values: 4096 (4 vCPU) 
             

            
      
    

    **Examples** 

    This example registers a task definition to the specified family.
    ::

      response = client.register_task_definition(
          containerDefinitions=[
              {
                  'name': 'sleep',
                  'command': [
                      'sleep',
                      '360',
                  ],
                  'cpu': 10,
                  'essential': True,
                  'image': 'busybox',
                  'memory': 10,
              },
          ],
          family='sleep360',
          taskRoleArn='',
          volumes=[
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'taskDefinition': {
              'containerDefinitions': [
                  {
                      'name': 'sleep',
                      'command': [
                          'sleep',
                          '360',
                      ],
                      'cpu': 10,
                      'environment': [
                      ],
                      'essential': True,
                      'image': 'busybox',
                      'memory': 10,
                      'mountPoints': [
                      ],
                      'portMappings': [
                      ],
                      'volumesFrom': [
                      ],
                  },
              ],
              'family': 'sleep360',
              'revision': 1,
              'taskDefinitionArn': 'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/sleep360:19',
              'volumes': [
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: run_task(**kwargs)

    

    Starts a new task using the specified task definition.

     

    You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see `Scheduling Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

     

    Alternatively, you can use  StartTask to use your own scheduler or place tasks manually on specific container instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/RunTask>`_    


    **Request Syntax** 
    ::

      response = client.run_task(
          cluster='string',
          taskDefinition='string',
          overrides={
              'containerOverrides': [
                  {
                      'name': 'string',
                      'command': [
                          'string',
                      ],
                      'environment': [
                          {
                              'name': 'string',
                              'value': 'string'
                          },
                      ],
                      'cpu': 123,
                      'memory': 123,
                      'memoryReservation': 123
                  },
              ],
              'taskRoleArn': 'string',
              'executionRoleArn': 'string'
          },
          count=123,
          startedBy='string',
          group='string',
          placementConstraints=[
              {
                  'type': 'distinctInstance'|'memberOf',
                  'expression': 'string'
              },
          ],
          placementStrategy=[
              {
                  'type': 'random'|'spread'|'binpack',
                  'field': 'string'
              },
          ],
          launchType='EC2'|'FARGATE',
          platformVersion='string',
          networkConfiguration={
              'awsvpcConfiguration': {
                  'subnets': [
                      'string',
                  ],
                  'securityGroups': [
                      'string',
                  ],
                  'assignPublicIp': 'ENABLED'|'DISABLED'
              }
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster on which to run your task. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type taskDefinition: string
    :param taskDefinition: **[REQUIRED]** 

      The ``family`` and ``revision`` (``family:revision`` ) or full ARN of the task definition to run. If a ``revision`` is not specified, the latest ``ACTIVE`` revision is used.

      

    
    :type overrides: dict
    :param overrides: 

      A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that is specified in the task definition or Docker image) with a ``command`` override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an ``environment`` override.

       

      .. note::

         

        A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.

         

      

    
      - **containerOverrides** *(list) --* 

        One or more container overrides sent to a task.

        

      
        - *(dict) --* 

          The overrides that should be sent to a container.

          

        
          - **name** *(string) --* 

            The name of the container that receives the override. This parameter is required if any override is specified.

            

          
          - **command** *(list) --* 

            The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

            

          
            - *(string) --* 

            
        
          - **environment** *(list) --* 

            The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

            

          
            - *(dict) --* 

              A key and value pair object.

              

            
              - **name** *(string) --* 

                The name of the key value pair. For environment variables, this is the name of the environment variable.

                

              
              - **value** *(string) --* 

                The value of the key value pair. For environment variables, this is the value of the environment variable.

                

              
            
        
          - **cpu** *(integer) --* 

            The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

            

          
          - **memory** *(integer) --* 

            The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

            

          
          - **memoryReservation** *(integer) --* 

            The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

            

          
        
    
      - **taskRoleArn** *(string) --* 

        The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

        

      
      - **executionRoleArn** *(string) --* 

        The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

        

      
    
    :type count: integer
    :param count: 

      The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks per call.

      

    
    :type startedBy: string
    :param startedBy: 

      An optional tag specified when a task is started. For example if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the ``startedBy`` parameter. You can then identify which tasks belong to that job by filtering the results of a  ListTasks call with the ``startedBy`` value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

       

      If a task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.

      

    
    :type group: string
    :param group: 

      The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).

      

    
    :type placementConstraints: list
    :param placementConstraints: 

      An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at run time).

      

    
      - *(dict) --* 

        An object representing a constraint on task placement. For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

        

      
        - **type** *(string) --* 

          The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.

          

        
        - **expression** *(string) --* 

          A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

          

        
      
  
    :type placementStrategy: list
    :param placementStrategy: 

      The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task.

      

    
      - *(dict) --* 

        The task placement strategy for a task or service. For more information, see `Task Placement Strategies <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

        

      
        - **type** *(string) --* 

          The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

          

        
        - **field** *(string) --* 

          The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.

          

        
      
  
    :type launchType: string
    :param launchType: 

      The launch type on which to run your task.

      

    
    :type platformVersion: string
    :param platformVersion: 

      The platform version on which to run your task. If one is not specified, the latest version is used by default.

      

    
    :type networkConfiguration: dict
    :param networkConfiguration: 

      The network configuration for the task. This parameter is required for task definitions that use the ``awsvpc`` network mode to receive their own Elastic Network Interface, and it is not supported for other network modes. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

      

    
      - **awsvpcConfiguration** *(dict) --* 

        The VPC subnets and security groups associated with a task.

        

      
        - **subnets** *(list) --* **[REQUIRED]** 

          The subnets associated with the task or service.

          

        
          - *(string) --* 

          
      
        - **securityGroups** *(list) --* 

          The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

          

        
          - *(string) --* 

          
      
        - **assignPublicIp** *(string) --* 

          Specifies whether or not the task's elastic network interface receives a public IP address.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tasks': [
                {
                    'taskArn': 'string',
                    'clusterArn': 'string',
                    'taskDefinitionArn': 'string',
                    'containerInstanceArn': 'string',
                    'overrides': {
                        'containerOverrides': [
                            {
                                'name': 'string',
                                'command': [
                                    'string',
                                ],
                                'environment': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'cpu': 123,
                                'memory': 123,
                                'memoryReservation': 123
                            },
                        ],
                        'taskRoleArn': 'string',
                        'executionRoleArn': 'string'
                    },
                    'lastStatus': 'string',
                    'desiredStatus': 'string',
                    'cpu': 'string',
                    'memory': 'string',
                    'containers': [
                        {
                            'containerArn': 'string',
                            'taskArn': 'string',
                            'name': 'string',
                            'lastStatus': 'string',
                            'exitCode': 123,
                            'reason': 'string',
                            'networkBindings': [
                                {
                                    'bindIP': 'string',
                                    'containerPort': 123,
                                    'hostPort': 123,
                                    'protocol': 'tcp'|'udp'
                                },
                            ],
                            'networkInterfaces': [
                                {
                                    'attachmentId': 'string',
                                    'privateIpv4Address': 'string',
                                    'ipv6Address': 'string'
                                },
                            ]
                        },
                    ],
                    'startedBy': 'string',
                    'version': 123,
                    'stoppedReason': 'string',
                    'connectivity': 'CONNECTED'|'DISCONNECTED',
                    'connectivityAt': datetime(2015, 1, 1),
                    'pullStartedAt': datetime(2015, 1, 1),
                    'pullStoppedAt': datetime(2015, 1, 1),
                    'executionStoppedAt': datetime(2015, 1, 1),
                    'createdAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'stoppingAt': datetime(2015, 1, 1),
                    'stoppedAt': datetime(2015, 1, 1),
                    'group': 'string',
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                },
            ],
            'failures': [
                {
                    'arn': 'string',
                    'reason': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tasks** *(list) --* 

          A full description of the tasks that were run. The tasks that were successfully placed on your cluster are described here.

          
          

          - *(dict) --* 

            Details on a task in a cluster.

            
            

            - **taskArn** *(string) --* 

              The Amazon Resource Name (ARN) of the task.

              
            

            - **clusterArn** *(string) --* 

              The ARN of the cluster that hosts the task.

              
            

            - **taskDefinitionArn** *(string) --* 

              The ARN of the task definition that creates the task.

              
            

            - **containerInstanceArn** *(string) --* 

              The ARN of the container instances that host the task.

              
            

            - **overrides** *(dict) --* 

              One or more container overrides.

              
              

              - **containerOverrides** *(list) --* 

                One or more container overrides sent to a task.

                
                

                - *(dict) --* 

                  The overrides that should be sent to a container.

                  
                  

                  - **name** *(string) --* 

                    The name of the container that receives the override. This parameter is required if any override is specified.

                    
                  

                  - **command** *(list) --* 

                    The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

                    
                    

                    - *(string) --* 
                
                  

                  - **environment** *(list) --* 

                    The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

                    
                    

                    - *(dict) --* 

                      A key and value pair object.

                      
                      

                      - **name** *(string) --* 

                        The name of the key value pair. For environment variables, this is the name of the environment variable.

                        
                      

                      - **value** *(string) --* 

                        The value of the key value pair. For environment variables, this is the value of the environment variable.

                        
                  
                
                  

                  - **cpu** *(integer) --* 

                    The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

                    
                  

                  - **memory** *(integer) --* 

                    The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

                    
                  

                  - **memoryReservation** *(integer) --* 

                    The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

                    
              
            
              

              - **taskRoleArn** *(string) --* 

                The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

                
              

              - **executionRoleArn** *(string) --* 

                The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

                
          
            

            - **lastStatus** *(string) --* 

              The last known status of the task.

              
            

            - **desiredStatus** *(string) --* 

              The desired status of the task.

              
            

            - **cpu** *(string) --* 

              The number of ``cpu`` units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:

               

               
              * 256 (.25 vCPU) - Available ``memory`` values: 512MB, 1GB, 2GB 
               
              * 512 (.5 vCPU) - Available ``memory`` values: 1GB, 2GB, 3GB, 4GB 
               
              * 1024 (1 vCPU) - Available ``memory`` values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 
               
              * 2048 (2 vCPU) - Available ``memory`` values: Between 4GB and 16GB in 1GB increments 
               
              * 4096 (4 vCPU) - Available ``memory`` values: Between 8GB and 30GB in 1GB increments 
               

              
            

            - **memory** *(string) --* 

              The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:

               

               
              * 512MB, 1GB, 2GB - Available ``cpu`` values: 256 (.25 vCPU) 
               
              * 1GB, 2GB, 3GB, 4GB - Available ``cpu`` values: 512 (.5 vCPU) 
               
              * 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available ``cpu`` values: 1024 (1 vCPU) 
               
              * Between 4GB and 16GB in 1GB increments - Available ``cpu`` values: 2048 (2 vCPU) 
               
              * Between 8GB and 30GB in 1GB increments - Available ``cpu`` values: 4096 (4 vCPU) 
               

              
            

            - **containers** *(list) --* 

              The containers associated with the task.

              
              

              - *(dict) --* 

                A Docker container that is part of a task.

                
                

                - **containerArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the container.

                  
                

                - **taskArn** *(string) --* 

                  The ARN of the task.

                  
                

                - **name** *(string) --* 

                  The name of the container.

                  
                

                - **lastStatus** *(string) --* 

                  The last known status of the container.

                  
                

                - **exitCode** *(integer) --* 

                  The exit code returned from the container.

                  
                

                - **reason** *(string) --* 

                  A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

                  
                

                - **networkBindings** *(list) --* 

                  The network bindings associated with the container.

                  
                  

                  - *(dict) --* 

                    Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

                    
                    

                    - **bindIP** *(string) --* 

                      The IP address that the container is bound to on the container instance.

                      
                    

                    - **containerPort** *(integer) --* 

                      The port number on the container that is used with the network binding.

                      
                    

                    - **hostPort** *(integer) --* 

                      The port number on the host that is used with the network binding.

                      
                    

                    - **protocol** *(string) --* 

                      The protocol used for the network binding.

                      
                
              
                

                - **networkInterfaces** *(list) --* 

                  The network interfaces associated with the container.

                  
                  

                  - *(dict) --* 

                    An object representing the Elastic Network Interface for tasks that use the ``awsvpc`` network mode.

                    
                    

                    - **attachmentId** *(string) --* 

                      The attachment ID for the network interface.

                      
                    

                    - **privateIpv4Address** *(string) --* 

                      The private IPv4 address for the network interface.

                      
                    

                    - **ipv6Address** *(string) --* 

                      The private IPv6 address for the network interface.

                      
                
              
            
          
            

            - **startedBy** *(string) --* 

              The tag specified when a task is started. If the task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.

              
            

            - **version** *(integer) --* 

              The version counter for the task. Every time a task experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the task (inside the ``detail`` object) to verify that the version in your event stream is current.

              
            

            - **stoppedReason** *(string) --* 

              The reason the task was stopped.

              
            

            - **connectivity** *(string) --* 

              The connectivity status of a task.

              
            

            - **connectivityAt** *(datetime) --* 

              The Unix time stamp for when the task last went into ``CONNECTED`` status.

              
            

            - **pullStartedAt** *(datetime) --* 

              The Unix time stamp for when the container image pull began.

              
            

            - **pullStoppedAt** *(datetime) --* 

              The Unix time stamp for when the container image pull completed.

              
            

            - **executionStoppedAt** *(datetime) --* 

              The Unix timestamp for when the task execution stopped.

              
            

            - **createdAt** *(datetime) --* 

              The Unix time stamp for when the task was created (the task entered the ``PENDING`` state).

              
            

            - **startedAt** *(datetime) --* 

              The Unix time stamp for when the task started (the task transitioned from the ``PENDING`` state to the ``RUNNING`` state).

              
            

            - **stoppingAt** *(datetime) --* 

              The Unix time stamp for when the task will stop (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).

              
            

            - **stoppedAt** *(datetime) --* 

              The Unix time stamp for when the task was stopped (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).

              
            

            - **group** *(string) --* 

              The name of the task group associated with the task.

              
            

            - **launchType** *(string) --* 

              The launch type on which your task is running.

              
            

            - **platformVersion** *(string) --* 

              The platform version on which your task is running. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
            

            - **attachments** *(list) --* 

              The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network mode.

              
              

              - *(dict) --* 

                An object representing a container instance or task attachment.

                
                

                - **id** *(string) --* 

                  The unique identifier for the attachment.

                  
                

                - **type** *(string) --* 

                  The type of the attachment, such as an ``ElasticNetworkInterface`` .

                  
                

                - **status** *(string) --* 

                  The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                  
                

                - **details** *(list) --* 

                  Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                  
                  

                  - *(dict) --* 

                    A key and value pair object.

                    
                    

                    - **name** *(string) --* 

                      The name of the key value pair. For environment variables, this is the name of the environment variable.

                      
                    

                    - **value** *(string) --* 

                      The value of the key value pair. For environment variables, this is the value of the environment variable.

                      
                
              
            
          
        
      
        

        - **failures** *(list) --* 

          Any failures associated with the call.

          
          

          - *(dict) --* 

            A failed resource.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the failed resource.

              
            

            - **reason** *(string) --* 

              The reason for the failure.

              
        
      
    

    **Examples** 

    This example runs the specified task definition on your default cluster.
    ::

      response = client.run_task(
          cluster='default',
          taskDefinition='sleep360:1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'tasks': [
              {
                  'containerInstanceArn': 'arn:aws:ecs:us-east-1:<aws_account_id>:container-instance/ffe3d344-77e2-476c-a4d0-bf560ad50acb',
                  'containers': [
                      {
                          'name': 'sleep',
                          'containerArn': 'arn:aws:ecs:us-east-1:<aws_account_id>:container/58591c8e-be29-4ddf-95aa-ee459d4c59fd',
                          'lastStatus': 'PENDING',
                          'taskArn': 'arn:aws:ecs:us-east-1:<aws_account_id>:task/a9f21ea7-c9f5-44b1-b8e6-b31f50ed33c0',
                      },
                  ],
                  'desiredStatus': 'RUNNING',
                  'lastStatus': 'PENDING',
                  'overrides': {
                      'containerOverrides': [
                          {
                              'name': 'sleep',
                          },
                      ],
                  },
                  'taskArn': 'arn:aws:ecs:us-east-1:<aws_account_id>:task/a9f21ea7-c9f5-44b1-b8e6-b31f50ed33c0',
                  'taskDefinitionArn': 'arn:aws:ecs:us-east-1:<aws_account_id>:task-definition/sleep360:1',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: start_task(**kwargs)

    

    Starts a new task from the specified task definition on the specified container instance or instances.

     

    Alternatively, you can use  RunTask to place tasks for you. For more information, see `Scheduling Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/StartTask>`_    


    **Request Syntax** 
    ::

      response = client.start_task(
          cluster='string',
          taskDefinition='string',
          overrides={
              'containerOverrides': [
                  {
                      'name': 'string',
                      'command': [
                          'string',
                      ],
                      'environment': [
                          {
                              'name': 'string',
                              'value': 'string'
                          },
                      ],
                      'cpu': 123,
                      'memory': 123,
                      'memoryReservation': 123
                  },
              ],
              'taskRoleArn': 'string',
              'executionRoleArn': 'string'
          },
          containerInstances=[
              'string',
          ],
          startedBy='string',
          group='string',
          networkConfiguration={
              'awsvpcConfiguration': {
                  'subnets': [
                      'string',
                  ],
                  'securityGroups': [
                      'string',
                  ],
                  'assignPublicIp': 'ENABLED'|'DISABLED'
              }
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster on which to start your task. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type taskDefinition: string
    :param taskDefinition: **[REQUIRED]** 

      The ``family`` and ``revision`` (``family:revision`` ) or full ARN of the task definition to start. If a ``revision`` is not specified, the latest ``ACTIVE`` revision is used.

      

    
    :type overrides: dict
    :param overrides: 

      A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that is specified in the task definition or Docker image) with a ``command`` override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an ``environment`` override.

       

      .. note::

         

        A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.

         

      

    
      - **containerOverrides** *(list) --* 

        One or more container overrides sent to a task.

        

      
        - *(dict) --* 

          The overrides that should be sent to a container.

          

        
          - **name** *(string) --* 

            The name of the container that receives the override. This parameter is required if any override is specified.

            

          
          - **command** *(list) --* 

            The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

            

          
            - *(string) --* 

            
        
          - **environment** *(list) --* 

            The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

            

          
            - *(dict) --* 

              A key and value pair object.

              

            
              - **name** *(string) --* 

                The name of the key value pair. For environment variables, this is the name of the environment variable.

                

              
              - **value** *(string) --* 

                The value of the key value pair. For environment variables, this is the value of the environment variable.

                

              
            
        
          - **cpu** *(integer) --* 

            The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

            

          
          - **memory** *(integer) --* 

            The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

            

          
          - **memoryReservation** *(integer) --* 

            The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

            

          
        
    
      - **taskRoleArn** *(string) --* 

        The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

        

      
      - **executionRoleArn** *(string) --* 

        The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

        

      
    
    :type containerInstances: list
    :param containerInstances: **[REQUIRED]** 

      The container instance IDs or full ARN entries for the container instances on which you would like to place your task. You can specify up to 10 container instances.

      

    
      - *(string) --* 

      
  
    :type startedBy: string
    :param startedBy: 

      An optional tag specified when a task is started. For example if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the ``startedBy`` parameter. You can then identify which tasks belong to that job by filtering the results of a  ListTasks call with the ``startedBy`` value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

       

      If a task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.

      

    
    :type group: string
    :param group: 

      The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).

      

    
    :type networkConfiguration: dict
    :param networkConfiguration: 

      The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

      

    
      - **awsvpcConfiguration** *(dict) --* 

        The VPC subnets and security groups associated with a task.

        

      
        - **subnets** *(list) --* **[REQUIRED]** 

          The subnets associated with the task or service.

          

        
          - *(string) --* 

          
      
        - **securityGroups** *(list) --* 

          The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

          

        
          - *(string) --* 

          
      
        - **assignPublicIp** *(string) --* 

          Specifies whether or not the task's elastic network interface receives a public IP address.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tasks': [
                {
                    'taskArn': 'string',
                    'clusterArn': 'string',
                    'taskDefinitionArn': 'string',
                    'containerInstanceArn': 'string',
                    'overrides': {
                        'containerOverrides': [
                            {
                                'name': 'string',
                                'command': [
                                    'string',
                                ],
                                'environment': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'cpu': 123,
                                'memory': 123,
                                'memoryReservation': 123
                            },
                        ],
                        'taskRoleArn': 'string',
                        'executionRoleArn': 'string'
                    },
                    'lastStatus': 'string',
                    'desiredStatus': 'string',
                    'cpu': 'string',
                    'memory': 'string',
                    'containers': [
                        {
                            'containerArn': 'string',
                            'taskArn': 'string',
                            'name': 'string',
                            'lastStatus': 'string',
                            'exitCode': 123,
                            'reason': 'string',
                            'networkBindings': [
                                {
                                    'bindIP': 'string',
                                    'containerPort': 123,
                                    'hostPort': 123,
                                    'protocol': 'tcp'|'udp'
                                },
                            ],
                            'networkInterfaces': [
                                {
                                    'attachmentId': 'string',
                                    'privateIpv4Address': 'string',
                                    'ipv6Address': 'string'
                                },
                            ]
                        },
                    ],
                    'startedBy': 'string',
                    'version': 123,
                    'stoppedReason': 'string',
                    'connectivity': 'CONNECTED'|'DISCONNECTED',
                    'connectivityAt': datetime(2015, 1, 1),
                    'pullStartedAt': datetime(2015, 1, 1),
                    'pullStoppedAt': datetime(2015, 1, 1),
                    'executionStoppedAt': datetime(2015, 1, 1),
                    'createdAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'stoppingAt': datetime(2015, 1, 1),
                    'stoppedAt': datetime(2015, 1, 1),
                    'group': 'string',
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                },
            ],
            'failures': [
                {
                    'arn': 'string',
                    'reason': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tasks** *(list) --* 

          A full description of the tasks that were started. Each task that was successfully placed on your container instances is described.

          
          

          - *(dict) --* 

            Details on a task in a cluster.

            
            

            - **taskArn** *(string) --* 

              The Amazon Resource Name (ARN) of the task.

              
            

            - **clusterArn** *(string) --* 

              The ARN of the cluster that hosts the task.

              
            

            - **taskDefinitionArn** *(string) --* 

              The ARN of the task definition that creates the task.

              
            

            - **containerInstanceArn** *(string) --* 

              The ARN of the container instances that host the task.

              
            

            - **overrides** *(dict) --* 

              One or more container overrides.

              
              

              - **containerOverrides** *(list) --* 

                One or more container overrides sent to a task.

                
                

                - *(dict) --* 

                  The overrides that should be sent to a container.

                  
                  

                  - **name** *(string) --* 

                    The name of the container that receives the override. This parameter is required if any override is specified.

                    
                  

                  - **command** *(list) --* 

                    The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

                    
                    

                    - *(string) --* 
                
                  

                  - **environment** *(list) --* 

                    The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

                    
                    

                    - *(dict) --* 

                      A key and value pair object.

                      
                      

                      - **name** *(string) --* 

                        The name of the key value pair. For environment variables, this is the name of the environment variable.

                        
                      

                      - **value** *(string) --* 

                        The value of the key value pair. For environment variables, this is the value of the environment variable.

                        
                  
                
                  

                  - **cpu** *(integer) --* 

                    The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

                    
                  

                  - **memory** *(integer) --* 

                    The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

                    
                  

                  - **memoryReservation** *(integer) --* 

                    The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

                    
              
            
              

              - **taskRoleArn** *(string) --* 

                The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

                
              

              - **executionRoleArn** *(string) --* 

                The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

                
          
            

            - **lastStatus** *(string) --* 

              The last known status of the task.

              
            

            - **desiredStatus** *(string) --* 

              The desired status of the task.

              
            

            - **cpu** *(string) --* 

              The number of ``cpu`` units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:

               

               
              * 256 (.25 vCPU) - Available ``memory`` values: 512MB, 1GB, 2GB 
               
              * 512 (.5 vCPU) - Available ``memory`` values: 1GB, 2GB, 3GB, 4GB 
               
              * 1024 (1 vCPU) - Available ``memory`` values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 
               
              * 2048 (2 vCPU) - Available ``memory`` values: Between 4GB and 16GB in 1GB increments 
               
              * 4096 (4 vCPU) - Available ``memory`` values: Between 8GB and 30GB in 1GB increments 
               

              
            

            - **memory** *(string) --* 

              The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:

               

               
              * 512MB, 1GB, 2GB - Available ``cpu`` values: 256 (.25 vCPU) 
               
              * 1GB, 2GB, 3GB, 4GB - Available ``cpu`` values: 512 (.5 vCPU) 
               
              * 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available ``cpu`` values: 1024 (1 vCPU) 
               
              * Between 4GB and 16GB in 1GB increments - Available ``cpu`` values: 2048 (2 vCPU) 
               
              * Between 8GB and 30GB in 1GB increments - Available ``cpu`` values: 4096 (4 vCPU) 
               

              
            

            - **containers** *(list) --* 

              The containers associated with the task.

              
              

              - *(dict) --* 

                A Docker container that is part of a task.

                
                

                - **containerArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the container.

                  
                

                - **taskArn** *(string) --* 

                  The ARN of the task.

                  
                

                - **name** *(string) --* 

                  The name of the container.

                  
                

                - **lastStatus** *(string) --* 

                  The last known status of the container.

                  
                

                - **exitCode** *(integer) --* 

                  The exit code returned from the container.

                  
                

                - **reason** *(string) --* 

                  A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

                  
                

                - **networkBindings** *(list) --* 

                  The network bindings associated with the container.

                  
                  

                  - *(dict) --* 

                    Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

                    
                    

                    - **bindIP** *(string) --* 

                      The IP address that the container is bound to on the container instance.

                      
                    

                    - **containerPort** *(integer) --* 

                      The port number on the container that is used with the network binding.

                      
                    

                    - **hostPort** *(integer) --* 

                      The port number on the host that is used with the network binding.

                      
                    

                    - **protocol** *(string) --* 

                      The protocol used for the network binding.

                      
                
              
                

                - **networkInterfaces** *(list) --* 

                  The network interfaces associated with the container.

                  
                  

                  - *(dict) --* 

                    An object representing the Elastic Network Interface for tasks that use the ``awsvpc`` network mode.

                    
                    

                    - **attachmentId** *(string) --* 

                      The attachment ID for the network interface.

                      
                    

                    - **privateIpv4Address** *(string) --* 

                      The private IPv4 address for the network interface.

                      
                    

                    - **ipv6Address** *(string) --* 

                      The private IPv6 address for the network interface.

                      
                
              
            
          
            

            - **startedBy** *(string) --* 

              The tag specified when a task is started. If the task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.

              
            

            - **version** *(integer) --* 

              The version counter for the task. Every time a task experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the task (inside the ``detail`` object) to verify that the version in your event stream is current.

              
            

            - **stoppedReason** *(string) --* 

              The reason the task was stopped.

              
            

            - **connectivity** *(string) --* 

              The connectivity status of a task.

              
            

            - **connectivityAt** *(datetime) --* 

              The Unix time stamp for when the task last went into ``CONNECTED`` status.

              
            

            - **pullStartedAt** *(datetime) --* 

              The Unix time stamp for when the container image pull began.

              
            

            - **pullStoppedAt** *(datetime) --* 

              The Unix time stamp for when the container image pull completed.

              
            

            - **executionStoppedAt** *(datetime) --* 

              The Unix timestamp for when the task execution stopped.

              
            

            - **createdAt** *(datetime) --* 

              The Unix time stamp for when the task was created (the task entered the ``PENDING`` state).

              
            

            - **startedAt** *(datetime) --* 

              The Unix time stamp for when the task started (the task transitioned from the ``PENDING`` state to the ``RUNNING`` state).

              
            

            - **stoppingAt** *(datetime) --* 

              The Unix time stamp for when the task will stop (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).

              
            

            - **stoppedAt** *(datetime) --* 

              The Unix time stamp for when the task was stopped (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).

              
            

            - **group** *(string) --* 

              The name of the task group associated with the task.

              
            

            - **launchType** *(string) --* 

              The launch type on which your task is running.

              
            

            - **platformVersion** *(string) --* 

              The platform version on which your task is running. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
            

            - **attachments** *(list) --* 

              The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network mode.

              
              

              - *(dict) --* 

                An object representing a container instance or task attachment.

                
                

                - **id** *(string) --* 

                  The unique identifier for the attachment.

                  
                

                - **type** *(string) --* 

                  The type of the attachment, such as an ``ElasticNetworkInterface`` .

                  
                

                - **status** *(string) --* 

                  The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                  
                

                - **details** *(list) --* 

                  Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                  
                  

                  - *(dict) --* 

                    A key and value pair object.

                    
                    

                    - **name** *(string) --* 

                      The name of the key value pair. For environment variables, this is the name of the environment variable.

                      
                    

                    - **value** *(string) --* 

                      The value of the key value pair. For environment variables, this is the value of the environment variable.

                      
                
              
            
          
        
      
        

        - **failures** *(list) --* 

          Any failures associated with the call.

          
          

          - *(dict) --* 

            A failed resource.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the failed resource.

              
            

            - **reason** *(string) --* 

              The reason for the failure.

              
        
      
    

  .. py:method:: stop_task(**kwargs)

    

    Stops a running task.

     

    When  StopTask is called on a task, the equivalent of ``docker stop`` is issued to the containers running in the task. This results in a ``SIGTERM`` and a default 30-second timeout, after which ``SIGKILL`` is sent and the containers are forcibly stopped. If the container handles the ``SIGTERM`` gracefully and exits within 30 seconds from receiving it, no ``SIGKILL`` is sent.

     

    .. note::

       

      The default 30-second timeout can be configured on the Amazon ECS container agent with the ``ECS_CONTAINER_STOP_TIMEOUT`` variable. For more information, see `Amazon ECS Container Agent Configuration <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/StopTask>`_    


    **Request Syntax** 
    ::

      response = client.stop_task(
          cluster='string',
          task='string',
          reason='string'
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type task: string
    :param task: **[REQUIRED]** 

      The task ID or full ARN entry of the task to stop.

      

    
    :type reason: string
    :param reason: 

      An optional message specified when a task is stopped. For example, if you are using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent  DescribeTasks API operations on this task. Up to 255 characters are allowed in this message.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'task': {
                'taskArn': 'string',
                'clusterArn': 'string',
                'taskDefinitionArn': 'string',
                'containerInstanceArn': 'string',
                'overrides': {
                    'containerOverrides': [
                        {
                            'name': 'string',
                            'command': [
                                'string',
                            ],
                            'environment': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ],
                            'cpu': 123,
                            'memory': 123,
                            'memoryReservation': 123
                        },
                    ],
                    'taskRoleArn': 'string',
                    'executionRoleArn': 'string'
                },
                'lastStatus': 'string',
                'desiredStatus': 'string',
                'cpu': 'string',
                'memory': 'string',
                'containers': [
                    {
                        'containerArn': 'string',
                        'taskArn': 'string',
                        'name': 'string',
                        'lastStatus': 'string',
                        'exitCode': 123,
                        'reason': 'string',
                        'networkBindings': [
                            {
                                'bindIP': 'string',
                                'containerPort': 123,
                                'hostPort': 123,
                                'protocol': 'tcp'|'udp'
                            },
                        ],
                        'networkInterfaces': [
                            {
                                'attachmentId': 'string',
                                'privateIpv4Address': 'string',
                                'ipv6Address': 'string'
                            },
                        ]
                    },
                ],
                'startedBy': 'string',
                'version': 123,
                'stoppedReason': 'string',
                'connectivity': 'CONNECTED'|'DISCONNECTED',
                'connectivityAt': datetime(2015, 1, 1),
                'pullStartedAt': datetime(2015, 1, 1),
                'pullStoppedAt': datetime(2015, 1, 1),
                'executionStoppedAt': datetime(2015, 1, 1),
                'createdAt': datetime(2015, 1, 1),
                'startedAt': datetime(2015, 1, 1),
                'stoppingAt': datetime(2015, 1, 1),
                'stoppedAt': datetime(2015, 1, 1),
                'group': 'string',
                'launchType': 'EC2'|'FARGATE',
                'platformVersion': 'string',
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **task** *(dict) --* 

          The task that was stopped.

          
          

          - **taskArn** *(string) --* 

            The Amazon Resource Name (ARN) of the task.

            
          

          - **clusterArn** *(string) --* 

            The ARN of the cluster that hosts the task.

            
          

          - **taskDefinitionArn** *(string) --* 

            The ARN of the task definition that creates the task.

            
          

          - **containerInstanceArn** *(string) --* 

            The ARN of the container instances that host the task.

            
          

          - **overrides** *(dict) --* 

            One or more container overrides.

            
            

            - **containerOverrides** *(list) --* 

              One or more container overrides sent to a task.

              
              

              - *(dict) --* 

                The overrides that should be sent to a container.

                
                

                - **name** *(string) --* 

                  The name of the container that receives the override. This parameter is required if any override is specified.

                  
                

                - **command** *(list) --* 

                  The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

                  
                  

                  - *(string) --* 
              
                

                - **environment** *(list) --* 

                  The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

                  
                  

                  - *(dict) --* 

                    A key and value pair object.

                    
                    

                    - **name** *(string) --* 

                      The name of the key value pair. For environment variables, this is the name of the environment variable.

                      
                    

                    - **value** *(string) --* 

                      The value of the key value pair. For environment variables, this is the value of the environment variable.

                      
                
              
                

                - **cpu** *(integer) --* 

                  The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

                  
                

                - **memory** *(integer) --* 

                  The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

                  
                

                - **memoryReservation** *(integer) --* 

                  The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

                  
            
          
            

            - **taskRoleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.

              
            

            - **executionRoleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

              
        
          

          - **lastStatus** *(string) --* 

            The last known status of the task.

            
          

          - **desiredStatus** *(string) --* 

            The desired status of the task.

            
          

          - **cpu** *(string) --* 

            The number of ``cpu`` units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:

             

             
            * 256 (.25 vCPU) - Available ``memory`` values: 512MB, 1GB, 2GB 
             
            * 512 (.5 vCPU) - Available ``memory`` values: 1GB, 2GB, 3GB, 4GB 
             
            * 1024 (1 vCPU) - Available ``memory`` values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 
             
            * 2048 (2 vCPU) - Available ``memory`` values: Between 4GB and 16GB in 1GB increments 
             
            * 4096 (4 vCPU) - Available ``memory`` values: Between 8GB and 30GB in 1GB increments 
             

            
          

          - **memory** *(string) --* 

            The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:

             

             
            * 512MB, 1GB, 2GB - Available ``cpu`` values: 256 (.25 vCPU) 
             
            * 1GB, 2GB, 3GB, 4GB - Available ``cpu`` values: 512 (.5 vCPU) 
             
            * 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available ``cpu`` values: 1024 (1 vCPU) 
             
            * Between 4GB and 16GB in 1GB increments - Available ``cpu`` values: 2048 (2 vCPU) 
             
            * Between 8GB and 30GB in 1GB increments - Available ``cpu`` values: 4096 (4 vCPU) 
             

            
          

          - **containers** *(list) --* 

            The containers associated with the task.

            
            

            - *(dict) --* 

              A Docker container that is part of a task.

              
              

              - **containerArn** *(string) --* 

                The Amazon Resource Name (ARN) of the container.

                
              

              - **taskArn** *(string) --* 

                The ARN of the task.

                
              

              - **name** *(string) --* 

                The name of the container.

                
              

              - **lastStatus** *(string) --* 

                The last known status of the container.

                
              

              - **exitCode** *(integer) --* 

                The exit code returned from the container.

                
              

              - **reason** *(string) --* 

                A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

                
              

              - **networkBindings** *(list) --* 

                The network bindings associated with the container.

                
                

                - *(dict) --* 

                  Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

                  
                  

                  - **bindIP** *(string) --* 

                    The IP address that the container is bound to on the container instance.

                    
                  

                  - **containerPort** *(integer) --* 

                    The port number on the container that is used with the network binding.

                    
                  

                  - **hostPort** *(integer) --* 

                    The port number on the host that is used with the network binding.

                    
                  

                  - **protocol** *(string) --* 

                    The protocol used for the network binding.

                    
              
            
              

              - **networkInterfaces** *(list) --* 

                The network interfaces associated with the container.

                
                

                - *(dict) --* 

                  An object representing the Elastic Network Interface for tasks that use the ``awsvpc`` network mode.

                  
                  

                  - **attachmentId** *(string) --* 

                    The attachment ID for the network interface.

                    
                  

                  - **privateIpv4Address** *(string) --* 

                    The private IPv4 address for the network interface.

                    
                  

                  - **ipv6Address** *(string) --* 

                    The private IPv6 address for the network interface.

                    
              
            
          
        
          

          - **startedBy** *(string) --* 

            The tag specified when a task is started. If the task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.

            
          

          - **version** *(integer) --* 

            The version counter for the task. Every time a task experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the task (inside the ``detail`` object) to verify that the version in your event stream is current.

            
          

          - **stoppedReason** *(string) --* 

            The reason the task was stopped.

            
          

          - **connectivity** *(string) --* 

            The connectivity status of a task.

            
          

          - **connectivityAt** *(datetime) --* 

            The Unix time stamp for when the task last went into ``CONNECTED`` status.

            
          

          - **pullStartedAt** *(datetime) --* 

            The Unix time stamp for when the container image pull began.

            
          

          - **pullStoppedAt** *(datetime) --* 

            The Unix time stamp for when the container image pull completed.

            
          

          - **executionStoppedAt** *(datetime) --* 

            The Unix timestamp for when the task execution stopped.

            
          

          - **createdAt** *(datetime) --* 

            The Unix time stamp for when the task was created (the task entered the ``PENDING`` state).

            
          

          - **startedAt** *(datetime) --* 

            The Unix time stamp for when the task started (the task transitioned from the ``PENDING`` state to the ``RUNNING`` state).

            
          

          - **stoppingAt** *(datetime) --* 

            The Unix time stamp for when the task will stop (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).

            
          

          - **stoppedAt** *(datetime) --* 

            The Unix time stamp for when the task was stopped (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).

            
          

          - **group** *(string) --* 

            The name of the task group associated with the task.

            
          

          - **launchType** *(string) --* 

            The launch type on which your task is running.

            
          

          - **platformVersion** *(string) --* 

            The platform version on which your task is running. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **attachments** *(list) --* 

            The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network mode.

            
            

            - *(dict) --* 

              An object representing a container instance or task attachment.

              
              

              - **id** *(string) --* 

                The unique identifier for the attachment.

                
              

              - **type** *(string) --* 

                The type of the attachment, such as an ``ElasticNetworkInterface`` .

                
              

              - **status** *(string) --* 

                The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                
              

              - **details** *(list) --* 

                Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                
                

                - *(dict) --* 

                  A key and value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key value pair. For environment variables, this is the value of the environment variable.

                    
              
            
          
        
      
    

  .. py:method:: submit_container_state_change(**kwargs)

    

    .. note::

       

      This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

       

     

    Sent to acknowledge that a container changed states.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/SubmitContainerStateChange>`_    


    **Request Syntax** 
    ::

      response = client.submit_container_state_change(
          cluster='string',
          task='string',
          containerName='string',
          status='string',
          exitCode=123,
          reason='string',
          networkBindings=[
              {
                  'bindIP': 'string',
                  'containerPort': 123,
                  'hostPort': 123,
                  'protocol': 'tcp'|'udp'
              },
          ]
      )
    :type cluster: string
    :param cluster: 

      The short name or full ARN of the cluster that hosts the container.

      

    
    :type task: string
    :param task: 

      The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.

      

    
    :type containerName: string
    :param containerName: 

      The name of the container.

      

    
    :type status: string
    :param status: 

      The status of the state change request.

      

    
    :type exitCode: integer
    :param exitCode: 

      The exit code returned for the state change request.

      

    
    :type reason: string
    :param reason: 

      The reason for the state change request.

      

    
    :type networkBindings: list
    :param networkBindings: 

      The network bindings of the container.

      

    
      - *(dict) --* 

        Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

        

      
        - **bindIP** *(string) --* 

          The IP address that the container is bound to on the container instance.

          

        
        - **containerPort** *(integer) --* 

          The port number on the container that is used with the network binding.

          

        
        - **hostPort** *(integer) --* 

          The port number on the host that is used with the network binding.

          

        
        - **protocol** *(string) --* 

          The protocol used for the network binding.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'acknowledgment': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **acknowledgment** *(string) --* 

          Acknowledgement of the state change.

          
    

  .. py:method:: submit_task_state_change(**kwargs)

    

    .. note::

       

      This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

       

     

    Sent to acknowledge that a task changed states.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/SubmitTaskStateChange>`_    


    **Request Syntax** 
    ::

      response = client.submit_task_state_change(
          cluster='string',
          task='string',
          status='string',
          reason='string',
          containers=[
              {
                  'containerName': 'string',
                  'exitCode': 123,
                  'networkBindings': [
                      {
                          'bindIP': 'string',
                          'containerPort': 123,
                          'hostPort': 123,
                          'protocol': 'tcp'|'udp'
                      },
                  ],
                  'reason': 'string',
                  'status': 'string'
              },
          ],
          attachments=[
              {
                  'attachmentArn': 'string',
                  'status': 'string'
              },
          ],
          pullStartedAt=datetime(2015, 1, 1),
          pullStoppedAt=datetime(2015, 1, 1),
          executionStoppedAt=datetime(2015, 1, 1)
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.

      

    
    :type task: string
    :param task: 

      The task ID or full ARN of the task in the state change request.

      

    
    :type status: string
    :param status: 

      The status of the state change request.

      

    
    :type reason: string
    :param reason: 

      The reason for the state change request.

      

    
    :type containers: list
    :param containers: 

      Any containers associated with the state change request.

      

    
      - *(dict) --* 

        An object representing a change in state for a container.

        

      
        - **containerName** *(string) --* 

          The name of the container.

          

        
        - **exitCode** *(integer) --* 

          The exit code for the container, if the state change is a result of the container exiting.

          

        
        - **networkBindings** *(list) --* 

          Any network bindings associated with the container.

          

        
          - *(dict) --* 

            Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.

            

          
            - **bindIP** *(string) --* 

              The IP address that the container is bound to on the container instance.

              

            
            - **containerPort** *(integer) --* 

              The port number on the container that is used with the network binding.

              

            
            - **hostPort** *(integer) --* 

              The port number on the host that is used with the network binding.

              

            
            - **protocol** *(string) --* 

              The protocol used for the network binding.

              

            
          
      
        - **reason** *(string) --* 

          The reason for the state change.

          

        
        - **status** *(string) --* 

          The status of the container.

          

        
      
  
    :type attachments: list
    :param attachments: 

      Any attachments associated with the state change request.

      

    
      - *(dict) --* 

        An object representing a change in state for a task attachment.

        

      
        - **attachmentArn** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the attachment.

          

        
        - **status** *(string) --* **[REQUIRED]** 

          The status of the attachment.

          

        
      
  
    :type pullStartedAt: datetime
    :param pullStartedAt: 

      The Unix time stamp for when the container image pull began.

      

    
    :type pullStoppedAt: datetime
    :param pullStoppedAt: 

      The Unix time stamp for when the container image pull completed.

      

    
    :type executionStoppedAt: datetime
    :param executionStoppedAt: 

      The Unix timestamp for when the task execution stopped.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'acknowledgment': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **acknowledgment** *(string) --* 

          Acknowledgement of the state change.

          
    

  .. py:method:: update_container_agent(**kwargs)

    

    Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent does not interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system.

     

     ``UpdateContainerAgent`` requires the Amazon ECS-optimized AMI or Amazon Linux with the ``ecs-init`` service installed and running. For help updating the Amazon ECS container agent on other operating systems, see `Manually Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html#manually_update_agent>`__ in the *Amazon Elastic Container Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UpdateContainerAgent>`_    


    **Request Syntax** 
    ::

      response = client.update_container_agent(
          cluster='string',
          containerInstance='string'
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type containerInstance: string
    :param containerInstance: **[REQUIRED]** 

      The container instance ID or full ARN entries for the container instance on which you would like to update the Amazon ECS container agent.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'containerInstance': {
                'containerInstanceArn': 'string',
                'ec2InstanceId': 'string',
                'version': 123,
                'versionInfo': {
                    'agentVersion': 'string',
                    'agentHash': 'string',
                    'dockerVersion': 'string'
                },
                'remainingResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'registeredResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'status': 'string',
                'agentConnected': True|False,
                'runningTasksCount': 123,
                'pendingTasksCount': 123,
                'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                'attributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'registeredAt': datetime(2015, 1, 1),
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **containerInstance** *(dict) --* 

          The container instance for which the container agent was updated.

          
          

          - **containerInstanceArn** *(string) --* 

            The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .

            
          

          - **ec2InstanceId** *(string) --* 

            The EC2 instance ID of the container instance.

            
          

          - **version** *(integer) --* 

            The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.

            
          

          - **versionInfo** *(dict) --* 

            The version information for the Amazon ECS container agent and Docker daemon running on the container instance.

            
            

            - **agentVersion** *(string) --* 

              The version number of the Amazon ECS container agent.

              
            

            - **agentHash** *(string) --* 

              The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.

              
            

            - **dockerVersion** *(string) --* 

              The Docker version running on the container instance.

              
        
          

          - **remainingResources** *(list) --* 

            For most resource types, this parameter describes the remaining resources of the container instance that are available for new tasks. For port resource types, this parameter describes the ports that are reserved by the Amazon ECS container agent and any containers that have reserved port mappings; any port that is not specified here is available for new tasks.

            
            

            - *(dict) --* 

              Describes the resources available for a container instance.

              
              

              - **name** *(string) --* 

                The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                
              

              - **type** *(string) --* 

                The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                
              

              - **doubleValue** *(float) --* 

                When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                
              

              - **longValue** *(integer) --* 

                When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                
              

              - **integerValue** *(integer) --* 

                When the ``integerValue`` type is set, the value of the resource must be an integer.

                
              

              - **stringSetValue** *(list) --* 

                When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                
                

                - *(string) --* 
            
          
        
          

          - **registeredResources** *(list) --* 

            For most resource types, this parameter describes the registered resources on the container instance that are in use by current tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.

            
            

            - *(dict) --* 

              Describes the resources available for a container instance.

              
              

              - **name** *(string) --* 

                The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                
              

              - **type** *(string) --* 

                The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                
              

              - **doubleValue** *(float) --* 

                When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                
              

              - **longValue** *(integer) --* 

                When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                
              

              - **integerValue** *(integer) --* 

                When the ``integerValue`` type is set, the value of the resource must be an integer.

                
              

              - **stringSetValue** *(list) --* 

                When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                
                

                - *(string) --* 
            
          
        
          

          - **status** *(string) --* 

            The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **agentConnected** *(boolean) --* 

            This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Instances without a connected agent can't accept placement requests.

            
          

          - **runningTasksCount** *(integer) --* 

            The number of tasks on the container instance that are in the ``RUNNING`` status.

            
          

          - **pendingTasksCount** *(integer) --* 

            The number of tasks on the container instance that are in the ``PENDING`` status.

            
          

          - **agentUpdateStatus** *(string) --* 

            The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .

            
          

          - **attributes** *(list) --* 

            The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.

            
            

            - *(dict) --* 

              An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **name** *(string) --* 

                The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

                
              

              - **value** *(string) --* 

                The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

                
              

              - **targetType** *(string) --* 

                The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

                
              

              - **targetId** *(string) --* 

                The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

                
          
        
          

          - **registeredAt** *(datetime) --* 

            The Unix time stamp for when the container instance was registered.

            
          

          - **attachments** *(list) --* 

            The Elastic Network Interfaces associated with the container instance.

            
            

            - *(dict) --* 

              An object representing a container instance or task attachment.

              
              

              - **id** *(string) --* 

                The unique identifier for the attachment.

                
              

              - **type** *(string) --* 

                The type of the attachment, such as an ``ElasticNetworkInterface`` .

                
              

              - **status** *(string) --* 

                The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                
              

              - **details** *(list) --* 

                Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                
                

                - *(dict) --* 

                  A key and value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key value pair. For environment variables, this is the value of the environment variable.

                    
              
            
          
        
      
    

  .. py:method:: update_container_instances_state(**kwargs)

    

    Modifies the status of an Amazon ECS container instance.

     

    You can change the status of a container instance to ``DRAINING`` to manually remove an instance from a cluster, for example to perform system updates, update the Docker daemon, or scale down the cluster size. 

     

    When you set a container instance to ``DRAINING`` , Amazon ECS prevents new tasks from being scheduled for placement on the container instance and replacement service tasks are started on other container instances in the cluster if the resources are available. Service tasks on the container instance that are in the ``PENDING`` state are stopped immediately.

     

    Service tasks on the container instance that are in the ``RUNNING`` state are stopped and replaced according to the service's deployment configuration parameters, ``minimumHealthyPercent`` and ``maximumPercent`` . You can change the deployment configuration of your service using  UpdateService .

     

     
    * If ``minimumHealthyPercent`` is below 100%, the scheduler can ignore ``desiredCount`` temporarily during task replacement. For example, ``desiredCount`` is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. If the minimum is 100%, the service scheduler can't remove existing tasks until the replacement tasks are considered healthy. Tasks for services that do not use a load balancer are considered healthy if they are in the ``RUNNING`` state. Tasks for services that use a load balancer are considered healthy if they are in the ``RUNNING`` state and the container instance they are hosted on is reported as healthy by the load balancer. 
     
    * The ``maximumPercent`` parameter represents an upper limit on the number of running tasks during task replacement, which enables you to define the replacement batch size. For example, if ``desiredCount`` of four tasks, a maximum of 200% starts four new tasks before stopping the four tasks to be drained (provided that the cluster resources required to do this are available). If the maximum is 100%, then replacement tasks can't start until the draining tasks have stopped. 
     

     

    Any ``PENDING`` or ``RUNNING`` tasks that do not belong to a service are not affected; you must wait for them to finish or stop them manually.

     

    A container instance has completed draining when it has no more ``RUNNING`` tasks. You can verify this using  ListTasks .

     

    When you set a container instance to ``ACTIVE`` , the Amazon ECS scheduler can begin scheduling tasks on the instance again.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UpdateContainerInstancesState>`_    


    **Request Syntax** 
    ::

      response = client.update_container_instances_state(
          cluster='string',
          containerInstances=[
              'string',
          ],
          status='ACTIVE'|'DRAINING'
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type containerInstances: list
    :param containerInstances: **[REQUIRED]** 

      A list of container instance IDs or full ARN entries.

      

    
      - *(string) --* 

      
  
    :type status: string
    :param status: **[REQUIRED]** 

      The container instance state with which to update the container instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'containerInstances': [
                {
                    'containerInstanceArn': 'string',
                    'ec2InstanceId': 'string',
                    'version': 123,
                    'versionInfo': {
                        'agentVersion': 'string',
                        'agentHash': 'string',
                        'dockerVersion': 'string'
                    },
                    'remainingResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'registeredResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'status': 'string',
                    'agentConnected': True|False,
                    'runningTasksCount': 123,
                    'pendingTasksCount': 123,
                    'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                    'attributes': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'targetType': 'container-instance',
                            'targetId': 'string'
                        },
                    ],
                    'registeredAt': datetime(2015, 1, 1),
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                },
            ],
            'failures': [
                {
                    'arn': 'string',
                    'reason': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **containerInstances** *(list) --* 

          The list of container instances.

          
          

          - *(dict) --* 

            An EC2 instance that is running the Amazon ECS agent and has been registered with a cluster.

            
            

            - **containerInstanceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .

              
            

            - **ec2InstanceId** *(string) --* 

              The EC2 instance ID of the container instance.

              
            

            - **version** *(integer) --* 

              The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.

              
            

            - **versionInfo** *(dict) --* 

              The version information for the Amazon ECS container agent and Docker daemon running on the container instance.

              
              

              - **agentVersion** *(string) --* 

                The version number of the Amazon ECS container agent.

                
              

              - **agentHash** *(string) --* 

                The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.

                
              

              - **dockerVersion** *(string) --* 

                The Docker version running on the container instance.

                
          
            

            - **remainingResources** *(list) --* 

              For most resource types, this parameter describes the remaining resources of the container instance that are available for new tasks. For port resource types, this parameter describes the ports that are reserved by the Amazon ECS container agent and any containers that have reserved port mappings; any port that is not specified here is available for new tasks.

              
              

              - *(dict) --* 

                Describes the resources available for a container instance.

                
                

                - **name** *(string) --* 

                  The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                  
                

                - **type** *(string) --* 

                  The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                  
                

                - **doubleValue** *(float) --* 

                  When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                  
                

                - **longValue** *(integer) --* 

                  When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                  
                

                - **integerValue** *(integer) --* 

                  When the ``integerValue`` type is set, the value of the resource must be an integer.

                  
                

                - **stringSetValue** *(list) --* 

                  When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                  
                  

                  - *(string) --* 
              
            
          
            

            - **registeredResources** *(list) --* 

              For most resource types, this parameter describes the registered resources on the container instance that are in use by current tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.

              
              

              - *(dict) --* 

                Describes the resources available for a container instance.

                
                

                - **name** *(string) --* 

                  The name of the resource, such as ``cpu`` , ``memory`` , ``ports`` , or a user-defined resource.

                  
                

                - **type** *(string) --* 

                  The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .

                  
                

                - **doubleValue** *(float) --* 

                  When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.

                  
                

                - **longValue** *(integer) --* 

                  When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.

                  
                

                - **integerValue** *(integer) --* 

                  When the ``integerValue`` type is set, the value of the resource must be an integer.

                  
                

                - **stringSetValue** *(list) --* 

                  When the ``stringSetValue`` type is set, the value of the resource must be a string type.

                  
                  

                  - *(string) --* 
              
            
          
            

            - **status** *(string) --* 

              The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
            

            - **agentConnected** *(boolean) --* 

              This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Instances without a connected agent can't accept placement requests.

              
            

            - **runningTasksCount** *(integer) --* 

              The number of tasks on the container instance that are in the ``RUNNING`` status.

              
            

            - **pendingTasksCount** *(integer) --* 

              The number of tasks on the container instance that are in the ``PENDING`` status.

              
            

            - **agentUpdateStatus** *(string) --* 

              The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .

              
            

            - **attributes** *(list) --* 

              The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.

              
              

              - *(dict) --* 

                An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
                

                - **name** *(string) --* 

                  The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.

                  
                

                - **value** *(string) --* 

                  The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.

                  
                

                - **targetType** *(string) --* 

                  The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.

                  
                

                - **targetId** *(string) --* 

                  The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

                  
            
          
            

            - **registeredAt** *(datetime) --* 

              The Unix time stamp for when the container instance was registered.

              
            

            - **attachments** *(list) --* 

              The Elastic Network Interfaces associated with the container instance.

              
              

              - *(dict) --* 

                An object representing a container instance or task attachment.

                
                

                - **id** *(string) --* 

                  The unique identifier for the attachment.

                  
                

                - **type** *(string) --* 

                  The type of the attachment, such as an ``ElasticNetworkInterface`` .

                  
                

                - **status** *(string) --* 

                  The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .

                  
                

                - **details** *(list) --* 

                  Details of the attachment. For Elastic Network Interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

                  
                  

                  - *(dict) --* 

                    A key and value pair object.

                    
                    

                    - **name** *(string) --* 

                      The name of the key value pair. For environment variables, this is the name of the environment variable.

                      
                    

                    - **value** *(string) --* 

                      The value of the key value pair. For environment variables, this is the value of the environment variable.

                      
                
              
            
          
        
      
        

        - **failures** *(list) --* 

          Any failures associated with the call.

          
          

          - *(dict) --* 

            A failed resource.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the failed resource.

              
            

            - **reason** *(string) --* 

              The reason for the failure.

              
        
      
    

  .. py:method:: update_service(**kwargs)

    

    Modifies the desired count, deployment configuration, network configuration, or task definition used in a service.

     

    You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new ``desiredCount`` parameter.

     

    You can use  UpdateService to modify your task definition and deploy a new version of your service.

     

    You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, ``minimumHealthyPercent`` and ``maximumPercent`` , to determine the deployment strategy.

     

     
    * If ``minimumHealthyPercent`` is below 100%, the scheduler can ignore ``desiredCount`` temporarily during a deployment. For example, if ``desiredCount`` is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the ``RUNNING`` state. Tasks for services that use a load balancer are considered healthy if they are in the ``RUNNING`` state and the container instance they are hosted on is reported as healthy by the load balancer. 
     
    * The ``maximumPercent`` parameter represents an upper limit on the number of running tasks during a deployment, which enables you to define the deployment batch size. For example, if ``desiredCount`` is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). 
     

     

    When  UpdateService stops a task during a deployment, the equivalent of ``docker stop`` is issued to the containers running in the task. This results in a ``SIGTERM`` and a 30-second timeout, after which ``SIGKILL`` is sent and the containers are forcibly stopped. If the container handles the ``SIGTERM`` gracefully and exits within 30 seconds from receiving it, no ``SIGKILL`` is sent.

     

    When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic:

     

     
    * Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes). 
     
    * By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy): 

       
      * Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement. 
       
      * Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service. 
       

     
     

     

    When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic: 

     

     
    * Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination. 
     
    * Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UpdateService>`_    


    **Request Syntax** 
    ::

      response = client.update_service(
          cluster='string',
          service='string',
          desiredCount=123,
          taskDefinition='string',
          deploymentConfiguration={
              'maximumPercent': 123,
              'minimumHealthyPercent': 123
          },
          networkConfiguration={
              'awsvpcConfiguration': {
                  'subnets': [
                      'string',
                  ],
                  'securityGroups': [
                      'string',
                  ],
                  'assignPublicIp': 'ENABLED'|'DISABLED'
              }
          },
          platformVersion='string',
          forceNewDeployment=True|False
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that your service is running on. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type service: string
    :param service: **[REQUIRED]** 

      The name of the service to update.

      

    
    :type desiredCount: integer
    :param desiredCount: 

      The number of instantiations of the task to place and keep running in your service.

      

    
    :type taskDefinition: string
    :param taskDefinition: 

      The ``family`` and ``revision`` (``family:revision`` ) or full ARN of the task definition to run in your service. If a ``revision`` is not specified, the latest ``ACTIVE`` revision is used. If you modify the task definition with ``UpdateService`` , Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.

      

    
    :type deploymentConfiguration: dict
    :param deploymentConfiguration: 

      Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.

      

    
      - **maximumPercent** *(integer) --* 

        The upper limit (as a percentage of the service's ``desiredCount`` ) of the number of tasks that are allowed in the ``RUNNING`` or ``PENDING`` state in a service during a deployment. The maximum number of tasks during a deployment is the ``desiredCount`` multiplied by ``maximumPercent`` /100, rounded down to the nearest integer value.

        

      
      - **minimumHealthyPercent** *(integer) --* 

        The lower limit (as a percentage of the service's ``desiredCount`` ) of the number of running tasks that must remain in the ``RUNNING`` state in a service during a deployment. The minimum number of healthy tasks during a deployment is the ``desiredCount`` multiplied by ``minimumHealthyPercent`` /100, rounded up to the nearest integer value.

        

      
    
    :type networkConfiguration: dict
    :param networkConfiguration: 

      The network configuration for the service. This parameter is required for task definitions that use the ``awsvpc`` network mode to receive their own Elastic Network Interface, and it is not supported for other network modes. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

       

      .. note::

         

        Updating a service to add a subnet to a list of existing subnets does not trigger a service deployment. For example, if your network configuration change is to keep the existing subnets and simply add another subnet to the network configuration, this does not trigger a new service deployment.

         

      

    
      - **awsvpcConfiguration** *(dict) --* 

        The VPC subnets and security groups associated with a task.

        

      
        - **subnets** *(list) --* **[REQUIRED]** 

          The subnets associated with the task or service.

          

        
          - *(string) --* 

          
      
        - **securityGroups** *(list) --* 

          The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

          

        
          - *(string) --* 

          
      
        - **assignPublicIp** *(string) --* 

          Specifies whether or not the task's elastic network interface receives a public IP address.

          

        
      
    
    :type platformVersion: string
    :param platformVersion: 

      The platform version you want to update your service to run.

      

    
    :type forceNewDeployment: boolean
    :param forceNewDeployment: 

      Whether or not to force a new deployment of the service.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'service': {
                'serviceArn': 'string',
                'serviceName': 'string',
                'clusterArn': 'string',
                'loadBalancers': [
                    {
                        'targetGroupArn': 'string',
                        'loadBalancerName': 'string',
                        'containerName': 'string',
                        'containerPort': 123
                    },
                ],
                'status': 'string',
                'desiredCount': 123,
                'runningCount': 123,
                'pendingCount': 123,
                'launchType': 'EC2'|'FARGATE',
                'platformVersion': 'string',
                'taskDefinition': 'string',
                'deploymentConfiguration': {
                    'maximumPercent': 123,
                    'minimumHealthyPercent': 123
                },
                'deployments': [
                    {
                        'id': 'string',
                        'status': 'string',
                        'taskDefinition': 'string',
                        'desiredCount': 123,
                        'pendingCount': 123,
                        'runningCount': 123,
                        'createdAt': datetime(2015, 1, 1),
                        'updatedAt': datetime(2015, 1, 1),
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'networkConfiguration': {
                            'awsvpcConfiguration': {
                                'subnets': [
                                    'string',
                                ],
                                'securityGroups': [
                                    'string',
                                ],
                                'assignPublicIp': 'ENABLED'|'DISABLED'
                            }
                        }
                    },
                ],
                'roleArn': 'string',
                'events': [
                    {
                        'id': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'message': 'string'
                    },
                ],
                'createdAt': datetime(2015, 1, 1),
                'placementConstraints': [
                    {
                        'type': 'distinctInstance'|'memberOf',
                        'expression': 'string'
                    },
                ],
                'placementStrategy': [
                    {
                        'type': 'random'|'spread'|'binpack',
                        'field': 'string'
                    },
                ],
                'networkConfiguration': {
                    'awsvpcConfiguration': {
                        'subnets': [
                            'string',
                        ],
                        'securityGroups': [
                            'string',
                        ],
                        'assignPublicIp': 'ENABLED'|'DISABLED'
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **service** *(dict) --* 

          The full description of your service following the update call.

          
          

          - **serviceArn** *(string) --* 

            The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace, followed by the region of the service, the AWS account ID of the service owner, the ``service`` namespace, and then the service name. For example, ``arn:aws:ecs:*region* :*012345678910* :service/*my-service* `` .

            
          

          - **serviceName** *(string) --* 

            The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a region or across multiple regions.

            
          

          - **clusterArn** *(string) --* 

            The Amazon Resource Name (ARN) of the cluster that hosts the service.

            
          

          - **loadBalancers** *(list) --* 

            A list of Elastic Load Balancing load balancer objects, containing the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer.

            
            

            - *(dict) --* 

              Details on a load balancer that is used with a service.

              
              

              - **targetGroupArn** *(string) --* 

                The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group associated with a service.

                
              

              - **loadBalancerName** *(string) --* 

                The name of a load balancer.

                
              

              - **containerName** *(string) --* 

                The name of the container (as it appears in a container definition) to associate with the load balancer.

                
              

              - **containerPort** *(integer) --* 

                The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.

                
          
        
          

          - **status** *(string) --* 

            The status of the service. The valid values are ``ACTIVE`` , ``DRAINING`` , or ``INACTIVE`` .

            
          

          - **desiredCount** *(integer) --* 

            The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .

            
          

          - **runningCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``RUNNING`` state.

            
          

          - **pendingCount** *(integer) --* 

            The number of tasks in the cluster that are in the ``PENDING`` state.

            
          

          - **launchType** *(string) --* 

            The launch type on which your service is running.

            
          

          - **platformVersion** *(string) --* 

            The platform version on which your task is running. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

            
          

          - **taskDefinition** *(string) --* 

            The task definition to use for tasks in the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .

            
          

          - **deploymentConfiguration** *(dict) --* 

            Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.

            
            

            - **maximumPercent** *(integer) --* 

              The upper limit (as a percentage of the service's ``desiredCount`` ) of the number of tasks that are allowed in the ``RUNNING`` or ``PENDING`` state in a service during a deployment. The maximum number of tasks during a deployment is the ``desiredCount`` multiplied by ``maximumPercent`` /100, rounded down to the nearest integer value.

              
            

            - **minimumHealthyPercent** *(integer) --* 

              The lower limit (as a percentage of the service's ``desiredCount`` ) of the number of running tasks that must remain in the ``RUNNING`` state in a service during a deployment. The minimum number of healthy tasks during a deployment is the ``desiredCount`` multiplied by ``minimumHealthyPercent`` /100, rounded up to the nearest integer value.

              
        
          

          - **deployments** *(list) --* 

            The current state of deployments for the service.

            
            

            - *(dict) --* 

              The details of an Amazon ECS service deployment.

              
              

              - **id** *(string) --* 

                The ID of the deployment.

                
              

              - **status** *(string) --* 

                The status of the deployment. Valid values are ``PRIMARY`` (for the most recent deployment), ``ACTIVE`` (for previous deployments that still have tasks running, but are being replaced with the ``PRIMARY`` deployment), and ``INACTIVE`` (for deployments that have been completely replaced).

                
              

              - **taskDefinition** *(string) --* 

                The most recent task definition that was specified for the service to use.

                
              

              - **desiredCount** *(integer) --* 

                The most recent desired count of tasks that was specified for the service to deploy or maintain.

                
              

              - **pendingCount** *(integer) --* 

                The number of tasks in the deployment that are in the ``PENDING`` status.

                
              

              - **runningCount** *(integer) --* 

                The number of tasks in the deployment that are in the ``RUNNING`` status.

                
              

              - **createdAt** *(datetime) --* 

                The Unix time stamp for when the service was created.

                
              

              - **updatedAt** *(datetime) --* 

                The Unix time stamp for when the service was last updated.

                
              

              - **launchType** *(string) --* 

                The launch type on which your service is running.

                
              

              - **platformVersion** *(string) --* 

                The platform version on which your service is running.

                
              

              - **networkConfiguration** *(dict) --* 

                The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

                
                

                - **awsvpcConfiguration** *(dict) --* 

                  The VPC subnets and security groups associated with a task.

                  
                  

                  - **subnets** *(list) --* 

                    The subnets associated with the task or service.

                    
                    

                    - *(string) --* 
                
                  

                  - **securityGroups** *(list) --* 

                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

                    
                    

                    - *(string) --* 
                
                  

                  - **assignPublicIp** *(string) --* 

                    Specifies whether or not the task's elastic network interface receives a public IP address.

                    
              
            
          
        
          

          - **roleArn** *(string) --* 

            The ARN of the IAM role associated with the service that allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.

            
          

          - **events** *(list) --* 

            The event stream for your service. A maximum of 100 of the latest events are displayed.

            
            

            - *(dict) --* 

              Details on an event associated with a service.

              
              

              - **id** *(string) --* 

                The ID string of the event.

                
              

              - **createdAt** *(datetime) --* 

                The Unix time stamp for when the event was triggered.

                
              

              - **message** *(string) --* 

                The event message.

                
          
        
          

          - **createdAt** *(datetime) --* 

            The Unix time stamp for when the service was created.

            
          

          - **placementConstraints** *(list) --* 

            The placement constraints for the tasks in the service.

            
            

            - *(dict) --* 

              An object representing a constraint on task placement. For more information, see `Task Placement Constraints <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.

                
              

              - **expression** *(string) --* 

                A cluster query language expression to apply to the constraint. Note you cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

                
          
        
          

          - **placementStrategy** *(list) --* 

            The placement strategy that determines how tasks for the service are placed.

            
            

            - *(dict) --* 

              The task placement strategy for a task or service. For more information, see `Task Placement Strategies <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

              
              

              - **type** *(string) --* 

                The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

                
              

              - **field** *(string) --* 

                The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.

                
          
        
          

          - **networkConfiguration** *(dict) --* 

            The VPC subnet and security group configuration for tasks that receive their own Elastic Network Interface by using the ``awsvpc`` networking mode.

            
            

            - **awsvpcConfiguration** *(dict) --* 

              The VPC subnets and security groups associated with a task.

              
              

              - **subnets** *(list) --* 

                The subnets associated with the task or service.

                
                

                - *(string) --* 
            
              

              - **securityGroups** *(list) --* 

                The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

                
                

                - *(string) --* 
            
              

              - **assignPublicIp** *(string) --* 

                Specifies whether or not the task's elastic network interface receives a public IP address.

                
          
        
      
    

    **Examples** 

    This example updates the my-http-service service to use the amazon-ecs-sample task definition.
    ::

      response = client.update_service(
          service='my-http-service',
          taskDefinition='amazon-ecs-sample',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example updates the desired count of the my-http-service service to 10.
    ::

      response = client.update_service(
          desiredCount=10,
          service='my-http-service',
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

* :py:class:`ECS.Paginator.ListClusters`


* :py:class:`ECS.Paginator.ListContainerInstances`


* :py:class:`ECS.Paginator.ListServices`


* :py:class:`ECS.Paginator.ListTaskDefinitionFamilies`


* :py:class:`ECS.Paginator.ListTaskDefinitions`


* :py:class:`ECS.Paginator.ListTasks`



.. py:class:: ECS.Paginator.ListClusters

  ::

    
    paginator = client.get_paginator('list_clusters')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ECS.Client.list_clusters`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListClusters>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
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
            'clusterArns': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **clusterArns** *(list) --* 

          The list of full Amazon Resource Name (ARN) entries for each cluster associated with your account.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ECS.Paginator.ListContainerInstances

  ::

    
    paginator = client.get_paginator('list_container_instances')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ECS.Client.list_container_instances`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListContainerInstances>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          cluster='string',
          filter='string',
          status='ACTIVE'|'DRAINING',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type filter: string
    :param filter: 

      You can filter the results of a ``ListContainerInstances`` operation with cluster query language statements. For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

      

    
    :type status: string
    :param status: 

      Filters the container instances by status. For example, if you specify the ``DRAINING`` status, the results include only container instances that have been set to ``DRAINING`` using  UpdateContainerInstancesState . If you do not specify this parameter, the default is to include container instances set to ``ACTIVE`` and ``DRAINING`` .

      

    
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
            'containerInstanceArns': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **containerInstanceArns** *(list) --* 

          The list of container instances with full ARN entries for each container instance associated with the specified cluster.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ECS.Paginator.ListServices

  ::

    
    paginator = client.get_paginator('list_services')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ECS.Client.list_services`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListServices>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          cluster='string',
          launchType='EC2'|'FARGATE',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the services to list. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type launchType: string
    :param launchType: 

      The launch type for services you want to list.

      

    
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
            'serviceArns': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **serviceArns** *(list) --* 

          The list of full ARN entries for each service associated with the specified cluster.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ECS.Paginator.ListTaskDefinitionFamilies

  ::

    
    paginator = client.get_paginator('list_task_definition_families')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ECS.Client.list_task_definition_families`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTaskDefinitionFamilies>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          familyPrefix='string',
          status='ACTIVE'|'INACTIVE'|'ALL',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type familyPrefix: string
    :param familyPrefix: 

      The ``familyPrefix`` is a string that is used to filter the results of ``ListTaskDefinitionFamilies`` . If you specify a ``familyPrefix`` , only task definition family names that begin with the ``familyPrefix`` string are returned.

      

    
    :type status: string
    :param status: 

      The task definition family status with which to filter the ``ListTaskDefinitionFamilies`` results. By default, both ``ACTIVE`` and ``INACTIVE`` task definition families are listed. If this parameter is set to ``ACTIVE`` , only task definition families that have an ``ACTIVE`` task definition revision are returned. If this parameter is set to ``INACTIVE`` , only task definition families that do not have any ``ACTIVE`` task definition revisions are returned. If you paginate the resulting output, be sure to keep the ``status`` value constant in each subsequent request.

      

    
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
            'families': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **families** *(list) --* 

          The list of task definition family names that match the ``ListTaskDefinitionFamilies`` request.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ECS.Paginator.ListTaskDefinitions

  ::

    
    paginator = client.get_paginator('list_task_definitions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ECS.Client.list_task_definitions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTaskDefinitions>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          familyPrefix='string',
          status='ACTIVE'|'INACTIVE',
          sort='ASC'|'DESC',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type familyPrefix: string
    :param familyPrefix: 

      The full family name with which to filter the ``ListTaskDefinitions`` results. Specifying a ``familyPrefix`` limits the listed task definitions to task definition revisions that belong to that family.

      

    
    :type status: string
    :param status: 

      The task definition status with which to filter the ``ListTaskDefinitions`` results. By default, only ``ACTIVE`` task definitions are listed. By setting this parameter to ``INACTIVE`` , you can view task definitions that are ``INACTIVE`` as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the ``status`` value constant in each subsequent request.

      

    
    :type sort: string
    :param sort: 

      The order in which to sort the results. Valid values are ``ASC`` and ``DESC`` . By default (``ASC`` ), task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to ``DESC`` reverses the sort order on family name and revision so that the newest task definitions in a family are listed first.

      

    
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
            'taskDefinitionArns': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskDefinitionArns** *(list) --* 

          The list of task definition Amazon Resource Name (ARN) entries for the ``ListTaskDefinitions`` request.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ECS.Paginator.ListTasks

  ::

    
    paginator = client.get_paginator('list_tasks')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ECS.Client.list_tasks`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTasks>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          cluster='string',
          containerInstance='string',
          family='string',
          startedBy='string',
          serviceName='string',
          desiredStatus='RUNNING'|'PENDING'|'STOPPED',
          launchType='EC2'|'FARGATE',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the tasks to list. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type containerInstance: string
    :param containerInstance: 

      The container instance ID or full ARN of the container instance with which to filter the ``ListTasks`` results. Specifying a ``containerInstance`` limits the results to tasks that belong to that container instance.

      

    
    :type family: string
    :param family: 

      The name of the family with which to filter the ``ListTasks`` results. Specifying a ``family`` limits the results to tasks that belong to that family.

      

    
    :type startedBy: string
    :param startedBy: 

      The ``startedBy`` value with which to filter the task results. Specifying a ``startedBy`` value limits the results to tasks that were started with that value.

      

    
    :type serviceName: string
    :param serviceName: 

      The name of the service with which to filter the ``ListTasks`` results. Specifying a ``serviceName`` limits the results to tasks that belong to that service.

      

    
    :type desiredStatus: string
    :param desiredStatus: 

      The task desired status with which to filter the ``ListTasks`` results. Specifying a ``desiredStatus`` of ``STOPPED`` limits the results to tasks that Amazon ECS has set the desired status to ``STOPPED`` , which can be useful for debugging tasks that are not starting properly or have died or finished. The default status filter is ``RUNNING`` , which shows tasks that Amazon ECS has set the desired status to ``RUNNING`` .

       

      .. note::

         

        Although you can filter results based on a desired status of ``PENDING`` , this does not return any results because Amazon ECS never sets the desired status of a task to that value (only a task's ``lastStatus`` may have a value of ``PENDING`` ).

         

      

    
    :type launchType: string
    :param launchType: 

      The launch type for services you want to list.

      

    
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
            'taskArns': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskArns** *(list) --* 

          The list of task ARN entries for the ``ListTasks`` request.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

=======
Waiters
=======


The available waiters are:

* :py:class:`ECS.Waiter.ServicesInactive`


* :py:class:`ECS.Waiter.ServicesStable`


* :py:class:`ECS.Waiter.TasksRunning`


* :py:class:`ECS.Waiter.TasksStopped`



.. py:class:: ECS.Waiter.ServicesInactive

  ::

    
    waiter = client.get_waiter('services_inactive')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`ECS.Client.describe_services` every 15 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeServices>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          cluster='string',
          services=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type services: list
    :param services: **[REQUIRED]** 

      A list of services to describe. You may specify up to 10 services to describe in a single operation.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

.. py:class:: ECS.Waiter.ServicesStable

  ::

    
    waiter = client.get_waiter('services_stable')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`ECS.Client.describe_services` every 15 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeServices>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          cluster='string',
          services=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type services: list
    :param services: **[REQUIRED]** 

      A list of services to describe. You may specify up to 10 services to describe in a single operation.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

.. py:class:: ECS.Waiter.TasksRunning

  ::

    
    waiter = client.get_waiter('tasks_running')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`ECS.Client.describe_tasks` every 6 seconds until a successful state is reached. An error is returned after 100 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTasks>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          cluster='string',
          tasks=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to describe. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type tasks: list
    :param tasks: **[REQUIRED]** 

      A list of up to 100 task IDs or full ARN entries.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 6

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 100

        

      
    
    
    :returns: None

.. py:class:: ECS.Waiter.TasksStopped

  ::

    
    waiter = client.get_waiter('tasks_stopped')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`ECS.Client.describe_tasks` every 6 seconds until a successful state is reached. An error is returned after 100 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTasks>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          cluster='string',
          tasks=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type cluster: string
    :param cluster: 

      The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to describe. If you do not specify a cluster, the default cluster is assumed.

      

    
    :type tasks: list
    :param tasks: **[REQUIRED]** 

      A list of up to 100 task IDs or full ARN entries.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 6

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 100

        

      
    
    
    :returns: None