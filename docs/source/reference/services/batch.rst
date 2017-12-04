

*****
Batch
*****

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Batch.Client

  A low-level client representing AWS Batch::

    
    import boto3
    
    client = boto3.client('batch')

  
  These are the available methods:
  
  *   :py:meth:`~Batch.Client.can_paginate`

  
  *   :py:meth:`~Batch.Client.cancel_job`

  
  *   :py:meth:`~Batch.Client.create_compute_environment`

  
  *   :py:meth:`~Batch.Client.create_job_queue`

  
  *   :py:meth:`~Batch.Client.delete_compute_environment`

  
  *   :py:meth:`~Batch.Client.delete_job_queue`

  
  *   :py:meth:`~Batch.Client.deregister_job_definition`

  
  *   :py:meth:`~Batch.Client.describe_compute_environments`

  
  *   :py:meth:`~Batch.Client.describe_job_definitions`

  
  *   :py:meth:`~Batch.Client.describe_job_queues`

  
  *   :py:meth:`~Batch.Client.describe_jobs`

  
  *   :py:meth:`~Batch.Client.generate_presigned_url`

  
  *   :py:meth:`~Batch.Client.get_paginator`

  
  *   :py:meth:`~Batch.Client.get_waiter`

  
  *   :py:meth:`~Batch.Client.list_jobs`

  
  *   :py:meth:`~Batch.Client.register_job_definition`

  
  *   :py:meth:`~Batch.Client.submit_job`

  
  *   :py:meth:`~Batch.Client.terminate_job`

  
  *   :py:meth:`~Batch.Client.update_compute_environment`

  
  *   :py:meth:`~Batch.Client.update_job_queue`

  

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


  .. py:method:: cancel_job(**kwargs)

    

    Cancels a job in an AWS Batch job queue. Jobs that are in the ``SUBMITTED`` , ``PENDING`` , or ``RUNNABLE`` state are cancelled. Jobs that have progressed to ``STARTING`` or ``RUNNING`` are not cancelled (but the API operation still succeeds, even if no job is cancelled); these jobs must be terminated with the  TerminateJob operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/CancelJob>`_    


    **Request Syntax** 
    ::

      response = client.cancel_job(
          jobId='string',
          reason='string'
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The AWS Batch job ID of the job to cancel.

      

    
    :type reason: string
    :param reason: **[REQUIRED]** 

      A message to attach to the job that explains the reason for canceling it. This message is returned by future  DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example cancels a job with the specified job ID.
    ::

      response = client.cancel_job(
          jobId='1d828f65-7a4d-42e8-996d-3b900ed59dc4',
          reason='Cancelling job.',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_compute_environment(**kwargs)

    

    Creates an AWS Batch compute environment. You can create ``MANAGED`` or ``UNMANAGED`` compute environments.

     

    In a managed compute environment, AWS Batch manages the compute resources within the environment, based on the compute resources that you specify. Instances launched into a managed compute environment use a recent, approved version of the Amazon ECS-optimized AMI. You can choose to use Amazon EC2 On-Demand Instances in your managed compute environment, or you can use Amazon EC2 Spot Instances that only launch when the Spot bid price is below a specified percentage of the On-Demand price.

     

    In an unmanaged compute environment, you can manage your own compute resources. This provides more compute resource configuration options, such as using a custom AMI, but you must ensure that your AMI meets the Amazon ECS container instance AMI specification. For more information, see `Container Instance AMIs <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container_instance_AMIs.html>`__ in the *Amazon Elastic Container Service Developer Guide* . After you have created your unmanaged compute environment, you can use the  DescribeComputeEnvironments operation to find the Amazon ECS cluster that is associated with it and then manually launch your container instances into that Amazon ECS cluster. For more information, see `Launching an Amazon ECS Container Instance <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html>`__ in the *Amazon Elastic Container Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/CreateComputeEnvironment>`_    


    **Request Syntax** 
    ::

      response = client.create_compute_environment(
          computeEnvironmentName='string',
          type='MANAGED'|'UNMANAGED',
          state='ENABLED'|'DISABLED',
          computeResources={
              'type': 'EC2'|'SPOT',
              'minvCpus': 123,
              'maxvCpus': 123,
              'desiredvCpus': 123,
              'instanceTypes': [
                  'string',
              ],
              'imageId': 'string',
              'subnets': [
                  'string',
              ],
              'securityGroupIds': [
                  'string',
              ],
              'ec2KeyPair': 'string',
              'instanceRole': 'string',
              'tags': {
                  'string': 'string'
              },
              'bidPercentage': 123,
              'spotIamFleetRole': 'string'
          },
          serviceRole='string'
      )
    :type computeEnvironmentName: string
    :param computeEnvironmentName: **[REQUIRED]** 

      The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      The type of the compute environment. 

      

    
    :type state: string
    :param state: 

      The state of the compute environment. If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.

      

    
    :type computeResources: dict
    :param computeResources: 

      Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of compute environment.

        

      
      - **minvCpus** *(integer) --* **[REQUIRED]** 

        The minimum number of EC2 vCPUs that an environment should maintain. 

        

      
      - **maxvCpus** *(integer) --* **[REQUIRED]** 

        The maximum number of EC2 vCPUs that an environment can reach. 

        

      
      - **desiredvCpus** *(integer) --* 

        The desired number of EC2 vCPUS in the compute environment. 

        

      
      - **instanceTypes** *(list) --* **[REQUIRED]** 

        The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, ``c4`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c4.8xlarge`` ). You can also choose ``optimal`` to pick instance types (from the latest C, M, and R instance families) on the fly that match the demand of your job queues.

        

      
        - *(string) --* 

        
    
      - **imageId** *(string) --* 

        The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.

        

      
      - **subnets** *(list) --* **[REQUIRED]** 

        The VPC subnets into which the compute resources are launched. 

        

      
        - *(string) --* 

        
    
      - **securityGroupIds** *(list) --* **[REQUIRED]** 

        The EC2 security group that is associated with instances launched in the compute environment. 

        

      
        - *(string) --* 

        
    
      - **ec2KeyPair** *(string) --* 

        The EC2 key pair that is used for instances launched in the compute environment.

        

      
      - **instanceRole** *(string) --* **[REQUIRED]** 

        The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ``ecsInstanceRole`` or ``arn:aws:iam::<aws_account_id>:instance-profile/ecsInstanceRole`` . For more information, see `Amazon ECS Instance Role <http://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the *AWS Batch User Guide* .

        

      
      - **tags** *(dict) --* 

        Key-value pair tags to be applied to resources that are launched in the compute environment. 

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **bidPercentage** *(integer) --* 

        The minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance.

        

      
      - **spotIamFleetRole** *(string) --* 

        The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment.

        

      
    
    :type serviceRole: string
    :param serviceRole: **[REQUIRED]** 

      The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

       

      If your specified role has a path other than ``/`` , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.

       

      .. note::

         

        Depending on how you created your AWS Batch service role, its ARN may contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'computeEnvironmentName': 'string',
            'computeEnvironmentArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **computeEnvironmentName** *(string) --* 

          The name of the compute environment.

          
        

        - **computeEnvironmentArn** *(string) --* 

          The Amazon Resource Name (ARN) of the compute environment. 

          
    

    **Examples** 

    This example creates a managed compute environment with specific C4 instance types that are launched on demand. The compute environment is called C4OnDemand.
    ::

      response = client.create_compute_environment(
          type='MANAGED',
          computeEnvironmentName='C4OnDemand',
          computeResources={
              'type': 'EC2',
              'desiredvCpus': 48,
              'ec2KeyPair': 'id_rsa',
              'instanceRole': 'ecsInstanceRole',
              'instanceTypes': [
                  'c4.large',
                  'c4.xlarge',
                  'c4.2xlarge',
                  'c4.4xlarge',
                  'c4.8xlarge',
              ],
              'maxvCpus': 128,
              'minvCpus': 0,
              'securityGroupIds': [
                  'sg-cf5093b2',
              ],
              'subnets': [
                  'subnet-220c0e0a',
                  'subnet-1a95556d',
                  'subnet-978f6dce',
              ],
              'tags': {
                  'Name': 'Batch Instance - C4OnDemand',
              },
          },
          serviceRole='arn:aws:iam::012345678910:role/AWSBatchServiceRole',
          state='ENABLED',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'computeEnvironmentArn': 'arn:aws:batch:us-east-1:012345678910:compute-environment/C4OnDemand',
          'computeEnvironmentName': 'C4OnDemand',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example creates a managed compute environment with the M4 instance type that is launched when the Spot bid price is at or below 20% of the On-Demand price for the instance type. The compute environment is called M4Spot.
    ::

      response = client.create_compute_environment(
          type='MANAGED',
          computeEnvironmentName='M4Spot',
          computeResources={
              'type': 'SPOT',
              'bidPercentage': 20,
              'desiredvCpus': 4,
              'ec2KeyPair': 'id_rsa',
              'instanceRole': 'ecsInstanceRole',
              'instanceTypes': [
                  'm4',
              ],
              'maxvCpus': 128,
              'minvCpus': 0,
              'securityGroupIds': [
                  'sg-cf5093b2',
              ],
              'spotIamFleetRole': 'arn:aws:iam::012345678910:role/aws-ec2-spot-fleet-role',
              'subnets': [
                  'subnet-220c0e0a',
                  'subnet-1a95556d',
                  'subnet-978f6dce',
              ],
              'tags': {
                  'Name': 'Batch Instance - M4Spot',
              },
          },
          serviceRole='arn:aws:iam::012345678910:role/AWSBatchServiceRole',
          state='ENABLED',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'computeEnvironmentArn': 'arn:aws:batch:us-east-1:012345678910:compute-environment/M4Spot',
          'computeEnvironmentName': 'M4Spot',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_job_queue(**kwargs)

    

    Creates an AWS Batch job queue. When you create a job queue, you associate one or more compute environments to the queue and assign an order of preference for the compute environments.

     

    You also set a priority to the job queue that determines the order in which the AWS Batch scheduler places jobs onto its associated compute environments. For example, if a compute environment is associated with more than one job queue, the job queue with a higher priority is given preference for scheduling jobs to that compute environment.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/CreateJobQueue>`_    


    **Request Syntax** 
    ::

      response = client.create_job_queue(
          jobQueueName='string',
          state='ENABLED'|'DISABLED',
          priority=123,
          computeEnvironmentOrder=[
              {
                  'order': 123,
                  'computeEnvironment': 'string'
              },
          ]
      )
    :type jobQueueName: string
    :param jobQueueName: **[REQUIRED]** 

      The name of the job queue.

      

    
    :type state: string
    :param state: 

      The state of the job queue. If the job queue state is ``ENABLED`` , it is able to accept jobs.

      

    
    :type priority: integer
    :param priority: **[REQUIRED]** 

      The priority of the job queue. Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with same compute environment. Priority is determined in descending order, for example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` .

      

    
    :type computeEnvironmentOrder: list
    :param computeEnvironmentOrder: **[REQUIRED]** 

      The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment should execute a given job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue.

      

    
      - *(dict) --* 

        The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.

        

      
        - **order** *(integer) --* **[REQUIRED]** 

          The order of the compute environment.

          

        
        - **computeEnvironment** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the compute environment.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobQueueName': 'string',
            'jobQueueArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobQueueName** *(string) --* 

          The name of the job queue.

          
        

        - **jobQueueArn** *(string) --* 

          The Amazon Resource Name (ARN) of the job queue.

          
    

    **Examples** 

    This example creates a job queue called LowPriority that uses the M4Spot compute environment.
    ::

      response = client.create_job_queue(
          computeEnvironmentOrder=[
              {
                  'computeEnvironment': 'M4Spot',
                  'order': 1,
              },
          ],
          jobQueueName='LowPriority',
          priority=10,
          state='ENABLED',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobQueueArn': 'arn:aws:batch:us-east-1:012345678910:job-queue/LowPriority',
          'jobQueueName': 'LowPriority',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2.
    ::

      response = client.create_job_queue(
          computeEnvironmentOrder=[
              {
                  'computeEnvironment': 'C4OnDemand',
                  'order': 1,
              },
              {
                  'computeEnvironment': 'M4Spot',
                  'order': 2,
              },
          ],
          jobQueueName='HighPriority',
          priority=1,
          state='ENABLED',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobQueueArn': 'arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority',
          'jobQueueName': 'HighPriority',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_compute_environment(**kwargs)

    

    Deletes an AWS Batch compute environment.

     

    Before you can delete a compute environment, you must set its state to ``DISABLED`` with the  UpdateComputeEnvironment API operation and disassociate it from any job queues with the  UpdateJobQueue API operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DeleteComputeEnvironment>`_    


    **Request Syntax** 
    ::

      response = client.delete_compute_environment(
          computeEnvironment='string'
      )
    :type computeEnvironment: string
    :param computeEnvironment: **[REQUIRED]** 

      The name or Amazon Resource Name (ARN) of the compute environment to delete. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deletes the P2OnDemand compute environment.
    ::

      response = client.delete_compute_environment(
          computeEnvironment='P2OnDemand',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_job_queue(**kwargs)

    

    Deletes the specified job queue. You must first disable submissions for a queue with the  UpdateJobQueue operation. All jobs in the queue are terminated when you delete a job queue.

     

    It is not necessary to disassociate compute environments from a queue before submitting a ``DeleteJobQueue`` request. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DeleteJobQueue>`_    


    **Request Syntax** 
    ::

      response = client.delete_job_queue(
          jobQueue='string'
      )
    :type jobQueue: string
    :param jobQueue: **[REQUIRED]** 

      The short name or full Amazon Resource Name (ARN) of the queue to delete. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deletes the GPGPU job queue.
    ::

      response = client.delete_job_queue(
          jobQueue='GPGPU',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: deregister_job_definition(**kwargs)

    

    Deregisters an AWS Batch job definition.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DeregisterJobDefinition>`_    


    **Request Syntax** 
    ::

      response = client.deregister_job_definition(
          jobDefinition='string'
      )
    :type jobDefinition: string
    :param jobDefinition: **[REQUIRED]** 

      The name and revision (``name:revision`` ) or full Amazon Resource Name (ARN) of the job definition to deregister. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deregisters a job definition called sleep10.
    ::

      response = client.deregister_job_definition(
          jobDefinition='sleep10',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_compute_environments(**kwargs)

    

    Describes one or more of your compute environments.

     

    If you are using an unmanaged compute environment, you can use the ``DescribeComputeEnvironment`` operation to determine the ``ecsClusterArn`` that you should launch your Amazon ECS container instances into.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeComputeEnvironments>`_    


    **Request Syntax** 
    ::

      response = client.describe_compute_environments(
          computeEnvironments=[
              'string',
          ],
          maxResults=123,
          nextToken='string'
      )
    :type computeEnvironments: list
    :param computeEnvironments: 

      A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries. 

      

    
      - *(string) --* 

      
  
    :type maxResults: integer
    :param maxResults: 

      The maximum number of cluster results returned by ``DescribeComputeEnvironments`` in paginated output. When this parameter is used, ``DescribeComputeEnvironments`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeComputeEnvironments`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``DescribeComputeEnvironments`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``DescribeComputeEnvironments`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'computeEnvironments': [
                {
                    'computeEnvironmentName': 'string',
                    'computeEnvironmentArn': 'string',
                    'ecsClusterArn': 'string',
                    'type': 'MANAGED'|'UNMANAGED',
                    'state': 'ENABLED'|'DISABLED',
                    'status': 'CREATING'|'UPDATING'|'DELETING'|'DELETED'|'VALID'|'INVALID',
                    'statusReason': 'string',
                    'computeResources': {
                        'type': 'EC2'|'SPOT',
                        'minvCpus': 123,
                        'maxvCpus': 123,
                        'desiredvCpus': 123,
                        'instanceTypes': [
                            'string',
                        ],
                        'imageId': 'string',
                        'subnets': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ],
                        'ec2KeyPair': 'string',
                        'instanceRole': 'string',
                        'tags': {
                            'string': 'string'
                        },
                        'bidPercentage': 123,
                        'spotIamFleetRole': 'string'
                    },
                    'serviceRole': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **computeEnvironments** *(list) --* 

          The list of compute environments.

          
          

          - *(dict) --* 

            An object representing an AWS Batch compute environment.

            
            

            - **computeEnvironmentName** *(string) --* 

              The name of the compute environment. 

              
            

            - **computeEnvironmentArn** *(string) --* 

              The Amazon Resource Name (ARN) of the compute environment. 

              
            

            - **ecsClusterArn** *(string) --* 

              The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment. 

              
            

            - **type** *(string) --* 

              The type of the compute environment.

              
            

            - **state** *(string) --* 

              The state of the compute environment. The valid values are ``ENABLED`` or ``DISABLED`` . An ``ENABLED`` state indicates that you can register instances with the compute environment and that the associated instances can accept jobs. 

              
            

            - **status** *(string) --* 

              The current status of the compute environment (for example, ``CREATING`` or ``VALID`` ).

              
            

            - **statusReason** *(string) --* 

              A short, human-readable string to provide additional details about the current status of the compute environment.

              
            

            - **computeResources** *(dict) --* 

              The compute resources defined for the compute environment. 

              
              

              - **type** *(string) --* 

                The type of compute environment.

                
              

              - **minvCpus** *(integer) --* 

                The minimum number of EC2 vCPUs that an environment should maintain. 

                
              

              - **maxvCpus** *(integer) --* 

                The maximum number of EC2 vCPUs that an environment can reach. 

                
              

              - **desiredvCpus** *(integer) --* 

                The desired number of EC2 vCPUS in the compute environment. 

                
              

              - **instanceTypes** *(list) --* 

                The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, ``c4`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c4.8xlarge`` ). You can also choose ``optimal`` to pick instance types (from the latest C, M, and R instance families) on the fly that match the demand of your job queues.

                
                

                - *(string) --* 
            
              

              - **imageId** *(string) --* 

                The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.

                
              

              - **subnets** *(list) --* 

                The VPC subnets into which the compute resources are launched. 

                
                

                - *(string) --* 
            
              

              - **securityGroupIds** *(list) --* 

                The EC2 security group that is associated with instances launched in the compute environment. 

                
                

                - *(string) --* 
            
              

              - **ec2KeyPair** *(string) --* 

                The EC2 key pair that is used for instances launched in the compute environment.

                
              

              - **instanceRole** *(string) --* 

                The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ``ecsInstanceRole`` or ``arn:aws:iam::<aws_account_id>:instance-profile/ecsInstanceRole`` . For more information, see `Amazon ECS Instance Role <http://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the *AWS Batch User Guide* .

                
              

              - **tags** *(dict) --* 

                Key-value pair tags to be applied to resources that are launched in the compute environment. 

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **bidPercentage** *(integer) --* 

                The minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance.

                
              

              - **spotIamFleetRole** *(string) --* 

                The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment.

                
          
            

            - **serviceRole** *(string) --* 

              The service role associated with the compute environment that allows AWS Batch to make calls to AWS API operations on your behalf.

              
        
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``DescribeComputeEnvironments`` request. When the results of a ``DescribeJobDefinitions`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example describes the P2OnDemand compute environment.
    ::

      response = client.describe_compute_environments(
          computeEnvironments=[
              'P2OnDemand',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'computeEnvironments': [
              {
                  'type': 'MANAGED',
                  'computeEnvironmentArn': 'arn:aws:batch:us-east-1:012345678910:compute-environment/P2OnDemand',
                  'computeEnvironmentName': 'P2OnDemand',
                  'computeResources': {
                      'type': 'EC2',
                      'desiredvCpus': 48,
                      'ec2KeyPair': 'id_rsa',
                      'instanceRole': 'ecsInstanceRole',
                      'instanceTypes': [
                          'p2',
                      ],
                      'maxvCpus': 128,
                      'minvCpus': 0,
                      'securityGroupIds': [
                          'sg-cf5093b2',
                      ],
                      'subnets': [
                          'subnet-220c0e0a',
                          'subnet-1a95556d',
                          'subnet-978f6dce',
                      ],
                      'tags': {
                          'Name': 'Batch Instance - P2OnDemand',
                      },
                  },
                  'ecsClusterArn': 'arn:aws:ecs:us-east-1:012345678910:cluster/P2OnDemand_Batch_2c06f29d-d1fe-3a49-879d-42394c86effc',
                  'serviceRole': 'arn:aws:iam::012345678910:role/AWSBatchServiceRole',
                  'state': 'ENABLED',
                  'status': 'VALID',
                  'statusReason': 'ComputeEnvironment Healthy',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_job_definitions(**kwargs)

    

    Describes a list of job definitions. You can specify a ``status`` (such as ``ACTIVE`` ) to only return job definitions that match that status.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeJobDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.describe_job_definitions(
          jobDefinitions=[
              'string',
          ],
          maxResults=123,
          jobDefinitionName='string',
          status='string',
          nextToken='string'
      )
    :type jobDefinitions: list
    :param jobDefinitions: 

      A space-separated list of up to 100 job definition names or full Amazon Resource Name (ARN) entries.

      

    
      - *(string) --* 

      
  
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results returned by ``DescribeJobDefinitions`` in paginated output. When this parameter is used, ``DescribeJobDefinitions`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeJobDefinitions`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``DescribeJobDefinitions`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    :type jobDefinitionName: string
    :param jobDefinitionName: 

      The name of the job definition to describe.

      

    
    :type status: string
    :param status: 

      The status with which to filter job definitions.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``DescribeJobDefinitions`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobDefinitions': [
                {
                    'jobDefinitionName': 'string',
                    'jobDefinitionArn': 'string',
                    'revision': 123,
                    'status': 'string',
                    'type': 'string',
                    'parameters': {
                        'string': 'string'
                    },
                    'retryStrategy': {
                        'attempts': 123
                    },
                    'containerProperties': {
                        'image': 'string',
                        'vcpus': 123,
                        'memory': 123,
                        'command': [
                            'string',
                        ],
                        'jobRoleArn': 'string',
                        'volumes': [
                            {
                                'host': {
                                    'sourcePath': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'mountPoints': [
                            {
                                'containerPath': 'string',
                                'readOnly': True|False,
                                'sourceVolume': 'string'
                            },
                        ],
                        'readonlyRootFilesystem': True|False,
                        'privileged': True|False,
                        'ulimits': [
                            {
                                'hardLimit': 123,
                                'name': 'string',
                                'softLimit': 123
                            },
                        ],
                        'user': 'string'
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobDefinitions** *(list) --* 

          The list of job definitions. 

          
          

          - *(dict) --* 

            An object representing an AWS Batch job definition.

            
            

            - **jobDefinitionName** *(string) --* 

              The name of the job definition. 

              
            

            - **jobDefinitionArn** *(string) --* 

              The Amazon Resource Name (ARN) for the job definition. 

              
            

            - **revision** *(integer) --* 

              The revision of the job definition.

              
            

            - **status** *(string) --* 

              The status of the job definition.

              
            

            - **type** *(string) --* 

              The type of job definition.

              
            

            - **parameters** *(dict) --* 

              Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **retryStrategy** *(dict) --* 

              The retry strategy to use for failed jobs that are submitted with this job definition.

              
              

              - **attempts** *(integer) --* 

                The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried if it fails until it has moved to ``RUNNABLE`` that many times.

                
          
            

            - **containerProperties** *(dict) --* 

              An object with various properties specific to container-based jobs. 

              
              

              - **image** *(string) --* 

                The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                 
                * Images in Amazon ECR repositories use the full registry and repository URI (for example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).  
                 
                * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                 
                * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                 
                * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                 

                
              

              - **vcpus** *(integer) --* 

                The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

                
              

              - **memory** *(integer) --* 

                The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4 MiB of memory for a job.

                
              

              - **command** *(list) --* 

                The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

                
                

                - *(string) --* 
            
              

              - **jobRoleArn** *(string) --* 

                The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.

                
              

              - **volumes** *(list) --* 

                A list of data volumes used in a job.

                
                

                - *(dict) --* 

                  A data volume used in a job's container properties.

                  
                  

                  - **host** *(dict) --* 

                    The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.

                    
                    

                    - **sourcePath** *(string) --* 

                      The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

                      
                
                  

                  - **name** *(string) --* 

                    The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

                    
              
            
              

              - **environment** *(list) --* 

                The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                 

                .. warning::

                   

                  We do not recommend using plaintext environment variables for sensitive information, such as credential data.

                   

                 

                .. note::

                   

                  Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.

                   

                
                

                - *(dict) --* 

                  A key-value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key-value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key-value pair. For environment variables, this is the value of the environment variable.

                    
              
            
              

              - **mountPoints** *(list) --* 

                The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
                

                - *(dict) --* 

                  Details on a Docker volume mount point that is used in a job's container properties.

                  
                  

                  - **containerPath** *(string) --* 

                    The path on the container at which to mount the host volume.

                    
                  

                  - **readOnly** *(boolean) --* 

                    If this value is ``true`` , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is ``false`` .

                    
                  

                  - **sourceVolume** *(string) --* 

                    The name of the volume to mount.

                    
              
            
              

              - **readonlyRootFilesystem** *(boolean) --* 

                When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--read-only`` option to ``docker run`` .

                
              

              - **privileged** *(boolean) --* 

                When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
              

              - **ulimits** *(list) --* 

                A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
                

                - *(dict) --* 

                  The ``ulimit`` settings to pass to the container.

                  
                  

                  - **hardLimit** *(integer) --* 

                    The hard limit for the ``ulimit`` type.

                    
                  

                  - **name** *(string) --* 

                    The ``type`` of the ``ulimit`` .

                    
                  

                  - **softLimit** *(integer) --* 

                    The soft limit for the ``ulimit`` type.

                    
              
            
              

              - **user** *(string) --* 

                The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

                
          
        
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``DescribeJobDefinitions`` request. When the results of a ``DescribeJobDefinitions`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example describes all of your active job definitions.
    ::

      response = client.describe_job_definitions(
          status='ACTIVE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobDefinitions': [
              {
                  'type': 'container',
                  'containerProperties': {
                      'command': [
                          'sleep',
                          '60',
                      ],
                      'environment': [
                      ],
                      'image': 'busybox',
                      'memory': 128,
                      'mountPoints': [
                      ],
                      'ulimits': [
                      ],
                      'vcpus': 1,
                      'volumes': [
                      ],
                  },
                  'jobDefinitionArn': 'arn:aws:batch:us-east-1:012345678910:job-definition/sleep60:1',
                  'jobDefinitionName': 'sleep60',
                  'revision': 1,
                  'status': 'ACTIVE',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_job_queues(**kwargs)

    

    Describes one or more of your job queues.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeJobQueues>`_    


    **Request Syntax** 
    ::

      response = client.describe_job_queues(
          jobQueues=[
              'string',
          ],
          maxResults=123,
          nextToken='string'
      )
    :type jobQueues: list
    :param jobQueues: 

      A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.

      

    
      - *(string) --* 

      
  
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results returned by ``DescribeJobQueues`` in paginated output. When this parameter is used, ``DescribeJobQueues`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeJobQueues`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``DescribeJobQueues`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``DescribeJobQueues`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobQueues': [
                {
                    'jobQueueName': 'string',
                    'jobQueueArn': 'string',
                    'state': 'ENABLED'|'DISABLED',
                    'status': 'CREATING'|'UPDATING'|'DELETING'|'DELETED'|'VALID'|'INVALID',
                    'statusReason': 'string',
                    'priority': 123,
                    'computeEnvironmentOrder': [
                        {
                            'order': 123,
                            'computeEnvironment': 'string'
                        },
                    ]
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobQueues** *(list) --* 

          The list of job queues. 

          
          

          - *(dict) --* 

            An object representing the details of an AWS Batch job queue.

            
            

            - **jobQueueName** *(string) --* 

              The name of the job queue.

              
            

            - **jobQueueArn** *(string) --* 

              The Amazon Resource Name (ARN) of the job queue.

              
            

            - **state** *(string) --* 

              Describes the ability of the queue to accept new jobs.

              
            

            - **status** *(string) --* 

              The status of the job queue (for example, ``CREATING`` or ``VALID`` ).

              
            

            - **statusReason** *(string) --* 

              A short, human-readable string to provide additional details about the current status of the job queue.

              
            

            - **priority** *(integer) --* 

              The priority of the job queue. 

              
            

            - **computeEnvironmentOrder** *(list) --* 

              The compute environments that are attached to the job queue and the order in which job placement is preferred. Compute environments are selected for job placement in ascending order.

              
              

              - *(dict) --* 

                The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.

                
                

                - **order** *(integer) --* 

                  The order of the compute environment.

                  
                

                - **computeEnvironment** *(string) --* 

                  The Amazon Resource Name (ARN) of the compute environment.

                  
            
          
        
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``DescribeJobQueues`` request. When the results of a ``DescribeJobQueues`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example describes the HighPriority job queue.
    ::

      response = client.describe_job_queues(
          jobQueues=[
              'HighPriority',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobQueues': [
              {
                  'computeEnvironmentOrder': [
                      {
                          'computeEnvironment': 'arn:aws:batch:us-east-1:012345678910:compute-environment/C4OnDemand',
                          'order': 1,
                      },
                  ],
                  'jobQueueArn': 'arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority',
                  'jobQueueName': 'HighPriority',
                  'priority': 1,
                  'state': 'ENABLED',
                  'status': 'VALID',
                  'statusReason': 'JobQueue Healthy',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_jobs(**kwargs)

    

    Describes a list of AWS Batch jobs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeJobs>`_    


    **Request Syntax** 
    ::

      response = client.describe_jobs(
          jobs=[
              'string',
          ]
      )
    :type jobs: list
    :param jobs: **[REQUIRED]** 

      A space-separated list of up to 100 job IDs.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobs': [
                {
                    'jobName': 'string',
                    'jobId': 'string',
                    'jobQueue': 'string',
                    'status': 'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
                    'attempts': [
                        {
                            'container': {
                                'containerInstanceArn': 'string',
                                'taskArn': 'string',
                                'exitCode': 123,
                                'reason': 'string',
                                'logStreamName': 'string'
                            },
                            'startedAt': 123,
                            'stoppedAt': 123,
                            'statusReason': 'string'
                        },
                    ],
                    'statusReason': 'string',
                    'createdAt': 123,
                    'retryStrategy': {
                        'attempts': 123
                    },
                    'startedAt': 123,
                    'stoppedAt': 123,
                    'dependsOn': [
                        {
                            'jobId': 'string',
                            'type': 'N_TO_N'|'SEQUENTIAL'
                        },
                    ],
                    'jobDefinition': 'string',
                    'parameters': {
                        'string': 'string'
                    },
                    'container': {
                        'image': 'string',
                        'vcpus': 123,
                        'memory': 123,
                        'command': [
                            'string',
                        ],
                        'jobRoleArn': 'string',
                        'volumes': [
                            {
                                'host': {
                                    'sourcePath': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'mountPoints': [
                            {
                                'containerPath': 'string',
                                'readOnly': True|False,
                                'sourceVolume': 'string'
                            },
                        ],
                        'readonlyRootFilesystem': True|False,
                        'ulimits': [
                            {
                                'hardLimit': 123,
                                'name': 'string',
                                'softLimit': 123
                            },
                        ],
                        'privileged': True|False,
                        'user': 'string',
                        'exitCode': 123,
                        'reason': 'string',
                        'containerInstanceArn': 'string',
                        'taskArn': 'string',
                        'logStreamName': 'string'
                    },
                    'arrayProperties': {
                        'statusSummary': {
                            'string': 123
                        },
                        'size': 123,
                        'index': 123
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobs** *(list) --* 

          The list of jobs. 

          
          

          - *(dict) --* 

            An object representing an AWS Batch job.

            
            

            - **jobName** *(string) --* 

              The name of the job.

              
            

            - **jobId** *(string) --* 

              The ID for the job.

              
            

            - **jobQueue** *(string) --* 

              The Amazon Resource Name (ARN) of the job queue with which the job is associated.

              
            

            - **status** *(string) --* 

              The current status for the job.

              
            

            - **attempts** *(list) --* 

              A list of job attempts associated with this job.

              
              

              - *(dict) --* 

                An object representing a job attempt.

                
                

                - **container** *(dict) --* 

                  Details about the container in this job attempt.

                  
                  

                  - **containerInstanceArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the job attempt.

                    
                  

                  - **taskArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the job attempt. Each container attempt receives a task ARN when they reach the ``STARTING`` status.

                    
                  

                  - **exitCode** *(integer) --* 

                    The exit code for the job attempt. A non-zero exit code is considered a failure.

                    
                  

                  - **reason** *(string) --* 

                    A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

                    
                  

                  - **logStreamName** *(string) --* 

                    The name of the CloudWatch Logs log stream associated with the container. The log group for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a log stream name when they reach the ``RUNNING`` status.

                    
              
                

                - **startedAt** *(integer) --* 

                  The Unix time stamp for when the attempt was started (when the attempt transitioned from the ``STARTING`` state to the ``RUNNING`` state).

                  
                

                - **stoppedAt** *(integer) --* 

                  The Unix time stamp for when the attempt was stopped (when the attempt transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).

                  
                

                - **statusReason** *(string) --* 

                  A short, human-readable string to provide additional details about the current status of the job attempt.

                  
            
          
            

            - **statusReason** *(string) --* 

              A short, human-readable string to provide additional details about the current status of the job. 

              
            

            - **createdAt** *(integer) --* 

              The Unix time stamp for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was called). For array child jobs, this is when the child job was spawned by its parent and entered the ``PENDING`` state.

              
            

            - **retryStrategy** *(dict) --* 

              The retry strategy to use for this job if an attempt fails.

              
              

              - **attempts** *(integer) --* 

                The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried if it fails until it has moved to ``RUNNABLE`` that many times.

                
          
            

            - **startedAt** *(integer) --* 

              The Unix time stamp for when the job was started (when the job transitioned from the ``STARTING`` state to the ``RUNNING`` state).

              
            

            - **stoppedAt** *(integer) --* 

              The Unix time stamp for when the job was stopped (when the job transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).

              
            

            - **dependsOn** *(list) --* 

              A list of job names or IDs on which this job depends.

              
              

              - *(dict) --* 

                An object representing an AWS Batch job dependency.

                
                

                - **jobId** *(string) --* 

                  The job ID of the AWS Batch job associated with this dependency.

                  
                

                - **type** *(string) --* 

                  The type of the job dependency.

                  
            
          
            

            - **jobDefinition** *(string) --* 

              The job definition that is used by this job.

              
            

            - **parameters** *(dict) --* 

              Additional parameters passed to the job that replace parameter substitution placeholders or override any corresponding parameter defaults from the job definition. 

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **container** *(dict) --* 

              An object representing the details of the container that is associated with the job.

              
              

              - **image** *(string) --* 

                The image used to start the container.

                
              

              - **vcpus** *(integer) --* 

                The number of VCPUs allocated for the job. 

                
              

              - **memory** *(integer) --* 

                The number of MiB of memory reserved for the job.

                
              

              - **command** *(list) --* 

                The command that is passed to the container. 

                
                

                - *(string) --* 
            
              

              - **jobRoleArn** *(string) --* 

                The Amazon Resource Name (ARN) associated with the job upon execution. 

                
              

              - **volumes** *(list) --* 

                A list of volumes associated with the job.

                
                

                - *(dict) --* 

                  A data volume used in a job's container properties.

                  
                  

                  - **host** *(dict) --* 

                    The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.

                    
                    

                    - **sourcePath** *(string) --* 

                      The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

                      
                
                  

                  - **name** *(string) --* 

                    The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

                    
              
            
              

              - **environment** *(list) --* 

                The environment variables to pass to a container.

                 

                .. note::

                   

                  Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.

                   

                
                

                - *(dict) --* 

                  A key-value pair object.

                  
                  

                  - **name** *(string) --* 

                    The name of the key-value pair. For environment variables, this is the name of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the key-value pair. For environment variables, this is the value of the environment variable.

                    
              
            
              

              - **mountPoints** *(list) --* 

                The mount points for data volumes in your container.

                
                

                - *(dict) --* 

                  Details on a Docker volume mount point that is used in a job's container properties.

                  
                  

                  - **containerPath** *(string) --* 

                    The path on the container at which to mount the host volume.

                    
                  

                  - **readOnly** *(boolean) --* 

                    If this value is ``true`` , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is ``false`` .

                    
                  

                  - **sourceVolume** *(string) --* 

                    The name of the volume to mount.

                    
              
            
              

              - **readonlyRootFilesystem** *(boolean) --* 

                When this parameter is true, the container is given read-only access to its root file system.

                
              

              - **ulimits** *(list) --* 

                A list of ``ulimit`` values to set in the container.

                
                

                - *(dict) --* 

                  The ``ulimit`` settings to pass to the container.

                  
                  

                  - **hardLimit** *(integer) --* 

                    The hard limit for the ``ulimit`` type.

                    
                  

                  - **name** *(string) --* 

                    The ``type`` of the ``ulimit`` .

                    
                  

                  - **softLimit** *(integer) --* 

                    The soft limit for the ``ulimit`` type.

                    
              
            
              

              - **privileged** *(boolean) --* 

                When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user).

                
              

              - **user** *(string) --* 

                The user name to use inside the container.

                
              

              - **exitCode** *(integer) --* 

                The exit code to return upon completion.

                
              

              - **reason** *(string) --* 

                A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

                
              

              - **containerInstanceArn** *(string) --* 

                The Amazon Resource Name (ARN) of the container instance on which the container is running.

                
              

              - **taskArn** *(string) --* 

                The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the container job. Each container attempt receives a task ARN when they reach the ``STARTING`` status.

                
              

              - **logStreamName** *(string) --* 

                The name of the CloudWatch Logs log stream associated with the container. The log group for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a log stream name when they reach the ``RUNNING`` status.

                
          
            

            - **arrayProperties** *(dict) --* 

              The array properties of the job, if it is an array job.

              
              

              - **statusSummary** *(dict) --* 

                A summary of the number of array job children in each available job status. This parameter is returned for parent array jobs.

                
                

                - *(string) --* 
                  

                  - *(integer) --* 
            
          
              

              - **size** *(integer) --* 

                The size of the array job. This parameter is returned for parent array jobs.

                
              

              - **index** *(integer) --* 

                The job index within the array that is associated with this job. This parameter is returned for array job children.

                
          
        
      
    

    **Examples** 

    This example describes a job with the specified job ID.
    ::

      response = client.describe_jobs(
          jobs=[
              '24fa2d7a-64c4-49d2-8b47-f8da4fbde8e9',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobs': [
              {
                  'container': {
                      'command': [
                          'sleep',
                          '60',
                      ],
                      'containerInstanceArn': 'arn:aws:ecs:us-east-1:012345678910:container-instance/5406d7cd-58bd-4b8f-9936-48d7c6b1526c',
                      'environment': [
                      ],
                      'exitCode': 0,
                      'image': 'busybox',
                      'memory': 128,
                      'mountPoints': [
                      ],
                      'ulimits': [
                      ],
                      'vcpus': 1,
                      'volumes': [
                      ],
                  },
                  'createdAt': 1480460782010,
                  'dependsOn': [
                  ],
                  'jobDefinition': 'sleep60',
                  'jobId': '24fa2d7a-64c4-49d2-8b47-f8da4fbde8e9',
                  'jobName': 'example',
                  'jobQueue': 'arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority',
                  'parameters': {
                  },
                  'startedAt': 1480460816500,
                  'status': 'SUCCEEDED',
                  'stoppedAt': 1480460880699,
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

        


  .. py:method:: list_jobs(**kwargs)

    

    Returns a list of task jobs for a specified job queue. You can filter the results by job status with the ``jobStatus`` parameter. If you do not specify a status, only ``RUNNING`` jobs are returned.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/ListJobs>`_    


    **Request Syntax** 
    ::

      response = client.list_jobs(
          jobQueue='string',
          arrayJobId='string',
          jobStatus='SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
          maxResults=123,
          nextToken='string'
      )
    :type jobQueue: string
    :param jobQueue: 

      The name or full Amazon Resource Name (ARN) of the job queue with which to list jobs.

      

    
    :type arrayJobId: string
    :param arrayJobId: 

      The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.

      

    
    :type jobStatus: string
    :param jobStatus: 

      The job status with which to filter jobs in the specified queue. If you do not specify a status, only ``RUNNING`` jobs are returned.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results returned by ``ListJobs`` in paginated output. When this parameter is used, ``ListJobs`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListJobs`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListJobs`` returns up to 100 results and a ``nextToken`` value if applicable.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``ListJobs`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.

       

      .. note::

         

        This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobSummaryList': [
                {
                    'jobId': 'string',
                    'jobName': 'string',
                    'createdAt': 123,
                    'status': 'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
                    'statusReason': 'string',
                    'startedAt': 123,
                    'stoppedAt': 123,
                    'container': {
                        'exitCode': 123,
                        'reason': 'string'
                    },
                    'arrayProperties': {
                        'size': 123,
                        'index': 123
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobSummaryList** *(list) --* 

          A list of job summaries that match the request.

          
          

          - *(dict) --* 

            An object representing summary details of a job.

            
            

            - **jobId** *(string) --* 

              The ID of the job.

              
            

            - **jobName** *(string) --* 

              The name of the job.

              
            

            - **createdAt** *(integer) --* 

              The Unix time stamp for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was called). For array child jobs, this is when the child job was spawned by its parent and entered the ``PENDING`` state.

              
            

            - **status** *(string) --* 

              The current status for the job.

              
            

            - **statusReason** *(string) --* 

              A short, human-readable string to provide additional details about the current status of the job.

              
            

            - **startedAt** *(integer) --* 

              The Unix time stamp for when the job was started (when the job transitioned from the ``STARTING`` state to the ``RUNNING`` state).

              
            

            - **stoppedAt** *(integer) --* 

              The Unix time stamp for when the job was stopped (when the job transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).

              
            

            - **container** *(dict) --* 

              An object representing the details of the container that is associated with the job.

              
              

              - **exitCode** *(integer) --* 

                The exit code to return upon completion.

                
              

              - **reason** *(string) --* 

                A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

                
          
            

            - **arrayProperties** *(dict) --* 

              The array properties of the job, if it is an array job.

              
              

              - **size** *(integer) --* 

                The size of the array job. This parameter is returned for parent array jobs.

                
              

              - **index** *(integer) --* 

                The job index within the array that is associated with this job. This parameter is returned for children of array jobs.

                
          
        
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``ListJobs`` request. When the results of a ``ListJobs`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

    **Examples** 

    This example lists the running jobs in the HighPriority job queue.
    ::

      response = client.list_jobs(
          jobQueue='HighPriority',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobSummaryList': [
              {
                  'jobId': 'e66ff5fd-a1ff-4640-b1a2-0b0a142f49bb',
                  'jobName': 'example',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.
    ::

      response = client.list_jobs(
          jobQueue='HighPriority',
          jobStatus='SUBMITTED',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobSummaryList': [
              {
                  'jobId': '68f0c163-fbd4-44e6-9fd1-25b14a434786',
                  'jobName': 'example',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: register_job_definition(**kwargs)

    

    Registers an AWS Batch job definition. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/RegisterJobDefinition>`_    


    **Request Syntax** 
    ::

      response = client.register_job_definition(
          jobDefinitionName='string',
          type='container',
          parameters={
              'string': 'string'
          },
          containerProperties={
              'image': 'string',
              'vcpus': 123,
              'memory': 123,
              'command': [
                  'string',
              ],
              'jobRoleArn': 'string',
              'volumes': [
                  {
                      'host': {
                          'sourcePath': 'string'
                      },
                      'name': 'string'
                  },
              ],
              'environment': [
                  {
                      'name': 'string',
                      'value': 'string'
                  },
              ],
              'mountPoints': [
                  {
                      'containerPath': 'string',
                      'readOnly': True|False,
                      'sourceVolume': 'string'
                  },
              ],
              'readonlyRootFilesystem': True|False,
              'privileged': True|False,
              'ulimits': [
                  {
                      'hardLimit': 123,
                      'name': 'string',
                      'softLimit': 123
                  },
              ],
              'user': 'string'
          },
          retryStrategy={
              'attempts': 123
          }
      )
    :type jobDefinitionName: string
    :param jobDefinitionName: **[REQUIRED]** 

      The name of the job definition to register. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      The type of job definition.

      

    
    :type parameters: dict
    :param parameters: 

      Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type containerProperties: dict
    :param containerProperties: 

      An object with various properties specific for container-based jobs. This parameter is required if the ``type`` parameter is ``container`` .

      

    
      - **image** *(string) --* **[REQUIRED]** 

        The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

         

         
        * Images in Amazon ECR repositories use the full registry and repository URI (for example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).  
         
        * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
         
        * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
         
        * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
         

        

      
      - **vcpus** *(integer) --* **[REQUIRED]** 

        The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

        

      
      - **memory** *(integer) --* **[REQUIRED]** 

        The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4 MiB of memory for a job.

        

      
      - **command** *(list) --* 

        The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

        

      
        - *(string) --* 

        
    
      - **jobRoleArn** *(string) --* 

        The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.

        

      
      - **volumes** *(list) --* 

        A list of data volumes used in a job.

        

      
        - *(dict) --* 

          A data volume used in a job's container properties.

          

        
          - **host** *(dict) --* 

            The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.

            

          
            - **sourcePath** *(string) --* 

              The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

              

            
          
          - **name** *(string) --* 

            The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

            

          
        
    
      - **environment** *(list) --* 

        The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

         

        .. warning::

           

          We do not recommend using plaintext environment variables for sensitive information, such as credential data.

           

         

        .. note::

           

          Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.

           

        

      
        - *(dict) --* 

          A key-value pair object.

          

        
          - **name** *(string) --* 

            The name of the key-value pair. For environment variables, this is the name of the environment variable.

            

          
          - **value** *(string) --* 

            The value of the key-value pair. For environment variables, this is the value of the environment variable.

            

          
        
    
      - **mountPoints** *(list) --* 

        The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        

      
        - *(dict) --* 

          Details on a Docker volume mount point that is used in a job's container properties.

          

        
          - **containerPath** *(string) --* 

            The path on the container at which to mount the host volume.

            

          
          - **readOnly** *(boolean) --* 

            If this value is ``true`` , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is ``false`` .

            

          
          - **sourceVolume** *(string) --* 

            The name of the volume to mount.

            

          
        
    
      - **readonlyRootFilesystem** *(boolean) --* 

        When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--read-only`` option to ``docker run`` .

        

      
      - **privileged** *(boolean) --* 

        When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        

      
      - **ulimits** *(list) --* 

        A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        

      
        - *(dict) --* 

          The ``ulimit`` settings to pass to the container.

          

        
          - **hardLimit** *(integer) --* **[REQUIRED]** 

            The hard limit for the ``ulimit`` type.

            

          
          - **name** *(string) --* **[REQUIRED]** 

            The ``type`` of the ``ulimit`` .

            

          
          - **softLimit** *(integer) --* **[REQUIRED]** 

            The soft limit for the ``ulimit`` type.

            

          
        
    
      - **user** *(string) --* 

        The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        

      
    
    :type retryStrategy: dict
    :param retryStrategy: 

      The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy that is specified during a  SubmitJob operation overrides the retry strategy defined here.

      

    
      - **attempts** *(integer) --* 

        The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried if it fails until it has moved to ``RUNNABLE`` that many times.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobDefinitionName': 'string',
            'jobDefinitionArn': 'string',
            'revision': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobDefinitionName** *(string) --* 

          The name of the job definition.

          
        

        - **jobDefinitionArn** *(string) --* 

          The Amazon Resource Name (ARN) of the job definition. 

          
        

        - **revision** *(integer) --* 

          The revision of the job definition.

          
    

    **Examples** 

    This example registers a job definition for a simple container job.
    ::

      response = client.register_job_definition(
          type='container',
          containerProperties={
              'command': [
                  'sleep',
                  '10',
              ],
              'image': 'busybox',
              'memory': 128,
              'vcpus': 1,
          },
          jobDefinitionName='sleep10',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobDefinitionArn': 'arn:aws:batch:us-east-1:012345678910:job-definition/sleep10:1',
          'jobDefinitionName': 'sleep10',
          'revision': 1,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: submit_job(**kwargs)

    

    Submits an AWS Batch job from a job definition. Parameters specified during  SubmitJob override parameters defined in the job definition. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/SubmitJob>`_    


    **Request Syntax** 
    ::

      response = client.submit_job(
          jobName='string',
          jobQueue='string',
          arrayProperties={
              'size': 123
          },
          dependsOn=[
              {
                  'jobId': 'string',
                  'type': 'N_TO_N'|'SEQUENTIAL'
              },
          ],
          jobDefinition='string',
          parameters={
              'string': 'string'
          },
          containerOverrides={
              'vcpus': 123,
              'memory': 123,
              'command': [
                  'string',
              ],
              'environment': [
                  {
                      'name': 'string',
                      'value': 'string'
                  },
              ]
          },
          retryStrategy={
              'attempts': 123
          }
      )
    :type jobName: string
    :param jobName: **[REQUIRED]** 

      The name of the job. The first character must be alphanumeric, and up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. 

      

    
    :type jobQueue: string
    :param jobQueue: **[REQUIRED]** 

      The job queue into which the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue. 

      

    
    :type arrayProperties: dict
    :param arrayProperties: 

      The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For more information, see `Array Jobs <http://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html>`__ in the *AWS Batch User Guide* .

      

    
      - **size** *(integer) --* 

        The size of the array job.

        

      
    
    :type dependsOn: list
    :param dependsOn: 

      A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a ``SEQUENTIAL`` type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an ``N_TO_N`` type dependency with a job ID for array jobs so that each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.

      

    
      - *(dict) --* 

        An object representing an AWS Batch job dependency.

        

      
        - **jobId** *(string) --* 

          The job ID of the AWS Batch job associated with this dependency.

          

        
        - **type** *(string) --* 

          The type of the job dependency.

          

        
      
  
    :type jobDefinition: string
    :param jobDefinition: **[REQUIRED]** 

      The job definition used by this job. This value can be either a ``name:revision`` or the Amazon Resource Name (ARN) for the job definition.

      

    
    :type parameters: dict
    :param parameters: 

      Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type containerOverrides: dict
    :param containerOverrides: 

      A list of container overrides in JSON format that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container (that is specified in the job definition or the Docker image) with a ``command`` override. You can also override existing environment variables (that are specified in the job definition or Docker image) on a container or add new environment variables to it with an ``environment`` override.

      

    
      - **vcpus** *(integer) --* 

        The number of vCPUs to reserve for the container. This value overrides the value set in the job definition.

        

      
      - **memory** *(integer) --* 

        The number of MiB of memory reserved for the job. This value overrides the value set in the job definition.

        

      
      - **command** *(list) --* 

        The command to send to the container that overrides the default command from the Docker image or the job definition.

        

      
        - *(string) --* 

        
    
      - **environment** *(list) --* 

        The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.

         

        .. note::

           

          Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.

           

        

      
        - *(dict) --* 

          A key-value pair object.

          

        
          - **name** *(string) --* 

            The name of the key-value pair. For environment variables, this is the name of the environment variable.

            

          
          - **value** *(string) --* 

            The value of the key-value pair. For environment variables, this is the value of the environment variable.

            

          
        
    
    
    :type retryStrategy: dict
    :param retryStrategy: 

      The retry strategy to use for failed jobs from this  SubmitJob operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.

      

    
      - **attempts** *(integer) --* 

        The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried if it fails until it has moved to ``RUNNABLE`` that many times.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobName': 'string',
            'jobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobName** *(string) --* 

          The name of the job. 

          
        

        - **jobId** *(string) --* 

          The unique identifier for the job.

          
    

    **Examples** 

    This example submits a simple container job called example to the HighPriority job queue.
    ::

      response = client.submit_job(
          jobDefinition='sleep60',
          jobName='example',
          jobQueue='HighPriority',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobId': '876da822-4198-45f2-a252-6cea32512ea8',
          'jobName': 'example',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: terminate_job(**kwargs)

    

    Terminates a job in a job queue. Jobs that are in the ``STARTING`` or ``RUNNING`` state are terminated, which causes them to transition to ``FAILED`` . Jobs that have not progressed to the ``STARTING`` state are cancelled.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/TerminateJob>`_    


    **Request Syntax** 
    ::

      response = client.terminate_job(
          jobId='string',
          reason='string'
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The AWS Batch job ID of the job to terminate.

      

    
    :type reason: string
    :param reason: **[REQUIRED]** 

      A message to attach to the job that explains the reason for canceling it. This message is returned by future  DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example terminates a job with the specified job ID.
    ::

      response = client.terminate_job(
          jobId='61e743ed-35e4-48da-b2de-5c8333821c84',
          reason='Terminating job.',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_compute_environment(**kwargs)

    

    Updates an AWS Batch compute environment.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/UpdateComputeEnvironment>`_    


    **Request Syntax** 
    ::

      response = client.update_compute_environment(
          computeEnvironment='string',
          state='ENABLED'|'DISABLED',
          computeResources={
              'minvCpus': 123,
              'maxvCpus': 123,
              'desiredvCpus': 123
          },
          serviceRole='string'
      )
    :type computeEnvironment: string
    :param computeEnvironment: **[REQUIRED]** 

      The name or full Amazon Resource Name (ARN) of the compute environment to update.

      

    
    :type state: string
    :param state: 

      The state of the compute environment. Compute environments in the ``ENABLED`` state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.

      

    
    :type computeResources: dict
    :param computeResources: 

      Details of the compute resources managed by the compute environment. Required for a managed compute environment.

      

    
      - **minvCpus** *(integer) --* 

        The minimum number of EC2 vCPUs that an environment should maintain.

        

      
      - **maxvCpus** *(integer) --* 

        The maximum number of EC2 vCPUs that an environment can reach.

        

      
      - **desiredvCpus** *(integer) --* 

        The desired number of EC2 vCPUS in the compute environment.

        

      
    
    :type serviceRole: string
    :param serviceRole: 

      The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

       

      If your specified role has a path other than ``/`` , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.

       

      .. note::

         

        Depending on how you created your AWS Batch service role, its ARN may contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'computeEnvironmentName': 'string',
            'computeEnvironmentArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **computeEnvironmentName** *(string) --* 

          The name of compute environment.

          
        

        - **computeEnvironmentArn** *(string) --* 

          The Amazon Resource Name (ARN) of the compute environment. 

          
    

    **Examples** 

    This example disables the P2OnDemand compute environment so it can be deleted.
    ::

      response = client.update_compute_environment(
          computeEnvironment='P2OnDemand',
          state='DISABLED',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'computeEnvironmentArn': 'arn:aws:batch:us-east-1:012345678910:compute-environment/P2OnDemand',
          'computeEnvironmentName': 'P2OnDemand',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_job_queue(**kwargs)

    

    Updates a job queue.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/UpdateJobQueue>`_    


    **Request Syntax** 
    ::

      response = client.update_job_queue(
          jobQueue='string',
          state='ENABLED'|'DISABLED',
          priority=123,
          computeEnvironmentOrder=[
              {
                  'order': 123,
                  'computeEnvironment': 'string'
              },
          ]
      )
    :type jobQueue: string
    :param jobQueue: **[REQUIRED]** 

      The name or the Amazon Resource Name (ARN) of the job queue.

      

    
    :type state: string
    :param state: 

      Describes the queue's ability to accept new jobs.

      

    
    :type priority: integer
    :param priority: 

      The priority of the job queue. Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with same compute environment. Priority is determined in descending order, for example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` .

      

    
    :type computeEnvironmentOrder: list
    :param computeEnvironmentOrder: 

      Details the set of compute environments mapped to a job queue and their order relative to each other. This is one of the parameters used by the job scheduler to determine which compute environment should execute a given job. 

      

    
      - *(dict) --* 

        The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.

        

      
        - **order** *(integer) --* **[REQUIRED]** 

          The order of the compute environment.

          

        
        - **computeEnvironment** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the compute environment.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobQueueName': 'string',
            'jobQueueArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobQueueName** *(string) --* 

          The name of the job queue.

          
        

        - **jobQueueArn** *(string) --* 

          The Amazon Resource Name (ARN) of the job queue.

          
    

    **Examples** 

    This example disables a job queue so that it can be deleted.
    ::

      response = client.update_job_queue(
          jobQueue='GPGPU',
          state='DISABLED',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobQueueArn': 'arn:aws:batch:us-east-1:012345678910:job-queue/GPGPU',
          'jobQueueName': 'GPGPU',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:
