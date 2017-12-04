

*********
CodeBuild
*********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CodeBuild.Client

  A low-level client representing AWS CodeBuild::

    
    import boto3
    
    client = boto3.client('codebuild')

  
  These are the available methods:
  
  *   :py:meth:`~CodeBuild.Client.batch_delete_builds`

  
  *   :py:meth:`~CodeBuild.Client.batch_get_builds`

  
  *   :py:meth:`~CodeBuild.Client.batch_get_projects`

  
  *   :py:meth:`~CodeBuild.Client.can_paginate`

  
  *   :py:meth:`~CodeBuild.Client.create_project`

  
  *   :py:meth:`~CodeBuild.Client.create_webhook`

  
  *   :py:meth:`~CodeBuild.Client.delete_project`

  
  *   :py:meth:`~CodeBuild.Client.delete_webhook`

  
  *   :py:meth:`~CodeBuild.Client.generate_presigned_url`

  
  *   :py:meth:`~CodeBuild.Client.get_paginator`

  
  *   :py:meth:`~CodeBuild.Client.get_waiter`

  
  *   :py:meth:`~CodeBuild.Client.invalidate_project_cache`

  
  *   :py:meth:`~CodeBuild.Client.list_builds`

  
  *   :py:meth:`~CodeBuild.Client.list_builds_for_project`

  
  *   :py:meth:`~CodeBuild.Client.list_curated_environment_images`

  
  *   :py:meth:`~CodeBuild.Client.list_projects`

  
  *   :py:meth:`~CodeBuild.Client.start_build`

  
  *   :py:meth:`~CodeBuild.Client.stop_build`

  
  *   :py:meth:`~CodeBuild.Client.update_project`

  

  .. py:method:: batch_delete_builds(**kwargs)

    

    Deletes one or more builds.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchDeleteBuilds>`_    


    **Request Syntax** 
    ::

      response = client.batch_delete_builds(
          ids=[
              'string',
          ]
      )
    :type ids: list
    :param ids: **[REQUIRED]** 

      The IDs of the builds to delete.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'buildsDeleted': [
                'string',
            ],
            'buildsNotDeleted': [
                {
                    'id': 'string',
                    'statusCode': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **buildsDeleted** *(list) --* 

          The IDs of the builds that were successfully deleted.

          
          

          - *(string) --* 
      
        

        - **buildsNotDeleted** *(list) --* 

          Information about any builds that could not be successfully deleted.

          
          

          - *(dict) --* 

            Information about a build that could not be successfully deleted.

            
            

            - **id** *(string) --* 

              The ID of the build that could not be successfully deleted.

              
            

            - **statusCode** *(string) --* 

              Additional information about the build that could not be successfully deleted.

              
        
      
    

  .. py:method:: batch_get_builds(**kwargs)

    

    Gets information about builds.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetBuilds>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_builds(
          ids=[
              'string',
          ]
      )
    :type ids: list
    :param ids: **[REQUIRED]** 

      The IDs of the builds.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'builds': [
                {
                    'id': 'string',
                    'arn': 'string',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'currentPhase': 'string',
                    'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                    'sourceVersion': 'string',
                    'projectName': 'string',
                    'phases': [
                        {
                            'phaseType': 'SUBMITTED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                            'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'durationInSeconds': 123,
                            'contexts': [
                                {
                                    'statusCode': 'string',
                                    'message': 'string'
                                },
                            ]
                        },
                    ],
                    'source': {
                        'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET',
                        'location': 'string',
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        }
                    },
                    'artifacts': {
                        'location': 'string',
                        'sha256sum': 'string',
                        'md5sum': 'string'
                    },
                    'cache': {
                        'type': 'NO_CACHE'|'S3',
                        'location': 'string'
                    },
                    'environment': {
                        'type': 'LINUX_CONTAINER',
                        'image': 'string',
                        'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                        'environmentVariables': [
                            {
                                'name': 'string',
                                'value': 'string',
                                'type': 'PLAINTEXT'|'PARAMETER_STORE'
                            },
                        ],
                        'privilegedMode': True|False
                    },
                    'logs': {
                        'groupName': 'string',
                        'streamName': 'string',
                        'deepLink': 'string'
                    },
                    'timeoutInMinutes': 123,
                    'buildComplete': True|False,
                    'initiator': 'string',
                    'vpcConfig': {
                        'vpcId': 'string',
                        'subnets': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ]
                    },
                    'networkInterface': {
                        'subnetId': 'string',
                        'networkInterfaceId': 'string'
                    }
                },
            ],
            'buildsNotFound': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **builds** *(list) --* 

          Information about the requested builds.

          
          

          - *(dict) --* 

            Information about a build.

            
            

            - **id** *(string) --* 

              The unique ID for the build.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the build.

              
            

            - **startTime** *(datetime) --* 

              When the build process started, expressed in Unix time format.

              
            

            - **endTime** *(datetime) --* 

              When the build process ended, expressed in Unix time format.

              
            

            - **currentPhase** *(string) --* 

              The current build phase.

              
            

            - **buildStatus** *(string) --* 

              The current status of the build. Valid values include:

               

               
              * ``FAILED`` : The build failed. 
               
              * ``FAULT`` : The build faulted. 
               
              * ``IN_PROGRESS`` : The build is still in progress. 
               
              * ``STOPPED`` : The build stopped. 
               
              * ``SUCCEEDED`` : The build succeeded. 
               
              * ``TIMED_OUT`` : The build timed out. 
               

              
            

            - **sourceVersion** *(string) --* 

              Any version identifier for the version of the source code to be built.

              
            

            - **projectName** *(string) --* 

              The name of the build project.

              
            

            - **phases** *(list) --* 

              Information about all previous build phases that are completed and information about any current build phase that is not yet complete.

              
              

              - *(dict) --* 

                Information about a stage for a build.

                
                

                - **phaseType** *(string) --* 

                  The name of the build phase. Valid values include:

                   

                   
                  * ``BUILD`` : Core build activities typically occur in this build phase. 
                   
                  * ``COMPLETED`` : The build has been completed. 
                   
                  * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase. 
                   
                  * ``FINALIZING`` : The build process is completing in this build phase. 
                   
                  * ``INSTALL`` : Installation activities typically occur in this build phase. 
                   
                  * ``POST_BUILD`` : Post-build activities typically occur in this build phase. 
                   
                  * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase. 
                   
                  * ``PROVISIONING`` : The build environment is being set up. 
                   
                  * ``SUBMITTED`` : The build has been submitted. 
                   
                  * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output location. 
                   

                  
                

                - **phaseStatus** *(string) --* 

                  The current status of the build phase. Valid values include:

                   

                   
                  * ``FAILED`` : The build phase failed. 
                   
                  * ``FAULT`` : The build phase faulted. 
                   
                  * ``IN_PROGRESS`` : The build phase is still in progress. 
                   
                  * ``STOPPED`` : The build phase stopped. 
                   
                  * ``SUCCEEDED`` : The build phase succeeded. 
                   
                  * ``TIMED_OUT`` : The build phase timed out. 
                   

                  
                

                - **startTime** *(datetime) --* 

                  When the build phase started, expressed in Unix time format.

                  
                

                - **endTime** *(datetime) --* 

                  When the build phase ended, expressed in Unix time format.

                  
                

                - **durationInSeconds** *(integer) --* 

                  How long, in seconds, between the starting and ending times of the build's phase.

                  
                

                - **contexts** *(list) --* 

                  Additional information about a build phase, especially to help troubleshoot a failed build.

                  
                  

                  - *(dict) --* 

                    Additional information about a build phase that has an error. You can use this information to help troubleshoot a failed build.

                    
                    

                    - **statusCode** *(string) --* 

                      The status code for the context of the build phase.

                      
                    

                    - **message** *(string) --* 

                      An explanation of the build phase's context. This explanation might include a command ID and an exit code.

                      
                
              
            
          
            

            - **source** *(dict) --* 

              Information about the source code to be built.

              
              

              - **type** *(string) --* 

                The type of repository that contains the source code to be built. Valid values include:

                 

                 
                * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                 
                * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                 
                * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                 
                * ``GITHUB`` : The source code is in a GitHub repository. 
                 
                * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                 

                
              

              - **location** *(string) --* 

                Information about the location of the source code to be built. Valid values include:

                 

                 
                * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value. 
                 
                * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                 
                * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ) 
                 
                * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
                 
                * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
                 

                
              

              - **buildspec** *(string) --* 

                The build spec declaration to use for the builds in this build project.

                 

                If this value is not specified, a build spec must be included along with the source code to be built.

                
              

              - **auth** *(dict) --* 

                Information about the authorization settings for AWS CodeBuild to access the source code to be built.

                 

                This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly (unless the build project's source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).

                
                

                - **type** *(string) --* 

                  The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.

                  
                

                - **resource** *(string) --* 

                  The resource value that applies to the specified authorization type.

                  
            
          
            

            - **artifacts** *(dict) --* 

              Information about the output artifacts for the build.

              
              

              - **location** *(string) --* 

                Information about the location of the build artifacts.

                
              

              - **sha256sum** *(string) --* 

                The SHA-256 hash of the build artifact.

                 

                You can use this hash along with a checksum tool to confirm both file integrity and authenticity.

                 

                .. note::

                   

                  This value is available only if the build project's ``packaging`` value is set to ``ZIP`` .

                   

                
              

              - **md5sum** *(string) --* 

                The MD5 hash of the build artifact.

                 

                You can use this hash along with a checksum tool to confirm both file integrity and authenticity.

                 

                .. note::

                   

                  This value is available only if the build project's ``packaging`` value is set to ``ZIP`` .

                   

                
          
            

            - **cache** *(dict) --* 

              Information about the cache for the build.

              
              

              - **type** *(string) --* 

                The type of cache used by the build project. Valid values include:

                 

                 
                * ``NO_CACHE`` : The build project will not use any cache. 
                 
                * ``S3`` : The build project will read and write from/to S3. 
                 

                
              

              - **location** *(string) --* 

                Information about the cache location, as follows: 

                 

                 
                * ``NO_CACHE`` : This value will be ignored. 
                 
                * ``S3`` : This is the S3 bucket name/prefix. 
                 

                
          
            

            - **environment** *(dict) --* 

              Information about the build environment for this build.

              
              

              - **type** *(string) --* 

                The type of build environment to use for related builds.

                
              

              - **image** *(string) --* 

                The ID of the Docker image to use for this build project.

                
              

              - **computeType** *(string) --* 

                Information about the compute resources the build project will use. Available values include:

                 

                 
                * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
                 
                * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
                 
                * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
                 

                
              

              - **environmentVariables** *(list) --* 

                A set of environment variables to make available to builds for this build project.

                
                

                - *(dict) --* 

                  Information about an environment variable for a build project or a build.

                  
                  

                  - **name** *(string) --* 

                    The name or key of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the environment variable.

                     

                    .. warning::

                       

                      We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

                       

                    
                  

                  - **type** *(string) --* 

                    The type of environment variable. Valid values include:

                     

                     
                    * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                     
                    * ``PLAINTEXT`` : An environment variable in plaintext format. 
                     

                    
              
            
              

              - **privilegedMode** *(boolean) --* 

                If set to true, enables running the Docker daemon inside a Docker container; otherwise, false or not specified (the default). This value must be set to true only if this build project will be used to build Docker images, and the specified build environment image is not one provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that your builds can interact with it as needed. One way to do this is to initialize the Docker daemon in the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)

                 

                 ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``  

                
          
            

            - **logs** *(dict) --* 

              Information about the build's logs in Amazon CloudWatch Logs.

              
              

              - **groupName** *(string) --* 

                The name of the Amazon CloudWatch Logs group for the build logs.

                
              

              - **streamName** *(string) --* 

                The name of the Amazon CloudWatch Logs stream for the build logs.

                
              

              - **deepLink** *(string) --* 

                The URL to an individual build log in Amazon CloudWatch Logs.

                
          
            

            - **timeoutInMinutes** *(integer) --* 

              How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.

              
            

            - **buildComplete** *(boolean) --* 

              Whether the build has finished. True if completed; otherwise, false.

              
            

            - **initiator** *(string) --* 

              The entity that started the build. Valid values include:

               

               
              * If AWS CodePipeline started the build, the pipeline's name (for example, ``codepipeline/my-demo-pipeline`` ). 
               
              * If an AWS Identity and Access Management (IAM) user started the build, the user's name (for example ``MyUserName`` ). 
               
              * If the Jenkins plugin for AWS CodeBuild started the build, the string ``CodeBuild-Jenkins-Plugin`` . 
               

              
            

            - **vpcConfig** *(dict) --* 

              If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

              
              

              - **vpcId** *(string) --* 

                The ID of the Amazon VPC.

                
              

              - **subnets** *(list) --* 

                A list of one or more subnet IDs in your Amazon VPC.

                
                

                - *(string) --* 
            
              

              - **securityGroupIds** *(list) --* 

                A list of one or more security groups IDs in your Amazon VPC.

                
                

                - *(string) --* 
            
          
            

            - **networkInterface** *(dict) --* 

              Describes a network interface.

              
              

              - **subnetId** *(string) --* 

                The ID of the subnet.

                
              

              - **networkInterfaceId** *(string) --* 

                The ID of the network interface.

                
          
        
      
        

        - **buildsNotFound** *(list) --* 

          The IDs of builds for which information could not be found.

          
          

          - *(string) --* 
      
    

  .. py:method:: batch_get_projects(**kwargs)

    

    Gets information about build projects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetProjects>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_projects(
          names=[
              'string',
          ]
      )
    :type names: list
    :param names: **[REQUIRED]** 

      The names of the build projects.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'projects': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'description': 'string',
                    'source': {
                        'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET',
                        'location': 'string',
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        }
                    },
                    'artifacts': {
                        'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                        'location': 'string',
                        'path': 'string',
                        'namespaceType': 'NONE'|'BUILD_ID',
                        'name': 'string',
                        'packaging': 'NONE'|'ZIP'
                    },
                    'cache': {
                        'type': 'NO_CACHE'|'S3',
                        'location': 'string'
                    },
                    'environment': {
                        'type': 'LINUX_CONTAINER',
                        'image': 'string',
                        'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                        'environmentVariables': [
                            {
                                'name': 'string',
                                'value': 'string',
                                'type': 'PLAINTEXT'|'PARAMETER_STORE'
                            },
                        ],
                        'privilegedMode': True|False
                    },
                    'serviceRole': 'string',
                    'timeoutInMinutes': 123,
                    'encryptionKey': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'created': datetime(2015, 1, 1),
                    'lastModified': datetime(2015, 1, 1),
                    'webhook': {
                        'url': 'string'
                    },
                    'vpcConfig': {
                        'vpcId': 'string',
                        'subnets': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ]
                    },
                    'badge': {
                        'badgeEnabled': True|False,
                        'badgeRequestUrl': 'string'
                    }
                },
            ],
            'projectsNotFound': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **projects** *(list) --* 

          Information about the requested build projects.

          
          

          - *(dict) --* 

            Information about a build project.

            
            

            - **name** *(string) --* 

              The name of the build project.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the build project.

              
            

            - **description** *(string) --* 

              A description that makes the build project easy to identify.

              
            

            - **source** *(dict) --* 

              Information about the build input source code for this build project.

              
              

              - **type** *(string) --* 

                The type of repository that contains the source code to be built. Valid values include:

                 

                 
                * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                 
                * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                 
                * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                 
                * ``GITHUB`` : The source code is in a GitHub repository. 
                 
                * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                 

                
              

              - **location** *(string) --* 

                Information about the location of the source code to be built. Valid values include:

                 

                 
                * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value. 
                 
                * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                 
                * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ) 
                 
                * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
                 
                * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
                 

                
              

              - **buildspec** *(string) --* 

                The build spec declaration to use for the builds in this build project.

                 

                If this value is not specified, a build spec must be included along with the source code to be built.

                
              

              - **auth** *(dict) --* 

                Information about the authorization settings for AWS CodeBuild to access the source code to be built.

                 

                This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly (unless the build project's source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).

                
                

                - **type** *(string) --* 

                  The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.

                  
                

                - **resource** *(string) --* 

                  The resource value that applies to the specified authorization type.

                  
            
          
            

            - **artifacts** *(dict) --* 

              Information about the build output artifacts for the build project.

              
              

              - **type** *(string) --* 

                The type of build output artifact. Valid values include:

                 

                 
                * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
                 
                * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
                 
                * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
                 

                
              

              - **location** *(string) --* 

                Information about the build output artifact location, as follows:

                 

                 
                * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
                 
                * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                 
                * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
                 

                
              

              - **path** *(string) --* 

                Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

                 

                 
                * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                 
                * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                 
                * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
                 

                 

                For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

                
              

              - **namespaceType** *(string) --* 

                Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:

                 

                 
                * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                 
                * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                 
                * If ``type`` is set to ``S3`` , then valid values include: 

                   
                  * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                   
                  * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                   

                 
                 

                 

                For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                
              

              - **name** *(string) --* 

                Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

                 

                 
                * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                 
                * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                 
                * If ``type`` is set to ``S3`` , this is the name of the output artifact object. 
                 

                 

                For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                
              

              - **packaging** *(string) --* 

                The type of build output artifact to create, as follows:

                 

                 
                * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
                 
                * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                 
                * If ``type`` is set to ``S3`` , valid values include: 

                   
                  * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                   
                  * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                   

                 
                 

                
          
            

            - **cache** *(dict) --* 

              Information about the cache for the build project.

              
              

              - **type** *(string) --* 

                The type of cache used by the build project. Valid values include:

                 

                 
                * ``NO_CACHE`` : The build project will not use any cache. 
                 
                * ``S3`` : The build project will read and write from/to S3. 
                 

                
              

              - **location** *(string) --* 

                Information about the cache location, as follows: 

                 

                 
                * ``NO_CACHE`` : This value will be ignored. 
                 
                * ``S3`` : This is the S3 bucket name/prefix. 
                 

                
          
            

            - **environment** *(dict) --* 

              Information about the build environment for this build project.

              
              

              - **type** *(string) --* 

                The type of build environment to use for related builds.

                
              

              - **image** *(string) --* 

                The ID of the Docker image to use for this build project.

                
              

              - **computeType** *(string) --* 

                Information about the compute resources the build project will use. Available values include:

                 

                 
                * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
                 
                * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
                 
                * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
                 

                
              

              - **environmentVariables** *(list) --* 

                A set of environment variables to make available to builds for this build project.

                
                

                - *(dict) --* 

                  Information about an environment variable for a build project or a build.

                  
                  

                  - **name** *(string) --* 

                    The name or key of the environment variable.

                    
                  

                  - **value** *(string) --* 

                    The value of the environment variable.

                     

                    .. warning::

                       

                      We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

                       

                    
                  

                  - **type** *(string) --* 

                    The type of environment variable. Valid values include:

                     

                     
                    * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                     
                    * ``PLAINTEXT`` : An environment variable in plaintext format. 
                     

                    
              
            
              

              - **privilegedMode** *(boolean) --* 

                If set to true, enables running the Docker daemon inside a Docker container; otherwise, false or not specified (the default). This value must be set to true only if this build project will be used to build Docker images, and the specified build environment image is not one provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that your builds can interact with it as needed. One way to do this is to initialize the Docker daemon in the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)

                 

                 ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``  

                
          
            

            - **serviceRole** *(string) --* 

              The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

              
            

            - **timeoutInMinutes** *(integer) --* 

              How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.

              
            

            - **encryptionKey** *(string) --* 

              The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

               

              This is expressed either as the CMK's Amazon Resource Name (ARN) or, if specified, the CMK's alias (using the format ``alias/*alias-name* `` ).

              
            

            - **tags** *(list) --* 

              The tags for this build project.

               

              These tags are available for use by AWS services that support AWS CodeBuild build project tags.

              
              

              - *(dict) --* 

                A tag, consisting of a key and a value.

                 

                This tag is available for use by AWS services that support tags in AWS CodeBuild.

                
                

                - **key** *(string) --* 

                  The tag's key.

                  
                

                - **value** *(string) --* 

                  The tag's value.

                  
            
          
            

            - **created** *(datetime) --* 

              When the build project was created, expressed in Unix time format.

              
            

            - **lastModified** *(datetime) --* 

              When the build project's settings were last modified, expressed in Unix time format.

              
            

            - **webhook** *(dict) --* 

              Information about a webhook in GitHub that connects repository events to a build project in AWS CodeBuild.

              
              

              - **url** *(string) --* 

                The URL to the webhook.

                
          
            

            - **vpcConfig** *(dict) --* 

              If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

              
              

              - **vpcId** *(string) --* 

                The ID of the Amazon VPC.

                
              

              - **subnets** *(list) --* 

                A list of one or more subnet IDs in your Amazon VPC.

                
                

                - *(string) --* 
            
              

              - **securityGroupIds** *(list) --* 

                A list of one or more security groups IDs in your Amazon VPC.

                
                

                - *(string) --* 
            
          
            

            - **badge** *(dict) --* 

              Information about the build badge for the build project.

              
              

              - **badgeEnabled** *(boolean) --* 

                Set this to true to generate a publicly-accessible URL for your project's build badge.

                
              

              - **badgeRequestUrl** *(string) --* 

                The publicly-accessible URL through which you can access the build badge for your project. 

                
          
        
      
        

        - **projectsNotFound** *(list) --* 

          The names of build projects for which information could not be found.

          
          

          - *(string) --* 
      
    

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


  .. py:method:: create_project(**kwargs)

    

    Creates a build project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/CreateProject>`_    


    **Request Syntax** 
    ::

      response = client.create_project(
          name='string',
          description='string',
          source={
              'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET',
              'location': 'string',
              'buildspec': 'string',
              'auth': {
                  'type': 'OAUTH',
                  'resource': 'string'
              }
          },
          artifacts={
              'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
              'location': 'string',
              'path': 'string',
              'namespaceType': 'NONE'|'BUILD_ID',
              'name': 'string',
              'packaging': 'NONE'|'ZIP'
          },
          cache={
              'type': 'NO_CACHE'|'S3',
              'location': 'string'
          },
          environment={
              'type': 'LINUX_CONTAINER',
              'image': 'string',
              'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
              'environmentVariables': [
                  {
                      'name': 'string',
                      'value': 'string',
                      'type': 'PLAINTEXT'|'PARAMETER_STORE'
                  },
              ],
              'privilegedMode': True|False
          },
          serviceRole='string',
          timeoutInMinutes=123,
          encryptionKey='string',
          tags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ],
          vpcConfig={
              'vpcId': 'string',
              'subnets': [
                  'string',
              ],
              'securityGroupIds': [
                  'string',
              ]
          },
          badgeEnabled=True|False
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the build project.

      

    
    :type description: string
    :param description: 

      A description that makes the build project easy to identify.

      

    
    :type source: dict
    :param source: **[REQUIRED]** 

      Information about the build input source code for the build project.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of repository that contains the source code to be built. Valid values include:

         

         
        * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
         
        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
         
        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
         
        * ``GITHUB`` : The source code is in a GitHub repository. 
         
        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
         

        

      
      - **location** *(string) --* 

        Information about the location of the source code to be built. Valid values include:

         

         
        * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value. 
         
        * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
         
        * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ) 
         
        * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
         
        * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
         

        

      
      - **buildspec** *(string) --* 

        The build spec declaration to use for the builds in this build project.

         

        If this value is not specified, a build spec must be included along with the source code to be built.

        

      
      - **auth** *(dict) --* 

        Information about the authorization settings for AWS CodeBuild to access the source code to be built.

         

        This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly (unless the build project's source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).

        

      
        - **type** *(string) --* **[REQUIRED]** 

          The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.

          

        
        - **resource** *(string) --* 

          The resource value that applies to the specified authorization type.

          

        
      
    
    :type artifacts: dict
    :param artifacts: **[REQUIRED]** 

      Information about the build output artifacts for the build project.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of build output artifact. Valid values include:

         

         
        * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
         
        * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
         
        * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
         

        

      
      - **location** *(string) --* 

        Information about the build output artifact location, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
         

        

      
      - **path** *(string) --* 

        Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

        

      
      - **namespaceType** *(string) --* 

        Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , then valid values include: 

           
          * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
           
          * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
           

         
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        

      
      - **name** *(string) --* 

        Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the name of the output artifact object. 
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        

      
      - **packaging** *(string) --* 

        The type of build output artifact to create, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , valid values include: 

           
          * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
           
          * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
           

         
         

        

      
    
    :type cache: dict
    :param cache: 

      Stores recently used information so that it can be quickly accessed at a later time.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of cache used by the build project. Valid values include:

         

         
        * ``NO_CACHE`` : The build project will not use any cache. 
         
        * ``S3`` : The build project will read and write from/to S3. 
         

        

      
      - **location** *(string) --* 

        Information about the cache location, as follows: 

         

         
        * ``NO_CACHE`` : This value will be ignored. 
         
        * ``S3`` : This is the S3 bucket name/prefix. 
         

        

      
    
    :type environment: dict
    :param environment: **[REQUIRED]** 

      Information about the build environment for the build project.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of build environment to use for related builds.

        

      
      - **image** *(string) --* **[REQUIRED]** 

        The ID of the Docker image to use for this build project.

        

      
      - **computeType** *(string) --* **[REQUIRED]** 

        Information about the compute resources the build project will use. Available values include:

         

         
        * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
         
        * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
         
        * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
         

        

      
      - **environmentVariables** *(list) --* 

        A set of environment variables to make available to builds for this build project.

        

      
        - *(dict) --* 

          Information about an environment variable for a build project or a build.

          

        
          - **name** *(string) --* **[REQUIRED]** 

            The name or key of the environment variable.

            

          
          - **value** *(string) --* **[REQUIRED]** 

            The value of the environment variable.

             

            .. warning::

               

              We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

               

            

          
          - **type** *(string) --* 

            The type of environment variable. Valid values include:

             

             
            * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
             
            * ``PLAINTEXT`` : An environment variable in plaintext format. 
             

            

          
        
    
      - **privilegedMode** *(boolean) --* 

        If set to true, enables running the Docker daemon inside a Docker container; otherwise, false or not specified (the default). This value must be set to true only if this build project will be used to build Docker images, and the specified build environment image is not one provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that your builds can interact with it as needed. One way to do this is to initialize the Docker daemon in the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)

         

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``  

        

      
    
    :type serviceRole: string
    :param serviceRole: 

      The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

      

    
    :type timeoutInMinutes: integer
    :param timeoutInMinutes: 

      How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any build that has not been marked as completed. The default is 60 minutes.

      

    
    :type encryptionKey: string
    :param encryptionKey: 

      The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

       

      You can specify either the CMK's Amazon Resource Name (ARN) or, if available, the CMK's alias (using the format ``alias/*alias-name* `` ).

      

    
    :type tags: list
    :param tags: 

      A set of tags for this build project.

       

      These tags are available for use by AWS services that support AWS CodeBuild build project tags.

      

    
      - *(dict) --* 

        A tag, consisting of a key and a value.

         

        This tag is available for use by AWS services that support tags in AWS CodeBuild.

        

      
        - **key** *(string) --* 

          The tag's key.

          

        
        - **value** *(string) --* 

          The tag's value.

          

        
      
  
    :type vpcConfig: dict
    :param vpcConfig: 

      VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.

      

    
      - **vpcId** *(string) --* 

        The ID of the Amazon VPC.

        

      
      - **subnets** *(list) --* 

        A list of one or more subnet IDs in your Amazon VPC.

        

      
        - *(string) --* 

        
    
      - **securityGroupIds** *(list) --* 

        A list of one or more security groups IDs in your Amazon VPC.

        

      
        - *(string) --* 

        
    
    
    :type badgeEnabled: boolean
    :param badgeEnabled: 

      Set this to true to generate a publicly-accessible URL for your project's build badge.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'project': {
                'name': 'string',
                'arn': 'string',
                'description': 'string',
                'source': {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET',
                    'location': 'string',
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    }
                },
                'artifacts': {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP'
                },
                'cache': {
                    'type': 'NO_CACHE'|'S3',
                    'location': 'string'
                },
                'environment': {
                    'type': 'LINUX_CONTAINER',
                    'image': 'string',
                    'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                    'environmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'type': 'PLAINTEXT'|'PARAMETER_STORE'
                        },
                    ],
                    'privilegedMode': True|False
                },
                'serviceRole': 'string',
                'timeoutInMinutes': 123,
                'encryptionKey': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'created': datetime(2015, 1, 1),
                'lastModified': datetime(2015, 1, 1),
                'webhook': {
                    'url': 'string'
                },
                'vpcConfig': {
                    'vpcId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ]
                },
                'badge': {
                    'badgeEnabled': True|False,
                    'badgeRequestUrl': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **project** *(dict) --* 

          Information about the build project that was created.

          
          

          - **name** *(string) --* 

            The name of the build project.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the build project.

            
          

          - **description** *(string) --* 

            A description that makes the build project easy to identify.

            
          

          - **source** *(dict) --* 

            Information about the build input source code for this build project.

            
            

            - **type** *(string) --* 

              The type of repository that contains the source code to be built. Valid values include:

               

               
              * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
               
              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
               
              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
               
              * ``GITHUB`` : The source code is in a GitHub repository. 
               
              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
               

              
            

            - **location** *(string) --* 

              Information about the location of the source code to be built. Valid values include:

               

               
              * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value. 
               
              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
               
              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ) 
               
              * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
               
              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
               

              
            

            - **buildspec** *(string) --* 

              The build spec declaration to use for the builds in this build project.

               

              If this value is not specified, a build spec must be included along with the source code to be built.

              
            

            - **auth** *(dict) --* 

              Information about the authorization settings for AWS CodeBuild to access the source code to be built.

               

              This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly (unless the build project's source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).

              
              

              - **type** *(string) --* 

                The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.

                
              

              - **resource** *(string) --* 

                The resource value that applies to the specified authorization type.

                
          
        
          

          - **artifacts** *(dict) --* 

            Information about the build output artifacts for the build project.

            
            

            - **type** *(string) --* 

              The type of build output artifact. Valid values include:

               

               
              * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
               
              * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
               
              * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
               

              
            

            - **location** *(string) --* 

              Information about the build output artifact location, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
               

              
            

            - **path** *(string) --* 

              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
               

               

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

              
            

            - **namespaceType** *(string) --* 

              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , then valid values include: 

                 
                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                 
                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                 

               
               

               

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

              
            

            - **name** *(string) --* 

              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. 
               

               

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

              
            

            - **packaging** *(string) --* 

              The type of build output artifact to create, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , valid values include: 

                 
                * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                 
                * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                 

               
               

              
        
          

          - **cache** *(dict) --* 

            Information about the cache for the build project.

            
            

            - **type** *(string) --* 

              The type of cache used by the build project. Valid values include:

               

               
              * ``NO_CACHE`` : The build project will not use any cache. 
               
              * ``S3`` : The build project will read and write from/to S3. 
               

              
            

            - **location** *(string) --* 

              Information about the cache location, as follows: 

               

               
              * ``NO_CACHE`` : This value will be ignored. 
               
              * ``S3`` : This is the S3 bucket name/prefix. 
               

              
        
          

          - **environment** *(dict) --* 

            Information about the build environment for this build project.

            
            

            - **type** *(string) --* 

              The type of build environment to use for related builds.

              
            

            - **image** *(string) --* 

              The ID of the Docker image to use for this build project.

              
            

            - **computeType** *(string) --* 

              Information about the compute resources the build project will use. Available values include:

               

               
              * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
               
              * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
               
              * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
               

              
            

            - **environmentVariables** *(list) --* 

              A set of environment variables to make available to builds for this build project.

              
              

              - *(dict) --* 

                Information about an environment variable for a build project or a build.

                
                

                - **name** *(string) --* 

                  The name or key of the environment variable.

                  
                

                - **value** *(string) --* 

                  The value of the environment variable.

                   

                  .. warning::

                     

                    We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

                     

                  
                

                - **type** *(string) --* 

                  The type of environment variable. Valid values include:

                   

                   
                  * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                   
                  * ``PLAINTEXT`` : An environment variable in plaintext format. 
                   

                  
            
          
            

            - **privilegedMode** *(boolean) --* 

              If set to true, enables running the Docker daemon inside a Docker container; otherwise, false or not specified (the default). This value must be set to true only if this build project will be used to build Docker images, and the specified build environment image is not one provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that your builds can interact with it as needed. One way to do this is to initialize the Docker daemon in the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)

               

               ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``  

              
        
          

          - **serviceRole** *(string) --* 

            The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

            
          

          - **timeoutInMinutes** *(integer) --* 

            How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.

            
          

          - **encryptionKey** *(string) --* 

            The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

             

            This is expressed either as the CMK's Amazon Resource Name (ARN) or, if specified, the CMK's alias (using the format ``alias/*alias-name* `` ).

            
          

          - **tags** *(list) --* 

            The tags for this build project.

             

            These tags are available for use by AWS services that support AWS CodeBuild build project tags.

            
            

            - *(dict) --* 

              A tag, consisting of a key and a value.

               

              This tag is available for use by AWS services that support tags in AWS CodeBuild.

              
              

              - **key** *(string) --* 

                The tag's key.

                
              

              - **value** *(string) --* 

                The tag's value.

                
          
        
          

          - **created** *(datetime) --* 

            When the build project was created, expressed in Unix time format.

            
          

          - **lastModified** *(datetime) --* 

            When the build project's settings were last modified, expressed in Unix time format.

            
          

          - **webhook** *(dict) --* 

            Information about a webhook in GitHub that connects repository events to a build project in AWS CodeBuild.

            
            

            - **url** *(string) --* 

              The URL to the webhook.

              
        
          

          - **vpcConfig** *(dict) --* 

            If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

            
            

            - **vpcId** *(string) --* 

              The ID of the Amazon VPC.

              
            

            - **subnets** *(list) --* 

              A list of one or more subnet IDs in your Amazon VPC.

              
              

              - *(string) --* 
          
            

            - **securityGroupIds** *(list) --* 

              A list of one or more security groups IDs in your Amazon VPC.

              
              

              - *(string) --* 
          
        
          

          - **badge** *(dict) --* 

            Information about the build badge for the build project.

            
            

            - **badgeEnabled** *(boolean) --* 

              Set this to true to generate a publicly-accessible URL for your project's build badge.

              
            

            - **badgeRequestUrl** *(string) --* 

              The publicly-accessible URL through which you can access the build badge for your project. 

              
        
      
    

  .. py:method:: create_webhook(**kwargs)

    

    For an existing AWS CodeBuild build project that has its source code stored in a GitHub repository, enables AWS CodeBuild to begin automatically rebuilding the source code every time a code change is pushed to the repository.

     

    .. warning::

       

      If you enable webhooks for an AWS CodeBuild project, and the project is used as a build step in AWS CodePipeline, then two identical builds will be created for each commit. One build is triggered through webhooks, and one through AWS CodePipeline. Because billing is on a per-build basis, you will be billed for both builds. Therefore, if you are using AWS CodePipeline, we recommend that you disable webhooks in CodeBuild. In the AWS CodeBuild console, clear the Webhook box. For more information, see step 9 in `Change a Build Project’s Settings <http://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console>`__ .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/CreateWebhook>`_    


    **Request Syntax** 
    ::

      response = client.create_webhook(
          projectName='string'
      )
    :type projectName: string
    :param projectName: **[REQUIRED]** 

      The name of the build project.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'webhook': {
                'url': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **webhook** *(dict) --* 

          Information about a webhook in GitHub that connects repository events to a build project in AWS CodeBuild.

          
          

          - **url** *(string) --* 

            The URL to the webhook.

            
      
    

  .. py:method:: delete_project(**kwargs)

    

    Deletes a build project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteProject>`_    


    **Request Syntax** 
    ::

      response = client.delete_project(
          name='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the build project.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_webhook(**kwargs)

    

    For an existing AWS CodeBuild build project that has its source code stored in a GitHub repository, stops AWS CodeBuild from automatically rebuilding the source code every time a code change is pushed to the repository.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteWebhook>`_    


    **Request Syntax** 
    ::

      response = client.delete_webhook(
          projectName='string'
      )
    :type projectName: string
    :param projectName: **[REQUIRED]** 

      The name of the build project.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

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

        


  .. py:method:: invalidate_project_cache(**kwargs)

    

    Resets the cache for a project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/InvalidateProjectCache>`_    


    **Request Syntax** 
    ::

      response = client.invalidate_project_cache(
          projectName='string'
      )
    :type projectName: string
    :param projectName: **[REQUIRED]** 

      The name of the build project that the cache will be reset for.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: list_builds(**kwargs)

    

    Gets a list of build IDs, with each build ID representing a single build.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuilds>`_    


    **Request Syntax** 
    ::

      response = client.list_builds(
          sortOrder='ASCENDING'|'DESCENDING',
          nextToken='string'
      )
    :type sortOrder: string
    :param sortOrder: 

      The order to list build IDs. Valid values include:

       

       
      * ``ASCENDING`` : List the build IDs in ascending order by build ID. 
       
      * ``DESCENDING`` : List the build IDs in descending order by build ID. 
       

      

    
    :type nextToken: string
    :param nextToken: 

      During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ids': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ids** *(list) --* 

          A list of build IDs, with each build ID representing a single build.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call.

          
    

  .. py:method:: list_builds_for_project(**kwargs)

    

    Gets a list of build IDs for the specified build project, with each build ID representing a single build.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuildsForProject>`_    


    **Request Syntax** 
    ::

      response = client.list_builds_for_project(
          projectName='string',
          sortOrder='ASCENDING'|'DESCENDING',
          nextToken='string'
      )
    :type projectName: string
    :param projectName: **[REQUIRED]** 

      The name of the build project.

      

    
    :type sortOrder: string
    :param sortOrder: 

      The order to list build IDs. Valid values include:

       

       
      * ``ASCENDING`` : List the build IDs in ascending order by build ID. 
       
      * ``DESCENDING`` : List the build IDs in descending order by build ID. 
       

      

    
    :type nextToken: string
    :param nextToken: 

      During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ids': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ids** *(list) --* 

          A list of build IDs for the specified build project, with each build ID representing a single build.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call.

          
    

  .. py:method:: list_curated_environment_images()

    

    Gets information about Docker images that are managed by AWS CodeBuild.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListCuratedEnvironmentImages>`_    


    **Request Syntax** 
    ::

      response = client.list_curated_environment_images()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'platforms': [
                {
                    'platform': 'DEBIAN'|'AMAZON_LINUX'|'UBUNTU',
                    'languages': [
                        {
                            'language': 'JAVA'|'PYTHON'|'NODE_JS'|'RUBY'|'GOLANG'|'DOCKER'|'ANDROID'|'DOTNET'|'BASE',
                            'images': [
                                {
                                    'name': 'string',
                                    'description': 'string'
                                },
                            ]
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **platforms** *(list) --* 

          Information about supported platforms for Docker images that are managed by AWS CodeBuild.

          
          

          - *(dict) --* 

            A set of Docker images that are related by platform and are managed by AWS CodeBuild.

            
            

            - **platform** *(string) --* 

              The platform's name.

              
            

            - **languages** *(list) --* 

              The list of programming languages that are available for the specified platform.

              
              

              - *(dict) --* 

                A set of Docker images that are related by programming language and are managed by AWS CodeBuild.

                
                

                - **language** *(string) --* 

                  The programming language for the Docker images.

                  
                

                - **images** *(list) --* 

                  The list of Docker images that are related by the specified programming language.

                  
                  

                  - *(dict) --* 

                    Information about a Docker image that is managed by AWS CodeBuild.

                    
                    

                    - **name** *(string) --* 

                      The name of the Docker image.

                      
                    

                    - **description** *(string) --* 

                      The description of the Docker image.

                      
                
              
            
          
        
      
    

  .. py:method:: list_projects(**kwargs)

    

    Gets a list of build project names, with each build project name representing a single build project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListProjects>`_    


    **Request Syntax** 
    ::

      response = client.list_projects(
          sortBy='NAME'|'CREATED_TIME'|'LAST_MODIFIED_TIME',
          sortOrder='ASCENDING'|'DESCENDING',
          nextToken='string'
      )
    :type sortBy: string
    :param sortBy: 

      The criterion to be used to list build project names. Valid values include:

       

       
      * ``CREATED_TIME`` : List the build project names based on when each build project was created. 
       
      * ``LAST_MODIFIED_TIME`` : List the build project names based on when information about each build project was last changed. 
       
      * ``NAME`` : List the build project names based on each build project's name. 
       

       

      Use ``sortOrder`` to specify in what order to list the build project names based on the preceding criteria.

      

    
    :type sortOrder: string
    :param sortOrder: 

      The order in which to list build projects. Valid values include:

       

       
      * ``ASCENDING`` : List the build project names in ascending order. 
       
      * ``DESCENDING`` : List the build project names in descending order. 
       

       

      Use ``sortBy`` to specify the criterion to be used to list build project names.

      

    
    :type nextToken: string
    :param nextToken: 

      During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'nextToken': 'string',
            'projects': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **nextToken** *(string) --* 

          If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call.

          
        

        - **projects** *(list) --* 

          The list of build project names, with each build project name representing a single build project.

          
          

          - *(string) --* 
      
    

  .. py:method:: start_build(**kwargs)

    

    Starts running a build.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StartBuild>`_    


    **Request Syntax** 
    ::

      response = client.start_build(
          projectName='string',
          sourceVersion='string',
          artifactsOverride={
              'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
              'location': 'string',
              'path': 'string',
              'namespaceType': 'NONE'|'BUILD_ID',
              'name': 'string',
              'packaging': 'NONE'|'ZIP'
          },
          environmentVariablesOverride=[
              {
                  'name': 'string',
                  'value': 'string',
                  'type': 'PLAINTEXT'|'PARAMETER_STORE'
              },
          ],
          buildspecOverride='string',
          timeoutInMinutesOverride=123
      )
    :type projectName: string
    :param projectName: **[REQUIRED]** 

      The name of the build project to start running a build.

      

    
    :type sourceVersion: string
    :param sourceVersion: 

      A version of the build input to be built, for this build only. If not specified, the latest version will be used. If specified, must be one of:

       

       
      * For AWS CodeCommit: the commit ID to use. 
       
      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID will be used. If not specified, the default branch's HEAD commit ID will be used. 
       
      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID will be used. If not specified, the default branch's HEAD commit ID will be used. 
       
      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
       

      

    
    :type artifactsOverride: dict
    :param artifactsOverride: 

      Build output artifact settings that override, for this build only, the latest ones already defined in the build project.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of build output artifact. Valid values include:

         

         
        * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
         
        * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
         
        * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
         

        

      
      - **location** *(string) --* 

        Information about the build output artifact location, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
         

        

      
      - **path** *(string) --* 

        Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

        

      
      - **namespaceType** *(string) --* 

        Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , then valid values include: 

           
          * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
           
          * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
           

         
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        

      
      - **name** *(string) --* 

        Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the name of the output artifact object. 
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        

      
      - **packaging** *(string) --* 

        The type of build output artifact to create, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , valid values include: 

           
          * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
           
          * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
           

         
         

        

      
    
    :type environmentVariablesOverride: list
    :param environmentVariablesOverride: 

      A set of environment variables that overrides, for this build only, the latest ones already defined in the build project.

      

    
      - *(dict) --* 

        Information about an environment variable for a build project or a build.

        

      
        - **name** *(string) --* **[REQUIRED]** 

          The name or key of the environment variable.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The value of the environment variable.

           

          .. warning::

             

            We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

             

          

        
        - **type** *(string) --* 

          The type of environment variable. Valid values include:

           

           
          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
           
          * ``PLAINTEXT`` : An environment variable in plaintext format. 
           

          

        
      
  
    :type buildspecOverride: string
    :param buildspecOverride: 

      A build spec declaration that overrides, for this build only, the latest one already defined in the build project.

      

    
    :type timeoutInMinutesOverride: integer
    :param timeoutInMinutesOverride: 

      The number of build timeout minutes, from 5 to 480 (8 hours), that overrides, for this build only, the latest setting already defined in the build project.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'build': {
                'id': 'string',
                'arn': 'string',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'currentPhase': 'string',
                'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                'sourceVersion': 'string',
                'projectName': 'string',
                'phases': [
                    {
                        'phaseType': 'SUBMITTED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                        'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'durationInSeconds': 123,
                        'contexts': [
                            {
                                'statusCode': 'string',
                                'message': 'string'
                            },
                        ]
                    },
                ],
                'source': {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET',
                    'location': 'string',
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    }
                },
                'artifacts': {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string'
                },
                'cache': {
                    'type': 'NO_CACHE'|'S3',
                    'location': 'string'
                },
                'environment': {
                    'type': 'LINUX_CONTAINER',
                    'image': 'string',
                    'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                    'environmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'type': 'PLAINTEXT'|'PARAMETER_STORE'
                        },
                    ],
                    'privilegedMode': True|False
                },
                'logs': {
                    'groupName': 'string',
                    'streamName': 'string',
                    'deepLink': 'string'
                },
                'timeoutInMinutes': 123,
                'buildComplete': True|False,
                'initiator': 'string',
                'vpcConfig': {
                    'vpcId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ]
                },
                'networkInterface': {
                    'subnetId': 'string',
                    'networkInterfaceId': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **build** *(dict) --* 

          Information about the build to be run.

          
          

          - **id** *(string) --* 

            The unique ID for the build.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the build.

            
          

          - **startTime** *(datetime) --* 

            When the build process started, expressed in Unix time format.

            
          

          - **endTime** *(datetime) --* 

            When the build process ended, expressed in Unix time format.

            
          

          - **currentPhase** *(string) --* 

            The current build phase.

            
          

          - **buildStatus** *(string) --* 

            The current status of the build. Valid values include:

             

             
            * ``FAILED`` : The build failed. 
             
            * ``FAULT`` : The build faulted. 
             
            * ``IN_PROGRESS`` : The build is still in progress. 
             
            * ``STOPPED`` : The build stopped. 
             
            * ``SUCCEEDED`` : The build succeeded. 
             
            * ``TIMED_OUT`` : The build timed out. 
             

            
          

          - **sourceVersion** *(string) --* 

            Any version identifier for the version of the source code to be built.

            
          

          - **projectName** *(string) --* 

            The name of the build project.

            
          

          - **phases** *(list) --* 

            Information about all previous build phases that are completed and information about any current build phase that is not yet complete.

            
            

            - *(dict) --* 

              Information about a stage for a build.

              
              

              - **phaseType** *(string) --* 

                The name of the build phase. Valid values include:

                 

                 
                * ``BUILD`` : Core build activities typically occur in this build phase. 
                 
                * ``COMPLETED`` : The build has been completed. 
                 
                * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase. 
                 
                * ``FINALIZING`` : The build process is completing in this build phase. 
                 
                * ``INSTALL`` : Installation activities typically occur in this build phase. 
                 
                * ``POST_BUILD`` : Post-build activities typically occur in this build phase. 
                 
                * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase. 
                 
                * ``PROVISIONING`` : The build environment is being set up. 
                 
                * ``SUBMITTED`` : The build has been submitted. 
                 
                * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output location. 
                 

                
              

              - **phaseStatus** *(string) --* 

                The current status of the build phase. Valid values include:

                 

                 
                * ``FAILED`` : The build phase failed. 
                 
                * ``FAULT`` : The build phase faulted. 
                 
                * ``IN_PROGRESS`` : The build phase is still in progress. 
                 
                * ``STOPPED`` : The build phase stopped. 
                 
                * ``SUCCEEDED`` : The build phase succeeded. 
                 
                * ``TIMED_OUT`` : The build phase timed out. 
                 

                
              

              - **startTime** *(datetime) --* 

                When the build phase started, expressed in Unix time format.

                
              

              - **endTime** *(datetime) --* 

                When the build phase ended, expressed in Unix time format.

                
              

              - **durationInSeconds** *(integer) --* 

                How long, in seconds, between the starting and ending times of the build's phase.

                
              

              - **contexts** *(list) --* 

                Additional information about a build phase, especially to help troubleshoot a failed build.

                
                

                - *(dict) --* 

                  Additional information about a build phase that has an error. You can use this information to help troubleshoot a failed build.

                  
                  

                  - **statusCode** *(string) --* 

                    The status code for the context of the build phase.

                    
                  

                  - **message** *(string) --* 

                    An explanation of the build phase's context. This explanation might include a command ID and an exit code.

                    
              
            
          
        
          

          - **source** *(dict) --* 

            Information about the source code to be built.

            
            

            - **type** *(string) --* 

              The type of repository that contains the source code to be built. Valid values include:

               

               
              * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
               
              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
               
              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
               
              * ``GITHUB`` : The source code is in a GitHub repository. 
               
              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
               

              
            

            - **location** *(string) --* 

              Information about the location of the source code to be built. Valid values include:

               

               
              * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value. 
               
              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
               
              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ) 
               
              * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
               
              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
               

              
            

            - **buildspec** *(string) --* 

              The build spec declaration to use for the builds in this build project.

               

              If this value is not specified, a build spec must be included along with the source code to be built.

              
            

            - **auth** *(dict) --* 

              Information about the authorization settings for AWS CodeBuild to access the source code to be built.

               

              This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly (unless the build project's source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).

              
              

              - **type** *(string) --* 

                The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.

                
              

              - **resource** *(string) --* 

                The resource value that applies to the specified authorization type.

                
          
        
          

          - **artifacts** *(dict) --* 

            Information about the output artifacts for the build.

            
            

            - **location** *(string) --* 

              Information about the location of the build artifacts.

              
            

            - **sha256sum** *(string) --* 

              The SHA-256 hash of the build artifact.

               

              You can use this hash along with a checksum tool to confirm both file integrity and authenticity.

               

              .. note::

                 

                This value is available only if the build project's ``packaging`` value is set to ``ZIP`` .

                 

              
            

            - **md5sum** *(string) --* 

              The MD5 hash of the build artifact.

               

              You can use this hash along with a checksum tool to confirm both file integrity and authenticity.

               

              .. note::

                 

                This value is available only if the build project's ``packaging`` value is set to ``ZIP`` .

                 

              
        
          

          - **cache** *(dict) --* 

            Information about the cache for the build.

            
            

            - **type** *(string) --* 

              The type of cache used by the build project. Valid values include:

               

               
              * ``NO_CACHE`` : The build project will not use any cache. 
               
              * ``S3`` : The build project will read and write from/to S3. 
               

              
            

            - **location** *(string) --* 

              Information about the cache location, as follows: 

               

               
              * ``NO_CACHE`` : This value will be ignored. 
               
              * ``S3`` : This is the S3 bucket name/prefix. 
               

              
        
          

          - **environment** *(dict) --* 

            Information about the build environment for this build.

            
            

            - **type** *(string) --* 

              The type of build environment to use for related builds.

              
            

            - **image** *(string) --* 

              The ID of the Docker image to use for this build project.

              
            

            - **computeType** *(string) --* 

              Information about the compute resources the build project will use. Available values include:

               

               
              * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
               
              * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
               
              * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
               

              
            

            - **environmentVariables** *(list) --* 

              A set of environment variables to make available to builds for this build project.

              
              

              - *(dict) --* 

                Information about an environment variable for a build project or a build.

                
                

                - **name** *(string) --* 

                  The name or key of the environment variable.

                  
                

                - **value** *(string) --* 

                  The value of the environment variable.

                   

                  .. warning::

                     

                    We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

                     

                  
                

                - **type** *(string) --* 

                  The type of environment variable. Valid values include:

                   

                   
                  * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                   
                  * ``PLAINTEXT`` : An environment variable in plaintext format. 
                   

                  
            
          
            

            - **privilegedMode** *(boolean) --* 

              If set to true, enables running the Docker daemon inside a Docker container; otherwise, false or not specified (the default). This value must be set to true only if this build project will be used to build Docker images, and the specified build environment image is not one provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that your builds can interact with it as needed. One way to do this is to initialize the Docker daemon in the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)

               

               ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``  

              
        
          

          - **logs** *(dict) --* 

            Information about the build's logs in Amazon CloudWatch Logs.

            
            

            - **groupName** *(string) --* 

              The name of the Amazon CloudWatch Logs group for the build logs.

              
            

            - **streamName** *(string) --* 

              The name of the Amazon CloudWatch Logs stream for the build logs.

              
            

            - **deepLink** *(string) --* 

              The URL to an individual build log in Amazon CloudWatch Logs.

              
        
          

          - **timeoutInMinutes** *(integer) --* 

            How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.

            
          

          - **buildComplete** *(boolean) --* 

            Whether the build has finished. True if completed; otherwise, false.

            
          

          - **initiator** *(string) --* 

            The entity that started the build. Valid values include:

             

             
            * If AWS CodePipeline started the build, the pipeline's name (for example, ``codepipeline/my-demo-pipeline`` ). 
             
            * If an AWS Identity and Access Management (IAM) user started the build, the user's name (for example ``MyUserName`` ). 
             
            * If the Jenkins plugin for AWS CodeBuild started the build, the string ``CodeBuild-Jenkins-Plugin`` . 
             

            
          

          - **vpcConfig** *(dict) --* 

            If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

            
            

            - **vpcId** *(string) --* 

              The ID of the Amazon VPC.

              
            

            - **subnets** *(list) --* 

              A list of one or more subnet IDs in your Amazon VPC.

              
              

              - *(string) --* 
          
            

            - **securityGroupIds** *(list) --* 

              A list of one or more security groups IDs in your Amazon VPC.

              
              

              - *(string) --* 
          
        
          

          - **networkInterface** *(dict) --* 

            Describes a network interface.

            
            

            - **subnetId** *(string) --* 

              The ID of the subnet.

              
            

            - **networkInterfaceId** *(string) --* 

              The ID of the network interface.

              
        
      
    

  .. py:method:: stop_build(**kwargs)

    

    Attempts to stop running a build.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StopBuild>`_    


    **Request Syntax** 
    ::

      response = client.stop_build(
          id='string'
      )
    :type id: string
    :param id: **[REQUIRED]** 

      The ID of the build.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'build': {
                'id': 'string',
                'arn': 'string',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'currentPhase': 'string',
                'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                'sourceVersion': 'string',
                'projectName': 'string',
                'phases': [
                    {
                        'phaseType': 'SUBMITTED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                        'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'durationInSeconds': 123,
                        'contexts': [
                            {
                                'statusCode': 'string',
                                'message': 'string'
                            },
                        ]
                    },
                ],
                'source': {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET',
                    'location': 'string',
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    }
                },
                'artifacts': {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string'
                },
                'cache': {
                    'type': 'NO_CACHE'|'S3',
                    'location': 'string'
                },
                'environment': {
                    'type': 'LINUX_CONTAINER',
                    'image': 'string',
                    'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                    'environmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'type': 'PLAINTEXT'|'PARAMETER_STORE'
                        },
                    ],
                    'privilegedMode': True|False
                },
                'logs': {
                    'groupName': 'string',
                    'streamName': 'string',
                    'deepLink': 'string'
                },
                'timeoutInMinutes': 123,
                'buildComplete': True|False,
                'initiator': 'string',
                'vpcConfig': {
                    'vpcId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ]
                },
                'networkInterface': {
                    'subnetId': 'string',
                    'networkInterfaceId': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **build** *(dict) --* 

          Information about the build.

          
          

          - **id** *(string) --* 

            The unique ID for the build.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the build.

            
          

          - **startTime** *(datetime) --* 

            When the build process started, expressed in Unix time format.

            
          

          - **endTime** *(datetime) --* 

            When the build process ended, expressed in Unix time format.

            
          

          - **currentPhase** *(string) --* 

            The current build phase.

            
          

          - **buildStatus** *(string) --* 

            The current status of the build. Valid values include:

             

             
            * ``FAILED`` : The build failed. 
             
            * ``FAULT`` : The build faulted. 
             
            * ``IN_PROGRESS`` : The build is still in progress. 
             
            * ``STOPPED`` : The build stopped. 
             
            * ``SUCCEEDED`` : The build succeeded. 
             
            * ``TIMED_OUT`` : The build timed out. 
             

            
          

          - **sourceVersion** *(string) --* 

            Any version identifier for the version of the source code to be built.

            
          

          - **projectName** *(string) --* 

            The name of the build project.

            
          

          - **phases** *(list) --* 

            Information about all previous build phases that are completed and information about any current build phase that is not yet complete.

            
            

            - *(dict) --* 

              Information about a stage for a build.

              
              

              - **phaseType** *(string) --* 

                The name of the build phase. Valid values include:

                 

                 
                * ``BUILD`` : Core build activities typically occur in this build phase. 
                 
                * ``COMPLETED`` : The build has been completed. 
                 
                * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase. 
                 
                * ``FINALIZING`` : The build process is completing in this build phase. 
                 
                * ``INSTALL`` : Installation activities typically occur in this build phase. 
                 
                * ``POST_BUILD`` : Post-build activities typically occur in this build phase. 
                 
                * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase. 
                 
                * ``PROVISIONING`` : The build environment is being set up. 
                 
                * ``SUBMITTED`` : The build has been submitted. 
                 
                * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output location. 
                 

                
              

              - **phaseStatus** *(string) --* 

                The current status of the build phase. Valid values include:

                 

                 
                * ``FAILED`` : The build phase failed. 
                 
                * ``FAULT`` : The build phase faulted. 
                 
                * ``IN_PROGRESS`` : The build phase is still in progress. 
                 
                * ``STOPPED`` : The build phase stopped. 
                 
                * ``SUCCEEDED`` : The build phase succeeded. 
                 
                * ``TIMED_OUT`` : The build phase timed out. 
                 

                
              

              - **startTime** *(datetime) --* 

                When the build phase started, expressed in Unix time format.

                
              

              - **endTime** *(datetime) --* 

                When the build phase ended, expressed in Unix time format.

                
              

              - **durationInSeconds** *(integer) --* 

                How long, in seconds, between the starting and ending times of the build's phase.

                
              

              - **contexts** *(list) --* 

                Additional information about a build phase, especially to help troubleshoot a failed build.

                
                

                - *(dict) --* 

                  Additional information about a build phase that has an error. You can use this information to help troubleshoot a failed build.

                  
                  

                  - **statusCode** *(string) --* 

                    The status code for the context of the build phase.

                    
                  

                  - **message** *(string) --* 

                    An explanation of the build phase's context. This explanation might include a command ID and an exit code.

                    
              
            
          
        
          

          - **source** *(dict) --* 

            Information about the source code to be built.

            
            

            - **type** *(string) --* 

              The type of repository that contains the source code to be built. Valid values include:

               

               
              * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
               
              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
               
              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
               
              * ``GITHUB`` : The source code is in a GitHub repository. 
               
              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
               

              
            

            - **location** *(string) --* 

              Information about the location of the source code to be built. Valid values include:

               

               
              * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value. 
               
              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
               
              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ) 
               
              * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
               
              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
               

              
            

            - **buildspec** *(string) --* 

              The build spec declaration to use for the builds in this build project.

               

              If this value is not specified, a build spec must be included along with the source code to be built.

              
            

            - **auth** *(dict) --* 

              Information about the authorization settings for AWS CodeBuild to access the source code to be built.

               

              This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly (unless the build project's source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).

              
              

              - **type** *(string) --* 

                The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.

                
              

              - **resource** *(string) --* 

                The resource value that applies to the specified authorization type.

                
          
        
          

          - **artifacts** *(dict) --* 

            Information about the output artifacts for the build.

            
            

            - **location** *(string) --* 

              Information about the location of the build artifacts.

              
            

            - **sha256sum** *(string) --* 

              The SHA-256 hash of the build artifact.

               

              You can use this hash along with a checksum tool to confirm both file integrity and authenticity.

               

              .. note::

                 

                This value is available only if the build project's ``packaging`` value is set to ``ZIP`` .

                 

              
            

            - **md5sum** *(string) --* 

              The MD5 hash of the build artifact.

               

              You can use this hash along with a checksum tool to confirm both file integrity and authenticity.

               

              .. note::

                 

                This value is available only if the build project's ``packaging`` value is set to ``ZIP`` .

                 

              
        
          

          - **cache** *(dict) --* 

            Information about the cache for the build.

            
            

            - **type** *(string) --* 

              The type of cache used by the build project. Valid values include:

               

               
              * ``NO_CACHE`` : The build project will not use any cache. 
               
              * ``S3`` : The build project will read and write from/to S3. 
               

              
            

            - **location** *(string) --* 

              Information about the cache location, as follows: 

               

               
              * ``NO_CACHE`` : This value will be ignored. 
               
              * ``S3`` : This is the S3 bucket name/prefix. 
               

              
        
          

          - **environment** *(dict) --* 

            Information about the build environment for this build.

            
            

            - **type** *(string) --* 

              The type of build environment to use for related builds.

              
            

            - **image** *(string) --* 

              The ID of the Docker image to use for this build project.

              
            

            - **computeType** *(string) --* 

              Information about the compute resources the build project will use. Available values include:

               

               
              * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
               
              * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
               
              * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
               

              
            

            - **environmentVariables** *(list) --* 

              A set of environment variables to make available to builds for this build project.

              
              

              - *(dict) --* 

                Information about an environment variable for a build project or a build.

                
                

                - **name** *(string) --* 

                  The name or key of the environment variable.

                  
                

                - **value** *(string) --* 

                  The value of the environment variable.

                   

                  .. warning::

                     

                    We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

                     

                  
                

                - **type** *(string) --* 

                  The type of environment variable. Valid values include:

                   

                   
                  * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                   
                  * ``PLAINTEXT`` : An environment variable in plaintext format. 
                   

                  
            
          
            

            - **privilegedMode** *(boolean) --* 

              If set to true, enables running the Docker daemon inside a Docker container; otherwise, false or not specified (the default). This value must be set to true only if this build project will be used to build Docker images, and the specified build environment image is not one provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that your builds can interact with it as needed. One way to do this is to initialize the Docker daemon in the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)

               

               ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``  

              
        
          

          - **logs** *(dict) --* 

            Information about the build's logs in Amazon CloudWatch Logs.

            
            

            - **groupName** *(string) --* 

              The name of the Amazon CloudWatch Logs group for the build logs.

              
            

            - **streamName** *(string) --* 

              The name of the Amazon CloudWatch Logs stream for the build logs.

              
            

            - **deepLink** *(string) --* 

              The URL to an individual build log in Amazon CloudWatch Logs.

              
        
          

          - **timeoutInMinutes** *(integer) --* 

            How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.

            
          

          - **buildComplete** *(boolean) --* 

            Whether the build has finished. True if completed; otherwise, false.

            
          

          - **initiator** *(string) --* 

            The entity that started the build. Valid values include:

             

             
            * If AWS CodePipeline started the build, the pipeline's name (for example, ``codepipeline/my-demo-pipeline`` ). 
             
            * If an AWS Identity and Access Management (IAM) user started the build, the user's name (for example ``MyUserName`` ). 
             
            * If the Jenkins plugin for AWS CodeBuild started the build, the string ``CodeBuild-Jenkins-Plugin`` . 
             

            
          

          - **vpcConfig** *(dict) --* 

            If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

            
            

            - **vpcId** *(string) --* 

              The ID of the Amazon VPC.

              
            

            - **subnets** *(list) --* 

              A list of one or more subnet IDs in your Amazon VPC.

              
              

              - *(string) --* 
          
            

            - **securityGroupIds** *(list) --* 

              A list of one or more security groups IDs in your Amazon VPC.

              
              

              - *(string) --* 
          
        
          

          - **networkInterface** *(dict) --* 

            Describes a network interface.

            
            

            - **subnetId** *(string) --* 

              The ID of the subnet.

              
            

            - **networkInterfaceId** *(string) --* 

              The ID of the network interface.

              
        
      
    

  .. py:method:: update_project(**kwargs)

    

    Changes the settings of a build project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateProject>`_    


    **Request Syntax** 
    ::

      response = client.update_project(
          name='string',
          description='string',
          source={
              'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET',
              'location': 'string',
              'buildspec': 'string',
              'auth': {
                  'type': 'OAUTH',
                  'resource': 'string'
              }
          },
          artifacts={
              'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
              'location': 'string',
              'path': 'string',
              'namespaceType': 'NONE'|'BUILD_ID',
              'name': 'string',
              'packaging': 'NONE'|'ZIP'
          },
          cache={
              'type': 'NO_CACHE'|'S3',
              'location': 'string'
          },
          environment={
              'type': 'LINUX_CONTAINER',
              'image': 'string',
              'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
              'environmentVariables': [
                  {
                      'name': 'string',
                      'value': 'string',
                      'type': 'PLAINTEXT'|'PARAMETER_STORE'
                  },
              ],
              'privilegedMode': True|False
          },
          serviceRole='string',
          timeoutInMinutes=123,
          encryptionKey='string',
          tags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ],
          vpcConfig={
              'vpcId': 'string',
              'subnets': [
                  'string',
              ],
              'securityGroupIds': [
                  'string',
              ]
          },
          badgeEnabled=True|False
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the build project.

       

      .. note::

         

        You cannot change a build project's name.

         

      

    
    :type description: string
    :param description: 

      A new or replacement description of the build project.

      

    
    :type source: dict
    :param source: 

      Information to be changed about the build input source code for the build project.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of repository that contains the source code to be built. Valid values include:

         

         
        * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
         
        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
         
        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
         
        * ``GITHUB`` : The source code is in a GitHub repository. 
         
        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
         

        

      
      - **location** *(string) --* 

        Information about the location of the source code to be built. Valid values include:

         

         
        * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value. 
         
        * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
         
        * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ) 
         
        * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
         
        * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
         

        

      
      - **buildspec** *(string) --* 

        The build spec declaration to use for the builds in this build project.

         

        If this value is not specified, a build spec must be included along with the source code to be built.

        

      
      - **auth** *(dict) --* 

        Information about the authorization settings for AWS CodeBuild to access the source code to be built.

         

        This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly (unless the build project's source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).

        

      
        - **type** *(string) --* **[REQUIRED]** 

          The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.

          

        
        - **resource** *(string) --* 

          The resource value that applies to the specified authorization type.

          

        
      
    
    :type artifacts: dict
    :param artifacts: 

      Information to be changed about the build output artifacts for the build project.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of build output artifact. Valid values include:

         

         
        * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
         
        * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
         
        * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
         

        

      
      - **location** *(string) --* 

        Information about the build output artifact location, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
         

        

      
      - **path** *(string) --* 

        Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

        

      
      - **namespaceType** *(string) --* 

        Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , then valid values include: 

           
          * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
           
          * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
           

         
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        

      
      - **name** *(string) --* 

        Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , this is the name of the output artifact object. 
         

         

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        

      
      - **packaging** *(string) --* 

        The type of build output artifact to create, as follows:

         

         
        * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
         
        * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
         
        * If ``type`` is set to ``S3`` , valid values include: 

           
          * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
           
          * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
           

         
         

        

      
    
    :type cache: dict
    :param cache: 

      Stores recently used information so that it can be quickly accessed at a later time.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of cache used by the build project. Valid values include:

         

         
        * ``NO_CACHE`` : The build project will not use any cache. 
         
        * ``S3`` : The build project will read and write from/to S3. 
         

        

      
      - **location** *(string) --* 

        Information about the cache location, as follows: 

         

         
        * ``NO_CACHE`` : This value will be ignored. 
         
        * ``S3`` : This is the S3 bucket name/prefix. 
         

        

      
    
    :type environment: dict
    :param environment: 

      Information to be changed about the build environment for the build project.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of build environment to use for related builds.

        

      
      - **image** *(string) --* **[REQUIRED]** 

        The ID of the Docker image to use for this build project.

        

      
      - **computeType** *(string) --* **[REQUIRED]** 

        Information about the compute resources the build project will use. Available values include:

         

         
        * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
         
        * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
         
        * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
         

        

      
      - **environmentVariables** *(list) --* 

        A set of environment variables to make available to builds for this build project.

        

      
        - *(dict) --* 

          Information about an environment variable for a build project or a build.

          

        
          - **name** *(string) --* **[REQUIRED]** 

            The name or key of the environment variable.

            

          
          - **value** *(string) --* **[REQUIRED]** 

            The value of the environment variable.

             

            .. warning::

               

              We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

               

            

          
          - **type** *(string) --* 

            The type of environment variable. Valid values include:

             

             
            * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
             
            * ``PLAINTEXT`` : An environment variable in plaintext format. 
             

            

          
        
    
      - **privilegedMode** *(boolean) --* 

        If set to true, enables running the Docker daemon inside a Docker container; otherwise, false or not specified (the default). This value must be set to true only if this build project will be used to build Docker images, and the specified build environment image is not one provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that your builds can interact with it as needed. One way to do this is to initialize the Docker daemon in the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)

         

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``  

        

      
    
    :type serviceRole: string
    :param serviceRole: 

      The replacement ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

      

    
    :type timeoutInMinutes: integer
    :param timeoutInMinutes: 

      The replacement value in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed.

      

    
    :type encryptionKey: string
    :param encryptionKey: 

      The replacement AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

       

      You can specify either the CMK's Amazon Resource Name (ARN) or, if available, the CMK's alias (using the format ``alias/*alias-name* `` ).

      

    
    :type tags: list
    :param tags: 

      The replacement set of tags for this build project.

       

      These tags are available for use by AWS services that support AWS CodeBuild build project tags.

      

    
      - *(dict) --* 

        A tag, consisting of a key and a value.

         

        This tag is available for use by AWS services that support tags in AWS CodeBuild.

        

      
        - **key** *(string) --* 

          The tag's key.

          

        
        - **value** *(string) --* 

          The tag's value.

          

        
      
  
    :type vpcConfig: dict
    :param vpcConfig: 

      VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.

      

    
      - **vpcId** *(string) --* 

        The ID of the Amazon VPC.

        

      
      - **subnets** *(list) --* 

        A list of one or more subnet IDs in your Amazon VPC.

        

      
        - *(string) --* 

        
    
      - **securityGroupIds** *(list) --* 

        A list of one or more security groups IDs in your Amazon VPC.

        

      
        - *(string) --* 

        
    
    
    :type badgeEnabled: boolean
    :param badgeEnabled: 

      Set this to true to generate a publicly-accessible URL for your project's build badge.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'project': {
                'name': 'string',
                'arn': 'string',
                'description': 'string',
                'source': {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET',
                    'location': 'string',
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    }
                },
                'artifacts': {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP'
                },
                'cache': {
                    'type': 'NO_CACHE'|'S3',
                    'location': 'string'
                },
                'environment': {
                    'type': 'LINUX_CONTAINER',
                    'image': 'string',
                    'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                    'environmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'type': 'PLAINTEXT'|'PARAMETER_STORE'
                        },
                    ],
                    'privilegedMode': True|False
                },
                'serviceRole': 'string',
                'timeoutInMinutes': 123,
                'encryptionKey': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'created': datetime(2015, 1, 1),
                'lastModified': datetime(2015, 1, 1),
                'webhook': {
                    'url': 'string'
                },
                'vpcConfig': {
                    'vpcId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ]
                },
                'badge': {
                    'badgeEnabled': True|False,
                    'badgeRequestUrl': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **project** *(dict) --* 

          Information about the build project that was changed.

          
          

          - **name** *(string) --* 

            The name of the build project.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the build project.

            
          

          - **description** *(string) --* 

            A description that makes the build project easy to identify.

            
          

          - **source** *(dict) --* 

            Information about the build input source code for this build project.

            
            

            - **type** *(string) --* 

              The type of repository that contains the source code to be built. Valid values include:

               

               
              * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
               
              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
               
              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
               
              * ``GITHUB`` : The source code is in a GitHub repository. 
               
              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
               

              
            

            - **location** *(string) --* 

              Information about the location of the source code to be built. Valid values include:

               

               
              * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value. 
               
              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
               
              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, the path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ) 
               
              * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
               
              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` . 
               

              
            

            - **buildspec** *(string) --* 

              The build spec declaration to use for the builds in this build project.

               

              If this value is not specified, a build spec must be included along with the source code to be built.

              
            

            - **auth** *(dict) --* 

              Information about the authorization settings for AWS CodeBuild to access the source code to be built.

               

              This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly (unless the build project's source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).

              
              

              - **type** *(string) --* 

                The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.

                
              

              - **resource** *(string) --* 

                The resource value that applies to the specified authorization type.

                
          
        
          

          - **artifacts** *(dict) --* 

            Information about the build output artifacts for the build project.

            
            

            - **type** *(string) --* 

              The type of build output artifact. Valid values include:

               

               
              * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
               
              * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
               
              * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
               

              
            

            - **location** *(string) --* 

              Information about the build output artifact location, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
               

              
            

            - **path** *(string) --* 

              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
               

               

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

              
            

            - **namespaceType** *(string) --* 

              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , then valid values include: 

                 
                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                 
                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                 

               
               

               

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

              
            

            - **name** *(string) --* 

              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. 
               

               

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

              
            

            - **packaging** *(string) --* 

              The type of build output artifact to create, as follows:

               

               
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , valid values include: 

                 
                * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                 
                * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                 

               
               

              
        
          

          - **cache** *(dict) --* 

            Information about the cache for the build project.

            
            

            - **type** *(string) --* 

              The type of cache used by the build project. Valid values include:

               

               
              * ``NO_CACHE`` : The build project will not use any cache. 
               
              * ``S3`` : The build project will read and write from/to S3. 
               

              
            

            - **location** *(string) --* 

              Information about the cache location, as follows: 

               

               
              * ``NO_CACHE`` : This value will be ignored. 
               
              * ``S3`` : This is the S3 bucket name/prefix. 
               

              
        
          

          - **environment** *(dict) --* 

            Information about the build environment for this build project.

            
            

            - **type** *(string) --* 

              The type of build environment to use for related builds.

              
            

            - **image** *(string) --* 

              The ID of the Docker image to use for this build project.

              
            

            - **computeType** *(string) --* 

              Information about the compute resources the build project will use. Available values include:

               

               
              * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
               
              * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
               
              * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
               

              
            

            - **environmentVariables** *(list) --* 

              A set of environment variables to make available to builds for this build project.

              
              

              - *(dict) --* 

                Information about an environment variable for a build project or a build.

                
                

                - **name** *(string) --* 

                  The name or key of the environment variable.

                  
                

                - **value** *(string) --* 

                  The value of the environment variable.

                   

                  .. warning::

                     

                    We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).

                     

                  
                

                - **type** *(string) --* 

                  The type of environment variable. Valid values include:

                   

                   
                  * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                   
                  * ``PLAINTEXT`` : An environment variable in plaintext format. 
                   

                  
            
          
            

            - **privilegedMode** *(boolean) --* 

              If set to true, enables running the Docker daemon inside a Docker container; otherwise, false or not specified (the default). This value must be set to true only if this build project will be used to build Docker images, and the specified build environment image is not one provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that your builds can interact with it as needed. One way to do this is to initialize the Docker daemon in the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)

               

               ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``  

              
        
          

          - **serviceRole** *(string) --* 

            The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

            
          

          - **timeoutInMinutes** *(integer) --* 

            How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.

            
          

          - **encryptionKey** *(string) --* 

            The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

             

            This is expressed either as the CMK's Amazon Resource Name (ARN) or, if specified, the CMK's alias (using the format ``alias/*alias-name* `` ).

            
          

          - **tags** *(list) --* 

            The tags for this build project.

             

            These tags are available for use by AWS services that support AWS CodeBuild build project tags.

            
            

            - *(dict) --* 

              A tag, consisting of a key and a value.

               

              This tag is available for use by AWS services that support tags in AWS CodeBuild.

              
              

              - **key** *(string) --* 

                The tag's key.

                
              

              - **value** *(string) --* 

                The tag's value.

                
          
        
          

          - **created** *(datetime) --* 

            When the build project was created, expressed in Unix time format.

            
          

          - **lastModified** *(datetime) --* 

            When the build project's settings were last modified, expressed in Unix time format.

            
          

          - **webhook** *(dict) --* 

            Information about a webhook in GitHub that connects repository events to a build project in AWS CodeBuild.

            
            

            - **url** *(string) --* 

              The URL to the webhook.

              
        
          

          - **vpcConfig** *(dict) --* 

            If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

            
            

            - **vpcId** *(string) --* 

              The ID of the Amazon VPC.

              
            

            - **subnets** *(list) --* 

              A list of one or more subnet IDs in your Amazon VPC.

              
              

              - *(string) --* 
          
            

            - **securityGroupIds** *(list) --* 

              A list of one or more security groups IDs in your Amazon VPC.

              
              

              - *(string) --* 
          
        
          

          - **badge** *(dict) --* 

            Information about the build badge for the build project.

            
            

            - **badgeEnabled** *(boolean) --* 

              Set this to true to generate a publicly-accessible URL for your project's build badge.

              
            

            - **badgeRequestUrl** *(string) --* 

              The publicly-accessible URL through which you can access the build badge for your project. 

              
        
      
    

==========
Paginators
==========


The available paginators are:

* :py:class:`CodeBuild.Paginator.ListBuilds`


* :py:class:`CodeBuild.Paginator.ListBuildsForProject`


* :py:class:`CodeBuild.Paginator.ListProjects`



.. py:class:: CodeBuild.Paginator.ListBuilds

  ::

    
    paginator = client.get_paginator('list_builds')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeBuild.Client.list_builds`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuilds>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          sortOrder='ASCENDING'|'DESCENDING',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type sortOrder: string
    :param sortOrder: 

      The order to list build IDs. Valid values include:

       

       
      * ``ASCENDING`` : List the build IDs in ascending order by build ID. 
       
      * ``DESCENDING`` : List the build IDs in descending order by build ID. 
       

      

    
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
            'ids': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ids** *(list) --* 

          A list of build IDs, with each build ID representing a single build.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CodeBuild.Paginator.ListBuildsForProject

  ::

    
    paginator = client.get_paginator('list_builds_for_project')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeBuild.Client.list_builds_for_project`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuildsForProject>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          projectName='string',
          sortOrder='ASCENDING'|'DESCENDING',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type projectName: string
    :param projectName: **[REQUIRED]** 

      The name of the build project.

      

    
    :type sortOrder: string
    :param sortOrder: 

      The order to list build IDs. Valid values include:

       

       
      * ``ASCENDING`` : List the build IDs in ascending order by build ID. 
       
      * ``DESCENDING`` : List the build IDs in descending order by build ID. 
       

      

    
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
            'ids': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ids** *(list) --* 

          A list of build IDs for the specified build project, with each build ID representing a single build.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CodeBuild.Paginator.ListProjects

  ::

    
    paginator = client.get_paginator('list_projects')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CodeBuild.Client.list_projects`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListProjects>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          sortBy='NAME'|'CREATED_TIME'|'LAST_MODIFIED_TIME',
          sortOrder='ASCENDING'|'DESCENDING',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type sortBy: string
    :param sortBy: 

      The criterion to be used to list build project names. Valid values include:

       

       
      * ``CREATED_TIME`` : List the build project names based on when each build project was created. 
       
      * ``LAST_MODIFIED_TIME`` : List the build project names based on when information about each build project was last changed. 
       
      * ``NAME`` : List the build project names based on each build project's name. 
       

       

      Use ``sortOrder`` to specify in what order to list the build project names based on the preceding criteria.

      

    
    :type sortOrder: string
    :param sortOrder: 

      The order in which to list build projects. Valid values include:

       

       
      * ``ASCENDING`` : List the build project names in ascending order. 
       
      * ``DESCENDING`` : List the build project names in descending order. 
       

       

      Use ``sortBy`` to specify the criterion to be used to list build project names.

      

    
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
            'projects': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **projects** *(list) --* 

          The list of build project names, with each build project name representing a single build project.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    