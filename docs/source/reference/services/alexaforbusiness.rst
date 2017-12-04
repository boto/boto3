

****************
AlexaForBusiness
****************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: AlexaForBusiness.Client

  A low-level client representing Alexa For Business::

    
    import boto3
    
    client = boto3.client('alexaforbusiness')

  
  These are the available methods:
  
  *   :py:meth:`~AlexaForBusiness.Client.associate_device_with_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.associate_skill_group_with_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.can_paginate`

  
  *   :py:meth:`~AlexaForBusiness.Client.create_profile`

  
  *   :py:meth:`~AlexaForBusiness.Client.create_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.create_skill_group`

  
  *   :py:meth:`~AlexaForBusiness.Client.create_user`

  
  *   :py:meth:`~AlexaForBusiness.Client.delete_profile`

  
  *   :py:meth:`~AlexaForBusiness.Client.delete_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.delete_room_skill_parameter`

  
  *   :py:meth:`~AlexaForBusiness.Client.delete_skill_group`

  
  *   :py:meth:`~AlexaForBusiness.Client.delete_user`

  
  *   :py:meth:`~AlexaForBusiness.Client.disassociate_device_from_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.disassociate_skill_group_from_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.generate_presigned_url`

  
  *   :py:meth:`~AlexaForBusiness.Client.get_device`

  
  *   :py:meth:`~AlexaForBusiness.Client.get_paginator`

  
  *   :py:meth:`~AlexaForBusiness.Client.get_profile`

  
  *   :py:meth:`~AlexaForBusiness.Client.get_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.get_room_skill_parameter`

  
  *   :py:meth:`~AlexaForBusiness.Client.get_skill_group`

  
  *   :py:meth:`~AlexaForBusiness.Client.get_waiter`

  
  *   :py:meth:`~AlexaForBusiness.Client.list_skills`

  
  *   :py:meth:`~AlexaForBusiness.Client.list_tags`

  
  *   :py:meth:`~AlexaForBusiness.Client.put_room_skill_parameter`

  
  *   :py:meth:`~AlexaForBusiness.Client.resolve_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.revoke_invitation`

  
  *   :py:meth:`~AlexaForBusiness.Client.search_devices`

  
  *   :py:meth:`~AlexaForBusiness.Client.search_profiles`

  
  *   :py:meth:`~AlexaForBusiness.Client.search_rooms`

  
  *   :py:meth:`~AlexaForBusiness.Client.search_skill_groups`

  
  *   :py:meth:`~AlexaForBusiness.Client.search_users`

  
  *   :py:meth:`~AlexaForBusiness.Client.send_invitation`

  
  *   :py:meth:`~AlexaForBusiness.Client.start_device_sync`

  
  *   :py:meth:`~AlexaForBusiness.Client.tag_resource`

  
  *   :py:meth:`~AlexaForBusiness.Client.untag_resource`

  
  *   :py:meth:`~AlexaForBusiness.Client.update_device`

  
  *   :py:meth:`~AlexaForBusiness.Client.update_profile`

  
  *   :py:meth:`~AlexaForBusiness.Client.update_room`

  
  *   :py:meth:`~AlexaForBusiness.Client.update_skill_group`

  

  .. py:method:: associate_device_with_room(**kwargs)

    

    Associates a device to a given room. This applies all the settings from the room profile to the device, and all the skills in any skill groups added to that room. This operation requires the device to be online, or a manual sync is required. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/AssociateDeviceWithRoom>`_    


    **Request Syntax** 
    ::

      response = client.associate_device_with_room(
          DeviceArn='string',
          RoomArn='string'
      )
    :type DeviceArn: string
    :param DeviceArn: 

      The ARN of the device to associate to a room. Required.

      

    
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room with which to associate the device. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: associate_skill_group_with_room(**kwargs)

    

    Associates a skill group to a given room. This enables all skills in the associated skill group on all devices in the room.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/AssociateSkillGroupWithRoom>`_    


    **Request Syntax** 
    ::

      response = client.associate_skill_group_with_room(
          SkillGroupArn='string',
          RoomArn='string'
      )
    :type SkillGroupArn: string
    :param SkillGroupArn: 

      The ARN of the skill group to associate with a room. Required.

      

    
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room with which to associate the skill group. Required.

      

    
    
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


  .. py:method:: create_profile(**kwargs)

    

    Creates a new room profile with the specified details.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateProfile>`_    


    **Request Syntax** 
    ::

      response = client.create_profile(
          ProfileName='string',
          Timezone='string',
          Address='string',
          DistanceUnit='METRIC'|'IMPERIAL',
          TemperatureUnit='FAHRENHEIT'|'CELSIUS',
          WakeWord='ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
          ClientRequestToken='string',
          SetupModeDisabled=True|False,
          MaxVolumeLimit=123,
          PSTNEnabled=True|False
      )
    :type ProfileName: string
    :param ProfileName: **[REQUIRED]** 

      The name of a room profile.

      

    
    :type Timezone: string
    :param Timezone: **[REQUIRED]** 

      The time zone used by a room profile.

      

    
    :type Address: string
    :param Address: **[REQUIRED]** 

      The valid address for the room.

      

    
    :type DistanceUnit: string
    :param DistanceUnit: **[REQUIRED]** 

      The distance unit to be used by devices in the profile.

      

    
    :type TemperatureUnit: string
    :param TemperatureUnit: **[REQUIRED]** 

      The temperature unit to be used by devices in the profile.

      

    
    :type WakeWord: string
    :param WakeWord: **[REQUIRED]** 

      A wake word for Alexa, Echo, Amazon, or a computer.

      

    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      The user-specified token that is used during the creation of a profile.

      This field is autopopulated if not provided.

    
    :type SetupModeDisabled: boolean
    :param SetupModeDisabled: 

      Whether room profile setup is enabled.

      

    
    :type MaxVolumeLimit: integer
    :param MaxVolumeLimit: 

      The maximum volume limit for a room profile.

      

    
    :type PSTNEnabled: boolean
    :param PSTNEnabled: 

      Whether PSTN calling is enabled.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProfileArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProfileArn** *(string) --* 

          The ARN of the newly created room profile in the response.

          
    

  .. py:method:: create_room(**kwargs)

    

    Creates a room with the specified details.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateRoom>`_    


    **Request Syntax** 
    ::

      response = client.create_room(
          RoomName='string',
          Description='string',
          ProfileArn='string',
          ProviderCalendarId='string',
          ClientRequestToken='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type RoomName: string
    :param RoomName: **[REQUIRED]** 

      The name for the room.

      

    
    :type Description: string
    :param Description: 

      The description for the room.

      

    
    :type ProfileArn: string
    :param ProfileArn: 

      The profile ARN for the room.

      

    
    :type ProviderCalendarId: string
    :param ProviderCalendarId: 

      The calendar ARN for the room.

      

    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      A unique, user-specified identifier for this request that ensures idempotency. 

      This field is autopopulated if not provided.

    
    :type Tags: list
    :param Tags: 

      The tags for the room.

      

    
      - *(dict) --* 

        A key-value pair that can be associated with a resource. 

        

      
        - **Key** *(string) --* 

          The key of a tag. Tag keys are case-sensitive. 

          

        
        - **Value** *(string) --* 

          The value of a tag. Tag values are case-sensitive and can be null.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RoomArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RoomArn** *(string) --* 

          The ARN of the newly created room in the response.

          
    

  .. py:method:: create_skill_group(**kwargs)

    

    Creates a skill group with a specified name and description.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateSkillGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_skill_group(
          SkillGroupName='string',
          Description='string',
          ClientRequestToken='string'
      )
    :type SkillGroupName: string
    :param SkillGroupName: **[REQUIRED]** 

      The name for the skill group.

      

    
    :type Description: string
    :param Description: 

      The description for the skill group.

      

    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      A unique, user-specified identifier for this request that ensures idempotency. 

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SkillGroupArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SkillGroupArn** *(string) --* 

          The ARN of the newly created skill group in the response.

          
    

  .. py:method:: create_user(**kwargs)

    

    Creates a user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateUser>`_    


    **Request Syntax** 
    ::

      response = client.create_user(
          UserId='string',
          FirstName='string',
          LastName='string',
          Email='string',
          ClientRequestToken='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type UserId: string
    :param UserId: **[REQUIRED]** 

      The ARN for the user.

      

    
    :type FirstName: string
    :param FirstName: 

      The first name for the user.

      

    
    :type LastName: string
    :param LastName: 

      The last name for the user.

      

    
    :type Email: string
    :param Email: 

      The email address for the user.

      

    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      A unique, user-specified identifier for this request that ensures idempotency. 

      This field is autopopulated if not provided.

    
    :type Tags: list
    :param Tags: 

      The tags for the user.

      

    
      - *(dict) --* 

        A key-value pair that can be associated with a resource. 

        

      
        - **Key** *(string) --* 

          The key of a tag. Tag keys are case-sensitive. 

          

        
        - **Value** *(string) --* 

          The value of a tag. Tag values are case-sensitive and can be null.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UserArn** *(string) --* 

          The ARN of the newly created user in the response.

          
    

  .. py:method:: delete_profile(**kwargs)

    

    Deletes a room profile by the profile ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteProfile>`_    


    **Request Syntax** 
    ::

      response = client.delete_profile(
          ProfileArn='string'
      )
    :type ProfileArn: string
    :param ProfileArn: 

      The ARN of the room profile to delete. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_room(**kwargs)

    

    Deletes a room by the room ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteRoom>`_    


    **Request Syntax** 
    ::

      response = client.delete_room(
          RoomArn='string'
      )
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room to delete. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_room_skill_parameter(**kwargs)

    

    Deletes room skill parameter details by room, skill, and parameter key ID.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteRoomSkillParameter>`_    


    **Request Syntax** 
    ::

      response = client.delete_room_skill_parameter(
          RoomArn='string',
          SkillId='string',
          ParameterKey='string'
      )
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room from which to remove the room skill parameter details.

      

    
    :type SkillId: string
    :param SkillId: **[REQUIRED]** 

      The ID of the skill from which to remove the room skill parameter details.

      

    
    :type ParameterKey: string
    :param ParameterKey: **[REQUIRED]** 

      The room skill parameter key for which to remove details.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_skill_group(**kwargs)

    

    Deletes a skill group by skill group ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteSkillGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_skill_group(
          SkillGroupArn='string'
      )
    :type SkillGroupArn: string
    :param SkillGroupArn: 

      The ARN of the skill group to delete. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_user(**kwargs)

    

    Deletes a specified user by user ARN and enrollment ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteUser>`_    


    **Request Syntax** 
    ::

      response = client.delete_user(
          UserArn='string',
          EnrollmentId='string'
      )
    :type UserArn: string
    :param UserArn: 

      The ARN of the user to delete in the organization. Required.

      

    
    :type EnrollmentId: string
    :param EnrollmentId: **[REQUIRED]** 

      The ARN of the user's enrollment in the organization. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: disassociate_device_from_room(**kwargs)

    

    Disassociates a device from its current room. The device continues to be connected to the Wi-Fi network and is still registered to the account. The device settings and skills are removed from the room.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DisassociateDeviceFromRoom>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_device_from_room(
          DeviceArn='string'
      )
    :type DeviceArn: string
    :param DeviceArn: 

      The ARN of the device to disassociate from a room. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: disassociate_skill_group_from_room(**kwargs)

    

    Disassociates a skill group from a specified room. This disables all skills in the skill group on all devices in the room.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DisassociateSkillGroupFromRoom>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_skill_group_from_room(
          SkillGroupArn='string',
          RoomArn='string'
      )
    :type SkillGroupArn: string
    :param SkillGroupArn: 

      The ARN of the skill group to disassociate from a room. Required.

      

    
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room from which the skill group is to be disassociated. Required.

      

    
    
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


  .. py:method:: get_device(**kwargs)

    

    Gets the details of a device by device ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetDevice>`_    


    **Request Syntax** 
    ::

      response = client.get_device(
          DeviceArn='string'
      )
    :type DeviceArn: string
    :param DeviceArn: 

      The ARN of the device for which to request details. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Device': {
                'DeviceArn': 'string',
                'DeviceSerialNumber': 'string',
                'DeviceType': 'string',
                'DeviceName': 'string',
                'SoftwareVersion': 'string',
                'MacAddress': 'string',
                'RoomArn': 'string',
                'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Device** *(dict) --* 

          The details of the device requested. Required.

          
          

          - **DeviceArn** *(string) --* 

            The ARN of a device.

            
          

          - **DeviceSerialNumber** *(string) --* 

            The serial number of a device.

            
          

          - **DeviceType** *(string) --* 

            The type of a device.

            
          

          - **DeviceName** *(string) --* 

            The name of a device.

            
          

          - **SoftwareVersion** *(string) --* 

            The software version of a device.

            
          

          - **MacAddress** *(string) --* 

            The MAC address of a device.

            
          

          - **RoomArn** *(string) --* 

            The room ARN of a device.

            
          

          - **DeviceStatus** *(string) --* 

            The status of a device.

            
      
    

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


  .. py:method:: get_profile(**kwargs)

    

    Gets the details of a room profile by profile ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetProfile>`_    


    **Request Syntax** 
    ::

      response = client.get_profile(
          ProfileArn='string'
      )
    :type ProfileArn: string
    :param ProfileArn: 

      The ARN of the room profile for which to request details. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Profile': {
                'ProfileArn': 'string',
                'ProfileName': 'string',
                'Address': 'string',
                'Timezone': 'string',
                'DistanceUnit': 'METRIC'|'IMPERIAL',
                'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
                'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
                'SetupModeDisabled': True|False,
                'MaxVolumeLimit': 123,
                'PSTNEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Profile** *(dict) --* 

          The details of the room profile requested. Required.

          
          

          - **ProfileArn** *(string) --* 

            The ARN of a room profile.

            
          

          - **ProfileName** *(string) --* 

            The name of a room profile.

            
          

          - **Address** *(string) --* 

            The address of a room profile.

            
          

          - **Timezone** *(string) --* 

            The time zone of a room profile.

            
          

          - **DistanceUnit** *(string) --* 

            The distance unit of a room profile.

            
          

          - **TemperatureUnit** *(string) --* 

            The temperature unit of a room profile.

            
          

          - **WakeWord** *(string) --* 

            The wake word of a room profile.

            
          

          - **SetupModeDisabled** *(boolean) --* 

            The setup mode of a room profile.

            
          

          - **MaxVolumeLimit** *(integer) --* 

            The max volume limit of a room profile.

            
          

          - **PSTNEnabled** *(boolean) --* 

            The PSTN setting of a room profile.

            
      
    

  .. py:method:: get_room(**kwargs)

    

    Gets room details by room ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetRoom>`_    


    **Request Syntax** 
    ::

      response = client.get_room(
          RoomArn='string'
      )
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room for which to request details. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Room': {
                'RoomArn': 'string',
                'RoomName': 'string',
                'Description': 'string',
                'ProviderCalendarId': 'string',
                'ProfileArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Room** *(dict) --* 

          The details of the room requested.

          
          

          - **RoomArn** *(string) --* 

            The ARN of a room.

            
          

          - **RoomName** *(string) --* 

            The name of a room.

            
          

          - **Description** *(string) --* 

            The description of a room.

            
          

          - **ProviderCalendarId** *(string) --* 

            The provider calendar ARN of a room.

            
          

          - **ProfileArn** *(string) --* 

            The profile ARN of a room.

            
      
    

  .. py:method:: get_room_skill_parameter(**kwargs)

    

    Gets room skill parameter details by room, skill, and parameter key ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetRoomSkillParameter>`_    


    **Request Syntax** 
    ::

      response = client.get_room_skill_parameter(
          RoomArn='string',
          SkillId='string',
          ParameterKey='string'
      )
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room from which to get the room skill parameter details. 

      

    
    :type SkillId: string
    :param SkillId: **[REQUIRED]** 

      The ARN of the skill from which to get the room skill parameter details. Required.

      

    
    :type ParameterKey: string
    :param ParameterKey: **[REQUIRED]** 

      The room skill parameter key for which to get details. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RoomSkillParameter': {
                'ParameterKey': 'string',
                'ParameterValue': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RoomSkillParameter** *(dict) --* 

          The details of the room skill parameter requested. Required.

          
          

          - **ParameterKey** *(string) --* 

            The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes “DEFAULT” or “SCOPE” as valid values.

            
          

          - **ParameterValue** *(string) --* 

            The parameter value of a room skill parameter.

            
      
    

  .. py:method:: get_skill_group(**kwargs)

    

    Gets skill group details by skill group ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetSkillGroup>`_    


    **Request Syntax** 
    ::

      response = client.get_skill_group(
          SkillGroupArn='string'
      )
    :type SkillGroupArn: string
    :param SkillGroupArn: 

      The ARN of the skill group for which to get details. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SkillGroup': {
                'SkillGroupArn': 'string',
                'SkillGroupName': 'string',
                'Description': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SkillGroup** *(dict) --* 

          The details of the skill group requested. Required.

          
          

          - **SkillGroupArn** *(string) --* 

            The ARN of a skill group.

            
          

          - **SkillGroupName** *(string) --* 

            The name of a skill group.

            
          

          - **Description** *(string) --* 

            The description of a skill group.

            
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_skills(**kwargs)

    

    Lists all enabled skills in a specific skill group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSkills>`_    


    **Request Syntax** 
    ::

      response = client.list_skills(
          SkillGroupArn='string',
          NextToken='string',
          MaxResults=123
      )
    :type SkillGroupArn: string
    :param SkillGroupArn: 

      The ARN of the skill group for which to list enabled skills. Required.

      

    
    :type NextToken: string
    :param NextToken: 

      An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` . Required.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SkillSummaries': [
                {
                    'SkillId': 'string',
                    'SkillName': 'string',
                    'SupportsLinking': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SkillSummaries** *(list) --* 

          The list of enabled skills requested. Required.

          
          

          - *(dict) --* 

            The summary of skills.

            
            

            - **SkillId** *(string) --* 

              The ARN of the skill summary.

              
            

            - **SkillName** *(string) --* 

              The name of the skill.

              
            

            - **SupportsLinking** *(boolean) --* 

              Linking support for a skill.

              
        
      
        

        - **NextToken** *(string) --* 

          The token returned to indicate that there is more data available.

          
    

  .. py:method:: list_tags(**kwargs)

    

    Lists all tags for a specific resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListTags>`_    


    **Request Syntax** 
    ::

      response = client.list_tags(
          Arn='string',
          NextToken='string',
          MaxResults=123
      )
    :type Arn: string
    :param Arn: **[REQUIRED]** 

      The ARN of the specific resource for which to list tags. Required.

      

    
    :type NextToken: string
    :param NextToken: 

      An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` . 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Tags** *(list) --* 

          The list of tags requested for the specific resource.

          
          

          - *(dict) --* 

            A key-value pair that can be associated with a resource. 

            
            

            - **Key** *(string) --* 

              The key of a tag. Tag keys are case-sensitive. 

              
            

            - **Value** *(string) --* 

              The value of a tag. Tag values are case-sensitive and can be null.

              
        
      
        

        - **NextToken** *(string) --* 

          The token returned to indicate that there is more data available.

          
    

  .. py:method:: put_room_skill_parameter(**kwargs)

    

    Updates room skill parameter details by room, skill, and parameter key ID. Not all skills have a room skill parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/PutRoomSkillParameter>`_    


    **Request Syntax** 
    ::

      response = client.put_room_skill_parameter(
          RoomArn='string',
          SkillId='string',
          RoomSkillParameter={
              'ParameterKey': 'string',
              'ParameterValue': 'string'
          }
      )
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room associated with the room skill parameter. Required.

      

    
    :type SkillId: string
    :param SkillId: **[REQUIRED]** 

      The ARN of the skill associated with the room skill parameter. Required.

      

    
    :type RoomSkillParameter: dict
    :param RoomSkillParameter: **[REQUIRED]** 

      The updated room skill parameter. Required.

      

    
      - **ParameterKey** *(string) --* **[REQUIRED]** 

        The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes “DEFAULT” or “SCOPE” as valid values.

        

      
      - **ParameterValue** *(string) --* **[REQUIRED]** 

        The parameter value of a room skill parameter.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: resolve_room(**kwargs)

    

    Determines the details for the room from which a skill request was invoked. This operation is used by skill developers.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ResolveRoom>`_    


    **Request Syntax** 
    ::

      response = client.resolve_room(
          UserId='string',
          SkillId='string'
      )
    :type UserId: string
    :param UserId: **[REQUIRED]** 

      The ARN of the user. Required.

      

    
    :type SkillId: string
    :param SkillId: **[REQUIRED]** 

      The ARN of the skill that was requested. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RoomArn': 'string',
            'RoomName': 'string',
            'RoomSkillParameters': [
                {
                    'ParameterKey': 'string',
                    'ParameterValue': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RoomArn** *(string) --* 

          The ARN of the room from which the skill request was invoked.

          
        

        - **RoomName** *(string) --* 

          The name of the room from which the skill request was invoked.

          
        

        - **RoomSkillParameters** *(list) --* 

          Response to get the room profile request. Required.

          
          

          - *(dict) --* 

            A skill parameter associated with a room.

            
            

            - **ParameterKey** *(string) --* 

              The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes “DEFAULT” or “SCOPE” as valid values.

              
            

            - **ParameterValue** *(string) --* 

              The parameter value of a room skill parameter.

              
        
      
    

  .. py:method:: revoke_invitation(**kwargs)

    

    Revokes an invitation and invalidates the enrollment URL.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/RevokeInvitation>`_    


    **Request Syntax** 
    ::

      response = client.revoke_invitation(
          UserArn='string',
          EnrollmentId='string'
      )
    :type UserArn: string
    :param UserArn: 

      The ARN of the user for whom to revoke an enrollment invitation. Required.

      

    
    :type EnrollmentId: string
    :param EnrollmentId: 

      The ARN of the enrollment invitation to revoke. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: search_devices(**kwargs)

    

    Searches devices and lists the ones that meet a set of filter criteria.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchDevices>`_    


    **Request Syntax** 
    ::

      response = client.search_devices(
          NextToken='string',
          MaxResults=123,
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          SortCriteria=[
              {
                  'Key': 'string',
                  'Value': 'ASC'|'DESC'
              },
          ]
      )
    :type NextToken: string
    :param NextToken: 

      An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      The filters to use to list a specified set of devices. Supported filter keys are DeviceName, DeviceStatus, RoomName, DeviceType, DeviceSerialNumber, and UnassociatedOnly.

      

    
      - *(dict) --* 

        A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of a filter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The values of a filter.

          

        
          - *(string) --* 

          
      
      
  
    :type SortCriteria: list
    :param SortCriteria: 

      The sort order to use in listing the specified set of devices. Supported sort keys are DeviceName, DeviceStatus, RoomName, DeviceType, and DeviceSerialNumber.

      

    
      - *(dict) --* 

        An object representing a sort criteria. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The sort key of a sort object.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The sort value of a sort object.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Devices': [
                {
                    'DeviceArn': 'string',
                    'DeviceSerialNumber': 'string',
                    'DeviceType': 'string',
                    'DeviceName': 'string',
                    'SoftwareVersion': 'string',
                    'MacAddress': 'string',
                    'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE',
                    'RoomArn': 'string',
                    'RoomName': 'string'
                },
            ],
            'NextToken': 'string',
            'TotalCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Devices** *(list) --* 

          The devices that meet the specified set of filter criteria, in sort order.

          
          

          - *(dict) --* 

            Device attributes.

            
            

            - **DeviceArn** *(string) --* 

              The ARN of a device.

              
            

            - **DeviceSerialNumber** *(string) --* 

              The serial number of a device.

              
            

            - **DeviceType** *(string) --* 

              The type of a device.

              
            

            - **DeviceName** *(string) --* 

              The name of a device.

              
            

            - **SoftwareVersion** *(string) --* 

              The software version of a device.

              
            

            - **MacAddress** *(string) --* 

              The MAC address of a device.

              
            

            - **DeviceStatus** *(string) --* 

              The status of a device.

              
            

            - **RoomArn** *(string) --* 

              The room ARN associated with a device.

              
            

            - **RoomName** *(string) --* 

              The name of the room associated with a device.

              
        
      
        

        - **NextToken** *(string) --* 

          The token returned to indicate that there is more data available.

          
        

        - **TotalCount** *(integer) --* 

          The total number of devices returned.

          
    

  .. py:method:: search_profiles(**kwargs)

    

    Searches room profiles and lists the ones that meet a set of filter criteria.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchProfiles>`_    


    **Request Syntax** 
    ::

      response = client.search_profiles(
          NextToken='string',
          MaxResults=123,
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          SortCriteria=[
              {
                  'Key': 'string',
                  'Value': 'ASC'|'DESC'
              },
          ]
      )
    :type NextToken: string
    :param NextToken: 

      An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.

      

    
    :type Filters: list
    :param Filters: 

      The filters to use to list a specified set of room profiles. Supported filter keys are ProfileName and Address. Required. 

      

    
      - *(dict) --* 

        A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of a filter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The values of a filter.

          

        
          - *(string) --* 

          
      
      
  
    :type SortCriteria: list
    :param SortCriteria: 

      The sort order to use in listing the specified set of room profiles. Supported sort keys are ProfileName and Address.

      

    
      - *(dict) --* 

        An object representing a sort criteria. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The sort key of a sort object.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The sort value of a sort object.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Profiles': [
                {
                    'ProfileArn': 'string',
                    'ProfileName': 'string',
                    'Address': 'string',
                    'Timezone': 'string',
                    'DistanceUnit': 'METRIC'|'IMPERIAL',
                    'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
                    'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER'
                },
            ],
            'NextToken': 'string',
            'TotalCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Profiles** *(list) --* 

          The profiles that meet the specified set of filter criteria, in sort order.

          
          

          - *(dict) --* 

            The data of a room profile.

            
            

            - **ProfileArn** *(string) --* 

              The ARN of a room profile.

              
            

            - **ProfileName** *(string) --* 

              The name of a room profile.

              
            

            - **Address** *(string) --* 

              The address of a room profile.

              
            

            - **Timezone** *(string) --* 

              The timezone of a room profile.

              
            

            - **DistanceUnit** *(string) --* 

              The distance unit of a room profile.

              
            

            - **TemperatureUnit** *(string) --* 

              The temperature unit of a room profile.

              
            

            - **WakeWord** *(string) --* 

              The wake word of a room profile.

              
        
      
        

        - **NextToken** *(string) --* 

          The token returned to indicate that there is more data available.

          
        

        - **TotalCount** *(integer) --* 

          The total number of room profiles returned.

          
    

  .. py:method:: search_rooms(**kwargs)

    

    Searches rooms and lists the ones that meet a set of filter and sort criteria.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchRooms>`_    


    **Request Syntax** 
    ::

      response = client.search_rooms(
          NextToken='string',
          MaxResults=123,
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          SortCriteria=[
              {
                  'Key': 'string',
                  'Value': 'ASC'|'DESC'
              },
          ]
      )
    :type NextToken: string
    :param NextToken: 

      An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved. 

      

    
    :type Filters: list
    :param Filters: 

      The filters to use to list a specified set of rooms. The supported filter keys are RoomName and ProfileName.

      

    
      - *(dict) --* 

        A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of a filter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The values of a filter.

          

        
          - *(string) --* 

          
      
      
  
    :type SortCriteria: list
    :param SortCriteria: 

      The sort order to use in listing the specified set of rooms. The supported sort keys are RoomName and ProfileName.

      

    
      - *(dict) --* 

        An object representing a sort criteria. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The sort key of a sort object.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The sort value of a sort object.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rooms': [
                {
                    'RoomArn': 'string',
                    'RoomName': 'string',
                    'Description': 'string',
                    'ProviderCalendarId': 'string',
                    'ProfileArn': 'string',
                    'ProfileName': 'string'
                },
            ],
            'NextToken': 'string',
            'TotalCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rooms** *(list) --* 

          The rooms that meet the specified set of filter criteria, in sort order.

          
          

          - *(dict) --* 

            The data of a room.

            
            

            - **RoomArn** *(string) --* 

              The ARN of a room.

              
            

            - **RoomName** *(string) --* 

              The name of a room.

              
            

            - **Description** *(string) --* 

              The description of a room.

              
            

            - **ProviderCalendarId** *(string) --* 

              The provider calendar ARN of a room.

              
            

            - **ProfileArn** *(string) --* 

              The profile ARN of a room.

              
            

            - **ProfileName** *(string) --* 

              The profile name of a room.

              
        
      
        

        - **NextToken** *(string) --* 

          The token returned to indicate that there is more data available.

          
        

        - **TotalCount** *(integer) --* 

          The total number of rooms returned.

          
    

  .. py:method:: search_skill_groups(**kwargs)

    

    Searches skill groups and lists the ones that meet a set of filter and sort criteria.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchSkillGroups>`_    


    **Request Syntax** 
    ::

      response = client.search_skill_groups(
          NextToken='string',
          MaxResults=123,
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          SortCriteria=[
              {
                  'Key': 'string',
                  'Value': 'ASC'|'DESC'
              },
          ]
      )
    :type NextToken: string
    :param NextToken: 

      An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` . Required.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved. 

      

    
    :type Filters: list
    :param Filters: 

      The filters to use to list a specified set of skill groups. The supported filter key is SkillGroupName. 

      

    
      - *(dict) --* 

        A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of a filter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The values of a filter.

          

        
          - *(string) --* 

          
      
      
  
    :type SortCriteria: list
    :param SortCriteria: 

      The sort order to use in listing the specified set of skill groups. The supported sort key is SkillGroupName. 

      

    
      - *(dict) --* 

        An object representing a sort criteria. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The sort key of a sort object.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The sort value of a sort object.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SkillGroups': [
                {
                    'SkillGroupArn': 'string',
                    'SkillGroupName': 'string',
                    'Description': 'string'
                },
            ],
            'NextToken': 'string',
            'TotalCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SkillGroups** *(list) --* 

          The skill groups that meet the filter criteria, in sort order.

          
          

          - *(dict) --* 

            The attributes of a skill group.

            
            

            - **SkillGroupArn** *(string) --* 

              The skill group ARN of a skill group.

              
            

            - **SkillGroupName** *(string) --* 

              The skill group name of a skill group.

              
            

            - **Description** *(string) --* 

              The description of a skill group.

              
        
      
        

        - **NextToken** *(string) --* 

          The token returned to indicate that there is more data available.

          
        

        - **TotalCount** *(integer) --* 

          The total number of skill groups returned.

          
    

  .. py:method:: search_users(**kwargs)

    

    Searches users and lists the ones that meet a set of filter and sort criteria.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchUsers>`_    


    **Request Syntax** 
    ::

      response = client.search_users(
          NextToken='string',
          MaxResults=123,
          Filters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          SortCriteria=[
              {
                  'Key': 'string',
                  'Value': 'ASC'|'DESC'
              },
          ]
      )
    :type NextToken: string
    :param NextToken: 

      An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` . Required.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved. Required.

      

    
    :type Filters: list
    :param Filters: 

      The filters to use for listing a specific set of users. Required. Supported filter keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.

      

    
      - *(dict) --* 

        A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of a filter.

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The values of a filter.

          

        
          - *(string) --* 

          
      
      
  
    :type SortCriteria: list
    :param SortCriteria: 

      The sort order to use in listing the filtered set of users. Required. Supported sort keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.

      

    
      - *(dict) --* 

        An object representing a sort criteria. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The sort key of a sort object.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The sort value of a sort object.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Users': [
                {
                    'UserArn': 'string',
                    'FirstName': 'string',
                    'LastName': 'string',
                    'Email': 'string',
                    'EnrollmentStatus': 'INITIALIZED'|'PENDING'|'REGISTERED'|'DEREGISTERING',
                    'EnrollmentId': 'string'
                },
            ],
            'NextToken': 'string',
            'TotalCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Users** *(list) --* 

          The users that meet the specified set of filter criteria, in sort order.

          
          

          - *(dict) --* 

            Information related to a user.

            
            

            - **UserArn** *(string) --* 

              The ARN of a user.

              
            

            - **FirstName** *(string) --* 

              The first name of a user.

              
            

            - **LastName** *(string) --* 

              The last name of a user.

              
            

            - **Email** *(string) --* 

              The email of a user.

              
            

            - **EnrollmentStatus** *(string) --* 

              The enrollment status of a user.

              
            

            - **EnrollmentId** *(string) --* 

              The enrollment ARN of a user.

              
        
      
        

        - **NextToken** *(string) --* 

          The token returned to indicate that there is more data available.

          
        

        - **TotalCount** *(integer) --* 

          The total number of users returned.

          
    

  .. py:method:: send_invitation(**kwargs)

    

    Sends an enrollment invitation email with a URL to a user. The URL is valid for 72 hours or until you call this operation again, whichever comes first. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SendInvitation>`_    


    **Request Syntax** 
    ::

      response = client.send_invitation(
          UserArn='string'
      )
    :type UserArn: string
    :param UserArn: 

      The ARN of the user to whom to send an invitation. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: start_device_sync(**kwargs)

    

    Resets a device and its account to the known default settings by clearing all information and settings set by previous users.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/StartDeviceSync>`_    


    **Request Syntax** 
    ::

      response = client.start_device_sync(
          RoomArn='string',
          DeviceArn='string',
          Features=[
              'BLUETOOTH'|'VOLUME'|'NOTIFICATIONS'|'LISTS'|'SKILLS'|'ALL',
          ]
      )
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room with which the device to sync is associated. Required.

      

    
    :type DeviceArn: string
    :param DeviceArn: 

      The ARN of the device to sync. Required.

      

    
    :type Features: list
    :param Features: **[REQUIRED]** 

      Request structure to start the device sync. Required.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: tag_resource(**kwargs)

    

    Adds metadata tags to a specified resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/TagResource>`_    


    **Request Syntax** 
    ::

      response = client.tag_resource(
          Arn='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type Arn: string
    :param Arn: **[REQUIRED]** 

      The ARN of the resource to which to add metadata tags. Required. 

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      The tags to be added to the specified resource. Do not provide system tags. Required. 

      

    
      - *(dict) --* 

        A key-value pair that can be associated with a resource. 

        

      
        - **Key** *(string) --* 

          The key of a tag. Tag keys are case-sensitive. 

          

        
        - **Value** *(string) --* 

          The value of a tag. Tag values are case-sensitive and can be null.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: untag_resource(**kwargs)

    

    Removes metadata tags from a specified resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UntagResource>`_    


    **Request Syntax** 
    ::

      response = client.untag_resource(
          Arn='string',
          TagKeys=[
              'string',
          ]
      )
    :type Arn: string
    :param Arn: **[REQUIRED]** 

      The ARN of the resource from which to remove metadata tags. Required. 

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      The tags to be removed from the specified resource. Do not provide system tags. Required. 

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_device(**kwargs)

    

    Updates the device name by device ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateDevice>`_    


    **Request Syntax** 
    ::

      response = client.update_device(
          DeviceArn='string',
          DeviceName='string'
      )
    :type DeviceArn: string
    :param DeviceArn: 

      The ARN of the device to update. Required.

      

    
    :type DeviceName: string
    :param DeviceName: 

      The updated device name. Required.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_profile(**kwargs)

    

    Updates an existing room profile by room profile ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateProfile>`_    


    **Request Syntax** 
    ::

      response = client.update_profile(
          ProfileArn='string',
          ProfileName='string',
          Timezone='string',
          Address='string',
          DistanceUnit='METRIC'|'IMPERIAL',
          TemperatureUnit='FAHRENHEIT'|'CELSIUS',
          WakeWord='ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
          SetupModeDisabled=True|False,
          MaxVolumeLimit=123,
          PSTNEnabled=True|False
      )
    :type ProfileArn: string
    :param ProfileArn: 

      The ARN of the room profile to update. Required.

      

    
    :type ProfileName: string
    :param ProfileName: 

      The updated name for the room profile.

      

    
    :type Timezone: string
    :param Timezone: 

      The updated timezone for the room profile.

      

    
    :type Address: string
    :param Address: 

      The updated address for the room profile.

      

    
    :type DistanceUnit: string
    :param DistanceUnit: 

      The updated distance unit for the room profile.

      

    
    :type TemperatureUnit: string
    :param TemperatureUnit: 

      The updated temperature unit for the room profile.

      

    
    :type WakeWord: string
    :param WakeWord: 

      The updated wake word for the room profile.

      

    
    :type SetupModeDisabled: boolean
    :param SetupModeDisabled: 

      Whether the setup mode of the profile is enabled.

      

    
    :type MaxVolumeLimit: integer
    :param MaxVolumeLimit: 

      The updated maximum volume limit for the room profile.

      

    
    :type PSTNEnabled: boolean
    :param PSTNEnabled: 

      Whether the PSTN setting of the room profile is enabled.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_room(**kwargs)

    

    Updates room details by room ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateRoom>`_    


    **Request Syntax** 
    ::

      response = client.update_room(
          RoomArn='string',
          RoomName='string',
          Description='string',
          ProviderCalendarId='string',
          ProfileArn='string'
      )
    :type RoomArn: string
    :param RoomArn: 

      The ARN of the room to update. 

      

    
    :type RoomName: string
    :param RoomName: 

      The updated name for the room.

      

    
    :type Description: string
    :param Description: 

      The updated description for the room.

      

    
    :type ProviderCalendarId: string
    :param ProviderCalendarId: 

      The updated provider calendar ARN for the room.

      

    
    :type ProfileArn: string
    :param ProfileArn: 

      The updated profile ARN for the room.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_skill_group(**kwargs)

    

    Updates skill group details by skill group ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateSkillGroup>`_    


    **Request Syntax** 
    ::

      response = client.update_skill_group(
          SkillGroupArn='string',
          SkillGroupName='string',
          Description='string'
      )
    :type SkillGroupArn: string
    :param SkillGroupArn: 

      The ARN of the skill group to update. 

      

    
    :type SkillGroupName: string
    :param SkillGroupName: 

      The updated name for the skill group.

      

    
    :type Description: string
    :param Description: 

      The updated description for the skill group.

      

    
    
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
