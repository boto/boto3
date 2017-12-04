

**********
Greengrass
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Greengrass.Client

  A low-level client representing AWS Greengrass::

    
    import boto3
    
    client = boto3.client('greengrass')

  
  These are the available methods:
  
  *   :py:meth:`~Greengrass.Client.associate_role_to_group`

  
  *   :py:meth:`~Greengrass.Client.associate_service_role_to_account`

  
  *   :py:meth:`~Greengrass.Client.can_paginate`

  
  *   :py:meth:`~Greengrass.Client.create_core_definition`

  
  *   :py:meth:`~Greengrass.Client.create_core_definition_version`

  
  *   :py:meth:`~Greengrass.Client.create_deployment`

  
  *   :py:meth:`~Greengrass.Client.create_device_definition`

  
  *   :py:meth:`~Greengrass.Client.create_device_definition_version`

  
  *   :py:meth:`~Greengrass.Client.create_function_definition`

  
  *   :py:meth:`~Greengrass.Client.create_function_definition_version`

  
  *   :py:meth:`~Greengrass.Client.create_group`

  
  *   :py:meth:`~Greengrass.Client.create_group_certificate_authority`

  
  *   :py:meth:`~Greengrass.Client.create_group_version`

  
  *   :py:meth:`~Greengrass.Client.create_logger_definition`

  
  *   :py:meth:`~Greengrass.Client.create_logger_definition_version`

  
  *   :py:meth:`~Greengrass.Client.create_resource_definition`

  
  *   :py:meth:`~Greengrass.Client.create_resource_definition_version`

  
  *   :py:meth:`~Greengrass.Client.create_software_update_job`

  
  *   :py:meth:`~Greengrass.Client.create_subscription_definition`

  
  *   :py:meth:`~Greengrass.Client.create_subscription_definition_version`

  
  *   :py:meth:`~Greengrass.Client.delete_core_definition`

  
  *   :py:meth:`~Greengrass.Client.delete_device_definition`

  
  *   :py:meth:`~Greengrass.Client.delete_function_definition`

  
  *   :py:meth:`~Greengrass.Client.delete_group`

  
  *   :py:meth:`~Greengrass.Client.delete_logger_definition`

  
  *   :py:meth:`~Greengrass.Client.delete_resource_definition`

  
  *   :py:meth:`~Greengrass.Client.delete_subscription_definition`

  
  *   :py:meth:`~Greengrass.Client.disassociate_role_from_group`

  
  *   :py:meth:`~Greengrass.Client.disassociate_service_role_from_account`

  
  *   :py:meth:`~Greengrass.Client.generate_presigned_url`

  
  *   :py:meth:`~Greengrass.Client.get_associated_role`

  
  *   :py:meth:`~Greengrass.Client.get_connectivity_info`

  
  *   :py:meth:`~Greengrass.Client.get_core_definition`

  
  *   :py:meth:`~Greengrass.Client.get_core_definition_version`

  
  *   :py:meth:`~Greengrass.Client.get_deployment_status`

  
  *   :py:meth:`~Greengrass.Client.get_device_definition`

  
  *   :py:meth:`~Greengrass.Client.get_device_definition_version`

  
  *   :py:meth:`~Greengrass.Client.get_function_definition`

  
  *   :py:meth:`~Greengrass.Client.get_function_definition_version`

  
  *   :py:meth:`~Greengrass.Client.get_group`

  
  *   :py:meth:`~Greengrass.Client.get_group_certificate_authority`

  
  *   :py:meth:`~Greengrass.Client.get_group_certificate_configuration`

  
  *   :py:meth:`~Greengrass.Client.get_group_version`

  
  *   :py:meth:`~Greengrass.Client.get_logger_definition`

  
  *   :py:meth:`~Greengrass.Client.get_logger_definition_version`

  
  *   :py:meth:`~Greengrass.Client.get_paginator`

  
  *   :py:meth:`~Greengrass.Client.get_resource_definition`

  
  *   :py:meth:`~Greengrass.Client.get_resource_definition_version`

  
  *   :py:meth:`~Greengrass.Client.get_service_role_for_account`

  
  *   :py:meth:`~Greengrass.Client.get_subscription_definition`

  
  *   :py:meth:`~Greengrass.Client.get_subscription_definition_version`

  
  *   :py:meth:`~Greengrass.Client.get_waiter`

  
  *   :py:meth:`~Greengrass.Client.list_core_definition_versions`

  
  *   :py:meth:`~Greengrass.Client.list_core_definitions`

  
  *   :py:meth:`~Greengrass.Client.list_deployments`

  
  *   :py:meth:`~Greengrass.Client.list_device_definition_versions`

  
  *   :py:meth:`~Greengrass.Client.list_device_definitions`

  
  *   :py:meth:`~Greengrass.Client.list_function_definition_versions`

  
  *   :py:meth:`~Greengrass.Client.list_function_definitions`

  
  *   :py:meth:`~Greengrass.Client.list_group_certificate_authorities`

  
  *   :py:meth:`~Greengrass.Client.list_group_versions`

  
  *   :py:meth:`~Greengrass.Client.list_groups`

  
  *   :py:meth:`~Greengrass.Client.list_logger_definition_versions`

  
  *   :py:meth:`~Greengrass.Client.list_logger_definitions`

  
  *   :py:meth:`~Greengrass.Client.list_resource_definition_versions`

  
  *   :py:meth:`~Greengrass.Client.list_resource_definitions`

  
  *   :py:meth:`~Greengrass.Client.list_subscription_definition_versions`

  
  *   :py:meth:`~Greengrass.Client.list_subscription_definitions`

  
  *   :py:meth:`~Greengrass.Client.reset_deployments`

  
  *   :py:meth:`~Greengrass.Client.update_connectivity_info`

  
  *   :py:meth:`~Greengrass.Client.update_core_definition`

  
  *   :py:meth:`~Greengrass.Client.update_device_definition`

  
  *   :py:meth:`~Greengrass.Client.update_function_definition`

  
  *   :py:meth:`~Greengrass.Client.update_group`

  
  *   :py:meth:`~Greengrass.Client.update_group_certificate_configuration`

  
  *   :py:meth:`~Greengrass.Client.update_logger_definition`

  
  *   :py:meth:`~Greengrass.Client.update_resource_definition`

  
  *   :py:meth:`~Greengrass.Client.update_subscription_definition`

  

  .. py:method:: associate_role_to_group(**kwargs)

    Associates a role with a group. The role will be used by the AWS Greengrass core in order to access AWS cloud services. The role's permissions will allow Greengrass core Lambda functions to perform actions against the cloud.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/AssociateRoleToGroup>`_    


    **Request Syntax** 
    ::

      response = client.associate_role_to_group(
          GroupId='string',
          RoleArn='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    :type RoleArn: string
    :param RoleArn: Role arn you wish to associate with this group.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociatedAt': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **AssociatedAt** *(string) --* Time the role arn was associated to your group.
    

  .. py:method:: associate_service_role_to_account(**kwargs)

    Associates a role which is used by AWS Greengrass. AWS Greengrass uses the role to access your Lambda functions and AWS IoT resources. This is necessary for deployments to succeed. It needs to have minimum permissions in policy ``AWSGreengrassResourceAccessRolePolicy``

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/AssociateServiceRoleToAccount>`_    


    **Request Syntax** 
    ::

      response = client.associate_service_role_to_account(
          RoleArn='string'
      )
    :type RoleArn: string
    :param RoleArn: Role arn you wish to associate with this account.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociatedAt': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **AssociatedAt** *(string) --* Time when the service role was associated to the account.
    

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


  .. py:method:: create_core_definition(**kwargs)

    Creates a core definition. You may optionally provide the initial version of the core definition or use ''CreateCoreDefinitionVersion'' at a later time. AWS Greengrass Groups must each contain exactly 1 AWS Greengrass Core.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateCoreDefinition>`_    


    **Request Syntax** 
    ::

      response = client.create_core_definition(
          AmznClientToken='string',
          InitialVersion={
              'Cores': [
                  {
                      'CertificateArn': 'string',
                      'Id': 'string',
                      'SyncShadow': True|False,
                      'ThingArn': 'string'
                  },
              ]
          },
          Name='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type InitialVersion: dict
    :param InitialVersion: Information on the initial version

    
      - **Cores** *(list) --* Cores in the definition version.

      
        - *(dict) --* Information on the core

        
          - **CertificateArn** *(string) --* Certificate arn of the core.

          
          - **Id** *(string) --* Element Id for this entry in the list.

          
          - **SyncShadow** *(boolean) --* If true, the local shadow value automatically syncs with the cloud's shadow state.

          
          - **ThingArn** *(string) --* Thing arn of the core.

          
        
    
    
    :type Name: string
    :param Name: name of the core definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: create_core_definition_version(**kwargs)

    Creates a version of a core definition that has already been defined. AWS Greengrass Groups must each contain exactly 1 AWS Greengrass Core.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateCoreDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_core_definition_version(
          AmznClientToken='string',
          CoreDefinitionId='string',
          Cores=[
              {
                  'CertificateArn': 'string',
                  'Id': 'string',
                  'SyncShadow': True|False,
                  'ThingArn': 'string'
              },
          ]
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type CoreDefinitionId: string
    :param CoreDefinitionId: **[REQUIRED]** core definition Id

    
    :type Cores: list
    :param Cores: Cores in the definition version.

    
      - *(dict) --* Information on the core

      
        - **CertificateArn** *(string) --* Certificate arn of the core.

        
        - **Id** *(string) --* Element Id for this entry in the list.

        
        - **SyncShadow** *(boolean) --* If true, the local shadow value automatically syncs with the cloud's shadow state.

        
        - **ThingArn** *(string) --* Thing arn of the core.

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
        

        - **Id** *(string) --* Id of the resource container.
        

        - **Version** *(string) --* Unique Id of a version.
    

  .. py:method:: create_deployment(**kwargs)

    Creates a deployment.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeployment>`_    


    **Request Syntax** 
    ::

      response = client.create_deployment(
          AmznClientToken='string',
          DeploymentId='string',
          DeploymentType='NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
          GroupId='string',
          GroupVersionId='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type DeploymentId: string
    :param DeploymentId: Id of the deployment if you wish to redeploy a previous deployment.

    
    :type DeploymentType: string
    :param DeploymentType: Type of deployment. When used in CreateDeployment, only NewDeployment and Redeployment are valid. 

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    :type GroupVersionId: string
    :param GroupVersionId: Group Version you wish to deploy.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeploymentArn': 'string',
            'DeploymentId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Successfully deployed the given group
        

        - **DeploymentArn** *(string) --* The arn of the deployment.
        

        - **DeploymentId** *(string) --* The id of the deployment.
    

  .. py:method:: create_device_definition(**kwargs)

    Creates a device definition. You may optinally provide the initial version of the device definition or use ``CreateDeviceDefinitionVersion`` at a later time.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeviceDefinition>`_    


    **Request Syntax** 
    ::

      response = client.create_device_definition(
          AmznClientToken='string',
          InitialVersion={
              'Devices': [
                  {
                      'CertificateArn': 'string',
                      'Id': 'string',
                      'SyncShadow': True|False,
                      'ThingArn': 'string'
                  },
              ]
          },
          Name='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type InitialVersion: dict
    :param InitialVersion: Information on the initial version

    
      - **Devices** *(list) --* Devices in the definition version.

      
        - *(dict) --* Information on a Device

        
          - **CertificateArn** *(string) --* Certificate arn of the device.

          
          - **Id** *(string) --* Element Id for this entry in the list.

          
          - **SyncShadow** *(boolean) --* If true, the local shadow value automatically syncs with the cloud's shadow state.

          
          - **ThingArn** *(string) --* Thing arn of the device.

          
        
    
    
    :type Name: string
    :param Name: name of the device definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: create_device_definition_version(**kwargs)

    Creates a version of a device definition that has already been defined.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeviceDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_device_definition_version(
          AmznClientToken='string',
          DeviceDefinitionId='string',
          Devices=[
              {
                  'CertificateArn': 'string',
                  'Id': 'string',
                  'SyncShadow': True|False,
                  'ThingArn': 'string'
              },
          ]
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type DeviceDefinitionId: string
    :param DeviceDefinitionId: **[REQUIRED]** device definition Id

    
    :type Devices: list
    :param Devices: Devices in the definition version.

    
      - *(dict) --* Information on a Device

      
        - **CertificateArn** *(string) --* Certificate arn of the device.

        
        - **Id** *(string) --* Element Id for this entry in the list.

        
        - **SyncShadow** *(boolean) --* If true, the local shadow value automatically syncs with the cloud's shadow state.

        
        - **ThingArn** *(string) --* Thing arn of the device.

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
        

        - **Id** *(string) --* Id of the resource container.
        

        - **Version** *(string) --* Unique Id of a version.
    

  .. py:method:: create_function_definition(**kwargs)

    Creates a Lambda function definition which contains a list of Lambda functions and their configurations to be used in a group. You can create an initial version of the definition by providing a list of Lambda functions and their configurations now, or use ``CreateFunctionDefinitionVersion`` later.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateFunctionDefinition>`_    


    **Request Syntax** 
    ::

      response = client.create_function_definition(
          AmznClientToken='string',
          InitialVersion={
              'Functions': [
                  {
                      'FunctionArn': 'string',
                      'FunctionConfiguration': {
                          'Environment': {
                              'AccessSysfs': True|False,
                              'ResourceAccessPolicies': [
                                  {
                                      'Permission': 'ro'|'rw',
                                      'ResourceId': 'string'
                                  },
                              ],
                              'Variables': {
                                  'string': 'string'
                              }
                          },
                          'ExecArgs': 'string',
                          'Executable': 'string',
                          'MemorySize': 123,
                          'Pinned': True|False,
                          'Timeout': 123
                      },
                      'Id': 'string'
                  },
              ]
          },
          Name='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type InitialVersion: dict
    :param InitialVersion: Information on the initial version

    
      - **Functions** *(list) --* Lambda functions in this function definition version.

      
        - *(dict) --* Information on function

        
          - **FunctionArn** *(string) --* Arn of the Lambda function.

          
          - **FunctionConfiguration** *(dict) --* Configuration of the function

          
            - **Environment** *(dict) --* Environment of the function configuration

            
              - **AccessSysfs** *(boolean) --* Flag to allow lambda access sys filesystem.

              
              - **ResourceAccessPolicies** *(list) --* Policies for the function to access resources.

              
                - *(dict) --* Policy for the function to access a resource.

                
                  - **Permission** *(string) --* The function's access permission to the resource.

                  
                  - **ResourceId** *(string) --* Id of the resource. A reference to the resource definiton.

                  
                
            
              - **Variables** *(dict) --* Environment variables for the lambda function.

              
                - *(string) --* 

                
                  - *(string) --* 

                  
            
          
            
            - **ExecArgs** *(string) --* Execution Arguments

            
            - **Executable** *(string) --* Executable

            
            - **MemorySize** *(integer) --* The memory size, in KB, you configured for the function.

            
            - **Pinned** *(boolean) --* Whether the function is pinned or not. Pinned means the function is long-lived and starts when the core starts.

            
            - **Timeout** *(integer) --* The function execution time at which Lambda should terminate the function. This timeout still applies to pinned lambdas for each request.

            
          
          - **Id** *(string) --* Id of the function in this version.

          
        
    
    
    :type Name: string
    :param Name: name of the function definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: create_function_definition_version(**kwargs)

    Create a version of a Lambda function definition that has already been defined.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateFunctionDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_function_definition_version(
          AmznClientToken='string',
          FunctionDefinitionId='string',
          Functions=[
              {
                  'FunctionArn': 'string',
                  'FunctionConfiguration': {
                      'Environment': {
                          'AccessSysfs': True|False,
                          'ResourceAccessPolicies': [
                              {
                                  'Permission': 'ro'|'rw',
                                  'ResourceId': 'string'
                              },
                          ],
                          'Variables': {
                              'string': 'string'
                          }
                      },
                      'ExecArgs': 'string',
                      'Executable': 'string',
                      'MemorySize': 123,
                      'Pinned': True|False,
                      'Timeout': 123
                  },
                  'Id': 'string'
              },
          ]
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type FunctionDefinitionId: string
    :param FunctionDefinitionId: **[REQUIRED]** the unique Id of the lambda definition

    
    :type Functions: list
    :param Functions: Lambda functions in this function definition version.

    
      - *(dict) --* Information on function

      
        - **FunctionArn** *(string) --* Arn of the Lambda function.

        
        - **FunctionConfiguration** *(dict) --* Configuration of the function

        
          - **Environment** *(dict) --* Environment of the function configuration

          
            - **AccessSysfs** *(boolean) --* Flag to allow lambda access sys filesystem.

            
            - **ResourceAccessPolicies** *(list) --* Policies for the function to access resources.

            
              - *(dict) --* Policy for the function to access a resource.

              
                - **Permission** *(string) --* The function's access permission to the resource.

                
                - **ResourceId** *(string) --* Id of the resource. A reference to the resource definiton.

                
              
          
            - **Variables** *(dict) --* Environment variables for the lambda function.

            
              - *(string) --* 

              
                - *(string) --* 

                
          
        
          
          - **ExecArgs** *(string) --* Execution Arguments

          
          - **Executable** *(string) --* Executable

          
          - **MemorySize** *(integer) --* The memory size, in KB, you configured for the function.

          
          - **Pinned** *(boolean) --* Whether the function is pinned or not. Pinned means the function is long-lived and starts when the core starts.

          
          - **Timeout** *(integer) --* The function execution time at which Lambda should terminate the function. This timeout still applies to pinned lambdas for each request.

          
        
        - **Id** *(string) --* Id of the function in this version.

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
        

        - **Id** *(string) --* Id of the resource container.
        

        - **Version** *(string) --* Unique Id of a version.
    

  .. py:method:: create_group(**kwargs)

    Creates a group. You may optionally provide the initial version of the group or use ''CreateGroupVersion'' at a later time.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_group(
          AmznClientToken='string',
          InitialVersion={
              'CoreDefinitionVersionArn': 'string',
              'DeviceDefinitionVersionArn': 'string',
              'FunctionDefinitionVersionArn': 'string',
              'LoggerDefinitionVersionArn': 'string',
              'ResourceDefinitionVersionArn': 'string',
              'SubscriptionDefinitionVersionArn': 'string'
          },
          Name='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type InitialVersion: dict
    :param InitialVersion: Information on the initial version

    
      - **CoreDefinitionVersionArn** *(string) --* Core definition version arn for this group.

      
      - **DeviceDefinitionVersionArn** *(string) --* Device definition version arn for this group.

      
      - **FunctionDefinitionVersionArn** *(string) --* Function definition version arn for this group.

      
      - **LoggerDefinitionVersionArn** *(string) --* Logger definition version arn for this group.

      
      - **ResourceDefinitionVersionArn** *(string) --* Resource definition version arn for this group.

      
      - **SubscriptionDefinitionVersionArn** *(string) --* Subscription definition version arn for this group.

      
    
    :type Name: string
    :param Name: name of the group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Group created successfully
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: create_group_certificate_authority(**kwargs)

    Creates a CA for the group. If a CA already exists, it will rotate the existing CA.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroupCertificateAuthority>`_    


    **Request Syntax** 
    ::

      response = client.create_group_certificate_authority(
          AmznClientToken='string',
          GroupId='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GroupCertificateAuthorityArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The response body contains the new active CA ARN
        

        - **GroupCertificateAuthorityArn** *(string) --* Arn of the group certificate authority.
    

  .. py:method:: create_group_version(**kwargs)

    Creates a version of a group which has already been defined.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroupVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_group_version(
          AmznClientToken='string',
          CoreDefinitionVersionArn='string',
          DeviceDefinitionVersionArn='string',
          FunctionDefinitionVersionArn='string',
          GroupId='string',
          LoggerDefinitionVersionArn='string',
          ResourceDefinitionVersionArn='string',
          SubscriptionDefinitionVersionArn='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type CoreDefinitionVersionArn: string
    :param CoreDefinitionVersionArn: Core definition version arn for this group.

    
    :type DeviceDefinitionVersionArn: string
    :param DeviceDefinitionVersionArn: Device definition version arn for this group.

    
    :type FunctionDefinitionVersionArn: string
    :param FunctionDefinitionVersionArn: Function definition version arn for this group.

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    :type LoggerDefinitionVersionArn: string
    :param LoggerDefinitionVersionArn: Logger definition version arn for this group.

    
    :type ResourceDefinitionVersionArn: string
    :param ResourceDefinitionVersionArn: Resource definition version arn for this group.

    
    :type SubscriptionDefinitionVersionArn: string
    :param SubscriptionDefinitionVersionArn: Subscription definition version arn for this group.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* the requested version of the Group
        

        - **Arn** *(string) --* Arn of the version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
        

        - **Id** *(string) --* Id of the resource container.
        

        - **Version** *(string) --* Unique Id of a version.
    

  .. py:method:: create_logger_definition(**kwargs)

    Creates a logger definition. You may optionally provide the initial version of the logger definition or use ``CreateLoggerDefinitionVersion`` at a later time.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateLoggerDefinition>`_    


    **Request Syntax** 
    ::

      response = client.create_logger_definition(
          AmznClientToken='string',
          InitialVersion={
              'Loggers': [
                  {
                      'Component': 'GreengrassSystem'|'Lambda',
                      'Id': 'string',
                      'Level': 'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
                      'Space': 123,
                      'Type': 'FileSystem'|'AWSCloudWatch'
                  },
              ]
          },
          Name='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type InitialVersion: dict
    :param InitialVersion: Information on the initial version

    
      - **Loggers** *(list) --* List of loggers.

      
        - *(dict) --* Information on the Logger

        
          - **Component** *(string) --* The component that will be subject to logs

          
          - **Id** *(string) --* Element Id for this entry in the list.

          
          - **Level** *(string) --* The level of the logs

          
          - **Space** *(integer) --* Amount of hardware space, in KB, to use if file system is used for logging purposes.

          
          - **Type** *(string) --* The type which will be use for log output

          
        
    
    
    :type Name: string
    :param Name: name of the logger definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: create_logger_definition_version(**kwargs)

    Creates a version of a logger definition that has already been defined.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateLoggerDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_logger_definition_version(
          AmznClientToken='string',
          LoggerDefinitionId='string',
          Loggers=[
              {
                  'Component': 'GreengrassSystem'|'Lambda',
                  'Id': 'string',
                  'Level': 'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
                  'Space': 123,
                  'Type': 'FileSystem'|'AWSCloudWatch'
              },
          ]
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type LoggerDefinitionId: string
    :param LoggerDefinitionId: **[REQUIRED]** logger definition Id

    
    :type Loggers: list
    :param Loggers: List of loggers.

    
      - *(dict) --* Information on the Logger

      
        - **Component** *(string) --* The component that will be subject to logs

        
        - **Id** *(string) --* Element Id for this entry in the list.

        
        - **Level** *(string) --* The level of the logs

        
        - **Space** *(integer) --* Amount of hardware space, in KB, to use if file system is used for logging purposes.

        
        - **Type** *(string) --* The type which will be use for log output

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
        

        - **Id** *(string) --* Id of the resource container.
        

        - **Version** *(string) --* Unique Id of a version.
    

  .. py:method:: create_resource_definition(**kwargs)

    Creates a resource definition which contains a list of resources to be used in a group. You can create an initial version of the definition by providing a list of resources now, or use ``CreateResourceDefinitionVersion`` later.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateResourceDefinition>`_    


    **Request Syntax** 
    ::

      response = client.create_resource_definition(
          AmznClientToken='string',
          InitialVersion={
              'Resources': [
                  {
                      'Id': 'string',
                      'Name': 'string',
                      'ResourceDataContainer': {
                          'LocalDeviceResourceData': {
                              'GroupOwnerSetting': {
                                  'AutoAddGroupOwner': True|False,
                                  'GroupOwner': 'string'
                              },
                              'SourcePath': 'string'
                          },
                          'LocalVolumeResourceData': {
                              'DestinationPath': 'string',
                              'GroupOwnerSetting': {
                                  'AutoAddGroupOwner': True|False,
                                  'GroupOwner': 'string'
                              },
                              'SourcePath': 'string'
                          }
                      }
                  },
              ]
          },
          Name='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type InitialVersion: dict
    :param InitialVersion: Information on the initial version

    
      - **Resources** *(list) --* List of resources.

      
        - *(dict) --* Information on the resource.

        
          - **Id** *(string) --* Resource Id.

          
          - **Name** *(string) --* A descriptive resource name.

          
          - **ResourceDataContainer** *(dict) --* A container of data for all resource types.

          
            - **LocalDeviceResourceData** *(dict) --* Attributes that define the Local Device Resource.

            
              - **GroupOwnerSetting** *(dict) --* Group owner related settings for local resources.

              
                - **AutoAddGroupOwner** *(boolean) --* Eanble the auto added group owner.

                
                - **GroupOwner** *(string) --* Name of the group owner.

                
              
              - **SourcePath** *(string) --* Local source path of the resource.

              
            
            - **LocalVolumeResourceData** *(dict) --* Attributes that define the Local Volume Resource.

            
              - **DestinationPath** *(string) --* Local destination path of the resource.

              
              - **GroupOwnerSetting** *(dict) --* Group owner related settings for local resources.

              
                - **AutoAddGroupOwner** *(boolean) --* Eanble the auto added group owner.

                
                - **GroupOwner** *(string) --* Name of the group owner.

                
              
              - **SourcePath** *(string) --* Local source path of the resource.

              
            
          
        
    
    
    :type Name: string
    :param Name: Name of the resource definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: create_resource_definition_version(**kwargs)

    Create a version of a resource definition that has already been defined.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateResourceDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_resource_definition_version(
          AmznClientToken='string',
          ResourceDefinitionId='string',
          Resources=[
              {
                  'Id': 'string',
                  'Name': 'string',
                  'ResourceDataContainer': {
                      'LocalDeviceResourceData': {
                          'GroupOwnerSetting': {
                              'AutoAddGroupOwner': True|False,
                              'GroupOwner': 'string'
                          },
                          'SourcePath': 'string'
                      },
                      'LocalVolumeResourceData': {
                          'DestinationPath': 'string',
                          'GroupOwnerSetting': {
                              'AutoAddGroupOwner': True|False,
                              'GroupOwner': 'string'
                          },
                          'SourcePath': 'string'
                      }
                  }
              },
          ]
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type ResourceDefinitionId: string
    :param ResourceDefinitionId: **[REQUIRED]** Resource definition Id.

    
    :type Resources: list
    :param Resources: List of resources.

    
      - *(dict) --* Information on the resource.

      
        - **Id** *(string) --* Resource Id.

        
        - **Name** *(string) --* A descriptive resource name.

        
        - **ResourceDataContainer** *(dict) --* A container of data for all resource types.

        
          - **LocalDeviceResourceData** *(dict) --* Attributes that define the Local Device Resource.

          
            - **GroupOwnerSetting** *(dict) --* Group owner related settings for local resources.

            
              - **AutoAddGroupOwner** *(boolean) --* Eanble the auto added group owner.

              
              - **GroupOwner** *(string) --* Name of the group owner.

              
            
            - **SourcePath** *(string) --* Local source path of the resource.

            
          
          - **LocalVolumeResourceData** *(dict) --* Attributes that define the Local Volume Resource.

          
            - **DestinationPath** *(string) --* Local destination path of the resource.

            
            - **GroupOwnerSetting** *(dict) --* Group owner related settings for local resources.

            
              - **AutoAddGroupOwner** *(boolean) --* Eanble the auto added group owner.

              
              - **GroupOwner** *(string) --* Name of the group owner.

              
            
            - **SourcePath** *(string) --* Local source path of the resource.

            
          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
        

        - **Id** *(string) --* Id of the resource container.
        

        - **Version** *(string) --* Unique Id of a version.
    

  .. py:method:: create_software_update_job(**kwargs)

    Creates an Iot Job that will trigger your Greengrass Cores to update the software they are running.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSoftwareUpdateJob>`_    


    **Request Syntax** 
    ::

      response = client.create_software_update_job(
          AmznClientToken='string',
          S3UrlSignerRole='string',
          SoftwareToUpdate='core'|'ota_agent',
          UpdateAgentLogLevel='NONE'|'TRACE'|'DEBUG'|'VERBOSE'|'INFO'|'WARN'|'ERROR'|'FATAL',
          UpdateTargets=[
              'string',
          ],
          UpdateTargetsArchitecture='armv7l'|'x86_64'|'aarch64',
          UpdateTargetsOperatingSystem='ubuntu'|'raspbian'|'amazon_linux'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type S3UrlSignerRole: string
    :param S3UrlSignerRole: The IAM Role that Greengrass will use to create pre-signed URLs pointing towards the update artifact.

    
    :type SoftwareToUpdate: string
    :param SoftwareToUpdate: The piece of software on the Greengrass Core that will be updated.

    
    :type UpdateAgentLogLevel: string
    :param UpdateAgentLogLevel: The minimum level of log statements that should be logged by the OTA Agent during an update.

    
    :type UpdateTargets: list
    :param UpdateTargets: The target arns that this update will be applied to.

    
      - *(string) --* 

      
  
    :type UpdateTargetsArchitecture: string
    :param UpdateTargetsArchitecture: The architecture of the Cores in the targets of an update

    
    :type UpdateTargetsOperatingSystem: string
    :param UpdateTargetsOperatingSystem: The operating system of the Cores in the targets of an update

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IotJobArn': 'string',
            'IotJobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **IotJobArn** *(string) --* The Iot Job Arn corresponding to this update.
        

        - **IotJobId** *(string) --* The Iot Job Id corresponding to this update.
    

  .. py:method:: create_subscription_definition(**kwargs)

    Creates a subscription definition. You may optionally provide the initial version of the subscription definition or use ``CreateSubscriptionDefinitionVersion`` at a later time.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSubscriptionDefinition>`_    


    **Request Syntax** 
    ::

      response = client.create_subscription_definition(
          AmznClientToken='string',
          InitialVersion={
              'Subscriptions': [
                  {
                      'Id': 'string',
                      'Source': 'string',
                      'Subject': 'string',
                      'Target': 'string'
                  },
              ]
          },
          Name='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type InitialVersion: dict
    :param InitialVersion: Information on the initial version

    
      - **Subscriptions** *(list) --* Subscriptions in the version.

      
        - *(dict) --* Information on subscription

        
          - **Id** *(string) --* Element Id for this entry in the list.

          
          - **Source** *(string) --* Source of the subscription. Can be a thing arn, lambda arn or word 'cloud'

          
          - **Subject** *(string) --* Subject of the message.

          
          - **Target** *(string) --* Where the message is sent to. Can be a thing arn, lambda arn or word 'cloud'.

          
        
    
    
    :type Name: string
    :param Name: name of the subscription definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: create_subscription_definition_version(**kwargs)

    Creates a version of a subscription definition which has already been defined.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSubscriptionDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_subscription_definition_version(
          AmznClientToken='string',
          SubscriptionDefinitionId='string',
          Subscriptions=[
              {
                  'Id': 'string',
                  'Source': 'string',
                  'Subject': 'string',
                  'Target': 'string'
              },
          ]
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type SubscriptionDefinitionId: string
    :param SubscriptionDefinitionId: **[REQUIRED]** subscription definition Id

    
    :type Subscriptions: list
    :param Subscriptions: Subscriptions in the version.

    
      - *(dict) --* Information on subscription

      
        - **Id** *(string) --* Element Id for this entry in the list.

        
        - **Source** *(string) --* Source of the subscription. Can be a thing arn, lambda arn or word 'cloud'

        
        - **Subject** *(string) --* Subject of the message.

        
        - **Target** *(string) --* Where the message is sent to. Can be a thing arn, lambda arn or word 'cloud'.

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
        

        - **Id** *(string) --* Id of the resource container.
        

        - **Version** *(string) --* Unique Id of a version.
    

  .. py:method:: delete_core_definition(**kwargs)

    Deletes a core definition. The core definition must not have been used in a deployment.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteCoreDefinition>`_    


    **Request Syntax** 
    ::

      response = client.delete_core_definition(
          CoreDefinitionId='string'
      )
    :type CoreDefinitionId: string
    :param CoreDefinitionId: **[REQUIRED]** core definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: delete_device_definition(**kwargs)

    Deletes a device definition. The device definition must not have been used in a deployment.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteDeviceDefinition>`_    


    **Request Syntax** 
    ::

      response = client.delete_device_definition(
          DeviceDefinitionId='string'
      )
    :type DeviceDefinitionId: string
    :param DeviceDefinitionId: **[REQUIRED]** device definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: delete_function_definition(**kwargs)

    Deletes a Lambda function definition. The Lambda function definition must not have been used in a deployment.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteFunctionDefinition>`_    


    **Request Syntax** 
    ::

      response = client.delete_function_definition(
          FunctionDefinitionId='string'
      )
    :type FunctionDefinitionId: string
    :param FunctionDefinitionId: **[REQUIRED]** the unique Id of the lambda definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: delete_group(**kwargs)

    Deletes a group. The group must not have been used in deployment.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_group(
          GroupId='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: delete_logger_definition(**kwargs)

    Deletes a logger definition. The logger definition must not have been used in a deployment.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteLoggerDefinition>`_    


    **Request Syntax** 
    ::

      response = client.delete_logger_definition(
          LoggerDefinitionId='string'
      )
    :type LoggerDefinitionId: string
    :param LoggerDefinitionId: **[REQUIRED]** logger definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: delete_resource_definition(**kwargs)

    Deletes a resource definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteResourceDefinition>`_    


    **Request Syntax** 
    ::

      response = client.delete_resource_definition(
          ResourceDefinitionId='string'
      )
    :type ResourceDefinitionId: string
    :param ResourceDefinitionId: **[REQUIRED]** Resource definition Id.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: delete_subscription_definition(**kwargs)

    Deletes a subscription definition. The subscription definition must not have been used in a deployment.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteSubscriptionDefinition>`_    


    **Request Syntax** 
    ::

      response = client.delete_subscription_definition(
          SubscriptionDefinitionId='string'
      )
    :type SubscriptionDefinitionId: string
    :param SubscriptionDefinitionId: **[REQUIRED]** subscription definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: disassociate_role_from_group(**kwargs)

    Disassociates the role from a group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DisassociateRoleFromGroup>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_role_from_group(
          GroupId='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DisassociatedAt': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **DisassociatedAt** *(string) --* Time when the role was disassociated from the group.
    

  .. py:method:: disassociate_service_role_from_account()

    Disassociates the service role from the account. Without a service role, deployments will not work.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DisassociateServiceRoleFromAccount>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_service_role_from_account()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DisassociatedAt': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **DisassociatedAt** *(string) --* Time when the service role was disassociated from the account.
    

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


  .. py:method:: get_associated_role(**kwargs)

    Retrieves the role associated with a particular group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetAssociatedRole>`_    


    **Request Syntax** 
    ::

      response = client.get_associated_role(
          GroupId='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociatedAt': 'string',
            'RoleArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **AssociatedAt** *(string) --* Time when the role was associated for the group.
        

        - **RoleArn** *(string) --* Arn of the role that is associated with the group.
    

  .. py:method:: get_connectivity_info(**kwargs)

    Retrieves the connectivity information for a core.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetConnectivityInfo>`_    


    **Request Syntax** 
    ::

      response = client.get_connectivity_info(
          ThingName='string'
      )
    :type ThingName: string
    :param ThingName: **[REQUIRED]** Thing Name

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConnectivityInfo': [
                {
                    'HostAddress': 'string',
                    'Id': 'string',
                    'Metadata': 'string',
                    'PortNumber': 123
                },
            ],
            'Message': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **ConnectivityInfo** *(list) --* Connectivity info list
          

          - *(dict) --* Connectivity Info
            

            - **HostAddress** *(string) --* Endpoint for the GGC. Can be an IP address or DNS.
            

            - **Id** *(string) --* Element Id for this entry in the list.
            

            - **Metadata** *(string) --* Metadata for this endpoint.
            

            - **PortNumber** *(integer) --* Port of the GGC. Usually 8883.
        
      
        

        - **Message** *(string) --* Response Text
    

  .. py:method:: get_core_definition(**kwargs)

    Retrieves information about a core definition version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetCoreDefinition>`_    


    **Request Syntax** 
    ::

      response = client.get_core_definition(
          CoreDefinitionId='string'
      )
    :type CoreDefinitionId: string
    :param CoreDefinitionId: **[REQUIRED]** core definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: get_core_definition_version(**kwargs)

    Retrieves information about a core definition version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetCoreDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_core_definition_version(
          CoreDefinitionId='string',
          CoreDefinitionVersionId='string'
      )
    :type CoreDefinitionId: string
    :param CoreDefinitionId: **[REQUIRED]** core definition Id

    
    :type CoreDefinitionVersionId: string
    :param CoreDefinitionVersionId: **[REQUIRED]** core definition version Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Definition': {
                'Cores': [
                    {
                        'CertificateArn': 'string',
                        'Id': 'string',
                        'SyncShadow': True|False,
                        'ThingArn': 'string'
                    },
                ]
            },
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Arn** *(string) --* Arn of the core definition version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the core definition version was created.
        

        - **Definition** *(dict) --* Information on definition
          

          - **Cores** *(list) --* Cores in the definition version.
            

            - *(dict) --* Information on the core
              

              - **CertificateArn** *(string) --* Certificate arn of the core.
              

              - **Id** *(string) --* Element Id for this entry in the list.
              

              - **SyncShadow** *(boolean) --* If true, the local shadow value automatically syncs with the cloud's shadow state.
              

              - **ThingArn** *(string) --* Thing arn of the core.
          
        
      
        

        - **Id** *(string) --* Id of the core definition the version belongs to.
        

        - **Version** *(string) --* Version of the core definition version.
    

  .. py:method:: get_deployment_status(**kwargs)

    Returns the status of a deployment.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeploymentStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_deployment_status(
          DeploymentId='string',
          GroupId='string'
      )
    :type DeploymentId: string
    :param DeploymentId: **[REQUIRED]** the deployment Id

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeploymentStatus': 'string',
            'DeploymentType': 'NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
            'ErrorDetails': [
                {
                    'DetailedErrorCode': 'string',
                    'DetailedErrorMessage': 'string'
                },
            ],
            'ErrorMessage': 'string',
            'UpdatedAt': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The response body contains the status of a deployment for a group.
        

        - **DeploymentStatus** *(string) --* Status of the deployment.
        

        - **DeploymentType** *(string) --* The type of the deployment.
        

        - **ErrorDetails** *(list) --* The error Details
          

          - *(dict) --* ErrorDetail
            

            - **DetailedErrorCode** *(string) --* Detailed Error Code
            

            - **DetailedErrorMessage** *(string) --* Detailed Error Message
        
      
        

        - **ErrorMessage** *(string) --* Error Message
        

        - **UpdatedAt** *(string) --* Last time the deployment status was updated.
    

  .. py:method:: get_device_definition(**kwargs)

    Retrieves information about a device definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeviceDefinition>`_    


    **Request Syntax** 
    ::

      response = client.get_device_definition(
          DeviceDefinitionId='string'
      )
    :type DeviceDefinitionId: string
    :param DeviceDefinitionId: **[REQUIRED]** device definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: get_device_definition_version(**kwargs)

    Retrieves information about a device definition version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeviceDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_device_definition_version(
          DeviceDefinitionId='string',
          DeviceDefinitionVersionId='string'
      )
    :type DeviceDefinitionId: string
    :param DeviceDefinitionId: **[REQUIRED]** device definition Id

    
    :type DeviceDefinitionVersionId: string
    :param DeviceDefinitionVersionId: **[REQUIRED]** device definition version Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Definition': {
                'Devices': [
                    {
                        'CertificateArn': 'string',
                        'Id': 'string',
                        'SyncShadow': True|False,
                        'ThingArn': 'string'
                    },
                ]
            },
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the device definition version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the device definition version was created.
        

        - **Definition** *(dict) --* Device definition version
          

          - **Devices** *(list) --* Devices in the definition version.
            

            - *(dict) --* Information on a Device
              

              - **CertificateArn** *(string) --* Certificate arn of the device.
              

              - **Id** *(string) --* Element Id for this entry in the list.
              

              - **SyncShadow** *(boolean) --* If true, the local shadow value automatically syncs with the cloud's shadow state.
              

              - **ThingArn** *(string) --* Thing arn of the device.
          
        
      
        

        - **Id** *(string) --* Id of the device definition the version belongs to.
        

        - **Version** *(string) --* Version of the device definition version.
    

  .. py:method:: get_function_definition(**kwargs)

    Retrieves information about a Lambda function definition, such as its creation time and latest version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetFunctionDefinition>`_    


    **Request Syntax** 
    ::

      response = client.get_function_definition(
          FunctionDefinitionId='string'
      )
    :type FunctionDefinitionId: string
    :param FunctionDefinitionId: **[REQUIRED]** the unique Id of the lambda definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: get_function_definition_version(**kwargs)

    Retrieves information about a Lambda function definition version, such as which Lambda functions are included in the version and their configurations.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetFunctionDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_function_definition_version(
          FunctionDefinitionId='string',
          FunctionDefinitionVersionId='string'
      )
    :type FunctionDefinitionId: string
    :param FunctionDefinitionId: **[REQUIRED]** the unique Id of the lambda definition

    
    :type FunctionDefinitionVersionId: string
    :param FunctionDefinitionVersionId: **[REQUIRED]** Function definition version Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Definition': {
                'Functions': [
                    {
                        'FunctionArn': 'string',
                        'FunctionConfiguration': {
                            'Environment': {
                                'AccessSysfs': True|False,
                                'ResourceAccessPolicies': [
                                    {
                                        'Permission': 'ro'|'rw',
                                        'ResourceId': 'string'
                                    },
                                ],
                                'Variables': {
                                    'string': 'string'
                                }
                            },
                            'ExecArgs': 'string',
                            'Executable': 'string',
                            'MemorySize': 123,
                            'Pinned': True|False,
                            'Timeout': 123
                        },
                        'Id': 'string'
                    },
                ]
            },
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Arn** *(string) --* Arn of the function definition version.
        

        - **CreationTimestamp** *(string) --* Timestamp when the funtion definition version was created.
        

        - **Definition** *(dict) --* Information on the definition
          

          - **Functions** *(list) --* Lambda functions in this function definition version.
            

            - *(dict) --* Information on function
              

              - **FunctionArn** *(string) --* Arn of the Lambda function.
              

              - **FunctionConfiguration** *(dict) --* Configuration of the function
                

                - **Environment** *(dict) --* Environment of the function configuration
                  

                  - **AccessSysfs** *(boolean) --* Flag to allow lambda access sys filesystem.
                  

                  - **ResourceAccessPolicies** *(list) --* Policies for the function to access resources.
                    

                    - *(dict) --* Policy for the function to access a resource.
                      

                      - **Permission** *(string) --* The function's access permission to the resource.
                      

                      - **ResourceId** *(string) --* Id of the resource. A reference to the resource definiton.
                  
                
                  

                  - **Variables** *(dict) --* Environment variables for the lambda function.
                    

                    - *(string) --* 
                      

                      - *(string) --* 
                
              
              
                

                - **ExecArgs** *(string) --* Execution Arguments
                

                - **Executable** *(string) --* Executable
                

                - **MemorySize** *(integer) --* The memory size, in KB, you configured for the function.
                

                - **Pinned** *(boolean) --* Whether the function is pinned or not. Pinned means the function is long-lived and starts when the core starts.
                

                - **Timeout** *(integer) --* The function execution time at which Lambda should terminate the function. This timeout still applies to pinned lambdas for each request.
            
              

              - **Id** *(string) --* Id of the function in this version.
          
        
      
        

        - **Id** *(string) --* Id of the function definition the version belongs to.
        

        - **Version** *(string) --* Version of the function definition version.
    

  .. py:method:: get_group(**kwargs)

    Retrieves information about a group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroup>`_    


    **Request Syntax** 
    ::

      response = client.get_group(
          GroupId='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* the requested Group
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: get_group_certificate_authority(**kwargs)

    Retreives the CA associated with a group. Returns the public key of the CA.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupCertificateAuthority>`_    


    **Request Syntax** 
    ::

      response = client.get_group_certificate_authority(
          CertificateAuthorityId='string',
          GroupId='string'
      )
    :type CertificateAuthorityId: string
    :param CertificateAuthorityId: **[REQUIRED]** certificate authority Id

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GroupCertificateAuthorityArn': 'string',
            'GroupCertificateAuthorityId': 'string',
            'PemEncodedCertificate': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The response body contains the PKI Configuration
        

        - **GroupCertificateAuthorityArn** *(string) --* Arn of the certificate authority for the group.
        

        - **GroupCertificateAuthorityId** *(string) --* Id of the certificate authority for the group.
        

        - **PemEncodedCertificate** *(string) --* PEM encoded certificate for the group.
    

  .. py:method:: get_group_certificate_configuration(**kwargs)

    Retrieves the current configuration for the CA used by the group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupCertificateConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.get_group_certificate_configuration(
          GroupId='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CertificateAuthorityExpiryInMilliseconds': 'string',
            'CertificateExpiryInMilliseconds': 'string',
            'GroupId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The response body contains the PKI Configuration
        

        - **CertificateAuthorityExpiryInMilliseconds** *(string) --* Amount of time when the certificate authority expires in milliseconds.
        

        - **CertificateExpiryInMilliseconds** *(string) --* Amount of time when the certificate expires in milliseconds.
        

        - **GroupId** *(string) --* Id of the group the certificate configuration belongs to.
    

  .. py:method:: get_group_version(**kwargs)

    Retrieves information about a group version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_group_version(
          GroupId='string',
          GroupVersionId='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    :type GroupVersionId: string
    :param GroupVersionId: **[REQUIRED]** Group version Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Definition': {
                'CoreDefinitionVersionArn': 'string',
                'DeviceDefinitionVersionArn': 'string',
                'FunctionDefinitionVersionArn': 'string',
                'LoggerDefinitionVersionArn': 'string',
                'ResourceDefinitionVersionArn': 'string',
                'SubscriptionDefinitionVersionArn': 'string'
            },
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Arn** *(string) --* Arn of the group version.
        

        - **CreationTimestamp** *(string) --* Timestamp when the group version was created.
        

        - **Definition** *(dict) --* Information on the definition
          

          - **CoreDefinitionVersionArn** *(string) --* Core definition version arn for this group.
          

          - **DeviceDefinitionVersionArn** *(string) --* Device definition version arn for this group.
          

          - **FunctionDefinitionVersionArn** *(string) --* Function definition version arn for this group.
          

          - **LoggerDefinitionVersionArn** *(string) --* Logger definition version arn for this group.
          

          - **ResourceDefinitionVersionArn** *(string) --* Resource definition version arn for this group.
          

          - **SubscriptionDefinitionVersionArn** *(string) --* Subscription definition version arn for this group.
      
        

        - **Id** *(string) --* Id of the group version.
        

        - **Version** *(string) --* Unique Id for a version of the Group.
    

  .. py:method:: get_logger_definition(**kwargs)

    Retrieves information about a logger definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetLoggerDefinition>`_    


    **Request Syntax** 
    ::

      response = client.get_logger_definition(
          LoggerDefinitionId='string'
      )
    :type LoggerDefinitionId: string
    :param LoggerDefinitionId: **[REQUIRED]** logger definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: get_logger_definition_version(**kwargs)

    Retrieves information about a logger definition version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetLoggerDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_logger_definition_version(
          LoggerDefinitionId='string',
          LoggerDefinitionVersionId='string'
      )
    :type LoggerDefinitionId: string
    :param LoggerDefinitionId: **[REQUIRED]** logger definition Id

    
    :type LoggerDefinitionVersionId: string
    :param LoggerDefinitionVersionId: **[REQUIRED]** logger definition version Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Definition': {
                'Loggers': [
                    {
                        'Component': 'GreengrassSystem'|'Lambda',
                        'Id': 'string',
                        'Level': 'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
                        'Space': 123,
                        'Type': 'FileSystem'|'AWSCloudWatch'
                    },
                ]
            },
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* test
        

        - **Arn** *(string) --* Arn of the logger definition version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the logger definition version was created.
        

        - **Definition** *(dict) --* Information on definition
          

          - **Loggers** *(list) --* List of loggers.
            

            - *(dict) --* Information on the Logger
              

              - **Component** *(string) --* The component that will be subject to logs
              

              - **Id** *(string) --* Element Id for this entry in the list.
              

              - **Level** *(string) --* The level of the logs
              

              - **Space** *(integer) --* Amount of hardware space, in KB, to use if file system is used for logging purposes.
              

              - **Type** *(string) --* The type which will be use for log output
          
        
      
        

        - **Id** *(string) --* Id of the logger definition the version belongs to.
        

        - **Version** *(string) --* Version of the logger definition version.
    

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


  .. py:method:: get_resource_definition(**kwargs)

    Retrieves information about a resource definition, such as its creation time and latest version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetResourceDefinition>`_    


    **Request Syntax** 
    ::

      response = client.get_resource_definition(
          ResourceDefinitionId='string'
      )
    :type ResourceDefinitionId: string
    :param ResourceDefinitionId: **[REQUIRED]** Resource definition Id.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: get_resource_definition_version(**kwargs)

    Retrieves information about a resource definition version, such as which resources are included in the version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetResourceDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_resource_definition_version(
          ResourceDefinitionId='string',
          ResourceDefinitionVersionId='string'
      )
    :type ResourceDefinitionId: string
    :param ResourceDefinitionId: **[REQUIRED]** Resource definition Id.

    
    :type ResourceDefinitionVersionId: string
    :param ResourceDefinitionVersionId: **[REQUIRED]** Resource definition version Id.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Definition': {
                'Resources': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'ResourceDataContainer': {
                            'LocalDeviceResourceData': {
                                'GroupOwnerSetting': {
                                    'AutoAddGroupOwner': True|False,
                                    'GroupOwner': 'string'
                                },
                                'SourcePath': 'string'
                            },
                            'LocalVolumeResourceData': {
                                'DestinationPath': 'string',
                                'GroupOwnerSetting': {
                                    'AutoAddGroupOwner': True|False,
                                    'GroupOwner': 'string'
                                },
                                'SourcePath': 'string'
                            }
                        }
                    },
                ]
            },
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Arn** *(string) --* Arn of the resource definition version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the resource definition version was created.
        

        - **Definition** *(dict) --* Information on definition.
          

          - **Resources** *(list) --* List of resources.
            

            - *(dict) --* Information on the resource.
              

              - **Id** *(string) --* Resource Id.
              

              - **Name** *(string) --* A descriptive resource name.
              

              - **ResourceDataContainer** *(dict) --* A container of data for all resource types.
                

                - **LocalDeviceResourceData** *(dict) --* Attributes that define the Local Device Resource.
                  

                  - **GroupOwnerSetting** *(dict) --* Group owner related settings for local resources.
                    

                    - **AutoAddGroupOwner** *(boolean) --* Eanble the auto added group owner.
                    

                    - **GroupOwner** *(string) --* Name of the group owner.
                
                  

                  - **SourcePath** *(string) --* Local source path of the resource.
              
                

                - **LocalVolumeResourceData** *(dict) --* Attributes that define the Local Volume Resource.
                  

                  - **DestinationPath** *(string) --* Local destination path of the resource.
                  

                  - **GroupOwnerSetting** *(dict) --* Group owner related settings for local resources.
                    

                    - **AutoAddGroupOwner** *(boolean) --* Eanble the auto added group owner.
                    

                    - **GroupOwner** *(string) --* Name of the group owner.
                
                  

                  - **SourcePath** *(string) --* Local source path of the resource.
              
            
          
        
      
        

        - **Id** *(string) --* Id of the resource definition the version belongs to.
        

        - **Version** *(string) --* Version of the resource definition version.
    

  .. py:method:: get_service_role_for_account()

    Retrieves the service role that is attached to the account.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetServiceRoleForAccount>`_    


    **Request Syntax** 
    ::

      response = client.get_service_role_for_account()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AssociatedAt': 'string',
            'RoleArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **AssociatedAt** *(string) --* Time when the service role was associated to the account.
        

        - **RoleArn** *(string) --* Role arn which is associated to the account.
    

  .. py:method:: get_subscription_definition(**kwargs)

    Retrieves information about a subscription definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetSubscriptionDefinition>`_    


    **Request Syntax** 
    ::

      response = client.get_subscription_definition(
          SubscriptionDefinitionId='string'
      )
    :type SubscriptionDefinitionId: string
    :param SubscriptionDefinitionId: **[REQUIRED]** subscription definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Id': 'string',
            'LastUpdatedTimestamp': 'string',
            'LatestVersion': 'string',
            'LatestVersionArn': 'string',
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the definition.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
        

        - **Id** *(string) --* Id of the definition.
        

        - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
        

        - **LatestVersion** *(string) --* Last version of the definition.
        

        - **LatestVersionArn** *(string) --* Latest version arn of the definition.
        

        - **Name** *(string) --* Name of the definition.
    

  .. py:method:: get_subscription_definition_version(**kwargs)

    Retrieves information about a subscription definition version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetSubscriptionDefinitionVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_subscription_definition_version(
          SubscriptionDefinitionId='string',
          SubscriptionDefinitionVersionId='string'
      )
    :type SubscriptionDefinitionId: string
    :param SubscriptionDefinitionId: **[REQUIRED]** subscription definition Id

    
    :type SubscriptionDefinitionVersionId: string
    :param SubscriptionDefinitionVersionId: **[REQUIRED]** subscription definition version Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'CreationTimestamp': 'string',
            'Definition': {
                'Subscriptions': [
                    {
                        'Id': 'string',
                        'Source': 'string',
                        'Subject': 'string',
                        'Target': 'string'
                    },
                ]
            },
            'Id': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* Arn of the subscription definition version.
        

        - **CreationTimestamp** *(string) --* Timestamp of when the subscription definition version was created.
        

        - **Definition** *(dict) --* Information on the definition
          

          - **Subscriptions** *(list) --* Subscriptions in the version.
            

            - *(dict) --* Information on subscription
              

              - **Id** *(string) --* Element Id for this entry in the list.
              

              - **Source** *(string) --* Source of the subscription. Can be a thing arn, lambda arn or word 'cloud'
              

              - **Subject** *(string) --* Subject of the message.
              

              - **Target** *(string) --* Where the message is sent to. Can be a thing arn, lambda arn or word 'cloud'.
          
        
      
        

        - **Id** *(string) --* Id of the subscription definition the version belongs to.
        

        - **Version** *(string) --* Version of the subscription definition version.
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_core_definition_versions(**kwargs)

    Lists versions of a core definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListCoreDefinitionVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_core_definition_versions(
          CoreDefinitionId='string',
          MaxResults='string',
          NextToken='string'
      )
    :type CoreDefinitionId: string
    :param CoreDefinitionId: **[REQUIRED]** core definition Id

    
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'Versions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'Version': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
        

        - **Versions** *(list) --* Versions
          

          - *(dict) --* Information on the version
            

            - **Arn** *(string) --* Arn of the version.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
            

            - **Id** *(string) --* Id of the resource container.
            

            - **Version** *(string) --* Unique Id of a version.
        
      
    

  .. py:method:: list_core_definitions(**kwargs)

    Retrieves a list of core definitions.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListCoreDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.list_core_definitions(
          MaxResults='string',
          NextToken='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Definitions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'LastUpdatedTimestamp': 'string',
                    'LatestVersion': 'string',
                    'LatestVersionArn': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Definitions** *(list) --* Definitions
          

          - *(dict) --* Information on the Definition
            

            - **Arn** *(string) --* Arn of the definition.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
            

            - **Id** *(string) --* Id of the definition.
            

            - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
            

            - **LatestVersion** *(string) --* Last version of the definition.
            

            - **LatestVersionArn** *(string) --* Latest version arn of the definition.
            

            - **Name** *(string) --* Name of the definition.
        
      
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
    

  .. py:method:: list_deployments(**kwargs)

    Returns a history of deployments for the group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeployments>`_    


    **Request Syntax** 
    ::

      response = client.list_deployments(
          GroupId='string',
          MaxResults='string',
          NextToken='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Deployments': [
                {
                    'CreatedAt': 'string',
                    'DeploymentArn': 'string',
                    'DeploymentId': 'string',
                    'DeploymentType': 'NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
                    'GroupArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The response body contains the list of deployments for the given group Id
        

        - **Deployments** *(list) --* List of deployments for the requested groups
          

          - *(dict) --* Information on the deployment
            

            - **CreatedAt** *(string) --* Timestamp when the deployment was created.
            

            - **DeploymentArn** *(string) --* Arn of the deployment.
            

            - **DeploymentId** *(string) --* Id of the deployment.
            

            - **DeploymentType** *(string) --* The type of deployment.
            

            - **GroupArn** *(string) --* Arn of the group for this deployment.
        
      
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
    

  .. py:method:: list_device_definition_versions(**kwargs)

    Lists the versions of a device definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeviceDefinitionVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_device_definition_versions(
          DeviceDefinitionId='string',
          MaxResults='string',
          NextToken='string'
      )
    :type DeviceDefinitionId: string
    :param DeviceDefinitionId: **[REQUIRED]** device definition Id

    
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'Versions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'Version': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
        

        - **Versions** *(list) --* Versions
          

          - *(dict) --* Information on the version
            

            - **Arn** *(string) --* Arn of the version.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
            

            - **Id** *(string) --* Id of the resource container.
            

            - **Version** *(string) --* Unique Id of a version.
        
      
    

  .. py:method:: list_device_definitions(**kwargs)

    Retrieves a list of device definitions.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeviceDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.list_device_definitions(
          MaxResults='string',
          NextToken='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Definitions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'LastUpdatedTimestamp': 'string',
                    'LatestVersion': 'string',
                    'LatestVersionArn': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Definitions** *(list) --* Definitions
          

          - *(dict) --* Information on the Definition
            

            - **Arn** *(string) --* Arn of the definition.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
            

            - **Id** *(string) --* Id of the definition.
            

            - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
            

            - **LatestVersion** *(string) --* Last version of the definition.
            

            - **LatestVersionArn** *(string) --* Latest version arn of the definition.
            

            - **Name** *(string) --* Name of the definition.
        
      
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
    

  .. py:method:: list_function_definition_versions(**kwargs)

    Lists the versions of a Lambda function definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListFunctionDefinitionVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_function_definition_versions(
          FunctionDefinitionId='string',
          MaxResults='string',
          NextToken='string'
      )
    :type FunctionDefinitionId: string
    :param FunctionDefinitionId: **[REQUIRED]** the unique Id of the lambda definition

    
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'Versions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'Version': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
        

        - **Versions** *(list) --* Versions
          

          - *(dict) --* Information on the version
            

            - **Arn** *(string) --* Arn of the version.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
            

            - **Id** *(string) --* Id of the resource container.
            

            - **Version** *(string) --* Unique Id of a version.
        
      
    

  .. py:method:: list_function_definitions(**kwargs)

    Retrieves a list of Lambda function definitions.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListFunctionDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.list_function_definitions(
          MaxResults='string',
          NextToken='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Definitions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'LastUpdatedTimestamp': 'string',
                    'LatestVersion': 'string',
                    'LatestVersionArn': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The Ids of all the Greengrass Function Definitions in this account.
        

        - **Definitions** *(list) --* Definitions
          

          - *(dict) --* Information on the Definition
            

            - **Arn** *(string) --* Arn of the definition.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
            

            - **Id** *(string) --* Id of the definition.
            

            - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
            

            - **LatestVersion** *(string) --* Last version of the definition.
            

            - **LatestVersionArn** *(string) --* Latest version arn of the definition.
            

            - **Name** *(string) --* Name of the definition.
        
      
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
    

  .. py:method:: list_group_certificate_authorities(**kwargs)

    Retrieves the current CAs for a group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroupCertificateAuthorities>`_    


    **Request Syntax** 
    ::

      response = client.list_group_certificate_authorities(
          GroupId='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GroupCertificateAuthorities': [
                {
                    'GroupCertificateAuthorityArn': 'string',
                    'GroupCertificateAuthorityId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* The response body contains the PKI Configuration
        

        - **GroupCertificateAuthorities** *(list) --* List of certificate authorities associated with the group.
          

          - *(dict) --* Information on group certificate authority properties
            

            - **GroupCertificateAuthorityArn** *(string) --* Arn of the certificate authority for the group.
            

            - **GroupCertificateAuthorityId** *(string) --* Id of the certificate authority for the group.
        
      
    

  .. py:method:: list_group_versions(**kwargs)

    List the versions of a group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroupVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_group_versions(
          GroupId='string',
          MaxResults='string',
          NextToken='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'Versions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'Version': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* the list of versions and metadata for the given group Id
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
        

        - **Versions** *(list) --* Versions
          

          - *(dict) --* Information on the version
            

            - **Arn** *(string) --* Arn of the version.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
            

            - **Id** *(string) --* Id of the resource container.
            

            - **Version** *(string) --* Unique Id of a version.
        
      
    

  .. py:method:: list_groups(**kwargs)

    Retrieves a list of groups.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroups>`_    


    **Request Syntax** 
    ::

      response = client.list_groups(
          MaxResults='string',
          NextToken='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Groups': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'LastUpdatedTimestamp': 'string',
                    'LatestVersion': 'string',
                    'LatestVersionArn': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Groups** *(list) --* Groups
          

          - *(dict) --* Information on the group
            

            - **Arn** *(string) --* Arn of a group.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the group was created.
            

            - **Id** *(string) --* Id of a group.
            

            - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the group.
            

            - **LatestVersion** *(string) --* Last version of the group.
            

            - **LatestVersionArn** *(string) --* Latest version arn of the group.
            

            - **Name** *(string) --* Name of a group.
        
      
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
    

  .. py:method:: list_logger_definition_versions(**kwargs)

    Lists the versions of a logger definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListLoggerDefinitionVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_logger_definition_versions(
          LoggerDefinitionId='string',
          MaxResults='string',
          NextToken='string'
      )
    :type LoggerDefinitionId: string
    :param LoggerDefinitionId: **[REQUIRED]** logger definition Id

    
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'Versions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'Version': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
        

        - **Versions** *(list) --* Versions
          

          - *(dict) --* Information on the version
            

            - **Arn** *(string) --* Arn of the version.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
            

            - **Id** *(string) --* Id of the resource container.
            

            - **Version** *(string) --* Unique Id of a version.
        
      
    

  .. py:method:: list_logger_definitions(**kwargs)

    Retrieves a list of logger definitions.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListLoggerDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.list_logger_definitions(
          MaxResults='string',
          NextToken='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Definitions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'LastUpdatedTimestamp': 'string',
                    'LatestVersion': 'string',
                    'LatestVersionArn': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Definitions** *(list) --* Definitions
          

          - *(dict) --* Information on the Definition
            

            - **Arn** *(string) --* Arn of the definition.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
            

            - **Id** *(string) --* Id of the definition.
            

            - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
            

            - **LatestVersion** *(string) --* Last version of the definition.
            

            - **LatestVersionArn** *(string) --* Latest version arn of the definition.
            

            - **Name** *(string) --* Name of the definition.
        
      
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
    

  .. py:method:: list_resource_definition_versions(**kwargs)

    Lists the versions of a resource definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListResourceDefinitionVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_resource_definition_versions(
          MaxResults='string',
          NextToken='string',
          ResourceDefinitionId='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    :type ResourceDefinitionId: string
    :param ResourceDefinitionId: **[REQUIRED]** Resource definition Id.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'Versions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'Version': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
        

        - **Versions** *(list) --* Versions
          

          - *(dict) --* Information on the version
            

            - **Arn** *(string) --* Arn of the version.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
            

            - **Id** *(string) --* Id of the resource container.
            

            - **Version** *(string) --* Unique Id of a version.
        
      
    

  .. py:method:: list_resource_definitions(**kwargs)

    Retrieves a list of resource definitions.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListResourceDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.list_resource_definitions(
          MaxResults='string',
          NextToken='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Definitions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'LastUpdatedTimestamp': 'string',
                    'LatestVersion': 'string',
                    'LatestVersionArn': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The Ids of all the Greengrass Resource Definitions in this account.
        

        - **Definitions** *(list) --* Definitions
          

          - *(dict) --* Information on the Definition
            

            - **Arn** *(string) --* Arn of the definition.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
            

            - **Id** *(string) --* Id of the definition.
            

            - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
            

            - **LatestVersion** *(string) --* Last version of the definition.
            

            - **LatestVersionArn** *(string) --* Latest version arn of the definition.
            

            - **Name** *(string) --* Name of the definition.
        
      
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
    

  .. py:method:: list_subscription_definition_versions(**kwargs)

    Lists the versions of a subscription definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListSubscriptionDefinitionVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_subscription_definition_versions(
          MaxResults='string',
          NextToken='string',
          SubscriptionDefinitionId='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    :type SubscriptionDefinitionId: string
    :param SubscriptionDefinitionId: **[REQUIRED]** subscription definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'Versions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'Version': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
        

        - **Versions** *(list) --* Versions
          

          - *(dict) --* Information on the version
            

            - **Arn** *(string) --* Arn of the version.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the version was created.
            

            - **Id** *(string) --* Id of the resource container.
            

            - **Version** *(string) --* Unique Id of a version.
        
      
    

  .. py:method:: list_subscription_definitions(**kwargs)

    Retrieves a list of subscription definitions.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListSubscriptionDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.list_subscription_definitions(
          MaxResults='string',
          NextToken='string'
      )
    :type MaxResults: string
    :param MaxResults: Specifies the maximum number of list results to be returned in this page

    
    :type NextToken: string
    :param NextToken: Specifies the pagination token used when iterating through a paginated request

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Definitions': [
                {
                    'Arn': 'string',
                    'CreationTimestamp': 'string',
                    'Id': 'string',
                    'LastUpdatedTimestamp': 'string',
                    'LatestVersion': 'string',
                    'LatestVersionArn': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Definitions** *(list) --* Definitions
          

          - *(dict) --* Information on the Definition
            

            - **Arn** *(string) --* Arn of the definition.
            

            - **CreationTimestamp** *(string) --* Timestamp of when the definition was created.
            

            - **Id** *(string) --* Id of the definition.
            

            - **LastUpdatedTimestamp** *(string) --* Last updated timestamp of the definition.
            

            - **LatestVersion** *(string) --* Last version of the definition.
            

            - **LatestVersionArn** *(string) --* Latest version arn of the definition.
            

            - **Name** *(string) --* Name of the definition.
        
      
        

        - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are no additional results.
    

  .. py:method:: reset_deployments(**kwargs)

    Resets a group's deployments.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ResetDeployments>`_    


    **Request Syntax** 
    ::

      response = client.reset_deployments(
          AmznClientToken='string',
          Force=True|False,
          GroupId='string'
      )
    :type AmznClientToken: string
    :param AmznClientToken: The client token used to request idempotent operations.

    
    :type Force: boolean
    :param Force: When set to true, perform a best-effort only core reset.

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeploymentArn': 'string',
            'DeploymentId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Success. The group's deployments were reset.
        

        - **DeploymentArn** *(string) --* The arn of the reset deployment.
        

        - **DeploymentId** *(string) --* The id of the reset deployment.
    

  .. py:method:: update_connectivity_info(**kwargs)

    Updates the connectivity information for the core. Any devices that belong to the group which has this core will receive this information in order to find the location of the core and connect to it.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateConnectivityInfo>`_    


    **Request Syntax** 
    ::

      response = client.update_connectivity_info(
          ConnectivityInfo=[
              {
                  'HostAddress': 'string',
                  'Id': 'string',
                  'Metadata': 'string',
                  'PortNumber': 123
              },
          ],
          ThingName='string'
      )
    :type ConnectivityInfo: list
    :param ConnectivityInfo: Connectivity info list

    
      - *(dict) --* Connectivity Info

      
        - **HostAddress** *(string) --* Endpoint for the GGC. Can be an IP address or DNS.

        
        - **Id** *(string) --* Element Id for this entry in the list.

        
        - **Metadata** *(string) --* Metadata for this endpoint.

        
        - **PortNumber** *(integer) --* Port of the GGC. Usually 8883.

        
      
  
    :type ThingName: string
    :param ThingName: **[REQUIRED]** Thing Name

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Message': 'string',
            'Version': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Message** *(string) --* Response Text
        

        - **Version** *(string) --* New Version
    

  .. py:method:: update_core_definition(**kwargs)

    Updates a core definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateCoreDefinition>`_    


    **Request Syntax** 
    ::

      response = client.update_core_definition(
          CoreDefinitionId='string',
          Name='string'
      )
    :type CoreDefinitionId: string
    :param CoreDefinitionId: **[REQUIRED]** core definition Id

    
    :type Name: string
    :param Name: name of the definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_device_definition(**kwargs)

    Updates a device definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateDeviceDefinition>`_    


    **Request Syntax** 
    ::

      response = client.update_device_definition(
          DeviceDefinitionId='string',
          Name='string'
      )
    :type DeviceDefinitionId: string
    :param DeviceDefinitionId: **[REQUIRED]** device definition Id

    
    :type Name: string
    :param Name: name of the definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_function_definition(**kwargs)

    Updates a Lambda function definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateFunctionDefinition>`_    


    **Request Syntax** 
    ::

      response = client.update_function_definition(
          FunctionDefinitionId='string',
          Name='string'
      )
    :type FunctionDefinitionId: string
    :param FunctionDefinitionId: **[REQUIRED]** the unique Id of the lambda definition

    
    :type Name: string
    :param Name: name of the definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_group(**kwargs)

    Updates a group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateGroup>`_    


    **Request Syntax** 
    ::

      response = client.update_group(
          GroupId='string',
          Name='string'
      )
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    :type Name: string
    :param Name: name of the definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_group_certificate_configuration(**kwargs)

    Updates the Cert expiry time for a group.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateGroupCertificateConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.update_group_certificate_configuration(
          CertificateExpiryInMilliseconds='string',
          GroupId='string'
      )
    :type CertificateExpiryInMilliseconds: string
    :param CertificateExpiryInMilliseconds: Amount of time when the certificate expires in milliseconds.

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** The unique Id of the AWS Greengrass Group

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CertificateAuthorityExpiryInMilliseconds': 'string',
            'CertificateExpiryInMilliseconds': 'string',
            'GroupId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The response body contains the PKI Configuration
        

        - **CertificateAuthorityExpiryInMilliseconds** *(string) --* Amount of time when the certificate authority expires in milliseconds.
        

        - **CertificateExpiryInMilliseconds** *(string) --* Amount of time when the certificate expires in milliseconds.
        

        - **GroupId** *(string) --* Id of the group the certificate configuration belongs to.
    

  .. py:method:: update_logger_definition(**kwargs)

    Updates a logger definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateLoggerDefinition>`_    


    **Request Syntax** 
    ::

      response = client.update_logger_definition(
          LoggerDefinitionId='string',
          Name='string'
      )
    :type LoggerDefinitionId: string
    :param LoggerDefinitionId: **[REQUIRED]** logger definition Id

    
    :type Name: string
    :param Name: name of the definition

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_resource_definition(**kwargs)

    Updates a resource definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateResourceDefinition>`_    


    **Request Syntax** 
    ::

      response = client.update_resource_definition(
          Name='string',
          ResourceDefinitionId='string'
      )
    :type Name: string
    :param Name: name of the definition

    
    :type ResourceDefinitionId: string
    :param ResourceDefinitionId: **[REQUIRED]** Resource definition Id.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_subscription_definition(**kwargs)

    Updates a subscription definition.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateSubscriptionDefinition>`_    


    **Request Syntax** 
    ::

      response = client.update_subscription_definition(
          Name='string',
          SubscriptionDefinitionId='string'
      )
    :type Name: string
    :param Name: name of the definition

    
    :type SubscriptionDefinitionId: string
    :param SubscriptionDefinitionId: **[REQUIRED]** subscription definition Id

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    