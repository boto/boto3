

**********
WorkSpaces
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: WorkSpaces.Client

  A low-level client representing Amazon WorkSpaces::

    
    import boto3
    
    client = boto3.client('workspaces')

  
  These are the available methods:
  
  *   :py:meth:`~WorkSpaces.Client.can_paginate`

  
  *   :py:meth:`~WorkSpaces.Client.create_tags`

  
  *   :py:meth:`~WorkSpaces.Client.create_workspaces`

  
  *   :py:meth:`~WorkSpaces.Client.delete_tags`

  
  *   :py:meth:`~WorkSpaces.Client.describe_tags`

  
  *   :py:meth:`~WorkSpaces.Client.describe_workspace_bundles`

  
  *   :py:meth:`~WorkSpaces.Client.describe_workspace_directories`

  
  *   :py:meth:`~WorkSpaces.Client.describe_workspaces`

  
  *   :py:meth:`~WorkSpaces.Client.describe_workspaces_connection_status`

  
  *   :py:meth:`~WorkSpaces.Client.generate_presigned_url`

  
  *   :py:meth:`~WorkSpaces.Client.get_paginator`

  
  *   :py:meth:`~WorkSpaces.Client.get_waiter`

  
  *   :py:meth:`~WorkSpaces.Client.modify_workspace_properties`

  
  *   :py:meth:`~WorkSpaces.Client.reboot_workspaces`

  
  *   :py:meth:`~WorkSpaces.Client.rebuild_workspaces`

  
  *   :py:meth:`~WorkSpaces.Client.start_workspaces`

  
  *   :py:meth:`~WorkSpaces.Client.stop_workspaces`

  
  *   :py:meth:`~WorkSpaces.Client.terminate_workspaces`

  

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


  .. py:method:: create_tags(**kwargs)

    

    Creates tags for a WorkSpace.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateTags>`_    


    **Request Syntax** 
    ::

      response = client.create_tags(
          ResourceId='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource ID of the request.

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      The tags of the request.

      

    
      - *(dict) --* 

        Describes the tag of the WorkSpace.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of the tag.

          

        
        - **Value** *(string) --* 

          The value of the tag.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The result of the  CreateTags operation.

        
    

  .. py:method:: create_workspaces(**kwargs)

    

    Creates one or more WorkSpaces.

     

    .. note::

       

      This operation is asynchronous and returns before the WorkSpaces are created.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateWorkspaces>`_    


    **Request Syntax** 
    ::

      response = client.create_workspaces(
          Workspaces=[
              {
                  'DirectoryId': 'string',
                  'UserName': 'string',
                  'BundleId': 'string',
                  'VolumeEncryptionKey': 'string',
                  'UserVolumeEncryptionEnabled': True|False,
                  'RootVolumeEncryptionEnabled': True|False,
                  'WorkspaceProperties': {
                      'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                      'RunningModeAutoStopTimeoutInMinutes': 123
                  },
                  'Tags': [
                      {
                          'Key': 'string',
                          'Value': 'string'
                      },
                  ]
              },
          ]
      )
    :type Workspaces: list
    :param Workspaces: **[REQUIRED]** 

      An array of structures that specify the WorkSpaces to create.

      

    
      - *(dict) --* 

        Contains information about a WorkSpace creation request.

        

      
        - **DirectoryId** *(string) --* **[REQUIRED]** 

          The identifier of the AWS Directory Service directory to create the WorkSpace in. You can use the  DescribeWorkspaceDirectories operation to obtain a list of the directories that are available.

          

        
        - **UserName** *(string) --* **[REQUIRED]** 

          The username that the WorkSpace is assigned to. This username must exist in the AWS Directory Service directory specified by the ``DirectoryId`` member.

          

        
        - **BundleId** *(string) --* **[REQUIRED]** 

          The identifier of the bundle to create the WorkSpace from. You can use the  DescribeWorkspaceBundles operation to obtain a list of the bundles that are available.

          

        
        - **VolumeEncryptionKey** *(string) --* 

          The KMS key used to encrypt data stored on your WorkSpace.

          

        
        - **UserVolumeEncryptionEnabled** *(boolean) --* 

          Specifies whether the data stored on the user volume, or D: drive, is encrypted.

          

        
        - **RootVolumeEncryptionEnabled** *(boolean) --* 

          Specifies whether the data stored on the root volume, or C: drive, is encrypted.

          

        
        - **WorkspaceProperties** *(dict) --* 

          Describes the properties of a WorkSpace.

          

        
          - **RunningMode** *(string) --* 

            The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.

            

          
          - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 

            The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.

            

          
        
        - **Tags** *(list) --* 

          The tags of the WorkSpace request.

          

        
          - *(dict) --* 

            Describes the tag of the WorkSpace.

            

          
            - **Key** *(string) --* **[REQUIRED]** 

              The key of the tag.

              

            
            - **Value** *(string) --* 

              The value of the tag.

              

            
          
      
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedRequests': [
                {
                    'WorkspaceRequest': {
                        'DirectoryId': 'string',
                        'UserName': 'string',
                        'BundleId': 'string',
                        'VolumeEncryptionKey': 'string',
                        'UserVolumeEncryptionEnabled': True|False,
                        'RootVolumeEncryptionEnabled': True|False,
                        'WorkspaceProperties': {
                            'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                            'RunningModeAutoStopTimeoutInMinutes': 123
                        },
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ],
            'PendingRequests': [
                {
                    'WorkspaceId': 'string',
                    'DirectoryId': 'string',
                    'UserName': 'string',
                    'IpAddress': 'string',
                    'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'STOPPING'|'STOPPED'|'ERROR',
                    'BundleId': 'string',
                    'SubnetId': 'string',
                    'ErrorMessage': 'string',
                    'ErrorCode': 'string',
                    'ComputerName': 'string',
                    'VolumeEncryptionKey': 'string',
                    'UserVolumeEncryptionEnabled': True|False,
                    'RootVolumeEncryptionEnabled': True|False,
                    'WorkspaceProperties': {
                        'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                        'RunningModeAutoStopTimeoutInMinutes': 123
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the result of the  CreateWorkspaces operation.

        
        

        - **FailedRequests** *(list) --* 

          An array of structures that represent the WorkSpaces that could not be created.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace that could not be created.

            
            

            - **WorkspaceRequest** *(dict) --* 

              A  FailedCreateWorkspaceRequest$WorkspaceRequest object that contains the information about the WorkSpace that could not be created.

              
              

              - **DirectoryId** *(string) --* 

                The identifier of the AWS Directory Service directory to create the WorkSpace in. You can use the  DescribeWorkspaceDirectories operation to obtain a list of the directories that are available.

                
              

              - **UserName** *(string) --* 

                The username that the WorkSpace is assigned to. This username must exist in the AWS Directory Service directory specified by the ``DirectoryId`` member.

                
              

              - **BundleId** *(string) --* 

                The identifier of the bundle to create the WorkSpace from. You can use the  DescribeWorkspaceBundles operation to obtain a list of the bundles that are available.

                
              

              - **VolumeEncryptionKey** *(string) --* 

                The KMS key used to encrypt data stored on your WorkSpace.

                
              

              - **UserVolumeEncryptionEnabled** *(boolean) --* 

                Specifies whether the data stored on the user volume, or D: drive, is encrypted.

                
              

              - **RootVolumeEncryptionEnabled** *(boolean) --* 

                Specifies whether the data stored on the root volume, or C: drive, is encrypted.

                
              

              - **WorkspaceProperties** *(dict) --* 

                Describes the properties of a WorkSpace.

                
                

                - **RunningMode** *(string) --* 

                  The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.

                  
                

                - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 

                  The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.

                  
            
              

              - **Tags** *(list) --* 

                The tags of the WorkSpace request.

                
                

                - *(dict) --* 

                  Describes the tag of the WorkSpace.

                  
                  

                  - **Key** *(string) --* 

                    The key of the tag.

                    
                  

                  - **Value** *(string) --* 

                    The value of the tag.

                    
              
            
          
            

            - **ErrorCode** *(string) --* 

              The error code.

              
            

            - **ErrorMessage** *(string) --* 

              The textual error message.

              
        
      
        

        - **PendingRequests** *(list) --* 

          An array of structures that represent the WorkSpaces that were created.

           

          Because this operation is asynchronous, the identifier in ``WorkspaceId`` is not immediately available. If you immediately call  DescribeWorkspaces with this identifier, no information will be returned.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace.

            
            

            - **WorkspaceId** *(string) --* 

              The identifier of the WorkSpace.

              
            

            - **DirectoryId** *(string) --* 

              The identifier of the AWS Directory Service directory that the WorkSpace belongs to.

              
            

            - **UserName** *(string) --* 

              The user that the WorkSpace is assigned to.

              
            

            - **IpAddress** *(string) --* 

              The IP address of the WorkSpace.

              
            

            - **State** *(string) --* 

              The operational state of the WorkSpace.

              
            

            - **BundleId** *(string) --* 

              The identifier of the bundle that the WorkSpace was created from.

              
            

            - **SubnetId** *(string) --* 

              The identifier of the subnet that the WorkSpace is in.

              
            

            - **ErrorMessage** *(string) --* 

              If the WorkSpace could not be created, this contains a textual error message that describes the failure.

              
            

            - **ErrorCode** *(string) --* 

              If the WorkSpace could not be created, this contains the error code.

              
            

            - **ComputerName** *(string) --* 

              The name of the WorkSpace as seen by the operating system.

              
            

            - **VolumeEncryptionKey** *(string) --* 

              The KMS key used to encrypt data stored on your WorkSpace.

              
            

            - **UserVolumeEncryptionEnabled** *(boolean) --* 

              Specifies whether the data stored on the user volume, or D: drive, is encrypted.

              
            

            - **RootVolumeEncryptionEnabled** *(boolean) --* 

              Specifies whether the data stored on the root volume, or C: drive, is encrypted.

              
            

            - **WorkspaceProperties** *(dict) --* 

              Describes the properties of a WorkSpace.

              
              

              - **RunningMode** *(string) --* 

                The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.

                
              

              - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 

                The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.

                
          
        
      
    

  .. py:method:: delete_tags(**kwargs)

    

    Deletes tags from a WorkSpace.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DeleteTags>`_    


    **Request Syntax** 
    ::

      response = client.delete_tags(
          ResourceId='string',
          TagKeys=[
              'string',
          ]
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource ID of the request.

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      The tag keys of the request.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The result of the  DeleteTags operation.

        
    

  .. py:method:: describe_tags(**kwargs)

    

    Describes tags for a WorkSpace.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeTags>`_    


    **Request Syntax** 
    ::

      response = client.describe_tags(
          ResourceId='string'
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource ID of the request.

      

    
    
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

        The result of the  DescribeTags operation.

        
        

        - **TagList** *(list) --* 

          The list of tags.

          
          

          - *(dict) --* 

            Describes the tag of the WorkSpace.

            
            

            - **Key** *(string) --* 

              The key of the tag.

              
            

            - **Value** *(string) --* 

              The value of the tag.

              
        
      
    

  .. py:method:: describe_workspace_bundles(**kwargs)

    

    Obtains information about the WorkSpace bundles that are available to your account in the specified region.

     

    You can filter the results with either the ``BundleIds`` parameter, or the ``Owner`` parameter, but not both.

     

    This operation supports pagination with the use of the ``NextToken`` request and response parameters. If more results are available, the ``NextToken`` response member contains a token that you pass in the next call to this operation to retrieve the next set of items.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceBundles>`_    


    **Request Syntax** 
    ::

      response = client.describe_workspace_bundles(
          BundleIds=[
              'string',
          ],
          Owner='string',
          NextToken='string'
      )
    :type BundleIds: list
    :param BundleIds: 

      An array of strings that contains the identifiers of the bundles to retrieve. This parameter cannot be combined with any other filter parameter.

      

    
      - *(string) --* 

      
  
    :type Owner: string
    :param Owner: 

      The owner of the bundles to retrieve. This parameter cannot be combined with any other filter parameter.

       

      This contains one of the following values:

       

       
      * null- Retrieves the bundles that belong to the account making the call. 
       
      * ``AMAZON`` - Retrieves the bundles that are provided by AWS. 
       

      

    
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` value from a previous call to this operation. Pass null if this is the first call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Bundles': [
                {
                    'BundleId': 'string',
                    'Name': 'string',
                    'Owner': 'string',
                    'Description': 'string',
                    'UserStorage': {
                        'Capacity': 'string'
                    },
                    'ComputeType': {
                        'Name': 'VALUE'|'STANDARD'|'PERFORMANCE'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results of the  DescribeWorkspaceBundles operation.

        
        

        - **Bundles** *(list) --* 

          An array of structures that contain information about the bundles.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace bundle.

            
            

            - **BundleId** *(string) --* 

              The bundle identifier.

              
            

            - **Name** *(string) --* 

              The name of the bundle.

              
            

            - **Owner** *(string) --* 

              The owner of the bundle. This contains the owner's account identifier, or ``AMAZON`` if the bundle is provided by AWS.

              
            

            - **Description** *(string) --* 

              The bundle description.

              
            

            - **UserStorage** *(dict) --* 

              A  UserStorage object that specifies the amount of user storage that the bundle contains.

              
              

              - **Capacity** *(string) --* 

                The amount of user storage for the bundle.

                
          
            

            - **ComputeType** *(dict) --* 

              A  ComputeType object that specifies the compute type for the bundle.

              
              

              - **Name** *(string) --* 

                The name of the compute type for the bundle.

                
          
        
      
        

        - **NextToken** *(string) --* 

          If not null, more results are available. Pass this value for the ``NextToken`` parameter in a subsequent call to this operation to retrieve the next set of items. This token is valid for one day and must be used within that time frame.

          
    

  .. py:method:: describe_workspace_directories(**kwargs)

    

    Retrieves information about the AWS Directory Service directories in the region that are registered with Amazon WorkSpaces and are available to your account.

     

    This operation supports pagination with the use of the ``NextToken`` request and response parameters. If more results are available, the ``NextToken`` response member contains a token that you pass in the next call to this operation to retrieve the next set of items.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceDirectories>`_    


    **Request Syntax** 
    ::

      response = client.describe_workspace_directories(
          DirectoryIds=[
              'string',
          ],
          NextToken='string'
      )
    :type DirectoryIds: list
    :param DirectoryIds: 

      An array of strings that contains the directory identifiers to retrieve information for. If this member is null, all directories are retrieved.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` value from a previous call to this operation. Pass null if this is the first call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Directories': [
                {
                    'DirectoryId': 'string',
                    'Alias': 'string',
                    'DirectoryName': 'string',
                    'RegistrationCode': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'DnsIpAddresses': [
                        'string',
                    ],
                    'CustomerUserName': 'string',
                    'IamRoleId': 'string',
                    'DirectoryType': 'SIMPLE_AD'|'AD_CONNECTOR',
                    'WorkspaceSecurityGroupId': 'string',
                    'State': 'REGISTERING'|'REGISTERED'|'DEREGISTERING'|'DEREGISTERED'|'ERROR',
                    'WorkspaceCreationProperties': {
                        'EnableWorkDocs': True|False,
                        'EnableInternetAccess': True|False,
                        'DefaultOu': 'string',
                        'CustomSecurityGroupId': 'string',
                        'UserEnabledAsLocalAdministrator': True|False
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results of the  DescribeWorkspaceDirectories operation.

        
        

        - **Directories** *(list) --* 

          An array of structures that contain information about the directories.

          
          

          - *(dict) --* 

            Contains information about an AWS Directory Service directory for use with Amazon WorkSpaces.

            
            

            - **DirectoryId** *(string) --* 

              The directory identifier.

              
            

            - **Alias** *(string) --* 

              The directory alias.

              
            

            - **DirectoryName** *(string) --* 

              The name of the directory.

              
            

            - **RegistrationCode** *(string) --* 

              The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.

              
            

            - **SubnetIds** *(list) --* 

              An array of strings that contains the identifiers of the subnets used with the directory.

              
              

              - *(string) --* 
          
            

            - **DnsIpAddresses** *(list) --* 

              An array of strings that contains the IP addresses of the DNS servers for the directory.

              
              

              - *(string) --* 
          
            

            - **CustomerUserName** *(string) --* 

              The user name for the service account.

              
            

            - **IamRoleId** *(string) --* 

              The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.

              
            

            - **DirectoryType** *(string) --* 

              The directory type.

              
            

            - **WorkspaceSecurityGroupId** *(string) --* 

              The identifier of the security group that is assigned to new WorkSpaces.

              
            

            - **State** *(string) --* 

              The state of the directory's registration with Amazon WorkSpaces

              
            

            - **WorkspaceCreationProperties** *(dict) --* 

              A structure that specifies the default creation properties for all WorkSpaces in the directory.

              
              

              - **EnableWorkDocs** *(boolean) --* 

                Specifies if the directory is enabled for Amazon WorkDocs.

                
              

              - **EnableInternetAccess** *(boolean) --* 

                A public IP address will be attached to all WorkSpaces that are created or rebuilt.

                
              

              - **DefaultOu** *(string) --* 

                The organizational unit (OU) in the directory that the WorkSpace machine accounts are placed in.

                
              

              - **CustomSecurityGroupId** *(string) --* 

                The identifier of any custom security groups that are applied to the WorkSpaces when they are created.

                
              

              - **UserEnabledAsLocalAdministrator** *(boolean) --* 

                The WorkSpace user is an administrator on the WorkSpace.

                
          
        
      
        

        - **NextToken** *(string) --* 

          If not null, more results are available. Pass this value for the ``NextToken`` parameter in a subsequent call to this operation to retrieve the next set of items. This token is valid for one day and must be used within that time frame.

          
    

  .. py:method:: describe_workspaces(**kwargs)

    

    Obtains information about the specified WorkSpaces.

     

    Only one of the filter parameters, such as ``BundleId`` , ``DirectoryId`` , or ``WorkspaceIds`` , can be specified at a time.

     

    This operation supports pagination with the use of the ``NextToken`` request and response parameters. If more results are available, the ``NextToken`` response member contains a token that you pass in the next call to this operation to retrieve the next set of items.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaces>`_    


    **Request Syntax** 
    ::

      response = client.describe_workspaces(
          WorkspaceIds=[
              'string',
          ],
          DirectoryId='string',
          UserName='string',
          BundleId='string',
          Limit=123,
          NextToken='string'
      )
    :type WorkspaceIds: list
    :param WorkspaceIds: 

      An array of strings that contain the identifiers of the WorkSpaces for which to retrieve information. This parameter cannot be combined with any other filter parameter.

       

      Because the  CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call  DescribeWorkspaces with this identifier, no information is returned.

      

    
      - *(string) --* 

      
  
    :type DirectoryId: string
    :param DirectoryId: 

      Specifies the directory identifier to which to limit the WorkSpaces. Optionally, you can specify a specific directory user with the ``UserName`` parameter. This parameter cannot be combined with any other filter parameter.

      

    
    :type UserName: string
    :param UserName: 

      Used with the ``DirectoryId`` parameter to specify the directory user for whom to obtain the WorkSpace.

      

    
    :type BundleId: string
    :param BundleId: 

      The identifier of a bundle to obtain the WorkSpaces for. All WorkSpaces that are created from this bundle will be retrieved. This parameter cannot be combined with any other filter parameter.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of items to return.

      

    
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` value from a previous call to this operation. Pass null if this is the first call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Workspaces': [
                {
                    'WorkspaceId': 'string',
                    'DirectoryId': 'string',
                    'UserName': 'string',
                    'IpAddress': 'string',
                    'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'STOPPING'|'STOPPED'|'ERROR',
                    'BundleId': 'string',
                    'SubnetId': 'string',
                    'ErrorMessage': 'string',
                    'ErrorCode': 'string',
                    'ComputerName': 'string',
                    'VolumeEncryptionKey': 'string',
                    'UserVolumeEncryptionEnabled': True|False,
                    'RootVolumeEncryptionEnabled': True|False,
                    'WorkspaceProperties': {
                        'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                        'RunningModeAutoStopTimeoutInMinutes': 123
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results for the  DescribeWorkspaces operation.

        
        

        - **Workspaces** *(list) --* 

          An array of structures that contain the information about the WorkSpaces.

           

          Because the  CreateWorkspaces operation is asynchronous, some of this information may be incomplete for a newly-created WorkSpace.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace.

            
            

            - **WorkspaceId** *(string) --* 

              The identifier of the WorkSpace.

              
            

            - **DirectoryId** *(string) --* 

              The identifier of the AWS Directory Service directory that the WorkSpace belongs to.

              
            

            - **UserName** *(string) --* 

              The user that the WorkSpace is assigned to.

              
            

            - **IpAddress** *(string) --* 

              The IP address of the WorkSpace.

              
            

            - **State** *(string) --* 

              The operational state of the WorkSpace.

              
            

            - **BundleId** *(string) --* 

              The identifier of the bundle that the WorkSpace was created from.

              
            

            - **SubnetId** *(string) --* 

              The identifier of the subnet that the WorkSpace is in.

              
            

            - **ErrorMessage** *(string) --* 

              If the WorkSpace could not be created, this contains a textual error message that describes the failure.

              
            

            - **ErrorCode** *(string) --* 

              If the WorkSpace could not be created, this contains the error code.

              
            

            - **ComputerName** *(string) --* 

              The name of the WorkSpace as seen by the operating system.

              
            

            - **VolumeEncryptionKey** *(string) --* 

              The KMS key used to encrypt data stored on your WorkSpace.

              
            

            - **UserVolumeEncryptionEnabled** *(boolean) --* 

              Specifies whether the data stored on the user volume, or D: drive, is encrypted.

              
            

            - **RootVolumeEncryptionEnabled** *(boolean) --* 

              Specifies whether the data stored on the root volume, or C: drive, is encrypted.

              
            

            - **WorkspaceProperties** *(dict) --* 

              Describes the properties of a WorkSpace.

              
              

              - **RunningMode** *(string) --* 

                The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.

                
              

              - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 

                The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.

                
          
        
      
        

        - **NextToken** *(string) --* 

          If not null, more results are available. Pass this value for the ``NextToken`` parameter in a subsequent call to this operation to retrieve the next set of items. This token is valid for one day and must be used within that time frame.

          
    

  .. py:method:: describe_workspaces_connection_status(**kwargs)

    

    Describes the connection status of a specified WorkSpace.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus>`_    


    **Request Syntax** 
    ::

      response = client.describe_workspaces_connection_status(
          WorkspaceIds=[
              'string',
          ],
          NextToken='string'
      )
    :type WorkspaceIds: list
    :param WorkspaceIds: 

      An array of strings that contain the identifiers of the WorkSpaces.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The next token of the request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WorkspacesConnectionStatus': [
                {
                    'WorkspaceId': 'string',
                    'ConnectionState': 'CONNECTED'|'DISCONNECTED'|'UNKNOWN',
                    'ConnectionStateCheckTimestamp': datetime(2015, 1, 1),
                    'LastKnownUserConnectionTimestamp': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WorkspacesConnectionStatus** *(list) --* 

          The connection status of the WorkSpace.

          
          

          - *(dict) --* 

            Describes the connection status of a WorkSpace.

            
            

            - **WorkspaceId** *(string) --* 

              The ID of the WorkSpace.

              
            

            - **ConnectionState** *(string) --* 

              The connection state of the WorkSpace. Returns UNKOWN if the WorkSpace is in a Stopped state.

              
            

            - **ConnectionStateCheckTimestamp** *(datetime) --* 

              The timestamp of the connection state check.

              
            

            - **LastKnownUserConnectionTimestamp** *(datetime) --* 

              The timestamp of the last known user connection.

              
        
      
        

        - **NextToken** *(string) --* 

          The next token of the result.

          
    

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

        


  .. py:method:: modify_workspace_properties(**kwargs)

    

    Modifies the WorkSpace properties, including the running mode and AutoStop time.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ModifyWorkspaceProperties>`_    


    **Request Syntax** 
    ::

      response = client.modify_workspace_properties(
          WorkspaceId='string',
          WorkspaceProperties={
              'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
              'RunningModeAutoStopTimeoutInMinutes': 123
          }
      )
    :type WorkspaceId: string
    :param WorkspaceId: **[REQUIRED]** 

      The ID of the WorkSpace.

      

    
    :type WorkspaceProperties: dict
    :param WorkspaceProperties: **[REQUIRED]** 

      The WorkSpace properties of the request.

      

    
      - **RunningMode** *(string) --* 

        The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.

        

      
      - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 

        The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: reboot_workspaces(**kwargs)

    

    Reboots the specified WorkSpaces.

     

    To be able to reboot a WorkSpace, the WorkSpace must have a **State** of ``AVAILABLE`` , ``IMPAIRED`` , or ``INOPERABLE`` .

     

    .. note::

       

      This operation is asynchronous and returns before the WorkSpaces have rebooted.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/RebootWorkspaces>`_    


    **Request Syntax** 
    ::

      response = client.reboot_workspaces(
          RebootWorkspaceRequests=[
              {
                  'WorkspaceId': 'string'
              },
          ]
      )
    :type RebootWorkspaceRequests: list
    :param RebootWorkspaceRequests: **[REQUIRED]** 

      An array of structures that specify the WorkSpaces to reboot.

      

    
      - *(dict) --* 

        Contains information used with the  RebootWorkspaces operation to reboot a WorkSpace.

        

      
        - **WorkspaceId** *(string) --* **[REQUIRED]** 

          The identifier of the WorkSpace to reboot.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedRequests': [
                {
                    'WorkspaceId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results of the  RebootWorkspaces operation.

        
        

        - **FailedRequests** *(list) --* 

          An array of structures representing any WorkSpaces that could not be rebooted.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

            
            

            - **WorkspaceId** *(string) --* 

              The identifier of the WorkSpace.

              
            

            - **ErrorCode** *(string) --* 

              The error code.

              
            

            - **ErrorMessage** *(string) --* 

              The textual error message.

              
        
      
    

  .. py:method:: rebuild_workspaces(**kwargs)

    

    Rebuilds the specified WorkSpaces.

     

    Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. Rebuilding a WorkSpace causes the following to occur:

     

     
    * The system is restored to the image of the bundle that the WorkSpace is created from. Any applications that have been installed, or system settings that have been made since the WorkSpace was created will be lost. 
     
    * The data drive (D drive) is re-created from the last automatic snapshot taken of the data drive. The current contents of the data drive are overwritten. Automatic snapshots of the data drive are taken every 12 hours, so the snapshot can be as much as 12 hours old. 
     

     

    To be able to rebuild a WorkSpace, the WorkSpace must have a **State** of ``AVAILABLE`` or ``ERROR`` .

     

    .. note::

       

      This operation is asynchronous and returns before the WorkSpaces have been completely rebuilt.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/RebuildWorkspaces>`_    


    **Request Syntax** 
    ::

      response = client.rebuild_workspaces(
          RebuildWorkspaceRequests=[
              {
                  'WorkspaceId': 'string'
              },
          ]
      )
    :type RebuildWorkspaceRequests: list
    :param RebuildWorkspaceRequests: **[REQUIRED]** 

      An array of structures that specify the WorkSpaces to rebuild.

      

    
      - *(dict) --* 

        Contains information used with the  RebuildWorkspaces operation to rebuild a WorkSpace.

        

      
        - **WorkspaceId** *(string) --* **[REQUIRED]** 

          The identifier of the WorkSpace to rebuild.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedRequests': [
                {
                    'WorkspaceId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results of the  RebuildWorkspaces operation.

        
        

        - **FailedRequests** *(list) --* 

          An array of structures representing any WorkSpaces that could not be rebuilt.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

            
            

            - **WorkspaceId** *(string) --* 

              The identifier of the WorkSpace.

              
            

            - **ErrorCode** *(string) --* 

              The error code.

              
            

            - **ErrorMessage** *(string) --* 

              The textual error message.

              
        
      
    

  .. py:method:: start_workspaces(**kwargs)

    

    Starts the specified WorkSpaces. The WorkSpaces must have a running mode of AutoStop and a state of STOPPED.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/StartWorkspaces>`_    


    **Request Syntax** 
    ::

      response = client.start_workspaces(
          StartWorkspaceRequests=[
              {
                  'WorkspaceId': 'string'
              },
          ]
      )
    :type StartWorkspaceRequests: list
    :param StartWorkspaceRequests: **[REQUIRED]** 

      The requests.

      

    
      - *(dict) --* 

        Describes the start request.

        

      
        - **WorkspaceId** *(string) --* 

          The ID of the WorkSpace.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedRequests': [
                {
                    'WorkspaceId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FailedRequests** *(list) --* 

          The failed requests.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

            
            

            - **WorkspaceId** *(string) --* 

              The identifier of the WorkSpace.

              
            

            - **ErrorCode** *(string) --* 

              The error code.

              
            

            - **ErrorMessage** *(string) --* 

              The textual error message.

              
        
      
    

  .. py:method:: stop_workspaces(**kwargs)

    

    Stops the specified WorkSpaces. The WorkSpaces must have a running mode of AutoStop and a state of AVAILABLE, IMPAIRED, UNHEALTHY, or ERROR.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/StopWorkspaces>`_    


    **Request Syntax** 
    ::

      response = client.stop_workspaces(
          StopWorkspaceRequests=[
              {
                  'WorkspaceId': 'string'
              },
          ]
      )
    :type StopWorkspaceRequests: list
    :param StopWorkspaceRequests: **[REQUIRED]** 

      The requests.

      

    
      - *(dict) --* 

        Describes the stop request.

        

      
        - **WorkspaceId** *(string) --* 

          The ID of the WorkSpace.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedRequests': [
                {
                    'WorkspaceId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FailedRequests** *(list) --* 

          The failed requests.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

            
            

            - **WorkspaceId** *(string) --* 

              The identifier of the WorkSpace.

              
            

            - **ErrorCode** *(string) --* 

              The error code.

              
            

            - **ErrorMessage** *(string) --* 

              The textual error message.

              
        
      
    

  .. py:method:: terminate_workspaces(**kwargs)

    

    Terminates the specified WorkSpaces.

     

    Terminating a WorkSpace is a permanent action and cannot be undone. The user's data is not maintained and will be destroyed. If you need to archive any user data, contact Amazon Web Services before terminating the WorkSpace.

     

    You can terminate a WorkSpace that is in any state except ``SUSPENDED`` .

     

    .. note::

       

      This operation is asynchronous and returns before the WorkSpaces have been completely terminated.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/TerminateWorkspaces>`_    


    **Request Syntax** 
    ::

      response = client.terminate_workspaces(
          TerminateWorkspaceRequests=[
              {
                  'WorkspaceId': 'string'
              },
          ]
      )
    :type TerminateWorkspaceRequests: list
    :param TerminateWorkspaceRequests: **[REQUIRED]** 

      An array of structures that specify the WorkSpaces to terminate.

      

    
      - *(dict) --* 

        Contains information used with the  TerminateWorkspaces operation to terminate a WorkSpace.

        

      
        - **WorkspaceId** *(string) --* **[REQUIRED]** 

          The identifier of the WorkSpace to terminate.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedRequests': [
                {
                    'WorkspaceId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results of the  TerminateWorkspaces operation.

        
        

        - **FailedRequests** *(list) --* 

          An array of structures representing any WorkSpaces that could not be terminated.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

            
            

            - **WorkspaceId** *(string) --* 

              The identifier of the WorkSpace.

              
            

            - **ErrorCode** *(string) --* 

              The error code.

              
            

            - **ErrorMessage** *(string) --* 

              The textual error message.

              
        
      
    

==========
Paginators
==========


The available paginators are:

* :py:class:`WorkSpaces.Paginator.DescribeWorkspaceBundles`


* :py:class:`WorkSpaces.Paginator.DescribeWorkspaceDirectories`


* :py:class:`WorkSpaces.Paginator.DescribeWorkspaces`



.. py:class:: WorkSpaces.Paginator.DescribeWorkspaceBundles

  ::

    
    paginator = client.get_paginator('describe_workspace_bundles')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`WorkSpaces.Client.describe_workspace_bundles`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceBundles>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          BundleIds=[
              'string',
          ],
          Owner='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type BundleIds: list
    :param BundleIds: 

      An array of strings that contains the identifiers of the bundles to retrieve. This parameter cannot be combined with any other filter parameter.

      

    
      - *(string) --* 

      
  
    :type Owner: string
    :param Owner: 

      The owner of the bundles to retrieve. This parameter cannot be combined with any other filter parameter.

       

      This contains one of the following values:

       

       
      * null- Retrieves the bundles that belong to the account making the call. 
       
      * ``AMAZON`` - Retrieves the bundles that are provided by AWS. 
       

      

    
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
            'Bundles': [
                {
                    'BundleId': 'string',
                    'Name': 'string',
                    'Owner': 'string',
                    'Description': 'string',
                    'UserStorage': {
                        'Capacity': 'string'
                    },
                    'ComputeType': {
                        'Name': 'VALUE'|'STANDARD'|'PERFORMANCE'
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results of the  DescribeWorkspaceBundles operation.

        
        

        - **Bundles** *(list) --* 

          An array of structures that contain information about the bundles.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace bundle.

            
            

            - **BundleId** *(string) --* 

              The bundle identifier.

              
            

            - **Name** *(string) --* 

              The name of the bundle.

              
            

            - **Owner** *(string) --* 

              The owner of the bundle. This contains the owner's account identifier, or ``AMAZON`` if the bundle is provided by AWS.

              
            

            - **Description** *(string) --* 

              The bundle description.

              
            

            - **UserStorage** *(dict) --* 

              A  UserStorage object that specifies the amount of user storage that the bundle contains.

              
              

              - **Capacity** *(string) --* 

                The amount of user storage for the bundle.

                
          
            

            - **ComputeType** *(dict) --* 

              A  ComputeType object that specifies the compute type for the bundle.

              
              

              - **Name** *(string) --* 

                The name of the compute type for the bundle.

                
          
        
      
    

.. py:class:: WorkSpaces.Paginator.DescribeWorkspaceDirectories

  ::

    
    paginator = client.get_paginator('describe_workspace_directories')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`WorkSpaces.Client.describe_workspace_directories`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceDirectories>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          DirectoryIds=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type DirectoryIds: list
    :param DirectoryIds: 

      An array of strings that contains the directory identifiers to retrieve information for. If this member is null, all directories are retrieved.

      

    
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
            'Directories': [
                {
                    'DirectoryId': 'string',
                    'Alias': 'string',
                    'DirectoryName': 'string',
                    'RegistrationCode': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'DnsIpAddresses': [
                        'string',
                    ],
                    'CustomerUserName': 'string',
                    'IamRoleId': 'string',
                    'DirectoryType': 'SIMPLE_AD'|'AD_CONNECTOR',
                    'WorkspaceSecurityGroupId': 'string',
                    'State': 'REGISTERING'|'REGISTERED'|'DEREGISTERING'|'DEREGISTERED'|'ERROR',
                    'WorkspaceCreationProperties': {
                        'EnableWorkDocs': True|False,
                        'EnableInternetAccess': True|False,
                        'DefaultOu': 'string',
                        'CustomSecurityGroupId': 'string',
                        'UserEnabledAsLocalAdministrator': True|False
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results of the  DescribeWorkspaceDirectories operation.

        
        

        - **Directories** *(list) --* 

          An array of structures that contain information about the directories.

          
          

          - *(dict) --* 

            Contains information about an AWS Directory Service directory for use with Amazon WorkSpaces.

            
            

            - **DirectoryId** *(string) --* 

              The directory identifier.

              
            

            - **Alias** *(string) --* 

              The directory alias.

              
            

            - **DirectoryName** *(string) --* 

              The name of the directory.

              
            

            - **RegistrationCode** *(string) --* 

              The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.

              
            

            - **SubnetIds** *(list) --* 

              An array of strings that contains the identifiers of the subnets used with the directory.

              
              

              - *(string) --* 
          
            

            - **DnsIpAddresses** *(list) --* 

              An array of strings that contains the IP addresses of the DNS servers for the directory.

              
              

              - *(string) --* 
          
            

            - **CustomerUserName** *(string) --* 

              The user name for the service account.

              
            

            - **IamRoleId** *(string) --* 

              The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.

              
            

            - **DirectoryType** *(string) --* 

              The directory type.

              
            

            - **WorkspaceSecurityGroupId** *(string) --* 

              The identifier of the security group that is assigned to new WorkSpaces.

              
            

            - **State** *(string) --* 

              The state of the directory's registration with Amazon WorkSpaces

              
            

            - **WorkspaceCreationProperties** *(dict) --* 

              A structure that specifies the default creation properties for all WorkSpaces in the directory.

              
              

              - **EnableWorkDocs** *(boolean) --* 

                Specifies if the directory is enabled for Amazon WorkDocs.

                
              

              - **EnableInternetAccess** *(boolean) --* 

                A public IP address will be attached to all WorkSpaces that are created or rebuilt.

                
              

              - **DefaultOu** *(string) --* 

                The organizational unit (OU) in the directory that the WorkSpace machine accounts are placed in.

                
              

              - **CustomSecurityGroupId** *(string) --* 

                The identifier of any custom security groups that are applied to the WorkSpaces when they are created.

                
              

              - **UserEnabledAsLocalAdministrator** *(boolean) --* 

                The WorkSpace user is an administrator on the WorkSpace.

                
          
        
      
    

.. py:class:: WorkSpaces.Paginator.DescribeWorkspaces

  ::

    
    paginator = client.get_paginator('describe_workspaces')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`WorkSpaces.Client.describe_workspaces`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaces>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          WorkspaceIds=[
              'string',
          ],
          DirectoryId='string',
          UserName='string',
          BundleId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type WorkspaceIds: list
    :param WorkspaceIds: 

      An array of strings that contain the identifiers of the WorkSpaces for which to retrieve information. This parameter cannot be combined with any other filter parameter.

       

      Because the  CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call  DescribeWorkspaces with this identifier, no information is returned.

      

    
      - *(string) --* 

      
  
    :type DirectoryId: string
    :param DirectoryId: 

      Specifies the directory identifier to which to limit the WorkSpaces. Optionally, you can specify a specific directory user with the ``UserName`` parameter. This parameter cannot be combined with any other filter parameter.

      

    
    :type UserName: string
    :param UserName: 

      Used with the ``DirectoryId`` parameter to specify the directory user for whom to obtain the WorkSpace.

      

    
    :type BundleId: string
    :param BundleId: 

      The identifier of a bundle to obtain the WorkSpaces for. All WorkSpaces that are created from this bundle will be retrieved. This parameter cannot be combined with any other filter parameter.

      

    
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
            'Workspaces': [
                {
                    'WorkspaceId': 'string',
                    'DirectoryId': 'string',
                    'UserName': 'string',
                    'IpAddress': 'string',
                    'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'STOPPING'|'STOPPED'|'ERROR',
                    'BundleId': 'string',
                    'SubnetId': 'string',
                    'ErrorMessage': 'string',
                    'ErrorCode': 'string',
                    'ComputerName': 'string',
                    'VolumeEncryptionKey': 'string',
                    'UserVolumeEncryptionEnabled': True|False,
                    'RootVolumeEncryptionEnabled': True|False,
                    'WorkspaceProperties': {
                        'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                        'RunningModeAutoStopTimeoutInMinutes': 123
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the results for the  DescribeWorkspaces operation.

        
        

        - **Workspaces** *(list) --* 

          An array of structures that contain the information about the WorkSpaces.

           

          Because the  CreateWorkspaces operation is asynchronous, some of this information may be incomplete for a newly-created WorkSpace.

          
          

          - *(dict) --* 

            Contains information about a WorkSpace.

            
            

            - **WorkspaceId** *(string) --* 

              The identifier of the WorkSpace.

              
            

            - **DirectoryId** *(string) --* 

              The identifier of the AWS Directory Service directory that the WorkSpace belongs to.

              
            

            - **UserName** *(string) --* 

              The user that the WorkSpace is assigned to.

              
            

            - **IpAddress** *(string) --* 

              The IP address of the WorkSpace.

              
            

            - **State** *(string) --* 

              The operational state of the WorkSpace.

              
            

            - **BundleId** *(string) --* 

              The identifier of the bundle that the WorkSpace was created from.

              
            

            - **SubnetId** *(string) --* 

              The identifier of the subnet that the WorkSpace is in.

              
            

            - **ErrorMessage** *(string) --* 

              If the WorkSpace could not be created, this contains a textual error message that describes the failure.

              
            

            - **ErrorCode** *(string) --* 

              If the WorkSpace could not be created, this contains the error code.

              
            

            - **ComputerName** *(string) --* 

              The name of the WorkSpace as seen by the operating system.

              
            

            - **VolumeEncryptionKey** *(string) --* 

              The KMS key used to encrypt data stored on your WorkSpace.

              
            

            - **UserVolumeEncryptionEnabled** *(boolean) --* 

              Specifies whether the data stored on the user volume, or D: drive, is encrypted.

              
            

            - **RootVolumeEncryptionEnabled** *(boolean) --* 

              Specifies whether the data stored on the root volume, or C: drive, is encrypted.

              
            

            - **WorkspaceProperties** *(dict) --* 

              Describes the properties of a WorkSpace.

              
              

              - **RunningMode** *(string) --* 

                The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.

                
              

              - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 

                The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.

                
          
        
      
    