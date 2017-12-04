

********
WorkMail
********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: WorkMail.Client

  A low-level client representing Amazon WorkMail::

    
    import boto3
    
    client = boto3.client('workmail')

  
  These are the available methods:
  
  *   :py:meth:`~WorkMail.Client.associate_delegate_to_resource`

  
  *   :py:meth:`~WorkMail.Client.associate_member_to_group`

  
  *   :py:meth:`~WorkMail.Client.can_paginate`

  
  *   :py:meth:`~WorkMail.Client.create_alias`

  
  *   :py:meth:`~WorkMail.Client.create_group`

  
  *   :py:meth:`~WorkMail.Client.create_resource`

  
  *   :py:meth:`~WorkMail.Client.create_user`

  
  *   :py:meth:`~WorkMail.Client.delete_alias`

  
  *   :py:meth:`~WorkMail.Client.delete_group`

  
  *   :py:meth:`~WorkMail.Client.delete_resource`

  
  *   :py:meth:`~WorkMail.Client.delete_user`

  
  *   :py:meth:`~WorkMail.Client.deregister_from_work_mail`

  
  *   :py:meth:`~WorkMail.Client.describe_group`

  
  *   :py:meth:`~WorkMail.Client.describe_organization`

  
  *   :py:meth:`~WorkMail.Client.describe_resource`

  
  *   :py:meth:`~WorkMail.Client.describe_user`

  
  *   :py:meth:`~WorkMail.Client.disassociate_delegate_from_resource`

  
  *   :py:meth:`~WorkMail.Client.disassociate_member_from_group`

  
  *   :py:meth:`~WorkMail.Client.generate_presigned_url`

  
  *   :py:meth:`~WorkMail.Client.get_paginator`

  
  *   :py:meth:`~WorkMail.Client.get_waiter`

  
  *   :py:meth:`~WorkMail.Client.list_aliases`

  
  *   :py:meth:`~WorkMail.Client.list_group_members`

  
  *   :py:meth:`~WorkMail.Client.list_groups`

  
  *   :py:meth:`~WorkMail.Client.list_organizations`

  
  *   :py:meth:`~WorkMail.Client.list_resource_delegates`

  
  *   :py:meth:`~WorkMail.Client.list_resources`

  
  *   :py:meth:`~WorkMail.Client.list_users`

  
  *   :py:meth:`~WorkMail.Client.register_to_work_mail`

  
  *   :py:meth:`~WorkMail.Client.reset_password`

  
  *   :py:meth:`~WorkMail.Client.update_primary_email_address`

  
  *   :py:meth:`~WorkMail.Client.update_resource`

  

  .. py:method:: associate_delegate_to_resource(**kwargs)

    

    Adds a member to the resource's set of delegates.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/AssociateDelegateToResource>`_    


    **Request Syntax** 
    ::

      response = client.associate_delegate_to_resource(
          OrganizationId='string',
          ResourceId='string',
          EntityId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The organization under which the resource exists.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource for which members are associated.

      

    
    :type EntityId: string
    :param EntityId: **[REQUIRED]** 

      The member (user or group) to associate to the resource.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: associate_member_to_group(**kwargs)

    

    Adds a member to the group's set.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/AssociateMemberToGroup>`_    


    **Request Syntax** 
    ::

      response = client.associate_member_to_group(
          OrganizationId='string',
          GroupId='string',
          MemberId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The organization under which the group exists.

      

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** 

      The group for which the member is associated.

      

    
    :type MemberId: string
    :param MemberId: **[REQUIRED]** 

      The member to associate to the group.

      

    
    
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


  .. py:method:: create_alias(**kwargs)

    

    Adds an alias to the set of a given member of Amazon WorkMail.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateAlias>`_    


    **Request Syntax** 
    ::

      response = client.create_alias(
          OrganizationId='string',
          EntityId='string',
          Alias='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The organization under which the member exists.

      

    
    :type EntityId: string
    :param EntityId: **[REQUIRED]** 

      The alias is added to this Amazon WorkMail entity.

      

    
    :type Alias: string
    :param Alias: **[REQUIRED]** 

      The alias to add to the user.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_group(**kwargs)

    

    Creates a group that can be used in Amazon WorkMail by calling the RegisterToWorkMail operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_group(
          OrganizationId='string',
          Name='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The organization under which the group is to be created.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GroupId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **GroupId** *(string) --* 

          The ID of the group.

          
    

  .. py:method:: create_resource(**kwargs)

    

    Creates a new Amazon WorkMail resource. The available types are equipment and room.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateResource>`_    


    **Request Syntax** 
    ::

      response = client.create_resource(
          OrganizationId='string',
          Name='string',
          Type='ROOM'|'EQUIPMENT'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier associated with the organization for which the resource is created.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the created resource.

      

    
    :type Type: string
    :param Type: **[REQUIRED]** 

      The type of the created resource.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceId** *(string) --* 

          The identifier of the created resource.

          
    

  .. py:method:: create_user(**kwargs)

    

    Creates a user who can be used in Amazon WorkMail by calling the RegisterToWorkMail operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateUser>`_    


    **Request Syntax** 
    ::

      response = client.create_user(
          OrganizationId='string',
          Name='string',
          DisplayName='string',
          Password='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier of the organization for which the user is created.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name for the user to be created.

      

    
    :type DisplayName: string
    :param DisplayName: **[REQUIRED]** 

      The display name for the user to be created.

      

    
    :type Password: string
    :param Password: **[REQUIRED]** 

      The password for the user to be created.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UserId** *(string) --* 

          The information regarding the newly created user.

          
    

  .. py:method:: delete_alias(**kwargs)

    

    Remove the alias from a set of aliases for a given user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteAlias>`_    


    **Request Syntax** 
    ::

      response = client.delete_alias(
          OrganizationId='string',
          EntityId='string',
          Alias='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the user exists.

      

    
    :type EntityId: string
    :param EntityId: **[REQUIRED]** 

      The identifier for the Amazon WorkMail entity to have the aliases removed.

      

    
    :type Alias: string
    :param Alias: **[REQUIRED]** 

      The aliases to be removed from the user's set of aliases. Duplicate entries in the list are collapsed into single entries (the list is transformed into a set).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_group(**kwargs)

    

    Deletes a group from Amazon WorkMail.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_group(
          OrganizationId='string',
          GroupId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The organization that contains the group.

      

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** 

      The identifier of the group to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_resource(**kwargs)

    

    Deletes the specified resource. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteResource>`_    


    **Request Syntax** 
    ::

      response = client.delete_resource(
          OrganizationId='string',
          ResourceId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier associated with the organization for which the resource is deleted.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The identifier of the resource to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_user(**kwargs)

    

    Deletes a user from Amazon WorkMail and all subsequent systems. The action can't be undone. The mailbox is kept as-is for a minimum of 30 days, without any means to restore it. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteUser>`_    


    **Request Syntax** 
    ::

      response = client.delete_user(
          OrganizationId='string',
          UserId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The organization that contains the user.

      

    
    :type UserId: string
    :param UserId: **[REQUIRED]** 

      The identifier of the user to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: deregister_from_work_mail(**kwargs)

    

    Mark a user, group, or resource as no longer used in Amazon WorkMail. This action disassociates the mailbox and schedules it for clean-up. Amazon WorkMail keeps mailboxes for 30 days before they are permanently removed. The functionality in the console is *Disable* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeregisterFromWorkMail>`_    


    **Request Syntax** 
    ::

      response = client.deregister_from_work_mail(
          OrganizationId='string',
          EntityId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the Amazon WorkMail entity exists.

      

    
    :type EntityId: string
    :param EntityId: **[REQUIRED]** 

      The identifier for the entity to be updated.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_group(**kwargs)

    

    Returns the data available for the group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeGroup>`_    


    **Request Syntax** 
    ::

      response = client.describe_group(
          OrganizationId='string',
          GroupId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the group exists.

      

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** 

      The identifier for the group to be described.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GroupId': 'string',
            'Name': 'string',
            'Email': 'string',
            'State': 'ENABLED'|'DISABLED'|'DELETED',
            'EnabledDate': datetime(2015, 1, 1),
            'DisabledDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **GroupId** *(string) --* 

          The identifier of the described group.

          
        

        - **Name** *(string) --* 

          The name of the described group.

          
        

        - **Email** *(string) --* 

          The email of the described group.

          
        

        - **State** *(string) --* 

          The state of the user: enabled (registered to Amazon WorkMail) or disabled (deregistered or never registered to Amazon WorkMail).

          
        

        - **EnabledDate** *(datetime) --* 

          The date and time when a user was registered to Amazon WorkMail, in UNIX epoch time format.

          
        

        - **DisabledDate** *(datetime) --* 

          The date and time when a user was deregistered from Amazon WorkMail, in UNIX epoch time format.

          
    

  .. py:method:: describe_organization(**kwargs)

    

    Provides more information regarding a given organization based on its identifier.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeOrganization>`_    


    **Request Syntax** 
    ::

      response = client.describe_organization(
          OrganizationId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization to be described.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OrganizationId': 'string',
            'Alias': 'string',
            'State': 'string',
            'DirectoryId': 'string',
            'DirectoryType': 'string',
            'DefaultMailDomain': 'string',
            'CompletedDate': datetime(2015, 1, 1),
            'ErrorMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OrganizationId** *(string) --* 

          The identifier of an organization.

          
        

        - **Alias** *(string) --* 

          The alias for an organization.

          
        

        - **State** *(string) --* 

          The state of an organization.

          
        

        - **DirectoryId** *(string) --* 

          The identifier for the directory associated with an Amazon WorkMail organization.

          
        

        - **DirectoryType** *(string) --* 

          The type of directory associated with the Amazon WorkMail organization.

          
        

        - **DefaultMailDomain** *(string) --* 

          The default mail domain associated with the organization.

          
        

        - **CompletedDate** *(datetime) --* 

          The date at which the organization became usable in the Amazon WorkMail context, in UNIX epoch time format.

          
        

        - **ErrorMessage** *(string) --* 

          The (optional) error message indicating if unexpected behavior was encountered with regards to the organization.

          
    

  .. py:method:: describe_resource(**kwargs)

    

    Returns the data available for the resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeResource>`_    


    **Request Syntax** 
    ::

      response = client.describe_resource(
          OrganizationId='string',
          ResourceId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier associated with the organization for which the resource is described.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The identifier of the resource to be described.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceId': 'string',
            'Email': 'string',
            'Name': 'string',
            'Type': 'ROOM'|'EQUIPMENT',
            'BookingOptions': {
                'AutoAcceptRequests': True|False,
                'AutoDeclineRecurringRequests': True|False,
                'AutoDeclineConflictingRequests': True|False
            },
            'State': 'ENABLED'|'DISABLED'|'DELETED',
            'EnabledDate': datetime(2015, 1, 1),
            'DisabledDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceId** *(string) --* 

          The identifier of the described resource.

          
        

        - **Email** *(string) --* 

          The email of the described resource.

          
        

        - **Name** *(string) --* 

          The name of the described resource.

          
        

        - **Type** *(string) --* 

          The type of the described resource.

          
        

        - **BookingOptions** *(dict) --* 

          The booking options for the described resource.

          
          

          - **AutoAcceptRequests** *(boolean) --* 

            The resource's ability to automatically reply to requests. If disabled, delegates must be associated to the resource.

            
          

          - **AutoDeclineRecurringRequests** *(boolean) --* 

            The resource's ability to automatically decline any recurring requests.

            
          

          - **AutoDeclineConflictingRequests** *(boolean) --* 

            The resource's ability to automatically decline any conflicting requests.

            
      
        

        - **State** *(string) --* 

          The state of the resource: enabled (registered to Amazon WorkMail) or disabled (deregistered or never registered to Amazon WorkMail).

          
        

        - **EnabledDate** *(datetime) --* 

          The date and time when a resource was registered to Amazon WorkMail, in UNIX epoch time format.

          
        

        - **DisabledDate** *(datetime) --* 

          The date and time when a resource was registered from Amazon WorkMail, in UNIX epoch time format.

          
    

  .. py:method:: describe_user(**kwargs)

    

    Provides information regarding the user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeUser>`_    


    **Request Syntax** 
    ::

      response = client.describe_user(
          OrganizationId='string',
          UserId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the user exists.

      

    
    :type UserId: string
    :param UserId: **[REQUIRED]** 

      The identifier for the user to be described.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserId': 'string',
            'Name': 'string',
            'Email': 'string',
            'DisplayName': 'string',
            'State': 'ENABLED'|'DISABLED'|'DELETED',
            'UserRole': 'USER'|'RESOURCE'|'SYSTEM_USER',
            'EnabledDate': datetime(2015, 1, 1),
            'DisabledDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UserId** *(string) --* 

          The identifier for the described user.

          
        

        - **Name** *(string) --* 

          The name for the user.

          
        

        - **Email** *(string) --* 

          The email of the user.

          
        

        - **DisplayName** *(string) --* 

          The display name of the user.

          
        

        - **State** *(string) --* 

          The state of a user: enabled (registered to Amazon WorkMail) or disabled (deregistered or never registered to Amazon WorkMail).

          
        

        - **UserRole** *(string) --* 

          In certain cases other entities are modeled as users. If interoperability is enabled, resources are imported into Amazon WorkMail as users. Because different Amazon WorkMail organizations rely on different directory types, administrators can distinguish between a user that is not registered to Amazon WorkMail (is disabled and has a user role) and the administrative users of the directory. The values are USER, RESOURCE, and SYSTEM_USER.

          
        

        - **EnabledDate** *(datetime) --* 

          The date and time at which the user was enabled for Amazon WorkMail usage, in UNIX epoch time format.

          
        

        - **DisabledDate** *(datetime) --* 

          The date and time at which the user was disabled for Amazon WorkMail usage, in UNIX epoch time format.

          
    

  .. py:method:: disassociate_delegate_from_resource(**kwargs)

    

    Removes a member from the resource's set of delegates.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DisassociateDelegateFromResource>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_delegate_from_resource(
          OrganizationId='string',
          ResourceId='string',
          EntityId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the resource exists.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The identifier of the resource from which delegates' set members are removed. 

      

    
    :type EntityId: string
    :param EntityId: **[REQUIRED]** 

      The identifier for the member (user, group) to be removed from the resource's delegates.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: disassociate_member_from_group(**kwargs)

    

    Removes a member from a group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DisassociateMemberFromGroup>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_member_from_group(
          OrganizationId='string',
          GroupId='string',
          MemberId='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the group exists.

      

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** 

      The identifier for the group from which members are removed.

      

    
    :type MemberId: string
    :param MemberId: **[REQUIRED]** 

      The identifier for the member to be removed to the group.

      

    
    
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

        


  .. py:method:: list_aliases(**kwargs)

    

    Creates a paginated call to list the aliases associated with a given entity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListAliases>`_    


    **Request Syntax** 
    ::

      response = client.list_aliases(
          OrganizationId='string',
          EntityId='string',
          NextToken='string',
          MaxResults=123
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the entity exists.

      

    
    :type EntityId: string
    :param EntityId: **[REQUIRED]** 

      The identifier for the entity for which to list the aliases.

      

    
    :type NextToken: string
    :param NextToken: 

      The token to use to retrieve the next page of results. The first call does not contain any tokens.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to return in a single call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Aliases': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Aliases** *(list) --* 

          The entity's paginated aliases.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          The token to use to retrieve the next page of results. The value is "null" when there are no more results to return.

          
    

  .. py:method:: list_group_members(**kwargs)

    

    Returns an overview of the members of a group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListGroupMembers>`_    


    **Request Syntax** 
    ::

      response = client.list_group_members(
          OrganizationId='string',
          GroupId='string',
          NextToken='string',
          MaxResults=123
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the group exists.

      

    
    :type GroupId: string
    :param GroupId: **[REQUIRED]** 

      The identifier for the group to which the members are associated.

      

    
    :type NextToken: string
    :param NextToken: 

      The token to use to retrieve the next page of results. The first call does not contain any tokens.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to return in a single call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Members': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'Type': 'GROUP'|'USER',
                    'State': 'ENABLED'|'DISABLED'|'DELETED',
                    'EnabledDate': datetime(2015, 1, 1),
                    'DisabledDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Members** *(list) --* 

          The members associated to the group.

          
          

          - *(dict) --* 

            The representation of a group member (user or group).

            
            

            - **Id** *(string) --* 

              The identifier of the member.

              
            

            - **Name** *(string) --* 

              The name of the member.

              
            

            - **Type** *(string) --* 

              A member can be a user or group.

              
            

            - **State** *(string) --* 

              The state of the member, which can be ENABLED, DISABLED, or DELETED.

              
            

            - **EnabledDate** *(datetime) --* 

              The date indicating when the member was enabled for Amazon WorkMail use.

              
            

            - **DisabledDate** *(datetime) --* 

              The date indicating when the member was disabled from Amazon WorkMail use.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use to retrieve the next page of results. The first call does not contain any tokens.

          
    

  .. py:method:: list_groups(**kwargs)

    

    Returns summaries of the organization's groups.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListGroups>`_    


    **Request Syntax** 
    ::

      response = client.list_groups(
          OrganizationId='string',
          NextToken='string',
          MaxResults=123
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the groups exist.

      

    
    :type NextToken: string
    :param NextToken: 

      The token to use to retrieve the next page of results. The first call does not contain any tokens.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to return in a single call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Groups': [
                {
                    'Id': 'string',
                    'Email': 'string',
                    'Name': 'string',
                    'State': 'ENABLED'|'DISABLED'|'DELETED',
                    'EnabledDate': datetime(2015, 1, 1),
                    'DisabledDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Groups** *(list) --* 

          The overview of groups for an organization.

          
          

          - *(dict) --* 

            The representation of an Amazon WorkMail group.

            
            

            - **Id** *(string) --* 

              The identifier of the group.

              
            

            - **Email** *(string) --* 

              The email of the group.

              
            

            - **Name** *(string) --* 

              The name of the group.

              
            

            - **State** *(string) --* 

              The state of the group, which can be ENABLED, DISABLED, or DELETED.

              
            

            - **EnabledDate** *(datetime) --* 

              The date indicating when the group was enabled for Amazon WorkMail use.

              
            

            - **DisabledDate** *(datetime) --* 

              The date indicating when the group was disabled from Amazon WorkMail use.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use to retrieve the next page of results. The value is "null" when there are no more results to return.

          
    

  .. py:method:: list_organizations(**kwargs)

    

    Returns summaries of the customer's non-deleted organizations.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListOrganizations>`_    


    **Request Syntax** 
    ::

      response = client.list_organizations(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      The token to use to retrieve the next page of results. The first call does not contain any tokens.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to return in a single call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OrganizationSummaries': [
                {
                    'OrganizationId': 'string',
                    'Alias': 'string',
                    'ErrorMessage': 'string',
                    'State': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OrganizationSummaries** *(list) --* 

          The overview of owned organizations presented as a list of organization summaries.

          
          

          - *(dict) --* 

            The brief overview associated with an organization.

            
            

            - **OrganizationId** *(string) --* 

              The identifier associated with the organization.

              
            

            - **Alias** *(string) --* 

              The alias associated with the organization.

              
            

            - **ErrorMessage** *(string) --* 

              The error message associated with the organization. It is only present if unexpected behavior has occurred with regards to the organization. It provides insight or solutions regarding unexpected behavior.

              
            

            - **State** *(string) --* 

              The state associated with the organization.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use to retrieve the next page of results. The value is "null" when there are no more results to return.

          
    

  .. py:method:: list_resource_delegates(**kwargs)

    

    Lists the delegates associated with a resource. Users and groups can be resource delegates and answer requests on behalf of the resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListResourceDelegates>`_    


    **Request Syntax** 
    ::

      response = client.list_resource_delegates(
          OrganizationId='string',
          ResourceId='string',
          NextToken='string',
          MaxResults=123
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization that contains the resource for which delegates are listed.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The identifier for the resource whose delegates are listed.

      

    
    :type NextToken: string
    :param NextToken: 

      The token used to paginate through the delegates associated with a resource.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The number of maximum results in a page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Delegates': [
                {
                    'Id': 'string',
                    'Type': 'GROUP'|'USER'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Delegates** *(list) --* 

          One page of the resource's delegates.

          
          

          - *(dict) --* 

            The name of the attribute, which is one of the values defined in the UserAttribute enumeration.

            
            

            - **Id** *(string) --* 

              The identifier for the user or group is associated as the resource's delegate.

              
            

            - **Type** *(string) --* 

              The type of the delegate: user or group.

              
        
      
        

        - **NextToken** *(string) --* 

          The token used to paginate through the delegates associated with a resource. While results are still available, it has an associated value. When the last page is reached, the token is empty. 

          
    

  .. py:method:: list_resources(**kwargs)

    

    Returns summaries of the organization's resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListResources>`_    


    **Request Syntax** 
    ::

      response = client.list_resources(
          OrganizationId='string',
          NextToken='string',
          MaxResults=123
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the resources exist.

      

    
    :type NextToken: string
    :param NextToken: 

      The token to use to retrieve the next page of results. The first call does not contain any tokens.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to return in a single call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Resources': [
                {
                    'Id': 'string',
                    'Email': 'string',
                    'Name': 'string',
                    'Type': 'ROOM'|'EQUIPMENT',
                    'State': 'ENABLED'|'DISABLED'|'DELETED',
                    'EnabledDate': datetime(2015, 1, 1),
                    'DisabledDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Resources** *(list) --* 

          One page of the organization's resource representation.

          
          

          - *(dict) --* 

            The overview for a resource containing relevant data regarding it.

            
            

            - **Id** *(string) --* 

              The identifier of the resource.

              
            

            - **Email** *(string) --* 

              The email of the resource.

              
            

            - **Name** *(string) --* 

              The name of the resource.

              
            

            - **Type** *(string) --* 

              The type of the resource: equipment or room.

              
            

            - **State** *(string) --* 

              The state of the resource, which can be ENABLED, DISABLED, or DELETED.

              
            

            - **EnabledDate** *(datetime) --* 

              The date indicating when the resource was enabled for Amazon WorkMail use.

              
            

            - **DisabledDate** *(datetime) --* 

              The date indicating when the resource was disabled from Amazon WorkMail use.

              
        
      
        

        - **NextToken** *(string) --* 

          The token used to paginate through all the organization's resources. While results are still available, it has an associated value. When the last page is reached, the token is empty.

          
    

  .. py:method:: list_users(**kwargs)

    

    Returns summaries of the organization's users.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListUsers>`_    


    **Request Syntax** 
    ::

      response = client.list_users(
          OrganizationId='string',
          NextToken='string',
          MaxResults=123
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the users exist.

      

    
    :type NextToken: string
    :param NextToken: 

      TBD

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to return in a single call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Users': [
                {
                    'Id': 'string',
                    'Email': 'string',
                    'Name': 'string',
                    'DisplayName': 'string',
                    'State': 'ENABLED'|'DISABLED'|'DELETED',
                    'UserRole': 'USER'|'RESOURCE'|'SYSTEM_USER',
                    'EnabledDate': datetime(2015, 1, 1),
                    'DisabledDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Users** *(list) --* 

          The overview of users for an organization.

          
          

          - *(dict) --* 

            The representation of an Amazon WorkMail user.

            
            

            - **Id** *(string) --* 

              The identifier of the user.

              
            

            - **Email** *(string) --* 

              The email of the user.

              
            

            - **Name** *(string) --* 

              The name of the user.

              
            

            - **DisplayName** *(string) --* 

              The display name of the user.

              
            

            - **State** *(string) --* 

              The state of the user, which can be ENABLED, DISABLED, or DELETED.

              
            

            - **UserRole** *(string) --* 

              The role of the user.

              
            

            - **EnabledDate** *(datetime) --* 

              The date indicating when the user was enabled for Amazon WorkMail use.

              
            

            - **DisabledDate** *(datetime) --* 

              The date indicating when the user was disabled from Amazon WorkMail use.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.

          
    

  .. py:method:: register_to_work_mail(**kwargs)

    

    Registers an existing and disabled user, group, or resource/entity for Amazon WorkMail use by associating a mailbox and calendaring capabilities. It performs no change if the entity is enabled and fails if the entity is deleted. This operation results in the accumulation of costs. For more information, see `Pricing <http://aws.amazon.com/workmail/pricing>`__ . The equivalent console functionality for this operation is *Enable* . Users can either be created by calling the CreateUser API or they can be synchronized from your directory. For more information, see DeregisterFromWorkMail.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/RegisterToWorkMail>`_    


    **Request Syntax** 
    ::

      response = client.register_to_work_mail(
          OrganizationId='string',
          EntityId='string',
          Email='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier for the organization under which the Amazon WorkMail entity exists.

      

    
    :type EntityId: string
    :param EntityId: **[REQUIRED]** 

      The identifier for the entity to be updated.

      

    
    :type Email: string
    :param Email: **[REQUIRED]** 

      The email for the entity to be updated.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: reset_password(**kwargs)

    

    Allows the administrator to reset the password for a user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ResetPassword>`_    


    **Request Syntax** 
    ::

      response = client.reset_password(
          OrganizationId='string',
          UserId='string',
          Password='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier of the organization that contains the user for which the password is reset.

      

    
    :type UserId: string
    :param UserId: **[REQUIRED]** 

      The identifier of the user for whom the password is reset.

      

    
    :type Password: string
    :param Password: **[REQUIRED]** 

      The new password for the user.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_primary_email_address(**kwargs)

    

    Updates the primary email for an entity. The current email is moved into the list of aliases (or swapped between an existing alias and the current primary email) and the email provided in the input is promoted as the primary.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/UpdatePrimaryEmailAddress>`_    


    **Request Syntax** 
    ::

      response = client.update_primary_email_address(
          OrganizationId='string',
          EntityId='string',
          Email='string'
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The organization that contains the entity to update.

      

    
    :type EntityId: string
    :param EntityId: **[REQUIRED]** 

      The entity to update (user, group, or resource).

      

    
    :type Email: string
    :param Email: **[REQUIRED]** 

      The value of the email to be updated as primary.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_resource(**kwargs)

    

    Updates data for the resource. It must be preceded by a describe call in order to have the latest information. The dataset in the request should be the one expected when performing another describe call.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/UpdateResource>`_    


    **Request Syntax** 
    ::

      response = client.update_resource(
          OrganizationId='string',
          ResourceId='string',
          Name='string',
          BookingOptions={
              'AutoAcceptRequests': True|False,
              'AutoDeclineRecurringRequests': True|False,
              'AutoDeclineConflictingRequests': True|False
          }
      )
    :type OrganizationId: string
    :param OrganizationId: **[REQUIRED]** 

      The identifier associated with the organization for which the resource is updated.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The identifier of the resource to be updated.

      

    
    :type Name: string
    :param Name: 

      The name of the resource to be updated.

      

    
    :type BookingOptions: dict
    :param BookingOptions: 

      The resource's booking options to be updated.

      

    
      - **AutoAcceptRequests** *(boolean) --* 

        The resource's ability to automatically reply to requests. If disabled, delegates must be associated to the resource.

        

      
      - **AutoDeclineRecurringRequests** *(boolean) --* 

        The resource's ability to automatically decline any recurring requests.

        

      
      - **AutoDeclineConflictingRequests** *(boolean) --* 

        The resource's ability to automatically decline any conflicting requests.

        

      
    
    
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
