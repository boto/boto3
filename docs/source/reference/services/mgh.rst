

************
MigrationHub
************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: MigrationHub.Client

  A low-level client representing AWS Migration Hub::

    
    import boto3
    
    client = boto3.client('mgh')

  
  These are the available methods:
  
  *   :py:meth:`~MigrationHub.Client.associate_created_artifact`

  
  *   :py:meth:`~MigrationHub.Client.associate_discovered_resource`

  
  *   :py:meth:`~MigrationHub.Client.can_paginate`

  
  *   :py:meth:`~MigrationHub.Client.create_progress_update_stream`

  
  *   :py:meth:`~MigrationHub.Client.delete_progress_update_stream`

  
  *   :py:meth:`~MigrationHub.Client.describe_application_state`

  
  *   :py:meth:`~MigrationHub.Client.describe_migration_task`

  
  *   :py:meth:`~MigrationHub.Client.disassociate_created_artifact`

  
  *   :py:meth:`~MigrationHub.Client.disassociate_discovered_resource`

  
  *   :py:meth:`~MigrationHub.Client.generate_presigned_url`

  
  *   :py:meth:`~MigrationHub.Client.get_paginator`

  
  *   :py:meth:`~MigrationHub.Client.get_waiter`

  
  *   :py:meth:`~MigrationHub.Client.import_migration_task`

  
  *   :py:meth:`~MigrationHub.Client.list_created_artifacts`

  
  *   :py:meth:`~MigrationHub.Client.list_discovered_resources`

  
  *   :py:meth:`~MigrationHub.Client.list_migration_tasks`

  
  *   :py:meth:`~MigrationHub.Client.list_progress_update_streams`

  
  *   :py:meth:`~MigrationHub.Client.notify_application_state`

  
  *   :py:meth:`~MigrationHub.Client.notify_migration_task_state`

  
  *   :py:meth:`~MigrationHub.Client.put_resource_attributes`

  

  .. py:method:: associate_created_artifact(**kwargs)

    

    Associates a created artifact of an AWS cloud resource, the target receiving the migration, with the migration task performed by a migration tool. This API has the following traits:

     

     
    * Migration tools can call the ``AssociateCreatedArtifact`` operation to indicate which AWS artifact is associated with a migration task. 
     
    * The created artifact name must be provided in ARN (Amazon Resource Name) format which will contain information about type and region; for example: ``arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b`` . 
     
    * Examples of the AWS resource behind the created artifact are, AMI's, EC2 instance, or DMS endpoint, etc. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/AssociateCreatedArtifact>`_    


    **Request Syntax** 
    ::

      response = client.associate_created_artifact(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          CreatedArtifact={
              'Name': 'string',
              'Description': 'string'
          },
          DryRun=True|False
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      Unique identifier that references the migration task.

      

    
    :type CreatedArtifact: dict
    :param CreatedArtifact: **[REQUIRED]** 

      An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.) 

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        An ARN that uniquely identifies the result of a migration task.

        

      
      - **Description** *(string) --* 

        A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.

        

      
    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: associate_discovered_resource(**kwargs)

    

    Associates a discovered resource ID from Application Discovery Service (ADS) with a migration task.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource>`_    


    **Request Syntax** 
    ::

      response = client.associate_discovered_resource(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          DiscoveredResource={
              'ConfigurationId': 'string',
              'Description': 'string'
          },
          DryRun=True|False
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream.

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      The identifier given to the MigrationTask.

      

    
    :type DiscoveredResource: dict
    :param DiscoveredResource: **[REQUIRED]** 

      Object representing a Resource.

      

    
      - **ConfigurationId** *(string) --* **[REQUIRED]** 

        The configurationId in ADS that uniquely identifies the on-premise resource.

        

      
      - **Description** *(string) --* 

        A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.

        

      
    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

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


  .. py:method:: create_progress_update_stream(**kwargs)

    

    Creates a progress update stream which is an AWS resource used for access control as well as a namespace for migration task names that is implicitly linked to your AWS account. It must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream>`_    


    **Request Syntax** 
    ::

      response = client.create_progress_update_stream(
          ProgressUpdateStreamName='string',
          DryRun=True|False
      )
    :type ProgressUpdateStreamName: string
    :param ProgressUpdateStreamName: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_progress_update_stream(**kwargs)

    

    Deletes a progress update stream, including all of its tasks, which was previously created as an AWS resource used for access control. This API has the following traits:

     

     
    * The only parameter needed for ``DeleteProgressUpdateStream`` is the stream name (same as a ``CreateProgressUpdateStream`` call). 
     
    * The call will return, and a background process will asynchronously be doing the actual delete of the stream and all of its resources (tasks, associated resources, resource attributes, created artifacts). 
     
    * If the stream takes time to be deleted, it might still show up on a ``ListProgressUpdateStreams`` call. 
     
    * ``CreateProgressUpdateStream`` , ``ImportMigrationTask`` , ``NotifyMigrationTaskState`` , and all Associate[*] APIs realted to the tasks belonging to the stream will throw "InvalidInputException" if the stream of the same name is in the process of being deleted. 
     
    * Once the stream and all of its resources are deleted, ``CreateProgressUpdateStream`` for a stream of the same name will succeed, and that stream will be an entirely new logical resource (without any resources associated with the old stream). 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DeleteProgressUpdateStream>`_    


    **Request Syntax** 
    ::

      response = client.delete_progress_update_stream(
          ProgressUpdateStreamName='string',
          DryRun=True|False
      )
    :type ProgressUpdateStreamName: string
    :param ProgressUpdateStreamName: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_application_state(**kwargs)

    

    Gets the migration status of an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DescribeApplicationState>`_    


    **Request Syntax** 
    ::

      response = client.describe_application_state(
          ApplicationId='string'
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** 

      The configurationId in ADS that uniquely identifies the grouped application.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationStatus': 'NOT_STARTED'|'IN_PROGRESS'|'COMPLETED',
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ApplicationStatus** *(string) --* 

          Status of the application - Not Started, In-Progress, Complete.

          
        

        - **LastUpdatedTime** *(datetime) --* 

          The timestamp when the application status was last updated.

          
    

  .. py:method:: describe_migration_task(**kwargs)

    

    Retrieves a list of all attributes associated with a specific migration task.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DescribeMigrationTask>`_    


    **Request Syntax** 
    ::

      response = client.describe_migration_task(
          ProgressUpdateStream='string',
          MigrationTaskName='string'
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      The identifier given to the MigrationTask.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MigrationTask': {
                'ProgressUpdateStream': 'string',
                'MigrationTaskName': 'string',
                'Task': {
                    'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
                    'StatusDetail': 'string',
                    'ProgressPercent': 123
                },
                'UpdateDateTime': datetime(2015, 1, 1),
                'ResourceAttributeList': [
                    {
                        'Type': 'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MAC_ADDRESS'|'FQDN'|'VM_MANAGER_ID'|'VM_MANAGED_OBJECT_REFERENCE'|'VM_NAME'|'VM_PATH'|'BIOS_ID'|'MOTHERBOARD_SERIAL_NUMBER'|'LABEL',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **MigrationTask** *(dict) --* 

          Object encapsulating information about the migration task.

          
          

          - **ProgressUpdateStream** *(string) --* 

            A name that identifies the vendor of the migration tool being used.

            
          

          - **MigrationTaskName** *(string) --* 

            Unique identifier that references the migration task.

            
          

          - **Task** *(dict) --* 

            Task object encapsulating task information.

            
            

            - **Status** *(string) --* 

              Status of the task - Not Started, In-Progress, Complete.

              
            

            - **StatusDetail** *(string) --* 

              Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.

              
            

            - **ProgressPercent** *(integer) --* 

              Indication of the percentage completion of the task.

              
        
          

          - **UpdateDateTime** *(datetime) --* 

            The timestamp when the task was gathered.

            
          

          - **ResourceAttributeList** *(list) --* 

            

            
            

            - *(dict) --* 

              Attribute associated with a resource.

              
              

              - **Type** *(string) --* 

                Type of resource.

                
              

              - **Value** *(string) --* 

                Value of the resource type.

                
          
        
      
    

  .. py:method:: disassociate_created_artifact(**kwargs)

    

    Disassociates a created artifact of an AWS resource with a migration task performed by a migration tool that was previously associated. This API has the following traits:

     

     
    * A migration user can call the ``DisassociateCreatedArtifacts`` operation to disassociate a created AWS Artifact from a migration task. 
     
    * The created artifact name must be provided in ARN (Amazon Resource Name) format which will contain information about type and region; for example: ``arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b`` . 
     
    * Examples of the AWS resource behind the created artifact are, AMI's, EC2 instance, or RDS instance, etc. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DisassociateCreatedArtifact>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_created_artifact(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          CreatedArtifactName='string',
          DryRun=True|False
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      Unique identifier that references the migration task to be disassociated with the artifact.

      

    
    :type CreatedArtifactName: string
    :param CreatedArtifactName: **[REQUIRED]** 

      An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)

      

    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: disassociate_discovered_resource(**kwargs)

    

    Disassociate an Application Discovery Service (ADS) discovered resource from a migration task.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DisassociateDiscoveredResource>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_discovered_resource(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          ConfigurationId='string',
          DryRun=True|False
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream.

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      The identifier given to the MigrationTask.

      

    
    :type ConfigurationId: string
    :param ConfigurationId: **[REQUIRED]** 

      ConfigurationId of the ADS resource to be disassociated.

      

    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
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

        


  .. py:method:: import_migration_task(**kwargs)

    

    Registers a new migration task which represents a server, database, etc., being migrated to AWS by a migration tool.

     

    This API is a prerequisite to calling the ``NotifyMigrationTaskState`` API as the migration tool must first register the migration task with Migration Hub.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ImportMigrationTask>`_    


    **Request Syntax** 
    ::

      response = client.import_migration_task(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          DryRun=True|False
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      Unique identifier that references the migration task.

      

    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: list_created_artifacts(**kwargs)

    

    Lists the created artifacts attached to a given migration task in an update stream. This API has the following traits:

     

     
    * Gets the list of the created artifacts while migration is taking place. 
     
    * Shows the artifacts created by the migration tool that was associated by the ``AssociateCreatedArtifact`` API.  
     
    * Lists created artifacts in a paginated interface.  
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListCreatedArtifacts>`_    


    **Request Syntax** 
    ::

      response = client.list_created_artifacts(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          NextToken='string',
          MaxResults=123
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      Unique identifier that references the migration task.

      

    
    :type NextToken: string
    :param NextToken: 

      If a ``NextToken`` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in ``NextToken`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of results to be returned per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'CreatedArtifactList': [
                {
                    'Name': 'string',
                    'Description': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* 

          If there are more created artifacts than the max result, return the next token to be passed to the next call as a bookmark of where to start from.

          
        

        - **CreatedArtifactList** *(list) --* 

          List of created artifacts up to the maximum number of results specified in the request.

          
          

          - *(dict) --* 

            An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance, RDS instance, etc.).

            
            

            - **Name** *(string) --* 

              An ARN that uniquely identifies the result of a migration task.

              
            

            - **Description** *(string) --* 

              A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.

              
        
      
    

  .. py:method:: list_discovered_resources(**kwargs)

    

    Lists discovered resources associated with the given ``MigrationTask`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListDiscoveredResources>`_    


    **Request Syntax** 
    ::

      response = client.list_discovered_resources(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          NextToken='string',
          MaxResults=123
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream.

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      The name of the MigrationTask.

      

    
    :type NextToken: string
    :param NextToken: 

      If a ``NextToken`` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in ``NextToken`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results returned per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'DiscoveredResourceList': [
                {
                    'ConfigurationId': 'string',
                    'Description': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* 

          If there are more discovered resources than the max result, return the next token to be passed to the next call as a bookmark of where to start from.

          
        

        - **DiscoveredResourceList** *(list) --* 

          Returned list of discovered resources associated with the given MigrationTask.

          
          

          - *(dict) --* 

            Object representing the on-premises resource being migrated.

            
            

            - **ConfigurationId** *(string) --* 

              The configurationId in ADS that uniquely identifies the on-premise resource.

              
            

            - **Description** *(string) --* 

              A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.

              
        
      
    

  .. py:method:: list_migration_tasks(**kwargs)

    

    Lists all, or filtered by resource name, migration tasks associated with the user account making this call. This API has the following traits:

     

     
    * Can show a summary list of the most recent migration tasks. 
     
    * Can show a summary list of migration tasks associated with a given discovered resource. 
     
    * Lists migration tasks in a paginated interface. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListMigrationTasks>`_    


    **Request Syntax** 
    ::

      response = client.list_migration_tasks(
          NextToken='string',
          MaxResults=123,
          ResourceName='string'
      )
    :type NextToken: string
    :param NextToken: 

      If a ``NextToken`` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in ``NextToken`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Value to specify how many results are returned per page.

      

    
    :type ResourceName: string
    :param ResourceName: 

      Filter migration tasks by discovered resource name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'MigrationTaskSummaryList': [
                {
                    'ProgressUpdateStream': 'string',
                    'MigrationTaskName': 'string',
                    'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
                    'ProgressPercent': 123,
                    'StatusDetail': 'string',
                    'UpdateDateTime': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* 

          If there are more migration tasks than the max result, return the next token to be passed to the next call as a bookmark of where to start from.

          
        

        - **MigrationTaskSummaryList** *(list) --* 

          Lists the migration task's summary which includes: ``MigrationTaskName`` , ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and the ``UpdateDateTime`` for each task.

          
          

          - *(dict) --* 

            MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.

            
            

            - **ProgressUpdateStream** *(string) --* 

              An AWS resource used for access control. It should uniquely identify the migration tool as it is used for all updates made by the tool.

              
            

            - **MigrationTaskName** *(string) --* 

              Unique identifier that references the migration task.

              
            

            - **Status** *(string) --* 

              Status of the task.

              
            

            - **ProgressPercent** *(integer) --* 

              

              
            

            - **StatusDetail** *(string) --* 

              Detail information of what is being done within the overall status state.

              
            

            - **UpdateDateTime** *(datetime) --* 

              The timestamp when the task was gathered.

              
        
      
    

  .. py:method:: list_progress_update_streams(**kwargs)

    

    Lists progress update streams associated with the user account making this call.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams>`_    


    **Request Syntax** 
    ::

      response = client.list_progress_update_streams(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      If a ``NextToken`` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in ``NextToken`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Filter to limit the maximum number of results to list per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProgressUpdateStreamSummaryList': [
                {
                    'ProgressUpdateStreamName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProgressUpdateStreamSummaryList** *(list) --* 

          List of progress update streams up to the max number of results passed in the input.

          
          

          - *(dict) --* 

            Summary of the AWS resource used for access control that is implicitly linked to your AWS account.

            
            

            - **ProgressUpdateStreamName** *(string) --* 

              The name of the ProgressUpdateStream. 

              
        
      
        

        - **NextToken** *(string) --* 

          If there are more streams created than the max result, return the next token to be passed to the next call as a bookmark of where to start from.

          
    

  .. py:method:: notify_application_state(**kwargs)

    

    Sets the migration state of an application. For a given application identified by the value passed to ``ApplicationId`` , its status is set or updated by passing one of three values to ``Status`` : ``NOT_STARTED | IN_PROGRESS | COMPLETED`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/NotifyApplicationState>`_    


    **Request Syntax** 
    ::

      response = client.notify_application_state(
          ApplicationId='string',
          Status='NOT_STARTED'|'IN_PROGRESS'|'COMPLETED',
          DryRun=True|False
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** 

      The configurationId in ADS that uniquely identifies the grouped application.

      

    
    :type Status: string
    :param Status: **[REQUIRED]** 

      Status of the application - Not Started, In-Progress, Complete.

      

    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: notify_migration_task_state(**kwargs)

    

    Notifies Migration Hub of the current status, progress, or other detail regarding a migration task. This API has the following traits:

     

     
    * Migration tools will call the ``NotifyMigrationTaskState`` API to share the latest progress and status. 
     
    * ``MigrationTaskName`` is used for addressing updates to the correct target. 
     
    * ``ProgressUpdateStream`` is used for access control and to provide a namespace for each migration tool. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState>`_    


    **Request Syntax** 
    ::

      response = client.notify_migration_task_state(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          Task={
              'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
              'StatusDetail': 'string',
              'ProgressPercent': 123
          },
          UpdateDateTime=datetime(2015, 1, 1),
          NextUpdateSeconds=123,
          DryRun=True|False
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      Unique identifier that references the migration task.

      

    
    :type Task: dict
    :param Task: **[REQUIRED]** 

      Information about the task's progress and status.

      

    
      - **Status** *(string) --* **[REQUIRED]** 

        Status of the task - Not Started, In-Progress, Complete.

        

      
      - **StatusDetail** *(string) --* 

        Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.

        

      
      - **ProgressPercent** *(integer) --* 

        Indication of the percentage completion of the task.

        

      
    
    :type UpdateDateTime: datetime
    :param UpdateDateTime: **[REQUIRED]** 

      The timestamp when the task was gathered.

      

    
    :type NextUpdateSeconds: integer
    :param NextUpdateSeconds: **[REQUIRED]** 

      Number of seconds after the UpdateDateTime within which the Migration Hub can expect an update. If Migration Hub does not receive an update within the specified interval, then the migration task will be considered stale.

      

    
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: put_resource_attributes(**kwargs)

    

    Provides identifying details of the resource being migrated so that it can be associated in the Application Discovery Service (ADS)'s repository. This association occurs asynchronously after ``PutResourceAttributes`` returns.

     

    .. warning::

       

      Keep in mind that subsequent calls to PutResourceAttributes will override previously stored attributes. For example, if it is first called with a MAC address, but later, it is desired to *add* an IP address, it will then be required to call it with *both* the IP and MAC addresses to prevent overiding the MAC address.

       

     

    .. note::

       

      Because this is an asynchronous call, it will always return 200, whether an association occurs or not. To confirm if an association was found based on the provided details, call ``ListAssociatedResource`` .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/PutResourceAttributes>`_    


    **Request Syntax** 
    ::

      response = client.put_resource_attributes(
          ProgressUpdateStream='string',
          MigrationTaskName='string',
          ResourceAttributeList=[
              {
                  'Type': 'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MAC_ADDRESS'|'FQDN'|'VM_MANAGER_ID'|'VM_MANAGED_OBJECT_REFERENCE'|'VM_NAME'|'VM_PATH'|'BIOS_ID'|'MOTHERBOARD_SERIAL_NUMBER'|'LABEL',
                  'Value': 'string'
              },
          ],
          DryRun=True|False
      )
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: **[REQUIRED]** 

      The name of the ProgressUpdateStream. 

      

    
    :type MigrationTaskName: string
    :param MigrationTaskName: **[REQUIRED]** 

      Unique identifier that references the migration task.

      

    
    :type ResourceAttributeList: list
    :param ResourceAttributeList: **[REQUIRED]** 

      Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service (ADS)'s repository.

      

    
      - *(dict) --* 

        Attribute associated with a resource.

        

      
        - **Type** *(string) --* **[REQUIRED]** 

          Type of resource.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          Value of the resource type.

          

        
      
  
    :type DryRun: boolean
    :param DryRun: 

      Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

==========
Paginators
==========


The available paginators are:
