

**********
DeviceFarm
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: DeviceFarm.Client

  A low-level client representing AWS Device Farm::

    
    import boto3
    
    client = boto3.client('devicefarm')

  
  These are the available methods:
  
  *   :py:meth:`~DeviceFarm.Client.can_paginate`

  
  *   :py:meth:`~DeviceFarm.Client.create_device_pool`

  
  *   :py:meth:`~DeviceFarm.Client.create_network_profile`

  
  *   :py:meth:`~DeviceFarm.Client.create_project`

  
  *   :py:meth:`~DeviceFarm.Client.create_remote_access_session`

  
  *   :py:meth:`~DeviceFarm.Client.create_upload`

  
  *   :py:meth:`~DeviceFarm.Client.delete_device_pool`

  
  *   :py:meth:`~DeviceFarm.Client.delete_network_profile`

  
  *   :py:meth:`~DeviceFarm.Client.delete_project`

  
  *   :py:meth:`~DeviceFarm.Client.delete_remote_access_session`

  
  *   :py:meth:`~DeviceFarm.Client.delete_run`

  
  *   :py:meth:`~DeviceFarm.Client.delete_upload`

  
  *   :py:meth:`~DeviceFarm.Client.generate_presigned_url`

  
  *   :py:meth:`~DeviceFarm.Client.get_account_settings`

  
  *   :py:meth:`~DeviceFarm.Client.get_device`

  
  *   :py:meth:`~DeviceFarm.Client.get_device_pool`

  
  *   :py:meth:`~DeviceFarm.Client.get_device_pool_compatibility`

  
  *   :py:meth:`~DeviceFarm.Client.get_job`

  
  *   :py:meth:`~DeviceFarm.Client.get_network_profile`

  
  *   :py:meth:`~DeviceFarm.Client.get_offering_status`

  
  *   :py:meth:`~DeviceFarm.Client.get_paginator`

  
  *   :py:meth:`~DeviceFarm.Client.get_project`

  
  *   :py:meth:`~DeviceFarm.Client.get_remote_access_session`

  
  *   :py:meth:`~DeviceFarm.Client.get_run`

  
  *   :py:meth:`~DeviceFarm.Client.get_suite`

  
  *   :py:meth:`~DeviceFarm.Client.get_test`

  
  *   :py:meth:`~DeviceFarm.Client.get_upload`

  
  *   :py:meth:`~DeviceFarm.Client.get_waiter`

  
  *   :py:meth:`~DeviceFarm.Client.install_to_remote_access_session`

  
  *   :py:meth:`~DeviceFarm.Client.list_artifacts`

  
  *   :py:meth:`~DeviceFarm.Client.list_device_pools`

  
  *   :py:meth:`~DeviceFarm.Client.list_devices`

  
  *   :py:meth:`~DeviceFarm.Client.list_jobs`

  
  *   :py:meth:`~DeviceFarm.Client.list_network_profiles`

  
  *   :py:meth:`~DeviceFarm.Client.list_offering_promotions`

  
  *   :py:meth:`~DeviceFarm.Client.list_offering_transactions`

  
  *   :py:meth:`~DeviceFarm.Client.list_offerings`

  
  *   :py:meth:`~DeviceFarm.Client.list_projects`

  
  *   :py:meth:`~DeviceFarm.Client.list_remote_access_sessions`

  
  *   :py:meth:`~DeviceFarm.Client.list_runs`

  
  *   :py:meth:`~DeviceFarm.Client.list_samples`

  
  *   :py:meth:`~DeviceFarm.Client.list_suites`

  
  *   :py:meth:`~DeviceFarm.Client.list_tests`

  
  *   :py:meth:`~DeviceFarm.Client.list_unique_problems`

  
  *   :py:meth:`~DeviceFarm.Client.list_uploads`

  
  *   :py:meth:`~DeviceFarm.Client.purchase_offering`

  
  *   :py:meth:`~DeviceFarm.Client.renew_offering`

  
  *   :py:meth:`~DeviceFarm.Client.schedule_run`

  
  *   :py:meth:`~DeviceFarm.Client.stop_remote_access_session`

  
  *   :py:meth:`~DeviceFarm.Client.stop_run`

  
  *   :py:meth:`~DeviceFarm.Client.update_device_pool`

  
  *   :py:meth:`~DeviceFarm.Client.update_network_profile`

  
  *   :py:meth:`~DeviceFarm.Client.update_project`

  

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


  .. py:method:: create_device_pool(**kwargs)

    

    Creates a device pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateDevicePool>`_    


    **Request Syntax** 
    ::

      response = client.create_device_pool(
          projectArn='string',
          name='string',
          description='string',
          rules=[
              {
                  'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION',
                  'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                  'value': 'string'
              },
          ]
      )
    :type projectArn: string
    :param projectArn: **[REQUIRED]** 

      The ARN of the project for the device pool.

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      The device pool's name.

      

    
    :type description: string
    :param description: 

      The device pool's description.

      

    
    :type rules: list
    :param rules: **[REQUIRED]** 

      The device pool's rules.

      

    
      - *(dict) --* 

        Represents a condition for a device pool.

        

      
        - **attribute** *(string) --* 

          The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .

           

          Allowed values include:

           

           
          * ARN: The ARN. 
           
          * FORM_FACTOR: The form factor (for example, phone or tablet). 
           
          * MANUFACTURER: The manufacturer. 
           
          * PLATFORM: The platform (for example, Android or iOS). 
           
          * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
           
          * APPIUM_VERSION: The Appium version for the test. 
           

          

        
        - **operator** *(string) --* 

          The rule's operator.

           

           
          * EQUALS: The equals operator. 
           
          * GREATER_THAN: The greater-than operator. 
           
          * IN: The in operator. 
           
          * LESS_THAN: The less-than operator. 
           
          * NOT_IN: The not-in operator. 
           
          * CONTAINS: The contains operator. 
           

          

        
        - **value** *(string) --* 

          The rule's value.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'devicePool': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'rules': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION',
                        'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                        'value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a create device pool request.

        
        

        - **devicePool** *(dict) --* 

          The newly created device pool.

          
          

          - **arn** *(string) --* 

            The device pool's ARN.

            
          

          - **name** *(string) --* 

            The device pool's name.

            
          

          - **description** *(string) --* 

            The device pool's description.

            
          

          - **type** *(string) --* 

            The device pool's type.

             

            Allowed values include:

             

             
            * CURATED: A device pool that is created and managed by AWS Device Farm. 
             
            * PRIVATE: A device pool that is created and managed by the device pool developer. 
             

            
          

          - **rules** *(list) --* 

            Information about the device pool's rules.

            
            

            - *(dict) --* 

              Represents a condition for a device pool.

              
              

              - **attribute** *(string) --* 

                The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .

                 

                Allowed values include:

                 

                 
                * ARN: The ARN. 
                 
                * FORM_FACTOR: The form factor (for example, phone or tablet). 
                 
                * MANUFACTURER: The manufacturer. 
                 
                * PLATFORM: The platform (for example, Android or iOS). 
                 
                * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                 
                * APPIUM_VERSION: The Appium version for the test. 
                 

                
              

              - **operator** *(string) --* 

                The rule's operator.

                 

                 
                * EQUALS: The equals operator. 
                 
                * GREATER_THAN: The greater-than operator. 
                 
                * IN: The in operator. 
                 
                * LESS_THAN: The less-than operator. 
                 
                * NOT_IN: The not-in operator. 
                 
                * CONTAINS: The contains operator. 
                 

                
              

              - **value** *(string) --* 

                The rule's value.

                
          
        
      
    

    **Examples** 

    The following example creates a new device pool named MyDevicePool inside an existing project.
    ::

      response = client.create_device_pool(
          # A device pool contains related devices, such as devices that run only on Android or that run only on iOS.
          name='MyDevicePool',
          description='My Android devices',
          # You can get the project ARN by using the list-projects CLI command.
          projectArn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
          rules=[
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'devicePool': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_network_profile(**kwargs)

    

    Creates a network profile.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateNetworkProfile>`_    


    **Request Syntax** 
    ::

      response = client.create_network_profile(
          projectArn='string',
          name='string',
          description='string',
          type='CURATED'|'PRIVATE',
          uplinkBandwidthBits=123,
          downlinkBandwidthBits=123,
          uplinkDelayMs=123,
          downlinkDelayMs=123,
          uplinkJitterMs=123,
          downlinkJitterMs=123,
          uplinkLossPercent=123,
          downlinkLossPercent=123
      )
    :type projectArn: string
    :param projectArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to create a network profile.

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      The name you wish to specify for the new network profile.

      

    
    :type description: string
    :param description: 

      The description of the network profile.

      

    
    :type type: string
    :param type: 

      The type of network profile you wish to create. Valid values are listed below.

      

    
    :type uplinkBandwidthBits: integer
    :param uplinkBandwidthBits: 

      The data throughput rate in bits per second, as an integer from 0 to 104857600.

      

    
    :type downlinkBandwidthBits: integer
    :param downlinkBandwidthBits: 

      The data throughput rate in bits per second, as an integer from 0 to 104857600.

      

    
    :type uplinkDelayMs: integer
    :param uplinkDelayMs: 

      Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

      

    
    :type downlinkDelayMs: integer
    :param downlinkDelayMs: 

      Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

      

    
    :type uplinkJitterMs: integer
    :param uplinkJitterMs: 

      Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

      

    
    :type downlinkJitterMs: integer
    :param downlinkJitterMs: 

      Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

      

    
    :type uplinkLossPercent: integer
    :param uplinkLossPercent: 

      Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

      

    
    :type downlinkLossPercent: integer
    :param downlinkLossPercent: 

      Proportion of received packets that fail to arrive from 0 to 100 percent.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **networkProfile** *(dict) --* 

          The network profile that is returned by the create network profile request.

          
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the network profile.

            
          

          - **name** *(string) --* 

            The name of the network profile.

            
          

          - **description** *(string) --* 

            The description of the network profile.

            
          

          - **type** *(string) --* 

            The type of network profile. Valid values are listed below.

            
          

          - **uplinkBandwidthBits** *(integer) --* 

            The data throughput rate in bits per second, as an integer from 0 to 104857600.

            
          

          - **downlinkBandwidthBits** *(integer) --* 

            The data throughput rate in bits per second, as an integer from 0 to 104857600.

            
          

          - **uplinkDelayMs** *(integer) --* 

            Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

            
          

          - **downlinkDelayMs** *(integer) --* 

            Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

            
          

          - **uplinkJitterMs** *(integer) --* 

            Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

            
          

          - **downlinkJitterMs** *(integer) --* 

            Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

            
          

          - **uplinkLossPercent** *(integer) --* 

            Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

            
          

          - **downlinkLossPercent** *(integer) --* 

            Proportion of received packets that fail to arrive from 0 to 100 percent.

            
      
    

  .. py:method:: create_project(**kwargs)

    

    Creates a new project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateProject>`_    


    **Request Syntax** 
    ::

      response = client.create_project(
          name='string',
          defaultJobTimeoutMinutes=123
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The project's name.

      

    
    :type defaultJobTimeoutMinutes: integer
    :param defaultJobTimeoutMinutes: 

      Sets the execution timeout value (in minutes) for a project. All test runs in this project will use the specified execution timeout value unless overridden when scheduling a run.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'project': {
                'arn': 'string',
                'name': 'string',
                'defaultJobTimeoutMinutes': 123,
                'created': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a create project request.

        
        

        - **project** *(dict) --* 

          The newly created project.

          
          

          - **arn** *(string) --* 

            The project's ARN.

            
          

          - **name** *(string) --* 

            The project's name.

            
          

          - **defaultJobTimeoutMinutes** *(integer) --* 

            The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.

            
          

          - **created** *(datetime) --* 

            When the project was created.

            
      
    

    **Examples** 

    The following example creates a new project named MyProject.
    ::

      response = client.create_project(
          # A project in Device Farm is a workspace that contains test runs. A run is a test of a single app against one or more devices.
          name='MyProject',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'project': {
              'name': 'MyProject',
              'arn': 'arn:aws:devicefarm:us-west-2:183774035805:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE',
              'created': datetime(2016, 8, 31, 9, 28, 59, 2, 244, 1),
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_remote_access_session(**kwargs)

    

    Specifies and starts a remote access session.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateRemoteAccessSession>`_    


    **Request Syntax** 
    ::

      response = client.create_remote_access_session(
          projectArn='string',
          deviceArn='string',
          sshPublicKey='string',
          remoteDebugEnabled=True|False,
          name='string',
          clientId='string',
          configuration={
              'billingMethod': 'METERED'|'UNMETERED'
          }
      )
    :type projectArn: string
    :param projectArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to create a remote access session.

      

    
    :type deviceArn: string
    :param deviceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the device for which you want to create a remote access session.

      

    
    :type sshPublicKey: string
    :param sshPublicKey: 

      The public key of the ``ssh`` key pair you want to use for connecting to remote devices in your remote debugging session. This is only required if ``remoteDebugEnabled`` is set to ``true`` .

      

    
    :type remoteDebugEnabled: boolean
    :param remoteDebugEnabled: 

      Set to ``true`` if you want to access devices remotely for debugging in your remote access session.

      

    
    :type name: string
    :param name: 

      The name of the remote access session that you wish to create.

      

    
    :type clientId: string
    :param clientId: 

      Unique identifier for the client. If you want access to multiple devices on the same client, you should pass the same ``clientId`` value in each call to ``CreateRemoteAccessSession`` . This is required only if ``remoteDebugEnabled`` is set to true ``true`` .

      

    
    :type configuration: dict
    :param configuration: 

      The configuration information for the remote access session request.

      

    
      - **billingMethod** *(string) --* 

        Returns the billing method for purposes of configuring a remote access session.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'remoteAccessSession': {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'message': 'string',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
                'remoteDebugEnabled': True|False,
                'hostAddress': 'string',
                'clientId': 'string',
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'endpoint': 'string',
                'deviceUdid': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the server response from a request to create a remote access session.

        
        

        - **remoteAccessSession** *(dict) --* 

          A container that describes the remote access session when the request to create a remote access session is sent.

          
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the remote access session.

            
          

          - **name** *(string) --* 

            The name of the remote access session.

            
          

          - **created** *(datetime) --* 

            The date and time the remote access session was created.

            
          

          - **status** *(string) --* 

            The status of the remote access session. Can be any of the following:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The result of the remote access session. Can be any of the following:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **message** *(string) --* 

            A message about the remote access session.

            
          

          - **started** *(datetime) --* 

            The date and time the remote access session was started.

            
          

          - **stopped** *(datetime) --* 

            The date and time the remote access session was stopped.

            
          

          - **device** *(dict) --* 

            The device (phone or tablet) used in the remote access session.

            
            

            - **arn** *(string) --* 

              The device's ARN.

              
            

            - **name** *(string) --* 

              The device's display name.

              
            

            - **manufacturer** *(string) --* 

              The device's manufacturer name.

              
            

            - **model** *(string) --* 

              The device's model name.

              
            

            - **formFactor** *(string) --* 

              The device's form factor.

               

              Allowed values include:

               

               
              * PHONE: The phone form factor. 
               
              * TABLET: The tablet form factor. 
               

              
            

            - **platform** *(string) --* 

              The device's platform.

               

              Allowed values include:

               

               
              * ANDROID: The Android platform. 
               
              * IOS: The iOS platform. 
               

              
            

            - **os** *(string) --* 

              The device's operating system type.

              
            

            - **cpu** *(dict) --* 

              Information about the device's CPU.

              
              

              - **frequency** *(string) --* 

                The CPU's frequency.

                
              

              - **architecture** *(string) --* 

                The CPU's architecture, for example x86 or ARM.

                
              

              - **clock** *(float) --* 

                The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                
          
            

            - **resolution** *(dict) --* 

              The resolution of the device.

              
              

              - **width** *(integer) --* 

                The screen resolution's width, expressed in pixels.

                
              

              - **height** *(integer) --* 

                The screen resolution's height, expressed in pixels.

                
          
            

            - **heapSize** *(integer) --* 

              The device's heap size, expressed in bytes.

              
            

            - **memory** *(integer) --* 

              The device's total memory size, expressed in bytes.

              
            

            - **image** *(string) --* 

              The device's image name.

              
            

            - **carrier** *(string) --* 

              The device's carrier.

              
            

            - **radio** *(string) --* 

              The device's radio.

              
            

            - **remoteAccessEnabled** *(boolean) --* 

              Specifies whether remote access has been enabled for the specified device.

              
            

            - **remoteDebugEnabled** *(boolean) --* 

              This flag is set to ``true`` if remote debugging is enabled for the device.

              
            

            - **fleetType** *(string) --* 

              The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

              
            

            - **fleetName** *(string) --* 

              The name of the fleet to which this device belongs.

              
        
          

          - **remoteDebugEnabled** *(boolean) --* 

            This flag is set to ``true`` if remote debugging is enabled for the remote access session.

            
          

          - **hostAddress** *(string) --* 

            IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.

            
          

          - **clientId** *(string) --* 

            Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.

            
          

          - **billingMethod** *(string) --* 

            The billing method of the remote access session. Possible values include ``METERED`` or ``UNMETERED`` . For more information about metered devices, see `AWS Device Farm terminology <http://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology>`__ ."

            
          

          - **deviceMinutes** *(dict) --* 

            The number of minutes a device is used in a remote access sesssion (including setup and teardown minutes).

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
          

          - **endpoint** *(string) --* 

            The endpoint for the remote access sesssion.

            
          

          - **deviceUdid** *(string) --* 

            Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.

            
      
    

    **Examples** 

    The following example creates a remote access session named MySession.
    ::

      response = client.create_remote_access_session(
          name='MySession',
          configuration={
              'billingMethod': 'METERED',
          },
          # You can get the device ARN by using the list-devices CLI command.
          deviceArn='arn:aws:devicefarm:us-west-2::device:123EXAMPLE',
          # You can get the project ARN by using the list-projects CLI command.
          projectArn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'remoteAccessSession': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_upload(**kwargs)

    

    Uploads an app or test scripts.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateUpload>`_    


    **Request Syntax** 
    ::

      response = client.create_upload(
          projectArn='string',
          name='string',
          type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
          contentType='string'
      )
    :type projectArn: string
    :param projectArn: **[REQUIRED]** 

      The ARN of the project for the upload.

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      The upload's file name. The name should not contain the '/' character. If uploading an iOS app, the file name needs to end with the ``.ipa`` extension. If uploading an Android app, the file name needs to end with the ``.apk`` extension. For all others, the file name must end with the ``.zip`` file extension.

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      The upload's upload type.

       

      Must be one of the following values:

       

       
      * ANDROID_APP: An Android upload. 
       
      * IOS_APP: An iOS upload. 
       
      * WEB_APP: A web appliction upload. 
       
      * EXTERNAL_DATA: An external data upload. 
       
      * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
       
      * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
       
      * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
       
      * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
       
      * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
       
      * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
       
      * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
       
      * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
       
      * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
       
      * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
       
      * XCTEST_TEST_PACKAGE: An XCode test package upload. 
       
      * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
       

       

       **Note** If you call ``CreateUpload`` with ``WEB_APP`` specified, AWS Device Farm throws an ``ArgumentException`` error.

      

    
    :type contentType: string
    :param contentType: 

      The upload's content type (for example, "application/octet-stream").

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'upload': {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
                'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                'url': 'string',
                'metadata': 'string',
                'contentType': 'string',
                'message': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a create upload request.

        
        

        - **upload** *(dict) --* 

          The newly created upload.

          
          

          - **arn** *(string) --* 

            The upload's ARN.

            
          

          - **name** *(string) --* 

            The upload's file name.

            
          

          - **created** *(datetime) --* 

            When the upload was created.

            
          

          - **type** *(string) --* 

            The upload's type.

             

            Must be one of the following values:

             

             
            * ANDROID_APP: An Android upload. 
             
            * IOS_APP: An iOS upload. 
             
            * WEB_APP: A web appliction upload. 
             
            * EXTERNAL_DATA: An external data upload. 
             
            * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
             
            * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
             
            * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
             
            * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
             
            * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
             
            * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
             
            * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
             
            * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
             
            * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
             
            * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
             
            * XCTEST_TEST_PACKAGE: An XCode test package upload. 
             
            * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
             

            
          

          - **status** *(string) --* 

            The upload's status.

             

            Must be one of the following values:

             

             
            * FAILED: A failed status. 
             
            * INITIALIZED: An initialized status. 
             
            * PROCESSING: A processing status. 
             
            * SUCCEEDED: A succeeded status. 
             

            
          

          - **url** *(string) --* 

            The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.

            
          

          - **metadata** *(string) --* 

            The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

            
          

          - **contentType** *(string) --* 

            The upload's content type (for example, "application/octet-stream").

            
          

          - **message** *(string) --* 

            A message about the upload's result.

            
      
    

    **Examples** 

    The following example creates a new Appium Python test package upload inside an existing project.
    ::

      response = client.create_upload(
          name='MyAppiumPythonUpload',
          type='APPIUM_PYTHON_TEST_PACKAGE',
          # You can get the project ARN by using the list-projects CLI command.
          projectArn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'upload': {
              'name': 'MyAppiumPythonUpload',
              'type': 'APPIUM_PYTHON_TEST_PACKAGE',
              'arn': 'arn:aws:devicefarm:us-west-2:183774035805:upload:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/b5340a65-3da7-4da6-a26e-12345EXAMPLE',
              'created': datetime(2016, 8, 31, 9, 36, 44, 2, 244, 1),
              'status': 'INITIALIZED',
              'url': 'https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A183774035805%3Aproject%3A5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE/uploads/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A183774035805%3Aupload%3A5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/b5340a65-3da7-4da6-a26e-12345EXAMPLE/MyAppiumPythonUpload?AWSAccessKeyId=1234567891011EXAMPLE&Expires=1472747804&Signature=1234567891011EXAMPLE',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_device_pool(**kwargs)

    

    Deletes a device pool given the pool ARN. Does not allow deletion of curated pools owned by the system.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteDevicePool>`_    


    **Request Syntax** 
    ::

      response = client.delete_device_pool(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      Represents the Amazon Resource Name (ARN) of the Device Farm device pool you wish to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a delete device pool request.

        
    

    **Examples** 

    The following example deletes a specific device pool.
    ::

      response = client.delete_device_pool(
          # You can get the device pool ARN by using the list-device-pools CLI command.
          arn='arn:aws:devicefarm:us-west-2::devicepool:123-456-EXAMPLE-GUID',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_network_profile(**kwargs)

    

    Deletes a network profile.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteNetworkProfile>`_    


    **Request Syntax** 
    ::

      response = client.delete_network_profile(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the network profile you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_project(**kwargs)

    

    Deletes an AWS Device Farm project, given the project ARN.

     

     **Note** Deleting this resource does not stop an in-progress run.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteProject>`_    


    **Request Syntax** 
    ::

      response = client.delete_project(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      Represents the Amazon Resource Name (ARN) of the Device Farm project you wish to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a delete project request.

        
    

    **Examples** 

    The following example deletes a specific project.
    ::

      response = client.delete_project(
          # You can get the project ARN by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_remote_access_session(**kwargs)

    

    Deletes a completed remote access session and its results.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteRemoteAccessSession>`_    


    **Request Syntax** 
    ::

      response = client.delete_remote_access_session(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the sesssion for which you want to delete remote access.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The response from the server when a request is made to delete the remote access session.

        
    

    **Examples** 

    The following example deletes a specific remote access session.
    ::

      response = client.delete_remote_access_session(
          # You can get the remote access session ARN by using the list-remote-access-sessions CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_run(**kwargs)

    

    Deletes the run, given the run ARN.

     

     **Note** Deleting this resource does not stop an in-progress run.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteRun>`_    


    **Request Syntax** 
    ::

      response = client.delete_run(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) for the run you wish to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a delete run request.

        
    

    **Examples** 

    The following example deletes a specific test run.
    ::

      response = client.delete_run(
          # You can get the run ARN by using the list-runs CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_upload(**kwargs)

    

    Deletes an upload given the upload ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteUpload>`_    


    **Request Syntax** 
    ::

      response = client.delete_upload(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      Represents the Amazon Resource Name (ARN) of the Device Farm upload you wish to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a delete upload request.

        
    

    **Examples** 

    The following example deletes a specific upload.
    ::

      response = client.delete_upload(
          # You can get the upload ARN by using the list-uploads CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:upload:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
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


  .. py:method:: get_account_settings()

    

    Returns the number of unmetered iOS and/or unmetered Android devices that have been purchased by the account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetAccountSettings>`_    


    **Request Syntax** 
    ::

      response = client.get_account_settings()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'accountSettings': {
                'awsAccountNumber': 'string',
                'unmeteredDevices': {
                    'string': 123
                },
                'unmeteredRemoteAccessDevices': {
                    'string': 123
                },
                'maxJobTimeoutMinutes': 123,
                'trialMinutes': {
                    'total': 123.0,
                    'remaining': 123.0
                },
                'maxSlots': {
                    'string': 123
                },
                'defaultJobTimeoutMinutes': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the account settings return values from the ``GetAccountSettings`` request.

        
        

        - **accountSettings** *(dict) --* 

          The account settings.

          
          

          - **awsAccountNumber** *(string) --* 

            The AWS account number specified in the ``AccountSettings`` container.

            
          

          - **unmeteredDevices** *(dict) --* 

            Returns the unmetered devices you have purchased or want to purchase.

            
            

            - *(string) --* 
              

              - *(integer) --* 
        
      
          

          - **unmeteredRemoteAccessDevices** *(dict) --* 

            Returns the unmetered remote access devices you have purchased or want to purchase.

            
            

            - *(string) --* 
              

              - *(integer) --* 
        
      
          

          - **maxJobTimeoutMinutes** *(integer) --* 

            The maximum number of minutes a test run will execute before it times out.

            
          

          - **trialMinutes** *(dict) --* 

            Information about an AWS account's usage of free trial device minutes.

            
            

            - **total** *(float) --* 

              The total number of free trial minutes that the account started with.

              
            

            - **remaining** *(float) --* 

              The number of free trial minutes remaining in the account.

              
        
          

          - **maxSlots** *(dict) --* 

            The maximum number of device slots that the AWS account can purchase. Each maximum is expressed as an ``offering-id:number`` pair, where the ``offering-id`` represents one of the IDs returned by the ``ListOfferings`` command.

            
            

            - *(string) --* 
              

              - *(integer) --* 
        
      
          

          - **defaultJobTimeoutMinutes** *(integer) --* 

            The default number of minutes (at the account level) a test run will execute before it times out. Default value is 60 minutes.

            
      
    

    **Examples** 

    The following example returns information about your Device Farm account settings.
    ::

      response = client.get_account_settings(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'accountSettings': {
              'awsAccountNumber': '123456789101',
              'unmeteredDevices': {
                  'ANDROID': 1,
                  'IOS': 2,
              },
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_device(**kwargs)

    

    Gets information about a unique device type.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetDevice>`_    


    **Request Syntax** 
    ::

      response = client.get_device(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The device type's ARN.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a get device request.

        
        

        - **device** *(dict) --* 

          An object containing information about the requested device.

          
          

          - **arn** *(string) --* 

            The device's ARN.

            
          

          - **name** *(string) --* 

            The device's display name.

            
          

          - **manufacturer** *(string) --* 

            The device's manufacturer name.

            
          

          - **model** *(string) --* 

            The device's model name.

            
          

          - **formFactor** *(string) --* 

            The device's form factor.

             

            Allowed values include:

             

             
            * PHONE: The phone form factor. 
             
            * TABLET: The tablet form factor. 
             

            
          

          - **platform** *(string) --* 

            The device's platform.

             

            Allowed values include:

             

             
            * ANDROID: The Android platform. 
             
            * IOS: The iOS platform. 
             

            
          

          - **os** *(string) --* 

            The device's operating system type.

            
          

          - **cpu** *(dict) --* 

            Information about the device's CPU.

            
            

            - **frequency** *(string) --* 

              The CPU's frequency.

              
            

            - **architecture** *(string) --* 

              The CPU's architecture, for example x86 or ARM.

              
            

            - **clock** *(float) --* 

              The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

              
        
          

          - **resolution** *(dict) --* 

            The resolution of the device.

            
            

            - **width** *(integer) --* 

              The screen resolution's width, expressed in pixels.

              
            

            - **height** *(integer) --* 

              The screen resolution's height, expressed in pixels.

              
        
          

          - **heapSize** *(integer) --* 

            The device's heap size, expressed in bytes.

            
          

          - **memory** *(integer) --* 

            The device's total memory size, expressed in bytes.

            
          

          - **image** *(string) --* 

            The device's image name.

            
          

          - **carrier** *(string) --* 

            The device's carrier.

            
          

          - **radio** *(string) --* 

            The device's radio.

            
          

          - **remoteAccessEnabled** *(boolean) --* 

            Specifies whether remote access has been enabled for the specified device.

            
          

          - **remoteDebugEnabled** *(boolean) --* 

            This flag is set to ``true`` if remote debugging is enabled for the device.

            
          

          - **fleetType** *(string) --* 

            The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

            
          

          - **fleetName** *(string) --* 

            The name of the fleet to which this device belongs.

            
      
    

    **Examples** 

    The following example returns information about a specific device.
    ::

      response = client.get_device(
          arn='arn:aws:devicefarm:us-west-2::device:123EXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'device': {
              'name': 'LG G2 (Sprint)',
              'arn': 'arn:aws:devicefarm:us-west-2::device:A0E6E6E1059E45918208DF75B2B7EF6C',
              'cpu': {
                  'architecture': 'armeabi-v7a',
                  'clock': 2265.6,
                  'frequency': 'MHz',
              },
              'formFactor': 'PHONE',
              'heapSize': 256000000,
              'image': '75B2B7EF6C12345EXAMPLE',
              'manufacturer': 'LG',
              'memory': 16000000000,
              'model': 'G2 (Sprint)',
              'os': '4.2.2',
              'platform': 'ANDROID',
              'resolution': {
                  'height': 1920,
                  'width': 1080,
              },
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_device_pool(**kwargs)

    

    Gets information about a device pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetDevicePool>`_    


    **Request Syntax** 
    ::

      response = client.get_device_pool(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The device pool's ARN.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'devicePool': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'rules': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION',
                        'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                        'value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a get device pool request.

        
        

        - **devicePool** *(dict) --* 

          An object containing information about the requested device pool.

          
          

          - **arn** *(string) --* 

            The device pool's ARN.

            
          

          - **name** *(string) --* 

            The device pool's name.

            
          

          - **description** *(string) --* 

            The device pool's description.

            
          

          - **type** *(string) --* 

            The device pool's type.

             

            Allowed values include:

             

             
            * CURATED: A device pool that is created and managed by AWS Device Farm. 
             
            * PRIVATE: A device pool that is created and managed by the device pool developer. 
             

            
          

          - **rules** *(list) --* 

            Information about the device pool's rules.

            
            

            - *(dict) --* 

              Represents a condition for a device pool.

              
              

              - **attribute** *(string) --* 

                The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .

                 

                Allowed values include:

                 

                 
                * ARN: The ARN. 
                 
                * FORM_FACTOR: The form factor (for example, phone or tablet). 
                 
                * MANUFACTURER: The manufacturer. 
                 
                * PLATFORM: The platform (for example, Android or iOS). 
                 
                * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                 
                * APPIUM_VERSION: The Appium version for the test. 
                 

                
              

              - **operator** *(string) --* 

                The rule's operator.

                 

                 
                * EQUALS: The equals operator. 
                 
                * GREATER_THAN: The greater-than operator. 
                 
                * IN: The in operator. 
                 
                * LESS_THAN: The less-than operator. 
                 
                * NOT_IN: The not-in operator. 
                 
                * CONTAINS: The contains operator. 
                 

                
              

              - **value** *(string) --* 

                The rule's value.

                
          
        
      
    

    **Examples** 

    The following example returns information about a specific device pool, given a project ARN.
    ::

      response = client.get_device_pool(
          # You can obtain the project ARN by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'devicePool': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_device_pool_compatibility(**kwargs)

    

    Gets information about compatibility with a device pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetDevicePoolCompatibility>`_    


    **Request Syntax** 
    ::

      response = client.get_device_pool_compatibility(
          devicePoolArn='string',
          appArn='string',
          testType='BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
          test={
              'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
              'testPackageArn': 'string',
              'filter': 'string',
              'parameters': {
                  'string': 'string'
              }
          }
      )
    :type devicePoolArn: string
    :param devicePoolArn: **[REQUIRED]** 

      The device pool's ARN.

      

    
    :type appArn: string
    :param appArn: 

      The ARN of the app that is associated with the specified device pool.

      

    
    :type testType: string
    :param testType: 

      The test type for the specified device pool.

       

      Allowed values include the following:

       

       
      * BUILTIN_FUZZ: The built-in fuzz type. 
       
      * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
       
      * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
       
      * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
       
      * APPIUM_PYTHON: The Appium Python type. 
       
      * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
       
      * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
       
      * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
       
      * CALABASH: The Calabash type. 
       
      * INSTRUMENTATION: The Instrumentation type. 
       
      * UIAUTOMATION: The uiautomation type. 
       
      * UIAUTOMATOR: The uiautomator type. 
       
      * XCTEST: The XCode test type. 
       
      * XCTEST_UI: The XCode UI test type. 
       

      

    
    :type test: dict
    :param test: 

      Information about the uploaded test to be run against the device pool.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The test's type.

         

        Must be one of the following values:

         

         
        * BUILTIN_FUZZ: The built-in fuzz type. 
         
        * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
         
        * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
         
        * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
         
        * APPIUM_PYTHON: The Appium Python type. 
         
        * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
         
        * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
         
        * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
         
        * CALABASH: The Calabash type. 
         
        * INSTRUMENTATION: The Instrumentation type. 
         
        * UIAUTOMATION: The uiautomation type. 
         
        * UIAUTOMATOR: The uiautomator type. 
         
        * XCTEST: The XCode test type. 
         
        * XCTEST_UI: The XCode UI test type. 
         

        

      
      - **testPackageArn** *(string) --* 

        The ARN of the uploaded test that will be run.

        

      
      - **filter** *(string) --* 

        The test's filter.

        

      
      - **parameters** *(dict) --* 

        The test's parameters, such as the following test framework parameters and fixture settings:

         

        For Calabash tests:

         

         
        * profile: A cucumber profile, for example, "my_profile_name". 
         
        * tags: You can limit execution to features or scenarios that have (or don't have) certain tags, for example, "@smoke" or "@smoke,~@wip". 
         

         

        For Appium tests (all types):

         

         
        * appium_version: The Appium version. Currently supported values are "1.4.16", "1.6.3", "latest", and "default". 

           
          * “latest” will run the latest Appium version supported by Device Farm (1.6.3). 
           
          * For “default”, Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.4.16 on Android devices and iOS 9 and earlier, 1.6.3 for iOS 10 and later. 
           
          * This behavior is subject to change. 
           

         
         

         

        For Fuzz tests (Android only):

         

         
        * event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform. 
         
        * throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events. 
         
        * seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences. 
         

         

        For Explorer tests:

         

         
        * username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted. 
         
        * password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted. 
         

         

        For Instrumentation:

         

         
        * filter: A test filter string. Examples: 

           
          * Running a single test case: "com.android.abc.Test1" 
           
          * Running a single test: "com.android.abc.Test1#smoke" 
           
          * Running multiple tests: "com.android.abc.Test1,com.android.abc.Test2" 
           

         
         

         

        For XCTest and XCTestUI:

         

         
        * filter: A test filter string. Examples: 

           
          * Running a single test class: "LoginTests" 
           
          * Running a multiple test classes: "LoginTests,SmokeTests" 
           
          * Running a single test: "LoginTests/testValid" 
           
          * Running multiple tests: "LoginTests/testValid,LoginTests/testInvalid" 
           

         
         

         

        For UIAutomator:

         

         
        * filter: A test filter string. Examples: 

           
          * Running a single test case: "com.android.abc.Test1" 
           
          * Running a single test: "com.android.abc.Test1#smoke" 
           
          * Running multiple tests: "com.android.abc.Test1,com.android.abc.Test2" 
           

         
         

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'compatibleDevices': [
                {
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string'
                    },
                    'compatible': True|False,
                    'incompatibilityMessages': [
                        {
                            'message': 'string',
                            'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'
                        },
                    ]
                },
            ],
            'incompatibleDevices': [
                {
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string'
                    },
                    'compatible': True|False,
                    'incompatibilityMessages': [
                        {
                            'message': 'string',
                            'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of describe device pool compatibility request.

        
        

        - **compatibleDevices** *(list) --* 

          Information about compatible devices.

          
          

          - *(dict) --* 

            Represents a device pool compatibility result.

            
            

            - **device** *(dict) --* 

              The device (phone or tablet) that you wish to return information about.

              
              

              - **arn** *(string) --* 

                The device's ARN.

                
              

              - **name** *(string) --* 

                The device's display name.

                
              

              - **manufacturer** *(string) --* 

                The device's manufacturer name.

                
              

              - **model** *(string) --* 

                The device's model name.

                
              

              - **formFactor** *(string) --* 

                The device's form factor.

                 

                Allowed values include:

                 

                 
                * PHONE: The phone form factor. 
                 
                * TABLET: The tablet form factor. 
                 

                
              

              - **platform** *(string) --* 

                The device's platform.

                 

                Allowed values include:

                 

                 
                * ANDROID: The Android platform. 
                 
                * IOS: The iOS platform. 
                 

                
              

              - **os** *(string) --* 

                The device's operating system type.

                
              

              - **cpu** *(dict) --* 

                Information about the device's CPU.

                
                

                - **frequency** *(string) --* 

                  The CPU's frequency.

                  
                

                - **architecture** *(string) --* 

                  The CPU's architecture, for example x86 or ARM.

                  
                

                - **clock** *(float) --* 

                  The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                  
            
              

              - **resolution** *(dict) --* 

                The resolution of the device.

                
                

                - **width** *(integer) --* 

                  The screen resolution's width, expressed in pixels.

                  
                

                - **height** *(integer) --* 

                  The screen resolution's height, expressed in pixels.

                  
            
              

              - **heapSize** *(integer) --* 

                The device's heap size, expressed in bytes.

                
              

              - **memory** *(integer) --* 

                The device's total memory size, expressed in bytes.

                
              

              - **image** *(string) --* 

                The device's image name.

                
              

              - **carrier** *(string) --* 

                The device's carrier.

                
              

              - **radio** *(string) --* 

                The device's radio.

                
              

              - **remoteAccessEnabled** *(boolean) --* 

                Specifies whether remote access has been enabled for the specified device.

                
              

              - **remoteDebugEnabled** *(boolean) --* 

                This flag is set to ``true`` if remote debugging is enabled for the device.

                
              

              - **fleetType** *(string) --* 

                The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

                
              

              - **fleetName** *(string) --* 

                The name of the fleet to which this device belongs.

                
          
            

            - **compatible** *(boolean) --* 

              Whether the result was compatible with the device pool.

              
            

            - **incompatibilityMessages** *(list) --* 

              Information about the compatibility.

              
              

              - *(dict) --* 

                Represents information about incompatibility.

                
                

                - **message** *(string) --* 

                  A message about the incompatibility.

                  
                

                - **type** *(string) --* 

                  The type of incompatibility.

                   

                  Allowed values include:

                   

                   
                  * ARN: The ARN. 
                   
                  * FORM_FACTOR: The form factor (for example, phone or tablet). 
                   
                  * MANUFACTURER: The manufacturer. 
                   
                  * PLATFORM: The platform (for example, Android or iOS). 
                   
                  * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                   
                  * APPIUM_VERSION: The Appium version for the test. 
                   

                  
            
          
        
      
        

        - **incompatibleDevices** *(list) --* 

          Information about incompatible devices.

          
          

          - *(dict) --* 

            Represents a device pool compatibility result.

            
            

            - **device** *(dict) --* 

              The device (phone or tablet) that you wish to return information about.

              
              

              - **arn** *(string) --* 

                The device's ARN.

                
              

              - **name** *(string) --* 

                The device's display name.

                
              

              - **manufacturer** *(string) --* 

                The device's manufacturer name.

                
              

              - **model** *(string) --* 

                The device's model name.

                
              

              - **formFactor** *(string) --* 

                The device's form factor.

                 

                Allowed values include:

                 

                 
                * PHONE: The phone form factor. 
                 
                * TABLET: The tablet form factor. 
                 

                
              

              - **platform** *(string) --* 

                The device's platform.

                 

                Allowed values include:

                 

                 
                * ANDROID: The Android platform. 
                 
                * IOS: The iOS platform. 
                 

                
              

              - **os** *(string) --* 

                The device's operating system type.

                
              

              - **cpu** *(dict) --* 

                Information about the device's CPU.

                
                

                - **frequency** *(string) --* 

                  The CPU's frequency.

                  
                

                - **architecture** *(string) --* 

                  The CPU's architecture, for example x86 or ARM.

                  
                

                - **clock** *(float) --* 

                  The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                  
            
              

              - **resolution** *(dict) --* 

                The resolution of the device.

                
                

                - **width** *(integer) --* 

                  The screen resolution's width, expressed in pixels.

                  
                

                - **height** *(integer) --* 

                  The screen resolution's height, expressed in pixels.

                  
            
              

              - **heapSize** *(integer) --* 

                The device's heap size, expressed in bytes.

                
              

              - **memory** *(integer) --* 

                The device's total memory size, expressed in bytes.

                
              

              - **image** *(string) --* 

                The device's image name.

                
              

              - **carrier** *(string) --* 

                The device's carrier.

                
              

              - **radio** *(string) --* 

                The device's radio.

                
              

              - **remoteAccessEnabled** *(boolean) --* 

                Specifies whether remote access has been enabled for the specified device.

                
              

              - **remoteDebugEnabled** *(boolean) --* 

                This flag is set to ``true`` if remote debugging is enabled for the device.

                
              

              - **fleetType** *(string) --* 

                The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

                
              

              - **fleetName** *(string) --* 

                The name of the fleet to which this device belongs.

                
          
            

            - **compatible** *(boolean) --* 

              Whether the result was compatible with the device pool.

              
            

            - **incompatibilityMessages** *(list) --* 

              Information about the compatibility.

              
              

              - *(dict) --* 

                Represents information about incompatibility.

                
                

                - **message** *(string) --* 

                  A message about the incompatibility.

                  
                

                - **type** *(string) --* 

                  The type of incompatibility.

                   

                  Allowed values include:

                   

                   
                  * ARN: The ARN. 
                   
                  * FORM_FACTOR: The form factor (for example, phone or tablet). 
                   
                  * MANUFACTURER: The manufacturer. 
                   
                  * PLATFORM: The platform (for example, Android or iOS). 
                   
                  * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                   
                  * APPIUM_VERSION: The Appium version for the test. 
                   

                  
            
          
        
      
    

    **Examples** 

    The following example returns information about the compatibility of a specific device pool, given its ARN.
    ::

      response = client.get_device_pool_compatibility(
          appArn='arn:aws:devicefarm:us-west-2::app:123-456-EXAMPLE-GUID',
          # You can get the device pool ARN by using the list-device-pools CLI command.
          devicePoolArn='arn:aws:devicefarm:us-west-2::devicepool:123-456-EXAMPLE-GUID',
          testType='APPIUM_PYTHON',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'compatibleDevices': [
          ],
          'incompatibleDevices': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_job(**kwargs)

    

    Gets information about a job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetJob>`_    


    **Request Syntax** 
    ::

      response = client.get_job(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The job's ARN.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'job': {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a get job request.

        
        

        - **job** *(dict) --* 

          An object containing information about the requested job.

          
          

          - **arn** *(string) --* 

            The job's ARN.

            
          

          - **name** *(string) --* 

            The job's name.

            
          

          - **type** *(string) --* 

            The job's type.

             

            Allowed values include the following:

             

             
            * BUILTIN_FUZZ: The built-in fuzz type. 
             
            * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
             
            * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
             
            * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
             
            * APPIUM_PYTHON: The Appium Python type. 
             
            * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
             
            * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
             
            * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
             
            * CALABASH: The Calabash type. 
             
            * INSTRUMENTATION: The Instrumentation type. 
             
            * UIAUTOMATION: The uiautomation type. 
             
            * UIAUTOMATOR: The uiautomator type. 
             
            * XCTEST: The XCode test type. 
             
            * XCTEST_UI: The XCode UI test type. 
             

            
          

          - **created** *(datetime) --* 

            When the job was created.

            
          

          - **status** *(string) --* 

            The job's status.

             

            Allowed values include:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The job's result.

             

            Allowed values include:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **started** *(datetime) --* 

            The job's start time.

            
          

          - **stopped** *(datetime) --* 

            The job's stop time.

            
          

          - **counters** *(dict) --* 

            The job's result counters.

            
            

            - **total** *(integer) --* 

              The total number of entities.

              
            

            - **passed** *(integer) --* 

              The number of passed entities.

              
            

            - **failed** *(integer) --* 

              The number of failed entities.

              
            

            - **warned** *(integer) --* 

              The number of warned entities.

              
            

            - **errored** *(integer) --* 

              The number of errored entities.

              
            

            - **stopped** *(integer) --* 

              The number of stopped entities.

              
            

            - **skipped** *(integer) --* 

              The number of skipped entities.

              
        
          

          - **message** *(string) --* 

            A message about the job's result.

            
          

          - **device** *(dict) --* 

            The device (phone or tablet).

            
            

            - **arn** *(string) --* 

              The device's ARN.

              
            

            - **name** *(string) --* 

              The device's display name.

              
            

            - **manufacturer** *(string) --* 

              The device's manufacturer name.

              
            

            - **model** *(string) --* 

              The device's model name.

              
            

            - **formFactor** *(string) --* 

              The device's form factor.

               

              Allowed values include:

               

               
              * PHONE: The phone form factor. 
               
              * TABLET: The tablet form factor. 
               

              
            

            - **platform** *(string) --* 

              The device's platform.

               

              Allowed values include:

               

               
              * ANDROID: The Android platform. 
               
              * IOS: The iOS platform. 
               

              
            

            - **os** *(string) --* 

              The device's operating system type.

              
            

            - **cpu** *(dict) --* 

              Information about the device's CPU.

              
              

              - **frequency** *(string) --* 

                The CPU's frequency.

                
              

              - **architecture** *(string) --* 

                The CPU's architecture, for example x86 or ARM.

                
              

              - **clock** *(float) --* 

                The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                
          
            

            - **resolution** *(dict) --* 

              The resolution of the device.

              
              

              - **width** *(integer) --* 

                The screen resolution's width, expressed in pixels.

                
              

              - **height** *(integer) --* 

                The screen resolution's height, expressed in pixels.

                
          
            

            - **heapSize** *(integer) --* 

              The device's heap size, expressed in bytes.

              
            

            - **memory** *(integer) --* 

              The device's total memory size, expressed in bytes.

              
            

            - **image** *(string) --* 

              The device's image name.

              
            

            - **carrier** *(string) --* 

              The device's carrier.

              
            

            - **radio** *(string) --* 

              The device's radio.

              
            

            - **remoteAccessEnabled** *(boolean) --* 

              Specifies whether remote access has been enabled for the specified device.

              
            

            - **remoteDebugEnabled** *(boolean) --* 

              This flag is set to ``true`` if remote debugging is enabled for the device.

              
            

            - **fleetType** *(string) --* 

              The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

              
            

            - **fleetName** *(string) --* 

              The name of the fleet to which this device belongs.

              
        
          

          - **deviceMinutes** *(dict) --* 

            Represents the total (metered or unmetered) minutes used by the job.

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
      
    

    **Examples** 

    The following example returns information about a specific job.
    ::

      response = client.get_job(
          # You can get the job ARN by using the list-jobs CLI command.
          arn='arn:aws:devicefarm:us-west-2::job:123-456-EXAMPLE-GUID',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'job': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_network_profile(**kwargs)

    

    Returns information about a network profile.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetNetworkProfile>`_    


    **Request Syntax** 
    ::

      response = client.get_network_profile(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the network profile you want to return information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **networkProfile** *(dict) --* 

          The network profile.

          
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the network profile.

            
          

          - **name** *(string) --* 

            The name of the network profile.

            
          

          - **description** *(string) --* 

            The description of the network profile.

            
          

          - **type** *(string) --* 

            The type of network profile. Valid values are listed below.

            
          

          - **uplinkBandwidthBits** *(integer) --* 

            The data throughput rate in bits per second, as an integer from 0 to 104857600.

            
          

          - **downlinkBandwidthBits** *(integer) --* 

            The data throughput rate in bits per second, as an integer from 0 to 104857600.

            
          

          - **uplinkDelayMs** *(integer) --* 

            Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

            
          

          - **downlinkDelayMs** *(integer) --* 

            Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

            
          

          - **uplinkJitterMs** *(integer) --* 

            Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

            
          

          - **downlinkJitterMs** *(integer) --* 

            Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

            
          

          - **uplinkLossPercent** *(integer) --* 

            Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

            
          

          - **downlinkLossPercent** *(integer) --* 

            Proportion of received packets that fail to arrive from 0 to 100 percent.

            
      
    

  .. py:method:: get_offering_status(**kwargs)

    

    Gets the current status and future status of all offerings purchased by an AWS account. The response indicates how many offerings are currently available and the offerings that will be available in the next period. The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetOfferingStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_offering_status(
          nextToken='string'
      )
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'current': {
                'string': {
                    'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                    'offering': {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                    'quantity': 123,
                    'effectiveOn': datetime(2015, 1, 1)
                }
            },
            'nextPeriod': {
                'string': {
                    'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                    'offering': {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                    'quantity': 123,
                    'effectiveOn': datetime(2015, 1, 1)
                }
            },
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the status result for a device offering.

        
        

        - **current** *(dict) --* 

          When specified, gets the offering status for the current period.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              The status of the offering.

              
              

              - **type** *(string) --* 

                The type specified for the offering status.

                
              

              - **offering** *(dict) --* 

                Represents the metadata of an offering status.

                
                

                - **id** *(string) --* 

                  The ID that corresponds to a device offering.

                  
                

                - **description** *(string) --* 

                  A string describing the offering.

                  
                

                - **type** *(string) --* 

                  The type of offering (e.g., "RECURRING") for a device.

                  
                

                - **platform** *(string) --* 

                  The platform of the device (e.g., ANDROID or IOS).

                  
                

                - **recurringCharges** *(list) --* 

                  Specifies whether there are recurring charges for the offering.

                  
                  

                  - *(dict) --* 

                    Specifies whether charges for devices will be recurring.

                    
                    

                    - **cost** *(dict) --* 

                      The cost of the recurring charge.

                      
                      

                      - **amount** *(float) --* 

                        The numerical amount of an offering or transaction.

                        
                      

                      - **currencyCode** *(string) --* 

                        The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                        
                  
                    

                    - **frequency** *(string) --* 

                      The frequency in which charges will recur.

                      
                
              
            
              

              - **quantity** *(integer) --* 

                The number of available devices in the offering.

                
              

              - **effectiveOn** *(datetime) --* 

                The date on which the offering is effective.

                
          
      
    
        

        - **nextPeriod** *(dict) --* 

          When specified, gets the offering status for the next period.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              The status of the offering.

              
              

              - **type** *(string) --* 

                The type specified for the offering status.

                
              

              - **offering** *(dict) --* 

                Represents the metadata of an offering status.

                
                

                - **id** *(string) --* 

                  The ID that corresponds to a device offering.

                  
                

                - **description** *(string) --* 

                  A string describing the offering.

                  
                

                - **type** *(string) --* 

                  The type of offering (e.g., "RECURRING") for a device.

                  
                

                - **platform** *(string) --* 

                  The platform of the device (e.g., ANDROID or IOS).

                  
                

                - **recurringCharges** *(list) --* 

                  Specifies whether there are recurring charges for the offering.

                  
                  

                  - *(dict) --* 

                    Specifies whether charges for devices will be recurring.

                    
                    

                    - **cost** *(dict) --* 

                      The cost of the recurring charge.

                      
                      

                      - **amount** *(float) --* 

                        The numerical amount of an offering or transaction.

                        
                      

                      - **currencyCode** *(string) --* 

                        The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                        
                  
                    

                    - **frequency** *(string) --* 

                      The frequency in which charges will recur.

                      
                
              
            
              

              - **quantity** *(integer) --* 

                The number of available devices in the offering.

                
              

              - **effectiveOn** *(datetime) --* 

                The date on which the offering is effective.

                
          
      
    
        

        - **nextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about Device Farm offerings available to your account.
    ::

      response = client.get_offering_status(
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'current': {
              'D68B3C05-1BA6-4360-BC69-12345EXAMPLE': {
                  'offering': {
                      'type': 'RECURRING',
                      'description': 'Android Remote Access Unmetered Device Slot',
                      'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                      'platform': 'ANDROID',
                  },
                  'quantity': 1,
              },
          },
          'nextPeriod': {
              'D68B3C05-1BA6-4360-BC69-12345EXAMPLE': {
                  'effectiveOn': datetime(2016, 8, 31, 17, 0, 0, 2, 244, 1),
                  'offering': {
                      'type': 'RECURRING',
                      'description': 'Android Remote Access Unmetered Device Slot',
                      'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                      'platform': 'ANDROID',
                  },
                  'quantity': 1,
              },
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

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


  .. py:method:: get_project(**kwargs)

    

    Gets information about a project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetProject>`_    


    **Request Syntax** 
    ::

      response = client.get_project(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The project's ARN.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'project': {
                'arn': 'string',
                'name': 'string',
                'defaultJobTimeoutMinutes': 123,
                'created': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a get project request.

        
        

        - **project** *(dict) --* 

          The project you wish to get information about.

          
          

          - **arn** *(string) --* 

            The project's ARN.

            
          

          - **name** *(string) --* 

            The project's name.

            
          

          - **defaultJobTimeoutMinutes** *(integer) --* 

            The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.

            
          

          - **created** *(datetime) --* 

            When the project was created.

            
      
    

    **Examples** 

    The following example gets information about a specific project.
    ::

      response = client.get_project(
          # You can get the project ARN by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'project': {
              'name': 'My Project',
              'arn': 'arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE',
              'created': datetime(2016, 8, 31, 9, 28, 59, 2, 244, 1),
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_remote_access_session(**kwargs)

    

    Returns a link to a currently running remote access session.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetRemoteAccessSession>`_    


    **Request Syntax** 
    ::

      response = client.get_remote_access_session(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the remote access session about which you want to get session information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'remoteAccessSession': {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'message': 'string',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
                'remoteDebugEnabled': True|False,
                'hostAddress': 'string',
                'clientId': 'string',
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'endpoint': 'string',
                'deviceUdid': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server that lists detailed information about the remote access session.

        
        

        - **remoteAccessSession** *(dict) --* 

          A container that lists detailed information about the remote access session.

          
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the remote access session.

            
          

          - **name** *(string) --* 

            The name of the remote access session.

            
          

          - **created** *(datetime) --* 

            The date and time the remote access session was created.

            
          

          - **status** *(string) --* 

            The status of the remote access session. Can be any of the following:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The result of the remote access session. Can be any of the following:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **message** *(string) --* 

            A message about the remote access session.

            
          

          - **started** *(datetime) --* 

            The date and time the remote access session was started.

            
          

          - **stopped** *(datetime) --* 

            The date and time the remote access session was stopped.

            
          

          - **device** *(dict) --* 

            The device (phone or tablet) used in the remote access session.

            
            

            - **arn** *(string) --* 

              The device's ARN.

              
            

            - **name** *(string) --* 

              The device's display name.

              
            

            - **manufacturer** *(string) --* 

              The device's manufacturer name.

              
            

            - **model** *(string) --* 

              The device's model name.

              
            

            - **formFactor** *(string) --* 

              The device's form factor.

               

              Allowed values include:

               

               
              * PHONE: The phone form factor. 
               
              * TABLET: The tablet form factor. 
               

              
            

            - **platform** *(string) --* 

              The device's platform.

               

              Allowed values include:

               

               
              * ANDROID: The Android platform. 
               
              * IOS: The iOS platform. 
               

              
            

            - **os** *(string) --* 

              The device's operating system type.

              
            

            - **cpu** *(dict) --* 

              Information about the device's CPU.

              
              

              - **frequency** *(string) --* 

                The CPU's frequency.

                
              

              - **architecture** *(string) --* 

                The CPU's architecture, for example x86 or ARM.

                
              

              - **clock** *(float) --* 

                The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                
          
            

            - **resolution** *(dict) --* 

              The resolution of the device.

              
              

              - **width** *(integer) --* 

                The screen resolution's width, expressed in pixels.

                
              

              - **height** *(integer) --* 

                The screen resolution's height, expressed in pixels.

                
          
            

            - **heapSize** *(integer) --* 

              The device's heap size, expressed in bytes.

              
            

            - **memory** *(integer) --* 

              The device's total memory size, expressed in bytes.

              
            

            - **image** *(string) --* 

              The device's image name.

              
            

            - **carrier** *(string) --* 

              The device's carrier.

              
            

            - **radio** *(string) --* 

              The device's radio.

              
            

            - **remoteAccessEnabled** *(boolean) --* 

              Specifies whether remote access has been enabled for the specified device.

              
            

            - **remoteDebugEnabled** *(boolean) --* 

              This flag is set to ``true`` if remote debugging is enabled for the device.

              
            

            - **fleetType** *(string) --* 

              The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

              
            

            - **fleetName** *(string) --* 

              The name of the fleet to which this device belongs.

              
        
          

          - **remoteDebugEnabled** *(boolean) --* 

            This flag is set to ``true`` if remote debugging is enabled for the remote access session.

            
          

          - **hostAddress** *(string) --* 

            IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.

            
          

          - **clientId** *(string) --* 

            Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.

            
          

          - **billingMethod** *(string) --* 

            The billing method of the remote access session. Possible values include ``METERED`` or ``UNMETERED`` . For more information about metered devices, see `AWS Device Farm terminology <http://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology>`__ ."

            
          

          - **deviceMinutes** *(dict) --* 

            The number of minutes a device is used in a remote access sesssion (including setup and teardown minutes).

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
          

          - **endpoint** *(string) --* 

            The endpoint for the remote access sesssion.

            
          

          - **deviceUdid** *(string) --* 

            Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.

            
      
    

    **Examples** 

    The following example gets a specific remote access session.
    ::

      response = client.get_remote_access_session(
          # You can get the remote access session ARN by using the list-remote-access-sessions CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'remoteAccessSession': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_run(**kwargs)

    

    Gets information about a run.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetRun>`_    


    **Request Syntax** 
    ::

      response = client.get_run(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The run's ARN.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'run': {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                'platform': 'ANDROID'|'IOS',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'totalJobs': 123,
                'completedJobs': 123,
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'networkProfile': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                },
                'parsingResultUrl': 'string',
                'resultCode': 'PARSING_FAILED',
                'customerArtifactPaths': {
                    'iosPaths': [
                        'string',
                    ],
                    'androidPaths': [
                        'string',
                    ],
                    'deviceHostPaths': [
                        'string',
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a get run request.

        
        

        - **run** *(dict) --* 

          The run you wish to get results from.

          
          

          - **arn** *(string) --* 

            The run's ARN.

            
          

          - **name** *(string) --* 

            The run's name.

            
          

          - **type** *(string) --* 

            The run's type.

             

            Must be one of the following values:

             

             
            * BUILTIN_FUZZ: The built-in fuzz type. 
             
            * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
             
            * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
             
            * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
             
            * APPIUM_PYTHON: The Appium Python type. 
             
            * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
             
            * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
             
            * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
             
            * CALABASH: The Calabash type. 
             
            * INSTRUMENTATION: The Instrumentation type. 
             
            * UIAUTOMATION: The uiautomation type. 
             
            * UIAUTOMATOR: The uiautomator type. 
             
            * XCTEST: The XCode test type. 
             
            * XCTEST_UI: The XCode UI test type. 
             

            
          

          - **platform** *(string) --* 

            The run's platform.

             

            Allowed values include:

             

             
            * ANDROID: The Android platform. 
             
            * IOS: The iOS platform. 
             

            
          

          - **created** *(datetime) --* 

            When the run was created.

            
          

          - **status** *(string) --* 

            The run's status.

             

            Allowed values include:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The run's result.

             

            Allowed values include:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **started** *(datetime) --* 

            The run's start time.

            
          

          - **stopped** *(datetime) --* 

            The run's stop time.

            
          

          - **counters** *(dict) --* 

            The run's result counters.

            
            

            - **total** *(integer) --* 

              The total number of entities.

              
            

            - **passed** *(integer) --* 

              The number of passed entities.

              
            

            - **failed** *(integer) --* 

              The number of failed entities.

              
            

            - **warned** *(integer) --* 

              The number of warned entities.

              
            

            - **errored** *(integer) --* 

              The number of errored entities.

              
            

            - **stopped** *(integer) --* 

              The number of stopped entities.

              
            

            - **skipped** *(integer) --* 

              The number of skipped entities.

              
        
          

          - **message** *(string) --* 

            A message about the run's result.

            
          

          - **totalJobs** *(integer) --* 

            The total number of jobs for the run.

            
          

          - **completedJobs** *(integer) --* 

            The total number of completed jobs.

            
          

          - **billingMethod** *(string) --* 

            Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .

            
          

          - **deviceMinutes** *(dict) --* 

            Represents the total (metered or unmetered) minutes used by the test run.

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
          

          - **networkProfile** *(dict) --* 

            The network profile being used for a test run.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the network profile.

              
            

            - **name** *(string) --* 

              The name of the network profile.

              
            

            - **description** *(string) --* 

              The description of the network profile.

              
            

            - **type** *(string) --* 

              The type of network profile. Valid values are listed below.

              
            

            - **uplinkBandwidthBits** *(integer) --* 

              The data throughput rate in bits per second, as an integer from 0 to 104857600.

              
            

            - **downlinkBandwidthBits** *(integer) --* 

              The data throughput rate in bits per second, as an integer from 0 to 104857600.

              
            

            - **uplinkDelayMs** *(integer) --* 

              Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

              
            

            - **downlinkDelayMs** *(integer) --* 

              Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

              
            

            - **uplinkJitterMs** *(integer) --* 

              Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

              
            

            - **downlinkJitterMs** *(integer) --* 

              Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

              
            

            - **uplinkLossPercent** *(integer) --* 

              Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

              
            

            - **downlinkLossPercent** *(integer) --* 

              Proportion of received packets that fail to arrive from 0 to 100 percent.

              
        
          

          - **parsingResultUrl** *(string) --* 

            Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.

            
          

          - **resultCode** *(string) --* 

            Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.

            
          

          - **customerArtifactPaths** *(dict) --* 

            Output ``CustomerArtifactPaths`` object for the test run.

            
            

            - **iosPaths** *(list) --* 

              Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
            

            - **androidPaths** *(list) --* 

              Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
            

            - **deviceHostPaths** *(list) --* 

              Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
        
      
    

    **Examples** 

    The following example gets information about a specific test run.
    ::

      response = client.get_run(
          # You can get the run ARN by using the list-runs CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/0fcac17b-6122-44d7-ae5a-12345EXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'run': {
              'name': 'My Test Run',
              'type': 'BUILTIN_EXPLORER',
              'arn': 'arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/0fcac17b-6122-44d7-ae5a-12345EXAMPLE',
              'billingMethod': 'METERED',
              'completedJobs': 0,
              'counters': {
                  'errored': 0,
                  'failed': 0,
                  'passed': 0,
                  'skipped': 0,
                  'stopped': 0,
                  'total': 0,
                  'warned': 0,
              },
              'created': datetime(2016, 8, 31, 11, 18, 29, 2, 244, 1),
              'deviceMinutes': {
                  'metered': 0.0,
                  'total': 0.0,
                  'unmetered': 0.0,
              },
              'platform': 'ANDROID',
              'result': 'PENDING',
              'status': 'RUNNING',
              'totalJobs': 3,
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_suite(**kwargs)

    

    Gets information about a suite.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetSuite>`_    


    **Request Syntax** 
    ::

      response = client.get_suite(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The suite's ARN.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'suite': {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a get suite request.

        
        

        - **suite** *(dict) --* 

          A collection of one or more tests.

          
          

          - **arn** *(string) --* 

            The suite's ARN.

            
          

          - **name** *(string) --* 

            The suite's name.

            
          

          - **type** *(string) --* 

            The suite's type.

             

            Must be one of the following values:

             

             
            * BUILTIN_FUZZ: The built-in fuzz type. 
             
            * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
             
            * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
             
            * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
             
            * APPIUM_PYTHON: The Appium Python type. 
             
            * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
             
            * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
             
            * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
             
            * CALABASH: The Calabash type. 
             
            * INSTRUMENTATION: The Instrumentation type. 
             
            * UIAUTOMATION: The uiautomation type. 
             
            * UIAUTOMATOR: The uiautomator type. 
             
            * XCTEST: The XCode test type. 
             
            * XCTEST_UI: The XCode UI test type. 
             

            
          

          - **created** *(datetime) --* 

            When the suite was created.

            
          

          - **status** *(string) --* 

            The suite's status.

             

            Allowed values include:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The suite's result.

             

            Allowed values include:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **started** *(datetime) --* 

            The suite's start time.

            
          

          - **stopped** *(datetime) --* 

            The suite's stop time.

            
          

          - **counters** *(dict) --* 

            The suite's result counters.

            
            

            - **total** *(integer) --* 

              The total number of entities.

              
            

            - **passed** *(integer) --* 

              The number of passed entities.

              
            

            - **failed** *(integer) --* 

              The number of failed entities.

              
            

            - **warned** *(integer) --* 

              The number of warned entities.

              
            

            - **errored** *(integer) --* 

              The number of errored entities.

              
            

            - **stopped** *(integer) --* 

              The number of stopped entities.

              
            

            - **skipped** *(integer) --* 

              The number of skipped entities.

              
        
          

          - **message** *(string) --* 

            A message about the suite's result.

            
          

          - **deviceMinutes** *(dict) --* 

            Represents the total (metered or unmetered) minutes used by the test suite.

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
      
    

    **Examples** 

    The following example gets information about a specific test suite.
    ::

      response = client.get_suite(
          # You can get the suite ARN by using the list-suites CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:suite:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'suite': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_test(**kwargs)

    

    Gets information about a test.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetTest>`_    


    **Request Syntax** 
    ::

      response = client.get_test(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The test's ARN.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'test': {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a get test request.

        
        

        - **test** *(dict) --* 

          A test condition that is evaluated.

          
          

          - **arn** *(string) --* 

            The test's ARN.

            
          

          - **name** *(string) --* 

            The test's name.

            
          

          - **type** *(string) --* 

            The test's type.

             

            Must be one of the following values:

             

             
            * BUILTIN_FUZZ: The built-in fuzz type. 
             
            * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
             
            * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
             
            * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
             
            * APPIUM_PYTHON: The Appium Python type. 
             
            * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
             
            * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
             
            * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
             
            * CALABASH: The Calabash type. 
             
            * INSTRUMENTATION: The Instrumentation type. 
             
            * UIAUTOMATION: The uiautomation type. 
             
            * UIAUTOMATOR: The uiautomator type. 
             
            * XCTEST: The XCode test type. 
             
            * XCTEST_UI: The XCode UI test type. 
             

            
          

          - **created** *(datetime) --* 

            When the test was created.

            
          

          - **status** *(string) --* 

            The test's status.

             

            Allowed values include:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The test's result.

             

            Allowed values include:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **started** *(datetime) --* 

            The test's start time.

            
          

          - **stopped** *(datetime) --* 

            The test's stop time.

            
          

          - **counters** *(dict) --* 

            The test's result counters.

            
            

            - **total** *(integer) --* 

              The total number of entities.

              
            

            - **passed** *(integer) --* 

              The number of passed entities.

              
            

            - **failed** *(integer) --* 

              The number of failed entities.

              
            

            - **warned** *(integer) --* 

              The number of warned entities.

              
            

            - **errored** *(integer) --* 

              The number of errored entities.

              
            

            - **stopped** *(integer) --* 

              The number of stopped entities.

              
            

            - **skipped** *(integer) --* 

              The number of skipped entities.

              
        
          

          - **message** *(string) --* 

            A message about the test's result.

            
          

          - **deviceMinutes** *(dict) --* 

            Represents the total (metered or unmetered) minutes used by the test.

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
      
    

    **Examples** 

    The following example gets information about a specific test.
    ::

      response = client.get_test(
          # You can get the test ARN by using the list-tests CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:test:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'test': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_upload(**kwargs)

    

    Gets information about an upload.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetUpload>`_    


    **Request Syntax** 
    ::

      response = client.get_upload(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The upload's ARN.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'upload': {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
                'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                'url': 'string',
                'metadata': 'string',
                'contentType': 'string',
                'message': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a get upload request.

        
        

        - **upload** *(dict) --* 

          An app or a set of one or more tests to upload or that have been uploaded.

          
          

          - **arn** *(string) --* 

            The upload's ARN.

            
          

          - **name** *(string) --* 

            The upload's file name.

            
          

          - **created** *(datetime) --* 

            When the upload was created.

            
          

          - **type** *(string) --* 

            The upload's type.

             

            Must be one of the following values:

             

             
            * ANDROID_APP: An Android upload. 
             
            * IOS_APP: An iOS upload. 
             
            * WEB_APP: A web appliction upload. 
             
            * EXTERNAL_DATA: An external data upload. 
             
            * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
             
            * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
             
            * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
             
            * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
             
            * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
             
            * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
             
            * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
             
            * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
             
            * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
             
            * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
             
            * XCTEST_TEST_PACKAGE: An XCode test package upload. 
             
            * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
             

            
          

          - **status** *(string) --* 

            The upload's status.

             

            Must be one of the following values:

             

             
            * FAILED: A failed status. 
             
            * INITIALIZED: An initialized status. 
             
            * PROCESSING: A processing status. 
             
            * SUCCEEDED: A succeeded status. 
             

            
          

          - **url** *(string) --* 

            The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.

            
          

          - **metadata** *(string) --* 

            The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

            
          

          - **contentType** *(string) --* 

            The upload's content type (for example, "application/octet-stream").

            
          

          - **message** *(string) --* 

            A message about the upload's result.

            
      
    

    **Examples** 

    The following example gets information about a specific upload.
    ::

      response = client.get_upload(
          # You can get the test ARN by using the list-uploads CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:upload:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'upload': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: install_to_remote_access_session(**kwargs)

    

    Installs an application to the device in a remote access session. For Android applications, the file must be in .apk format. For iOS applications, the file must be in .ipa format.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/InstallToRemoteAccessSession>`_    


    **Request Syntax** 
    ::

      response = client.install_to_remote_access_session(
          remoteAccessSessionArn='string',
          appArn='string'
      )
    :type remoteAccessSessionArn: string
    :param remoteAccessSessionArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.

      

    
    :type appArn: string
    :param appArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the app about which you are requesting information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'appUpload': {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
                'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                'url': 'string',
                'metadata': 'string',
                'contentType': 'string',
                'message': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server after AWS Device Farm makes a request to install to a remote access session.

        
        

        - **appUpload** *(dict) --* 

          An app to upload or that has been uploaded.

          
          

          - **arn** *(string) --* 

            The upload's ARN.

            
          

          - **name** *(string) --* 

            The upload's file name.

            
          

          - **created** *(datetime) --* 

            When the upload was created.

            
          

          - **type** *(string) --* 

            The upload's type.

             

            Must be one of the following values:

             

             
            * ANDROID_APP: An Android upload. 
             
            * IOS_APP: An iOS upload. 
             
            * WEB_APP: A web appliction upload. 
             
            * EXTERNAL_DATA: An external data upload. 
             
            * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
             
            * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
             
            * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
             
            * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
             
            * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
             
            * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
             
            * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
             
            * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
             
            * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
             
            * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
             
            * XCTEST_TEST_PACKAGE: An XCode test package upload. 
             
            * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
             

            
          

          - **status** *(string) --* 

            The upload's status.

             

            Must be one of the following values:

             

             
            * FAILED: A failed status. 
             
            * INITIALIZED: An initialized status. 
             
            * PROCESSING: A processing status. 
             
            * SUCCEEDED: A succeeded status. 
             

            
          

          - **url** *(string) --* 

            The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.

            
          

          - **metadata** *(string) --* 

            The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

            
          

          - **contentType** *(string) --* 

            The upload's content type (for example, "application/octet-stream").

            
          

          - **message** *(string) --* 

            A message about the upload's result.

            
      
    

    **Examples** 

    The following example installs a specific app to a device in a specific remote access session.
    ::

      response = client.install_to_remote_access_session(
          appArn='arn:aws:devicefarm:us-west-2:123456789101:app:EXAMPLE-GUID-123-456',
          # You can get the remote access session ARN by using the list-remote-access-sessions CLI command.
          remoteAccessSessionArn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'appUpload': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_artifacts(**kwargs)

    

    Gets information about artifacts.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListArtifacts>`_    


    **Request Syntax** 
    ::

      response = client.list_artifacts(
          arn='string',
          type='SCREENSHOT'|'FILE'|'LOG',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Run, Job, Suite, or Test ARN.

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      The artifacts' type.

       

      Allowed values include:

       

       
      * FILE: The artifacts are files. 
       
      * LOG: The artifacts are logs. 
       
      * SCREENSHOT: The artifacts are screenshots. 
       

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'artifacts': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'UNKNOWN'|'SCREENSHOT'|'DEVICE_LOG'|'MESSAGE_LOG'|'VIDEO_LOG'|'RESULT_LOG'|'SERVICE_LOG'|'WEBKIT_LOG'|'INSTRUMENTATION_OUTPUT'|'EXERCISER_MONKEY_OUTPUT'|'CALABASH_JSON_OUTPUT'|'CALABASH_PRETTY_OUTPUT'|'CALABASH_STANDARD_OUTPUT'|'CALABASH_JAVA_XML_OUTPUT'|'AUTOMATION_OUTPUT'|'APPIUM_SERVER_OUTPUT'|'APPIUM_JAVA_OUTPUT'|'APPIUM_JAVA_XML_OUTPUT'|'APPIUM_PYTHON_OUTPUT'|'APPIUM_PYTHON_XML_OUTPUT'|'EXPLORER_EVENT_LOG'|'EXPLORER_SUMMARY_LOG'|'APPLICATION_CRASH_REPORT'|'XCTEST_LOG'|'VIDEO'|'CUSTOMER_ARTIFACT'|'CUSTOMER_ARTIFACT_LOG',
                    'extension': 'string',
                    'url': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list artifacts operation.

        
        

        - **artifacts** *(list) --* 

          Information about the artifacts.

          
          

          - *(dict) --* 

            Represents the output of a test. Examples of artifacts include logs and screenshots.

            
            

            - **arn** *(string) --* 

              The artifact's ARN.

              
            

            - **name** *(string) --* 

              The artifact's name.

              
            

            - **type** *(string) --* 

              The artifact's type.

               

              Allowed values include the following:

               

               
              * UNKNOWN: An unknown type. 
               
              * SCREENSHOT: The screenshot type. 
               
              * DEVICE_LOG: The device log type. 
               
              * MESSAGE_LOG: The message log type. 
               
              * RESULT_LOG: The result log type. 
               
              * SERVICE_LOG: The service log type. 
               
              * WEBKIT_LOG: The web kit log type. 
               
              * INSTRUMENTATION_OUTPUT: The instrumentation type. 
               
              * EXERCISER_MONKEY_OUTPUT: For Android, the artifact (log) generated by an Android fuzz test. 
               
              * CALABASH_JSON_OUTPUT: The Calabash JSON output type. 
               
              * CALABASH_PRETTY_OUTPUT: The Calabash pretty output type. 
               
              * CALABASH_STANDARD_OUTPUT: The Calabash standard output type. 
               
              * CALABASH_JAVA_XML_OUTPUT: The Calabash Java XML output type. 
               
              * AUTOMATION_OUTPUT: The automation output type. 
               
              * APPIUM_SERVER_OUTPUT: The Appium server output type. 
               
              * APPIUM_JAVA_OUTPUT: The Appium Java output type. 
               
              * APPIUM_JAVA_XML_OUTPUT: The Appium Java XML output type. 
               
              * APPIUM_PYTHON_OUTPUT: The Appium Python output type. 
               
              * APPIUM_PYTHON_XML_OUTPUT: The Appium Python XML output type. 
               
              * EXPLORER_EVENT_LOG: The Explorer event log output type. 
               
              * EXPLORER_SUMMARY_LOG: The Explorer summary log output type. 
               
              * APPLICATION_CRASH_REPORT: The application crash report output type. 
               
              * XCTEST_LOG: The XCode test output type. 
               

              
            

            - **extension** *(string) --* 

              The artifact's file extension.

              
            

            - **url** *(string) --* 

              The pre-signed Amazon S3 URL that can be used with a corresponding GET request to download the artifact's file.

              
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example lists screenshot artifacts for a specific run.
    ::

      response = client.list_artifacts(
          type='SCREENSHOT',
          # Can also be used to list artifacts for a Job, Suite, or Test ARN.
          arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_device_pools(**kwargs)

    

    Gets information about device pools.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevicePools>`_    


    **Request Syntax** 
    ::

      response = client.list_device_pools(
          arn='string',
          type='CURATED'|'PRIVATE',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The project ARN.

      

    
    :type type: string
    :param type: 

      The device pools' type.

       

      Allowed values include:

       

       
      * CURATED: A device pool that is created and managed by AWS Device Farm. 
       
      * PRIVATE: A device pool that is created and managed by the device pool developer. 
       

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'devicePools': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'rules': [
                        {
                            'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION',
                            'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list device pools request.

        
        

        - **devicePools** *(list) --* 

          Information about the device pools.

          
          

          - *(dict) --* 

            Represents a collection of device types.

            
            

            - **arn** *(string) --* 

              The device pool's ARN.

              
            

            - **name** *(string) --* 

              The device pool's name.

              
            

            - **description** *(string) --* 

              The device pool's description.

              
            

            - **type** *(string) --* 

              The device pool's type.

               

              Allowed values include:

               

               
              * CURATED: A device pool that is created and managed by AWS Device Farm. 
               
              * PRIVATE: A device pool that is created and managed by the device pool developer. 
               

              
            

            - **rules** *(list) --* 

              Information about the device pool's rules.

              
              

              - *(dict) --* 

                Represents a condition for a device pool.

                
                

                - **attribute** *(string) --* 

                  The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .

                   

                  Allowed values include:

                   

                   
                  * ARN: The ARN. 
                   
                  * FORM_FACTOR: The form factor (for example, phone or tablet). 
                   
                  * MANUFACTURER: The manufacturer. 
                   
                  * PLATFORM: The platform (for example, Android or iOS). 
                   
                  * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                   
                  * APPIUM_VERSION: The Appium version for the test. 
                   

                  
                

                - **operator** *(string) --* 

                  The rule's operator.

                   

                   
                  * EQUALS: The equals operator. 
                   
                  * GREATER_THAN: The greater-than operator. 
                   
                  * IN: The in operator. 
                   
                  * LESS_THAN: The less-than operator. 
                   
                  * NOT_IN: The not-in operator. 
                   
                  * CONTAINS: The contains operator. 
                   

                  
                

                - **value** *(string) --* 

                  The rule's value.

                  
            
          
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about the private device pools in a specific project.
    ::

      response = client.list_device_pools(
          type='PRIVATE',
          # You can get the project ARN by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'devicePools': [
              {
                  'name': 'Top Devices',
                  'arn': 'arn:aws:devicefarm:us-west-2::devicepool:082d10e5-d7d7-48a5-ba5c-12345EXAMPLE',
                  'description': 'Top devices',
                  'rules': [
                      {
                          'value': '["arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE"]',
                          'attribute': 'ARN',
                          'operator': 'IN',
                      },
                  ],
              },
              {
                  'name': 'My Android Device Pool',
                  'arn': 'arn:aws:devicefarm:us-west-2:123456789101:devicepool:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/bf96e75a-28f6-4e61-b6a7-12345EXAMPLE',
                  'description': 'Samsung Galaxy Android devices',
                  'rules': [
                      {
                          'value': '["arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE"]',
                          'attribute': 'ARN',
                          'operator': 'IN',
                      },
                  ],
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_devices(**kwargs)

    

    Gets information about unique device types.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevices>`_    


    **Request Syntax** 
    ::

      response = client.list_devices(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: 

      The Amazon Resource Name (ARN) of the project.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'devices': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list devices operation.

        
        

        - **devices** *(list) --* 

          Information about the devices.

          
          

          - *(dict) --* 

            Represents a device type that an app is tested against.

            
            

            - **arn** *(string) --* 

              The device's ARN.

              
            

            - **name** *(string) --* 

              The device's display name.

              
            

            - **manufacturer** *(string) --* 

              The device's manufacturer name.

              
            

            - **model** *(string) --* 

              The device's model name.

              
            

            - **formFactor** *(string) --* 

              The device's form factor.

               

              Allowed values include:

               

               
              * PHONE: The phone form factor. 
               
              * TABLET: The tablet form factor. 
               

              
            

            - **platform** *(string) --* 

              The device's platform.

               

              Allowed values include:

               

               
              * ANDROID: The Android platform. 
               
              * IOS: The iOS platform. 
               

              
            

            - **os** *(string) --* 

              The device's operating system type.

              
            

            - **cpu** *(dict) --* 

              Information about the device's CPU.

              
              

              - **frequency** *(string) --* 

                The CPU's frequency.

                
              

              - **architecture** *(string) --* 

                The CPU's architecture, for example x86 or ARM.

                
              

              - **clock** *(float) --* 

                The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                
          
            

            - **resolution** *(dict) --* 

              The resolution of the device.

              
              

              - **width** *(integer) --* 

                The screen resolution's width, expressed in pixels.

                
              

              - **height** *(integer) --* 

                The screen resolution's height, expressed in pixels.

                
          
            

            - **heapSize** *(integer) --* 

              The device's heap size, expressed in bytes.

              
            

            - **memory** *(integer) --* 

              The device's total memory size, expressed in bytes.

              
            

            - **image** *(string) --* 

              The device's image name.

              
            

            - **carrier** *(string) --* 

              The device's carrier.

              
            

            - **radio** *(string) --* 

              The device's radio.

              
            

            - **remoteAccessEnabled** *(boolean) --* 

              Specifies whether remote access has been enabled for the specified device.

              
            

            - **remoteDebugEnabled** *(boolean) --* 

              This flag is set to ``true`` if remote debugging is enabled for the device.

              
            

            - **fleetType** *(string) --* 

              The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

              
            

            - **fleetName** *(string) --* 

              The name of the fleet to which this device belongs.

              
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about the available devices in a specific project.
    ::

      response = client.list_devices(
          # You can get the project ARN by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_jobs(**kwargs)

    

    Gets information about jobs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListJobs>`_    


    **Request Syntax** 
    ::

      response = client.list_jobs(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The jobs' ARNs.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobs': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string'
                    },
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list jobs request.

        
        

        - **jobs** *(list) --* 

          Information about the jobs.

          
          

          - *(dict) --* 

            Represents a device.

            
            

            - **arn** *(string) --* 

              The job's ARN.

              
            

            - **name** *(string) --* 

              The job's name.

              
            

            - **type** *(string) --* 

              The job's type.

               

              Allowed values include the following:

               

               
              * BUILTIN_FUZZ: The built-in fuzz type. 
               
              * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
               
              * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
               
              * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
               
              * APPIUM_PYTHON: The Appium Python type. 
               
              * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
               
              * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
               
              * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
               
              * CALABASH: The Calabash type. 
               
              * INSTRUMENTATION: The Instrumentation type. 
               
              * UIAUTOMATION: The uiautomation type. 
               
              * UIAUTOMATOR: The uiautomator type. 
               
              * XCTEST: The XCode test type. 
               
              * XCTEST_UI: The XCode UI test type. 
               

              
            

            - **created** *(datetime) --* 

              When the job was created.

              
            

            - **status** *(string) --* 

              The job's status.

               

              Allowed values include:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The job's result.

               

              Allowed values include:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **started** *(datetime) --* 

              The job's start time.

              
            

            - **stopped** *(datetime) --* 

              The job's stop time.

              
            

            - **counters** *(dict) --* 

              The job's result counters.

              
              

              - **total** *(integer) --* 

                The total number of entities.

                
              

              - **passed** *(integer) --* 

                The number of passed entities.

                
              

              - **failed** *(integer) --* 

                The number of failed entities.

                
              

              - **warned** *(integer) --* 

                The number of warned entities.

                
              

              - **errored** *(integer) --* 

                The number of errored entities.

                
              

              - **stopped** *(integer) --* 

                The number of stopped entities.

                
              

              - **skipped** *(integer) --* 

                The number of skipped entities.

                
          
            

            - **message** *(string) --* 

              A message about the job's result.

              
            

            - **device** *(dict) --* 

              The device (phone or tablet).

              
              

              - **arn** *(string) --* 

                The device's ARN.

                
              

              - **name** *(string) --* 

                The device's display name.

                
              

              - **manufacturer** *(string) --* 

                The device's manufacturer name.

                
              

              - **model** *(string) --* 

                The device's model name.

                
              

              - **formFactor** *(string) --* 

                The device's form factor.

                 

                Allowed values include:

                 

                 
                * PHONE: The phone form factor. 
                 
                * TABLET: The tablet form factor. 
                 

                
              

              - **platform** *(string) --* 

                The device's platform.

                 

                Allowed values include:

                 

                 
                * ANDROID: The Android platform. 
                 
                * IOS: The iOS platform. 
                 

                
              

              - **os** *(string) --* 

                The device's operating system type.

                
              

              - **cpu** *(dict) --* 

                Information about the device's CPU.

                
                

                - **frequency** *(string) --* 

                  The CPU's frequency.

                  
                

                - **architecture** *(string) --* 

                  The CPU's architecture, for example x86 or ARM.

                  
                

                - **clock** *(float) --* 

                  The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                  
            
              

              - **resolution** *(dict) --* 

                The resolution of the device.

                
                

                - **width** *(integer) --* 

                  The screen resolution's width, expressed in pixels.

                  
                

                - **height** *(integer) --* 

                  The screen resolution's height, expressed in pixels.

                  
            
              

              - **heapSize** *(integer) --* 

                The device's heap size, expressed in bytes.

                
              

              - **memory** *(integer) --* 

                The device's total memory size, expressed in bytes.

                
              

              - **image** *(string) --* 

                The device's image name.

                
              

              - **carrier** *(string) --* 

                The device's carrier.

                
              

              - **radio** *(string) --* 

                The device's radio.

                
              

              - **remoteAccessEnabled** *(boolean) --* 

                Specifies whether remote access has been enabled for the specified device.

                
              

              - **remoteDebugEnabled** *(boolean) --* 

                This flag is set to ``true`` if remote debugging is enabled for the device.

                
              

              - **fleetType** *(string) --* 

                The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

                
              

              - **fleetName** *(string) --* 

                The name of the fleet to which this device belongs.

                
          
            

            - **deviceMinutes** *(dict) --* 

              Represents the total (metered or unmetered) minutes used by the job.

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about jobs in a specific project.
    ::

      response = client.list_jobs(
          # You can get the project ARN by using the list-jobs CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_network_profiles(**kwargs)

    

    Returns the list of available network profiles.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListNetworkProfiles>`_    


    **Request Syntax** 
    ::

      response = client.list_network_profiles(
          arn='string',
          type='CURATED'|'PRIVATE',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to list network profiles.

      

    
    :type type: string
    :param type: 

      The type of network profile you wish to return information about. Valid values are listed below.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'networkProfiles': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **networkProfiles** *(list) --* 

          A list of the available network profiles.

          
          

          - *(dict) --* 

            An array of settings that describes characteristics of a network profile.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the network profile.

              
            

            - **name** *(string) --* 

              The name of the network profile.

              
            

            - **description** *(string) --* 

              The description of the network profile.

              
            

            - **type** *(string) --* 

              The type of network profile. Valid values are listed below.

              
            

            - **uplinkBandwidthBits** *(integer) --* 

              The data throughput rate in bits per second, as an integer from 0 to 104857600.

              
            

            - **downlinkBandwidthBits** *(integer) --* 

              The data throughput rate in bits per second, as an integer from 0 to 104857600.

              
            

            - **uplinkDelayMs** *(integer) --* 

              Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

              
            

            - **downlinkDelayMs** *(integer) --* 

              Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

              
            

            - **uplinkJitterMs** *(integer) --* 

              Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

              
            

            - **downlinkJitterMs** *(integer) --* 

              Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

              
            

            - **uplinkLossPercent** *(integer) --* 

              Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

              
            

            - **downlinkLossPercent** *(integer) --* 

              Proportion of received packets that fail to arrive from 0 to 100 percent.

              
        
      
        

        - **nextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

  .. py:method:: list_offering_promotions(**kwargs)

    

    Returns a list of offering promotions. Each offering promotion record contains the ID and description of the promotion. The API returns a ``NotEligible`` error if the caller is not permitted to invoke the operation. Contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferingPromotions>`_    


    **Request Syntax** 
    ::

      response = client.list_offering_promotions(
          nextToken='string'
      )
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'offeringPromotions': [
                {
                    'id': 'string',
                    'description': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **offeringPromotions** *(list) --* 

          Information about the offering promotions.

          
          

          - *(dict) --* 

            Represents information about an offering promotion.

            
            

            - **id** *(string) --* 

              The ID of the offering promotion.

              
            

            - **description** *(string) --* 

              A string describing the offering promotion.

              
        
      
        

        - **nextToken** *(string) --* 

          An identifier to be used in the next call to this operation, to return the next set of items in the list.

          
    

  .. py:method:: list_offering_transactions(**kwargs)

    

    Returns a list of all historical purchases, renewals, and system renewal transactions for an AWS account. The list is paginated and ordered by a descending timestamp (most recent transactions are first). The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferingTransactions>`_    


    **Request Syntax** 
    ::

      response = client.list_offering_transactions(
          nextToken='string'
      )
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'offeringTransactions': [
                {
                    'offeringStatus': {
                        'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                        'offering': {
                            'id': 'string',
                            'description': 'string',
                            'type': 'RECURRING',
                            'platform': 'ANDROID'|'IOS',
                            'recurringCharges': [
                                {
                                    'cost': {
                                        'amount': 123.0,
                                        'currencyCode': 'USD'
                                    },
                                    'frequency': 'MONTHLY'
                                },
                            ]
                        },
                        'quantity': 123,
                        'effectiveOn': datetime(2015, 1, 1)
                    },
                    'transactionId': 'string',
                    'offeringPromotionId': 'string',
                    'createdOn': datetime(2015, 1, 1),
                    'cost': {
                        'amount': 123.0,
                        'currencyCode': 'USD'
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the transaction log of the specified offerings.

        
        

        - **offeringTransactions** *(list) --* 

          The audit log of subscriptions you have purchased and modified through AWS Device Farm.

          
          

          - *(dict) --* 

            Represents the metadata of an offering transaction.

            
            

            - **offeringStatus** *(dict) --* 

              The status of an offering transaction.

              
              

              - **type** *(string) --* 

                The type specified for the offering status.

                
              

              - **offering** *(dict) --* 

                Represents the metadata of an offering status.

                
                

                - **id** *(string) --* 

                  The ID that corresponds to a device offering.

                  
                

                - **description** *(string) --* 

                  A string describing the offering.

                  
                

                - **type** *(string) --* 

                  The type of offering (e.g., "RECURRING") for a device.

                  
                

                - **platform** *(string) --* 

                  The platform of the device (e.g., ANDROID or IOS).

                  
                

                - **recurringCharges** *(list) --* 

                  Specifies whether there are recurring charges for the offering.

                  
                  

                  - *(dict) --* 

                    Specifies whether charges for devices will be recurring.

                    
                    

                    - **cost** *(dict) --* 

                      The cost of the recurring charge.

                      
                      

                      - **amount** *(float) --* 

                        The numerical amount of an offering or transaction.

                        
                      

                      - **currencyCode** *(string) --* 

                        The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                        
                  
                    

                    - **frequency** *(string) --* 

                      The frequency in which charges will recur.

                      
                
              
            
              

              - **quantity** *(integer) --* 

                The number of available devices in the offering.

                
              

              - **effectiveOn** *(datetime) --* 

                The date on which the offering is effective.

                
          
            

            - **transactionId** *(string) --* 

              The transaction ID of the offering transaction.

              
            

            - **offeringPromotionId** *(string) --* 

              The ID that corresponds to a device offering promotion.

              
            

            - **createdOn** *(datetime) --* 

              The date on which an offering transaction was created.

              
            

            - **cost** *(dict) --* 

              The cost of an offering transaction.

              
              

              - **amount** *(float) --* 

                The numerical amount of an offering or transaction.

                
              

              - **currencyCode** *(string) --* 

                The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                
          
        
      
        

        - **nextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about Device Farm offering transactions.
    ::

      response = client.list_offering_transactions(
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'offeringTransactions': [
              {
                  'cost': {
                      'amount': 0,
                      'currencyCode': 'USD',
                  },
                  'createdOn': datetime(2016, 7, 31, 20, 17, 0, 6, 213, 1),
                  'offeringStatus': {
                      'type': 'RENEW',
                      'effectiveOn': datetime(2016, 8, 31, 17, 0, 0, 2, 244, 1),
                      'offering': {
                          'type': 'RECURRING',
                          'description': 'Android Remote Access Unmetered Device Slot',
                          'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                          'platform': 'ANDROID',
                      },
                      'quantity': 0,
                  },
                  'transactionId': '03728003-d1ea-4851-abd6-12345EXAMPLE',
              },
              {
                  'cost': {
                      'amount': 250,
                      'currencyCode': 'USD',
                  },
                  'createdOn': datetime(2016, 7, 31, 20, 17, 0, 6, 213, 1),
                  'offeringStatus': {
                      'type': 'PURCHASE',
                      'effectiveOn': datetime(2016, 7, 31, 20, 17, 0, 6, 213, 1),
                      'offering': {
                          'type': 'RECURRING',
                          'description': 'Android Remote Access Unmetered Device Slot',
                          'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                          'platform': 'ANDROID',
                      },
                      'quantity': 1,
                  },
                  'transactionId': '56820b6e-06bd-473a-8ff8-12345EXAMPLE',
              },
              {
                  'cost': {
                      'amount': 175,
                      'currencyCode': 'USD',
                  },
                  'createdOn': datetime(2016, 6, 9, 23, 2, 0, 3, 161, 1),
                  'offeringStatus': {
                      'type': 'PURCHASE',
                      'effectiveOn': datetime(2016, 6, 9, 23, 2, 0, 3, 161, 1),
                      'offering': {
                          'type': 'RECURRING',
                          'description': 'Android Unmetered Device Slot',
                          'id': '8980F81C-00D7-469D-8EC6-12345EXAMPLE',
                          'platform': 'ANDROID',
                      },
                      'quantity': 1,
                  },
                  'transactionId': '953ae2c6-d760-4a04-9597-12345EXAMPLE',
              },
              {
                  'cost': {
                      'amount': 8.07,
                      'currencyCode': 'USD',
                  },
                  'createdOn': datetime(2016, 3, 30, 6, 25, 0, 2, 90, 1),
                  'offeringStatus': {
                      'type': 'PURCHASE',
                      'effectiveOn': datetime(2016, 3, 30, 6, 25, 0, 2, 90, 1),
                      'offering': {
                          'type': 'RECURRING',
                          'description': 'iOS Unmetered Device Slot',
                          'id': 'A53D4D73-A6F6-4B82-A0B0-12345EXAMPLE',
                          'platform': 'IOS',
                      },
                      'quantity': 1,
                  },
                  'transactionId': '2baf9021-ae3e-47f5-ab52-12345EXAMPLE',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_offerings(**kwargs)

    

    Returns a list of products or offerings that the user can manage through the API. Each offering record indicates the recurring price per unit and the frequency for that offering. The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferings>`_    


    **Request Syntax** 
    ::

      response = client.list_offerings(
          nextToken='string'
      )
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'offerings': [
                {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the return values of the list of offerings.

        
        

        - **offerings** *(list) --* 

          A value representing the list offering results.

          
          

          - *(dict) --* 

            Represents the metadata of a device offering.

            
            

            - **id** *(string) --* 

              The ID that corresponds to a device offering.

              
            

            - **description** *(string) --* 

              A string describing the offering.

              
            

            - **type** *(string) --* 

              The type of offering (e.g., "RECURRING") for a device.

              
            

            - **platform** *(string) --* 

              The platform of the device (e.g., ANDROID or IOS).

              
            

            - **recurringCharges** *(list) --* 

              Specifies whether there are recurring charges for the offering.

              
              

              - *(dict) --* 

                Specifies whether charges for devices will be recurring.

                
                

                - **cost** *(dict) --* 

                  The cost of the recurring charge.

                  
                  

                  - **amount** *(float) --* 

                    The numerical amount of an offering or transaction.

                    
                  

                  - **currencyCode** *(string) --* 

                    The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                    
              
                

                - **frequency** *(string) --* 

                  The frequency in which charges will recur.

                  
            
          
        
      
        

        - **nextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about available device offerings.
    ::

      response = client.list_offerings(
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'offerings': [
              {
                  'type': 'RECURRING',
                  'description': 'iOS Unmetered Device Slot',
                  'id': 'A53D4D73-A6F6-4B82-A0B0-12345EXAMPLE',
                  'platform': 'IOS',
                  'recurringCharges': [
                      {
                          'cost': {
                              'amount': 250,
                              'currencyCode': 'USD',
                          },
                          'frequency': 'MONTHLY',
                      },
                  ],
              },
              {
                  'type': 'RECURRING',
                  'description': 'Android Unmetered Device Slot',
                  'id': '8980F81C-00D7-469D-8EC6-12345EXAMPLE',
                  'platform': 'ANDROID',
                  'recurringCharges': [
                      {
                          'cost': {
                              'amount': 250,
                              'currencyCode': 'USD',
                          },
                          'frequency': 'MONTHLY',
                      },
                  ],
              },
              {
                  'type': 'RECURRING',
                  'description': 'Android Remote Access Unmetered Device Slot',
                  'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                  'platform': 'ANDROID',
                  'recurringCharges': [
                      {
                          'cost': {
                              'amount': 250,
                              'currencyCode': 'USD',
                          },
                          'frequency': 'MONTHLY',
                      },
                  ],
              },
              {
                  'type': 'RECURRING',
                  'description': 'iOS Remote Access Unmetered Device Slot',
                  'id': '552B4DAD-A6C9-45C4-94FB-12345EXAMPLE',
                  'platform': 'IOS',
                  'recurringCharges': [
                      {
                          'cost': {
                              'amount': 250,
                              'currencyCode': 'USD',
                          },
                          'frequency': 'MONTHLY',
                      },
                  ],
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_projects(**kwargs)

    

    Gets information about projects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListProjects>`_    


    **Request Syntax** 
    ::

      response = client.list_projects(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: 

      Optional. If no Amazon Resource Name (ARN) is specified, then AWS Device Farm returns a list of all projects for the AWS account. You can also specify a project ARN.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'projects': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'defaultJobTimeoutMinutes': 123,
                    'created': datetime(2015, 1, 1)
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list projects request.

        
        

        - **projects** *(list) --* 

          Information about the projects.

          
          

          - *(dict) --* 

            Represents an operating-system neutral workspace for running and managing tests.

            
            

            - **arn** *(string) --* 

              The project's ARN.

              
            

            - **name** *(string) --* 

              The project's name.

              
            

            - **defaultJobTimeoutMinutes** *(integer) --* 

              The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.

              
            

            - **created** *(datetime) --* 

              When the project was created.

              
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about the specified project in Device Farm.
    ::

      response = client.list_projects(
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:7ad300ed-8183-41a7-bf94-12345EXAMPLE',
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'projects': [
              {
                  'name': 'My Test Project',
                  'arn': 'arn:aws:devicefarm:us-west-2:183774035805:project:7ad300ed-8183-41a7-bf94-12345EXAMPLE',
                  'created': datetime(2016, 1, 18, 16, 27, 42, 0, 18, 0),
              },
              {
                  'name': 'Hello World',
                  'arn': 'arn:aws:devicefarm:us-west-2:183774035805:project:d6b087d9-56db-4e44-b9ec-12345EXAMPLE',
                  'created': datetime(2016, 8, 4, 15, 35, 12, 3, 217, 1),
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_remote_access_sessions(**kwargs)

    

    Returns a list of all currently running remote access sessions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListRemoteAccessSessions>`_    


    **Request Syntax** 
    ::

      response = client.list_remote_access_sessions(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'remoteAccessSessions': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'message': 'string',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string'
                    },
                    'remoteDebugEnabled': True|False,
                    'hostAddress': 'string',
                    'clientId': 'string',
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'endpoint': 'string',
                    'deviceUdid': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server after AWS Device Farm makes a request to return information about the remote access session.

        
        

        - **remoteAccessSessions** *(list) --* 

          A container representing the metadata from the service about each remote access session you are requesting.

          
          

          - *(dict) --* 

            Represents information about the remote access session.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the remote access session.

              
            

            - **name** *(string) --* 

              The name of the remote access session.

              
            

            - **created** *(datetime) --* 

              The date and time the remote access session was created.

              
            

            - **status** *(string) --* 

              The status of the remote access session. Can be any of the following:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The result of the remote access session. Can be any of the following:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **message** *(string) --* 

              A message about the remote access session.

              
            

            - **started** *(datetime) --* 

              The date and time the remote access session was started.

              
            

            - **stopped** *(datetime) --* 

              The date and time the remote access session was stopped.

              
            

            - **device** *(dict) --* 

              The device (phone or tablet) used in the remote access session.

              
              

              - **arn** *(string) --* 

                The device's ARN.

                
              

              - **name** *(string) --* 

                The device's display name.

                
              

              - **manufacturer** *(string) --* 

                The device's manufacturer name.

                
              

              - **model** *(string) --* 

                The device's model name.

                
              

              - **formFactor** *(string) --* 

                The device's form factor.

                 

                Allowed values include:

                 

                 
                * PHONE: The phone form factor. 
                 
                * TABLET: The tablet form factor. 
                 

                
              

              - **platform** *(string) --* 

                The device's platform.

                 

                Allowed values include:

                 

                 
                * ANDROID: The Android platform. 
                 
                * IOS: The iOS platform. 
                 

                
              

              - **os** *(string) --* 

                The device's operating system type.

                
              

              - **cpu** *(dict) --* 

                Information about the device's CPU.

                
                

                - **frequency** *(string) --* 

                  The CPU's frequency.

                  
                

                - **architecture** *(string) --* 

                  The CPU's architecture, for example x86 or ARM.

                  
                

                - **clock** *(float) --* 

                  The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                  
            
              

              - **resolution** *(dict) --* 

                The resolution of the device.

                
                

                - **width** *(integer) --* 

                  The screen resolution's width, expressed in pixels.

                  
                

                - **height** *(integer) --* 

                  The screen resolution's height, expressed in pixels.

                  
            
              

              - **heapSize** *(integer) --* 

                The device's heap size, expressed in bytes.

                
              

              - **memory** *(integer) --* 

                The device's total memory size, expressed in bytes.

                
              

              - **image** *(string) --* 

                The device's image name.

                
              

              - **carrier** *(string) --* 

                The device's carrier.

                
              

              - **radio** *(string) --* 

                The device's radio.

                
              

              - **remoteAccessEnabled** *(boolean) --* 

                Specifies whether remote access has been enabled for the specified device.

                
              

              - **remoteDebugEnabled** *(boolean) --* 

                This flag is set to ``true`` if remote debugging is enabled for the device.

                
              

              - **fleetType** *(string) --* 

                The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

                
              

              - **fleetName** *(string) --* 

                The name of the fleet to which this device belongs.

                
          
            

            - **remoteDebugEnabled** *(boolean) --* 

              This flag is set to ``true`` if remote debugging is enabled for the remote access session.

              
            

            - **hostAddress** *(string) --* 

              IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.

              
            

            - **clientId** *(string) --* 

              Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.

              
            

            - **billingMethod** *(string) --* 

              The billing method of the remote access session. Possible values include ``METERED`` or ``UNMETERED`` . For more information about metered devices, see `AWS Device Farm terminology <http://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology>`__ ."

              
            

            - **deviceMinutes** *(dict) --* 

              The number of minutes a device is used in a remote access sesssion (including setup and teardown minutes).

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
            

            - **endpoint** *(string) --* 

              The endpoint for the remote access sesssion.

              
            

            - **deviceUdid** *(string) --* 

              Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.

              
        
      
        

        - **nextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about a specific Device Farm remote access session.
    ::

      response = client.list_remote_access_sessions(
          # You can get the Amazon Resource Name (ARN) of the session by using the list-sessions CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456',
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'remoteAccessSessions': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_runs(**kwargs)

    

    Gets information about runs, given an AWS Device Farm project ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListRuns>`_    


    **Request Syntax** 
    ::

      response = client.list_runs(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to list runs.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'runs': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                    'platform': 'ANDROID'|'IOS',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'totalJobs': 123,
                    'completedJobs': 123,
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'networkProfile': {
                        'arn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'CURATED'|'PRIVATE',
                        'uplinkBandwidthBits': 123,
                        'downlinkBandwidthBits': 123,
                        'uplinkDelayMs': 123,
                        'downlinkDelayMs': 123,
                        'uplinkJitterMs': 123,
                        'downlinkJitterMs': 123,
                        'uplinkLossPercent': 123,
                        'downlinkLossPercent': 123
                    },
                    'parsingResultUrl': 'string',
                    'resultCode': 'PARSING_FAILED',
                    'customerArtifactPaths': {
                        'iosPaths': [
                            'string',
                        ],
                        'androidPaths': [
                            'string',
                        ],
                        'deviceHostPaths': [
                            'string',
                        ]
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list runs request.

        
        

        - **runs** *(list) --* 

          Information about the runs.

          
          

          - *(dict) --* 

            Represents a test run on a set of devices with a given app package, test parameters, etc.

            
            

            - **arn** *(string) --* 

              The run's ARN.

              
            

            - **name** *(string) --* 

              The run's name.

              
            

            - **type** *(string) --* 

              The run's type.

               

              Must be one of the following values:

               

               
              * BUILTIN_FUZZ: The built-in fuzz type. 
               
              * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
               
              * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
               
              * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
               
              * APPIUM_PYTHON: The Appium Python type. 
               
              * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
               
              * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
               
              * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
               
              * CALABASH: The Calabash type. 
               
              * INSTRUMENTATION: The Instrumentation type. 
               
              * UIAUTOMATION: The uiautomation type. 
               
              * UIAUTOMATOR: The uiautomator type. 
               
              * XCTEST: The XCode test type. 
               
              * XCTEST_UI: The XCode UI test type. 
               

              
            

            - **platform** *(string) --* 

              The run's platform.

               

              Allowed values include:

               

               
              * ANDROID: The Android platform. 
               
              * IOS: The iOS platform. 
               

              
            

            - **created** *(datetime) --* 

              When the run was created.

              
            

            - **status** *(string) --* 

              The run's status.

               

              Allowed values include:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The run's result.

               

              Allowed values include:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **started** *(datetime) --* 

              The run's start time.

              
            

            - **stopped** *(datetime) --* 

              The run's stop time.

              
            

            - **counters** *(dict) --* 

              The run's result counters.

              
              

              - **total** *(integer) --* 

                The total number of entities.

                
              

              - **passed** *(integer) --* 

                The number of passed entities.

                
              

              - **failed** *(integer) --* 

                The number of failed entities.

                
              

              - **warned** *(integer) --* 

                The number of warned entities.

                
              

              - **errored** *(integer) --* 

                The number of errored entities.

                
              

              - **stopped** *(integer) --* 

                The number of stopped entities.

                
              

              - **skipped** *(integer) --* 

                The number of skipped entities.

                
          
            

            - **message** *(string) --* 

              A message about the run's result.

              
            

            - **totalJobs** *(integer) --* 

              The total number of jobs for the run.

              
            

            - **completedJobs** *(integer) --* 

              The total number of completed jobs.

              
            

            - **billingMethod** *(string) --* 

              Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .

              
            

            - **deviceMinutes** *(dict) --* 

              Represents the total (metered or unmetered) minutes used by the test run.

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
            

            - **networkProfile** *(dict) --* 

              The network profile being used for a test run.

              
              

              - **arn** *(string) --* 

                The Amazon Resource Name (ARN) of the network profile.

                
              

              - **name** *(string) --* 

                The name of the network profile.

                
              

              - **description** *(string) --* 

                The description of the network profile.

                
              

              - **type** *(string) --* 

                The type of network profile. Valid values are listed below.

                
              

              - **uplinkBandwidthBits** *(integer) --* 

                The data throughput rate in bits per second, as an integer from 0 to 104857600.

                
              

              - **downlinkBandwidthBits** *(integer) --* 

                The data throughput rate in bits per second, as an integer from 0 to 104857600.

                
              

              - **uplinkDelayMs** *(integer) --* 

                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

                
              

              - **downlinkDelayMs** *(integer) --* 

                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

                
              

              - **uplinkJitterMs** *(integer) --* 

                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

                
              

              - **downlinkJitterMs** *(integer) --* 

                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

                
              

              - **uplinkLossPercent** *(integer) --* 

                Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

                
              

              - **downlinkLossPercent** *(integer) --* 

                Proportion of received packets that fail to arrive from 0 to 100 percent.

                
          
            

            - **parsingResultUrl** *(string) --* 

              Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.

              
            

            - **resultCode** *(string) --* 

              Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.

              
            

            - **customerArtifactPaths** *(dict) --* 

              Output ``CustomerArtifactPaths`` object for the test run.

              
              

              - **iosPaths** *(list) --* 

                Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.

                
                

                - *(string) --* 
            
              

              - **androidPaths** *(list) --* 

                Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.

                
                

                - *(string) --* 
            
              

              - **deviceHostPaths** *(list) --* 

                Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.

                
                

                - *(string) --* 
            
          
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about a specific test run.
    ::

      response = client.list_runs(
          # You can get the Amazon Resource Name (ARN) of the run by using the list-runs CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/0fcac17b-6122-44d7-ae5a-12345EXAMPLE',
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'runs': [
              {
                  'name': 'My Test Run',
                  'type': 'BUILTIN_EXPLORER',
                  'arn': 'arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/0fcac17b-6122-44d7-ae5a-12345EXAMPLE',
                  'billingMethod': 'METERED',
                  'completedJobs': 0,
                  'counters': {
                      'errored': 0,
                      'failed': 0,
                      'passed': 0,
                      'skipped': 0,
                      'stopped': 0,
                      'total': 0,
                      'warned': 0,
                  },
                  'created': datetime(2016, 8, 31, 11, 18, 29, 2, 244, 1),
                  'deviceMinutes': {
                      'metered': 0.0,
                      'total': 0.0,
                      'unmetered': 0.0,
                  },
                  'platform': 'ANDROID',
                  'result': 'PENDING',
                  'status': 'RUNNING',
                  'totalJobs': 3,
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_samples(**kwargs)

    

    Gets information about samples, given an AWS Device Farm project ARN

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListSamples>`_    


    **Request Syntax** 
    ::

      response = client.list_samples(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to list samples.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'samples': [
                {
                    'arn': 'string',
                    'type': 'CPU'|'MEMORY'|'THREADS'|'RX_RATE'|'TX_RATE'|'RX'|'TX'|'NATIVE_FRAMES'|'NATIVE_FPS'|'NATIVE_MIN_DRAWTIME'|'NATIVE_AVG_DRAWTIME'|'NATIVE_MAX_DRAWTIME'|'OPENGL_FRAMES'|'OPENGL_FPS'|'OPENGL_MIN_DRAWTIME'|'OPENGL_AVG_DRAWTIME'|'OPENGL_MAX_DRAWTIME',
                    'url': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list samples request.

        
        

        - **samples** *(list) --* 

          Information about the samples.

          
          

          - *(dict) --* 

            Represents a sample of performance data.

            
            

            - **arn** *(string) --* 

              The sample's ARN.

              
            

            - **type** *(string) --* 

              The sample's type.

               

              Must be one of the following values:

               

               
              * CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage. 
               
              * MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes. 
               
              * NATIVE_AVG_DRAWTIME 
               
              * NATIVE_FPS 
               
              * NATIVE_FRAMES 
               
              * NATIVE_MAX_DRAWTIME 
               
              * NATIVE_MIN_DRAWTIME 
               
              * OPENGL_AVG_DRAWTIME 
               
              * OPENGL_FPS 
               
              * OPENGL_FRAMES 
               
              * OPENGL_MAX_DRAWTIME 
               
              * OPENGL_MIN_DRAWTIME 
               
              * RX 
               
              * RX_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process. 
               
              * THREADS: A threads sample type. This is expressed as the total number of threads per app process. 
               
              * TX 
               
              * TX_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process. 
               

              
            

            - **url** *(string) --* 

              The pre-signed Amazon S3 URL that can be used with a corresponding GET request to download the sample's file.

              
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about samples, given a specific Device Farm project.
    ::

      response = client.list_samples(
          # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'samples': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_suites(**kwargs)

    

    Gets information about suites.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListSuites>`_    


    **Request Syntax** 
    ::

      response = client.list_suites(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The suites' ARNs.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'suites': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list suites request.

        
        

        - **suites** *(list) --* 

          Information about the suites.

          
          

          - *(dict) --* 

            Represents a collection of one or more tests.

            
            

            - **arn** *(string) --* 

              The suite's ARN.

              
            

            - **name** *(string) --* 

              The suite's name.

              
            

            - **type** *(string) --* 

              The suite's type.

               

              Must be one of the following values:

               

               
              * BUILTIN_FUZZ: The built-in fuzz type. 
               
              * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
               
              * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
               
              * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
               
              * APPIUM_PYTHON: The Appium Python type. 
               
              * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
               
              * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
               
              * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
               
              * CALABASH: The Calabash type. 
               
              * INSTRUMENTATION: The Instrumentation type. 
               
              * UIAUTOMATION: The uiautomation type. 
               
              * UIAUTOMATOR: The uiautomator type. 
               
              * XCTEST: The XCode test type. 
               
              * XCTEST_UI: The XCode UI test type. 
               

              
            

            - **created** *(datetime) --* 

              When the suite was created.

              
            

            - **status** *(string) --* 

              The suite's status.

               

              Allowed values include:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The suite's result.

               

              Allowed values include:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **started** *(datetime) --* 

              The suite's start time.

              
            

            - **stopped** *(datetime) --* 

              The suite's stop time.

              
            

            - **counters** *(dict) --* 

              The suite's result counters.

              
              

              - **total** *(integer) --* 

                The total number of entities.

                
              

              - **passed** *(integer) --* 

                The number of passed entities.

                
              

              - **failed** *(integer) --* 

                The number of failed entities.

                
              

              - **warned** *(integer) --* 

                The number of warned entities.

                
              

              - **errored** *(integer) --* 

                The number of errored entities.

                
              

              - **stopped** *(integer) --* 

                The number of stopped entities.

                
              

              - **skipped** *(integer) --* 

                The number of skipped entities.

                
          
            

            - **message** *(string) --* 

              A message about the suite's result.

              
            

            - **deviceMinutes** *(dict) --* 

              Represents the total (metered or unmetered) minutes used by the test suite.

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about suites, given a specific Device Farm project.
    ::

      response = client.list_suites(
          # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'suites': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_tests(**kwargs)

    

    Gets information about tests.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListTests>`_    


    **Request Syntax** 
    ::

      response = client.list_tests(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The tests' ARNs.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tests': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list tests request.

        
        

        - **tests** *(list) --* 

          Information about the tests.

          
          

          - *(dict) --* 

            Represents a condition that is evaluated.

            
            

            - **arn** *(string) --* 

              The test's ARN.

              
            

            - **name** *(string) --* 

              The test's name.

              
            

            - **type** *(string) --* 

              The test's type.

               

              Must be one of the following values:

               

               
              * BUILTIN_FUZZ: The built-in fuzz type. 
               
              * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
               
              * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
               
              * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
               
              * APPIUM_PYTHON: The Appium Python type. 
               
              * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
               
              * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
               
              * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
               
              * CALABASH: The Calabash type. 
               
              * INSTRUMENTATION: The Instrumentation type. 
               
              * UIAUTOMATION: The uiautomation type. 
               
              * UIAUTOMATOR: The uiautomator type. 
               
              * XCTEST: The XCode test type. 
               
              * XCTEST_UI: The XCode UI test type. 
               

              
            

            - **created** *(datetime) --* 

              When the test was created.

              
            

            - **status** *(string) --* 

              The test's status.

               

              Allowed values include:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The test's result.

               

              Allowed values include:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **started** *(datetime) --* 

              The test's start time.

              
            

            - **stopped** *(datetime) --* 

              The test's stop time.

              
            

            - **counters** *(dict) --* 

              The test's result counters.

              
              

              - **total** *(integer) --* 

                The total number of entities.

                
              

              - **passed** *(integer) --* 

                The number of passed entities.

                
              

              - **failed** *(integer) --* 

                The number of failed entities.

                
              

              - **warned** *(integer) --* 

                The number of warned entities.

                
              

              - **errored** *(integer) --* 

                The number of errored entities.

                
              

              - **stopped** *(integer) --* 

                The number of stopped entities.

                
              

              - **skipped** *(integer) --* 

                The number of skipped entities.

                
          
            

            - **message** *(string) --* 

              A message about the test's result.

              
            

            - **deviceMinutes** *(dict) --* 

              Represents the total (metered or unmetered) minutes used by the test.

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about tests, given a specific Device Farm project.
    ::

      response = client.list_tests(
          # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'tests': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_unique_problems(**kwargs)

    

    Gets information about unique problems.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListUniqueProblems>`_    


    **Request Syntax** 
    ::

      response = client.list_unique_problems(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The unique problems' ARNs.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'uniqueProblems': {
                'string': [
                    {
                        'message': 'string',
                        'problems': [
                            {
                                'run': {
                                    'arn': 'string',
                                    'name': 'string'
                                },
                                'job': {
                                    'arn': 'string',
                                    'name': 'string'
                                },
                                'suite': {
                                    'arn': 'string',
                                    'name': 'string'
                                },
                                'test': {
                                    'arn': 'string',
                                    'name': 'string'
                                },
                                'device': {
                                    'arn': 'string',
                                    'name': 'string',
                                    'manufacturer': 'string',
                                    'model': 'string',
                                    'formFactor': 'PHONE'|'TABLET',
                                    'platform': 'ANDROID'|'IOS',
                                    'os': 'string',
                                    'cpu': {
                                        'frequency': 'string',
                                        'architecture': 'string',
                                        'clock': 123.0
                                    },
                                    'resolution': {
                                        'width': 123,
                                        'height': 123
                                    },
                                    'heapSize': 123,
                                    'memory': 123,
                                    'image': 'string',
                                    'carrier': 'string',
                                    'radio': 'string',
                                    'remoteAccessEnabled': True|False,
                                    'remoteDebugEnabled': True|False,
                                    'fleetType': 'string',
                                    'fleetName': 'string'
                                },
                                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                                'message': 'string'
                            },
                        ]
                    },
                ]
            },
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list unique problems request.

        
        

        - **uniqueProblems** *(dict) --* 

          Information about the unique problems.

           

          Allowed values include:

           

           
          * PENDING: A pending condition. 
           
          * PASSED: A passing condition. 
           
          * WARNED: A warning condition. 
           
          * FAILED: A failed condition. 
           
          * SKIPPED: A skipped condition. 
           
          * ERRORED: An error condition. 
           
          * STOPPED: A stopped condition. 
           

          
          

          - *(string) --* 
            

            - *(list) --* 
              

              - *(dict) --* 

                A collection of one or more problems, grouped by their result.

                
                

                - **message** *(string) --* 

                  A message about the unique problems' result.

                  
                

                - **problems** *(list) --* 

                  Information about the problems.

                  
                  

                  - *(dict) --* 

                    Represents a specific warning or failure.

                    
                    

                    - **run** *(dict) --* 

                      Information about the associated run.

                      
                      

                      - **arn** *(string) --* 

                        The problem detail's ARN.

                        
                      

                      - **name** *(string) --* 

                        The problem detail's name.

                        
                  
                    

                    - **job** *(dict) --* 

                      Information about the associated job.

                      
                      

                      - **arn** *(string) --* 

                        The problem detail's ARN.

                        
                      

                      - **name** *(string) --* 

                        The problem detail's name.

                        
                  
                    

                    - **suite** *(dict) --* 

                      Information about the associated suite.

                      
                      

                      - **arn** *(string) --* 

                        The problem detail's ARN.

                        
                      

                      - **name** *(string) --* 

                        The problem detail's name.

                        
                  
                    

                    - **test** *(dict) --* 

                      Information about the associated test.

                      
                      

                      - **arn** *(string) --* 

                        The problem detail's ARN.

                        
                      

                      - **name** *(string) --* 

                        The problem detail's name.

                        
                  
                    

                    - **device** *(dict) --* 

                      Information about the associated device.

                      
                      

                      - **arn** *(string) --* 

                        The device's ARN.

                        
                      

                      - **name** *(string) --* 

                        The device's display name.

                        
                      

                      - **manufacturer** *(string) --* 

                        The device's manufacturer name.

                        
                      

                      - **model** *(string) --* 

                        The device's model name.

                        
                      

                      - **formFactor** *(string) --* 

                        The device's form factor.

                         

                        Allowed values include:

                         

                         
                        * PHONE: The phone form factor. 
                         
                        * TABLET: The tablet form factor. 
                         

                        
                      

                      - **platform** *(string) --* 

                        The device's platform.

                         

                        Allowed values include:

                         

                         
                        * ANDROID: The Android platform. 
                         
                        * IOS: The iOS platform. 
                         

                        
                      

                      - **os** *(string) --* 

                        The device's operating system type.

                        
                      

                      - **cpu** *(dict) --* 

                        Information about the device's CPU.

                        
                        

                        - **frequency** *(string) --* 

                          The CPU's frequency.

                          
                        

                        - **architecture** *(string) --* 

                          The CPU's architecture, for example x86 or ARM.

                          
                        

                        - **clock** *(float) --* 

                          The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                          
                    
                      

                      - **resolution** *(dict) --* 

                        The resolution of the device.

                        
                        

                        - **width** *(integer) --* 

                          The screen resolution's width, expressed in pixels.

                          
                        

                        - **height** *(integer) --* 

                          The screen resolution's height, expressed in pixels.

                          
                    
                      

                      - **heapSize** *(integer) --* 

                        The device's heap size, expressed in bytes.

                        
                      

                      - **memory** *(integer) --* 

                        The device's total memory size, expressed in bytes.

                        
                      

                      - **image** *(string) --* 

                        The device's image name.

                        
                      

                      - **carrier** *(string) --* 

                        The device's carrier.

                        
                      

                      - **radio** *(string) --* 

                        The device's radio.

                        
                      

                      - **remoteAccessEnabled** *(boolean) --* 

                        Specifies whether remote access has been enabled for the specified device.

                        
                      

                      - **remoteDebugEnabled** *(boolean) --* 

                        This flag is set to ``true`` if remote debugging is enabled for the device.

                        
                      

                      - **fleetType** *(string) --* 

                        The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

                        
                      

                      - **fleetName** *(string) --* 

                        The name of the fleet to which this device belongs.

                        
                  
                    

                    - **result** *(string) --* 

                      The problem's result.

                       

                      Allowed values include:

                       

                       
                      * PENDING: A pending condition. 
                       
                      * PASSED: A passing condition. 
                       
                      * WARNED: A warning condition. 
                       
                      * FAILED: A failed condition. 
                       
                      * SKIPPED: A skipped condition. 
                       
                      * ERRORED: An error condition. 
                       
                      * STOPPED: A stopped condition. 
                       

                      
                    

                    - **message** *(string) --* 

                      A message about the problem's result.

                      
                
              
            
          
      
    
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about unique problems, given a specific Device Farm project.
    ::

      response = client.list_unique_problems(
          # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'uniqueProblems': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_uploads(**kwargs)

    

    Gets information about uploads, given an AWS Device Farm project ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListUploads>`_    


    **Request Syntax** 
    ::

      response = client.list_uploads(
          arn='string',
          nextToken='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to list uploads.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'uploads': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
                    'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                    'url': 'string',
                    'metadata': 'string',
                    'contentType': 'string',
                    'message': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list uploads request.

        
        

        - **uploads** *(list) --* 

          Information about the uploads.

          
          

          - *(dict) --* 

            An app or a set of one or more tests to upload or that have been uploaded.

            
            

            - **arn** *(string) --* 

              The upload's ARN.

              
            

            - **name** *(string) --* 

              The upload's file name.

              
            

            - **created** *(datetime) --* 

              When the upload was created.

              
            

            - **type** *(string) --* 

              The upload's type.

               

              Must be one of the following values:

               

               
              * ANDROID_APP: An Android upload. 
               
              * IOS_APP: An iOS upload. 
               
              * WEB_APP: A web appliction upload. 
               
              * EXTERNAL_DATA: An external data upload. 
               
              * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
               
              * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
               
              * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
               
              * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
               
              * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
               
              * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
               
              * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
               
              * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
               
              * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
               
              * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
               
              * XCTEST_TEST_PACKAGE: An XCode test package upload. 
               
              * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
               

              
            

            - **status** *(string) --* 

              The upload's status.

               

              Must be one of the following values:

               

               
              * FAILED: A failed status. 
               
              * INITIALIZED: An initialized status. 
               
              * PROCESSING: A processing status. 
               
              * SUCCEEDED: A succeeded status. 
               

              
            

            - **url** *(string) --* 

              The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.

              
            

            - **metadata** *(string) --* 

              The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

              
            

            - **contentType** *(string) --* 

              The upload's content type (for example, "application/octet-stream").

              
            

            - **message** *(string) --* 

              A message about the upload's result.

              
        
      
        

        - **nextToken** *(string) --* 

          If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.

          
    

    **Examples** 

    The following example returns information about uploads, given a specific Device Farm project.
    ::

      response = client.list_uploads(
          # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
          # A dynamically generated value, used for paginating results.
          nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'uploads': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: purchase_offering(**kwargs)

    

    Immediately purchases offerings for an AWS account. Offerings renew with the latest total purchased quantity for an offering, unless the renewal was overridden. The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/PurchaseOffering>`_    


    **Request Syntax** 
    ::

      response = client.purchase_offering(
          offeringId='string',
          quantity=123,
          offeringPromotionId='string'
      )
    :type offeringId: string
    :param offeringId: 

      The ID of the offering.

      

    
    :type quantity: integer
    :param quantity: 

      The number of device slots you wish to purchase in an offering request.

      

    
    :type offeringPromotionId: string
    :param offeringPromotionId: 

      The ID of the offering promotion to be applied to the purchase.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'offeringTransaction': {
                'offeringStatus': {
                    'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                    'offering': {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                    'quantity': 123,
                    'effectiveOn': datetime(2015, 1, 1)
                },
                'transactionId': 'string',
                'offeringPromotionId': 'string',
                'createdOn': datetime(2015, 1, 1),
                'cost': {
                    'amount': 123.0,
                    'currencyCode': 'USD'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of the purchase offering (e.g., success or failure).

        
        

        - **offeringTransaction** *(dict) --* 

          Represents the offering transaction for the purchase result.

          
          

          - **offeringStatus** *(dict) --* 

            The status of an offering transaction.

            
            

            - **type** *(string) --* 

              The type specified for the offering status.

              
            

            - **offering** *(dict) --* 

              Represents the metadata of an offering status.

              
              

              - **id** *(string) --* 

                The ID that corresponds to a device offering.

                
              

              - **description** *(string) --* 

                A string describing the offering.

                
              

              - **type** *(string) --* 

                The type of offering (e.g., "RECURRING") for a device.

                
              

              - **platform** *(string) --* 

                The platform of the device (e.g., ANDROID or IOS).

                
              

              - **recurringCharges** *(list) --* 

                Specifies whether there are recurring charges for the offering.

                
                

                - *(dict) --* 

                  Specifies whether charges for devices will be recurring.

                  
                  

                  - **cost** *(dict) --* 

                    The cost of the recurring charge.

                    
                    

                    - **amount** *(float) --* 

                      The numerical amount of an offering or transaction.

                      
                    

                    - **currencyCode** *(string) --* 

                      The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                      
                
                  

                  - **frequency** *(string) --* 

                    The frequency in which charges will recur.

                    
              
            
          
            

            - **quantity** *(integer) --* 

              The number of available devices in the offering.

              
            

            - **effectiveOn** *(datetime) --* 

              The date on which the offering is effective.

              
        
          

          - **transactionId** *(string) --* 

            The transaction ID of the offering transaction.

            
          

          - **offeringPromotionId** *(string) --* 

            The ID that corresponds to a device offering promotion.

            
          

          - **createdOn** *(datetime) --* 

            The date on which an offering transaction was created.

            
          

          - **cost** *(dict) --* 

            The cost of an offering transaction.

            
            

            - **amount** *(float) --* 

              The numerical amount of an offering or transaction.

              
            

            - **currencyCode** *(string) --* 

              The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

              
        
      
    

    **Examples** 

    The following example purchases a specific device slot offering.
    ::

      response = client.purchase_offering(
          # You can get the offering ID by using the list-offerings CLI command.
          offeringId='D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
          quantity=1,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'offeringTransaction': {
              'cost': {
                  'amount': 8.07,
                  'currencyCode': 'USD',
              },
              'createdOn': datetime(2016, 8, 31, 5, 59, 0, 2, 244, 1),
              'offeringStatus': {
                  'type': 'PURCHASE',
                  'effectiveOn': datetime(2016, 8, 31, 5, 59, 0, 2, 244, 1),
                  'offering': {
                      'type': 'RECURRING',
                      'description': 'Android Remote Access Unmetered Device Slot',
                      'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                      'platform': 'ANDROID',
                  },
                  'quantity': 1,
              },
              'transactionId': 'd30614ed-1b03-404c-9893-12345EXAMPLE',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: renew_offering(**kwargs)

    

    Explicitly sets the quantity of devices to renew for an offering, starting from the ``effectiveDate`` of the next period. The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/RenewOffering>`_    


    **Request Syntax** 
    ::

      response = client.renew_offering(
          offeringId='string',
          quantity=123
      )
    :type offeringId: string
    :param offeringId: 

      The ID of a request to renew an offering.

      

    
    :type quantity: integer
    :param quantity: 

      The quantity requested in an offering renewal.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'offeringTransaction': {
                'offeringStatus': {
                    'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                    'offering': {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                    'quantity': 123,
                    'effectiveOn': datetime(2015, 1, 1)
                },
                'transactionId': 'string',
                'offeringPromotionId': 'string',
                'createdOn': datetime(2015, 1, 1),
                'cost': {
                    'amount': 123.0,
                    'currencyCode': 'USD'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of a renewal offering.

        
        

        - **offeringTransaction** *(dict) --* 

          Represents the status of the offering transaction for the renewal.

          
          

          - **offeringStatus** *(dict) --* 

            The status of an offering transaction.

            
            

            - **type** *(string) --* 

              The type specified for the offering status.

              
            

            - **offering** *(dict) --* 

              Represents the metadata of an offering status.

              
              

              - **id** *(string) --* 

                The ID that corresponds to a device offering.

                
              

              - **description** *(string) --* 

                A string describing the offering.

                
              

              - **type** *(string) --* 

                The type of offering (e.g., "RECURRING") for a device.

                
              

              - **platform** *(string) --* 

                The platform of the device (e.g., ANDROID or IOS).

                
              

              - **recurringCharges** *(list) --* 

                Specifies whether there are recurring charges for the offering.

                
                

                - *(dict) --* 

                  Specifies whether charges for devices will be recurring.

                  
                  

                  - **cost** *(dict) --* 

                    The cost of the recurring charge.

                    
                    

                    - **amount** *(float) --* 

                      The numerical amount of an offering or transaction.

                      
                    

                    - **currencyCode** *(string) --* 

                      The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                      
                
                  

                  - **frequency** *(string) --* 

                    The frequency in which charges will recur.

                    
              
            
          
            

            - **quantity** *(integer) --* 

              The number of available devices in the offering.

              
            

            - **effectiveOn** *(datetime) --* 

              The date on which the offering is effective.

              
        
          

          - **transactionId** *(string) --* 

            The transaction ID of the offering transaction.

            
          

          - **offeringPromotionId** *(string) --* 

            The ID that corresponds to a device offering promotion.

            
          

          - **createdOn** *(datetime) --* 

            The date on which an offering transaction was created.

            
          

          - **cost** *(dict) --* 

            The cost of an offering transaction.

            
            

            - **amount** *(float) --* 

              The numerical amount of an offering or transaction.

              
            

            - **currencyCode** *(string) --* 

              The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

              
        
      
    

    **Examples** 

    The following example renews a specific device slot offering.
    ::

      response = client.renew_offering(
          # You can get the offering ID by using the list-offerings CLI command.
          offeringId='D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
          quantity=1,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'offeringTransaction': {
              'cost': {
                  'amount': 250,
                  'currencyCode': 'USD',
              },
              'createdOn': datetime(2016, 8, 31, 6, 8, 0, 2, 244, 1),
              'offeringStatus': {
                  'type': 'RENEW',
                  'effectiveOn': datetime(2016, 8, 31, 17, 0, 0, 2, 244, 1),
                  'offering': {
                      'type': 'RECURRING',
                      'description': 'Android Remote Access Unmetered Device Slot',
                      'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                      'platform': 'ANDROID',
                  },
                  'quantity': 1,
              },
              'transactionId': 'e90f1405-8c35-4561-be43-12345EXAMPLE',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: schedule_run(**kwargs)

    

    Schedules a run.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ScheduleRun>`_    


    **Request Syntax** 
    ::

      response = client.schedule_run(
          projectArn='string',
          appArn='string',
          devicePoolArn='string',
          name='string',
          test={
              'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
              'testPackageArn': 'string',
              'filter': 'string',
              'parameters': {
                  'string': 'string'
              }
          },
          configuration={
              'extraDataPackageArn': 'string',
              'networkProfileArn': 'string',
              'locale': 'string',
              'location': {
                  'latitude': 123.0,
                  'longitude': 123.0
              },
              'customerArtifactPaths': {
                  'iosPaths': [
                      'string',
                  ],
                  'androidPaths': [
                      'string',
                  ],
                  'deviceHostPaths': [
                      'string',
                  ]
              },
              'radios': {
                  'wifi': True|False,
                  'bluetooth': True|False,
                  'nfc': True|False,
                  'gps': True|False
              },
              'auxiliaryApps': [
                  'string',
              ],
              'billingMethod': 'METERED'|'UNMETERED'
          },
          executionConfiguration={
              'jobTimeoutMinutes': 123,
              'accountsCleanup': True|False,
              'appPackagesCleanup': True|False
          }
      )
    :type projectArn: string
    :param projectArn: **[REQUIRED]** 

      The ARN of the project for the run to be scheduled.

      

    
    :type appArn: string
    :param appArn: 

      The ARN of the app to schedule a run.

      

    
    :type devicePoolArn: string
    :param devicePoolArn: **[REQUIRED]** 

      The ARN of the device pool for the run to be scheduled.

      

    
    :type name: string
    :param name: 

      The name for the run to be scheduled.

      

    
    :type test: dict
    :param test: **[REQUIRED]** 

      Information about the test for the run to be scheduled.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The test's type.

         

        Must be one of the following values:

         

         
        * BUILTIN_FUZZ: The built-in fuzz type. 
         
        * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
         
        * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
         
        * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
         
        * APPIUM_PYTHON: The Appium Python type. 
         
        * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
         
        * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
         
        * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
         
        * CALABASH: The Calabash type. 
         
        * INSTRUMENTATION: The Instrumentation type. 
         
        * UIAUTOMATION: The uiautomation type. 
         
        * UIAUTOMATOR: The uiautomator type. 
         
        * XCTEST: The XCode test type. 
         
        * XCTEST_UI: The XCode UI test type. 
         

        

      
      - **testPackageArn** *(string) --* 

        The ARN of the uploaded test that will be run.

        

      
      - **filter** *(string) --* 

        The test's filter.

        

      
      - **parameters** *(dict) --* 

        The test's parameters, such as the following test framework parameters and fixture settings:

         

        For Calabash tests:

         

         
        * profile: A cucumber profile, for example, "my_profile_name". 
         
        * tags: You can limit execution to features or scenarios that have (or don't have) certain tags, for example, "@smoke" or "@smoke,~@wip". 
         

         

        For Appium tests (all types):

         

         
        * appium_version: The Appium version. Currently supported values are "1.4.16", "1.6.3", "latest", and "default". 

           
          * “latest” will run the latest Appium version supported by Device Farm (1.6.3). 
           
          * For “default”, Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.4.16 on Android devices and iOS 9 and earlier, 1.6.3 for iOS 10 and later. 
           
          * This behavior is subject to change. 
           

         
         

         

        For Fuzz tests (Android only):

         

         
        * event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform. 
         
        * throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events. 
         
        * seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences. 
         

         

        For Explorer tests:

         

         
        * username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted. 
         
        * password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted. 
         

         

        For Instrumentation:

         

         
        * filter: A test filter string. Examples: 

           
          * Running a single test case: "com.android.abc.Test1" 
           
          * Running a single test: "com.android.abc.Test1#smoke" 
           
          * Running multiple tests: "com.android.abc.Test1,com.android.abc.Test2" 
           

         
         

         

        For XCTest and XCTestUI:

         

         
        * filter: A test filter string. Examples: 

           
          * Running a single test class: "LoginTests" 
           
          * Running a multiple test classes: "LoginTests,SmokeTests" 
           
          * Running a single test: "LoginTests/testValid" 
           
          * Running multiple tests: "LoginTests/testValid,LoginTests/testInvalid" 
           

         
         

         

        For UIAutomator:

         

         
        * filter: A test filter string. Examples: 

           
          * Running a single test case: "com.android.abc.Test1" 
           
          * Running a single test: "com.android.abc.Test1#smoke" 
           
          * Running multiple tests: "com.android.abc.Test1,com.android.abc.Test2" 
           

         
         

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    :type configuration: dict
    :param configuration: 

      Information about the settings for the run to be scheduled.

      

    
      - **extraDataPackageArn** *(string) --* 

        The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm will extract to external data for Android or the app's sandbox for iOS.

        

      
      - **networkProfileArn** *(string) --* 

        Reserved for internal use.

        

      
      - **locale** *(string) --* 

        Information about the locale that is used for the run.

        

      
      - **location** *(dict) --* 

        Information about the location that is used for the run.

        

      
        - **latitude** *(float) --* **[REQUIRED]** 

          The latitude.

          

        
        - **longitude** *(float) --* **[REQUIRED]** 

          The longitude.

          

        
      
      - **customerArtifactPaths** *(dict) --* 

        Input ``CustomerArtifactPaths`` object for the scheduled run configuration.

        

      
        - **iosPaths** *(list) --* 

          Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.

          

        
          - *(string) --* 

          
      
        - **androidPaths** *(list) --* 

          Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.

          

        
          - *(string) --* 

          
      
        - **deviceHostPaths** *(list) --* 

          Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.

          

        
          - *(string) --* 

          
      
      
      - **radios** *(dict) --* 

        Information about the radio states for the run.

        

      
        - **wifi** *(boolean) --* 

          True if Wi-Fi is enabled at the beginning of the test; otherwise, false.

          

        
        - **bluetooth** *(boolean) --* 

          True if Bluetooth is enabled at the beginning of the test; otherwise, false.

          

        
        - **nfc** *(boolean) --* 

          True if NFC is enabled at the beginning of the test; otherwise, false.

          

        
        - **gps** *(boolean) --* 

          True if GPS is enabled at the beginning of the test; otherwise, false.

          

        
      
      - **auxiliaryApps** *(list) --* 

        A list of auxiliary apps for the run.

        

      
        - *(string) --* 

        
    
      - **billingMethod** *(string) --* 

        Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .

        

      
    
    :type executionConfiguration: dict
    :param executionConfiguration: 

      Specifies configuration information about a test run, such as the execution timeout (in minutes).

      

    
      - **jobTimeoutMinutes** *(integer) --* 

        The number of minutes a test run will execute before it times out.

        

      
      - **accountsCleanup** *(boolean) --* 

        True if account cleanup is enabled at the beginning of the test; otherwise, false.

        

      
      - **appPackagesCleanup** *(boolean) --* 

        True if app package cleanup is enabled at the beginning of the test; otherwise, false.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'run': {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                'platform': 'ANDROID'|'IOS',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'totalJobs': 123,
                'completedJobs': 123,
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'networkProfile': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                },
                'parsingResultUrl': 'string',
                'resultCode': 'PARSING_FAILED',
                'customerArtifactPaths': {
                    'iosPaths': [
                        'string',
                    ],
                    'androidPaths': [
                        'string',
                    ],
                    'deviceHostPaths': [
                        'string',
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a schedule run request.

        
        

        - **run** *(dict) --* 

          Information about the scheduled run.

          
          

          - **arn** *(string) --* 

            The run's ARN.

            
          

          - **name** *(string) --* 

            The run's name.

            
          

          - **type** *(string) --* 

            The run's type.

             

            Must be one of the following values:

             

             
            * BUILTIN_FUZZ: The built-in fuzz type. 
             
            * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
             
            * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
             
            * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
             
            * APPIUM_PYTHON: The Appium Python type. 
             
            * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
             
            * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
             
            * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
             
            * CALABASH: The Calabash type. 
             
            * INSTRUMENTATION: The Instrumentation type. 
             
            * UIAUTOMATION: The uiautomation type. 
             
            * UIAUTOMATOR: The uiautomator type. 
             
            * XCTEST: The XCode test type. 
             
            * XCTEST_UI: The XCode UI test type. 
             

            
          

          - **platform** *(string) --* 

            The run's platform.

             

            Allowed values include:

             

             
            * ANDROID: The Android platform. 
             
            * IOS: The iOS platform. 
             

            
          

          - **created** *(datetime) --* 

            When the run was created.

            
          

          - **status** *(string) --* 

            The run's status.

             

            Allowed values include:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The run's result.

             

            Allowed values include:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **started** *(datetime) --* 

            The run's start time.

            
          

          - **stopped** *(datetime) --* 

            The run's stop time.

            
          

          - **counters** *(dict) --* 

            The run's result counters.

            
            

            - **total** *(integer) --* 

              The total number of entities.

              
            

            - **passed** *(integer) --* 

              The number of passed entities.

              
            

            - **failed** *(integer) --* 

              The number of failed entities.

              
            

            - **warned** *(integer) --* 

              The number of warned entities.

              
            

            - **errored** *(integer) --* 

              The number of errored entities.

              
            

            - **stopped** *(integer) --* 

              The number of stopped entities.

              
            

            - **skipped** *(integer) --* 

              The number of skipped entities.

              
        
          

          - **message** *(string) --* 

            A message about the run's result.

            
          

          - **totalJobs** *(integer) --* 

            The total number of jobs for the run.

            
          

          - **completedJobs** *(integer) --* 

            The total number of completed jobs.

            
          

          - **billingMethod** *(string) --* 

            Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .

            
          

          - **deviceMinutes** *(dict) --* 

            Represents the total (metered or unmetered) minutes used by the test run.

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
          

          - **networkProfile** *(dict) --* 

            The network profile being used for a test run.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the network profile.

              
            

            - **name** *(string) --* 

              The name of the network profile.

              
            

            - **description** *(string) --* 

              The description of the network profile.

              
            

            - **type** *(string) --* 

              The type of network profile. Valid values are listed below.

              
            

            - **uplinkBandwidthBits** *(integer) --* 

              The data throughput rate in bits per second, as an integer from 0 to 104857600.

              
            

            - **downlinkBandwidthBits** *(integer) --* 

              The data throughput rate in bits per second, as an integer from 0 to 104857600.

              
            

            - **uplinkDelayMs** *(integer) --* 

              Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

              
            

            - **downlinkDelayMs** *(integer) --* 

              Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

              
            

            - **uplinkJitterMs** *(integer) --* 

              Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

              
            

            - **downlinkJitterMs** *(integer) --* 

              Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

              
            

            - **uplinkLossPercent** *(integer) --* 

              Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

              
            

            - **downlinkLossPercent** *(integer) --* 

              Proportion of received packets that fail to arrive from 0 to 100 percent.

              
        
          

          - **parsingResultUrl** *(string) --* 

            Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.

            
          

          - **resultCode** *(string) --* 

            Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.

            
          

          - **customerArtifactPaths** *(dict) --* 

            Output ``CustomerArtifactPaths`` object for the test run.

            
            

            - **iosPaths** *(list) --* 

              Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
            

            - **androidPaths** *(list) --* 

              Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
            

            - **deviceHostPaths** *(list) --* 

              Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
        
      
    

    **Examples** 

    The following example schedules a test run named MyRun.
    ::

      response = client.schedule_run(
          name='MyRun',
          # You can get the Amazon Resource Name (ARN) of the device pool by using the list-pools CLI command.
          devicePoolArn='arn:aws:devicefarm:us-west-2:123456789101:pool:EXAMPLE-GUID-123-456',
          # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
          projectArn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
          test={
              'type': 'APPIUM_JAVA_JUNIT',
              'testPackageArn': 'arn:aws:devicefarm:us-west-2:123456789101:test:EXAMPLE-GUID-123-456',
          },
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'run': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: stop_remote_access_session(**kwargs)

    

    Ends a specified remote access session.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/StopRemoteAccessSession>`_    


    **Request Syntax** 
    ::

      response = client.stop_remote_access_session(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the remote access session you wish to stop.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'remoteAccessSession': {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'message': 'string',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
                'remoteDebugEnabled': True|False,
                'hostAddress': 'string',
                'clientId': 'string',
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'endpoint': 'string',
                'deviceUdid': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server that describes the remote access session when AWS Device Farm stops the session.

        
        

        - **remoteAccessSession** *(dict) --* 

          A container representing the metadata from the service about the remote access session you are stopping.

          
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the remote access session.

            
          

          - **name** *(string) --* 

            The name of the remote access session.

            
          

          - **created** *(datetime) --* 

            The date and time the remote access session was created.

            
          

          - **status** *(string) --* 

            The status of the remote access session. Can be any of the following:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The result of the remote access session. Can be any of the following:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **message** *(string) --* 

            A message about the remote access session.

            
          

          - **started** *(datetime) --* 

            The date and time the remote access session was started.

            
          

          - **stopped** *(datetime) --* 

            The date and time the remote access session was stopped.

            
          

          - **device** *(dict) --* 

            The device (phone or tablet) used in the remote access session.

            
            

            - **arn** *(string) --* 

              The device's ARN.

              
            

            - **name** *(string) --* 

              The device's display name.

              
            

            - **manufacturer** *(string) --* 

              The device's manufacturer name.

              
            

            - **model** *(string) --* 

              The device's model name.

              
            

            - **formFactor** *(string) --* 

              The device's form factor.

               

              Allowed values include:

               

               
              * PHONE: The phone form factor. 
               
              * TABLET: The tablet form factor. 
               

              
            

            - **platform** *(string) --* 

              The device's platform.

               

              Allowed values include:

               

               
              * ANDROID: The Android platform. 
               
              * IOS: The iOS platform. 
               

              
            

            - **os** *(string) --* 

              The device's operating system type.

              
            

            - **cpu** *(dict) --* 

              Information about the device's CPU.

              
              

              - **frequency** *(string) --* 

                The CPU's frequency.

                
              

              - **architecture** *(string) --* 

                The CPU's architecture, for example x86 or ARM.

                
              

              - **clock** *(float) --* 

                The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                
          
            

            - **resolution** *(dict) --* 

              The resolution of the device.

              
              

              - **width** *(integer) --* 

                The screen resolution's width, expressed in pixels.

                
              

              - **height** *(integer) --* 

                The screen resolution's height, expressed in pixels.

                
          
            

            - **heapSize** *(integer) --* 

              The device's heap size, expressed in bytes.

              
            

            - **memory** *(integer) --* 

              The device's total memory size, expressed in bytes.

              
            

            - **image** *(string) --* 

              The device's image name.

              
            

            - **carrier** *(string) --* 

              The device's carrier.

              
            

            - **radio** *(string) --* 

              The device's radio.

              
            

            - **remoteAccessEnabled** *(boolean) --* 

              Specifies whether remote access has been enabled for the specified device.

              
            

            - **remoteDebugEnabled** *(boolean) --* 

              This flag is set to ``true`` if remote debugging is enabled for the device.

              
            

            - **fleetType** *(string) --* 

              The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

              
            

            - **fleetName** *(string) --* 

              The name of the fleet to which this device belongs.

              
        
          

          - **remoteDebugEnabled** *(boolean) --* 

            This flag is set to ``true`` if remote debugging is enabled for the remote access session.

            
          

          - **hostAddress** *(string) --* 

            IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.

            
          

          - **clientId** *(string) --* 

            Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.

            
          

          - **billingMethod** *(string) --* 

            The billing method of the remote access session. Possible values include ``METERED`` or ``UNMETERED`` . For more information about metered devices, see `AWS Device Farm terminology <http://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology>`__ ."

            
          

          - **deviceMinutes** *(dict) --* 

            The number of minutes a device is used in a remote access sesssion (including setup and teardown minutes).

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
          

          - **endpoint** *(string) --* 

            The endpoint for the remote access sesssion.

            
          

          - **deviceUdid** *(string) --* 

            Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.

            
      
    

  .. py:method:: stop_run(**kwargs)

    

    Initiates a stop request for the current test run. AWS Device Farm will immediately stop the run on devices where tests have not started executing, and you will not be billed for these devices. On devices where tests have started executing, Setup Suite and Teardown Suite tests will run to completion before stopping execution on those devices. You will be billed for Setup, Teardown, and any tests that were in progress or already completed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/StopRun>`_    


    **Request Syntax** 
    ::

      response = client.stop_run(
          arn='string'
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      Represents the Amazon Resource Name (ARN) of the Device Farm run you wish to stop.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'run': {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                'platform': 'ANDROID'|'IOS',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'totalJobs': 123,
                'completedJobs': 123,
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'networkProfile': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                },
                'parsingResultUrl': 'string',
                'resultCode': 'PARSING_FAILED',
                'customerArtifactPaths': {
                    'iosPaths': [
                        'string',
                    ],
                    'androidPaths': [
                        'string',
                    ],
                    'deviceHostPaths': [
                        'string',
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the results of your stop run attempt.

        
        

        - **run** *(dict) --* 

          The run that was stopped.

          
          

          - **arn** *(string) --* 

            The run's ARN.

            
          

          - **name** *(string) --* 

            The run's name.

            
          

          - **type** *(string) --* 

            The run's type.

             

            Must be one of the following values:

             

             
            * BUILTIN_FUZZ: The built-in fuzz type. 
             
            * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
             
            * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
             
            * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
             
            * APPIUM_PYTHON: The Appium Python type. 
             
            * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
             
            * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
             
            * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
             
            * CALABASH: The Calabash type. 
             
            * INSTRUMENTATION: The Instrumentation type. 
             
            * UIAUTOMATION: The uiautomation type. 
             
            * UIAUTOMATOR: The uiautomator type. 
             
            * XCTEST: The XCode test type. 
             
            * XCTEST_UI: The XCode UI test type. 
             

            
          

          - **platform** *(string) --* 

            The run's platform.

             

            Allowed values include:

             

             
            * ANDROID: The Android platform. 
             
            * IOS: The iOS platform. 
             

            
          

          - **created** *(datetime) --* 

            When the run was created.

            
          

          - **status** *(string) --* 

            The run's status.

             

            Allowed values include:

             

             
            * PENDING: A pending status. 
             
            * PENDING_CONCURRENCY: A pending concurrency status. 
             
            * PENDING_DEVICE: A pending device status. 
             
            * PROCESSING: A processing status. 
             
            * SCHEDULING: A scheduling status. 
             
            * PREPARING: A preparing status. 
             
            * RUNNING: A running status. 
             
            * COMPLETED: A completed status. 
             
            * STOPPING: A stopping status. 
             

            
          

          - **result** *(string) --* 

            The run's result.

             

            Allowed values include:

             

             
            * PENDING: A pending condition. 
             
            * PASSED: A passing condition. 
             
            * WARNED: A warning condition. 
             
            * FAILED: A failed condition. 
             
            * SKIPPED: A skipped condition. 
             
            * ERRORED: An error condition. 
             
            * STOPPED: A stopped condition. 
             

            
          

          - **started** *(datetime) --* 

            The run's start time.

            
          

          - **stopped** *(datetime) --* 

            The run's stop time.

            
          

          - **counters** *(dict) --* 

            The run's result counters.

            
            

            - **total** *(integer) --* 

              The total number of entities.

              
            

            - **passed** *(integer) --* 

              The number of passed entities.

              
            

            - **failed** *(integer) --* 

              The number of failed entities.

              
            

            - **warned** *(integer) --* 

              The number of warned entities.

              
            

            - **errored** *(integer) --* 

              The number of errored entities.

              
            

            - **stopped** *(integer) --* 

              The number of stopped entities.

              
            

            - **skipped** *(integer) --* 

              The number of skipped entities.

              
        
          

          - **message** *(string) --* 

            A message about the run's result.

            
          

          - **totalJobs** *(integer) --* 

            The total number of jobs for the run.

            
          

          - **completedJobs** *(integer) --* 

            The total number of completed jobs.

            
          

          - **billingMethod** *(string) --* 

            Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .

            
          

          - **deviceMinutes** *(dict) --* 

            Represents the total (metered or unmetered) minutes used by the test run.

            
            

            - **total** *(float) --* 

              When specified, represents the total minutes used by the resource to run tests.

              
            

            - **metered** *(float) --* 

              When specified, represents only the sum of metered minutes used by the resource to run tests.

              
            

            - **unmetered** *(float) --* 

              When specified, represents only the sum of unmetered minutes used by the resource to run tests.

              
        
          

          - **networkProfile** *(dict) --* 

            The network profile being used for a test run.

            
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the network profile.

              
            

            - **name** *(string) --* 

              The name of the network profile.

              
            

            - **description** *(string) --* 

              The description of the network profile.

              
            

            - **type** *(string) --* 

              The type of network profile. Valid values are listed below.

              
            

            - **uplinkBandwidthBits** *(integer) --* 

              The data throughput rate in bits per second, as an integer from 0 to 104857600.

              
            

            - **downlinkBandwidthBits** *(integer) --* 

              The data throughput rate in bits per second, as an integer from 0 to 104857600.

              
            

            - **uplinkDelayMs** *(integer) --* 

              Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

              
            

            - **downlinkDelayMs** *(integer) --* 

              Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

              
            

            - **uplinkJitterMs** *(integer) --* 

              Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

              
            

            - **downlinkJitterMs** *(integer) --* 

              Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

              
            

            - **uplinkLossPercent** *(integer) --* 

              Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

              
            

            - **downlinkLossPercent** *(integer) --* 

              Proportion of received packets that fail to arrive from 0 to 100 percent.

              
        
          

          - **parsingResultUrl** *(string) --* 

            Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.

            
          

          - **resultCode** *(string) --* 

            Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.

            
          

          - **customerArtifactPaths** *(dict) --* 

            Output ``CustomerArtifactPaths`` object for the test run.

            
            

            - **iosPaths** *(list) --* 

              Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
            

            - **androidPaths** *(list) --* 

              Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
            

            - **deviceHostPaths** *(list) --* 

              Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.

              
              

              - *(string) --* 
          
        
      
    

    **Examples** 

    The following example stops a specific test run.
    ::

      response = client.stop_run(
          # You can get the Amazon Resource Name (ARN) of the test run by using the list-runs CLI command.
          arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'run': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_device_pool(**kwargs)

    

    Modifies the name, description, and rules in a device pool given the attributes and the pool ARN. Rule updates are all-or-nothing, meaning they can only be updated as a whole (or not at all).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateDevicePool>`_    


    **Request Syntax** 
    ::

      response = client.update_device_pool(
          arn='string',
          name='string',
          description='string',
          rules=[
              {
                  'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION',
                  'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                  'value': 'string'
              },
          ]
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resourc Name (ARN) of the Device Farm device pool you wish to update.

      

    
    :type name: string
    :param name: 

      A string representing the name of the device pool you wish to update.

      

    
    :type description: string
    :param description: 

      A description of the device pool you wish to update.

      

    
    :type rules: list
    :param rules: 

      Represents the rules you wish to modify for the device pool. Updating rules is optional; however, if you choose to update rules for your request, the update will replace the existing rules.

      

    
      - *(dict) --* 

        Represents a condition for a device pool.

        

      
        - **attribute** *(string) --* 

          The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .

           

          Allowed values include:

           

           
          * ARN: The ARN. 
           
          * FORM_FACTOR: The form factor (for example, phone or tablet). 
           
          * MANUFACTURER: The manufacturer. 
           
          * PLATFORM: The platform (for example, Android or iOS). 
           
          * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
           
          * APPIUM_VERSION: The Appium version for the test. 
           

          

        
        - **operator** *(string) --* 

          The rule's operator.

           

           
          * EQUALS: The equals operator. 
           
          * GREATER_THAN: The greater-than operator. 
           
          * IN: The in operator. 
           
          * LESS_THAN: The less-than operator. 
           
          * NOT_IN: The not-in operator. 
           
          * CONTAINS: The contains operator. 
           

          

        
        - **value** *(string) --* 

          The rule's value.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'devicePool': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'rules': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION',
                        'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                        'value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of an update device pool request.

        
        

        - **devicePool** *(dict) --* 

          The device pool you just updated.

          
          

          - **arn** *(string) --* 

            The device pool's ARN.

            
          

          - **name** *(string) --* 

            The device pool's name.

            
          

          - **description** *(string) --* 

            The device pool's description.

            
          

          - **type** *(string) --* 

            The device pool's type.

             

            Allowed values include:

             

             
            * CURATED: A device pool that is created and managed by AWS Device Farm. 
             
            * PRIVATE: A device pool that is created and managed by the device pool developer. 
             

            
          

          - **rules** *(list) --* 

            Information about the device pool's rules.

            
            

            - *(dict) --* 

              Represents a condition for a device pool.

              
              

              - **attribute** *(string) --* 

                The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .

                 

                Allowed values include:

                 

                 
                * ARN: The ARN. 
                 
                * FORM_FACTOR: The form factor (for example, phone or tablet). 
                 
                * MANUFACTURER: The manufacturer. 
                 
                * PLATFORM: The platform (for example, Android or iOS). 
                 
                * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                 
                * APPIUM_VERSION: The Appium version for the test. 
                 

                
              

              - **operator** *(string) --* 

                The rule's operator.

                 

                 
                * EQUALS: The equals operator. 
                 
                * GREATER_THAN: The greater-than operator. 
                 
                * IN: The in operator. 
                 
                * LESS_THAN: The less-than operator. 
                 
                * NOT_IN: The not-in operator. 
                 
                * CONTAINS: The contains operator. 
                 

                
              

              - **value** *(string) --* 

                The rule's value.

                
          
        
      
    

    **Examples** 

    The following example updates the specified device pool with a new name and description. It also enables remote access of devices in the device pool.
    ::

      response = client.update_device_pool(
          name='NewName',
          # You can get the Amazon Resource Name (ARN) of the device pool by using the list-pools CLI command.
          arn='arn:aws:devicefarm:us-west-2::devicepool:082d10e5-d7d7-48a5-ba5c-12345EXAMPLE',
          description='NewDescription',
          rules=[
              {
                  'value': 'True',
                  'attribute': 'REMOTE_ACCESS_ENABLED',
                  'operator': 'EQUALS',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # Note: you cannot update curated device pools.
          'devicePool': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_network_profile(**kwargs)

    

    Updates the network profile with specific settings.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateNetworkProfile>`_    


    **Request Syntax** 
    ::

      response = client.update_network_profile(
          arn='string',
          name='string',
          description='string',
          type='CURATED'|'PRIVATE',
          uplinkBandwidthBits=123,
          downlinkBandwidthBits=123,
          uplinkDelayMs=123,
          downlinkDelayMs=123,
          uplinkJitterMs=123,
          downlinkJitterMs=123,
          uplinkLossPercent=123,
          downlinkLossPercent=123
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project that you wish to update network profile settings.

      

    
    :type name: string
    :param name: 

      The name of the network profile about which you are returning information.

      

    
    :type description: string
    :param description: 

      The descriptoin of the network profile about which you are returning information.

      

    
    :type type: string
    :param type: 

      The type of network profile you wish to return information about. Valid values are listed below.

      

    
    :type uplinkBandwidthBits: integer
    :param uplinkBandwidthBits: 

      The data throughput rate in bits per second, as an integer from 0 to 104857600.

      

    
    :type downlinkBandwidthBits: integer
    :param downlinkBandwidthBits: 

      The data throughput rate in bits per second, as an integer from 0 to 104857600.

      

    
    :type uplinkDelayMs: integer
    :param uplinkDelayMs: 

      Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

      

    
    :type downlinkDelayMs: integer
    :param downlinkDelayMs: 

      Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

      

    
    :type uplinkJitterMs: integer
    :param uplinkJitterMs: 

      Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

      

    
    :type downlinkJitterMs: integer
    :param downlinkJitterMs: 

      Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

      

    
    :type uplinkLossPercent: integer
    :param uplinkLossPercent: 

      Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

      

    
    :type downlinkLossPercent: integer
    :param downlinkLossPercent: 

      Proportion of received packets that fail to arrive from 0 to 100 percent.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **networkProfile** *(dict) --* 

          A list of the available network profiles.

          
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the network profile.

            
          

          - **name** *(string) --* 

            The name of the network profile.

            
          

          - **description** *(string) --* 

            The description of the network profile.

            
          

          - **type** *(string) --* 

            The type of network profile. Valid values are listed below.

            
          

          - **uplinkBandwidthBits** *(integer) --* 

            The data throughput rate in bits per second, as an integer from 0 to 104857600.

            
          

          - **downlinkBandwidthBits** *(integer) --* 

            The data throughput rate in bits per second, as an integer from 0 to 104857600.

            
          

          - **uplinkDelayMs** *(integer) --* 

            Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

            
          

          - **downlinkDelayMs** *(integer) --* 

            Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

            
          

          - **uplinkJitterMs** *(integer) --* 

            Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

            
          

          - **downlinkJitterMs** *(integer) --* 

            Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

            
          

          - **uplinkLossPercent** *(integer) --* 

            Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

            
          

          - **downlinkLossPercent** *(integer) --* 

            Proportion of received packets that fail to arrive from 0 to 100 percent.

            
      
    

  .. py:method:: update_project(**kwargs)

    

    Modifies the specified project name, given the project ARN and a new name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateProject>`_    


    **Request Syntax** 
    ::

      response = client.update_project(
          arn='string',
          name='string',
          defaultJobTimeoutMinutes=123
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project whose name you wish to update.

      

    
    :type name: string
    :param name: 

      A string representing the new name of the project that you are updating.

      

    
    :type defaultJobTimeoutMinutes: integer
    :param defaultJobTimeoutMinutes: 

      The number of minutes a test run in the project will execute before it times out.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'project': {
                'arn': 'string',
                'name': 'string',
                'defaultJobTimeoutMinutes': 123,
                'created': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of an update project request.

        
        

        - **project** *(dict) --* 

          The project you wish to update.

          
          

          - **arn** *(string) --* 

            The project's ARN.

            
          

          - **name** *(string) --* 

            The project's name.

            
          

          - **defaultJobTimeoutMinutes** *(integer) --* 

            The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.

            
          

          - **created** *(datetime) --* 

            When the project was created.

            
      
    

    **Examples** 

    The following example updates the specified project with a new name.
    ::

      response = client.update_project(
          name='NewName',
          # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
          arn='arn:aws:devicefarm:us-west-2:183774035805:project:8f75187d-101e-4625-accc-12345EXAMPLE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'project': {
              'name': 'NewName',
              'arn': 'arn:aws:devicefarm:us-west-2:183774035805:project:8f75187d-101e-4625-accc-12345EXAMPLE',
              'created': datetime(2015, 11, 24, 13, 31, 49, 1, 328, 0),
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:

* :py:class:`DeviceFarm.Paginator.GetOfferingStatus`


* :py:class:`DeviceFarm.Paginator.ListArtifacts`


* :py:class:`DeviceFarm.Paginator.ListDevicePools`


* :py:class:`DeviceFarm.Paginator.ListDevices`


* :py:class:`DeviceFarm.Paginator.ListJobs`


* :py:class:`DeviceFarm.Paginator.ListOfferingTransactions`


* :py:class:`DeviceFarm.Paginator.ListOfferings`


* :py:class:`DeviceFarm.Paginator.ListProjects`


* :py:class:`DeviceFarm.Paginator.ListRuns`


* :py:class:`DeviceFarm.Paginator.ListSamples`


* :py:class:`DeviceFarm.Paginator.ListSuites`


* :py:class:`DeviceFarm.Paginator.ListTests`


* :py:class:`DeviceFarm.Paginator.ListUniqueProblems`


* :py:class:`DeviceFarm.Paginator.ListUploads`



.. py:class:: DeviceFarm.Paginator.GetOfferingStatus

  ::

    
    paginator = client.get_paginator('get_offering_status')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.get_offering_status`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetOfferingStatus>`_    


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
            'current': {
                'string': {
                    'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                    'offering': {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                    'quantity': 123,
                    'effectiveOn': datetime(2015, 1, 1)
                }
            },
            'nextPeriod': {
                'string': {
                    'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                    'offering': {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                    'quantity': 123,
                    'effectiveOn': datetime(2015, 1, 1)
                }
            },
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the status result for a device offering.

        
        

        - **current** *(dict) --* 

          When specified, gets the offering status for the current period.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              The status of the offering.

              
              

              - **type** *(string) --* 

                The type specified for the offering status.

                
              

              - **offering** *(dict) --* 

                Represents the metadata of an offering status.

                
                

                - **id** *(string) --* 

                  The ID that corresponds to a device offering.

                  
                

                - **description** *(string) --* 

                  A string describing the offering.

                  
                

                - **type** *(string) --* 

                  The type of offering (e.g., "RECURRING") for a device.

                  
                

                - **platform** *(string) --* 

                  The platform of the device (e.g., ANDROID or IOS).

                  
                

                - **recurringCharges** *(list) --* 

                  Specifies whether there are recurring charges for the offering.

                  
                  

                  - *(dict) --* 

                    Specifies whether charges for devices will be recurring.

                    
                    

                    - **cost** *(dict) --* 

                      The cost of the recurring charge.

                      
                      

                      - **amount** *(float) --* 

                        The numerical amount of an offering or transaction.

                        
                      

                      - **currencyCode** *(string) --* 

                        The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                        
                  
                    

                    - **frequency** *(string) --* 

                      The frequency in which charges will recur.

                      
                
              
            
              

              - **quantity** *(integer) --* 

                The number of available devices in the offering.

                
              

              - **effectiveOn** *(datetime) --* 

                The date on which the offering is effective.

                
          
      
    
        

        - **nextPeriod** *(dict) --* 

          When specified, gets the offering status for the next period.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              The status of the offering.

              
              

              - **type** *(string) --* 

                The type specified for the offering status.

                
              

              - **offering** *(dict) --* 

                Represents the metadata of an offering status.

                
                

                - **id** *(string) --* 

                  The ID that corresponds to a device offering.

                  
                

                - **description** *(string) --* 

                  A string describing the offering.

                  
                

                - **type** *(string) --* 

                  The type of offering (e.g., "RECURRING") for a device.

                  
                

                - **platform** *(string) --* 

                  The platform of the device (e.g., ANDROID or IOS).

                  
                

                - **recurringCharges** *(list) --* 

                  Specifies whether there are recurring charges for the offering.

                  
                  

                  - *(dict) --* 

                    Specifies whether charges for devices will be recurring.

                    
                    

                    - **cost** *(dict) --* 

                      The cost of the recurring charge.

                      
                      

                      - **amount** *(float) --* 

                        The numerical amount of an offering or transaction.

                        
                      

                      - **currencyCode** *(string) --* 

                        The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                        
                  
                    

                    - **frequency** *(string) --* 

                      The frequency in which charges will recur.

                      
                
              
            
              

              - **quantity** *(integer) --* 

                The number of available devices in the offering.

                
              

              - **effectiveOn** *(datetime) --* 

                The date on which the offering is effective.

                
          
      
    
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListArtifacts

  ::

    
    paginator = client.get_paginator('list_artifacts')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_artifacts`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListArtifacts>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          type='SCREENSHOT'|'FILE'|'LOG',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Run, Job, Suite, or Test ARN.

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      The artifacts' type.

       

      Allowed values include:

       

       
      * FILE: The artifacts are files. 
       
      * LOG: The artifacts are logs. 
       
      * SCREENSHOT: The artifacts are screenshots. 
       

      

    
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
            'artifacts': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'UNKNOWN'|'SCREENSHOT'|'DEVICE_LOG'|'MESSAGE_LOG'|'VIDEO_LOG'|'RESULT_LOG'|'SERVICE_LOG'|'WEBKIT_LOG'|'INSTRUMENTATION_OUTPUT'|'EXERCISER_MONKEY_OUTPUT'|'CALABASH_JSON_OUTPUT'|'CALABASH_PRETTY_OUTPUT'|'CALABASH_STANDARD_OUTPUT'|'CALABASH_JAVA_XML_OUTPUT'|'AUTOMATION_OUTPUT'|'APPIUM_SERVER_OUTPUT'|'APPIUM_JAVA_OUTPUT'|'APPIUM_JAVA_XML_OUTPUT'|'APPIUM_PYTHON_OUTPUT'|'APPIUM_PYTHON_XML_OUTPUT'|'EXPLORER_EVENT_LOG'|'EXPLORER_SUMMARY_LOG'|'APPLICATION_CRASH_REPORT'|'XCTEST_LOG'|'VIDEO'|'CUSTOMER_ARTIFACT'|'CUSTOMER_ARTIFACT_LOG',
                    'extension': 'string',
                    'url': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list artifacts operation.

        
        

        - **artifacts** *(list) --* 

          Information about the artifacts.

          
          

          - *(dict) --* 

            Represents the output of a test. Examples of artifacts include logs and screenshots.

            
            

            - **arn** *(string) --* 

              The artifact's ARN.

              
            

            - **name** *(string) --* 

              The artifact's name.

              
            

            - **type** *(string) --* 

              The artifact's type.

               

              Allowed values include the following:

               

               
              * UNKNOWN: An unknown type. 
               
              * SCREENSHOT: The screenshot type. 
               
              * DEVICE_LOG: The device log type. 
               
              * MESSAGE_LOG: The message log type. 
               
              * RESULT_LOG: The result log type. 
               
              * SERVICE_LOG: The service log type. 
               
              * WEBKIT_LOG: The web kit log type. 
               
              * INSTRUMENTATION_OUTPUT: The instrumentation type. 
               
              * EXERCISER_MONKEY_OUTPUT: For Android, the artifact (log) generated by an Android fuzz test. 
               
              * CALABASH_JSON_OUTPUT: The Calabash JSON output type. 
               
              * CALABASH_PRETTY_OUTPUT: The Calabash pretty output type. 
               
              * CALABASH_STANDARD_OUTPUT: The Calabash standard output type. 
               
              * CALABASH_JAVA_XML_OUTPUT: The Calabash Java XML output type. 
               
              * AUTOMATION_OUTPUT: The automation output type. 
               
              * APPIUM_SERVER_OUTPUT: The Appium server output type. 
               
              * APPIUM_JAVA_OUTPUT: The Appium Java output type. 
               
              * APPIUM_JAVA_XML_OUTPUT: The Appium Java XML output type. 
               
              * APPIUM_PYTHON_OUTPUT: The Appium Python output type. 
               
              * APPIUM_PYTHON_XML_OUTPUT: The Appium Python XML output type. 
               
              * EXPLORER_EVENT_LOG: The Explorer event log output type. 
               
              * EXPLORER_SUMMARY_LOG: The Explorer summary log output type. 
               
              * APPLICATION_CRASH_REPORT: The application crash report output type. 
               
              * XCTEST_LOG: The XCode test output type. 
               

              
            

            - **extension** *(string) --* 

              The artifact's file extension.

              
            

            - **url** *(string) --* 

              The pre-signed Amazon S3 URL that can be used with a corresponding GET request to download the artifact's file.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListDevicePools

  ::

    
    paginator = client.get_paginator('list_device_pools')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_device_pools`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevicePools>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          type='CURATED'|'PRIVATE',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The project ARN.

      

    
    :type type: string
    :param type: 

      The device pools' type.

       

      Allowed values include:

       

       
      * CURATED: A device pool that is created and managed by AWS Device Farm. 
       
      * PRIVATE: A device pool that is created and managed by the device pool developer. 
       

      

    
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
            'devicePools': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'rules': [
                        {
                            'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION',
                            'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list device pools request.

        
        

        - **devicePools** *(list) --* 

          Information about the device pools.

          
          

          - *(dict) --* 

            Represents a collection of device types.

            
            

            - **arn** *(string) --* 

              The device pool's ARN.

              
            

            - **name** *(string) --* 

              The device pool's name.

              
            

            - **description** *(string) --* 

              The device pool's description.

              
            

            - **type** *(string) --* 

              The device pool's type.

               

              Allowed values include:

               

               
              * CURATED: A device pool that is created and managed by AWS Device Farm. 
               
              * PRIVATE: A device pool that is created and managed by the device pool developer. 
               

              
            

            - **rules** *(list) --* 

              Information about the device pool's rules.

              
              

              - *(dict) --* 

                Represents a condition for a device pool.

                
                

                - **attribute** *(string) --* 

                  The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .

                   

                  Allowed values include:

                   

                   
                  * ARN: The ARN. 
                   
                  * FORM_FACTOR: The form factor (for example, phone or tablet). 
                   
                  * MANUFACTURER: The manufacturer. 
                   
                  * PLATFORM: The platform (for example, Android or iOS). 
                   
                  * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                   
                  * APPIUM_VERSION: The Appium version for the test. 
                   

                  
                

                - **operator** *(string) --* 

                  The rule's operator.

                   

                   
                  * EQUALS: The equals operator. 
                   
                  * GREATER_THAN: The greater-than operator. 
                   
                  * IN: The in operator. 
                   
                  * LESS_THAN: The less-than operator. 
                   
                  * NOT_IN: The not-in operator. 
                   
                  * CONTAINS: The contains operator. 
                   

                  
                

                - **value** *(string) --* 

                  The rule's value.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListDevices

  ::

    
    paginator = client.get_paginator('list_devices')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_devices`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevices>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: 

      The Amazon Resource Name (ARN) of the project.

      

    
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
            'devices': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list devices operation.

        
        

        - **devices** *(list) --* 

          Information about the devices.

          
          

          - *(dict) --* 

            Represents a device type that an app is tested against.

            
            

            - **arn** *(string) --* 

              The device's ARN.

              
            

            - **name** *(string) --* 

              The device's display name.

              
            

            - **manufacturer** *(string) --* 

              The device's manufacturer name.

              
            

            - **model** *(string) --* 

              The device's model name.

              
            

            - **formFactor** *(string) --* 

              The device's form factor.

               

              Allowed values include:

               

               
              * PHONE: The phone form factor. 
               
              * TABLET: The tablet form factor. 
               

              
            

            - **platform** *(string) --* 

              The device's platform.

               

              Allowed values include:

               

               
              * ANDROID: The Android platform. 
               
              * IOS: The iOS platform. 
               

              
            

            - **os** *(string) --* 

              The device's operating system type.

              
            

            - **cpu** *(dict) --* 

              Information about the device's CPU.

              
              

              - **frequency** *(string) --* 

                The CPU's frequency.

                
              

              - **architecture** *(string) --* 

                The CPU's architecture, for example x86 or ARM.

                
              

              - **clock** *(float) --* 

                The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                
          
            

            - **resolution** *(dict) --* 

              The resolution of the device.

              
              

              - **width** *(integer) --* 

                The screen resolution's width, expressed in pixels.

                
              

              - **height** *(integer) --* 

                The screen resolution's height, expressed in pixels.

                
          
            

            - **heapSize** *(integer) --* 

              The device's heap size, expressed in bytes.

              
            

            - **memory** *(integer) --* 

              The device's total memory size, expressed in bytes.

              
            

            - **image** *(string) --* 

              The device's image name.

              
            

            - **carrier** *(string) --* 

              The device's carrier.

              
            

            - **radio** *(string) --* 

              The device's radio.

              
            

            - **remoteAccessEnabled** *(boolean) --* 

              Specifies whether remote access has been enabled for the specified device.

              
            

            - **remoteDebugEnabled** *(boolean) --* 

              This flag is set to ``true`` if remote debugging is enabled for the device.

              
            

            - **fleetType** *(string) --* 

              The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

              
            

            - **fleetName** *(string) --* 

              The name of the fleet to which this device belongs.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListJobs

  ::

    
    paginator = client.get_paginator('list_jobs')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_jobs`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListJobs>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The jobs' ARNs.

      

    
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
            'jobs': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string'
                    },
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list jobs request.

        
        

        - **jobs** *(list) --* 

          Information about the jobs.

          
          

          - *(dict) --* 

            Represents a device.

            
            

            - **arn** *(string) --* 

              The job's ARN.

              
            

            - **name** *(string) --* 

              The job's name.

              
            

            - **type** *(string) --* 

              The job's type.

               

              Allowed values include the following:

               

               
              * BUILTIN_FUZZ: The built-in fuzz type. 
               
              * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
               
              * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
               
              * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
               
              * APPIUM_PYTHON: The Appium Python type. 
               
              * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
               
              * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
               
              * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
               
              * CALABASH: The Calabash type. 
               
              * INSTRUMENTATION: The Instrumentation type. 
               
              * UIAUTOMATION: The uiautomation type. 
               
              * UIAUTOMATOR: The uiautomator type. 
               
              * XCTEST: The XCode test type. 
               
              * XCTEST_UI: The XCode UI test type. 
               

              
            

            - **created** *(datetime) --* 

              When the job was created.

              
            

            - **status** *(string) --* 

              The job's status.

               

              Allowed values include:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The job's result.

               

              Allowed values include:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **started** *(datetime) --* 

              The job's start time.

              
            

            - **stopped** *(datetime) --* 

              The job's stop time.

              
            

            - **counters** *(dict) --* 

              The job's result counters.

              
              

              - **total** *(integer) --* 

                The total number of entities.

                
              

              - **passed** *(integer) --* 

                The number of passed entities.

                
              

              - **failed** *(integer) --* 

                The number of failed entities.

                
              

              - **warned** *(integer) --* 

                The number of warned entities.

                
              

              - **errored** *(integer) --* 

                The number of errored entities.

                
              

              - **stopped** *(integer) --* 

                The number of stopped entities.

                
              

              - **skipped** *(integer) --* 

                The number of skipped entities.

                
          
            

            - **message** *(string) --* 

              A message about the job's result.

              
            

            - **device** *(dict) --* 

              The device (phone or tablet).

              
              

              - **arn** *(string) --* 

                The device's ARN.

                
              

              - **name** *(string) --* 

                The device's display name.

                
              

              - **manufacturer** *(string) --* 

                The device's manufacturer name.

                
              

              - **model** *(string) --* 

                The device's model name.

                
              

              - **formFactor** *(string) --* 

                The device's form factor.

                 

                Allowed values include:

                 

                 
                * PHONE: The phone form factor. 
                 
                * TABLET: The tablet form factor. 
                 

                
              

              - **platform** *(string) --* 

                The device's platform.

                 

                Allowed values include:

                 

                 
                * ANDROID: The Android platform. 
                 
                * IOS: The iOS platform. 
                 

                
              

              - **os** *(string) --* 

                The device's operating system type.

                
              

              - **cpu** *(dict) --* 

                Information about the device's CPU.

                
                

                - **frequency** *(string) --* 

                  The CPU's frequency.

                  
                

                - **architecture** *(string) --* 

                  The CPU's architecture, for example x86 or ARM.

                  
                

                - **clock** *(float) --* 

                  The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                  
            
              

              - **resolution** *(dict) --* 

                The resolution of the device.

                
                

                - **width** *(integer) --* 

                  The screen resolution's width, expressed in pixels.

                  
                

                - **height** *(integer) --* 

                  The screen resolution's height, expressed in pixels.

                  
            
              

              - **heapSize** *(integer) --* 

                The device's heap size, expressed in bytes.

                
              

              - **memory** *(integer) --* 

                The device's total memory size, expressed in bytes.

                
              

              - **image** *(string) --* 

                The device's image name.

                
              

              - **carrier** *(string) --* 

                The device's carrier.

                
              

              - **radio** *(string) --* 

                The device's radio.

                
              

              - **remoteAccessEnabled** *(boolean) --* 

                Specifies whether remote access has been enabled for the specified device.

                
              

              - **remoteDebugEnabled** *(boolean) --* 

                This flag is set to ``true`` if remote debugging is enabled for the device.

                
              

              - **fleetType** *(string) --* 

                The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

                
              

              - **fleetName** *(string) --* 

                The name of the fleet to which this device belongs.

                
          
            

            - **deviceMinutes** *(dict) --* 

              Represents the total (metered or unmetered) minutes used by the job.

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListOfferingTransactions

  ::

    
    paginator = client.get_paginator('list_offering_transactions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_offering_transactions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferingTransactions>`_    


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
            'offeringTransactions': [
                {
                    'offeringStatus': {
                        'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                        'offering': {
                            'id': 'string',
                            'description': 'string',
                            'type': 'RECURRING',
                            'platform': 'ANDROID'|'IOS',
                            'recurringCharges': [
                                {
                                    'cost': {
                                        'amount': 123.0,
                                        'currencyCode': 'USD'
                                    },
                                    'frequency': 'MONTHLY'
                                },
                            ]
                        },
                        'quantity': 123,
                        'effectiveOn': datetime(2015, 1, 1)
                    },
                    'transactionId': 'string',
                    'offeringPromotionId': 'string',
                    'createdOn': datetime(2015, 1, 1),
                    'cost': {
                        'amount': 123.0,
                        'currencyCode': 'USD'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the transaction log of the specified offerings.

        
        

        - **offeringTransactions** *(list) --* 

          The audit log of subscriptions you have purchased and modified through AWS Device Farm.

          
          

          - *(dict) --* 

            Represents the metadata of an offering transaction.

            
            

            - **offeringStatus** *(dict) --* 

              The status of an offering transaction.

              
              

              - **type** *(string) --* 

                The type specified for the offering status.

                
              

              - **offering** *(dict) --* 

                Represents the metadata of an offering status.

                
                

                - **id** *(string) --* 

                  The ID that corresponds to a device offering.

                  
                

                - **description** *(string) --* 

                  A string describing the offering.

                  
                

                - **type** *(string) --* 

                  The type of offering (e.g., "RECURRING") for a device.

                  
                

                - **platform** *(string) --* 

                  The platform of the device (e.g., ANDROID or IOS).

                  
                

                - **recurringCharges** *(list) --* 

                  Specifies whether there are recurring charges for the offering.

                  
                  

                  - *(dict) --* 

                    Specifies whether charges for devices will be recurring.

                    
                    

                    - **cost** *(dict) --* 

                      The cost of the recurring charge.

                      
                      

                      - **amount** *(float) --* 

                        The numerical amount of an offering or transaction.

                        
                      

                      - **currencyCode** *(string) --* 

                        The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                        
                  
                    

                    - **frequency** *(string) --* 

                      The frequency in which charges will recur.

                      
                
              
            
              

              - **quantity** *(integer) --* 

                The number of available devices in the offering.

                
              

              - **effectiveOn** *(datetime) --* 

                The date on which the offering is effective.

                
          
            

            - **transactionId** *(string) --* 

              The transaction ID of the offering transaction.

              
            

            - **offeringPromotionId** *(string) --* 

              The ID that corresponds to a device offering promotion.

              
            

            - **createdOn** *(datetime) --* 

              The date on which an offering transaction was created.

              
            

            - **cost** *(dict) --* 

              The cost of an offering transaction.

              
              

              - **amount** *(float) --* 

                The numerical amount of an offering or transaction.

                
              

              - **currencyCode** *(string) --* 

                The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListOfferings

  ::

    
    paginator = client.get_paginator('list_offerings')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_offerings`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferings>`_    


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
            'offerings': [
                {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the return values of the list of offerings.

        
        

        - **offerings** *(list) --* 

          A value representing the list offering results.

          
          

          - *(dict) --* 

            Represents the metadata of a device offering.

            
            

            - **id** *(string) --* 

              The ID that corresponds to a device offering.

              
            

            - **description** *(string) --* 

              A string describing the offering.

              
            

            - **type** *(string) --* 

              The type of offering (e.g., "RECURRING") for a device.

              
            

            - **platform** *(string) --* 

              The platform of the device (e.g., ANDROID or IOS).

              
            

            - **recurringCharges** *(list) --* 

              Specifies whether there are recurring charges for the offering.

              
              

              - *(dict) --* 

                Specifies whether charges for devices will be recurring.

                
                

                - **cost** *(dict) --* 

                  The cost of the recurring charge.

                  
                  

                  - **amount** *(float) --* 

                    The numerical amount of an offering or transaction.

                    
                  

                  - **currencyCode** *(string) --* 

                    The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."

                    
              
                

                - **frequency** *(string) --* 

                  The frequency in which charges will recur.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListProjects

  ::

    
    paginator = client.get_paginator('list_projects')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_projects`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListProjects>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: 

      Optional. If no Amazon Resource Name (ARN) is specified, then AWS Device Farm returns a list of all projects for the AWS account. You can also specify a project ARN.

      

    
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
                {
                    'arn': 'string',
                    'name': 'string',
                    'defaultJobTimeoutMinutes': 123,
                    'created': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list projects request.

        
        

        - **projects** *(list) --* 

          Information about the projects.

          
          

          - *(dict) --* 

            Represents an operating-system neutral workspace for running and managing tests.

            
            

            - **arn** *(string) --* 

              The project's ARN.

              
            

            - **name** *(string) --* 

              The project's name.

              
            

            - **defaultJobTimeoutMinutes** *(integer) --* 

              The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.

              
            

            - **created** *(datetime) --* 

              When the project was created.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListRuns

  ::

    
    paginator = client.get_paginator('list_runs')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_runs`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListRuns>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to list runs.

      

    
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
            'runs': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                    'platform': 'ANDROID'|'IOS',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'totalJobs': 123,
                    'completedJobs': 123,
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'networkProfile': {
                        'arn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'CURATED'|'PRIVATE',
                        'uplinkBandwidthBits': 123,
                        'downlinkBandwidthBits': 123,
                        'uplinkDelayMs': 123,
                        'downlinkDelayMs': 123,
                        'uplinkJitterMs': 123,
                        'downlinkJitterMs': 123,
                        'uplinkLossPercent': 123,
                        'downlinkLossPercent': 123
                    },
                    'parsingResultUrl': 'string',
                    'resultCode': 'PARSING_FAILED',
                    'customerArtifactPaths': {
                        'iosPaths': [
                            'string',
                        ],
                        'androidPaths': [
                            'string',
                        ],
                        'deviceHostPaths': [
                            'string',
                        ]
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list runs request.

        
        

        - **runs** *(list) --* 

          Information about the runs.

          
          

          - *(dict) --* 

            Represents a test run on a set of devices with a given app package, test parameters, etc.

            
            

            - **arn** *(string) --* 

              The run's ARN.

              
            

            - **name** *(string) --* 

              The run's name.

              
            

            - **type** *(string) --* 

              The run's type.

               

              Must be one of the following values:

               

               
              * BUILTIN_FUZZ: The built-in fuzz type. 
               
              * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
               
              * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
               
              * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
               
              * APPIUM_PYTHON: The Appium Python type. 
               
              * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
               
              * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
               
              * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
               
              * CALABASH: The Calabash type. 
               
              * INSTRUMENTATION: The Instrumentation type. 
               
              * UIAUTOMATION: The uiautomation type. 
               
              * UIAUTOMATOR: The uiautomator type. 
               
              * XCTEST: The XCode test type. 
               
              * XCTEST_UI: The XCode UI test type. 
               

              
            

            - **platform** *(string) --* 

              The run's platform.

               

              Allowed values include:

               

               
              * ANDROID: The Android platform. 
               
              * IOS: The iOS platform. 
               

              
            

            - **created** *(datetime) --* 

              When the run was created.

              
            

            - **status** *(string) --* 

              The run's status.

               

              Allowed values include:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The run's result.

               

              Allowed values include:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **started** *(datetime) --* 

              The run's start time.

              
            

            - **stopped** *(datetime) --* 

              The run's stop time.

              
            

            - **counters** *(dict) --* 

              The run's result counters.

              
              

              - **total** *(integer) --* 

                The total number of entities.

                
              

              - **passed** *(integer) --* 

                The number of passed entities.

                
              

              - **failed** *(integer) --* 

                The number of failed entities.

                
              

              - **warned** *(integer) --* 

                The number of warned entities.

                
              

              - **errored** *(integer) --* 

                The number of errored entities.

                
              

              - **stopped** *(integer) --* 

                The number of stopped entities.

                
              

              - **skipped** *(integer) --* 

                The number of skipped entities.

                
          
            

            - **message** *(string) --* 

              A message about the run's result.

              
            

            - **totalJobs** *(integer) --* 

              The total number of jobs for the run.

              
            

            - **completedJobs** *(integer) --* 

              The total number of completed jobs.

              
            

            - **billingMethod** *(string) --* 

              Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .

              
            

            - **deviceMinutes** *(dict) --* 

              Represents the total (metered or unmetered) minutes used by the test run.

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
            

            - **networkProfile** *(dict) --* 

              The network profile being used for a test run.

              
              

              - **arn** *(string) --* 

                The Amazon Resource Name (ARN) of the network profile.

                
              

              - **name** *(string) --* 

                The name of the network profile.

                
              

              - **description** *(string) --* 

                The description of the network profile.

                
              

              - **type** *(string) --* 

                The type of network profile. Valid values are listed below.

                
              

              - **uplinkBandwidthBits** *(integer) --* 

                The data throughput rate in bits per second, as an integer from 0 to 104857600.

                
              

              - **downlinkBandwidthBits** *(integer) --* 

                The data throughput rate in bits per second, as an integer from 0 to 104857600.

                
              

              - **uplinkDelayMs** *(integer) --* 

                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

                
              

              - **downlinkDelayMs** *(integer) --* 

                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

                
              

              - **uplinkJitterMs** *(integer) --* 

                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

                
              

              - **downlinkJitterMs** *(integer) --* 

                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

                
              

              - **uplinkLossPercent** *(integer) --* 

                Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

                
              

              - **downlinkLossPercent** *(integer) --* 

                Proportion of received packets that fail to arrive from 0 to 100 percent.

                
          
            

            - **parsingResultUrl** *(string) --* 

              Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.

              
            

            - **resultCode** *(string) --* 

              Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.

              
            

            - **customerArtifactPaths** *(dict) --* 

              Output ``CustomerArtifactPaths`` object for the test run.

              
              

              - **iosPaths** *(list) --* 

                Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.

                
                

                - *(string) --* 
            
              

              - **androidPaths** *(list) --* 

                Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.

                
                

                - *(string) --* 
            
              

              - **deviceHostPaths** *(list) --* 

                Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.

                
                

                - *(string) --* 
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListSamples

  ::

    
    paginator = client.get_paginator('list_samples')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_samples`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListSamples>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to list samples.

      

    
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
            'samples': [
                {
                    'arn': 'string',
                    'type': 'CPU'|'MEMORY'|'THREADS'|'RX_RATE'|'TX_RATE'|'RX'|'TX'|'NATIVE_FRAMES'|'NATIVE_FPS'|'NATIVE_MIN_DRAWTIME'|'NATIVE_AVG_DRAWTIME'|'NATIVE_MAX_DRAWTIME'|'OPENGL_FRAMES'|'OPENGL_FPS'|'OPENGL_MIN_DRAWTIME'|'OPENGL_AVG_DRAWTIME'|'OPENGL_MAX_DRAWTIME',
                    'url': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list samples request.

        
        

        - **samples** *(list) --* 

          Information about the samples.

          
          

          - *(dict) --* 

            Represents a sample of performance data.

            
            

            - **arn** *(string) --* 

              The sample's ARN.

              
            

            - **type** *(string) --* 

              The sample's type.

               

              Must be one of the following values:

               

               
              * CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage. 
               
              * MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes. 
               
              * NATIVE_AVG_DRAWTIME 
               
              * NATIVE_FPS 
               
              * NATIVE_FRAMES 
               
              * NATIVE_MAX_DRAWTIME 
               
              * NATIVE_MIN_DRAWTIME 
               
              * OPENGL_AVG_DRAWTIME 
               
              * OPENGL_FPS 
               
              * OPENGL_FRAMES 
               
              * OPENGL_MAX_DRAWTIME 
               
              * OPENGL_MIN_DRAWTIME 
               
              * RX 
               
              * RX_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process. 
               
              * THREADS: A threads sample type. This is expressed as the total number of threads per app process. 
               
              * TX 
               
              * TX_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process. 
               

              
            

            - **url** *(string) --* 

              The pre-signed Amazon S3 URL that can be used with a corresponding GET request to download the sample's file.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListSuites

  ::

    
    paginator = client.get_paginator('list_suites')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_suites`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListSuites>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The suites' ARNs.

      

    
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
            'suites': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list suites request.

        
        

        - **suites** *(list) --* 

          Information about the suites.

          
          

          - *(dict) --* 

            Represents a collection of one or more tests.

            
            

            - **arn** *(string) --* 

              The suite's ARN.

              
            

            - **name** *(string) --* 

              The suite's name.

              
            

            - **type** *(string) --* 

              The suite's type.

               

              Must be one of the following values:

               

               
              * BUILTIN_FUZZ: The built-in fuzz type. 
               
              * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
               
              * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
               
              * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
               
              * APPIUM_PYTHON: The Appium Python type. 
               
              * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
               
              * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
               
              * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
               
              * CALABASH: The Calabash type. 
               
              * INSTRUMENTATION: The Instrumentation type. 
               
              * UIAUTOMATION: The uiautomation type. 
               
              * UIAUTOMATOR: The uiautomator type. 
               
              * XCTEST: The XCode test type. 
               
              * XCTEST_UI: The XCode UI test type. 
               

              
            

            - **created** *(datetime) --* 

              When the suite was created.

              
            

            - **status** *(string) --* 

              The suite's status.

               

              Allowed values include:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The suite's result.

               

              Allowed values include:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **started** *(datetime) --* 

              The suite's start time.

              
            

            - **stopped** *(datetime) --* 

              The suite's stop time.

              
            

            - **counters** *(dict) --* 

              The suite's result counters.

              
              

              - **total** *(integer) --* 

                The total number of entities.

                
              

              - **passed** *(integer) --* 

                The number of passed entities.

                
              

              - **failed** *(integer) --* 

                The number of failed entities.

                
              

              - **warned** *(integer) --* 

                The number of warned entities.

                
              

              - **errored** *(integer) --* 

                The number of errored entities.

                
              

              - **stopped** *(integer) --* 

                The number of stopped entities.

                
              

              - **skipped** *(integer) --* 

                The number of skipped entities.

                
          
            

            - **message** *(string) --* 

              A message about the suite's result.

              
            

            - **deviceMinutes** *(dict) --* 

              Represents the total (metered or unmetered) minutes used by the test suite.

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListTests

  ::

    
    paginator = client.get_paginator('list_tests')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_tests`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListTests>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The tests' ARNs.

      

    
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
            'tests': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list tests request.

        
        

        - **tests** *(list) --* 

          Information about the tests.

          
          

          - *(dict) --* 

            Represents a condition that is evaluated.

            
            

            - **arn** *(string) --* 

              The test's ARN.

              
            

            - **name** *(string) --* 

              The test's name.

              
            

            - **type** *(string) --* 

              The test's type.

               

              Must be one of the following values:

               

               
              * BUILTIN_FUZZ: The built-in fuzz type. 
               
              * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
               
              * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
               
              * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
               
              * APPIUM_PYTHON: The Appium Python type. 
               
              * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps. 
               
              * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps. 
               
              * APPIUM_WEB_PYTHON: The Appium Python type for Web apps. 
               
              * CALABASH: The Calabash type. 
               
              * INSTRUMENTATION: The Instrumentation type. 
               
              * UIAUTOMATION: The uiautomation type. 
               
              * UIAUTOMATOR: The uiautomator type. 
               
              * XCTEST: The XCode test type. 
               
              * XCTEST_UI: The XCode UI test type. 
               

              
            

            - **created** *(datetime) --* 

              When the test was created.

              
            

            - **status** *(string) --* 

              The test's status.

               

              Allowed values include:

               

               
              * PENDING: A pending status. 
               
              * PENDING_CONCURRENCY: A pending concurrency status. 
               
              * PENDING_DEVICE: A pending device status. 
               
              * PROCESSING: A processing status. 
               
              * SCHEDULING: A scheduling status. 
               
              * PREPARING: A preparing status. 
               
              * RUNNING: A running status. 
               
              * COMPLETED: A completed status. 
               
              * STOPPING: A stopping status. 
               

              
            

            - **result** *(string) --* 

              The test's result.

               

              Allowed values include:

               

               
              * PENDING: A pending condition. 
               
              * PASSED: A passing condition. 
               
              * WARNED: A warning condition. 
               
              * FAILED: A failed condition. 
               
              * SKIPPED: A skipped condition. 
               
              * ERRORED: An error condition. 
               
              * STOPPED: A stopped condition. 
               

              
            

            - **started** *(datetime) --* 

              The test's start time.

              
            

            - **stopped** *(datetime) --* 

              The test's stop time.

              
            

            - **counters** *(dict) --* 

              The test's result counters.

              
              

              - **total** *(integer) --* 

                The total number of entities.

                
              

              - **passed** *(integer) --* 

                The number of passed entities.

                
              

              - **failed** *(integer) --* 

                The number of failed entities.

                
              

              - **warned** *(integer) --* 

                The number of warned entities.

                
              

              - **errored** *(integer) --* 

                The number of errored entities.

                
              

              - **stopped** *(integer) --* 

                The number of stopped entities.

                
              

              - **skipped** *(integer) --* 

                The number of skipped entities.

                
          
            

            - **message** *(string) --* 

              A message about the test's result.

              
            

            - **deviceMinutes** *(dict) --* 

              Represents the total (metered or unmetered) minutes used by the test.

              
              

              - **total** *(float) --* 

                When specified, represents the total minutes used by the resource to run tests.

                
              

              - **metered** *(float) --* 

                When specified, represents only the sum of metered minutes used by the resource to run tests.

                
              

              - **unmetered** *(float) --* 

                When specified, represents only the sum of unmetered minutes used by the resource to run tests.

                
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListUniqueProblems

  ::

    
    paginator = client.get_paginator('list_unique_problems')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_unique_problems`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListUniqueProblems>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The unique problems' ARNs.

      

    
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
            'uniqueProblems': {
                'string': [
                    {
                        'message': 'string',
                        'problems': [
                            {
                                'run': {
                                    'arn': 'string',
                                    'name': 'string'
                                },
                                'job': {
                                    'arn': 'string',
                                    'name': 'string'
                                },
                                'suite': {
                                    'arn': 'string',
                                    'name': 'string'
                                },
                                'test': {
                                    'arn': 'string',
                                    'name': 'string'
                                },
                                'device': {
                                    'arn': 'string',
                                    'name': 'string',
                                    'manufacturer': 'string',
                                    'model': 'string',
                                    'formFactor': 'PHONE'|'TABLET',
                                    'platform': 'ANDROID'|'IOS',
                                    'os': 'string',
                                    'cpu': {
                                        'frequency': 'string',
                                        'architecture': 'string',
                                        'clock': 123.0
                                    },
                                    'resolution': {
                                        'width': 123,
                                        'height': 123
                                    },
                                    'heapSize': 123,
                                    'memory': 123,
                                    'image': 'string',
                                    'carrier': 'string',
                                    'radio': 'string',
                                    'remoteAccessEnabled': True|False,
                                    'remoteDebugEnabled': True|False,
                                    'fleetType': 'string',
                                    'fleetName': 'string'
                                },
                                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                                'message': 'string'
                            },
                        ]
                    },
                ]
            },
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list unique problems request.

        
        

        - **uniqueProblems** *(dict) --* 

          Information about the unique problems.

           

          Allowed values include:

           

           
          * PENDING: A pending condition. 
           
          * PASSED: A passing condition. 
           
          * WARNED: A warning condition. 
           
          * FAILED: A failed condition. 
           
          * SKIPPED: A skipped condition. 
           
          * ERRORED: An error condition. 
           
          * STOPPED: A stopped condition. 
           

          
          

          - *(string) --* 
            

            - *(list) --* 
              

              - *(dict) --* 

                A collection of one or more problems, grouped by their result.

                
                

                - **message** *(string) --* 

                  A message about the unique problems' result.

                  
                

                - **problems** *(list) --* 

                  Information about the problems.

                  
                  

                  - *(dict) --* 

                    Represents a specific warning or failure.

                    
                    

                    - **run** *(dict) --* 

                      Information about the associated run.

                      
                      

                      - **arn** *(string) --* 

                        The problem detail's ARN.

                        
                      

                      - **name** *(string) --* 

                        The problem detail's name.

                        
                  
                    

                    - **job** *(dict) --* 

                      Information about the associated job.

                      
                      

                      - **arn** *(string) --* 

                        The problem detail's ARN.

                        
                      

                      - **name** *(string) --* 

                        The problem detail's name.

                        
                  
                    

                    - **suite** *(dict) --* 

                      Information about the associated suite.

                      
                      

                      - **arn** *(string) --* 

                        The problem detail's ARN.

                        
                      

                      - **name** *(string) --* 

                        The problem detail's name.

                        
                  
                    

                    - **test** *(dict) --* 

                      Information about the associated test.

                      
                      

                      - **arn** *(string) --* 

                        The problem detail's ARN.

                        
                      

                      - **name** *(string) --* 

                        The problem detail's name.

                        
                  
                    

                    - **device** *(dict) --* 

                      Information about the associated device.

                      
                      

                      - **arn** *(string) --* 

                        The device's ARN.

                        
                      

                      - **name** *(string) --* 

                        The device's display name.

                        
                      

                      - **manufacturer** *(string) --* 

                        The device's manufacturer name.

                        
                      

                      - **model** *(string) --* 

                        The device's model name.

                        
                      

                      - **formFactor** *(string) --* 

                        The device's form factor.

                         

                        Allowed values include:

                         

                         
                        * PHONE: The phone form factor. 
                         
                        * TABLET: The tablet form factor. 
                         

                        
                      

                      - **platform** *(string) --* 

                        The device's platform.

                         

                        Allowed values include:

                         

                         
                        * ANDROID: The Android platform. 
                         
                        * IOS: The iOS platform. 
                         

                        
                      

                      - **os** *(string) --* 

                        The device's operating system type.

                        
                      

                      - **cpu** *(dict) --* 

                        Information about the device's CPU.

                        
                        

                        - **frequency** *(string) --* 

                          The CPU's frequency.

                          
                        

                        - **architecture** *(string) --* 

                          The CPU's architecture, for example x86 or ARM.

                          
                        

                        - **clock** *(float) --* 

                          The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

                          
                    
                      

                      - **resolution** *(dict) --* 

                        The resolution of the device.

                        
                        

                        - **width** *(integer) --* 

                          The screen resolution's width, expressed in pixels.

                          
                        

                        - **height** *(integer) --* 

                          The screen resolution's height, expressed in pixels.

                          
                    
                      

                      - **heapSize** *(integer) --* 

                        The device's heap size, expressed in bytes.

                        
                      

                      - **memory** *(integer) --* 

                        The device's total memory size, expressed in bytes.

                        
                      

                      - **image** *(string) --* 

                        The device's image name.

                        
                      

                      - **carrier** *(string) --* 

                        The device's carrier.

                        
                      

                      - **radio** *(string) --* 

                        The device's radio.

                        
                      

                      - **remoteAccessEnabled** *(boolean) --* 

                        Specifies whether remote access has been enabled for the specified device.

                        
                      

                      - **remoteDebugEnabled** *(boolean) --* 

                        This flag is set to ``true`` if remote debugging is enabled for the device.

                        
                      

                      - **fleetType** *(string) --* 

                        The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.

                        
                      

                      - **fleetName** *(string) --* 

                        The name of the fleet to which this device belongs.

                        
                  
                    

                    - **result** *(string) --* 

                      The problem's result.

                       

                      Allowed values include:

                       

                       
                      * PENDING: A pending condition. 
                       
                      * PASSED: A passing condition. 
                       
                      * WARNED: A warning condition. 
                       
                      * FAILED: A failed condition. 
                       
                      * SKIPPED: A skipped condition. 
                       
                      * ERRORED: An error condition. 
                       
                      * STOPPED: A stopped condition. 
                       

                      
                    

                    - **message** *(string) --* 

                      A message about the problem's result.

                      
                
              
            
          
      
    
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DeviceFarm.Paginator.ListUploads

  ::

    
    paginator = client.get_paginator('list_uploads')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_uploads`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListUploads>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          arn='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type arn: string
    :param arn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the project for which you want to list uploads.

      

    
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
            'uploads': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
                    'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                    'url': 'string',
                    'metadata': 'string',
                    'contentType': 'string',
                    'message': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the result of a list uploads request.

        
        

        - **uploads** *(list) --* 

          Information about the uploads.

          
          

          - *(dict) --* 

            An app or a set of one or more tests to upload or that have been uploaded.

            
            

            - **arn** *(string) --* 

              The upload's ARN.

              
            

            - **name** *(string) --* 

              The upload's file name.

              
            

            - **created** *(datetime) --* 

              When the upload was created.

              
            

            - **type** *(string) --* 

              The upload's type.

               

              Must be one of the following values:

               

               
              * ANDROID_APP: An Android upload. 
               
              * IOS_APP: An iOS upload. 
               
              * WEB_APP: A web appliction upload. 
               
              * EXTERNAL_DATA: An external data upload. 
               
              * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
               
              * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
               
              * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
               
              * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
               
              * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
               
              * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
               
              * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
               
              * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
               
              * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
               
              * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
               
              * XCTEST_TEST_PACKAGE: An XCode test package upload. 
               
              * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
               

              
            

            - **status** *(string) --* 

              The upload's status.

               

              Must be one of the following values:

               

               
              * FAILED: A failed status. 
               
              * INITIALIZED: An initialized status. 
               
              * PROCESSING: A processing status. 
               
              * SUCCEEDED: A succeeded status. 
               

              
            

            - **url** *(string) --* 

              The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.

              
            

            - **metadata** *(string) --* 

              The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

              
            

            - **contentType** *(string) --* 

              The upload's content type (for example, "application/octet-stream").

              
            

            - **message** *(string) --* 

              A message about the upload's result.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    