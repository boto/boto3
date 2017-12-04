

**
MQ
**

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: MQ.Client

  A low-level client representing AmazonMQ::

    
    import boto3
    
    client = boto3.client('mq')

  
  These are the available methods:
  
  *   :py:meth:`~MQ.Client.can_paginate`

  
  *   :py:meth:`~MQ.Client.create_broker`

  
  *   :py:meth:`~MQ.Client.create_configuration`

  
  *   :py:meth:`~MQ.Client.create_user`

  
  *   :py:meth:`~MQ.Client.delete_broker`

  
  *   :py:meth:`~MQ.Client.delete_user`

  
  *   :py:meth:`~MQ.Client.describe_broker`

  
  *   :py:meth:`~MQ.Client.describe_configuration`

  
  *   :py:meth:`~MQ.Client.describe_configuration_revision`

  
  *   :py:meth:`~MQ.Client.describe_user`

  
  *   :py:meth:`~MQ.Client.generate_presigned_url`

  
  *   :py:meth:`~MQ.Client.get_paginator`

  
  *   :py:meth:`~MQ.Client.get_waiter`

  
  *   :py:meth:`~MQ.Client.list_brokers`

  
  *   :py:meth:`~MQ.Client.list_configuration_revisions`

  
  *   :py:meth:`~MQ.Client.list_configurations`

  
  *   :py:meth:`~MQ.Client.list_users`

  
  *   :py:meth:`~MQ.Client.reboot_broker`

  
  *   :py:meth:`~MQ.Client.update_broker`

  
  *   :py:meth:`~MQ.Client.update_configuration`

  
  *   :py:meth:`~MQ.Client.update_user`

  

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


  .. py:method:: create_broker(**kwargs)

    Creates a broker. Note: This API is asynchronous.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/CreateBroker>`_    


    **Request Syntax** 
    ::

      response = client.create_broker(
          AutoMinorVersionUpgrade=True|False,
          BrokerName='string',
          Configuration={
              'Id': 'string',
              'Revision': 123
          },
          CreatorRequestId='string',
          DeploymentMode='SINGLE_INSTANCE'|'ACTIVE_STANDBY_MULTI_AZ',
          EngineType='ACTIVEMQ',
          EngineVersion='string',
          HostInstanceType='string',
          MaintenanceWindowStartTime={
              'DayOfWeek': 'MONDAY'|'TUESDAY'|'WEDNESDAY'|'THURSDAY'|'FRIDAY'|'SATURDAY'|'SUNDAY',
              'TimeOfDay': 'string',
              'TimeZone': 'string'
          },
          PubliclyAccessible=True|False,
          SecurityGroups=[
              'string',
          ],
          SubnetIds=[
              'string',
          ],
          Users=[
              {
                  'ConsoleAccess': True|False,
                  'Groups': [
                      'string',
                  ],
                  'Password': 'string',
                  'Username': 'string'
              },
          ]
      )
    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Required. Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions. The automatic upgrades occur during the maintenance window of the broker or after a manual broker reboot.

    
    :type BrokerName: string
    :param BrokerName: Required. The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.

    
    :type Configuration: dict
    :param Configuration: A list of information about the configuration.

    
      - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

      
      - **Revision** *(integer) --* The Universally Unique Identifier (UUID) of the request.

      
    
    :type CreatorRequestId: string
    :param CreatorRequestId: The unique ID that the requester receives for the created broker. Amazon MQ passes your ID with the API action. Note: We recommend using a Universally Unique Identifier (UUID) for the creatorRequestId. You may omit the creatorRequestId if your application doesn't require idempotency.This field is autopopulated if not provided.

    
    :type DeploymentMode: string
    :param DeploymentMode: Required. The deployment mode of the broker. Possible values: SINGLE_INSTANCE, ACTIVE_STANDBY_MULTI_AZ SINGLE_INSTANCE creates a single-instance broker in a single Availability Zone. ACTIVE_STANDBY_MULTI_AZ creates an active/standby broker for high availability.

    
    :type EngineType: string
    :param EngineType: Required. The type of broker engine. Note: Currently, Amazon MQ supports only ACTIVEMQ.

    
    :type EngineVersion: string
    :param EngineVersion: Required. The version of the broker engine. Note: Currently, Amazon MQ supports only 5.15.0.

    
    :type HostInstanceType: string
    :param HostInstanceType: Required. The broker's instance type. Possible values: mq.t2.micro, mq.m4.large

    
    :type MaintenanceWindowStartTime: dict
    :param MaintenanceWindowStartTime: The parameters that determine the WeeklyStartTime.

    
      - **DayOfWeek** *(string) --* Required. The day of the week. Possible values: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY

      
      - **TimeOfDay** *(string) --* Required. The time, in 24-hour format.

      
      - **TimeZone** *(string) --* The time zone, UTC by default, in either the Country/City format, or the UTC offset format.

      
    
    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: Required. Enables connections from applications outside of the VPC that hosts the broker's subnets.

    
    :type SecurityGroups: list
    :param SecurityGroups: Required. The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.

    
      - *(string) --* 

      
  
    :type SubnetIds: list
    :param SubnetIds: Required. The list of groups (2 maximum) that define which subnets and IP ranges the broker can use from different Availability Zones. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ deployment requires two subnets.

    
      - *(string) --* 

      
  
    :type Users: list
    :param Users: Required. The list of ActiveMQ users (persons or applications) who can access queues and topics. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    
      - *(dict) --* An ActiveMQ user associated with the broker.

      
        - **ConsoleAccess** *(boolean) --* Enables access to the the ActiveMQ Web Console for the ActiveMQ user.

        
        - **Groups** *(list) --* The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

        
          - *(string) --* 

          
      
        - **Password** *(string) --* Required. The password of the ActiveMQ user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas.

        
        - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BrokerArn': 'string',
            'BrokerId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.
        

        - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.
    

  .. py:method:: create_configuration(**kwargs)

    Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version). Note: If the configuration name already exists, Amazon MQ doesn't create a configuration.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/CreateConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.create_configuration(
          EngineType='ACTIVEMQ',
          EngineVersion='string',
          Name='string'
      )
    :type EngineType: string
    :param EngineType: Required. The type of broker engine. Note: Currently, Amazon MQ supports only ACTIVEMQ.

    
    :type EngineVersion: string
    :param EngineVersion: Required. The version of the broker engine. Note: Currently, Amazon MQ supports only 5.15.0.

    
    :type Name: string
    :param Name: Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'Id': 'string',
            'LatestRevision': {
                'Description': 'string',
                'Revision': 123
            },
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **Arn** *(string) --* Required. The Amazon Resource Name (ARN) of the configuration.
        

        - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
        

        - **LatestRevision** *(dict) --* The latest revision of the configuration.
          

          - **Description** *(string) --* The description of the configuration revision.
          

          - **Revision** *(integer) --* Required. The revision of the configuration.
      
        

        - **Name** *(string) --* Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
    

  .. py:method:: create_user(**kwargs)

    Creates an ActiveMQ user.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/CreateUser>`_    


    **Request Syntax** 
    ::

      response = client.create_user(
          BrokerId='string',
          ConsoleAccess=True|False,
          Groups=[
              'string',
          ],
          Password='string',
          Username='string'
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The unique ID that Amazon MQ generates for the broker.

    
    :type ConsoleAccess: boolean
    :param ConsoleAccess: Enables access to the the ActiveMQ Web Console for the ActiveMQ user.

    
    :type Groups: list
    :param Groups: The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    
      - *(string) --* 

      
  
    :type Password: string
    :param Password: Required. The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas.

    
    :type Username: string
    :param Username: **[REQUIRED]** The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
    

  .. py:method:: delete_broker(**kwargs)

    Deletes a broker. Note: This API is asynchronous.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/DeleteBroker>`_    


    **Request Syntax** 
    ::

      response = client.delete_broker(
          BrokerId='string'
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BrokerId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.
    

  .. py:method:: delete_user(**kwargs)

    Deletes an ActiveMQ user.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/DeleteUser>`_    


    **Request Syntax** 
    ::

      response = client.delete_user(
          BrokerId='string',
          Username='string'
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The unique ID that Amazon MQ generates for the broker.

    
    :type Username: string
    :param Username: **[REQUIRED]** The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
    

  .. py:method:: describe_broker(**kwargs)

    Returns information about the specified broker.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/DescribeBroker>`_    


    **Request Syntax** 
    ::

      response = client.describe_broker(
          BrokerId='string'
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AutoMinorVersionUpgrade': True|False,
            'BrokerArn': 'string',
            'BrokerId': 'string',
            'BrokerInstances': [
                {
                    'ConsoleURL': 'string',
                    'Endpoints': [
                        'string',
                    ]
                },
            ],
            'BrokerName': 'string',
            'BrokerState': 'CREATION_IN_PROGRESS'|'CREATION_FAILED'|'DELETION_IN_PROGRESS'|'RUNNING'|'REBOOT_IN_PROGRESS',
            'Configurations': {
                'Current': {
                    'Id': 'string',
                    'Revision': 123
                },
                'History': [
                    {
                        'Id': 'string',
                        'Revision': 123
                    },
                ],
                'Pending': {
                    'Id': 'string',
                    'Revision': 123
                }
            },
            'DeploymentMode': 'SINGLE_INSTANCE'|'ACTIVE_STANDBY_MULTI_AZ',
            'EngineType': 'ACTIVEMQ',
            'EngineVersion': 'string',
            'HostInstanceType': 'string',
            'MaintenanceWindowStartTime': {
                'DayOfWeek': 'MONDAY'|'TUESDAY'|'WEDNESDAY'|'THURSDAY'|'FRIDAY'|'SATURDAY'|'SUNDAY',
                'TimeOfDay': 'string',
                'TimeZone': 'string'
            },
            'PubliclyAccessible': True|False,
            'SecurityGroups': [
                'string',
            ],
            'SubnetIds': [
                'string',
            ],
            'Users': [
                {
                    'PendingChange': 'CREATE'|'UPDATE'|'DELETE',
                    'Username': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **AutoMinorVersionUpgrade** *(boolean) --* Required. Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions. The automatic upgrades occur during the maintenance window of the broker or after a manual broker reboot.
        

        - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.
        

        - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.
        

        - **BrokerInstances** *(list) --* A list of information about allocated brokers.
          

          - *(dict) --* Returns information about all brokers.
            

            - **ConsoleURL** *(string) --* The URL of the broker's ActiveMQ Web Console.
            

            - **Endpoints** *(list) --* The broker's wire-level protocol endpoints.
              

              - *(string) --* 
          
        
      
        

        - **BrokerName** *(string) --* The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.
        

        - **BrokerState** *(string) --* The status of the broker. Possible values: CREATION_IN_PROGRESS, CREATION_FAILED, DELETION_IN_PROGRESS, RUNNING, REBOOT_IN_PROGRESS
        

        - **Configurations** *(dict) --* The list of all revisions for the specified configuration.
          

          - **Current** *(dict) --* The current configuration of the broker.
            

            - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
            

            - **Revision** *(integer) --* The Universally Unique Identifier (UUID) of the request.
        
          

          - **History** *(list) --* The history of configurations applied to the broker.
            

            - *(dict) --* A list of information about the configuration.
              

              - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
              

              - **Revision** *(integer) --* The Universally Unique Identifier (UUID) of the request.
          
        
          

          - **Pending** *(dict) --* The pending configuration of the broker.
            

            - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
            

            - **Revision** *(integer) --* The Universally Unique Identifier (UUID) of the request.
        
      
        

        - **DeploymentMode** *(string) --* Required. The deployment mode of the broker. Possible values: SINGLE_INSTANCE, ACTIVE_STANDBY_MULTI_AZ SINGLE_INSTANCE creates a single-instance broker in a single Availability Zone. ACTIVE_STANDBY_MULTI_AZ creates an active/standby broker for high availability.
        

        - **EngineType** *(string) --* Required. The type of broker engine. Note: Currently, Amazon MQ supports only ACTIVEMQ.
        

        - **EngineVersion** *(string) --* The version of the broker engine. Note: Currently, Amazon MQ supports only 5.15.0.
        

        - **HostInstanceType** *(string) --* The broker's instance type. Possible values: mq.t2.micro, mq.m4.large
        

        - **MaintenanceWindowStartTime** *(dict) --* The parameters that determine the WeeklyStartTime.
          

          - **DayOfWeek** *(string) --* Required. The day of the week. Possible values: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
          

          - **TimeOfDay** *(string) --* Required. The time, in 24-hour format.
          

          - **TimeZone** *(string) --* The time zone, UTC by default, in either the Country/City format, or the UTC offset format.
      
        

        - **PubliclyAccessible** *(boolean) --* Required. Enables connections from applications outside of the VPC that hosts the broker's subnets.
        

        - **SecurityGroups** *(list) --* Required. The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.
          

          - *(string) --* 
      
        

        - **SubnetIds** *(list) --* The list of groups (2 maximum) that define which subnets and IP ranges the broker can use from different Availability Zones. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ deployment requires two subnets.
          

          - *(string) --* 
      
        

        - **Users** *(list) --* The list of all ActiveMQ usernames for the specified broker.
          

          - *(dict) --* Returns a list of all ActiveMQ users.
            

            - **PendingChange** *(string) --* The type of change pending for the ActiveMQ user. Possible values: CREATE, UPDATE, DELETE
            

            - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
        
      
    

  .. py:method:: describe_configuration(**kwargs)

    Returns information about the specified configuration.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/DescribeConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.describe_configuration(
          ConfigurationId='string'
      )
    :type ConfigurationId: string
    :param ConfigurationId: **[REQUIRED]** The unique ID that Amazon MQ generates for the configuration.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'Description': 'string',
            'EngineType': 'ACTIVEMQ',
            'EngineVersion': 'string',
            'Id': 'string',
            'LatestRevision': {
                'Description': 'string',
                'Revision': 123
            },
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **Arn** *(string) --* Required. The ARN of the configuration.
        

        - **Description** *(string) --* Required. The description of the configuration.
        

        - **EngineType** *(string) --* Required. The type of broker engine. Note: Currently, Amazon MQ supports only ACTIVEMQ.
        

        - **EngineVersion** *(string) --* Required. The version of the broker engine.
        

        - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
        

        - **LatestRevision** *(dict) --* Required. The latest revision of the configuration.
          

          - **Description** *(string) --* The description of the configuration revision.
          

          - **Revision** *(integer) --* Required. The revision of the configuration.
      
        

        - **Name** *(string) --* Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
    

  .. py:method:: describe_configuration_revision(**kwargs)

    Returns the specified configuration revision for the specified configuration.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/DescribeConfigurationRevision>`_    


    **Request Syntax** 
    ::

      response = client.describe_configuration_revision(
          ConfigurationId='string',
          ConfigurationRevision='string'
      )
    :type ConfigurationId: string
    :param ConfigurationId: **[REQUIRED]** The unique ID that Amazon MQ generates for the configuration.

    
    :type ConfigurationRevision: string
    :param ConfigurationRevision: **[REQUIRED]** The revision of the configuration.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigurationId': 'string',
            'Data': 'string',
            'Description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **ConfigurationId** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
        

        - **Data** *(string) --* Required. The base64-encoded XML configuration.
        

        - **Description** *(string) --* The description of the configuration.
    

  .. py:method:: describe_user(**kwargs)

    Returns information about an ActiveMQ user.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/DescribeUser>`_    


    **Request Syntax** 
    ::

      response = client.describe_user(
          BrokerId='string',
          Username='string'
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The unique ID that Amazon MQ generates for the broker.

    
    :type Username: string
    :param Username: **[REQUIRED]** The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BrokerId': 'string',
            'ConsoleAccess': True|False,
            'Groups': [
                'string',
            ],
            'Pending': {
                'ConsoleAccess': True|False,
                'Groups': [
                    'string',
                ],
                'PendingChange': 'CREATE'|'UPDATE'|'DELETE'
            },
            'Username': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **BrokerId** *(string) --* Required. The unique ID that Amazon MQ generates for the broker.
        

        - **ConsoleAccess** *(boolean) --* Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
        

        - **Groups** *(list) --* The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
          

          - *(string) --* 
      
        

        - **Pending** *(dict) --* The status of the changes pending for the ActiveMQ user.
          

          - **ConsoleAccess** *(boolean) --* Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
          

          - **Groups** *(list) --* The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
            

            - *(string) --* 
        
          

          - **PendingChange** *(string) --* Required. The type of change pending for the ActiveMQ user. Possible values: CREATE, UPDATE, DELETE
      
        

        - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    

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

        


  .. py:method:: list_brokers(**kwargs)

    Returns a list of all brokers.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/ListBrokers>`_    


    **Request Syntax** 
    ::

      response = client.list_brokers(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.

    
    :type NextToken: string
    :param NextToken: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BrokerSummaries': [
                {
                    'BrokerArn': 'string',
                    'BrokerId': 'string',
                    'BrokerName': 'string',
                    'BrokerState': 'CREATION_IN_PROGRESS'|'CREATION_FAILED'|'DELETION_IN_PROGRESS'|'RUNNING'|'REBOOT_IN_PROGRESS',
                    'DeploymentMode': 'SINGLE_INSTANCE'|'ACTIVE_STANDBY_MULTI_AZ',
                    'HostInstanceType': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **BrokerSummaries** *(list) --* A list of information about all brokers.
          

          - *(dict) --* The Amazon Resource Name (ARN) of the broker.
            

            - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.
            

            - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.
            

            - **BrokerName** *(string) --* The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.
            

            - **BrokerState** *(string) --* The status of the broker. Possible values: CREATION_IN_PROGRESS, CREATION_FAILED, DELETION_IN_PROGRESS, RUNNING, REBOOT_IN_PROGRESS
            

            - **DeploymentMode** *(string) --* Required. The deployment mode of the broker. Possible values: SINGLE_INSTANCE, ACTIVE_STANDBY_MULTI_AZ SINGLE_INSTANCE creates a single-instance broker in a single Availability Zone. ACTIVE_STANDBY_MULTI_AZ creates an active/standby broker for high availability.
            

            - **HostInstanceType** *(string) --* The broker's instance type. Possible values: mq.t2.micro, mq.m4.large
        
      
        

        - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    

  .. py:method:: list_configuration_revisions(**kwargs)

    Returns a list of all revisions for the specified configuration.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/ListConfigurationRevisions>`_    


    **Request Syntax** 
    ::

      response = client.list_configuration_revisions(
          ConfigurationId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type ConfigurationId: string
    :param ConfigurationId: **[REQUIRED]** The unique ID that Amazon MQ generates for the configuration.

    
    :type MaxResults: integer
    :param MaxResults: The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.

    
    :type NextToken: string
    :param NextToken: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigurationId': 'string',
            'MaxResults': 123,
            'NextToken': 'string',
            'Revisions': [
                {
                    'Description': 'string',
                    'Revision': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **ConfigurationId** *(string) --* The unique ID that Amazon MQ generates for the configuration.
        

        - **MaxResults** *(integer) --* The maximum number of configuration revisions that can be returned per page (20 by default). This value must be an integer from 5 to 100.
        

        - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
        

        - **Revisions** *(list) --* The list of all revisions for the specified configuration.
          

          - *(dict) --* Returns information about the specified configuration revision.
            

            - **Description** *(string) --* The description of the configuration revision.
            

            - **Revision** *(integer) --* Required. The revision of the configuration.
        
      
    

  .. py:method:: list_configurations(**kwargs)

    Returns a list of all configurations.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/ListConfigurations>`_    


    **Request Syntax** 
    ::

      response = client.list_configurations(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.

    
    :type NextToken: string
    :param NextToken: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Configurations': [
                {
                    'Arn': 'string',
                    'Description': 'string',
                    'EngineType': 'ACTIVEMQ',
                    'EngineVersion': 'string',
                    'Id': 'string',
                    'LatestRevision': {
                        'Description': 'string',
                        'Revision': 123
                    },
                    'Name': 'string'
                },
            ],
            'MaxResults': 123,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **Configurations** *(list) --* The list of all revisions for the specified configuration.
          

          - *(dict) --* Returns information about all configurations.
            

            - **Arn** *(string) --* Required. The ARN of the configuration.
            

            - **Description** *(string) --* Required. The description of the configuration.
            

            - **EngineType** *(string) --* Required. The type of broker engine. Note: Currently, Amazon MQ supports only ACTIVEMQ.
            

            - **EngineVersion** *(string) --* Required. The version of the broker engine.
            

            - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
            

            - **LatestRevision** *(dict) --* Required. The latest revision of the configuration.
              

              - **Description** *(string) --* The description of the configuration revision.
              

              - **Revision** *(integer) --* Required. The revision of the configuration.
          
            

            - **Name** *(string) --* Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
        
      
        

        - **MaxResults** *(integer) --* The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
        

        - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    

  .. py:method:: list_users(**kwargs)

    Returns a list of all ActiveMQ users.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/ListUsers>`_    


    **Request Syntax** 
    ::

      response = client.list_users(
          BrokerId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The unique ID that Amazon MQ generates for the broker.

    
    :type MaxResults: integer
    :param MaxResults: The maximum number of ActiveMQ users that can be returned per page (20 by default). This value must be an integer from 5 to 100.

    
    :type NextToken: string
    :param NextToken: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BrokerId': 'string',
            'MaxResults': 123,
            'NextToken': 'string',
            'Users': [
                {
                    'PendingChange': 'CREATE'|'UPDATE'|'DELETE',
                    'Username': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **BrokerId** *(string) --* Required. The unique ID that Amazon MQ generates for the broker.
        

        - **MaxResults** *(integer) --* Required. The maximum number of ActiveMQ users that can be returned per page (20 by default). This value must be an integer from 5 to 100.
        

        - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
        

        - **Users** *(list) --* Required. The list of all ActiveMQ usernames for the specified broker.
          

          - *(dict) --* Returns a list of all ActiveMQ users.
            

            - **PendingChange** *(string) --* The type of change pending for the ActiveMQ user. Possible values: CREATE, UPDATE, DELETE
            

            - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
        
      
    

  .. py:method:: reboot_broker(**kwargs)

    Reboots a broker. Note: This API is asynchronous.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/RebootBroker>`_    


    **Request Syntax** 
    ::

      response = client.reboot_broker(
          BrokerId='string'
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The unique ID that Amazon MQ generates for the broker.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
    

  .. py:method:: update_broker(**kwargs)

    Adds a pending configuration change to a broker.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/UpdateBroker>`_    


    **Request Syntax** 
    ::

      response = client.update_broker(
          BrokerId='string',
          Configuration={
              'Id': 'string',
              'Revision': 123
          }
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.

    
    :type Configuration: dict
    :param Configuration: A list of information about the configuration.

    
      - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

      
      - **Revision** *(integer) --* The Universally Unique Identifier (UUID) of the request.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BrokerId': 'string',
            'Configuration': {
                'Id': 'string',
                'Revision': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **BrokerId** *(string) --* Required. The unique ID that Amazon MQ generates for the broker.
        

        - **Configuration** *(dict) --* The ID of the updated configuration.
          

          - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
          

          - **Revision** *(integer) --* The Universally Unique Identifier (UUID) of the request.
      
    

  .. py:method:: update_configuration(**kwargs)

    Updates the specified configuration.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/UpdateConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.update_configuration(
          ConfigurationId='string',
          Data='string',
          Description='string'
      )
    :type ConfigurationId: string
    :param ConfigurationId: **[REQUIRED]** The unique ID that Amazon MQ generates for the configuration.

    
    :type Data: string
    :param Data: Required. The base64-encoded XML configuration.

    
    :type Description: string
    :param Description: The description of the configuration.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'Id': 'string',
            'LatestRevision': {
                'Description': 'string',
                'Revision': 123
            },
            'Name': 'string',
            'Warnings': [
                {
                    'AttributeName': 'string',
                    'ElementName': 'string',
                    'Reason': 'DISALLOWED_ELEMENT_REMOVED'|'DISALLOWED_ATTRIBUTE_REMOVED'|'INVALID_ATTRIBUTE_VALUE_REMOVED'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
        

        - **Arn** *(string) --* Required. The Amazon Resource Name (ARN) of the configuration.
        

        - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.
        

        - **LatestRevision** *(dict) --* The latest revision of the configuration.
          

          - **Description** *(string) --* The description of the configuration revision.
          

          - **Revision** *(integer) --* Required. The revision of the configuration.
      
        

        - **Name** *(string) --* Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
        

        - **Warnings** *(list) --* The list of the first 20 warnings about the configuration XML elements or attributes that were sanitized.
          

          - *(dict) --* Returns information about the XML element or attribute that was sanitized in the configuration.
            

            - **AttributeName** *(string) --* The name of the XML attribute that has been sanitized.
            

            - **ElementName** *(string) --* The name of the XML element that has been sanitized.
            

            - **Reason** *(string) --* Required. The reason for which the XML elements or attributes were sanitized. Possible values: DISALLOWED_ELEMENT_REMOVED, DISALLOWED_ATTRIBUTE_REMOVED, INVALID_ATTRIBUTE_VALUE_REMOVED DISALLOWED_ELEMENT_REMOVED shows that the provided element isn't allowed and has been removed. DISALLOWED_ATTRIBUTE_REMOVED shows that the provided attribute isn't allowed and has been removed. INVALID_ATTRIBUTE_VALUE_REMOVED shows that the provided value for the attribute isn't allowed and has been removed.
        
      
    

  .. py:method:: update_user(**kwargs)

    Updates the information for an ActiveMQ user.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/UpdateUser>`_    


    **Request Syntax** 
    ::

      response = client.update_user(
          BrokerId='string',
          ConsoleAccess=True|False,
          Groups=[
              'string',
          ],
          Password='string',
          Username='string'
      )
    :type BrokerId: string
    :param BrokerId: **[REQUIRED]** The unique ID that Amazon MQ generates for the broker.

    
    :type ConsoleAccess: boolean
    :param ConsoleAccess: Enables access to the the ActiveMQ Web Console for the ActiveMQ user.

    
    :type Groups: list
    :param Groups: The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    
      - *(string) --* 

      
  
    :type Password: string
    :param Password: The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas.

    
    :type Username: string
    :param Username: **[REQUIRED]** Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* HTTP Status Code 200: OK.
    