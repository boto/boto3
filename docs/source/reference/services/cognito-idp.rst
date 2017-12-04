

***********************
CognitoIdentityProvider
***********************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CognitoIdentityProvider.Client

  A low-level client representing Amazon Cognito Identity Provider::

    
    import boto3
    
    client = boto3.client('cognito-idp')

  
  These are the available methods:
  
  *   :py:meth:`~CognitoIdentityProvider.Client.add_custom_attributes`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_add_user_to_group`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_confirm_sign_up`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_create_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_delete_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_delete_user_attributes`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_disable_provider_for_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_disable_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_enable_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_forget_device`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_get_device`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_get_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_initiate_auth`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_link_provider_for_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_list_devices`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_list_groups_for_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_list_user_auth_events`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_remove_user_from_group`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_reset_user_password`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_respond_to_auth_challenge`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_set_user_mfa_preference`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_set_user_settings`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_update_auth_event_feedback`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_update_device_status`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_update_user_attributes`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.admin_user_global_sign_out`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.associate_software_token`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.can_paginate`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.change_password`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.confirm_device`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.confirm_forgot_password`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.confirm_sign_up`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.create_group`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.create_identity_provider`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.create_resource_server`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.create_user_import_job`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.create_user_pool`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.create_user_pool_client`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.create_user_pool_domain`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.delete_group`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.delete_identity_provider`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.delete_resource_server`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.delete_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.delete_user_attributes`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.delete_user_pool`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.delete_user_pool_client`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.delete_user_pool_domain`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.describe_identity_provider`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.describe_resource_server`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.describe_risk_configuration`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.describe_user_import_job`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.describe_user_pool`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.describe_user_pool_client`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.describe_user_pool_domain`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.forget_device`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.forgot_password`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.generate_presigned_url`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_csv_header`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_device`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_group`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_identity_provider_by_identifier`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_paginator`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_ui_customization`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_user`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_user_attribute_verification_code`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_user_pool_mfa_config`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.get_waiter`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.global_sign_out`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.initiate_auth`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_devices`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_groups`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_identity_providers`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_resource_servers`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_user_import_jobs`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_user_pool_clients`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_user_pools`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_users`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.list_users_in_group`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.resend_confirmation_code`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.respond_to_auth_challenge`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.set_risk_configuration`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.set_ui_customization`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.set_user_mfa_preference`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.set_user_pool_mfa_config`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.set_user_settings`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.sign_up`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.start_user_import_job`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.stop_user_import_job`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.update_auth_event_feedback`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.update_device_status`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.update_group`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.update_identity_provider`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.update_resource_server`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.update_user_attributes`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.update_user_pool`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.update_user_pool_client`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.verify_software_token`

  
  *   :py:meth:`~CognitoIdentityProvider.Client.verify_user_attribute`

  

  .. py:method:: add_custom_attributes(**kwargs)

    

    Adds additional user attributes to the user pool schema.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AddCustomAttributes>`_    


    **Request Syntax** 
    ::

      response = client.add_custom_attributes(
          UserPoolId='string',
          CustomAttributes=[
              {
                  'Name': 'string',
                  'AttributeDataType': 'String'|'Number'|'DateTime'|'Boolean',
                  'DeveloperOnlyAttribute': True|False,
                  'Mutable': True|False,
                  'Required': True|False,
                  'NumberAttributeConstraints': {
                      'MinValue': 'string',
                      'MaxValue': 'string'
                  },
                  'StringAttributeConstraints': {
                      'MinLength': 'string',
                      'MaxLength': 'string'
                  }
              },
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to add custom attributes.

      

    
    :type CustomAttributes: list
    :param CustomAttributes: **[REQUIRED]** 

      An array of custom attributes, such as Mutable and Name.

      

    
      - *(dict) --* 

        Contains information about the schema attribute.

        

      
        - **Name** *(string) --* 

          A schema attribute of the name type.

          

        
        - **AttributeDataType** *(string) --* 

          The attribute data type.

          

        
        - **DeveloperOnlyAttribute** *(boolean) --* 

          Specifies whether the attribute type is developer only.

          

        
        - **Mutable** *(boolean) --* 

          Specifies whether the attribute can be changed once it has been created.

          

        
        - **Required** *(boolean) --* 

          Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.

          

        
        - **NumberAttributeConstraints** *(dict) --* 

          Specifies the constraints for an attribute of the number type.

          

        
          - **MinValue** *(string) --* 

            The minimum value of an attribute that is of the number data type.

            

          
          - **MaxValue** *(string) --* 

            The maximum value of an attribute that is of the number data type.

            

          
        
        - **StringAttributeConstraints** *(dict) --* 

          Specifies the constraints for an attribute of the string type.

          

        
          - **MinLength** *(string) --* 

            The minimum length.

            

          
          - **MaxLength** *(string) --* 

            The maximum length.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server for the request to add custom attributes.

        
    

  .. py:method:: admin_add_user_to_group(**kwargs)

    

    Adds the specified user to the specified group.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminAddUserToGroup>`_    


    **Request Syntax** 
    ::

      response = client.admin_add_user_to_group(
          UserPoolId='string',
          Username='string',
          GroupName='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The username for the user.

      

    
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The group name.

      

    
    
    :returns: None

  .. py:method:: admin_confirm_sign_up(**kwargs)

    

    Confirms user registration as an admin without using a confirmation code. Works on any user.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminConfirmSignUp>`_    


    **Request Syntax** 
    ::

      response = client.admin_confirm_sign_up(
          UserPoolId='string',
          Username='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for which you want to confirm user registration.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name for which you want to confirm user registration.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server for the request to confirm registration.

        
    

  .. py:method:: admin_create_user(**kwargs)

    

    Creates a new user in the specified user pool.

     

    If ``MessageAction`` is not set, the default is to send a welcome message via email or phone (SMS).

     

    .. note::

       

      This message is based on a template that you configured in your call to or . This template includes your custom sign-up instructions and placeholders for user name and temporary password.

       

     

    Alternatively, you can call AdminCreateUser with “SUPPRESS” for the ``MessageAction`` parameter, and Amazon Cognito will not send any email. 

     

    In either case, the user will be in the ``FORCE_CHANGE_PASSWORD`` state until they sign in and change their password.

     

    AdminCreateUser requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminCreateUser>`_    


    **Request Syntax** 
    ::

      response = client.admin_create_user(
          UserPoolId='string',
          Username='string',
          UserAttributes=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          ValidationData=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          TemporaryPassword='string',
          ForceAliasCreation=True|False,
          MessageAction='RESEND'|'SUPPRESS',
          DesiredDeliveryMediums=[
              'SMS'|'EMAIL',
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where the user will be created.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The username for the user. Must be unique within the user pool. Must be a UTF-8 string between 1 and 128 characters. After the user is created, the username cannot be changed.

      

    
    :type UserAttributes: list
    :param UserAttributes: 

      An array of name-value pairs that contain user attributes and attribute values to be set for the user to be created. You can create a user without specifying any attributes other than ``Username`` . However, any attributes that you specify as required (in or in the **Attributes** tab of the console) must be supplied either by you (in your call to ``AdminCreateUser`` ) or by the user (when he or she signs up in response to your welcome message).

       

      For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

       

      To send a message inviting the user to sign up, you must specify the user's email address or phone number. This can be done in your call to AdminCreateUser or in the **Users** tab of the Amazon Cognito console for managing your user pools.

       

      In your call to ``AdminCreateUser`` , you can set the ``email_verified`` attribute to ``True`` , and you can set the ``phone_number_verified`` attribute to ``True`` . (You can also do this by calling .)

       

       
      * **email** : The email address of the user to whom the message that contains the code and username will be sent. Required if the ``email_verified`` attribute is set to ``True`` , or if ``"EMAIL"`` is specified in the ``DesiredDeliveryMediums`` parameter. 
       
      * **phone_number** : The phone number of the user to whom the message that contains the code and username will be sent. Required if the ``phone_number_verified`` attribute is set to ``True`` , or if ``"SMS"`` is specified in the ``DesiredDeliveryMediums`` parameter. 
       

      

    
      - *(dict) --* 

        Specifies whether the attribute is standard or custom.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the attribute.

          

        
        - **Value** *(string) --* 

          The value of the attribute.

          

        
      
  
    :type ValidationData: list
    :param ValidationData: 

      The user's validation data. This is an array of name-value pairs that contain user attributes and attribute values that you can use for custom validation, such as restricting the types of user accounts that can be registered. For example, you might choose to allow or disallow user sign-up based on the user's domain.

       

      To configure custom validation, you must create a Pre Sign-up Lambda trigger for the user pool as described in the Amazon Cognito Developer Guide. The Lambda trigger receives the validation data and uses it in the validation process.

       

      The user's validation data is not persisted.

      

    
      - *(dict) --* 

        Specifies whether the attribute is standard or custom.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the attribute.

          

        
        - **Value** *(string) --* 

          The value of the attribute.

          

        
      
  
    :type TemporaryPassword: string
    :param TemporaryPassword: 

      The user's temporary password. This password must conform to the password policy that you specified when you created the user pool.

       

      The temporary password is valid only once. To complete the Admin Create User flow, the user must enter the temporary password in the sign-in page along with a new password to be used in all future sign-ins.

       

      This parameter is not required. If you do not specify a value, Amazon Cognito generates one for you.

       

      The temporary password can only be used until the user account expiration limit that you specified when you created the user pool. To reset the account after that time limit, you must call ``AdminCreateUser`` again, specifying ``"RESEND"`` for the ``MessageAction`` parameter.

      

    
    :type ForceAliasCreation: boolean
    :param ForceAliasCreation: 

      This parameter is only used if the ``phone_number_verified`` or ``email_verified`` attribute is set to ``True`` . Otherwise, it is ignored.

       

      If this parameter is set to ``True`` and the phone number or email address specified in the UserAttributes parameter already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user. The previous user will no longer be able to log in using that alias.

       

      If this parameter is set to ``False`` , the API throws an ``AliasExistsException`` error if the alias already exists. The default value is ``False`` .

      

    
    :type MessageAction: string
    :param MessageAction: 

      Set to ``"RESEND"`` to resend the invitation message to a user that already exists and reset the expiration limit on the user's account. Set to ``"SUPPRESS"`` to suppress sending the message. Only one value can be specified.

      

    
    :type DesiredDeliveryMediums: list
    :param DesiredDeliveryMediums: 

      Specify ``"EMAIL"`` if email will be used to send the welcome message. Specify ``"SMS"`` if the phone number will be used. The default value is ``"SMS"`` . More than one value can be specified.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'User': {
                'Username': 'string',
                'Attributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'UserCreateDate': datetime(2015, 1, 1),
                'UserLastModifiedDate': datetime(2015, 1, 1),
                'Enabled': True|False,
                'UserStatus': 'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'|'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
                'MFAOptions': [
                    {
                        'DeliveryMedium': 'SMS'|'EMAIL',
                        'AttributeName': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to the request to create the user.

        
        

        - **User** *(dict) --* 

          The newly created user.

          
          

          - **Username** *(string) --* 

            The user name of the user you wish to describe.

            
          

          - **Attributes** *(list) --* 

            A container with information about the user type attributes.

            
            

            - *(dict) --* 

              Specifies whether the attribute is standard or custom.

              
              

              - **Name** *(string) --* 

                The name of the attribute.

                
              

              - **Value** *(string) --* 

                The value of the attribute.

                
          
        
          

          - **UserCreateDate** *(datetime) --* 

            The creation date of the user.

            
          

          - **UserLastModifiedDate** *(datetime) --* 

            The last modified date of the user.

            
          

          - **Enabled** *(boolean) --* 

            Specifies whether the user is enabled.

            
          

          - **UserStatus** *(string) --* 

            The user status. Can be one of the following:

             

             
            * UNCONFIRMED - User has been created but not confirmed. 
             
            * CONFIRMED - User has been confirmed. 
             
            * ARCHIVED - User is no longer active. 
             
            * COMPROMISED - User is disabled due to a potential security threat. 
             
            * UNKNOWN - User status is not known. 
             

            
          

          - **MFAOptions** *(list) --* 

            The MFA options for the user.

            
            

            - *(dict) --* 

              Specifies the different settings for multi-factor authentication (MFA).

              
              

              - **DeliveryMedium** *(string) --* 

                The delivery medium (email message or SMS message) to send the MFA code.

                
              

              - **AttributeName** *(string) --* 

                The attribute name of the MFA option type.

                
          
        
      
    

  .. py:method:: admin_delete_user(**kwargs)

    

    Deletes a user as an administrator. Works on any user.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminDeleteUser>`_    


    **Request Syntax** 
    ::

      response = client.admin_delete_user(
          UserPoolId='string',
          Username='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to delete the user.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user you wish to delete.

      

    
    
    :returns: None

  .. py:method:: admin_delete_user_attributes(**kwargs)

    

    Deletes the user attributes in a user pool as an administrator. Works on any user.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminDeleteUserAttributes>`_    


    **Request Syntax** 
    ::

      response = client.admin_delete_user_attributes(
          UserPoolId='string',
          Username='string',
          UserAttributeNames=[
              'string',
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to delete user attributes.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user from which you would like to delete attributes.

      

    
    :type UserAttributeNames: list
    :param UserAttributeNames: **[REQUIRED]** 

      An array of strings representing the user attribute names you wish to delete.

       

      For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response received from the server for a request to delete user attributes.

        
    

  .. py:method:: admin_disable_provider_for_user(**kwargs)

    

    Disables the user from signing in with the specified external (SAML or social) identity provider. If the user to disable is a Cognito User Pools native username + password user, they are not permitted to use their password to sign-in. If the user to disable is a linked external IdP user, any link between that user and an existing user is removed. The next time the external user (no longer attached to the previously linked ``DestinationUser`` ) signs in, they must create a new user account. See .

     

    This action is enabled only for admin access and requires developer credentials.

     

    The ``ProviderName`` must match the value specified when creating an IdP for the pool. 

     

    To disable a native username + password user, the ``ProviderName`` value must be ``Cognito`` and the ``ProviderAttributeName`` must be ``Cognito_Subject`` , with the ``ProviderAttributeValue`` being the name that is used in the user pool for the user.

     

    The ``ProviderAttributeName`` must always be ``Cognito_Subject`` for social identity providers. The ``ProviderAttributeValue`` must always be the exact subject that was used when the user was originally linked as a source user.

     

    For de-linking a SAML identity, there are two scenarios. If the linked identity has not yet been used to sign-in, the ``ProviderAttributeName`` and ``ProviderAttributeValue`` must be the same values that were used for the ``SourceUser`` when the identities were originally linked in the call. (If the linking was done with ``ProviderAttributeName`` set to ``Cognito_Subject`` , the same applies here). However, if the user has already signed in, the ``ProviderAttributeName`` must be ``Cognito_Subject`` and ``ProviderAttributeValue`` must be the subject of the SAML assertion.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminDisableProviderForUser>`_    


    **Request Syntax** 
    ::

      response = client.admin_disable_provider_for_user(
          UserPoolId='string',
          User={
              'ProviderName': 'string',
              'ProviderAttributeName': 'string',
              'ProviderAttributeValue': 'string'
          }
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type User: dict
    :param User: **[REQUIRED]** 

      The user to be disabled.

      

    
      - **ProviderName** *(string) --* 

        The name of the provider, for example, Facebook, Google, or Login with Amazon.

        

      
      - **ProviderAttributeName** *(string) --* 

        The name of the provider attribute to link to, for example, ``NameID`` .

        

      
      - **ProviderAttributeValue** *(string) --* 

        The value of the provider attribute to link to, for example, ``xxxxx_account`` .

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: admin_disable_user(**kwargs)

    

    Disables the specified user as an administrator. Works on any user.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminDisableUser>`_    


    **Request Syntax** 
    ::

      response = client.admin_disable_user(
          UserPoolId='string',
          Username='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to disable the user.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user you wish to disable.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response received from the server to disable the user as an administrator.

        
    

  .. py:method:: admin_enable_user(**kwargs)

    

    Enables the specified user as an administrator. Works on any user.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminEnableUser>`_    


    **Request Syntax** 
    ::

      response = client.admin_enable_user(
          UserPoolId='string',
          Username='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to enable the user.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user you wish to enable.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server for the request to enable a user as an administrator.

        
    

  .. py:method:: admin_forget_device(**kwargs)

    

    Forgets the device, as an administrator.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminForgetDevice>`_    


    **Request Syntax** 
    ::

      response = client.admin_forget_device(
          UserPoolId='string',
          Username='string',
          DeviceKey='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name.

      

    
    :type DeviceKey: string
    :param DeviceKey: **[REQUIRED]** 

      The device key.

      

    
    
    :returns: None

  .. py:method:: admin_get_device(**kwargs)

    

    Gets the device, as an administrator.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminGetDevice>`_    


    **Request Syntax** 
    ::

      response = client.admin_get_device(
          DeviceKey='string',
          UserPoolId='string',
          Username='string'
      )
    :type DeviceKey: string
    :param DeviceKey: **[REQUIRED]** 

      The device key.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Device': {
                'DeviceKey': 'string',
                'DeviceAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'DeviceCreateDate': datetime(2015, 1, 1),
                'DeviceLastModifiedDate': datetime(2015, 1, 1),
                'DeviceLastAuthenticatedDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Gets the device response, as an administrator.

        
        

        - **Device** *(dict) --* 

          The device.

          
          

          - **DeviceKey** *(string) --* 

            The device key.

            
          

          - **DeviceAttributes** *(list) --* 

            The device attributes.

            
            

            - *(dict) --* 

              Specifies whether the attribute is standard or custom.

              
              

              - **Name** *(string) --* 

                The name of the attribute.

                
              

              - **Value** *(string) --* 

                The value of the attribute.

                
          
        
          

          - **DeviceCreateDate** *(datetime) --* 

            The creation date of the device.

            
          

          - **DeviceLastModifiedDate** *(datetime) --* 

            The last modified date of the device.

            
          

          - **DeviceLastAuthenticatedDate** *(datetime) --* 

            The date in which the device was last authenticated.

            
      
    

  .. py:method:: admin_get_user(**kwargs)

    

    Gets the specified user by user name in a user pool as an administrator. Works on any user.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminGetUser>`_    


    **Request Syntax** 
    ::

      response = client.admin_get_user(
          UserPoolId='string',
          Username='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to get information about the user.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user you wish to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Username': 'string',
            'UserAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'UserCreateDate': datetime(2015, 1, 1),
            'UserLastModifiedDate': datetime(2015, 1, 1),
            'Enabled': True|False,
            'UserStatus': 'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'|'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
            'MFAOptions': [
                {
                    'DeliveryMedium': 'SMS'|'EMAIL',
                    'AttributeName': 'string'
                },
            ],
            'PreferredMfaSetting': 'string',
            'UserMFASettingList': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server from the request to get the specified user as an administrator.

        
        

        - **Username** *(string) --* 

          The user name of the user about whom you are receiving information.

          
        

        - **UserAttributes** *(list) --* 

          An array of name-value pairs representing user attributes.

          
          

          - *(dict) --* 

            Specifies whether the attribute is standard or custom.

            
            

            - **Name** *(string) --* 

              The name of the attribute.

              
            

            - **Value** *(string) --* 

              The value of the attribute.

              
        
      
        

        - **UserCreateDate** *(datetime) --* 

          The date the user was created.

          
        

        - **UserLastModifiedDate** *(datetime) --* 

          The date the user was last modified.

          
        

        - **Enabled** *(boolean) --* 

          Indicates that the status is enabled.

          
        

        - **UserStatus** *(string) --* 

          The user status. Can be one of the following:

           

           
          * UNCONFIRMED - User has been created but not confirmed. 
           
          * CONFIRMED - User has been confirmed. 
           
          * ARCHIVED - User is no longer active. 
           
          * COMPROMISED - User is disabled due to a potential security threat. 
           
          * UNKNOWN - User status is not known. 
           

          
        

        - **MFAOptions** *(list) --* 

          Specifies the options for MFA (e.g., email or phone number).

          
          

          - *(dict) --* 

            Specifies the different settings for multi-factor authentication (MFA).

            
            

            - **DeliveryMedium** *(string) --* 

              The delivery medium (email message or SMS message) to send the MFA code.

              
            

            - **AttributeName** *(string) --* 

              The attribute name of the MFA option type.

              
        
      
        

        - **PreferredMfaSetting** *(string) --* 

          The user's preferred MFA setting.

          
        

        - **UserMFASettingList** *(list) --* 

          The list of the user's MFA settings.

          
          

          - *(string) --* 
      
    

  .. py:method:: admin_initiate_auth(**kwargs)

    

    Initiates the authentication flow, as an administrator.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminInitiateAuth>`_    


    **Request Syntax** 
    ::

      response = client.admin_initiate_auth(
          UserPoolId='string',
          ClientId='string',
          AuthFlow='USER_SRP_AUTH'|'REFRESH_TOKEN_AUTH'|'REFRESH_TOKEN'|'CUSTOM_AUTH'|'ADMIN_NO_SRP_AUTH',
          AuthParameters={
              'string': 'string'
          },
          ClientMetadata={
              'string': 'string'
          },
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          },
          ContextData={
              'IpAddress': 'string',
              'ServerName': 'string',
              'ServerPath': 'string',
              'HttpHeaders': [
                  {
                      'headerName': 'string',
                      'headerValue': 'string'
                  },
              ],
              'EncodedData': 'string'
          }
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The ID of the Amazon Cognito user pool.

      

    
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The app client ID.

      

    
    :type AuthFlow: string
    :param AuthFlow: **[REQUIRED]** 

      The authentication flow for this call to execute. The API action will depend on this value. For example:

       

       
      * ``REFRESH_TOKEN_AUTH`` will take in a valid refresh token and return new tokens. 
       
      * ``USER_SRP_AUTH`` will take in ``USERNAME`` and ``SRP_A`` and return the SRP variables to be used for next challenge execution. 
       

       

      Valid values include:

       

       
      * ``USER_SRP_AUTH`` : Authentication flow for the Secure Remote Password (SRP) protocol. 
       
      * ``REFRESH_TOKEN_AUTH`` /``REFRESH_TOKEN`` : Authentication flow for refreshing the access token and ID token by supplying a valid refresh token. 
       
      * ``CUSTOM_AUTH`` : Custom authentication flow. 
       
      * ``ADMIN_NO_SRP_AUTH`` : Non-SRP authentication flow; you can pass in the USERNAME and PASSWORD directly if the flow is enabled for calling the app client. 
       

      

    
    :type AuthParameters: dict
    :param AuthParameters: 

      The authentication parameters. These are inputs corresponding to the ``AuthFlow`` that you are invoking. The required values depend on the value of ``AuthFlow`` :

       

       
      * For ``USER_SRP_AUTH`` : ``USERNAME`` (required), ``SRP_A`` (required), ``SECRET_HASH`` (required if the app client is configured with a client secret), ``DEVICE_KEY``   
       
      * For ``REFRESH_TOKEN_AUTH/REFRESH_TOKEN`` : ``USERNAME`` (required), ``SECRET_HASH`` (required if the app client is configured with a client secret), ``REFRESH_TOKEN`` (required), ``DEVICE_KEY``   
       
      * For ``ADMIN_NO_SRP_AUTH`` : ``USERNAME`` (required), ``SECRET_HASH`` (if app client is configured with client secret), ``PASSWORD`` (required), ``DEVICE_KEY``   
       
      * For ``CUSTOM_AUTH`` : ``USERNAME`` (required), ``SECRET_HASH`` (if app client is configured with client secret), ``DEVICE_KEY``   
       

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type ClientMetadata: dict
    :param ClientMetadata: 

      This is a random key-value pair map which can contain any key and will be passed to your PreAuthentication Lambda trigger as-is. It can be used to implement additional validations around authentication.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The analytics metadata for collecting Amazon Pinpoint metrics for ``AdminInitiateAuth`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    :type ContextData: dict
    :param ContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **IpAddress** *(string) --* **[REQUIRED]** 

        Source IP address of your user.

        

      
      - **ServerName** *(string) --* **[REQUIRED]** 

        Your server endpoint where this API is invoked.

        

      
      - **ServerPath** *(string) --* **[REQUIRED]** 

        Your server path where this API is invoked. 

        

      
      - **HttpHeaders** *(list) --* **[REQUIRED]** 

        HttpHeaders received on your server in same order.

        

      
        - *(dict) --* 

          The HTTP header.

          

        
          - **headerName** *(string) --* 

            The header name

            

          
          - **headerValue** *(string) --* 

            The header value.

            

          
        
    
      - **EncodedData** *(string) --* 

        Encoded data containing device fingerprinting details, collected using the Amazon Cognito context data collection library.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
            'Session': 'string',
            'ChallengeParameters': {
                'string': 'string'
            },
            'AuthenticationResult': {
                'AccessToken': 'string',
                'ExpiresIn': 123,
                'TokenType': 'string',
                'RefreshToken': 'string',
                'IdToken': 'string',
                'NewDeviceMetadata': {
                    'DeviceKey': 'string',
                    'DeviceGroupKey': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Initiates the authentication response, as an administrator.

        
        

        - **ChallengeName** *(string) --* 

          The name of the challenge which you are responding to with this call. This is returned to you in the ``AdminInitiateAuth`` response if you need to pass another challenge.

           

           
          * ``SMS_MFA`` : Next challenge is to supply an ``SMS_MFA_CODE`` , delivered via SMS. 
           
          * ``PASSWORD_VERIFIER`` : Next challenge is to supply ``PASSWORD_CLAIM_SIGNATURE`` , ``PASSWORD_CLAIM_SECRET_BLOCK`` , and ``TIMESTAMP`` after the client-side SRP calculations. 
           
          * ``CUSTOM_CHALLENGE`` : This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued. 
           
          * ``DEVICE_SRP_AUTH`` : If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device. 
           
          * ``DEVICE_PASSWORD_VERIFIER`` : Similar to ``PASSWORD_VERIFIER`` , but for devices only. 
           
          * ``ADMIN_NO_SRP_AUTH`` : This is returned if you need to authenticate with ``USERNAME`` and ``PASSWORD`` directly. An app client must be enabled to use this flow. 
           
          * ``NEW_PASSWORD_REQUIRED`` : For users which are required to change their passwords after successful first login. This challenge should be passed with ``NEW_PASSWORD`` and any other required attributes. 
           

          
        

        - **Session** *(string) --* 

          The session which should be passed both ways in challenge-response calls to the service. If ``AdminInitiateAuth`` or ``AdminRespondToAuthChallenge`` API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next ``AdminRespondToAuthChallenge`` API call.

          
        

        - **ChallengeParameters** *(dict) --* 

          The challenge parameters. These are returned to you in the ``AdminInitiateAuth`` response if you need to pass another challenge. The responses in this parameter should be used to compute inputs to the next call (``AdminRespondToAuthChallenge`` ).

           

          All challenges require ``USERNAME`` and ``SECRET_HASH`` (if applicable).

           

          The value of the ``USER_IF_FOR_SRP`` attribute will be the user's actual username, not an alias (such as email address or phone number), even if you specified an alias in your call to ``AdminInitiateAuth`` . This is because, in the ``AdminRespondToAuthChallenge`` API ``ChallengeResponses`` , the ``USERNAME`` attribute cannot be an alias.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **AuthenticationResult** *(dict) --* 

          The result of the authentication response. This is only returned if the caller does not need to pass another challenge. If the caller does need to pass another challenge before it gets tokens, ``ChallengeName`` , ``ChallengeParameters`` , and ``Session`` are returned.

          
          

          - **AccessToken** *(string) --* 

            The access token.

            
          

          - **ExpiresIn** *(integer) --* 

            The expiration period of the authentication result.

            
          

          - **TokenType** *(string) --* 

            The token type.

            
          

          - **RefreshToken** *(string) --* 

            The refresh token.

            
          

          - **IdToken** *(string) --* 

            The ID token.

            
          

          - **NewDeviceMetadata** *(dict) --* 

            The new device metadata from an authentication result.

            
            

            - **DeviceKey** *(string) --* 

              The device key.

              
            

            - **DeviceGroupKey** *(string) --* 

              The device group key.

              
        
      
    

  .. py:method:: admin_link_provider_for_user(**kwargs)

    

    Links an existing user account in a user pool (``DestinationUser`` ) to an identity from an external identity provider (``SourceUser`` ) based on a specified attribute name and value from the external identity provider. This allows you to create a link from the existing user account to an external federated user identity that has not yet been used to sign in, so that the federated user identity can be used to sign in as the existing user account. 

     

    For example, if there is an existing user with a username and password, this API links that user to a federated user identity, so that when the federated user identity is used, the user signs in as the existing user account. 

     

    .. warning::

       

      Because this API allows a user with an external federated identity to sign in as an existing user in the user pool, it is critical that it only be used with external identity providers and provider attributes that have been trusted by the application owner.

       

     

    See also .

     

    This action is enabled only for admin access and requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminLinkProviderForUser>`_    


    **Request Syntax** 
    ::

      response = client.admin_link_provider_for_user(
          UserPoolId='string',
          DestinationUser={
              'ProviderName': 'string',
              'ProviderAttributeName': 'string',
              'ProviderAttributeValue': 'string'
          },
          SourceUser={
              'ProviderName': 'string',
              'ProviderAttributeName': 'string',
              'ProviderAttributeValue': 'string'
          }
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type DestinationUser: dict
    :param DestinationUser: **[REQUIRED]** 

      The existing user in the user pool to be linked to the external identity provider user account. Can be a native (Username + Password) Cognito User Pools user or a federated user (for example, a SAML or Facebook user). If the user doesn't exist, an exception is thrown. This is the user that is returned when the new user (with the linked identity provider attribute) signs in.

       

      For a native username + password user, the ``ProviderAttributeValue`` for the ``DestinationUser`` should be the username in the user pool. For a federated user, it should be the provider-specific ``user_id`` .

       

      The ``ProviderAttributeName`` of the ``DestinationUser`` is ignored.

       

      The ``ProviderName`` should be set to ``Cognito`` for users in Cognito user pools.

      

    
      - **ProviderName** *(string) --* 

        The name of the provider, for example, Facebook, Google, or Login with Amazon.

        

      
      - **ProviderAttributeName** *(string) --* 

        The name of the provider attribute to link to, for example, ``NameID`` .

        

      
      - **ProviderAttributeValue** *(string) --* 

        The value of the provider attribute to link to, for example, ``xxxxx_account`` .

        

      
    
    :type SourceUser: dict
    :param SourceUser: **[REQUIRED]** 

      An external identity provider account for a user who does not currently exist yet in the user pool. This user must be a federated user (for example, a SAML or Facebook user), not another native user.

       

      If the ``SourceUser`` is a federated social identity provider user (Facebook, Google, or Login with Amazon), you must set the ``ProviderAttributeName`` to ``Cognito_Subject`` . For social identity providers, the ``ProviderName`` will be ``Facebook`` , ``Google`` , or ``LoginWithAmazon`` , and Cognito will automatically parse the Facebook, Google, and Login with Amazon tokens for ``id`` , ``sub`` , and ``user_id`` , respectively. The ``ProviderAttributeValue`` for the user must be the same value as the ``id`` , ``sub`` , or ``user_id`` value found in the social identity provider token.

       

      

       

      For SAML, the ``ProviderAttributeName`` can be any value that matches a claim in the SAML assertion. If you wish to link SAML users based on the subject of the SAML assertion, you should map the subject to a claim through the SAML identity provider and submit that claim name as the ``ProviderAttributeName`` . If you set ``ProviderAttributeName`` to ``Cognito_Subject`` , Cognito will automatically parse the default unique identifier found in the subject from the SAML token.

      

    
      - **ProviderName** *(string) --* 

        The name of the provider, for example, Facebook, Google, or Login with Amazon.

        

      
      - **ProviderAttributeName** *(string) --* 

        The name of the provider attribute to link to, for example, ``NameID`` .

        

      
      - **ProviderAttributeValue** *(string) --* 

        The value of the provider attribute to link to, for example, ``xxxxx_account`` .

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: admin_list_devices(**kwargs)

    

    Lists devices, as an administrator.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminListDevices>`_    


    **Request Syntax** 
    ::

      response = client.admin_list_devices(
          UserPoolId='string',
          Username='string',
          Limit=123,
          PaginationToken='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name.

      

    
    :type Limit: integer
    :param Limit: 

      The limit of the devices request.

      

    
    :type PaginationToken: string
    :param PaginationToken: 

      The pagination token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Devices': [
                {
                    'DeviceKey': 'string',
                    'DeviceAttributes': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'DeviceCreateDate': datetime(2015, 1, 1),
                    'DeviceLastModifiedDate': datetime(2015, 1, 1),
                    'DeviceLastAuthenticatedDate': datetime(2015, 1, 1)
                },
            ],
            'PaginationToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Lists the device's response, as an administrator.

        
        

        - **Devices** *(list) --* 

          The devices in the list of devices response.

          
          

          - *(dict) --* 

            The device type.

            
            

            - **DeviceKey** *(string) --* 

              The device key.

              
            

            - **DeviceAttributes** *(list) --* 

              The device attributes.

              
              

              - *(dict) --* 

                Specifies whether the attribute is standard or custom.

                
                

                - **Name** *(string) --* 

                  The name of the attribute.

                  
                

                - **Value** *(string) --* 

                  The value of the attribute.

                  
            
          
            

            - **DeviceCreateDate** *(datetime) --* 

              The creation date of the device.

              
            

            - **DeviceLastModifiedDate** *(datetime) --* 

              The last modified date of the device.

              
            

            - **DeviceLastAuthenticatedDate** *(datetime) --* 

              The date in which the device was last authenticated.

              
        
      
        

        - **PaginationToken** *(string) --* 

          The pagination token.

          
    

  .. py:method:: admin_list_groups_for_user(**kwargs)

    

    Lists the groups that the user belongs to.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminListGroupsForUser>`_    


    **Request Syntax** 
    ::

      response = client.admin_list_groups_for_user(
          Username='string',
          UserPoolId='string',
          Limit=123,
          NextToken='string'
      )
    :type Username: string
    :param Username: **[REQUIRED]** 

      The username for the user.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type Limit: integer
    :param Limit: 

      The limit of the request to list groups.

      

    
    :type NextToken: string
    :param NextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Groups': [
                {
                    'GroupName': 'string',
                    'UserPoolId': 'string',
                    'Description': 'string',
                    'RoleArn': 'string',
                    'Precedence': 123,
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'CreationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Groups** *(list) --* 

          The groups that the user belongs to.

          
          

          - *(dict) --* 

            The group type.

            
            

            - **GroupName** *(string) --* 

              The name of the group.

              
            

            - **UserPoolId** *(string) --* 

              The user pool ID for the user pool.

              
            

            - **Description** *(string) --* 

              A string containing the description of the group.

              
            

            - **RoleArn** *(string) --* 

              The role ARN for the group.

              
            

            - **Precedence** *(integer) --* 

              A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values or with null ``Precedence`` values.

               

              Two groups can have the same ``Precedence`` value. If this happens, neither group takes precedence over the other. If two groups with the same ``Precedence`` have the same role ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is not set in users' tokens.

               

              The default ``Precedence`` value is null.

              
            

            - **LastModifiedDate** *(datetime) --* 

              The date the group was last modified.

              
            

            - **CreationDate** *(datetime) --* 

              The date the group was created.

              
        
      
        

        - **NextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

  .. py:method:: admin_list_user_auth_events(**kwargs)

    

    Lists a history of user activity and any risks detected as part of Amazon Cognito advanced security.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminListUserAuthEvents>`_    


    **Request Syntax** 
    ::

      response = client.admin_list_user_auth_events(
          UserPoolId='string',
          Username='string',
          MaxResults=123,
          NextToken='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user pool username.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of authentication events to return.

      

    
    :type NextToken: string
    :param NextToken: 

      A pagination token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AuthEvents': [
                {
                    'EventId': 'string',
                    'EventType': 'SignIn'|'SignUp'|'ForgotPassword',
                    'CreationDate': datetime(2015, 1, 1),
                    'EventResponse': 'Success'|'Failure',
                    'EventRisk': {
                        'RiskDecision': 'NoRisk'|'AccountTakeover'|'Block',
                        'RiskLevel': 'Low'|'Medium'|'High'
                    },
                    'ChallengeResponses': [
                        {
                            'ChallengeName': 'Password'|'Mfa',
                            'ChallengeResponse': 'Success'|'Failure'
                        },
                    ],
                    'EventContextData': {
                        'IpAddress': 'string',
                        'DeviceName': 'string',
                        'Timezone': 'string',
                        'City': 'string',
                        'Country': 'string'
                    },
                    'EventFeedback': {
                        'FeedbackValue': 'Valid'|'Invalid',
                        'Provider': 'string',
                        'FeedbackDate': datetime(2015, 1, 1)
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AuthEvents** *(list) --* 

          The response object. It includes the ``EventID`` , ``EventType`` , ``CreationDate`` , ``EventRisk`` , and ``EventResponse`` .

          
          

          - *(dict) --* 

            The authentication event type.

            
            

            - **EventId** *(string) --* 

              The event ID.

              
            

            - **EventType** *(string) --* 

              The event type.

              
            

            - **CreationDate** *(datetime) --* 

              The creation date

              
            

            - **EventResponse** *(string) --* 

              The event response.

              
            

            - **EventRisk** *(dict) --* 

              The event risk.

              
              

              - **RiskDecision** *(string) --* 

                The risk decision.

                
              

              - **RiskLevel** *(string) --* 

                The risk level.

                
          
            

            - **ChallengeResponses** *(list) --* 

              The challenge responses.

              
              

              - *(dict) --* 

                The challenge response type.

                
                

                - **ChallengeName** *(string) --* 

                  The challenge name

                  
                

                - **ChallengeResponse** *(string) --* 

                  The challenge response.

                  
            
          
            

            - **EventContextData** *(dict) --* 

              The user context data captured at the time of an event request. It provides additional information about the client from which event the request is received.

              
              

              - **IpAddress** *(string) --* 

                The user's IP address.

                
              

              - **DeviceName** *(string) --* 

                The user's device name.

                
              

              - **Timezone** *(string) --* 

                The user's time zone.

                
              

              - **City** *(string) --* 

                The user's city.

                
              

              - **Country** *(string) --* 

                The user's country.

                
          
            

            - **EventFeedback** *(dict) --* 

              A flag specifying the user feedback captured at the time of an event request is good or bad. 

              
              

              - **FeedbackValue** *(string) --* 

                The event feedback value.

                
              

              - **Provider** *(string) --* 

                The provider.

                
              

              - **FeedbackDate** *(datetime) --* 

                The event feedback date.

                
          
        
      
        

        - **NextToken** *(string) --* 

          A pagination token.

          
    

  .. py:method:: admin_remove_user_from_group(**kwargs)

    

    Removes the specified user from the specified group.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminRemoveUserFromGroup>`_    


    **Request Syntax** 
    ::

      response = client.admin_remove_user_from_group(
          UserPoolId='string',
          Username='string',
          GroupName='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The username for the user.

      

    
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The group name.

      

    
    
    :returns: None

  .. py:method:: admin_reset_user_password(**kwargs)

    

    Resets the specified user's password in a user pool as an administrator. Works on any user.

     

    When a developer calls this API, the current password is invalidated, so it must be changed. If a user tries to sign in after the API is called, the app will get a PasswordResetRequiredException exception back and should direct the user down the flow to reset the password, which is the same as the forgot password flow. In addition, if the user pool has phone verification selected and a verified phone number exists for the user, or if email verification is selected and a verified email exists for the user, calling this API will also result in sending a message to the end user with the code to change their password.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminResetUserPassword>`_    


    **Request Syntax** 
    ::

      response = client.admin_reset_user_password(
          UserPoolId='string',
          Username='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to reset the user's password.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user whose password you wish to reset.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to reset a user password as an administrator.

        
    

  .. py:method:: admin_respond_to_auth_challenge(**kwargs)

    

    Responds to an authentication challenge, as an administrator.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminRespondToAuthChallenge>`_    


    **Request Syntax** 
    ::

      response = client.admin_respond_to_auth_challenge(
          UserPoolId='string',
          ClientId='string',
          ChallengeName='SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
          ChallengeResponses={
              'string': 'string'
          },
          Session='string',
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          },
          ContextData={
              'IpAddress': 'string',
              'ServerName': 'string',
              'ServerPath': 'string',
              'HttpHeaders': [
                  {
                      'headerName': 'string',
                      'headerValue': 'string'
                  },
              ],
              'EncodedData': 'string'
          }
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The ID of the Amazon Cognito user pool.

      

    
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The app client ID.

      

    
    :type ChallengeName: string
    :param ChallengeName: **[REQUIRED]** 

      The challenge name. For more information, see .

      

    
    :type ChallengeResponses: dict
    :param ChallengeResponses: 

      The challenge responses. These are inputs corresponding to the value of ``ChallengeName`` , for example:

       

       
      * ``SMS_MFA`` : ``SMS_MFA_CODE`` , ``USERNAME`` , ``SECRET_HASH`` (if app client is configured with client secret). 
       
      * ``PASSWORD_VERIFIER`` : ``PASSWORD_CLAIM_SIGNATURE`` , ``PASSWORD_CLAIM_SECRET_BLOCK`` , ``TIMESTAMP`` , ``USERNAME`` , ``SECRET_HASH`` (if app client is configured with client secret). 
       
      * ``ADMIN_NO_SRP_AUTH`` : ``PASSWORD`` , ``USERNAME`` , ``SECRET_HASH`` (if app client is configured with client secret).  
       
      * ``NEW_PASSWORD_REQUIRED`` : ``NEW_PASSWORD`` , any other required attributes, ``USERNAME`` , ``SECRET_HASH`` (if app client is configured with client secret).  
       

       

      The value of the ``USERNAME`` attribute must be the user's actual username, not an alias (such as email address or phone number). To make this easier, the ``AdminInitiateAuth`` response includes the actual username value in the ``USERNAMEUSER_ID_FOR_SRP`` attribute, even if you specified an alias in your call to ``AdminInitiateAuth`` .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type Session: string
    :param Session: 

      The session which should be passed both ways in challenge-response calls to the service. If ``InitiateAuth`` or ``RespondToAuthChallenge`` API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next ``RespondToAuthChallenge`` API call.

      

    
    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The analytics metadata for collecting Amazon Pinpoint metrics for ``AdminRespondToAuthChallenge`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    :type ContextData: dict
    :param ContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **IpAddress** *(string) --* **[REQUIRED]** 

        Source IP address of your user.

        

      
      - **ServerName** *(string) --* **[REQUIRED]** 

        Your server endpoint where this API is invoked.

        

      
      - **ServerPath** *(string) --* **[REQUIRED]** 

        Your server path where this API is invoked. 

        

      
      - **HttpHeaders** *(list) --* **[REQUIRED]** 

        HttpHeaders received on your server in same order.

        

      
        - *(dict) --* 

          The HTTP header.

          

        
          - **headerName** *(string) --* 

            The header name

            

          
          - **headerValue** *(string) --* 

            The header value.

            

          
        
    
      - **EncodedData** *(string) --* 

        Encoded data containing device fingerprinting details, collected using the Amazon Cognito context data collection library.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
            'Session': 'string',
            'ChallengeParameters': {
                'string': 'string'
            },
            'AuthenticationResult': {
                'AccessToken': 'string',
                'ExpiresIn': 123,
                'TokenType': 'string',
                'RefreshToken': 'string',
                'IdToken': 'string',
                'NewDeviceMetadata': {
                    'DeviceKey': 'string',
                    'DeviceGroupKey': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Responds to the authentication challenge, as an administrator.

        
        

        - **ChallengeName** *(string) --* 

          The name of the challenge. For more information, see .

          
        

        - **Session** *(string) --* 

          The session which should be passed both ways in challenge-response calls to the service. If the or API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next ``RespondToAuthChallenge`` API call.

          
        

        - **ChallengeParameters** *(dict) --* 

          The challenge parameters. For more information, see .

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **AuthenticationResult** *(dict) --* 

          The result returned by the server in response to the authentication request.

          
          

          - **AccessToken** *(string) --* 

            The access token.

            
          

          - **ExpiresIn** *(integer) --* 

            The expiration period of the authentication result.

            
          

          - **TokenType** *(string) --* 

            The token type.

            
          

          - **RefreshToken** *(string) --* 

            The refresh token.

            
          

          - **IdToken** *(string) --* 

            The ID token.

            
          

          - **NewDeviceMetadata** *(dict) --* 

            The new device metadata from an authentication result.

            
            

            - **DeviceKey** *(string) --* 

              The device key.

              
            

            - **DeviceGroupKey** *(string) --* 

              The device group key.

              
        
      
    

  .. py:method:: admin_set_user_mfa_preference(**kwargs)

    

    Sets the user's multi-factor authentication (MFA) preference.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminSetUserMFAPreference>`_    


    **Request Syntax** 
    ::

      response = client.admin_set_user_mfa_preference(
          SMSMfaSettings={
              'Enabled': True|False,
              'PreferredMfa': True|False
          },
          SoftwareTokenMfaSettings={
              'Enabled': True|False,
              'PreferredMfa': True|False
          },
          Username='string',
          UserPoolId='string'
      )
    :type SMSMfaSettings: dict
    :param SMSMfaSettings: 

      The SMS text message MFA settings.

      

    
      - **Enabled** *(boolean) --* 

        Specifies whether SMS text message MFA is enabled.

        

      
      - **PreferredMfa** *(boolean) --* 

        The preferred MFA method.

        

      
    
    :type SoftwareTokenMfaSettings: dict
    :param SoftwareTokenMfaSettings: 

      The time-based one-time password software token MFA settings.

      

    
      - **Enabled** *(boolean) --* 

        Specifies whether software token MFA is enabled.

        

      
      - **PreferredMfa** *(boolean) --* 

        The preferred MFA method.

        

      
    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user pool username.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: admin_set_user_settings(**kwargs)

    

    Sets all the user settings for a specified user name. Works on any user.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminSetUserSettings>`_    


    **Request Syntax** 
    ::

      response = client.admin_set_user_settings(
          UserPoolId='string',
          Username='string',
          MFAOptions=[
              {
                  'DeliveryMedium': 'SMS'|'EMAIL',
                  'AttributeName': 'string'
              },
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to set the user's settings, such as MFA options.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user for whom you wish to set user settings.

      

    
    :type MFAOptions: list
    :param MFAOptions: **[REQUIRED]** 

      Specifies the options for MFA (e.g., email or phone number).

      

    
      - *(dict) --* 

        Specifies the different settings for multi-factor authentication (MFA).

        

      
        - **DeliveryMedium** *(string) --* 

          The delivery medium (email message or SMS message) to send the MFA code.

          

        
        - **AttributeName** *(string) --* 

          The attribute name of the MFA option type.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to set user settings as an administrator.

        
    

  .. py:method:: admin_update_auth_event_feedback(**kwargs)

    

    Provides feedback for an authentication event as to whether it was from a valid user. This feedback is used for improving the risk evaluation decision for the user pool as part of Amazon Cognito advanced security.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminUpdateAuthEventFeedback>`_    


    **Request Syntax** 
    ::

      response = client.admin_update_auth_event_feedback(
          UserPoolId='string',
          Username='string',
          EventId='string',
          FeedbackValue='Valid'|'Invalid'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user pool username.

      

    
    :type EventId: string
    :param EventId: **[REQUIRED]** 

      The authentication event ID.

      

    
    :type FeedbackValue: string
    :param FeedbackValue: **[REQUIRED]** 

      The authentication event feedback value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: admin_update_device_status(**kwargs)

    

    Updates the device status as an administrator.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminUpdateDeviceStatus>`_    


    **Request Syntax** 
    ::

      response = client.admin_update_device_status(
          UserPoolId='string',
          Username='string',
          DeviceKey='string',
          DeviceRememberedStatus='remembered'|'not_remembered'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name.

      

    
    :type DeviceKey: string
    :param DeviceKey: **[REQUIRED]** 

      The device key.

      

    
    :type DeviceRememberedStatus: string
    :param DeviceRememberedStatus: 

      The status indicating whether a device has been remembered or not.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The status response from the request to update the device, as an administrator.

        
    

  .. py:method:: admin_update_user_attributes(**kwargs)

    

    Updates the specified user's attributes, including developer attributes, as an administrator. Works on any user.

     

    For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

     

    In addition to updating user attributes, this API can also be used to mark phone and email as verified.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminUpdateUserAttributes>`_    


    **Request Syntax** 
    ::

      response = client.admin_update_user_attributes(
          UserPoolId='string',
          Username='string',
          UserAttributes=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to update user attributes.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user for whom you want to update user attributes.

      

    
    :type UserAttributes: list
    :param UserAttributes: **[REQUIRED]** 

      An array of name-value pairs representing user attributes.

       

      For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

      

    
      - *(dict) --* 

        Specifies whether the attribute is standard or custom.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the attribute.

          

        
        - **Value** *(string) --* 

          The value of the attribute.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server for the request to update user attributes as an administrator.

        
    

  .. py:method:: admin_user_global_sign_out(**kwargs)

    

    Signs out users from all devices, as an administrator.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminUserGlobalSignOut>`_    


    **Request Syntax** 
    ::

      response = client.admin_user_global_sign_out(
          UserPoolId='string',
          Username='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The global sign-out response, as an administrator.

        
    

  .. py:method:: associate_software_token(**kwargs)

    

    Returns a unique generated shared secret key code for the user account. The request takes an access token or a session string, but not both.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AssociateSoftwareToken>`_    


    **Request Syntax** 
    ::

      response = client.associate_software_token(
          AccessToken='string',
          Session='string'
      )
    :type AccessToken: string
    :param AccessToken: 

      The access token.

      

    
    :type Session: string
    :param Session: 

      The session which should be passed both ways in challenge-response calls to the service. This allows authentication of the user as part of the MFA setup process.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SecretCode': 'string',
            'Session': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SecretCode** *(string) --* 

          A unique generated shared secret code that is used in the TOTP algorithm to generate a one time code.

          
        

        - **Session** *(string) --* 

          The session which should be passed both ways in challenge-response calls to the service. This allows authentication of the user as part of the MFA setup process.

          
    

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


  .. py:method:: change_password(**kwargs)

    

    Changes the password for a specified user in a user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ChangePassword>`_    


    **Request Syntax** 
    ::

      response = client.change_password(
          PreviousPassword='string',
          ProposedPassword='string',
          AccessToken='string'
      )
    :type PreviousPassword: string
    :param PreviousPassword: **[REQUIRED]** 

      The old password.

      

    
    :type ProposedPassword: string
    :param ProposedPassword: **[REQUIRED]** 

      The new password.

      

    
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The response from the server to the change password request.

        
    

  .. py:method:: confirm_device(**kwargs)

    

    Confirms tracking of the device. This API call is the call that begins device tracking.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ConfirmDevice>`_    


    **Request Syntax** 
    ::

      response = client.confirm_device(
          AccessToken='string',
          DeviceKey='string',
          DeviceSecretVerifierConfig={
              'PasswordVerifier': 'string',
              'Salt': 'string'
          },
          DeviceName='string'
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token.

      

    
    :type DeviceKey: string
    :param DeviceKey: **[REQUIRED]** 

      The device key.

      

    
    :type DeviceSecretVerifierConfig: dict
    :param DeviceSecretVerifierConfig: 

      The configuration of the device secret verifier.

      

    
      - **PasswordVerifier** *(string) --* 

        The password verifier.

        

      
      - **Salt** *(string) --* 

        The salt.

        

      
    
    :type DeviceName: string
    :param DeviceName: 

      The device name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserConfirmationNecessary': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Confirms the device response.

        
        

        - **UserConfirmationNecessary** *(boolean) --* 

          Indicates whether the user confirmation is necessary to confirm the device response.

          
    

  .. py:method:: confirm_forgot_password(**kwargs)

    

    Allows a user to enter a confirmation code to reset a forgotten password.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ConfirmForgotPassword>`_    


    **Request Syntax** 
    ::

      response = client.confirm_forgot_password(
          ClientId='string',
          SecretHash='string',
          Username='string',
          ConfirmationCode='string',
          Password='string',
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          },
          UserContextData={
              'EncodedData': 'string'
          }
      )
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The app client ID of the app associated with the user pool.

      

    
    :type SecretHash: string
    :param SecretHash: 

      A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user for whom you want to enter a code to retrieve a forgotten password.

      

    
    :type ConfirmationCode: string
    :param ConfirmationCode: **[REQUIRED]** 

      The confirmation code sent by a user's request to retrieve a forgotten password. For more information, see 

      

    
    :type Password: string
    :param Password: **[REQUIRED]** 

      The password sent by a user's request to retrieve a forgotten password.

      

    
    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The Amazon Pinpoint analytics metadata for collecting metrics for ``ConfirmForgotPassword`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    :type UserContextData: dict
    :param UserContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **EncodedData** *(string) --* 

        Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The response from the server that results from a user's request to retrieve a forgotten password.

        
    

  .. py:method:: confirm_sign_up(**kwargs)

    

    Confirms registration of a user and handles the existing alias from a previous user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ConfirmSignUp>`_    


    **Request Syntax** 
    ::

      response = client.confirm_sign_up(
          ClientId='string',
          SecretHash='string',
          Username='string',
          ConfirmationCode='string',
          ForceAliasCreation=True|False,
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          },
          UserContextData={
              'EncodedData': 'string'
          }
      )
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The ID of the app client associated with the user pool.

      

    
    :type SecretHash: string
    :param SecretHash: 

      A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user whose registration you wish to confirm.

      

    
    :type ConfirmationCode: string
    :param ConfirmationCode: **[REQUIRED]** 

      The confirmation code sent by a user's request to confirm registration.

      

    
    :type ForceAliasCreation: boolean
    :param ForceAliasCreation: 

      Boolean to be specified to force user confirmation irrespective of existing alias. By default set to ``False`` . If this parameter is set to ``True`` and the phone number/email used for sign up confirmation already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user being confirmed. If set to ``False`` , the API will throw an **AliasExistsException** error.

      

    
    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The Amazon Pinpoint analytics metadata for collecting metrics for ``ConfirmSignUp`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    :type UserContextData: dict
    :param UserContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **EncodedData** *(string) --* 

        Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server for the registration confirmation.

        
    

  .. py:method:: create_group(**kwargs)

    

    Creates a new group in the specified user pool.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/CreateGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_group(
          GroupName='string',
          UserPoolId='string',
          Description='string',
          RoleArn='string',
          Precedence=123
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the group. Must be unique.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type Description: string
    :param Description: 

      A string containing the description of the group.

      

    
    :type RoleArn: string
    :param RoleArn: 

      The role ARN for the group.

      

    
    :type Precedence: integer
    :param Precedence: 

      A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. Zero is the highest precedence value. Groups with lower ``Precedence`` values take precedence over groups with higher or null ``Precedence`` values. If a user belongs to two or more groups, it is the group with the lowest precedence value whose role ARN will be used in the ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens.

       

      Two groups can have the same ``Precedence`` value. If this happens, neither group takes precedence over the other. If two groups with the same ``Precedence`` have the same role ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is not set in users' tokens.

       

      The default ``Precedence`` value is null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Group': {
                'GroupName': 'string',
                'UserPoolId': 'string',
                'Description': 'string',
                'RoleArn': 'string',
                'Precedence': 123,
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Group** *(dict) --* 

          The group object for the group.

          
          

          - **GroupName** *(string) --* 

            The name of the group.

            
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool.

            
          

          - **Description** *(string) --* 

            A string containing the description of the group.

            
          

          - **RoleArn** *(string) --* 

            The role ARN for the group.

            
          

          - **Precedence** *(integer) --* 

            A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values or with null ``Precedence`` values.

             

            Two groups can have the same ``Precedence`` value. If this happens, neither group takes precedence over the other. If two groups with the same ``Precedence`` have the same role ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is not set in users' tokens.

             

            The default ``Precedence`` value is null.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The date the group was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the group was created.

            
      
    

  .. py:method:: create_identity_provider(**kwargs)

    

    Creates an identity provider for a user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/CreateIdentityProvider>`_    


    **Request Syntax** 
    ::

      response = client.create_identity_provider(
          UserPoolId='string',
          ProviderName='string',
          ProviderType='SAML'|'Facebook'|'Google'|'LoginWithAmazon',
          ProviderDetails={
              'string': 'string'
          },
          AttributeMapping={
              'string': 'string'
          },
          IdpIdentifiers=[
              'string',
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type ProviderName: string
    :param ProviderName: **[REQUIRED]** 

      The identity provider name.

      

    
    :type ProviderType: string
    :param ProviderType: **[REQUIRED]** 

      The identity provider type.

      

    
    :type ProviderDetails: dict
    :param ProviderDetails: **[REQUIRED]** 

      The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AttributeMapping: dict
    :param AttributeMapping: 

      A mapping of identity provider attributes to standard and custom user pool attributes.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type IdpIdentifiers: list
    :param IdpIdentifiers: 

      A list of identity provider identifiers.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityProvider': {
                'UserPoolId': 'string',
                'ProviderName': 'string',
                'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon',
                'ProviderDetails': {
                    'string': 'string'
                },
                'AttributeMapping': {
                    'string': 'string'
                },
                'IdpIdentifiers': [
                    'string',
                ],
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **IdentityProvider** *(dict) --* 

          The newly created identity provider object.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID.

            
          

          - **ProviderName** *(string) --* 

            The identity provider name.

            
          

          - **ProviderType** *(string) --* 

            The identity provider type.

            
          

          - **ProviderDetails** *(dict) --* 

            The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **AttributeMapping** *(dict) --* 

            A mapping of identity provider attributes to standard and custom user pool attributes.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **IdpIdentifiers** *(list) --* 

            A list of identity provider identifiers.

            
            

            - *(string) --* 
        
          

          - **LastModifiedDate** *(datetime) --* 

            The date the identity provider was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the identity provider was created.

            
      
    

  .. py:method:: create_resource_server(**kwargs)

    

    Creates a new OAuth2.0 resource server and defines custom scopes in it.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/CreateResourceServer>`_    


    **Request Syntax** 
    ::

      response = client.create_resource_server(
          UserPoolId='string',
          Identifier='string',
          Name='string',
          Scopes=[
              {
                  'ScopeName': 'string',
                  'ScopeDescription': 'string'
              },
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type Identifier: string
    :param Identifier: **[REQUIRED]** 

      A unique resource server identifier for the resource server. This could be an HTTPS endpoint where the resource server is located. For example, ``https://my-weather-api.example.com`` .

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name for the resource server.

      

    
    :type Scopes: list
    :param Scopes: 

      A list of scopes. Each scope is map, where the keys are ``name`` and ``description`` .

      

    
      - *(dict) --* 

        A resource server scope.

        

      
        - **ScopeName** *(string) --* **[REQUIRED]** 

          The name of the scope.

          

        
        - **ScopeDescription** *(string) --* **[REQUIRED]** 

          A description of the scope.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceServer': {
                'UserPoolId': 'string',
                'Identifier': 'string',
                'Name': 'string',
                'Scopes': [
                    {
                        'ScopeName': 'string',
                        'ScopeDescription': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceServer** *(dict) --* 

          The newly created resource server.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool that hosts the resource server.

            
          

          - **Identifier** *(string) --* 

            The identifier for the resource server.

            
          

          - **Name** *(string) --* 

            The name of the resource server.

            
          

          - **Scopes** *(list) --* 

            A list of scopes that are defined for the resource server.

            
            

            - *(dict) --* 

              A resource server scope.

              
              

              - **ScopeName** *(string) --* 

                The name of the scope.

                
              

              - **ScopeDescription** *(string) --* 

                A description of the scope.

                
          
        
      
    

  .. py:method:: create_user_import_job(**kwargs)

    

    Creates the user import job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/CreateUserImportJob>`_    


    **Request Syntax** 
    ::

      response = client.create_user_import_job(
          JobName='string',
          UserPoolId='string',
          CloudWatchLogsRoleArn='string'
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      The job name for the user import job.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool that the users are being imported into.

      

    
    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: **[REQUIRED]** 

      The role ARN for the Amazon CloudWatch Logging role for the user import job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserImportJob': {
                'JobName': 'string',
                'JobId': 'string',
                'UserPoolId': 'string',
                'PreSignedUrl': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
                'CloudWatchLogsRoleArn': 'string',
                'ImportedUsers': 123,
                'SkippedUsers': 123,
                'FailedUsers': 123,
                'CompletionMessage': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to the request to create the user import job.

        
        

        - **UserImportJob** *(dict) --* 

          The job object that represents the user import job.

          
          

          - **JobName** *(string) --* 

            The job name for the user import job.

            
          

          - **JobId** *(string) --* 

            The job ID for the user import job.

            
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool that the users are being imported into.

            
          

          - **PreSignedUrl** *(string) --* 

            The pre-signed URL to be used to upload the ``.csv`` file.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user import job was created.

            
          

          - **StartDate** *(datetime) --* 

            The date when the user import job was started.

            
          

          - **CompletionDate** *(datetime) --* 

            The date when the user import job was completed.

            
          

          - **Status** *(string) --* 

            The status of the user import job. One of the following:

             

             
            * ``Created`` - The job was created but not started. 
             
            * ``Pending`` - A transition state. You have started the job, but it has not begun importing users yet. 
             
            * ``InProgress`` - The job has started, and users are being imported. 
             
            * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet. 
             
            * ``Stopped`` - You have stopped the job, and the job has stopped importing users. 
             
            * ``Succeeded`` - The job has completed successfully. 
             
            * ``Failed`` - The job has stopped due to an error. 
             
            * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started. 
             

            
          

          - **CloudWatchLogsRoleArn** *(string) --* 

            The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

            
          

          - **ImportedUsers** *(integer) --* 

            The number of users that were successfully imported.

            
          

          - **SkippedUsers** *(integer) --* 

            The number of users that were skipped.

            
          

          - **FailedUsers** *(integer) --* 

            The number of users that could not be imported.

            
          

          - **CompletionMessage** *(string) --* 

            The message returned when the user import job is completed.

            
      
    

  .. py:method:: create_user_pool(**kwargs)

    

    Creates a new Amazon Cognito user pool and sets the password policy for the pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/CreateUserPool>`_    


    **Request Syntax** 
    ::

      response = client.create_user_pool(
          PoolName='string',
          Policies={
              'PasswordPolicy': {
                  'MinimumLength': 123,
                  'RequireUppercase': True|False,
                  'RequireLowercase': True|False,
                  'RequireNumbers': True|False,
                  'RequireSymbols': True|False
              }
          },
          LambdaConfig={
              'PreSignUp': 'string',
              'CustomMessage': 'string',
              'PostConfirmation': 'string',
              'PreAuthentication': 'string',
              'PostAuthentication': 'string',
              'DefineAuthChallenge': 'string',
              'CreateAuthChallenge': 'string',
              'VerifyAuthChallengeResponse': 'string',
              'PreTokenGeneration': 'string'
          },
          AutoVerifiedAttributes=[
              'phone_number'|'email',
          ],
          AliasAttributes=[
              'phone_number'|'email'|'preferred_username',
          ],
          UsernameAttributes=[
              'phone_number'|'email',
          ],
          SmsVerificationMessage='string',
          EmailVerificationMessage='string',
          EmailVerificationSubject='string',
          VerificationMessageTemplate={
              'SmsMessage': 'string',
              'EmailMessage': 'string',
              'EmailSubject': 'string',
              'EmailMessageByLink': 'string',
              'EmailSubjectByLink': 'string',
              'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
          },
          SmsAuthenticationMessage='string',
          MfaConfiguration='OFF'|'ON'|'OPTIONAL',
          DeviceConfiguration={
              'ChallengeRequiredOnNewDevice': True|False,
              'DeviceOnlyRememberedOnUserPrompt': True|False
          },
          EmailConfiguration={
              'SourceArn': 'string',
              'ReplyToEmailAddress': 'string'
          },
          SmsConfiguration={
              'SnsCallerArn': 'string',
              'ExternalId': 'string'
          },
          UserPoolTags={
              'string': 'string'
          },
          AdminCreateUserConfig={
              'AllowAdminCreateUserOnly': True|False,
              'UnusedAccountValidityDays': 123,
              'InviteMessageTemplate': {
                  'SMSMessage': 'string',
                  'EmailMessage': 'string',
                  'EmailSubject': 'string'
              }
          },
          Schema=[
              {
                  'Name': 'string',
                  'AttributeDataType': 'String'|'Number'|'DateTime'|'Boolean',
                  'DeveloperOnlyAttribute': True|False,
                  'Mutable': True|False,
                  'Required': True|False,
                  'NumberAttributeConstraints': {
                      'MinValue': 'string',
                      'MaxValue': 'string'
                  },
                  'StringAttributeConstraints': {
                      'MinLength': 'string',
                      'MaxLength': 'string'
                  }
              },
          ],
          UserPoolAddOns={
              'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
          }
      )
    :type PoolName: string
    :param PoolName: **[REQUIRED]** 

      A string used to name the user pool.

      

    
    :type Policies: dict
    :param Policies: 

      The policies associated with the new user pool.

      

    
      - **PasswordPolicy** *(dict) --* 

        The password policy.

        

      
        - **MinimumLength** *(integer) --* 

          The minimum length of the password policy that you have set. Cannot be less than 6.

          

        
        - **RequireUppercase** *(boolean) --* 

          In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.

          

        
        - **RequireLowercase** *(boolean) --* 

          In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.

          

        
        - **RequireNumbers** *(boolean) --* 

          In the password policy that you have set, refers to whether you have required users to use at least one number in their password.

          

        
        - **RequireSymbols** *(boolean) --* 

          In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.

          

        
      
    
    :type LambdaConfig: dict
    :param LambdaConfig: 

      The Lambda trigger configuration information for the new user pool.

      

    
      - **PreSignUp** *(string) --* 

        A pre-registration AWS Lambda trigger.

        

      
      - **CustomMessage** *(string) --* 

        A custom Message AWS Lambda trigger.

        

      
      - **PostConfirmation** *(string) --* 

        A post-confirmation AWS Lambda trigger.

        

      
      - **PreAuthentication** *(string) --* 

        A pre-authentication AWS Lambda trigger.

        

      
      - **PostAuthentication** *(string) --* 

        A post-authentication AWS Lambda trigger.

        

      
      - **DefineAuthChallenge** *(string) --* 

        Defines the authentication challenge.

        

      
      - **CreateAuthChallenge** *(string) --* 

        Creates an authentication challenge.

        

      
      - **VerifyAuthChallengeResponse** *(string) --* 

        Verifies the authentication challenge response.

        

      
      - **PreTokenGeneration** *(string) --* 

        A Lambda trigger that is invoked before token generation.

        

      
    
    :type AutoVerifiedAttributes: list
    :param AutoVerifiedAttributes: 

      The attributes to be auto-verified. Possible values: **email** , **phone_number** .

      

    
      - *(string) --* 

      
  
    :type AliasAttributes: list
    :param AliasAttributes: 

      Attributes supported as an alias for this user pool. Possible values: **phone_number** , **email** , or **preferred_username** .

      

    
      - *(string) --* 

      
  
    :type UsernameAttributes: list
    :param UsernameAttributes: 

      Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up.

      

    
      - *(string) --* 

      
  
    :type SmsVerificationMessage: string
    :param SmsVerificationMessage: 

      A string representing the SMS verification message.

      

    
    :type EmailVerificationMessage: string
    :param EmailVerificationMessage: 

      A string representing the email verification message.

      

    
    :type EmailVerificationSubject: string
    :param EmailVerificationSubject: 

      A string representing the email verification subject.

      

    
    :type VerificationMessageTemplate: dict
    :param VerificationMessageTemplate: 

      The template for the verification message that the user sees when the app requests permission to access the user's information.

      

    
      - **SmsMessage** *(string) --* 

        The SMS message template.

        

      
      - **EmailMessage** *(string) --* 

        The email message template.

        

      
      - **EmailSubject** *(string) --* 

        The subject line for the email message template.

        

      
      - **EmailMessageByLink** *(string) --* 

        The email message template for sending a confirmation link to the user.

        

      
      - **EmailSubjectByLink** *(string) --* 

        The subject line for the email message template for sending a confirmation link to the user.

        

      
      - **DefaultEmailOption** *(string) --* 

        The default email option.

        

      
    
    :type SmsAuthenticationMessage: string
    :param SmsAuthenticationMessage: 

      A string representing the SMS authentication message.

      

    
    :type MfaConfiguration: string
    :param MfaConfiguration: 

      Specifies MFA configuration details.

      

    
    :type DeviceConfiguration: dict
    :param DeviceConfiguration: 

      The device configuration.

      

    
      - **ChallengeRequiredOnNewDevice** *(boolean) --* 

        Indicates whether a challenge is required on a new device. Only applicable to a new device.

        

      
      - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --* 

        If true, a device is only remembered on user prompt.

        

      
    
    :type EmailConfiguration: dict
    :param EmailConfiguration: 

      The email configuration.

      

    
      - **SourceArn** *(string) --* 

        The Amazon Resource Name (ARN) of the email source.

        

      
      - **ReplyToEmailAddress** *(string) --* 

        The destination to which the receiver of the email should reply to.

        

      
    
    :type SmsConfiguration: dict
    :param SmsConfiguration: 

      The SMS configuration.

      

    
      - **SnsCallerArn** *(string) --* **[REQUIRED]** 

        The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.

        

      
      - **ExternalId** *(string) --* 

        The external ID.

        

      
    
    :type UserPoolTags: dict
    :param UserPoolTags: 

      The cost allocation tags for the user pool. For more information, see `Adding Cost Allocation Tags to Your User Pool <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-cost-allocation-tagging.html>`__  

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AdminCreateUserConfig: dict
    :param AdminCreateUserConfig: 

      The configuration for ``AdminCreateUser`` requests.

      

    
      - **AllowAdminCreateUserOnly** *(boolean) --* 

        Set to ``True`` if only the administrator is allowed to create user profiles. Set to ``False`` if users can sign themselves up via an app.

        

      
      - **UnusedAccountValidityDays** *(integer) --* 

        The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call ``AdminCreateUser`` again, specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this parameter is 7.

        

      
      - **InviteMessageTemplate** *(dict) --* 

        The message template to be used for the welcome message to new users.

         

        See also `Customizing User Invitation Messages <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__ .

        

      
        - **SMSMessage** *(string) --* 

          The message template for SMS messages.

          

        
        - **EmailMessage** *(string) --* 

          The message template for email messages.

          

        
        - **EmailSubject** *(string) --* 

          The subject line for email messages.

          

        
      
    
    :type Schema: list
    :param Schema: 

      An array of schema attributes for the new user pool. These attributes can be standard or custom attributes.

      

    
      - *(dict) --* 

        Contains information about the schema attribute.

        

      
        - **Name** *(string) --* 

          A schema attribute of the name type.

          

        
        - **AttributeDataType** *(string) --* 

          The attribute data type.

          

        
        - **DeveloperOnlyAttribute** *(boolean) --* 

          Specifies whether the attribute type is developer only.

          

        
        - **Mutable** *(boolean) --* 

          Specifies whether the attribute can be changed once it has been created.

          

        
        - **Required** *(boolean) --* 

          Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.

          

        
        - **NumberAttributeConstraints** *(dict) --* 

          Specifies the constraints for an attribute of the number type.

          

        
          - **MinValue** *(string) --* 

            The minimum value of an attribute that is of the number data type.

            

          
          - **MaxValue** *(string) --* 

            The maximum value of an attribute that is of the number data type.

            

          
        
        - **StringAttributeConstraints** *(dict) --* 

          Specifies the constraints for an attribute of the string type.

          

        
          - **MinLength** *(string) --* 

            The minimum length.

            

          
          - **MaxLength** *(string) --* 

            The maximum length.

            

          
        
      
  
    :type UserPoolAddOns: dict
    :param UserPoolAddOns: 

      Used to enable advanced security risk detection. Set the key ``AdvancedSecurityMode`` to the value "AUDIT".

      

    
      - **AdvancedSecurityMode** *(string) --* **[REQUIRED]** 

        The advanced security mode.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserPool': {
                'Id': 'string',
                'Name': 'string',
                'Policies': {
                    'PasswordPolicy': {
                        'MinimumLength': 123,
                        'RequireUppercase': True|False,
                        'RequireLowercase': True|False,
                        'RequireNumbers': True|False,
                        'RequireSymbols': True|False
                    }
                },
                'LambdaConfig': {
                    'PreSignUp': 'string',
                    'CustomMessage': 'string',
                    'PostConfirmation': 'string',
                    'PreAuthentication': 'string',
                    'PostAuthentication': 'string',
                    'DefineAuthChallenge': 'string',
                    'CreateAuthChallenge': 'string',
                    'VerifyAuthChallengeResponse': 'string',
                    'PreTokenGeneration': 'string'
                },
                'Status': 'Enabled'|'Disabled',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1),
                'SchemaAttributes': [
                    {
                        'Name': 'string',
                        'AttributeDataType': 'String'|'Number'|'DateTime'|'Boolean',
                        'DeveloperOnlyAttribute': True|False,
                        'Mutable': True|False,
                        'Required': True|False,
                        'NumberAttributeConstraints': {
                            'MinValue': 'string',
                            'MaxValue': 'string'
                        },
                        'StringAttributeConstraints': {
                            'MinLength': 'string',
                            'MaxLength': 'string'
                        }
                    },
                ],
                'AutoVerifiedAttributes': [
                    'phone_number'|'email',
                ],
                'AliasAttributes': [
                    'phone_number'|'email'|'preferred_username',
                ],
                'UsernameAttributes': [
                    'phone_number'|'email',
                ],
                'SmsVerificationMessage': 'string',
                'EmailVerificationMessage': 'string',
                'EmailVerificationSubject': 'string',
                'VerificationMessageTemplate': {
                    'SmsMessage': 'string',
                    'EmailMessage': 'string',
                    'EmailSubject': 'string',
                    'EmailMessageByLink': 'string',
                    'EmailSubjectByLink': 'string',
                    'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
                },
                'SmsAuthenticationMessage': 'string',
                'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL',
                'DeviceConfiguration': {
                    'ChallengeRequiredOnNewDevice': True|False,
                    'DeviceOnlyRememberedOnUserPrompt': True|False
                },
                'EstimatedNumberOfUsers': 123,
                'EmailConfiguration': {
                    'SourceArn': 'string',
                    'ReplyToEmailAddress': 'string'
                },
                'SmsConfiguration': {
                    'SnsCallerArn': 'string',
                    'ExternalId': 'string'
                },
                'UserPoolTags': {
                    'string': 'string'
                },
                'SmsConfigurationFailure': 'string',
                'EmailConfigurationFailure': 'string',
                'Domain': 'string',
                'AdminCreateUserConfig': {
                    'AllowAdminCreateUserOnly': True|False,
                    'UnusedAccountValidityDays': 123,
                    'InviteMessageTemplate': {
                        'SMSMessage': 'string',
                        'EmailMessage': 'string',
                        'EmailSubject': 'string'
                    }
                },
                'UserPoolAddOns': {
                    'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server for the request to create a user pool.

        
        

        - **UserPool** *(dict) --* 

          A container for the user pool details.

          
          

          - **Id** *(string) --* 

            The ID of the user pool.

            
          

          - **Name** *(string) --* 

            The name of the user pool.

            
          

          - **Policies** *(dict) --* 

            The policies associated with the user pool.

            
            

            - **PasswordPolicy** *(dict) --* 

              The password policy.

              
              

              - **MinimumLength** *(integer) --* 

                The minimum length of the password policy that you have set. Cannot be less than 6.

                
              

              - **RequireUppercase** *(boolean) --* 

                In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.

                
              

              - **RequireLowercase** *(boolean) --* 

                In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.

                
              

              - **RequireNumbers** *(boolean) --* 

                In the password policy that you have set, refers to whether you have required users to use at least one number in their password.

                
              

              - **RequireSymbols** *(boolean) --* 

                In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.

                
          
        
          

          - **LambdaConfig** *(dict) --* 

            The AWS Lambda triggers associated with tue user pool.

            
            

            - **PreSignUp** *(string) --* 

              A pre-registration AWS Lambda trigger.

              
            

            - **CustomMessage** *(string) --* 

              A custom Message AWS Lambda trigger.

              
            

            - **PostConfirmation** *(string) --* 

              A post-confirmation AWS Lambda trigger.

              
            

            - **PreAuthentication** *(string) --* 

              A pre-authentication AWS Lambda trigger.

              
            

            - **PostAuthentication** *(string) --* 

              A post-authentication AWS Lambda trigger.

              
            

            - **DefineAuthChallenge** *(string) --* 

              Defines the authentication challenge.

              
            

            - **CreateAuthChallenge** *(string) --* 

              Creates an authentication challenge.

              
            

            - **VerifyAuthChallengeResponse** *(string) --* 

              Verifies the authentication challenge response.

              
            

            - **PreTokenGeneration** *(string) --* 

              A Lambda trigger that is invoked before token generation.

              
        
          

          - **Status** *(string) --* 

            The status of a user pool.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The date the user pool was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user pool was created.

            
          

          - **SchemaAttributes** *(list) --* 

            A container with the schema attributes of a user pool.

            
            

            - *(dict) --* 

              Contains information about the schema attribute.

              
              

              - **Name** *(string) --* 

                A schema attribute of the name type.

                
              

              - **AttributeDataType** *(string) --* 

                The attribute data type.

                
              

              - **DeveloperOnlyAttribute** *(boolean) --* 

                Specifies whether the attribute type is developer only.

                
              

              - **Mutable** *(boolean) --* 

                Specifies whether the attribute can be changed once it has been created.

                
              

              - **Required** *(boolean) --* 

                Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.

                
              

              - **NumberAttributeConstraints** *(dict) --* 

                Specifies the constraints for an attribute of the number type.

                
                

                - **MinValue** *(string) --* 

                  The minimum value of an attribute that is of the number data type.

                  
                

                - **MaxValue** *(string) --* 

                  The maximum value of an attribute that is of the number data type.

                  
            
              

              - **StringAttributeConstraints** *(dict) --* 

                Specifies the constraints for an attribute of the string type.

                
                

                - **MinLength** *(string) --* 

                  The minimum length.

                  
                

                - **MaxLength** *(string) --* 

                  The maximum length.

                  
            
          
        
          

          - **AutoVerifiedAttributes** *(list) --* 

            Specifies the attributes that are auto-verified in a user pool.

            
            

            - *(string) --* 
        
          

          - **AliasAttributes** *(list) --* 

            Specifies the attributes that are aliased in a user pool.

            
            

            - *(string) --* 
        
          

          - **UsernameAttributes** *(list) --* 

            Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up.

            
            

            - *(string) --* 
        
          

          - **SmsVerificationMessage** *(string) --* 

            The contents of the SMS verification message.

            
          

          - **EmailVerificationMessage** *(string) --* 

            The contents of the email verification message.

            
          

          - **EmailVerificationSubject** *(string) --* 

            The subject of the email verification message.

            
          

          - **VerificationMessageTemplate** *(dict) --* 

            The template for verification messages.

            
            

            - **SmsMessage** *(string) --* 

              The SMS message template.

              
            

            - **EmailMessage** *(string) --* 

              The email message template.

              
            

            - **EmailSubject** *(string) --* 

              The subject line for the email message template.

              
            

            - **EmailMessageByLink** *(string) --* 

              The email message template for sending a confirmation link to the user.

              
            

            - **EmailSubjectByLink** *(string) --* 

              The subject line for the email message template for sending a confirmation link to the user.

              
            

            - **DefaultEmailOption** *(string) --* 

              The default email option.

              
        
          

          - **SmsAuthenticationMessage** *(string) --* 

            The contents of the SMS authentication message.

            
          

          - **MfaConfiguration** *(string) --* 

            Can be one of the following values:

             

             
            * ``OFF`` - MFA tokens are not required and cannot be specified during user registration. 
             
            * ``ON`` - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool. 
             
            * ``OPTIONAL`` - Users have the option when registering to create an MFA token. 
             

            
          

          - **DeviceConfiguration** *(dict) --* 

            The device configuration.

            
            

            - **ChallengeRequiredOnNewDevice** *(boolean) --* 

              Indicates whether a challenge is required on a new device. Only applicable to a new device.

              
            

            - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --* 

              If true, a device is only remembered on user prompt.

              
        
          

          - **EstimatedNumberOfUsers** *(integer) --* 

            A number estimating the size of the user pool.

            
          

          - **EmailConfiguration** *(dict) --* 

            The email configuration.

            
            

            - **SourceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the email source.

              
            

            - **ReplyToEmailAddress** *(string) --* 

              The destination to which the receiver of the email should reply to.

              
        
          

          - **SmsConfiguration** *(dict) --* 

            The SMS configuration.

            
            

            - **SnsCallerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.

              
            

            - **ExternalId** *(string) --* 

              The external ID.

              
        
          

          - **UserPoolTags** *(dict) --* 

            The cost allocation tags for the user pool. For more information, see `Adding Cost Allocation Tags to Your User Pool <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-cost-allocation-tagging.html>`__  

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **SmsConfigurationFailure** *(string) --* 

            The reason why the SMS configuration cannot send the messages to your users.

            
          

          - **EmailConfigurationFailure** *(string) --* 

            The reason why the email configuration cannot send the messages to your users.

            
          

          - **Domain** *(string) --* 

            Holds the domain prefix if the user pool has a domain associated with it.

            
          

          - **AdminCreateUserConfig** *(dict) --* 

            The configuration for ``AdminCreateUser`` requests.

            
            

            - **AllowAdminCreateUserOnly** *(boolean) --* 

              Set to ``True`` if only the administrator is allowed to create user profiles. Set to ``False`` if users can sign themselves up via an app.

              
            

            - **UnusedAccountValidityDays** *(integer) --* 

              The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call ``AdminCreateUser`` again, specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this parameter is 7.

              
            

            - **InviteMessageTemplate** *(dict) --* 

              The message template to be used for the welcome message to new users.

               

              See also `Customizing User Invitation Messages <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__ .

              
              

              - **SMSMessage** *(string) --* 

                The message template for SMS messages.

                
              

              - **EmailMessage** *(string) --* 

                The message template for email messages.

                
              

              - **EmailSubject** *(string) --* 

                The subject line for email messages.

                
          
        
          

          - **UserPoolAddOns** *(dict) --* 

            The user pool add-ons.

            
            

            - **AdvancedSecurityMode** *(string) --* 

              The advanced security mode.

              
        
      
    

  .. py:method:: create_user_pool_client(**kwargs)

    

    Creates the user pool client.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/CreateUserPoolClient>`_    


    **Request Syntax** 
    ::

      response = client.create_user_pool_client(
          UserPoolId='string',
          ClientName='string',
          GenerateSecret=True|False,
          RefreshTokenValidity=123,
          ReadAttributes=[
              'string',
          ],
          WriteAttributes=[
              'string',
          ],
          ExplicitAuthFlows=[
              'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
          ],
          SupportedIdentityProviders=[
              'string',
          ],
          CallbackURLs=[
              'string',
          ],
          LogoutURLs=[
              'string',
          ],
          DefaultRedirectURI='string',
          AllowedOAuthFlows=[
              'code'|'implicit'|'client_credentials',
          ],
          AllowedOAuthScopes=[
              'string',
          ],
          AllowedOAuthFlowsUserPoolClient=True|False,
          AnalyticsConfiguration={
              'ApplicationId': 'string',
              'RoleArn': 'string',
              'ExternalId': 'string',
              'UserDataShared': True|False
          }
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to create a user pool client.

      

    
    :type ClientName: string
    :param ClientName: **[REQUIRED]** 

      The client name for the user pool client you would like to create.

      

    
    :type GenerateSecret: boolean
    :param GenerateSecret: 

      Boolean to specify whether you want to generate a secret for the user pool client being created.

      

    
    :type RefreshTokenValidity: integer
    :param RefreshTokenValidity: 

      The time limit, in days, after which the refresh token is no longer valid and cannot be used.

      

    
    :type ReadAttributes: list
    :param ReadAttributes: 

      The read attributes.

      

    
      - *(string) --* 

      
  
    :type WriteAttributes: list
    :param WriteAttributes: 

      The write attributes.

      

    
      - *(string) --* 

      
  
    :type ExplicitAuthFlows: list
    :param ExplicitAuthFlows: 

      The explicit authentication flows.

      

    
      - *(string) --* 

      
  
    :type SupportedIdentityProviders: list
    :param SupportedIdentityProviders: 

      A list of provider names for the identity providers that are supported on this client.

      

    
      - *(string) --* 

      
  
    :type CallbackURLs: list
    :param CallbackURLs: 

      A list of allowed callback URLs for the identity providers.

      

    
      - *(string) --* 

      
  
    :type LogoutURLs: list
    :param LogoutURLs: 

      A list of allowed logout URLs for the identity providers.

      

    
      - *(string) --* 

      
  
    :type DefaultRedirectURI: string
    :param DefaultRedirectURI: 

      The default redirect URI. Must be in the ``CallbackURLs`` list.

      

    
    :type AllowedOAuthFlows: list
    :param AllowedOAuthFlows: 

      Set to ``code`` to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.

       

      Set to ``token`` to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.

      

    
      - *(string) --* 

      
  
    :type AllowedOAuthScopes: list
    :param AllowedOAuthScopes: 

      A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` , ``"email"`` , ``"openid"`` , and ``"Cognito"`` .

      

    
      - *(string) --* 

      
  
    :type AllowedOAuthFlowsUserPoolClient: boolean
    :param AllowedOAuthFlowsUserPoolClient: 

      Set to ``True`` if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

      

    
    :type AnalyticsConfiguration: dict
    :param AnalyticsConfiguration: 

      The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.

      

    
      - **ApplicationId** *(string) --* **[REQUIRED]** 

        The application ID for an Amazon Pinpoint application.

        

      
      - **RoleArn** *(string) --* **[REQUIRED]** 

        The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.

        

      
      - **ExternalId** *(string) --* **[REQUIRED]** 

        The external ID.

        

      
      - **UserDataShared** *(boolean) --* 

        If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserPoolClient': {
                'UserPoolId': 'string',
                'ClientName': 'string',
                'ClientId': 'string',
                'ClientSecret': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1),
                'RefreshTokenValidity': 123,
                'ReadAttributes': [
                    'string',
                ],
                'WriteAttributes': [
                    'string',
                ],
                'ExplicitAuthFlows': [
                    'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
                ],
                'SupportedIdentityProviders': [
                    'string',
                ],
                'CallbackURLs': [
                    'string',
                ],
                'LogoutURLs': [
                    'string',
                ],
                'DefaultRedirectURI': 'string',
                'AllowedOAuthFlows': [
                    'code'|'implicit'|'client_credentials',
                ],
                'AllowedOAuthScopes': [
                    'string',
                ],
                'AllowedOAuthFlowsUserPoolClient': True|False,
                'AnalyticsConfiguration': {
                    'ApplicationId': 'string',
                    'RoleArn': 'string',
                    'ExternalId': 'string',
                    'UserDataShared': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to create a user pool client.

        
        

        - **UserPoolClient** *(dict) --* 

          The user pool client that was just created.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool client.

            
          

          - **ClientName** *(string) --* 

            The client name from the user pool request of the client type.

            
          

          - **ClientId** *(string) --* 

            The ID of the client associated with the user pool.

            
          

          - **ClientSecret** *(string) --* 

            The client secret from the user pool request of the client type.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The date the user pool client was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user pool client was created.

            
          

          - **RefreshTokenValidity** *(integer) --* 

            The time limit, in days, after which the refresh token is no longer valid and cannot be used.

            
          

          - **ReadAttributes** *(list) --* 

            The Read-only attributes.

            
            

            - *(string) --* 
        
          

          - **WriteAttributes** *(list) --* 

            The writeable attributes.

            
            

            - *(string) --* 
        
          

          - **ExplicitAuthFlows** *(list) --* 

            The explicit authentication flows.

            
            

            - *(string) --* 
        
          

          - **SupportedIdentityProviders** *(list) --* 

            A list of provider names for the identity providers that are supported on this client.

            
            

            - *(string) --* 
        
          

          - **CallbackURLs** *(list) --* 

            A list of allowed callback URLs for the identity providers.

            
            

            - *(string) --* 
        
          

          - **LogoutURLs** *(list) --* 

            A list of allowed logout URLs for the identity providers.

            
            

            - *(string) --* 
        
          

          - **DefaultRedirectURI** *(string) --* 

            The default redirect URI. Must be in the ``CallbackURLs`` list.

            
          

          - **AllowedOAuthFlows** *(list) --* 

            Set to ``code`` to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.

             

            Set to ``token`` to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.

            
            

            - *(string) --* 
        
          

          - **AllowedOAuthScopes** *(list) --* 

            A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` , ``"email"`` , ``"openid"`` , and ``"Cognito"`` .

            
            

            - *(string) --* 
        
          

          - **AllowedOAuthFlowsUserPoolClient** *(boolean) --* 

            Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

            
          

          - **AnalyticsConfiguration** *(dict) --* 

            The Amazon Pinpoint analytics configuration for the user pool client.

            
            

            - **ApplicationId** *(string) --* 

              The application ID for an Amazon Pinpoint application.

              
            

            - **RoleArn** *(string) --* 

              The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.

              
            

            - **ExternalId** *(string) --* 

              The external ID.

              
            

            - **UserDataShared** *(boolean) --* 

              If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.

              
        
      
    

  .. py:method:: create_user_pool_domain(**kwargs)

    

    Creates a new domain for a user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/CreateUserPoolDomain>`_    


    **Request Syntax** 
    ::

      response = client.create_user_pool_domain(
          Domain='string',
          UserPoolId='string'
      )
    :type Domain: string
    :param Domain: **[REQUIRED]** 

      The domain string.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_group(**kwargs)

    

    Deletes a group. Currently only groups with no members can be deleted.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DeleteGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_group(
          GroupName='string',
          UserPoolId='string'
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the group.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    
    :returns: None

  .. py:method:: delete_identity_provider(**kwargs)

    

    Deletes an identity provider for a user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DeleteIdentityProvider>`_    


    **Request Syntax** 
    ::

      response = client.delete_identity_provider(
          UserPoolId='string',
          ProviderName='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type ProviderName: string
    :param ProviderName: **[REQUIRED]** 

      The identity provider name.

      

    
    
    :returns: None

  .. py:method:: delete_resource_server(**kwargs)

    

    Deletes a resource server.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DeleteResourceServer>`_    


    **Request Syntax** 
    ::

      response = client.delete_resource_server(
          UserPoolId='string',
          Identifier='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool that hosts the resource server.

      

    
    :type Identifier: string
    :param Identifier: **[REQUIRED]** 

      The identifier for the resource server.

      

    
    
    :returns: None

  .. py:method:: delete_user(**kwargs)

    

    Allows a user to delete himself or herself.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DeleteUser>`_    


    **Request Syntax** 
    ::

      response = client.delete_user(
          AccessToken='string'
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token from a request to delete a user.

      

    
    
    :returns: None

  .. py:method:: delete_user_attributes(**kwargs)

    

    Deletes the attributes for a user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DeleteUserAttributes>`_    


    **Request Syntax** 
    ::

      response = client.delete_user_attributes(
          UserAttributeNames=[
              'string',
          ],
          AccessToken='string'
      )
    :type UserAttributeNames: list
    :param UserAttributeNames: **[REQUIRED]** 

      An array of strings representing the user attribute names you wish to delete.

       

      For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

      

    
      - *(string) --* 

      
  
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token used in the request to delete user attributes.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to delete user attributes.

        
    

  .. py:method:: delete_user_pool(**kwargs)

    

    Deletes the specified Amazon Cognito user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DeleteUserPool>`_    


    **Request Syntax** 
    ::

      response = client.delete_user_pool(
          UserPoolId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool you want to delete.

      

    
    
    :returns: None

  .. py:method:: delete_user_pool_client(**kwargs)

    

    Allows the developer to delete the user pool client.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DeleteUserPoolClient>`_    


    **Request Syntax** 
    ::

      response = client.delete_user_pool_client(
          UserPoolId='string',
          ClientId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to delete the client.

      

    
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The app client ID of the app associated with the user pool.

      

    
    
    :returns: None

  .. py:method:: delete_user_pool_domain(**kwargs)

    

    Deletes a domain for a user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DeleteUserPoolDomain>`_    


    **Request Syntax** 
    ::

      response = client.delete_user_pool_domain(
          Domain='string',
          UserPoolId='string'
      )
    :type Domain: string
    :param Domain: **[REQUIRED]** 

      The domain string.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_identity_provider(**kwargs)

    

    Gets information about a specific identity provider.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DescribeIdentityProvider>`_    


    **Request Syntax** 
    ::

      response = client.describe_identity_provider(
          UserPoolId='string',
          ProviderName='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type ProviderName: string
    :param ProviderName: **[REQUIRED]** 

      The identity provider name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityProvider': {
                'UserPoolId': 'string',
                'ProviderName': 'string',
                'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon',
                'ProviderDetails': {
                    'string': 'string'
                },
                'AttributeMapping': {
                    'string': 'string'
                },
                'IdpIdentifiers': [
                    'string',
                ],
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **IdentityProvider** *(dict) --* 

          The identity provider that was deleted.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID.

            
          

          - **ProviderName** *(string) --* 

            The identity provider name.

            
          

          - **ProviderType** *(string) --* 

            The identity provider type.

            
          

          - **ProviderDetails** *(dict) --* 

            The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **AttributeMapping** *(dict) --* 

            A mapping of identity provider attributes to standard and custom user pool attributes.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **IdpIdentifiers** *(list) --* 

            A list of identity provider identifiers.

            
            

            - *(string) --* 
        
          

          - **LastModifiedDate** *(datetime) --* 

            The date the identity provider was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the identity provider was created.

            
      
    

  .. py:method:: describe_resource_server(**kwargs)

    

    Describes a resource server.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DescribeResourceServer>`_    


    **Request Syntax** 
    ::

      response = client.describe_resource_server(
          UserPoolId='string',
          Identifier='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool that hosts the resource server.

      

    
    :type Identifier: string
    :param Identifier: **[REQUIRED]** 

      The identifier for the resource server

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceServer': {
                'UserPoolId': 'string',
                'Identifier': 'string',
                'Name': 'string',
                'Scopes': [
                    {
                        'ScopeName': 'string',
                        'ScopeDescription': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceServer** *(dict) --* 

          The resource server.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool that hosts the resource server.

            
          

          - **Identifier** *(string) --* 

            The identifier for the resource server.

            
          

          - **Name** *(string) --* 

            The name of the resource server.

            
          

          - **Scopes** *(list) --* 

            A list of scopes that are defined for the resource server.

            
            

            - *(dict) --* 

              A resource server scope.

              
              

              - **ScopeName** *(string) --* 

                The name of the scope.

                
              

              - **ScopeDescription** *(string) --* 

                A description of the scope.

                
          
        
      
    

  .. py:method:: describe_risk_configuration(**kwargs)

    

    Describes the risk configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DescribeRiskConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.describe_risk_configuration(
          UserPoolId='string',
          ClientId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type ClientId: string
    :param ClientId: 

      The app client ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RiskConfiguration': {
                'UserPoolId': 'string',
                'ClientId': 'string',
                'CompromisedCredentialsRiskConfiguration': {
                    'EventFilter': [
                        'SIGN_IN'|'PASSWORD_CHANGE'|'SIGN_UP',
                    ],
                    'Actions': {
                        'EventAction': 'BLOCK'|'NO_ACTION'
                    }
                },
                'AccountTakeoverRiskConfiguration': {
                    'NotifyConfiguration': {
                        'From': 'string',
                        'ReplyTo': 'string',
                        'SourceArn': 'string',
                        'BlockEmail': {
                            'Subject': 'string',
                            'HtmlBody': 'string',
                            'TextBody': 'string'
                        },
                        'NoActionEmail': {
                            'Subject': 'string',
                            'HtmlBody': 'string',
                            'TextBody': 'string'
                        },
                        'MfaEmail': {
                            'Subject': 'string',
                            'HtmlBody': 'string',
                            'TextBody': 'string'
                        }
                    },
                    'Actions': {
                        'LowAction': {
                            'Notify': True|False,
                            'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                        },
                        'MediumAction': {
                            'Notify': True|False,
                            'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                        },
                        'HighAction': {
                            'Notify': True|False,
                            'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                        }
                    }
                },
                'RiskExceptionConfiguration': {
                    'BlockedIPRangeList': [
                        'string',
                    ],
                    'SkippedIPRangeList': [
                        'string',
                    ]
                },
                'LastModifiedDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RiskConfiguration** *(dict) --* 

          The risk configuration.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID.

            
          

          - **ClientId** *(string) --* 

            The app client ID.

            
          

          - **CompromisedCredentialsRiskConfiguration** *(dict) --* 

            The compromised credentials risk configuration object including the ``EventFilter`` and the ``EventAction``  

            
            

            - **EventFilter** *(list) --* 

              Perform the action for these events. The default is to perform all events if no event filter is specified.

              
              

              - *(string) --* 
          
            

            - **Actions** *(dict) --* 

              The compromised credentials risk configuration actions.

              
              

              - **EventAction** *(string) --* 

                The event action.

                
          
        
          

          - **AccountTakeoverRiskConfiguration** *(dict) --* 

            The account takeover risk configuration object including the ``NotifyConfiguration`` object and ``Actions`` to take in the case of an account takeover.

            
            

            - **NotifyConfiguration** *(dict) --* 

              The notify configuration used to construct email notifications.

              
              

              - **From** *(string) --* 

                The email address that is sending the email. It must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

                
              

              - **ReplyTo** *(string) --* 

                The destination to which the receiver of an email should reply to.

                
              

              - **SourceArn** *(string) --* 

                The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. It permits Amazon Cognito to send for the email address specified in the ``From`` parameter.

                
              

              - **BlockEmail** *(dict) --* 

                Email template used when a detected risk event is blocked.

                
                

                - **Subject** *(string) --* 

                  The subject.

                  
                

                - **HtmlBody** *(string) --* 

                  The HTML body.

                  
                

                - **TextBody** *(string) --* 

                  The text body.

                  
            
              

              - **NoActionEmail** *(dict) --* 

                The email template used when a detected risk event is allowed.

                
                

                - **Subject** *(string) --* 

                  The subject.

                  
                

                - **HtmlBody** *(string) --* 

                  The HTML body.

                  
                

                - **TextBody** *(string) --* 

                  The text body.

                  
            
              

              - **MfaEmail** *(dict) --* 

                The MFA email template used when MFA is challenged as part of a detected risk.

                
                

                - **Subject** *(string) --* 

                  The subject.

                  
                

                - **HtmlBody** *(string) --* 

                  The HTML body.

                  
                

                - **TextBody** *(string) --* 

                  The text body.

                  
            
          
            

            - **Actions** *(dict) --* 

              Account takeover risk configuration actions

              
              

              - **LowAction** *(dict) --* 

                Action to take for a low risk.

                
                

                - **Notify** *(boolean) --* 

                  Flag specifying whether to send a notification.

                  
                

                - **EventAction** *(string) --* 

                  The event action.

                   

                   
                  * ``BLOCK`` Choosing this action will block the request. 
                   
                  * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
                   
                  * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
                   
                  * ``NO_ACTION`` Allow the user sign-in. 
                   

                  
            
              

              - **MediumAction** *(dict) --* 

                Action to take for a medium risk.

                
                

                - **Notify** *(boolean) --* 

                  Flag specifying whether to send a notification.

                  
                

                - **EventAction** *(string) --* 

                  The event action.

                   

                   
                  * ``BLOCK`` Choosing this action will block the request. 
                   
                  * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
                   
                  * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
                   
                  * ``NO_ACTION`` Allow the user sign-in. 
                   

                  
            
              

              - **HighAction** *(dict) --* 

                Action to take for a high risk.

                
                

                - **Notify** *(boolean) --* 

                  Flag specifying whether to send a notification.

                  
                

                - **EventAction** *(string) --* 

                  The event action.

                   

                   
                  * ``BLOCK`` Choosing this action will block the request. 
                   
                  * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
                   
                  * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
                   
                  * ``NO_ACTION`` Allow the user sign-in. 
                   

                  
            
          
        
          

          - **RiskExceptionConfiguration** *(dict) --* 

            The configuration to override the risk decision.

            
            

            - **BlockedIPRangeList** *(list) --* 

              Overrides the risk decision to always block the pre-authentication requests. The IP range is in CIDR notation: a compact representation of an IP address and its associated routing prefix.

              
              

              - *(string) --* 
          
            

            - **SkippedIPRangeList** *(list) --* 

              Risk detection is not performed on the IP addresses in the range list. The IP range is in CIDR notation.

              
              

              - *(string) --* 
          
        
          

          - **LastModifiedDate** *(datetime) --* 

            The last modified date.

            
      
    

  .. py:method:: describe_user_import_job(**kwargs)

    

    Describes the user import job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DescribeUserImportJob>`_    


    **Request Syntax** 
    ::

      response = client.describe_user_import_job(
          UserPoolId='string',
          JobId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool that the users are being imported into.

      

    
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      The job ID for the user import job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserImportJob': {
                'JobName': 'string',
                'JobId': 'string',
                'UserPoolId': 'string',
                'PreSignedUrl': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
                'CloudWatchLogsRoleArn': 'string',
                'ImportedUsers': 123,
                'SkippedUsers': 123,
                'FailedUsers': 123,
                'CompletionMessage': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to the request to describe the user import job.

        
        

        - **UserImportJob** *(dict) --* 

          The job object that represents the user import job.

          
          

          - **JobName** *(string) --* 

            The job name for the user import job.

            
          

          - **JobId** *(string) --* 

            The job ID for the user import job.

            
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool that the users are being imported into.

            
          

          - **PreSignedUrl** *(string) --* 

            The pre-signed URL to be used to upload the ``.csv`` file.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user import job was created.

            
          

          - **StartDate** *(datetime) --* 

            The date when the user import job was started.

            
          

          - **CompletionDate** *(datetime) --* 

            The date when the user import job was completed.

            
          

          - **Status** *(string) --* 

            The status of the user import job. One of the following:

             

             
            * ``Created`` - The job was created but not started. 
             
            * ``Pending`` - A transition state. You have started the job, but it has not begun importing users yet. 
             
            * ``InProgress`` - The job has started, and users are being imported. 
             
            * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet. 
             
            * ``Stopped`` - You have stopped the job, and the job has stopped importing users. 
             
            * ``Succeeded`` - The job has completed successfully. 
             
            * ``Failed`` - The job has stopped due to an error. 
             
            * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started. 
             

            
          

          - **CloudWatchLogsRoleArn** *(string) --* 

            The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

            
          

          - **ImportedUsers** *(integer) --* 

            The number of users that were successfully imported.

            
          

          - **SkippedUsers** *(integer) --* 

            The number of users that were skipped.

            
          

          - **FailedUsers** *(integer) --* 

            The number of users that could not be imported.

            
          

          - **CompletionMessage** *(string) --* 

            The message returned when the user import job is completed.

            
      
    

  .. py:method:: describe_user_pool(**kwargs)

    

    Returns the configuration information and metadata of the specified user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DescribeUserPool>`_    


    **Request Syntax** 
    ::

      response = client.describe_user_pool(
          UserPoolId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool you want to describe.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserPool': {
                'Id': 'string',
                'Name': 'string',
                'Policies': {
                    'PasswordPolicy': {
                        'MinimumLength': 123,
                        'RequireUppercase': True|False,
                        'RequireLowercase': True|False,
                        'RequireNumbers': True|False,
                        'RequireSymbols': True|False
                    }
                },
                'LambdaConfig': {
                    'PreSignUp': 'string',
                    'CustomMessage': 'string',
                    'PostConfirmation': 'string',
                    'PreAuthentication': 'string',
                    'PostAuthentication': 'string',
                    'DefineAuthChallenge': 'string',
                    'CreateAuthChallenge': 'string',
                    'VerifyAuthChallengeResponse': 'string',
                    'PreTokenGeneration': 'string'
                },
                'Status': 'Enabled'|'Disabled',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1),
                'SchemaAttributes': [
                    {
                        'Name': 'string',
                        'AttributeDataType': 'String'|'Number'|'DateTime'|'Boolean',
                        'DeveloperOnlyAttribute': True|False,
                        'Mutable': True|False,
                        'Required': True|False,
                        'NumberAttributeConstraints': {
                            'MinValue': 'string',
                            'MaxValue': 'string'
                        },
                        'StringAttributeConstraints': {
                            'MinLength': 'string',
                            'MaxLength': 'string'
                        }
                    },
                ],
                'AutoVerifiedAttributes': [
                    'phone_number'|'email',
                ],
                'AliasAttributes': [
                    'phone_number'|'email'|'preferred_username',
                ],
                'UsernameAttributes': [
                    'phone_number'|'email',
                ],
                'SmsVerificationMessage': 'string',
                'EmailVerificationMessage': 'string',
                'EmailVerificationSubject': 'string',
                'VerificationMessageTemplate': {
                    'SmsMessage': 'string',
                    'EmailMessage': 'string',
                    'EmailSubject': 'string',
                    'EmailMessageByLink': 'string',
                    'EmailSubjectByLink': 'string',
                    'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
                },
                'SmsAuthenticationMessage': 'string',
                'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL',
                'DeviceConfiguration': {
                    'ChallengeRequiredOnNewDevice': True|False,
                    'DeviceOnlyRememberedOnUserPrompt': True|False
                },
                'EstimatedNumberOfUsers': 123,
                'EmailConfiguration': {
                    'SourceArn': 'string',
                    'ReplyToEmailAddress': 'string'
                },
                'SmsConfiguration': {
                    'SnsCallerArn': 'string',
                    'ExternalId': 'string'
                },
                'UserPoolTags': {
                    'string': 'string'
                },
                'SmsConfigurationFailure': 'string',
                'EmailConfigurationFailure': 'string',
                'Domain': 'string',
                'AdminCreateUserConfig': {
                    'AllowAdminCreateUserOnly': True|False,
                    'UnusedAccountValidityDays': 123,
                    'InviteMessageTemplate': {
                        'SMSMessage': 'string',
                        'EmailMessage': 'string',
                        'EmailSubject': 'string'
                    }
                },
                'UserPoolAddOns': {
                    'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response to describe the user pool.

        
        

        - **UserPool** *(dict) --* 

          The container of metadata returned by the server to describe the pool.

          
          

          - **Id** *(string) --* 

            The ID of the user pool.

            
          

          - **Name** *(string) --* 

            The name of the user pool.

            
          

          - **Policies** *(dict) --* 

            The policies associated with the user pool.

            
            

            - **PasswordPolicy** *(dict) --* 

              The password policy.

              
              

              - **MinimumLength** *(integer) --* 

                The minimum length of the password policy that you have set. Cannot be less than 6.

                
              

              - **RequireUppercase** *(boolean) --* 

                In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.

                
              

              - **RequireLowercase** *(boolean) --* 

                In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.

                
              

              - **RequireNumbers** *(boolean) --* 

                In the password policy that you have set, refers to whether you have required users to use at least one number in their password.

                
              

              - **RequireSymbols** *(boolean) --* 

                In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.

                
          
        
          

          - **LambdaConfig** *(dict) --* 

            The AWS Lambda triggers associated with tue user pool.

            
            

            - **PreSignUp** *(string) --* 

              A pre-registration AWS Lambda trigger.

              
            

            - **CustomMessage** *(string) --* 

              A custom Message AWS Lambda trigger.

              
            

            - **PostConfirmation** *(string) --* 

              A post-confirmation AWS Lambda trigger.

              
            

            - **PreAuthentication** *(string) --* 

              A pre-authentication AWS Lambda trigger.

              
            

            - **PostAuthentication** *(string) --* 

              A post-authentication AWS Lambda trigger.

              
            

            - **DefineAuthChallenge** *(string) --* 

              Defines the authentication challenge.

              
            

            - **CreateAuthChallenge** *(string) --* 

              Creates an authentication challenge.

              
            

            - **VerifyAuthChallengeResponse** *(string) --* 

              Verifies the authentication challenge response.

              
            

            - **PreTokenGeneration** *(string) --* 

              A Lambda trigger that is invoked before token generation.

              
        
          

          - **Status** *(string) --* 

            The status of a user pool.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The date the user pool was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user pool was created.

            
          

          - **SchemaAttributes** *(list) --* 

            A container with the schema attributes of a user pool.

            
            

            - *(dict) --* 

              Contains information about the schema attribute.

              
              

              - **Name** *(string) --* 

                A schema attribute of the name type.

                
              

              - **AttributeDataType** *(string) --* 

                The attribute data type.

                
              

              - **DeveloperOnlyAttribute** *(boolean) --* 

                Specifies whether the attribute type is developer only.

                
              

              - **Mutable** *(boolean) --* 

                Specifies whether the attribute can be changed once it has been created.

                
              

              - **Required** *(boolean) --* 

                Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.

                
              

              - **NumberAttributeConstraints** *(dict) --* 

                Specifies the constraints for an attribute of the number type.

                
                

                - **MinValue** *(string) --* 

                  The minimum value of an attribute that is of the number data type.

                  
                

                - **MaxValue** *(string) --* 

                  The maximum value of an attribute that is of the number data type.

                  
            
              

              - **StringAttributeConstraints** *(dict) --* 

                Specifies the constraints for an attribute of the string type.

                
                

                - **MinLength** *(string) --* 

                  The minimum length.

                  
                

                - **MaxLength** *(string) --* 

                  The maximum length.

                  
            
          
        
          

          - **AutoVerifiedAttributes** *(list) --* 

            Specifies the attributes that are auto-verified in a user pool.

            
            

            - *(string) --* 
        
          

          - **AliasAttributes** *(list) --* 

            Specifies the attributes that are aliased in a user pool.

            
            

            - *(string) --* 
        
          

          - **UsernameAttributes** *(list) --* 

            Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up.

            
            

            - *(string) --* 
        
          

          - **SmsVerificationMessage** *(string) --* 

            The contents of the SMS verification message.

            
          

          - **EmailVerificationMessage** *(string) --* 

            The contents of the email verification message.

            
          

          - **EmailVerificationSubject** *(string) --* 

            The subject of the email verification message.

            
          

          - **VerificationMessageTemplate** *(dict) --* 

            The template for verification messages.

            
            

            - **SmsMessage** *(string) --* 

              The SMS message template.

              
            

            - **EmailMessage** *(string) --* 

              The email message template.

              
            

            - **EmailSubject** *(string) --* 

              The subject line for the email message template.

              
            

            - **EmailMessageByLink** *(string) --* 

              The email message template for sending a confirmation link to the user.

              
            

            - **EmailSubjectByLink** *(string) --* 

              The subject line for the email message template for sending a confirmation link to the user.

              
            

            - **DefaultEmailOption** *(string) --* 

              The default email option.

              
        
          

          - **SmsAuthenticationMessage** *(string) --* 

            The contents of the SMS authentication message.

            
          

          - **MfaConfiguration** *(string) --* 

            Can be one of the following values:

             

             
            * ``OFF`` - MFA tokens are not required and cannot be specified during user registration. 
             
            * ``ON`` - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool. 
             
            * ``OPTIONAL`` - Users have the option when registering to create an MFA token. 
             

            
          

          - **DeviceConfiguration** *(dict) --* 

            The device configuration.

            
            

            - **ChallengeRequiredOnNewDevice** *(boolean) --* 

              Indicates whether a challenge is required on a new device. Only applicable to a new device.

              
            

            - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --* 

              If true, a device is only remembered on user prompt.

              
        
          

          - **EstimatedNumberOfUsers** *(integer) --* 

            A number estimating the size of the user pool.

            
          

          - **EmailConfiguration** *(dict) --* 

            The email configuration.

            
            

            - **SourceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the email source.

              
            

            - **ReplyToEmailAddress** *(string) --* 

              The destination to which the receiver of the email should reply to.

              
        
          

          - **SmsConfiguration** *(dict) --* 

            The SMS configuration.

            
            

            - **SnsCallerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.

              
            

            - **ExternalId** *(string) --* 

              The external ID.

              
        
          

          - **UserPoolTags** *(dict) --* 

            The cost allocation tags for the user pool. For more information, see `Adding Cost Allocation Tags to Your User Pool <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-cost-allocation-tagging.html>`__  

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **SmsConfigurationFailure** *(string) --* 

            The reason why the SMS configuration cannot send the messages to your users.

            
          

          - **EmailConfigurationFailure** *(string) --* 

            The reason why the email configuration cannot send the messages to your users.

            
          

          - **Domain** *(string) --* 

            Holds the domain prefix if the user pool has a domain associated with it.

            
          

          - **AdminCreateUserConfig** *(dict) --* 

            The configuration for ``AdminCreateUser`` requests.

            
            

            - **AllowAdminCreateUserOnly** *(boolean) --* 

              Set to ``True`` if only the administrator is allowed to create user profiles. Set to ``False`` if users can sign themselves up via an app.

              
            

            - **UnusedAccountValidityDays** *(integer) --* 

              The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call ``AdminCreateUser`` again, specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this parameter is 7.

              
            

            - **InviteMessageTemplate** *(dict) --* 

              The message template to be used for the welcome message to new users.

               

              See also `Customizing User Invitation Messages <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__ .

              
              

              - **SMSMessage** *(string) --* 

                The message template for SMS messages.

                
              

              - **EmailMessage** *(string) --* 

                The message template for email messages.

                
              

              - **EmailSubject** *(string) --* 

                The subject line for email messages.

                
          
        
          

          - **UserPoolAddOns** *(dict) --* 

            The user pool add-ons.

            
            

            - **AdvancedSecurityMode** *(string) --* 

              The advanced security mode.

              
        
      
    

  .. py:method:: describe_user_pool_client(**kwargs)

    

    Client method for returning the configuration information and metadata of the specified user pool client.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DescribeUserPoolClient>`_    


    **Request Syntax** 
    ::

      response = client.describe_user_pool_client(
          UserPoolId='string',
          ClientId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool you want to describe.

      

    
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The app client ID of the app associated with the user pool.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserPoolClient': {
                'UserPoolId': 'string',
                'ClientName': 'string',
                'ClientId': 'string',
                'ClientSecret': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1),
                'RefreshTokenValidity': 123,
                'ReadAttributes': [
                    'string',
                ],
                'WriteAttributes': [
                    'string',
                ],
                'ExplicitAuthFlows': [
                    'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
                ],
                'SupportedIdentityProviders': [
                    'string',
                ],
                'CallbackURLs': [
                    'string',
                ],
                'LogoutURLs': [
                    'string',
                ],
                'DefaultRedirectURI': 'string',
                'AllowedOAuthFlows': [
                    'code'|'implicit'|'client_credentials',
                ],
                'AllowedOAuthScopes': [
                    'string',
                ],
                'AllowedOAuthFlowsUserPoolClient': True|False,
                'AnalyticsConfiguration': {
                    'ApplicationId': 'string',
                    'RoleArn': 'string',
                    'ExternalId': 'string',
                    'UserDataShared': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server from a request to describe the user pool client.

        
        

        - **UserPoolClient** *(dict) --* 

          The user pool client from a server response to describe the user pool client.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool client.

            
          

          - **ClientName** *(string) --* 

            The client name from the user pool request of the client type.

            
          

          - **ClientId** *(string) --* 

            The ID of the client associated with the user pool.

            
          

          - **ClientSecret** *(string) --* 

            The client secret from the user pool request of the client type.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The date the user pool client was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user pool client was created.

            
          

          - **RefreshTokenValidity** *(integer) --* 

            The time limit, in days, after which the refresh token is no longer valid and cannot be used.

            
          

          - **ReadAttributes** *(list) --* 

            The Read-only attributes.

            
            

            - *(string) --* 
        
          

          - **WriteAttributes** *(list) --* 

            The writeable attributes.

            
            

            - *(string) --* 
        
          

          - **ExplicitAuthFlows** *(list) --* 

            The explicit authentication flows.

            
            

            - *(string) --* 
        
          

          - **SupportedIdentityProviders** *(list) --* 

            A list of provider names for the identity providers that are supported on this client.

            
            

            - *(string) --* 
        
          

          - **CallbackURLs** *(list) --* 

            A list of allowed callback URLs for the identity providers.

            
            

            - *(string) --* 
        
          

          - **LogoutURLs** *(list) --* 

            A list of allowed logout URLs for the identity providers.

            
            

            - *(string) --* 
        
          

          - **DefaultRedirectURI** *(string) --* 

            The default redirect URI. Must be in the ``CallbackURLs`` list.

            
          

          - **AllowedOAuthFlows** *(list) --* 

            Set to ``code`` to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.

             

            Set to ``token`` to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.

            
            

            - *(string) --* 
        
          

          - **AllowedOAuthScopes** *(list) --* 

            A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` , ``"email"`` , ``"openid"`` , and ``"Cognito"`` .

            
            

            - *(string) --* 
        
          

          - **AllowedOAuthFlowsUserPoolClient** *(boolean) --* 

            Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

            
          

          - **AnalyticsConfiguration** *(dict) --* 

            The Amazon Pinpoint analytics configuration for the user pool client.

            
            

            - **ApplicationId** *(string) --* 

              The application ID for an Amazon Pinpoint application.

              
            

            - **RoleArn** *(string) --* 

              The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.

              
            

            - **ExternalId** *(string) --* 

              The external ID.

              
            

            - **UserDataShared** *(boolean) --* 

              If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.

              
        
      
    

  .. py:method:: describe_user_pool_domain(**kwargs)

    

    Gets information about a domain.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DescribeUserPoolDomain>`_    


    **Request Syntax** 
    ::

      response = client.describe_user_pool_domain(
          Domain='string'
      )
    :type Domain: string
    :param Domain: **[REQUIRED]** 

      The domain string.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DomainDescription': {
                'UserPoolId': 'string',
                'AWSAccountId': 'string',
                'Domain': 'string',
                'S3Bucket': 'string',
                'CloudFrontDistribution': 'string',
                'Version': 'string',
                'Status': 'CREATING'|'DELETING'|'UPDATING'|'ACTIVE'|'FAILED'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DomainDescription** *(dict) --* 

          A domain description object containing information about the domain.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID.

            
          

          - **AWSAccountId** *(string) --* 

            The AWS account ID for the user pool owner.

            
          

          - **Domain** *(string) --* 

            The domain string.

            
          

          - **S3Bucket** *(string) --* 

            The S3 bucket where the static files for this domain are stored.

            
          

          - **CloudFrontDistribution** *(string) --* 

            The ARN of the CloudFront distribution.

            
          

          - **Version** *(string) --* 

            The app version.

            
          

          - **Status** *(string) --* 

            The domain status.

            
      
    

  .. py:method:: forget_device(**kwargs)

    

    Forgets the specified device.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ForgetDevice>`_    


    **Request Syntax** 
    ::

      response = client.forget_device(
          AccessToken='string',
          DeviceKey='string'
      )
    :type AccessToken: string
    :param AccessToken: 

      The access token for the forgotten device request.

      

    
    :type DeviceKey: string
    :param DeviceKey: **[REQUIRED]** 

      The device key.

      

    
    
    :returns: None

  .. py:method:: forgot_password(**kwargs)

    

    Calling this API causes a message to be sent to the end user with a confirmation code that is required to change the user's password. For the ``Username`` parameter, you can use the username or user alias. If a verified phone number exists for the user, the confirmation code is sent to the phone number. Otherwise, if a verified email exists, the confirmation code is sent to the email. If neither a verified phone number nor a verified email exists, ``InvalidParameterException`` is thrown. To use the confirmation code for resetting the password, call .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ForgotPassword>`_    


    **Request Syntax** 
    ::

      response = client.forgot_password(
          ClientId='string',
          SecretHash='string',
          UserContextData={
              'EncodedData': 'string'
          },
          Username='string',
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          }
      )
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The ID of the client associated with the user pool.

      

    
    :type SecretHash: string
    :param SecretHash: 

      A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

      

    
    :type UserContextData: dict
    :param UserContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **EncodedData** *(string) --* 

        Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

        

      
    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user for whom you want to enter a code to reset a forgotten password.

      

    
    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The Amazon Pinpoint analytics metadata for collecting metrics for ``ForgotPassword`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CodeDeliveryDetails': {
                'Destination': 'string',
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Respresents the response from the server regarding the request to reset a password.

        
        

        - **CodeDeliveryDetails** *(dict) --* 

          The code delivery details returned by the server in response to the request to reset a password.

          
          

          - **Destination** *(string) --* 

            The destination for the code delivery details.

            
          

          - **DeliveryMedium** *(string) --* 

            The delivery medium (email message or phone number).

            
          

          - **AttributeName** *(string) --* 

            The attribute name.

            
      
    

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


  .. py:method:: get_csv_header(**kwargs)

    

    Gets the header information for the .csv file to be used as input for the user import job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetCSVHeader>`_    


    **Request Syntax** 
    ::

      response = client.get_csv_header(
          UserPoolId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool that the users are to be imported into.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserPoolId': 'string',
            'CSVHeader': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to the request to get the header information for the .csv file for the user import job.

        
        

        - **UserPoolId** *(string) --* 

          The user pool ID for the user pool that the users are to be imported into.

          
        

        - **CSVHeader** *(list) --* 

          The header information for the .csv file for the user import job.

          
          

          - *(string) --* 
      
    

  .. py:method:: get_device(**kwargs)

    

    Gets the device.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetDevice>`_    


    **Request Syntax** 
    ::

      response = client.get_device(
          DeviceKey='string',
          AccessToken='string'
      )
    :type DeviceKey: string
    :param DeviceKey: **[REQUIRED]** 

      The device key.

      

    
    :type AccessToken: string
    :param AccessToken: 

      The access token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Device': {
                'DeviceKey': 'string',
                'DeviceAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'DeviceCreateDate': datetime(2015, 1, 1),
                'DeviceLastModifiedDate': datetime(2015, 1, 1),
                'DeviceLastAuthenticatedDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Gets the device response.

        
        

        - **Device** *(dict) --* 

          The device.

          
          

          - **DeviceKey** *(string) --* 

            The device key.

            
          

          - **DeviceAttributes** *(list) --* 

            The device attributes.

            
            

            - *(dict) --* 

              Specifies whether the attribute is standard or custom.

              
              

              - **Name** *(string) --* 

                The name of the attribute.

                
              

              - **Value** *(string) --* 

                The value of the attribute.

                
          
        
          

          - **DeviceCreateDate** *(datetime) --* 

            The creation date of the device.

            
          

          - **DeviceLastModifiedDate** *(datetime) --* 

            The last modified date of the device.

            
          

          - **DeviceLastAuthenticatedDate** *(datetime) --* 

            The date in which the device was last authenticated.

            
      
    

  .. py:method:: get_group(**kwargs)

    

    Gets a group.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetGroup>`_    


    **Request Syntax** 
    ::

      response = client.get_group(
          GroupName='string',
          UserPoolId='string'
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the group.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Group': {
                'GroupName': 'string',
                'UserPoolId': 'string',
                'Description': 'string',
                'RoleArn': 'string',
                'Precedence': 123,
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Group** *(dict) --* 

          The group object for the group.

          
          

          - **GroupName** *(string) --* 

            The name of the group.

            
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool.

            
          

          - **Description** *(string) --* 

            A string containing the description of the group.

            
          

          - **RoleArn** *(string) --* 

            The role ARN for the group.

            
          

          - **Precedence** *(integer) --* 

            A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values or with null ``Precedence`` values.

             

            Two groups can have the same ``Precedence`` value. If this happens, neither group takes precedence over the other. If two groups with the same ``Precedence`` have the same role ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is not set in users' tokens.

             

            The default ``Precedence`` value is null.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The date the group was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the group was created.

            
      
    

  .. py:method:: get_identity_provider_by_identifier(**kwargs)

    

    Gets the specified identity provider.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetIdentityProviderByIdentifier>`_    


    **Request Syntax** 
    ::

      response = client.get_identity_provider_by_identifier(
          UserPoolId='string',
          IdpIdentifier='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type IdpIdentifier: string
    :param IdpIdentifier: **[REQUIRED]** 

      The identity provider ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityProvider': {
                'UserPoolId': 'string',
                'ProviderName': 'string',
                'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon',
                'ProviderDetails': {
                    'string': 'string'
                },
                'AttributeMapping': {
                    'string': 'string'
                },
                'IdpIdentifiers': [
                    'string',
                ],
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **IdentityProvider** *(dict) --* 

          The identity provider object.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID.

            
          

          - **ProviderName** *(string) --* 

            The identity provider name.

            
          

          - **ProviderType** *(string) --* 

            The identity provider type.

            
          

          - **ProviderDetails** *(dict) --* 

            The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **AttributeMapping** *(dict) --* 

            A mapping of identity provider attributes to standard and custom user pool attributes.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **IdpIdentifiers** *(list) --* 

            A list of identity provider identifiers.

            
            

            - *(string) --* 
        
          

          - **LastModifiedDate** *(datetime) --* 

            The date the identity provider was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the identity provider was created.

            
      
    

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


  .. py:method:: get_ui_customization(**kwargs)

    

    Gets the UI Customization information for a particular app client's app UI, if there is something set. If nothing is set for the particular client, but there is an existing pool level customization (app ``clientId`` will be ``ALL`` ), then that is returned. If nothing is present, then an empty shape is returned.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetUICustomization>`_    


    **Request Syntax** 
    ::

      response = client.get_ui_customization(
          UserPoolId='string',
          ClientId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type ClientId: string
    :param ClientId: 

      The client ID for the client app.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UICustomization': {
                'UserPoolId': 'string',
                'ClientId': 'string',
                'ImageUrl': 'string',
                'CSS': 'string',
                'CSSVersion': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UICustomization** *(dict) --* 

          The UI customization information.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool.

            
          

          - **ClientId** *(string) --* 

            The client ID for the client app.

            
          

          - **ImageUrl** *(string) --* 

            The logo image for the UI customization.

            
          

          - **CSS** *(string) --* 

            The CSS values in the UI customization.

            
          

          - **CSSVersion** *(string) --* 

            The CSS version number.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The last-modified date for the UI customization.

            
          

          - **CreationDate** *(datetime) --* 

            The creation date for the UI customization.

            
      
    

  .. py:method:: get_user(**kwargs)

    

    Gets the user attributes and metadata for a user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetUser>`_    


    **Request Syntax** 
    ::

      response = client.get_user(
          AccessToken='string'
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token returned by the server response to get information about the user.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Username': 'string',
            'UserAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'MFAOptions': [
                {
                    'DeliveryMedium': 'SMS'|'EMAIL',
                    'AttributeName': 'string'
                },
            ],
            'PreferredMfaSetting': 'string',
            'UserMFASettingList': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server from the request to get information about the user.

        
        

        - **Username** *(string) --* 

          The user name of the user you wish to retrieve from the get user request.

          
        

        - **UserAttributes** *(list) --* 

          An array of name-value pairs representing user attributes.

           

          For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

          
          

          - *(dict) --* 

            Specifies whether the attribute is standard or custom.

            
            

            - **Name** *(string) --* 

              The name of the attribute.

              
            

            - **Value** *(string) --* 

              The value of the attribute.

              
        
      
        

        - **MFAOptions** *(list) --* 

          Specifies the options for MFA (e.g., email or phone number).

          
          

          - *(dict) --* 

            Specifies the different settings for multi-factor authentication (MFA).

            
            

            - **DeliveryMedium** *(string) --* 

              The delivery medium (email message or SMS message) to send the MFA code.

              
            

            - **AttributeName** *(string) --* 

              The attribute name of the MFA option type.

              
        
      
        

        - **PreferredMfaSetting** *(string) --* 

          The user's preferred MFA setting.

          
        

        - **UserMFASettingList** *(list) --* 

          The list of the user's MFA settings.

          
          

          - *(string) --* 
      
    

  .. py:method:: get_user_attribute_verification_code(**kwargs)

    

    Gets the user attribute verification code for the specified attribute name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetUserAttributeVerificationCode>`_    


    **Request Syntax** 
    ::

      response = client.get_user_attribute_verification_code(
          AccessToken='string',
          AttributeName='string'
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token returned by the server response to get the user attribute verification code.

      

    
    :type AttributeName: string
    :param AttributeName: **[REQUIRED]** 

      The attribute name returned by the server response to get the user attribute verification code.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CodeDeliveryDetails': {
                'Destination': 'string',
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The verification code response returned by the server response to get the user attribute verification code.

        
        

        - **CodeDeliveryDetails** *(dict) --* 

          The code delivery details returned by the server in response to the request to get the user attribute verification code.

          
          

          - **Destination** *(string) --* 

            The destination for the code delivery details.

            
          

          - **DeliveryMedium** *(string) --* 

            The delivery medium (email message or phone number).

            
          

          - **AttributeName** *(string) --* 

            The attribute name.

            
      
    

  .. py:method:: get_user_pool_mfa_config(**kwargs)

    

    Gets the user pool multi-factor authentication (MFA) configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetUserPoolMfaConfig>`_    


    **Request Syntax** 
    ::

      response = client.get_user_pool_mfa_config(
          UserPoolId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SmsMfaConfiguration': {
                'SmsAuthenticationMessage': 'string',
                'SmsConfiguration': {
                    'SnsCallerArn': 'string',
                    'ExternalId': 'string'
                }
            },
            'SoftwareTokenMfaConfiguration': {
                'Enabled': True|False
            },
            'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SmsMfaConfiguration** *(dict) --* 

          The SMS text message multi-factor (MFA) configuration.

          
          

          - **SmsAuthenticationMessage** *(string) --* 

            The SMS authentication message.

            
          

          - **SmsConfiguration** *(dict) --* 

            The SMS configuration.

            
            

            - **SnsCallerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.

              
            

            - **ExternalId** *(string) --* 

              The external ID.

              
        
      
        

        - **SoftwareTokenMfaConfiguration** *(dict) --* 

          The software token multi-factor (MFA) configuration.

          
          

          - **Enabled** *(boolean) --* 

            Specifies whether software token MFA is enabled.

            
      
        

        - **MfaConfiguration** *(string) --* 

          The multi-factor (MFA) configuration.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: global_sign_out(**kwargs)

    

    Signs out users from all devices.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GlobalSignOut>`_    


    **Request Syntax** 
    ::

      response = client.global_sign_out(
          AccessToken='string'
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The response to the request to sign out all devices.

        
    

  .. py:method:: initiate_auth(**kwargs)

    

    Initiates the authentication flow.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/InitiateAuth>`_    


    **Request Syntax** 
    ::

      response = client.initiate_auth(
          AuthFlow='USER_SRP_AUTH'|'REFRESH_TOKEN_AUTH'|'REFRESH_TOKEN'|'CUSTOM_AUTH'|'ADMIN_NO_SRP_AUTH',
          AuthParameters={
              'string': 'string'
          },
          ClientMetadata={
              'string': 'string'
          },
          ClientId='string',
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          },
          UserContextData={
              'EncodedData': 'string'
          }
      )
    :type AuthFlow: string
    :param AuthFlow: **[REQUIRED]** 

      The authentication flow for this call to execute. The API action will depend on this value. For example: 

       

       
      * ``REFRESH_TOKEN_AUTH`` will take in a valid refresh token and return new tokens. 
       
      * ``USER_SRP_AUTH`` will take in ``USERNAME`` and ``SRP_A`` and return the SRP variables to be used for next challenge execution. 
       

       

      Valid values include:

       

       
      * ``USER_SRP_AUTH`` : Authentication flow for the Secure Remote Password (SRP) protocol. 
       
      * ``REFRESH_TOKEN_AUTH`` /``REFRESH_TOKEN`` : Authentication flow for refreshing the access token and ID token by supplying a valid refresh token. 
       
      * ``CUSTOM_AUTH`` : Custom authentication flow. 
       

       

       ``ADMIN_NO_SRP_AUTH`` is not a valid value.

      

    
    :type AuthParameters: dict
    :param AuthParameters: 

      The authentication parameters. These are inputs corresponding to the ``AuthFlow`` that you are invoking. The required values depend on the value of ``AuthFlow`` :

       

       
      * For ``USER_SRP_AUTH`` : ``USERNAME`` (required), ``SRP_A`` (required), ``SECRET_HASH`` (required if the app client is configured with a client secret), ``DEVICE_KEY``   
       
      * For ``REFRESH_TOKEN_AUTH/REFRESH_TOKEN`` : ``USERNAME`` (required), ``SECRET_HASH`` (required if the app client is configured with a client secret), ``REFRESH_TOKEN`` (required), ``DEVICE_KEY``   
       
      * For ``CUSTOM_AUTH`` : ``USERNAME`` (required), ``SECRET_HASH`` (if app client is configured with client secret), ``DEVICE_KEY``   
       

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type ClientMetadata: dict
    :param ClientMetadata: 

      This is a random key-value pair map which can contain any key and will be passed to your PreAuthentication Lambda trigger as-is. It can be used to implement additional validations around authentication.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The app client ID.

      

    
    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The Amazon Pinpoint analytics metadata for collecting metrics for ``InitiateAuth`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    :type UserContextData: dict
    :param UserContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **EncodedData** *(string) --* 

        Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
            'Session': 'string',
            'ChallengeParameters': {
                'string': 'string'
            },
            'AuthenticationResult': {
                'AccessToken': 'string',
                'ExpiresIn': 123,
                'TokenType': 'string',
                'RefreshToken': 'string',
                'IdToken': 'string',
                'NewDeviceMetadata': {
                    'DeviceKey': 'string',
                    'DeviceGroupKey': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Initiates the authentication response.

        
        

        - **ChallengeName** *(string) --* 

          The name of the challenge which you are responding to with this call. This is returned to you in the ``AdminInitiateAuth`` response if you need to pass another challenge.

           

          Valid values include the following. Note that all of these challenges require ``USERNAME`` and ``SECRET_HASH`` (if applicable) in the parameters.

           

           
          * ``SMS_MFA`` : Next challenge is to supply an ``SMS_MFA_CODE`` , delivered via SMS. 
           
          * ``PASSWORD_VERIFIER`` : Next challenge is to supply ``PASSWORD_CLAIM_SIGNATURE`` , ``PASSWORD_CLAIM_SECRET_BLOCK`` , and ``TIMESTAMP`` after the client-side SRP calculations. 
           
          * ``CUSTOM_CHALLENGE`` : This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued. 
           
          * ``DEVICE_SRP_AUTH`` : If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device. 
           
          * ``DEVICE_PASSWORD_VERIFIER`` : Similar to ``PASSWORD_VERIFIER`` , but for devices only. 
           
          * ``NEW_PASSWORD_REQUIRED`` : For users which are required to change their passwords after successful first login. This challenge should be passed with ``NEW_PASSWORD`` and any other required attributes. 
           

          
        

        - **Session** *(string) --* 

          The session which should be passed both ways in challenge-response calls to the service. If the or API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next ``RespondToAuthChallenge`` API call.

          
        

        - **ChallengeParameters** *(dict) --* 

          The challenge parameters. These are returned to you in the ``InitiateAuth`` response if you need to pass another challenge. The responses in this parameter should be used to compute inputs to the next call (``RespondToAuthChallenge`` ). 

           

          All challenges require ``USERNAME`` and ``SECRET_HASH`` (if applicable).

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **AuthenticationResult** *(dict) --* 

          The result of the authentication response. This is only returned if the caller does not need to pass another challenge. If the caller does need to pass another challenge before it gets tokens, ``ChallengeName`` , ``ChallengeParameters`` , and ``Session`` are returned.

          
          

          - **AccessToken** *(string) --* 

            The access token.

            
          

          - **ExpiresIn** *(integer) --* 

            The expiration period of the authentication result.

            
          

          - **TokenType** *(string) --* 

            The token type.

            
          

          - **RefreshToken** *(string) --* 

            The refresh token.

            
          

          - **IdToken** *(string) --* 

            The ID token.

            
          

          - **NewDeviceMetadata** *(dict) --* 

            The new device metadata from an authentication result.

            
            

            - **DeviceKey** *(string) --* 

              The device key.

              
            

            - **DeviceGroupKey** *(string) --* 

              The device group key.

              
        
      
    

  .. py:method:: list_devices(**kwargs)

    

    Lists the devices.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListDevices>`_    


    **Request Syntax** 
    ::

      response = client.list_devices(
          AccessToken='string',
          Limit=123,
          PaginationToken='string'
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access tokens for the request to list devices.

      

    
    :type Limit: integer
    :param Limit: 

      The limit of the device request.

      

    
    :type PaginationToken: string
    :param PaginationToken: 

      The pagination token for the list request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Devices': [
                {
                    'DeviceKey': 'string',
                    'DeviceAttributes': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'DeviceCreateDate': datetime(2015, 1, 1),
                    'DeviceLastModifiedDate': datetime(2015, 1, 1),
                    'DeviceLastAuthenticatedDate': datetime(2015, 1, 1)
                },
            ],
            'PaginationToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response to list devices.

        
        

        - **Devices** *(list) --* 

          The devices returned in the list devices response.

          
          

          - *(dict) --* 

            The device type.

            
            

            - **DeviceKey** *(string) --* 

              The device key.

              
            

            - **DeviceAttributes** *(list) --* 

              The device attributes.

              
              

              - *(dict) --* 

                Specifies whether the attribute is standard or custom.

                
                

                - **Name** *(string) --* 

                  The name of the attribute.

                  
                

                - **Value** *(string) --* 

                  The value of the attribute.

                  
            
          
            

            - **DeviceCreateDate** *(datetime) --* 

              The creation date of the device.

              
            

            - **DeviceLastModifiedDate** *(datetime) --* 

              The last modified date of the device.

              
            

            - **DeviceLastAuthenticatedDate** *(datetime) --* 

              The date in which the device was last authenticated.

              
        
      
        

        - **PaginationToken** *(string) --* 

          The pagination token for the list device response.

          
    

  .. py:method:: list_groups(**kwargs)

    

    Lists the groups associated with a user pool.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListGroups>`_    


    **Request Syntax** 
    ::

      response = client.list_groups(
          UserPoolId='string',
          Limit=123,
          NextToken='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type Limit: integer
    :param Limit: 

      The limit of the request to list groups.

      

    
    :type NextToken: string
    :param NextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Groups': [
                {
                    'GroupName': 'string',
                    'UserPoolId': 'string',
                    'Description': 'string',
                    'RoleArn': 'string',
                    'Precedence': 123,
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'CreationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Groups** *(list) --* 

          The group objects for the groups.

          
          

          - *(dict) --* 

            The group type.

            
            

            - **GroupName** *(string) --* 

              The name of the group.

              
            

            - **UserPoolId** *(string) --* 

              The user pool ID for the user pool.

              
            

            - **Description** *(string) --* 

              A string containing the description of the group.

              
            

            - **RoleArn** *(string) --* 

              The role ARN for the group.

              
            

            - **Precedence** *(integer) --* 

              A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values or with null ``Precedence`` values.

               

              Two groups can have the same ``Precedence`` value. If this happens, neither group takes precedence over the other. If two groups with the same ``Precedence`` have the same role ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is not set in users' tokens.

               

              The default ``Precedence`` value is null.

              
            

            - **LastModifiedDate** *(datetime) --* 

              The date the group was last modified.

              
            

            - **CreationDate** *(datetime) --* 

              The date the group was created.

              
        
      
        

        - **NextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

  .. py:method:: list_identity_providers(**kwargs)

    

    Lists information about all identity providers for a user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListIdentityProviders>`_    


    **Request Syntax** 
    ::

      response = client.list_identity_providers(
          UserPoolId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of identity providers to return.

      

    
    :type NextToken: string
    :param NextToken: 

      A pagination token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Providers': [
                {
                    'ProviderName': 'string',
                    'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon',
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'CreationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Providers** *(list) --* 

          A list of identity provider objects.

          
          

          - *(dict) --* 

            A container for identity provider details.

            
            

            - **ProviderName** *(string) --* 

              The identity provider name.

              
            

            - **ProviderType** *(string) --* 

              The identity provider type.

              
            

            - **LastModifiedDate** *(datetime) --* 

              The date the provider was last modified.

              
            

            - **CreationDate** *(datetime) --* 

              The date the provider was added to the user pool.

              
        
      
        

        - **NextToken** *(string) --* 

          A pagination token.

          
    

  .. py:method:: list_resource_servers(**kwargs)

    

    Lists the resource servers for a user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListResourceServers>`_    


    **Request Syntax** 
    ::

      response = client.list_resource_servers(
          UserPoolId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of resource servers to return.

      

    
    :type NextToken: string
    :param NextToken: 

      A pagination token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceServers': [
                {
                    'UserPoolId': 'string',
                    'Identifier': 'string',
                    'Name': 'string',
                    'Scopes': [
                        {
                            'ScopeName': 'string',
                            'ScopeDescription': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceServers** *(list) --* 

          The resource servers.

          
          

          - *(dict) --* 

            A container for information about a resource server for a user pool.

            
            

            - **UserPoolId** *(string) --* 

              The user pool ID for the user pool that hosts the resource server.

              
            

            - **Identifier** *(string) --* 

              The identifier for the resource server.

              
            

            - **Name** *(string) --* 

              The name of the resource server.

              
            

            - **Scopes** *(list) --* 

              A list of scopes that are defined for the resource server.

              
              

              - *(dict) --* 

                A resource server scope.

                
                

                - **ScopeName** *(string) --* 

                  The name of the scope.

                  
                

                - **ScopeDescription** *(string) --* 

                  A description of the scope.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A pagination token.

          
    

  .. py:method:: list_user_import_jobs(**kwargs)

    

    Lists the user import jobs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUserImportJobs>`_    


    **Request Syntax** 
    ::

      response = client.list_user_import_jobs(
          UserPoolId='string',
          MaxResults=123,
          PaginationToken='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool that the users are being imported into.

      

    
    :type MaxResults: integer
    :param MaxResults: **[REQUIRED]** 

      The maximum number of import jobs you want the request to return.

      

    
    :type PaginationToken: string
    :param PaginationToken: 

      An identifier that was returned from the previous call to ``ListUserImportJobs`` , which can be used to return the next set of import jobs in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserImportJobs': [
                {
                    'JobName': 'string',
                    'JobId': 'string',
                    'UserPoolId': 'string',
                    'PreSignedUrl': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'StartDate': datetime(2015, 1, 1),
                    'CompletionDate': datetime(2015, 1, 1),
                    'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
                    'CloudWatchLogsRoleArn': 'string',
                    'ImportedUsers': 123,
                    'SkippedUsers': 123,
                    'FailedUsers': 123,
                    'CompletionMessage': 'string'
                },
            ],
            'PaginationToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to the request to list the user import jobs.

        
        

        - **UserImportJobs** *(list) --* 

          The user import jobs.

          
          

          - *(dict) --* 

            The user import job type.

            
            

            - **JobName** *(string) --* 

              The job name for the user import job.

              
            

            - **JobId** *(string) --* 

              The job ID for the user import job.

              
            

            - **UserPoolId** *(string) --* 

              The user pool ID for the user pool that the users are being imported into.

              
            

            - **PreSignedUrl** *(string) --* 

              The pre-signed URL to be used to upload the ``.csv`` file.

              
            

            - **CreationDate** *(datetime) --* 

              The date the user import job was created.

              
            

            - **StartDate** *(datetime) --* 

              The date when the user import job was started.

              
            

            - **CompletionDate** *(datetime) --* 

              The date when the user import job was completed.

              
            

            - **Status** *(string) --* 

              The status of the user import job. One of the following:

               

               
              * ``Created`` - The job was created but not started. 
               
              * ``Pending`` - A transition state. You have started the job, but it has not begun importing users yet. 
               
              * ``InProgress`` - The job has started, and users are being imported. 
               
              * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet. 
               
              * ``Stopped`` - You have stopped the job, and the job has stopped importing users. 
               
              * ``Succeeded`` - The job has completed successfully. 
               
              * ``Failed`` - The job has stopped due to an error. 
               
              * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started. 
               

              
            

            - **CloudWatchLogsRoleArn** *(string) --* 

              The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

              
            

            - **ImportedUsers** *(integer) --* 

              The number of users that were successfully imported.

              
            

            - **SkippedUsers** *(integer) --* 

              The number of users that were skipped.

              
            

            - **FailedUsers** *(integer) --* 

              The number of users that could not be imported.

              
            

            - **CompletionMessage** *(string) --* 

              The message returned when the user import job is completed.

              
        
      
        

        - **PaginationToken** *(string) --* 

          An identifier that can be used to return the next set of user import jobs in the list.

          
    

  .. py:method:: list_user_pool_clients(**kwargs)

    

    Lists the clients that have been created for the specified user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUserPoolClients>`_    


    **Request Syntax** 
    ::

      response = client.list_user_pool_clients(
          UserPoolId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to list user pool clients.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results you want the request to return when listing the user pool clients.

      

    
    :type NextToken: string
    :param NextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserPoolClients': [
                {
                    'ClientId': 'string',
                    'UserPoolId': 'string',
                    'ClientName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server that lists user pool clients.

        
        

        - **UserPoolClients** *(list) --* 

          The user pool clients in the response that lists user pool clients.

          
          

          - *(dict) --* 

            The description of the user pool client.

            
            

            - **ClientId** *(string) --* 

              The ID of the client associated with the user pool.

              
            

            - **UserPoolId** *(string) --* 

              The user pool ID for the user pool where you want to describe the user pool client.

              
            

            - **ClientName** *(string) --* 

              The client name from the user pool client description.

              
        
      
        

        - **NextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

  .. py:method:: list_user_pools(**kwargs)

    

    Lists the user pools associated with an AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUserPools>`_    


    **Request Syntax** 
    ::

      response = client.list_user_pools(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    :type MaxResults: integer
    :param MaxResults: **[REQUIRED]** 

      The maximum number of results you want the request to return when listing the user pools.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserPools': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'LambdaConfig': {
                        'PreSignUp': 'string',
                        'CustomMessage': 'string',
                        'PostConfirmation': 'string',
                        'PreAuthentication': 'string',
                        'PostAuthentication': 'string',
                        'DefineAuthChallenge': 'string',
                        'CreateAuthChallenge': 'string',
                        'VerifyAuthChallengeResponse': 'string',
                        'PreTokenGeneration': 'string'
                    },
                    'Status': 'Enabled'|'Disabled',
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'CreationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response to list user pools.

        
        

        - **UserPools** *(list) --* 

          The user pools from the response to list users.

          
          

          - *(dict) --* 

            A user pool description.

            
            

            - **Id** *(string) --* 

              The ID in a user pool description.

              
            

            - **Name** *(string) --* 

              The name in a user pool description.

              
            

            - **LambdaConfig** *(dict) --* 

              The AWS Lambda configuration information in a user pool description.

              
              

              - **PreSignUp** *(string) --* 

                A pre-registration AWS Lambda trigger.

                
              

              - **CustomMessage** *(string) --* 

                A custom Message AWS Lambda trigger.

                
              

              - **PostConfirmation** *(string) --* 

                A post-confirmation AWS Lambda trigger.

                
              

              - **PreAuthentication** *(string) --* 

                A pre-authentication AWS Lambda trigger.

                
              

              - **PostAuthentication** *(string) --* 

                A post-authentication AWS Lambda trigger.

                
              

              - **DefineAuthChallenge** *(string) --* 

                Defines the authentication challenge.

                
              

              - **CreateAuthChallenge** *(string) --* 

                Creates an authentication challenge.

                
              

              - **VerifyAuthChallengeResponse** *(string) --* 

                Verifies the authentication challenge response.

                
              

              - **PreTokenGeneration** *(string) --* 

                A Lambda trigger that is invoked before token generation.

                
          
            

            - **Status** *(string) --* 

              The user pool status in a user pool description.

              
            

            - **LastModifiedDate** *(datetime) --* 

              The date the user pool description was last modified.

              
            

            - **CreationDate** *(datetime) --* 

              The date the user pool description was created.

              
        
      
        

        - **NextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

  .. py:method:: list_users(**kwargs)

    

    Lists the users in the Amazon Cognito user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUsers>`_    


    **Request Syntax** 
    ::

      response = client.list_users(
          UserPoolId='string',
          AttributesToGet=[
              'string',
          ],
          Limit=123,
          PaginationToken='string',
          Filter='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool on which the search should be performed.

      

    
    :type AttributesToGet: list
    :param AttributesToGet: 

      An array of strings, where each string is the name of a user attribute to be returned for each user in the search results. If the array is null, all attributes are returned.

      

    
      - *(string) --* 

      
  
    :type Limit: integer
    :param Limit: 

      Maximum number of users to be returned.

      

    
    :type PaginationToken: string
    :param PaginationToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    :type Filter: string
    :param Filter: 

      A filter string of the form "*AttributeName*  *Filter-Type* "*AttributeValue* "". Quotation marks within the filter string must be escaped using the backslash (\) character. For example, "``family_name`` = \"Reddy\"".

       

       
      * *AttributeName* : The name of the attribute to search for. You can only search for one attribute at a time. 
       
      * *Filter-Type* : For an exact match, use =, for example, "``given_name`` = \"Jon\"". For a prefix ("starts with") match, use ^=, for example, "``given_name`` ^= \"Jon\"".  
       
      * *AttributeValue* : The attribute value that must be matched for each user. 
       

       

      If the filter string is empty, ``ListUsers`` returns all users in the user pool.

       

      You can only search for the following standard attributes:

       

       
      * ``username`` (case-sensitive) 
       
      * ``email``   
       
      * ``phone_number``   
       
      * ``name``   
       
      * ``given_name``   
       
      * ``family_name``   
       
      * ``preferred_username``   
       
      * ``cognito:user_status`` (called **Enabled** in the Console) (case-sensitive) 
       
      * ``status`` (case-insensitive) 
       
      * ``sub``   
       

       

      Custom attributes are not searchable.

       

      For more information, see `Searching for Users Using the ListUsers API <http://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html#cognito-user-pools-searching-for-users-using-listusers-api>`__ and `Examples of Using the ListUsers API <http://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html#cognito-user-pools-searching-for-users-listusers-api-examples>`__ in the *Amazon Cognito Developer Guide* .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Users': [
                {
                    'Username': 'string',
                    'Attributes': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'UserCreateDate': datetime(2015, 1, 1),
                    'UserLastModifiedDate': datetime(2015, 1, 1),
                    'Enabled': True|False,
                    'UserStatus': 'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'|'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
                    'MFAOptions': [
                        {
                            'DeliveryMedium': 'SMS'|'EMAIL',
                            'AttributeName': 'string'
                        },
                    ]
                },
            ],
            'PaginationToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response from the request to list users.

        
        

        - **Users** *(list) --* 

          The users returned in the request to list users.

          
          

          - *(dict) --* 

            The user type.

            
            

            - **Username** *(string) --* 

              The user name of the user you wish to describe.

              
            

            - **Attributes** *(list) --* 

              A container with information about the user type attributes.

              
              

              - *(dict) --* 

                Specifies whether the attribute is standard or custom.

                
                

                - **Name** *(string) --* 

                  The name of the attribute.

                  
                

                - **Value** *(string) --* 

                  The value of the attribute.

                  
            
          
            

            - **UserCreateDate** *(datetime) --* 

              The creation date of the user.

              
            

            - **UserLastModifiedDate** *(datetime) --* 

              The last modified date of the user.

              
            

            - **Enabled** *(boolean) --* 

              Specifies whether the user is enabled.

              
            

            - **UserStatus** *(string) --* 

              The user status. Can be one of the following:

               

               
              * UNCONFIRMED - User has been created but not confirmed. 
               
              * CONFIRMED - User has been confirmed. 
               
              * ARCHIVED - User is no longer active. 
               
              * COMPROMISED - User is disabled due to a potential security threat. 
               
              * UNKNOWN - User status is not known. 
               

              
            

            - **MFAOptions** *(list) --* 

              The MFA options for the user.

              
              

              - *(dict) --* 

                Specifies the different settings for multi-factor authentication (MFA).

                
                

                - **DeliveryMedium** *(string) --* 

                  The delivery medium (email message or SMS message) to send the MFA code.

                  
                

                - **AttributeName** *(string) --* 

                  The attribute name of the MFA option type.

                  
            
          
        
      
        

        - **PaginationToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

  .. py:method:: list_users_in_group(**kwargs)

    

    Lists the users in the specified group.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUsersInGroup>`_    


    **Request Syntax** 
    ::

      response = client.list_users_in_group(
          UserPoolId='string',
          GroupName='string',
          Limit=123,
          NextToken='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the group.

      

    
    :type Limit: integer
    :param Limit: 

      The limit of the request to list users.

      

    
    :type NextToken: string
    :param NextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Users': [
                {
                    'Username': 'string',
                    'Attributes': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'UserCreateDate': datetime(2015, 1, 1),
                    'UserLastModifiedDate': datetime(2015, 1, 1),
                    'Enabled': True|False,
                    'UserStatus': 'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'|'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
                    'MFAOptions': [
                        {
                            'DeliveryMedium': 'SMS'|'EMAIL',
                            'AttributeName': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Users** *(list) --* 

          The users returned in the request to list users.

          
          

          - *(dict) --* 

            The user type.

            
            

            - **Username** *(string) --* 

              The user name of the user you wish to describe.

              
            

            - **Attributes** *(list) --* 

              A container with information about the user type attributes.

              
              

              - *(dict) --* 

                Specifies whether the attribute is standard or custom.

                
                

                - **Name** *(string) --* 

                  The name of the attribute.

                  
                

                - **Value** *(string) --* 

                  The value of the attribute.

                  
            
          
            

            - **UserCreateDate** *(datetime) --* 

              The creation date of the user.

              
            

            - **UserLastModifiedDate** *(datetime) --* 

              The last modified date of the user.

              
            

            - **Enabled** *(boolean) --* 

              Specifies whether the user is enabled.

              
            

            - **UserStatus** *(string) --* 

              The user status. Can be one of the following:

               

               
              * UNCONFIRMED - User has been created but not confirmed. 
               
              * CONFIRMED - User has been confirmed. 
               
              * ARCHIVED - User is no longer active. 
               
              * COMPROMISED - User is disabled due to a potential security threat. 
               
              * UNKNOWN - User status is not known. 
               

              
            

            - **MFAOptions** *(list) --* 

              The MFA options for the user.

              
              

              - *(dict) --* 

                Specifies the different settings for multi-factor authentication (MFA).

                
                

                - **DeliveryMedium** *(string) --* 

                  The delivery medium (email message or SMS message) to send the MFA code.

                  
                

                - **AttributeName** *(string) --* 

                  The attribute name of the MFA option type.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

  .. py:method:: resend_confirmation_code(**kwargs)

    

    Resends the confirmation (for confirmation of registration) to a specific user in the user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ResendConfirmationCode>`_    


    **Request Syntax** 
    ::

      response = client.resend_confirmation_code(
          ClientId='string',
          SecretHash='string',
          UserContextData={
              'EncodedData': 'string'
          },
          Username='string',
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          }
      )
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The ID of the client associated with the user pool.

      

    
    :type SecretHash: string
    :param SecretHash: 

      A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

      

    
    :type UserContextData: dict
    :param UserContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **EncodedData** *(string) --* 

        Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

        

      
    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user to whom you wish to resend a confirmation code.

      

    
    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The Amazon Pinpoint analytics metadata for collecting metrics for ``ResendConfirmationCode`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CodeDeliveryDetails': {
                'Destination': 'string',
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response from the server when the Amazon Cognito Your User Pools service makes the request to resend a confirmation code.

        
        

        - **CodeDeliveryDetails** *(dict) --* 

          The code delivery details returned by the server in response to the request to resend the confirmation code.

          
          

          - **Destination** *(string) --* 

            The destination for the code delivery details.

            
          

          - **DeliveryMedium** *(string) --* 

            The delivery medium (email message or phone number).

            
          

          - **AttributeName** *(string) --* 

            The attribute name.

            
      
    

  .. py:method:: respond_to_auth_challenge(**kwargs)

    

    Responds to the authentication challenge.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/RespondToAuthChallenge>`_    


    **Request Syntax** 
    ::

      response = client.respond_to_auth_challenge(
          ClientId='string',
          ChallengeName='SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
          Session='string',
          ChallengeResponses={
              'string': 'string'
          },
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          },
          UserContextData={
              'EncodedData': 'string'
          }
      )
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The app client ID.

      

    
    :type ChallengeName: string
    :param ChallengeName: **[REQUIRED]** 

      The challenge name. For more information, see .

       

       ``ADMIN_NO_SRP_AUTH`` is not a valid value.

      

    
    :type Session: string
    :param Session: 

      The session which should be passed both ways in challenge-response calls to the service. If ``InitiateAuth`` or ``RespondToAuthChallenge`` API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next ``RespondToAuthChallenge`` API call.

      

    
    :type ChallengeResponses: dict
    :param ChallengeResponses: 

      The challenge responses. These are inputs corresponding to the value of ``ChallengeName`` , for example:

       

       
      * ``SMS_MFA`` : ``SMS_MFA_CODE`` , ``USERNAME`` , ``SECRET_HASH`` (if app client is configured with client secret). 
       
      * ``PASSWORD_VERIFIER`` : ``PASSWORD_CLAIM_SIGNATURE`` , ``PASSWORD_CLAIM_SECRET_BLOCK`` , ``TIMESTAMP`` , ``USERNAME`` , ``SECRET_HASH`` (if app client is configured with client secret). 
       
      * ``NEW_PASSWORD_REQUIRED`` : ``NEW_PASSWORD`` , any other required attributes, ``USERNAME`` , ``SECRET_HASH`` (if app client is configured with client secret).  
       

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The Amazon Pinpoint analytics metadata for collecting metrics for ``RespondToAuthChallenge`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    :type UserContextData: dict
    :param UserContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **EncodedData** *(string) --* 

        Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
            'Session': 'string',
            'ChallengeParameters': {
                'string': 'string'
            },
            'AuthenticationResult': {
                'AccessToken': 'string',
                'ExpiresIn': 123,
                'TokenType': 'string',
                'RefreshToken': 'string',
                'IdToken': 'string',
                'NewDeviceMetadata': {
                    'DeviceKey': 'string',
                    'DeviceGroupKey': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to respond to the authentication challenge.

        
        

        - **ChallengeName** *(string) --* 

          The challenge name. For more information, see .

          
        

        - **Session** *(string) --* 

          The session which should be passed both ways in challenge-response calls to the service. If the or API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next ``RespondToAuthChallenge`` API call.

          
        

        - **ChallengeParameters** *(dict) --* 

          The challenge parameters. For more information, see .

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **AuthenticationResult** *(dict) --* 

          The result returned by the server in response to the request to respond to the authentication challenge.

          
          

          - **AccessToken** *(string) --* 

            The access token.

            
          

          - **ExpiresIn** *(integer) --* 

            The expiration period of the authentication result.

            
          

          - **TokenType** *(string) --* 

            The token type.

            
          

          - **RefreshToken** *(string) --* 

            The refresh token.

            
          

          - **IdToken** *(string) --* 

            The ID token.

            
          

          - **NewDeviceMetadata** *(dict) --* 

            The new device metadata from an authentication result.

            
            

            - **DeviceKey** *(string) --* 

              The device key.

              
            

            - **DeviceGroupKey** *(string) --* 

              The device group key.

              
        
      
    

  .. py:method:: set_risk_configuration(**kwargs)

    

    Configures actions on detected risks. To delete the risk configuration for ``UserPoolId`` or ``ClientId`` , pass null values for all four configuration types.

     

    To enable Amazon Cognito advanced security features, update the user pool to include the ``UserPoolAddOns`` key``AdvancedSecurityMode`` .

     

    See .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SetRiskConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.set_risk_configuration(
          UserPoolId='string',
          ClientId='string',
          CompromisedCredentialsRiskConfiguration={
              'EventFilter': [
                  'SIGN_IN'|'PASSWORD_CHANGE'|'SIGN_UP',
              ],
              'Actions': {
                  'EventAction': 'BLOCK'|'NO_ACTION'
              }
          },
          AccountTakeoverRiskConfiguration={
              'NotifyConfiguration': {
                  'From': 'string',
                  'ReplyTo': 'string',
                  'SourceArn': 'string',
                  'BlockEmail': {
                      'Subject': 'string',
                      'HtmlBody': 'string',
                      'TextBody': 'string'
                  },
                  'NoActionEmail': {
                      'Subject': 'string',
                      'HtmlBody': 'string',
                      'TextBody': 'string'
                  },
                  'MfaEmail': {
                      'Subject': 'string',
                      'HtmlBody': 'string',
                      'TextBody': 'string'
                  }
              },
              'Actions': {
                  'LowAction': {
                      'Notify': True|False,
                      'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                  },
                  'MediumAction': {
                      'Notify': True|False,
                      'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                  },
                  'HighAction': {
                      'Notify': True|False,
                      'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                  }
              }
          },
          RiskExceptionConfiguration={
              'BlockedIPRangeList': [
                  'string',
              ],
              'SkippedIPRangeList': [
                  'string',
              ]
          }
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID. 

      

    
    :type ClientId: string
    :param ClientId: 

      The app client ID. If ``ClientId`` is null, then the risk configuration is mapped to ``userPoolId`` . When the client ID is null, the same risk configuration is applied to all the clients in the userPool.

       

      Otherwise, ``ClientId`` is mapped to the client. When the client ID is not null, the user pool configuration is overridden and the risk configuration for the client is used instead.

      

    
    :type CompromisedCredentialsRiskConfiguration: dict
    :param CompromisedCredentialsRiskConfiguration: 

      The compromised credentials risk configuration.

      

    
      - **EventFilter** *(list) --* 

        Perform the action for these events. The default is to perform all events if no event filter is specified.

        

      
        - *(string) --* 

        
    
      - **Actions** *(dict) --* **[REQUIRED]** 

        The compromised credentials risk configuration actions.

        

      
        - **EventAction** *(string) --* **[REQUIRED]** 

          The event action.

          

        
      
    
    :type AccountTakeoverRiskConfiguration: dict
    :param AccountTakeoverRiskConfiguration: 

      The account takeover risk configuration.

      

    
      - **NotifyConfiguration** *(dict) --* 

        The notify configuration used to construct email notifications.

        

      
        - **From** *(string) --* 

          The email address that is sending the email. It must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

          

        
        - **ReplyTo** *(string) --* 

          The destination to which the receiver of an email should reply to.

          

        
        - **SourceArn** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. It permits Amazon Cognito to send for the email address specified in the ``From`` parameter.

          

        
        - **BlockEmail** *(dict) --* 

          Email template used when a detected risk event is blocked.

          

        
          - **Subject** *(string) --* **[REQUIRED]** 

            The subject.

            

          
          - **HtmlBody** *(string) --* 

            The HTML body.

            

          
          - **TextBody** *(string) --* 

            The text body.

            

          
        
        - **NoActionEmail** *(dict) --* 

          The email template used when a detected risk event is allowed.

          

        
          - **Subject** *(string) --* **[REQUIRED]** 

            The subject.

            

          
          - **HtmlBody** *(string) --* 

            The HTML body.

            

          
          - **TextBody** *(string) --* 

            The text body.

            

          
        
        - **MfaEmail** *(dict) --* 

          The MFA email template used when MFA is challenged as part of a detected risk.

          

        
          - **Subject** *(string) --* **[REQUIRED]** 

            The subject.

            

          
          - **HtmlBody** *(string) --* 

            The HTML body.

            

          
          - **TextBody** *(string) --* 

            The text body.

            

          
        
      
      - **Actions** *(dict) --* **[REQUIRED]** 

        Account takeover risk configuration actions

        

      
        - **LowAction** *(dict) --* 

          Action to take for a low risk.

          

        
          - **Notify** *(boolean) --* **[REQUIRED]** 

            Flag specifying whether to send a notification.

            

          
          - **EventAction** *(string) --* **[REQUIRED]** 

            The event action.

             

             
            * ``BLOCK`` Choosing this action will block the request. 
             
            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
             
            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
             
            * ``NO_ACTION`` Allow the user sign-in. 
             

            

          
        
        - **MediumAction** *(dict) --* 

          Action to take for a medium risk.

          

        
          - **Notify** *(boolean) --* **[REQUIRED]** 

            Flag specifying whether to send a notification.

            

          
          - **EventAction** *(string) --* **[REQUIRED]** 

            The event action.

             

             
            * ``BLOCK`` Choosing this action will block the request. 
             
            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
             
            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
             
            * ``NO_ACTION`` Allow the user sign-in. 
             

            

          
        
        - **HighAction** *(dict) --* 

          Action to take for a high risk.

          

        
          - **Notify** *(boolean) --* **[REQUIRED]** 

            Flag specifying whether to send a notification.

            

          
          - **EventAction** *(string) --* **[REQUIRED]** 

            The event action.

             

             
            * ``BLOCK`` Choosing this action will block the request. 
             
            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
             
            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
             
            * ``NO_ACTION`` Allow the user sign-in. 
             

            

          
        
      
    
    :type RiskExceptionConfiguration: dict
    :param RiskExceptionConfiguration: 

      The configuration to override the risk decision.

      

    
      - **BlockedIPRangeList** *(list) --* 

        Overrides the risk decision to always block the pre-authentication requests. The IP range is in CIDR notation: a compact representation of an IP address and its associated routing prefix.

        

      
        - *(string) --* 

        
    
      - **SkippedIPRangeList** *(list) --* 

        Risk detection is not performed on the IP addresses in the range list. The IP range is in CIDR notation.

        

      
        - *(string) --* 

        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RiskConfiguration': {
                'UserPoolId': 'string',
                'ClientId': 'string',
                'CompromisedCredentialsRiskConfiguration': {
                    'EventFilter': [
                        'SIGN_IN'|'PASSWORD_CHANGE'|'SIGN_UP',
                    ],
                    'Actions': {
                        'EventAction': 'BLOCK'|'NO_ACTION'
                    }
                },
                'AccountTakeoverRiskConfiguration': {
                    'NotifyConfiguration': {
                        'From': 'string',
                        'ReplyTo': 'string',
                        'SourceArn': 'string',
                        'BlockEmail': {
                            'Subject': 'string',
                            'HtmlBody': 'string',
                            'TextBody': 'string'
                        },
                        'NoActionEmail': {
                            'Subject': 'string',
                            'HtmlBody': 'string',
                            'TextBody': 'string'
                        },
                        'MfaEmail': {
                            'Subject': 'string',
                            'HtmlBody': 'string',
                            'TextBody': 'string'
                        }
                    },
                    'Actions': {
                        'LowAction': {
                            'Notify': True|False,
                            'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                        },
                        'MediumAction': {
                            'Notify': True|False,
                            'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                        },
                        'HighAction': {
                            'Notify': True|False,
                            'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                        }
                    }
                },
                'RiskExceptionConfiguration': {
                    'BlockedIPRangeList': [
                        'string',
                    ],
                    'SkippedIPRangeList': [
                        'string',
                    ]
                },
                'LastModifiedDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RiskConfiguration** *(dict) --* 

          The risk configuration.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID.

            
          

          - **ClientId** *(string) --* 

            The app client ID.

            
          

          - **CompromisedCredentialsRiskConfiguration** *(dict) --* 

            The compromised credentials risk configuration object including the ``EventFilter`` and the ``EventAction``  

            
            

            - **EventFilter** *(list) --* 

              Perform the action for these events. The default is to perform all events if no event filter is specified.

              
              

              - *(string) --* 
          
            

            - **Actions** *(dict) --* 

              The compromised credentials risk configuration actions.

              
              

              - **EventAction** *(string) --* 

                The event action.

                
          
        
          

          - **AccountTakeoverRiskConfiguration** *(dict) --* 

            The account takeover risk configuration object including the ``NotifyConfiguration`` object and ``Actions`` to take in the case of an account takeover.

            
            

            - **NotifyConfiguration** *(dict) --* 

              The notify configuration used to construct email notifications.

              
              

              - **From** *(string) --* 

                The email address that is sending the email. It must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

                
              

              - **ReplyTo** *(string) --* 

                The destination to which the receiver of an email should reply to.

                
              

              - **SourceArn** *(string) --* 

                The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. It permits Amazon Cognito to send for the email address specified in the ``From`` parameter.

                
              

              - **BlockEmail** *(dict) --* 

                Email template used when a detected risk event is blocked.

                
                

                - **Subject** *(string) --* 

                  The subject.

                  
                

                - **HtmlBody** *(string) --* 

                  The HTML body.

                  
                

                - **TextBody** *(string) --* 

                  The text body.

                  
            
              

              - **NoActionEmail** *(dict) --* 

                The email template used when a detected risk event is allowed.

                
                

                - **Subject** *(string) --* 

                  The subject.

                  
                

                - **HtmlBody** *(string) --* 

                  The HTML body.

                  
                

                - **TextBody** *(string) --* 

                  The text body.

                  
            
              

              - **MfaEmail** *(dict) --* 

                The MFA email template used when MFA is challenged as part of a detected risk.

                
                

                - **Subject** *(string) --* 

                  The subject.

                  
                

                - **HtmlBody** *(string) --* 

                  The HTML body.

                  
                

                - **TextBody** *(string) --* 

                  The text body.

                  
            
          
            

            - **Actions** *(dict) --* 

              Account takeover risk configuration actions

              
              

              - **LowAction** *(dict) --* 

                Action to take for a low risk.

                
                

                - **Notify** *(boolean) --* 

                  Flag specifying whether to send a notification.

                  
                

                - **EventAction** *(string) --* 

                  The event action.

                   

                   
                  * ``BLOCK`` Choosing this action will block the request. 
                   
                  * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
                   
                  * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
                   
                  * ``NO_ACTION`` Allow the user sign-in. 
                   

                  
            
              

              - **MediumAction** *(dict) --* 

                Action to take for a medium risk.

                
                

                - **Notify** *(boolean) --* 

                  Flag specifying whether to send a notification.

                  
                

                - **EventAction** *(string) --* 

                  The event action.

                   

                   
                  * ``BLOCK`` Choosing this action will block the request. 
                   
                  * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
                   
                  * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
                   
                  * ``NO_ACTION`` Allow the user sign-in. 
                   

                  
            
              

              - **HighAction** *(dict) --* 

                Action to take for a high risk.

                
                

                - **Notify** *(boolean) --* 

                  Flag specifying whether to send a notification.

                  
                

                - **EventAction** *(string) --* 

                  The event action.

                   

                   
                  * ``BLOCK`` Choosing this action will block the request. 
                   
                  * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the request. 
                   
                  * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request. 
                   
                  * ``NO_ACTION`` Allow the user sign-in. 
                   

                  
            
          
        
          

          - **RiskExceptionConfiguration** *(dict) --* 

            The configuration to override the risk decision.

            
            

            - **BlockedIPRangeList** *(list) --* 

              Overrides the risk decision to always block the pre-authentication requests. The IP range is in CIDR notation: a compact representation of an IP address and its associated routing prefix.

              
              

              - *(string) --* 
          
            

            - **SkippedIPRangeList** *(list) --* 

              Risk detection is not performed on the IP addresses in the range list. The IP range is in CIDR notation.

              
              

              - *(string) --* 
          
        
          

          - **LastModifiedDate** *(datetime) --* 

            The last modified date.

            
      
    

  .. py:method:: set_ui_customization(**kwargs)

    

    Sets the UI customization information for a user pool's built-in app UI.

     

    You can specify app UI customization settings for a single client (with a specific ``clientId`` ) or for all clients (by setting the ``clientId`` to ``ALL`` ). If you specify ``ALL`` , the default configuration will be used for every client that has no UI customization set previously. If you specify UI customization settings for a particular client, it will no longer fall back to the ``ALL`` configuration. 

     

    .. note::

       

      To use this API, your user pool must have a domain associated with it. Otherwise, there is no place to host the app's pages, and the service will throw an error.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SetUICustomization>`_    


    **Request Syntax** 
    ::

      response = client.set_ui_customization(
          UserPoolId='string',
          ClientId='string',
          CSS='string',
          ImageFile=b'bytes'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type ClientId: string
    :param ClientId: 

      The client ID for the client app.

      

    
    :type CSS: string
    :param CSS: 

      The CSS values in the UI customization.

      

    
    :type ImageFile: bytes
    :param ImageFile: 

      The uploaded logo image for the UI customization.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UICustomization': {
                'UserPoolId': 'string',
                'ClientId': 'string',
                'ImageUrl': 'string',
                'CSS': 'string',
                'CSSVersion': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UICustomization** *(dict) --* 

          The UI customization information.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool.

            
          

          - **ClientId** *(string) --* 

            The client ID for the client app.

            
          

          - **ImageUrl** *(string) --* 

            The logo image for the UI customization.

            
          

          - **CSS** *(string) --* 

            The CSS values in the UI customization.

            
          

          - **CSSVersion** *(string) --* 

            The CSS version number.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The last-modified date for the UI customization.

            
          

          - **CreationDate** *(datetime) --* 

            The creation date for the UI customization.

            
      
    

  .. py:method:: set_user_mfa_preference(**kwargs)

    

    Set the user's multi-factor authentication (MFA) method preference.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SetUserMFAPreference>`_    


    **Request Syntax** 
    ::

      response = client.set_user_mfa_preference(
          SMSMfaSettings={
              'Enabled': True|False,
              'PreferredMfa': True|False
          },
          SoftwareTokenMfaSettings={
              'Enabled': True|False,
              'PreferredMfa': True|False
          },
          AccessToken='string'
      )
    :type SMSMfaSettings: dict
    :param SMSMfaSettings: 

      The SMS text message multi-factor authentication (MFA) settings.

      

    
      - **Enabled** *(boolean) --* 

        Specifies whether SMS text message MFA is enabled.

        

      
      - **PreferredMfa** *(boolean) --* 

        The preferred MFA method.

        

      
    
    :type SoftwareTokenMfaSettings: dict
    :param SoftwareTokenMfaSettings: 

      The time-based one-time password software token MFA settings.

      

    
      - **Enabled** *(boolean) --* 

        Specifies whether software token MFA is enabled.

        

      
      - **PreferredMfa** *(boolean) --* 

        The preferred MFA method.

        

      
    
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: set_user_pool_mfa_config(**kwargs)

    

    Set the user pool MFA configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SetUserPoolMfaConfig>`_    


    **Request Syntax** 
    ::

      response = client.set_user_pool_mfa_config(
          UserPoolId='string',
          SmsMfaConfiguration={
              'SmsAuthenticationMessage': 'string',
              'SmsConfiguration': {
                  'SnsCallerArn': 'string',
                  'ExternalId': 'string'
              }
          },
          SoftwareTokenMfaConfiguration={
              'Enabled': True|False
          },
          MfaConfiguration='OFF'|'ON'|'OPTIONAL'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type SmsMfaConfiguration: dict
    :param SmsMfaConfiguration: 

      The SMS text message MFA configuration.

      

    
      - **SmsAuthenticationMessage** *(string) --* 

        The SMS authentication message.

        

      
      - **SmsConfiguration** *(dict) --* 

        The SMS configuration.

        

      
        - **SnsCallerArn** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.

          

        
        - **ExternalId** *(string) --* 

          The external ID.

          

        
      
    
    :type SoftwareTokenMfaConfiguration: dict
    :param SoftwareTokenMfaConfiguration: 

      The software token MFA configuration.

      

    
      - **Enabled** *(boolean) --* 

        Specifies whether software token MFA is enabled.

        

      
    
    :type MfaConfiguration: string
    :param MfaConfiguration: 

      The MFA configuration.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SmsMfaConfiguration': {
                'SmsAuthenticationMessage': 'string',
                'SmsConfiguration': {
                    'SnsCallerArn': 'string',
                    'ExternalId': 'string'
                }
            },
            'SoftwareTokenMfaConfiguration': {
                'Enabled': True|False
            },
            'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SmsMfaConfiguration** *(dict) --* 

          The SMS text message MFA configuration.

          
          

          - **SmsAuthenticationMessage** *(string) --* 

            The SMS authentication message.

            
          

          - **SmsConfiguration** *(dict) --* 

            The SMS configuration.

            
            

            - **SnsCallerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.

              
            

            - **ExternalId** *(string) --* 

              The external ID.

              
        
      
        

        - **SoftwareTokenMfaConfiguration** *(dict) --* 

          The software token MFA configuration.

          
          

          - **Enabled** *(boolean) --* 

            Specifies whether software token MFA is enabled.

            
      
        

        - **MfaConfiguration** *(string) --* 

          The MFA configuration.

          
    

  .. py:method:: set_user_settings(**kwargs)

    

    Sets the user settings like multi-factor authentication (MFA). If MFA is to be removed for a particular attribute pass the attribute with code delivery as null. If null list is passed, all MFA options are removed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SetUserSettings>`_    


    **Request Syntax** 
    ::

      response = client.set_user_settings(
          AccessToken='string',
          MFAOptions=[
              {
                  'DeliveryMedium': 'SMS'|'EMAIL',
                  'AttributeName': 'string'
              },
          ]
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token for the set user settings request.

      

    
    :type MFAOptions: list
    :param MFAOptions: **[REQUIRED]** 

      Specifies the options for MFA (e.g., email or phone number).

      

    
      - *(dict) --* 

        Specifies the different settings for multi-factor authentication (MFA).

        

      
        - **DeliveryMedium** *(string) --* 

          The delivery medium (email message or SMS message) to send the MFA code.

          

        
        - **AttributeName** *(string) --* 

          The attribute name of the MFA option type.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The response from the server for a set user settings request.

        
    

  .. py:method:: sign_up(**kwargs)

    

    Registers the user in the specified user pool and creates a user name, password, and user attributes.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SignUp>`_    


    **Request Syntax** 
    ::

      response = client.sign_up(
          ClientId='string',
          SecretHash='string',
          Username='string',
          Password='string',
          UserAttributes=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          ValidationData=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          AnalyticsMetadata={
              'AnalyticsEndpointId': 'string'
          },
          UserContextData={
              'EncodedData': 'string'
          }
      )
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The ID of the client associated with the user pool.

      

    
    :type SecretHash: string
    :param SecretHash: 

      A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user name of the user you wish to register.

      

    
    :type Password: string
    :param Password: **[REQUIRED]** 

      The password of the user you wish to register.

      

    
    :type UserAttributes: list
    :param UserAttributes: 

      An array of name-value pairs representing user attributes.

       

      For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

      

    
      - *(dict) --* 

        Specifies whether the attribute is standard or custom.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the attribute.

          

        
        - **Value** *(string) --* 

          The value of the attribute.

          

        
      
  
    :type ValidationData: list
    :param ValidationData: 

      The validation data in the request to register a user.

      

    
      - *(dict) --* 

        Specifies whether the attribute is standard or custom.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the attribute.

          

        
        - **Value** *(string) --* 

          The value of the attribute.

          

        
      
  
    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: 

      The Amazon Pinpoint analytics metadata for collecting metrics for ``SignUp`` calls.

      

    
      - **AnalyticsEndpointId** *(string) --* 

        The endpoint ID.

        

      
    
    :type UserContextData: dict
    :param UserContextData: 

      Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

      

    
      - **EncodedData** *(string) --* 

        Contextual data such as the user's device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserConfirmed': True|False,
            'CodeDeliveryDetails': {
                'Destination': 'string',
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            },
            'UserSub': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response from the server for a registration request.

        
        

        - **UserConfirmed** *(boolean) --* 

          A response from the server indicating that a user registration has been confirmed.

          
        

        - **CodeDeliveryDetails** *(dict) --* 

          The code delivery details returned by the server response to the user registration request.

          
          

          - **Destination** *(string) --* 

            The destination for the code delivery details.

            
          

          - **DeliveryMedium** *(string) --* 

            The delivery medium (email message or phone number).

            
          

          - **AttributeName** *(string) --* 

            The attribute name.

            
      
        

        - **UserSub** *(string) --* 

          The UUID of the authenticated user. This is not the same as ``username`` .

          
    

  .. py:method:: start_user_import_job(**kwargs)

    

    Starts the user import.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/StartUserImportJob>`_    


    **Request Syntax** 
    ::

      response = client.start_user_import_job(
          UserPoolId='string',
          JobId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool that the users are being imported into.

      

    
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      The job ID for the user import job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserImportJob': {
                'JobName': 'string',
                'JobId': 'string',
                'UserPoolId': 'string',
                'PreSignedUrl': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
                'CloudWatchLogsRoleArn': 'string',
                'ImportedUsers': 123,
                'SkippedUsers': 123,
                'FailedUsers': 123,
                'CompletionMessage': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to the request to start the user import job.

        
        

        - **UserImportJob** *(dict) --* 

          The job object that represents the user import job.

          
          

          - **JobName** *(string) --* 

            The job name for the user import job.

            
          

          - **JobId** *(string) --* 

            The job ID for the user import job.

            
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool that the users are being imported into.

            
          

          - **PreSignedUrl** *(string) --* 

            The pre-signed URL to be used to upload the ``.csv`` file.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user import job was created.

            
          

          - **StartDate** *(datetime) --* 

            The date when the user import job was started.

            
          

          - **CompletionDate** *(datetime) --* 

            The date when the user import job was completed.

            
          

          - **Status** *(string) --* 

            The status of the user import job. One of the following:

             

             
            * ``Created`` - The job was created but not started. 
             
            * ``Pending`` - A transition state. You have started the job, but it has not begun importing users yet. 
             
            * ``InProgress`` - The job has started, and users are being imported. 
             
            * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet. 
             
            * ``Stopped`` - You have stopped the job, and the job has stopped importing users. 
             
            * ``Succeeded`` - The job has completed successfully. 
             
            * ``Failed`` - The job has stopped due to an error. 
             
            * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started. 
             

            
          

          - **CloudWatchLogsRoleArn** *(string) --* 

            The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

            
          

          - **ImportedUsers** *(integer) --* 

            The number of users that were successfully imported.

            
          

          - **SkippedUsers** *(integer) --* 

            The number of users that were skipped.

            
          

          - **FailedUsers** *(integer) --* 

            The number of users that could not be imported.

            
          

          - **CompletionMessage** *(string) --* 

            The message returned when the user import job is completed.

            
      
    

  .. py:method:: stop_user_import_job(**kwargs)

    

    Stops the user import job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/StopUserImportJob>`_    


    **Request Syntax** 
    ::

      response = client.stop_user_import_job(
          UserPoolId='string',
          JobId='string'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool that the users are being imported into.

      

    
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      The job ID for the user import job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserImportJob': {
                'JobName': 'string',
                'JobId': 'string',
                'UserPoolId': 'string',
                'PreSignedUrl': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
                'CloudWatchLogsRoleArn': 'string',
                'ImportedUsers': 123,
                'SkippedUsers': 123,
                'FailedUsers': 123,
                'CompletionMessage': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to the request to stop the user import job.

        
        

        - **UserImportJob** *(dict) --* 

          The job object that represents the user import job.

          
          

          - **JobName** *(string) --* 

            The job name for the user import job.

            
          

          - **JobId** *(string) --* 

            The job ID for the user import job.

            
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool that the users are being imported into.

            
          

          - **PreSignedUrl** *(string) --* 

            The pre-signed URL to be used to upload the ``.csv`` file.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user import job was created.

            
          

          - **StartDate** *(datetime) --* 

            The date when the user import job was started.

            
          

          - **CompletionDate** *(datetime) --* 

            The date when the user import job was completed.

            
          

          - **Status** *(string) --* 

            The status of the user import job. One of the following:

             

             
            * ``Created`` - The job was created but not started. 
             
            * ``Pending`` - A transition state. You have started the job, but it has not begun importing users yet. 
             
            * ``InProgress`` - The job has started, and users are being imported. 
             
            * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet. 
             
            * ``Stopped`` - You have stopped the job, and the job has stopped importing users. 
             
            * ``Succeeded`` - The job has completed successfully. 
             
            * ``Failed`` - The job has stopped due to an error. 
             
            * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started. 
             

            
          

          - **CloudWatchLogsRoleArn** *(string) --* 

            The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

            
          

          - **ImportedUsers** *(integer) --* 

            The number of users that were successfully imported.

            
          

          - **SkippedUsers** *(integer) --* 

            The number of users that were skipped.

            
          

          - **FailedUsers** *(integer) --* 

            The number of users that could not be imported.

            
          

          - **CompletionMessage** *(string) --* 

            The message returned when the user import job is completed.

            
      
    

  .. py:method:: update_auth_event_feedback(**kwargs)

    

    Provides the feedback for an authentication event whether it was from a valid user or not. This feedback is used for improving the risk evaluation decision for the user pool as part of Amazon Cognito advanced security.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateAuthEventFeedback>`_    


    **Request Syntax** 
    ::

      response = client.update_auth_event_feedback(
          UserPoolId='string',
          Username='string',
          EventId='string',
          FeedbackToken='string',
          FeedbackValue='Valid'|'Invalid'
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type Username: string
    :param Username: **[REQUIRED]** 

      The user pool username.

      

    
    :type EventId: string
    :param EventId: **[REQUIRED]** 

      The event ID.

      

    
    :type FeedbackToken: string
    :param FeedbackToken: **[REQUIRED]** 

      The feedback token.

      

    
    :type FeedbackValue: string
    :param FeedbackValue: **[REQUIRED]** 

      The authentication event feedback value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_device_status(**kwargs)

    

    Updates the device status.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateDeviceStatus>`_    


    **Request Syntax** 
    ::

      response = client.update_device_status(
          AccessToken='string',
          DeviceKey='string',
          DeviceRememberedStatus='remembered'|'not_remembered'
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token.

      

    
    :type DeviceKey: string
    :param DeviceKey: **[REQUIRED]** 

      The device key.

      

    
    :type DeviceRememberedStatus: string
    :param DeviceRememberedStatus: 

      The status of whether a device is remembered.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The response to the request to update the device status.

        
    

  .. py:method:: update_group(**kwargs)

    

    Updates the specified group with the specified attributes.

     

    Requires developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateGroup>`_    


    **Request Syntax** 
    ::

      response = client.update_group(
          GroupName='string',
          UserPoolId='string',
          Description='string',
          RoleArn='string',
          Precedence=123
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the group.

      

    
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type Description: string
    :param Description: 

      A string containing the new description of the group.

      

    
    :type RoleArn: string
    :param RoleArn: 

      The new role ARN for the group. This is used for setting the ``cognito:roles`` and ``cognito:preferred_role`` claims in the token.

      

    
    :type Precedence: integer
    :param Precedence: 

      The new precedence value for the group. For more information about this parameter, see .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Group': {
                'GroupName': 'string',
                'UserPoolId': 'string',
                'Description': 'string',
                'RoleArn': 'string',
                'Precedence': 123,
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Group** *(dict) --* 

          The group object for the group.

          
          

          - **GroupName** *(string) --* 

            The name of the group.

            
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool.

            
          

          - **Description** *(string) --* 

            A string containing the description of the group.

            
          

          - **RoleArn** *(string) --* 

            The role ARN for the group.

            
          

          - **Precedence** *(integer) --* 

            A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values or with null ``Precedence`` values.

             

            Two groups can have the same ``Precedence`` value. If this happens, neither group takes precedence over the other. If two groups with the same ``Precedence`` have the same role ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is not set in users' tokens.

             

            The default ``Precedence`` value is null.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The date the group was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the group was created.

            
      
    

  .. py:method:: update_identity_provider(**kwargs)

    

    Updates identity provider information for a user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateIdentityProvider>`_    


    **Request Syntax** 
    ::

      response = client.update_identity_provider(
          UserPoolId='string',
          ProviderName='string',
          ProviderDetails={
              'string': 'string'
          },
          AttributeMapping={
              'string': 'string'
          },
          IdpIdentifiers=[
              'string',
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID.

      

    
    :type ProviderName: string
    :param ProviderName: **[REQUIRED]** 

      The identity provider name.

      

    
    :type ProviderDetails: dict
    :param ProviderDetails: 

      The identity provider details to be updated, such as ``MetadataURL`` and ``MetadataFile`` .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AttributeMapping: dict
    :param AttributeMapping: 

      The identity provider attribute mapping to be changed.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type IdpIdentifiers: list
    :param IdpIdentifiers: 

      A list of identity provider identifiers.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityProvider': {
                'UserPoolId': 'string',
                'ProviderName': 'string',
                'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon',
                'ProviderDetails': {
                    'string': 'string'
                },
                'AttributeMapping': {
                    'string': 'string'
                },
                'IdpIdentifiers': [
                    'string',
                ],
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **IdentityProvider** *(dict) --* 

          The identity provider object.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID.

            
          

          - **ProviderName** *(string) --* 

            The identity provider name.

            
          

          - **ProviderType** *(string) --* 

            The identity provider type.

            
          

          - **ProviderDetails** *(dict) --* 

            The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **AttributeMapping** *(dict) --* 

            A mapping of identity provider attributes to standard and custom user pool attributes.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **IdpIdentifiers** *(list) --* 

            A list of identity provider identifiers.

            
            

            - *(string) --* 
        
          

          - **LastModifiedDate** *(datetime) --* 

            The date the identity provider was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the identity provider was created.

            
      
    

  .. py:method:: update_resource_server(**kwargs)

    

    Updates the name and scopes of resource server. All other fields are read-only.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateResourceServer>`_    


    **Request Syntax** 
    ::

      response = client.update_resource_server(
          UserPoolId='string',
          Identifier='string',
          Name='string',
          Scopes=[
              {
                  'ScopeName': 'string',
                  'ScopeDescription': 'string'
              },
          ]
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool.

      

    
    :type Identifier: string
    :param Identifier: **[REQUIRED]** 

      The identifier for the resource server.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the resource server.

      

    
    :type Scopes: list
    :param Scopes: 

      The scope values to be set for the resource server.

      

    
      - *(dict) --* 

        A resource server scope.

        

      
        - **ScopeName** *(string) --* **[REQUIRED]** 

          The name of the scope.

          

        
        - **ScopeDescription** *(string) --* **[REQUIRED]** 

          A description of the scope.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceServer': {
                'UserPoolId': 'string',
                'Identifier': 'string',
                'Name': 'string',
                'Scopes': [
                    {
                        'ScopeName': 'string',
                        'ScopeDescription': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceServer** *(dict) --* 

          The resource server.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool that hosts the resource server.

            
          

          - **Identifier** *(string) --* 

            The identifier for the resource server.

            
          

          - **Name** *(string) --* 

            The name of the resource server.

            
          

          - **Scopes** *(list) --* 

            A list of scopes that are defined for the resource server.

            
            

            - *(dict) --* 

              A resource server scope.

              
              

              - **ScopeName** *(string) --* 

                The name of the scope.

                
              

              - **ScopeDescription** *(string) --* 

                A description of the scope.

                
          
        
      
    

  .. py:method:: update_user_attributes(**kwargs)

    

    Allows a user to update a specific attribute (one at a time).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateUserAttributes>`_    


    **Request Syntax** 
    ::

      response = client.update_user_attributes(
          UserAttributes=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          AccessToken='string'
      )
    :type UserAttributes: list
    :param UserAttributes: **[REQUIRED]** 

      An array of name-value pairs representing user attributes.

       

      For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

      

    
      - *(dict) --* 

        Specifies whether the attribute is standard or custom.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the attribute.

          

        
        - **Value** *(string) --* 

          The value of the attribute.

          

        
      
  
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      The access token for the request to update user attributes.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CodeDeliveryDetailsList': [
                {
                    'Destination': 'string',
                    'DeliveryMedium': 'SMS'|'EMAIL',
                    'AttributeName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server for the request to update user attributes.

        
        

        - **CodeDeliveryDetailsList** *(list) --* 

          The code delivery details list from the server for the request to update user attributes.

          
          

          - *(dict) --* 

            The code delivery details being returned from the server.

            
            

            - **Destination** *(string) --* 

              The destination for the code delivery details.

              
            

            - **DeliveryMedium** *(string) --* 

              The delivery medium (email message or phone number).

              
            

            - **AttributeName** *(string) --* 

              The attribute name.

              
        
      
    

  .. py:method:: update_user_pool(**kwargs)

    

    Updates the specified user pool with the specified attributes.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateUserPool>`_    


    **Request Syntax** 
    ::

      response = client.update_user_pool(
          UserPoolId='string',
          Policies={
              'PasswordPolicy': {
                  'MinimumLength': 123,
                  'RequireUppercase': True|False,
                  'RequireLowercase': True|False,
                  'RequireNumbers': True|False,
                  'RequireSymbols': True|False
              }
          },
          LambdaConfig={
              'PreSignUp': 'string',
              'CustomMessage': 'string',
              'PostConfirmation': 'string',
              'PreAuthentication': 'string',
              'PostAuthentication': 'string',
              'DefineAuthChallenge': 'string',
              'CreateAuthChallenge': 'string',
              'VerifyAuthChallengeResponse': 'string',
              'PreTokenGeneration': 'string'
          },
          AutoVerifiedAttributes=[
              'phone_number'|'email',
          ],
          SmsVerificationMessage='string',
          EmailVerificationMessage='string',
          EmailVerificationSubject='string',
          VerificationMessageTemplate={
              'SmsMessage': 'string',
              'EmailMessage': 'string',
              'EmailSubject': 'string',
              'EmailMessageByLink': 'string',
              'EmailSubjectByLink': 'string',
              'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
          },
          SmsAuthenticationMessage='string',
          MfaConfiguration='OFF'|'ON'|'OPTIONAL',
          DeviceConfiguration={
              'ChallengeRequiredOnNewDevice': True|False,
              'DeviceOnlyRememberedOnUserPrompt': True|False
          },
          EmailConfiguration={
              'SourceArn': 'string',
              'ReplyToEmailAddress': 'string'
          },
          SmsConfiguration={
              'SnsCallerArn': 'string',
              'ExternalId': 'string'
          },
          UserPoolTags={
              'string': 'string'
          },
          AdminCreateUserConfig={
              'AllowAdminCreateUserOnly': True|False,
              'UnusedAccountValidityDays': 123,
              'InviteMessageTemplate': {
                  'SMSMessage': 'string',
                  'EmailMessage': 'string',
                  'EmailSubject': 'string'
              }
          },
          UserPoolAddOns={
              'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
          }
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool you want to update.

      

    
    :type Policies: dict
    :param Policies: 

      A container with the policies you wish to update in a user pool.

      

    
      - **PasswordPolicy** *(dict) --* 

        The password policy.

        

      
        - **MinimumLength** *(integer) --* 

          The minimum length of the password policy that you have set. Cannot be less than 6.

          

        
        - **RequireUppercase** *(boolean) --* 

          In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.

          

        
        - **RequireLowercase** *(boolean) --* 

          In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.

          

        
        - **RequireNumbers** *(boolean) --* 

          In the password policy that you have set, refers to whether you have required users to use at least one number in their password.

          

        
        - **RequireSymbols** *(boolean) --* 

          In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.

          

        
      
    
    :type LambdaConfig: dict
    :param LambdaConfig: 

      The AWS Lambda configuration information from the request to update the user pool.

      

    
      - **PreSignUp** *(string) --* 

        A pre-registration AWS Lambda trigger.

        

      
      - **CustomMessage** *(string) --* 

        A custom Message AWS Lambda trigger.

        

      
      - **PostConfirmation** *(string) --* 

        A post-confirmation AWS Lambda trigger.

        

      
      - **PreAuthentication** *(string) --* 

        A pre-authentication AWS Lambda trigger.

        

      
      - **PostAuthentication** *(string) --* 

        A post-authentication AWS Lambda trigger.

        

      
      - **DefineAuthChallenge** *(string) --* 

        Defines the authentication challenge.

        

      
      - **CreateAuthChallenge** *(string) --* 

        Creates an authentication challenge.

        

      
      - **VerifyAuthChallengeResponse** *(string) --* 

        Verifies the authentication challenge response.

        

      
      - **PreTokenGeneration** *(string) --* 

        A Lambda trigger that is invoked before token generation.

        

      
    
    :type AutoVerifiedAttributes: list
    :param AutoVerifiedAttributes: 

      The attributes that are automatically verified when the Amazon Cognito service makes a request to update user pools.

      

    
      - *(string) --* 

      
  
    :type SmsVerificationMessage: string
    :param SmsVerificationMessage: 

      A container with information about the SMS verification message.

      

    
    :type EmailVerificationMessage: string
    :param EmailVerificationMessage: 

      The contents of the email verification message.

      

    
    :type EmailVerificationSubject: string
    :param EmailVerificationSubject: 

      The subject of the email verification message.

      

    
    :type VerificationMessageTemplate: dict
    :param VerificationMessageTemplate: 

      The template for verification messages.

      

    
      - **SmsMessage** *(string) --* 

        The SMS message template.

        

      
      - **EmailMessage** *(string) --* 

        The email message template.

        

      
      - **EmailSubject** *(string) --* 

        The subject line for the email message template.

        

      
      - **EmailMessageByLink** *(string) --* 

        The email message template for sending a confirmation link to the user.

        

      
      - **EmailSubjectByLink** *(string) --* 

        The subject line for the email message template for sending a confirmation link to the user.

        

      
      - **DefaultEmailOption** *(string) --* 

        The default email option.

        

      
    
    :type SmsAuthenticationMessage: string
    :param SmsAuthenticationMessage: 

      The contents of the SMS authentication message.

      

    
    :type MfaConfiguration: string
    :param MfaConfiguration: 

      Can be one of the following values:

       

       
      * ``OFF`` - MFA tokens are not required and cannot be specified during user registration. 
       
      * ``ON`` - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool. 
       
      * ``OPTIONAL`` - Users have the option when registering to create an MFA token. 
       

      

    
    :type DeviceConfiguration: dict
    :param DeviceConfiguration: 

      Device configuration.

      

    
      - **ChallengeRequiredOnNewDevice** *(boolean) --* 

        Indicates whether a challenge is required on a new device. Only applicable to a new device.

        

      
      - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --* 

        If true, a device is only remembered on user prompt.

        

      
    
    :type EmailConfiguration: dict
    :param EmailConfiguration: 

      Email configuration.

      

    
      - **SourceArn** *(string) --* 

        The Amazon Resource Name (ARN) of the email source.

        

      
      - **ReplyToEmailAddress** *(string) --* 

        The destination to which the receiver of the email should reply to.

        

      
    
    :type SmsConfiguration: dict
    :param SmsConfiguration: 

      SMS configuration.

      

    
      - **SnsCallerArn** *(string) --* **[REQUIRED]** 

        The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.

        

      
      - **ExternalId** *(string) --* 

        The external ID.

        

      
    
    :type UserPoolTags: dict
    :param UserPoolTags: 

      The cost allocation tags for the user pool. For more information, see `Adding Cost Allocation Tags to Your User Pool <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-cost-allocation-tagging.html>`__  

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AdminCreateUserConfig: dict
    :param AdminCreateUserConfig: 

      The configuration for ``AdminCreateUser`` requests.

      

    
      - **AllowAdminCreateUserOnly** *(boolean) --* 

        Set to ``True`` if only the administrator is allowed to create user profiles. Set to ``False`` if users can sign themselves up via an app.

        

      
      - **UnusedAccountValidityDays** *(integer) --* 

        The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call ``AdminCreateUser`` again, specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this parameter is 7.

        

      
      - **InviteMessageTemplate** *(dict) --* 

        The message template to be used for the welcome message to new users.

         

        See also `Customizing User Invitation Messages <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__ .

        

      
        - **SMSMessage** *(string) --* 

          The message template for SMS messages.

          

        
        - **EmailMessage** *(string) --* 

          The message template for email messages.

          

        
        - **EmailSubject** *(string) --* 

          The subject line for email messages.

          

        
      
    
    :type UserPoolAddOns: dict
    :param UserPoolAddOns: 

      Used to enable advanced security risk detection. Set the key ``AdvancedSecurityMode`` to the value "AUDIT".

      

    
      - **AdvancedSecurityMode** *(string) --* **[REQUIRED]** 

        The advanced security mode.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server when you make a request to update the user pool.

        
    

  .. py:method:: update_user_pool_client(**kwargs)

    

    Allows the developer to update the specified user pool client and password policy.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateUserPoolClient>`_    


    **Request Syntax** 
    ::

      response = client.update_user_pool_client(
          UserPoolId='string',
          ClientId='string',
          ClientName='string',
          RefreshTokenValidity=123,
          ReadAttributes=[
              'string',
          ],
          WriteAttributes=[
              'string',
          ],
          ExplicitAuthFlows=[
              'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
          ],
          SupportedIdentityProviders=[
              'string',
          ],
          CallbackURLs=[
              'string',
          ],
          LogoutURLs=[
              'string',
          ],
          DefaultRedirectURI='string',
          AllowedOAuthFlows=[
              'code'|'implicit'|'client_credentials',
          ],
          AllowedOAuthScopes=[
              'string',
          ],
          AllowedOAuthFlowsUserPoolClient=True|False,
          AnalyticsConfiguration={
              'ApplicationId': 'string',
              'RoleArn': 'string',
              'ExternalId': 'string',
              'UserDataShared': True|False
          }
      )
    :type UserPoolId: string
    :param UserPoolId: **[REQUIRED]** 

      The user pool ID for the user pool where you want to update the user pool client.

      

    
    :type ClientId: string
    :param ClientId: **[REQUIRED]** 

      The ID of the client associated with the user pool.

      

    
    :type ClientName: string
    :param ClientName: 

      The client name from the update user pool client request.

      

    
    :type RefreshTokenValidity: integer
    :param RefreshTokenValidity: 

      The time limit, in days, after which the refresh token is no longer valid and cannot be used.

      

    
    :type ReadAttributes: list
    :param ReadAttributes: 

      The read-only attributes of the user pool.

      

    
      - *(string) --* 

      
  
    :type WriteAttributes: list
    :param WriteAttributes: 

      The writeable attributes of the user pool.

      

    
      - *(string) --* 

      
  
    :type ExplicitAuthFlows: list
    :param ExplicitAuthFlows: 

      Explicit authentication flows.

      

    
      - *(string) --* 

      
  
    :type SupportedIdentityProviders: list
    :param SupportedIdentityProviders: 

      A list of provider names for the identity providers that are supported on this client.

      

    
      - *(string) --* 

      
  
    :type CallbackURLs: list
    :param CallbackURLs: 

      A list of allowed callback URLs for the identity providers.

      

    
      - *(string) --* 

      
  
    :type LogoutURLs: list
    :param LogoutURLs: 

      A list of allowed logout URLs for the identity providers.

      

    
      - *(string) --* 

      
  
    :type DefaultRedirectURI: string
    :param DefaultRedirectURI: 

      The default redirect URI. Must be in the ``CallbackURLs`` list.

      

    
    :type AllowedOAuthFlows: list
    :param AllowedOAuthFlows: 

      Set to ``code`` to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.

       

      Set to ``token`` to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.

      

    
      - *(string) --* 

      
  
    :type AllowedOAuthScopes: list
    :param AllowedOAuthScopes: 

      A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` , ``"email"`` , ``"openid"`` , and ``"Cognito"`` .

      

    
      - *(string) --* 

      
  
    :type AllowedOAuthFlowsUserPoolClient: boolean
    :param AllowedOAuthFlowsUserPoolClient: 

      Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

      

    
    :type AnalyticsConfiguration: dict
    :param AnalyticsConfiguration: 

      The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.

      

    
      - **ApplicationId** *(string) --* **[REQUIRED]** 

        The application ID for an Amazon Pinpoint application.

        

      
      - **RoleArn** *(string) --* **[REQUIRED]** 

        The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.

        

      
      - **ExternalId** *(string) --* **[REQUIRED]** 

        The external ID.

        

      
      - **UserDataShared** *(boolean) --* 

        If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserPoolClient': {
                'UserPoolId': 'string',
                'ClientName': 'string',
                'ClientId': 'string',
                'ClientSecret': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1),
                'RefreshTokenValidity': 123,
                'ReadAttributes': [
                    'string',
                ],
                'WriteAttributes': [
                    'string',
                ],
                'ExplicitAuthFlows': [
                    'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
                ],
                'SupportedIdentityProviders': [
                    'string',
                ],
                'CallbackURLs': [
                    'string',
                ],
                'LogoutURLs': [
                    'string',
                ],
                'DefaultRedirectURI': 'string',
                'AllowedOAuthFlows': [
                    'code'|'implicit'|'client_credentials',
                ],
                'AllowedOAuthScopes': [
                    'string',
                ],
                'AllowedOAuthFlowsUserPoolClient': True|False,
                'AnalyticsConfiguration': {
                    'ApplicationId': 'string',
                    'RoleArn': 'string',
                    'ExternalId': 'string',
                    'UserDataShared': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response from the server to the request to update the user pool client.

        
        

        - **UserPoolClient** *(dict) --* 

          The user pool client value from the response from the server when an update user pool client request is made.

          
          

          - **UserPoolId** *(string) --* 

            The user pool ID for the user pool client.

            
          

          - **ClientName** *(string) --* 

            The client name from the user pool request of the client type.

            
          

          - **ClientId** *(string) --* 

            The ID of the client associated with the user pool.

            
          

          - **ClientSecret** *(string) --* 

            The client secret from the user pool request of the client type.

            
          

          - **LastModifiedDate** *(datetime) --* 

            The date the user pool client was last modified.

            
          

          - **CreationDate** *(datetime) --* 

            The date the user pool client was created.

            
          

          - **RefreshTokenValidity** *(integer) --* 

            The time limit, in days, after which the refresh token is no longer valid and cannot be used.

            
          

          - **ReadAttributes** *(list) --* 

            The Read-only attributes.

            
            

            - *(string) --* 
        
          

          - **WriteAttributes** *(list) --* 

            The writeable attributes.

            
            

            - *(string) --* 
        
          

          - **ExplicitAuthFlows** *(list) --* 

            The explicit authentication flows.

            
            

            - *(string) --* 
        
          

          - **SupportedIdentityProviders** *(list) --* 

            A list of provider names for the identity providers that are supported on this client.

            
            

            - *(string) --* 
        
          

          - **CallbackURLs** *(list) --* 

            A list of allowed callback URLs for the identity providers.

            
            

            - *(string) --* 
        
          

          - **LogoutURLs** *(list) --* 

            A list of allowed logout URLs for the identity providers.

            
            

            - *(string) --* 
        
          

          - **DefaultRedirectURI** *(string) --* 

            The default redirect URI. Must be in the ``CallbackURLs`` list.

            
          

          - **AllowedOAuthFlows** *(list) --* 

            Set to ``code`` to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.

             

            Set to ``token`` to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.

            
            

            - *(string) --* 
        
          

          - **AllowedOAuthScopes** *(list) --* 

            A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` , ``"email"`` , ``"openid"`` , and ``"Cognito"`` .

            
            

            - *(string) --* 
        
          

          - **AllowedOAuthFlowsUserPoolClient** *(boolean) --* 

            Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

            
          

          - **AnalyticsConfiguration** *(dict) --* 

            The Amazon Pinpoint analytics configuration for the user pool client.

            
            

            - **ApplicationId** *(string) --* 

              The application ID for an Amazon Pinpoint application.

              
            

            - **RoleArn** *(string) --* 

              The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.

              
            

            - **ExternalId** *(string) --* 

              The external ID.

              
            

            - **UserDataShared** *(boolean) --* 

              If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.

              
        
      
    

  .. py:method:: verify_software_token(**kwargs)

    

    Use this API to register a user's entered TOTP code and mark the user's software token MFA status as "verified" if successful,

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/VerifySoftwareToken>`_    


    **Request Syntax** 
    ::

      response = client.verify_software_token(
          AccessToken='string',
          Session='string',
          UserCode='string',
          FriendlyDeviceName='string'
      )
    :type AccessToken: string
    :param AccessToken: 

      The access token.

      

    
    :type Session: string
    :param Session: 

      The session which should be passed both ways in challenge-response calls to the service.

      

    
    :type UserCode: string
    :param UserCode: **[REQUIRED]** 

      The one time password computed using the secret code returned by 

      

    
    :type FriendlyDeviceName: string
    :param FriendlyDeviceName: 

      The friendly device name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Status': 'SUCCESS'|'ERROR',
            'Session': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Status** *(string) --* 

          The status of the verify software token.

          
        

        - **Session** *(string) --* 

          The session which should be passed both ways in challenge-response calls to the service.

          
    

  .. py:method:: verify_user_attribute(**kwargs)

    

    Verifies the specified user attributes in the user pool.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/VerifyUserAttribute>`_    


    **Request Syntax** 
    ::

      response = client.verify_user_attribute(
          AccessToken='string',
          AttributeName='string',
          Code='string'
      )
    :type AccessToken: string
    :param AccessToken: **[REQUIRED]** 

      Represents the access token of the request to verify user attributes.

      

    
    :type AttributeName: string
    :param AttributeName: **[REQUIRED]** 

      The attribute name in the request to verify user attributes.

      

    
    :type Code: string
    :param Code: **[REQUIRED]** 

      The verification code in the request to verify user attributes.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        A container representing the response from the server from the request to verify user attributes.

        
    

==========
Paginators
==========


The available paginators are:
