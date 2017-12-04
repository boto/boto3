

*********
AppStream
*********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: AppStream.Client

  A low-level client representing Amazon AppStream::

    
    import boto3
    
    client = boto3.client('appstream')

  
  These are the available methods:
  
  *   :py:meth:`~AppStream.Client.associate_fleet`

  
  *   :py:meth:`~AppStream.Client.can_paginate`

  
  *   :py:meth:`~AppStream.Client.create_directory_config`

  
  *   :py:meth:`~AppStream.Client.create_fleet`

  
  *   :py:meth:`~AppStream.Client.create_image_builder`

  
  *   :py:meth:`~AppStream.Client.create_image_builder_streaming_url`

  
  *   :py:meth:`~AppStream.Client.create_stack`

  
  *   :py:meth:`~AppStream.Client.create_streaming_url`

  
  *   :py:meth:`~AppStream.Client.delete_directory_config`

  
  *   :py:meth:`~AppStream.Client.delete_fleet`

  
  *   :py:meth:`~AppStream.Client.delete_image`

  
  *   :py:meth:`~AppStream.Client.delete_image_builder`

  
  *   :py:meth:`~AppStream.Client.delete_stack`

  
  *   :py:meth:`~AppStream.Client.describe_directory_configs`

  
  *   :py:meth:`~AppStream.Client.describe_fleets`

  
  *   :py:meth:`~AppStream.Client.describe_image_builders`

  
  *   :py:meth:`~AppStream.Client.describe_images`

  
  *   :py:meth:`~AppStream.Client.describe_sessions`

  
  *   :py:meth:`~AppStream.Client.describe_stacks`

  
  *   :py:meth:`~AppStream.Client.disassociate_fleet`

  
  *   :py:meth:`~AppStream.Client.expire_session`

  
  *   :py:meth:`~AppStream.Client.generate_presigned_url`

  
  *   :py:meth:`~AppStream.Client.get_paginator`

  
  *   :py:meth:`~AppStream.Client.get_waiter`

  
  *   :py:meth:`~AppStream.Client.list_associated_fleets`

  
  *   :py:meth:`~AppStream.Client.list_associated_stacks`

  
  *   :py:meth:`~AppStream.Client.start_fleet`

  
  *   :py:meth:`~AppStream.Client.start_image_builder`

  
  *   :py:meth:`~AppStream.Client.stop_fleet`

  
  *   :py:meth:`~AppStream.Client.stop_image_builder`

  
  *   :py:meth:`~AppStream.Client.update_directory_config`

  
  *   :py:meth:`~AppStream.Client.update_fleet`

  
  *   :py:meth:`~AppStream.Client.update_stack`

  

  .. py:method:: associate_fleet(**kwargs)

    

    Associates the specified fleet with the specified stack.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/AssociateFleet>`_    


    **Request Syntax** 
    ::

      response = client.associate_fleet(
          FleetName='string',
          StackName='string'
      )
    :type FleetName: string
    :param FleetName: **[REQUIRED]** 

      The name of the fleet.

      

    
    :type StackName: string
    :param StackName: **[REQUIRED]** 

      The name of the stack.

      

    
    
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


  .. py:method:: create_directory_config(**kwargs)

    

    Creates a directory configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateDirectoryConfig>`_    


    **Request Syntax** 
    ::

      response = client.create_directory_config(
          DirectoryName='string',
          OrganizationalUnitDistinguishedNames=[
              'string',
          ],
          ServiceAccountCredentials={
              'AccountName': 'string',
              'AccountPassword': 'string'
          }
      )
    :type DirectoryName: string
    :param DirectoryName: **[REQUIRED]** 

      The fully qualified name of the directory (for example, corp.example.com).

      

    
    :type OrganizationalUnitDistinguishedNames: list
    :param OrganizationalUnitDistinguishedNames: **[REQUIRED]** 

      The distinguished names of the organizational units for computer accounts.

      

    
      - *(string) --* 

      
  
    :type ServiceAccountCredentials: dict
    :param ServiceAccountCredentials: **[REQUIRED]** 

      The credentials for the service account used by the streaming instance to connect to the directory.

      

    
      - **AccountName** *(string) --* **[REQUIRED]** 

        The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

        

      
      - **AccountPassword** *(string) --* **[REQUIRED]** 

        The password for the account.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DirectoryConfig': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedNames': [
                    'string',
                ],
                'ServiceAccountCredentials': {
                    'AccountName': 'string',
                    'AccountPassword': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DirectoryConfig** *(dict) --* 

          Information about the directory configuration.

          
          

          - **DirectoryName** *(string) --* 

            The fully qualified name of the directory (for example, corp.example.com).

            
          

          - **OrganizationalUnitDistinguishedNames** *(list) --* 

            The distinguished names of the organizational units for computer accounts.

            
            

            - *(string) --* 
        
          

          - **ServiceAccountCredentials** *(dict) --* 

            The credentials for the service account used by the streaming instance to connect to the directory.

            
            

            - **AccountName** *(string) --* 

              The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

              
            

            - **AccountPassword** *(string) --* 

              The password for the account.

              
        
          

          - **CreatedTime** *(datetime) --* 

            The time the directory configuration was created.

            
      
    

  .. py:method:: create_fleet(**kwargs)

    

    Creates a fleet.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateFleet>`_    


    **Request Syntax** 
    ::

      response = client.create_fleet(
          Name='string',
          ImageName='string',
          InstanceType='string',
          FleetType='ALWAYS_ON'|'ON_DEMAND',
          ComputeCapacity={
              'DesiredInstances': 123
          },
          VpcConfig={
              'SubnetIds': [
                  'string',
              ],
              'SecurityGroupIds': [
                  'string',
              ]
          },
          MaxUserDurationInSeconds=123,
          DisconnectTimeoutInSeconds=123,
          Description='string',
          DisplayName='string',
          EnableDefaultInternetAccess=True|False,
          DomainJoinInfo={
              'DirectoryName': 'string',
              'OrganizationalUnitDistinguishedName': 'string'
          }
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A unique name for the fleet.

      

    
    :type ImageName: string
    :param ImageName: **[REQUIRED]** 

      The name of the image used to create the fleet.

      

    
    :type InstanceType: string
    :param InstanceType: **[REQUIRED]** 

      The instance type to use when launching fleet instances. The following instance types are available:

       

       
      * stream.standard.medium 
       
      * stream.standard.large 
       
      * stream.compute.large 
       
      * stream.compute.xlarge 
       
      * stream.compute.2xlarge 
       
      * stream.compute.4xlarge 
       
      * stream.compute.8xlarge 
       
      * stream.memory.large 
       
      * stream.memory.xlarge 
       
      * stream.memory.2xlarge 
       
      * stream.memory.4xlarge 
       
      * stream.memory.8xlarge 
       
      * stream.graphics-design.large 
       
      * stream.graphics-design.xlarge 
       
      * stream.graphics-design.2xlarge 
       
      * stream.graphics-design.4xlarge 
       
      * stream.graphics-desktop.2xlarge 
       
      * stream.graphics-pro.4xlarge 
       
      * stream.graphics-pro.8xlarge 
       
      * stream.graphics-pro.16xlarge 
       

      

    
    :type FleetType: string
    :param FleetType: 

      The fleet type.

        ALWAYS_ON  

      Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.

        ON_DEMAND  

      Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.

        

    
    :type ComputeCapacity: dict
    :param ComputeCapacity: **[REQUIRED]** 

      The desired capacity for the fleet.

      

    
      - **DesiredInstances** *(integer) --* **[REQUIRED]** 

        The desired number of streaming instances.

        

      
    
    :type VpcConfig: dict
    :param VpcConfig: 

      The VPC configuration for the fleet.

      

    
      - **SubnetIds** *(list) --* 

        The subnets to which a network interface is established from the fleet instance.

        

      
        - *(string) --* 

        
    
      - **SecurityGroupIds** *(list) --* 

        The security groups for the fleet.

        

      
        - *(string) --* 

        
    
    
    :type MaxUserDurationInSeconds: integer
    :param MaxUserDurationInSeconds: 

      The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.

      

    
    :type DisconnectTimeoutInSeconds: integer
    :param DisconnectTimeoutInSeconds: 

      The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.

      

    
    :type Description: string
    :param Description: 

      The description for display.

      

    
    :type DisplayName: string
    :param DisplayName: 

      The fleet name for display.

      

    
    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: 

      Enables or disables default internet access for the fleet.

      

    
    :type DomainJoinInfo: dict
    :param DomainJoinInfo: 

      The information needed to join a Microsoft Active Directory domain.

      

    
      - **DirectoryName** *(string) --* 

        The fully qualified name of the directory (for example, corp.example.com).

        

      
      - **OrganizationalUnitDistinguishedName** *(string) --* 

        The distinguished name of the organizational unit for computer accounts.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Fleet': {
                'Arn': 'string',
                'Name': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'ImageName': 'string',
                'InstanceType': 'string',
                'FleetType': 'ALWAYS_ON'|'ON_DEMAND',
                'ComputeCapacityStatus': {
                    'Desired': 123,
                    'Running': 123,
                    'InUse': 123,
                    'Available': 123
                },
                'MaxUserDurationInSeconds': 123,
                'DisconnectTimeoutInSeconds': 123,
                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'CreatedTime': datetime(2015, 1, 1),
                'FleetErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ],
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Fleet** *(dict) --* 

          Information about the fleet.

          
          

          - **Arn** *(string) --* 

            The ARN for the fleet.

            
          

          - **Name** *(string) --* 

            The name of the fleet.

            
          

          - **DisplayName** *(string) --* 

            The fleet name for display.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **ImageName** *(string) --* 

            The name of the image used to create the fleet.

            
          

          - **InstanceType** *(string) --* 

            The instance type to use when launching fleet instances.

            
          

          - **FleetType** *(string) --* 

            The fleet type.

              ALWAYS_ON  

            Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.

              ON_DEMAND  

            Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.

              
          

          - **ComputeCapacityStatus** *(dict) --* 

            The capacity status for the fleet.

            
            

            - **Desired** *(integer) --* 

              The desired number of streaming instances.

              
            

            - **Running** *(integer) --* 

              The total number of simultaneous streaming instances that are running.

              
            

            - **InUse** *(integer) --* 

              The number of instances in use for streaming.

              
            

            - **Available** *(integer) --* 

              The number of currently available instances that can be used to stream sessions.

              
        
          

          - **MaxUserDurationInSeconds** *(integer) --* 

            The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.

            
          

          - **DisconnectTimeoutInSeconds** *(integer) --* 

            The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.

            
          

          - **State** *(string) --* 

            The current state for the fleet.

            
          

          - **VpcConfig** *(dict) --* 

            The VPC configuration for the fleet.

            
            

            - **SubnetIds** *(list) --* 

              The subnets to which a network interface is established from the fleet instance.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              The security groups for the fleet.

              
              

              - *(string) --* 
          
        
          

          - **CreatedTime** *(datetime) --* 

            The time the fleet was created.

            
          

          - **FleetErrors** *(list) --* 

            The fleet errors.

            
            

            - *(dict) --* 

              Describes a fleet error.

              
              

              - **ErrorCode** *(string) --* 

                The error code.

                
              

              - **ErrorMessage** *(string) --* 

                The error message.

                
          
        
          

          - **EnableDefaultInternetAccess** *(boolean) --* 

            Indicates whether default internet access is enabled for the fleet.

            
          

          - **DomainJoinInfo** *(dict) --* 

            The information needed to join a Microsoft Active Directory domain.

            
            

            - **DirectoryName** *(string) --* 

              The fully qualified name of the directory (for example, corp.example.com).

              
            

            - **OrganizationalUnitDistinguishedName** *(string) --* 

              The distinguished name of the organizational unit for computer accounts.

              
        
      
    

  .. py:method:: create_image_builder(**kwargs)

    

    Creates an image builder.

     

    The initial state of the builder is ``PENDING`` . When it is ready, the state is ``RUNNING`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateImageBuilder>`_    


    **Request Syntax** 
    ::

      response = client.create_image_builder(
          Name='string',
          ImageName='string',
          InstanceType='string',
          Description='string',
          DisplayName='string',
          VpcConfig={
              'SubnetIds': [
                  'string',
              ],
              'SecurityGroupIds': [
                  'string',
              ]
          },
          EnableDefaultInternetAccess=True|False,
          DomainJoinInfo={
              'DirectoryName': 'string',
              'OrganizationalUnitDistinguishedName': 'string'
          },
          AppstreamAgentVersion='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A unique name for the image builder.

      

    
    :type ImageName: string
    :param ImageName: **[REQUIRED]** 

      The name of the image used to create the builder.

      

    
    :type InstanceType: string
    :param InstanceType: **[REQUIRED]** 

      The instance type to use when launching the image builder.

      

    
    :type Description: string
    :param Description: 

      The description for display.

      

    
    :type DisplayName: string
    :param DisplayName: 

      The image builder name for display.

      

    
    :type VpcConfig: dict
    :param VpcConfig: 

      The VPC configuration for the image builder. You can specify only one subnet.

      

    
      - **SubnetIds** *(list) --* 

        The subnets to which a network interface is established from the fleet instance.

        

      
        - *(string) --* 

        
    
      - **SecurityGroupIds** *(list) --* 

        The security groups for the fleet.

        

      
        - *(string) --* 

        
    
    
    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: 

      Enables or disables default internet access for the image builder.

      

    
    :type DomainJoinInfo: dict
    :param DomainJoinInfo: 

      The information needed to join a Microsoft Active Directory domain.

      

    
      - **DirectoryName** *(string) --* 

        The fully qualified name of the directory (for example, corp.example.com).

        

      
      - **OrganizationalUnitDistinguishedName** *(string) --* 

        The distinguished name of the organizational unit for computer accounts.

        

      
    
    :type AppstreamAgentVersion: string
    :param AppstreamAgentVersion: 

      The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ImageBuilder': {
                'Name': 'string',
                'Arn': 'string',
                'ImageArn': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'InstanceType': 'string',
                'Platform': 'WINDOWS',
                'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                    'Message': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1),
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                },
                'ImageBuilderErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string',
                        'ErrorTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'AppstreamAgentVersion': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ImageBuilder** *(dict) --* 

          Information about the image builder.

          
          

          - **Name** *(string) --* 

            The name of the image builder.

            
          

          - **Arn** *(string) --* 

            The ARN for the image builder.

            
          

          - **ImageArn** *(string) --* 

            The ARN of the image from which this builder was created.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **DisplayName** *(string) --* 

            The image builder name for display.

            
          

          - **VpcConfig** *(dict) --* 

            The VPC configuration of the image builder.

            
            

            - **SubnetIds** *(list) --* 

              The subnets to which a network interface is established from the fleet instance.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              The security groups for the fleet.

              
              

              - *(string) --* 
          
        
          

          - **InstanceType** *(string) --* 

            The instance type for the image builder.

            
          

          - **Platform** *(string) --* 

            The operating system platform of the image builder.

            
          

          - **State** *(string) --* 

            The state of the image builder.

            
          

          - **StateChangeReason** *(dict) --* 

            The reason why the last state change occurred.

            
            

            - **Code** *(string) --* 

              The state change reason code.

              
            

            - **Message** *(string) --* 

              The state change reason message.

              
        
          

          - **CreatedTime** *(datetime) --* 

            The time stamp when the image builder was created.

            
          

          - **EnableDefaultInternetAccess** *(boolean) --* 

            Enables or disables default internet access for the image builder.

            
          

          - **DomainJoinInfo** *(dict) --* 

            The information needed to join a Microsoft Active Directory domain.

            
            

            - **DirectoryName** *(string) --* 

              The fully qualified name of the directory (for example, corp.example.com).

              
            

            - **OrganizationalUnitDistinguishedName** *(string) --* 

              The distinguished name of the organizational unit for computer accounts.

              
        
          

          - **ImageBuilderErrors** *(list) --* 

            The image builder errors.

            
            

            - *(dict) --* 

              Describes a resource error.

              
              

              - **ErrorCode** *(string) --* 

                The error code.

                
              

              - **ErrorMessage** *(string) --* 

                The error message.

                
              

              - **ErrorTimestamp** *(datetime) --* 

                The time the error occurred.

                
          
        
          

          - **AppstreamAgentVersion** *(string) --* 

            The version of the AppStream 2.0 agent that is currently being used by this image builder.

            
      
    

  .. py:method:: create_image_builder_streaming_url(**kwargs)

    

    Creates a URL to start an image builder streaming session.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateImageBuilderStreamingURL>`_    


    **Request Syntax** 
    ::

      response = client.create_image_builder_streaming_url(
          Name='string',
          Validity=123
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the image builder.

      

    
    :type Validity: integer
    :param Validity: 

      The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamingURL': 'string',
            'Expires': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StreamingURL** *(string) --* 

          The URL to start the AppStream 2.0 streaming session.

          
        

        - **Expires** *(datetime) --* 

          The elapsed time, in seconds after the Unix epoch, when this URL expires.

          
    

  .. py:method:: create_stack(**kwargs)

    

    Creates a stack.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateStack>`_    


    **Request Syntax** 
    ::

      response = client.create_stack(
          Name='string',
          Description='string',
          DisplayName='string',
          StorageConnectors=[
              {
                  'ConnectorType': 'HOMEFOLDERS',
                  'ResourceIdentifier': 'string'
              },
          ]
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the stack.

      

    
    :type Description: string
    :param Description: 

      The description for display.

      

    
    :type DisplayName: string
    :param DisplayName: 

      The stack name for display.

      

    
    :type StorageConnectors: list
    :param StorageConnectors: 

      The storage connectors to enable.

      

    
      - *(dict) --* 

        Describes a storage connector.

        

      
        - **ConnectorType** *(string) --* **[REQUIRED]** 

          The type of storage connector.

          

        
        - **ResourceIdentifier** *(string) --* 

          The ARN of the storage connector.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Stack': {
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'StorageConnectors': [
                    {
                        'ConnectorType': 'HOMEFOLDERS',
                        'ResourceIdentifier': 'string'
                    },
                ],
                'StackErrors': [
                    {
                        'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Stack** *(dict) --* 

          Information about the stack.

          
          

          - **Arn** *(string) --* 

            The ARN of the stack.

            
          

          - **Name** *(string) --* 

            The name of the stack.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **DisplayName** *(string) --* 

            The stack name for display.

            
          

          - **CreatedTime** *(datetime) --* 

            The time the stack was created.

            
          

          - **StorageConnectors** *(list) --* 

            The storage connectors to enable.

            
            

            - *(dict) --* 

              Describes a storage connector.

              
              

              - **ConnectorType** *(string) --* 

                The type of storage connector.

                
              

              - **ResourceIdentifier** *(string) --* 

                The ARN of the storage connector.

                
          
        
          

          - **StackErrors** *(list) --* 

            The errors for the stack.

            
            

            - *(dict) --* 

              Describes a stack error.

              
              

              - **ErrorCode** *(string) --* 

                The error code.

                
              

              - **ErrorMessage** *(string) --* 

                The error message.

                
          
        
      
    

  .. py:method:: create_streaming_url(**kwargs)

    

    Creates a URL to start a streaming session for the specified user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateStreamingURL>`_    


    **Request Syntax** 
    ::

      response = client.create_streaming_url(
          StackName='string',
          FleetName='string',
          UserId='string',
          ApplicationId='string',
          Validity=123,
          SessionContext='string'
      )
    :type StackName: string
    :param StackName: **[REQUIRED]** 

      The name of the stack.

      

    
    :type FleetName: string
    :param FleetName: **[REQUIRED]** 

      The name of the fleet.

      

    
    :type UserId: string
    :param UserId: **[REQUIRED]** 

      The ID of the user.

      

    
    :type ApplicationId: string
    :param ApplicationId: 

      The name of the application to launch after the session starts. This is the name that you specified as **Name** in the Image Assistant.

      

    
    :type Validity: integer
    :param Validity: 

      The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 60 seconds.

      

    
    :type SessionContext: string
    :param SessionContext: 

      The session context. For more information, see `Session Context <http://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html#managing-stacks-fleets-parameters>`__ in the *Amazon AppStream 2.0 Developer Guide* .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamingURL': 'string',
            'Expires': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StreamingURL** *(string) --* 

          The URL to start the AppStream 2.0 streaming session.

          
        

        - **Expires** *(datetime) --* 

          The elapsed time, in seconds after the Unix epoch, when this URL expires.

          
    

  .. py:method:: delete_directory_config(**kwargs)

    

    Deletes the specified directory configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteDirectoryConfig>`_    


    **Request Syntax** 
    ::

      response = client.delete_directory_config(
          DirectoryName='string'
      )
    :type DirectoryName: string
    :param DirectoryName: **[REQUIRED]** 

      The name of the directory configuration.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_fleet(**kwargs)

    

    Deletes the specified fleet.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteFleet>`_    


    **Request Syntax** 
    ::

      response = client.delete_fleet(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the fleet.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_image(**kwargs)

    

    Deletes the specified image. You cannot delete an image that is currently in use. After you delete an image, you cannot provision new capacity using the image.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteImage>`_    


    **Request Syntax** 
    ::

      response = client.delete_image(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the image.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Image': {
                'Name': 'string',
                'Arn': 'string',
                'BaseImageArn': 'string',
                'DisplayName': 'string',
                'State': 'PENDING'|'AVAILABLE'|'FAILED'|'DELETING',
                'Visibility': 'PUBLIC'|'PRIVATE',
                'ImageBuilderSupported': True|False,
                'Platform': 'WINDOWS',
                'Description': 'string',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'IMAGE_BUILDER_NOT_AVAILABLE',
                    'Message': 'string'
                },
                'Applications': [
                    {
                        'Name': 'string',
                        'DisplayName': 'string',
                        'IconURL': 'string',
                        'LaunchPath': 'string',
                        'LaunchParameters': 'string',
                        'Enabled': True|False,
                        'Metadata': {
                            'string': 'string'
                        }
                    },
                ],
                'CreatedTime': datetime(2015, 1, 1),
                'PublicBaseImageReleasedDate': datetime(2015, 1, 1),
                'AppstreamAgentVersion': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Image** *(dict) --* 

          Information about the image.

          
          

          - **Name** *(string) --* 

            The name of the image.

            
          

          - **Arn** *(string) --* 

            The ARN of the image.

            
          

          - **BaseImageArn** *(string) --* 

            The ARN of the image from which this image was created.

            
          

          - **DisplayName** *(string) --* 

            The image name for display.

            
          

          - **State** *(string) --* 

            The image starts in the ``PENDING`` state. If image creation succeeds, the state is ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .

            
          

          - **Visibility** *(string) --* 

            Indicates whether the image is public or private.

            
          

          - **ImageBuilderSupported** *(boolean) --* 

            Indicates whether an image builder can be launched from this image.

            
          

          - **Platform** *(string) --* 

            The operating system platform of the image.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **StateChangeReason** *(dict) --* 

            The reason why the last state change occurred.

            
            

            - **Code** *(string) --* 

              The state change reason code.

              
            

            - **Message** *(string) --* 

              The state change reason message.

              
        
          

          - **Applications** *(list) --* 

            The applications associated with the image.

            
            

            - *(dict) --* 

              Describes an application in the application catalog.

              
              

              - **Name** *(string) --* 

                The name of the application.

                
              

              - **DisplayName** *(string) --* 

                The application name for display.

                
              

              - **IconURL** *(string) --* 

                The URL for the application icon. This URL might be time-limited.

                
              

              - **LaunchPath** *(string) --* 

                The path to the application executable in the instance.

                
              

              - **LaunchParameters** *(string) --* 

                The arguments that are passed to the application at launch.

                
              

              - **Enabled** *(boolean) --* 

                If there is a problem, the application can be disabled after image creation.

                
              

              - **Metadata** *(dict) --* 

                Additional attributes that describe the application.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
        
          

          - **CreatedTime** *(datetime) --* 

            The time the image was created.

            
          

          - **PublicBaseImageReleasedDate** *(datetime) --* 

            The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.

            
          

          - **AppstreamAgentVersion** *(string) --* 

            The version of the AppStream 2.0 agent to use for instances that are launched from this image.

            
      
    

  .. py:method:: delete_image_builder(**kwargs)

    

    Deletes the specified image builder and releases the capacity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteImageBuilder>`_    


    **Request Syntax** 
    ::

      response = client.delete_image_builder(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the image builder.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ImageBuilder': {
                'Name': 'string',
                'Arn': 'string',
                'ImageArn': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'InstanceType': 'string',
                'Platform': 'WINDOWS',
                'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                    'Message': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1),
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                },
                'ImageBuilderErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string',
                        'ErrorTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'AppstreamAgentVersion': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ImageBuilder** *(dict) --* 

          Information about the image builder.

          
          

          - **Name** *(string) --* 

            The name of the image builder.

            
          

          - **Arn** *(string) --* 

            The ARN for the image builder.

            
          

          - **ImageArn** *(string) --* 

            The ARN of the image from which this builder was created.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **DisplayName** *(string) --* 

            The image builder name for display.

            
          

          - **VpcConfig** *(dict) --* 

            The VPC configuration of the image builder.

            
            

            - **SubnetIds** *(list) --* 

              The subnets to which a network interface is established from the fleet instance.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              The security groups for the fleet.

              
              

              - *(string) --* 
          
        
          

          - **InstanceType** *(string) --* 

            The instance type for the image builder.

            
          

          - **Platform** *(string) --* 

            The operating system platform of the image builder.

            
          

          - **State** *(string) --* 

            The state of the image builder.

            
          

          - **StateChangeReason** *(dict) --* 

            The reason why the last state change occurred.

            
            

            - **Code** *(string) --* 

              The state change reason code.

              
            

            - **Message** *(string) --* 

              The state change reason message.

              
        
          

          - **CreatedTime** *(datetime) --* 

            The time stamp when the image builder was created.

            
          

          - **EnableDefaultInternetAccess** *(boolean) --* 

            Enables or disables default internet access for the image builder.

            
          

          - **DomainJoinInfo** *(dict) --* 

            The information needed to join a Microsoft Active Directory domain.

            
            

            - **DirectoryName** *(string) --* 

              The fully qualified name of the directory (for example, corp.example.com).

              
            

            - **OrganizationalUnitDistinguishedName** *(string) --* 

              The distinguished name of the organizational unit for computer accounts.

              
        
          

          - **ImageBuilderErrors** *(list) --* 

            The image builder errors.

            
            

            - *(dict) --* 

              Describes a resource error.

              
              

              - **ErrorCode** *(string) --* 

                The error code.

                
              

              - **ErrorMessage** *(string) --* 

                The error message.

                
              

              - **ErrorTimestamp** *(datetime) --* 

                The time the error occurred.

                
          
        
          

          - **AppstreamAgentVersion** *(string) --* 

            The version of the AppStream 2.0 agent that is currently being used by this image builder.

            
      
    

  .. py:method:: delete_stack(**kwargs)

    

    Deletes the specified stack. After this operation completes, the environment can no longer be activated and any reservations made for the stack are released.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteStack>`_    


    **Request Syntax** 
    ::

      response = client.delete_stack(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the stack.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_directory_configs(**kwargs)

    

    Describes the specified directory configurations.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeDirectoryConfigs>`_    


    **Request Syntax** 
    ::

      response = client.describe_directory_configs(
          DirectoryNames=[
              'string',
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type DirectoryNames: list
    :param DirectoryNames: 

      The directory names.

      

    
      - *(string) --* 

      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum size of each page of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DirectoryConfigs': [
                {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedNames': [
                        'string',
                    ],
                    'ServiceAccountCredentials': {
                        'AccountName': 'string',
                        'AccountPassword': 'string'
                    },
                    'CreatedTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DirectoryConfigs** *(list) --* 

          Information about the directory configurations.

          
          

          - *(dict) --* 

            Configuration information for the directory used to join domains.

            
            

            - **DirectoryName** *(string) --* 

              The fully qualified name of the directory (for example, corp.example.com).

              
            

            - **OrganizationalUnitDistinguishedNames** *(list) --* 

              The distinguished names of the organizational units for computer accounts.

              
              

              - *(string) --* 
          
            

            - **ServiceAccountCredentials** *(dict) --* 

              The credentials for the service account used by the streaming instance to connect to the directory.

              
              

              - **AccountName** *(string) --* 

                The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

                
              

              - **AccountPassword** *(string) --* 

                The password for the account.

                
          
            

            - **CreatedTime** *(datetime) --* 

              The time the directory configuration was created.

              
        
      
        

        - **NextToken** *(string) --* 

          The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.

          
    

  .. py:method:: describe_fleets(**kwargs)

    

    Describes the specified fleets or all fleets in the account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeFleets>`_    


    **Request Syntax** 
    ::

      response = client.describe_fleets(
          Names=[
              'string',
          ],
          NextToken='string'
      )
    :type Names: list
    :param Names: 

      The names of the fleets to describe.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Fleets': [
                {
                    'Arn': 'string',
                    'Name': 'string',
                    'DisplayName': 'string',
                    'Description': 'string',
                    'ImageName': 'string',
                    'InstanceType': 'string',
                    'FleetType': 'ALWAYS_ON'|'ON_DEMAND',
                    'ComputeCapacityStatus': {
                        'Desired': 123,
                        'Running': 123,
                        'InUse': 123,
                        'Available': 123
                    },
                    'MaxUserDurationInSeconds': 123,
                    'DisconnectTimeoutInSeconds': 123,
                    'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
                    'VpcConfig': {
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ]
                    },
                    'CreatedTime': datetime(2015, 1, 1),
                    'FleetErrors': [
                        {
                            'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                            'ErrorMessage': 'string'
                        },
                    ],
                    'EnableDefaultInternetAccess': True|False,
                    'DomainJoinInfo': {
                        'DirectoryName': 'string',
                        'OrganizationalUnitDistinguishedName': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Fleets** *(list) --* 

          Information about the fleets.

          
          

          - *(dict) --* 

            Contains the parameters for a fleet.

            
            

            - **Arn** *(string) --* 

              The ARN for the fleet.

              
            

            - **Name** *(string) --* 

              The name of the fleet.

              
            

            - **DisplayName** *(string) --* 

              The fleet name for display.

              
            

            - **Description** *(string) --* 

              The description for display.

              
            

            - **ImageName** *(string) --* 

              The name of the image used to create the fleet.

              
            

            - **InstanceType** *(string) --* 

              The instance type to use when launching fleet instances.

              
            

            - **FleetType** *(string) --* 

              The fleet type.

                ALWAYS_ON  

              Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.

                ON_DEMAND  

              Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.

                
            

            - **ComputeCapacityStatus** *(dict) --* 

              The capacity status for the fleet.

              
              

              - **Desired** *(integer) --* 

                The desired number of streaming instances.

                
              

              - **Running** *(integer) --* 

                The total number of simultaneous streaming instances that are running.

                
              

              - **InUse** *(integer) --* 

                The number of instances in use for streaming.

                
              

              - **Available** *(integer) --* 

                The number of currently available instances that can be used to stream sessions.

                
          
            

            - **MaxUserDurationInSeconds** *(integer) --* 

              The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.

              
            

            - **DisconnectTimeoutInSeconds** *(integer) --* 

              The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.

              
            

            - **State** *(string) --* 

              The current state for the fleet.

              
            

            - **VpcConfig** *(dict) --* 

              The VPC configuration for the fleet.

              
              

              - **SubnetIds** *(list) --* 

                The subnets to which a network interface is established from the fleet instance.

                
                

                - *(string) --* 
            
              

              - **SecurityGroupIds** *(list) --* 

                The security groups for the fleet.

                
                

                - *(string) --* 
            
          
            

            - **CreatedTime** *(datetime) --* 

              The time the fleet was created.

              
            

            - **FleetErrors** *(list) --* 

              The fleet errors.

              
              

              - *(dict) --* 

                Describes a fleet error.

                
                

                - **ErrorCode** *(string) --* 

                  The error code.

                  
                

                - **ErrorMessage** *(string) --* 

                  The error message.

                  
            
          
            

            - **EnableDefaultInternetAccess** *(boolean) --* 

              Indicates whether default internet access is enabled for the fleet.

              
            

            - **DomainJoinInfo** *(dict) --* 

              The information needed to join a Microsoft Active Directory domain.

              
              

              - **DirectoryName** *(string) --* 

                The fully qualified name of the directory (for example, corp.example.com).

                
              

              - **OrganizationalUnitDistinguishedName** *(string) --* 

                The distinguished name of the organizational unit for computer accounts.

                
          
        
      
        

        - **NextToken** *(string) --* 

          The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.

          
    

  .. py:method:: describe_image_builders(**kwargs)

    

    Describes the specified image builders or all image builders in the account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeImageBuilders>`_    


    **Request Syntax** 
    ::

      response = client.describe_image_builders(
          Names=[
              'string',
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type Names: list
    :param Names: 

      The names of the image builders to describe.

      

    
      - *(string) --* 

      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum size of each page of results.

      

    
    :type NextToken: string
    :param NextToken: 

      The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ImageBuilders': [
                {
                    'Name': 'string',
                    'Arn': 'string',
                    'ImageArn': 'string',
                    'Description': 'string',
                    'DisplayName': 'string',
                    'VpcConfig': {
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ]
                    },
                    'InstanceType': 'string',
                    'Platform': 'WINDOWS',
                    'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
                    'StateChangeReason': {
                        'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                        'Message': 'string'
                    },
                    'CreatedTime': datetime(2015, 1, 1),
                    'EnableDefaultInternetAccess': True|False,
                    'DomainJoinInfo': {
                        'DirectoryName': 'string',
                        'OrganizationalUnitDistinguishedName': 'string'
                    },
                    'ImageBuilderErrors': [
                        {
                            'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                            'ErrorMessage': 'string',
                            'ErrorTimestamp': datetime(2015, 1, 1)
                        },
                    ],
                    'AppstreamAgentVersion': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ImageBuilders** *(list) --* 

          Information about the image builders.

          
          

          - *(dict) --* 

            Describes a streaming instance used for editing an image. New images are created from a snapshot through an image builder.

            
            

            - **Name** *(string) --* 

              The name of the image builder.

              
            

            - **Arn** *(string) --* 

              The ARN for the image builder.

              
            

            - **ImageArn** *(string) --* 

              The ARN of the image from which this builder was created.

              
            

            - **Description** *(string) --* 

              The description for display.

              
            

            - **DisplayName** *(string) --* 

              The image builder name for display.

              
            

            - **VpcConfig** *(dict) --* 

              The VPC configuration of the image builder.

              
              

              - **SubnetIds** *(list) --* 

                The subnets to which a network interface is established from the fleet instance.

                
                

                - *(string) --* 
            
              

              - **SecurityGroupIds** *(list) --* 

                The security groups for the fleet.

                
                

                - *(string) --* 
            
          
            

            - **InstanceType** *(string) --* 

              The instance type for the image builder.

              
            

            - **Platform** *(string) --* 

              The operating system platform of the image builder.

              
            

            - **State** *(string) --* 

              The state of the image builder.

              
            

            - **StateChangeReason** *(dict) --* 

              The reason why the last state change occurred.

              
              

              - **Code** *(string) --* 

                The state change reason code.

                
              

              - **Message** *(string) --* 

                The state change reason message.

                
          
            

            - **CreatedTime** *(datetime) --* 

              The time stamp when the image builder was created.

              
            

            - **EnableDefaultInternetAccess** *(boolean) --* 

              Enables or disables default internet access for the image builder.

              
            

            - **DomainJoinInfo** *(dict) --* 

              The information needed to join a Microsoft Active Directory domain.

              
              

              - **DirectoryName** *(string) --* 

                The fully qualified name of the directory (for example, corp.example.com).

                
              

              - **OrganizationalUnitDistinguishedName** *(string) --* 

                The distinguished name of the organizational unit for computer accounts.

                
          
            

            - **ImageBuilderErrors** *(list) --* 

              The image builder errors.

              
              

              - *(dict) --* 

                Describes a resource error.

                
                

                - **ErrorCode** *(string) --* 

                  The error code.

                  
                

                - **ErrorMessage** *(string) --* 

                  The error message.

                  
                

                - **ErrorTimestamp** *(datetime) --* 

                  The time the error occurred.

                  
            
          
            

            - **AppstreamAgentVersion** *(string) --* 

              The version of the AppStream 2.0 agent that is currently being used by this image builder.

              
        
      
        

        - **NextToken** *(string) --* 

          The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.

          
    

  .. py:method:: describe_images(**kwargs)

    

    Describes the specified images or all images in the account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeImages>`_    


    **Request Syntax** 
    ::

      response = client.describe_images(
          Names=[
              'string',
          ]
      )
    :type Names: list
    :param Names: 

      The names of the images to describe.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Images': [
                {
                    'Name': 'string',
                    'Arn': 'string',
                    'BaseImageArn': 'string',
                    'DisplayName': 'string',
                    'State': 'PENDING'|'AVAILABLE'|'FAILED'|'DELETING',
                    'Visibility': 'PUBLIC'|'PRIVATE',
                    'ImageBuilderSupported': True|False,
                    'Platform': 'WINDOWS',
                    'Description': 'string',
                    'StateChangeReason': {
                        'Code': 'INTERNAL_ERROR'|'IMAGE_BUILDER_NOT_AVAILABLE',
                        'Message': 'string'
                    },
                    'Applications': [
                        {
                            'Name': 'string',
                            'DisplayName': 'string',
                            'IconURL': 'string',
                            'LaunchPath': 'string',
                            'LaunchParameters': 'string',
                            'Enabled': True|False,
                            'Metadata': {
                                'string': 'string'
                            }
                        },
                    ],
                    'CreatedTime': datetime(2015, 1, 1),
                    'PublicBaseImageReleasedDate': datetime(2015, 1, 1),
                    'AppstreamAgentVersion': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Images** *(list) --* 

          Information about the images.

          
          

          - *(dict) --* 

            Describes an image.

            
            

            - **Name** *(string) --* 

              The name of the image.

              
            

            - **Arn** *(string) --* 

              The ARN of the image.

              
            

            - **BaseImageArn** *(string) --* 

              The ARN of the image from which this image was created.

              
            

            - **DisplayName** *(string) --* 

              The image name for display.

              
            

            - **State** *(string) --* 

              The image starts in the ``PENDING`` state. If image creation succeeds, the state is ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .

              
            

            - **Visibility** *(string) --* 

              Indicates whether the image is public or private.

              
            

            - **ImageBuilderSupported** *(boolean) --* 

              Indicates whether an image builder can be launched from this image.

              
            

            - **Platform** *(string) --* 

              The operating system platform of the image.

              
            

            - **Description** *(string) --* 

              The description for display.

              
            

            - **StateChangeReason** *(dict) --* 

              The reason why the last state change occurred.

              
              

              - **Code** *(string) --* 

                The state change reason code.

                
              

              - **Message** *(string) --* 

                The state change reason message.

                
          
            

            - **Applications** *(list) --* 

              The applications associated with the image.

              
              

              - *(dict) --* 

                Describes an application in the application catalog.

                
                

                - **Name** *(string) --* 

                  The name of the application.

                  
                

                - **DisplayName** *(string) --* 

                  The application name for display.

                  
                

                - **IconURL** *(string) --* 

                  The URL for the application icon. This URL might be time-limited.

                  
                

                - **LaunchPath** *(string) --* 

                  The path to the application executable in the instance.

                  
                

                - **LaunchParameters** *(string) --* 

                  The arguments that are passed to the application at launch.

                  
                

                - **Enabled** *(boolean) --* 

                  If there is a problem, the application can be disabled after image creation.

                  
                

                - **Metadata** *(dict) --* 

                  Additional attributes that describe the application.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
          
            

            - **CreatedTime** *(datetime) --* 

              The time the image was created.

              
            

            - **PublicBaseImageReleasedDate** *(datetime) --* 

              The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.

              
            

            - **AppstreamAgentVersion** *(string) --* 

              The version of the AppStream 2.0 agent to use for instances that are launched from this image.

              
        
      
    

  .. py:method:: describe_sessions(**kwargs)

    

    Describes the streaming sessions for the specified stack and fleet. If a user ID is provided, only the streaming sessions for only that user are returned. If an authentication type is not provided, the default is to authenticate users using a streaming URL.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeSessions>`_    


    **Request Syntax** 
    ::

      response = client.describe_sessions(
          StackName='string',
          FleetName='string',
          UserId='string',
          NextToken='string',
          Limit=123,
          AuthenticationType='API'|'SAML'|'USERPOOL'
      )
    :type StackName: string
    :param StackName: **[REQUIRED]** 

      The name of the stack.

      

    
    :type FleetName: string
    :param FleetName: **[REQUIRED]** 

      The name of the fleet.

      

    
    :type UserId: string
    :param UserId: 

      The user ID.

      

    
    :type NextToken: string
    :param NextToken: 

      The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

      

    
    :type Limit: integer
    :param Limit: 

      The size of each page of results. The default value is 20 and the maximum value is 50.

      

    
    :type AuthenticationType: string
    :param AuthenticationType: 

      The authentication method. Specify ``API`` for a user authenticated using a streaming URL or ``SAML`` for a SAML federated user. The default is to authenticate users using a streaming URL.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Sessions': [
                {
                    'Id': 'string',
                    'UserId': 'string',
                    'StackName': 'string',
                    'FleetName': 'string',
                    'State': 'ACTIVE'|'PENDING'|'EXPIRED',
                    'AuthenticationType': 'API'|'SAML'|'USERPOOL'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Sessions** *(list) --* 

          Information about the streaming sessions.

          
          

          - *(dict) --* 

            Describes a streaming session.

            
            

            - **Id** *(string) --* 

              The ID of the streaming session.

              
            

            - **UserId** *(string) --* 

              The identifier of the user for whom the session was created.

              
            

            - **StackName** *(string) --* 

              The name of the stack for the streaming session.

              
            

            - **FleetName** *(string) --* 

              The name of the fleet for the streaming session.

              
            

            - **State** *(string) --* 

              The current state of the streaming session.

              
            

            - **AuthenticationType** *(string) --* 

              The authentication method. The user is authenticated using a streaming URL (``API`` ) or SAML federation (``SAML`` ).

              
        
      
        

        - **NextToken** *(string) --* 

          The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.

          
    

  .. py:method:: describe_stacks(**kwargs)

    

    Describes the specified stacks or all stacks in the account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeStacks>`_    


    **Request Syntax** 
    ::

      response = client.describe_stacks(
          Names=[
              'string',
          ],
          NextToken='string'
      )
    :type Names: list
    :param Names: 

      The names of the stacks to describe.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Stacks': [
                {
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'DisplayName': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'StorageConnectors': [
                        {
                            'ConnectorType': 'HOMEFOLDERS',
                            'ResourceIdentifier': 'string'
                        },
                    ],
                    'StackErrors': [
                        {
                            'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                            'ErrorMessage': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Stacks** *(list) --* 

          Information about the stacks.

          
          

          - *(dict) --* 

            Describes a stack.

            
            

            - **Arn** *(string) --* 

              The ARN of the stack.

              
            

            - **Name** *(string) --* 

              The name of the stack.

              
            

            - **Description** *(string) --* 

              The description for display.

              
            

            - **DisplayName** *(string) --* 

              The stack name for display.

              
            

            - **CreatedTime** *(datetime) --* 

              The time the stack was created.

              
            

            - **StorageConnectors** *(list) --* 

              The storage connectors to enable.

              
              

              - *(dict) --* 

                Describes a storage connector.

                
                

                - **ConnectorType** *(string) --* 

                  The type of storage connector.

                  
                

                - **ResourceIdentifier** *(string) --* 

                  The ARN of the storage connector.

                  
            
          
            

            - **StackErrors** *(list) --* 

              The errors for the stack.

              
              

              - *(dict) --* 

                Describes a stack error.

                
                

                - **ErrorCode** *(string) --* 

                  The error code.

                  
                

                - **ErrorMessage** *(string) --* 

                  The error message.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.

          
    

  .. py:method:: disassociate_fleet(**kwargs)

    

    Disassociates the specified fleet from the specified stack.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DisassociateFleet>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_fleet(
          FleetName='string',
          StackName='string'
      )
    :type FleetName: string
    :param FleetName: **[REQUIRED]** 

      The name of the fleet.

      

    
    :type StackName: string
    :param StackName: **[REQUIRED]** 

      The name of the stack.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: expire_session(**kwargs)

    

    Stops the specified streaming session.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ExpireSession>`_    


    **Request Syntax** 
    ::

      response = client.expire_session(
          SessionId='string'
      )
    :type SessionId: string
    :param SessionId: **[REQUIRED]** 

      The ID of the streaming session.

      

    
    
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

        


  .. py:method:: list_associated_fleets(**kwargs)

    

    Lists the fleets associated with the specified stack.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ListAssociatedFleets>`_    


    **Request Syntax** 
    ::

      response = client.list_associated_fleets(
          StackName='string',
          NextToken='string'
      )
    :type StackName: string
    :param StackName: **[REQUIRED]** 

      The name of the stack.

      

    
    :type NextToken: string
    :param NextToken: 

      The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Names': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Names** *(list) --* 

          The names of the fleets.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.

          
    

  .. py:method:: list_associated_stacks(**kwargs)

    

    Lists the stacks associated with the specified fleet.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ListAssociatedStacks>`_    


    **Request Syntax** 
    ::

      response = client.list_associated_stacks(
          FleetName='string',
          NextToken='string'
      )
    :type FleetName: string
    :param FleetName: **[REQUIRED]** 

      The name of the fleet.

      

    
    :type NextToken: string
    :param NextToken: 

      The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Names': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Names** *(list) --* 

          The names of the stacks.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.

          
    

  .. py:method:: start_fleet(**kwargs)

    

    Starts the specified fleet.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StartFleet>`_    


    **Request Syntax** 
    ::

      response = client.start_fleet(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the fleet.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: start_image_builder(**kwargs)

    

    Starts the specified image builder.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StartImageBuilder>`_    


    **Request Syntax** 
    ::

      response = client.start_image_builder(
          Name='string',
          AppstreamAgentVersion='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the image builder.

      

    
    :type AppstreamAgentVersion: string
    :param AppstreamAgentVersion: 

      The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ImageBuilder': {
                'Name': 'string',
                'Arn': 'string',
                'ImageArn': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'InstanceType': 'string',
                'Platform': 'WINDOWS',
                'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                    'Message': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1),
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                },
                'ImageBuilderErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string',
                        'ErrorTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'AppstreamAgentVersion': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ImageBuilder** *(dict) --* 

          Information about the image builder.

          
          

          - **Name** *(string) --* 

            The name of the image builder.

            
          

          - **Arn** *(string) --* 

            The ARN for the image builder.

            
          

          - **ImageArn** *(string) --* 

            The ARN of the image from which this builder was created.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **DisplayName** *(string) --* 

            The image builder name for display.

            
          

          - **VpcConfig** *(dict) --* 

            The VPC configuration of the image builder.

            
            

            - **SubnetIds** *(list) --* 

              The subnets to which a network interface is established from the fleet instance.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              The security groups for the fleet.

              
              

              - *(string) --* 
          
        
          

          - **InstanceType** *(string) --* 

            The instance type for the image builder.

            
          

          - **Platform** *(string) --* 

            The operating system platform of the image builder.

            
          

          - **State** *(string) --* 

            The state of the image builder.

            
          

          - **StateChangeReason** *(dict) --* 

            The reason why the last state change occurred.

            
            

            - **Code** *(string) --* 

              The state change reason code.

              
            

            - **Message** *(string) --* 

              The state change reason message.

              
        
          

          - **CreatedTime** *(datetime) --* 

            The time stamp when the image builder was created.

            
          

          - **EnableDefaultInternetAccess** *(boolean) --* 

            Enables or disables default internet access for the image builder.

            
          

          - **DomainJoinInfo** *(dict) --* 

            The information needed to join a Microsoft Active Directory domain.

            
            

            - **DirectoryName** *(string) --* 

              The fully qualified name of the directory (for example, corp.example.com).

              
            

            - **OrganizationalUnitDistinguishedName** *(string) --* 

              The distinguished name of the organizational unit for computer accounts.

              
        
          

          - **ImageBuilderErrors** *(list) --* 

            The image builder errors.

            
            

            - *(dict) --* 

              Describes a resource error.

              
              

              - **ErrorCode** *(string) --* 

                The error code.

                
              

              - **ErrorMessage** *(string) --* 

                The error message.

                
              

              - **ErrorTimestamp** *(datetime) --* 

                The time the error occurred.

                
          
        
          

          - **AppstreamAgentVersion** *(string) --* 

            The version of the AppStream 2.0 agent that is currently being used by this image builder.

            
      
    

  .. py:method:: stop_fleet(**kwargs)

    

    Stops the specified fleet.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StopFleet>`_    


    **Request Syntax** 
    ::

      response = client.stop_fleet(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the fleet.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: stop_image_builder(**kwargs)

    

    Stops the specified image builder.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StopImageBuilder>`_    


    **Request Syntax** 
    ::

      response = client.stop_image_builder(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the image builder.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ImageBuilder': {
                'Name': 'string',
                'Arn': 'string',
                'ImageArn': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'InstanceType': 'string',
                'Platform': 'WINDOWS',
                'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                    'Message': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1),
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                },
                'ImageBuilderErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string',
                        'ErrorTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'AppstreamAgentVersion': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ImageBuilder** *(dict) --* 

          Information about the image builder.

          
          

          - **Name** *(string) --* 

            The name of the image builder.

            
          

          - **Arn** *(string) --* 

            The ARN for the image builder.

            
          

          - **ImageArn** *(string) --* 

            The ARN of the image from which this builder was created.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **DisplayName** *(string) --* 

            The image builder name for display.

            
          

          - **VpcConfig** *(dict) --* 

            The VPC configuration of the image builder.

            
            

            - **SubnetIds** *(list) --* 

              The subnets to which a network interface is established from the fleet instance.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              The security groups for the fleet.

              
              

              - *(string) --* 
          
        
          

          - **InstanceType** *(string) --* 

            The instance type for the image builder.

            
          

          - **Platform** *(string) --* 

            The operating system platform of the image builder.

            
          

          - **State** *(string) --* 

            The state of the image builder.

            
          

          - **StateChangeReason** *(dict) --* 

            The reason why the last state change occurred.

            
            

            - **Code** *(string) --* 

              The state change reason code.

              
            

            - **Message** *(string) --* 

              The state change reason message.

              
        
          

          - **CreatedTime** *(datetime) --* 

            The time stamp when the image builder was created.

            
          

          - **EnableDefaultInternetAccess** *(boolean) --* 

            Enables or disables default internet access for the image builder.

            
          

          - **DomainJoinInfo** *(dict) --* 

            The information needed to join a Microsoft Active Directory domain.

            
            

            - **DirectoryName** *(string) --* 

              The fully qualified name of the directory (for example, corp.example.com).

              
            

            - **OrganizationalUnitDistinguishedName** *(string) --* 

              The distinguished name of the organizational unit for computer accounts.

              
        
          

          - **ImageBuilderErrors** *(list) --* 

            The image builder errors.

            
            

            - *(dict) --* 

              Describes a resource error.

              
              

              - **ErrorCode** *(string) --* 

                The error code.

                
              

              - **ErrorMessage** *(string) --* 

                The error message.

                
              

              - **ErrorTimestamp** *(datetime) --* 

                The time the error occurred.

                
          
        
          

          - **AppstreamAgentVersion** *(string) --* 

            The version of the AppStream 2.0 agent that is currently being used by this image builder.

            
      
    

  .. py:method:: update_directory_config(**kwargs)

    

    Updates the specified directory configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateDirectoryConfig>`_    


    **Request Syntax** 
    ::

      response = client.update_directory_config(
          DirectoryName='string',
          OrganizationalUnitDistinguishedNames=[
              'string',
          ],
          ServiceAccountCredentials={
              'AccountName': 'string',
              'AccountPassword': 'string'
          }
      )
    :type DirectoryName: string
    :param DirectoryName: **[REQUIRED]** 

      The name of the directory configuration.

      

    
    :type OrganizationalUnitDistinguishedNames: list
    :param OrganizationalUnitDistinguishedNames: 

      The distinguished names of the organizational units for computer accounts.

      

    
      - *(string) --* 

      
  
    :type ServiceAccountCredentials: dict
    :param ServiceAccountCredentials: 

      The credentials for the service account used by the streaming instance to connect to the directory.

      

    
      - **AccountName** *(string) --* **[REQUIRED]** 

        The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

        

      
      - **AccountPassword** *(string) --* **[REQUIRED]** 

        The password for the account.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DirectoryConfig': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedNames': [
                    'string',
                ],
                'ServiceAccountCredentials': {
                    'AccountName': 'string',
                    'AccountPassword': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DirectoryConfig** *(dict) --* 

          Information about the directory configuration.

          
          

          - **DirectoryName** *(string) --* 

            The fully qualified name of the directory (for example, corp.example.com).

            
          

          - **OrganizationalUnitDistinguishedNames** *(list) --* 

            The distinguished names of the organizational units for computer accounts.

            
            

            - *(string) --* 
        
          

          - **ServiceAccountCredentials** *(dict) --* 

            The credentials for the service account used by the streaming instance to connect to the directory.

            
            

            - **AccountName** *(string) --* 

              The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

              
            

            - **AccountPassword** *(string) --* 

              The password for the account.

              
        
          

          - **CreatedTime** *(datetime) --* 

            The time the directory configuration was created.

            
      
    

  .. py:method:: update_fleet(**kwargs)

    

    Updates the specified fleet.

     

    If the fleet is in the ``STOPPED`` state, you can update any attribute except the fleet name. If the fleet is in the ``RUNNING`` state, you can update the ``DisplayName`` and ``ComputeCapacity`` attributes. If the fleet is in the ``STARTING`` or ``STOPPING`` state, you can't update it.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateFleet>`_    


    **Request Syntax** 
    ::

      response = client.update_fleet(
          ImageName='string',
          Name='string',
          InstanceType='string',
          ComputeCapacity={
              'DesiredInstances': 123
          },
          VpcConfig={
              'SubnetIds': [
                  'string',
              ],
              'SecurityGroupIds': [
                  'string',
              ]
          },
          MaxUserDurationInSeconds=123,
          DisconnectTimeoutInSeconds=123,
          DeleteVpcConfig=True|False,
          Description='string',
          DisplayName='string',
          EnableDefaultInternetAccess=True|False,
          DomainJoinInfo={
              'DirectoryName': 'string',
              'OrganizationalUnitDistinguishedName': 'string'
          },
          AttributesToDelete=[
              'VPC_CONFIGURATION'|'VPC_CONFIGURATION_SECURITY_GROUP_IDS'|'DOMAIN_JOIN_INFO',
          ]
      )
    :type ImageName: string
    :param ImageName: 

      The name of the image used to create the fleet.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      A unique name for the fleet.

      

    
    :type InstanceType: string
    :param InstanceType: 

      The instance type to use when launching fleet instances. The following instance types are available:

       

       
      * stream.standard.medium 
       
      * stream.standard.large 
       
      * stream.compute.large 
       
      * stream.compute.xlarge 
       
      * stream.compute.2xlarge 
       
      * stream.compute.4xlarge 
       
      * stream.compute.8xlarge 
       
      * stream.memory.large 
       
      * stream.memory.xlarge 
       
      * stream.memory.2xlarge 
       
      * stream.memory.4xlarge 
       
      * stream.memory.8xlarge 
       
      * stream.graphics-design.large 
       
      * stream.graphics-design.xlarge 
       
      * stream.graphics-design.2xlarge 
       
      * stream.graphics-design.4xlarge 
       
      * stream.graphics-desktop.2xlarge 
       
      * stream.graphics-pro.4xlarge 
       
      * stream.graphics-pro.8xlarge 
       
      * stream.graphics-pro.16xlarge 
       

      

    
    :type ComputeCapacity: dict
    :param ComputeCapacity: 

      The desired capacity for the fleet.

      

    
      - **DesiredInstances** *(integer) --* **[REQUIRED]** 

        The desired number of streaming instances.

        

      
    
    :type VpcConfig: dict
    :param VpcConfig: 

      The VPC configuration for the fleet.

      

    
      - **SubnetIds** *(list) --* 

        The subnets to which a network interface is established from the fleet instance.

        

      
        - *(string) --* 

        
    
      - **SecurityGroupIds** *(list) --* 

        The security groups for the fleet.

        

      
        - *(string) --* 

        
    
    
    :type MaxUserDurationInSeconds: integer
    :param MaxUserDurationInSeconds: 

      The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.

      

    
    :type DisconnectTimeoutInSeconds: integer
    :param DisconnectTimeoutInSeconds: 

      The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.

      

    
    :type DeleteVpcConfig: boolean
    :param DeleteVpcConfig: 

      Deletes the VPC association for the specified fleet.

      

    
    :type Description: string
    :param Description: 

      The description for display.

      

    
    :type DisplayName: string
    :param DisplayName: 

      The fleet name for display.

      

    
    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: 

      Enables or disables default internet access for the fleet.

      

    
    :type DomainJoinInfo: dict
    :param DomainJoinInfo: 

      The information needed to join a Microsoft Active Directory domain.

      

    
      - **DirectoryName** *(string) --* 

        The fully qualified name of the directory (for example, corp.example.com).

        

      
      - **OrganizationalUnitDistinguishedName** *(string) --* 

        The distinguished name of the organizational unit for computer accounts.

        

      
    
    :type AttributesToDelete: list
    :param AttributesToDelete: 

      The fleet attributes to delete.

      

    
      - *(string) --* 

        The fleet attribute.

        

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Fleet': {
                'Arn': 'string',
                'Name': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'ImageName': 'string',
                'InstanceType': 'string',
                'FleetType': 'ALWAYS_ON'|'ON_DEMAND',
                'ComputeCapacityStatus': {
                    'Desired': 123,
                    'Running': 123,
                    'InUse': 123,
                    'Available': 123
                },
                'MaxUserDurationInSeconds': 123,
                'DisconnectTimeoutInSeconds': 123,
                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'CreatedTime': datetime(2015, 1, 1),
                'FleetErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ],
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Fleet** *(dict) --* 

          Information about the fleet.

          
          

          - **Arn** *(string) --* 

            The ARN for the fleet.

            
          

          - **Name** *(string) --* 

            The name of the fleet.

            
          

          - **DisplayName** *(string) --* 

            The fleet name for display.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **ImageName** *(string) --* 

            The name of the image used to create the fleet.

            
          

          - **InstanceType** *(string) --* 

            The instance type to use when launching fleet instances.

            
          

          - **FleetType** *(string) --* 

            The fleet type.

              ALWAYS_ON  

            Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.

              ON_DEMAND  

            Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.

              
          

          - **ComputeCapacityStatus** *(dict) --* 

            The capacity status for the fleet.

            
            

            - **Desired** *(integer) --* 

              The desired number of streaming instances.

              
            

            - **Running** *(integer) --* 

              The total number of simultaneous streaming instances that are running.

              
            

            - **InUse** *(integer) --* 

              The number of instances in use for streaming.

              
            

            - **Available** *(integer) --* 

              The number of currently available instances that can be used to stream sessions.

              
        
          

          - **MaxUserDurationInSeconds** *(integer) --* 

            The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.

            
          

          - **DisconnectTimeoutInSeconds** *(integer) --* 

            The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.

            
          

          - **State** *(string) --* 

            The current state for the fleet.

            
          

          - **VpcConfig** *(dict) --* 

            The VPC configuration for the fleet.

            
            

            - **SubnetIds** *(list) --* 

              The subnets to which a network interface is established from the fleet instance.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              The security groups for the fleet.

              
              

              - *(string) --* 
          
        
          

          - **CreatedTime** *(datetime) --* 

            The time the fleet was created.

            
          

          - **FleetErrors** *(list) --* 

            The fleet errors.

            
            

            - *(dict) --* 

              Describes a fleet error.

              
              

              - **ErrorCode** *(string) --* 

                The error code.

                
              

              - **ErrorMessage** *(string) --* 

                The error message.

                
          
        
          

          - **EnableDefaultInternetAccess** *(boolean) --* 

            Indicates whether default internet access is enabled for the fleet.

            
          

          - **DomainJoinInfo** *(dict) --* 

            The information needed to join a Microsoft Active Directory domain.

            
            

            - **DirectoryName** *(string) --* 

              The fully qualified name of the directory (for example, corp.example.com).

              
            

            - **OrganizationalUnitDistinguishedName** *(string) --* 

              The distinguished name of the organizational unit for computer accounts.

              
        
      
    

  .. py:method:: update_stack(**kwargs)

    

    Updates the specified stack.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateStack>`_    


    **Request Syntax** 
    ::

      response = client.update_stack(
          DisplayName='string',
          Description='string',
          Name='string',
          StorageConnectors=[
              {
                  'ConnectorType': 'HOMEFOLDERS',
                  'ResourceIdentifier': 'string'
              },
          ],
          DeleteStorageConnectors=True|False
      )
    :type DisplayName: string
    :param DisplayName: 

      The stack name for display.

      

    
    :type Description: string
    :param Description: 

      The description for display.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the stack.

      

    
    :type StorageConnectors: list
    :param StorageConnectors: 

      The storage connectors to enable.

      

    
      - *(dict) --* 

        Describes a storage connector.

        

      
        - **ConnectorType** *(string) --* **[REQUIRED]** 

          The type of storage connector.

          

        
        - **ResourceIdentifier** *(string) --* 

          The ARN of the storage connector.

          

        
      
  
    :type DeleteStorageConnectors: boolean
    :param DeleteStorageConnectors: 

      Deletes the storage connectors currently enabled for the stack.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Stack': {
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'StorageConnectors': [
                    {
                        'ConnectorType': 'HOMEFOLDERS',
                        'ResourceIdentifier': 'string'
                    },
                ],
                'StackErrors': [
                    {
                        'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Stack** *(dict) --* 

          Information about the stack.

          
          

          - **Arn** *(string) --* 

            The ARN of the stack.

            
          

          - **Name** *(string) --* 

            The name of the stack.

            
          

          - **Description** *(string) --* 

            The description for display.

            
          

          - **DisplayName** *(string) --* 

            The stack name for display.

            
          

          - **CreatedTime** *(datetime) --* 

            The time the stack was created.

            
          

          - **StorageConnectors** *(list) --* 

            The storage connectors to enable.

            
            

            - *(dict) --* 

              Describes a storage connector.

              
              

              - **ConnectorType** *(string) --* 

                The type of storage connector.

                
              

              - **ResourceIdentifier** *(string) --* 

                The ARN of the storage connector.

                
          
        
          

          - **StackErrors** *(list) --* 

            The errors for the stack.

            
            

            - *(dict) --* 

              Describes a stack error.

              
              

              - **ErrorCode** *(string) --* 

                The error code.

                
              

              - **ErrorMessage** *(string) --* 

                The error message.

                
          
        
      
    

==========
Paginators
==========


The available paginators are:
