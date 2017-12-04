

**********
CodeDeploy
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CodeDeploy.Client

  A low-level client representing AWS CodeDeploy::

    
    import boto3
    
    client = boto3.client('codedeploy')

  
  These are the available methods:
  
  *   :py:meth:`~CodeDeploy.Client.add_tags_to_on_premises_instances`

  
  *   :py:meth:`~CodeDeploy.Client.batch_get_application_revisions`

  
  *   :py:meth:`~CodeDeploy.Client.batch_get_applications`

  
  *   :py:meth:`~CodeDeploy.Client.batch_get_deployment_groups`

  
  *   :py:meth:`~CodeDeploy.Client.batch_get_deployment_instances`

  
  *   :py:meth:`~CodeDeploy.Client.batch_get_deployments`

  
  *   :py:meth:`~CodeDeploy.Client.batch_get_on_premises_instances`

  
  *   :py:meth:`~CodeDeploy.Client.can_paginate`

  
  *   :py:meth:`~CodeDeploy.Client.continue_deployment`

  
  *   :py:meth:`~CodeDeploy.Client.create_application`

  
  *   :py:meth:`~CodeDeploy.Client.create_deployment`

  
  *   :py:meth:`~CodeDeploy.Client.create_deployment_config`

  
  *   :py:meth:`~CodeDeploy.Client.create_deployment_group`

  
  *   :py:meth:`~CodeDeploy.Client.delete_application`

  
  *   :py:meth:`~CodeDeploy.Client.delete_deployment_config`

  
  *   :py:meth:`~CodeDeploy.Client.delete_deployment_group`

  
  *   :py:meth:`~CodeDeploy.Client.deregister_on_premises_instance`

  
  *   :py:meth:`~CodeDeploy.Client.generate_presigned_url`

  
  *   :py:meth:`~CodeDeploy.Client.get_application`

  
  *   :py:meth:`~CodeDeploy.Client.get_application_revision`

  
  *   :py:meth:`~CodeDeploy.Client.get_deployment`

  
  *   :py:meth:`~CodeDeploy.Client.get_deployment_config`

  
  *   :py:meth:`~CodeDeploy.Client.get_deployment_group`

  
  *   :py:meth:`~CodeDeploy.Client.get_deployment_instance`

  
  *   :py:meth:`~CodeDeploy.Client.get_on_premises_instance`

  
  *   :py:meth:`~CodeDeploy.Client.get_paginator`

  
  *   :py:meth:`~CodeDeploy.Client.get_waiter`

  
  *   :py:meth:`~CodeDeploy.Client.list_application_revisions`

  
  *   :py:meth:`~CodeDeploy.Client.list_applications`

  
  *   :py:meth:`~CodeDeploy.Client.list_deployment_configs`

  
  *   :py:meth:`~CodeDeploy.Client.list_deployment_groups`

  
  *   :py:meth:`~CodeDeploy.Client.list_deployment_instances`

  
  *   :py:meth:`~CodeDeploy.Client.list_deployments`

  
  *   :py:meth:`~CodeDeploy.Client.list_git_hub_account_token_names`

  
  *   :py:meth:`~CodeDeploy.Client.list_on_premises_instances`

  
  *   :py:meth:`~CodeDeploy.Client.put_lifecycle_event_hook_execution_status`

  
  *   :py:meth:`~CodeDeploy.Client.register_application_revision`

  
  *   :py:meth:`~CodeDeploy.Client.register_on_premises_instance`

  
  *   :py:meth:`~CodeDeploy.Client.remove_tags_from_on_premises_instances`

  
  *   :py:meth:`~CodeDeploy.Client.skip_wait_time_for_instance_termination`

  
  *   :py:meth:`~CodeDeploy.Client.stop_deployment`

  
  *   :py:meth:`~CodeDeploy.Client.update_application`

  
  *   :py:meth:`~CodeDeploy.Client.update_deployment_group`

  

  .. py:method:: add_tags_to_on_premises_instances(**kwargs)

    

    Adds tags to on-premises instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/AddTagsToOnPremisesInstances>`_    


    **Request Syntax** 
    ::

      response = client.add_tags_to_on_premises_instances(
          tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          instanceNames=[
              'string',
          ]
      )
    :type tags: list
    :param tags: **[REQUIRED]** 

      The tag key-value pairs to add to the on-premises instances.

       

      Keys and values are both required. Keys cannot be null or empty strings. Value-only tags are not allowed.

      

    
      - *(dict) --* 

        Information about a tag.

        

      
        - **Key** *(string) --* 

          The tag's key.

          

        
        - **Value** *(string) --* 

          The tag's value.

          

        
      
  
    :type instanceNames: list
    :param instanceNames: **[REQUIRED]** 

      The names of the on-premises instances to which to add tags.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: batch_get_application_revisions(**kwargs)

    

    Gets information about one or more application revisions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetApplicationRevisions>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_application_revisions(
          applicationName='string',
          revisions=[
              {
                  'revisionType': 'S3'|'GitHub'|'String',
                  's3Location': {
                      'bucket': 'string',
                      'key': 'string',
                      'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                      'version': 'string',
                      'eTag': 'string'
                  },
                  'gitHubLocation': {
                      'repository': 'string',
                      'commitId': 'string'
                  },
                  'string': {
                      'content': 'string',
                      'sha256': 'string'
                  }
              },
          ]
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application about which to get revision information.

      

    
    :type revisions: list
    :param revisions: **[REQUIRED]** 

      Information to get about the application revisions, including type and location.

      

    
      - *(dict) --* 

        Information about the location of an application revision.

        

      
        - **revisionType** *(string) --* 

          The type of application revision:

           

           
          * S3: An application revision stored in Amazon S3. 
           
          * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
           
          * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
           

          

        
        - **s3Location** *(dict) --* 

          Information about the location of a revision stored in Amazon S3. 

          

        
          - **bucket** *(string) --* 

            The name of the Amazon S3 bucket where the application revision is stored.

            

          
          - **key** *(string) --* 

            The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

            

          
          - **bundleType** *(string) --* 

            The file type of the application revision. Must be one of the following:

             

             
            * tar: A tar archive file. 
             
            * tgz: A compressed tar archive file. 
             
            * zip: A zip archive file. 
             

            

          
          - **version** *(string) --* 

            A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

             

            If the version is not specified, the system will use the most recent version by default.

            

          
          - **eTag** *(string) --* 

            The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

             

            If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

            

          
        
        - **gitHubLocation** *(dict) --* 

          Information about the location of application artifacts stored in GitHub.

          

        
          - **repository** *(string) --* 

            The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

             

            Specified as account/repository.

            

          
          - **commitId** *(string) --* 

            The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

            

          
        
        - **string** *(dict) --* 

          Information about the location of an AWS Lambda deployment revision stored as a RawString.

          

        
          - **content** *(string) --* 

            The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

            

          
          - **sha256** *(string) --* 

            The SHA256 hash value of the revision that is specified as a RawString.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'applicationName': 'string',
            'errorMessage': 'string',
            'revisions': [
                {
                    'revisionLocation': {
                        'revisionType': 'S3'|'GitHub'|'String',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                    'genericRevisionInfo': {
                        'description': 'string',
                        'deploymentGroups': [
                            'string',
                        ],
                        'firstUsedTime': datetime(2015, 1, 1),
                        'lastUsedTime': datetime(2015, 1, 1),
                        'registerTime': datetime(2015, 1, 1)
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a BatchGetApplicationRevisions operation.

        
        

        - **applicationName** *(string) --* 

          The name of the application that corresponds to the revisions.

          
        

        - **errorMessage** *(string) --* 

          Information about errors that may have occurred during the API call.

          
        

        - **revisions** *(list) --* 

          Additional information about the revisions, including the type and location.

          
          

          - *(dict) --* 

            Information about an application revision.

            
            

            - **revisionLocation** *(dict) --* 

              Information about the location and type of an application revision.

              
              

              - **revisionType** *(string) --* 

                The type of application revision:

                 

                 
                * S3: An application revision stored in Amazon S3. 
                 
                * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
                 
                * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
                 

                
              

              - **s3Location** *(dict) --* 

                Information about the location of a revision stored in Amazon S3. 

                
                

                - **bucket** *(string) --* 

                  The name of the Amazon S3 bucket where the application revision is stored.

                  
                

                - **key** *(string) --* 

                  The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                  
                

                - **bundleType** *(string) --* 

                  The file type of the application revision. Must be one of the following:

                   

                   
                  * tar: A tar archive file. 
                   
                  * tgz: A compressed tar archive file. 
                   
                  * zip: A zip archive file. 
                   

                  
                

                - **version** *(string) --* 

                  A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                   

                  If the version is not specified, the system will use the most recent version by default.

                  
                

                - **eTag** *(string) --* 

                  The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                   

                  If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                  
            
              

              - **gitHubLocation** *(dict) --* 

                Information about the location of application artifacts stored in GitHub.

                
                

                - **repository** *(string) --* 

                  The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                   

                  Specified as account/repository.

                  
                

                - **commitId** *(string) --* 

                  The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                  
            
              

              - **string** *(dict) --* 

                Information about the location of an AWS Lambda deployment revision stored as a RawString.

                
                

                - **content** *(string) --* 

                  The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                  
                

                - **sha256** *(string) --* 

                  The SHA256 hash value of the revision that is specified as a RawString.

                  
            
          
            

            - **genericRevisionInfo** *(dict) --* 

              Information about an application revision, including usage details and associated deployment groups.

              
              

              - **description** *(string) --* 

                A comment about the revision.

                
              

              - **deploymentGroups** *(list) --* 

                The deployment groups for which this is the current target revision.

                
                

                - *(string) --* 
            
              

              - **firstUsedTime** *(datetime) --* 

                When the revision was first used by AWS CodeDeploy.

                
              

              - **lastUsedTime** *(datetime) --* 

                When the revision was last used by AWS CodeDeploy.

                
              

              - **registerTime** *(datetime) --* 

                When the revision was registered with AWS CodeDeploy.

                
          
        
      
    

  .. py:method:: batch_get_applications(**kwargs)

    

    Gets information about one or more applications.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetApplications>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_applications(
          applicationNames=[
              'string',
          ]
      )
    :type applicationNames: list
    :param applicationNames: **[REQUIRED]** 

      A list of application names separated by spaces.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'applicationsInfo': [
                {
                    'applicationId': 'string',
                    'applicationName': 'string',
                    'createTime': datetime(2015, 1, 1),
                    'linkedToGitHub': True|False,
                    'gitHubAccountName': 'string',
                    'computePlatform': 'Server'|'Lambda'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a BatchGetApplications operation.

        
        

        - **applicationsInfo** *(list) --* 

          Information about the applications.

          
          

          - *(dict) --* 

            Information about an application.

            
            

            - **applicationId** *(string) --* 

              The application ID.

              
            

            - **applicationName** *(string) --* 

              The application name.

              
            

            - **createTime** *(datetime) --* 

              The time at which the application was created.

              
            

            - **linkedToGitHub** *(boolean) --* 

              True if the user has authenticated with GitHub for the specified application; otherwise, false.

              
            

            - **gitHubAccountName** *(string) --* 

              The name for a connection to a GitHub account.

              
            

            - **computePlatform** *(string) --* 

              The destination platform type for deployment of the application (``Lambda`` or ``Server`` ).

              
        
      
    

  .. py:method:: batch_get_deployment_groups(**kwargs)

    

    Gets information about one or more deployment groups.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetDeploymentGroups>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_deployment_groups(
          applicationName='string',
          deploymentGroupNames=[
              'string',
          ]
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type deploymentGroupNames: list
    :param deploymentGroupNames: **[REQUIRED]** 

      The deployment groups' names.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentGroupsInfo': [
                {
                    'applicationName': 'string',
                    'deploymentGroupId': 'string',
                    'deploymentGroupName': 'string',
                    'deploymentConfigName': 'string',
                    'ec2TagFilters': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                    'onPremisesInstanceTagFilters': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                    'autoScalingGroups': [
                        {
                            'name': 'string',
                            'hook': 'string'
                        },
                    ],
                    'serviceRoleArn': 'string',
                    'targetRevision': {
                        'revisionType': 'S3'|'GitHub'|'String',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                    'triggerConfigurations': [
                        {
                            'triggerName': 'string',
                            'triggerTargetArn': 'string',
                            'triggerEvents': [
                                'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                            ]
                        },
                    ],
                    'alarmConfiguration': {
                        'enabled': True|False,
                        'ignorePollAlarmFailure': True|False,
                        'alarms': [
                            {
                                'name': 'string'
                            },
                        ]
                    },
                    'autoRollbackConfiguration': {
                        'enabled': True|False,
                        'events': [
                            'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                        ]
                    },
                    'deploymentStyle': {
                        'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                        'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                    },
                    'blueGreenDeploymentConfiguration': {
                        'terminateBlueInstancesOnDeploymentSuccess': {
                            'action': 'TERMINATE'|'KEEP_ALIVE',
                            'terminationWaitTimeInMinutes': 123
                        },
                        'deploymentReadyOption': {
                            'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                            'waitTimeInMinutes': 123
                        },
                        'greenFleetProvisioningOption': {
                            'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                        }
                    },
                    'loadBalancerInfo': {
                        'elbInfoList': [
                            {
                                'name': 'string'
                            },
                        ],
                        'targetGroupInfoList': [
                            {
                                'name': 'string'
                            },
                        ]
                    },
                    'lastSuccessfulDeployment': {
                        'deploymentId': 'string',
                        'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                        'endTime': datetime(2015, 1, 1),
                        'createTime': datetime(2015, 1, 1)
                    },
                    'lastAttemptedDeployment': {
                        'deploymentId': 'string',
                        'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                        'endTime': datetime(2015, 1, 1),
                        'createTime': datetime(2015, 1, 1)
                    },
                    'ec2TagSet': {
                        'ec2TagSetList': [
                            [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                },
                            ],
                        ]
                    },
                    'onPremisesTagSet': {
                        'onPremisesTagSetList': [
                            [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                },
                            ],
                        ]
                    },
                    'computePlatform': 'Server'|'Lambda'
                },
            ],
            'errorMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a BatchGetDeploymentGroups operation.

        
        

        - **deploymentGroupsInfo** *(list) --* 

          Information about the deployment groups.

          
          

          - *(dict) --* 

            Information about a deployment group.

            
            

            - **applicationName** *(string) --* 

              The application name.

              
            

            - **deploymentGroupId** *(string) --* 

              The deployment group ID.

              
            

            - **deploymentGroupName** *(string) --* 

              The deployment group name.

              
            

            - **deploymentConfigName** *(string) --* 

              The deployment configuration name.

              
            

            - **ec2TagFilters** *(list) --* 

              The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with any of the specified tags.

              
              

              - *(dict) --* 

                Information about an EC2 tag filter.

                
                

                - **Key** *(string) --* 

                  The tag filter key.

                  
                

                - **Value** *(string) --* 

                  The tag filter value.

                  
                

                - **Type** *(string) --* 

                  The tag filter type:

                   

                   
                  * KEY_ONLY: Key only. 
                   
                  * VALUE_ONLY: Value only. 
                   
                  * KEY_AND_VALUE: Key and value. 
                   

                  
            
          
            

            - **onPremisesInstanceTagFilters** *(list) --* 

              The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags.

              
              

              - *(dict) --* 

                Information about an on-premises instance tag filter.

                
                

                - **Key** *(string) --* 

                  The on-premises instance tag filter key.

                  
                

                - **Value** *(string) --* 

                  The on-premises instance tag filter value.

                  
                

                - **Type** *(string) --* 

                  The on-premises instance tag filter type:

                   

                   
                  * KEY_ONLY: Key only. 
                   
                  * VALUE_ONLY: Value only. 
                   
                  * KEY_AND_VALUE: Key and value. 
                   

                  
            
          
            

            - **autoScalingGroups** *(list) --* 

              A list of associated Auto Scaling groups.

              
              

              - *(dict) --* 

                Information about an Auto Scaling group.

                
                

                - **name** *(string) --* 

                  The Auto Scaling group name.

                  
                

                - **hook** *(string) --* 

                  An Auto Scaling lifecycle event hook name.

                  
            
          
            

            - **serviceRoleArn** *(string) --* 

              A service role ARN.

              
            

            - **targetRevision** *(dict) --* 

              Information about the deployment group's target revision, including type and location.

              
              

              - **revisionType** *(string) --* 

                The type of application revision:

                 

                 
                * S3: An application revision stored in Amazon S3. 
                 
                * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
                 
                * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
                 

                
              

              - **s3Location** *(dict) --* 

                Information about the location of a revision stored in Amazon S3. 

                
                

                - **bucket** *(string) --* 

                  The name of the Amazon S3 bucket where the application revision is stored.

                  
                

                - **key** *(string) --* 

                  The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                  
                

                - **bundleType** *(string) --* 

                  The file type of the application revision. Must be one of the following:

                   

                   
                  * tar: A tar archive file. 
                   
                  * tgz: A compressed tar archive file. 
                   
                  * zip: A zip archive file. 
                   

                  
                

                - **version** *(string) --* 

                  A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                   

                  If the version is not specified, the system will use the most recent version by default.

                  
                

                - **eTag** *(string) --* 

                  The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                   

                  If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                  
            
              

              - **gitHubLocation** *(dict) --* 

                Information about the location of application artifacts stored in GitHub.

                
                

                - **repository** *(string) --* 

                  The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                   

                  Specified as account/repository.

                  
                

                - **commitId** *(string) --* 

                  The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                  
            
              

              - **string** *(dict) --* 

                Information about the location of an AWS Lambda deployment revision stored as a RawString.

                
                

                - **content** *(string) --* 

                  The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                  
                

                - **sha256** *(string) --* 

                  The SHA256 hash value of the revision that is specified as a RawString.

                  
            
          
            

            - **triggerConfigurations** *(list) --* 

              Information about triggers associated with the deployment group.

              
              

              - *(dict) --* 

                Information about notification triggers for the deployment group.

                
                

                - **triggerName** *(string) --* 

                  The name of the notification trigger.

                  
                

                - **triggerTargetArn** *(string) --* 

                  The ARN of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

                  
                

                - **triggerEvents** *(list) --* 

                  The event type or types for which notifications are triggered.

                  
                  

                  - *(string) --* 
              
            
          
            

            - **alarmConfiguration** *(dict) --* 

              A list of alarms associated with the deployment group.

              
              

              - **enabled** *(boolean) --* 

                Indicates whether the alarm configuration is enabled.

                
              

              - **ignorePollAlarmFailure** *(boolean) --* 

                Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

                 

                 
                * true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch. 
                 
                * false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch. 
                 

                
              

              - **alarms** *(list) --* 

                A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.

                
                

                - *(dict) --* 

                  Information about an alarm.

                  
                  

                  - **name** *(string) --* 

                    The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.

                    
              
            
          
            

            - **autoRollbackConfiguration** *(dict) --* 

              Information about the automatic rollback configuration associated with the deployment group.

              
              

              - **enabled** *(boolean) --* 

                Indicates whether a defined automatic rollback configuration is currently enabled.

                
              

              - **events** *(list) --* 

                The event type or types that trigger a rollback.

                
                

                - *(string) --* 
            
          
            

            - **deploymentStyle** *(dict) --* 

              Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

              
              

              - **deploymentType** *(string) --* 

                Indicates whether to run an in-place deployment or a blue/green deployment.

                
              

              - **deploymentOption** *(string) --* 

                Indicates whether to route deployment traffic behind a load balancer.

                
          
            

            - **blueGreenDeploymentConfiguration** *(dict) --* 

              Information about blue/green deployment options for a deployment group.

              
              

              - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --* 

                Information about whether to terminate instances in the original fleet during a blue/green deployment.

                
                

                - **action** *(string) --* 

                  The action to take on instances in the original environment after a successful blue/green deployment.

                   

                   
                  * TERMINATE: Instances are terminated after a specified wait time. 
                   
                  * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group. 
                   

                  
                

                - **terminationWaitTimeInMinutes** *(integer) --* 

                  The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.

                  
            
              

              - **deploymentReadyOption** *(dict) --* 

                Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

                
                

                - **actionOnTimeout** *(string) --* 

                  Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

                   

                   
                  * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment. 
                   
                  * STOP_DEPLOYMENT: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped. 
                   

                  
                

                - **waitTimeInMinutes** *(integer) --* 

                  The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout

                  
            
              

              - **greenFleetProvisioningOption** *(dict) --* 

                Information about how instances are provisioned for a replacement environment in a blue/green deployment.

                
                

                - **action** *(string) --* 

                  The method used to add instances to a replacement environment.

                   

                   
                  * DISCOVER_EXISTING: Use instances that already exist or will be created manually. 
                   
                  * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group. 
                   

                  
            
          
            

            - **loadBalancerInfo** *(dict) --* 

              Information about the load balancer to use in a deployment.

              
              

              - **elbInfoList** *(list) --* 

                An array containing information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

                
                

                - *(dict) --* 

                  Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

                  
                  

                  - **name** *(string) --* 

                    For blue/green deployments, the name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.

                    
              
            
              

              - **targetGroupInfoList** *(list) --* 

                An array containing information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

                
                

                - *(dict) --* 

                  Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

                  
                  

                  - **name** *(string) --* 

                    For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes. 

                    
              
            
          
            

            - **lastSuccessfulDeployment** *(dict) --* 

              Information about the most recent successful deployment to the deployment group.

              
              

              - **deploymentId** *(string) --* 

                The deployment ID.

                
              

              - **status** *(string) --* 

                The status of the most recent deployment.

                
              

              - **endTime** *(datetime) --* 

                A timestamp indicating when the most recent deployment to the deployment group completed.

                
              

              - **createTime** *(datetime) --* 

                A timestamp indicating when the most recent deployment to the deployment group started.

                
          
            

            - **lastAttemptedDeployment** *(dict) --* 

              Information about the most recent attempted deployment to the deployment group.

              
              

              - **deploymentId** *(string) --* 

                The deployment ID.

                
              

              - **status** *(string) --* 

                The status of the most recent deployment.

                
              

              - **endTime** *(datetime) --* 

                A timestamp indicating when the most recent deployment to the deployment group completed.

                
              

              - **createTime** *(datetime) --* 

                A timestamp indicating when the most recent deployment to the deployment group started.

                
          
            

            - **ec2TagSet** *(dict) --* 

              Information about groups of tags applied to an EC2 instance. The deployment group includes only EC2 instances identified by all the tag groups. Cannot be used in the same call as ec2TagFilters.

              
              

              - **ec2TagSetList** *(list) --* 

                A list containing other lists of EC2 instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

                
                

                - *(list) --* 
                  

                  - *(dict) --* 

                    Information about an EC2 tag filter.

                    
                    

                    - **Key** *(string) --* 

                      The tag filter key.

                      
                    

                    - **Value** *(string) --* 

                      The tag filter value.

                      
                    

                    - **Type** *(string) --* 

                      The tag filter type:

                       

                       
                      * KEY_ONLY: Key only. 
                       
                      * VALUE_ONLY: Value only. 
                       
                      * KEY_AND_VALUE: Key and value. 
                       

                      
                
              
            
          
            

            - **onPremisesTagSet** *(dict) --* 

              Information about groups of tags applied to an on-premises instance. The deployment group includes only on-premises instances identified by all the tag groups. Cannot be used in the same call as onPremisesInstanceTagFilters.

              
              

              - **onPremisesTagSetList** *(list) --* 

                A list containing other lists of on-premises instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

                
                

                - *(list) --* 
                  

                  - *(dict) --* 

                    Information about an on-premises instance tag filter.

                    
                    

                    - **Key** *(string) --* 

                      The on-premises instance tag filter key.

                      
                    

                    - **Value** *(string) --* 

                      The on-premises instance tag filter value.

                      
                    

                    - **Type** *(string) --* 

                      The on-premises instance tag filter type:

                       

                       
                      * KEY_ONLY: Key only. 
                       
                      * VALUE_ONLY: Value only. 
                       
                      * KEY_AND_VALUE: Key and value. 
                       

                      
                
              
            
          
            

            - **computePlatform** *(string) --* 

              The destination platform type for the deployment group (``Lambda`` or ``Server`` ).

              
        
      
        

        - **errorMessage** *(string) --* 

          Information about errors that may have occurred during the API call.

          
    

  .. py:method:: batch_get_deployment_instances(**kwargs)

    

    Gets information about one or more instance that are part of a deployment group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetDeploymentInstances>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_deployment_instances(
          deploymentId='string',
          instanceIds=[
              'string',
          ]
      )
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      The unique ID of a deployment.

      

    
    :type instanceIds: list
    :param instanceIds: **[REQUIRED]** 

      The unique IDs of instances in the deployment group.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instancesSummary': [
                {
                    'deploymentId': 'string',
                    'instanceId': 'string',
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'lifecycleEvents': [
                        {
                            'lifecycleEventName': 'string',
                            'diagnostics': {
                                'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                                'scriptName': 'string',
                                'message': 'string',
                                'logTail': 'string'
                            },
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                        },
                    ],
                    'instanceType': 'Blue'|'Green'
                },
            ],
            'errorMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a BatchGetDeploymentInstances operation.

        
        

        - **instancesSummary** *(list) --* 

          Information about the instance.

          
          

          - *(dict) --* 

            Information about an instance in a deployment.

            
            

            - **deploymentId** *(string) --* 

              The deployment ID.

              
            

            - **instanceId** *(string) --* 

              The instance ID.

              
            

            - **status** *(string) --* 

              The deployment status for this instance:

               

               
              * Pending: The deployment is pending for this instance. 
               
              * In Progress: The deployment is in progress for this instance. 
               
              * Succeeded: The deployment has succeeded for this instance. 
               
              * Failed: The deployment has failed for this instance. 
               
              * Skipped: The deployment has been skipped for this instance. 
               
              * Unknown: The deployment status is unknown for this instance. 
               

              
            

            - **lastUpdatedAt** *(datetime) --* 

              A timestamp indicating when the instance information was last updated.

              
            

            - **lifecycleEvents** *(list) --* 

              A list of lifecycle events for this instance.

              
              

              - *(dict) --* 

                Information about a deployment lifecycle event.

                
                

                - **lifecycleEventName** *(string) --* 

                  The deployment lifecycle event name, such as ApplicationStop, BeforeInstall, AfterInstall, ApplicationStart, or ValidateService.

                  
                

                - **diagnostics** *(dict) --* 

                  Diagnostic information about the deployment lifecycle event.

                  
                  

                  - **errorCode** *(string) --* 

                    The associated error code:

                     

                     
                    * Success: The specified script ran. 
                     
                    * ScriptMissing: The specified script was not found in the specified location. 
                     
                    * ScriptNotExecutable: The specified script is not a recognized executable file type. 
                     
                    * ScriptTimedOut: The specified script did not finish running in the specified time period. 
                     
                    * ScriptFailed: The specified script failed to run as expected. 
                     
                    * UnknownError: The specified script did not run for an unknown reason. 
                     

                    
                  

                  - **scriptName** *(string) --* 

                    The name of the script.

                    
                  

                  - **message** *(string) --* 

                    The message associated with the error.

                    
                  

                  - **logTail** *(string) --* 

                    The last portion of the diagnostic log.

                     

                    If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

                    
              
                

                - **startTime** *(datetime) --* 

                  A timestamp indicating when the deployment lifecycle event started.

                  
                

                - **endTime** *(datetime) --* 

                  A timestamp indicating when the deployment lifecycle event ended.

                  
                

                - **status** *(string) --* 

                  The deployment lifecycle event status:

                   

                   
                  * Pending: The deployment lifecycle event is pending. 
                   
                  * InProgress: The deployment lifecycle event is in progress. 
                   
                  * Succeeded: The deployment lifecycle event ran successfully. 
                   
                  * Failed: The deployment lifecycle event has failed. 
                   
                  * Skipped: The deployment lifecycle event has been skipped. 
                   
                  * Unknown: The deployment lifecycle event is unknown. 
                   

                  
            
          
            

            - **instanceType** *(string) --* 

              Information about which environment an instance belongs to in a blue/green deployment.

               

               
              * BLUE: The instance is part of the original environment. 
               
              * GREEN: The instance is part of the replacement environment. 
               

              
        
      
        

        - **errorMessage** *(string) --* 

          Information about errors that may have occurred during the API call.

          
    

  .. py:method:: batch_get_deployments(**kwargs)

    

    Gets information about one or more deployments.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetDeployments>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_deployments(
          deploymentIds=[
              'string',
          ]
      )
    :type deploymentIds: list
    :param deploymentIds: **[REQUIRED]** 

      A list of deployment IDs, separated by spaces.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentsInfo': [
                {
                    'applicationName': 'string',
                    'deploymentGroupName': 'string',
                    'deploymentConfigName': 'string',
                    'deploymentId': 'string',
                    'previousRevision': {
                        'revisionType': 'S3'|'GitHub'|'String',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                    'revision': {
                        'revisionType': 'S3'|'GitHub'|'String',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                    'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                    'errorInformation': {
                        'code': 'DEPLOYMENT_GROUP_MISSING'|'APPLICATION_MISSING'|'REVISION_MISSING'|'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'NO_EC2_SUBSCRIPTION'|'OVER_MAX_INSTANCES'|'NO_INSTANCES'|'TIMEOUT'|'HEALTH_CONSTRAINTS_INVALID'|'HEALTH_CONSTRAINTS'|'INTERNAL_ERROR'|'THROTTLED'|'ALARM_ACTIVE'|'AGENT_ISSUE'|'AUTO_SCALING_IAM_ROLE_PERMISSIONS'|'AUTO_SCALING_CONFIGURATION'|'MANUAL_STOP'|'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION'|'MISSING_ELB_INFORMATION'|'MISSING_GITHUB_TOKEN'|'ELASTIC_LOAD_BALANCING_INVALID'|'ELB_INVALID_INSTANCE'|'INVALID_LAMBDA_CONFIGURATION'|'INVALID_LAMBDA_FUNCTION'|'HOOK_EXECUTION_FAILURE',
                        'message': 'string'
                    },
                    'createTime': datetime(2015, 1, 1),
                    'startTime': datetime(2015, 1, 1),
                    'completeTime': datetime(2015, 1, 1),
                    'deploymentOverview': {
                        'Pending': 123,
                        'InProgress': 123,
                        'Succeeded': 123,
                        'Failed': 123,
                        'Skipped': 123,
                        'Ready': 123
                    },
                    'description': 'string',
                    'creator': 'user'|'autoscaling'|'codeDeployRollback',
                    'ignoreApplicationStopFailures': True|False,
                    'autoRollbackConfiguration': {
                        'enabled': True|False,
                        'events': [
                            'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                        ]
                    },
                    'updateOutdatedInstancesOnly': True|False,
                    'rollbackInfo': {
                        'rollbackDeploymentId': 'string',
                        'rollbackTriggeringDeploymentId': 'string',
                        'rollbackMessage': 'string'
                    },
                    'deploymentStyle': {
                        'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                        'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                    },
                    'targetInstances': {
                        'tagFilters': [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                        'autoScalingGroups': [
                            'string',
                        ],
                        'ec2TagSet': {
                            'ec2TagSetList': [
                                [
                                    {
                                        'Key': 'string',
                                        'Value': 'string',
                                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                    },
                                ],
                            ]
                        }
                    },
                    'instanceTerminationWaitTimeStarted': True|False,
                    'blueGreenDeploymentConfiguration': {
                        'terminateBlueInstancesOnDeploymentSuccess': {
                            'action': 'TERMINATE'|'KEEP_ALIVE',
                            'terminationWaitTimeInMinutes': 123
                        },
                        'deploymentReadyOption': {
                            'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                            'waitTimeInMinutes': 123
                        },
                        'greenFleetProvisioningOption': {
                            'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                        }
                    },
                    'loadBalancerInfo': {
                        'elbInfoList': [
                            {
                                'name': 'string'
                            },
                        ],
                        'targetGroupInfoList': [
                            {
                                'name': 'string'
                            },
                        ]
                    },
                    'additionalDeploymentStatusInfo': 'string',
                    'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN',
                    'deploymentStatusMessages': [
                        'string',
                    ],
                    'computePlatform': 'Server'|'Lambda'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a BatchGetDeployments operation.

        
        

        - **deploymentsInfo** *(list) --* 

          Information about the deployments.

          
          

          - *(dict) --* 

            Information about a deployment.

            
            

            - **applicationName** *(string) --* 

              The application name.

              
            

            - **deploymentGroupName** *(string) --* 

              The deployment group name.

              
            

            - **deploymentConfigName** *(string) --* 

              The deployment configuration name.

              
            

            - **deploymentId** *(string) --* 

              The deployment ID.

              
            

            - **previousRevision** *(dict) --* 

              Information about the application revision that was deployed to the deployment group before the most recent successful deployment.

              
              

              - **revisionType** *(string) --* 

                The type of application revision:

                 

                 
                * S3: An application revision stored in Amazon S3. 
                 
                * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
                 
                * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
                 

                
              

              - **s3Location** *(dict) --* 

                Information about the location of a revision stored in Amazon S3. 

                
                

                - **bucket** *(string) --* 

                  The name of the Amazon S3 bucket where the application revision is stored.

                  
                

                - **key** *(string) --* 

                  The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                  
                

                - **bundleType** *(string) --* 

                  The file type of the application revision. Must be one of the following:

                   

                   
                  * tar: A tar archive file. 
                   
                  * tgz: A compressed tar archive file. 
                   
                  * zip: A zip archive file. 
                   

                  
                

                - **version** *(string) --* 

                  A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                   

                  If the version is not specified, the system will use the most recent version by default.

                  
                

                - **eTag** *(string) --* 

                  The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                   

                  If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                  
            
              

              - **gitHubLocation** *(dict) --* 

                Information about the location of application artifacts stored in GitHub.

                
                

                - **repository** *(string) --* 

                  The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                   

                  Specified as account/repository.

                  
                

                - **commitId** *(string) --* 

                  The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                  
            
              

              - **string** *(dict) --* 

                Information about the location of an AWS Lambda deployment revision stored as a RawString.

                
                

                - **content** *(string) --* 

                  The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                  
                

                - **sha256** *(string) --* 

                  The SHA256 hash value of the revision that is specified as a RawString.

                  
            
          
            

            - **revision** *(dict) --* 

              Information about the location of stored application artifacts and the service from which to retrieve them.

              
              

              - **revisionType** *(string) --* 

                The type of application revision:

                 

                 
                * S3: An application revision stored in Amazon S3. 
                 
                * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
                 
                * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
                 

                
              

              - **s3Location** *(dict) --* 

                Information about the location of a revision stored in Amazon S3. 

                
                

                - **bucket** *(string) --* 

                  The name of the Amazon S3 bucket where the application revision is stored.

                  
                

                - **key** *(string) --* 

                  The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                  
                

                - **bundleType** *(string) --* 

                  The file type of the application revision. Must be one of the following:

                   

                   
                  * tar: A tar archive file. 
                   
                  * tgz: A compressed tar archive file. 
                   
                  * zip: A zip archive file. 
                   

                  
                

                - **version** *(string) --* 

                  A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                   

                  If the version is not specified, the system will use the most recent version by default.

                  
                

                - **eTag** *(string) --* 

                  The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                   

                  If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                  
            
              

              - **gitHubLocation** *(dict) --* 

                Information about the location of application artifacts stored in GitHub.

                
                

                - **repository** *(string) --* 

                  The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                   

                  Specified as account/repository.

                  
                

                - **commitId** *(string) --* 

                  The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                  
            
              

              - **string** *(dict) --* 

                Information about the location of an AWS Lambda deployment revision stored as a RawString.

                
                

                - **content** *(string) --* 

                  The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                  
                

                - **sha256** *(string) --* 

                  The SHA256 hash value of the revision that is specified as a RawString.

                  
            
          
            

            - **status** *(string) --* 

              The current state of the deployment as a whole.

              
            

            - **errorInformation** *(dict) --* 

              Information about any error associated with this deployment.

              
              

              - **code** *(string) --* 

                For information about additional error codes, see `Error Codes for AWS CodeDeploy <http://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in the `AWS CodeDeploy User Guide <http://docs.aws.amazon.com/codedeploy/latest/userguide>`__ .

                 

                The error code:

                 

                 
                * APPLICATION_MISSING: The application was missing. This error code will most likely be raised if the application is deleted after the deployment is created but before it is started. 
                 
                * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code will most likely be raised if the deployment group is deleted after the deployment is created but before it is started. 
                 
                * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified. 
                 
                * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified. 
                 
                * IAM_ROLE_MISSING: The service role cannot be accessed. 
                 
                * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions. 
                 
                * INTERNAL_ERROR: There was an internal error. 
                 
                * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to the Amazon EC2 service. 
                 
                * NO_INSTANCES: No instance were specified, or no instance can be found. 
                 
                * OVER_MAX_INSTANCES: The maximum number of instance was exceeded. 
                 
                * THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more AWS services. 
                 
                * TIMEOUT: The deployment has timed out. 
                 
                * REVISION_MISSING: The revision ID was missing. This error code will most likely be raised if the revision is deleted after the deployment is created but before it is started. 
                 

                
              

              - **message** *(string) --* 

                An accompanying error message.

                
          
            

            - **createTime** *(datetime) --* 

              A timestamp indicating when the deployment was created.

              
            

            - **startTime** *(datetime) --* 

              A timestamp indicating when the deployment was deployed to the deployment group.

               

              In some cases, the reported value of the start time may be later than the complete time. This is due to differences in the clock settings of back-end servers that participate in the deployment process.

              
            

            - **completeTime** *(datetime) --* 

              A timestamp indicating when the deployment was complete.

              
            

            - **deploymentOverview** *(dict) --* 

              A summary of the deployment status of the instances in the deployment.

              
              

              - **Pending** *(integer) --* 

                The number of instances in the deployment in a pending state.

                
              

              - **InProgress** *(integer) --* 

                The number of instances in which the deployment is in progress.

                
              

              - **Succeeded** *(integer) --* 

                The number of instances in the deployment to which revisions have been successfully deployed.

                
              

              - **Failed** *(integer) --* 

                The number of instances in the deployment in a failed state.

                
              

              - **Skipped** *(integer) --* 

                The number of instances in the deployment in a skipped state.

                
              

              - **Ready** *(integer) --* 

                The number of instances in a replacement environment ready to receive traffic in a blue/green deployment.

                
          
            

            - **description** *(string) --* 

              A comment about the deployment.

              
            

            - **creator** *(string) --* 

              The means by which the deployment was created:

               

               
              * user: A user created the deployment. 
               
              * autoscaling: Auto Scaling created the deployment. 
               
              * codeDeployRollback: A rollback process created the deployment. 
               

              
            

            - **ignoreApplicationStopFailures** *(boolean) --* 

              If true, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will not be considered to have failed at that point and will continue on to the BeforeInstall deployment lifecycle event.

               

              If false or not specified, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will stop, and the deployment to that instance will be considered to have failed.

              
            

            - **autoRollbackConfiguration** *(dict) --* 

              Information about the automatic rollback configuration associated with the deployment.

              
              

              - **enabled** *(boolean) --* 

                Indicates whether a defined automatic rollback configuration is currently enabled.

                
              

              - **events** *(list) --* 

                The event type or types that trigger a rollback.

                
                

                - *(string) --* 
            
          
            

            - **updateOutdatedInstancesOnly** *(boolean) --* 

              Indicates whether only instances that are not running the latest application revision are to be deployed to.

              
            

            - **rollbackInfo** *(dict) --* 

              Information about a deployment rollback.

              
              

              - **rollbackDeploymentId** *(string) --* 

                The ID of the deployment rollback.

                
              

              - **rollbackTriggeringDeploymentId** *(string) --* 

                The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.

                
              

              - **rollbackMessage** *(string) --* 

                Information describing the status of a deployment rollback; for example, whether the deployment can't be rolled back, is in progress, failed, or succeeded. 

                
          
            

            - **deploymentStyle** *(dict) --* 

              Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

              
              

              - **deploymentType** *(string) --* 

                Indicates whether to run an in-place deployment or a blue/green deployment.

                
              

              - **deploymentOption** *(string) --* 

                Indicates whether to route deployment traffic behind a load balancer.

                
          
            

            - **targetInstances** *(dict) --* 

              Information about the instances that belong to the replacement environment in a blue/green deployment.

              
              

              - **tagFilters** *(list) --* 

                The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as ec2TagSet.

                
                

                - *(dict) --* 

                  Information about an EC2 tag filter.

                  
                  

                  - **Key** *(string) --* 

                    The tag filter key.

                    
                  

                  - **Value** *(string) --* 

                    The tag filter value.

                    
                  

                  - **Type** *(string) --* 

                    The tag filter type:

                     

                     
                    * KEY_ONLY: Key only. 
                     
                    * VALUE_ONLY: Value only. 
                     
                    * KEY_AND_VALUE: Key and value. 
                     

                    
              
            
              

              - **autoScalingGroups** *(list) --* 

                The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.

                
                

                - *(string) --* 
            
              

              - **ec2TagSet** *(dict) --* 

                Information about the groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as tagFilters.

                
                

                - **ec2TagSetList** *(list) --* 

                  A list containing other lists of EC2 instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

                  
                  

                  - *(list) --* 
                    

                    - *(dict) --* 

                      Information about an EC2 tag filter.

                      
                      

                      - **Key** *(string) --* 

                        The tag filter key.

                        
                      

                      - **Value** *(string) --* 

                        The tag filter value.

                        
                      

                      - **Type** *(string) --* 

                        The tag filter type:

                         

                         
                        * KEY_ONLY: Key only. 
                         
                        * VALUE_ONLY: Value only. 
                         
                        * KEY_AND_VALUE: Key and value. 
                         

                        
                  
                
              
            
          
            

            - **instanceTerminationWaitTimeStarted** *(boolean) --* 

              Indicates whether the wait period set for the termination of instances in the original environment has started. Status is 'false' if the KEEP_ALIVE option is specified; otherwise, 'true' as soon as the termination wait period starts.

              
            

            - **blueGreenDeploymentConfiguration** *(dict) --* 

              Information about blue/green deployment options for this deployment.

              
              

              - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --* 

                Information about whether to terminate instances in the original fleet during a blue/green deployment.

                
                

                - **action** *(string) --* 

                  The action to take on instances in the original environment after a successful blue/green deployment.

                   

                   
                  * TERMINATE: Instances are terminated after a specified wait time. 
                   
                  * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group. 
                   

                  
                

                - **terminationWaitTimeInMinutes** *(integer) --* 

                  The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.

                  
            
              

              - **deploymentReadyOption** *(dict) --* 

                Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

                
                

                - **actionOnTimeout** *(string) --* 

                  Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

                   

                   
                  * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment. 
                   
                  * STOP_DEPLOYMENT: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped. 
                   

                  
                

                - **waitTimeInMinutes** *(integer) --* 

                  The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout

                  
            
              

              - **greenFleetProvisioningOption** *(dict) --* 

                Information about how instances are provisioned for a replacement environment in a blue/green deployment.

                
                

                - **action** *(string) --* 

                  The method used to add instances to a replacement environment.

                   

                   
                  * DISCOVER_EXISTING: Use instances that already exist or will be created manually. 
                   
                  * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group. 
                   

                  
            
          
            

            - **loadBalancerInfo** *(dict) --* 

              Information about the load balancer used in the deployment.

              
              

              - **elbInfoList** *(list) --* 

                An array containing information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

                
                

                - *(dict) --* 

                  Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

                  
                  

                  - **name** *(string) --* 

                    For blue/green deployments, the name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.

                    
              
            
              

              - **targetGroupInfoList** *(list) --* 

                An array containing information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

                
                

                - *(dict) --* 

                  Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

                  
                  

                  - **name** *(string) --* 

                    For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes. 

                    
              
            
          
            

            - **additionalDeploymentStatusInfo** *(string) --* 

              Provides information about the results of a deployment, such as whether instances in the original environment in a blue/green deployment were not terminated.

              
            

            - **fileExistsBehavior** *(string) --* 

              Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.

               

               
              * DISALLOW: The deployment fails. This is also the default behavior if no option is specified. 
               
              * OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance. 
               
              * RETAIN: The version of the file already on the instance is kept and used as part of the new deployment. 
               

              
            

            - **deploymentStatusMessages** *(list) --* 

              Messages that contain information about the status of a deployment.

              
              

              - *(string) --* 
          
            

            - **computePlatform** *(string) --* 

              The destination platform type for the deployment (``Lambda`` or ``Server`` ).

              
        
      
    

  .. py:method:: batch_get_on_premises_instances(**kwargs)

    

    Gets information about one or more on-premises instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetOnPremisesInstances>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_on_premises_instances(
          instanceNames=[
              'string',
          ]
      )
    :type instanceNames: list
    :param instanceNames: **[REQUIRED]** 

      The names of the on-premises instances about which to get information.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instanceInfos': [
                {
                    'instanceName': 'string',
                    'iamSessionArn': 'string',
                    'iamUserArn': 'string',
                    'instanceArn': 'string',
                    'registerTime': datetime(2015, 1, 1),
                    'deregisterTime': datetime(2015, 1, 1),
                    'tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a BatchGetOnPremisesInstances operation.

        
        

        - **instanceInfos** *(list) --* 

          Information about the on-premises instances.

          
          

          - *(dict) --* 

            Information about an on-premises instance.

            
            

            - **instanceName** *(string) --* 

              The name of the on-premises instance.

              
            

            - **iamSessionArn** *(string) --* 

              The ARN of the IAM session associated with the on-premises instance.

              
            

            - **iamUserArn** *(string) --* 

              The IAM user ARN associated with the on-premises instance.

              
            

            - **instanceArn** *(string) --* 

              The ARN of the on-premises instance.

              
            

            - **registerTime** *(datetime) --* 

              The time at which the on-premises instance was registered.

              
            

            - **deregisterTime** *(datetime) --* 

              If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.

              
            

            - **tags** *(list) --* 

              The tags currently associated with the on-premises instance.

              
              

              - *(dict) --* 

                Information about a tag.

                
                

                - **Key** *(string) --* 

                  The tag's key.

                  
                

                - **Value** *(string) --* 

                  The tag's value.

                  
            
          
        
      
    

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


  .. py:method:: continue_deployment(**kwargs)

    

    For a blue/green deployment, starts the process of rerouting traffic from instances in the original environment to instances in the replacement environment without waiting for a specified wait time to elapse. (Traffic rerouting, which is achieved by registering instances in the replacement environment with the load balancer, can start as soon as all instances have a status of Ready.) 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ContinueDeployment>`_    


    **Request Syntax** 
    ::

      response = client.continue_deployment(
          deploymentId='string'
      )
    :type deploymentId: string
    :param deploymentId: 

      The deployment ID of the blue/green deployment for which you want to start rerouting traffic to the replacement environment.

      

    
    
    :returns: None

  .. py:method:: create_application(**kwargs)

    

    Creates an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateApplication>`_    


    **Request Syntax** 
    ::

      response = client.create_application(
          applicationName='string',
          computePlatform='Server'|'Lambda'
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of the application. This name must be unique with the applicable IAM user or AWS account.

      

    
    :type computePlatform: string
    :param computePlatform: 

      The destination platform type for the deployment (``Lambda`` or ``Server`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'applicationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a CreateApplication operation.

        
        

        - **applicationId** *(string) --* 

          A unique application ID.

          
    

  .. py:method:: create_deployment(**kwargs)

    

    Deploys an application revision through the specified deployment group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateDeployment>`_    


    **Request Syntax** 
    ::

      response = client.create_deployment(
          applicationName='string',
          deploymentGroupName='string',
          revision={
              'revisionType': 'S3'|'GitHub'|'String',
              's3Location': {
                  'bucket': 'string',
                  'key': 'string',
                  'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                  'version': 'string',
                  'eTag': 'string'
              },
              'gitHubLocation': {
                  'repository': 'string',
                  'commitId': 'string'
              },
              'string': {
                  'content': 'string',
                  'sha256': 'string'
              }
          },
          deploymentConfigName='string',
          description='string',
          ignoreApplicationStopFailures=True|False,
          targetInstances={
              'tagFilters': [
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                  },
              ],
              'autoScalingGroups': [
                  'string',
              ],
              'ec2TagSet': {
                  'ec2TagSetList': [
                      [
                          {
                              'Key': 'string',
                              'Value': 'string',
                              'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                          },
                      ],
                  ]
              }
          },
          autoRollbackConfiguration={
              'enabled': True|False,
              'events': [
                  'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
              ]
          },
          updateOutdatedInstancesOnly=True|False,
          fileExistsBehavior='DISALLOW'|'OVERWRITE'|'RETAIN'
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type deploymentGroupName: string
    :param deploymentGroupName: 

      The name of the deployment group.

      

    
    :type revision: dict
    :param revision: 

      The type and location of the revision to deploy.

      

    
      - **revisionType** *(string) --* 

        The type of application revision:

         

         
        * S3: An application revision stored in Amazon S3. 
         
        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
         
        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
         

        

      
      - **s3Location** *(dict) --* 

        Information about the location of a revision stored in Amazon S3. 

        

      
        - **bucket** *(string) --* 

          The name of the Amazon S3 bucket where the application revision is stored.

          

        
        - **key** *(string) --* 

          The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

          

        
        - **bundleType** *(string) --* 

          The file type of the application revision. Must be one of the following:

           

           
          * tar: A tar archive file. 
           
          * tgz: A compressed tar archive file. 
           
          * zip: A zip archive file. 
           

          

        
        - **version** *(string) --* 

          A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

           

          If the version is not specified, the system will use the most recent version by default.

          

        
        - **eTag** *(string) --* 

          The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

           

          If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

          

        
      
      - **gitHubLocation** *(dict) --* 

        Information about the location of application artifacts stored in GitHub.

        

      
        - **repository** *(string) --* 

          The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

           

          Specified as account/repository.

          

        
        - **commitId** *(string) --* 

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

          

        
      
      - **string** *(dict) --* 

        Information about the location of an AWS Lambda deployment revision stored as a RawString.

        

      
        - **content** *(string) --* 

          The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

          

        
        - **sha256** *(string) --* 

          The SHA256 hash value of the revision that is specified as a RawString.

          

        
      
    
    :type deploymentConfigName: string
    :param deploymentConfigName: 

      The name of a deployment configuration associated with the applicable IAM user or AWS account.

       

      If not specified, the value configured in the deployment group will be used as the default. If the deployment group does not have a deployment configuration associated with it, then CodeDeployDefault.OneAtATime will be used by default.

      

    
    :type description: string
    :param description: 

      A comment about the deployment.

      

    
    :type ignoreApplicationStopFailures: boolean
    :param ignoreApplicationStopFailures: 

      If set to true, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will not be considered to have failed at that point and will continue on to the BeforeInstall deployment lifecycle event.

       

      If set to false or not specified, then if the deployment causes the ApplicationStop deployment lifecycle event to fail to an instance, the deployment to that instance will stop, and the deployment to that instance will be considered to have failed.

      

    
    :type targetInstances: dict
    :param targetInstances: 

      Information about the instances that will belong to the replacement environment in a blue/green deployment.

      

    
      - **tagFilters** *(list) --* 

        The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as ec2TagSet.

        

      
        - *(dict) --* 

          Information about an EC2 tag filter.

          

        
          - **Key** *(string) --* 

            The tag filter key.

            

          
          - **Value** *(string) --* 

            The tag filter value.

            

          
          - **Type** *(string) --* 

            The tag filter type:

             

             
            * KEY_ONLY: Key only. 
             
            * VALUE_ONLY: Value only. 
             
            * KEY_AND_VALUE: Key and value. 
             

            

          
        
    
      - **autoScalingGroups** *(list) --* 

        The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.

        

      
        - *(string) --* 

        
    
      - **ec2TagSet** *(dict) --* 

        Information about the groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as tagFilters.

        

      
        - **ec2TagSetList** *(list) --* 

          A list containing other lists of EC2 instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

          

        
          - *(list) --* 

          
            - *(dict) --* 

              Information about an EC2 tag filter.

              

            
              - **Key** *(string) --* 

                The tag filter key.

                

              
              - **Value** *(string) --* 

                The tag filter value.

                

              
              - **Type** *(string) --* 

                The tag filter type:

                 

                 
                * KEY_ONLY: Key only. 
                 
                * VALUE_ONLY: Value only. 
                 
                * KEY_AND_VALUE: Key and value. 
                 

                

              
            
        
      
      
    
    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: 

      Configuration information for an automatic rollback that is added when a deployment is created.

      

    
      - **enabled** *(boolean) --* 

        Indicates whether a defined automatic rollback configuration is currently enabled.

        

      
      - **events** *(list) --* 

        The event type or types that trigger a rollback.

        

      
        - *(string) --* 

        
    
    
    :type updateOutdatedInstancesOnly: boolean
    :param updateOutdatedInstancesOnly: 

      Indicates whether to deploy to all instances or only to instances that are not running the latest application revision.

      

    
    :type fileExistsBehavior: string
    :param fileExistsBehavior: 

      Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.

       

      The fileExistsBehavior parameter takes any of the following values:

       

       
      * DISALLOW: The deployment fails. This is also the default behavior if no option is specified. 
       
      * OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance. 
       
      * RETAIN: The version of the file already on the instance is kept and used as part of the new deployment. 
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a CreateDeployment operation.

        
        

        - **deploymentId** *(string) --* 

          A unique deployment ID.

          
    

  .. py:method:: create_deployment_config(**kwargs)

    

    Creates a deployment configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateDeploymentConfig>`_    


    **Request Syntax** 
    ::

      response = client.create_deployment_config(
          deploymentConfigName='string',
          minimumHealthyHosts={
              'value': 123,
              'type': 'HOST_COUNT'|'FLEET_PERCENT'
          },
          trafficRoutingConfig={
              'type': 'TimeBasedCanary'|'TimeBasedLinear'|'AllAtOnce',
              'timeBasedCanary': {
                  'canaryPercentage': 123,
                  'canaryInterval': 123
              },
              'timeBasedLinear': {
                  'linearPercentage': 123,
                  'linearInterval': 123
              }
          },
          computePlatform='Server'|'Lambda'
      )
    :type deploymentConfigName: string
    :param deploymentConfigName: **[REQUIRED]** 

      The name of the deployment configuration to create.

      

    
    :type minimumHealthyHosts: dict
    :param minimumHealthyHosts: **[REQUIRED]** 

      The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.

       

      The type parameter takes either of the following values:

       

       
      * HOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value. 
       
      * FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances. 
       

       

      The value parameter takes an integer.

       

      For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a value of 95.

      

    
      - **value** *(integer) --* 

        The minimum healthy instance value.

        

      
      - **type** *(string) --* 

        The minimum healthy instance type:

         

         
        * HOST_COUNT: The minimum number of healthy instance as an absolute value. 
         
        * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total number of instance in the deployment. 
         

         

        In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment will be successful if six or more instances are deployed to successfully; otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instance at a time. The deployment will be successful if four or more instance are deployed to successfully; otherwise, the deployment fails.

         

        .. note::

           

          In a call to the get deployment configuration operation, CodeDeployDefault.OneAtATime will return a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy will try to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment still succeeds.

           

         

        For more information, see `AWS CodeDeploy Instance Health <http://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`__ in the *AWS CodeDeploy User Guide* .

        

      
    
    :type trafficRoutingConfig: dict
    :param trafficRoutingConfig: 

      The configuration that specifies how the deployment traffic will be routed.

      

    
      - **type** *(string) --* 

        The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a deployment configuration .

        

      
      - **timeBasedCanary** *(dict) --* 

        A configuration that shifts traffic from one version of a Lambda function to another in two increments. The original and target Lambda function versions are specified in the deployment's AppSpec file.

        

      
        - **canaryPercentage** *(integer) --* 

          The percentage of traffic to shift in the first increment of a ``TimeBasedCanary`` deployment.

          

        
        - **canaryInterval** *(integer) --* 

          The number of minutes between the first and second traffic shifts of a ``TimeBasedCanary`` deployment.

          

        
      
      - **timeBasedLinear** *(dict) --* 

        A configuration that shifts traffic from one version of a Lambda function to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions are specified in the deployment's AppSpec file.

        

      
        - **linearPercentage** *(integer) --* 

          The percentage of traffic that is shifted at the start of each increment of a ``TimeBasedLinear`` deployment.

          

        
        - **linearInterval** *(integer) --* 

          The number of minutes between each incremental traffic shift of a ``TimeBasedLinear`` deployment.

          

        
      
    
    :type computePlatform: string
    :param computePlatform: 

      The destination platform type for the deployment (``Lambda`` or ``Server`` >).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentConfigId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a CreateDeploymentConfig operation.

        
        

        - **deploymentConfigId** *(string) --* 

          A unique deployment configuration ID.

          
    

  .. py:method:: create_deployment_group(**kwargs)

    

    Creates a deployment group to which application revisions will be deployed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateDeploymentGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_deployment_group(
          applicationName='string',
          deploymentGroupName='string',
          deploymentConfigName='string',
          ec2TagFilters=[
              {
                  'Key': 'string',
                  'Value': 'string',
                  'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
              },
          ],
          onPremisesInstanceTagFilters=[
              {
                  'Key': 'string',
                  'Value': 'string',
                  'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
              },
          ],
          autoScalingGroups=[
              'string',
          ],
          serviceRoleArn='string',
          triggerConfigurations=[
              {
                  'triggerName': 'string',
                  'triggerTargetArn': 'string',
                  'triggerEvents': [
                      'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                  ]
              },
          ],
          alarmConfiguration={
              'enabled': True|False,
              'ignorePollAlarmFailure': True|False,
              'alarms': [
                  {
                      'name': 'string'
                  },
              ]
          },
          autoRollbackConfiguration={
              'enabled': True|False,
              'events': [
                  'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
              ]
          },
          deploymentStyle={
              'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
              'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
          },
          blueGreenDeploymentConfiguration={
              'terminateBlueInstancesOnDeploymentSuccess': {
                  'action': 'TERMINATE'|'KEEP_ALIVE',
                  'terminationWaitTimeInMinutes': 123
              },
              'deploymentReadyOption': {
                  'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                  'waitTimeInMinutes': 123
              },
              'greenFleetProvisioningOption': {
                  'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
              }
          },
          loadBalancerInfo={
              'elbInfoList': [
                  {
                      'name': 'string'
                  },
              ],
              'targetGroupInfoList': [
                  {
                      'name': 'string'
                  },
              ]
          },
          ec2TagSet={
              'ec2TagSetList': [
                  [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                      },
                  ],
              ]
          },
          onPremisesTagSet={
              'onPremisesTagSetList': [
                  [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                      },
                  ],
              ]
          }
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type deploymentGroupName: string
    :param deploymentGroupName: **[REQUIRED]** 

      The name of a new deployment group for the specified application.

      

    
    :type deploymentConfigName: string
    :param deploymentConfigName: 

      If specified, the deployment configuration name can be either one of the predefined configurations provided with AWS CodeDeploy or a custom deployment configuration that you create by calling the create deployment configuration operation.

       

      CodeDeployDefault.OneAtATime is the default deployment configuration. It is used if a configuration isn't specified for the deployment or the deployment group.

       

      For more information about the predefined deployment configurations in AWS CodeDeploy, see `Working with Deployment Groups in AWS CodeDeploy <http://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html>`__ in the AWS CodeDeploy User Guide.

      

    
    :type ec2TagFilters: list
    :param ec2TagFilters: 

      The Amazon EC2 tags on which to filter. The deployment group will include EC2 instances with any of the specified tags. Cannot be used in the same call as ec2TagSet.

      

    
      - *(dict) --* 

        Information about an EC2 tag filter.

        

      
        - **Key** *(string) --* 

          The tag filter key.

          

        
        - **Value** *(string) --* 

          The tag filter value.

          

        
        - **Type** *(string) --* 

          The tag filter type:

           

           
          * KEY_ONLY: Key only. 
           
          * VALUE_ONLY: Value only. 
           
          * KEY_AND_VALUE: Key and value. 
           

          

        
      
  
    :type onPremisesInstanceTagFilters: list
    :param onPremisesInstanceTagFilters: 

      The on-premises instance tags on which to filter. The deployment group will include on-premises instances with any of the specified tags. Cannot be used in the same call as OnPremisesTagSet.

      

    
      - *(dict) --* 

        Information about an on-premises instance tag filter.

        

      
        - **Key** *(string) --* 

          The on-premises instance tag filter key.

          

        
        - **Value** *(string) --* 

          The on-premises instance tag filter value.

          

        
        - **Type** *(string) --* 

          The on-premises instance tag filter type:

           

           
          * KEY_ONLY: Key only. 
           
          * VALUE_ONLY: Value only. 
           
          * KEY_AND_VALUE: Key and value. 
           

          

        
      
  
    :type autoScalingGroups: list
    :param autoScalingGroups: 

      A list of associated Auto Scaling groups.

      

    
      - *(string) --* 

      
  
    :type serviceRoleArn: string
    :param serviceRoleArn: **[REQUIRED]** 

      A service role ARN that allows AWS CodeDeploy to act on the user's behalf when interacting with AWS services.

      

    
    :type triggerConfigurations: list
    :param triggerConfigurations: 

      Information about triggers to create when the deployment group is created. For examples, see `Create a Trigger for an AWS CodeDeploy Event <http://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-sns.html>`__ in the AWS CodeDeploy User Guide.

      

    
      - *(dict) --* 

        Information about notification triggers for the deployment group.

        

      
        - **triggerName** *(string) --* 

          The name of the notification trigger.

          

        
        - **triggerTargetArn** *(string) --* 

          The ARN of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

          

        
        - **triggerEvents** *(list) --* 

          The event type or types for which notifications are triggered.

          

        
          - *(string) --* 

          
      
      
  
    :type alarmConfiguration: dict
    :param alarmConfiguration: 

      Information to add about Amazon CloudWatch alarms when the deployment group is created.

      

    
      - **enabled** *(boolean) --* 

        Indicates whether the alarm configuration is enabled.

        

      
      - **ignorePollAlarmFailure** *(boolean) --* 

        Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

         

         
        * true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch. 
         
        * false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch. 
         

        

      
      - **alarms** *(list) --* 

        A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.

        

      
        - *(dict) --* 

          Information about an alarm.

          

        
          - **name** *(string) --* 

            The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.

            

          
        
    
    
    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: 

      Configuration information for an automatic rollback that is added when a deployment group is created.

      

    
      - **enabled** *(boolean) --* 

        Indicates whether a defined automatic rollback configuration is currently enabled.

        

      
      - **events** *(list) --* 

        The event type or types that trigger a rollback.

        

      
        - *(string) --* 

        
    
    
    :type deploymentStyle: dict
    :param deploymentStyle: 

      Information about the type of deployment, in-place or blue/green, that you want to run and whether to route deployment traffic behind a load balancer.

      

    
      - **deploymentType** *(string) --* 

        Indicates whether to run an in-place deployment or a blue/green deployment.

        

      
      - **deploymentOption** *(string) --* 

        Indicates whether to route deployment traffic behind a load balancer.

        

      
    
    :type blueGreenDeploymentConfiguration: dict
    :param blueGreenDeploymentConfiguration: 

      Information about blue/green deployment options for a deployment group.

      

    
      - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --* 

        Information about whether to terminate instances in the original fleet during a blue/green deployment.

        

      
        - **action** *(string) --* 

          The action to take on instances in the original environment after a successful blue/green deployment.

           

           
          * TERMINATE: Instances are terminated after a specified wait time. 
           
          * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group. 
           

          

        
        - **terminationWaitTimeInMinutes** *(integer) --* 

          The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.

          

        
      
      - **deploymentReadyOption** *(dict) --* 

        Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

        

      
        - **actionOnTimeout** *(string) --* 

          Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

           

           
          * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment. 
           
          * STOP_DEPLOYMENT: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped. 
           

          

        
        - **waitTimeInMinutes** *(integer) --* 

          The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout

          

        
      
      - **greenFleetProvisioningOption** *(dict) --* 

        Information about how instances are provisioned for a replacement environment in a blue/green deployment.

        

      
        - **action** *(string) --* 

          The method used to add instances to a replacement environment.

           

           
          * DISCOVER_EXISTING: Use instances that already exist or will be created manually. 
           
          * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group. 
           

          

        
      
    
    :type loadBalancerInfo: dict
    :param loadBalancerInfo: 

      Information about the load balancer used in a deployment.

      

    
      - **elbInfoList** *(list) --* 

        An array containing information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

        

      
        - *(dict) --* 

          Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

          

        
          - **name** *(string) --* 

            For blue/green deployments, the name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.

            

          
        
    
      - **targetGroupInfoList** *(list) --* 

        An array containing information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

        

      
        - *(dict) --* 

          Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

          

        
          - **name** *(string) --* 

            For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes. 

            

          
        
    
    
    :type ec2TagSet: dict
    :param ec2TagSet: 

      Information about groups of tags applied to EC2 instances. The deployment group will include only EC2 instances identified by all the tag groups. Cannot be used in the same call as ec2TagFilters.

      

    
      - **ec2TagSetList** *(list) --* 

        A list containing other lists of EC2 instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

        

      
        - *(list) --* 

        
          - *(dict) --* 

            Information about an EC2 tag filter.

            

          
            - **Key** *(string) --* 

              The tag filter key.

              

            
            - **Value** *(string) --* 

              The tag filter value.

              

            
            - **Type** *(string) --* 

              The tag filter type:

               

               
              * KEY_ONLY: Key only. 
               
              * VALUE_ONLY: Value only. 
               
              * KEY_AND_VALUE: Key and value. 
               

              

            
          
      
    
    
    :type onPremisesTagSet: dict
    :param onPremisesTagSet: 

      Information about groups of tags applied to on-premises instances. The deployment group will include only on-premises instances identified by all the tag groups. Cannot be used in the same call as onPremisesInstanceTagFilters.

      

    
      - **onPremisesTagSetList** *(list) --* 

        A list containing other lists of on-premises instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

        

      
        - *(list) --* 

        
          - *(dict) --* 

            Information about an on-premises instance tag filter.

            

          
            - **Key** *(string) --* 

              The on-premises instance tag filter key.

              

            
            - **Value** *(string) --* 

              The on-premises instance tag filter value.

              

            
            - **Type** *(string) --* 

              The on-premises instance tag filter type:

               

               
              * KEY_ONLY: Key only. 
               
              * VALUE_ONLY: Value only. 
               
              * KEY_AND_VALUE: Key and value. 
               

              

            
          
      
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentGroupId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a CreateDeploymentGroup operation.

        
        

        - **deploymentGroupId** *(string) --* 

          A unique deployment group ID.

          
    

  .. py:method:: delete_application(**kwargs)

    

    Deletes an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeleteApplication>`_    


    **Request Syntax** 
    ::

      response = client.delete_application(
          applicationName='string'
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    
    :returns: None

  .. py:method:: delete_deployment_config(**kwargs)

    

    Deletes a deployment configuration.

     

    .. note::

       

      A deployment configuration cannot be deleted if it is currently in use. Predefined configurations cannot be deleted.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeleteDeploymentConfig>`_    


    **Request Syntax** 
    ::

      response = client.delete_deployment_config(
          deploymentConfigName='string'
      )
    :type deploymentConfigName: string
    :param deploymentConfigName: **[REQUIRED]** 

      The name of a deployment configuration associated with the applicable IAM user or AWS account.

      

    
    
    :returns: None

  .. py:method:: delete_deployment_group(**kwargs)

    

    Deletes a deployment group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeleteDeploymentGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_deployment_group(
          applicationName='string',
          deploymentGroupName='string'
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type deploymentGroupName: string
    :param deploymentGroupName: **[REQUIRED]** 

      The name of an existing deployment group for the specified application.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'hooksNotCleanedUp': [
                {
                    'name': 'string',
                    'hook': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a DeleteDeploymentGroup operation.

        
        

        - **hooksNotCleanedUp** *(list) --* 

          If the output contains no data, and the corresponding deployment group contained at least one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group. If the output contains data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group.

          
          

          - *(dict) --* 

            Information about an Auto Scaling group.

            
            

            - **name** *(string) --* 

              The Auto Scaling group name.

              
            

            - **hook** *(string) --* 

              An Auto Scaling lifecycle event hook name.

              
        
      
    

  .. py:method:: deregister_on_premises_instance(**kwargs)

    

    Deregisters an on-premises instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeregisterOnPremisesInstance>`_    


    **Request Syntax** 
    ::

      response = client.deregister_on_premises_instance(
          instanceName='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the on-premises instance to deregister.

      

    
    
    :returns: None

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


  .. py:method:: get_application(**kwargs)

    

    Gets information about an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetApplication>`_    


    **Request Syntax** 
    ::

      response = client.get_application(
          applicationName='string'
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'application': {
                'applicationId': 'string',
                'applicationName': 'string',
                'createTime': datetime(2015, 1, 1),
                'linkedToGitHub': True|False,
                'gitHubAccountName': 'string',
                'computePlatform': 'Server'|'Lambda'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a GetApplication operation.

        
        

        - **application** *(dict) --* 

          Information about the application.

          
          

          - **applicationId** *(string) --* 

            The application ID.

            
          

          - **applicationName** *(string) --* 

            The application name.

            
          

          - **createTime** *(datetime) --* 

            The time at which the application was created.

            
          

          - **linkedToGitHub** *(boolean) --* 

            True if the user has authenticated with GitHub for the specified application; otherwise, false.

            
          

          - **gitHubAccountName** *(string) --* 

            The name for a connection to a GitHub account.

            
          

          - **computePlatform** *(string) --* 

            The destination platform type for deployment of the application (``Lambda`` or ``Server`` ).

            
      
    

  .. py:method:: get_application_revision(**kwargs)

    

    Gets information about an application revision.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetApplicationRevision>`_    


    **Request Syntax** 
    ::

      response = client.get_application_revision(
          applicationName='string',
          revision={
              'revisionType': 'S3'|'GitHub'|'String',
              's3Location': {
                  'bucket': 'string',
                  'key': 'string',
                  'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                  'version': 'string',
                  'eTag': 'string'
              },
              'gitHubLocation': {
                  'repository': 'string',
                  'commitId': 'string'
              },
              'string': {
                  'content': 'string',
                  'sha256': 'string'
              }
          }
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of the application that corresponds to the revision.

      

    
    :type revision: dict
    :param revision: **[REQUIRED]** 

      Information about the application revision to get, including type and location.

      

    
      - **revisionType** *(string) --* 

        The type of application revision:

         

         
        * S3: An application revision stored in Amazon S3. 
         
        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
         
        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
         

        

      
      - **s3Location** *(dict) --* 

        Information about the location of a revision stored in Amazon S3. 

        

      
        - **bucket** *(string) --* 

          The name of the Amazon S3 bucket where the application revision is stored.

          

        
        - **key** *(string) --* 

          The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

          

        
        - **bundleType** *(string) --* 

          The file type of the application revision. Must be one of the following:

           

           
          * tar: A tar archive file. 
           
          * tgz: A compressed tar archive file. 
           
          * zip: A zip archive file. 
           

          

        
        - **version** *(string) --* 

          A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

           

          If the version is not specified, the system will use the most recent version by default.

          

        
        - **eTag** *(string) --* 

          The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

           

          If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

          

        
      
      - **gitHubLocation** *(dict) --* 

        Information about the location of application artifacts stored in GitHub.

        

      
        - **repository** *(string) --* 

          The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

           

          Specified as account/repository.

          

        
        - **commitId** *(string) --* 

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

          

        
      
      - **string** *(dict) --* 

        Information about the location of an AWS Lambda deployment revision stored as a RawString.

        

      
        - **content** *(string) --* 

          The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

          

        
        - **sha256** *(string) --* 

          The SHA256 hash value of the revision that is specified as a RawString.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'applicationName': 'string',
            'revision': {
                'revisionType': 'S3'|'GitHub'|'String',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
            'revisionInfo': {
                'description': 'string',
                'deploymentGroups': [
                    'string',
                ],
                'firstUsedTime': datetime(2015, 1, 1),
                'lastUsedTime': datetime(2015, 1, 1),
                'registerTime': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a GetApplicationRevision operation.

        
        

        - **applicationName** *(string) --* 

          The name of the application that corresponds to the revision.

          
        

        - **revision** *(dict) --* 

          Additional information about the revision, including type and location.

          
          

          - **revisionType** *(string) --* 

            The type of application revision:

             

             
            * S3: An application revision stored in Amazon S3. 
             
            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
             
            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
             

            
          

          - **s3Location** *(dict) --* 

            Information about the location of a revision stored in Amazon S3. 

            
            

            - **bucket** *(string) --* 

              The name of the Amazon S3 bucket where the application revision is stored.

              
            

            - **key** *(string) --* 

              The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

              
            

            - **bundleType** *(string) --* 

              The file type of the application revision. Must be one of the following:

               

               
              * tar: A tar archive file. 
               
              * tgz: A compressed tar archive file. 
               
              * zip: A zip archive file. 
               

              
            

            - **version** *(string) --* 

              A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

               

              If the version is not specified, the system will use the most recent version by default.

              
            

            - **eTag** *(string) --* 

              The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

               

              If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

              
        
          

          - **gitHubLocation** *(dict) --* 

            Information about the location of application artifacts stored in GitHub.

            
            

            - **repository** *(string) --* 

              The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

               

              Specified as account/repository.

              
            

            - **commitId** *(string) --* 

              The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

              
        
          

          - **string** *(dict) --* 

            Information about the location of an AWS Lambda deployment revision stored as a RawString.

            
            

            - **content** *(string) --* 

              The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

              
            

            - **sha256** *(string) --* 

              The SHA256 hash value of the revision that is specified as a RawString.

              
        
      
        

        - **revisionInfo** *(dict) --* 

          General information about the revision.

          
          

          - **description** *(string) --* 

            A comment about the revision.

            
          

          - **deploymentGroups** *(list) --* 

            The deployment groups for which this is the current target revision.

            
            

            - *(string) --* 
        
          

          - **firstUsedTime** *(datetime) --* 

            When the revision was first used by AWS CodeDeploy.

            
          

          - **lastUsedTime** *(datetime) --* 

            When the revision was last used by AWS CodeDeploy.

            
          

          - **registerTime** *(datetime) --* 

            When the revision was registered with AWS CodeDeploy.

            
      
    

  .. py:method:: get_deployment(**kwargs)

    

    Gets information about a deployment.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeployment>`_    


    **Request Syntax** 
    ::

      response = client.get_deployment(
          deploymentId='string'
      )
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      A deployment ID associated with the applicable IAM user or AWS account.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentInfo': {
                'applicationName': 'string',
                'deploymentGroupName': 'string',
                'deploymentConfigName': 'string',
                'deploymentId': 'string',
                'previousRevision': {
                    'revisionType': 'S3'|'GitHub'|'String',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
                'revision': {
                    'revisionType': 'S3'|'GitHub'|'String',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
                'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'errorInformation': {
                    'code': 'DEPLOYMENT_GROUP_MISSING'|'APPLICATION_MISSING'|'REVISION_MISSING'|'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'NO_EC2_SUBSCRIPTION'|'OVER_MAX_INSTANCES'|'NO_INSTANCES'|'TIMEOUT'|'HEALTH_CONSTRAINTS_INVALID'|'HEALTH_CONSTRAINTS'|'INTERNAL_ERROR'|'THROTTLED'|'ALARM_ACTIVE'|'AGENT_ISSUE'|'AUTO_SCALING_IAM_ROLE_PERMISSIONS'|'AUTO_SCALING_CONFIGURATION'|'MANUAL_STOP'|'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION'|'MISSING_ELB_INFORMATION'|'MISSING_GITHUB_TOKEN'|'ELASTIC_LOAD_BALANCING_INVALID'|'ELB_INVALID_INSTANCE'|'INVALID_LAMBDA_CONFIGURATION'|'INVALID_LAMBDA_FUNCTION'|'HOOK_EXECUTION_FAILURE',
                    'message': 'string'
                },
                'createTime': datetime(2015, 1, 1),
                'startTime': datetime(2015, 1, 1),
                'completeTime': datetime(2015, 1, 1),
                'deploymentOverview': {
                    'Pending': 123,
                    'InProgress': 123,
                    'Succeeded': 123,
                    'Failed': 123,
                    'Skipped': 123,
                    'Ready': 123
                },
                'description': 'string',
                'creator': 'user'|'autoscaling'|'codeDeployRollback',
                'ignoreApplicationStopFailures': True|False,
                'autoRollbackConfiguration': {
                    'enabled': True|False,
                    'events': [
                        'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                    ]
                },
                'updateOutdatedInstancesOnly': True|False,
                'rollbackInfo': {
                    'rollbackDeploymentId': 'string',
                    'rollbackTriggeringDeploymentId': 'string',
                    'rollbackMessage': 'string'
                },
                'deploymentStyle': {
                    'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                    'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                },
                'targetInstances': {
                    'tagFilters': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                    'autoScalingGroups': [
                        'string',
                    ],
                    'ec2TagSet': {
                        'ec2TagSetList': [
                            [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                },
                            ],
                        ]
                    }
                },
                'instanceTerminationWaitTimeStarted': True|False,
                'blueGreenDeploymentConfiguration': {
                    'terminateBlueInstancesOnDeploymentSuccess': {
                        'action': 'TERMINATE'|'KEEP_ALIVE',
                        'terminationWaitTimeInMinutes': 123
                    },
                    'deploymentReadyOption': {
                        'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                        'waitTimeInMinutes': 123
                    },
                    'greenFleetProvisioningOption': {
                        'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                    }
                },
                'loadBalancerInfo': {
                    'elbInfoList': [
                        {
                            'name': 'string'
                        },
                    ],
                    'targetGroupInfoList': [
                        {
                            'name': 'string'
                        },
                    ]
                },
                'additionalDeploymentStatusInfo': 'string',
                'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN',
                'deploymentStatusMessages': [
                    'string',
                ],
                'computePlatform': 'Server'|'Lambda'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a GetDeployment operation.

        
        

        - **deploymentInfo** *(dict) --* 

          Information about the deployment.

          
          

          - **applicationName** *(string) --* 

            The application name.

            
          

          - **deploymentGroupName** *(string) --* 

            The deployment group name.

            
          

          - **deploymentConfigName** *(string) --* 

            The deployment configuration name.

            
          

          - **deploymentId** *(string) --* 

            The deployment ID.

            
          

          - **previousRevision** *(dict) --* 

            Information about the application revision that was deployed to the deployment group before the most recent successful deployment.

            
            

            - **revisionType** *(string) --* 

              The type of application revision:

               

               
              * S3: An application revision stored in Amazon S3. 
               
              * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
               
              * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
               

              
            

            - **s3Location** *(dict) --* 

              Information about the location of a revision stored in Amazon S3. 

              
              

              - **bucket** *(string) --* 

                The name of the Amazon S3 bucket where the application revision is stored.

                
              

              - **key** *(string) --* 

                The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                
              

              - **bundleType** *(string) --* 

                The file type of the application revision. Must be one of the following:

                 

                 
                * tar: A tar archive file. 
                 
                * tgz: A compressed tar archive file. 
                 
                * zip: A zip archive file. 
                 

                
              

              - **version** *(string) --* 

                A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the version is not specified, the system will use the most recent version by default.

                
              

              - **eTag** *(string) --* 

                The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                
          
            

            - **gitHubLocation** *(dict) --* 

              Information about the location of application artifacts stored in GitHub.

              
              

              - **repository** *(string) --* 

                The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                 

                Specified as account/repository.

                
              

              - **commitId** *(string) --* 

                The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                
          
            

            - **string** *(dict) --* 

              Information about the location of an AWS Lambda deployment revision stored as a RawString.

              
              

              - **content** *(string) --* 

                The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                
              

              - **sha256** *(string) --* 

                The SHA256 hash value of the revision that is specified as a RawString.

                
          
        
          

          - **revision** *(dict) --* 

            Information about the location of stored application artifacts and the service from which to retrieve them.

            
            

            - **revisionType** *(string) --* 

              The type of application revision:

               

               
              * S3: An application revision stored in Amazon S3. 
               
              * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
               
              * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
               

              
            

            - **s3Location** *(dict) --* 

              Information about the location of a revision stored in Amazon S3. 

              
              

              - **bucket** *(string) --* 

                The name of the Amazon S3 bucket where the application revision is stored.

                
              

              - **key** *(string) --* 

                The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                
              

              - **bundleType** *(string) --* 

                The file type of the application revision. Must be one of the following:

                 

                 
                * tar: A tar archive file. 
                 
                * tgz: A compressed tar archive file. 
                 
                * zip: A zip archive file. 
                 

                
              

              - **version** *(string) --* 

                A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the version is not specified, the system will use the most recent version by default.

                
              

              - **eTag** *(string) --* 

                The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                
          
            

            - **gitHubLocation** *(dict) --* 

              Information about the location of application artifacts stored in GitHub.

              
              

              - **repository** *(string) --* 

                The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                 

                Specified as account/repository.

                
              

              - **commitId** *(string) --* 

                The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                
          
            

            - **string** *(dict) --* 

              Information about the location of an AWS Lambda deployment revision stored as a RawString.

              
              

              - **content** *(string) --* 

                The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                
              

              - **sha256** *(string) --* 

                The SHA256 hash value of the revision that is specified as a RawString.

                
          
        
          

          - **status** *(string) --* 

            The current state of the deployment as a whole.

            
          

          - **errorInformation** *(dict) --* 

            Information about any error associated with this deployment.

            
            

            - **code** *(string) --* 

              For information about additional error codes, see `Error Codes for AWS CodeDeploy <http://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in the `AWS CodeDeploy User Guide <http://docs.aws.amazon.com/codedeploy/latest/userguide>`__ .

               

              The error code:

               

               
              * APPLICATION_MISSING: The application was missing. This error code will most likely be raised if the application is deleted after the deployment is created but before it is started. 
               
              * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code will most likely be raised if the deployment group is deleted after the deployment is created but before it is started. 
               
              * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified. 
               
              * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified. 
               
              * IAM_ROLE_MISSING: The service role cannot be accessed. 
               
              * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions. 
               
              * INTERNAL_ERROR: There was an internal error. 
               
              * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to the Amazon EC2 service. 
               
              * NO_INSTANCES: No instance were specified, or no instance can be found. 
               
              * OVER_MAX_INSTANCES: The maximum number of instance was exceeded. 
               
              * THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more AWS services. 
               
              * TIMEOUT: The deployment has timed out. 
               
              * REVISION_MISSING: The revision ID was missing. This error code will most likely be raised if the revision is deleted after the deployment is created but before it is started. 
               

              
            

            - **message** *(string) --* 

              An accompanying error message.

              
        
          

          - **createTime** *(datetime) --* 

            A timestamp indicating when the deployment was created.

            
          

          - **startTime** *(datetime) --* 

            A timestamp indicating when the deployment was deployed to the deployment group.

             

            In some cases, the reported value of the start time may be later than the complete time. This is due to differences in the clock settings of back-end servers that participate in the deployment process.

            
          

          - **completeTime** *(datetime) --* 

            A timestamp indicating when the deployment was complete.

            
          

          - **deploymentOverview** *(dict) --* 

            A summary of the deployment status of the instances in the deployment.

            
            

            - **Pending** *(integer) --* 

              The number of instances in the deployment in a pending state.

              
            

            - **InProgress** *(integer) --* 

              The number of instances in which the deployment is in progress.

              
            

            - **Succeeded** *(integer) --* 

              The number of instances in the deployment to which revisions have been successfully deployed.

              
            

            - **Failed** *(integer) --* 

              The number of instances in the deployment in a failed state.

              
            

            - **Skipped** *(integer) --* 

              The number of instances in the deployment in a skipped state.

              
            

            - **Ready** *(integer) --* 

              The number of instances in a replacement environment ready to receive traffic in a blue/green deployment.

              
        
          

          - **description** *(string) --* 

            A comment about the deployment.

            
          

          - **creator** *(string) --* 

            The means by which the deployment was created:

             

             
            * user: A user created the deployment. 
             
            * autoscaling: Auto Scaling created the deployment. 
             
            * codeDeployRollback: A rollback process created the deployment. 
             

            
          

          - **ignoreApplicationStopFailures** *(boolean) --* 

            If true, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will not be considered to have failed at that point and will continue on to the BeforeInstall deployment lifecycle event.

             

            If false or not specified, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will stop, and the deployment to that instance will be considered to have failed.

            
          

          - **autoRollbackConfiguration** *(dict) --* 

            Information about the automatic rollback configuration associated with the deployment.

            
            

            - **enabled** *(boolean) --* 

              Indicates whether a defined automatic rollback configuration is currently enabled.

              
            

            - **events** *(list) --* 

              The event type or types that trigger a rollback.

              
              

              - *(string) --* 
          
        
          

          - **updateOutdatedInstancesOnly** *(boolean) --* 

            Indicates whether only instances that are not running the latest application revision are to be deployed to.

            
          

          - **rollbackInfo** *(dict) --* 

            Information about a deployment rollback.

            
            

            - **rollbackDeploymentId** *(string) --* 

              The ID of the deployment rollback.

              
            

            - **rollbackTriggeringDeploymentId** *(string) --* 

              The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.

              
            

            - **rollbackMessage** *(string) --* 

              Information describing the status of a deployment rollback; for example, whether the deployment can't be rolled back, is in progress, failed, or succeeded. 

              
        
          

          - **deploymentStyle** *(dict) --* 

            Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

            
            

            - **deploymentType** *(string) --* 

              Indicates whether to run an in-place deployment or a blue/green deployment.

              
            

            - **deploymentOption** *(string) --* 

              Indicates whether to route deployment traffic behind a load balancer.

              
        
          

          - **targetInstances** *(dict) --* 

            Information about the instances that belong to the replacement environment in a blue/green deployment.

            
            

            - **tagFilters** *(list) --* 

              The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as ec2TagSet.

              
              

              - *(dict) --* 

                Information about an EC2 tag filter.

                
                

                - **Key** *(string) --* 

                  The tag filter key.

                  
                

                - **Value** *(string) --* 

                  The tag filter value.

                  
                

                - **Type** *(string) --* 

                  The tag filter type:

                   

                   
                  * KEY_ONLY: Key only. 
                   
                  * VALUE_ONLY: Value only. 
                   
                  * KEY_AND_VALUE: Key and value. 
                   

                  
            
          
            

            - **autoScalingGroups** *(list) --* 

              The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.

              
              

              - *(string) --* 
          
            

            - **ec2TagSet** *(dict) --* 

              Information about the groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as tagFilters.

              
              

              - **ec2TagSetList** *(list) --* 

                A list containing other lists of EC2 instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

                
                

                - *(list) --* 
                  

                  - *(dict) --* 

                    Information about an EC2 tag filter.

                    
                    

                    - **Key** *(string) --* 

                      The tag filter key.

                      
                    

                    - **Value** *(string) --* 

                      The tag filter value.

                      
                    

                    - **Type** *(string) --* 

                      The tag filter type:

                       

                       
                      * KEY_ONLY: Key only. 
                       
                      * VALUE_ONLY: Value only. 
                       
                      * KEY_AND_VALUE: Key and value. 
                       

                      
                
              
            
          
        
          

          - **instanceTerminationWaitTimeStarted** *(boolean) --* 

            Indicates whether the wait period set for the termination of instances in the original environment has started. Status is 'false' if the KEEP_ALIVE option is specified; otherwise, 'true' as soon as the termination wait period starts.

            
          

          - **blueGreenDeploymentConfiguration** *(dict) --* 

            Information about blue/green deployment options for this deployment.

            
            

            - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --* 

              Information about whether to terminate instances in the original fleet during a blue/green deployment.

              
              

              - **action** *(string) --* 

                The action to take on instances in the original environment after a successful blue/green deployment.

                 

                 
                * TERMINATE: Instances are terminated after a specified wait time. 
                 
                * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group. 
                 

                
              

              - **terminationWaitTimeInMinutes** *(integer) --* 

                The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.

                
          
            

            - **deploymentReadyOption** *(dict) --* 

              Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

              
              

              - **actionOnTimeout** *(string) --* 

                Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

                 

                 
                * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment. 
                 
                * STOP_DEPLOYMENT: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped. 
                 

                
              

              - **waitTimeInMinutes** *(integer) --* 

                The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout

                
          
            

            - **greenFleetProvisioningOption** *(dict) --* 

              Information about how instances are provisioned for a replacement environment in a blue/green deployment.

              
              

              - **action** *(string) --* 

                The method used to add instances to a replacement environment.

                 

                 
                * DISCOVER_EXISTING: Use instances that already exist or will be created manually. 
                 
                * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group. 
                 

                
          
        
          

          - **loadBalancerInfo** *(dict) --* 

            Information about the load balancer used in the deployment.

            
            

            - **elbInfoList** *(list) --* 

              An array containing information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

              
              

              - *(dict) --* 

                Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

                
                

                - **name** *(string) --* 

                  For blue/green deployments, the name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.

                  
            
          
            

            - **targetGroupInfoList** *(list) --* 

              An array containing information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

              
              

              - *(dict) --* 

                Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

                
                

                - **name** *(string) --* 

                  For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes. 

                  
            
          
        
          

          - **additionalDeploymentStatusInfo** *(string) --* 

            Provides information about the results of a deployment, such as whether instances in the original environment in a blue/green deployment were not terminated.

            
          

          - **fileExistsBehavior** *(string) --* 

            Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.

             

             
            * DISALLOW: The deployment fails. This is also the default behavior if no option is specified. 
             
            * OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance. 
             
            * RETAIN: The version of the file already on the instance is kept and used as part of the new deployment. 
             

            
          

          - **deploymentStatusMessages** *(list) --* 

            Messages that contain information about the status of a deployment.

            
            

            - *(string) --* 
        
          

          - **computePlatform** *(string) --* 

            The destination platform type for the deployment (``Lambda`` or ``Server`` ).

            
      
    

  .. py:method:: get_deployment_config(**kwargs)

    

    Gets information about a deployment configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeploymentConfig>`_    


    **Request Syntax** 
    ::

      response = client.get_deployment_config(
          deploymentConfigName='string'
      )
    :type deploymentConfigName: string
    :param deploymentConfigName: **[REQUIRED]** 

      The name of a deployment configuration associated with the applicable IAM user or AWS account.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentConfigInfo': {
                'deploymentConfigId': 'string',
                'deploymentConfigName': 'string',
                'minimumHealthyHosts': {
                    'value': 123,
                    'type': 'HOST_COUNT'|'FLEET_PERCENT'
                },
                'createTime': datetime(2015, 1, 1),
                'computePlatform': 'Server'|'Lambda',
                'trafficRoutingConfig': {
                    'type': 'TimeBasedCanary'|'TimeBasedLinear'|'AllAtOnce',
                    'timeBasedCanary': {
                        'canaryPercentage': 123,
                        'canaryInterval': 123
                    },
                    'timeBasedLinear': {
                        'linearPercentage': 123,
                        'linearInterval': 123
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a GetDeploymentConfig operation.

        
        

        - **deploymentConfigInfo** *(dict) --* 

          Information about the deployment configuration.

          
          

          - **deploymentConfigId** *(string) --* 

            The deployment configuration ID.

            
          

          - **deploymentConfigName** *(string) --* 

            The deployment configuration name.

            
          

          - **minimumHealthyHosts** *(dict) --* 

            Information about the number or percentage of minimum healthy instance.

            
            

            - **value** *(integer) --* 

              The minimum healthy instance value.

              
            

            - **type** *(string) --* 

              The minimum healthy instance type:

               

               
              * HOST_COUNT: The minimum number of healthy instance as an absolute value. 
               
              * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total number of instance in the deployment. 
               

               

              In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment will be successful if six or more instances are deployed to successfully; otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instance at a time. The deployment will be successful if four or more instance are deployed to successfully; otherwise, the deployment fails.

               

              .. note::

                 

                In a call to the get deployment configuration operation, CodeDeployDefault.OneAtATime will return a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy will try to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment still succeeds.

                 

               

              For more information, see `AWS CodeDeploy Instance Health <http://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`__ in the *AWS CodeDeploy User Guide* .

              
        
          

          - **createTime** *(datetime) --* 

            The time at which the deployment configuration was created.

            
          

          - **computePlatform** *(string) --* 

            The destination platform type for the deployment (``Lambda`` or ``Server`` ).

            
          

          - **trafficRoutingConfig** *(dict) --* 

            The configuration specifying how the deployment traffic will be routed. Only deployments with a Lambda compute platform can specify this.

            
            

            - **type** *(string) --* 

              The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a deployment configuration .

              
            

            - **timeBasedCanary** *(dict) --* 

              A configuration that shifts traffic from one version of a Lambda function to another in two increments. The original and target Lambda function versions are specified in the deployment's AppSpec file.

              
              

              - **canaryPercentage** *(integer) --* 

                The percentage of traffic to shift in the first increment of a ``TimeBasedCanary`` deployment.

                
              

              - **canaryInterval** *(integer) --* 

                The number of minutes between the first and second traffic shifts of a ``TimeBasedCanary`` deployment.

                
          
            

            - **timeBasedLinear** *(dict) --* 

              A configuration that shifts traffic from one version of a Lambda function to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions are specified in the deployment's AppSpec file.

              
              

              - **linearPercentage** *(integer) --* 

                The percentage of traffic that is shifted at the start of each increment of a ``TimeBasedLinear`` deployment.

                
              

              - **linearInterval** *(integer) --* 

                The number of minutes between each incremental traffic shift of a ``TimeBasedLinear`` deployment.

                
          
        
      
    

  .. py:method:: get_deployment_group(**kwargs)

    

    Gets information about a deployment group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeploymentGroup>`_    


    **Request Syntax** 
    ::

      response = client.get_deployment_group(
          applicationName='string',
          deploymentGroupName='string'
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type deploymentGroupName: string
    :param deploymentGroupName: **[REQUIRED]** 

      The name of an existing deployment group for the specified application.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentGroupInfo': {
                'applicationName': 'string',
                'deploymentGroupId': 'string',
                'deploymentGroupName': 'string',
                'deploymentConfigName': 'string',
                'ec2TagFilters': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
                'onPremisesInstanceTagFilters': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
                'autoScalingGroups': [
                    {
                        'name': 'string',
                        'hook': 'string'
                    },
                ],
                'serviceRoleArn': 'string',
                'targetRevision': {
                    'revisionType': 'S3'|'GitHub'|'String',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
                'triggerConfigurations': [
                    {
                        'triggerName': 'string',
                        'triggerTargetArn': 'string',
                        'triggerEvents': [
                            'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                        ]
                    },
                ],
                'alarmConfiguration': {
                    'enabled': True|False,
                    'ignorePollAlarmFailure': True|False,
                    'alarms': [
                        {
                            'name': 'string'
                        },
                    ]
                },
                'autoRollbackConfiguration': {
                    'enabled': True|False,
                    'events': [
                        'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                    ]
                },
                'deploymentStyle': {
                    'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                    'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                },
                'blueGreenDeploymentConfiguration': {
                    'terminateBlueInstancesOnDeploymentSuccess': {
                        'action': 'TERMINATE'|'KEEP_ALIVE',
                        'terminationWaitTimeInMinutes': 123
                    },
                    'deploymentReadyOption': {
                        'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                        'waitTimeInMinutes': 123
                    },
                    'greenFleetProvisioningOption': {
                        'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                    }
                },
                'loadBalancerInfo': {
                    'elbInfoList': [
                        {
                            'name': 'string'
                        },
                    ],
                    'targetGroupInfoList': [
                        {
                            'name': 'string'
                        },
                    ]
                },
                'lastSuccessfulDeployment': {
                    'deploymentId': 'string',
                    'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                    'endTime': datetime(2015, 1, 1),
                    'createTime': datetime(2015, 1, 1)
                },
                'lastAttemptedDeployment': {
                    'deploymentId': 'string',
                    'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                    'endTime': datetime(2015, 1, 1),
                    'createTime': datetime(2015, 1, 1)
                },
                'ec2TagSet': {
                    'ec2TagSetList': [
                        [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                    ]
                },
                'onPremisesTagSet': {
                    'onPremisesTagSetList': [
                        [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                    ]
                },
                'computePlatform': 'Server'|'Lambda'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a GetDeploymentGroup operation.

        
        

        - **deploymentGroupInfo** *(dict) --* 

          Information about the deployment group.

          
          

          - **applicationName** *(string) --* 

            The application name.

            
          

          - **deploymentGroupId** *(string) --* 

            The deployment group ID.

            
          

          - **deploymentGroupName** *(string) --* 

            The deployment group name.

            
          

          - **deploymentConfigName** *(string) --* 

            The deployment configuration name.

            
          

          - **ec2TagFilters** *(list) --* 

            The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with any of the specified tags.

            
            

            - *(dict) --* 

              Information about an EC2 tag filter.

              
              

              - **Key** *(string) --* 

                The tag filter key.

                
              

              - **Value** *(string) --* 

                The tag filter value.

                
              

              - **Type** *(string) --* 

                The tag filter type:

                 

                 
                * KEY_ONLY: Key only. 
                 
                * VALUE_ONLY: Value only. 
                 
                * KEY_AND_VALUE: Key and value. 
                 

                
          
        
          

          - **onPremisesInstanceTagFilters** *(list) --* 

            The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags.

            
            

            - *(dict) --* 

              Information about an on-premises instance tag filter.

              
              

              - **Key** *(string) --* 

                The on-premises instance tag filter key.

                
              

              - **Value** *(string) --* 

                The on-premises instance tag filter value.

                
              

              - **Type** *(string) --* 

                The on-premises instance tag filter type:

                 

                 
                * KEY_ONLY: Key only. 
                 
                * VALUE_ONLY: Value only. 
                 
                * KEY_AND_VALUE: Key and value. 
                 

                
          
        
          

          - **autoScalingGroups** *(list) --* 

            A list of associated Auto Scaling groups.

            
            

            - *(dict) --* 

              Information about an Auto Scaling group.

              
              

              - **name** *(string) --* 

                The Auto Scaling group name.

                
              

              - **hook** *(string) --* 

                An Auto Scaling lifecycle event hook name.

                
          
        
          

          - **serviceRoleArn** *(string) --* 

            A service role ARN.

            
          

          - **targetRevision** *(dict) --* 

            Information about the deployment group's target revision, including type and location.

            
            

            - **revisionType** *(string) --* 

              The type of application revision:

               

               
              * S3: An application revision stored in Amazon S3. 
               
              * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
               
              * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
               

              
            

            - **s3Location** *(dict) --* 

              Information about the location of a revision stored in Amazon S3. 

              
              

              - **bucket** *(string) --* 

                The name of the Amazon S3 bucket where the application revision is stored.

                
              

              - **key** *(string) --* 

                The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                
              

              - **bundleType** *(string) --* 

                The file type of the application revision. Must be one of the following:

                 

                 
                * tar: A tar archive file. 
                 
                * tgz: A compressed tar archive file. 
                 
                * zip: A zip archive file. 
                 

                
              

              - **version** *(string) --* 

                A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the version is not specified, the system will use the most recent version by default.

                
              

              - **eTag** *(string) --* 

                The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                
          
            

            - **gitHubLocation** *(dict) --* 

              Information about the location of application artifacts stored in GitHub.

              
              

              - **repository** *(string) --* 

                The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                 

                Specified as account/repository.

                
              

              - **commitId** *(string) --* 

                The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                
          
            

            - **string** *(dict) --* 

              Information about the location of an AWS Lambda deployment revision stored as a RawString.

              
              

              - **content** *(string) --* 

                The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                
              

              - **sha256** *(string) --* 

                The SHA256 hash value of the revision that is specified as a RawString.

                
          
        
          

          - **triggerConfigurations** *(list) --* 

            Information about triggers associated with the deployment group.

            
            

            - *(dict) --* 

              Information about notification triggers for the deployment group.

              
              

              - **triggerName** *(string) --* 

                The name of the notification trigger.

                
              

              - **triggerTargetArn** *(string) --* 

                The ARN of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

                
              

              - **triggerEvents** *(list) --* 

                The event type or types for which notifications are triggered.

                
                

                - *(string) --* 
            
          
        
          

          - **alarmConfiguration** *(dict) --* 

            A list of alarms associated with the deployment group.

            
            

            - **enabled** *(boolean) --* 

              Indicates whether the alarm configuration is enabled.

              
            

            - **ignorePollAlarmFailure** *(boolean) --* 

              Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

               

               
              * true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch. 
               
              * false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch. 
               

              
            

            - **alarms** *(list) --* 

              A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.

              
              

              - *(dict) --* 

                Information about an alarm.

                
                

                - **name** *(string) --* 

                  The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.

                  
            
          
        
          

          - **autoRollbackConfiguration** *(dict) --* 

            Information about the automatic rollback configuration associated with the deployment group.

            
            

            - **enabled** *(boolean) --* 

              Indicates whether a defined automatic rollback configuration is currently enabled.

              
            

            - **events** *(list) --* 

              The event type or types that trigger a rollback.

              
              

              - *(string) --* 
          
        
          

          - **deploymentStyle** *(dict) --* 

            Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

            
            

            - **deploymentType** *(string) --* 

              Indicates whether to run an in-place deployment or a blue/green deployment.

              
            

            - **deploymentOption** *(string) --* 

              Indicates whether to route deployment traffic behind a load balancer.

              
        
          

          - **blueGreenDeploymentConfiguration** *(dict) --* 

            Information about blue/green deployment options for a deployment group.

            
            

            - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --* 

              Information about whether to terminate instances in the original fleet during a blue/green deployment.

              
              

              - **action** *(string) --* 

                The action to take on instances in the original environment after a successful blue/green deployment.

                 

                 
                * TERMINATE: Instances are terminated after a specified wait time. 
                 
                * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group. 
                 

                
              

              - **terminationWaitTimeInMinutes** *(integer) --* 

                The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.

                
          
            

            - **deploymentReadyOption** *(dict) --* 

              Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

              
              

              - **actionOnTimeout** *(string) --* 

                Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

                 

                 
                * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment. 
                 
                * STOP_DEPLOYMENT: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped. 
                 

                
              

              - **waitTimeInMinutes** *(integer) --* 

                The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout

                
          
            

            - **greenFleetProvisioningOption** *(dict) --* 

              Information about how instances are provisioned for a replacement environment in a blue/green deployment.

              
              

              - **action** *(string) --* 

                The method used to add instances to a replacement environment.

                 

                 
                * DISCOVER_EXISTING: Use instances that already exist or will be created manually. 
                 
                * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group. 
                 

                
          
        
          

          - **loadBalancerInfo** *(dict) --* 

            Information about the load balancer to use in a deployment.

            
            

            - **elbInfoList** *(list) --* 

              An array containing information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

              
              

              - *(dict) --* 

                Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

                
                

                - **name** *(string) --* 

                  For blue/green deployments, the name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.

                  
            
          
            

            - **targetGroupInfoList** *(list) --* 

              An array containing information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

              
              

              - *(dict) --* 

                Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

                
                

                - **name** *(string) --* 

                  For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes. 

                  
            
          
        
          

          - **lastSuccessfulDeployment** *(dict) --* 

            Information about the most recent successful deployment to the deployment group.

            
            

            - **deploymentId** *(string) --* 

              The deployment ID.

              
            

            - **status** *(string) --* 

              The status of the most recent deployment.

              
            

            - **endTime** *(datetime) --* 

              A timestamp indicating when the most recent deployment to the deployment group completed.

              
            

            - **createTime** *(datetime) --* 

              A timestamp indicating when the most recent deployment to the deployment group started.

              
        
          

          - **lastAttemptedDeployment** *(dict) --* 

            Information about the most recent attempted deployment to the deployment group.

            
            

            - **deploymentId** *(string) --* 

              The deployment ID.

              
            

            - **status** *(string) --* 

              The status of the most recent deployment.

              
            

            - **endTime** *(datetime) --* 

              A timestamp indicating when the most recent deployment to the deployment group completed.

              
            

            - **createTime** *(datetime) --* 

              A timestamp indicating when the most recent deployment to the deployment group started.

              
        
          

          - **ec2TagSet** *(dict) --* 

            Information about groups of tags applied to an EC2 instance. The deployment group includes only EC2 instances identified by all the tag groups. Cannot be used in the same call as ec2TagFilters.

            
            

            - **ec2TagSetList** *(list) --* 

              A list containing other lists of EC2 instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

              
              

              - *(list) --* 
                

                - *(dict) --* 

                  Information about an EC2 tag filter.

                  
                  

                  - **Key** *(string) --* 

                    The tag filter key.

                    
                  

                  - **Value** *(string) --* 

                    The tag filter value.

                    
                  

                  - **Type** *(string) --* 

                    The tag filter type:

                     

                     
                    * KEY_ONLY: Key only. 
                     
                    * VALUE_ONLY: Value only. 
                     
                    * KEY_AND_VALUE: Key and value. 
                     

                    
              
            
          
        
          

          - **onPremisesTagSet** *(dict) --* 

            Information about groups of tags applied to an on-premises instance. The deployment group includes only on-premises instances identified by all the tag groups. Cannot be used in the same call as onPremisesInstanceTagFilters.

            
            

            - **onPremisesTagSetList** *(list) --* 

              A list containing other lists of on-premises instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

              
              

              - *(list) --* 
                

                - *(dict) --* 

                  Information about an on-premises instance tag filter.

                  
                  

                  - **Key** *(string) --* 

                    The on-premises instance tag filter key.

                    
                  

                  - **Value** *(string) --* 

                    The on-premises instance tag filter value.

                    
                  

                  - **Type** *(string) --* 

                    The on-premises instance tag filter type:

                     

                     
                    * KEY_ONLY: Key only. 
                     
                    * VALUE_ONLY: Value only. 
                     
                    * KEY_AND_VALUE: Key and value. 
                     

                    
              
            
          
        
          

          - **computePlatform** *(string) --* 

            The destination platform type for the deployment group (``Lambda`` or ``Server`` ).

            
      
    

  .. py:method:: get_deployment_instance(**kwargs)

    

    Gets information about an instance as part of a deployment.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeploymentInstance>`_    


    **Request Syntax** 
    ::

      response = client.get_deployment_instance(
          deploymentId='string',
          instanceId='string'
      )
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      The unique ID of a deployment.

      

    
    :type instanceId: string
    :param instanceId: **[REQUIRED]** 

      The unique ID of an instance in the deployment group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instanceSummary': {
                'deploymentId': 'string',
                'instanceId': 'string',
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'instanceType': 'Blue'|'Green'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a GetDeploymentInstance operation.

        
        

        - **instanceSummary** *(dict) --* 

          Information about the instance.

          
          

          - **deploymentId** *(string) --* 

            The deployment ID.

            
          

          - **instanceId** *(string) --* 

            The instance ID.

            
          

          - **status** *(string) --* 

            The deployment status for this instance:

             

             
            * Pending: The deployment is pending for this instance. 
             
            * In Progress: The deployment is in progress for this instance. 
             
            * Succeeded: The deployment has succeeded for this instance. 
             
            * Failed: The deployment has failed for this instance. 
             
            * Skipped: The deployment has been skipped for this instance. 
             
            * Unknown: The deployment status is unknown for this instance. 
             

            
          

          - **lastUpdatedAt** *(datetime) --* 

            A timestamp indicating when the instance information was last updated.

            
          

          - **lifecycleEvents** *(list) --* 

            A list of lifecycle events for this instance.

            
            

            - *(dict) --* 

              Information about a deployment lifecycle event.

              
              

              - **lifecycleEventName** *(string) --* 

                The deployment lifecycle event name, such as ApplicationStop, BeforeInstall, AfterInstall, ApplicationStart, or ValidateService.

                
              

              - **diagnostics** *(dict) --* 

                Diagnostic information about the deployment lifecycle event.

                
                

                - **errorCode** *(string) --* 

                  The associated error code:

                   

                   
                  * Success: The specified script ran. 
                   
                  * ScriptMissing: The specified script was not found in the specified location. 
                   
                  * ScriptNotExecutable: The specified script is not a recognized executable file type. 
                   
                  * ScriptTimedOut: The specified script did not finish running in the specified time period. 
                   
                  * ScriptFailed: The specified script failed to run as expected. 
                   
                  * UnknownError: The specified script did not run for an unknown reason. 
                   

                  
                

                - **scriptName** *(string) --* 

                  The name of the script.

                  
                

                - **message** *(string) --* 

                  The message associated with the error.

                  
                

                - **logTail** *(string) --* 

                  The last portion of the diagnostic log.

                   

                  If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

                  
            
              

              - **startTime** *(datetime) --* 

                A timestamp indicating when the deployment lifecycle event started.

                
              

              - **endTime** *(datetime) --* 

                A timestamp indicating when the deployment lifecycle event ended.

                
              

              - **status** *(string) --* 

                The deployment lifecycle event status:

                 

                 
                * Pending: The deployment lifecycle event is pending. 
                 
                * InProgress: The deployment lifecycle event is in progress. 
                 
                * Succeeded: The deployment lifecycle event ran successfully. 
                 
                * Failed: The deployment lifecycle event has failed. 
                 
                * Skipped: The deployment lifecycle event has been skipped. 
                 
                * Unknown: The deployment lifecycle event is unknown. 
                 

                
          
        
          

          - **instanceType** *(string) --* 

            Information about which environment an instance belongs to in a blue/green deployment.

             

             
            * BLUE: The instance is part of the original environment. 
             
            * GREEN: The instance is part of the replacement environment. 
             

            
      
    

  .. py:method:: get_on_premises_instance(**kwargs)

    

    Gets information about an on-premises instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetOnPremisesInstance>`_    


    **Request Syntax** 
    ::

      response = client.get_on_premises_instance(
          instanceName='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the on-premises instance about which to get information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instanceInfo': {
                'instanceName': 'string',
                'iamSessionArn': 'string',
                'iamUserArn': 'string',
                'instanceArn': 'string',
                'registerTime': datetime(2015, 1, 1),
                'deregisterTime': datetime(2015, 1, 1),
                'tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a GetOnPremisesInstance operation.

        
        

        - **instanceInfo** *(dict) --* 

          Information about the on-premises instance.

          
          

          - **instanceName** *(string) --* 

            The name of the on-premises instance.

            
          

          - **iamSessionArn** *(string) --* 

            The ARN of the IAM session associated with the on-premises instance.

            
          

          - **iamUserArn** *(string) --* 

            The IAM user ARN associated with the on-premises instance.

            
          

          - **instanceArn** *(string) --* 

            The ARN of the on-premises instance.

            
          

          - **registerTime** *(datetime) --* 

            The time at which the on-premises instance was registered.

            
          

          - **deregisterTime** *(datetime) --* 

            If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.

            
          

          - **tags** *(list) --* 

            The tags currently associated with the on-premises instance.

            
            

            - *(dict) --* 

              Information about a tag.

              
              

              - **Key** *(string) --* 

                The tag's key.

                
              

              - **Value** *(string) --* 

                The tag's value.

                
          
        
      
    

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

        


  .. py:method:: list_application_revisions(**kwargs)

    

    Lists information about revisions for an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplicationRevisions>`_    


    **Request Syntax** 
    ::

      response = client.list_application_revisions(
          applicationName='string',
          sortBy='registerTime'|'firstUsedTime'|'lastUsedTime',
          sortOrder='ascending'|'descending',
          s3Bucket='string',
          s3KeyPrefix='string',
          deployed='include'|'exclude'|'ignore',
          nextToken='string'
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type sortBy: string
    :param sortBy: 

      The column name to use to sort the list results:

       

       
      * registerTime: Sort by the time the revisions were registered with AWS CodeDeploy. 
       
      * firstUsedTime: Sort by the time the revisions were first used in a deployment. 
       
      * lastUsedTime: Sort by the time the revisions were last used in a deployment. 
       

       

      If not specified or set to null, the results will be returned in an arbitrary order.

      

    
    :type sortOrder: string
    :param sortOrder: 

      The order in which to sort the list results:

       

       
      * ascending: ascending order. 
       
      * descending: descending order. 
       

       

      If not specified, the results will be sorted in ascending order.

       

      If set to null, the results will be sorted in an arbitrary order.

      

    
    :type s3Bucket: string
    :param s3Bucket: 

      An Amazon S3 bucket name to limit the search for revisions.

       

      If set to null, all of the user's buckets will be searched.

      

    
    :type s3KeyPrefix: string
    :param s3KeyPrefix: 

      A key prefix for the set of Amazon S3 objects to limit the search for revisions.

      

    
    :type deployed: string
    :param deployed: 

      Whether to list revisions based on whether the revision is the target revision of an deployment group:

       

       
      * include: List revisions that are target revisions of a deployment group. 
       
      * exclude: Do not list revisions that are target revisions of a deployment group. 
       
      * ignore: List all revisions. 
       

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier returned from the previous list application revisions call. It can be used to return the next set of applications in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'revisions': [
                {
                    'revisionType': 'S3'|'GitHub'|'String',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListApplicationRevisions operation.

        
        

        - **revisions** *(list) --* 

          A list of locations that contain the matching revisions.

          
          

          - *(dict) --* 

            Information about the location of an application revision.

            
            

            - **revisionType** *(string) --* 

              The type of application revision:

               

               
              * S3: An application revision stored in Amazon S3. 
               
              * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
               
              * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
               

              
            

            - **s3Location** *(dict) --* 

              Information about the location of a revision stored in Amazon S3. 

              
              

              - **bucket** *(string) --* 

                The name of the Amazon S3 bucket where the application revision is stored.

                
              

              - **key** *(string) --* 

                The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                
              

              - **bundleType** *(string) --* 

                The file type of the application revision. Must be one of the following:

                 

                 
                * tar: A tar archive file. 
                 
                * tgz: A compressed tar archive file. 
                 
                * zip: A zip archive file. 
                 

                
              

              - **version** *(string) --* 

                A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the version is not specified, the system will use the most recent version by default.

                
              

              - **eTag** *(string) --* 

                The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                
          
            

            - **gitHubLocation** *(dict) --* 

              Information about the location of application artifacts stored in GitHub.

              
              

              - **repository** *(string) --* 

                The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                 

                Specified as account/repository.

                
              

              - **commitId** *(string) --* 

                The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                
          
            

            - **string** *(dict) --* 

              Information about the location of an AWS Lambda deployment revision stored as a RawString.

              
              

              - **content** *(string) --* 

                The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                
              

              - **sha256** *(string) --* 

                The SHA256 hash value of the revision that is specified as a RawString.

                
          
        
      
        

        - **nextToken** *(string) --* 

          If a large amount of information is returned, an identifier will also be returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.

          
    

  .. py:method:: list_applications(**kwargs)

    

    Lists the applications registered with the applicable IAM user or AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplications>`_    


    **Request Syntax** 
    ::

      response = client.list_applications(
          nextToken='string'
      )
    :type nextToken: string
    :param nextToken: 

      An identifier returned from the previous list applications call. It can be used to return the next set of applications in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'applications': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListApplications operation.

        
        

        - **applications** *(list) --* 

          A list of application names.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list applications call to return the next set of applications, will also be returned. in the list.

          
    

  .. py:method:: list_deployment_configs(**kwargs)

    

    Lists the deployment configurations with the applicable IAM user or AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentConfigs>`_    


    **Request Syntax** 
    ::

      response = client.list_deployment_configs(
          nextToken='string'
      )
    :type nextToken: string
    :param nextToken: 

      An identifier returned from the previous list deployment configurations call. It can be used to return the next set of deployment configurations in the list. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentConfigsList': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListDeploymentConfigs operation.

        
        

        - **deploymentConfigsList** *(list) --* 

          A list of deployment configurations, including built-in configurations such as CodeDeployDefault.OneAtATime.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment configurations call to return the next set of deployment configurations in the list.

          
    

  .. py:method:: list_deployment_groups(**kwargs)

    

    Lists the deployment groups for an application registered with the applicable IAM user or AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentGroups>`_    


    **Request Syntax** 
    ::

      response = client.list_deployment_groups(
          applicationName='string',
          nextToken='string'
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier returned from the previous list deployment groups call. It can be used to return the next set of deployment groups in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'applicationName': 'string',
            'deploymentGroups': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListDeploymentGroups operation.

        
        

        - **applicationName** *(string) --* 

          The application name.

          
        

        - **deploymentGroups** *(list) --* 

          A list of corresponding deployment group names.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment groups call to return the next set of deployment groups in the list.

          
    

  .. py:method:: list_deployment_instances(**kwargs)

    

    Lists the instance for a deployment associated with the applicable IAM user or AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentInstances>`_    


    **Request Syntax** 
    ::

      response = client.list_deployment_instances(
          deploymentId='string',
          nextToken='string',
          instanceStatusFilter=[
              'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
          ],
          instanceTypeFilter=[
              'Blue'|'Green',
          ]
      )
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      The unique ID of a deployment.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier returned from the previous list deployment instances call. It can be used to return the next set of deployment instances in the list.

      

    
    :type instanceStatusFilter: list
    :param instanceStatusFilter: 

      A subset of instances to list by status:

       

       
      * Pending: Include those instance with pending deployments. 
       
      * InProgress: Include those instance where deployments are still in progress. 
       
      * Succeeded: Include those instances with successful deployments. 
       
      * Failed: Include those instance with failed deployments. 
       
      * Skipped: Include those instance with skipped deployments. 
       
      * Unknown: Include those instance with deployments in an unknown state. 
       

      

    
      - *(string) --* 

      
  
    :type instanceTypeFilter: list
    :param instanceTypeFilter: 

      The set of instances in a blue/green deployment, either those in the original environment ("BLUE") or those in the replacement environment ("GREEN"), for which you want to view instance information.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instancesList': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListDeploymentInstances operation.

        
        

        - **instancesList** *(list) --* 

          A list of instance IDs.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment instances call to return the next set of deployment instances in the list.

          
    

  .. py:method:: list_deployments(**kwargs)

    

    Lists the deployments in a deployment group for an application registered with the applicable IAM user or AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeployments>`_    


    **Request Syntax** 
    ::

      response = client.list_deployments(
          applicationName='string',
          deploymentGroupName='string',
          includeOnlyStatuses=[
              'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
          ],
          createTimeRange={
              'start': datetime(2015, 1, 1),
              'end': datetime(2015, 1, 1)
          },
          nextToken='string'
      )
    :type applicationName: string
    :param applicationName: 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type deploymentGroupName: string
    :param deploymentGroupName: 

      The name of an existing deployment group for the specified application.

      

    
    :type includeOnlyStatuses: list
    :param includeOnlyStatuses: 

      A subset of deployments to list by status:

       

       
      * Created: Include created deployments in the resulting list. 
       
      * Queued: Include queued deployments in the resulting list. 
       
      * In Progress: Include in-progress deployments in the resulting list. 
       
      * Succeeded: Include successful deployments in the resulting list. 
       
      * Failed: Include failed deployments in the resulting list. 
       
      * Stopped: Include stopped deployments in the resulting list. 
       

      

    
      - *(string) --* 

      
  
    :type createTimeRange: dict
    :param createTimeRange: 

      A time range (start and end) for returning a subset of the list of deployments.

      

    
      - **start** *(datetime) --* 

        The start time of the time range.

         

        .. note::

           

          Specify null to leave the start time open-ended.

           

        

      
      - **end** *(datetime) --* 

        The end time of the time range.

         

        .. note::

           

          Specify null to leave the end time open-ended.

           

        

      
    
    :type nextToken: string
    :param nextToken: 

      An identifier returned from the previous list deployments call. It can be used to return the next set of deployments in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deployments': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListDeployments operation.

        
        

        - **deployments** *(list) --* 

          A list of deployment IDs.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployments call to return the next set of deployments in the list.

          
    

  .. py:method:: list_git_hub_account_token_names(**kwargs)

    

    Lists the names of stored connections to GitHub accounts.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListGitHubAccountTokenNames>`_    


    **Request Syntax** 
    ::

      response = client.list_git_hub_account_token_names(
          nextToken='string'
      )
    :type nextToken: string
    :param nextToken: 

      An identifier returned from the previous ListGitHubAccountTokenNames call. It can be used to return the next set of names in the list. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tokenNameList': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListGitHubAccountTokenNames operation.

        
        

        - **tokenNameList** *(list) --* 

          A list of names of connections to GitHub accounts.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent ListGitHubAccountTokenNames call to return the next set of names in the list. 

          
    

  .. py:method:: list_on_premises_instances(**kwargs)

    

    Gets a list of names for one or more on-premises instances.

     

    Unless otherwise specified, both registered and deregistered on-premises instance names will be listed. To list only registered or deregistered on-premises instance names, use the registration status parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListOnPremisesInstances>`_    


    **Request Syntax** 
    ::

      response = client.list_on_premises_instances(
          registrationStatus='Registered'|'Deregistered',
          tagFilters=[
              {
                  'Key': 'string',
                  'Value': 'string',
                  'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
              },
          ],
          nextToken='string'
      )
    :type registrationStatus: string
    :param registrationStatus: 

      The registration status of the on-premises instances:

       

       
      * Deregistered: Include deregistered on-premises instances in the resulting list. 
       
      * Registered: Include registered on-premises instances in the resulting list. 
       

      

    
    :type tagFilters: list
    :param tagFilters: 

      The on-premises instance tags that will be used to restrict the corresponding on-premises instance names returned.

      

    
      - *(dict) --* 

        Information about an on-premises instance tag filter.

        

      
        - **Key** *(string) --* 

          The on-premises instance tag filter key.

          

        
        - **Value** *(string) --* 

          The on-premises instance tag filter value.

          

        
        - **Type** *(string) --* 

          The on-premises instance tag filter type:

           

           
          * KEY_ONLY: Key only. 
           
          * VALUE_ONLY: Value only. 
           
          * KEY_AND_VALUE: Key and value. 
           

          

        
      
  
    :type nextToken: string
    :param nextToken: 

      An identifier returned from the previous list on-premises instances call. It can be used to return the next set of on-premises instances in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instanceNames': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of list on-premises instances operation.

        
        

        - **instanceNames** *(list) --* 

          The list of matching on-premises instance names.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list on-premises instances call to return the next set of on-premises instances in the list.

          
    

  .. py:method:: put_lifecycle_event_hook_execution_status(**kwargs)

    

    Sets the result of a Lambda validation function. The function validates one or both lifecycle events (``BeforeAllowTraffic`` and ``AfterAllowTraffic`` ) and returns ``Succeeded`` or ``Failed`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus>`_    


    **Request Syntax** 
    ::

      response = client.put_lifecycle_event_hook_execution_status(
          deploymentId='string',
          lifecycleEventHookExecutionId='string',
          status='Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
      )
    :type deploymentId: string
    :param deploymentId: 

      The ID of the deployment. Pass this ID to a Lambda function that validates a deployment lifecycle event.

      

    
    :type lifecycleEventHookExecutionId: string
    :param lifecycleEventHookExecutionId: 

      The execution ID of a deployment's lifecycle hook. A deployment lifecycle hook is specified in the ``hooks`` section of the AppSpec file.

      

    
    :type status: string
    :param status: 

      The result of a Lambda function that validates a deployment lifecycle event (``Succeeded`` or ``Failed`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'lifecycleEventHookExecutionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **lifecycleEventHookExecutionId** *(string) --* 

          The execution ID of the lifecycle event hook. A hook is specified in the ``hooks`` section of the deployment's AppSpec file.

          
    

  .. py:method:: register_application_revision(**kwargs)

    

    Registers with AWS CodeDeploy a revision for the specified application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/RegisterApplicationRevision>`_    


    **Request Syntax** 
    ::

      response = client.register_application_revision(
          applicationName='string',
          description='string',
          revision={
              'revisionType': 'S3'|'GitHub'|'String',
              's3Location': {
                  'bucket': 'string',
                  'key': 'string',
                  'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                  'version': 'string',
                  'eTag': 'string'
              },
              'gitHubLocation': {
                  'repository': 'string',
                  'commitId': 'string'
              },
              'string': {
                  'content': 'string',
                  'sha256': 'string'
              }
          }
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type description: string
    :param description: 

      A comment about the revision.

      

    
    :type revision: dict
    :param revision: **[REQUIRED]** 

      Information about the application revision to register, including type and location.

      

    
      - **revisionType** *(string) --* 

        The type of application revision:

         

         
        * S3: An application revision stored in Amazon S3. 
         
        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
         
        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
         

        

      
      - **s3Location** *(dict) --* 

        Information about the location of a revision stored in Amazon S3. 

        

      
        - **bucket** *(string) --* 

          The name of the Amazon S3 bucket where the application revision is stored.

          

        
        - **key** *(string) --* 

          The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

          

        
        - **bundleType** *(string) --* 

          The file type of the application revision. Must be one of the following:

           

           
          * tar: A tar archive file. 
           
          * tgz: A compressed tar archive file. 
           
          * zip: A zip archive file. 
           

          

        
        - **version** *(string) --* 

          A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

           

          If the version is not specified, the system will use the most recent version by default.

          

        
        - **eTag** *(string) --* 

          The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

           

          If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

          

        
      
      - **gitHubLocation** *(dict) --* 

        Information about the location of application artifacts stored in GitHub.

        

      
        - **repository** *(string) --* 

          The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

           

          Specified as account/repository.

          

        
        - **commitId** *(string) --* 

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

          

        
      
      - **string** *(dict) --* 

        Information about the location of an AWS Lambda deployment revision stored as a RawString.

        

      
        - **content** *(string) --* 

          The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

          

        
        - **sha256** *(string) --* 

          The SHA256 hash value of the revision that is specified as a RawString.

          

        
      
    
    
    :returns: None

  .. py:method:: register_on_premises_instance(**kwargs)

    

    Registers an on-premises instance.

     

    .. note::

       

      Only one IAM ARN (an IAM session ARN or IAM user ARN) is supported in the request. You cannot use both.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/RegisterOnPremisesInstance>`_    


    **Request Syntax** 
    ::

      response = client.register_on_premises_instance(
          instanceName='string',
          iamSessionArn='string',
          iamUserArn='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the on-premises instance to register.

      

    
    :type iamSessionArn: string
    :param iamSessionArn: 

      The ARN of the IAM session to associate with the on-premises instance.

      

    
    :type iamUserArn: string
    :param iamUserArn: 

      The ARN of the IAM user to associate with the on-premises instance.

      

    
    
    :returns: None

  .. py:method:: remove_tags_from_on_premises_instances(**kwargs)

    

    Removes one or more tags from one or more on-premises instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags_from_on_premises_instances(
          tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          instanceNames=[
              'string',
          ]
      )
    :type tags: list
    :param tags: **[REQUIRED]** 

      The tag key-value pairs to remove from the on-premises instances.

      

    
      - *(dict) --* 

        Information about a tag.

        

      
        - **Key** *(string) --* 

          The tag's key.

          

        
        - **Value** *(string) --* 

          The tag's value.

          

        
      
  
    :type instanceNames: list
    :param instanceNames: **[REQUIRED]** 

      The names of the on-premises instances from which to remove tags.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: skip_wait_time_for_instance_termination(**kwargs)

    

    In a blue/green deployment, overrides any specified wait time and starts terminating instances immediately after the traffic routing is completed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination>`_    


    **Request Syntax** 
    ::

      response = client.skip_wait_time_for_instance_termination(
          deploymentId='string'
      )
    :type deploymentId: string
    :param deploymentId: 

      The ID of the blue/green deployment for which you want to skip the instance termination wait time.

      

    
    
    :returns: None

  .. py:method:: stop_deployment(**kwargs)

    

    Attempts to stop an ongoing deployment.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/StopDeployment>`_    


    **Request Syntax** 
    ::

      response = client.stop_deployment(
          deploymentId='string',
          autoRollbackEnabled=True|False
      )
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      The unique ID of a deployment.

      

    
    :type autoRollbackEnabled: boolean
    :param autoRollbackEnabled: 

      Indicates, when a deployment is stopped, whether instances that have been updated should be rolled back to the previous version of the application revision.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'status': 'Pending'|'Succeeded',
            'statusMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a StopDeployment operation.

        
        

        - **status** *(string) --* 

          The status of the stop deployment operation:

           

           
          * Pending: The stop operation is pending. 
           
          * Succeeded: The stop operation was successful. 
           

          
        

        - **statusMessage** *(string) --* 

          An accompanying status message.

          
    

  .. py:method:: update_application(**kwargs)

    

    Changes the name of an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/UpdateApplication>`_    


    **Request Syntax** 
    ::

      response = client.update_application(
          applicationName='string',
          newApplicationName='string'
      )
    :type applicationName: string
    :param applicationName: 

      The current name of the application you want to change.

      

    
    :type newApplicationName: string
    :param newApplicationName: 

      The new name to give the application.

      

    
    
    :returns: None

  .. py:method:: update_deployment_group(**kwargs)

    

    Changes information about a deployment group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/UpdateDeploymentGroup>`_    


    **Request Syntax** 
    ::

      response = client.update_deployment_group(
          applicationName='string',
          currentDeploymentGroupName='string',
          newDeploymentGroupName='string',
          deploymentConfigName='string',
          ec2TagFilters=[
              {
                  'Key': 'string',
                  'Value': 'string',
                  'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
              },
          ],
          onPremisesInstanceTagFilters=[
              {
                  'Key': 'string',
                  'Value': 'string',
                  'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
              },
          ],
          autoScalingGroups=[
              'string',
          ],
          serviceRoleArn='string',
          triggerConfigurations=[
              {
                  'triggerName': 'string',
                  'triggerTargetArn': 'string',
                  'triggerEvents': [
                      'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                  ]
              },
          ],
          alarmConfiguration={
              'enabled': True|False,
              'ignorePollAlarmFailure': True|False,
              'alarms': [
                  {
                      'name': 'string'
                  },
              ]
          },
          autoRollbackConfiguration={
              'enabled': True|False,
              'events': [
                  'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
              ]
          },
          deploymentStyle={
              'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
              'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
          },
          blueGreenDeploymentConfiguration={
              'terminateBlueInstancesOnDeploymentSuccess': {
                  'action': 'TERMINATE'|'KEEP_ALIVE',
                  'terminationWaitTimeInMinutes': 123
              },
              'deploymentReadyOption': {
                  'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                  'waitTimeInMinutes': 123
              },
              'greenFleetProvisioningOption': {
                  'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
              }
          },
          loadBalancerInfo={
              'elbInfoList': [
                  {
                      'name': 'string'
                  },
              ],
              'targetGroupInfoList': [
                  {
                      'name': 'string'
                  },
              ]
          },
          ec2TagSet={
              'ec2TagSetList': [
                  [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                      },
                  ],
              ]
          },
          onPremisesTagSet={
              'onPremisesTagSetList': [
                  [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                      },
                  ],
              ]
          }
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The application name corresponding to the deployment group to update.

      

    
    :type currentDeploymentGroupName: string
    :param currentDeploymentGroupName: **[REQUIRED]** 

      The current name of the deployment group.

      

    
    :type newDeploymentGroupName: string
    :param newDeploymentGroupName: 

      The new name of the deployment group, if you want to change it.

      

    
    :type deploymentConfigName: string
    :param deploymentConfigName: 

      The replacement deployment configuration name to use, if you want to change it.

      

    
    :type ec2TagFilters: list
    :param ec2TagFilters: 

      The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.

      

    
      - *(dict) --* 

        Information about an EC2 tag filter.

        

      
        - **Key** *(string) --* 

          The tag filter key.

          

        
        - **Value** *(string) --* 

          The tag filter value.

          

        
        - **Type** *(string) --* 

          The tag filter type:

           

           
          * KEY_ONLY: Key only. 
           
          * VALUE_ONLY: Value only. 
           
          * KEY_AND_VALUE: Key and value. 
           

          

        
      
  
    :type onPremisesInstanceTagFilters: list
    :param onPremisesInstanceTagFilters: 

      The replacement set of on-premises instance tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.

      

    
      - *(dict) --* 

        Information about an on-premises instance tag filter.

        

      
        - **Key** *(string) --* 

          The on-premises instance tag filter key.

          

        
        - **Value** *(string) --* 

          The on-premises instance tag filter value.

          

        
        - **Type** *(string) --* 

          The on-premises instance tag filter type:

           

           
          * KEY_ONLY: Key only. 
           
          * VALUE_ONLY: Value only. 
           
          * KEY_AND_VALUE: Key and value. 
           

          

        
      
  
    :type autoScalingGroups: list
    :param autoScalingGroups: 

      The replacement list of Auto Scaling groups to be included in the deployment group, if you want to change them. To keep the Auto Scaling groups, enter their names. To remove Auto Scaling groups, do not enter any Auto Scaling group names.

      

    
      - *(string) --* 

      
  
    :type serviceRoleArn: string
    :param serviceRoleArn: 

      A replacement ARN for the service role, if you want to change it.

      

    
    :type triggerConfigurations: list
    :param triggerConfigurations: 

      Information about triggers to change when the deployment group is updated. For examples, see `Modify Triggers in an AWS CodeDeploy Deployment Group <http://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-edit.html>`__ in the AWS CodeDeploy User Guide.

      

    
      - *(dict) --* 

        Information about notification triggers for the deployment group.

        

      
        - **triggerName** *(string) --* 

          The name of the notification trigger.

          

        
        - **triggerTargetArn** *(string) --* 

          The ARN of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

          

        
        - **triggerEvents** *(list) --* 

          The event type or types for which notifications are triggered.

          

        
          - *(string) --* 

          
      
      
  
    :type alarmConfiguration: dict
    :param alarmConfiguration: 

      Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.

      

    
      - **enabled** *(boolean) --* 

        Indicates whether the alarm configuration is enabled.

        

      
      - **ignorePollAlarmFailure** *(boolean) --* 

        Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

         

         
        * true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch. 
         
        * false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch. 
         

        

      
      - **alarms** *(list) --* 

        A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.

        

      
        - *(dict) --* 

          Information about an alarm.

          

        
          - **name** *(string) --* 

            The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.

            

          
        
    
    
    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: 

      Information for an automatic rollback configuration that is added or changed when a deployment group is updated.

      

    
      - **enabled** *(boolean) --* 

        Indicates whether a defined automatic rollback configuration is currently enabled.

        

      
      - **events** *(list) --* 

        The event type or types that trigger a rollback.

        

      
        - *(string) --* 

        
    
    
    :type deploymentStyle: dict
    :param deploymentStyle: 

      Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

      

    
      - **deploymentType** *(string) --* 

        Indicates whether to run an in-place deployment or a blue/green deployment.

        

      
      - **deploymentOption** *(string) --* 

        Indicates whether to route deployment traffic behind a load balancer.

        

      
    
    :type blueGreenDeploymentConfiguration: dict
    :param blueGreenDeploymentConfiguration: 

      Information about blue/green deployment options for a deployment group.

      

    
      - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --* 

        Information about whether to terminate instances in the original fleet during a blue/green deployment.

        

      
        - **action** *(string) --* 

          The action to take on instances in the original environment after a successful blue/green deployment.

           

           
          * TERMINATE: Instances are terminated after a specified wait time. 
           
          * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group. 
           

          

        
        - **terminationWaitTimeInMinutes** *(integer) --* 

          The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.

          

        
      
      - **deploymentReadyOption** *(dict) --* 

        Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

        

      
        - **actionOnTimeout** *(string) --* 

          Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

           

           
          * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment. 
           
          * STOP_DEPLOYMENT: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped. 
           

          

        
        - **waitTimeInMinutes** *(integer) --* 

          The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout

          

        
      
      - **greenFleetProvisioningOption** *(dict) --* 

        Information about how instances are provisioned for a replacement environment in a blue/green deployment.

        

      
        - **action** *(string) --* 

          The method used to add instances to a replacement environment.

           

           
          * DISCOVER_EXISTING: Use instances that already exist or will be created manually. 
           
          * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group. 
           

          

        
      
    
    :type loadBalancerInfo: dict
    :param loadBalancerInfo: 

      Information about the load balancer used in a deployment.

      

    
      - **elbInfoList** *(list) --* 

        An array containing information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

        

      
        - *(dict) --* 

          Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

          

        
          - **name** *(string) --* 

            For blue/green deployments, the name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.

            

          
        
    
      - **targetGroupInfoList** *(list) --* 

        An array containing information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

        

      
        - *(dict) --* 

          Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

          

        
          - **name** *(string) --* 

            For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes. 

            

          
        
    
    
    :type ec2TagSet: dict
    :param ec2TagSet: 

      Information about groups of tags applied to on-premises instances. The deployment group will include only EC2 instances identified by all the tag groups.

      

    
      - **ec2TagSetList** *(list) --* 

        A list containing other lists of EC2 instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

        

      
        - *(list) --* 

        
          - *(dict) --* 

            Information about an EC2 tag filter.

            

          
            - **Key** *(string) --* 

              The tag filter key.

              

            
            - **Value** *(string) --* 

              The tag filter value.

              

            
            - **Type** *(string) --* 

              The tag filter type:

               

               
              * KEY_ONLY: Key only. 
               
              * VALUE_ONLY: Value only. 
               
              * KEY_AND_VALUE: Key and value. 
               

              

            
          
      
    
    
    :type onPremisesTagSet: dict
    :param onPremisesTagSet: 

      Information about an on-premises instance tag set. The deployment group will include only on-premises instances identified by all the tag groups.

      

    
      - **onPremisesTagSetList** *(list) --* 

        A list containing other lists of on-premises instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

        

      
        - *(list) --* 

        
          - *(dict) --* 

            Information about an on-premises instance tag filter.

            

          
            - **Key** *(string) --* 

              The on-premises instance tag filter key.

              

            
            - **Value** *(string) --* 

              The on-premises instance tag filter value.

              

            
            - **Type** *(string) --* 

              The on-premises instance tag filter type:

               

               
              * KEY_ONLY: Key only. 
               
              * VALUE_ONLY: Value only. 
               
              * KEY_AND_VALUE: Key and value. 
               

              

            
          
      
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'hooksNotCleanedUp': [
                {
                    'name': 'string',
                    'hook': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of an UpdateDeploymentGroup operation.

        
        

        - **hooksNotCleanedUp** *(list) --* 

          If the output contains no data, and the corresponding deployment group contained at least one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling lifecycle event hooks from the AWS account. If the output contains data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the AWS account.

          
          

          - *(dict) --* 

            Information about an Auto Scaling group.

            
            

            - **name** *(string) --* 

              The Auto Scaling group name.

              
            

            - **hook** *(string) --* 

              An Auto Scaling lifecycle event hook name.

              
        
      
    

==========
Paginators
==========


The available paginators are:

* :py:class:`CodeDeploy.Paginator.ListApplicationRevisions`


* :py:class:`CodeDeploy.Paginator.ListApplications`


* :py:class:`CodeDeploy.Paginator.ListDeploymentConfigs`


* :py:class:`CodeDeploy.Paginator.ListDeploymentGroups`


* :py:class:`CodeDeploy.Paginator.ListDeploymentInstances`


* :py:class:`CodeDeploy.Paginator.ListDeployments`



.. py:class:: CodeDeploy.Paginator.ListApplicationRevisions

  ::

    
    paginator = client.get_paginator('list_application_revisions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeDeploy.Client.list_application_revisions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplicationRevisions>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          applicationName='string',
          sortBy='registerTime'|'firstUsedTime'|'lastUsedTime',
          sortOrder='ascending'|'descending',
          s3Bucket='string',
          s3KeyPrefix='string',
          deployed='include'|'exclude'|'ignore',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type sortBy: string
    :param sortBy: 

      The column name to use to sort the list results:

       

       
      * registerTime: Sort by the time the revisions were registered with AWS CodeDeploy. 
       
      * firstUsedTime: Sort by the time the revisions were first used in a deployment. 
       
      * lastUsedTime: Sort by the time the revisions were last used in a deployment. 
       

       

      If not specified or set to null, the results will be returned in an arbitrary order.

      

    
    :type sortOrder: string
    :param sortOrder: 

      The order in which to sort the list results:

       

       
      * ascending: ascending order. 
       
      * descending: descending order. 
       

       

      If not specified, the results will be sorted in ascending order.

       

      If set to null, the results will be sorted in an arbitrary order.

      

    
    :type s3Bucket: string
    :param s3Bucket: 

      An Amazon S3 bucket name to limit the search for revisions.

       

      If set to null, all of the user's buckets will be searched.

      

    
    :type s3KeyPrefix: string
    :param s3KeyPrefix: 

      A key prefix for the set of Amazon S3 objects to limit the search for revisions.

      

    
    :type deployed: string
    :param deployed: 

      Whether to list revisions based on whether the revision is the target revision of an deployment group:

       

       
      * include: List revisions that are target revisions of a deployment group. 
       
      * exclude: Do not list revisions that are target revisions of a deployment group. 
       
      * ignore: List all revisions. 
       

      

    
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
            'revisions': [
                {
                    'revisionType': 'S3'|'GitHub'|'String',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListApplicationRevisions operation.

        
        

        - **revisions** *(list) --* 

          A list of locations that contain the matching revisions.

          
          

          - *(dict) --* 

            Information about the location of an application revision.

            
            

            - **revisionType** *(string) --* 

              The type of application revision:

               

               
              * S3: An application revision stored in Amazon S3. 
               
              * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
               
              * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
               

              
            

            - **s3Location** *(dict) --* 

              Information about the location of a revision stored in Amazon S3. 

              
              

              - **bucket** *(string) --* 

                The name of the Amazon S3 bucket where the application revision is stored.

                
              

              - **key** *(string) --* 

                The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

                
              

              - **bundleType** *(string) --* 

                The file type of the application revision. Must be one of the following:

                 

                 
                * tar: A tar archive file. 
                 
                * tgz: A compressed tar archive file. 
                 
                * zip: A zip archive file. 
                 

                
              

              - **version** *(string) --* 

                A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the version is not specified, the system will use the most recent version by default.

                
              

              - **eTag** *(string) --* 

                The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

                 

                If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.

                
          
            

            - **gitHubLocation** *(dict) --* 

              Information about the location of application artifacts stored in GitHub.

              
              

              - **repository** *(string) --* 

                The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 

                 

                Specified as account/repository.

                
              

              - **commitId** *(string) --* 

                The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

                
          
            

            - **string** *(dict) --* 

              Information about the location of an AWS Lambda deployment revision stored as a RawString.

              
              

              - **content** *(string) --* 

                The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

                
              

              - **sha256** *(string) --* 

                The SHA256 hash value of the revision that is specified as a RawString.

                
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CodeDeploy.Paginator.ListApplications

  ::

    
    paginator = client.get_paginator('list_applications')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeDeploy.Client.list_applications`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplications>`_    


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
            'applications': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListApplications operation.

        
        

        - **applications** *(list) --* 

          A list of application names.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CodeDeploy.Paginator.ListDeploymentConfigs

  ::

    
    paginator = client.get_paginator('list_deployment_configs')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeDeploy.Client.list_deployment_configs`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentConfigs>`_    


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
            'deploymentConfigsList': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListDeploymentConfigs operation.

        
        

        - **deploymentConfigsList** *(list) --* 

          A list of deployment configurations, including built-in configurations such as CodeDeployDefault.OneAtATime.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CodeDeploy.Paginator.ListDeploymentGroups

  ::

    
    paginator = client.get_paginator('list_deployment_groups')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeDeploy.Client.list_deployment_groups`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentGroups>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          applicationName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type applicationName: string
    :param applicationName: **[REQUIRED]** 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
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
            'applicationName': 'string',
            'deploymentGroups': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListDeploymentGroups operation.

        
        

        - **applicationName** *(string) --* 

          The application name.

          
        

        - **deploymentGroups** *(list) --* 

          A list of corresponding deployment group names.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CodeDeploy.Paginator.ListDeploymentInstances

  ::

    
    paginator = client.get_paginator('list_deployment_instances')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeDeploy.Client.list_deployment_instances`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentInstances>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          deploymentId='string',
          instanceStatusFilter=[
              'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
          ],
          instanceTypeFilter=[
              'Blue'|'Green',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      The unique ID of a deployment.

      

    
    :type instanceStatusFilter: list
    :param instanceStatusFilter: 

      A subset of instances to list by status:

       

       
      * Pending: Include those instance with pending deployments. 
       
      * InProgress: Include those instance where deployments are still in progress. 
       
      * Succeeded: Include those instances with successful deployments. 
       
      * Failed: Include those instance with failed deployments. 
       
      * Skipped: Include those instance with skipped deployments. 
       
      * Unknown: Include those instance with deployments in an unknown state. 
       

      

    
      - *(string) --* 

      
  
    :type instanceTypeFilter: list
    :param instanceTypeFilter: 

      The set of instances in a blue/green deployment, either those in the original environment ("BLUE") or those in the replacement environment ("GREEN"), for which you want to view instance information.

      

    
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
            'instancesList': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListDeploymentInstances operation.

        
        

        - **instancesList** *(list) --* 

          A list of instance IDs.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CodeDeploy.Paginator.ListDeployments

  ::

    
    paginator = client.get_paginator('list_deployments')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeDeploy.Client.list_deployments`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeployments>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          applicationName='string',
          deploymentGroupName='string',
          includeOnlyStatuses=[
              'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
          ],
          createTimeRange={
              'start': datetime(2015, 1, 1),
              'end': datetime(2015, 1, 1)
          },
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type applicationName: string
    :param applicationName: 

      The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

      

    
    :type deploymentGroupName: string
    :param deploymentGroupName: 

      The name of an existing deployment group for the specified application.

      

    
    :type includeOnlyStatuses: list
    :param includeOnlyStatuses: 

      A subset of deployments to list by status:

       

       
      * Created: Include created deployments in the resulting list. 
       
      * Queued: Include queued deployments in the resulting list. 
       
      * In Progress: Include in-progress deployments in the resulting list. 
       
      * Succeeded: Include successful deployments in the resulting list. 
       
      * Failed: Include failed deployments in the resulting list. 
       
      * Stopped: Include stopped deployments in the resulting list. 
       

      

    
      - *(string) --* 

      
  
    :type createTimeRange: dict
    :param createTimeRange: 

      A time range (start and end) for returning a subset of the list of deployments.

      

    
      - **start** *(datetime) --* 

        The start time of the time range.

         

        .. note::

           

          Specify null to leave the start time open-ended.

           

        

      
      - **end** *(datetime) --* 

        The end time of the time range.

         

        .. note::

           

          Specify null to leave the end time open-ended.

           

        

      
    
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
            'deployments': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ListDeployments operation.

        
        

        - **deployments** *(list) --* 

          A list of deployment IDs.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

=======
Waiters
=======


The available waiters are:

* :py:class:`CodeDeploy.Waiter.DeploymentSuccessful`



.. py:class:: CodeDeploy.Waiter.DeploymentSuccessful

  ::

    
    waiter = client.get_waiter('deployment_successful')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`CodeDeploy.Client.get_deployment` every 15 seconds until a successful state is reached. An error is returned after 120 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeployment>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          deploymentId='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      A deployment ID associated with the applicable IAM user or AWS account.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 120

        

      
    
    
    :returns: None