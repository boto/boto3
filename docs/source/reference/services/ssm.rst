

***
SSM
***

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: SSM.Client

  A low-level client representing Amazon Simple Systems Manager (SSM)::

    
    import boto3
    
    client = boto3.client('ssm')

  
  These are the available methods:
  
  *   :py:meth:`~SSM.Client.add_tags_to_resource`

  
  *   :py:meth:`~SSM.Client.can_paginate`

  
  *   :py:meth:`~SSM.Client.cancel_command`

  
  *   :py:meth:`~SSM.Client.create_activation`

  
  *   :py:meth:`~SSM.Client.create_association`

  
  *   :py:meth:`~SSM.Client.create_association_batch`

  
  *   :py:meth:`~SSM.Client.create_document`

  
  *   :py:meth:`~SSM.Client.create_maintenance_window`

  
  *   :py:meth:`~SSM.Client.create_patch_baseline`

  
  *   :py:meth:`~SSM.Client.create_resource_data_sync`

  
  *   :py:meth:`~SSM.Client.delete_activation`

  
  *   :py:meth:`~SSM.Client.delete_association`

  
  *   :py:meth:`~SSM.Client.delete_document`

  
  *   :py:meth:`~SSM.Client.delete_maintenance_window`

  
  *   :py:meth:`~SSM.Client.delete_parameter`

  
  *   :py:meth:`~SSM.Client.delete_parameters`

  
  *   :py:meth:`~SSM.Client.delete_patch_baseline`

  
  *   :py:meth:`~SSM.Client.delete_resource_data_sync`

  
  *   :py:meth:`~SSM.Client.deregister_managed_instance`

  
  *   :py:meth:`~SSM.Client.deregister_patch_baseline_for_patch_group`

  
  *   :py:meth:`~SSM.Client.deregister_target_from_maintenance_window`

  
  *   :py:meth:`~SSM.Client.deregister_task_from_maintenance_window`

  
  *   :py:meth:`~SSM.Client.describe_activations`

  
  *   :py:meth:`~SSM.Client.describe_association`

  
  *   :py:meth:`~SSM.Client.describe_automation_executions`

  
  *   :py:meth:`~SSM.Client.describe_automation_step_executions`

  
  *   :py:meth:`~SSM.Client.describe_available_patches`

  
  *   :py:meth:`~SSM.Client.describe_document`

  
  *   :py:meth:`~SSM.Client.describe_document_permission`

  
  *   :py:meth:`~SSM.Client.describe_effective_instance_associations`

  
  *   :py:meth:`~SSM.Client.describe_effective_patches_for_patch_baseline`

  
  *   :py:meth:`~SSM.Client.describe_instance_associations_status`

  
  *   :py:meth:`~SSM.Client.describe_instance_information`

  
  *   :py:meth:`~SSM.Client.describe_instance_patch_states`

  
  *   :py:meth:`~SSM.Client.describe_instance_patch_states_for_patch_group`

  
  *   :py:meth:`~SSM.Client.describe_instance_patches`

  
  *   :py:meth:`~SSM.Client.describe_maintenance_window_execution_task_invocations`

  
  *   :py:meth:`~SSM.Client.describe_maintenance_window_execution_tasks`

  
  *   :py:meth:`~SSM.Client.describe_maintenance_window_executions`

  
  *   :py:meth:`~SSM.Client.describe_maintenance_window_targets`

  
  *   :py:meth:`~SSM.Client.describe_maintenance_window_tasks`

  
  *   :py:meth:`~SSM.Client.describe_maintenance_windows`

  
  *   :py:meth:`~SSM.Client.describe_parameters`

  
  *   :py:meth:`~SSM.Client.describe_patch_baselines`

  
  *   :py:meth:`~SSM.Client.describe_patch_group_state`

  
  *   :py:meth:`~SSM.Client.describe_patch_groups`

  
  *   :py:meth:`~SSM.Client.generate_presigned_url`

  
  *   :py:meth:`~SSM.Client.get_automation_execution`

  
  *   :py:meth:`~SSM.Client.get_command_invocation`

  
  *   :py:meth:`~SSM.Client.get_default_patch_baseline`

  
  *   :py:meth:`~SSM.Client.get_deployable_patch_snapshot_for_instance`

  
  *   :py:meth:`~SSM.Client.get_document`

  
  *   :py:meth:`~SSM.Client.get_inventory`

  
  *   :py:meth:`~SSM.Client.get_inventory_schema`

  
  *   :py:meth:`~SSM.Client.get_maintenance_window`

  
  *   :py:meth:`~SSM.Client.get_maintenance_window_execution`

  
  *   :py:meth:`~SSM.Client.get_maintenance_window_execution_task`

  
  *   :py:meth:`~SSM.Client.get_maintenance_window_execution_task_invocation`

  
  *   :py:meth:`~SSM.Client.get_maintenance_window_task`

  
  *   :py:meth:`~SSM.Client.get_paginator`

  
  *   :py:meth:`~SSM.Client.get_parameter`

  
  *   :py:meth:`~SSM.Client.get_parameter_history`

  
  *   :py:meth:`~SSM.Client.get_parameters`

  
  *   :py:meth:`~SSM.Client.get_parameters_by_path`

  
  *   :py:meth:`~SSM.Client.get_patch_baseline`

  
  *   :py:meth:`~SSM.Client.get_patch_baseline_for_patch_group`

  
  *   :py:meth:`~SSM.Client.get_waiter`

  
  *   :py:meth:`~SSM.Client.list_association_versions`

  
  *   :py:meth:`~SSM.Client.list_associations`

  
  *   :py:meth:`~SSM.Client.list_command_invocations`

  
  *   :py:meth:`~SSM.Client.list_commands`

  
  *   :py:meth:`~SSM.Client.list_compliance_items`

  
  *   :py:meth:`~SSM.Client.list_compliance_summaries`

  
  *   :py:meth:`~SSM.Client.list_document_versions`

  
  *   :py:meth:`~SSM.Client.list_documents`

  
  *   :py:meth:`~SSM.Client.list_inventory_entries`

  
  *   :py:meth:`~SSM.Client.list_resource_compliance_summaries`

  
  *   :py:meth:`~SSM.Client.list_resource_data_sync`

  
  *   :py:meth:`~SSM.Client.list_tags_for_resource`

  
  *   :py:meth:`~SSM.Client.modify_document_permission`

  
  *   :py:meth:`~SSM.Client.put_compliance_items`

  
  *   :py:meth:`~SSM.Client.put_inventory`

  
  *   :py:meth:`~SSM.Client.put_parameter`

  
  *   :py:meth:`~SSM.Client.register_default_patch_baseline`

  
  *   :py:meth:`~SSM.Client.register_patch_baseline_for_patch_group`

  
  *   :py:meth:`~SSM.Client.register_target_with_maintenance_window`

  
  *   :py:meth:`~SSM.Client.register_task_with_maintenance_window`

  
  *   :py:meth:`~SSM.Client.remove_tags_from_resource`

  
  *   :py:meth:`~SSM.Client.send_automation_signal`

  
  *   :py:meth:`~SSM.Client.send_command`

  
  *   :py:meth:`~SSM.Client.start_automation_execution`

  
  *   :py:meth:`~SSM.Client.stop_automation_execution`

  
  *   :py:meth:`~SSM.Client.update_association`

  
  *   :py:meth:`~SSM.Client.update_association_status`

  
  *   :py:meth:`~SSM.Client.update_document`

  
  *   :py:meth:`~SSM.Client.update_document_default_version`

  
  *   :py:meth:`~SSM.Client.update_maintenance_window`

  
  *   :py:meth:`~SSM.Client.update_maintenance_window_target`

  
  *   :py:meth:`~SSM.Client.update_maintenance_window_task`

  
  *   :py:meth:`~SSM.Client.update_managed_instance_role`

  
  *   :py:meth:`~SSM.Client.update_patch_baseline`

  

  .. py:method:: add_tags_to_resource(**kwargs)

    

    Adds or overwrites one or more tags for the specified resource. Tags are metadata that you can assign to your documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account's managed instances that helps you track each instance's owner and stack level. For example: Key=Owner and Value=DbAdmin, SysAdmin, or Dev. Or Key=Stack and Value=Production, Pre-Production, or Test.

     

    Each resource can have a maximum of 10 tags. 

     

    We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags don't have any semantic meaning to Amazon EC2 and are interpreted strictly as a string of characters. 

     

    For more information about tags, see `Tagging Your Amazon EC2 Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon EC2 User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/AddTagsToResource>`_    


    **Request Syntax** 
    ::

      response = client.add_tags_to_resource(
          ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline',
          ResourceId='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      Specifies the type of resource you are tagging.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource ID you want to tag.

       

      For the ManagedInstance, MaintenanceWindow, and PatchBaseline values, use the ID of the resource, such as mw-01234361858c9b57b for a Maintenance Window.

       

      For the Document and Parameter values, use the name of the resource.

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      One or more tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 

      

    
      - *(dict) --* 

        Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The name of the tag.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value of the tag.

          

        
      
  
    
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


  .. py:method:: cancel_command(**kwargs)

    

    Attempts to cancel the command specified by the Command ID. There is no guarantee that the command will be terminated and the underlying process stopped.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CancelCommand>`_    


    **Request Syntax** 
    ::

      response = client.cancel_command(
          CommandId='string',
          InstanceIds=[
              'string',
          ]
      )
    :type CommandId: string
    :param CommandId: **[REQUIRED]** 

      The ID of the command you want to cancel.

      

    
    :type InstanceIds: list
    :param InstanceIds: 

      (Optional) A list of instance IDs on which you want to cancel the command. If not provided, the command is canceled on every instance on which it was requested.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Whether or not the command was successfully canceled. There is no guarantee that a request can be canceled.

        
    

  .. py:method:: create_activation(**kwargs)

    

    Registers your on-premises server or virtual machine with Amazon EC2 so that you can manage these resources using Run Command. An on-premises server or virtual machine that has been registered with EC2 is called a managed instance. For more information about activations, see `Setting Up Systems Manager in Hybrid Environments <http://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateActivation>`_    


    **Request Syntax** 
    ::

      response = client.create_activation(
          Description='string',
          DefaultInstanceName='string',
          IamRole='string',
          RegistrationLimit=123,
          ExpirationDate=datetime(2015, 1, 1)
      )
    :type Description: string
    :param Description: 

      A userdefined description of the resource that you want to register with Amazon EC2. 

      

    
    :type DefaultInstanceName: string
    :param DefaultInstanceName: 

      The name of the registered, managed instance as it will appear in the Amazon EC2 console or when you use the AWS command line tools to list EC2 resources.

      

    
    :type IamRole: string
    :param IamRole: **[REQUIRED]** 

      The Amazon Identity and Access Management (IAM) role that you want to assign to the managed instance. 

      

    
    :type RegistrationLimit: integer
    :param RegistrationLimit: 

      Specify the maximum number of managed instances you want to register. The default value is 1 instance.

      

    
    :type ExpirationDate: datetime
    :param ExpirationDate: 

      The date by which this activation request should expire. The default value is 24 hours.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ActivationId': 'string',
            'ActivationCode': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ActivationId** *(string) --* 

          The ID number generated by the system when it processed the activation. The activation ID functions like a user name.

          
        

        - **ActivationCode** *(string) --* 

          The code the system generates when it processes the activation. The activation code functions like a password to validate the activation ID. 

          
    

  .. py:method:: create_association(**kwargs)

    

    Associates the specified Systems Manager document with the specified instances or targets.

     

    When you associate a document with one or more instances using instance IDs or tags, the SSM Agent running on the instance processes the document and configures the instance as specified.

     

    If you associate a document with an instance that already has an associated document, the system throws the AssociationAlreadyExists exception.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateAssociation>`_    


    **Request Syntax** 
    ::

      response = client.create_association(
          Name='string',
          DocumentVersion='string',
          InstanceId='string',
          Parameters={
              'string': [
                  'string',
              ]
          },
          Targets=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          ScheduleExpression='string',
          OutputLocation={
              'S3Location': {
                  'OutputS3Region': 'string',
                  'OutputS3BucketName': 'string',
                  'OutputS3KeyPrefix': 'string'
              }
          },
          AssociationName='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the Systems Manager document.

      

    
    :type DocumentVersion: string
    :param DocumentVersion: 

      The document version you want to associate with the target(s). Can be a specific version or the default version.

      

    
    :type InstanceId: string
    :param InstanceId: 

      The instance ID.

      

    
    :type Parameters: dict
    :param Parameters: 

      The parameters for the documents runtime configuration. 

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(string) --* 

          
      
  

    :type Targets: list
    :param Targets: 

      The targets (either instances or tags) for the association.

      

    
      - *(dict) --* 

        An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

         

        

        

      
        - **Key** *(string) --* 

          User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
        - **Values** *(list) --* 

          User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
          - *(string) --* 

          
      
      
  
    :type ScheduleExpression: string
    :param ScheduleExpression: 

      A cron expression when the association will be applied to the target(s).

      

    
    :type OutputLocation: dict
    :param OutputLocation: 

      An Amazon S3 bucket where you want to store the output details of the request.

      

    
      - **S3Location** *(dict) --* 

        An Amazon S3 bucket where you want to store the results of this request.

        

      
        - **OutputS3Region** *(string) --* 

          (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

          

        
        - **OutputS3BucketName** *(string) --* 

          The name of the Amazon S3 bucket.

          

        
        - **OutputS3KeyPrefix** *(string) --* 

          The Amazon S3 bucket subfolder.

          

        
      
    
    :type AssociationName: string
    :param AssociationName: 

      Specify a descriptive name for the association.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociationDescription': {
                'Name': 'string',
                'InstanceId': 'string',
                'AssociationVersion': 'string',
                'Date': datetime(2015, 1, 1),
                'LastUpdateAssociationDate': datetime(2015, 1, 1),
                'Status': {
                    'Date': datetime(2015, 1, 1),
                    'Name': 'Pending'|'Success'|'Failed',
                    'Message': 'string',
                    'AdditionalInfo': 'string'
                },
                'Overview': {
                    'Status': 'string',
                    'DetailedStatus': 'string',
                    'AssociationStatusAggregatedCount': {
                        'string': 123
                    }
                },
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'AssociationId': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ScheduleExpression': 'string',
                'OutputLocation': {
                    'S3Location': {
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string'
                    }
                },
                'LastExecutionDate': datetime(2015, 1, 1),
                'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
                'AssociationName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AssociationDescription** *(dict) --* 

          Information about the association.

          
          

          - **Name** *(string) --* 

            The name of the Systems Manager document.

            
          

          - **InstanceId** *(string) --* 

            The ID of the instance.

            
          

          - **AssociationVersion** *(string) --* 

            The association version.

            
          

          - **Date** *(datetime) --* 

            The date when the association was made.

            
          

          - **LastUpdateAssociationDate** *(datetime) --* 

            The date when the association was last updated.

            
          

          - **Status** *(dict) --* 

            The association status.

            
            

            - **Date** *(datetime) --* 

              The date when the status changed.

              
            

            - **Name** *(string) --* 

              The status.

              
            

            - **Message** *(string) --* 

              The reason for the status.

              
            

            - **AdditionalInfo** *(string) --* 

              A user-defined string.

              
        
          

          - **Overview** *(dict) --* 

            Information about the association.

            
            

            - **Status** *(string) --* 

              The status of the association. Status can be: Pending, Success, or Failed.

              
            

            - **DetailedStatus** *(string) --* 

              A detailed status of the association.

              
            

            - **AssociationStatusAggregatedCount** *(dict) --* 

              Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

              
              

              - *(string) --* 
                

                - *(integer) --* 
          
        
        
          

          - **DocumentVersion** *(string) --* 

            The document version.

            
          

          - **Parameters** *(dict) --* 

            A description of the parameters for a document. 

            
            

            - *(string) --* 
              

              - *(list) --* 
                

                - *(string) --* 
            
        
      
          

          - **AssociationId** *(string) --* 

            The association ID.

            
          

          - **Targets** *(list) --* 

            The instances targeted by the request. 

            
            

            - *(dict) --* 

              An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

               

              

              
              

              - **Key** *(string) --* 

                User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
              

              - **Values** *(list) --* 

                User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
                

                - *(string) --* 
            
          
        
          

          - **ScheduleExpression** *(string) --* 

            A cron expression that specifies a schedule when the association runs.

            
          

          - **OutputLocation** *(dict) --* 

            An Amazon S3 bucket where you want to store the output details of the request.

            
            

            - **S3Location** *(dict) --* 

              An Amazon S3 bucket where you want to store the results of this request.

              
              

              - **OutputS3Region** *(string) --* 

                (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                
              

              - **OutputS3BucketName** *(string) --* 

                The name of the Amazon S3 bucket.

                
              

              - **OutputS3KeyPrefix** *(string) --* 

                The Amazon S3 bucket subfolder.

                
          
        
          

          - **LastExecutionDate** *(datetime) --* 

            The date on which the association was last run.

            
          

          - **LastSuccessfulExecutionDate** *(datetime) --* 

            The last date on which the association was successfully run.

            
          

          - **AssociationName** *(string) --* 

            The association name.

            
      
    

  .. py:method:: create_association_batch(**kwargs)

    

    Associates the specified Systems Manager document with the specified instances or targets.

     

    When you associate a document with one or more instances using instance IDs or tags, the SSM Agent running on the instance processes the document and configures the instance as specified.

     

    If you associate a document with an instance that already has an associated document, the system throws the AssociationAlreadyExists exception.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateAssociationBatch>`_    


    **Request Syntax** 
    ::

      response = client.create_association_batch(
          Entries=[
              {
                  'Name': 'string',
                  'InstanceId': 'string',
                  'Parameters': {
                      'string': [
                          'string',
                      ]
                  },
                  'DocumentVersion': 'string',
                  'Targets': [
                      {
                          'Key': 'string',
                          'Values': [
                              'string',
                          ]
                      },
                  ],
                  'ScheduleExpression': 'string',
                  'OutputLocation': {
                      'S3Location': {
                          'OutputS3Region': 'string',
                          'OutputS3BucketName': 'string',
                          'OutputS3KeyPrefix': 'string'
                      }
                  },
                  'AssociationName': 'string'
              },
          ]
      )
    :type Entries: list
    :param Entries: **[REQUIRED]** 

      One or more associations.

      

    
      - *(dict) --* 

        Describes the association of a Systems Manager document and an instance.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the configuration document. 

          

        
        - **InstanceId** *(string) --* 

          The ID of the instance. 

          

        
        - **Parameters** *(dict) --* 

          A description of the parameters for a document. 

          

        
          - *(string) --* 

          
            - *(list) --* 

            
              - *(string) --* 

              
          
      
    
        - **DocumentVersion** *(string) --* 

          The document version.

          

        
        - **Targets** *(list) --* 

          The instances targeted by the request.

          

        
          - *(dict) --* 

            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

             

            

            

          
            - **Key** *(string) --* 

              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

              

            
            - **Values** *(list) --* 

              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

              

            
              - *(string) --* 

              
          
          
      
        - **ScheduleExpression** *(string) --* 

          A cron expression that specifies a schedule when the association runs.

          

        
        - **OutputLocation** *(dict) --* 

          An Amazon S3 bucket where you want to store the results of this request.

          

        
          - **S3Location** *(dict) --* 

            An Amazon S3 bucket where you want to store the results of this request.

            

          
            - **OutputS3Region** *(string) --* 

              (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

              

            
            - **OutputS3BucketName** *(string) --* 

              The name of the Amazon S3 bucket.

              

            
            - **OutputS3KeyPrefix** *(string) --* 

              The Amazon S3 bucket subfolder.

              

            
          
        
        - **AssociationName** *(string) --* 

          Specify a descriptive name for the association.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Successful': [
                {
                    'Name': 'string',
                    'InstanceId': 'string',
                    'AssociationVersion': 'string',
                    'Date': datetime(2015, 1, 1),
                    'LastUpdateAssociationDate': datetime(2015, 1, 1),
                    'Status': {
                        'Date': datetime(2015, 1, 1),
                        'Name': 'Pending'|'Success'|'Failed',
                        'Message': 'string',
                        'AdditionalInfo': 'string'
                    },
                    'Overview': {
                        'Status': 'string',
                        'DetailedStatus': 'string',
                        'AssociationStatusAggregatedCount': {
                            'string': 123
                        }
                    },
                    'DocumentVersion': 'string',
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    },
                    'AssociationId': 'string',
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'ScheduleExpression': 'string',
                    'OutputLocation': {
                        'S3Location': {
                            'OutputS3Region': 'string',
                            'OutputS3BucketName': 'string',
                            'OutputS3KeyPrefix': 'string'
                        }
                    },
                    'LastExecutionDate': datetime(2015, 1, 1),
                    'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
                    'AssociationName': 'string'
                },
            ],
            'Failed': [
                {
                    'Entry': {
                        'Name': 'string',
                        'InstanceId': 'string',
                        'Parameters': {
                            'string': [
                                'string',
                            ]
                        },
                        'DocumentVersion': 'string',
                        'Targets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ],
                        'ScheduleExpression': 'string',
                        'OutputLocation': {
                            'S3Location': {
                                'OutputS3Region': 'string',
                                'OutputS3BucketName': 'string',
                                'OutputS3KeyPrefix': 'string'
                            }
                        },
                        'AssociationName': 'string'
                    },
                    'Message': 'string',
                    'Fault': 'Client'|'Server'|'Unknown'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Successful** *(list) --* 

          Information about the associations that succeeded.

          
          

          - *(dict) --* 

            Describes the parameters for a document.

            
            

            - **Name** *(string) --* 

              The name of the Systems Manager document.

              
            

            - **InstanceId** *(string) --* 

              The ID of the instance.

              
            

            - **AssociationVersion** *(string) --* 

              The association version.

              
            

            - **Date** *(datetime) --* 

              The date when the association was made.

              
            

            - **LastUpdateAssociationDate** *(datetime) --* 

              The date when the association was last updated.

              
            

            - **Status** *(dict) --* 

              The association status.

              
              

              - **Date** *(datetime) --* 

                The date when the status changed.

                
              

              - **Name** *(string) --* 

                The status.

                
              

              - **Message** *(string) --* 

                The reason for the status.

                
              

              - **AdditionalInfo** *(string) --* 

                A user-defined string.

                
          
            

            - **Overview** *(dict) --* 

              Information about the association.

              
              

              - **Status** *(string) --* 

                The status of the association. Status can be: Pending, Success, or Failed.

                
              

              - **DetailedStatus** *(string) --* 

                A detailed status of the association.

                
              

              - **AssociationStatusAggregatedCount** *(dict) --* 

                Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

                
                

                - *(string) --* 
                  

                  - *(integer) --* 
            
          
          
            

            - **DocumentVersion** *(string) --* 

              The document version.

              
            

            - **Parameters** *(dict) --* 

              A description of the parameters for a document. 

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
            

            - **AssociationId** *(string) --* 

              The association ID.

              
            

            - **Targets** *(list) --* 

              The instances targeted by the request. 

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **ScheduleExpression** *(string) --* 

              A cron expression that specifies a schedule when the association runs.

              
            

            - **OutputLocation** *(dict) --* 

              An Amazon S3 bucket where you want to store the output details of the request.

              
              

              - **S3Location** *(dict) --* 

                An Amazon S3 bucket where you want to store the results of this request.

                
                

                - **OutputS3Region** *(string) --* 

                  (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                  
                

                - **OutputS3BucketName** *(string) --* 

                  The name of the Amazon S3 bucket.

                  
                

                - **OutputS3KeyPrefix** *(string) --* 

                  The Amazon S3 bucket subfolder.

                  
            
          
            

            - **LastExecutionDate** *(datetime) --* 

              The date on which the association was last run.

              
            

            - **LastSuccessfulExecutionDate** *(datetime) --* 

              The last date on which the association was successfully run.

              
            

            - **AssociationName** *(string) --* 

              The association name.

              
        
      
        

        - **Failed** *(list) --* 

          Information about the associations that failed.

          
          

          - *(dict) --* 

            Describes a failed association.

            
            

            - **Entry** *(dict) --* 

              The association.

              
              

              - **Name** *(string) --* 

                The name of the configuration document. 

                
              

              - **InstanceId** *(string) --* 

                The ID of the instance. 

                
              

              - **Parameters** *(dict) --* 

                A description of the parameters for a document. 

                
                

                - *(string) --* 
                  

                  - *(list) --* 
                    

                    - *(string) --* 
                
            
          
              

              - **DocumentVersion** *(string) --* 

                The document version.

                
              

              - **Targets** *(list) --* 

                The instances targeted by the request.

                
                

                - *(dict) --* 

                  An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                   

                  

                  
                  

                  - **Key** *(string) --* 

                    User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                    
                  

                  - **Values** *(list) --* 

                    User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                    
                    

                    - *(string) --* 
                
              
            
              

              - **ScheduleExpression** *(string) --* 

                A cron expression that specifies a schedule when the association runs.

                
              

              - **OutputLocation** *(dict) --* 

                An Amazon S3 bucket where you want to store the results of this request.

                
                

                - **S3Location** *(dict) --* 

                  An Amazon S3 bucket where you want to store the results of this request.

                  
                  

                  - **OutputS3Region** *(string) --* 

                    (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                    
                  

                  - **OutputS3BucketName** *(string) --* 

                    The name of the Amazon S3 bucket.

                    
                  

                  - **OutputS3KeyPrefix** *(string) --* 

                    The Amazon S3 bucket subfolder.

                    
              
            
              

              - **AssociationName** *(string) --* 

                Specify a descriptive name for the association.

                
          
            

            - **Message** *(string) --* 

              A description of the failure.

              
            

            - **Fault** *(string) --* 

              The source of the failure.

              
        
      
    

  .. py:method:: create_document(**kwargs)

    

    Creates a Systems Manager document.

     

    After you create a document, you can use CreateAssociation to associate it with one or more running instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateDocument>`_    


    **Request Syntax** 
    ::

      response = client.create_document(
          Content='string',
          Name='string',
          DocumentType='Command'|'Policy'|'Automation',
          DocumentFormat='YAML'|'JSON',
          TargetType='string'
      )
    :type Content: string
    :param Content: **[REQUIRED]** 

      A valid JSON or YAML string.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      A name for the Systems Manager document.

      

    
    :type DocumentType: string
    :param DocumentType: 

      The type of document to create. Valid document types include: Policy, Automation, and Command.

      

    
    :type DocumentFormat: string
    :param DocumentFormat: 

      Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.

      

    
    :type TargetType: string
    :param TargetType: 

      Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: /AWS::EC2::Instance. If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DocumentDescription': {
                'Sha1': 'string',
                'Hash': 'string',
                'HashType': 'Sha256'|'Sha1',
                'Name': 'string',
                'Owner': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'Status': 'Creating'|'Active'|'Updating'|'Deleting',
                'DocumentVersion': 'string',
                'Description': 'string',
                'Parameters': [
                    {
                        'Name': 'string',
                        'Type': 'String'|'StringList',
                        'Description': 'string',
                        'DefaultValue': 'string'
                    },
                ],
                'PlatformTypes': [
                    'Windows'|'Linux',
                ],
                'DocumentType': 'Command'|'Policy'|'Automation',
                'SchemaVersion': 'string',
                'LatestVersion': 'string',
                'DefaultVersion': 'string',
                'DocumentFormat': 'YAML'|'JSON',
                'TargetType': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DocumentDescription** *(dict) --* 

          Information about the Systems Manager document.

          
          

          - **Sha1** *(string) --* 

            The SHA1 hash of the document, which you can use for verification.

            
          

          - **Hash** *(string) --* 

            The Sha256 or Sha1 hash created by the system when the document was created. 

             

            .. note::

               

              Sha1 hashes have been deprecated.

               

            
          

          - **HashType** *(string) --* 

            Sha256 or Sha1.

             

            .. note::

               

              Sha1 hashes have been deprecated.

               

            
          

          - **Name** *(string) --* 

            The name of the Systems Manager document.

            
          

          - **Owner** *(string) --* 

            The AWS user account that created the document.

            
          

          - **CreatedDate** *(datetime) --* 

            The date when the document was created.

            
          

          - **Status** *(string) --* 

            The status of the Systems Manager document.

            
          

          - **DocumentVersion** *(string) --* 

            The document version.

            
          

          - **Description** *(string) --* 

            A description of the document. 

            
          

          - **Parameters** *(list) --* 

            A description of the parameters for a document.

            
            

            - *(dict) --* 

              Parameters specified in a System Manager document that execute on the server when the command is run. 

              
              

              - **Name** *(string) --* 

                The name of the parameter.

                
              

              - **Type** *(string) --* 

                The type of parameter. The type can be either String or StringList.

                
              

              - **Description** *(string) --* 

                A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.

                
              

              - **DefaultValue** *(string) --* 

                If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.

                
          
        
          

          - **PlatformTypes** *(list) --* 

            The list of OS platforms compatible with this Systems Manager document. 

            
            

            - *(string) --* 
        
          

          - **DocumentType** *(string) --* 

            The type of document. 

            
          

          - **SchemaVersion** *(string) --* 

            The schema version.

            
          

          - **LatestVersion** *(string) --* 

            The latest version of the document.

            
          

          - **DefaultVersion** *(string) --* 

            The default version.

            
          

          - **DocumentFormat** *(string) --* 

            The document format, either JSON or YAML.

            
          

          - **TargetType** *(string) --* 

            The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 

            
          

          - **Tags** *(list) --* 

            The tags, or metadata, that have been applied to the document.

            
            

            - *(dict) --* 

              Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.

              
              

              - **Key** *(string) --* 

                The name of the tag.

                
              

              - **Value** *(string) --* 

                The value of the tag.

                
          
        
      
    

  .. py:method:: create_maintenance_window(**kwargs)

    

    Creates a new Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateMaintenanceWindow>`_    


    **Request Syntax** 
    ::

      response = client.create_maintenance_window(
          Name='string',
          Description='string',
          Schedule='string',
          Duration=123,
          Cutoff=123,
          AllowUnassociatedTargets=True|False,
          ClientToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the Maintenance Window.

      

    
    :type Description: string
    :param Description: 

      An optional description for the Maintenance Window. We recommend specifying a description to help you organize your Maintenance Windows. 

      

    
    :type Schedule: string
    :param Schedule: **[REQUIRED]** 

      The schedule of the Maintenance Window in the form of a cron or rate expression.

      

    
    :type Duration: integer
    :param Duration: **[REQUIRED]** 

      The duration of the Maintenance Window in hours.

      

    
    :type Cutoff: integer
    :param Cutoff: **[REQUIRED]** 

      The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

      

    
    :type AllowUnassociatedTargets: boolean
    :param AllowUnassociatedTargets: **[REQUIRED]** 

      Enables a Maintenance Window task to execute on managed instances, even if you have not registered those instances as targets. If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the Maintenance Window 

       

      If you don't enable this option, then you must specify previously-registered targets when you register a task with the Maintenance Window. 

      

    
    :type ClientToken: string
    :param ClientToken: 

      User-provided idempotency token.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The ID of the created Maintenance Window.

          
    

  .. py:method:: create_patch_baseline(**kwargs)

    

    Creates a patch baseline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreatePatchBaseline>`_    


    **Request Syntax** 
    ::

      response = client.create_patch_baseline(
          OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX',
          Name='string',
          GlobalFilters={
              'PatchFilters': [
                  {
                      'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          },
          ApprovalRules={
              'PatchRules': [
                  {
                      'PatchFilterGroup': {
                          'PatchFilters': [
                              {
                                  'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                  'Values': [
                                      'string',
                                  ]
                              },
                          ]
                      },
                      'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                      'ApproveAfterDays': 123
                  },
              ]
          },
          ApprovedPatches=[
              'string',
          ],
          ApprovedPatchesComplianceLevel='CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
          RejectedPatches=[
              'string',
          ],
          Description='string',
          ClientToken='string'
      )
    :type OperatingSystem: string
    :param OperatingSystem: 

      Defines the operating system the patch baseline applies to. The Default value is WINDOWS.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the patch baseline.

      

    
    :type GlobalFilters: dict
    :param GlobalFilters: 

      A set of global filters used to exclude patches from the baseline.

      

    
      - **PatchFilters** *(list) --* **[REQUIRED]** 

        The set of patch filters that make up the group.

        

      
        - *(dict) --* 

          Defines a patch filter.

          

        
          - **Key** *(string) --* **[REQUIRED]** 

            The key for the filter (PRODUCT, CLASSIFICATION, MSRC_SEVERITY, PATCH_ID)

            

          
          - **Values** *(list) --* **[REQUIRED]** 

            The value for the filter key.

            

          
            - *(string) --* 

            
        
        
    
    
    :type ApprovalRules: dict
    :param ApprovalRules: 

      A set of rules used to include patches in the baseline.

      

    
      - **PatchRules** *(list) --* **[REQUIRED]** 

        The rules that make up the rule group.

        

      
        - *(dict) --* 

          Defines an approval rule for a patch baseline.

          

        
          - **PatchFilterGroup** *(dict) --* **[REQUIRED]** 

            The patch filter group that defines the criteria for the rule.

            

          
            - **PatchFilters** *(list) --* **[REQUIRED]** 

              The set of patch filters that make up the group.

              

            
              - *(dict) --* 

                Defines a patch filter.

                

              
                - **Key** *(string) --* **[REQUIRED]** 

                  The key for the filter (PRODUCT, CLASSIFICATION, MSRC_SEVERITY, PATCH_ID)

                  

                
                - **Values** *(list) --* **[REQUIRED]** 

                  The value for the filter key.

                  

                
                  - *(string) --* 

                  
              
              
          
          
          - **ComplianceLevel** *(string) --* 

            A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.

            

          
          - **ApproveAfterDays** *(integer) --* **[REQUIRED]** 

            The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline.

            

          
        
    
    
    :type ApprovedPatches: list
    :param ApprovedPatches: 

      A list of explicitly approved patches for the baseline.

      

    
      - *(string) --* 

      
  
    :type ApprovedPatchesComplianceLevel: string
    :param ApprovedPatchesComplianceLevel: 

      Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance severity levels include the following: CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL, UNSPECIFIED. The default value is UNSPECIFIED.

      

    
    :type RejectedPatches: list
    :param RejectedPatches: 

      A list of explicitly rejected patches for the baseline.

      

    
      - *(string) --* 

      
  
    :type Description: string
    :param Description: 

      A description of the patch baseline.

      

    
    :type ClientToken: string
    :param ClientToken: 

      User-provided idempotency token.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the created patch baseline.

          
    

  .. py:method:: create_resource_data_sync(**kwargs)

    

    Creates a resource data sync configuration to a single bucket in Amazon S3. This is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data to the Amazon S3 bucket. To check the status of the sync, use the  ListResourceDataSync .

     

    By default, data is not encrypted in Amazon S3. We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy. To view an example of a restrictive Amazon S3 bucket policy for Resource Data Sync, see `Configuring Resource Data Sync for Inventory <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html#sysman-inventory-datasync>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateResourceDataSync>`_    


    **Request Syntax** 
    ::

      response = client.create_resource_data_sync(
          SyncName='string',
          S3Destination={
              'BucketName': 'string',
              'Prefix': 'string',
              'SyncFormat': 'JsonSerDe',
              'Region': 'string',
              'AWSKMSKeyARN': 'string'
          }
      )
    :type SyncName: string
    :param SyncName: **[REQUIRED]** 

      A name for the configuration.

      

    
    :type S3Destination: dict
    :param S3Destination: **[REQUIRED]** 

      Amazon S3 configuration details for the sync.

      

    
      - **BucketName** *(string) --* **[REQUIRED]** 

        The name of the Amazon S3 bucket where the aggregated data is stored.

        

      
      - **Prefix** *(string) --* 

        An Amazon S3 prefix for the bucket.

        

      
      - **SyncFormat** *(string) --* **[REQUIRED]** 

        A supported sync format. The following format is currently supported: JsonSerDe

        

      
      - **Region** *(string) --* **[REQUIRED]** 

        The AWS Region with the Amazon S3 bucket targeted by the Resource Data Sync.

        

      
      - **AWSKMSKeyARN** *(string) --* 

        The ARN of an encryption key for a destination in Amazon S3. Must belong to the same region as the destination Amazon S3 bucket.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_activation(**kwargs)

    

    Deletes an activation. You are not required to delete an activation. If you delete an activation, you can no longer use it to register additional managed instances. Deleting an activation does not de-register managed instances. You must manually de-register managed instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteActivation>`_    


    **Request Syntax** 
    ::

      response = client.delete_activation(
          ActivationId='string'
      )
    :type ActivationId: string
    :param ActivationId: **[REQUIRED]** 

      The ID of the activation that you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_association(**kwargs)

    

    Disassociates the specified Systems Manager document from the specified instance.

     

    When you disassociate a document from an instance, it does not change the configuration of the instance. To change the configuration state of an instance after you disassociate a document, you must create a new document with the desired configuration and associate it with the instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteAssociation>`_    


    **Request Syntax** 
    ::

      response = client.delete_association(
          Name='string',
          InstanceId='string',
          AssociationId='string'
      )
    :type Name: string
    :param Name: 

      The name of the Systems Manager document.

      

    
    :type InstanceId: string
    :param InstanceId: 

      The ID of the instance.

      

    
    :type AssociationId: string
    :param AssociationId: 

      The association ID that you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_document(**kwargs)

    

    Deletes the Systems Manager document and all instance associations to the document.

     

    Before you delete the document, we recommend that you use  DeleteAssociation to disassociate all instances that are associated with the document.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteDocument>`_    


    **Request Syntax** 
    ::

      response = client.delete_document(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the document.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_maintenance_window(**kwargs)

    

    Deletes a Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteMaintenanceWindow>`_    


    **Request Syntax** 
    ::

      response = client.delete_maintenance_window(
          WindowId='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the Maintenance Window to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The ID of the deleted Maintenance Window.

          
    

  .. py:method:: delete_parameter(**kwargs)

    

    Delete a parameter from the system.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteParameter>`_    


    **Request Syntax** 
    ::

      response = client.delete_parameter(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the parameter to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_parameters(**kwargs)

    

    Delete a list of parameters. This API is used to delete parameters by using the Amazon EC2 console.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteParameters>`_    


    **Request Syntax** 
    ::

      response = client.delete_parameters(
          Names=[
              'string',
          ]
      )
    :type Names: list
    :param Names: **[REQUIRED]** 

      The names of the parameters to delete.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeletedParameters': [
                'string',
            ],
            'InvalidParameters': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DeletedParameters** *(list) --* 

          The names of the deleted parameters.

          
          

          - *(string) --* 
      
        

        - **InvalidParameters** *(list) --* 

          The names of parameters that weren't deleted because the parameters are not valid.

          
          

          - *(string) --* 
      
    

  .. py:method:: delete_patch_baseline(**kwargs)

    

    Deletes a patch baseline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeletePatchBaseline>`_    


    **Request Syntax** 
    ::

      response = client.delete_patch_baseline(
          BaselineId='string'
      )
    :type BaselineId: string
    :param BaselineId: **[REQUIRED]** 

      The ID of the patch baseline to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the deleted patch baseline.

          
    

  .. py:method:: delete_resource_data_sync(**kwargs)

    

    Deletes a Resource Data Sync configuration. After the configuration is deleted, changes to inventory data on managed instances are no longer synced with the target Amazon S3 bucket. Deleting a sync configuration does not delete data in the target Amazon S3 bucket.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteResourceDataSync>`_    


    **Request Syntax** 
    ::

      response = client.delete_resource_data_sync(
          SyncName='string'
      )
    :type SyncName: string
    :param SyncName: **[REQUIRED]** 

      The name of the configuration to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: deregister_managed_instance(**kwargs)

    

    Removes the server or virtual machine from the list of registered servers. You can reregister the instance again at any time. If you don't plan to use Run Command on the server, we suggest uninstalling the SSM Agent first.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeregisterManagedInstance>`_    


    **Request Syntax** 
    ::

      response = client.deregister_managed_instance(
          InstanceId='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The ID assigned to the managed instance when you registered it using the activation process. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: deregister_patch_baseline_for_patch_group(**kwargs)

    

    Removes a patch group from a patch baseline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup>`_    


    **Request Syntax** 
    ::

      response = client.deregister_patch_baseline_for_patch_group(
          BaselineId='string',
          PatchGroup='string'
      )
    :type BaselineId: string
    :param BaselineId: **[REQUIRED]** 

      The ID of the patch baseline to deregister the patch group from.

      

    
    :type PatchGroup: string
    :param PatchGroup: **[REQUIRED]** 

      The name of the patch group that should be deregistered from the patch baseline.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string',
            'PatchGroup': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the patch baseline the patch group was deregistered from.

          
        

        - **PatchGroup** *(string) --* 

          The name of the patch group deregistered from the patch baseline.

          
    

  .. py:method:: deregister_target_from_maintenance_window(**kwargs)

    

    Removes a target from a Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow>`_    


    **Request Syntax** 
    ::

      response = client.deregister_target_from_maintenance_window(
          WindowId='string',
          WindowTargetId='string',
          Safe=True|False
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the Maintenance Window the target should be removed from.

      

    
    :type WindowTargetId: string
    :param WindowTargetId: **[REQUIRED]** 

      The ID of the target definition to remove.

      

    
    :type Safe: boolean
    :param Safe: 

      The system checks if the target is being referenced by a task. If the target is being referenced, the system returns an error and does not deregister the target from the Maintenance Window.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string',
            'WindowTargetId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The ID of the Maintenance Window the target was removed from.

          
        

        - **WindowTargetId** *(string) --* 

          The ID of the removed target definition.

          
    

  .. py:method:: deregister_task_from_maintenance_window(**kwargs)

    

    Removes a task from a Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow>`_    


    **Request Syntax** 
    ::

      response = client.deregister_task_from_maintenance_window(
          WindowId='string',
          WindowTaskId='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the Maintenance Window the task should be removed from.

      

    
    :type WindowTaskId: string
    :param WindowTaskId: **[REQUIRED]** 

      The ID of the task to remove from the Maintenance Window.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string',
            'WindowTaskId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The ID of the Maintenance Window the task was removed from.

          
        

        - **WindowTaskId** *(string) --* 

          The ID of the task removed from the Maintenance Window.

          
    

  .. py:method:: describe_activations(**kwargs)

    

    Details about the activation, including: the date and time the activation was created, the expiration date, the IAM role assigned to the instances in the activation, and the number of instances activated by this registration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeActivations>`_    


    **Request Syntax** 
    ::

      response = client.describe_activations(
          Filters=[
              {
                  'FilterKey': 'ActivationIds'|'DefaultInstanceName'|'IamRole',
                  'FilterValues': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type Filters: list
    :param Filters: 

      A filter to view information about your activations.

      

    
      - *(dict) --* 

        Filter for the DescribeActivation API.

        

      
        - **FilterKey** *(string) --* 

          The name of the filter.

          

        
        - **FilterValues** *(list) --* 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      A token to start the list. Use this token to get the next set of results. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ActivationList': [
                {
                    'ActivationId': 'string',
                    'Description': 'string',
                    'DefaultInstanceName': 'string',
                    'IamRole': 'string',
                    'RegistrationLimit': 123,
                    'RegistrationsCount': 123,
                    'ExpirationDate': datetime(2015, 1, 1),
                    'Expired': True|False,
                    'CreatedDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ActivationList** *(list) --* 

          A list of activations for your AWS account.

          
          

          - *(dict) --* 

            An activation registers one or more on-premises servers or virtual machines (VMs) with AWS so that you can configure those servers or VMs using Run Command. A server or VM that has been registered with AWS is called a managed instance.

            
            

            - **ActivationId** *(string) --* 

              The ID created by Systems Manager when you submitted the activation.

              
            

            - **Description** *(string) --* 

              A user defined description of the activation.

              
            

            - **DefaultInstanceName** *(string) --* 

              A name for the managed instance when it is created.

              
            

            - **IamRole** *(string) --* 

              The Amazon Identity and Access Management (IAM) role to assign to the managed instance.

              
            

            - **RegistrationLimit** *(integer) --* 

              The maximum number of managed instances that can be registered using this activation.

              
            

            - **RegistrationsCount** *(integer) --* 

              The number of managed instances already registered with this activation.

              
            

            - **ExpirationDate** *(datetime) --* 

              The date when this activation can no longer be used to register managed instances.

              
            

            - **Expired** *(boolean) --* 

              Whether or not the activation is expired.

              
            

            - **CreatedDate** *(datetime) --* 

              The date the activation was created.

              
        
      
        

        - **NextToken** *(string) --* 

          The token for the next set of items to return. Use this token to get the next set of results. 

          
    

  .. py:method:: describe_association(**kwargs)

    

    Describes the association for the specified target or instance. If you created the association by using the ``Targets`` parameter, then you must retrieve the association by using the association ID. If you created the association by specifying an instance ID and a Systems Manager document, then you retrieve the association by specifying the document name and the instance ID. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAssociation>`_    


    **Request Syntax** 
    ::

      response = client.describe_association(
          Name='string',
          InstanceId='string',
          AssociationId='string',
          AssociationVersion='string'
      )
    :type Name: string
    :param Name: 

      The name of the Systems Manager document.

      

    
    :type InstanceId: string
    :param InstanceId: 

      The instance ID.

      

    
    :type AssociationId: string
    :param AssociationId: 

      The association ID for which you want information.

      

    
    :type AssociationVersion: string
    :param AssociationVersion: 

      Specify the association version to retrieve. To view the latest version, either specify ``$LATEST`` for this parameter, or omit this parameter. To view a list of all associations for an instance, use ListInstanceAssociations. To get a list of versions for a specific association, use ListAssociationVersions. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociationDescription': {
                'Name': 'string',
                'InstanceId': 'string',
                'AssociationVersion': 'string',
                'Date': datetime(2015, 1, 1),
                'LastUpdateAssociationDate': datetime(2015, 1, 1),
                'Status': {
                    'Date': datetime(2015, 1, 1),
                    'Name': 'Pending'|'Success'|'Failed',
                    'Message': 'string',
                    'AdditionalInfo': 'string'
                },
                'Overview': {
                    'Status': 'string',
                    'DetailedStatus': 'string',
                    'AssociationStatusAggregatedCount': {
                        'string': 123
                    }
                },
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'AssociationId': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ScheduleExpression': 'string',
                'OutputLocation': {
                    'S3Location': {
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string'
                    }
                },
                'LastExecutionDate': datetime(2015, 1, 1),
                'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
                'AssociationName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AssociationDescription** *(dict) --* 

          Information about the association.

          
          

          - **Name** *(string) --* 

            The name of the Systems Manager document.

            
          

          - **InstanceId** *(string) --* 

            The ID of the instance.

            
          

          - **AssociationVersion** *(string) --* 

            The association version.

            
          

          - **Date** *(datetime) --* 

            The date when the association was made.

            
          

          - **LastUpdateAssociationDate** *(datetime) --* 

            The date when the association was last updated.

            
          

          - **Status** *(dict) --* 

            The association status.

            
            

            - **Date** *(datetime) --* 

              The date when the status changed.

              
            

            - **Name** *(string) --* 

              The status.

              
            

            - **Message** *(string) --* 

              The reason for the status.

              
            

            - **AdditionalInfo** *(string) --* 

              A user-defined string.

              
        
          

          - **Overview** *(dict) --* 

            Information about the association.

            
            

            - **Status** *(string) --* 

              The status of the association. Status can be: Pending, Success, or Failed.

              
            

            - **DetailedStatus** *(string) --* 

              A detailed status of the association.

              
            

            - **AssociationStatusAggregatedCount** *(dict) --* 

              Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

              
              

              - *(string) --* 
                

                - *(integer) --* 
          
        
        
          

          - **DocumentVersion** *(string) --* 

            The document version.

            
          

          - **Parameters** *(dict) --* 

            A description of the parameters for a document. 

            
            

            - *(string) --* 
              

              - *(list) --* 
                

                - *(string) --* 
            
        
      
          

          - **AssociationId** *(string) --* 

            The association ID.

            
          

          - **Targets** *(list) --* 

            The instances targeted by the request. 

            
            

            - *(dict) --* 

              An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

               

              

              
              

              - **Key** *(string) --* 

                User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
              

              - **Values** *(list) --* 

                User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
                

                - *(string) --* 
            
          
        
          

          - **ScheduleExpression** *(string) --* 

            A cron expression that specifies a schedule when the association runs.

            
          

          - **OutputLocation** *(dict) --* 

            An Amazon S3 bucket where you want to store the output details of the request.

            
            

            - **S3Location** *(dict) --* 

              An Amazon S3 bucket where you want to store the results of this request.

              
              

              - **OutputS3Region** *(string) --* 

                (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                
              

              - **OutputS3BucketName** *(string) --* 

                The name of the Amazon S3 bucket.

                
              

              - **OutputS3KeyPrefix** *(string) --* 

                The Amazon S3 bucket subfolder.

                
          
        
          

          - **LastExecutionDate** *(datetime) --* 

            The date on which the association was last run.

            
          

          - **LastSuccessfulExecutionDate** *(datetime) --* 

            The last date on which the association was successfully run.

            
          

          - **AssociationName** *(string) --* 

            The association name.

            
      
    

  .. py:method:: describe_automation_executions(**kwargs)

    

    Provides details about all active and terminated Automation executions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAutomationExecutions>`_    


    **Request Syntax** 
    ::

      response = client.describe_automation_executions(
          Filters=[
              {
                  'Key': 'DocumentNamePrefix'|'ExecutionStatus'|'ExecutionId'|'ParentExecutionId'|'CurrentAction'|'StartTimeBefore'|'StartTimeAfter',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type Filters: list
    :param Filters: 

      Filters used to limit the scope of executions that are requested.

      

    
      - *(dict) --* 

        A filter used to match specific automation executions. This is used to limit the scope of Automation execution information returned.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          One or more keys to limit the results. Valid filter keys include the following: DocumentNamePrefix, ExecutionStatus, ExecutionId, ParentExecutionId, CurrentAction, StartTimeBefore, StartTimeAfter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The values used to limit the execution information associated with the filter's key.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutomationExecutionMetadataList': [
                {
                    'AutomationExecutionId': 'string',
                    'DocumentName': 'string',
                    'DocumentVersion': 'string',
                    'AutomationExecutionStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                    'ExecutionStartTime': datetime(2015, 1, 1),
                    'ExecutionEndTime': datetime(2015, 1, 1),
                    'ExecutedBy': 'string',
                    'LogFile': 'string',
                    'Outputs': {
                        'string': [
                            'string',
                        ]
                    },
                    'Mode': 'Auto'|'Interactive',
                    'ParentAutomationExecutionId': 'string',
                    'CurrentStepName': 'string',
                    'CurrentAction': 'string',
                    'FailureMessage': 'string',
                    'TargetParameterName': 'string',
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'ResolvedTargets': {
                        'ParameterValues': [
                            'string',
                        ],
                        'Truncated': True|False
                    },
                    'MaxConcurrency': 'string',
                    'MaxErrors': 'string',
                    'Target': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AutomationExecutionMetadataList** *(list) --* 

          The list of details about each automation execution which has occurred which matches the filter specification, if any.

          
          

          - *(dict) --* 

            Details about a specific Automation execution.

            
            

            - **AutomationExecutionId** *(string) --* 

              The execution ID.

              
            

            - **DocumentName** *(string) --* 

              The name of the Automation document used during execution.

              
            

            - **DocumentVersion** *(string) --* 

              The document version used during the execution.

              
            

            - **AutomationExecutionStatus** *(string) --* 

              The status of the execution. Valid values include: Running, Succeeded, Failed, Timed out, or Cancelled.

              
            

            - **ExecutionStartTime** *(datetime) --* 

              The time the execution started.>

              
            

            - **ExecutionEndTime** *(datetime) --* 

              The time the execution finished. This is not populated if the execution is still in progress.

              
            

            - **ExecutedBy** *(string) --* 

              The IAM role ARN of the user who executed the Automation.

              
            

            - **LogFile** *(string) --* 

              An Amazon S3 bucket where execution information is stored.

              
            

            - **Outputs** *(dict) --* 

              The list of execution outputs as defined in the Automation document.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
            

            - **Mode** *(string) --* 

              The Automation execution mode.

              
            

            - **ParentAutomationExecutionId** *(string) --* 

              The ExecutionId of the parent Automation.

              
            

            - **CurrentStepName** *(string) --* 

              The name of the currently executing step.

              
            

            - **CurrentAction** *(string) --* 

              The action of the currently executing step.

              
            

            - **FailureMessage** *(string) --* 

              The list of execution outputs as defined in the Automation document.

              
            

            - **TargetParameterName** *(string) --* 

              The list of execution outputs as defined in the Automation document.

              
            

            - **Targets** *(list) --* 

              The targets defined by the user when starting the Automation.

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **ResolvedTargets** *(dict) --* 

              A list of targets that resolved during the execution.

              
              

              - **ParameterValues** *(list) --* 

                A list of parameter values sent to targets that resolved during the Automation execution.

                
                

                - *(string) --* 
            
              

              - **Truncated** *(boolean) --* 

                A boolean value indicating whether the resolved target list is truncated.

                
          
            

            - **MaxConcurrency** *(string) --* 

              The MaxConcurrency value specified by the user when starting the Automation.

              
            

            - **MaxErrors** *(string) --* 

              The MaxErrors value specified by the user when starting the Automation.

              
            

            - **Target** *(string) --* 

              The list of execution outputs as defined in the Automation document.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_automation_step_executions(**kwargs)

    

    Information about all active and terminated step executions in an Automation workflow.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAutomationStepExecutions>`_    


    **Request Syntax** 
    ::

      response = client.describe_automation_step_executions(
          AutomationExecutionId='string',
          Filters=[
              {
                  'Key': 'StartTimeBefore'|'StartTimeAfter'|'StepExecutionStatus'|'StepExecutionId'|'StepName'|'Action',
                  'Values': [
                      'string',
                  ]
              },
          ],
          NextToken='string',
          MaxResults=123,
          ReverseOrder=True|False
      )
    :type AutomationExecutionId: string
    :param AutomationExecutionId: **[REQUIRED]** 

      The Automation execution ID for which you want step execution descriptions.

      

    
    :type Filters: list
    :param Filters: 

      One or more filters to limit the number of step executions returned by the request.

      

    
      - *(dict) --* 

        A filter to limit the amount of step execution information returned by the call.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          One or more keys to limit the results. Valid filter keys include the following: StepName, Action, StepExecutionId, StepExecutionStatus, StartTimeBefore, StartTimeAfter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The values of the filter key.

          

        
          - *(string) --* 

          
      
      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type ReverseOrder: boolean
    :param ReverseOrder: 

      A boolean that indicates whether to list step executions in reverse order by start time. The default value is false.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StepExecutions': [
                {
                    'StepName': 'string',
                    'Action': 'string',
                    'TimeoutSeconds': 123,
                    'OnFailure': 'string',
                    'MaxAttempts': 123,
                    'ExecutionStartTime': datetime(2015, 1, 1),
                    'ExecutionEndTime': datetime(2015, 1, 1),
                    'StepStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                    'ResponseCode': 'string',
                    'Inputs': {
                        'string': 'string'
                    },
                    'Outputs': {
                        'string': [
                            'string',
                        ]
                    },
                    'Response': 'string',
                    'FailureMessage': 'string',
                    'FailureDetails': {
                        'FailureStage': 'string',
                        'FailureType': 'string',
                        'Details': {
                            'string': [
                                'string',
                            ]
                        }
                    },
                    'StepExecutionId': 'string',
                    'OverriddenParameters': {
                        'string': [
                            'string',
                        ]
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StepExecutions** *(list) --* 

          A list of details about the current state of all steps that make up an execution.

          
          

          - *(dict) --* 

            Detailed information about an the execution state of an Automation step.

            
            

            - **StepName** *(string) --* 

              The name of this execution step.

              
            

            - **Action** *(string) --* 

              The action this step performs. The action determines the behavior of the step.

              
            

            - **TimeoutSeconds** *(integer) --* 

              The timeout seconds of the step.

              
            

            - **OnFailure** *(string) --* 

              The action to take if the step fails. The default value is Abort.

              
            

            - **MaxAttempts** *(integer) --* 

              The maximum number of tries to run the action of the step. The default value is 1.

              
            

            - **ExecutionStartTime** *(datetime) --* 

              If a step has begun execution, this contains the time the step started. If the step is in Pending status, this field is not populated.

              
            

            - **ExecutionEndTime** *(datetime) --* 

              If a step has finished execution, this contains the time the execution ended. If the step has not yet concluded, this field is not populated.

              
            

            - **StepStatus** *(string) --* 

              The execution status for this step. Valid values include: Pending, InProgress, Success, Cancelled, Failed, and TimedOut.

              
            

            - **ResponseCode** *(string) --* 

              The response code returned by the execution of the step.

              
            

            - **Inputs** *(dict) --* 

              Fully-resolved values passed into the step before execution.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **Outputs** *(dict) --* 

              Returned values from the execution of the step.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
            

            - **Response** *(string) --* 

              A message associated with the response code for an execution.

              
            

            - **FailureMessage** *(string) --* 

              If a step failed, this message explains why the execution failed.

              
            

            - **FailureDetails** *(dict) --* 

              Information about the Automation failure.

              
              

              - **FailureStage** *(string) --* 

                The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.

                
              

              - **FailureType** *(string) --* 

                The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.

                
              

              - **Details** *(dict) --* 

                Detailed information about the Automation step failure.

                
                

                - *(string) --* 
                  

                  - *(list) --* 
                    

                    - *(string) --* 
                
            
          
          
            

            - **StepExecutionId** *(string) --* 

              The unique ID of a step execution.

              
            

            - **OverriddenParameters** *(dict) --* 

              A user-specified list of parameters to override when executing a step.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_available_patches(**kwargs)

    

    Lists all patches that could possibly be included in a patch baseline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAvailablePatches>`_    


    **Request Syntax** 
    ::

      response = client.describe_available_patches(
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type Filters: list
    :param Filters: 

      Filters used to scope down the returned patches.

      

    
      - *(dict) --* 

        Defines a filter used in Patch Manager APIs.

        

      
        - **Key** *(string) --* 

          The key for the filter.

          

        
        - **Values** *(list) --* 

          The value for the filter.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of patches to return (per page).

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Patches': [
                {
                    'Id': 'string',
                    'ReleaseDate': datetime(2015, 1, 1),
                    'Title': 'string',
                    'Description': 'string',
                    'ContentUrl': 'string',
                    'Vendor': 'string',
                    'ProductFamily': 'string',
                    'Product': 'string',
                    'Classification': 'string',
                    'MsrcSeverity': 'string',
                    'KbNumber': 'string',
                    'MsrcNumber': 'string',
                    'Language': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Patches** *(list) --* 

          An array of patches. Each entry in the array is a patch structure.

          
          

          - *(dict) --* 

            Represents metadata about a patch.

            
            

            - **Id** *(string) --* 

              The ID of the patch (this is different than the Microsoft Knowledge Base ID).

              
            

            - **ReleaseDate** *(datetime) --* 

              The date the patch was released.

              
            

            - **Title** *(string) --* 

              The title of the patch.

              
            

            - **Description** *(string) --* 

              The description of the patch.

              
            

            - **ContentUrl** *(string) --* 

              The URL where more information can be obtained about the patch.

              
            

            - **Vendor** *(string) --* 

              The name of the vendor providing the patch.

              
            

            - **ProductFamily** *(string) --* 

              The product family the patch is applicable for (for example, Windows).

              
            

            - **Product** *(string) --* 

              The specific product the patch is applicable for (for example, WindowsServer2016).

              
            

            - **Classification** *(string) --* 

              The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).

              
            

            - **MsrcSeverity** *(string) --* 

              The severity of the patch (for example Critical, Important, Moderate).

              
            

            - **KbNumber** *(string) --* 

              The Microsoft Knowledge Base ID of the patch.

              
            

            - **MsrcNumber** *(string) --* 

              The ID of the MSRC bulletin the patch is related to.

              
            

            - **Language** *(string) --* 

              The language of the patch if it's language-specific.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_document(**kwargs)

    

    Describes the specified Systems Manager document.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeDocument>`_    


    **Request Syntax** 
    ::

      response = client.describe_document(
          Name='string',
          DocumentVersion='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the Systems Manager document.

      

    
    :type DocumentVersion: string
    :param DocumentVersion: 

      The document version for which you want information. Can be a specific version or the default version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Document': {
                'Sha1': 'string',
                'Hash': 'string',
                'HashType': 'Sha256'|'Sha1',
                'Name': 'string',
                'Owner': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'Status': 'Creating'|'Active'|'Updating'|'Deleting',
                'DocumentVersion': 'string',
                'Description': 'string',
                'Parameters': [
                    {
                        'Name': 'string',
                        'Type': 'String'|'StringList',
                        'Description': 'string',
                        'DefaultValue': 'string'
                    },
                ],
                'PlatformTypes': [
                    'Windows'|'Linux',
                ],
                'DocumentType': 'Command'|'Policy'|'Automation',
                'SchemaVersion': 'string',
                'LatestVersion': 'string',
                'DefaultVersion': 'string',
                'DocumentFormat': 'YAML'|'JSON',
                'TargetType': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Document** *(dict) --* 

          Information about the Systems Manager document.

          
          

          - **Sha1** *(string) --* 

            The SHA1 hash of the document, which you can use for verification.

            
          

          - **Hash** *(string) --* 

            The Sha256 or Sha1 hash created by the system when the document was created. 

             

            .. note::

               

              Sha1 hashes have been deprecated.

               

            
          

          - **HashType** *(string) --* 

            Sha256 or Sha1.

             

            .. note::

               

              Sha1 hashes have been deprecated.

               

            
          

          - **Name** *(string) --* 

            The name of the Systems Manager document.

            
          

          - **Owner** *(string) --* 

            The AWS user account that created the document.

            
          

          - **CreatedDate** *(datetime) --* 

            The date when the document was created.

            
          

          - **Status** *(string) --* 

            The status of the Systems Manager document.

            
          

          - **DocumentVersion** *(string) --* 

            The document version.

            
          

          - **Description** *(string) --* 

            A description of the document. 

            
          

          - **Parameters** *(list) --* 

            A description of the parameters for a document.

            
            

            - *(dict) --* 

              Parameters specified in a System Manager document that execute on the server when the command is run. 

              
              

              - **Name** *(string) --* 

                The name of the parameter.

                
              

              - **Type** *(string) --* 

                The type of parameter. The type can be either String or StringList.

                
              

              - **Description** *(string) --* 

                A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.

                
              

              - **DefaultValue** *(string) --* 

                If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.

                
          
        
          

          - **PlatformTypes** *(list) --* 

            The list of OS platforms compatible with this Systems Manager document. 

            
            

            - *(string) --* 
        
          

          - **DocumentType** *(string) --* 

            The type of document. 

            
          

          - **SchemaVersion** *(string) --* 

            The schema version.

            
          

          - **LatestVersion** *(string) --* 

            The latest version of the document.

            
          

          - **DefaultVersion** *(string) --* 

            The default version.

            
          

          - **DocumentFormat** *(string) --* 

            The document format, either JSON or YAML.

            
          

          - **TargetType** *(string) --* 

            The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 

            
          

          - **Tags** *(list) --* 

            The tags, or metadata, that have been applied to the document.

            
            

            - *(dict) --* 

              Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.

              
              

              - **Key** *(string) --* 

                The name of the tag.

                
              

              - **Value** *(string) --* 

                The value of the tag.

                
          
        
      
    

  .. py:method:: describe_document_permission(**kwargs)

    

    Describes the permissions for a Systems Manager document. If you created the document, you are the owner. If a document is shared, it can either be shared privately (by specifying a user's AWS account ID) or publicly (*All* ). 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeDocumentPermission>`_    


    **Request Syntax** 
    ::

      response = client.describe_document_permission(
          Name='string',
          PermissionType='Share'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the document for which you are the owner.

      

    
    :type PermissionType: string
    :param PermissionType: **[REQUIRED]** 

      The permission type for the document. The permission type can be *Share* .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AccountIds': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AccountIds** *(list) --* 

          The account IDs that have permission to use this document. The ID can be either an AWS account or *All* .

          
          

          - *(string) --* 
      
    

  .. py:method:: describe_effective_instance_associations(**kwargs)

    

    All associations for the instance(s).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeEffectiveInstanceAssociations>`_    


    **Request Syntax** 
    ::

      response = client.describe_effective_instance_associations(
          InstanceId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID for which you want to view all associations.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Associations': [
                {
                    'AssociationId': 'string',
                    'InstanceId': 'string',
                    'Content': 'string',
                    'AssociationVersion': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Associations** *(list) --* 

          The associations for the requested instance.

          
          

          - *(dict) --* 

            One or more association documents on the instance. 

            
            

            - **AssociationId** *(string) --* 

              The association ID.

              
            

            - **InstanceId** *(string) --* 

              The instance ID.

              
            

            - **Content** *(string) --* 

              The content of the association document for the instance(s).

              
            

            - **AssociationVersion** *(string) --* 

              Version information for the association on the instance.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_effective_patches_for_patch_baseline(**kwargs)

    

    Retrieves the current effective patches (the patch and the approval state) for the specified patch baseline. Note that this API applies only to Windows patch baselines.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline>`_    


    **Request Syntax** 
    ::

      response = client.describe_effective_patches_for_patch_baseline(
          BaselineId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type BaselineId: string
    :param BaselineId: **[REQUIRED]** 

      The ID of the patch baseline to retrieve the effective patches for.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of patches to return (per page).

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EffectivePatches': [
                {
                    'Patch': {
                        'Id': 'string',
                        'ReleaseDate': datetime(2015, 1, 1),
                        'Title': 'string',
                        'Description': 'string',
                        'ContentUrl': 'string',
                        'Vendor': 'string',
                        'ProductFamily': 'string',
                        'Product': 'string',
                        'Classification': 'string',
                        'MsrcSeverity': 'string',
                        'KbNumber': 'string',
                        'MsrcNumber': 'string',
                        'Language': 'string'
                    },
                    'PatchStatus': {
                        'DeploymentStatus': 'APPROVED'|'PENDING_APPROVAL'|'EXPLICIT_APPROVED'|'EXPLICIT_REJECTED',
                        'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                        'ApprovalDate': datetime(2015, 1, 1)
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EffectivePatches** *(list) --* 

          An array of patches and patch status.

          
          

          - *(dict) --* 

            The EffectivePatch structure defines metadata about a patch along with the approval state of the patch in a particular patch baseline. The approval state includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.

            
            

            - **Patch** *(dict) --* 

              Provides metadata for a patch, including information such as the KB ID, severity, classification and a URL for where more information can be obtained about the patch.

              
              

              - **Id** *(string) --* 

                The ID of the patch (this is different than the Microsoft Knowledge Base ID).

                
              

              - **ReleaseDate** *(datetime) --* 

                The date the patch was released.

                
              

              - **Title** *(string) --* 

                The title of the patch.

                
              

              - **Description** *(string) --* 

                The description of the patch.

                
              

              - **ContentUrl** *(string) --* 

                The URL where more information can be obtained about the patch.

                
              

              - **Vendor** *(string) --* 

                The name of the vendor providing the patch.

                
              

              - **ProductFamily** *(string) --* 

                The product family the patch is applicable for (for example, Windows).

                
              

              - **Product** *(string) --* 

                The specific product the patch is applicable for (for example, WindowsServer2016).

                
              

              - **Classification** *(string) --* 

                The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).

                
              

              - **MsrcSeverity** *(string) --* 

                The severity of the patch (for example Critical, Important, Moderate).

                
              

              - **KbNumber** *(string) --* 

                The Microsoft Knowledge Base ID of the patch.

                
              

              - **MsrcNumber** *(string) --* 

                The ID of the MSRC bulletin the patch is related to.

                
              

              - **Language** *(string) --* 

                The language of the patch if it's language-specific.

                
          
            

            - **PatchStatus** *(dict) --* 

              The status of the patch in a patch baseline. This includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.

              
              

              - **DeploymentStatus** *(string) --* 

                The approval status of a patch (APPROVED, PENDING_APPROVAL, EXPLICIT_APPROVED, EXPLICIT_REJECTED).

                
              

              - **ComplianceLevel** *(string) --* 

                The compliance severity level for a patch.

                
              

              - **ApprovalDate** *(datetime) --* 

                The date the patch was approved (or will be approved if the status is PENDING_APPROVAL).

                
          
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_instance_associations_status(**kwargs)

    

    The status of the associations for the instance(s).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceAssociationsStatus>`_    


    **Request Syntax** 
    ::

      response = client.describe_instance_associations_status(
          InstanceId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance IDs for which you want association status information.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InstanceAssociationStatusInfos': [
                {
                    'AssociationId': 'string',
                    'Name': 'string',
                    'DocumentVersion': 'string',
                    'AssociationVersion': 'string',
                    'InstanceId': 'string',
                    'ExecutionDate': datetime(2015, 1, 1),
                    'Status': 'string',
                    'DetailedStatus': 'string',
                    'ExecutionSummary': 'string',
                    'ErrorCode': 'string',
                    'OutputUrl': {
                        'S3OutputUrl': {
                            'OutputUrl': 'string'
                        }
                    },
                    'AssociationName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **InstanceAssociationStatusInfos** *(list) --* 

          Status information about the association.

          
          

          - *(dict) --* 

            Status information about the instance association.

            
            

            - **AssociationId** *(string) --* 

              The association ID.

              
            

            - **Name** *(string) --* 

              The name of the association.

              
            

            - **DocumentVersion** *(string) --* 

              The association document verions.

              
            

            - **AssociationVersion** *(string) --* 

              The version of the association applied to the instance.

              
            

            - **InstanceId** *(string) --* 

              The instance ID where the association was created.

              
            

            - **ExecutionDate** *(datetime) --* 

              The date the instance association executed. 

              
            

            - **Status** *(string) --* 

              Status information about the instance association.

              
            

            - **DetailedStatus** *(string) --* 

              Detailed status information about the instance association.

              
            

            - **ExecutionSummary** *(string) --* 

              Summary information about association execution.

              
            

            - **ErrorCode** *(string) --* 

              An error code returned by the request to create the association.

              
            

            - **OutputUrl** *(dict) --* 

              A URL for an Amazon S3 bucket where you want to store the results of this request.

              
              

              - **S3OutputUrl** *(dict) --* 

                The URL of Amazon S3 bucket where you want to store the results of this request.

                
                

                - **OutputUrl** *(string) --* 

                  A URL for an Amazon S3 bucket where you want to store the results of this request.

                  
            
          
            

            - **AssociationName** *(string) --* 

              The name of the association applied to the instance.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_instance_information(**kwargs)

    

    Describes one or more of your instances. You can use this to get information about instances like the operating system platform, the SSM Agent version (Linux), status etc. If you specify one or more instance IDs, it returns information for those instances. If you do not specify instance IDs, it returns information for all your instances. If you specify an instance ID that is not valid or an instance that you do not own, you receive an error. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceInformation>`_    


    **Request Syntax** 
    ::

      response = client.describe_instance_information(
          InstanceInformationFilterList=[
              {
                  'key': 'InstanceIds'|'AgentVersion'|'PingStatus'|'PlatformTypes'|'ActivationIds'|'IamRole'|'ResourceType'|'AssociationStatus',
                  'valueSet': [
                      'string',
                  ]
              },
          ],
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type InstanceInformationFilterList: list
    :param InstanceInformationFilterList: 

      One or more filters. Use a filter to return a more specific list of instances.

      

    
      - *(dict) --* 

        Describes a filter for a specific list of instances. 

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter. 

          

        
        - **valueSet** *(list) --* **[REQUIRED]** 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of instances.

      

    
      - *(dict) --* 

        The filters to describe or get information about your managed instances.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The filter key name to describe your instances. For example:

           

          "InstanceIds"|"AgentVersion"|"PingStatus"|"PlatformTypes"|"ActivationIds"|"IamRole"|"ResourceType"|"AssociationStatus"|"Tag Key"

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. 

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InstanceInformationList': [
                {
                    'InstanceId': 'string',
                    'PingStatus': 'Online'|'ConnectionLost'|'Inactive',
                    'LastPingDateTime': datetime(2015, 1, 1),
                    'AgentVersion': 'string',
                    'IsLatestVersion': True|False,
                    'PlatformType': 'Windows'|'Linux',
                    'PlatformName': 'string',
                    'PlatformVersion': 'string',
                    'ActivationId': 'string',
                    'IamRole': 'string',
                    'RegistrationDate': datetime(2015, 1, 1),
                    'ResourceType': 'ManagedInstance'|'Document'|'EC2Instance',
                    'Name': 'string',
                    'IPAddress': 'string',
                    'ComputerName': 'string',
                    'AssociationStatus': 'string',
                    'LastAssociationExecutionDate': datetime(2015, 1, 1),
                    'LastSuccessfulAssociationExecutionDate': datetime(2015, 1, 1),
                    'AssociationOverview': {
                        'DetailedStatus': 'string',
                        'InstanceAssociationStatusAggregatedCount': {
                            'string': 123
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **InstanceInformationList** *(list) --* 

          The instance information list.

          
          

          - *(dict) --* 

            Describes a filter for a specific list of instances. 

            
            

            - **InstanceId** *(string) --* 

              The instance ID. 

              
            

            - **PingStatus** *(string) --* 

              Connection status of the SSM Agent. 

              
            

            - **LastPingDateTime** *(datetime) --* 

              The date and time when agent last pinged Systems Manager service. 

              
            

            - **AgentVersion** *(string) --* 

              The version of the SSM Agent running on your Linux instance. 

              
            

            - **IsLatestVersion** *(boolean) --* 

              Indicates whether latest version of the SSM Agent is running on your instance. 

              
            

            - **PlatformType** *(string) --* 

              The operating system platform type. 

              
            

            - **PlatformName** *(string) --* 

              The name of the operating system platform running on your instance. 

              
            

            - **PlatformVersion** *(string) --* 

              The version of the OS platform running on your instance. 

              
            

            - **ActivationId** *(string) --* 

              The activation ID created by Systems Manager when the server or VM was registered.

              
            

            - **IamRole** *(string) --* 

              The Amazon Identity and Access Management (IAM) role assigned to EC2 instances or managed instances. 

              
            

            - **RegistrationDate** *(datetime) --* 

              The date the server or VM was registered with AWS as a managed instance.

              
            

            - **ResourceType** *(string) --* 

              The type of instance. Instances are either EC2 instances or managed instances. 

              
            

            - **Name** *(string) --* 

              The name of the managed instance.

              
            

            - **IPAddress** *(string) --* 

              The IP address of the managed instance.

              
            

            - **ComputerName** *(string) --* 

              The fully qualified host name of the managed instance.

              
            

            - **AssociationStatus** *(string) --* 

              The status of the association.

              
            

            - **LastAssociationExecutionDate** *(datetime) --* 

              The date the association was last executed.

              
            

            - **LastSuccessfulAssociationExecutionDate** *(datetime) --* 

              The last date the association was successfully run.

              
            

            - **AssociationOverview** *(dict) --* 

              Information about the association.

              
              

              - **DetailedStatus** *(string) --* 

                Detailed status information about the aggregated associations.

                
              

              - **InstanceAssociationStatusAggregatedCount** *(dict) --* 

                The number of associations for the instance(s).

                
                

                - *(string) --* 
                  

                  - *(integer) --* 
            
          
          
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty. 

          
    

  .. py:method:: describe_instance_patch_states(**kwargs)

    

    Retrieves the high-level patch state of one or more instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatchStates>`_    


    **Request Syntax** 
    ::

      response = client.describe_instance_patch_states(
          InstanceIds=[
              'string',
          ],
          NextToken='string',
          MaxResults=123
      )
    :type InstanceIds: list
    :param InstanceIds: **[REQUIRED]** 

      The ID of the instance whose patch state information should be retrieved.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of instances to return (per page).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InstancePatchStates': [
                {
                    'InstanceId': 'string',
                    'PatchGroup': 'string',
                    'BaselineId': 'string',
                    'SnapshotId': 'string',
                    'OwnerInformation': 'string',
                    'InstalledCount': 123,
                    'InstalledOtherCount': 123,
                    'MissingCount': 123,
                    'FailedCount': 123,
                    'NotApplicableCount': 123,
                    'OperationStartTime': datetime(2015, 1, 1),
                    'OperationEndTime': datetime(2015, 1, 1),
                    'Operation': 'Scan'|'Install'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **InstancePatchStates** *(list) --* 

          The high-level patch state for the requested instances.

          
          

          - *(dict) --* 

            Defines the high-level patch compliance state for a managed instance, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the instance.

            
            

            - **InstanceId** *(string) --* 

              The ID of the managed instance the high-level patch compliance information was collected for.

              
            

            - **PatchGroup** *(string) --* 

              The name of the patch group the managed instance belongs to.

              
            

            - **BaselineId** *(string) --* 

              The ID of the patch baseline used to patch the instance.

              
            

            - **SnapshotId** *(string) --* 

              The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.

              
            

            - **OwnerInformation** *(string) --* 

              Placeholder information, this field will always be empty in the current release of the service.

              
            

            - **InstalledCount** *(integer) --* 

              The number of patches from the patch baseline that are installed on the instance.

              
            

            - **InstalledOtherCount** *(integer) --* 

              The number of patches not specified in the patch baseline that are installed on the instance.

              
            

            - **MissingCount** *(integer) --* 

              The number of patches from the patch baseline that are applicable for the instance but aren't currently installed.

              
            

            - **FailedCount** *(integer) --* 

              The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.

              
            

            - **NotApplicableCount** *(integer) --* 

              The number of patches from the patch baseline that aren't applicable for the instance and hence aren't installed on the instance.

              
            

            - **OperationStartTime** *(datetime) --* 

              The time the most recent patching operation was started on the instance.

              
            

            - **OperationEndTime** *(datetime) --* 

              The time the most recent patching operation completed on the instance.

              
            

            - **Operation** *(string) --* 

              The type of patching operation that was performed: SCAN (assess patch compliance state) or INSTALL (install missing patches).

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_instance_patch_states_for_patch_group(**kwargs)

    

    Retrieves the high-level patch state for the instances in the specified patch group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup>`_    


    **Request Syntax** 
    ::

      response = client.describe_instance_patch_states_for_patch_group(
          PatchGroup='string',
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ],
                  'Type': 'Equal'|'NotEqual'|'LessThan'|'GreaterThan'
              },
          ],
          NextToken='string',
          MaxResults=123
      )
    :type PatchGroup: string
    :param PatchGroup: **[REQUIRED]** 

      The name of the patch group for which the patch state information should be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      Each entry in the array is a structure containing:

       

      Key (string between 1 and 200 characters)

       

      Values (array containing a single string)

       

      Type (string "Equal", "NotEqual", "LessThan", "GreaterThan")

      

    
      - *(dict) --* 

        Defines a filter used in DescribeInstancePatchStatesForPatchGroup used to scope down the information returned by the API.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key for the filter. Supported values are FailedCount, InstalledCount, InstalledOtherCount, MissingCount and NotApplicableCount.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The value for the filter, must be an integer greater than or equal to 0.

          

        
          - *(string) --* 

          
      
        - **Type** *(string) --* **[REQUIRED]** 

          The type of comparison that should be performed for the value: Equal, NotEqual, LessThan or GreaterThan.

          

        
      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of patches to return (per page).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InstancePatchStates': [
                {
                    'InstanceId': 'string',
                    'PatchGroup': 'string',
                    'BaselineId': 'string',
                    'SnapshotId': 'string',
                    'OwnerInformation': 'string',
                    'InstalledCount': 123,
                    'InstalledOtherCount': 123,
                    'MissingCount': 123,
                    'FailedCount': 123,
                    'NotApplicableCount': 123,
                    'OperationStartTime': datetime(2015, 1, 1),
                    'OperationEndTime': datetime(2015, 1, 1),
                    'Operation': 'Scan'|'Install'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **InstancePatchStates** *(list) --* 

          The high-level patch state for the requested instances. 

          
          

          - *(dict) --* 

            Defines the high-level patch compliance state for a managed instance, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the instance.

            
            

            - **InstanceId** *(string) --* 

              The ID of the managed instance the high-level patch compliance information was collected for.

              
            

            - **PatchGroup** *(string) --* 

              The name of the patch group the managed instance belongs to.

              
            

            - **BaselineId** *(string) --* 

              The ID of the patch baseline used to patch the instance.

              
            

            - **SnapshotId** *(string) --* 

              The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.

              
            

            - **OwnerInformation** *(string) --* 

              Placeholder information, this field will always be empty in the current release of the service.

              
            

            - **InstalledCount** *(integer) --* 

              The number of patches from the patch baseline that are installed on the instance.

              
            

            - **InstalledOtherCount** *(integer) --* 

              The number of patches not specified in the patch baseline that are installed on the instance.

              
            

            - **MissingCount** *(integer) --* 

              The number of patches from the patch baseline that are applicable for the instance but aren't currently installed.

              
            

            - **FailedCount** *(integer) --* 

              The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.

              
            

            - **NotApplicableCount** *(integer) --* 

              The number of patches from the patch baseline that aren't applicable for the instance and hence aren't installed on the instance.

              
            

            - **OperationStartTime** *(datetime) --* 

              The time the most recent patching operation was started on the instance.

              
            

            - **OperationEndTime** *(datetime) --* 

              The time the most recent patching operation completed on the instance.

              
            

            - **Operation** *(string) --* 

              The type of patching operation that was performed: SCAN (assess patch compliance state) or INSTALL (install missing patches).

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_instance_patches(**kwargs)

    

    Retrieves information about the patches on the specified instance and their state relative to the patch baseline being used for the instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatches>`_    


    **Request Syntax** 
    ::

      response = client.describe_instance_patches(
          InstanceId='string',
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          NextToken='string',
          MaxResults=123
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The ID of the instance whose patch state information should be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      Each entry in the array is a structure containing:

       

      Key (string, between 1 and 128 characters)

       

      Values (array of strings, each string between 1 and 256 characters)

      

    
      - *(dict) --* 

        Defines a filter used in Patch Manager APIs.

        

      
        - **Key** *(string) --* 

          The key for the filter.

          

        
        - **Values** *(list) --* 

          The value for the filter.

          

        
          - *(string) --* 

          
      
      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of patches to return (per page).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Patches': [
                {
                    'Title': 'string',
                    'KBId': 'string',
                    'Classification': 'string',
                    'Severity': 'string',
                    'State': 'INSTALLED'|'INSTALLED_OTHER'|'MISSING'|'NOT_APPLICABLE'|'FAILED',
                    'InstalledTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Patches** *(list) --* 

          Each entry in the array is a structure containing:

           

          Title (string)

           

          KBId (string)

           

          Classification (string)

           

          Severity (string)

           

          State (string: "INSTALLED", "INSTALLED OTHER", "MISSING", "NOT APPLICABLE", "FAILED")

           

          InstalledTime (DateTime)

           

          InstalledBy (string)

          
          

          - *(dict) --* 

            Information about the state of a patch on a particular instance as it relates to the patch baseline used to patch the instance.

            
            

            - **Title** *(string) --* 

              The title of the patch.

              
            

            - **KBId** *(string) --* 

              The operating system-specific ID of the patch.

              
            

            - **Classification** *(string) --* 

              The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).

              
            

            - **Severity** *(string) --* 

              The severity of the patch (for example, Critical, Important, Moderate).

              
            

            - **State** *(string) --* 

              The state of the patch on the instance (INSTALLED, INSTALLED_OTHER, MISSING, NOT_APPLICABLE or FAILED).

              
            

            - **InstalledTime** *(datetime) --* 

              The date/time the patch was installed on the instance. Note that not all operating systems provide this level of information.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_maintenance_window_execution_task_invocations(**kwargs)

    

    Retrieves the individual task executions (one per target) for a particular task executed as part of a Maintenance Window execution.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations>`_    


    **Request Syntax** 
    ::

      response = client.describe_maintenance_window_execution_task_invocations(
          WindowExecutionId='string',
          TaskId='string',
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type WindowExecutionId: string
    :param WindowExecutionId: **[REQUIRED]** 

      The ID of the Maintenance Window execution the task is part of.

      

    
    :type TaskId: string
    :param TaskId: **[REQUIRED]** 

      The ID of the specific task in the Maintenance Window task that should be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      Optional filters used to scope down the returned task invocations. The supported filter key is STATUS with the corresponding values PENDING, IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.

      

    
      - *(dict) --* 

        Filter used in the request.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowExecutionTaskInvocationIdentities': [
                {
                    'WindowExecutionId': 'string',
                    'TaskExecutionId': 'string',
                    'InvocationId': 'string',
                    'ExecutionId': 'string',
                    'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
                    'Parameters': 'string',
                    'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                    'StatusDetails': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'OwnerInformation': 'string',
                    'WindowTargetId': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowExecutionTaskInvocationIdentities** *(list) --* 

          Information about the task invocation results per invocation.

          
          

          - *(dict) --* 

            Describes the information about a task invocation for a particular target as part of a task execution performed as part of a Maintenance Window execution.

            
            

            - **WindowExecutionId** *(string) --* 

              The ID of the Maintenance Window execution that ran the task.

              
            

            - **TaskExecutionId** *(string) --* 

              The ID of the specific task execution in the Maintenance Window execution.

              
            

            - **InvocationId** *(string) --* 

              The ID of the task invocation.

              
            

            - **ExecutionId** *(string) --* 

              The ID of the action performed in the service that actually handled the task invocation. If the task type is RUN_COMMAND, this value is the command ID.

              
            

            - **TaskType** *(string) --* 

              The task type.

              
            

            - **Parameters** *(string) --* 

              The parameters that were provided for the invocation when it was executed.

              
            

            - **Status** *(string) --* 

              The status of the task invocation.

              
            

            - **StatusDetails** *(string) --* 

              The details explaining the status of the task invocation. Only available for certain Status values. 

              
            

            - **StartTime** *(datetime) --* 

              The time the invocation started.

              
            

            - **EndTime** *(datetime) --* 

              The time the invocation finished.

              
            

            - **OwnerInformation** *(string) --* 

              User-provided value that was specified when the target was registered with the Maintenance Window. This was also included in any CloudWatch events raised during the task invocation.

              
            

            - **WindowTargetId** *(string) --* 

              The ID of the target definition in this Maintenance Window the invocation was performed for.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_maintenance_window_execution_tasks(**kwargs)

    

    For a given Maintenance Window execution, lists the tasks that were executed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks>`_    


    **Request Syntax** 
    ::

      response = client.describe_maintenance_window_execution_tasks(
          WindowExecutionId='string',
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type WindowExecutionId: string
    :param WindowExecutionId: **[REQUIRED]** 

      The ID of the Maintenance Window execution whose task executions should be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      Optional filters used to scope down the returned tasks. The supported filter key is STATUS with the corresponding values PENDING, IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED. 

      

    
      - *(dict) --* 

        Filter used in the request.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowExecutionTaskIdentities': [
                {
                    'WindowExecutionId': 'string',
                    'TaskExecutionId': 'string',
                    'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                    'StatusDetails': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'TaskArn': 'string',
                    'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowExecutionTaskIdentities** *(list) --* 

          Information about the task executions.

          
          

          - *(dict) --* 

            Information about a task execution performed as part of a Maintenance Window execution.

            
            

            - **WindowExecutionId** *(string) --* 

              The ID of the Maintenance Window execution that ran the task.

              
            

            - **TaskExecutionId** *(string) --* 

              The ID of the specific task execution in the Maintenance Window execution.

              
            

            - **Status** *(string) --* 

              The status of the task execution.

              
            

            - **StatusDetails** *(string) --* 

              The details explaining the status of the task execution. Only available for certain status values.

              
            

            - **StartTime** *(datetime) --* 

              The time the task execution started.

              
            

            - **EndTime** *(datetime) --* 

              The time the task execution finished.

              
            

            - **TaskArn** *(string) --* 

              The ARN of the executed task.

              
            

            - **TaskType** *(string) --* 

              The type of executed task.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_maintenance_window_executions(**kwargs)

    

    Lists the executions of a Maintenance Window. This includes information about when the Maintenance Window was scheduled to be active, and information about tasks registered and run with the Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutions>`_    


    **Request Syntax** 
    ::

      response = client.describe_maintenance_window_executions(
          WindowId='string',
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the Maintenance Window whose executions should be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      Each entry in the array is a structure containing:

       

      Key (string, between 1 and 128 characters)

       

      Values (array of strings, each string is between 1 and 256 characters)

       

      The supported Keys are ExecutedBefore and ExecutedAfter with the value being a date/time string such as 2016-11-04T05:00:00Z.

      

    
      - *(dict) --* 

        Filter used in the request.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowExecutions': [
                {
                    'WindowId': 'string',
                    'WindowExecutionId': 'string',
                    'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                    'StatusDetails': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowExecutions** *(list) --* 

          Information about the Maintenance Windows execution.

          
          

          - *(dict) --* 

            Describes the information about an execution of a Maintenance Window. 

            
            

            - **WindowId** *(string) --* 

              The ID of the Maintenance Window.

              
            

            - **WindowExecutionId** *(string) --* 

              The ID of the Maintenance Window execution.

              
            

            - **Status** *(string) --* 

              The status of the execution.

              
            

            - **StatusDetails** *(string) --* 

              The details explaining the Status. Only available for certain status values.

              
            

            - **StartTime** *(datetime) --* 

              The time the execution started.

              
            

            - **EndTime** *(datetime) --* 

              The time the execution finished.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_maintenance_window_targets(**kwargs)

    

    Lists the targets registered with the Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowTargets>`_    


    **Request Syntax** 
    ::

      response = client.describe_maintenance_window_targets(
          WindowId='string',
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the Maintenance Window whose targets should be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      Optional filters that can be used to narrow down the scope of the returned window targets. The supported filter keys are Type, WindowTargetId and OwnerInformation.

      

    
      - *(dict) --* 

        Filter used in the request.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Targets': [
                {
                    'WindowId': 'string',
                    'WindowTargetId': 'string',
                    'ResourceType': 'INSTANCE',
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'OwnerInformation': 'string',
                    'Name': 'string',
                    'Description': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Targets** *(list) --* 

          Information about the targets in the Maintenance Window.

          
          

          - *(dict) --* 

            The target registered with the Maintenance Window.

            
            

            - **WindowId** *(string) --* 

              The Maintenance Window ID where the target is registered.

              
            

            - **WindowTargetId** *(string) --* 

              The ID of the target.

              
            

            - **ResourceType** *(string) --* 

              The type of target.

              
            

            - **Targets** *(list) --* 

              The targets (either instances or tags). Instances are specified using Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified using Key=<tag name>,Values=<tag value>.

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **OwnerInformation** *(string) --* 

              User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

              
            

            - **Name** *(string) --* 

              The target name.

              
            

            - **Description** *(string) --* 

              A description of the target.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_maintenance_window_tasks(**kwargs)

    

    Lists the tasks in a Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowTasks>`_    


    **Request Syntax** 
    ::

      response = client.describe_maintenance_window_tasks(
          WindowId='string',
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the Maintenance Window whose tasks should be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      Optional filters used to narrow down the scope of the returned tasks. The supported filter keys are WindowTaskId, TaskArn, Priority, and TaskType.

      

    
      - *(dict) --* 

        Filter used in the request.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tasks': [
                {
                    'WindowId': 'string',
                    'WindowTaskId': 'string',
                    'TaskArn': 'string',
                    'Type': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'TaskParameters': {
                        'string': {
                            'Values': [
                                'string',
                            ]
                        }
                    },
                    'Priority': 123,
                    'LoggingInfo': {
                        'S3BucketName': 'string',
                        'S3KeyPrefix': 'string',
                        'S3Region': 'string'
                    },
                    'ServiceRoleArn': 'string',
                    'MaxConcurrency': 'string',
                    'MaxErrors': 'string',
                    'Name': 'string',
                    'Description': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Tasks** *(list) --* 

          Information about the tasks in the Maintenance Window.

          
          

          - *(dict) --* 

            Information about a task defined for a Maintenance Window.

            
            

            - **WindowId** *(string) --* 

              The Maintenance Window ID where the task is registered.

              
            

            - **WindowTaskId** *(string) --* 

              The task ID.

              
            

            - **TaskArn** *(string) --* 

              The resource that the task uses during execution. For RUN_COMMAND and AUTOMATION task types, ``TaskArn`` is the Systems Manager document name or ARN. For LAMBDA tasks, it's the function name or ARN. For STEP_FUNCTION tasks, it's the state machine ARN.

              
            

            - **Type** *(string) --* 

              The type of task. The type can be one of the following: RUN_COMMAND, AUTOMATION, LAMBDA, or STEP_FUNCTION.

              
            

            - **Targets** *(list) --* 

              The targets (either instances or tags). Instances are specified using Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified using Key=<tag name>,Values=<tag value>.

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **TaskParameters** *(dict) --* 

              The parameters that should be passed to the task when it is executed.

              
              

              - *(string) --* 
                

                - *(dict) --* 

                  Defines the values for a task parameter.

                  
                  

                  - **Values** *(list) --* 

                    This field contains an array of 0 or more strings, each 1 to 255 characters in length.

                    
                    

                    - *(string) --* 
                
              
          
        
            

            - **Priority** *(integer) --* 

              The priority of the task in the Maintenance Window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

              
            

            - **LoggingInfo** *(dict) --* 

              Information about an Amazon S3 bucket to write task-level logs to.

              
              

              - **S3BucketName** *(string) --* 

                The name of an Amazon S3 bucket where execution logs are stored .

                
              

              - **S3KeyPrefix** *(string) --* 

                (Optional) The Amazon S3 bucket subfolder. 

                
              

              - **S3Region** *(string) --* 

                The region where the Amazon S3 bucket is located.

                
          
            

            - **ServiceRoleArn** *(string) --* 

              The role that should be assumed when executing the task

              
            

            - **MaxConcurrency** *(string) --* 

              The maximum number of targets this task can be run for in parallel.

              
            

            - **MaxErrors** *(string) --* 

              The maximum number of errors allowed before this task stops being scheduled.

              
            

            - **Name** *(string) --* 

              The task name.

              
            

            - **Description** *(string) --* 

              A description of the task.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_maintenance_windows(**kwargs)

    

    Retrieves the Maintenance Windows in an AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindows>`_    


    **Request Syntax** 
    ::

      response = client.describe_maintenance_windows(
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type Filters: list
    :param Filters: 

      Optional filters used to narrow down the scope of the returned Maintenance Windows. Supported filter keys are Name and Enabled.

      

    
      - *(dict) --* 

        Filter used in the request.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowIdentities': [
                {
                    'WindowId': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Enabled': True|False,
                    'Duration': 123,
                    'Cutoff': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowIdentities** *(list) --* 

          Information about the Maintenance Windows.

          
          

          - *(dict) --* 

            Information about the Maintenance Window.

            
            

            - **WindowId** *(string) --* 

              The ID of the Maintenance Window.

              
            

            - **Name** *(string) --* 

              The name of the Maintenance Window.

              
            

            - **Description** *(string) --* 

              A description of the Maintenance Window.

              
            

            - **Enabled** *(boolean) --* 

              Whether the Maintenance Window is enabled.

              
            

            - **Duration** *(integer) --* 

              The duration of the Maintenance Window in hours.

              
            

            - **Cutoff** *(integer) --* 

              The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_parameters(**kwargs)

    

    Get information about a parameter.

     

    Request results are returned on a best-effort basis. If you specify ``MaxResults`` in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of ``MaxResults`` . If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a ``NextToken`` . You can specify the ``NextToken`` in a subsequent call to get the next set of results.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeParameters>`_    


    **Request Syntax** 
    ::

      response = client.describe_parameters(
          Filters=[
              {
                  'Key': 'Name'|'Type'|'KeyId',
                  'Values': [
                      'string',
                  ]
              },
          ],
          ParameterFilters=[
              {
                  'Key': 'string',
                  'Option': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type ParameterFilters: list
    :param ParameterFilters: 

      Filters to limit the request results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **Option** *(string) --* 

          Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.

          

        
        - **Values** *(list) --* 

          The value you want to search for.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Parameters': [
                {
                    'Name': 'string',
                    'Type': 'String'|'StringList'|'SecureString',
                    'KeyId': 'string',
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'LastModifiedUser': 'string',
                    'Description': 'string',
                    'AllowedPattern': 'string',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Parameters** *(list) --* 

          Parameters returned by the request.

          
          

          - *(dict) --* 

            Metada includes information like the ARN of the last user and the date/time the parameter was last used.

            
            

            - **Name** *(string) --* 

              The parameter name.

              
            

            - **Type** *(string) --* 

              The type of parameter. Valid parameter types include the following: String, String list, Secure string.

              
            

            - **KeyId** *(string) --* 

              The ID of the query key used for this parameter.

              
            

            - **LastModifiedDate** *(datetime) --* 

              Date the parameter was last changed or updated.

              
            

            - **LastModifiedUser** *(string) --* 

              Amazon Resource Name (ARN) of the AWS user who last changed the parameter.

              
            

            - **Description** *(string) --* 

              Description of the parameter actions.

              
            

            - **AllowedPattern** *(string) --* 

              A parameter name can include only the following letters and symbols.

               

              a-zA-Z0-9_.-

              
            

            - **Version** *(integer) --* 

              The parameter version.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_patch_baselines(**kwargs)

    

    Lists the patch baselines in your AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchBaselines>`_    


    **Request Syntax** 
    ::

      response = client.describe_patch_baselines(
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type Filters: list
    :param Filters: 

      Each element in the array is a structure containing: 

       

      Key: (string, "NAME_PREFIX" or "OWNER")

       

      Value: (array of strings, exactly 1 entry, between 1 and 255 characters)

      

    
      - *(dict) --* 

        Defines a filter used in Patch Manager APIs.

        

      
        - **Key** *(string) --* 

          The key for the filter.

          

        
        - **Values** *(list) --* 

          The value for the filter.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of patch baselines to return (per page).

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineIdentities': [
                {
                    'BaselineId': 'string',
                    'BaselineName': 'string',
                    'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX',
                    'BaselineDescription': 'string',
                    'DefaultBaseline': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineIdentities** *(list) --* 

          An array of PatchBaselineIdentity elements.

          
          

          - *(dict) --* 

            Defines the basic information about a patch baseline.

            
            

            - **BaselineId** *(string) --* 

              The ID of the patch baseline.

              
            

            - **BaselineName** *(string) --* 

              The name of the patch baseline.

              
            

            - **OperatingSystem** *(string) --* 

              Defines the operating system the patch baseline applies to. The Default value is WINDOWS. 

              
            

            - **BaselineDescription** *(string) --* 

              The description of the patch baseline.

              
            

            - **DefaultBaseline** *(boolean) --* 

              Whether this is the default baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: describe_patch_group_state(**kwargs)

    

    Returns high-level aggregated patch compliance state for a patch group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchGroupState>`_    


    **Request Syntax** 
    ::

      response = client.describe_patch_group_state(
          PatchGroup='string'
      )
    :type PatchGroup: string
    :param PatchGroup: **[REQUIRED]** 

      The name of the patch group whose patch snapshot should be retrieved.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Instances': 123,
            'InstancesWithInstalledPatches': 123,
            'InstancesWithInstalledOtherPatches': 123,
            'InstancesWithMissingPatches': 123,
            'InstancesWithFailedPatches': 123,
            'InstancesWithNotApplicablePatches': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Instances** *(integer) --* 

          The number of instances in the patch group.

          
        

        - **InstancesWithInstalledPatches** *(integer) --* 

          The number of instances with installed patches.

          
        

        - **InstancesWithInstalledOtherPatches** *(integer) --* 

          The number of instances with patches installed that aren't defined in the patch baseline.

          
        

        - **InstancesWithMissingPatches** *(integer) --* 

          The number of instances with missing patches from the patch baseline.

          
        

        - **InstancesWithFailedPatches** *(integer) --* 

          The number of instances with patches from the patch baseline that failed to install.

          
        

        - **InstancesWithNotApplicablePatches** *(integer) --* 

          The number of instances with patches that aren't applicable.

          
    

  .. py:method:: describe_patch_groups(**kwargs)

    

    Lists all patch groups that have been registered with patch baselines.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_patch_groups(
          MaxResults=123,
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of patch groups to return (per page).

      

    
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        Defines a filter used in Patch Manager APIs.

        

      
        - **Key** *(string) --* 

          The key for the filter.

          

        
        - **Values** *(list) --* 

          The value for the filter.

          

        
          - *(string) --* 

          
      
      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Mappings': [
                {
                    'PatchGroup': 'string',
                    'BaselineIdentity': {
                        'BaselineId': 'string',
                        'BaselineName': 'string',
                        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX',
                        'BaselineDescription': 'string',
                        'DefaultBaseline': True|False
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Mappings** *(list) --* 

          Each entry in the array contains:

           

          PatchGroup: string (between 1 and 256 characters, Regex: ^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$)

           

          PatchBaselineIdentity: A PatchBaselineIdentity element. 

          
          

          - *(dict) --* 

            The mapping between a patch group and the patch baseline the patch group is registered with.

            
            

            - **PatchGroup** *(string) --* 

              The name of the patch group registered with the patch baseline.

              
            

            - **BaselineIdentity** *(dict) --* 

              The patch baseline the patch group is registered with.

              
              

              - **BaselineId** *(string) --* 

                The ID of the patch baseline.

                
              

              - **BaselineName** *(string) --* 

                The name of the patch baseline.

                
              

              - **OperatingSystem** *(string) --* 

                Defines the operating system the patch baseline applies to. The Default value is WINDOWS. 

                
              

              - **BaselineDescription** *(string) --* 

                The description of the patch baseline.

                
              

              - **DefaultBaseline** *(boolean) --* 

                Whether this is the default baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.

                
          
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

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


  .. py:method:: get_automation_execution(**kwargs)

    

    Get detailed information about a particular Automation execution.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetAutomationExecution>`_    


    **Request Syntax** 
    ::

      response = client.get_automation_execution(
          AutomationExecutionId='string'
      )
    :type AutomationExecutionId: string
    :param AutomationExecutionId: **[REQUIRED]** 

      The unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation document is initiated.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutomationExecution': {
                'AutomationExecutionId': 'string',
                'DocumentName': 'string',
                'DocumentVersion': 'string',
                'ExecutionStartTime': datetime(2015, 1, 1),
                'ExecutionEndTime': datetime(2015, 1, 1),
                'AutomationExecutionStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                'StepExecutions': [
                    {
                        'StepName': 'string',
                        'Action': 'string',
                        'TimeoutSeconds': 123,
                        'OnFailure': 'string',
                        'MaxAttempts': 123,
                        'ExecutionStartTime': datetime(2015, 1, 1),
                        'ExecutionEndTime': datetime(2015, 1, 1),
                        'StepStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                        'ResponseCode': 'string',
                        'Inputs': {
                            'string': 'string'
                        },
                        'Outputs': {
                            'string': [
                                'string',
                            ]
                        },
                        'Response': 'string',
                        'FailureMessage': 'string',
                        'FailureDetails': {
                            'FailureStage': 'string',
                            'FailureType': 'string',
                            'Details': {
                                'string': [
                                    'string',
                                ]
                            }
                        },
                        'StepExecutionId': 'string',
                        'OverriddenParameters': {
                            'string': [
                                'string',
                            ]
                        }
                    },
                ],
                'StepExecutionsTruncated': True|False,
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'Outputs': {
                    'string': [
                        'string',
                    ]
                },
                'FailureMessage': 'string',
                'Mode': 'Auto'|'Interactive',
                'ParentAutomationExecutionId': 'string',
                'ExecutedBy': 'string',
                'CurrentStepName': 'string',
                'CurrentAction': 'string',
                'TargetParameterName': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ResolvedTargets': {
                    'ParameterValues': [
                        'string',
                    ],
                    'Truncated': True|False
                },
                'MaxConcurrency': 'string',
                'MaxErrors': 'string',
                'Target': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AutomationExecution** *(dict) --* 

          Detailed information about the current state of an automation execution.

          
          

          - **AutomationExecutionId** *(string) --* 

            The execution ID.

            
          

          - **DocumentName** *(string) --* 

            The name of the Automation document used during the execution.

            
          

          - **DocumentVersion** *(string) --* 

            The version of the document to use during execution.

            
          

          - **ExecutionStartTime** *(datetime) --* 

            The time the execution started.

            
          

          - **ExecutionEndTime** *(datetime) --* 

            The time the execution finished.

            
          

          - **AutomationExecutionStatus** *(string) --* 

            The execution status of the Automation.

            
          

          - **StepExecutions** *(list) --* 

            A list of details about the current state of all steps that comprise an execution. An Automation document contains a list of steps that are executed in order.

            
            

            - *(dict) --* 

              Detailed information about an the execution state of an Automation step.

              
              

              - **StepName** *(string) --* 

                The name of this execution step.

                
              

              - **Action** *(string) --* 

                The action this step performs. The action determines the behavior of the step.

                
              

              - **TimeoutSeconds** *(integer) --* 

                The timeout seconds of the step.

                
              

              - **OnFailure** *(string) --* 

                The action to take if the step fails. The default value is Abort.

                
              

              - **MaxAttempts** *(integer) --* 

                The maximum number of tries to run the action of the step. The default value is 1.

                
              

              - **ExecutionStartTime** *(datetime) --* 

                If a step has begun execution, this contains the time the step started. If the step is in Pending status, this field is not populated.

                
              

              - **ExecutionEndTime** *(datetime) --* 

                If a step has finished execution, this contains the time the execution ended. If the step has not yet concluded, this field is not populated.

                
              

              - **StepStatus** *(string) --* 

                The execution status for this step. Valid values include: Pending, InProgress, Success, Cancelled, Failed, and TimedOut.

                
              

              - **ResponseCode** *(string) --* 

                The response code returned by the execution of the step.

                
              

              - **Inputs** *(dict) --* 

                Fully-resolved values passed into the step before execution.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Outputs** *(dict) --* 

                Returned values from the execution of the step.

                
                

                - *(string) --* 
                  

                  - *(list) --* 
                    

                    - *(string) --* 
                
            
          
              

              - **Response** *(string) --* 

                A message associated with the response code for an execution.

                
              

              - **FailureMessage** *(string) --* 

                If a step failed, this message explains why the execution failed.

                
              

              - **FailureDetails** *(dict) --* 

                Information about the Automation failure.

                
                

                - **FailureStage** *(string) --* 

                  The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.

                  
                

                - **FailureType** *(string) --* 

                  The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.

                  
                

                - **Details** *(dict) --* 

                  Detailed information about the Automation step failure.

                  
                  

                  - *(string) --* 
                    

                    - *(list) --* 
                      

                      - *(string) --* 
                  
              
            
            
              

              - **StepExecutionId** *(string) --* 

                The unique ID of a step execution.

                
              

              - **OverriddenParameters** *(dict) --* 

                A user-specified list of parameters to override when executing a step.

                
                

                - *(string) --* 
                  

                  - *(list) --* 
                    

                    - *(string) --* 
                
            
          
          
        
          

          - **StepExecutionsTruncated** *(boolean) --* 

            A boolean value that indicates if the response contains the full list of the Automation step executions. If true, use the DescribeAutomationStepExecutions API action to get the full list of step executions.

            
          

          - **Parameters** *(dict) --* 

            The key-value map of execution parameters, which were supplied when calling StartAutomationExecution.

            
            

            - *(string) --* 
              

              - *(list) --* 
                

                - *(string) --* 
            
        
      
          

          - **Outputs** *(dict) --* 

            The list of execution outputs as defined in the automation document.

            
            

            - *(string) --* 
              

              - *(list) --* 
                

                - *(string) --* 
            
        
      
          

          - **FailureMessage** *(string) --* 

            A message describing why an execution has failed, if the status is set to Failed.

            
          

          - **Mode** *(string) --* 

            The automation execution mode.

            
          

          - **ParentAutomationExecutionId** *(string) --* 

            The AutomationExecutionId of the parent automation.

            
          

          - **ExecutedBy** *(string) --* 

            The Amazon Resource Name (ARN) of the user who executed the automation.

            
          

          - **CurrentStepName** *(string) --* 

            The name of the currently executing step.

            
          

          - **CurrentAction** *(string) --* 

            The action of the currently executing step.

            
          

          - **TargetParameterName** *(string) --* 

            The parameter name.

            
          

          - **Targets** *(list) --* 

            The specified targets.

            
            

            - *(dict) --* 

              An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

               

              

              
              

              - **Key** *(string) --* 

                User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
              

              - **Values** *(list) --* 

                User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
                

                - *(string) --* 
            
          
        
          

          - **ResolvedTargets** *(dict) --* 

            A list of resolved targets in the rate control execution.

            
            

            - **ParameterValues** *(list) --* 

              A list of parameter values sent to targets that resolved during the Automation execution.

              
              

              - *(string) --* 
          
            

            - **Truncated** *(boolean) --* 

              A boolean value indicating whether the resolved target list is truncated.

              
        
          

          - **MaxConcurrency** *(string) --* 

            The MaxConcurrency value specified by the user when the execution started.

            
          

          - **MaxErrors** *(string) --* 

            The MaxErrors value specified by the user when the execution started.

            
          

          - **Target** *(string) --* 

            The target of the execution.

            
      
    

  .. py:method:: get_command_invocation(**kwargs)

    

    Returns detailed information about command execution for an invocation or plugin. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetCommandInvocation>`_    


    **Request Syntax** 
    ::

      response = client.get_command_invocation(
          CommandId='string',
          InstanceId='string',
          PluginName='string'
      )
    :type CommandId: string
    :param CommandId: **[REQUIRED]** 

      (Required) The parent command ID of the invocation plugin.

      

    
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      (Required) The ID of the managed instance targeted by the command. A managed instance can be an Amazon EC2 instance or an instance in your hybrid environment that is configured for Systems Manager.

      

    
    :type PluginName: string
    :param PluginName: 

      (Optional) The name of the plugin for which you want detailed results. If the document contains only one plugin, the name can be omitted and the details will be returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CommandId': 'string',
            'InstanceId': 'string',
            'Comment': 'string',
            'DocumentName': 'string',
            'PluginName': 'string',
            'ResponseCode': 123,
            'ExecutionStartDateTime': 'string',
            'ExecutionElapsedTime': 'string',
            'ExecutionEndDateTime': 'string',
            'Status': 'Pending'|'InProgress'|'Delayed'|'Success'|'Cancelled'|'TimedOut'|'Failed'|'Cancelling',
            'StatusDetails': 'string',
            'StandardOutputContent': 'string',
            'StandardOutputUrl': 'string',
            'StandardErrorContent': 'string',
            'StandardErrorUrl': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CommandId** *(string) --* 

          The parent command ID of the invocation plugin.

          
        

        - **InstanceId** *(string) --* 

          The ID of the managed instance targeted by the command. A managed instance can be an Amazon EC2 instance or an instance in your hybrid environment that is configured for Systems Manager.

          
        

        - **Comment** *(string) --* 

          The comment text for the command.

          
        

        - **DocumentName** *(string) --* 

          The name of the document that was executed. For example, AWS-RunShellScript.

          
        

        - **PluginName** *(string) --* 

          The name of the plugin for which you want detailed results. For example, aws:RunShellScript is a plugin.

          
        

        - **ResponseCode** *(integer) --* 

          The error level response code for the plugin script. If the response code is -1, then the command has not started executing on the instance, or it was not received by the instance.

          
        

        - **ExecutionStartDateTime** *(string) --* 

          The date and time the plugin started executing. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample AWS CLI command uses the ``InvokedBefore`` filter.

           

           ``aws ssm list-commands --filters key=InvokedBefore,value=2017-06-07T00:00:00Z``  

           

          If the plugin has not started to execute, the string is empty.

          
        

        - **ExecutionElapsedTime** *(string) --* 

          Duration since ExecutionStartDateTime.

          
        

        - **ExecutionEndDateTime** *(string) --* 

          The date and time the plugin was finished executing. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample AWS CLI command uses the ``InvokedAfter`` filter.

           

           ``aws ssm list-commands --filters key=InvokedAfter,value=2017-06-07T00:00:00Z``  

           

          If the plugin has not started to execute, the string is empty.

          
        

        - **Status** *(string) --* 

          The status of the parent command for this invocation. This status can be different than StatusDetails.

          
        

        - **StatusDetails** *(string) --* 

          A detailed status of the command execution for an invocation. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Run Command Status <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-about-status.html>`__ . StatusDetails can be one of the following values:

           

           
          * Pending: The command has not been sent to the instance. 
           
          * In Progress: The command has been sent to the instance but has not reached a terminal state. 
           
          * Delayed: The system attempted to send the command to the target, but the target was not available. The instance might not be available because of network issues, the instance was stopped, etc. The system will try to deliver the command again. 
           
          * Success: The command or plugin was executed successfully. This is a terminal state. 
           
          * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
           
          * Execution Timed Out: The command started to execute on the instance, but the execution was not complete before the timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
           
          * Failed: The command wasn't executed successfully on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
           
          * Canceled: The command was terminated before it was completed. This is a terminal state. 
           
          * Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
           
          * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
           

          
        

        - **StandardOutputContent** *(string) --* 

          The first 24,000 characters written by the plugin to stdout. If the command has not finished executing, if ExecutionStatus is neither Succeeded nor Failed, then this string is empty.

          
        

        - **StandardOutputUrl** *(string) --* 

          The URL for the complete text written by the plugin to stdout in Amazon S3. If an Amazon S3 bucket was not specified, then this string is empty.

          
        

        - **StandardErrorContent** *(string) --* 

          The first 8,000 characters written by the plugin to stderr. If the command has not finished executing, then this string is empty.

          
        

        - **StandardErrorUrl** *(string) --* 

          The URL for the complete text written by the plugin to stderr. If the command has not finished executing, then this string is empty.

          
    

  .. py:method:: get_default_patch_baseline(**kwargs)

    

    Retrieves the default patch baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetDefaultPatchBaseline>`_    


    **Request Syntax** 
    ::

      response = client.get_default_patch_baseline(
          OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'
      )
    :type OperatingSystem: string
    :param OperatingSystem: 

      Returns the default patch baseline for the specified operating system.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string',
            'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the default patch baseline.

          
        

        - **OperatingSystem** *(string) --* 

          The operating system for the returned patch baseline. 

          
    

  .. py:method:: get_deployable_patch_snapshot_for_instance(**kwargs)

    

    Retrieves the current snapshot for the patch baseline the instance uses. This API is primarily used by the AWS-RunPatchBaseline Systems Manager document. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance>`_    


    **Request Syntax** 
    ::

      response = client.get_deployable_patch_snapshot_for_instance(
          InstanceId='string',
          SnapshotId='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The ID of the instance for which the appropriate patch snapshot should be retrieved.

      

    
    :type SnapshotId: string
    :param SnapshotId: **[REQUIRED]** 

      The user-defined snapshot ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InstanceId': 'string',
            'SnapshotId': 'string',
            'SnapshotDownloadUrl': 'string',
            'Product': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **InstanceId** *(string) --* 

          The ID of the instance.

          
        

        - **SnapshotId** *(string) --* 

          The user-defined snapshot ID.

          
        

        - **SnapshotDownloadUrl** *(string) --* 

          A pre-signed Amazon S3 URL that can be used to download the patch snapshot.

          
        

        - **Product** *(string) --* 

          Returns the specific operating system (for example Windows Server 2012 or Amazon Linux 2015.09) on the instance for the specified patch snapshot.

          
    

  .. py:method:: get_document(**kwargs)

    

    Gets the contents of the specified Systems Manager document.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetDocument>`_    


    **Request Syntax** 
    ::

      response = client.get_document(
          Name='string',
          DocumentVersion='string',
          DocumentFormat='YAML'|'JSON'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the Systems Manager document.

      

    
    :type DocumentVersion: string
    :param DocumentVersion: 

      The document version for which you want information.

      

    
    :type DocumentFormat: string
    :param DocumentFormat: 

      Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string',
            'DocumentVersion': 'string',
            'Content': 'string',
            'DocumentType': 'Command'|'Policy'|'Automation',
            'DocumentFormat': 'YAML'|'JSON'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          The name of the Systems Manager document.

          
        

        - **DocumentVersion** *(string) --* 

          The document version.

          
        

        - **Content** *(string) --* 

          The contents of the Systems Manager document.

          
        

        - **DocumentType** *(string) --* 

          The document type.

          
        

        - **DocumentFormat** *(string) --* 

          The document format, either JSON or YAML.

          
    

  .. py:method:: get_inventory(**kwargs)

    

    Query inventory information.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetInventory>`_    


    **Request Syntax** 
    ::

      response = client.get_inventory(
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ],
                  'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'
              },
          ],
          Aggregators=[
              {
                  'Expression': 'string',
                  'Aggregators': {'... recursive ...'}
              },
          ],
          ResultAttributes=[
              {
                  'TypeName': 'string'
              },
          ],
          NextToken='string',
          MaxResults=123
      )
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The name of the filter key.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal 

          

        
          - *(string) --* 

          
      
        - **Type** *(string) --* 

          The type of filter. Valid values include the following: "Equal"|"NotEqual"|"BeginWith"|"LessThan"|"GreaterThan"

          

        
      
  
    :type Aggregators: list
    :param Aggregators: 

      Returns counts of inventory types based on one or more expressions. For example, if you aggregate by using an expression that uses the ``AWS:InstanceInformation.PlatformType`` type, you can see a count of how many Windows and Linux instances exist in your inventoried fleet.

      

    
      - *(dict) --* 

        Specifies the inventory type and attribute for the aggregation execution.

        

      
        - **Expression** *(string) --* 

          The inventory type and attribute name for aggregation.

          

        
        - **Aggregators** *(list) --* 

          Nested aggregators to further refine aggregation for an inventory type.

          

        
      
  
    :type ResultAttributes: list
    :param ResultAttributes: 

      The list of inventory item types to return.

      

    
      - *(dict) --* 

        The inventory item result attribute.

        

      
        - **TypeName** *(string) --* **[REQUIRED]** 

          Name of the inventory item type. Valid value: AWS:InstanceInformation. Default Value: AWS:InstanceInformation.

          

        
      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Entities': [
                {
                    'Id': 'string',
                    'Data': {
                        'string': {
                            'TypeName': 'string',
                            'SchemaVersion': 'string',
                            'CaptureTime': 'string',
                            'ContentHash': 'string',
                            'Content': [
                                {
                                    'string': 'string'
                                },
                            ]
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Entities** *(list) --* 

          Collection of inventory entities such as a collection of instance inventory. 

          
          

          - *(dict) --* 

            Inventory query results.

            
            

            - **Id** *(string) --* 

              ID of the inventory result entity. For example, for managed instance inventory the result will be the managed instance ID. For EC2 instance inventory, the result will be the instance ID. 

              
            

            - **Data** *(dict) --* 

              The data section in the inventory result entity JSON.

              
              

              - *(string) --* 
                

                - *(dict) --* 

                  The inventory result item.

                  
                  

                  - **TypeName** *(string) --* 

                    The name of the inventory result item type.

                    
                  

                  - **SchemaVersion** *(string) --* 

                    The schema version for the inventory result item/

                    
                  

                  - **CaptureTime** *(string) --* 

                    The time inventory item data was captured.

                    
                  

                  - **ContentHash** *(string) --* 

                    MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API does not update the inventory item type contents if the MD5 hash has not changed since last update. 

                    
                  

                  - **Content** *(list) --* 

                    Contains all the inventory data of the item type. Results include attribute names and values. 

                    
                    

                    - *(dict) --* 
                      

                      - *(string) --* 
                        

                        - *(string) --* 
                  
                
                
              
          
        
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: get_inventory_schema(**kwargs)

    

    Return a list of inventory type names for the account, or return a list of attribute names for a specific Inventory item type. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetInventorySchema>`_    


    **Request Syntax** 
    ::

      response = client.get_inventory_schema(
          TypeName='string',
          NextToken='string',
          MaxResults=123,
          Aggregator=True|False,
          SubType=True|False
      )
    :type TypeName: string
    :param TypeName: 

      The type of inventory item to return.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type Aggregator: boolean
    :param Aggregator: 

      Returns inventory schemas that support aggregation. For example, this call returns the ``AWS:InstanceInformation`` type, because it supports aggregation based on the ``PlatformName`` , ``PlatformType`` , and ``PlatformVersion`` attributes.

      

    
    :type SubType: boolean
    :param SubType: 

      Returns the sub-type schema for a specified inventory type.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Schemas': [
                {
                    'TypeName': 'string',
                    'Version': 'string',
                    'Attributes': [
                        {
                            'Name': 'string',
                            'DataType': 'string'|'number'
                        },
                    ],
                    'DisplayName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Schemas** *(list) --* 

          Inventory schemas returned by the request.

          
          

          - *(dict) --* 

            The inventory item schema definition. Users can use this to compose inventory query filters.

            
            

            - **TypeName** *(string) --* 

              The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and AWS:WindowsUpdate.

              
            

            - **Version** *(string) --* 

              The schema version for the inventory item.

              
            

            - **Attributes** *(list) --* 

              The schema attributes for inventory. This contains data type and attribute name.

              
              

              - *(dict) --* 

                Attributes are the entries within the inventory item content. It contains name and value.

                
                

                - **Name** *(string) --* 

                  Name of the inventory item attribute.

                  
                

                - **DataType** *(string) --* 

                  The data type of the inventory item attribute. 

                  
            
          
            

            - **DisplayName** *(string) --* 

              The alias name of the inventory type. The alias name is used for display purposes.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: get_maintenance_window(**kwargs)

    

    Retrieves a Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindow>`_    


    **Request Syntax** 
    ::

      response = client.get_maintenance_window(
          WindowId='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the desired Maintenance Window.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string',
            'Name': 'string',
            'Description': 'string',
            'Schedule': 'string',
            'Duration': 123,
            'Cutoff': 123,
            'AllowUnassociatedTargets': True|False,
            'Enabled': True|False,
            'CreatedDate': datetime(2015, 1, 1),
            'ModifiedDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The ID of the created Maintenance Window.

          
        

        - **Name** *(string) --* 

          The name of the Maintenance Window.

          
        

        - **Description** *(string) --* 

          The description of the Maintenance Window.

          
        

        - **Schedule** *(string) --* 

          The schedule of the Maintenance Window in the form of a cron or rate expression.

          
        

        - **Duration** *(integer) --* 

          The duration of the Maintenance Window in hours.

          
        

        - **Cutoff** *(integer) --* 

          The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

          
        

        - **AllowUnassociatedTargets** *(boolean) --* 

          Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.

          
        

        - **Enabled** *(boolean) --* 

          Whether the Maintenance Windows is enabled.

          
        

        - **CreatedDate** *(datetime) --* 

          The date the Maintenance Window was created.

          
        

        - **ModifiedDate** *(datetime) --* 

          The date the Maintenance Window was last modified.

          
    

  .. py:method:: get_maintenance_window_execution(**kwargs)

    

    Retrieves details about a specific task executed as part of a Maintenance Window execution.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindowExecution>`_    


    **Request Syntax** 
    ::

      response = client.get_maintenance_window_execution(
          WindowExecutionId='string'
      )
    :type WindowExecutionId: string
    :param WindowExecutionId: **[REQUIRED]** 

      The ID of the Maintenance Window execution that includes the task.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowExecutionId': 'string',
            'TaskIds': [
                'string',
            ],
            'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
            'StatusDetails': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowExecutionId** *(string) --* 

          The ID of the Maintenance Window execution.

          
        

        - **TaskIds** *(list) --* 

          The ID of the task executions from the Maintenance Window execution.

          
          

          - *(string) --* 
      
        

        - **Status** *(string) --* 

          The status of the Maintenance Window execution.

          
        

        - **StatusDetails** *(string) --* 

          The details explaining the Status. Only available for certain status values.

          
        

        - **StartTime** *(datetime) --* 

          The time the Maintenance Window started executing.

          
        

        - **EndTime** *(datetime) --* 

          The time the Maintenance Window finished executing.

          
    

  .. py:method:: get_maintenance_window_execution_task(**kwargs)

    

    Retrieves the details about a specific task executed as part of a Maintenance Window execution.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindowExecutionTask>`_    


    **Request Syntax** 
    ::

      response = client.get_maintenance_window_execution_task(
          WindowExecutionId='string',
          TaskId='string'
      )
    :type WindowExecutionId: string
    :param WindowExecutionId: **[REQUIRED]** 

      The ID of the Maintenance Window execution that includes the task.

      

    
    :type TaskId: string
    :param TaskId: **[REQUIRED]** 

      The ID of the specific task execution in the Maintenance Window task that should be retrieved.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowExecutionId': 'string',
            'TaskExecutionId': 'string',
            'TaskArn': 'string',
            'ServiceRole': 'string',
            'Type': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
            'TaskParameters': [
                {
                    'string': {
                        'Values': [
                            'string',
                        ]
                    }
                },
            ],
            'Priority': 123,
            'MaxConcurrency': 'string',
            'MaxErrors': 'string',
            'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
            'StatusDetails': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowExecutionId** *(string) --* 

          The ID of the Maintenance Window execution that includes the task.

          
        

        - **TaskExecutionId** *(string) --* 

          The ID of the specific task execution in the Maintenance Window task that was retrieved.

          
        

        - **TaskArn** *(string) --* 

          The ARN of the executed task.

          
        

        - **ServiceRole** *(string) --* 

          The role that was assumed when executing the task.

          
        

        - **Type** *(string) --* 

          The type of task executed.

          
        

        - **TaskParameters** *(list) --* 

          The parameters passed to the task when it was executed. The map has the following format:

           

          Key: string, between 1 and 255 characters

           

          Value: an array of strings, each string is between 1 and 255 characters

          
          

          - *(dict) --* 
            

            - *(string) --* 
              

              - *(dict) --* 

                Defines the values for a task parameter.

                
                

                - **Values** *(list) --* 

                  This field contains an array of 0 or more strings, each 1 to 255 characters in length.

                  
                  

                  - *(string) --* 
              
            
        
      
      
        

        - **Priority** *(integer) --* 

          The priority of the task.

          
        

        - **MaxConcurrency** *(string) --* 

          The defined maximum number of task executions that could be run in parallel.

          
        

        - **MaxErrors** *(string) --* 

          The defined maximum number of task execution errors allowed before scheduling of the task execution would have been stopped.

          
        

        - **Status** *(string) --* 

          The status of the task.

          
        

        - **StatusDetails** *(string) --* 

          The details explaining the Status. Only available for certain status values.

          
        

        - **StartTime** *(datetime) --* 

          The time the task execution started.

          
        

        - **EndTime** *(datetime) --* 

          The time the task execution completed.

          
    

  .. py:method:: get_maintenance_window_execution_task_invocation(**kwargs)

    

    Retrieves a task invocation. A task invocation is a specific task executing on a specific target. Maintenance Windows report status for all invocations. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation>`_    


    **Request Syntax** 
    ::

      response = client.get_maintenance_window_execution_task_invocation(
          WindowExecutionId='string',
          TaskId='string',
          InvocationId='string'
      )
    :type WindowExecutionId: string
    :param WindowExecutionId: **[REQUIRED]** 

      The ID of the Maintenance Window execution for which the task is a part.

      

    
    :type TaskId: string
    :param TaskId: **[REQUIRED]** 

      The ID of the specific task in the Maintenance Window task that should be retrieved. 

      

    
    :type InvocationId: string
    :param InvocationId: **[REQUIRED]** 

      The invocation ID to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowExecutionId': 'string',
            'TaskExecutionId': 'string',
            'InvocationId': 'string',
            'ExecutionId': 'string',
            'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
            'Parameters': 'string',
            'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
            'StatusDetails': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'OwnerInformation': 'string',
            'WindowTargetId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowExecutionId** *(string) --* 

          The Maintenance Window execution ID.

          
        

        - **TaskExecutionId** *(string) --* 

          The task execution ID.

          
        

        - **InvocationId** *(string) --* 

          The invocation ID.

          
        

        - **ExecutionId** *(string) --* 

          The execution ID.

          
        

        - **TaskType** *(string) --* 

          Retrieves the task type for a Maintenance Window. Task types include the following: LAMBDA, STEP_FUNCTION, AUTOMATION, RUN_COMMAND.

          
        

        - **Parameters** *(string) --* 

          The parameters used at the time that the task executed.

          
        

        - **Status** *(string) --* 

          The task status for an invocation.

          
        

        - **StatusDetails** *(string) --* 

          The details explaining the status. Details are only available for certain status values.

          
        

        - **StartTime** *(datetime) --* 

          The time that the task started executing on the target.

          
        

        - **EndTime** *(datetime) --* 

          The time that the task finished executing on the target.

          
        

        - **OwnerInformation** *(string) --* 

          User-provided value to be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window. 

          
        

        - **WindowTargetId** *(string) --* 

          The Maintenance Window target ID.

          
    

  .. py:method:: get_maintenance_window_task(**kwargs)

    

    Lists the tasks in a Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindowTask>`_    


    **Request Syntax** 
    ::

      response = client.get_maintenance_window_task(
          WindowId='string',
          WindowTaskId='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The Maintenance Window ID that includes the task to retrieve.

      

    
    :type WindowTaskId: string
    :param WindowTaskId: **[REQUIRED]** 

      The Maintenance Window task ID to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string',
            'WindowTaskId': 'string',
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'TaskArn': 'string',
            'ServiceRoleArn': 'string',
            'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
            'TaskParameters': {
                'string': {
                    'Values': [
                        'string',
                    ]
                }
            },
            'TaskInvocationParameters': {
                'RunCommand': {
                    'Comment': 'string',
                    'DocumentHash': 'string',
                    'DocumentHashType': 'Sha256'|'Sha1',
                    'NotificationConfig': {
                        'NotificationArn': 'string',
                        'NotificationEvents': [
                            'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                        ],
                        'NotificationType': 'Command'|'Invocation'
                    },
                    'OutputS3BucketName': 'string',
                    'OutputS3KeyPrefix': 'string',
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    },
                    'ServiceRoleArn': 'string',
                    'TimeoutSeconds': 123
                },
                'Automation': {
                    'DocumentVersion': 'string',
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'StepFunctions': {
                    'Input': 'string',
                    'Name': 'string'
                },
                'Lambda': {
                    'ClientContext': 'string',
                    'Qualifier': 'string',
                    'Payload': b'bytes'
                }
            },
            'Priority': 123,
            'MaxConcurrency': 'string',
            'MaxErrors': 'string',
            'LoggingInfo': {
                'S3BucketName': 'string',
                'S3KeyPrefix': 'string',
                'S3Region': 'string'
            },
            'Name': 'string',
            'Description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The retrieved Maintenance Window ID.

          
        

        - **WindowTaskId** *(string) --* 

          The retrieved Maintenance Window task ID.

          
        

        - **Targets** *(list) --* 

          The targets where the task should execute.

          
          

          - *(dict) --* 

            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

             

            

            
            

            - **Key** *(string) --* 

              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

              
            

            - **Values** *(list) --* 

              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

              
              

              - *(string) --* 
          
        
      
        

        - **TaskArn** *(string) --* 

          The resource that the task used during execution. For RUN_COMMAND and AUTOMATION task types, the TaskArn is the Systems Manager Document name/ARN. For LAMBDA tasks, the value is the function name/ARN. For STEP_FUNCTION tasks, the value is the state machine ARN.

          
        

        - **ServiceRoleArn** *(string) --* 

          The IAM service role to assume during task execution.

          
        

        - **TaskType** *(string) --* 

          The type of task to execute.

          
        

        - **TaskParameters** *(dict) --* 

          The parameters to pass to the task when it executes.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Defines the values for a task parameter.

              
              

              - **Values** *(list) --* 

                This field contains an array of 0 or more strings, each 1 to 255 characters in length.

                
                

                - *(string) --* 
            
          
      
    
        

        - **TaskInvocationParameters** *(dict) --* 

          The parameters to pass to the task when it executes.

          
          

          - **RunCommand** *(dict) --* 

            The parameters for a RUN_COMMAND task type.

            
            

            - **Comment** *(string) --* 

              Information about the command(s) to execute.

              
            

            - **DocumentHash** *(string) --* 

              The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.

              
            

            - **DocumentHashType** *(string) --* 

              SHA-256 or SHA-1. SHA-1 hashes have been deprecated.

              
            

            - **NotificationConfig** *(dict) --* 

              Configurations for sending notifications about command status changes on a per-instance basis.

              
              

              - **NotificationArn** *(string) --* 

                An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

                
              

              - **NotificationEvents** *(list) --* 

                The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

                
                

                - *(string) --* 
            
              

              - **NotificationType** *(string) --* 

                Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

                
          
            

            - **OutputS3BucketName** *(string) --* 

              The name of the Amazon S3 bucket.

              
            

            - **OutputS3KeyPrefix** *(string) --* 

              The Amazon S3 bucket subfolder.

              
            

            - **Parameters** *(dict) --* 

              The parameters for the RUN_COMMAND task execution.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
            

            - **ServiceRoleArn** *(string) --* 

              The IAM service role to assume during task execution.

              
            

            - **TimeoutSeconds** *(integer) --* 

              If this time is reached and the command has not already started executing, it doesn not execute.

              
        
          

          - **Automation** *(dict) --* 

            The parameters for a AUTOMATION task type.

            
            

            - **DocumentVersion** *(string) --* 

              The version of an Automation document to use during task execution.

              
            

            - **Parameters** *(dict) --* 

              The parameters for the AUTOMATION task.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
        
          

          - **StepFunctions** *(dict) --* 

            The parameters for a STEP_FUNCTION task type.

            
            

            - **Input** *(string) --* 

              The inputs for the STEP_FUNCTION task.

              
            

            - **Name** *(string) --* 

              The name of the STEP_FUNCTION task.

              
        
          

          - **Lambda** *(dict) --* 

            The parameters for a LAMBDA task type.

            
            

            - **ClientContext** *(string) --* 

              Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.

              
            

            - **Qualifier** *(string) --* 

              (Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.

              
            

            - **Payload** *(bytes) --* 

              JSON to provide to your Lambda function as input.

              
        
      
        

        - **Priority** *(integer) --* 

          The priority of the task when it executes. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

          
        

        - **MaxConcurrency** *(string) --* 

          The maximum number of targets allowed to run this task in parallel.

          
        

        - **MaxErrors** *(string) --* 

          The maximum number of errors allowed before the task stops being scheduled.

          
        

        - **LoggingInfo** *(dict) --* 

          The location in Amazon S3 where the task results are logged.

          
          

          - **S3BucketName** *(string) --* 

            The name of an Amazon S3 bucket where execution logs are stored .

            
          

          - **S3KeyPrefix** *(string) --* 

            (Optional) The Amazon S3 bucket subfolder. 

            
          

          - **S3Region** *(string) --* 

            The region where the Amazon S3 bucket is located.

            
      
        

        - **Name** *(string) --* 

          The retrieved task name.

          
        

        - **Description** *(string) --* 

          The retrieved task description.

          
    

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


  .. py:method:: get_parameter(**kwargs)

    

    Get information about a parameter by using the parameter name. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParameter>`_    


    **Request Syntax** 
    ::

      response = client.get_parameter(
          Name='string',
          WithDecryption=True|False
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the parameter you want to query.

      

    
    :type WithDecryption: boolean
    :param WithDecryption: 

      Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Parameter': {
                'Name': 'string',
                'Type': 'String'|'StringList'|'SecureString',
                'Value': 'string',
                'Version': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Parameter** *(dict) --* 

          Information about a parameter.

          
          

          - **Name** *(string) --* 

            The name of the parameter.

            
          

          - **Type** *(string) --* 

            The type of parameter. Valid values include the following: String, String list, Secure string.

            
          

          - **Value** *(string) --* 

            The parameter value.

            
          

          - **Version** *(integer) --* 

            The parameter version.

            
      
    

  .. py:method:: get_parameter_history(**kwargs)

    

    Query a list of all parameters used by the AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParameterHistory>`_    


    **Request Syntax** 
    ::

      response = client.get_parameter_history(
          Name='string',
          WithDecryption=True|False,
          MaxResults=123,
          NextToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of a parameter you want to query.

      

    
    :type WithDecryption: boolean
    :param WithDecryption: 

      Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Parameters': [
                {
                    'Name': 'string',
                    'Type': 'String'|'StringList'|'SecureString',
                    'KeyId': 'string',
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'LastModifiedUser': 'string',
                    'Description': 'string',
                    'Value': 'string',
                    'AllowedPattern': 'string',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Parameters** *(list) --* 

          A list of parameters returned by the request.

          
          

          - *(dict) --* 

            Information about parameter usage.

            
            

            - **Name** *(string) --* 

              The name of the parameter.

              
            

            - **Type** *(string) --* 

              The type of parameter used.

              
            

            - **KeyId** *(string) --* 

              The ID of the query key used for this parameter.

              
            

            - **LastModifiedDate** *(datetime) --* 

              Date the parameter was last changed or updated.

              
            

            - **LastModifiedUser** *(string) --* 

              Amazon Resource Name (ARN) of the AWS user who last changed the parameter.

              
            

            - **Description** *(string) --* 

              Information about the parameter.

              
            

            - **Value** *(string) --* 

              The parameter value.

              
            

            - **AllowedPattern** *(string) --* 

              Parameter names can include the following letters and symbols.

               

              a-zA-Z0-9_.-

              
            

            - **Version** *(integer) --* 

              The parameter version.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: get_parameters(**kwargs)

    

    Get details of a parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParameters>`_    


    **Request Syntax** 
    ::

      response = client.get_parameters(
          Names=[
              'string',
          ],
          WithDecryption=True|False
      )
    :type Names: list
    :param Names: **[REQUIRED]** 

      Names of the parameters for which you want to query information.

      

    
      - *(string) --* 

      
  
    :type WithDecryption: boolean
    :param WithDecryption: 

      Return decrypted secure string value. Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Parameters': [
                {
                    'Name': 'string',
                    'Type': 'String'|'StringList'|'SecureString',
                    'Value': 'string',
                    'Version': 123
                },
            ],
            'InvalidParameters': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Parameters** *(list) --* 

          A list of details for a parameter.

          
          

          - *(dict) --* 

            An Amazon EC2 Systems Manager parameter in Parameter Store.

            
            

            - **Name** *(string) --* 

              The name of the parameter.

              
            

            - **Type** *(string) --* 

              The type of parameter. Valid values include the following: String, String list, Secure string.

              
            

            - **Value** *(string) --* 

              The parameter value.

              
            

            - **Version** *(integer) --* 

              The parameter version.

              
        
      
        

        - **InvalidParameters** *(list) --* 

          A list of parameters that are not formatted correctly or do not run when executed.

          
          

          - *(string) --* 
      
    

  .. py:method:: get_parameters_by_path(**kwargs)

    

    Retrieve parameters in a specific hierarchy. For more information, see `Working with Systems Manager Parameters <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-working.html>`__ . 

     

    Request results are returned on a best-effort basis. If you specify ``MaxResults`` in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of ``MaxResults`` . If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a ``NextToken`` . You can specify the ``NextToken`` in a subsequent call to get the next set of results.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParametersByPath>`_    


    **Request Syntax** 
    ::

      response = client.get_parameters_by_path(
          Path='string',
          Recursive=True|False,
          ParameterFilters=[
              {
                  'Key': 'string',
                  'Option': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          WithDecryption=True|False,
          MaxResults=123,
          NextToken='string'
      )
    :type Path: string
    :param Path: **[REQUIRED]** 

      The hierarchy for the parameter. Hierarchies start with a forward slash (/) and end with the parameter name. A hierarchy can have a maximum of five levels. For example: ``/Finance/Prod/IAD/WinServ2016/license15``  

      

    
    :type Recursive: boolean
    :param Recursive: 

      Retrieve all parameters within a hierarchy.

      

    
    :type ParameterFilters: list
    :param ParameterFilters: 

      Filters to limit the request results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **Option** *(string) --* 

          Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.

          

        
        - **Values** *(list) --* 

          The value you want to search for.

          

        
          - *(string) --* 

          
      
      
  
    :type WithDecryption: boolean
    :param WithDecryption: 

      Retrieve all parameters in a hierarchy with their value decrypted.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      A token to start the list. Use this token to get the next set of results. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Parameters': [
                {
                    'Name': 'string',
                    'Type': 'String'|'StringList'|'SecureString',
                    'Value': 'string',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Parameters** *(list) --* 

          A list of parameters found in the specified hierarchy.

          
          

          - *(dict) --* 

            An Amazon EC2 Systems Manager parameter in Parameter Store.

            
            

            - **Name** *(string) --* 

              The name of the parameter.

              
            

            - **Type** *(string) --* 

              The type of parameter. Valid values include the following: String, String list, Secure string.

              
            

            - **Value** *(string) --* 

              The parameter value.

              
            

            - **Version** *(integer) --* 

              The parameter version.

              
        
      
        

        - **NextToken** *(string) --* 

          The token for the next set of items to return. Use this token to get the next set of results.

          
    

  .. py:method:: get_patch_baseline(**kwargs)

    

    Retrieves information about a patch baseline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetPatchBaseline>`_    


    **Request Syntax** 
    ::

      response = client.get_patch_baseline(
          BaselineId='string'
      )
    :type BaselineId: string
    :param BaselineId: **[REQUIRED]** 

      The ID of the patch baseline to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string',
            'Name': 'string',
            'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX',
            'GlobalFilters': {
                'PatchFilters': [
                    {
                        'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                        'Values': [
                            'string',
                        ]
                    },
                ]
            },
            'ApprovalRules': {
                'PatchRules': [
                    {
                        'PatchFilterGroup': {
                            'PatchFilters': [
                                {
                                    'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                    'Values': [
                                        'string',
                                    ]
                                },
                            ]
                        },
                        'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                        'ApproveAfterDays': 123
                    },
                ]
            },
            'ApprovedPatches': [
                'string',
            ],
            'ApprovedPatchesComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
            'RejectedPatches': [
                'string',
            ],
            'PatchGroups': [
                'string',
            ],
            'CreatedDate': datetime(2015, 1, 1),
            'ModifiedDate': datetime(2015, 1, 1),
            'Description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the retrieved patch baseline.

          
        

        - **Name** *(string) --* 

          The name of the patch baseline.

          
        

        - **OperatingSystem** *(string) --* 

          Returns the operating system specified for the patch baseline.

          
        

        - **GlobalFilters** *(dict) --* 

          A set of global filters used to exclude patches from the baseline.

          
          

          - **PatchFilters** *(list) --* 

            The set of patch filters that make up the group.

            
            

            - *(dict) --* 

              Defines a patch filter.

              
              

              - **Key** *(string) --* 

                The key for the filter (PRODUCT, CLASSIFICATION, MSRC_SEVERITY, PATCH_ID)

                
              

              - **Values** *(list) --* 

                The value for the filter key.

                
                

                - *(string) --* 
            
          
        
      
        

        - **ApprovalRules** *(dict) --* 

          A set of rules used to include patches in the baseline.

          
          

          - **PatchRules** *(list) --* 

            The rules that make up the rule group.

            
            

            - *(dict) --* 

              Defines an approval rule for a patch baseline.

              
              

              - **PatchFilterGroup** *(dict) --* 

                The patch filter group that defines the criteria for the rule.

                
                

                - **PatchFilters** *(list) --* 

                  The set of patch filters that make up the group.

                  
                  

                  - *(dict) --* 

                    Defines a patch filter.

                    
                    

                    - **Key** *(string) --* 

                      The key for the filter (PRODUCT, CLASSIFICATION, MSRC_SEVERITY, PATCH_ID)

                      
                    

                    - **Values** *(list) --* 

                      The value for the filter key.

                      
                      

                      - *(string) --* 
                  
                
              
            
              

              - **ComplianceLevel** *(string) --* 

                A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.

                
              

              - **ApproveAfterDays** *(integer) --* 

                The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline.

                
          
        
      
        

        - **ApprovedPatches** *(list) --* 

          A list of explicitly approved patches for the baseline.

          
          

          - *(string) --* 
      
        

        - **ApprovedPatchesComplianceLevel** *(string) --* 

          Returns the specified compliance severity level for approved patches in the patch baseline.

          
        

        - **RejectedPatches** *(list) --* 

          A list of explicitly rejected patches for the baseline.

          
          

          - *(string) --* 
      
        

        - **PatchGroups** *(list) --* 

          Patch groups included in the patch baseline.

          
          

          - *(string) --* 
      
        

        - **CreatedDate** *(datetime) --* 

          The date the patch baseline was created.

          
        

        - **ModifiedDate** *(datetime) --* 

          The date the patch baseline was last modified.

          
        

        - **Description** *(string) --* 

          A description of the patch baseline.

          
    

  .. py:method:: get_patch_baseline_for_patch_group(**kwargs)

    

    Retrieves the patch baseline that should be used for the specified patch group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetPatchBaselineForPatchGroup>`_    


    **Request Syntax** 
    ::

      response = client.get_patch_baseline_for_patch_group(
          PatchGroup='string',
          OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'
      )
    :type PatchGroup: string
    :param PatchGroup: **[REQUIRED]** 

      The name of the patch group whose patch baseline should be retrieved.

      

    
    :type OperatingSystem: string
    :param OperatingSystem: 

      Returns he operating system rule specified for patch groups using the patch baseline.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string',
            'PatchGroup': 'string',
            'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the patch baseline that should be used for the patch group.

          
        

        - **PatchGroup** *(string) --* 

          The name of the patch group.

          
        

        - **OperatingSystem** *(string) --* 

          The operating system rule specified for patch groups using the patch baseline.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_association_versions(**kwargs)

    

    Retrieves all versions of an association for a specific association ID.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListAssociationVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_association_versions(
          AssociationId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type AssociationId: string
    :param AssociationId: **[REQUIRED]** 

      The association ID for which you want to view all versions.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      A token to start the list. Use this token to get the next set of results. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociationVersions': [
                {
                    'AssociationId': 'string',
                    'AssociationVersion': 'string',
                    'CreatedDate': datetime(2015, 1, 1),
                    'Name': 'string',
                    'DocumentVersion': 'string',
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    },
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'ScheduleExpression': 'string',
                    'OutputLocation': {
                        'S3Location': {
                            'OutputS3Region': 'string',
                            'OutputS3BucketName': 'string',
                            'OutputS3KeyPrefix': 'string'
                        }
                    },
                    'AssociationName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AssociationVersions** *(list) --* 

          Information about all versions of the association for the specified association ID.

          
          

          - *(dict) --* 

            Information about the association version.

            
            

            - **AssociationId** *(string) --* 

              The ID created by the system when the association was created.

              
            

            - **AssociationVersion** *(string) --* 

              The association version.

              
            

            - **CreatedDate** *(datetime) --* 

              The date the association version was created.

              
            

            - **Name** *(string) --* 

              The name specified when the association was created.

              
            

            - **DocumentVersion** *(string) --* 

              The version of a Systems Manager document used when the association version was created.

              
            

            - **Parameters** *(dict) --* 

              Parameters specified when the association version was created.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
            

            - **Targets** *(list) --* 

              The targets specified for the association when the association version was created. 

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **ScheduleExpression** *(string) --* 

              The cron or rate schedule specified for the association when the association version was created.

              
            

            - **OutputLocation** *(dict) --* 

              The location in Amazon S3 specified for the association when the association version was created.

              
              

              - **S3Location** *(dict) --* 

                An Amazon S3 bucket where you want to store the results of this request.

                
                

                - **OutputS3Region** *(string) --* 

                  (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                  
                

                - **OutputS3BucketName** *(string) --* 

                  The name of the Amazon S3 bucket.

                  
                

                - **OutputS3KeyPrefix** *(string) --* 

                  The Amazon S3 bucket subfolder.

                  
            
          
            

            - **AssociationName** *(string) --* 

              The name specified for the association version when the association version was created.

              
        
      
        

        - **NextToken** *(string) --* 

          The token for the next set of items to return. Use this token to get the next set of results.

          
    

  .. py:method:: list_associations(**kwargs)

    

    Lists the associations for the specified Systems Manager document or instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListAssociations>`_    


    **Request Syntax** 
    ::

      response = client.list_associations(
          AssociationFilterList=[
              {
                  'key': 'InstanceId'|'Name'|'AssociationId'|'AssociationStatusName'|'LastExecutedBefore'|'LastExecutedAfter'|'AssociationName',
                  'value': 'string'
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type AssociationFilterList: list
    :param AssociationFilterList: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        Describes a filter.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The filter value.

          

        
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Associations': [
                {
                    'Name': 'string',
                    'InstanceId': 'string',
                    'AssociationId': 'string',
                    'AssociationVersion': 'string',
                    'DocumentVersion': 'string',
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'LastExecutionDate': datetime(2015, 1, 1),
                    'Overview': {
                        'Status': 'string',
                        'DetailedStatus': 'string',
                        'AssociationStatusAggregatedCount': {
                            'string': 123
                        }
                    },
                    'ScheduleExpression': 'string',
                    'AssociationName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Associations** *(list) --* 

          The associations.

          
          

          - *(dict) --* 

            Describes an association of a Systems Manager document and an instance.

            
            

            - **Name** *(string) --* 

              The name of the Systems Manager document.

              
            

            - **InstanceId** *(string) --* 

              The ID of the instance.

              
            

            - **AssociationId** *(string) --* 

              The ID created by the system when you create an association. An association is a binding between a document and a set of targets with a schedule.

              
            

            - **AssociationVersion** *(string) --* 

              The association version.

              
            

            - **DocumentVersion** *(string) --* 

              The version of the document used in the association.

              
            

            - **Targets** *(list) --* 

              The instances targeted by the request to create an association. 

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **LastExecutionDate** *(datetime) --* 

              The date on which the association was last run.

              
            

            - **Overview** *(dict) --* 

              Information about the association.

              
              

              - **Status** *(string) --* 

                The status of the association. Status can be: Pending, Success, or Failed.

                
              

              - **DetailedStatus** *(string) --* 

                A detailed status of the association.

                
              

              - **AssociationStatusAggregatedCount** *(dict) --* 

                Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

                
                

                - *(string) --* 
                  

                  - *(integer) --* 
            
          
          
            

            - **ScheduleExpression** *(string) --* 

              A cron expression that specifies a schedule when the association runs.

              
            

            - **AssociationName** *(string) --* 

              The association name.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: list_command_invocations(**kwargs)

    

    An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user executes SendCommand against three instances, then a command invocation is created for each requested instance ID. ListCommandInvocations provide status about command execution.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommandInvocations>`_    


    **Request Syntax** 
    ::

      response = client.list_command_invocations(
          CommandId='string',
          InstanceId='string',
          MaxResults=123,
          NextToken='string',
          Filters=[
              {
                  'key': 'InvokedAfter'|'InvokedBefore'|'Status',
                  'value': 'string'
              },
          ],
          Details=True|False
      )
    :type CommandId: string
    :param CommandId: 

      (Optional) The invocations for a specific command ID.

      

    
    :type InstanceId: string
    :param InstanceId: 

      (Optional) The command execution details for a specific instance ID.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      (Optional) The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type Filters: list
    :param Filters: 

      (Optional) One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        Describes a command filter.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The filter value. 

          

        
      
  
    :type Details: boolean
    :param Details: 

      (Optional) If set this returns the response of the command executions and any command output. By default this is set to False. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CommandInvocations': [
                {
                    'CommandId': 'string',
                    'InstanceId': 'string',
                    'InstanceName': 'string',
                    'Comment': 'string',
                    'DocumentName': 'string',
                    'RequestedDateTime': datetime(2015, 1, 1),
                    'Status': 'Pending'|'InProgress'|'Delayed'|'Success'|'Cancelled'|'TimedOut'|'Failed'|'Cancelling',
                    'StatusDetails': 'string',
                    'TraceOutput': 'string',
                    'StandardOutputUrl': 'string',
                    'StandardErrorUrl': 'string',
                    'CommandPlugins': [
                        {
                            'Name': 'string',
                            'Status': 'Pending'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                            'StatusDetails': 'string',
                            'ResponseCode': 123,
                            'ResponseStartDateTime': datetime(2015, 1, 1),
                            'ResponseFinishDateTime': datetime(2015, 1, 1),
                            'Output': 'string',
                            'StandardOutputUrl': 'string',
                            'StandardErrorUrl': 'string',
                            'OutputS3Region': 'string',
                            'OutputS3BucketName': 'string',
                            'OutputS3KeyPrefix': 'string'
                        },
                    ],
                    'ServiceRole': 'string',
                    'NotificationConfig': {
                        'NotificationArn': 'string',
                        'NotificationEvents': [
                            'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                        ],
                        'NotificationType': 'Command'|'Invocation'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CommandInvocations** *(list) --* 

          (Optional) A list of all invocations. 

          
          

          - *(dict) --* 

            An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user executes SendCommand against three instances, then a command invocation is created for each requested instance ID. A command invocation returns status and detail information about a command you executed. 

            
            

            - **CommandId** *(string) --* 

              The command against which this invocation was requested.

              
            

            - **InstanceId** *(string) --* 

              The instance ID in which this invocation was requested.

              
            

            - **InstanceName** *(string) --* 

              The name of the invocation target. For Amazon EC2 instances this is the value for the aws:Name tag. For on-premises instances, this is the name of the instance.

              
            

            - **Comment** *(string) --* 

              User-specified information about the command, such as a brief description of what the command should do.

              
            

            - **DocumentName** *(string) --* 

              The document name that was requested for execution.

              
            

            - **RequestedDateTime** *(datetime) --* 

              The time and date the request was sent to this instance.

              
            

            - **Status** *(string) --* 

              Whether or not the invocation succeeded, failed, or is pending.

              
            

            - **StatusDetails** *(string) --* 

              A detailed status of the command execution for each invocation (each instance targeted by the command). StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Run Command Status <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-about-status.html>`__ . StatusDetails can be one of the following values:

               

               
              * Pending: The command has not been sent to the instance. 
               
              * In Progress: The command has been sent to the instance but has not reached a terminal state. 
               
              * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
               
              * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
               
              * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
               
              * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
               
              * Canceled: The command was terminated before it was completed. This is a terminal state. 
               
              * Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
               
              * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
               

              
            

            - **TraceOutput** *(string) --* 

              Gets the trace output sent by the agent. 

              
            

            - **StandardOutputUrl** *(string) --* 

              The URL to the plugin's StdOut file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardOutputUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.

              
            

            - **StandardErrorUrl** *(string) --* 

              The URL to the plugin's StdErr file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardErrorUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.

              
            

            - **CommandPlugins** *(list) --* 
              

              - *(dict) --* 

                Describes plugin details.

                
                

                - **Name** *(string) --* 

                  The name of the plugin. Must be one of the following: aws:updateAgent, aws:domainjoin, aws:applications, aws:runPowerShellScript, aws:psmodule, aws:cloudWatch, aws:runShellScript, or aws:updateSSMAgent. 

                  
                

                - **Status** *(string) --* 

                  The status of this plugin. You can execute a document with multiple plugins.

                  
                

                - **StatusDetails** *(string) --* 

                  A detailed status of the plugin execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Run Command Status <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-about-status.html>`__ . StatusDetails can be one of the following values:

                   

                   
                  * Pending: The command has not been sent to the instance. 
                   
                  * In Progress: The command has been sent to the instance but has not reached a terminal state. 
                   
                  * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
                   
                  * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                   
                  * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
                   
                  * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
                   
                  * Canceled: The command was terminated before it was completed. This is a terminal state. 
                   
                  * Undeliverable: The command can't be delivered to the instance. The instance might not exist, or it might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit, and they don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                   
                  * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
                   

                  
                

                - **ResponseCode** *(integer) --* 

                  A numeric response code generated after executing the plugin. 

                  
                

                - **ResponseStartDateTime** *(datetime) --* 

                  The time the plugin started executing. 

                  
                

                - **ResponseFinishDateTime** *(datetime) --* 

                  The time the plugin stopped executing. Could stop prematurely if, for example, a cancel command was sent. 

                  
                

                - **Output** *(string) --* 

                  Output of the plugin execution.

                  
                

                - **StandardOutputUrl** *(string) --* 

                  The URL for the complete text written by the plugin to stdout in Amazon S3. If the Amazon S3 bucket for the command was not specified, then this string is empty.

                  
                

                - **StandardErrorUrl** *(string) --* 

                  The URL for the complete text written by the plugin to stderr. If execution is not yet complete, then this string is empty.

                  
                

                - **OutputS3Region** *(string) --* 

                  (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                  
                

                - **OutputS3BucketName** *(string) --* 

                  The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:

                   

                  test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript 

                   

                  test_folder is the name of the Amazon S3 bucket;

                   

                  ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;

                   

                  i-1234567876543 is the instance ID;

                   

                  awsrunShellScript is the name of the plugin.

                  
                

                - **OutputS3KeyPrefix** *(string) --* 

                  The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:

                   

                  test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript 

                   

                  test_folder is the name of the Amazon S3 bucket;

                   

                  ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;

                   

                  i-1234567876543 is the instance ID;

                   

                  awsrunShellScript is the name of the plugin.

                  
            
          
            

            - **ServiceRole** *(string) --* 

              The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes on a per instance basis.

              
            

            - **NotificationConfig** *(dict) --* 

              Configurations for sending notifications about command status changes on a per instance basis.

              
              

              - **NotificationArn** *(string) --* 

                An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

                
              

              - **NotificationEvents** *(list) --* 

                The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

                
                

                - *(string) --* 
            
              

              - **NotificationType** *(string) --* 

                Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

                
          
        
      
        

        - **NextToken** *(string) --* 

          (Optional) The token for the next set of items to return. (You received this token from a previous call.)

          
    

  .. py:method:: list_commands(**kwargs)

    

    Lists the commands requested by users of the AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommands>`_    


    **Request Syntax** 
    ::

      response = client.list_commands(
          CommandId='string',
          InstanceId='string',
          MaxResults=123,
          NextToken='string',
          Filters=[
              {
                  'key': 'InvokedAfter'|'InvokedBefore'|'Status',
                  'value': 'string'
              },
          ]
      )
    :type CommandId: string
    :param CommandId: 

      (Optional) If provided, lists only the specified command.

      

    
    :type InstanceId: string
    :param InstanceId: 

      (Optional) Lists commands issued against this instance ID.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      (Optional) The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type Filters: list
    :param Filters: 

      (Optional) One or more filters. Use a filter to return a more specific list of results. 

      

    
      - *(dict) --* 

        Describes a command filter.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The filter value. 

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Commands': [
                {
                    'CommandId': 'string',
                    'DocumentName': 'string',
                    'Comment': 'string',
                    'ExpiresAfter': datetime(2015, 1, 1),
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    },
                    'InstanceIds': [
                        'string',
                    ],
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'RequestedDateTime': datetime(2015, 1, 1),
                    'Status': 'Pending'|'InProgress'|'Success'|'Cancelled'|'Failed'|'TimedOut'|'Cancelling',
                    'StatusDetails': 'string',
                    'OutputS3Region': 'string',
                    'OutputS3BucketName': 'string',
                    'OutputS3KeyPrefix': 'string',
                    'MaxConcurrency': 'string',
                    'MaxErrors': 'string',
                    'TargetCount': 123,
                    'CompletedCount': 123,
                    'ErrorCount': 123,
                    'ServiceRole': 'string',
                    'NotificationConfig': {
                        'NotificationArn': 'string',
                        'NotificationEvents': [
                            'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                        ],
                        'NotificationType': 'Command'|'Invocation'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Commands** *(list) --* 

          (Optional) The list of commands requested by the user. 

          
          

          - *(dict) --* 

            Describes a command request.

            
            

            - **CommandId** *(string) --* 

              A unique identifier for this command.

              
            

            - **DocumentName** *(string) --* 

              The name of the document requested for execution.

              
            

            - **Comment** *(string) --* 

              User-specified information about the command, such as a brief description of what the command should do.

              
            

            - **ExpiresAfter** *(datetime) --* 

              If this time is reached and the command has not already started executing, it will not execute. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.

              
            

            - **Parameters** *(dict) --* 

              The parameter values to be inserted in the document when executing the command.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
            

            - **InstanceIds** *(list) --* 

              The instance IDs against which this command was requested.

              
              

              - *(string) --* 
          
            

            - **Targets** *(list) --* 

              An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **RequestedDateTime** *(datetime) --* 

              The date and time the command was requested.

              
            

            - **Status** *(string) --* 

              The status of the command.

              
            

            - **StatusDetails** *(string) --* 

              A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Run Command Status <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-about-status.html>`__ . StatusDetails can be one of the following values:

               

               
              * Pending: The command has not been sent to any instances. 
               
              * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances. 
               
              * Success: The command successfully executed on all invocations. This is a terminal state. 
               
              * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state. 
               
              * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state. 
               
              * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state. 
               
              * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state. 
               
              * Canceled: The command was terminated before it was completed. This is a terminal state. 
               
              * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before executing it on any instance. This is a terminal state. 
               

              
            

            - **OutputS3Region** *(string) --* 

              (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

              
            

            - **OutputS3BucketName** *(string) --* 

              The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.

              
            

            - **OutputS3KeyPrefix** *(string) --* 

              The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.

              
            

            - **MaxConcurrency** *(string) --* 

              The maximum number of instances that are allowed to execute the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ .

              
            

            - **MaxErrors** *(string) --* 

              The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 50. For more information about how to use MaxErrors, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ .

              
            

            - **TargetCount** *(integer) --* 

              The number of targets for the command.

              
            

            - **CompletedCount** *(integer) --* 

              The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.

              
            

            - **ErrorCount** *(integer) --* 

              The number of targets for which the status is Failed or Execution Timed Out.

              
            

            - **ServiceRole** *(string) --* 

              The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes. 

              
            

            - **NotificationConfig** *(dict) --* 

              Configurations for sending notifications about command status changes. 

              
              

              - **NotificationArn** *(string) --* 

                An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

                
              

              - **NotificationEvents** *(list) --* 

                The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

                
                

                - *(string) --* 
            
              

              - **NotificationType** *(string) --* 

                Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

                
          
        
      
        

        - **NextToken** *(string) --* 

          (Optional) The token for the next set of items to return. (You received this token from a previous call.)

          
    

  .. py:method:: list_compliance_items(**kwargs)

    

    For a specified resource ID, this API action returns a list of compliance statuses for different resource types. Currently, you can only specify one resource ID per call. List results depend on the criteria specified in the filter. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListComplianceItems>`_    


    **Request Syntax** 
    ::

      response = client.list_compliance_items(
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ],
                  'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
              },
          ],
          ResourceIds=[
              'string',
          ],
          ResourceTypes=[
              'string',
          ],
          NextToken='string',
          MaxResults=123
      )
    :type Filters: list
    :param Filters: 

      One or more compliance filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The value for which to search.

          

        
          - *(string) --* 

          
      
        - **Type** *(string) --* 

          The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.

          

        
      
  
    :type ResourceIds: list
    :param ResourceIds: 

      The ID for the resources from which to get compliance information. Currently, you can only specify one resource ID.

      

    
      - *(string) --* 

      
  
    :type ResourceTypes: list
    :param ResourceTypes: 

      The type of resource from which to get compliance information. Currently, the only supported resource type is ``ManagedInstance`` .

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      A token to start the list. Use this token to get the next set of results. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ComplianceItems': [
                {
                    'ComplianceType': 'string',
                    'ResourceType': 'string',
                    'ResourceId': 'string',
                    'Id': 'string',
                    'Title': 'string',
                    'Status': 'COMPLIANT'|'NON_COMPLIANT',
                    'Severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ExecutionSummary': {
                        'ExecutionTime': datetime(2015, 1, 1),
                        'ExecutionId': 'string',
                        'ExecutionType': 'string'
                    },
                    'Details': {
                        'string': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ComplianceItems** *(list) --* 

          A list of compliance information for the specified resource ID. 

          
          

          - *(dict) --* 

            Information about the compliance as defined by the resource type. For example, for a patch resource type, ``Items`` includes information about the PatchSeverity, Classification, etc.

            
            

            - **ComplianceType** *(string) --* 

              The compliance type. For example, Association (for a State Manager association), Patch, or Custom:``string`` are all valid compliance types.

              
            

            - **ResourceType** *(string) --* 

              The type of resource. ``ManagedInstance`` is currently the only supported resource type.

              
            

            - **ResourceId** *(string) --* 

              An ID for the resource. For a managed instance, this is the instance ID.

              
            

            - **Id** *(string) --* 

              An ID for the compliance item. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article. Here's an example: KB4010320.

              
            

            - **Title** *(string) --* 

              A title for the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch. Here's an example: Security Update for Active Directory Federation Services.

              
            

            - **Status** *(string) --* 

              The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.

              
            

            - **Severity** *(string) --* 

              The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.

              
            

            - **ExecutionSummary** *(dict) --* 

              A summary for the compliance item. The summary includes an execution ID, the execution type (for example, command), and the execution time.

              
              

              - **ExecutionTime** *(datetime) --* 

                The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.

                
              

              - **ExecutionId** *(string) --* 

                An ID created by the system when ``PutComplianceItems`` was called. For example, ``CommandID`` is a valid execution ID. You can use this ID in subsequent calls.

                
              

              - **ExecutionType** *(string) --* 

                The type of execution. For example, ``Command`` is a valid execution type.

                
          
            

            - **Details** *(dict) --* 

              A "Key": "Value" tag combination for the compliance item.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **NextToken** *(string) --* 

          The token for the next set of items to return. Use this token to get the next set of results.

          
    

  .. py:method:: list_compliance_summaries(**kwargs)

    

    Returns a summary count of compliant and non-compliant resources for a compliance type. For example, this call can return State Manager associations, patches, or custom compliance types according to the filter criteria that you specify. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListComplianceSummaries>`_    


    **Request Syntax** 
    ::

      response = client.list_compliance_summaries(
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ],
                  'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
              },
          ],
          NextToken='string',
          MaxResults=123
      )
    :type Filters: list
    :param Filters: 

      One or more compliance or inventory filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The value for which to search.

          

        
          - *(string) --* 

          
      
        - **Type** *(string) --* 

          The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.

          

        
      
  
    :type NextToken: string
    :param NextToken: 

      A token to start the list. Use this token to get the next set of results. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. Currently, you can specify null or 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ComplianceSummaryItems': [
                {
                    'ComplianceType': 'string',
                    'CompliantSummary': {
                        'CompliantCount': 123,
                        'SeveritySummary': {
                            'CriticalCount': 123,
                            'HighCount': 123,
                            'MediumCount': 123,
                            'LowCount': 123,
                            'InformationalCount': 123,
                            'UnspecifiedCount': 123
                        }
                    },
                    'NonCompliantSummary': {
                        'NonCompliantCount': 123,
                        'SeveritySummary': {
                            'CriticalCount': 123,
                            'HighCount': 123,
                            'MediumCount': 123,
                            'LowCount': 123,
                            'InformationalCount': 123,
                            'UnspecifiedCount': 123
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ComplianceSummaryItems** *(list) --* 

          A list of compliant and non-compliant summary counts based on compliance types. For example, this call returns State Manager associations, patches, or custom compliance types according to the filter criteria that you specified.

          
          

          - *(dict) --* 

            A summary of compliance information by compliance type.

            
            

            - **ComplianceType** *(string) --* 

              The type of compliance item. For example, the compliance type can be Association, Patch, or Custom:string.

              
            

            - **CompliantSummary** *(dict) --* 

              A list of COMPLIANT items for the specified compliance type.

              
              

              - **CompliantCount** *(integer) --* 

                The total number of resources that are compliant.

                
              

              - **SeveritySummary** *(dict) --* 

                A summary of the compliance severity by compliance type.

                
                

                - **CriticalCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.

                  
                

                - **HighCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

                  
                

                - **MediumCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

                  
                

                - **LowCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

                  
                

                - **InformationalCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

                  
                

                - **UnspecifiedCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.

                  
            
          
            

            - **NonCompliantSummary** *(dict) --* 

              A list of NON_COMPLIANT items for the specified compliance type.

              
              

              - **NonCompliantCount** *(integer) --* 

                The total number of compliance items that are not compliant.

                
              

              - **SeveritySummary** *(dict) --* 

                A summary of the non-compliance severity by compliance type

                
                

                - **CriticalCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.

                  
                

                - **HighCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

                  
                

                - **MediumCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

                  
                

                - **LowCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

                  
                

                - **InformationalCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

                  
                

                - **UnspecifiedCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          The token for the next set of items to return. Use this token to get the next set of results.

          
    

  .. py:method:: list_document_versions(**kwargs)

    

    List all versions for a document.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocumentVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_document_versions(
          Name='string',
          MaxResults=123,
          NextToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the document about which you want version information.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DocumentVersions': [
                {
                    'Name': 'string',
                    'DocumentVersion': 'string',
                    'CreatedDate': datetime(2015, 1, 1),
                    'IsDefaultVersion': True|False,
                    'DocumentFormat': 'YAML'|'JSON'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DocumentVersions** *(list) --* 

          The document versions.

          
          

          - *(dict) --* 

            Version information about the document.

            
            

            - **Name** *(string) --* 

              The document name.

              
            

            - **DocumentVersion** *(string) --* 

              The document version.

              
            

            - **CreatedDate** *(datetime) --* 

              The date the document was created.

              
            

            - **IsDefaultVersion** *(boolean) --* 

              An identifier for the default version of the document.

              
            

            - **DocumentFormat** *(string) --* 

              The document format, either JSON or YAML.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: list_documents(**kwargs)

    

    Describes one or more of your Systems Manager documents.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocuments>`_    


    **Request Syntax** 
    ::

      response = client.list_documents(
          DocumentFilterList=[
              {
                  'key': 'Name'|'Owner'|'PlatformTypes'|'DocumentType',
                  'value': 'string'
              },
          ],
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type DocumentFilterList: list
    :param DocumentFilterList: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        Describes a filter.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The value of the filter.

          

        
      
  
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of documents.

         

        For keys, you can specify one or more tags that have been applied to a document. 

         

        Other valid values include Owner, Name, PlatformTypes, and DocumentType.

         

        Note that only one Owner can be specified in a request. For example: ``Key=Owner,Values=Self`` .

         

        If you use Name as a key, you can use a name prefix to return a list of documents. For example, in the AWS CLI, to return a list of all documents that begin with ``Te`` , run the following command:

         

         ``aws ssm list-documents --filters Key=Name,Values=Te``  

         

        If you specify more than two keys, only documents that are identified by all the tags are returned in the results. If you specify more than two values for a key, documents that are identified by any of the values are returned in the results.

         

        To specify a custom key and value pair, use the format ``Key=tag:[tagName],Values=[valueName]`` .

         

        For example, if you created a Key called region and are using the AWS CLI to call the ``list-documents`` command: 

         

         ``aws ssm list-documents --filters Key=tag:region,Values=east,west Key=Owner,Values=Self``  

        

      
        - **Key** *(string) --* 

          The name of the filter key.

          

        
        - **Values** *(list) --* 

          The value for the filter key.

          

        
          - *(string) --* 

          
      
      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DocumentIdentifiers': [
                {
                    'Name': 'string',
                    'Owner': 'string',
                    'PlatformTypes': [
                        'Windows'|'Linux',
                    ],
                    'DocumentVersion': 'string',
                    'DocumentType': 'Command'|'Policy'|'Automation',
                    'SchemaVersion': 'string',
                    'DocumentFormat': 'YAML'|'JSON',
                    'TargetType': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DocumentIdentifiers** *(list) --* 

          The names of the Systems Manager documents.

          
          

          - *(dict) --* 

            Describes the name of a Systems Manager document.

            
            

            - **Name** *(string) --* 

              The name of the Systems Manager document.

              
            

            - **Owner** *(string) --* 

              The AWS user account that created the document.

              
            

            - **PlatformTypes** *(list) --* 

              The operating system platform. 

              
              

              - *(string) --* 
          
            

            - **DocumentVersion** *(string) --* 

              The document version.

              
            

            - **DocumentType** *(string) --* 

              The document type.

              
            

            - **SchemaVersion** *(string) --* 

              The schema version.

              
            

            - **DocumentFormat** *(string) --* 

              The document format, either JSON or YAML.

              
            

            - **TargetType** *(string) --* 

              The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 

              
            

            - **Tags** *(list) --* 

              The tags, or metadata, that have been applied to the document.

              
              

              - *(dict) --* 

                Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.

                
                

                - **Key** *(string) --* 

                  The name of the tag.

                  
                

                - **Value** *(string) --* 

                  The value of the tag.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: list_inventory_entries(**kwargs)

    

    A list of inventory items returned by the request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListInventoryEntries>`_    


    **Request Syntax** 
    ::

      response = client.list_inventory_entries(
          InstanceId='string',
          TypeName='string',
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ],
                  'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'
              },
          ],
          NextToken='string',
          MaxResults=123
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID for which you want inventory information.

      

    
    :type TypeName: string
    :param TypeName: **[REQUIRED]** 

      The type of inventory item for which you want information.

      

    
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The name of the filter key.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal 

          

        
          - *(string) --* 

          
      
        - **Type** *(string) --* 

          The type of filter. Valid values include the following: "Equal"|"NotEqual"|"BeginWith"|"LessThan"|"GreaterThan"

          

        
      
  
    :type NextToken: string
    :param NextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TypeName': 'string',
            'InstanceId': 'string',
            'SchemaVersion': 'string',
            'CaptureTime': 'string',
            'Entries': [
                {
                    'string': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TypeName** *(string) --* 

          The type of inventory item returned by the request.

          
        

        - **InstanceId** *(string) --* 

          The instance ID targeted by the request to query inventory information.

          
        

        - **SchemaVersion** *(string) --* 

          The inventory schema version used by the instance(s).

          
        

        - **CaptureTime** *(string) --* 

          The time that inventory information was collected for the instance(s).

          
        

        - **Entries** *(list) --* 

          A list of inventory items on the instance(s).

          
          

          - *(dict) --* 
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
        

        - **NextToken** *(string) --* 

          The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.

          
    

  .. py:method:: list_resource_compliance_summaries(**kwargs)

    

    Returns a resource-level summary count. The summary includes information about compliant and non-compliant statuses and detailed compliance-item severity counts, according to the filter criteria you specify.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListResourceComplianceSummaries>`_    


    **Request Syntax** 
    ::

      response = client.list_resource_compliance_summaries(
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ],
                  'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
              },
          ],
          NextToken='string',
          MaxResults=123
      )
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* 

          The name of the filter.

          

        
        - **Values** *(list) --* 

          The value for which to search.

          

        
          - *(string) --* 

          
      
        - **Type** *(string) --* 

          The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.

          

        
      
  
    :type NextToken: string
    :param NextToken: 

      A token to start the list. Use this token to get the next set of results. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceComplianceSummaryItems': [
                {
                    'ComplianceType': 'string',
                    'ResourceType': 'string',
                    'ResourceId': 'string',
                    'Status': 'COMPLIANT'|'NON_COMPLIANT',
                    'OverallSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ExecutionSummary': {
                        'ExecutionTime': datetime(2015, 1, 1),
                        'ExecutionId': 'string',
                        'ExecutionType': 'string'
                    },
                    'CompliantSummary': {
                        'CompliantCount': 123,
                        'SeveritySummary': {
                            'CriticalCount': 123,
                            'HighCount': 123,
                            'MediumCount': 123,
                            'LowCount': 123,
                            'InformationalCount': 123,
                            'UnspecifiedCount': 123
                        }
                    },
                    'NonCompliantSummary': {
                        'NonCompliantCount': 123,
                        'SeveritySummary': {
                            'CriticalCount': 123,
                            'HighCount': 123,
                            'MediumCount': 123,
                            'LowCount': 123,
                            'InformationalCount': 123,
                            'UnspecifiedCount': 123
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceComplianceSummaryItems** *(list) --* 

          A summary count for specified or targeted managed instances. Summary count includes information about compliant and non-compliant State Manager associations, patch status, or custom items according to the filter criteria that you specify. 

          
          

          - *(dict) --* 

            Compliance summary information for a specific resource. 

            
            

            - **ComplianceType** *(string) --* 

              The compliance type.

              
            

            - **ResourceType** *(string) --* 

              The resource type.

              
            

            - **ResourceId** *(string) --* 

              The resource ID.

              
            

            - **Status** *(string) --* 

              The compliance status for the resource.

              
            

            - **OverallSeverity** *(string) --* 

              The highest severity item found for the resource. The resource is compliant for this item.

              
            

            - **ExecutionSummary** *(dict) --* 

              Information about the execution.

              
              

              - **ExecutionTime** *(datetime) --* 

                The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.

                
              

              - **ExecutionId** *(string) --* 

                An ID created by the system when ``PutComplianceItems`` was called. For example, ``CommandID`` is a valid execution ID. You can use this ID in subsequent calls.

                
              

              - **ExecutionType** *(string) --* 

                The type of execution. For example, ``Command`` is a valid execution type.

                
          
            

            - **CompliantSummary** *(dict) --* 

              A list of items that are compliant for the resource.

              
              

              - **CompliantCount** *(integer) --* 

                The total number of resources that are compliant.

                
              

              - **SeveritySummary** *(dict) --* 

                A summary of the compliance severity by compliance type.

                
                

                - **CriticalCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.

                  
                

                - **HighCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

                  
                

                - **MediumCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

                  
                

                - **LowCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

                  
                

                - **InformationalCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

                  
                

                - **UnspecifiedCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.

                  
            
          
            

            - **NonCompliantSummary** *(dict) --* 

              A list of items that aren't compliant for the resource.

              
              

              - **NonCompliantCount** *(integer) --* 

                The total number of compliance items that are not compliant.

                
              

              - **SeveritySummary** *(dict) --* 

                A summary of the non-compliance severity by compliance type

                
                

                - **CriticalCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.

                  
                

                - **HighCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

                  
                

                - **MediumCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

                  
                

                - **LowCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

                  
                

                - **InformationalCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

                  
                

                - **UnspecifiedCount** *(integer) --* 

                  The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          The token for the next set of items to return. Use this token to get the next set of results.

          
    

  .. py:method:: list_resource_data_sync(**kwargs)

    

    Lists your resource data sync configurations. Includes information about the last time a sync attempted to start, the last sync status, and the last time a sync successfully completed.

     

    The number of sync configurations might be too large to return using a single call to ``ListResourceDataSync`` . You can limit the number of sync configurations returned by using the ``MaxResults`` parameter. To determine whether there are more sync configurations to list, check the value of ``NextToken`` in the output. If there are more sync configurations to list, you can request them by specifying the ``NextToken`` returned in the call to the parameter of a subsequent call. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListResourceDataSync>`_    


    **Request Syntax** 
    ::

      response = client.list_resource_data_sync(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      A token to start the list. Use this token to get the next set of results. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceDataSyncItems': [
                {
                    'SyncName': 'string',
                    'S3Destination': {
                        'BucketName': 'string',
                        'Prefix': 'string',
                        'SyncFormat': 'JsonSerDe',
                        'Region': 'string',
                        'AWSKMSKeyARN': 'string'
                    },
                    'LastSyncTime': datetime(2015, 1, 1),
                    'LastSuccessfulSyncTime': datetime(2015, 1, 1),
                    'LastStatus': 'Successful'|'Failed'|'InProgress',
                    'SyncCreatedTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceDataSyncItems** *(list) --* 

          A list of your current Resource Data Sync configurations and their statuses.

          
          

          - *(dict) --* 

            Information about a Resource Data Sync configuration, including its current status and last successful sync.

            
            

            - **SyncName** *(string) --* 

              The name of the Resource Data Sync.

              
            

            - **S3Destination** *(dict) --* 

              Configuration information for the target Amazon S3 bucket.

              
              

              - **BucketName** *(string) --* 

                The name of the Amazon S3 bucket where the aggregated data is stored.

                
              

              - **Prefix** *(string) --* 

                An Amazon S3 prefix for the bucket.

                
              

              - **SyncFormat** *(string) --* 

                A supported sync format. The following format is currently supported: JsonSerDe

                
              

              - **Region** *(string) --* 

                The AWS Region with the Amazon S3 bucket targeted by the Resource Data Sync.

                
              

              - **AWSKMSKeyARN** *(string) --* 

                The ARN of an encryption key for a destination in Amazon S3. Must belong to the same region as the destination Amazon S3 bucket.

                
          
            

            - **LastSyncTime** *(datetime) --* 

              The last time the configuration attempted to sync (UTC).

              
            

            - **LastSuccessfulSyncTime** *(datetime) --* 

              The last time the sync operations returned a status of ``SUCCESSFUL`` (UTC).

              
            

            - **LastStatus** *(string) --* 

              The status reported by the last sync.

              
            

            - **SyncCreatedTime** *(datetime) --* 

              The date and time the configuration was created (UTC).

              
        
      
        

        - **NextToken** *(string) --* 

          The token for the next set of items to return. Use this token to get the next set of results.

          
    

  .. py:method:: list_tags_for_resource(**kwargs)

    

    Returns a list of the tags assigned to the specified resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListTagsForResource>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_resource(
          ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline',
          ResourceId='string'
      )
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      Returns a list of tags for a specific resource type.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource ID for which you want to see a list of tags.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TagList** *(list) --* 

          A list of tags.

          
          

          - *(dict) --* 

            Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.

            
            

            - **Key** *(string) --* 

              The name of the tag.

              
            

            - **Value** *(string) --* 

              The value of the tag.

              
        
      
    

  .. py:method:: modify_document_permission(**kwargs)

    

    Shares a Systems Manager document publicly or privately. If you share a document privately, you must specify the AWS user account IDs for those people who can use the document. If you share a document publicly, you must specify *All* as the account ID.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ModifyDocumentPermission>`_    


    **Request Syntax** 
    ::

      response = client.modify_document_permission(
          Name='string',
          PermissionType='Share',
          AccountIdsToAdd=[
              'string',
          ],
          AccountIdsToRemove=[
              'string',
          ]
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the document that you want to share.

      

    
    :type PermissionType: string
    :param PermissionType: **[REQUIRED]** 

      The permission type for the document. The permission type can be *Share* .

      

    
    :type AccountIdsToAdd: list
    :param AccountIdsToAdd: 

      The AWS user accounts that should have access to the document. The account IDs can either be a group of account IDs or *All* .

      

    
      - *(string) --* 

      
  
    :type AccountIdsToRemove: list
    :param AccountIdsToRemove: 

      The AWS user accounts that should no longer have access to the document. The AWS user account can either be a group of account IDs or *All* . This action has a higher priority than *AccountIdsToAdd* . If you specify an account ID to add and the same ID to remove, the system removes access to the document.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: put_compliance_items(**kwargs)

    

    Registers a compliance type and other compliance details on a designated resource. This action lets you register custom compliance details with a resource. This call overwrites existing compliance information on the resource, so you must provide a full list of compliance items each time that you send the request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/PutComplianceItems>`_    


    **Request Syntax** 
    ::

      response = client.put_compliance_items(
          ResourceId='string',
          ResourceType='string',
          ComplianceType='string',
          ExecutionSummary={
              'ExecutionTime': datetime(2015, 1, 1),
              'ExecutionId': 'string',
              'ExecutionType': 'string'
          },
          Items=[
              {
                  'Id': 'string',
                  'Title': 'string',
                  'Severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                  'Status': 'COMPLIANT'|'NON_COMPLIANT',
                  'Details': {
                      'string': 'string'
                  }
              },
          ],
          ItemContentHash='string'
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      Specify an ID for this resource. For a managed instance, this is the instance ID.

      

    
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      Specify the type of resource. ``ManagedInstance`` is currently the only supported resource type.

      

    
    :type ComplianceType: string
    :param ComplianceType: **[REQUIRED]** 

      Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:``string`` .

      

    
    :type ExecutionSummary: dict
    :param ExecutionSummary: **[REQUIRED]** 

      A summary of the call execution that includes an execution ID, the type of execution (for example, ``Command`` ), and the date/time of the execution using a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.

      

    
      - **ExecutionTime** *(datetime) --* **[REQUIRED]** 

        The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.

        

      
      - **ExecutionId** *(string) --* 

        An ID created by the system when ``PutComplianceItems`` was called. For example, ``CommandID`` is a valid execution ID. You can use this ID in subsequent calls.

        

      
      - **ExecutionType** *(string) --* 

        The type of execution. For example, ``Command`` is a valid execution type.

        

      
    
    :type Items: list
    :param Items: **[REQUIRED]** 

      Information about the compliance as defined by the resource type. For example, for a patch compliance type, ``Items`` includes information about the PatchSeverity, Classification, etc.

      

    
      - *(dict) --* 

        Information about a compliance item.

        

      
        - **Id** *(string) --* 

          The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.

          

        
        - **Title** *(string) --* 

          The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch. Here's an example: Security Update for Active Directory Federation Services. 

          

        
        - **Severity** *(string) --* **[REQUIRED]** 

          The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.

          

        
        - **Status** *(string) --* **[REQUIRED]** 

          The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.

          

        
        - **Details** *(dict) --* 

          A "Key": "Value" tag combination for the compliance item.

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
      
  
    :type ItemContentHash: string
    :param ItemContentHash: 

      MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: put_inventory(**kwargs)

    

    Bulk update custom inventory items on one more instance. The request adds an inventory item, if it doesn't already exist, or updates an inventory item, if it does exist.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/PutInventory>`_    


    **Request Syntax** 
    ::

      response = client.put_inventory(
          InstanceId='string',
          Items=[
              {
                  'TypeName': 'string',
                  'SchemaVersion': 'string',
                  'CaptureTime': 'string',
                  'ContentHash': 'string',
                  'Content': [
                      {
                          'string': 'string'
                      },
                  ],
                  'Context': {
                      'string': 'string'
                  }
              },
          ]
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      One or more instance IDs where you want to add or update inventory items.

      

    
    :type Items: list
    :param Items: **[REQUIRED]** 

      The inventory items that you want to add or update on instances.

      

    
      - *(dict) --* 

        Information collected from managed instances based on your inventory policy document

        

      
        - **TypeName** *(string) --* **[REQUIRED]** 

          The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and AWS:WindowsUpdate.

          

        
        - **SchemaVersion** *(string) --* **[REQUIRED]** 

          The schema version for the inventory item.

          

        
        - **CaptureTime** *(string) --* **[REQUIRED]** 

          The time the inventory information was collected.

          

        
        - **ContentHash** *(string) --* 

          MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API does not update the inventory item type contents if the MD5 hash has not changed since last update. 

          

        
        - **Content** *(list) --* 

          The inventory data of the inventory type.

          

        
          - *(dict) --* 

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
      
        - **Context** *(dict) --* 

          A map of associated properties for a specified inventory type. For example, with this attribute, you can specify the ``ExecutionId`` , ``ExecutionType`` , ``ComplianceType`` properties of the ``AWS:ComplianceItem`` type.

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: put_parameter(**kwargs)

    

    Add one or more parameters to the system.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/PutParameter>`_    


    **Request Syntax** 
    ::

      response = client.put_parameter(
          Name='string',
          Description='string',
          Value='string',
          Type='String'|'StringList'|'SecureString',
          KeyId='string',
          Overwrite=True|False,
          AllowedPattern='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The fully qualified name of the parameter that you want to add to the system. The fully qualified name includes the complete hierarchy of the parameter path and name. For example: ``/Dev/DBServer/MySQL/db-string13``  

       

      .. note::

         

        The maximum length constraint listed below includes capacity for additional system attributes that are not part of the name. The maximum length for the fully qualified parameter name is 1011 characters. 

         

      

    
    :type Description: string
    :param Description: 

      Information about the parameter that you want to add to the system.

      

    
    :type Value: string
    :param Value: **[REQUIRED]** 

      The parameter value that you want to add to the system.

      

    
    :type Type: string
    :param Type: **[REQUIRED]** 

      The type of parameter that you want to add to the system.

      

    
    :type KeyId: string
    :param KeyId: 

      The KMS Key ID that you want to use to encrypt a parameter when you choose the SecureString data type. If you don't specify a key ID, the system uses the default key associated with your AWS account.

      

    
    :type Overwrite: boolean
    :param Overwrite: 

      Overwrite an existing parameter. If not specified, will default to "false".

      

    
    :type AllowedPattern: string
    :param AllowedPattern: 

      A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: AllowedPattern=^\d+$ 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Version': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Version** *(integer) --* 

          The new version number of a parameter. If you edit a parameter value, Parameter Store automatically creates a new version and assigns this new version a unique ID. You can reference a parameter version ID in API actions or in Systems Manager documents (SSM documents). By default, if you don't specify a specific version, the system returns the latest parameter value when a parameter is called.

          
    

  .. py:method:: register_default_patch_baseline(**kwargs)

    

    Defines the default patch baseline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterDefaultPatchBaseline>`_    


    **Request Syntax** 
    ::

      response = client.register_default_patch_baseline(
          BaselineId='string'
      )
    :type BaselineId: string
    :param BaselineId: **[REQUIRED]** 

      The ID of the patch baseline that should be the default patch baseline.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the default patch baseline.

          
    

  .. py:method:: register_patch_baseline_for_patch_group(**kwargs)

    

    Registers a patch baseline for a patch group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterPatchBaselineForPatchGroup>`_    


    **Request Syntax** 
    ::

      response = client.register_patch_baseline_for_patch_group(
          BaselineId='string',
          PatchGroup='string'
      )
    :type BaselineId: string
    :param BaselineId: **[REQUIRED]** 

      The ID of the patch baseline to register the patch group with.

      

    
    :type PatchGroup: string
    :param PatchGroup: **[REQUIRED]** 

      The name of the patch group that should be registered with the patch baseline.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string',
            'PatchGroup': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the patch baseline the patch group was registered with.

          
        

        - **PatchGroup** *(string) --* 

          The name of the patch group registered with the patch baseline.

          
    

  .. py:method:: register_target_with_maintenance_window(**kwargs)

    

    Registers a target with a Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow>`_    


    **Request Syntax** 
    ::

      response = client.register_target_with_maintenance_window(
          WindowId='string',
          ResourceType='INSTANCE',
          Targets=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          OwnerInformation='string',
          Name='string',
          Description='string',
          ClientToken='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the Maintenance Window the target should be registered with.

      

    
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of target being registered with the Maintenance Window.

      

    
    :type Targets: list
    :param Targets: **[REQUIRED]** 

      The targets (either instances or tags). Instances are specified using Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified using Key=<tag name>,Values=<tag value>.

      

    
      - *(dict) --* 

        An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

         

        

        

      
        - **Key** *(string) --* 

          User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
        - **Values** *(list) --* 

          User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
          - *(string) --* 

          
      
      
  
    :type OwnerInformation: string
    :param OwnerInformation: 

      User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

      

    
    :type Name: string
    :param Name: 

      An optional name for the target.

      

    
    :type Description: string
    :param Description: 

      An optional description for the target.

      

    
    :type ClientToken: string
    :param ClientToken: 

      User-provided idempotency token.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowTargetId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowTargetId** *(string) --* 

          The ID of the target definition in this Maintenance Window.

          
    

  .. py:method:: register_task_with_maintenance_window(**kwargs)

    

    Adds a new task to a Maintenance Window.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow>`_    


    **Request Syntax** 
    ::

      response = client.register_task_with_maintenance_window(
          WindowId='string',
          Targets=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          TaskArn='string',
          ServiceRoleArn='string',
          TaskType='RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
          TaskParameters={
              'string': {
                  'Values': [
                      'string',
                  ]
              }
          },
          TaskInvocationParameters={
              'RunCommand': {
                  'Comment': 'string',
                  'DocumentHash': 'string',
                  'DocumentHashType': 'Sha256'|'Sha1',
                  'NotificationConfig': {
                      'NotificationArn': 'string',
                      'NotificationEvents': [
                          'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                      ],
                      'NotificationType': 'Command'|'Invocation'
                  },
                  'OutputS3BucketName': 'string',
                  'OutputS3KeyPrefix': 'string',
                  'Parameters': {
                      'string': [
                          'string',
                      ]
                  },
                  'ServiceRoleArn': 'string',
                  'TimeoutSeconds': 123
              },
              'Automation': {
                  'DocumentVersion': 'string',
                  'Parameters': {
                      'string': [
                          'string',
                      ]
                  }
              },
              'StepFunctions': {
                  'Input': 'string',
                  'Name': 'string'
              },
              'Lambda': {
                  'ClientContext': 'string',
                  'Qualifier': 'string',
                  'Payload': b'bytes'
              }
          },
          Priority=123,
          MaxConcurrency='string',
          MaxErrors='string',
          LoggingInfo={
              'S3BucketName': 'string',
              'S3KeyPrefix': 'string',
              'S3Region': 'string'
          },
          Name='string',
          Description='string',
          ClientToken='string'
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The id of the Maintenance Window the task should be added to.

      

    
    :type Targets: list
    :param Targets: **[REQUIRED]** 

      The targets (either instances or tags). Instances are specified using Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified using Key=<tag name>,Values=<tag value>.

      

    
      - *(dict) --* 

        An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

         

        

        

      
        - **Key** *(string) --* 

          User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
        - **Values** *(list) --* 

          User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
          - *(string) --* 

          
      
      
  
    :type TaskArn: string
    :param TaskArn: **[REQUIRED]** 

      The ARN of the task to execute 

      

    
    :type ServiceRoleArn: string
    :param ServiceRoleArn: **[REQUIRED]** 

      The role that should be assumed when executing the task.

      

    
    :type TaskType: string
    :param TaskType: **[REQUIRED]** 

      The type of task being registered.

      

    
    :type TaskParameters: dict
    :param TaskParameters: 

      The parameters that should be passed to the task when it is executed.

      

    
      - *(string) --* 

      
        - *(dict) --* 

          Defines the values for a task parameter.

          

        
          - **Values** *(list) --* 

            This field contains an array of 0 or more strings, each 1 to 255 characters in length.

            

          
            - *(string) --* 

            
        
        
  

    :type TaskInvocationParameters: dict
    :param TaskInvocationParameters: 

      The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty. 

      

    
      - **RunCommand** *(dict) --* 

        The parameters for a RUN_COMMAND task type.

        

      
        - **Comment** *(string) --* 

          Information about the command(s) to execute.

          

        
        - **DocumentHash** *(string) --* 

          The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.

          

        
        - **DocumentHashType** *(string) --* 

          SHA-256 or SHA-1. SHA-1 hashes have been deprecated.

          

        
        - **NotificationConfig** *(dict) --* 

          Configurations for sending notifications about command status changes on a per-instance basis.

          

        
          - **NotificationArn** *(string) --* 

            An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

            

          
          - **NotificationEvents** *(list) --* 

            The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

            

          
            - *(string) --* 

            
        
          - **NotificationType** *(string) --* 

            Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

            

          
        
        - **OutputS3BucketName** *(string) --* 

          The name of the Amazon S3 bucket.

          

        
        - **OutputS3KeyPrefix** *(string) --* 

          The Amazon S3 bucket subfolder.

          

        
        - **Parameters** *(dict) --* 

          The parameters for the RUN_COMMAND task execution.

          

        
          - *(string) --* 

          
            - *(list) --* 

            
              - *(string) --* 

              
          
      
    
        - **ServiceRoleArn** *(string) --* 

          The IAM service role to assume during task execution.

          

        
        - **TimeoutSeconds** *(integer) --* 

          If this time is reached and the command has not already started executing, it doesn not execute.

          

        
      
      - **Automation** *(dict) --* 

        The parameters for a AUTOMATION task type.

        

      
        - **DocumentVersion** *(string) --* 

          The version of an Automation document to use during task execution.

          

        
        - **Parameters** *(dict) --* 

          The parameters for the AUTOMATION task.

          

        
          - *(string) --* 

          
            - *(list) --* 

            
              - *(string) --* 

              
          
      
    
      
      - **StepFunctions** *(dict) --* 

        The parameters for a STEP_FUNCTION task type.

        

      
        - **Input** *(string) --* 

          The inputs for the STEP_FUNCTION task.

          

        
        - **Name** *(string) --* 

          The name of the STEP_FUNCTION task.

          

        
      
      - **Lambda** *(dict) --* 

        The parameters for a LAMBDA task type.

        

      
        - **ClientContext** *(string) --* 

          Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.

          

        
        - **Qualifier** *(string) --* 

          (Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.

          

        
        - **Payload** *(bytes) --* 

          JSON to provide to your Lambda function as input.

          

        
      
    
    :type Priority: integer
    :param Priority: 

      The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

      

    
    :type MaxConcurrency: string
    :param MaxConcurrency: **[REQUIRED]** 

      The maximum number of targets this task can be run for in parallel.

      

    
    :type MaxErrors: string
    :param MaxErrors: **[REQUIRED]** 

      The maximum number of errors allowed before this task stops being scheduled.

      

    
    :type LoggingInfo: dict
    :param LoggingInfo: 

      A structure containing information about an Amazon S3 bucket to write instance-level logs to. 

      

    
      - **S3BucketName** *(string) --* **[REQUIRED]** 

        The name of an Amazon S3 bucket where execution logs are stored .

        

      
      - **S3KeyPrefix** *(string) --* 

        (Optional) The Amazon S3 bucket subfolder. 

        

      
      - **S3Region** *(string) --* **[REQUIRED]** 

        The region where the Amazon S3 bucket is located.

        

      
    
    :type Name: string
    :param Name: 

      An optional name for the task.

      

    
    :type Description: string
    :param Description: 

      An optional description for the task.

      

    
    :type ClientToken: string
    :param ClientToken: 

      User-provided idempotency token.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowTaskId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowTaskId** *(string) --* 

          The id of the task in the Maintenance Window.

          
    

  .. py:method:: remove_tags_from_resource(**kwargs)

    

    Removes all tags from the specified resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RemoveTagsFromResource>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags_from_resource(
          ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline',
          ResourceId='string',
          TagKeys=[
              'string',
          ]
      )
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of resource of which you want to remove a tag.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource ID for which you want to remove tags.

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      Tag keys that you want to remove from the specified resource.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: send_automation_signal(**kwargs)

    

    Sends a signal to an Automation execution to change the current behavior or status of the execution. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/SendAutomationSignal>`_    


    **Request Syntax** 
    ::

      response = client.send_automation_signal(
          AutomationExecutionId='string',
          SignalType='Approve'|'Reject'|'StartStep'|'StopStep'|'Resume',
          Payload={
              'string': [
                  'string',
              ]
          }
      )
    :type AutomationExecutionId: string
    :param AutomationExecutionId: **[REQUIRED]** 

      The unique identifier for an existing Automation execution that you want to send the signal to.

      

    
    :type SignalType: string
    :param SignalType: **[REQUIRED]** 

      The type of signal. Valid signal types include the following: Approve and Reject 

      

    
    :type Payload: dict
    :param Payload: 

      The data sent with the signal. The data schema depends on the type of signal used in the request. 

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(string) --* 

          
      
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: send_command(**kwargs)

    

    Executes commands on one or more managed instances.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/SendCommand>`_    


    **Request Syntax** 
    ::

      response = client.send_command(
          InstanceIds=[
              'string',
          ],
          Targets=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          DocumentName='string',
          DocumentHash='string',
          DocumentHashType='Sha256'|'Sha1',
          TimeoutSeconds=123,
          Comment='string',
          Parameters={
              'string': [
                  'string',
              ]
          },
          OutputS3Region='string',
          OutputS3BucketName='string',
          OutputS3KeyPrefix='string',
          MaxConcurrency='string',
          MaxErrors='string',
          ServiceRoleArn='string',
          NotificationConfig={
              'NotificationArn': 'string',
              'NotificationEvents': [
                  'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
              ],
              'NotificationType': 'Command'|'Invocation'
          }
      )
    :type InstanceIds: list
    :param InstanceIds: 

      The instance IDs where the command should execute. You can specify a maximum of 50 IDs. If you prefer not to list individual instance IDs, you can instead send commands to a fleet of instances using the Targets parameter, which accepts EC2 tags. For more information about how to use Targets, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

      

    
      - *(string) --* 

      
  
    :type Targets: list
    :param Targets: 

      (Optional) An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call. For more information about how to use Targets, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

      

    
      - *(dict) --* 

        An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

         

        

        

      
        - **Key** *(string) --* 

          User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
        - **Values** *(list) --* 

          User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
          - *(string) --* 

          
      
      
  
    :type DocumentName: string
    :param DocumentName: **[REQUIRED]** 

      Required. The name of the Systems Manager document to execute. This can be a public document or a custom document.

      

    
    :type DocumentHash: string
    :param DocumentHash: 

      The Sha256 or Sha1 hash created by the system when the document was created. 

       

      .. note::

         

        Sha1 hashes have been deprecated.

         

      

    
    :type DocumentHashType: string
    :param DocumentHashType: 

      Sha256 or Sha1.

       

      .. note::

         

        Sha1 hashes have been deprecated.

         

      

    
    :type TimeoutSeconds: integer
    :param TimeoutSeconds: 

      If this time is reached and the command has not already started executing, it will not execute.

      

    
    :type Comment: string
    :param Comment: 

      User-specified information about the command, such as a brief description of what the command should do.

      

    
    :type Parameters: dict
    :param Parameters: 

      The required and optional parameters specified in the document being executed.

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(string) --* 

          
      
  

    :type OutputS3Region: string
    :param OutputS3Region: 

      (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

      

    
    :type OutputS3BucketName: string
    :param OutputS3BucketName: 

      The name of the S3 bucket where command execution responses should be stored.

      

    
    :type OutputS3KeyPrefix: string
    :param OutputS3KeyPrefix: 

      The directory structure within the S3 bucket where the responses should be stored.

      

    
    :type MaxConcurrency: string
    :param MaxConcurrency: 

      (Optional) The maximum number of instances that are allowed to execute the command at the same time. You can specify a number such as 10 or a percentage such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Using Concurrency Controls <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-velocity.html>`__ .

      

    
    :type MaxErrors: string
    :param MaxErrors: 

      The maximum number of errors allowed without the command failing. When the command fails one more time beyond the value of MaxErrors, the systems stops sending the command to additional targets. You can specify a number like 10 or a percentage like 10%. The default value is 50. For more information about how to use MaxErrors, see `Using Error Controls <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-maxerrors.html>`__ .

      

    
    :type ServiceRoleArn: string
    :param ServiceRoleArn: 

      The IAM role that Systems Manager uses to send notifications. 

      

    
    :type NotificationConfig: dict
    :param NotificationConfig: 

      Configurations for sending notifications.

      

    
      - **NotificationArn** *(string) --* 

        An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

        

      
      - **NotificationEvents** *(list) --* 

        The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

        

      
        - *(string) --* 

        
    
      - **NotificationType** *(string) --* 

        Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Command': {
                'CommandId': 'string',
                'DocumentName': 'string',
                'Comment': 'string',
                'ExpiresAfter': datetime(2015, 1, 1),
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'InstanceIds': [
                    'string',
                ],
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'RequestedDateTime': datetime(2015, 1, 1),
                'Status': 'Pending'|'InProgress'|'Success'|'Cancelled'|'Failed'|'TimedOut'|'Cancelling',
                'StatusDetails': 'string',
                'OutputS3Region': 'string',
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string',
                'MaxConcurrency': 'string',
                'MaxErrors': 'string',
                'TargetCount': 123,
                'CompletedCount': 123,
                'ErrorCount': 123,
                'ServiceRole': 'string',
                'NotificationConfig': {
                    'NotificationArn': 'string',
                    'NotificationEvents': [
                        'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                    ],
                    'NotificationType': 'Command'|'Invocation'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Command** *(dict) --* 

          The request as it was received by Systems Manager. Also provides the command ID which can be used future references to this request.

          
          

          - **CommandId** *(string) --* 

            A unique identifier for this command.

            
          

          - **DocumentName** *(string) --* 

            The name of the document requested for execution.

            
          

          - **Comment** *(string) --* 

            User-specified information about the command, such as a brief description of what the command should do.

            
          

          - **ExpiresAfter** *(datetime) --* 

            If this time is reached and the command has not already started executing, it will not execute. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.

            
          

          - **Parameters** *(dict) --* 

            The parameter values to be inserted in the document when executing the command.

            
            

            - *(string) --* 
              

              - *(list) --* 
                

                - *(string) --* 
            
        
      
          

          - **InstanceIds** *(list) --* 

            The instance IDs against which this command was requested.

            
            

            - *(string) --* 
        
          

          - **Targets** *(list) --* 

            An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.

            
            

            - *(dict) --* 

              An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

               

              

              
              

              - **Key** *(string) --* 

                User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
              

              - **Values** *(list) --* 

                User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
                

                - *(string) --* 
            
          
        
          

          - **RequestedDateTime** *(datetime) --* 

            The date and time the command was requested.

            
          

          - **Status** *(string) --* 

            The status of the command.

            
          

          - **StatusDetails** *(string) --* 

            A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Run Command Status <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-about-status.html>`__ . StatusDetails can be one of the following values:

             

             
            * Pending: The command has not been sent to any instances. 
             
            * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances. 
             
            * Success: The command successfully executed on all invocations. This is a terminal state. 
             
            * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state. 
             
            * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state. 
             
            * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state. 
             
            * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state. 
             
            * Canceled: The command was terminated before it was completed. This is a terminal state. 
             
            * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before executing it on any instance. This is a terminal state. 
             

            
          

          - **OutputS3Region** *(string) --* 

            (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

            
          

          - **OutputS3BucketName** *(string) --* 

            The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.

            
          

          - **OutputS3KeyPrefix** *(string) --* 

            The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.

            
          

          - **MaxConcurrency** *(string) --* 

            The maximum number of instances that are allowed to execute the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ .

            
          

          - **MaxErrors** *(string) --* 

            The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 50. For more information about how to use MaxErrors, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ .

            
          

          - **TargetCount** *(integer) --* 

            The number of targets for the command.

            
          

          - **CompletedCount** *(integer) --* 

            The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.

            
          

          - **ErrorCount** *(integer) --* 

            The number of targets for which the status is Failed or Execution Timed Out.

            
          

          - **ServiceRole** *(string) --* 

            The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes. 

            
          

          - **NotificationConfig** *(dict) --* 

            Configurations for sending notifications about command status changes. 

            
            

            - **NotificationArn** *(string) --* 

              An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

              
            

            - **NotificationEvents** *(list) --* 

              The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

              
              

              - *(string) --* 
          
            

            - **NotificationType** *(string) --* 

              Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

              
        
      
    

  .. py:method:: start_automation_execution(**kwargs)

    

    Initiates execution of an Automation document.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/StartAutomationExecution>`_    


    **Request Syntax** 
    ::

      response = client.start_automation_execution(
          DocumentName='string',
          DocumentVersion='string',
          Parameters={
              'string': [
                  'string',
              ]
          },
          ClientToken='string',
          Mode='Auto'|'Interactive',
          TargetParameterName='string',
          Targets=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          MaxConcurrency='string',
          MaxErrors='string'
      )
    :type DocumentName: string
    :param DocumentName: **[REQUIRED]** 

      The name of the Automation document to use for this execution.

      

    
    :type DocumentVersion: string
    :param DocumentVersion: 

      The version of the Automation document to use for this execution.

      

    
    :type Parameters: dict
    :param Parameters: 

      A key-value map of execution parameters, which match the declared parameters in the Automation document.

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(string) --* 

          
      
  

    :type ClientToken: string
    :param ClientToken: 

      User-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can't be reused.

      

    
    :type Mode: string
    :param Mode: 

      The execution mode of the automation. Valid modes include the following: Auto and Interactive. The default mode is Auto.

      

    
    :type TargetParameterName: string
    :param TargetParameterName: 

      The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify Targets.

      

    
    :type Targets: list
    :param Targets: 

      A key-value mapping to target resources. Required if you specify TargetParameterName.

      

    
      - *(dict) --* 

        An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

         

        

        

      
        - **Key** *(string) --* 

          User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
        - **Values** *(list) --* 

          User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
          - *(string) --* 

          
      
      
  
    :type MaxConcurrency: string
    :param MaxConcurrency: 

      The maximum number of targets allowed to run this task in parallel. You can specify a number, such as 10, or a percentage, such as 10%. The default value is 10.

      

    
    :type MaxErrors: string
    :param MaxErrors: 

      The number of errors that are allowed before the system stops running the automation on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops running the automation when the fourth error is received. If you specify 0, then the system stops running the automation on additional targets after the first error result is returned. If you run an automation on 50 resources and set max-errors to 10%, then the system stops running the automation on additional targets when the sixth error is received.

       

      Executions that are already running an automation when max-errors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set max-concurrency to 1 so the executions proceed one at a time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutomationExecutionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AutomationExecutionId** *(string) --* 

          The unique ID of a newly scheduled automation execution.

          
    

  .. py:method:: stop_automation_execution(**kwargs)

    

    Stop an Automation that is currently executing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/StopAutomationExecution>`_    


    **Request Syntax** 
    ::

      response = client.stop_automation_execution(
          AutomationExecutionId='string',
          Type='Complete'|'Cancel'
      )
    :type AutomationExecutionId: string
    :param AutomationExecutionId: **[REQUIRED]** 

      The execution ID of the Automation to stop.

      

    
    :type Type: string
    :param Type: 

      The stop request type. Valid types include the following: Cancel and Complete. The default type is Cancel.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_association(**kwargs)

    

    Updates an association. You can update the association name and version, the document version, schedule, parameters, and Amazon S3 output.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateAssociation>`_    


    **Request Syntax** 
    ::

      response = client.update_association(
          AssociationId='string',
          Parameters={
              'string': [
                  'string',
              ]
          },
          DocumentVersion='string',
          ScheduleExpression='string',
          OutputLocation={
              'S3Location': {
                  'OutputS3Region': 'string',
                  'OutputS3BucketName': 'string',
                  'OutputS3KeyPrefix': 'string'
              }
          },
          Name='string',
          Targets=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          AssociationName='string',
          AssociationVersion='string'
      )
    :type AssociationId: string
    :param AssociationId: **[REQUIRED]** 

      The ID of the association you want to update. 

      

    
    :type Parameters: dict
    :param Parameters: 

      The parameters you want to update for the association. If you create a parameter using Parameter Store, you can reference the parameter using {{ssm:parameter-name}}

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(string) --* 

          
      
  

    :type DocumentVersion: string
    :param DocumentVersion: 

      The document version you want update for the association. 

      

    
    :type ScheduleExpression: string
    :param ScheduleExpression: 

      The cron expression used to schedule the association that you want to update.

      

    
    :type OutputLocation: dict
    :param OutputLocation: 

      An Amazon S3 bucket where you want to store the results of this request.

      

    
      - **S3Location** *(dict) --* 

        An Amazon S3 bucket where you want to store the results of this request.

        

      
        - **OutputS3Region** *(string) --* 

          (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

          

        
        - **OutputS3BucketName** *(string) --* 

          The name of the Amazon S3 bucket.

          

        
        - **OutputS3KeyPrefix** *(string) --* 

          The Amazon S3 bucket subfolder.

          

        
      
    
    :type Name: string
    :param Name: 

      The name of the association document.

      

    
    :type Targets: list
    :param Targets: 

      The targets of the association.

      

    
      - *(dict) --* 

        An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

         

        

        

      
        - **Key** *(string) --* 

          User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
        - **Values** *(list) --* 

          User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
          - *(string) --* 

          
      
      
  
    :type AssociationName: string
    :param AssociationName: 

      The name of the association that you want to update.

      

    
    :type AssociationVersion: string
    :param AssociationVersion: 

      This parameter is provided for concurrency control purposes. You must specify the latest association version in the service. If you want to ensure that this request succeeds, either specify ``$LATEST`` , or omit this parameter.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociationDescription': {
                'Name': 'string',
                'InstanceId': 'string',
                'AssociationVersion': 'string',
                'Date': datetime(2015, 1, 1),
                'LastUpdateAssociationDate': datetime(2015, 1, 1),
                'Status': {
                    'Date': datetime(2015, 1, 1),
                    'Name': 'Pending'|'Success'|'Failed',
                    'Message': 'string',
                    'AdditionalInfo': 'string'
                },
                'Overview': {
                    'Status': 'string',
                    'DetailedStatus': 'string',
                    'AssociationStatusAggregatedCount': {
                        'string': 123
                    }
                },
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'AssociationId': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ScheduleExpression': 'string',
                'OutputLocation': {
                    'S3Location': {
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string'
                    }
                },
                'LastExecutionDate': datetime(2015, 1, 1),
                'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
                'AssociationName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AssociationDescription** *(dict) --* 

          The description of the association that was updated.

          
          

          - **Name** *(string) --* 

            The name of the Systems Manager document.

            
          

          - **InstanceId** *(string) --* 

            The ID of the instance.

            
          

          - **AssociationVersion** *(string) --* 

            The association version.

            
          

          - **Date** *(datetime) --* 

            The date when the association was made.

            
          

          - **LastUpdateAssociationDate** *(datetime) --* 

            The date when the association was last updated.

            
          

          - **Status** *(dict) --* 

            The association status.

            
            

            - **Date** *(datetime) --* 

              The date when the status changed.

              
            

            - **Name** *(string) --* 

              The status.

              
            

            - **Message** *(string) --* 

              The reason for the status.

              
            

            - **AdditionalInfo** *(string) --* 

              A user-defined string.

              
        
          

          - **Overview** *(dict) --* 

            Information about the association.

            
            

            - **Status** *(string) --* 

              The status of the association. Status can be: Pending, Success, or Failed.

              
            

            - **DetailedStatus** *(string) --* 

              A detailed status of the association.

              
            

            - **AssociationStatusAggregatedCount** *(dict) --* 

              Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

              
              

              - *(string) --* 
                

                - *(integer) --* 
          
        
        
          

          - **DocumentVersion** *(string) --* 

            The document version.

            
          

          - **Parameters** *(dict) --* 

            A description of the parameters for a document. 

            
            

            - *(string) --* 
              

              - *(list) --* 
                

                - *(string) --* 
            
        
      
          

          - **AssociationId** *(string) --* 

            The association ID.

            
          

          - **Targets** *(list) --* 

            The instances targeted by the request. 

            
            

            - *(dict) --* 

              An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

               

              

              
              

              - **Key** *(string) --* 

                User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
              

              - **Values** *(list) --* 

                User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
                

                - *(string) --* 
            
          
        
          

          - **ScheduleExpression** *(string) --* 

            A cron expression that specifies a schedule when the association runs.

            
          

          - **OutputLocation** *(dict) --* 

            An Amazon S3 bucket where you want to store the output details of the request.

            
            

            - **S3Location** *(dict) --* 

              An Amazon S3 bucket where you want to store the results of this request.

              
              

              - **OutputS3Region** *(string) --* 

                (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                
              

              - **OutputS3BucketName** *(string) --* 

                The name of the Amazon S3 bucket.

                
              

              - **OutputS3KeyPrefix** *(string) --* 

                The Amazon S3 bucket subfolder.

                
          
        
          

          - **LastExecutionDate** *(datetime) --* 

            The date on which the association was last run.

            
          

          - **LastSuccessfulExecutionDate** *(datetime) --* 

            The last date on which the association was successfully run.

            
          

          - **AssociationName** *(string) --* 

            The association name.

            
      
    

  .. py:method:: update_association_status(**kwargs)

    

    Updates the status of the Systems Manager document associated with the specified instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateAssociationStatus>`_    


    **Request Syntax** 
    ::

      response = client.update_association_status(
          Name='string',
          InstanceId='string',
          AssociationStatus={
              'Date': datetime(2015, 1, 1),
              'Name': 'Pending'|'Success'|'Failed',
              'Message': 'string',
              'AdditionalInfo': 'string'
          }
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the Systems Manager document.

      

    
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The ID of the instance.

      

    
    :type AssociationStatus: dict
    :param AssociationStatus: **[REQUIRED]** 

      The association status.

      

    
      - **Date** *(datetime) --* **[REQUIRED]** 

        The date when the status changed.

        

      
      - **Name** *(string) --* **[REQUIRED]** 

        The status.

        

      
      - **Message** *(string) --* **[REQUIRED]** 

        The reason for the status.

        

      
      - **AdditionalInfo** *(string) --* 

        A user-defined string.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociationDescription': {
                'Name': 'string',
                'InstanceId': 'string',
                'AssociationVersion': 'string',
                'Date': datetime(2015, 1, 1),
                'LastUpdateAssociationDate': datetime(2015, 1, 1),
                'Status': {
                    'Date': datetime(2015, 1, 1),
                    'Name': 'Pending'|'Success'|'Failed',
                    'Message': 'string',
                    'AdditionalInfo': 'string'
                },
                'Overview': {
                    'Status': 'string',
                    'DetailedStatus': 'string',
                    'AssociationStatusAggregatedCount': {
                        'string': 123
                    }
                },
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'AssociationId': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ScheduleExpression': 'string',
                'OutputLocation': {
                    'S3Location': {
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string'
                    }
                },
                'LastExecutionDate': datetime(2015, 1, 1),
                'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
                'AssociationName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AssociationDescription** *(dict) --* 

          Information about the association.

          
          

          - **Name** *(string) --* 

            The name of the Systems Manager document.

            
          

          - **InstanceId** *(string) --* 

            The ID of the instance.

            
          

          - **AssociationVersion** *(string) --* 

            The association version.

            
          

          - **Date** *(datetime) --* 

            The date when the association was made.

            
          

          - **LastUpdateAssociationDate** *(datetime) --* 

            The date when the association was last updated.

            
          

          - **Status** *(dict) --* 

            The association status.

            
            

            - **Date** *(datetime) --* 

              The date when the status changed.

              
            

            - **Name** *(string) --* 

              The status.

              
            

            - **Message** *(string) --* 

              The reason for the status.

              
            

            - **AdditionalInfo** *(string) --* 

              A user-defined string.

              
        
          

          - **Overview** *(dict) --* 

            Information about the association.

            
            

            - **Status** *(string) --* 

              The status of the association. Status can be: Pending, Success, or Failed.

              
            

            - **DetailedStatus** *(string) --* 

              A detailed status of the association.

              
            

            - **AssociationStatusAggregatedCount** *(dict) --* 

              Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

              
              

              - *(string) --* 
                

                - *(integer) --* 
          
        
        
          

          - **DocumentVersion** *(string) --* 

            The document version.

            
          

          - **Parameters** *(dict) --* 

            A description of the parameters for a document. 

            
            

            - *(string) --* 
              

              - *(list) --* 
                

                - *(string) --* 
            
        
      
          

          - **AssociationId** *(string) --* 

            The association ID.

            
          

          - **Targets** *(list) --* 

            The instances targeted by the request. 

            
            

            - *(dict) --* 

              An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

               

              

              
              

              - **Key** *(string) --* 

                User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
              

              - **Values** *(list) --* 

                User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                
                

                - *(string) --* 
            
          
        
          

          - **ScheduleExpression** *(string) --* 

            A cron expression that specifies a schedule when the association runs.

            
          

          - **OutputLocation** *(dict) --* 

            An Amazon S3 bucket where you want to store the output details of the request.

            
            

            - **S3Location** *(dict) --* 

              An Amazon S3 bucket where you want to store the results of this request.

              
              

              - **OutputS3Region** *(string) --* 

                (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                
              

              - **OutputS3BucketName** *(string) --* 

                The name of the Amazon S3 bucket.

                
              

              - **OutputS3KeyPrefix** *(string) --* 

                The Amazon S3 bucket subfolder.

                
          
        
          

          - **LastExecutionDate** *(datetime) --* 

            The date on which the association was last run.

            
          

          - **LastSuccessfulExecutionDate** *(datetime) --* 

            The last date on which the association was successfully run.

            
          

          - **AssociationName** *(string) --* 

            The association name.

            
      
    

  .. py:method:: update_document(**kwargs)

    

    The document you want to update.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateDocument>`_    


    **Request Syntax** 
    ::

      response = client.update_document(
          Content='string',
          Name='string',
          DocumentVersion='string',
          DocumentFormat='YAML'|'JSON',
          TargetType='string'
      )
    :type Content: string
    :param Content: **[REQUIRED]** 

      The content in a document that you want to update.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the document that you want to update.

      

    
    :type DocumentVersion: string
    :param DocumentVersion: 

      The version of the document that you want to update.

      

    
    :type DocumentFormat: string
    :param DocumentFormat: 

      Specify the document format for the new document version. Systems Manager supports JSON and YAML documents. JSON is the default format.

      

    
    :type TargetType: string
    :param TargetType: 

      Specify a new target type for the document.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DocumentDescription': {
                'Sha1': 'string',
                'Hash': 'string',
                'HashType': 'Sha256'|'Sha1',
                'Name': 'string',
                'Owner': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'Status': 'Creating'|'Active'|'Updating'|'Deleting',
                'DocumentVersion': 'string',
                'Description': 'string',
                'Parameters': [
                    {
                        'Name': 'string',
                        'Type': 'String'|'StringList',
                        'Description': 'string',
                        'DefaultValue': 'string'
                    },
                ],
                'PlatformTypes': [
                    'Windows'|'Linux',
                ],
                'DocumentType': 'Command'|'Policy'|'Automation',
                'SchemaVersion': 'string',
                'LatestVersion': 'string',
                'DefaultVersion': 'string',
                'DocumentFormat': 'YAML'|'JSON',
                'TargetType': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DocumentDescription** *(dict) --* 

          A description of the document that was updated.

          
          

          - **Sha1** *(string) --* 

            The SHA1 hash of the document, which you can use for verification.

            
          

          - **Hash** *(string) --* 

            The Sha256 or Sha1 hash created by the system when the document was created. 

             

            .. note::

               

              Sha1 hashes have been deprecated.

               

            
          

          - **HashType** *(string) --* 

            Sha256 or Sha1.

             

            .. note::

               

              Sha1 hashes have been deprecated.

               

            
          

          - **Name** *(string) --* 

            The name of the Systems Manager document.

            
          

          - **Owner** *(string) --* 

            The AWS user account that created the document.

            
          

          - **CreatedDate** *(datetime) --* 

            The date when the document was created.

            
          

          - **Status** *(string) --* 

            The status of the Systems Manager document.

            
          

          - **DocumentVersion** *(string) --* 

            The document version.

            
          

          - **Description** *(string) --* 

            A description of the document. 

            
          

          - **Parameters** *(list) --* 

            A description of the parameters for a document.

            
            

            - *(dict) --* 

              Parameters specified in a System Manager document that execute on the server when the command is run. 

              
              

              - **Name** *(string) --* 

                The name of the parameter.

                
              

              - **Type** *(string) --* 

                The type of parameter. The type can be either String or StringList.

                
              

              - **Description** *(string) --* 

                A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.

                
              

              - **DefaultValue** *(string) --* 

                If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.

                
          
        
          

          - **PlatformTypes** *(list) --* 

            The list of OS platforms compatible with this Systems Manager document. 

            
            

            - *(string) --* 
        
          

          - **DocumentType** *(string) --* 

            The type of document. 

            
          

          - **SchemaVersion** *(string) --* 

            The schema version.

            
          

          - **LatestVersion** *(string) --* 

            The latest version of the document.

            
          

          - **DefaultVersion** *(string) --* 

            The default version.

            
          

          - **DocumentFormat** *(string) --* 

            The document format, either JSON or YAML.

            
          

          - **TargetType** *(string) --* 

            The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 

            
          

          - **Tags** *(list) --* 

            The tags, or metadata, that have been applied to the document.

            
            

            - *(dict) --* 

              Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.

              
              

              - **Key** *(string) --* 

                The name of the tag.

                
              

              - **Value** *(string) --* 

                The value of the tag.

                
          
        
      
    

  .. py:method:: update_document_default_version(**kwargs)

    

    Set the default version of a document. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateDocumentDefaultVersion>`_    


    **Request Syntax** 
    ::

      response = client.update_document_default_version(
          Name='string',
          DocumentVersion='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of a custom document that you want to set as the default version.

      

    
    :type DocumentVersion: string
    :param DocumentVersion: **[REQUIRED]** 

      The version of a custom document that you want to set as the default version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Description': {
                'Name': 'string',
                'DefaultVersion': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Description** *(dict) --* 

          The description of a custom document that you want to set as the default version.

          
          

          - **Name** *(string) --* 

            The name of the document.

            
          

          - **DefaultVersion** *(string) --* 

            The default version of the document.

            
      
    

  .. py:method:: update_maintenance_window(**kwargs)

    

    Updates an existing Maintenance Window. Only specified parameters are modified.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateMaintenanceWindow>`_    


    **Request Syntax** 
    ::

      response = client.update_maintenance_window(
          WindowId='string',
          Name='string',
          Description='string',
          Schedule='string',
          Duration=123,
          Cutoff=123,
          AllowUnassociatedTargets=True|False,
          Enabled=True|False,
          Replace=True|False
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The ID of the Maintenance Window to update.

      

    
    :type Name: string
    :param Name: 

      The name of the Maintenance Window.

      

    
    :type Description: string
    :param Description: 

      An optional description for the update request.

      

    
    :type Schedule: string
    :param Schedule: 

      The schedule of the Maintenance Window in the form of a cron or rate expression.

      

    
    :type Duration: integer
    :param Duration: 

      The duration of the Maintenance Window in hours.

      

    
    :type Cutoff: integer
    :param Cutoff: 

      The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

      

    
    :type AllowUnassociatedTargets: boolean
    :param AllowUnassociatedTargets: 

      Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.

      

    
    :type Enabled: boolean
    :param Enabled: 

      Whether the Maintenance Window is enabled.

      

    
    :type Replace: boolean
    :param Replace: 

      If True, then all fields that are required by the CreateMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string',
            'Name': 'string',
            'Description': 'string',
            'Schedule': 'string',
            'Duration': 123,
            'Cutoff': 123,
            'AllowUnassociatedTargets': True|False,
            'Enabled': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The ID of the created Maintenance Window.

          
        

        - **Name** *(string) --* 

          The name of the Maintenance Window.

          
        

        - **Description** *(string) --* 

          An optional description of the update.

          
        

        - **Schedule** *(string) --* 

          The schedule of the Maintenance Window in the form of a cron or rate expression.

          
        

        - **Duration** *(integer) --* 

          The duration of the Maintenance Window in hours.

          
        

        - **Cutoff** *(integer) --* 

          The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

          
        

        - **AllowUnassociatedTargets** *(boolean) --* 

          Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.

          
        

        - **Enabled** *(boolean) --* 

          Whether the Maintenance Window is enabled.

          
    

  .. py:method:: update_maintenance_window_target(**kwargs)

    

    Modifies the target of an existing Maintenance Window. You can't change the target type, but you can change the following:

     

    The target from being an ID target to a Tag target, or a Tag target to an ID target.

     

    IDs for an ID target.

     

    Tags for a Tag target.

     

    Owner.

     

    Name.

     

    Description.

     

    If a parameter is null, then the corresponding field is not modified.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateMaintenanceWindowTarget>`_    


    **Request Syntax** 
    ::

      response = client.update_maintenance_window_target(
          WindowId='string',
          WindowTargetId='string',
          Targets=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          OwnerInformation='string',
          Name='string',
          Description='string',
          Replace=True|False
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The Maintenance Window ID with which to modify the target.

      

    
    :type WindowTargetId: string
    :param WindowTargetId: **[REQUIRED]** 

      The target ID to modify.

      

    
    :type Targets: list
    :param Targets: 

      The targets to add or replace.

      

    
      - *(dict) --* 

        An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

         

        

        

      
        - **Key** *(string) --* 

          User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
        - **Values** *(list) --* 

          User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
          - *(string) --* 

          
      
      
  
    :type OwnerInformation: string
    :param OwnerInformation: 

      User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

      

    
    :type Name: string
    :param Name: 

      A name for the update.

      

    
    :type Description: string
    :param Description: 

      An optional description for the update.

      

    
    :type Replace: boolean
    :param Replace: 

      If True, then all fields that are required by the RegisterTargetWithMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string',
            'WindowTargetId': 'string',
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'OwnerInformation': 'string',
            'Name': 'string',
            'Description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The Maintenance Window ID specified in the update request.

          
        

        - **WindowTargetId** *(string) --* 

          The target ID specified in the update request.

          
        

        - **Targets** *(list) --* 

          The updated targets.

          
          

          - *(dict) --* 

            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

             

            

            
            

            - **Key** *(string) --* 

              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

              
            

            - **Values** *(list) --* 

              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

              
              

              - *(string) --* 
          
        
      
        

        - **OwnerInformation** *(string) --* 

          The updated owner.

          
        

        - **Name** *(string) --* 

          The updated name.

          
        

        - **Description** *(string) --* 

          The updated description.

          
    

  .. py:method:: update_maintenance_window_task(**kwargs)

    

    Modifies a task assigned to a Maintenance Window. You can't change the task type, but you can change the following values:

     

    Task ARN. For example, you can change a RUN_COMMAND task from AWS-RunPowerShellScript to AWS-RunShellScript.

     

    Service role ARN.

     

    Task parameters.

     

    Task priority.

     

    Task MaxConcurrency and MaxErrors.

     

    Log location.

     

    If a parameter is null, then the corresponding field is not modified. Also, if you set Replace to true, then all fields required by the RegisterTaskWithMaintenanceWindow action are required for this request. Optional fields that aren't specified are set to null.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateMaintenanceWindowTask>`_    


    **Request Syntax** 
    ::

      response = client.update_maintenance_window_task(
          WindowId='string',
          WindowTaskId='string',
          Targets=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          TaskArn='string',
          ServiceRoleArn='string',
          TaskParameters={
              'string': {
                  'Values': [
                      'string',
                  ]
              }
          },
          TaskInvocationParameters={
              'RunCommand': {
                  'Comment': 'string',
                  'DocumentHash': 'string',
                  'DocumentHashType': 'Sha256'|'Sha1',
                  'NotificationConfig': {
                      'NotificationArn': 'string',
                      'NotificationEvents': [
                          'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                      ],
                      'NotificationType': 'Command'|'Invocation'
                  },
                  'OutputS3BucketName': 'string',
                  'OutputS3KeyPrefix': 'string',
                  'Parameters': {
                      'string': [
                          'string',
                      ]
                  },
                  'ServiceRoleArn': 'string',
                  'TimeoutSeconds': 123
              },
              'Automation': {
                  'DocumentVersion': 'string',
                  'Parameters': {
                      'string': [
                          'string',
                      ]
                  }
              },
              'StepFunctions': {
                  'Input': 'string',
                  'Name': 'string'
              },
              'Lambda': {
                  'ClientContext': 'string',
                  'Qualifier': 'string',
                  'Payload': b'bytes'
              }
          },
          Priority=123,
          MaxConcurrency='string',
          MaxErrors='string',
          LoggingInfo={
              'S3BucketName': 'string',
              'S3KeyPrefix': 'string',
              'S3Region': 'string'
          },
          Name='string',
          Description='string',
          Replace=True|False
      )
    :type WindowId: string
    :param WindowId: **[REQUIRED]** 

      The Maintenance Window ID that contains the task to modify.

      

    
    :type WindowTaskId: string
    :param WindowTaskId: **[REQUIRED]** 

      The task ID to modify.

      

    
    :type Targets: list
    :param Targets: 

      The targets (either instances or tags) to modify. Instances are specified using Key=instanceids,Values=instanceID_1,instanceID_2. Tags are specified using Key=tag_name,Values=tag_value. 

      

    
      - *(dict) --* 

        An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

         

        

        

      
        - **Key** *(string) --* 

          User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
        - **Values** *(list) --* 

          User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

          

        
          - *(string) --* 

          
      
      
  
    :type TaskArn: string
    :param TaskArn: 

      The task ARN to modify.

      

    
    :type ServiceRoleArn: string
    :param ServiceRoleArn: 

      The IAM service role ARN to modify. The system assumes this role during task execution. 

      

    
    :type TaskParameters: dict
    :param TaskParameters: 

      The parameters to modify. The map has the following format:

       

      Key: string, between 1 and 255 characters

       

      Value: an array of strings, each string is between 1 and 255 characters

      

    
      - *(string) --* 

      
        - *(dict) --* 

          Defines the values for a task parameter.

          

        
          - **Values** *(list) --* 

            This field contains an array of 0 or more strings, each 1 to 255 characters in length.

            

          
            - *(string) --* 

            
        
        
  

    :type TaskInvocationParameters: dict
    :param TaskInvocationParameters: 

      The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.

      

    
      - **RunCommand** *(dict) --* 

        The parameters for a RUN_COMMAND task type.

        

      
        - **Comment** *(string) --* 

          Information about the command(s) to execute.

          

        
        - **DocumentHash** *(string) --* 

          The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.

          

        
        - **DocumentHashType** *(string) --* 

          SHA-256 or SHA-1. SHA-1 hashes have been deprecated.

          

        
        - **NotificationConfig** *(dict) --* 

          Configurations for sending notifications about command status changes on a per-instance basis.

          

        
          - **NotificationArn** *(string) --* 

            An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

            

          
          - **NotificationEvents** *(list) --* 

            The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

            

          
            - *(string) --* 

            
        
          - **NotificationType** *(string) --* 

            Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

            

          
        
        - **OutputS3BucketName** *(string) --* 

          The name of the Amazon S3 bucket.

          

        
        - **OutputS3KeyPrefix** *(string) --* 

          The Amazon S3 bucket subfolder.

          

        
        - **Parameters** *(dict) --* 

          The parameters for the RUN_COMMAND task execution.

          

        
          - *(string) --* 

          
            - *(list) --* 

            
              - *(string) --* 

              
          
      
    
        - **ServiceRoleArn** *(string) --* 

          The IAM service role to assume during task execution.

          

        
        - **TimeoutSeconds** *(integer) --* 

          If this time is reached and the command has not already started executing, it doesn not execute.

          

        
      
      - **Automation** *(dict) --* 

        The parameters for a AUTOMATION task type.

        

      
        - **DocumentVersion** *(string) --* 

          The version of an Automation document to use during task execution.

          

        
        - **Parameters** *(dict) --* 

          The parameters for the AUTOMATION task.

          

        
          - *(string) --* 

          
            - *(list) --* 

            
              - *(string) --* 

              
          
      
    
      
      - **StepFunctions** *(dict) --* 

        The parameters for a STEP_FUNCTION task type.

        

      
        - **Input** *(string) --* 

          The inputs for the STEP_FUNCTION task.

          

        
        - **Name** *(string) --* 

          The name of the STEP_FUNCTION task.

          

        
      
      - **Lambda** *(dict) --* 

        The parameters for a LAMBDA task type.

        

      
        - **ClientContext** *(string) --* 

          Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.

          

        
        - **Qualifier** *(string) --* 

          (Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.

          

        
        - **Payload** *(bytes) --* 

          JSON to provide to your Lambda function as input.

          

        
      
    
    :type Priority: integer
    :param Priority: 

      The new task priority to specify. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

      

    
    :type MaxConcurrency: string
    :param MaxConcurrency: 

      The new ``MaxConcurrency`` value you want to specify. ``MaxConcurrency`` is the number of targets that are allowed to run this task in parallel.

      

    
    :type MaxErrors: string
    :param MaxErrors: 

      The new ``MaxErrors`` value to specify. ``MaxErrors`` is the maximum number of errors that are allowed before the task stops being scheduled.

      

    
    :type LoggingInfo: dict
    :param LoggingInfo: 

      The new logging location in Amazon S3 to specify.

      

    
      - **S3BucketName** *(string) --* **[REQUIRED]** 

        The name of an Amazon S3 bucket where execution logs are stored .

        

      
      - **S3KeyPrefix** *(string) --* 

        (Optional) The Amazon S3 bucket subfolder. 

        

      
      - **S3Region** *(string) --* **[REQUIRED]** 

        The region where the Amazon S3 bucket is located.

        

      
    
    :type Name: string
    :param Name: 

      The new task name to specify.

      

    
    :type Description: string
    :param Description: 

      The new task description to specify.

      

    
    :type Replace: boolean
    :param Replace: 

      If True, then all fields that are required by the RegisterTaskWithMaintenanceWndow action are also required for this API request. Optional fields that are not specified are set to null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WindowId': 'string',
            'WindowTaskId': 'string',
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'TaskArn': 'string',
            'ServiceRoleArn': 'string',
            'TaskParameters': {
                'string': {
                    'Values': [
                        'string',
                    ]
                }
            },
            'TaskInvocationParameters': {
                'RunCommand': {
                    'Comment': 'string',
                    'DocumentHash': 'string',
                    'DocumentHashType': 'Sha256'|'Sha1',
                    'NotificationConfig': {
                        'NotificationArn': 'string',
                        'NotificationEvents': [
                            'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                        ],
                        'NotificationType': 'Command'|'Invocation'
                    },
                    'OutputS3BucketName': 'string',
                    'OutputS3KeyPrefix': 'string',
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    },
                    'ServiceRoleArn': 'string',
                    'TimeoutSeconds': 123
                },
                'Automation': {
                    'DocumentVersion': 'string',
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'StepFunctions': {
                    'Input': 'string',
                    'Name': 'string'
                },
                'Lambda': {
                    'ClientContext': 'string',
                    'Qualifier': 'string',
                    'Payload': b'bytes'
                }
            },
            'Priority': 123,
            'MaxConcurrency': 'string',
            'MaxErrors': 'string',
            'LoggingInfo': {
                'S3BucketName': 'string',
                'S3KeyPrefix': 'string',
                'S3Region': 'string'
            },
            'Name': 'string',
            'Description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WindowId** *(string) --* 

          The ID of the Maintenance Window that was updated.

          
        

        - **WindowTaskId** *(string) --* 

          The task ID of the Maintenance Window that was updated.

          
        

        - **Targets** *(list) --* 

          The updated target values.

          
          

          - *(dict) --* 

            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

             

            

            
            

            - **Key** *(string) --* 

              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

              
            

            - **Values** *(list) --* 

              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

              
              

              - *(string) --* 
          
        
      
        

        - **TaskArn** *(string) --* 

          The updated task ARN value.

          
        

        - **ServiceRoleArn** *(string) --* 

          The updated service role ARN value.

          
        

        - **TaskParameters** *(dict) --* 

          The updated parameter values.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Defines the values for a task parameter.

              
              

              - **Values** *(list) --* 

                This field contains an array of 0 or more strings, each 1 to 255 characters in length.

                
                

                - *(string) --* 
            
          
      
    
        

        - **TaskInvocationParameters** *(dict) --* 

          The updated parameter values.

          
          

          - **RunCommand** *(dict) --* 

            The parameters for a RUN_COMMAND task type.

            
            

            - **Comment** *(string) --* 

              Information about the command(s) to execute.

              
            

            - **DocumentHash** *(string) --* 

              The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.

              
            

            - **DocumentHashType** *(string) --* 

              SHA-256 or SHA-1. SHA-1 hashes have been deprecated.

              
            

            - **NotificationConfig** *(dict) --* 

              Configurations for sending notifications about command status changes on a per-instance basis.

              
              

              - **NotificationArn** *(string) --* 

                An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

                
              

              - **NotificationEvents** *(list) --* 

                The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

                
                

                - *(string) --* 
            
              

              - **NotificationType** *(string) --* 

                Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

                
          
            

            - **OutputS3BucketName** *(string) --* 

              The name of the Amazon S3 bucket.

              
            

            - **OutputS3KeyPrefix** *(string) --* 

              The Amazon S3 bucket subfolder.

              
            

            - **Parameters** *(dict) --* 

              The parameters for the RUN_COMMAND task execution.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
            

            - **ServiceRoleArn** *(string) --* 

              The IAM service role to assume during task execution.

              
            

            - **TimeoutSeconds** *(integer) --* 

              If this time is reached and the command has not already started executing, it doesn not execute.

              
        
          

          - **Automation** *(dict) --* 

            The parameters for a AUTOMATION task type.

            
            

            - **DocumentVersion** *(string) --* 

              The version of an Automation document to use during task execution.

              
            

            - **Parameters** *(dict) --* 

              The parameters for the AUTOMATION task.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
        
          

          - **StepFunctions** *(dict) --* 

            The parameters for a STEP_FUNCTION task type.

            
            

            - **Input** *(string) --* 

              The inputs for the STEP_FUNCTION task.

              
            

            - **Name** *(string) --* 

              The name of the STEP_FUNCTION task.

              
        
          

          - **Lambda** *(dict) --* 

            The parameters for a LAMBDA task type.

            
            

            - **ClientContext** *(string) --* 

              Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.

              
            

            - **Qualifier** *(string) --* 

              (Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.

              
            

            - **Payload** *(bytes) --* 

              JSON to provide to your Lambda function as input.

              
        
      
        

        - **Priority** *(integer) --* 

          The updated priority value.

          
        

        - **MaxConcurrency** *(string) --* 

          The updated MaxConcurrency value.

          
        

        - **MaxErrors** *(string) --* 

          The updated MaxErrors value.

          
        

        - **LoggingInfo** *(dict) --* 

          The updated logging information in Amazon S3.

          
          

          - **S3BucketName** *(string) --* 

            The name of an Amazon S3 bucket where execution logs are stored .

            
          

          - **S3KeyPrefix** *(string) --* 

            (Optional) The Amazon S3 bucket subfolder. 

            
          

          - **S3Region** *(string) --* 

            The region where the Amazon S3 bucket is located.

            
      
        

        - **Name** *(string) --* 

          The updated task name.

          
        

        - **Description** *(string) --* 

          The updated task description.

          
    

  .. py:method:: update_managed_instance_role(**kwargs)

    

    Assigns or changes an Amazon Identity and Access Management (IAM) role to the managed instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateManagedInstanceRole>`_    


    **Request Syntax** 
    ::

      response = client.update_managed_instance_role(
          InstanceId='string',
          IamRole='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The ID of the managed instance where you want to update the role.

      

    
    :type IamRole: string
    :param IamRole: **[REQUIRED]** 

      The IAM role you want to assign or change.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_patch_baseline(**kwargs)

    

    Modifies an existing patch baseline. Fields not specified in the request are left unchanged.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdatePatchBaseline>`_    


    **Request Syntax** 
    ::

      response = client.update_patch_baseline(
          BaselineId='string',
          Name='string',
          GlobalFilters={
              'PatchFilters': [
                  {
                      'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          },
          ApprovalRules={
              'PatchRules': [
                  {
                      'PatchFilterGroup': {
                          'PatchFilters': [
                              {
                                  'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                  'Values': [
                                      'string',
                                  ]
                              },
                          ]
                      },
                      'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                      'ApproveAfterDays': 123
                  },
              ]
          },
          ApprovedPatches=[
              'string',
          ],
          ApprovedPatchesComplianceLevel='CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
          RejectedPatches=[
              'string',
          ],
          Description='string'
      )
    :type BaselineId: string
    :param BaselineId: **[REQUIRED]** 

      The ID of the patch baseline to update.

      

    
    :type Name: string
    :param Name: 

      The name of the patch baseline.

      

    
    :type GlobalFilters: dict
    :param GlobalFilters: 

      A set of global filters used to exclude patches from the baseline.

      

    
      - **PatchFilters** *(list) --* **[REQUIRED]** 

        The set of patch filters that make up the group.

        

      
        - *(dict) --* 

          Defines a patch filter.

          

        
          - **Key** *(string) --* **[REQUIRED]** 

            The key for the filter (PRODUCT, CLASSIFICATION, MSRC_SEVERITY, PATCH_ID)

            

          
          - **Values** *(list) --* **[REQUIRED]** 

            The value for the filter key.

            

          
            - *(string) --* 

            
        
        
    
    
    :type ApprovalRules: dict
    :param ApprovalRules: 

      A set of rules used to include patches in the baseline.

      

    
      - **PatchRules** *(list) --* **[REQUIRED]** 

        The rules that make up the rule group.

        

      
        - *(dict) --* 

          Defines an approval rule for a patch baseline.

          

        
          - **PatchFilterGroup** *(dict) --* **[REQUIRED]** 

            The patch filter group that defines the criteria for the rule.

            

          
            - **PatchFilters** *(list) --* **[REQUIRED]** 

              The set of patch filters that make up the group.

              

            
              - *(dict) --* 

                Defines a patch filter.

                

              
                - **Key** *(string) --* **[REQUIRED]** 

                  The key for the filter (PRODUCT, CLASSIFICATION, MSRC_SEVERITY, PATCH_ID)

                  

                
                - **Values** *(list) --* **[REQUIRED]** 

                  The value for the filter key.

                  

                
                  - *(string) --* 

                  
              
              
          
          
          - **ComplianceLevel** *(string) --* 

            A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.

            

          
          - **ApproveAfterDays** *(integer) --* **[REQUIRED]** 

            The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline.

            

          
        
    
    
    :type ApprovedPatches: list
    :param ApprovedPatches: 

      A list of explicitly approved patches for the baseline.

      

    
      - *(string) --* 

      
  
    :type ApprovedPatchesComplianceLevel: string
    :param ApprovedPatchesComplianceLevel: 

      Assigns a new compliance severity level to an existing patch baseline.

      

    
    :type RejectedPatches: list
    :param RejectedPatches: 

      A list of explicitly rejected patches for the baseline.

      

    
      - *(string) --* 

      
  
    :type Description: string
    :param Description: 

      A description of the patch baseline.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BaselineId': 'string',
            'Name': 'string',
            'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX',
            'GlobalFilters': {
                'PatchFilters': [
                    {
                        'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                        'Values': [
                            'string',
                        ]
                    },
                ]
            },
            'ApprovalRules': {
                'PatchRules': [
                    {
                        'PatchFilterGroup': {
                            'PatchFilters': [
                                {
                                    'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                    'Values': [
                                        'string',
                                    ]
                                },
                            ]
                        },
                        'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                        'ApproveAfterDays': 123
                    },
                ]
            },
            'ApprovedPatches': [
                'string',
            ],
            'ApprovedPatchesComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
            'RejectedPatches': [
                'string',
            ],
            'CreatedDate': datetime(2015, 1, 1),
            'ModifiedDate': datetime(2015, 1, 1),
            'Description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BaselineId** *(string) --* 

          The ID of the deleted patch baseline.

          
        

        - **Name** *(string) --* 

          The name of the patch baseline.

          
        

        - **OperatingSystem** *(string) --* 

          The operating system rule used by the updated patch baseline.

          
        

        - **GlobalFilters** *(dict) --* 

          A set of global filters used to exclude patches from the baseline.

          
          

          - **PatchFilters** *(list) --* 

            The set of patch filters that make up the group.

            
            

            - *(dict) --* 

              Defines a patch filter.

              
              

              - **Key** *(string) --* 

                The key for the filter (PRODUCT, CLASSIFICATION, MSRC_SEVERITY, PATCH_ID)

                
              

              - **Values** *(list) --* 

                The value for the filter key.

                
                

                - *(string) --* 
            
          
        
      
        

        - **ApprovalRules** *(dict) --* 

          A set of rules used to include patches in the baseline.

          
          

          - **PatchRules** *(list) --* 

            The rules that make up the rule group.

            
            

            - *(dict) --* 

              Defines an approval rule for a patch baseline.

              
              

              - **PatchFilterGroup** *(dict) --* 

                The patch filter group that defines the criteria for the rule.

                
                

                - **PatchFilters** *(list) --* 

                  The set of patch filters that make up the group.

                  
                  

                  - *(dict) --* 

                    Defines a patch filter.

                    
                    

                    - **Key** *(string) --* 

                      The key for the filter (PRODUCT, CLASSIFICATION, MSRC_SEVERITY, PATCH_ID)

                      
                    

                    - **Values** *(list) --* 

                      The value for the filter key.

                      
                      

                      - *(string) --* 
                  
                
              
            
              

              - **ComplianceLevel** *(string) --* 

                A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.

                
              

              - **ApproveAfterDays** *(integer) --* 

                The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline.

                
          
        
      
        

        - **ApprovedPatches** *(list) --* 

          A list of explicitly approved patches for the baseline.

          
          

          - *(string) --* 
      
        

        - **ApprovedPatchesComplianceLevel** *(string) --* 

          The compliance severity level assigned to the patch baseline after the update completed.

          
        

        - **RejectedPatches** *(list) --* 

          A list of explicitly rejected patches for the baseline.

          
          

          - *(string) --* 
      
        

        - **CreatedDate** *(datetime) --* 

          The date when the patch baseline was created.

          
        

        - **ModifiedDate** *(datetime) --* 

          The date when the patch baseline was last modified.

          
        

        - **Description** *(string) --* 

          A description of the Patch Baseline.

          
    

==========
Paginators
==========


The available paginators are:

* :py:class:`SSM.Paginator.DescribeActivations`


* :py:class:`SSM.Paginator.DescribeInstanceInformation`


* :py:class:`SSM.Paginator.DescribeParameters`


* :py:class:`SSM.Paginator.ListAssociations`


* :py:class:`SSM.Paginator.ListCommandInvocations`


* :py:class:`SSM.Paginator.ListCommands`


* :py:class:`SSM.Paginator.ListDocuments`



.. py:class:: SSM.Paginator.DescribeActivations

  ::

    
    paginator = client.get_paginator('describe_activations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_activations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeActivations>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Filters=[
              {
                  'FilterKey': 'ActivationIds'|'DefaultInstanceName'|'IamRole',
                  'FilterValues': [
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

      A filter to view information about your activations.

      

    
      - *(dict) --* 

        Filter for the DescribeActivation API.

        

      
        - **FilterKey** *(string) --* 

          The name of the filter.

          

        
        - **FilterValues** *(list) --* 

          The filter values.

          

        
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
            'ActivationList': [
                {
                    'ActivationId': 'string',
                    'Description': 'string',
                    'DefaultInstanceName': 'string',
                    'IamRole': 'string',
                    'RegistrationLimit': 123,
                    'RegistrationsCount': 123,
                    'ExpirationDate': datetime(2015, 1, 1),
                    'Expired': True|False,
                    'CreatedDate': datetime(2015, 1, 1)
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ActivationList** *(list) --* 

          A list of activations for your AWS account.

          
          

          - *(dict) --* 

            An activation registers one or more on-premises servers or virtual machines (VMs) with AWS so that you can configure those servers or VMs using Run Command. A server or VM that has been registered with AWS is called a managed instance.

            
            

            - **ActivationId** *(string) --* 

              The ID created by Systems Manager when you submitted the activation.

              
            

            - **Description** *(string) --* 

              A user defined description of the activation.

              
            

            - **DefaultInstanceName** *(string) --* 

              A name for the managed instance when it is created.

              
            

            - **IamRole** *(string) --* 

              The Amazon Identity and Access Management (IAM) role to assign to the managed instance.

              
            

            - **RegistrationLimit** *(integer) --* 

              The maximum number of managed instances that can be registered using this activation.

              
            

            - **RegistrationsCount** *(integer) --* 

              The number of managed instances already registered with this activation.

              
            

            - **ExpirationDate** *(datetime) --* 

              The date when this activation can no longer be used to register managed instances.

              
            

            - **Expired** *(boolean) --* 

              Whether or not the activation is expired.

              
            

            - **CreatedDate** *(datetime) --* 

              The date the activation was created.

              
        
      
    

.. py:class:: SSM.Paginator.DescribeInstanceInformation

  ::

    
    paginator = client.get_paginator('describe_instance_information')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_instance_information`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceInformation>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          InstanceInformationFilterList=[
              {
                  'key': 'InstanceIds'|'AgentVersion'|'PingStatus'|'PlatformTypes'|'ActivationIds'|'IamRole'|'ResourceType'|'AssociationStatus',
                  'valueSet': [
                      'string',
                  ]
              },
          ],
          Filters=[
              {
                  'Key': 'string',
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
    :type InstanceInformationFilterList: list
    :param InstanceInformationFilterList: 

      One or more filters. Use a filter to return a more specific list of instances.

      

    
      - *(dict) --* 

        Describes a filter for a specific list of instances. 

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter. 

          

        
        - **valueSet** *(list) --* **[REQUIRED]** 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of instances.

      

    
      - *(dict) --* 

        The filters to describe or get information about your managed instances.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The filter key name to describe your instances. For example:

           

          "InstanceIds"|"AgentVersion"|"PingStatus"|"PlatformTypes"|"ActivationIds"|"IamRole"|"ResourceType"|"AssociationStatus"|"Tag Key"

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The filter values.

          

        
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
            'InstanceInformationList': [
                {
                    'InstanceId': 'string',
                    'PingStatus': 'Online'|'ConnectionLost'|'Inactive',
                    'LastPingDateTime': datetime(2015, 1, 1),
                    'AgentVersion': 'string',
                    'IsLatestVersion': True|False,
                    'PlatformType': 'Windows'|'Linux',
                    'PlatformName': 'string',
                    'PlatformVersion': 'string',
                    'ActivationId': 'string',
                    'IamRole': 'string',
                    'RegistrationDate': datetime(2015, 1, 1),
                    'ResourceType': 'ManagedInstance'|'Document'|'EC2Instance',
                    'Name': 'string',
                    'IPAddress': 'string',
                    'ComputerName': 'string',
                    'AssociationStatus': 'string',
                    'LastAssociationExecutionDate': datetime(2015, 1, 1),
                    'LastSuccessfulAssociationExecutionDate': datetime(2015, 1, 1),
                    'AssociationOverview': {
                        'DetailedStatus': 'string',
                        'InstanceAssociationStatusAggregatedCount': {
                            'string': 123
                        }
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **InstanceInformationList** *(list) --* 

          The instance information list.

          
          

          - *(dict) --* 

            Describes a filter for a specific list of instances. 

            
            

            - **InstanceId** *(string) --* 

              The instance ID. 

              
            

            - **PingStatus** *(string) --* 

              Connection status of the SSM Agent. 

              
            

            - **LastPingDateTime** *(datetime) --* 

              The date and time when agent last pinged Systems Manager service. 

              
            

            - **AgentVersion** *(string) --* 

              The version of the SSM Agent running on your Linux instance. 

              
            

            - **IsLatestVersion** *(boolean) --* 

              Indicates whether latest version of the SSM Agent is running on your instance. 

              
            

            - **PlatformType** *(string) --* 

              The operating system platform type. 

              
            

            - **PlatformName** *(string) --* 

              The name of the operating system platform running on your instance. 

              
            

            - **PlatformVersion** *(string) --* 

              The version of the OS platform running on your instance. 

              
            

            - **ActivationId** *(string) --* 

              The activation ID created by Systems Manager when the server or VM was registered.

              
            

            - **IamRole** *(string) --* 

              The Amazon Identity and Access Management (IAM) role assigned to EC2 instances or managed instances. 

              
            

            - **RegistrationDate** *(datetime) --* 

              The date the server or VM was registered with AWS as a managed instance.

              
            

            - **ResourceType** *(string) --* 

              The type of instance. Instances are either EC2 instances or managed instances. 

              
            

            - **Name** *(string) --* 

              The name of the managed instance.

              
            

            - **IPAddress** *(string) --* 

              The IP address of the managed instance.

              
            

            - **ComputerName** *(string) --* 

              The fully qualified host name of the managed instance.

              
            

            - **AssociationStatus** *(string) --* 

              The status of the association.

              
            

            - **LastAssociationExecutionDate** *(datetime) --* 

              The date the association was last executed.

              
            

            - **LastSuccessfulAssociationExecutionDate** *(datetime) --* 

              The last date the association was successfully run.

              
            

            - **AssociationOverview** *(dict) --* 

              Information about the association.

              
              

              - **DetailedStatus** *(string) --* 

                Detailed status information about the aggregated associations.

                
              

              - **InstanceAssociationStatusAggregatedCount** *(dict) --* 

                The number of associations for the instance(s).

                
                

                - *(string) --* 
                  

                  - *(integer) --* 
            
          
          
        
      
    

.. py:class:: SSM.Paginator.DescribeParameters

  ::

    
    paginator = client.get_paginator('describe_parameters')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_parameters`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeParameters>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Filters=[
              {
                  'Key': 'Name'|'Type'|'KeyId',
                  'Values': [
                      'string',
                  ]
              },
          ],
          ParameterFilters=[
              {
                  'Key': 'string',
                  'Option': 'string',
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

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The filter values.

          

        
          - *(string) --* 

          
      
      
  
    :type ParameterFilters: list
    :param ParameterFilters: 

      Filters to limit the request results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of results.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **Option** *(string) --* 

          Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.

          

        
        - **Values** *(list) --* 

          The value you want to search for.

          

        
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
            'Parameters': [
                {
                    'Name': 'string',
                    'Type': 'String'|'StringList'|'SecureString',
                    'KeyId': 'string',
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'LastModifiedUser': 'string',
                    'Description': 'string',
                    'AllowedPattern': 'string',
                    'Version': 123
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Parameters** *(list) --* 

          Parameters returned by the request.

          
          

          - *(dict) --* 

            Metada includes information like the ARN of the last user and the date/time the parameter was last used.

            
            

            - **Name** *(string) --* 

              The parameter name.

              
            

            - **Type** *(string) --* 

              The type of parameter. Valid parameter types include the following: String, String list, Secure string.

              
            

            - **KeyId** *(string) --* 

              The ID of the query key used for this parameter.

              
            

            - **LastModifiedDate** *(datetime) --* 

              Date the parameter was last changed or updated.

              
            

            - **LastModifiedUser** *(string) --* 

              Amazon Resource Name (ARN) of the AWS user who last changed the parameter.

              
            

            - **Description** *(string) --* 

              Description of the parameter actions.

              
            

            - **AllowedPattern** *(string) --* 

              A parameter name can include only the following letters and symbols.

               

              a-zA-Z0-9_.-

              
            

            - **Version** *(integer) --* 

              The parameter version.

              
        
      
    

.. py:class:: SSM.Paginator.ListAssociations

  ::

    
    paginator = client.get_paginator('list_associations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_associations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListAssociations>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          AssociationFilterList=[
              {
                  'key': 'InstanceId'|'Name'|'AssociationId'|'AssociationStatusName'|'LastExecutedBefore'|'LastExecutedAfter'|'AssociationName',
                  'value': 'string'
              },
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type AssociationFilterList: list
    :param AssociationFilterList: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        Describes a filter.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The filter value.

          

        
      
  
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
            'Associations': [
                {
                    'Name': 'string',
                    'InstanceId': 'string',
                    'AssociationId': 'string',
                    'AssociationVersion': 'string',
                    'DocumentVersion': 'string',
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'LastExecutionDate': datetime(2015, 1, 1),
                    'Overview': {
                        'Status': 'string',
                        'DetailedStatus': 'string',
                        'AssociationStatusAggregatedCount': {
                            'string': 123
                        }
                    },
                    'ScheduleExpression': 'string',
                    'AssociationName': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Associations** *(list) --* 

          The associations.

          
          

          - *(dict) --* 

            Describes an association of a Systems Manager document and an instance.

            
            

            - **Name** *(string) --* 

              The name of the Systems Manager document.

              
            

            - **InstanceId** *(string) --* 

              The ID of the instance.

              
            

            - **AssociationId** *(string) --* 

              The ID created by the system when you create an association. An association is a binding between a document and a set of targets with a schedule.

              
            

            - **AssociationVersion** *(string) --* 

              The association version.

              
            

            - **DocumentVersion** *(string) --* 

              The version of the document used in the association.

              
            

            - **Targets** *(list) --* 

              The instances targeted by the request to create an association. 

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **LastExecutionDate** *(datetime) --* 

              The date on which the association was last run.

              
            

            - **Overview** *(dict) --* 

              Information about the association.

              
              

              - **Status** *(string) --* 

                The status of the association. Status can be: Pending, Success, or Failed.

                
              

              - **DetailedStatus** *(string) --* 

                A detailed status of the association.

                
              

              - **AssociationStatusAggregatedCount** *(dict) --* 

                Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

                
                

                - *(string) --* 
                  

                  - *(integer) --* 
            
          
          
            

            - **ScheduleExpression** *(string) --* 

              A cron expression that specifies a schedule when the association runs.

              
            

            - **AssociationName** *(string) --* 

              The association name.

              
        
      
    

.. py:class:: SSM.Paginator.ListCommandInvocations

  ::

    
    paginator = client.get_paginator('list_command_invocations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_command_invocations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommandInvocations>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CommandId='string',
          InstanceId='string',
          Filters=[
              {
                  'key': 'InvokedAfter'|'InvokedBefore'|'Status',
                  'value': 'string'
              },
          ],
          Details=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CommandId: string
    :param CommandId: 

      (Optional) The invocations for a specific command ID.

      

    
    :type InstanceId: string
    :param InstanceId: 

      (Optional) The command execution details for a specific instance ID.

      

    
    :type Filters: list
    :param Filters: 

      (Optional) One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        Describes a command filter.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The filter value. 

          

        
      
  
    :type Details: boolean
    :param Details: 

      (Optional) If set this returns the response of the command executions and any command output. By default this is set to False. 

      

    
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
            'CommandInvocations': [
                {
                    'CommandId': 'string',
                    'InstanceId': 'string',
                    'InstanceName': 'string',
                    'Comment': 'string',
                    'DocumentName': 'string',
                    'RequestedDateTime': datetime(2015, 1, 1),
                    'Status': 'Pending'|'InProgress'|'Delayed'|'Success'|'Cancelled'|'TimedOut'|'Failed'|'Cancelling',
                    'StatusDetails': 'string',
                    'TraceOutput': 'string',
                    'StandardOutputUrl': 'string',
                    'StandardErrorUrl': 'string',
                    'CommandPlugins': [
                        {
                            'Name': 'string',
                            'Status': 'Pending'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                            'StatusDetails': 'string',
                            'ResponseCode': 123,
                            'ResponseStartDateTime': datetime(2015, 1, 1),
                            'ResponseFinishDateTime': datetime(2015, 1, 1),
                            'Output': 'string',
                            'StandardOutputUrl': 'string',
                            'StandardErrorUrl': 'string',
                            'OutputS3Region': 'string',
                            'OutputS3BucketName': 'string',
                            'OutputS3KeyPrefix': 'string'
                        },
                    ],
                    'ServiceRole': 'string',
                    'NotificationConfig': {
                        'NotificationArn': 'string',
                        'NotificationEvents': [
                            'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                        ],
                        'NotificationType': 'Command'|'Invocation'
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CommandInvocations** *(list) --* 

          (Optional) A list of all invocations. 

          
          

          - *(dict) --* 

            An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user executes SendCommand against three instances, then a command invocation is created for each requested instance ID. A command invocation returns status and detail information about a command you executed. 

            
            

            - **CommandId** *(string) --* 

              The command against which this invocation was requested.

              
            

            - **InstanceId** *(string) --* 

              The instance ID in which this invocation was requested.

              
            

            - **InstanceName** *(string) --* 

              The name of the invocation target. For Amazon EC2 instances this is the value for the aws:Name tag. For on-premises instances, this is the name of the instance.

              
            

            - **Comment** *(string) --* 

              User-specified information about the command, such as a brief description of what the command should do.

              
            

            - **DocumentName** *(string) --* 

              The document name that was requested for execution.

              
            

            - **RequestedDateTime** *(datetime) --* 

              The time and date the request was sent to this instance.

              
            

            - **Status** *(string) --* 

              Whether or not the invocation succeeded, failed, or is pending.

              
            

            - **StatusDetails** *(string) --* 

              A detailed status of the command execution for each invocation (each instance targeted by the command). StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Run Command Status <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-about-status.html>`__ . StatusDetails can be one of the following values:

               

               
              * Pending: The command has not been sent to the instance. 
               
              * In Progress: The command has been sent to the instance but has not reached a terminal state. 
               
              * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
               
              * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
               
              * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
               
              * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
               
              * Canceled: The command was terminated before it was completed. This is a terminal state. 
               
              * Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
               
              * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
               

              
            

            - **TraceOutput** *(string) --* 

              Gets the trace output sent by the agent. 

              
            

            - **StandardOutputUrl** *(string) --* 

              The URL to the plugin's StdOut file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardOutputUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.

              
            

            - **StandardErrorUrl** *(string) --* 

              The URL to the plugin's StdErr file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardErrorUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.

              
            

            - **CommandPlugins** *(list) --* 
              

              - *(dict) --* 

                Describes plugin details.

                
                

                - **Name** *(string) --* 

                  The name of the plugin. Must be one of the following: aws:updateAgent, aws:domainjoin, aws:applications, aws:runPowerShellScript, aws:psmodule, aws:cloudWatch, aws:runShellScript, or aws:updateSSMAgent. 

                  
                

                - **Status** *(string) --* 

                  The status of this plugin. You can execute a document with multiple plugins.

                  
                

                - **StatusDetails** *(string) --* 

                  A detailed status of the plugin execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Run Command Status <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-about-status.html>`__ . StatusDetails can be one of the following values:

                   

                   
                  * Pending: The command has not been sent to the instance. 
                   
                  * In Progress: The command has been sent to the instance but has not reached a terminal state. 
                   
                  * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
                   
                  * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                   
                  * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
                   
                  * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
                   
                  * Canceled: The command was terminated before it was completed. This is a terminal state. 
                   
                  * Undeliverable: The command can't be delivered to the instance. The instance might not exist, or it might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit, and they don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                   
                  * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
                   

                  
                

                - **ResponseCode** *(integer) --* 

                  A numeric response code generated after executing the plugin. 

                  
                

                - **ResponseStartDateTime** *(datetime) --* 

                  The time the plugin started executing. 

                  
                

                - **ResponseFinishDateTime** *(datetime) --* 

                  The time the plugin stopped executing. Could stop prematurely if, for example, a cancel command was sent. 

                  
                

                - **Output** *(string) --* 

                  Output of the plugin execution.

                  
                

                - **StandardOutputUrl** *(string) --* 

                  The URL for the complete text written by the plugin to stdout in Amazon S3. If the Amazon S3 bucket for the command was not specified, then this string is empty.

                  
                

                - **StandardErrorUrl** *(string) --* 

                  The URL for the complete text written by the plugin to stderr. If execution is not yet complete, then this string is empty.

                  
                

                - **OutputS3Region** *(string) --* 

                  (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

                  
                

                - **OutputS3BucketName** *(string) --* 

                  The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:

                   

                  test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript 

                   

                  test_folder is the name of the Amazon S3 bucket;

                   

                  ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;

                   

                  i-1234567876543 is the instance ID;

                   

                  awsrunShellScript is the name of the plugin.

                  
                

                - **OutputS3KeyPrefix** *(string) --* 

                  The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:

                   

                  test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript 

                   

                  test_folder is the name of the Amazon S3 bucket;

                   

                  ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;

                   

                  i-1234567876543 is the instance ID;

                   

                  awsrunShellScript is the name of the plugin.

                  
            
          
            

            - **ServiceRole** *(string) --* 

              The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes on a per instance basis.

              
            

            - **NotificationConfig** *(dict) --* 

              Configurations for sending notifications about command status changes on a per instance basis.

              
              

              - **NotificationArn** *(string) --* 

                An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

                
              

              - **NotificationEvents** *(list) --* 

                The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

                
                

                - *(string) --* 
            
              

              - **NotificationType** *(string) --* 

                Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

                
          
        
      
    

.. py:class:: SSM.Paginator.ListCommands

  ::

    
    paginator = client.get_paginator('list_commands')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_commands`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommands>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CommandId='string',
          InstanceId='string',
          Filters=[
              {
                  'key': 'InvokedAfter'|'InvokedBefore'|'Status',
                  'value': 'string'
              },
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CommandId: string
    :param CommandId: 

      (Optional) If provided, lists only the specified command.

      

    
    :type InstanceId: string
    :param InstanceId: 

      (Optional) Lists commands issued against this instance ID.

      

    
    :type Filters: list
    :param Filters: 

      (Optional) One or more filters. Use a filter to return a more specific list of results. 

      

    
      - *(dict) --* 

        Describes a command filter.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The filter value. 

          

        
      
  
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
            'Commands': [
                {
                    'CommandId': 'string',
                    'DocumentName': 'string',
                    'Comment': 'string',
                    'ExpiresAfter': datetime(2015, 1, 1),
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    },
                    'InstanceIds': [
                        'string',
                    ],
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'RequestedDateTime': datetime(2015, 1, 1),
                    'Status': 'Pending'|'InProgress'|'Success'|'Cancelled'|'Failed'|'TimedOut'|'Cancelling',
                    'StatusDetails': 'string',
                    'OutputS3Region': 'string',
                    'OutputS3BucketName': 'string',
                    'OutputS3KeyPrefix': 'string',
                    'MaxConcurrency': 'string',
                    'MaxErrors': 'string',
                    'TargetCount': 123,
                    'CompletedCount': 123,
                    'ErrorCount': 123,
                    'ServiceRole': 'string',
                    'NotificationConfig': {
                        'NotificationArn': 'string',
                        'NotificationEvents': [
                            'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                        ],
                        'NotificationType': 'Command'|'Invocation'
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Commands** *(list) --* 

          (Optional) The list of commands requested by the user. 

          
          

          - *(dict) --* 

            Describes a command request.

            
            

            - **CommandId** *(string) --* 

              A unique identifier for this command.

              
            

            - **DocumentName** *(string) --* 

              The name of the document requested for execution.

              
            

            - **Comment** *(string) --* 

              User-specified information about the command, such as a brief description of what the command should do.

              
            

            - **ExpiresAfter** *(datetime) --* 

              If this time is reached and the command has not already started executing, it will not execute. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.

              
            

            - **Parameters** *(dict) --* 

              The parameter values to be inserted in the document when executing the command.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(string) --* 
              
          
        
            

            - **InstanceIds** *(list) --* 

              The instance IDs against which this command was requested.

              
              

              - *(string) --* 
          
            

            - **Targets** *(list) --* 

              An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.

              
              

              - *(dict) --* 

                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.

                 

                

                
                

                - **Key** *(string) --* 

                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                

                - **Values** *(list) --* 

                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **RequestedDateTime** *(datetime) --* 

              The date and time the command was requested.

              
            

            - **Status** *(string) --* 

              The status of the command.

              
            

            - **StatusDetails** *(string) --* 

              A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Run Command Status <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-about-status.html>`__ . StatusDetails can be one of the following values:

               

               
              * Pending: The command has not been sent to any instances. 
               
              * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances. 
               
              * Success: The command successfully executed on all invocations. This is a terminal state. 
               
              * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state. 
               
              * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state. 
               
              * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state. 
               
              * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state. 
               
              * Canceled: The command was terminated before it was completed. This is a terminal state. 
               
              * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before executing it on any instance. This is a terminal state. 
               

              
            

            - **OutputS3Region** *(string) --* 

              (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

              
            

            - **OutputS3BucketName** *(string) --* 

              The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.

              
            

            - **OutputS3KeyPrefix** *(string) --* 

              The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.

              
            

            - **MaxConcurrency** *(string) --* 

              The maximum number of instances that are allowed to execute the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ .

              
            

            - **MaxErrors** *(string) --* 

              The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 50. For more information about how to use MaxErrors, see `Executing a Command Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ .

              
            

            - **TargetCount** *(integer) --* 

              The number of targets for the command.

              
            

            - **CompletedCount** *(integer) --* 

              The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.

              
            

            - **ErrorCount** *(integer) --* 

              The number of targets for which the status is Failed or Execution Timed Out.

              
            

            - **ServiceRole** *(string) --* 

              The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes. 

              
            

            - **NotificationConfig** *(dict) --* 

              Configurations for sending notifications about command status changes. 

              
              

              - **NotificationArn** *(string) --* 

                An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.

                
              

              - **NotificationEvents** *(list) --* 

                The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Setting Up Events and Notifications <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* .

                
                

                - *(string) --* 
            
              

              - **NotificationType** *(string) --* 

                Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 

                
          
        
      
    

.. py:class:: SSM.Paginator.ListDocuments

  ::

    
    paginator = client.get_paginator('list_documents')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_documents`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocuments>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          DocumentFilterList=[
              {
                  'key': 'Name'|'Owner'|'PlatformTypes'|'DocumentType',
                  'value': 'string'
              },
          ],
          Filters=[
              {
                  'Key': 'string',
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
    :type DocumentFilterList: list
    :param DocumentFilterList: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        Describes a filter.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The value of the filter.

          

        
      
  
    :type Filters: list
    :param Filters: 

      One or more filters. Use a filter to return a more specific list of results.

      

    
      - *(dict) --* 

        One or more filters. Use a filter to return a more specific list of documents.

         

        For keys, you can specify one or more tags that have been applied to a document. 

         

        Other valid values include Owner, Name, PlatformTypes, and DocumentType.

         

        Note that only one Owner can be specified in a request. For example: ``Key=Owner,Values=Self`` .

         

        If you use Name as a key, you can use a name prefix to return a list of documents. For example, in the AWS CLI, to return a list of all documents that begin with ``Te`` , run the following command:

         

         ``aws ssm list-documents --filters Key=Name,Values=Te``  

         

        If you specify more than two keys, only documents that are identified by all the tags are returned in the results. If you specify more than two values for a key, documents that are identified by any of the values are returned in the results.

         

        To specify a custom key and value pair, use the format ``Key=tag:[tagName],Values=[valueName]`` .

         

        For example, if you created a Key called region and are using the AWS CLI to call the ``list-documents`` command: 

         

         ``aws ssm list-documents --filters Key=tag:region,Values=east,west Key=Owner,Values=Self``  

        

      
        - **Key** *(string) --* 

          The name of the filter key.

          

        
        - **Values** *(list) --* 

          The value for the filter key.

          

        
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
            'DocumentIdentifiers': [
                {
                    'Name': 'string',
                    'Owner': 'string',
                    'PlatformTypes': [
                        'Windows'|'Linux',
                    ],
                    'DocumentVersion': 'string',
                    'DocumentType': 'Command'|'Policy'|'Automation',
                    'SchemaVersion': 'string',
                    'DocumentFormat': 'YAML'|'JSON',
                    'TargetType': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DocumentIdentifiers** *(list) --* 

          The names of the Systems Manager documents.

          
          

          - *(dict) --* 

            Describes the name of a Systems Manager document.

            
            

            - **Name** *(string) --* 

              The name of the Systems Manager document.

              
            

            - **Owner** *(string) --* 

              The AWS user account that created the document.

              
            

            - **PlatformTypes** *(list) --* 

              The operating system platform. 

              
              

              - *(string) --* 
          
            

            - **DocumentVersion** *(string) --* 

              The document version.

              
            

            - **DocumentType** *(string) --* 

              The document type.

              
            

            - **SchemaVersion** *(string) --* 

              The schema version.

              
            

            - **DocumentFormat** *(string) --* 

              The document format, either JSON or YAML.

              
            

            - **TargetType** *(string) --* 

              The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 

              
            

            - **Tags** *(list) --* 

              The tags, or metadata, that have been applied to the document.

              
              

              - *(dict) --* 

                Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.

                
                

                - **Key** *(string) --* 

                  The name of the tag.

                  
                

                - **Value** *(string) --* 

                  The value of the tag.

                  
            
          
        
      
    