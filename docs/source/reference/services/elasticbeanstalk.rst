

****************
ElasticBeanstalk
****************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ElasticBeanstalk.Client

  A low-level client representing AWS Elastic Beanstalk::

    
    import boto3
    
    client = boto3.client('elasticbeanstalk')

  
  These are the available methods:
  
  *   :py:meth:`~ElasticBeanstalk.Client.abort_environment_update`

  
  *   :py:meth:`~ElasticBeanstalk.Client.apply_environment_managed_action`

  
  *   :py:meth:`~ElasticBeanstalk.Client.can_paginate`

  
  *   :py:meth:`~ElasticBeanstalk.Client.check_dns_availability`

  
  *   :py:meth:`~ElasticBeanstalk.Client.compose_environments`

  
  *   :py:meth:`~ElasticBeanstalk.Client.create_application`

  
  *   :py:meth:`~ElasticBeanstalk.Client.create_application_version`

  
  *   :py:meth:`~ElasticBeanstalk.Client.create_configuration_template`

  
  *   :py:meth:`~ElasticBeanstalk.Client.create_environment`

  
  *   :py:meth:`~ElasticBeanstalk.Client.create_platform_version`

  
  *   :py:meth:`~ElasticBeanstalk.Client.create_storage_location`

  
  *   :py:meth:`~ElasticBeanstalk.Client.delete_application`

  
  *   :py:meth:`~ElasticBeanstalk.Client.delete_application_version`

  
  *   :py:meth:`~ElasticBeanstalk.Client.delete_configuration_template`

  
  *   :py:meth:`~ElasticBeanstalk.Client.delete_environment_configuration`

  
  *   :py:meth:`~ElasticBeanstalk.Client.delete_platform_version`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_application_versions`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_applications`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_configuration_options`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_configuration_settings`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_environment_health`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_environment_managed_action_history`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_environment_managed_actions`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_environment_resources`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_environments`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_events`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_instances_health`

  
  *   :py:meth:`~ElasticBeanstalk.Client.describe_platform_version`

  
  *   :py:meth:`~ElasticBeanstalk.Client.generate_presigned_url`

  
  *   :py:meth:`~ElasticBeanstalk.Client.get_paginator`

  
  *   :py:meth:`~ElasticBeanstalk.Client.get_waiter`

  
  *   :py:meth:`~ElasticBeanstalk.Client.list_available_solution_stacks`

  
  *   :py:meth:`~ElasticBeanstalk.Client.list_platform_versions`

  
  *   :py:meth:`~ElasticBeanstalk.Client.list_tags_for_resource`

  
  *   :py:meth:`~ElasticBeanstalk.Client.rebuild_environment`

  
  *   :py:meth:`~ElasticBeanstalk.Client.request_environment_info`

  
  *   :py:meth:`~ElasticBeanstalk.Client.restart_app_server`

  
  *   :py:meth:`~ElasticBeanstalk.Client.retrieve_environment_info`

  
  *   :py:meth:`~ElasticBeanstalk.Client.swap_environment_cnames`

  
  *   :py:meth:`~ElasticBeanstalk.Client.terminate_environment`

  
  *   :py:meth:`~ElasticBeanstalk.Client.update_application`

  
  *   :py:meth:`~ElasticBeanstalk.Client.update_application_resource_lifecycle`

  
  *   :py:meth:`~ElasticBeanstalk.Client.update_application_version`

  
  *   :py:meth:`~ElasticBeanstalk.Client.update_configuration_template`

  
  *   :py:meth:`~ElasticBeanstalk.Client.update_environment`

  
  *   :py:meth:`~ElasticBeanstalk.Client.update_tags_for_resource`

  
  *   :py:meth:`~ElasticBeanstalk.Client.validate_configuration_settings`

  

  .. py:method:: abort_environment_update(**kwargs)

    

    Cancels in-progress environment configuration update or application version deployment.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/AbortEnvironmentUpdate>`_    


    **Request Syntax** 
    ::

      response = client.abort_environment_update(
          EnvironmentId='string',
          EnvironmentName='string'
      )
    :type EnvironmentId: string
    :param EnvironmentId: 

      This specifies the ID of the environment with the in-progress update that you want to cancel.

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      This specifies the name of the environment with the in-progress update that you want to cancel.

      

    
    
    :returns: None

    **Examples** 

    The following code aborts a running application version deployment for an environment named my-env:
    ::

      response = client.abort_environment_update(
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: apply_environment_managed_action(**kwargs)

    

    Applies a scheduled managed action immediately. A managed action can be applied only if its status is ``Scheduled`` . Get the status and action ID of a managed action with  DescribeEnvironmentManagedActions .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction>`_    


    **Request Syntax** 
    ::

      response = client.apply_environment_managed_action(
          EnvironmentName='string',
          EnvironmentId='string',
          ActionId='string'
      )
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the target environment.

      

    
    :type EnvironmentId: string
    :param EnvironmentId: 

      The environment ID of the target environment.

      

    
    :type ActionId: string
    :param ActionId: **[REQUIRED]** 

      The action ID of the scheduled managed action to execute.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ActionId': 'string',
            'ActionDescription': 'string',
            'ActionType': 'InstanceRefresh'|'PlatformUpdate'|'Unknown',
            'Status': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result message containing information about the managed action.

        
        

        - **ActionId** *(string) --* 

          The action ID of the managed action.

          
        

        - **ActionDescription** *(string) --* 

          A description of the managed action.

          
        

        - **ActionType** *(string) --* 

          The type of managed action.

          
        

        - **Status** *(string) --* 

          The status of the managed action.

          
    

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


  .. py:method:: check_dns_availability(**kwargs)

    

    Checks if the specified CNAME is available.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CheckDNSAvailability>`_    


    **Request Syntax** 
    ::

      response = client.check_dns_availability(
          CNAMEPrefix='string'
      )
    :type CNAMEPrefix: string
    :param CNAMEPrefix: **[REQUIRED]** 

      The prefix used when this CNAME is reserved.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Available': True|False,
            'FullyQualifiedCNAME': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Indicates if the specified CNAME is available.

        
        

        - **Available** *(boolean) --* 

          Indicates if the specified CNAME is available:

           

           
          * ``true`` : The CNAME is available. 
           
          * ``false`` : The CNAME is not available. 
           

          
        

        - **FullyQualifiedCNAME** *(string) --* 

          The fully qualified CNAME to reserve when  CreateEnvironment is called with the provided prefix.

          
    

    **Examples** 

    The following operation checks the availability of the subdomain my-cname:
    ::

      response = client.check_dns_availability(
          CNAMEPrefix='my-cname',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Available': True,
          'FullyQualifiedCNAME': 'my-cname.us-west-2.elasticbeanstalk.com',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: compose_environments(**kwargs)

    

    Create or update a group of environments that each run a separate component of a single application. Takes a list of version labels that specify application source bundles for each of the environments to create or update. The name of each environment and other required information must be included in the source bundles in an environment manifest named ``env.yaml`` . See `Compose Environments <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-mgmt-compose.html>`__ for details.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ComposeEnvironments>`_    


    **Request Syntax** 
    ::

      response = client.compose_environments(
          ApplicationName='string',
          GroupName='string',
          VersionLabels=[
              'string',
          ]
      )
    :type ApplicationName: string
    :param ApplicationName: 

      The name of the application to which the specified source bundles belong.

      

    
    :type GroupName: string
    :param GroupName: 

      The name of the group to which the target environments belong. Specify a group name only if the environment name defined in each target environment's manifest ends with a + (plus) character. See `Environment Manifest (env.yaml) <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.

      

    
    :type VersionLabels: list
    :param VersionLabels: 

      A list of version labels, specifying one or more application source bundles that belong to the target application. Each source bundle must include an environment manifest that specifies the name of the environment and the name of the solution stack to use, and optionally can specify environment links to create.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Environments': [
                {
                    'EnvironmentName': 'string',
                    'EnvironmentId': 'string',
                    'ApplicationName': 'string',
                    'VersionLabel': 'string',
                    'SolutionStackName': 'string',
                    'PlatformArn': 'string',
                    'TemplateName': 'string',
                    'Description': 'string',
                    'EndpointURL': 'string',
                    'CNAME': 'string',
                    'DateCreated': datetime(2015, 1, 1),
                    'DateUpdated': datetime(2015, 1, 1),
                    'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
                    'AbortableOperationInProgress': True|False,
                    'Health': 'Green'|'Yellow'|'Red'|'Grey',
                    'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
                    'Resources': {
                        'LoadBalancer': {
                            'LoadBalancerName': 'string',
                            'Domain': 'string',
                            'Listeners': [
                                {
                                    'Protocol': 'string',
                                    'Port': 123
                                },
                            ]
                        }
                    },
                    'Tier': {
                        'Name': 'string',
                        'Type': 'string',
                        'Version': 'string'
                    },
                    'EnvironmentLinks': [
                        {
                            'LinkName': 'string',
                            'EnvironmentName': 'string'
                        },
                    ],
                    'EnvironmentArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message containing a list of environment descriptions.

        
        

        - **Environments** *(list) --* 

          Returns an  EnvironmentDescription list. 

          
          

          - *(dict) --* 

            Describes the properties of an environment.

            
            

            - **EnvironmentName** *(string) --* 

              The name of this environment.

              
            

            - **EnvironmentId** *(string) --* 

              The ID of this environment.

              
            

            - **ApplicationName** *(string) --* 

              The name of the application associated with this environment.

              
            

            - **VersionLabel** *(string) --* 

              The application version deployed in this environment.

              
            

            - **SolutionStackName** *(string) --* 

              The name of the ``SolutionStack`` deployed with this environment. 

              
            

            - **PlatformArn** *(string) --* 

              The ARN of the platform.

              
            

            - **TemplateName** *(string) --* 

              The name of the configuration template used to originally launch this environment.

              
            

            - **Description** *(string) --* 

              Describes this environment.

              
            

            - **EndpointURL** *(string) --* 

              For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.

              
            

            - **CNAME** *(string) --* 

              The URL to the CNAME for this environment.

              
            

            - **DateCreated** *(datetime) --* 

              The creation date for this environment.

              
            

            - **DateUpdated** *(datetime) --* 

              The last modified date for this environment.

              
            

            - **Status** *(string) --* 

              The current operational status of the environment:

               

               
              * ``Launching`` : Environment is in the process of initial deployment. 
               
              * ``Updating`` : Environment is in the process of updating its configuration settings or application version. 
               
              * ``Ready`` : Environment is available to have an action performed on it, such as update or terminate. 
               
              * ``Terminating`` : Environment is in the shut-down process. 
               
              * ``Terminated`` : Environment is not running. 
               

              
            

            - **AbortableOperationInProgress** *(boolean) --* 

              Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.

               

               ``true:`` There is an update in progress. 

               

               ``false:`` There are no updates currently in progress. 

              
            

            - **Health** *(string) --* 

              Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:

               

               
              * ``Red`` : Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment. 
               
              * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur for an environment. 
               
              * ``Green`` : Indicates the environment is healthy and fully functional. 
               
              * ``Grey`` : Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an ``UpdateEnvironment`` or ``RestartEnvironement`` request. 
               

               

              Default: ``Grey``  

              
            

            - **HealthStatus** *(string) --* 

              Returns the health status of the application running in your environment. For more information, see `Health Colors and Statuses <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

              
            

            - **Resources** *(dict) --* 

              The description of the AWS resources used by this environment.

              
              

              - **LoadBalancer** *(dict) --* 

                Describes the LoadBalancer.

                
                

                - **LoadBalancerName** *(string) --* 

                  The name of the LoadBalancer.

                  
                

                - **Domain** *(string) --* 

                  The domain name of the LoadBalancer.

                  
                

                - **Listeners** *(list) --* 

                  A list of Listeners used by the LoadBalancer.

                  
                  

                  - *(dict) --* 

                    Describes the properties of a Listener for the LoadBalancer.

                    
                    

                    - **Protocol** *(string) --* 

                      The protocol that is used by the Listener.

                      
                    

                    - **Port** *(integer) --* 

                      The port that is used by the Listener.

                      
                
              
            
          
            

            - **Tier** *(dict) --* 

              Describes the current tier of this environment.

              
              

              - **Name** *(string) --* 

                The name of this environment tier.

                
              

              - **Type** *(string) --* 

                The type of this environment tier.

                
              

              - **Version** *(string) --* 

                The version of this environment tier.

                
          
            

            - **EnvironmentLinks** *(list) --* 

              A list of links to other environments in the same group.

              
              

              - *(dict) --* 

                A link to another environment, defined in the environment's manifest. Links provide connection information in system properties that can be used to connect to another environment in the same group. See `Environment Manifest (env.yaml) <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.

                
                

                - **LinkName** *(string) --* 

                  The name of the link.

                  
                

                - **EnvironmentName** *(string) --* 

                  The name of the linked environment (the dependency).

                  
            
          
            

            - **EnvironmentArn** *(string) --* 

              The environment's Amazon Resource Name (ARN), which can be used in other API reuqests that require an ARN.

              
        
      
        

        - **NextToken** *(string) --* 

          In a paginated request, the token that you can pass in a subsequent request to get the next response page.

          
    

  .. py:method:: create_application(**kwargs)

    

    Creates an application that has one configuration template named ``default`` and no application versions. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreateApplication>`_    


    **Request Syntax** 
    ::

      response = client.create_application(
          ApplicationName='string',
          Description='string',
          ResourceLifecycleConfig={
              'ServiceRole': 'string',
              'VersionLifecycleConfig': {
                  'MaxCountRule': {
                      'Enabled': True|False,
                      'MaxCount': 123,
                      'DeleteSourceFromS3': True|False
                  },
                  'MaxAgeRule': {
                      'Enabled': True|False,
                      'MaxAgeInDays': 123,
                      'DeleteSourceFromS3': True|False
                  }
              }
          }
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application.

       

      Constraint: This name must be unique within your account. If the specified name already exists, the action returns an ``InvalidParameterValue`` error.

      

    
    :type Description: string
    :param Description: 

      Describes the application.

      

    
    :type ResourceLifecycleConfig: dict
    :param ResourceLifecycleConfig: 

      Specify an application resource lifecycle configuration to prevent your application from accumulating too many versions.

      

    
      - **ServiceRole** *(string) --* 

        The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

        

      
      - **VersionLifecycleConfig** *(dict) --* 

        The application version lifecycle configuration.

        

      
        - **MaxCountRule** *(dict) --* 

          Specify a max count rule to restrict the number of application versions that are retained for an application.

          

        
          - **Enabled** *(boolean) --* **[REQUIRED]** 

            Specify ``true`` to apply the rule, or ``false`` to disable it.

            

          
          - **MaxCount** *(integer) --* 

            Specify the maximum number of application versions to retain.

            

          
          - **DeleteSourceFromS3** *(boolean) --* 

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

            

          
        
        - **MaxAgeRule** *(dict) --* 

          Specify a max age rule to restrict the length of time that application versions are retained for an application.

          

        
          - **Enabled** *(boolean) --* **[REQUIRED]** 

            Specify ``true`` to apply the rule, or ``false`` to disable it.

            

          
          - **MaxAgeInDays** *(integer) --* 

            Specify the number of days to retain an application versions.

            

          
          - **DeleteSourceFromS3** *(boolean) --* 

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

            

          
        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Application': {
                'ApplicationName': 'string',
                'Description': 'string',
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'Versions': [
                    'string',
                ],
                'ConfigurationTemplates': [
                    'string',
                ],
                'ResourceLifecycleConfig': {
                    'ServiceRole': 'string',
                    'VersionLifecycleConfig': {
                        'MaxCountRule': {
                            'Enabled': True|False,
                            'MaxCount': 123,
                            'DeleteSourceFromS3': True|False
                        },
                        'MaxAgeRule': {
                            'Enabled': True|False,
                            'MaxAgeInDays': 123,
                            'DeleteSourceFromS3': True|False
                        }
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message containing a single description of an application.

        
        

        - **Application** *(dict) --* 

          The  ApplicationDescription of the application. 

          
          

          - **ApplicationName** *(string) --* 

            The name of the application.

            
          

          - **Description** *(string) --* 

            User-defined description of the application.

            
          

          - **DateCreated** *(datetime) --* 

            The date when the application was created.

            
          

          - **DateUpdated** *(datetime) --* 

            The date when the application was last modified.

            
          

          - **Versions** *(list) --* 

            The names of the versions for this application.

            
            

            - *(string) --* 
        
          

          - **ConfigurationTemplates** *(list) --* 

            The names of the configuration templates associated with this application.

            
            

            - *(string) --* 
        
          

          - **ResourceLifecycleConfig** *(dict) --* 

            The lifecycle settings for the application.

            
            

            - **ServiceRole** *(string) --* 

              The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

              
            

            - **VersionLifecycleConfig** *(dict) --* 

              The application version lifecycle configuration.

              
              

              - **MaxCountRule** *(dict) --* 

                Specify a max count rule to restrict the number of application versions that are retained for an application.

                
                

                - **Enabled** *(boolean) --* 

                  Specify ``true`` to apply the rule, or ``false`` to disable it.

                  
                

                - **MaxCount** *(integer) --* 

                  Specify the maximum number of application versions to retain.

                  
                

                - **DeleteSourceFromS3** *(boolean) --* 

                  Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

                  
            
              

              - **MaxAgeRule** *(dict) --* 

                Specify a max age rule to restrict the length of time that application versions are retained for an application.

                
                

                - **Enabled** *(boolean) --* 

                  Specify ``true`` to apply the rule, or ``false`` to disable it.

                  
                

                - **MaxAgeInDays** *(integer) --* 

                  Specify the number of days to retain an application versions.

                  
                

                - **DeleteSourceFromS3** *(boolean) --* 

                  Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

                  
            
          
        
      
    

    **Examples** 

    The following operation creates a new application named my-app:
    ::

      response = client.create_application(
          ApplicationName='my-app',
          Description='my application',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Application': {
              'ApplicationName': 'my-app',
              'ConfigurationTemplates': [
              ],
              'DateCreated': datetime(2015, 2, 12, 18, 32, 21, 3, 43, 0),
              'DateUpdated': datetime(2015, 2, 12, 18, 32, 21, 3, 43, 0),
              'Description': 'my application',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_application_version(**kwargs)

    

    Creates an application version for the specified application. You can create an application version from a source bundle in Amazon S3, a commit in AWS CodeCommit, or the output of an AWS CodeBuild build as follows:

     

    Specify a commit in an AWS CodeCommit repository with ``SourceBuildInformation`` .

     

    Specify a build in an AWS CodeBuild with ``SourceBuildInformation`` and ``BuildConfiguration`` .

     

    Specify a source bundle in S3 with ``SourceBundle``  

     

    Omit both ``SourceBuildInformation`` and ``SourceBundle`` to use the default sample application.

     

    .. note::

       

      Once you create an application version with a specified Amazon S3 bucket and key location, you cannot change that Amazon S3 location. If you change the Amazon S3 location, you receive an exception when you attempt to launch an environment from the application version.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreateApplicationVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_application_version(
          ApplicationName='string',
          VersionLabel='string',
          Description='string',
          SourceBuildInformation={
              'SourceType': 'Git'|'Zip',
              'SourceRepository': 'CodeCommit'|'S3',
              'SourceLocation': 'string'
          },
          SourceBundle={
              'S3Bucket': 'string',
              'S3Key': 'string'
          },
          BuildConfiguration={
              'ArtifactName': 'string',
              'CodeBuildServiceRole': 'string',
              'ComputeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
              'Image': 'string',
              'TimeoutInMinutes': 123
          },
          AutoCreateApplication=True|False,
          Process=True|False
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application. If no application is found with this name, and ``AutoCreateApplication`` is ``false`` , returns an ``InvalidParameterValue`` error. 

      

    
    :type VersionLabel: string
    :param VersionLabel: **[REQUIRED]** 

      A label identifying this version.

       

      Constraint: Must be unique per application. If an application version already exists with this label for the specified application, AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error. 

      

    
    :type Description: string
    :param Description: 

      Describes this version.

      

    
    :type SourceBuildInformation: dict
    :param SourceBuildInformation: 

      Specify a commit in an AWS CodeCommit Git repository to use as the source code for the application version.

      

    
      - **SourceType** *(string) --* **[REQUIRED]** 

        The type of repository.

         

         
        * ``Git``   
         
        * ``Zip``   
         

        

      
      - **SourceRepository** *(string) --* **[REQUIRED]** 

        Location where the repository is stored.

         

         
        * ``CodeCommit``   
         
        * ``S3``   
         

        

      
      - **SourceLocation** *(string) --* **[REQUIRED]** 

        The location of the source code, as a formatted string, depending on the value of ``SourceRepository``  

         

         
        * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` . 
         
        * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward slash. For example, ``my-s3-bucket/Folders/my-source-file`` . 
         

        

      
    
    :type SourceBundle: dict
    :param SourceBundle: 

      The Amazon S3 bucket and key that identify the location of the source bundle for this version.

       

      .. note::

         

        The Amazon S3 bucket must be in the same region as the environment.

         

       

      Specify a source bundle in S3 or a commit in an AWS CodeCommit repository (with ``SourceBuildInformation`` ), but not both. If neither ``SourceBundle`` nor ``SourceBuildInformation`` are provided, Elastic Beanstalk uses a sample application.

      

    
      - **S3Bucket** *(string) --* 

        The Amazon S3 bucket where the data is located.

        

      
      - **S3Key** *(string) --* 

        The Amazon S3 key where the data is located.

        

      
    
    :type BuildConfiguration: dict
    :param BuildConfiguration: 

      Settings for an AWS CodeBuild build.

      

    
      - **ArtifactName** *(string) --* 

        The name of the artifact of the CodeBuild build. If provided, Elastic Beanstalk stores the build artifact in the S3 location *S3-bucket* /resources/*application-name* /codebuild/codebuild-*version-label* -*artifact-name* .zip. If not provided, Elastic Beanstalk stores the build artifact in the S3 location *S3-bucket* /resources/*application-name* /codebuild/codebuild-*version-label* .zip. 

        

      
      - **CodeBuildServiceRole** *(string) --* **[REQUIRED]** 

        The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

        

      
      - **ComputeType** *(string) --* 

        Information about the compute resources the build project will use.

         

         
        * ``BUILD_GENERAL1_SMALL: Use up to 3 GB memory and 2 vCPUs for builds``   
         
        * ``BUILD_GENERAL1_MEDIUM: Use up to 7 GB memory and 4 vCPUs for builds``   
         
        * ``BUILD_GENERAL1_LARGE: Use up to 15 GB memory and 8 vCPUs for builds``   
         

        

      
      - **Image** *(string) --* **[REQUIRED]** 

        The ID of the Docker image to use for this build project.

        

      
      - **TimeoutInMinutes** *(integer) --* 

        How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

        

      
    
    :type AutoCreateApplication: boolean
    :param AutoCreateApplication: 

      Set to ``true`` to create an application with the specified name if it doesn't already exist.

      

    
    :type Process: boolean
    :param Process: 

      Preprocesses and validates the environment manifest (``env.yaml`` ) and configuration files (``*.config`` files in the ``.ebextensions`` folder) in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.

       

      .. note::

         

        The ``Process`` option validates Elastic Beanstalk configuration files. It doesn't validate your application's configuration files, like proxy server or Docker configuration.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationVersion': {
                'ApplicationName': 'string',
                'Description': 'string',
                'VersionLabel': 'string',
                'SourceBuildInformation': {
                    'SourceType': 'Git'|'Zip',
                    'SourceRepository': 'CodeCommit'|'S3',
                    'SourceLocation': 'string'
                },
                'BuildArn': 'string',
                'SourceBundle': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'Status': 'Processed'|'Unprocessed'|'Failed'|'Processing'|'Building'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message wrapping a single description of an application version.

        
        

        - **ApplicationVersion** *(dict) --* 

          The  ApplicationVersionDescription of the application version. 

          
          

          - **ApplicationName** *(string) --* 

            The name of the application to which the application version belongs.

            
          

          - **Description** *(string) --* 

            The description of the application version.

            
          

          - **VersionLabel** *(string) --* 

            A unique identifier for the application version.

            
          

          - **SourceBuildInformation** *(dict) --* 

            If the version's source code was retrieved from AWS CodeCommit, the location of the source code for the application version.

            
            

            - **SourceType** *(string) --* 

              The type of repository.

               

               
              * ``Git``   
               
              * ``Zip``   
               

              
            

            - **SourceRepository** *(string) --* 

              Location where the repository is stored.

               

               
              * ``CodeCommit``   
               
              * ``S3``   
               

              
            

            - **SourceLocation** *(string) --* 

              The location of the source code, as a formatted string, depending on the value of ``SourceRepository``  

               

               
              * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` . 
               
              * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward slash. For example, ``my-s3-bucket/Folders/my-source-file`` . 
               

              
        
          

          - **BuildArn** *(string) --* 

            Reference to the artifact from the AWS CodeBuild build.

            
          

          - **SourceBundle** *(dict) --* 

            The storage location of the application version's source bundle in Amazon S3.

            
            

            - **S3Bucket** *(string) --* 

              The Amazon S3 bucket where the data is located.

              
            

            - **S3Key** *(string) --* 

              The Amazon S3 key where the data is located.

              
        
          

          - **DateCreated** *(datetime) --* 

            The creation date of the application version.

            
          

          - **DateUpdated** *(datetime) --* 

            The last modified date of the application version.

            
          

          - **Status** *(string) --* 

            The processing status of the application version.

            
      
    

    **Examples** 

    The following operation creates a new version (v1) of an application named my-app:
    ::

      response = client.create_application_version(
          ApplicationName='my-app',
          AutoCreateApplication=True,
          Description='my-app-v1',
          Process=True,
          SourceBundle={
              'S3Bucket': 'my-bucket',
              'S3Key': 'sample.war',
          },
          VersionLabel='v1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ApplicationVersion': {
              'ApplicationName': 'my-app',
              'DateCreated': datetime(2015, 2, 3, 23, 1, 25, 1, 34, 0),
              'DateUpdated': datetime(2015, 2, 3, 23, 1, 25, 1, 34, 0),
              'Description': 'my-app-v1',
              'SourceBundle': {
                  'S3Bucket': 'my-bucket',
                  'S3Key': 'sample.war',
              },
              'VersionLabel': 'v1',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_configuration_template(**kwargs)

    

    Creates a configuration template. Templates are associated with a specific application and are used to deploy different versions of the application with the same configuration settings.

     

    Related Topics

     

     
    *  DescribeConfigurationOptions   
     
    *  DescribeConfigurationSettings   
     
    *  ListAvailableSolutionStacks   
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate>`_    


    **Request Syntax** 
    ::

      response = client.create_configuration_template(
          ApplicationName='string',
          TemplateName='string',
          SolutionStackName='string',
          PlatformArn='string',
          SourceConfiguration={
              'ApplicationName': 'string',
              'TemplateName': 'string'
          },
          EnvironmentId='string',
          Description='string',
          OptionSettings=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application to associate with this configuration template. If no application is found with this name, AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error. 

      

    
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the configuration template.

       

      Constraint: This name must be unique per application.

       

      Default: If a configuration template already exists with this name, AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error. 

      

    
    :type SolutionStackName: string
    :param SolutionStackName: 

      The name of the solution stack used by this configuration. The solution stack specifies the operating system, architecture, and application server for a configuration template. It determines the set of configuration options as well as the possible and default values.

       

      Use  ListAvailableSolutionStacks to obtain a list of available solution stacks. 

       

      A solution stack name or a source configuration parameter must be specified, otherwise AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error. 

       

      If a solution stack name is not specified and the source configuration parameter is specified, AWS Elastic Beanstalk uses the same solution stack as the source configuration template.

      

    
    :type PlatformArn: string
    :param PlatformArn: 

      The ARN of the custom platform.

      

    
    :type SourceConfiguration: dict
    :param SourceConfiguration: 

      If specified, AWS Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.

       

      Values specified in the ``OptionSettings`` parameter of this call overrides any values obtained from the ``SourceConfiguration`` . 

       

      If no configuration template is found, returns an ``InvalidParameterValue`` error. 

       

      Constraint: If both the solution stack name parameter and the source configuration parameters are specified, the solution stack of the source configuration template must match the specified solution stack name or else AWS Elastic Beanstalk returns an ``InvalidParameterCombination`` error. 

      

    
      - **ApplicationName** *(string) --* 

        The name of the application associated with the configuration.

        

      
      - **TemplateName** *(string) --* 

        The name of the configuration template.

        

      
    
    :type EnvironmentId: string
    :param EnvironmentId: 

      The ID of the environment used with this configuration template.

      

    
    :type Description: string
    :param Description: 

      Describes this configuration.

      

    
    :type OptionSettings: list
    :param OptionSettings: 

      If specified, AWS Elastic Beanstalk sets the specified configuration option to the requested value. The new value overrides the value obtained from the solution stack or the source configuration template.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
        - **Value** *(string) --* 

          The current value for the configuration option.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SolutionStackName': 'string',
            'PlatformArn': 'string',
            'ApplicationName': 'string',
            'TemplateName': 'string',
            'Description': 'string',
            'EnvironmentName': 'string',
            'DeploymentStatus': 'deployed'|'pending'|'failed',
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'OptionSettings': [
                {
                    'ResourceName': 'string',
                    'Namespace': 'string',
                    'OptionName': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes the settings for a configuration set.

        
        

        - **SolutionStackName** *(string) --* 

          The name of the solution stack this configuration set uses.

          
        

        - **PlatformArn** *(string) --* 

          The ARN of the platform.

          
        

        - **ApplicationName** *(string) --* 

          The name of the application associated with this configuration set.

          
        

        - **TemplateName** *(string) --* 

          If not ``null`` , the name of the configuration template for this configuration set. 

          
        

        - **Description** *(string) --* 

          Describes this configuration set.

          
        

        - **EnvironmentName** *(string) --* 

          If not ``null`` , the name of the environment for this configuration set. 

          
        

        - **DeploymentStatus** *(string) --* 

          If this configuration set is associated with an environment, the ``DeploymentStatus`` parameter indicates the deployment status of this configuration set: 

           

           
          * ``null`` : This configuration is not associated with a running environment. 
           
          * ``pending`` : This is a draft configuration that is not deployed to the associated environment but is in the process of deploying. 
           
          * ``deployed`` : This is the configuration that is currently deployed to the associated running environment. 
           
          * ``failed`` : This is a draft configuration that failed to successfully deploy. 
           

          
        

        - **DateCreated** *(datetime) --* 

          The date (in UTC time) when this configuration set was created.

          
        

        - **DateUpdated** *(datetime) --* 

          The date (in UTC time) when this configuration set was last modified.

          
        

        - **OptionSettings** *(list) --* 

          A list of the configuration options and their values in this configuration set.

          
          

          - *(dict) --* 

            A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

            
            

            - **ResourceName** *(string) --* 

              A unique resource name for a time-based scaling configuration option.

              
            

            - **Namespace** *(string) --* 

              A unique namespace identifying the option's associated AWS resource.

              
            

            - **OptionName** *(string) --* 

              The name of the configuration option.

              
            

            - **Value** *(string) --* 

              The current value for the configuration option.

              
        
      
    

    **Examples** 

    The following operation creates a configuration template named my-app-v1 from the settings applied to an environment with the id e-rpqsewtp2j:
    ::

      response = client.create_configuration_template(
          ApplicationName='my-app',
          EnvironmentId='e-rpqsewtp2j',
          TemplateName='my-app-v1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ApplicationName': 'my-app',
          'DateCreated': datetime(2015, 8, 12, 18, 40, 39, 2, 224, 0),
          'DateUpdated': datetime(2015, 8, 12, 18, 40, 39, 2, 224, 0),
          'SolutionStackName': '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
          'TemplateName': 'my-app-v1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_environment(**kwargs)

    

    Launches an environment for the specified application using the specified configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreateEnvironment>`_    


    **Request Syntax** 
    ::

      response = client.create_environment(
          ApplicationName='string',
          EnvironmentName='string',
          GroupName='string',
          Description='string',
          CNAMEPrefix='string',
          Tier={
              'Name': 'string',
              'Type': 'string',
              'Version': 'string'
          },
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          VersionLabel='string',
          TemplateName='string',
          SolutionStackName='string',
          PlatformArn='string',
          OptionSettings=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string',
                  'Value': 'string'
              },
          ],
          OptionsToRemove=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string'
              },
          ]
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application that contains the version to be deployed.

       

      If no application is found with this name, ``CreateEnvironment`` returns an ``InvalidParameterValue`` error. 

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      A unique name for the deployment environment. Used in the application URL.

       

      Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It cannot start or end with a hyphen. This name must be unique within a region in your account. If the specified name already exists in the region, AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error. 

       

      Default: If the CNAME parameter is not specified, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application.

      

    
    :type GroupName: string
    :param GroupName: 

      The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name parameter. See `Environment Manifest (env.yaml) <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.

      

    
    :type Description: string
    :param Description: 

      Describes this environment.

      

    
    :type CNAMEPrefix: string
    :param CNAMEPrefix: 

      If specified, the environment attempts to use this value as the prefix for the CNAME. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.

      

    
    :type Tier: dict
    :param Tier: 

      This specifies the tier to use for creating this environment.

      

    
      - **Name** *(string) --* 

        The name of this environment tier.

        

      
      - **Type** *(string) --* 

        The type of this environment tier.

        

      
      - **Version** *(string) --* 

        The version of this environment tier.

        

      
    
    :type Tags: list
    :param Tags: 

      This specifies the tags applied to resources in the environment.

      

    
      - *(dict) --* 

        Describes a tag applied to a resource in an environment.

        

      
        - **Key** *(string) --* 

          The key of the tag.

          

        
        - **Value** *(string) --* 

          The value of the tag.

          

        
      
  
    :type VersionLabel: string
    :param VersionLabel: 

      The name of the application version to deploy.

       

      If the specified application has no associated application versions, AWS Elastic Beanstalk ``UpdateEnvironment`` returns an ``InvalidParameterValue`` error. 

       

      Default: If not specified, AWS Elastic Beanstalk attempts to launch the sample application in the container.

      

    
    :type TemplateName: string
    :param TemplateName: 

      The name of the configuration template to use in deployment. If no configuration template is found with this name, AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error. 

      

    
    :type SolutionStackName: string
    :param SolutionStackName: 

      This is an alternative to specifying a template name. If specified, AWS Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack.

      

    
    :type PlatformArn: string
    :param PlatformArn: 

      The ARN of the platform.

      

    
    :type OptionSettings: list
    :param OptionSettings: 

      If specified, AWS Elastic Beanstalk sets the specified configuration options to the requested value in the configuration set for the new environment. These override the values obtained from the solution stack or the configuration template.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
        - **Value** *(string) --* 

          The current value for the configuration option.

          

        
      
  
    :type OptionsToRemove: list
    :param OptionsToRemove: 

      A list of custom user-defined configuration options to remove from the configuration set for this new environment.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option.

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EnvironmentName': 'string',
            'EnvironmentId': 'string',
            'ApplicationName': 'string',
            'VersionLabel': 'string',
            'SolutionStackName': 'string',
            'PlatformArn': 'string',
            'TemplateName': 'string',
            'Description': 'string',
            'EndpointURL': 'string',
            'CNAME': 'string',
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
            'AbortableOperationInProgress': True|False,
            'Health': 'Green'|'Yellow'|'Red'|'Grey',
            'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
            'Resources': {
                'LoadBalancer': {
                    'LoadBalancerName': 'string',
                    'Domain': 'string',
                    'Listeners': [
                        {
                            'Protocol': 'string',
                            'Port': 123
                        },
                    ]
                }
            },
            'Tier': {
                'Name': 'string',
                'Type': 'string',
                'Version': 'string'
            },
            'EnvironmentLinks': [
                {
                    'LinkName': 'string',
                    'EnvironmentName': 'string'
                },
            ],
            'EnvironmentArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes the properties of an environment.

        
        

        - **EnvironmentName** *(string) --* 

          The name of this environment.

          
        

        - **EnvironmentId** *(string) --* 

          The ID of this environment.

          
        

        - **ApplicationName** *(string) --* 

          The name of the application associated with this environment.

          
        

        - **VersionLabel** *(string) --* 

          The application version deployed in this environment.

          
        

        - **SolutionStackName** *(string) --* 

          The name of the ``SolutionStack`` deployed with this environment. 

          
        

        - **PlatformArn** *(string) --* 

          The ARN of the platform.

          
        

        - **TemplateName** *(string) --* 

          The name of the configuration template used to originally launch this environment.

          
        

        - **Description** *(string) --* 

          Describes this environment.

          
        

        - **EndpointURL** *(string) --* 

          For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.

          
        

        - **CNAME** *(string) --* 

          The URL to the CNAME for this environment.

          
        

        - **DateCreated** *(datetime) --* 

          The creation date for this environment.

          
        

        - **DateUpdated** *(datetime) --* 

          The last modified date for this environment.

          
        

        - **Status** *(string) --* 

          The current operational status of the environment:

           

           
          * ``Launching`` : Environment is in the process of initial deployment. 
           
          * ``Updating`` : Environment is in the process of updating its configuration settings or application version. 
           
          * ``Ready`` : Environment is available to have an action performed on it, such as update or terminate. 
           
          * ``Terminating`` : Environment is in the shut-down process. 
           
          * ``Terminated`` : Environment is not running. 
           

          
        

        - **AbortableOperationInProgress** *(boolean) --* 

          Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.

           

           ``true:`` There is an update in progress. 

           

           ``false:`` There are no updates currently in progress. 

          
        

        - **Health** *(string) --* 

          Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:

           

           
          * ``Red`` : Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment. 
           
          * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur for an environment. 
           
          * ``Green`` : Indicates the environment is healthy and fully functional. 
           
          * ``Grey`` : Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an ``UpdateEnvironment`` or ``RestartEnvironement`` request. 
           

           

          Default: ``Grey``  

          
        

        - **HealthStatus** *(string) --* 

          Returns the health status of the application running in your environment. For more information, see `Health Colors and Statuses <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

          
        

        - **Resources** *(dict) --* 

          The description of the AWS resources used by this environment.

          
          

          - **LoadBalancer** *(dict) --* 

            Describes the LoadBalancer.

            
            

            - **LoadBalancerName** *(string) --* 

              The name of the LoadBalancer.

              
            

            - **Domain** *(string) --* 

              The domain name of the LoadBalancer.

              
            

            - **Listeners** *(list) --* 

              A list of Listeners used by the LoadBalancer.

              
              

              - *(dict) --* 

                Describes the properties of a Listener for the LoadBalancer.

                
                

                - **Protocol** *(string) --* 

                  The protocol that is used by the Listener.

                  
                

                - **Port** *(integer) --* 

                  The port that is used by the Listener.

                  
            
          
        
      
        

        - **Tier** *(dict) --* 

          Describes the current tier of this environment.

          
          

          - **Name** *(string) --* 

            The name of this environment tier.

            
          

          - **Type** *(string) --* 

            The type of this environment tier.

            
          

          - **Version** *(string) --* 

            The version of this environment tier.

            
      
        

        - **EnvironmentLinks** *(list) --* 

          A list of links to other environments in the same group.

          
          

          - *(dict) --* 

            A link to another environment, defined in the environment's manifest. Links provide connection information in system properties that can be used to connect to another environment in the same group. See `Environment Manifest (env.yaml) <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.

            
            

            - **LinkName** *(string) --* 

              The name of the link.

              
            

            - **EnvironmentName** *(string) --* 

              The name of the linked environment (the dependency).

              
        
      
        

        - **EnvironmentArn** *(string) --* 

          The environment's Amazon Resource Name (ARN), which can be used in other API reuqests that require an ARN.

          
    

    **Examples** 

    The following operation creates a new environment for version v1 of a java application named my-app:
    ::

      response = client.create_environment(
          ApplicationName='my-app',
          CNAMEPrefix='my-app',
          EnvironmentName='my-env',
          SolutionStackName='64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
          VersionLabel='v1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ApplicationName': 'my-app',
          'CNAME': 'my-app.elasticbeanstalk.com',
          'DateCreated': datetime(2015, 2, 3, 23, 4, 54, 1, 34, 0),
          'DateUpdated': datetime(2015, 2, 3, 23, 4, 54, 1, 34, 0),
          'EnvironmentId': 'e-izqpassy4h',
          'EnvironmentName': 'my-env',
          'Health': 'Grey',
          'SolutionStackName': '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
          'Status': 'Launching',
          'Tier': {
              'Name': 'WebServer',
              'Type': 'Standard',
              'Version': ' ',
          },
          'VersionLabel': 'v1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_platform_version(**kwargs)

    

    Create a new version of your custom platform.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreatePlatformVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_platform_version(
          PlatformName='string',
          PlatformVersion='string',
          PlatformDefinitionBundle={
              'S3Bucket': 'string',
              'S3Key': 'string'
          },
          EnvironmentName='string',
          OptionSettings=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type PlatformName: string
    :param PlatformName: **[REQUIRED]** 

      The name of your custom platform.

      

    
    :type PlatformVersion: string
    :param PlatformVersion: **[REQUIRED]** 

      The number, such as 1.0.2, for the new platform version.

      

    
    :type PlatformDefinitionBundle: dict
    :param PlatformDefinitionBundle: **[REQUIRED]** 

      The location of the platform definition archive in Amazon S3.

      

    
      - **S3Bucket** *(string) --* 

        The Amazon S3 bucket where the data is located.

        

      
      - **S3Key** *(string) --* 

        The Amazon S3 key where the data is located.

        

      
    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the builder environment.

      

    
    :type OptionSettings: list
    :param OptionSettings: 

      The configuration option settings to apply to the builder environment.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
        - **Value** *(string) --* 

          The current value for the configuration option.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PlatformSummary': {
                'PlatformArn': 'string',
                'PlatformOwner': 'string',
                'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
                'PlatformCategory': 'string',
                'OperatingSystemName': 'string',
                'OperatingSystemVersion': 'string',
                'SupportedTierList': [
                    'string',
                ],
                'SupportedAddonList': [
                    'string',
                ]
            },
            'Builder': {
                'ARN': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PlatformSummary** *(dict) --* 

          Detailed information about the new version of the custom platform.

          
          

          - **PlatformArn** *(string) --* 

            The ARN of the platform.

            
          

          - **PlatformOwner** *(string) --* 

            The AWS account ID of the person who created the platform.

            
          

          - **PlatformStatus** *(string) --* 

            The status of the platform. You can create an environment from the platform once it is ready.

            
          

          - **PlatformCategory** *(string) --* 

            The category of platform.

            
          

          - **OperatingSystemName** *(string) --* 

            The operating system used by the platform.

            
          

          - **OperatingSystemVersion** *(string) --* 

            The version of the operating system used by the platform.

            
          

          - **SupportedTierList** *(list) --* 

            The tiers in which the platform runs.

            
            

            - *(string) --* 
        
          

          - **SupportedAddonList** *(list) --* 

            The additions associated with the platform.

            
            

            - *(string) --* 
        
      
        

        - **Builder** *(dict) --* 

          The builder used to create the custom platform.

          
          

          - **ARN** *(string) --* 

            The ARN of the builder.

            
      
    

  .. py:method:: create_storage_location()

    

    Creates a bucket in Amazon S3 to store application versions, logs, and other files used by Elastic Beanstalk environments. The Elastic Beanstalk console and EB CLI call this API the first time you create an environment in a region. If the storage location already exists, ``CreateStorageLocation`` still returns the bucket name but does not create a new bucket.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreateStorageLocation>`_    


    **Request Syntax** 

    ::

      response = client.create_storage_location()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'S3Bucket': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Results of a  CreateStorageLocationResult call.

        
        

        - **S3Bucket** *(string) --* 

          The name of the Amazon S3 bucket created.

          
    

    **Examples** 

    The following operation creates a new environment for version v1 of a java application named my-app:
    ::

      response = client.create_storage_location(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'S3Bucket': 'elasticbeanstalk-us-west-2-0123456789012',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_application(**kwargs)

    

    Deletes the specified application along with all associated versions and configurations. The application versions will not be deleted from your Amazon S3 bucket.

     

    .. note::

       

      You cannot delete an application that has a running environment.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DeleteApplication>`_    


    **Request Syntax** 
    ::

      response = client.delete_application(
          ApplicationName='string',
          TerminateEnvByForce=True|False
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application to delete.

      

    
    :type TerminateEnvByForce: boolean
    :param TerminateEnvByForce: 

      When set to true, running environments will be terminated before deleting the application.

      

    
    
    :returns: None

    **Examples** 

    The following operation deletes an application named my-app:
    ::

      response = client.delete_application(
          ApplicationName='my-app',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_application_version(**kwargs)

    

    Deletes the specified version from the specified application.

     

    .. note::

       

      You cannot delete an application version that is associated with a running environment.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DeleteApplicationVersion>`_    


    **Request Syntax** 
    ::

      response = client.delete_application_version(
          ApplicationName='string',
          VersionLabel='string',
          DeleteSourceBundle=True|False
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application to which the version belongs.

      

    
    :type VersionLabel: string
    :param VersionLabel: **[REQUIRED]** 

      The label of the version to delete.

      

    
    :type DeleteSourceBundle: boolean
    :param DeleteSourceBundle: 

      Set to ``true`` to delete the source bundle from your storage bucket. Otherwise, the application version is deleted only from Elastic Beanstalk and the source bundle remains in Amazon S3.

      

    
    
    :returns: None

    **Examples** 

    The following operation deletes an application version named 22a0-stage-150819_182129 for an application named my-app:
    ::

      response = client.delete_application_version(
          ApplicationName='my-app',
          DeleteSourceBundle=True,
          VersionLabel='22a0-stage-150819_182129',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_configuration_template(**kwargs)

    

    Deletes the specified configuration template.

     

    .. note::

       

      When you launch an environment using a configuration template, the environment gets a copy of the template. You can delete or modify the environment's copy of the template without affecting the running environment.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate>`_    


    **Request Syntax** 
    ::

      response = client.delete_configuration_template(
          ApplicationName='string',
          TemplateName='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application to delete the configuration template from.

      

    
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the configuration template to delete.

      

    
    
    :returns: None

    **Examples** 

    The following operation deletes a configuration template named my-template for an application named my-app:
    ::

      response = client.delete_configuration_template(
          ApplicationName='my-app',
          TemplateName='my-template',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_environment_configuration(**kwargs)

    

    Deletes the draft configuration associated with the running environment.

     

    Updating a running environment with any configuration changes creates a draft configuration set. You can get the draft configuration using  DescribeConfigurationSettings while the update is in progress or if the update fails. The ``DeploymentStatus`` for the draft configuration indicates whether the deployment is in process or has failed. The draft configuration remains in existence until it is deleted with this action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DeleteEnvironmentConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.delete_environment_configuration(
          ApplicationName='string',
          EnvironmentName='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application the environment is associated with.

      

    
    :type EnvironmentName: string
    :param EnvironmentName: **[REQUIRED]** 

      The name of the environment to delete the draft configuration from.

      

    
    
    :returns: None

    **Examples** 

    The following operation deletes a draft configuration for an environment named my-env:
    ::

      response = client.delete_environment_configuration(
          ApplicationName='my-app',
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_platform_version(**kwargs)

    

    Deletes the specified version of a custom platform.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DeletePlatformVersion>`_    


    **Request Syntax** 
    ::

      response = client.delete_platform_version(
          PlatformArn='string'
      )
    :type PlatformArn: string
    :param PlatformArn: 

      The ARN of the version of the custom platform.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PlatformSummary': {
                'PlatformArn': 'string',
                'PlatformOwner': 'string',
                'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
                'PlatformCategory': 'string',
                'OperatingSystemName': 'string',
                'OperatingSystemVersion': 'string',
                'SupportedTierList': [
                    'string',
                ],
                'SupportedAddonList': [
                    'string',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PlatformSummary** *(dict) --* 

          Detailed information about the version of the custom platform.

          
          

          - **PlatformArn** *(string) --* 

            The ARN of the platform.

            
          

          - **PlatformOwner** *(string) --* 

            The AWS account ID of the person who created the platform.

            
          

          - **PlatformStatus** *(string) --* 

            The status of the platform. You can create an environment from the platform once it is ready.

            
          

          - **PlatformCategory** *(string) --* 

            The category of platform.

            
          

          - **OperatingSystemName** *(string) --* 

            The operating system used by the platform.

            
          

          - **OperatingSystemVersion** *(string) --* 

            The version of the operating system used by the platform.

            
          

          - **SupportedTierList** *(list) --* 

            The tiers in which the platform runs.

            
            

            - *(string) --* 
        
          

          - **SupportedAddonList** *(list) --* 

            The additions associated with the platform.

            
            

            - *(string) --* 
        
      
    

  .. py:method:: describe_application_versions(**kwargs)

    

    Retrieve a list of application versions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeApplicationVersions>`_    


    **Request Syntax** 
    ::

      response = client.describe_application_versions(
          ApplicationName='string',
          VersionLabels=[
              'string',
          ],
          MaxRecords=123,
          NextToken='string'
      )
    :type ApplicationName: string
    :param ApplicationName: 

      Specify an application name to show only application versions for that application.

      

    
    :type VersionLabels: list
    :param VersionLabels: 

      Specify a version label to show a specific application version.

      

    
      - *(string) --* 

      
  
    :type MaxRecords: integer
    :param MaxRecords: 

      For a paginated request. Specify a maximum number of application versions to include in each response.

       

      If no ``MaxRecords`` is specified, all available application versions are retrieved in a single response.

      

    
    :type NextToken: string
    :param NextToken: 

      For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.

       

      If no ``NextToken`` is specified, the first page is retrieved.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationVersions': [
                {
                    'ApplicationName': 'string',
                    'Description': 'string',
                    'VersionLabel': 'string',
                    'SourceBuildInformation': {
                        'SourceType': 'Git'|'Zip',
                        'SourceRepository': 'CodeCommit'|'S3',
                        'SourceLocation': 'string'
                    },
                    'BuildArn': 'string',
                    'SourceBundle': {
                        'S3Bucket': 'string',
                        'S3Key': 'string'
                    },
                    'DateCreated': datetime(2015, 1, 1),
                    'DateUpdated': datetime(2015, 1, 1),
                    'Status': 'Processed'|'Unprocessed'|'Failed'|'Processing'|'Building'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message wrapping a list of application version descriptions.

        
        

        - **ApplicationVersions** *(list) --* 

          List of ``ApplicationVersionDescription`` objects sorted in order of creation.

          
          

          - *(dict) --* 

            Describes the properties of an application version.

            
            

            - **ApplicationName** *(string) --* 

              The name of the application to which the application version belongs.

              
            

            - **Description** *(string) --* 

              The description of the application version.

              
            

            - **VersionLabel** *(string) --* 

              A unique identifier for the application version.

              
            

            - **SourceBuildInformation** *(dict) --* 

              If the version's source code was retrieved from AWS CodeCommit, the location of the source code for the application version.

              
              

              - **SourceType** *(string) --* 

                The type of repository.

                 

                 
                * ``Git``   
                 
                * ``Zip``   
                 

                
              

              - **SourceRepository** *(string) --* 

                Location where the repository is stored.

                 

                 
                * ``CodeCommit``   
                 
                * ``S3``   
                 

                
              

              - **SourceLocation** *(string) --* 

                The location of the source code, as a formatted string, depending on the value of ``SourceRepository``  

                 

                 
                * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` . 
                 
                * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward slash. For example, ``my-s3-bucket/Folders/my-source-file`` . 
                 

                
          
            

            - **BuildArn** *(string) --* 

              Reference to the artifact from the AWS CodeBuild build.

              
            

            - **SourceBundle** *(dict) --* 

              The storage location of the application version's source bundle in Amazon S3.

              
              

              - **S3Bucket** *(string) --* 

                The Amazon S3 bucket where the data is located.

                
              

              - **S3Key** *(string) --* 

                The Amazon S3 key where the data is located.

                
          
            

            - **DateCreated** *(datetime) --* 

              The creation date of the application version.

              
            

            - **DateUpdated** *(datetime) --* 

              The last modified date of the application version.

              
            

            - **Status** *(string) --* 

              The processing status of the application version.

              
        
      
        

        - **NextToken** *(string) --* 

          In a paginated request, the token that you can pass in a subsequent request to get the next response page.

          
    

    **Examples** 

    The following operation retrieves information about an application version labeled v2:
    ::

      response = client.describe_application_versions(
          ApplicationName='my-app',
          VersionLabels=[
              'v2',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ApplicationVersions': [
              {
                  'ApplicationName': 'my-app',
                  'DateCreated': datetime(2015, 7, 23, 1, 32, 26, 3, 204, 0),
                  'DateUpdated': datetime(2015, 7, 23, 1, 32, 26, 3, 204, 0),
                  'Description': 'update cover page',
                  'SourceBundle': {
                      'S3Bucket': 'elasticbeanstalk-us-west-2-015321684451',
                      'S3Key': 'my-app/5026-stage-150723_224258.war',
                  },
                  'VersionLabel': 'v2',
              },
              {
                  'ApplicationName': 'my-app',
                  'DateCreated': datetime(2015, 7, 23, 22, 26, 10, 3, 204, 0),
                  'DateUpdated': datetime(2015, 7, 23, 22, 26, 10, 3, 204, 0),
                  'Description': 'initial version',
                  'SourceBundle': {
                      'S3Bucket': 'elasticbeanstalk-us-west-2-015321684451',
                      'S3Key': 'my-app/5026-stage-150723_222618.war',
                  },
                  'VersionLabel': 'v1',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_applications(**kwargs)

    

    Returns the descriptions of existing applications.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeApplications>`_    


    **Request Syntax** 
    ::

      response = client.describe_applications(
          ApplicationNames=[
              'string',
          ]
      )
    :type ApplicationNames: list
    :param ApplicationNames: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include those with the specified names.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Applications': [
                {
                    'ApplicationName': 'string',
                    'Description': 'string',
                    'DateCreated': datetime(2015, 1, 1),
                    'DateUpdated': datetime(2015, 1, 1),
                    'Versions': [
                        'string',
                    ],
                    'ConfigurationTemplates': [
                        'string',
                    ],
                    'ResourceLifecycleConfig': {
                        'ServiceRole': 'string',
                        'VersionLifecycleConfig': {
                            'MaxCountRule': {
                                'Enabled': True|False,
                                'MaxCount': 123,
                                'DeleteSourceFromS3': True|False
                            },
                            'MaxAgeRule': {
                                'Enabled': True|False,
                                'MaxAgeInDays': 123,
                                'DeleteSourceFromS3': True|False
                            }
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message containing a list of application descriptions.

        
        

        - **Applications** *(list) --* 

          This parameter contains a list of  ApplicationDescription .

          
          

          - *(dict) --* 

            Describes the properties of an application.

            
            

            - **ApplicationName** *(string) --* 

              The name of the application.

              
            

            - **Description** *(string) --* 

              User-defined description of the application.

              
            

            - **DateCreated** *(datetime) --* 

              The date when the application was created.

              
            

            - **DateUpdated** *(datetime) --* 

              The date when the application was last modified.

              
            

            - **Versions** *(list) --* 

              The names of the versions for this application.

              
              

              - *(string) --* 
          
            

            - **ConfigurationTemplates** *(list) --* 

              The names of the configuration templates associated with this application.

              
              

              - *(string) --* 
          
            

            - **ResourceLifecycleConfig** *(dict) --* 

              The lifecycle settings for the application.

              
              

              - **ServiceRole** *(string) --* 

                The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

                
              

              - **VersionLifecycleConfig** *(dict) --* 

                The application version lifecycle configuration.

                
                

                - **MaxCountRule** *(dict) --* 

                  Specify a max count rule to restrict the number of application versions that are retained for an application.

                  
                  

                  - **Enabled** *(boolean) --* 

                    Specify ``true`` to apply the rule, or ``false`` to disable it.

                    
                  

                  - **MaxCount** *(integer) --* 

                    Specify the maximum number of application versions to retain.

                    
                  

                  - **DeleteSourceFromS3** *(boolean) --* 

                    Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

                    
              
                

                - **MaxAgeRule** *(dict) --* 

                  Specify a max age rule to restrict the length of time that application versions are retained for an application.

                  
                  

                  - **Enabled** *(boolean) --* 

                    Specify ``true`` to apply the rule, or ``false`` to disable it.

                    
                  

                  - **MaxAgeInDays** *(integer) --* 

                    Specify the number of days to retain an application versions.

                    
                  

                  - **DeleteSourceFromS3** *(boolean) --* 

                    Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

                    
              
            
          
        
      
    

    **Examples** 

    The following operation retrieves information about applications in the current region:
    ::

      response = client.describe_applications(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Applications': [
              {
                  'ApplicationName': 'ruby',
                  'ConfigurationTemplates': [
                  ],
                  'DateCreated': datetime(2015, 8, 13, 21, 5, 44, 3, 225, 0),
                  'DateUpdated': datetime(2015, 8, 13, 21, 5, 44, 3, 225, 0),
                  'Versions': [
                      'Sample Application',
                  ],
              },
              {
                  'ApplicationName': 'pythonsample',
                  'ConfigurationTemplates': [
                  ],
                  'DateCreated': datetime(2015, 8, 13, 19, 5, 43, 3, 225, 0),
                  'DateUpdated': datetime(2015, 8, 13, 19, 5, 43, 3, 225, 0),
                  'Description': 'Application created from the EB CLI using "eb init"',
                  'Versions': [
                      'Sample Application',
                  ],
              },
              {
                  'ApplicationName': 'nodejs-example',
                  'ConfigurationTemplates': [
                  ],
                  'DateCreated': datetime(2015, 8, 6, 17, 50, 2, 3, 218, 0),
                  'DateUpdated': datetime(2015, 8, 6, 17, 50, 2, 3, 218, 0),
                  'Versions': [
                      'add elasticache',
                      'First Release',
                  ],
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_configuration_options(**kwargs)

    

    Describes the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines. The description includes the values the options, their default values, and an indication of the required action on a running environment if an option value is changed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions>`_    


    **Request Syntax** 
    ::

      response = client.describe_configuration_options(
          ApplicationName='string',
          TemplateName='string',
          EnvironmentName='string',
          SolutionStackName='string',
          PlatformArn='string',
          Options=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string'
              },
          ]
      )
    :type ApplicationName: string
    :param ApplicationName: 

      The name of the application associated with the configuration template or environment. Only needed if you want to describe the configuration options associated with either the configuration template or environment.

      

    
    :type TemplateName: string
    :param TemplateName: 

      The name of the configuration template whose configuration options you want to describe.

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment whose configuration options you want to describe.

      

    
    :type SolutionStackName: string
    :param SolutionStackName: 

      The name of the solution stack whose configuration options you want to describe.

      

    
    :type PlatformArn: string
    :param PlatformArn: 

      The ARN of the custom platform.

      

    
    :type Options: list
    :param Options: 

      If specified, restricts the descriptions to only the specified options.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option.

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SolutionStackName': 'string',
            'PlatformArn': 'string',
            'Options': [
                {
                    'Namespace': 'string',
                    'Name': 'string',
                    'DefaultValue': 'string',
                    'ChangeSeverity': 'string',
                    'UserDefined': True|False,
                    'ValueType': 'Scalar'|'List',
                    'ValueOptions': [
                        'string',
                    ],
                    'MinValue': 123,
                    'MaxValue': 123,
                    'MaxLength': 123,
                    'Regex': {
                        'Pattern': 'string',
                        'Label': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes the settings for a specified configuration set.

        
        

        - **SolutionStackName** *(string) --* 

          The name of the solution stack these configuration options belong to.

          
        

        - **PlatformArn** *(string) --* 

          The ARN of the platform.

          
        

        - **Options** *(list) --* 

          A list of  ConfigurationOptionDescription . 

          
          

          - *(dict) --* 

            Describes the possible values for a configuration option.

            
            

            - **Namespace** *(string) --* 

              A unique namespace identifying the option's associated AWS resource.

              
            

            - **Name** *(string) --* 

              The name of the configuration option.

              
            

            - **DefaultValue** *(string) --* 

              The default value for this configuration option.

              
            

            - **ChangeSeverity** *(string) --* 

              An indication of which action is required if the value for this configuration option changes:

               

               
              * ``NoInterruption`` : There is no interruption to the environment or application availability. 
               
              * ``RestartEnvironment`` : The environment is entirely restarted, all AWS resources are deleted and recreated, and the environment is unavailable during the process. 
               
              * ``RestartApplicationServer`` : The environment is available the entire time. However, a short application outage occurs when the application servers on the running Amazon EC2 instances are restarted. 
               

              
            

            - **UserDefined** *(boolean) --* 

              An indication of whether the user defined this configuration option:

               

               
              * ``true`` : This configuration option was defined by the user. It is a valid choice for specifying if this as an ``Option to Remove`` when updating configuration settings.  
               
              * ``false`` : This configuration was not defined by the user. 
               

               

              Constraint: You can remove only ``UserDefined`` options from a configuration. 

               

              Valid Values: ``true`` | ``false``  

              
            

            - **ValueType** *(string) --* 

              An indication of which type of values this option has and whether it is allowable to select one or more than one of the possible values:

               

               
              * ``Scalar`` : Values for this option are a single selection from the possible values, or an unformatted string, or numeric value governed by the ``MIN/MAX/Regex`` constraints. 
               
              * ``List`` : Values for this option are multiple selections from the possible values. 
               
              * ``Boolean`` : Values for this option are either ``true`` or ``false`` . 
               
              * ``Json`` : Values for this option are a JSON representation of a ``ConfigDocument`` . 
               

              
            

            - **ValueOptions** *(list) --* 

              If specified, values for the configuration option are selected from this list.

              
              

              - *(string) --* 
          
            

            - **MinValue** *(integer) --* 

              If specified, the configuration option must be a numeric value greater than this value.

              
            

            - **MaxValue** *(integer) --* 

              If specified, the configuration option must be a numeric value less than this value.

              
            

            - **MaxLength** *(integer) --* 

              If specified, the configuration option must be a string value no longer than this value.

              
            

            - **Regex** *(dict) --* 

              If specified, the configuration option must be a string value that satisfies this regular expression.

              
              

              - **Pattern** *(string) --* 

                The regular expression pattern that a string configuration option value with this restriction must match.

                
              

              - **Label** *(string) --* 

                A unique name representing this regular expression.

                
          
        
      
    

    **Examples** 

    The following operation retrieves descriptions of all available configuration options for an environment named my-env:
    ::

      response = client.describe_configuration_options(
          ApplicationName='my-app',
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Options': [
              {
                  'ChangeSeverity': 'NoInterruption',
                  'DefaultValue': '30',
                  'MaxValue': 300,
                  'MinValue': 5,
                  'Name': 'Interval',
                  'Namespace': 'aws:elb:healthcheck',
                  'UserDefined': False,
                  'ValueType': 'Scalar',
              },
              {
                  'ChangeSeverity': 'NoInterruption',
                  'DefaultValue': '2000000',
                  'MinValue': 0,
                  'Name': 'LowerThreshold',
                  'Namespace': 'aws:autoscaling:trigger',
                  'UserDefined': False,
                  'ValueType': 'Scalar',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_configuration_settings(**kwargs)

    

    Returns a description of the settings for the specified configuration set, that is, either a configuration template or the configuration set associated with a running environment.

     

    When describing the settings for the configuration set associated with a running environment, it is possible to receive two sets of setting descriptions. One is the deployed configuration set, and the other is a draft configuration of an environment that is either in the process of deployment or that failed to deploy.

     

    Related Topics

     

     
    *  DeleteEnvironmentConfiguration   
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings>`_    


    **Request Syntax** 
    ::

      response = client.describe_configuration_settings(
          ApplicationName='string',
          TemplateName='string',
          EnvironmentName='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The application for the environment or configuration template.

      

    
    :type TemplateName: string
    :param TemplateName: 

      The name of the configuration template to describe.

       

      Conditional: You must specify either this parameter or an EnvironmentName, but not both. If you specify both, AWS Elastic Beanstalk returns an ``InvalidParameterCombination`` error. If you do not specify either, AWS Elastic Beanstalk returns a ``MissingRequiredParameter`` error. 

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment to describe.

       

      Condition: You must specify either this or a TemplateName, but not both. If you specify both, AWS Elastic Beanstalk returns an ``InvalidParameterCombination`` error. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigurationSettings': [
                {
                    'SolutionStackName': 'string',
                    'PlatformArn': 'string',
                    'ApplicationName': 'string',
                    'TemplateName': 'string',
                    'Description': 'string',
                    'EnvironmentName': 'string',
                    'DeploymentStatus': 'deployed'|'pending'|'failed',
                    'DateCreated': datetime(2015, 1, 1),
                    'DateUpdated': datetime(2015, 1, 1),
                    'OptionSettings': [
                        {
                            'ResourceName': 'string',
                            'Namespace': 'string',
                            'OptionName': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The results from a request to change the configuration settings of an environment.

        
        

        - **ConfigurationSettings** *(list) --* 

          A list of  ConfigurationSettingsDescription . 

          
          

          - *(dict) --* 

            Describes the settings for a configuration set.

            
            

            - **SolutionStackName** *(string) --* 

              The name of the solution stack this configuration set uses.

              
            

            - **PlatformArn** *(string) --* 

              The ARN of the platform.

              
            

            - **ApplicationName** *(string) --* 

              The name of the application associated with this configuration set.

              
            

            - **TemplateName** *(string) --* 

              If not ``null`` , the name of the configuration template for this configuration set. 

              
            

            - **Description** *(string) --* 

              Describes this configuration set.

              
            

            - **EnvironmentName** *(string) --* 

              If not ``null`` , the name of the environment for this configuration set. 

              
            

            - **DeploymentStatus** *(string) --* 

              If this configuration set is associated with an environment, the ``DeploymentStatus`` parameter indicates the deployment status of this configuration set: 

               

               
              * ``null`` : This configuration is not associated with a running environment. 
               
              * ``pending`` : This is a draft configuration that is not deployed to the associated environment but is in the process of deploying. 
               
              * ``deployed`` : This is the configuration that is currently deployed to the associated running environment. 
               
              * ``failed`` : This is a draft configuration that failed to successfully deploy. 
               

              
            

            - **DateCreated** *(datetime) --* 

              The date (in UTC time) when this configuration set was created.

              
            

            - **DateUpdated** *(datetime) --* 

              The date (in UTC time) when this configuration set was last modified.

              
            

            - **OptionSettings** *(list) --* 

              A list of the configuration options and their values in this configuration set.

              
              

              - *(dict) --* 

                A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

                
                

                - **ResourceName** *(string) --* 

                  A unique resource name for a time-based scaling configuration option.

                  
                

                - **Namespace** *(string) --* 

                  A unique namespace identifying the option's associated AWS resource.

                  
                

                - **OptionName** *(string) --* 

                  The name of the configuration option.

                  
                

                - **Value** *(string) --* 

                  The current value for the configuration option.

                  
            
          
        
      
    

    **Examples** 

    The following operation retrieves configuration settings for an environment named my-env:
    ::

      response = client.describe_configuration_settings(
          ApplicationName='my-app',
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ConfigurationSettings': [
              {
                  'ApplicationName': 'my-app',
                  'DateCreated': datetime(2015, 8, 13, 19, 16, 25, 3, 225, 0),
                  'DateUpdated': datetime(2015, 8, 13, 23, 30, 7, 3, 225, 0),
                  'DeploymentStatus': 'deployed',
                  'Description': 'Environment created from the EB CLI using "eb create"',
                  'EnvironmentName': 'my-env',
                  'OptionSettings': [
                      {
                          'Namespace': 'aws:autoscaling:asg',
                          'OptionName': 'Availability Zones',
                          'ResourceName': 'AWSEBAutoScalingGroup',
                          'Value': 'Any',
                      },
                      {
                          'Namespace': 'aws:autoscaling:asg',
                          'OptionName': 'Cooldown',
                          'ResourceName': 'AWSEBAutoScalingGroup',
                          'Value': '360',
                      },
                      {
                          'Namespace': 'aws:elb:policies',
                          'OptionName': 'ConnectionDrainingTimeout',
                          'ResourceName': 'AWSEBLoadBalancer',
                          'Value': '20',
                      },
                      {
                          'Namespace': 'aws:elb:policies',
                          'OptionName': 'ConnectionSettingIdleTimeout',
                          'ResourceName': 'AWSEBLoadBalancer',
                          'Value': '60',
                      },
                  ],
                  'SolutionStackName': '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_environment_health(**kwargs)

    

    Returns information about the overall health of the specified environment. The **DescribeEnvironmentHealth** operation is only available with AWS Elastic Beanstalk Enhanced Health.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth>`_    


    **Request Syntax** 
    ::

      response = client.describe_environment_health(
          EnvironmentName='string',
          EnvironmentId='string',
          AttributeNames=[
              'Status'|'Color'|'Causes'|'ApplicationMetrics'|'InstancesHealth'|'All'|'HealthStatus'|'RefreshedAt',
          ]
      )
    :type EnvironmentName: string
    :param EnvironmentName: 

      Specify the environment by name.

       

      You must specify either this or an EnvironmentName, or both.

      

    
    :type EnvironmentId: string
    :param EnvironmentId: 

      Specify the environment by ID.

       

      You must specify either this or an EnvironmentName, or both.

      

    
    :type AttributeNames: list
    :param AttributeNames: 

      Specify the response elements to return. To retrieve all attributes, set to ``All`` . If no attribute names are specified, returns the name of the environment.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EnvironmentName': 'string',
            'HealthStatus': 'string',
            'Status': 'Green'|'Yellow'|'Red'|'Grey',
            'Color': 'string',
            'Causes': [
                'string',
            ],
            'ApplicationMetrics': {
                'Duration': 123,
                'RequestCount': 123,
                'StatusCodes': {
                    'Status2xx': 123,
                    'Status3xx': 123,
                    'Status4xx': 123,
                    'Status5xx': 123
                },
                'Latency': {
                    'P999': 123.0,
                    'P99': 123.0,
                    'P95': 123.0,
                    'P90': 123.0,
                    'P85': 123.0,
                    'P75': 123.0,
                    'P50': 123.0,
                    'P10': 123.0
                }
            },
            'InstancesHealth': {
                'NoData': 123,
                'Unknown': 123,
                'Pending': 123,
                'Ok': 123,
                'Info': 123,
                'Warning': 123,
                'Degraded': 123,
                'Severe': 123
            },
            'RefreshedAt': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 

        Health details for an AWS Elastic Beanstalk environment.

        
        

        - **EnvironmentName** *(string) --* 

          The environment's name.

          
        

        - **HealthStatus** *(string) --* 

          The `health status <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ of the environment. For example, ``Ok`` .

          
        

        - **Status** *(string) --* 

          The environment's operational status. ``Ready`` , ``Launching`` , ``Updating`` , ``Terminating`` , or ``Terminated`` .

          
        

        - **Color** *(string) --* 

          The `health color <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ of the environment.

          
        

        - **Causes** *(list) --* 

          Descriptions of the data that contributed to the environment's current health status.

          
          

          - *(string) --* 
      
        

        - **ApplicationMetrics** *(dict) --* 

          Application request metrics for the environment.

          
          

          - **Duration** *(integer) --* 

            The amount of time that the metrics cover (usually 10 seconds). For example, you might have 5 requests (``request_count`` ) within the most recent time slice of 10 seconds (``duration`` ).

            
          

          - **RequestCount** *(integer) --* 

            Average number of requests handled by the web server per second over the last 10 seconds.

            
          

          - **StatusCodes** *(dict) --* 

            Represents the percentage of requests over the last 10 seconds that resulted in each type of status code response.

            
            

            - **Status2xx** *(integer) --* 

              The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201, etc.) status code.

              
            

            - **Status3xx** *(integer) --* 

              The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301, etc.) status code.

              
            

            - **Status4xx** *(integer) --* 

              The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401, etc.) status code.

              
            

            - **Status5xx** *(integer) --* 

              The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501, etc.) status code.

              
        
          

          - **Latency** *(dict) --* 

            Represents the average latency for the slowest X percent of requests over the last 10 seconds. Latencies are in seconds with one millisecond resolution.

            
            

            - **P999** *(float) --* 

              The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

              
            

            - **P99** *(float) --* 

              The average latency for the slowest 1 percent of requests over the last 10 seconds.

              
            

            - **P95** *(float) --* 

              The average latency for the slowest 5 percent of requests over the last 10 seconds.

              
            

            - **P90** *(float) --* 

              The average latency for the slowest 10 percent of requests over the last 10 seconds.

              
            

            - **P85** *(float) --* 

              The average latency for the slowest 15 percent of requests over the last 10 seconds.

              
            

            - **P75** *(float) --* 

              The average latency for the slowest 25 percent of requests over the last 10 seconds.

              
            

            - **P50** *(float) --* 

              The average latency for the slowest 50 percent of requests over the last 10 seconds.

              
            

            - **P10** *(float) --* 

              The average latency for the slowest 90 percent of requests over the last 10 seconds.

              
        
      
        

        - **InstancesHealth** *(dict) --* 

          Summary health information for the instances in the environment.

          
          

          - **NoData** *(integer) --* 

             **Grey.** AWS Elastic Beanstalk and the health agent are reporting no data on an instance.

            
          

          - **Unknown** *(integer) --* 

             **Grey.** AWS Elastic Beanstalk and the health agent are reporting an insufficient amount of data on an instance.

            
          

          - **Pending** *(integer) --* 

             **Grey.** An operation is in progress on an instance within the command timeout.

            
          

          - **Ok** *(integer) --* 

             **Green.** An instance is passing health checks and the health agent is not reporting any problems.

            
          

          - **Info** *(integer) --* 

             **Green.** An operation is in progress on an instance.

            
          

          - **Warning** *(integer) --* 

             **Yellow.** The health agent is reporting a moderate number of request failures or other issues for an instance or environment.

            
          

          - **Degraded** *(integer) --* 

             **Red.** The health agent is reporting a high number of request failures or other issues for an instance or environment.

            
          

          - **Severe** *(integer) --* 

             **Red.** The health agent is reporting a very high number of request failures or other issues for an instance or environment.

            
      
        

        - **RefreshedAt** *(datetime) --* 

          The date and time that the health information was retrieved.

          
    

    **Examples** 

    The following operation retrieves overall health information for an environment named my-env:
    ::

      response = client.describe_environment_health(
          AttributeNames=[
              'All',
          ],
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ApplicationMetrics': {
              'Duration': 10,
              'Latency': {
                  'P10': 0.001,
                  'P50': 0.001,
                  'P75': 0.002,
                  'P85': 0.003,
                  'P90': 0.003,
                  'P95': 0.004,
                  'P99': 0.004,
                  'P999': 0.004,
              },
              'RequestCount': 45,
              'StatusCodes': {
                  'Status2xx': 45,
                  'Status3xx': 0,
                  'Status4xx': 0,
                  'Status5xx': 0,
              },
          },
          'Causes': [
          ],
          'Color': 'Green',
          'EnvironmentName': 'my-env',
          'HealthStatus': 'Ok',
          'InstancesHealth': {
              'Degraded': 0,
              'Info': 0,
              'NoData': 0,
              'Ok': 1,
              'Pending': 0,
              'Severe': 0,
              'Unknown': 0,
              'Warning': 0,
          },
          'RefreshedAt': datetime(2015, 8, 20, 21, 9, 18, 3, 232, 0),
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_environment_managed_action_history(**kwargs)

    

    Lists an environment's completed and failed managed actions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory>`_    


    **Request Syntax** 
    ::

      response = client.describe_environment_managed_action_history(
          EnvironmentId='string',
          EnvironmentName='string',
          NextToken='string',
          MaxItems=123
      )
    :type EnvironmentId: string
    :param EnvironmentId: 

      The environment ID of the target environment.

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the target environment.

      

    
    :type NextToken: string
    :param NextToken: 

      The pagination token returned by a previous request.

      

    
    :type MaxItems: integer
    :param MaxItems: 

      The maximum number of items to return for a single request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ManagedActionHistoryItems': [
                {
                    'ActionId': 'string',
                    'ActionType': 'InstanceRefresh'|'PlatformUpdate'|'Unknown',
                    'ActionDescription': 'string',
                    'FailureType': 'UpdateCancelled'|'CancellationFailed'|'RollbackFailed'|'RollbackSuccessful'|'InternalFailure'|'InvalidEnvironmentState'|'PermissionsError',
                    'Status': 'Completed'|'Failed'|'Unknown',
                    'FailureDescription': 'string',
                    'ExecutedTime': datetime(2015, 1, 1),
                    'FinishedTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A result message containing a list of completed and failed managed actions.

        
        

        - **ManagedActionHistoryItems** *(list) --* 

          A list of completed and failed managed actions.

          
          

          - *(dict) --* 

            The record of a completed or failed managed action.

            
            

            - **ActionId** *(string) --* 

              A unique identifier for the managed action.

              
            

            - **ActionType** *(string) --* 

              The type of the managed action.

              
            

            - **ActionDescription** *(string) --* 

              A description of the managed action.

              
            

            - **FailureType** *(string) --* 

              If the action failed, the type of failure.

              
            

            - **Status** *(string) --* 

              The status of the action.

              
            

            - **FailureDescription** *(string) --* 

              If the action failed, a description of the failure.

              
            

            - **ExecutedTime** *(datetime) --* 

              The date and time that the action started executing.

              
            

            - **FinishedTime** *(datetime) --* 

              The date and time that the action finished executing.

              
        
      
        

        - **NextToken** *(string) --* 

          A pagination token that you pass to  DescribeEnvironmentManagedActionHistory to get the next page of results.

          
    

  .. py:method:: describe_environment_managed_actions(**kwargs)

    

    Lists an environment's upcoming and in-progress managed actions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActions>`_    


    **Request Syntax** 
    ::

      response = client.describe_environment_managed_actions(
          EnvironmentName='string',
          EnvironmentId='string',
          Status='Scheduled'|'Pending'|'Running'|'Unknown'
      )
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the target environment.

      

    
    :type EnvironmentId: string
    :param EnvironmentId: 

      The environment ID of the target environment.

      

    
    :type Status: string
    :param Status: 

      To show only actions with a particular status, specify a status.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ManagedActions': [
                {
                    'ActionId': 'string',
                    'ActionDescription': 'string',
                    'ActionType': 'InstanceRefresh'|'PlatformUpdate'|'Unknown',
                    'Status': 'Scheduled'|'Pending'|'Running'|'Unknown',
                    'WindowStartTime': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result message containing a list of managed actions.

        
        

        - **ManagedActions** *(list) --* 

          A list of upcoming and in-progress managed actions.

          
          

          - *(dict) --* 

            The record of an upcoming or in-progress managed action.

            
            

            - **ActionId** *(string) --* 

              A unique identifier for the managed action.

              
            

            - **ActionDescription** *(string) --* 

              A description of the managed action.

              
            

            - **ActionType** *(string) --* 

              The type of managed action.

              
            

            - **Status** *(string) --* 

              The status of the managed action. If the action is ``Scheduled`` , you can apply it immediately with  ApplyEnvironmentManagedAction .

              
            

            - **WindowStartTime** *(datetime) --* 

              The start time of the maintenance window in which the managed action will execute.

              
        
      
    

  .. py:method:: describe_environment_resources(**kwargs)

    

    Returns AWS resources for this environment.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources>`_    


    **Request Syntax** 
    ::

      response = client.describe_environment_resources(
          EnvironmentId='string',
          EnvironmentName='string'
      )
    :type EnvironmentId: string
    :param EnvironmentId: 

      The ID of the environment to retrieve AWS resource usage data.

       

      Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment to retrieve AWS resource usage data.

       

      Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EnvironmentResources': {
                'EnvironmentName': 'string',
                'AutoScalingGroups': [
                    {
                        'Name': 'string'
                    },
                ],
                'Instances': [
                    {
                        'Id': 'string'
                    },
                ],
                'LaunchConfigurations': [
                    {
                        'Name': 'string'
                    },
                ],
                'LoadBalancers': [
                    {
                        'Name': 'string'
                    },
                ],
                'Triggers': [
                    {
                        'Name': 'string'
                    },
                ],
                'Queues': [
                    {
                        'Name': 'string',
                        'URL': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message containing a list of environment resource descriptions.

        
        

        - **EnvironmentResources** *(dict) --* 

          A list of  EnvironmentResourceDescription . 

          
          

          - **EnvironmentName** *(string) --* 

            The name of the environment.

            
          

          - **AutoScalingGroups** *(list) --* 

            The ``AutoScalingGroups`` used by this environment. 

            
            

            - *(dict) --* 

              Describes an Auto Scaling launch configuration.

              
              

              - **Name** *(string) --* 

                The name of the ``AutoScalingGroup`` . 

                
          
        
          

          - **Instances** *(list) --* 

            The Amazon EC2 instances used by this environment.

            
            

            - *(dict) --* 

              The description of an Amazon EC2 instance.

              
              

              - **Id** *(string) --* 

                The ID of the Amazon EC2 instance.

                
          
        
          

          - **LaunchConfigurations** *(list) --* 

            The Auto Scaling launch configurations in use by this environment.

            
            

            - *(dict) --* 

              Describes an Auto Scaling launch configuration.

              
              

              - **Name** *(string) --* 

                The name of the launch configuration.

                
          
        
          

          - **LoadBalancers** *(list) --* 

            The LoadBalancers in use by this environment.

            
            

            - *(dict) --* 

              Describes a LoadBalancer.

              
              

              - **Name** *(string) --* 

                The name of the LoadBalancer.

                
          
        
          

          - **Triggers** *(list) --* 

            The ``AutoScaling`` triggers in use by this environment. 

            
            

            - *(dict) --* 

              Describes a trigger.

              
              

              - **Name** *(string) --* 

                The name of the trigger.

                
          
        
          

          - **Queues** *(list) --* 

            The queues used by this environment.

            
            

            - *(dict) --* 

              Describes a queue.

              
              

              - **Name** *(string) --* 

                The name of the queue.

                
              

              - **URL** *(string) --* 

                The URL of the queue.

                
          
        
      
    

    **Examples** 

    The following operation retrieves information about resources in an environment named my-env:
    ::

      response = client.describe_environment_resources(
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'EnvironmentResources': {
              'AutoScalingGroups': [
                  {
                      'Name': 'awseb-e-qu3fyyjyjs-stack-AWSEBAutoScalingGroup-QSB2ZO88SXZT',
                  },
              ],
              'EnvironmentName': 'my-env',
              'Instances': [
                  {
                      'Id': 'i-0c91c786',
                  },
              ],
              'LaunchConfigurations': [
                  {
                      'Name': 'awseb-e-qu3fyyjyjs-stack-AWSEBAutoScalingLaunchConfiguration-1UUVQIBC96TQ2',
                  },
              ],
              'LoadBalancers': [
                  {
                      'Name': 'awseb-e-q-AWSEBLoa-1EEPZ0K98BIF0',
                  },
              ],
              'Queues': [
              ],
              'Triggers': [
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_environments(**kwargs)

    

    Returns descriptions for existing environments.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEnvironments>`_    


    **Request Syntax** 
    ::

      response = client.describe_environments(
          ApplicationName='string',
          VersionLabel='string',
          EnvironmentIds=[
              'string',
          ],
          EnvironmentNames=[
              'string',
          ],
          IncludeDeleted=True|False,
          IncludedDeletedBackTo=datetime(2015, 1, 1),
          MaxRecords=123,
          NextToken='string'
      )
    :type ApplicationName: string
    :param ApplicationName: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application.

      

    
    :type VersionLabel: string
    :param VersionLabel: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application version.

      

    
    :type EnvironmentIds: list
    :param EnvironmentIds: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs.

      

    
      - *(string) --* 

      
  
    :type EnvironmentNames: list
    :param EnvironmentNames: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names.

      

    
      - *(string) --* 

      
  
    :type IncludeDeleted: boolean
    :param IncludeDeleted: 

      Indicates whether to include deleted environments:

       

       ``true`` : Environments that have been deleted after ``IncludedDeletedBackTo`` are displayed.

       

       ``false`` : Do not include deleted environments.

      

    
    :type IncludedDeletedBackTo: datetime
    :param IncludedDeletedBackTo: 

      If specified when ``IncludeDeleted`` is set to ``true`` , then environments deleted after this date are displayed. 

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      For a paginated request. Specify a maximum number of environments to include in each response.

       

      If no ``MaxRecords`` is specified, all available environments are retrieved in a single response.

      

    
    :type NextToken: string
    :param NextToken: 

      For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.

       

      If no ``NextToken`` is specified, the first page is retrieved.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Environments': [
                {
                    'EnvironmentName': 'string',
                    'EnvironmentId': 'string',
                    'ApplicationName': 'string',
                    'VersionLabel': 'string',
                    'SolutionStackName': 'string',
                    'PlatformArn': 'string',
                    'TemplateName': 'string',
                    'Description': 'string',
                    'EndpointURL': 'string',
                    'CNAME': 'string',
                    'DateCreated': datetime(2015, 1, 1),
                    'DateUpdated': datetime(2015, 1, 1),
                    'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
                    'AbortableOperationInProgress': True|False,
                    'Health': 'Green'|'Yellow'|'Red'|'Grey',
                    'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
                    'Resources': {
                        'LoadBalancer': {
                            'LoadBalancerName': 'string',
                            'Domain': 'string',
                            'Listeners': [
                                {
                                    'Protocol': 'string',
                                    'Port': 123
                                },
                            ]
                        }
                    },
                    'Tier': {
                        'Name': 'string',
                        'Type': 'string',
                        'Version': 'string'
                    },
                    'EnvironmentLinks': [
                        {
                            'LinkName': 'string',
                            'EnvironmentName': 'string'
                        },
                    ],
                    'EnvironmentArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message containing a list of environment descriptions.

        
        

        - **Environments** *(list) --* 

          Returns an  EnvironmentDescription list. 

          
          

          - *(dict) --* 

            Describes the properties of an environment.

            
            

            - **EnvironmentName** *(string) --* 

              The name of this environment.

              
            

            - **EnvironmentId** *(string) --* 

              The ID of this environment.

              
            

            - **ApplicationName** *(string) --* 

              The name of the application associated with this environment.

              
            

            - **VersionLabel** *(string) --* 

              The application version deployed in this environment.

              
            

            - **SolutionStackName** *(string) --* 

              The name of the ``SolutionStack`` deployed with this environment. 

              
            

            - **PlatformArn** *(string) --* 

              The ARN of the platform.

              
            

            - **TemplateName** *(string) --* 

              The name of the configuration template used to originally launch this environment.

              
            

            - **Description** *(string) --* 

              Describes this environment.

              
            

            - **EndpointURL** *(string) --* 

              For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.

              
            

            - **CNAME** *(string) --* 

              The URL to the CNAME for this environment.

              
            

            - **DateCreated** *(datetime) --* 

              The creation date for this environment.

              
            

            - **DateUpdated** *(datetime) --* 

              The last modified date for this environment.

              
            

            - **Status** *(string) --* 

              The current operational status of the environment:

               

               
              * ``Launching`` : Environment is in the process of initial deployment. 
               
              * ``Updating`` : Environment is in the process of updating its configuration settings or application version. 
               
              * ``Ready`` : Environment is available to have an action performed on it, such as update or terminate. 
               
              * ``Terminating`` : Environment is in the shut-down process. 
               
              * ``Terminated`` : Environment is not running. 
               

              
            

            - **AbortableOperationInProgress** *(boolean) --* 

              Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.

               

               ``true:`` There is an update in progress. 

               

               ``false:`` There are no updates currently in progress. 

              
            

            - **Health** *(string) --* 

              Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:

               

               
              * ``Red`` : Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment. 
               
              * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur for an environment. 
               
              * ``Green`` : Indicates the environment is healthy and fully functional. 
               
              * ``Grey`` : Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an ``UpdateEnvironment`` or ``RestartEnvironement`` request. 
               

               

              Default: ``Grey``  

              
            

            - **HealthStatus** *(string) --* 

              Returns the health status of the application running in your environment. For more information, see `Health Colors and Statuses <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

              
            

            - **Resources** *(dict) --* 

              The description of the AWS resources used by this environment.

              
              

              - **LoadBalancer** *(dict) --* 

                Describes the LoadBalancer.

                
                

                - **LoadBalancerName** *(string) --* 

                  The name of the LoadBalancer.

                  
                

                - **Domain** *(string) --* 

                  The domain name of the LoadBalancer.

                  
                

                - **Listeners** *(list) --* 

                  A list of Listeners used by the LoadBalancer.

                  
                  

                  - *(dict) --* 

                    Describes the properties of a Listener for the LoadBalancer.

                    
                    

                    - **Protocol** *(string) --* 

                      The protocol that is used by the Listener.

                      
                    

                    - **Port** *(integer) --* 

                      The port that is used by the Listener.

                      
                
              
            
          
            

            - **Tier** *(dict) --* 

              Describes the current tier of this environment.

              
              

              - **Name** *(string) --* 

                The name of this environment tier.

                
              

              - **Type** *(string) --* 

                The type of this environment tier.

                
              

              - **Version** *(string) --* 

                The version of this environment tier.

                
          
            

            - **EnvironmentLinks** *(list) --* 

              A list of links to other environments in the same group.

              
              

              - *(dict) --* 

                A link to another environment, defined in the environment's manifest. Links provide connection information in system properties that can be used to connect to another environment in the same group. See `Environment Manifest (env.yaml) <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.

                
                

                - **LinkName** *(string) --* 

                  The name of the link.

                  
                

                - **EnvironmentName** *(string) --* 

                  The name of the linked environment (the dependency).

                  
            
          
            

            - **EnvironmentArn** *(string) --* 

              The environment's Amazon Resource Name (ARN), which can be used in other API reuqests that require an ARN.

              
        
      
        

        - **NextToken** *(string) --* 

          In a paginated request, the token that you can pass in a subsequent request to get the next response page.

          
    

    **Examples** 

    The following operation retrieves information about an environment named my-env:
    ::

      response = client.describe_environments(
          EnvironmentNames=[
              'my-env',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Environments': [
              {
                  'AbortableOperationInProgress': False,
                  'ApplicationName': 'my-app',
                  'CNAME': 'my-env.elasticbeanstalk.com',
                  'DateCreated': datetime(2015, 8, 7, 20, 48, 49, 4, 219, 0),
                  'DateUpdated': datetime(2015, 8, 12, 18, 16, 55, 2, 224, 0),
                  'EndpointURL': 'awseb-e-w-AWSEBLoa-1483140XB0Q4L-109QXY8121.us-west-2.elb.amazonaws.com',
                  'EnvironmentId': 'e-rpqsewtp2j',
                  'EnvironmentName': 'my-env',
                  'Health': 'Green',
                  'SolutionStackName': '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
                  'Status': 'Ready',
                  'Tier': {
                      'Name': 'WebServer',
                      'Type': 'Standard',
                      'Version': ' ',
                  },
                  'VersionLabel': '7f58-stage-150812_025409',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_events(**kwargs)

    

    Returns list of event descriptions matching criteria up to the last 6 weeks.

     

    .. note::

       

      This action returns the most recent 1,000 events from the specified ``NextToken`` .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEvents>`_    


    **Request Syntax** 
    ::

      response = client.describe_events(
          ApplicationName='string',
          VersionLabel='string',
          TemplateName='string',
          EnvironmentId='string',
          EnvironmentName='string',
          PlatformArn='string',
          RequestId='string',
          Severity='TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          MaxRecords=123,
          NextToken='string'
      )
    :type ApplicationName: string
    :param ApplicationName: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.

      

    
    :type VersionLabel: string
    :param VersionLabel: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.

      

    
    :type TemplateName: string
    :param TemplateName: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.

      

    
    :type EnvironmentId: string
    :param EnvironmentId: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.

      

    
    :type PlatformArn: string
    :param PlatformArn: 

      The ARN of the version of the custom platform.

      

    
    :type RequestId: string
    :param RequestId: 

      If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.

      

    
    :type Severity: string
    :param Severity: 

      If specified, limits the events returned from this call to include only those with the specified severity or higher.

      

    
    :type StartTime: datetime
    :param StartTime: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.

      

    
    :type EndTime: datetime
    :param EndTime: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the ``EndTime`` . 

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      Specifies the maximum number of events that can be returned, beginning with the most recent event.

      

    
    :type NextToken: string
    :param NextToken: 

      Pagination token. If specified, the events return the next batch of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Events': [
                {
                    'EventDate': datetime(2015, 1, 1),
                    'Message': 'string',
                    'ApplicationName': 'string',
                    'VersionLabel': 'string',
                    'TemplateName': 'string',
                    'EnvironmentName': 'string',
                    'PlatformArn': 'string',
                    'RequestId': 'string',
                    'Severity': 'TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message wrapping a list of event descriptions.

        
        

        - **Events** *(list) --* 

          A list of  EventDescription . 

          
          

          - *(dict) --* 

            Describes an event.

            
            

            - **EventDate** *(datetime) --* 

              The date when the event occurred.

              
            

            - **Message** *(string) --* 

              The event message.

              
            

            - **ApplicationName** *(string) --* 

              The application associated with the event.

              
            

            - **VersionLabel** *(string) --* 

              The release label for the application version associated with this event.

              
            

            - **TemplateName** *(string) --* 

              The name of the configuration associated with this event.

              
            

            - **EnvironmentName** *(string) --* 

              The name of the environment associated with this event.

              
            

            - **PlatformArn** *(string) --* 

              The ARN of the platform.

              
            

            - **RequestId** *(string) --* 

              The web service request ID for the activity of this event.

              
            

            - **Severity** *(string) --* 

              The severity level of this event.

              
        
      
        

        - **NextToken** *(string) --* 

          If returned, this indicates that there are more results to obtain. Use this token in the next  DescribeEvents call to get the next batch of events. 

          
    

    **Examples** 

    The following operation retrieves events for an environment named my-env:
    ::

      response = client.describe_events(
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Events': [
              {
                  'ApplicationName': 'my-app',
                  'EnvironmentName': 'my-env',
                  'EventDate': datetime(2015, 8, 20, 7, 6, 53, 3, 232, 0),
                  'Message': 'Environment health has transitioned from Info to Ok.',
                  'Severity': 'INFO',
              },
              {
                  'ApplicationName': 'my-app',
                  'EnvironmentName': 'my-env',
                  'EventDate': datetime(2015, 8, 20, 7, 6, 2, 3, 232, 0),
                  'Message': 'Environment update completed successfully.',
                  'RequestId': 'b7f3960b-4709-11e5-ba1e-07e16200da41',
                  'Severity': 'INFO',
              },
              {
                  'ApplicationName': 'my-app',
                  'EnvironmentName': 'my-env',
                  'EventDate': datetime(2015, 8, 13, 19, 16, 27, 3, 225, 0),
                  'Message': 'Using elasticbeanstalk-us-west-2-012445113685 as Amazon S3 storage bucket for environment data.',
                  'RequestId': 'ca8dfbf6-41ef-11e5-988b-651aa638f46b',
                  'Severity': 'INFO',
              },
              {
                  'ApplicationName': 'my-app',
                  'EnvironmentName': 'my-env',
                  'EventDate': datetime(2015, 8, 13, 19, 16, 26, 3, 225, 0),
                  'Message': 'createEnvironment is starting.',
                  'RequestId': 'cdfba8f6-41ef-11e5-988b-65638f41aa6b',
                  'Severity': 'INFO',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_instances_health(**kwargs)

    

    Retrives detailed information about the health of instances in your AWS Elastic Beanstalk. This operation requires `enhanced health reporting <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeInstancesHealth>`_    


    **Request Syntax** 
    ::

      response = client.describe_instances_health(
          EnvironmentName='string',
          EnvironmentId='string',
          AttributeNames=[
              'HealthStatus'|'Color'|'Causes'|'ApplicationMetrics'|'RefreshedAt'|'LaunchedAt'|'System'|'Deployment'|'AvailabilityZone'|'InstanceType'|'All',
          ],
          NextToken='string'
      )
    :type EnvironmentName: string
    :param EnvironmentName: 

      Specify the AWS Elastic Beanstalk environment by name.

      

    
    :type EnvironmentId: string
    :param EnvironmentId: 

      Specify the AWS Elastic Beanstalk environment by ID.

      

    
    :type AttributeNames: list
    :param AttributeNames: 

      Specifies the response elements you wish to receive. To retrieve all attributes, set to ``All`` . If no attribute names are specified, returns a list of instances.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      Specify the pagination token returned by a previous call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InstanceHealthList': [
                {
                    'InstanceId': 'string',
                    'HealthStatus': 'string',
                    'Color': 'string',
                    'Causes': [
                        'string',
                    ],
                    'LaunchedAt': datetime(2015, 1, 1),
                    'ApplicationMetrics': {
                        'Duration': 123,
                        'RequestCount': 123,
                        'StatusCodes': {
                            'Status2xx': 123,
                            'Status3xx': 123,
                            'Status4xx': 123,
                            'Status5xx': 123
                        },
                        'Latency': {
                            'P999': 123.0,
                            'P99': 123.0,
                            'P95': 123.0,
                            'P90': 123.0,
                            'P85': 123.0,
                            'P75': 123.0,
                            'P50': 123.0,
                            'P10': 123.0
                        }
                    },
                    'System': {
                        'CPUUtilization': {
                            'User': 123.0,
                            'Nice': 123.0,
                            'System': 123.0,
                            'Idle': 123.0,
                            'IOWait': 123.0,
                            'IRQ': 123.0,
                            'SoftIRQ': 123.0
                        },
                        'LoadAverage': [
                            123.0,
                        ]
                    },
                    'Deployment': {
                        'VersionLabel': 'string',
                        'DeploymentId': 123,
                        'Status': 'string',
                        'DeploymentTime': datetime(2015, 1, 1)
                    },
                    'AvailabilityZone': 'string',
                    'InstanceType': 'string'
                },
            ],
            'RefreshedAt': datetime(2015, 1, 1),
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Detailed health information about the Amazon EC2 instances in an AWS Elastic Beanstalk environment.

        
        

        - **InstanceHealthList** *(list) --* 

          Detailed health information about each instance.

          
          

          - *(dict) --* 

            Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk environment.

            
            

            - **InstanceId** *(string) --* 

              The ID of the Amazon EC2 instance.

              
            

            - **HealthStatus** *(string) --* 

              Returns the health status of the specified instance. For more information, see `Health Colors and Statuses <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

              
            

            - **Color** *(string) --* 

              Represents the color indicator that gives you information about the health of the EC2 instance. For more information, see `Health Colors and Statuses <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

              
            

            - **Causes** *(list) --* 

              Represents the causes, which provide more information about the current health status.

              
              

              - *(string) --* 
          
            

            - **LaunchedAt** *(datetime) --* 

              The time at which the EC2 instance was launched.

              
            

            - **ApplicationMetrics** *(dict) --* 

              Request metrics from your application.

              
              

              - **Duration** *(integer) --* 

                The amount of time that the metrics cover (usually 10 seconds). For example, you might have 5 requests (``request_count`` ) within the most recent time slice of 10 seconds (``duration`` ).

                
              

              - **RequestCount** *(integer) --* 

                Average number of requests handled by the web server per second over the last 10 seconds.

                
              

              - **StatusCodes** *(dict) --* 

                Represents the percentage of requests over the last 10 seconds that resulted in each type of status code response.

                
                

                - **Status2xx** *(integer) --* 

                  The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201, etc.) status code.

                  
                

                - **Status3xx** *(integer) --* 

                  The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301, etc.) status code.

                  
                

                - **Status4xx** *(integer) --* 

                  The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401, etc.) status code.

                  
                

                - **Status5xx** *(integer) --* 

                  The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501, etc.) status code.

                  
            
              

              - **Latency** *(dict) --* 

                Represents the average latency for the slowest X percent of requests over the last 10 seconds. Latencies are in seconds with one millisecond resolution.

                
                

                - **P999** *(float) --* 

                  The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

                  
                

                - **P99** *(float) --* 

                  The average latency for the slowest 1 percent of requests over the last 10 seconds.

                  
                

                - **P95** *(float) --* 

                  The average latency for the slowest 5 percent of requests over the last 10 seconds.

                  
                

                - **P90** *(float) --* 

                  The average latency for the slowest 10 percent of requests over the last 10 seconds.

                  
                

                - **P85** *(float) --* 

                  The average latency for the slowest 15 percent of requests over the last 10 seconds.

                  
                

                - **P75** *(float) --* 

                  The average latency for the slowest 25 percent of requests over the last 10 seconds.

                  
                

                - **P50** *(float) --* 

                  The average latency for the slowest 50 percent of requests over the last 10 seconds.

                  
                

                - **P10** *(float) --* 

                  The average latency for the slowest 90 percent of requests over the last 10 seconds.

                  
            
          
            

            - **System** *(dict) --* 

              Operating system metrics from the instance.

              
              

              - **CPUUtilization** *(dict) --* 

                CPU utilization metrics for the instance.

                
                

                - **User** *(float) --* 

                  Percentage of time that the CPU has spent in the ``User`` state over the last 10 seconds.

                  
                

                - **Nice** *(float) --* 

                  Percentage of time that the CPU has spent in the ``Nice`` state over the last 10 seconds.

                  
                

                - **System** *(float) --* 

                  Percentage of time that the CPU has spent in the ``System`` state over the last 10 seconds.

                  
                

                - **Idle** *(float) --* 

                  Percentage of time that the CPU has spent in the ``Idle`` state over the last 10 seconds.

                  
                

                - **IOWait** *(float) --* 

                  Percentage of time that the CPU has spent in the ``I/O Wait`` state over the last 10 seconds.

                  
                

                - **IRQ** *(float) --* 

                  Percentage of time that the CPU has spent in the ``IRQ`` state over the last 10 seconds.

                  
                

                - **SoftIRQ** *(float) --* 

                  Percentage of time that the CPU has spent in the ``SoftIRQ`` state over the last 10 seconds.

                  
            
              

              - **LoadAverage** *(list) --* 

                Load average in the last 1-minute, 5-minute, and 15-minute periods. For more information, see `Operating System Metrics <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics.html#health-enhanced-metrics-os>`__ .

                
                

                - *(float) --* 
            
          
            

            - **Deployment** *(dict) --* 

              Information about the most recent deployment to an instance.

              
              

              - **VersionLabel** *(string) --* 

                The version label of the application version in the deployment.

                
              

              - **DeploymentId** *(integer) --* 

                The ID of the deployment. This number increases by one each time that you deploy source code or change instance configuration settings.

                
              

              - **Status** *(string) --* 

                The status of the deployment:

                 

                 
                * ``In Progress`` : The deployment is in progress. 
                 
                * ``Deployed`` : The deployment succeeded. 
                 
                * ``Failed`` : The deployment failed. 
                 

                
              

              - **DeploymentTime** *(datetime) --* 

                For in-progress deployments, the time that the deployment started.

                 

                For completed deployments, the time that the deployment ended.

                
          
            

            - **AvailabilityZone** *(string) --* 

              The availability zone in which the instance runs.

              
            

            - **InstanceType** *(string) --* 

              The instance's type.

              
        
      
        

        - **RefreshedAt** *(datetime) --* 

          The date and time that the health information was retrieved.

          
        

        - **NextToken** *(string) --* 

          Pagination token for the next page of results, if available.

          
    

    **Examples** 

    The following operation retrieves health information for instances in an environment named my-env:
    ::

      response = client.describe_instances_health(
          AttributeNames=[
              'All',
          ],
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'InstanceHealthList': [
              {
                  'ApplicationMetrics': {
                      'Duration': 10,
                      'Latency': {
                          'P10': 0,
                          'P50': 0.001,
                          'P75': 0.002,
                          'P85': 0.003,
                          'P90': 0.004,
                          'P95': 0.005,
                          'P99': 0.006,
                          'P999': 0.006,
                      },
                      'RequestCount': 48,
                      'StatusCodes': {
                          'Status2xx': 47,
                          'Status3xx': 0,
                          'Status4xx': 1,
                          'Status5xx': 0,
                      },
                  },
                  'Causes': [
                  ],
                  'Color': 'Green',
                  'HealthStatus': 'Ok',
                  'InstanceId': 'i-08691cc7',
                  'LaunchedAt': datetime(2015, 8, 13, 19, 17, 9, 3, 225, 0),
                  'System': {
                      'CPUUtilization': {
                          'IOWait': 0.2,
                          'IRQ': 0,
                          'Idle': 97.8,
                          'Nice': 0.1,
                          'SoftIRQ': 0.1,
                          'System': 0.3,
                          'User': 1.5,
                      },
                      'LoadAverage': [
                          0,
                          0.02,
                          0.05,
                      ],
                  },
              },
          ],
          'RefreshedAt': datetime(2015, 8, 20, 21, 9, 8, 3, 232, 0),
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_platform_version(**kwargs)

    

    Describes the version of the platform.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribePlatformVersion>`_    


    **Request Syntax** 
    ::

      response = client.describe_platform_version(
          PlatformArn='string'
      )
    :type PlatformArn: string
    :param PlatformArn: 

      The ARN of the version of the platform.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PlatformDescription': {
                'PlatformArn': 'string',
                'PlatformOwner': 'string',
                'PlatformName': 'string',
                'PlatformVersion': 'string',
                'SolutionStackName': 'string',
                'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'PlatformCategory': 'string',
                'Description': 'string',
                'Maintainer': 'string',
                'OperatingSystemName': 'string',
                'OperatingSystemVersion': 'string',
                'ProgrammingLanguages': [
                    {
                        'Name': 'string',
                        'Version': 'string'
                    },
                ],
                'Frameworks': [
                    {
                        'Name': 'string',
                        'Version': 'string'
                    },
                ],
                'CustomAmiList': [
                    {
                        'VirtualizationType': 'string',
                        'ImageId': 'string'
                    },
                ],
                'SupportedTierList': [
                    'string',
                ],
                'SupportedAddonList': [
                    'string',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PlatformDescription** *(dict) --* 

          Detailed information about the version of the platform.

          
          

          - **PlatformArn** *(string) --* 

            The ARN of the platform.

            
          

          - **PlatformOwner** *(string) --* 

            The AWS account ID of the person who created the platform.

            
          

          - **PlatformName** *(string) --* 

            The name of the platform.

            
          

          - **PlatformVersion** *(string) --* 

            The version of the platform.

            
          

          - **SolutionStackName** *(string) --* 

            The name of the solution stack used by the platform.

            
          

          - **PlatformStatus** *(string) --* 

            The status of the platform.

            
          

          - **DateCreated** *(datetime) --* 

            The date when the platform was created.

            
          

          - **DateUpdated** *(datetime) --* 

            The date when the platform was last updated.

            
          

          - **PlatformCategory** *(string) --* 

            The category of the platform.

            
          

          - **Description** *(string) --* 

            The description of the platform.

            
          

          - **Maintainer** *(string) --* 

            Information about the maintainer of the platform.

            
          

          - **OperatingSystemName** *(string) --* 

            The operating system used by the platform.

            
          

          - **OperatingSystemVersion** *(string) --* 

            The version of the operating system used by the platform.

            
          

          - **ProgrammingLanguages** *(list) --* 

            The programming languages supported by the platform.

            
            

            - *(dict) --* 

              A programming language supported by the platform.

              
              

              - **Name** *(string) --* 

                The name of the programming language.

                
              

              - **Version** *(string) --* 

                The version of the programming language.

                
          
        
          

          - **Frameworks** *(list) --* 

            The frameworks supported by the platform.

            
            

            - *(dict) --* 

              A framework supported by the custom platform.

              
              

              - **Name** *(string) --* 

                The name of the framework.

                
              

              - **Version** *(string) --* 

                The version of the framework.

                
          
        
          

          - **CustomAmiList** *(list) --* 

            The custom AMIs supported by the platform.

            
            

            - *(dict) --* 

              A custom AMI available to platforms.

              
              

              - **VirtualizationType** *(string) --* 

                The type of virtualization used to create the custom AMI.

                
              

              - **ImageId** *(string) --* 

                THe ID of the image used to create the custom AMI.

                
          
        
          

          - **SupportedTierList** *(list) --* 

            The tiers supported by the platform.

            
            

            - *(string) --* 
        
          

          - **SupportedAddonList** *(list) --* 

            The additions supported by the platform.

            
            

            - *(string) --* 
        
      
    

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

        


  .. py:method:: list_available_solution_stacks()

    

    Returns a list of the available solution stack names, with the public version first and then in reverse chronological order.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks>`_    


    **Request Syntax** 

    ::

      response = client.list_available_solution_stacks()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SolutionStacks': [
                'string',
            ],
            'SolutionStackDetails': [
                {
                    'SolutionStackName': 'string',
                    'PermittedFileTypes': [
                        'string',
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of available AWS Elastic Beanstalk solution stacks.

        
        

        - **SolutionStacks** *(list) --* 

          A list of available solution stacks.

          
          

          - *(string) --* 
      
        

        - **SolutionStackDetails** *(list) --* 

          A list of available solution stacks and their  SolutionStackDescription . 

          
          

          - *(dict) --* 

            Describes the solution stack.

            
            

            - **SolutionStackName** *(string) --* 

              The name of the solution stack.

              
            

            - **PermittedFileTypes** *(list) --* 

              The permitted file types allowed for a solution stack.

              
              

              - *(string) --* 
          
        
      
    

    **Examples** 

    The following operation lists solution stacks for all currently available platform configurations and any that you have used in the past:
    ::

      response = client.list_available_solution_stacks(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SolutionStackDetails': [
              {
                  'PermittedFileTypes': [
                      'zip',
                  ],
                  'SolutionStackName': '64bit Amazon Linux 2015.03 v2.0.0 running Node.js',
              },
          ],
          'SolutionStacks': [
              '64bit Amazon Linux 2015.03 v2.0.0 running Node.js',
              '64bit Amazon Linux 2015.03 v2.0.0 running PHP 5.6',
              '64bit Amazon Linux 2015.03 v2.0.0 running PHP 5.5',
              '64bit Amazon Linux 2015.03 v2.0.0 running PHP 5.4',
              '64bit Amazon Linux 2015.03 v2.0.0 running Python 3.4',
              '64bit Amazon Linux 2015.03 v2.0.0 running Python 2.7',
              '64bit Amazon Linux 2015.03 v2.0.0 running Python',
              '64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.2 (Puma)',
              '64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.2 (Passenger Standalone)',
              '64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.1 (Puma)',
              '64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.1 (Passenger Standalone)',
              '64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.0 (Puma)',
              '64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.0 (Passenger Standalone)',
              '64bit Amazon Linux 2015.03 v2.0.0 running Ruby 1.9.3',
              '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
              '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 7 Java 7',
              '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 7 Java 6',
              '64bit Windows Server Core 2012 R2 running IIS 8.5',
              '64bit Windows Server 2012 R2 running IIS 8.5',
              '64bit Windows Server 2012 running IIS 8',
              '64bit Windows Server 2008 R2 running IIS 7.5',
              '64bit Amazon Linux 2015.03 v2.0.0 running Docker 1.6.2',
              '64bit Amazon Linux 2015.03 v2.0.0 running Multi-container Docker 1.6.2 (Generic)',
              '64bit Debian jessie v2.0.0 running GlassFish 4.1 Java 8 (Preconfigured - Docker)',
              '64bit Debian jessie v2.0.0 running GlassFish 4.0 Java 7 (Preconfigured - Docker)',
              '64bit Debian jessie v2.0.0 running Go 1.4 (Preconfigured - Docker)',
              '64bit Debian jessie v2.0.0 running Go 1.3 (Preconfigured - Docker)',
              '64bit Debian jessie v2.0.0 running Python 3.4 (Preconfigured - Docker)',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_platform_versions(**kwargs)

    

    Lists the available platforms.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ListPlatformVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_platform_versions(
          Filters=[
              {
                  'Type': 'string',
                  'Operator': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxRecords=123,
          NextToken='string'
      )
    :type Filters: list
    :param Filters: 

      List only the platforms where the platform member value relates to one of the supplied values.

      

    
      - *(dict) --* 

        Specify criteria to restrict the results when listing custom platforms.

         

        The filter is evaluated as the expression:

         

         ``Type``  ``Operator``  ``Values[i]``  

        

      
        - **Type** *(string) --* 

          The custom platform attribute to which the filter values are applied.

           

          Valid Values: ``PlatformName`` | ``PlatformVersion`` | ``PlatformStatus`` | ``PlatformOwner``  

          

        
        - **Operator** *(string) --* 

          The operator to apply to the ``Type`` with each of the ``Values`` .

           

          Valid Values: ``=`` (equal to) | ``!=`` (not equal to) | ``<`` (less than) | ``<=`` (less than or equal to) | ``>`` (greater than) | ``>=`` (greater than or equal to) | ``contains`` | ``begins_with`` | ``ends_with``  

          

        
        - **Values** *(list) --* 

          The list of values applied to the custom platform attribute.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of platform values returned in one call.

      

    
    :type NextToken: string
    :param NextToken: 

      The starting index into the remaining list of platforms. Use the ``NextToken`` value from a previous ``ListPlatformVersion`` call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PlatformSummaryList': [
                {
                    'PlatformArn': 'string',
                    'PlatformOwner': 'string',
                    'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
                    'PlatformCategory': 'string',
                    'OperatingSystemName': 'string',
                    'OperatingSystemVersion': 'string',
                    'SupportedTierList': [
                        'string',
                    ],
                    'SupportedAddonList': [
                        'string',
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PlatformSummaryList** *(list) --* 

          Detailed information about the platforms.

          
          

          - *(dict) --* 

            Detailed information about a platform.

            
            

            - **PlatformArn** *(string) --* 

              The ARN of the platform.

              
            

            - **PlatformOwner** *(string) --* 

              The AWS account ID of the person who created the platform.

              
            

            - **PlatformStatus** *(string) --* 

              The status of the platform. You can create an environment from the platform once it is ready.

              
            

            - **PlatformCategory** *(string) --* 

              The category of platform.

              
            

            - **OperatingSystemName** *(string) --* 

              The operating system used by the platform.

              
            

            - **OperatingSystemVersion** *(string) --* 

              The version of the operating system used by the platform.

              
            

            - **SupportedTierList** *(list) --* 

              The tiers in which the platform runs.

              
              

              - *(string) --* 
          
            

            - **SupportedAddonList** *(list) --* 

              The additions associated with the platform.

              
              

              - *(string) --* 
          
        
      
        

        - **NextToken** *(string) --* 

          The starting index into the remaining list of platforms. if this value is not ``null`` , you can use it in a subsequent ``ListPlatformVersion`` call. 

          
    

  .. py:method:: list_tags_for_resource(**kwargs)

    

    Returns the tags applied to an AWS Elastic Beanstalk resource. The response contains a list of tag key-value pairs.

     

    Currently, Elastic Beanstalk only supports tagging of Elastic Beanstalk environments. For details about environment tagging, see `Tagging Resources in Your Elastic Beanstalk Environment <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.tagging.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ListTagsForResource>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_resource(
          ResourceArn='string'
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resouce for which a tag list is requested.

       

      Must be the ARN of an Elastic Beanstalk environment.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceArn': 'string',
            'ResourceTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceArn** *(string) --* 

          The Amazon Resource Name (ARN) of the resouce for which a tag list was requested.

          
        

        - **ResourceTags** *(list) --* 

          A list of tag key-value pairs.

          
          

          - *(dict) --* 

            Describes a tag applied to a resource in an environment.

            
            

            - **Key** *(string) --* 

              The key of the tag.

              
            

            - **Value** *(string) --* 

              The value of the tag.

              
        
      
    

  .. py:method:: rebuild_environment(**kwargs)

    

    Deletes and recreates all of the AWS resources (for example: the Auto Scaling group, load balancer, etc.) for a specified environment and forces a restart.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/RebuildEnvironment>`_    


    **Request Syntax** 
    ::

      response = client.rebuild_environment(
          EnvironmentId='string',
          EnvironmentName='string'
      )
    :type EnvironmentId: string
    :param EnvironmentId: 

      The ID of the environment to rebuild.

       

      Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment to rebuild.

       

      Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    
    :returns: None

    **Examples** 

    The following operation terminates and recreates the resources in an environment named my-env:
    ::

      response = client.rebuild_environment(
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: request_environment_info(**kwargs)

    

    Initiates a request to compile the specified type of information of the deployed environment.

     

    Setting the ``InfoType`` to ``tail`` compiles the last lines from the application server log files of every Amazon EC2 instance in your environment. 

     

    Setting the ``InfoType`` to ``bundle`` compresses the application server log files for every Amazon EC2 instance into a ``.zip`` file. Legacy and .NET containers do not support bundle logs. 

     

    Use  RetrieveEnvironmentInfo to obtain the set of logs. 

     

    Related Topics

     

     
    *  RetrieveEnvironmentInfo   
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo>`_    


    **Request Syntax** 
    ::

      response = client.request_environment_info(
          EnvironmentId='string',
          EnvironmentName='string',
          InfoType='tail'|'bundle'
      )
    :type EnvironmentId: string
    :param EnvironmentId: 

      The ID of the environment of the requested data.

       

      If no such environment is found, ``RequestEnvironmentInfo`` returns an ``InvalidParameterValue`` error. 

       

      Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment of the requested data.

       

      If no such environment is found, ``RequestEnvironmentInfo`` returns an ``InvalidParameterValue`` error. 

       

      Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type InfoType: string
    :param InfoType: **[REQUIRED]** 

      The type of information to request.

      

    
    
    :returns: None

    **Examples** 

    The following operation requests logs from an environment named my-env:
    ::

      response = client.request_environment_info(
          EnvironmentName='my-env',
          InfoType='tail',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: restart_app_server(**kwargs)

    

    Causes the environment to restart the application container server running on each Amazon EC2 instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/RestartAppServer>`_    


    **Request Syntax** 
    ::

      response = client.restart_app_server(
          EnvironmentId='string',
          EnvironmentName='string'
      )
    :type EnvironmentId: string
    :param EnvironmentId: 

      The ID of the environment to restart the server for.

       

      Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment to restart the server for.

       

      Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    
    :returns: None

    **Examples** 

    The following operation restarts application servers on all instances in an environment named my-env:
    ::

      response = client.restart_app_server(
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: retrieve_environment_info(**kwargs)

    

    Retrieves the compiled information from a  RequestEnvironmentInfo request.

     

    Related Topics

     

     
    *  RequestEnvironmentInfo   
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo>`_    


    **Request Syntax** 
    ::

      response = client.retrieve_environment_info(
          EnvironmentId='string',
          EnvironmentName='string',
          InfoType='tail'|'bundle'
      )
    :type EnvironmentId: string
    :param EnvironmentId: 

      The ID of the data's environment.

       

      If no such environment is found, returns an ``InvalidParameterValue`` error.

       

      Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error.

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the data's environment.

       

      If no such environment is found, returns an ``InvalidParameterValue`` error. 

       

      Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type InfoType: string
    :param InfoType: **[REQUIRED]** 

      The type of information to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EnvironmentInfo': [
                {
                    'InfoType': 'tail'|'bundle',
                    'Ec2InstanceId': 'string',
                    'SampleTimestamp': datetime(2015, 1, 1),
                    'Message': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message containing a description of the requested environment info.

        
        

        - **EnvironmentInfo** *(list) --* 

          The  EnvironmentInfoDescription of the environment. 

          
          

          - *(dict) --* 

            The information retrieved from the Amazon EC2 instances.

            
            

            - **InfoType** *(string) --* 

              The type of information retrieved.

              
            

            - **Ec2InstanceId** *(string) --* 

              The Amazon EC2 Instance ID for this information.

              
            

            - **SampleTimestamp** *(datetime) --* 

              The time stamp when this information was retrieved.

              
            

            - **Message** *(string) --* 

              The retrieved information.

              
        
      
    

    **Examples** 

    The following operation retrieves a link to logs from an environment named my-env:
    ::

      response = client.retrieve_environment_info(
          EnvironmentName='my-env',
          InfoType='tail',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'EnvironmentInfo': [
              {
                  'Ec2InstanceId': 'i-09c1c867',
                  'InfoType': 'tail',
                  'Message': 'https://elasticbeanstalk-us-west-2-0123456789012.s3.amazonaws.com/resources/environments/logs/tail/e-fyqyju3yjs/i-09c1c867/TailLogs-1440109397703.out?AWSAccessKeyId=AKGPT4J56IAJ2EUBL5CQ&Expires=1440195891&Signature=n%2BEalOV6A2HIOx4Rcfb7LT16bBM%3D',
                  'SampleTimestamp': datetime(2015, 8, 20, 22, 23, 17, 3, 232, 0),
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: swap_environment_cnames(**kwargs)

    

    Swaps the CNAMEs of two environments.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs>`_    


    **Request Syntax** 
    ::

      response = client.swap_environment_cnames(
          SourceEnvironmentId='string',
          SourceEnvironmentName='string',
          DestinationEnvironmentId='string',
          DestinationEnvironmentName='string'
      )
    :type SourceEnvironmentId: string
    :param SourceEnvironmentId: 

      The ID of the source environment.

       

      Condition: You must specify at least the ``SourceEnvironmentID`` or the ``SourceEnvironmentName`` . You may also specify both. If you specify the ``SourceEnvironmentId`` , you must specify the ``DestinationEnvironmentId`` . 

      

    
    :type SourceEnvironmentName: string
    :param SourceEnvironmentName: 

      The name of the source environment.

       

      Condition: You must specify at least the ``SourceEnvironmentID`` or the ``SourceEnvironmentName`` . You may also specify both. If you specify the ``SourceEnvironmentName`` , you must specify the ``DestinationEnvironmentName`` . 

      

    
    :type DestinationEnvironmentId: string
    :param DestinationEnvironmentId: 

      The ID of the destination environment.

       

      Condition: You must specify at least the ``DestinationEnvironmentID`` or the ``DestinationEnvironmentName`` . You may also specify both. You must specify the ``SourceEnvironmentId`` with the ``DestinationEnvironmentId`` . 

      

    
    :type DestinationEnvironmentName: string
    :param DestinationEnvironmentName: 

      The name of the destination environment.

       

      Condition: You must specify at least the ``DestinationEnvironmentID`` or the ``DestinationEnvironmentName`` . You may also specify both. You must specify the ``SourceEnvironmentName`` with the ``DestinationEnvironmentName`` . 

      

    
    
    :returns: None

    **Examples** 

    The following operation swaps the assigned subdomains of two environments:
    ::

      response = client.swap_environment_cnames(
          DestinationEnvironmentName='my-env-green',
          SourceEnvironmentName='my-env-blue',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: terminate_environment(**kwargs)

    

    Terminates the specified environment.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/TerminateEnvironment>`_    


    **Request Syntax** 
    ::

      response = client.terminate_environment(
          EnvironmentId='string',
          EnvironmentName='string',
          TerminateResources=True|False,
          ForceTerminate=True|False
      )
    :type EnvironmentId: string
    :param EnvironmentId: 

      The ID of the environment to terminate.

       

      Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment to terminate.

       

      Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type TerminateResources: boolean
    :param TerminateResources: 

      Indicates whether the associated AWS resources should shut down when the environment is terminated:

       

       
      * ``true`` : The specified environment as well as the associated AWS resources, such as Auto Scaling group and LoadBalancer, are terminated. 
       
      * ``false`` : AWS Elastic Beanstalk resource management is removed from the environment, but the AWS resources continue to operate. 
       

       

      For more information, see the `AWS Elastic Beanstalk User Guide. <http://docs.aws.amazon.com/elasticbeanstalk/latest/ug/>`__  

       

      Default: ``true``  

       

      Valid Values: ``true`` | ``false``  

      

    
    :type ForceTerminate: boolean
    :param ForceTerminate: 

      Terminates the target environment even if another environment in the same group is dependent on it.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EnvironmentName': 'string',
            'EnvironmentId': 'string',
            'ApplicationName': 'string',
            'VersionLabel': 'string',
            'SolutionStackName': 'string',
            'PlatformArn': 'string',
            'TemplateName': 'string',
            'Description': 'string',
            'EndpointURL': 'string',
            'CNAME': 'string',
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
            'AbortableOperationInProgress': True|False,
            'Health': 'Green'|'Yellow'|'Red'|'Grey',
            'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
            'Resources': {
                'LoadBalancer': {
                    'LoadBalancerName': 'string',
                    'Domain': 'string',
                    'Listeners': [
                        {
                            'Protocol': 'string',
                            'Port': 123
                        },
                    ]
                }
            },
            'Tier': {
                'Name': 'string',
                'Type': 'string',
                'Version': 'string'
            },
            'EnvironmentLinks': [
                {
                    'LinkName': 'string',
                    'EnvironmentName': 'string'
                },
            ],
            'EnvironmentArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes the properties of an environment.

        
        

        - **EnvironmentName** *(string) --* 

          The name of this environment.

          
        

        - **EnvironmentId** *(string) --* 

          The ID of this environment.

          
        

        - **ApplicationName** *(string) --* 

          The name of the application associated with this environment.

          
        

        - **VersionLabel** *(string) --* 

          The application version deployed in this environment.

          
        

        - **SolutionStackName** *(string) --* 

          The name of the ``SolutionStack`` deployed with this environment. 

          
        

        - **PlatformArn** *(string) --* 

          The ARN of the platform.

          
        

        - **TemplateName** *(string) --* 

          The name of the configuration template used to originally launch this environment.

          
        

        - **Description** *(string) --* 

          Describes this environment.

          
        

        - **EndpointURL** *(string) --* 

          For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.

          
        

        - **CNAME** *(string) --* 

          The URL to the CNAME for this environment.

          
        

        - **DateCreated** *(datetime) --* 

          The creation date for this environment.

          
        

        - **DateUpdated** *(datetime) --* 

          The last modified date for this environment.

          
        

        - **Status** *(string) --* 

          The current operational status of the environment:

           

           
          * ``Launching`` : Environment is in the process of initial deployment. 
           
          * ``Updating`` : Environment is in the process of updating its configuration settings or application version. 
           
          * ``Ready`` : Environment is available to have an action performed on it, such as update or terminate. 
           
          * ``Terminating`` : Environment is in the shut-down process. 
           
          * ``Terminated`` : Environment is not running. 
           

          
        

        - **AbortableOperationInProgress** *(boolean) --* 

          Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.

           

           ``true:`` There is an update in progress. 

           

           ``false:`` There are no updates currently in progress. 

          
        

        - **Health** *(string) --* 

          Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:

           

           
          * ``Red`` : Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment. 
           
          * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur for an environment. 
           
          * ``Green`` : Indicates the environment is healthy and fully functional. 
           
          * ``Grey`` : Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an ``UpdateEnvironment`` or ``RestartEnvironement`` request. 
           

           

          Default: ``Grey``  

          
        

        - **HealthStatus** *(string) --* 

          Returns the health status of the application running in your environment. For more information, see `Health Colors and Statuses <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

          
        

        - **Resources** *(dict) --* 

          The description of the AWS resources used by this environment.

          
          

          - **LoadBalancer** *(dict) --* 

            Describes the LoadBalancer.

            
            

            - **LoadBalancerName** *(string) --* 

              The name of the LoadBalancer.

              
            

            - **Domain** *(string) --* 

              The domain name of the LoadBalancer.

              
            

            - **Listeners** *(list) --* 

              A list of Listeners used by the LoadBalancer.

              
              

              - *(dict) --* 

                Describes the properties of a Listener for the LoadBalancer.

                
                

                - **Protocol** *(string) --* 

                  The protocol that is used by the Listener.

                  
                

                - **Port** *(integer) --* 

                  The port that is used by the Listener.

                  
            
          
        
      
        

        - **Tier** *(dict) --* 

          Describes the current tier of this environment.

          
          

          - **Name** *(string) --* 

            The name of this environment tier.

            
          

          - **Type** *(string) --* 

            The type of this environment tier.

            
          

          - **Version** *(string) --* 

            The version of this environment tier.

            
      
        

        - **EnvironmentLinks** *(list) --* 

          A list of links to other environments in the same group.

          
          

          - *(dict) --* 

            A link to another environment, defined in the environment's manifest. Links provide connection information in system properties that can be used to connect to another environment in the same group. See `Environment Manifest (env.yaml) <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.

            
            

            - **LinkName** *(string) --* 

              The name of the link.

              
            

            - **EnvironmentName** *(string) --* 

              The name of the linked environment (the dependency).

              
        
      
        

        - **EnvironmentArn** *(string) --* 

          The environment's Amazon Resource Name (ARN), which can be used in other API reuqests that require an ARN.

          
    

    **Examples** 

    The following operation terminates an Elastic Beanstalk environment named my-env:
    ::

      response = client.terminate_environment(
          EnvironmentName='my-env',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AbortableOperationInProgress': False,
          'ApplicationName': 'my-app',
          'CNAME': 'my-env.elasticbeanstalk.com',
          'DateCreated': datetime(2015, 8, 12, 18, 52, 53, 2, 224, 0),
          'DateUpdated': datetime(2015, 8, 12, 19, 5, 54, 2, 224, 0),
          'EndpointURL': 'awseb-e-f-AWSEBLoa-1I9XUMP4-8492WNUP202574.us-west-2.elb.amazonaws.com',
          'EnvironmentId': 'e-fh2eravpns',
          'EnvironmentName': 'my-env',
          'Health': 'Grey',
          'SolutionStackName': '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
          'Status': 'Terminating',
          'Tier': {
              'Name': 'WebServer',
              'Type': 'Standard',
              'Version': ' ',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_application(**kwargs)

    

    Updates the specified application to have the specified properties.

     

    .. note::

       

      If a property (for example, ``description`` ) is not provided, the value remains unchanged. To clear these properties, specify an empty string.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/UpdateApplication>`_    


    **Request Syntax** 
    ::

      response = client.update_application(
          ApplicationName='string',
          Description='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application to update. If no such application is found, ``UpdateApplication`` returns an ``InvalidParameterValue`` error. 

      

    
    :type Description: string
    :param Description: 

      A new description for the application.

       

      Default: If not specified, AWS Elastic Beanstalk does not update the description.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Application': {
                'ApplicationName': 'string',
                'Description': 'string',
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'Versions': [
                    'string',
                ],
                'ConfigurationTemplates': [
                    'string',
                ],
                'ResourceLifecycleConfig': {
                    'ServiceRole': 'string',
                    'VersionLifecycleConfig': {
                        'MaxCountRule': {
                            'Enabled': True|False,
                            'MaxCount': 123,
                            'DeleteSourceFromS3': True|False
                        },
                        'MaxAgeRule': {
                            'Enabled': True|False,
                            'MaxAgeInDays': 123,
                            'DeleteSourceFromS3': True|False
                        }
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message containing a single description of an application.

        
        

        - **Application** *(dict) --* 

          The  ApplicationDescription of the application. 

          
          

          - **ApplicationName** *(string) --* 

            The name of the application.

            
          

          - **Description** *(string) --* 

            User-defined description of the application.

            
          

          - **DateCreated** *(datetime) --* 

            The date when the application was created.

            
          

          - **DateUpdated** *(datetime) --* 

            The date when the application was last modified.

            
          

          - **Versions** *(list) --* 

            The names of the versions for this application.

            
            

            - *(string) --* 
        
          

          - **ConfigurationTemplates** *(list) --* 

            The names of the configuration templates associated with this application.

            
            

            - *(string) --* 
        
          

          - **ResourceLifecycleConfig** *(dict) --* 

            The lifecycle settings for the application.

            
            

            - **ServiceRole** *(string) --* 

              The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

              
            

            - **VersionLifecycleConfig** *(dict) --* 

              The application version lifecycle configuration.

              
              

              - **MaxCountRule** *(dict) --* 

                Specify a max count rule to restrict the number of application versions that are retained for an application.

                
                

                - **Enabled** *(boolean) --* 

                  Specify ``true`` to apply the rule, or ``false`` to disable it.

                  
                

                - **MaxCount** *(integer) --* 

                  Specify the maximum number of application versions to retain.

                  
                

                - **DeleteSourceFromS3** *(boolean) --* 

                  Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

                  
            
              

              - **MaxAgeRule** *(dict) --* 

                Specify a max age rule to restrict the length of time that application versions are retained for an application.

                
                

                - **Enabled** *(boolean) --* 

                  Specify ``true`` to apply the rule, or ``false`` to disable it.

                  
                

                - **MaxAgeInDays** *(integer) --* 

                  Specify the number of days to retain an application versions.

                  
                

                - **DeleteSourceFromS3** *(boolean) --* 

                  Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

                  
            
          
        
      
    

    **Examples** 

    The following operation updates the description of an application named my-app:
    ::

      response = client.update_application(
          ApplicationName='my-app',
          Description='my Elastic Beanstalk application',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Application': {
              'ApplicationName': 'my-app',
              'ConfigurationTemplates': [
              ],
              'DateCreated': datetime(2015, 8, 13, 19, 15, 50, 3, 225, 0),
              'DateUpdated': datetime(2015, 8, 20, 22, 34, 56, 3, 232, 0),
              'Description': 'my Elastic Beanstalk application',
              'Versions': [
                  '2fba-stage-150819_234450',
                  'bf07-stage-150820_214945',
                  '93f8',
                  'fd7c-stage-150820_000431',
                  '22a0-stage-150819_185942',
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_application_resource_lifecycle(**kwargs)

    

    Modifies lifecycle settings for an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle>`_    


    **Request Syntax** 
    ::

      response = client.update_application_resource_lifecycle(
          ApplicationName='string',
          ResourceLifecycleConfig={
              'ServiceRole': 'string',
              'VersionLifecycleConfig': {
                  'MaxCountRule': {
                      'Enabled': True|False,
                      'MaxCount': 123,
                      'DeleteSourceFromS3': True|False
                  },
                  'MaxAgeRule': {
                      'Enabled': True|False,
                      'MaxAgeInDays': 123,
                      'DeleteSourceFromS3': True|False
                  }
              }
          }
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application.

      

    
    :type ResourceLifecycleConfig: dict
    :param ResourceLifecycleConfig: **[REQUIRED]** 

      The lifecycle configuration.

      

    
      - **ServiceRole** *(string) --* 

        The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

        

      
      - **VersionLifecycleConfig** *(dict) --* 

        The application version lifecycle configuration.

        

      
        - **MaxCountRule** *(dict) --* 

          Specify a max count rule to restrict the number of application versions that are retained for an application.

          

        
          - **Enabled** *(boolean) --* **[REQUIRED]** 

            Specify ``true`` to apply the rule, or ``false`` to disable it.

            

          
          - **MaxCount** *(integer) --* 

            Specify the maximum number of application versions to retain.

            

          
          - **DeleteSourceFromS3** *(boolean) --* 

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

            

          
        
        - **MaxAgeRule** *(dict) --* 

          Specify a max age rule to restrict the length of time that application versions are retained for an application.

          

        
          - **Enabled** *(boolean) --* **[REQUIRED]** 

            Specify ``true`` to apply the rule, or ``false`` to disable it.

            

          
          - **MaxAgeInDays** *(integer) --* 

            Specify the number of days to retain an application versions.

            

          
          - **DeleteSourceFromS3** *(boolean) --* 

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

            

          
        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationName': 'string',
            'ResourceLifecycleConfig': {
                'ServiceRole': 'string',
                'VersionLifecycleConfig': {
                    'MaxCountRule': {
                        'Enabled': True|False,
                        'MaxCount': 123,
                        'DeleteSourceFromS3': True|False
                    },
                    'MaxAgeRule': {
                        'Enabled': True|False,
                        'MaxAgeInDays': 123,
                        'DeleteSourceFromS3': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ApplicationName** *(string) --* 

          The name of the application.

          
        

        - **ResourceLifecycleConfig** *(dict) --* 

          The lifecycle configuration.

          
          

          - **ServiceRole** *(string) --* 

            The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

            
          

          - **VersionLifecycleConfig** *(dict) --* 

            The application version lifecycle configuration.

            
            

            - **MaxCountRule** *(dict) --* 

              Specify a max count rule to restrict the number of application versions that are retained for an application.

              
              

              - **Enabled** *(boolean) --* 

                Specify ``true`` to apply the rule, or ``false`` to disable it.

                
              

              - **MaxCount** *(integer) --* 

                Specify the maximum number of application versions to retain.

                
              

              - **DeleteSourceFromS3** *(boolean) --* 

                Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

                
          
            

            - **MaxAgeRule** *(dict) --* 

              Specify a max age rule to restrict the length of time that application versions are retained for an application.

              
              

              - **Enabled** *(boolean) --* 

                Specify ``true`` to apply the rule, or ``false`` to disable it.

                
              

              - **MaxAgeInDays** *(integer) --* 

                Specify the number of days to retain an application versions.

                
              

              - **DeleteSourceFromS3** *(boolean) --* 

                Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

                
          
        
      
    

  .. py:method:: update_application_version(**kwargs)

    

    Updates the specified application version to have the specified properties.

     

    .. note::

       

      If a property (for example, ``description`` ) is not provided, the value remains unchanged. To clear properties, specify an empty string.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/UpdateApplicationVersion>`_    


    **Request Syntax** 
    ::

      response = client.update_application_version(
          ApplicationName='string',
          VersionLabel='string',
          Description='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application associated with this version.

       

      If no application is found with this name, ``UpdateApplication`` returns an ``InvalidParameterValue`` error.

      

    
    :type VersionLabel: string
    :param VersionLabel: **[REQUIRED]** 

      The name of the version to update.

       

      If no application version is found with this label, ``UpdateApplication`` returns an ``InvalidParameterValue`` error. 

      

    
    :type Description: string
    :param Description: 

      A new description for this version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationVersion': {
                'ApplicationName': 'string',
                'Description': 'string',
                'VersionLabel': 'string',
                'SourceBuildInformation': {
                    'SourceType': 'Git'|'Zip',
                    'SourceRepository': 'CodeCommit'|'S3',
                    'SourceLocation': 'string'
                },
                'BuildArn': 'string',
                'SourceBundle': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'Status': 'Processed'|'Unprocessed'|'Failed'|'Processing'|'Building'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message wrapping a single description of an application version.

        
        

        - **ApplicationVersion** *(dict) --* 

          The  ApplicationVersionDescription of the application version. 

          
          

          - **ApplicationName** *(string) --* 

            The name of the application to which the application version belongs.

            
          

          - **Description** *(string) --* 

            The description of the application version.

            
          

          - **VersionLabel** *(string) --* 

            A unique identifier for the application version.

            
          

          - **SourceBuildInformation** *(dict) --* 

            If the version's source code was retrieved from AWS CodeCommit, the location of the source code for the application version.

            
            

            - **SourceType** *(string) --* 

              The type of repository.

               

               
              * ``Git``   
               
              * ``Zip``   
               

              
            

            - **SourceRepository** *(string) --* 

              Location where the repository is stored.

               

               
              * ``CodeCommit``   
               
              * ``S3``   
               

              
            

            - **SourceLocation** *(string) --* 

              The location of the source code, as a formatted string, depending on the value of ``SourceRepository``  

               

               
              * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` . 
               
              * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward slash. For example, ``my-s3-bucket/Folders/my-source-file`` . 
               

              
        
          

          - **BuildArn** *(string) --* 

            Reference to the artifact from the AWS CodeBuild build.

            
          

          - **SourceBundle** *(dict) --* 

            The storage location of the application version's source bundle in Amazon S3.

            
            

            - **S3Bucket** *(string) --* 

              The Amazon S3 bucket where the data is located.

              
            

            - **S3Key** *(string) --* 

              The Amazon S3 key where the data is located.

              
        
          

          - **DateCreated** *(datetime) --* 

            The creation date of the application version.

            
          

          - **DateUpdated** *(datetime) --* 

            The last modified date of the application version.

            
          

          - **Status** *(string) --* 

            The processing status of the application version.

            
      
    

    **Examples** 

    The following operation updates the description of an application version named 22a0-stage-150819_185942:
    ::

      response = client.update_application_version(
          ApplicationName='my-app',
          Description='new description',
          VersionLabel='22a0-stage-150819_185942',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ApplicationVersion': {
              'ApplicationName': 'my-app',
              'DateCreated': datetime(2015, 8, 19, 18, 59, 17, 2, 231, 0),
              'DateUpdated': datetime(2015, 8, 20, 22, 53, 28, 3, 232, 0),
              'Description': 'new description',
              'SourceBundle': {
                  'S3Bucket': 'elasticbeanstalk-us-west-2-0123456789012',
                  'S3Key': 'my-app/22a0-stage-150819_185942.war',
              },
              'VersionLabel': '22a0-stage-150819_185942',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_configuration_template(**kwargs)

    

    Updates the specified configuration template to have the specified properties or configuration option values.

     

    .. note::

       

      If a property (for example, ``ApplicationName`` ) is not provided, its value remains unchanged. To clear such properties, specify an empty string.

       

     

    Related Topics

     

     
    *  DescribeConfigurationOptions   
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate>`_    


    **Request Syntax** 
    ::

      response = client.update_configuration_template(
          ApplicationName='string',
          TemplateName='string',
          Description='string',
          OptionSettings=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string',
                  'Value': 'string'
              },
          ],
          OptionsToRemove=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string'
              },
          ]
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application associated with the configuration template to update.

       

      If no application is found with this name, ``UpdateConfigurationTemplate`` returns an ``InvalidParameterValue`` error. 

      

    
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the configuration template to update.

       

      If no configuration template is found with this name, ``UpdateConfigurationTemplate`` returns an ``InvalidParameterValue`` error. 

      

    
    :type Description: string
    :param Description: 

      A new description for the configuration.

      

    
    :type OptionSettings: list
    :param OptionSettings: 

      A list of configuration option settings to update with the new specified option value.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
        - **Value** *(string) --* 

          The current value for the configuration option.

          

        
      
  
    :type OptionsToRemove: list
    :param OptionsToRemove: 

      A list of configuration options to remove from the configuration set.

       

      Constraint: You can remove only ``UserDefined`` configuration options. 

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option.

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SolutionStackName': 'string',
            'PlatformArn': 'string',
            'ApplicationName': 'string',
            'TemplateName': 'string',
            'Description': 'string',
            'EnvironmentName': 'string',
            'DeploymentStatus': 'deployed'|'pending'|'failed',
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'OptionSettings': [
                {
                    'ResourceName': 'string',
                    'Namespace': 'string',
                    'OptionName': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes the settings for a configuration set.

        
        

        - **SolutionStackName** *(string) --* 

          The name of the solution stack this configuration set uses.

          
        

        - **PlatformArn** *(string) --* 

          The ARN of the platform.

          
        

        - **ApplicationName** *(string) --* 

          The name of the application associated with this configuration set.

          
        

        - **TemplateName** *(string) --* 

          If not ``null`` , the name of the configuration template for this configuration set. 

          
        

        - **Description** *(string) --* 

          Describes this configuration set.

          
        

        - **EnvironmentName** *(string) --* 

          If not ``null`` , the name of the environment for this configuration set. 

          
        

        - **DeploymentStatus** *(string) --* 

          If this configuration set is associated with an environment, the ``DeploymentStatus`` parameter indicates the deployment status of this configuration set: 

           

           
          * ``null`` : This configuration is not associated with a running environment. 
           
          * ``pending`` : This is a draft configuration that is not deployed to the associated environment but is in the process of deploying. 
           
          * ``deployed`` : This is the configuration that is currently deployed to the associated running environment. 
           
          * ``failed`` : This is a draft configuration that failed to successfully deploy. 
           

          
        

        - **DateCreated** *(datetime) --* 

          The date (in UTC time) when this configuration set was created.

          
        

        - **DateUpdated** *(datetime) --* 

          The date (in UTC time) when this configuration set was last modified.

          
        

        - **OptionSettings** *(list) --* 

          A list of the configuration options and their values in this configuration set.

          
          

          - *(dict) --* 

            A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

            
            

            - **ResourceName** *(string) --* 

              A unique resource name for a time-based scaling configuration option.

              
            

            - **Namespace** *(string) --* 

              A unique namespace identifying the option's associated AWS resource.

              
            

            - **OptionName** *(string) --* 

              The name of the configuration option.

              
            

            - **Value** *(string) --* 

              The current value for the configuration option.

              
        
      
    

    **Examples** 

    The following operation removes the configured CloudWatch custom health metrics configuration ConfigDocument from a saved configuration template named my-template:
    ::

      response = client.update_configuration_template(
          ApplicationName='my-app',
          OptionsToRemove=[
              {
                  'Namespace': 'aws:elasticbeanstalk:healthreporting:system',
                  'OptionName': 'ConfigDocument',
              },
          ],
          TemplateName='my-template',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ApplicationName': 'my-app',
          'DateCreated': datetime(2015, 8, 20, 22, 39, 31, 3, 232, 0),
          'DateUpdated': datetime(2015, 8, 20, 22, 43, 11, 3, 232, 0),
          'SolutionStackName': '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
          'TemplateName': 'my-template',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_environment(**kwargs)

    

    Updates the environment description, deploys a new application version, updates the configuration settings to an entirely new configuration template, or updates select configuration option values in the running environment.

     

    Attempting to update both the release and configuration is not allowed and AWS Elastic Beanstalk returns an ``InvalidParameterCombination`` error. 

     

    When updating the configuration settings to a new template or individual settings, a draft configuration is created and  DescribeConfigurationSettings for this environment returns two setting descriptions with different ``DeploymentStatus`` values. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/UpdateEnvironment>`_    


    **Request Syntax** 
    ::

      response = client.update_environment(
          ApplicationName='string',
          EnvironmentId='string',
          EnvironmentName='string',
          GroupName='string',
          Description='string',
          Tier={
              'Name': 'string',
              'Type': 'string',
              'Version': 'string'
          },
          VersionLabel='string',
          TemplateName='string',
          SolutionStackName='string',
          PlatformArn='string',
          OptionSettings=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string',
                  'Value': 'string'
              },
          ],
          OptionsToRemove=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string'
              },
          ]
      )
    :type ApplicationName: string
    :param ApplicationName: 

      The name of the application with which the environment is associated.

      

    
    :type EnvironmentId: string
    :param EnvironmentId: 

      The ID of the environment to update.

       

      If no environment with this ID exists, AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error.

       

      Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment to update. If no environment with this name exists, AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error. 

       

      Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns ``MissingRequiredParameter`` error. 

      

    
    :type GroupName: string
    :param GroupName: 

      The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name or environment ID parameters. See `Environment Manifest (env.yaml) <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.

      

    
    :type Description: string
    :param Description: 

      If this parameter is specified, AWS Elastic Beanstalk updates the description of this environment.

      

    
    :type Tier: dict
    :param Tier: 

      This specifies the tier to use to update the environment.

       

      Condition: At this time, if you change the tier version, name, or type, AWS Elastic Beanstalk returns ``InvalidParameterValue`` error. 

      

    
      - **Name** *(string) --* 

        The name of this environment tier.

        

      
      - **Type** *(string) --* 

        The type of this environment tier.

        

      
      - **Version** *(string) --* 

        The version of this environment tier.

        

      
    
    :type VersionLabel: string
    :param VersionLabel: 

      If this parameter is specified, AWS Elastic Beanstalk deploys the named application version to the environment. If no such application version is found, returns an ``InvalidParameterValue`` error. 

      

    
    :type TemplateName: string
    :param TemplateName: 

      If this parameter is specified, AWS Elastic Beanstalk deploys this configuration template to the environment. If no such configuration template is found, AWS Elastic Beanstalk returns an ``InvalidParameterValue`` error. 

      

    
    :type SolutionStackName: string
    :param SolutionStackName: 

      This specifies the platform version that the environment will run after the environment is updated.

      

    
    :type PlatformArn: string
    :param PlatformArn: 

      The ARN of the platform, if used.

      

    
    :type OptionSettings: list
    :param OptionSettings: 

      If specified, AWS Elastic Beanstalk updates the configuration set associated with the running environment and sets the specified configuration options to the requested value.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
        - **Value** *(string) --* 

          The current value for the configuration option.

          

        
      
  
    :type OptionsToRemove: list
    :param OptionsToRemove: 

      A list of custom user-defined configuration options to remove from the configuration set for this environment.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option.

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EnvironmentName': 'string',
            'EnvironmentId': 'string',
            'ApplicationName': 'string',
            'VersionLabel': 'string',
            'SolutionStackName': 'string',
            'PlatformArn': 'string',
            'TemplateName': 'string',
            'Description': 'string',
            'EndpointURL': 'string',
            'CNAME': 'string',
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
            'AbortableOperationInProgress': True|False,
            'Health': 'Green'|'Yellow'|'Red'|'Grey',
            'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
            'Resources': {
                'LoadBalancer': {
                    'LoadBalancerName': 'string',
                    'Domain': 'string',
                    'Listeners': [
                        {
                            'Protocol': 'string',
                            'Port': 123
                        },
                    ]
                }
            },
            'Tier': {
                'Name': 'string',
                'Type': 'string',
                'Version': 'string'
            },
            'EnvironmentLinks': [
                {
                    'LinkName': 'string',
                    'EnvironmentName': 'string'
                },
            ],
            'EnvironmentArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes the properties of an environment.

        
        

        - **EnvironmentName** *(string) --* 

          The name of this environment.

          
        

        - **EnvironmentId** *(string) --* 

          The ID of this environment.

          
        

        - **ApplicationName** *(string) --* 

          The name of the application associated with this environment.

          
        

        - **VersionLabel** *(string) --* 

          The application version deployed in this environment.

          
        

        - **SolutionStackName** *(string) --* 

          The name of the ``SolutionStack`` deployed with this environment. 

          
        

        - **PlatformArn** *(string) --* 

          The ARN of the platform.

          
        

        - **TemplateName** *(string) --* 

          The name of the configuration template used to originally launch this environment.

          
        

        - **Description** *(string) --* 

          Describes this environment.

          
        

        - **EndpointURL** *(string) --* 

          For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.

          
        

        - **CNAME** *(string) --* 

          The URL to the CNAME for this environment.

          
        

        - **DateCreated** *(datetime) --* 

          The creation date for this environment.

          
        

        - **DateUpdated** *(datetime) --* 

          The last modified date for this environment.

          
        

        - **Status** *(string) --* 

          The current operational status of the environment:

           

           
          * ``Launching`` : Environment is in the process of initial deployment. 
           
          * ``Updating`` : Environment is in the process of updating its configuration settings or application version. 
           
          * ``Ready`` : Environment is available to have an action performed on it, such as update or terminate. 
           
          * ``Terminating`` : Environment is in the shut-down process. 
           
          * ``Terminated`` : Environment is not running. 
           

          
        

        - **AbortableOperationInProgress** *(boolean) --* 

          Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.

           

           ``true:`` There is an update in progress. 

           

           ``false:`` There are no updates currently in progress. 

          
        

        - **Health** *(string) --* 

          Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:

           

           
          * ``Red`` : Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment. 
           
          * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur for an environment. 
           
          * ``Green`` : Indicates the environment is healthy and fully functional. 
           
          * ``Grey`` : Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an ``UpdateEnvironment`` or ``RestartEnvironement`` request. 
           

           

          Default: ``Grey``  

          
        

        - **HealthStatus** *(string) --* 

          Returns the health status of the application running in your environment. For more information, see `Health Colors and Statuses <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

          
        

        - **Resources** *(dict) --* 

          The description of the AWS resources used by this environment.

          
          

          - **LoadBalancer** *(dict) --* 

            Describes the LoadBalancer.

            
            

            - **LoadBalancerName** *(string) --* 

              The name of the LoadBalancer.

              
            

            - **Domain** *(string) --* 

              The domain name of the LoadBalancer.

              
            

            - **Listeners** *(list) --* 

              A list of Listeners used by the LoadBalancer.

              
              

              - *(dict) --* 

                Describes the properties of a Listener for the LoadBalancer.

                
                

                - **Protocol** *(string) --* 

                  The protocol that is used by the Listener.

                  
                

                - **Port** *(integer) --* 

                  The port that is used by the Listener.

                  
            
          
        
      
        

        - **Tier** *(dict) --* 

          Describes the current tier of this environment.

          
          

          - **Name** *(string) --* 

            The name of this environment tier.

            
          

          - **Type** *(string) --* 

            The type of this environment tier.

            
          

          - **Version** *(string) --* 

            The version of this environment tier.

            
      
        

        - **EnvironmentLinks** *(list) --* 

          A list of links to other environments in the same group.

          
          

          - *(dict) --* 

            A link to another environment, defined in the environment's manifest. Links provide connection information in system properties that can be used to connect to another environment in the same group. See `Environment Manifest (env.yaml) <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.

            
            

            - **LinkName** *(string) --* 

              The name of the link.

              
            

            - **EnvironmentName** *(string) --* 

              The name of the linked environment (the dependency).

              
        
      
        

        - **EnvironmentArn** *(string) --* 

          The environment's Amazon Resource Name (ARN), which can be used in other API reuqests that require an ARN.

          
    

    **Examples** 

    The following operation updates an environment named "my-env" to version "v2" of the application to which it belongs:
    ::

      response = client.update_environment(
          EnvironmentName='my-env',
          VersionLabel='v2',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ApplicationName': 'my-app',
          'CNAME': 'my-env.elasticbeanstalk.com',
          'DateCreated': datetime(2015, 2, 3, 23, 4, 54, 1, 34, 0),
          'DateUpdated': datetime(2015, 2, 3, 23, 12, 29, 1, 34, 0),
          'EndpointURL': 'awseb-e-i-AWSEBLoa-1RDLX6TC9VUAO-0123456789.us-west-2.elb.amazonaws.com',
          'EnvironmentId': 'e-szqipays4h',
          'EnvironmentName': 'my-env',
          'Health': 'Grey',
          'SolutionStackName': '64bit Amazon Linux running Tomcat 7',
          'Status': 'Updating',
          'Tier': {
              'Name': 'WebServer',
              'Type': 'Standard',
              'Version': ' ',
          },
          'VersionLabel': 'v2',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    The following operation configures several options in the aws:elb:loadbalancer namespace:
    ::

      response = client.update_environment(
          EnvironmentName='my-env',
          OptionSettings=[
              {
                  'Namespace': 'aws:elb:healthcheck',
                  'OptionName': 'Interval',
                  'Value': '15',
              },
              {
                  'Namespace': 'aws:elb:healthcheck',
                  'OptionName': 'Timeout',
                  'Value': '8',
              },
              {
                  'Namespace': 'aws:elb:healthcheck',
                  'OptionName': 'HealthyThreshold',
                  'Value': '2',
              },
              {
                  'Namespace': 'aws:elb:healthcheck',
                  'OptionName': 'UnhealthyThreshold',
                  'Value': '3',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AbortableOperationInProgress': True,
          'ApplicationName': 'my-app',
          'CNAME': 'my-env.elasticbeanstalk.com',
          'DateCreated': datetime(2015, 8, 7, 20, 48, 49, 4, 219, 0),
          'DateUpdated': datetime(2015, 8, 12, 18, 15, 23, 2, 224, 0),
          'EndpointURL': 'awseb-e-w-AWSEBLoa-14XB83101Q4L-104QXY80921.sa-east-1.elb.amazonaws.com',
          'EnvironmentId': 'e-wtp2rpqsej',
          'EnvironmentName': 'my-env',
          'Health': 'Grey',
          'SolutionStackName': '64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8',
          'Status': 'Updating',
          'Tier': {
              'Name': 'WebServer',
              'Type': 'Standard',
              'Version': ' ',
          },
          'VersionLabel': '7f58-stage-150812_025409',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_tags_for_resource(**kwargs)

    

    Update the list of tags applied to an AWS Elastic Beanstalk resource. Two lists can be passed: ``TagsToAdd`` for tags to add or update, and ``TagsToRemove`` .

     

    Currently, Elastic Beanstalk only supports tagging of Elastic Beanstalk environments. For details about environment tagging, see `Tagging Resources in Your Elastic Beanstalk Environment <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.tagging.html>`__ .

     

    If you create a custom IAM user policy to control permission to this operation, specify one of the following two virtual actions (or both) instead of the API operation name:

      elasticbeanstalk:AddTags  

    Controls permission to call ``UpdateTagsForResource`` and pass a list of tags to add in the ``TagsToAdd`` parameter.

      elasticbeanstalk:RemoveTags  

    Controls permission to call ``UpdateTagsForResource`` and pass a list of tag keys to remove in the ``TagsToRemove`` parameter.

       

    For details about creating a custom user policy, see `Creating a Custom User Policy <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#AWSHowTo.iam.policies>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/UpdateTagsForResource>`_    


    **Request Syntax** 
    ::

      response = client.update_tags_for_resource(
          ResourceArn='string',
          TagsToAdd=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          TagsToRemove=[
              'string',
          ]
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resouce to be updated.

       

      Must be the ARN of an Elastic Beanstalk environment.

      

    
    :type TagsToAdd: list
    :param TagsToAdd: 

      A list of tags to add or update.

       

      If a key of an existing tag is added, the tag's value is updated.

      

    
      - *(dict) --* 

        Describes a tag applied to a resource in an environment.

        

      
        - **Key** *(string) --* 

          The key of the tag.

          

        
        - **Value** *(string) --* 

          The value of the tag.

          

        
      
  
    :type TagsToRemove: list
    :param TagsToRemove: 

      A list of tag keys to remove.

       

      If a tag key doesn't exist, it is silently ignored.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: validate_configuration_settings(**kwargs)

    

    Takes a set of configuration settings and either a configuration template or environment, and determines whether those values are valid.

     

    This action returns a list of messages indicating any errors or warnings associated with the selection of option values.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ValidateConfigurationSettings>`_    


    **Request Syntax** 
    ::

      response = client.validate_configuration_settings(
          ApplicationName='string',
          TemplateName='string',
          EnvironmentName='string',
          OptionSettings=[
              {
                  'ResourceName': 'string',
                  'Namespace': 'string',
                  'OptionName': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The name of the application that the configuration template or environment belongs to.

      

    
    :type TemplateName: string
    :param TemplateName: 

      The name of the configuration template to validate the settings against.

       

      Condition: You cannot specify both this and an environment name.

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      The name of the environment to validate the settings against.

       

      Condition: You cannot specify both this and a configuration template name.

      

    
    :type OptionSettings: list
    :param OptionSettings: **[REQUIRED]** 

      A list of the options and desired values to evaluate.

      

    
      - *(dict) --* 

        A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to `Option Values <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 

        

      
        - **ResourceName** *(string) --* 

          A unique resource name for a time-based scaling configuration option.

          

        
        - **Namespace** *(string) --* 

          A unique namespace identifying the option's associated AWS resource.

          

        
        - **OptionName** *(string) --* 

          The name of the configuration option.

          

        
        - **Value** *(string) --* 

          The current value for the configuration option.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Messages': [
                {
                    'Message': 'string',
                    'Severity': 'error'|'warning',
                    'Namespace': 'string',
                    'OptionName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Provides a list of validation messages.

        
        

        - **Messages** *(list) --* 

          A list of  ValidationMessage . 

          
          

          - *(dict) --* 

            An error or warning for a desired configuration option value.

            
            

            - **Message** *(string) --* 

              A message describing the error or warning.

              
            

            - **Severity** *(string) --* 

              An indication of the severity of this message:

               

               
              * ``error`` : This message indicates that this is not a valid setting for an option. 
               
              * ``warning`` : This message is providing information you should take into account. 
               

              
            

            - **Namespace** *(string) --* 

              The namespace to which the option belongs.

              
            

            - **OptionName** *(string) --* 

              The name of the option.

              
        
      
    

    **Examples** 

    The following operation validates a CloudWatch custom metrics config document:
    ::

      response = client.validate_configuration_settings(
          ApplicationName='my-app',
          EnvironmentName='my-env',
          OptionSettings=[
              {
                  'Namespace': 'aws:elasticbeanstalk:healthreporting:system',
                  'OptionName': 'ConfigDocument',
                  'Value': '{"CloudWatchMetrics": {"Environment": {"ApplicationLatencyP99.9": null,"InstancesSevere": 60,"ApplicationLatencyP90": 60,"ApplicationLatencyP99": null,"ApplicationLatencyP95": 60,"InstancesUnknown": 60,"ApplicationLatencyP85": 60,"InstancesInfo": null,"ApplicationRequests2xx": null,"InstancesDegraded": null,"InstancesWarning": 60,"ApplicationLatencyP50": 60,"ApplicationRequestsTotal": null,"InstancesNoData": null,"InstancesPending": 60,"ApplicationLatencyP10": null,"ApplicationRequests5xx": null,"ApplicationLatencyP75": null,"InstancesOk": 60,"ApplicationRequests3xx": null,"ApplicationRequests4xx": null},"Instance": {"ApplicationLatencyP99.9": null,"ApplicationLatencyP90": 60,"ApplicationLatencyP99": null,"ApplicationLatencyP95": null,"ApplicationLatencyP85": null,"CPUUser": 60,"ApplicationRequests2xx": null,"CPUIdle": null,"ApplicationLatencyP50": null,"ApplicationRequestsTotal": 60,"RootFilesystemUtil": null,"LoadAverage1min": null,"CPUIrq": null,"CPUNice": 60,"CPUIowait": 60,"ApplicationLatencyP10": null,"LoadAverage5min": null,"ApplicationRequests5xx": null,"ApplicationLatencyP75": 60,"CPUSystem": 60,"ApplicationRequests3xx": 60,"ApplicationRequests4xx": null,"InstanceHealth": null,"CPUSoftirq": 60}},"Version": 1}',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Messages': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:

* :py:class:`ElasticBeanstalk.Paginator.DescribeEvents`



.. py:class:: ElasticBeanstalk.Paginator.DescribeEvents

  ::

    
    paginator = client.get_paginator('describe_events')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElasticBeanstalk.Client.describe_events`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEvents>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ApplicationName='string',
          VersionLabel='string',
          TemplateName='string',
          EnvironmentId='string',
          EnvironmentName='string',
          PlatformArn='string',
          RequestId='string',
          Severity='TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ApplicationName: string
    :param ApplicationName: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.

      

    
    :type VersionLabel: string
    :param VersionLabel: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.

      

    
    :type TemplateName: string
    :param TemplateName: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.

      

    
    :type EnvironmentId: string
    :param EnvironmentId: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.

      

    
    :type EnvironmentName: string
    :param EnvironmentName: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.

      

    
    :type PlatformArn: string
    :param PlatformArn: 

      The ARN of the version of the custom platform.

      

    
    :type RequestId: string
    :param RequestId: 

      If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.

      

    
    :type Severity: string
    :param Severity: 

      If specified, limits the events returned from this call to include only those with the specified severity or higher.

      

    
    :type StartTime: datetime
    :param StartTime: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.

      

    
    :type EndTime: datetime
    :param EndTime: 

      If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the ``EndTime`` . 

      

    
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
            'Events': [
                {
                    'EventDate': datetime(2015, 1, 1),
                    'Message': 'string',
                    'ApplicationName': 'string',
                    'VersionLabel': 'string',
                    'TemplateName': 'string',
                    'EnvironmentName': 'string',
                    'PlatformArn': 'string',
                    'RequestId': 'string',
                    'Severity': 'TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Result message wrapping a list of event descriptions.

        
        

        - **Events** *(list) --* 

          A list of  EventDescription . 

          
          

          - *(dict) --* 

            Describes an event.

            
            

            - **EventDate** *(datetime) --* 

              The date when the event occurred.

              
            

            - **Message** *(string) --* 

              The event message.

              
            

            - **ApplicationName** *(string) --* 

              The application associated with the event.

              
            

            - **VersionLabel** *(string) --* 

              The release label for the application version associated with this event.

              
            

            - **TemplateName** *(string) --* 

              The name of the configuration associated with this event.

              
            

            - **EnvironmentName** *(string) --* 

              The name of the environment associated with this event.

              
            

            - **PlatformArn** *(string) --* 

              The ARN of the platform.

              
            

            - **RequestId** *(string) --* 

              The web service request ID for the activity of this event.

              
            

            - **Severity** *(string) --* 

              The severity level of this event.

              
        
      
    