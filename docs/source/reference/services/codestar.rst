

********
CodeStar
********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CodeStar.Client

  A low-level client representing AWS CodeStar::

    
    import boto3
    
    client = boto3.client('codestar')

  
  These are the available methods:
  
  *   :py:meth:`~CodeStar.Client.associate_team_member`

  
  *   :py:meth:`~CodeStar.Client.can_paginate`

  
  *   :py:meth:`~CodeStar.Client.create_project`

  
  *   :py:meth:`~CodeStar.Client.create_user_profile`

  
  *   :py:meth:`~CodeStar.Client.delete_project`

  
  *   :py:meth:`~CodeStar.Client.delete_user_profile`

  
  *   :py:meth:`~CodeStar.Client.describe_project`

  
  *   :py:meth:`~CodeStar.Client.describe_user_profile`

  
  *   :py:meth:`~CodeStar.Client.disassociate_team_member`

  
  *   :py:meth:`~CodeStar.Client.generate_presigned_url`

  
  *   :py:meth:`~CodeStar.Client.get_paginator`

  
  *   :py:meth:`~CodeStar.Client.get_waiter`

  
  *   :py:meth:`~CodeStar.Client.list_projects`

  
  *   :py:meth:`~CodeStar.Client.list_resources`

  
  *   :py:meth:`~CodeStar.Client.list_tags_for_project`

  
  *   :py:meth:`~CodeStar.Client.list_team_members`

  
  *   :py:meth:`~CodeStar.Client.list_user_profiles`

  
  *   :py:meth:`~CodeStar.Client.tag_project`

  
  *   :py:meth:`~CodeStar.Client.untag_project`

  
  *   :py:meth:`~CodeStar.Client.update_project`

  
  *   :py:meth:`~CodeStar.Client.update_team_member`

  
  *   :py:meth:`~CodeStar.Client.update_user_profile`

  

  .. py:method:: associate_team_member(**kwargs)

    

    Adds an IAM user to the team for an AWS CodeStar project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/AssociateTeamMember>`_    


    **Request Syntax** 
    ::

      response = client.associate_team_member(
          projectId='string',
          clientRequestToken='string',
          userArn='string',
          projectRole='string',
          remoteAccessAllowed=True|False
      )
    :type projectId: string
    :param projectId: **[REQUIRED]** 

      The ID of the project to which you will add the IAM user.

      

    
    :type clientRequestToken: string
    :param clientRequestToken: 

      A user- or system-generated token that identifies the entity that requested the team member association to the project. This token can be used to repeat the request.

      

    
    :type userArn: string
    :param userArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) for the IAM user you want to add to the AWS CodeStar project.

      

    
    :type projectRole: string
    :param projectRole: **[REQUIRED]** 

      The AWS CodeStar project role that will apply to this user. This role determines what actions a user can take in an AWS CodeStar project.

      

    
    :type remoteAccessAllowed: boolean
    :param remoteAccessAllowed: 

      Whether the team member is allowed to use an SSH public/private key pair to remotely access project resources, for example Amazon EC2 instances.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'clientRequestToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **clientRequestToken** *(string) --* 

          The user- or system-generated token from the initial request that can be used to repeat the request.

          
    

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


  .. py:method:: create_project(**kwargs)

    

    Reserved for future use. To create a project, use the AWS CodeStar console.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/CreateProject>`_    


    **Request Syntax** 
    ::

      response = client.create_project(
          name='string',
          id='string',
          description='string',
          clientRequestToken='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      Reserved for future use.

      

    
    :type id: string
    :param id: **[REQUIRED]** 

      Reserved for future use.

      

    
    :type description: string
    :param description: 

      Reserved for future use.

      

    
    :type clientRequestToken: string
    :param clientRequestToken: 

      Reserved for future use.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'arn': 'string',
            'clientRequestToken': 'string',
            'projectTemplateId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **id** *(string) --* 

          Reserved for future use.

          
        

        - **arn** *(string) --* 

          Reserved for future use.

          
        

        - **clientRequestToken** *(string) --* 

          Reserved for future use.

          
        

        - **projectTemplateId** *(string) --* 

          Reserved for future use.

          
    

  .. py:method:: create_user_profile(**kwargs)

    

    Creates a profile for a user that includes user preferences, such as the display name and email address assocciated with the user, in AWS CodeStar. The user profile is not project-specific. Information in the user profile is displayed wherever the user's information appears to other users in AWS CodeStar.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/CreateUserProfile>`_    


    **Request Syntax** 
    ::

      response = client.create_user_profile(
          userArn='string',
          displayName='string',
          emailAddress='string',
          sshPublicKey='string'
      )
    :type userArn: string
    :param userArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the user in IAM.

      

    
    :type displayName: string
    :param displayName: **[REQUIRED]** 

      The name that will be displayed as the friendly name for the user in AWS CodeStar. 

      

    
    :type emailAddress: string
    :param emailAddress: **[REQUIRED]** 

      The email address that will be displayed as part of the user's profile in AWS CodeStar.

      

    
    :type sshPublicKey: string
    :param sshPublicKey: 

      The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user's private key for SSH access.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'userArn': 'string',
            'displayName': 'string',
            'emailAddress': 'string',
            'sshPublicKey': 'string',
            'createdTimestamp': datetime(2015, 1, 1),
            'lastModifiedTimestamp': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **userArn** *(string) --* 

          The Amazon Resource Name (ARN) of the user in IAM.

          
        

        - **displayName** *(string) --* 

          The name that is displayed as the friendly name for the user in AWS CodeStar.

          
        

        - **emailAddress** *(string) --* 

          The email address that is displayed as part of the user's profile in AWS CodeStar.

          
        

        - **sshPublicKey** *(string) --* 

          The SSH public key associated with the user in AWS CodeStar. This is the public portion of the public/private keypair the user can use to access project resources if a project owner allows the user remote access to those resources.

          
        

        - **createdTimestamp** *(datetime) --* 

          The date the user profile was created, in timestamp format.

          
        

        - **lastModifiedTimestamp** *(datetime) --* 

          The date the user profile was last modified, in timestamp format.

          
    

  .. py:method:: delete_project(**kwargs)

    

    Deletes a project, including project resources. Does not delete users associated with the project, but does delete the IAM roles that allowed access to the project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DeleteProject>`_    


    **Request Syntax** 
    ::

      response = client.delete_project(
          id='string',
          clientRequestToken='string',
          deleteStack=True|False
      )
    :type id: string
    :param id: **[REQUIRED]** 

      The ID of the project to be deleted in AWS CodeStar.

      

    
    :type clientRequestToken: string
    :param clientRequestToken: 

      A user- or system-generated token that identifies the entity that requested project deletion. This token can be used to repeat the request. 

      

    
    :type deleteStack: boolean
    :param deleteStack: 

      Whether to send a delete request for the primary stack in AWS CloudFormation originally used to generate the project and its resources. This option will delete all AWS resources for the project (except for any buckets in Amazon S3) as well as deleting the project itself. Recommended for most use cases.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'stackId': 'string',
            'projectArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **stackId** *(string) --* 

          The ID of the primary stack in AWS CloudFormation that will be deleted as part of deleting the project and its resources.

          
        

        - **projectArn** *(string) --* 

          The Amazon Resource Name (ARN) of the deleted project.

          
    

  .. py:method:: delete_user_profile(**kwargs)

    

    Deletes a user profile in AWS CodeStar, including all personal preference data associated with that profile, such as display name and email address. It does not delete the history of that user, for example the history of commits made by that user.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DeleteUserProfile>`_    


    **Request Syntax** 
    ::

      response = client.delete_user_profile(
          userArn='string'
      )
    :type userArn: string
    :param userArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the user to delete from AWS CodeStar.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'userArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **userArn** *(string) --* 

          The Amazon Resource Name (ARN) of the user deleted from AWS CodeStar.

          
    

  .. py:method:: describe_project(**kwargs)

    

    Describes a project and its resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DescribeProject>`_    


    **Request Syntax** 
    ::

      response = client.describe_project(
          id='string'
      )
    :type id: string
    :param id: **[REQUIRED]** 

      The ID of the project.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'id': 'string',
            'arn': 'string',
            'description': 'string',
            'clientRequestToken': 'string',
            'createdTimeStamp': datetime(2015, 1, 1),
            'stackId': 'string',
            'projectTemplateId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The display name for the project.

          
        

        - **id** *(string) --* 

          The ID of the project.

          
        

        - **arn** *(string) --* 

          The Amazon Resource Name (ARN) for the project.

          
        

        - **description** *(string) --* 

          The description of the project, if any.

          
        

        - **clientRequestToken** *(string) --* 

          A user- or system-generated token that identifies the entity that requested project creation. 

          
        

        - **createdTimeStamp** *(datetime) --* 

          The date and time the project was created, in timestamp format.

          
        

        - **stackId** *(string) --* 

          The ID of the primary stack in AWS CloudFormation used to generate resources for the project.

          
        

        - **projectTemplateId** *(string) --* 

          The ID for the AWS CodeStar project template used to create the project.

          
    

  .. py:method:: describe_user_profile(**kwargs)

    

    Describes a user in AWS CodeStar and the user attributes across all projects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DescribeUserProfile>`_    


    **Request Syntax** 
    ::

      response = client.describe_user_profile(
          userArn='string'
      )
    :type userArn: string
    :param userArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the user.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'userArn': 'string',
            'displayName': 'string',
            'emailAddress': 'string',
            'sshPublicKey': 'string',
            'createdTimestamp': datetime(2015, 1, 1),
            'lastModifiedTimestamp': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **userArn** *(string) --* 

          The Amazon Resource Name (ARN) of the user.

          
        

        - **displayName** *(string) --* 

          The display name shown for the user in AWS CodeStar projects. For example, this could be set to both first and last name ("Mary Major") or a single name ("Mary"). The display name is also used to generate the initial icon associated with the user in AWS CodeStar projects. If spaces are included in the display name, the first character that appears after the space will be used as the second character in the user initial icon. The initial icon displays a maximum of two characters, so a display name with more than one space (for example "Mary Jane Major") would generate an initial icon using the first character and the first character after the space ("MJ", not "MM").

          
        

        - **emailAddress** *(string) --* 

          The email address for the user. Optional.

          
        

        - **sshPublicKey** *(string) --* 

          The SSH public key associated with the user. This SSH public key is associated with the user profile, and can be used in conjunction with the associated private key for access to project resources, such as Amazon EC2 instances, if a project owner grants remote access to those resources.

          
        

        - **createdTimestamp** *(datetime) --* 

          The date and time when the user profile was created in AWS CodeStar, in timestamp format.

          
        

        - **lastModifiedTimestamp** *(datetime) --* 

          The date and time when the user profile was last modified, in timestamp format.

          
    

  .. py:method:: disassociate_team_member(**kwargs)

    

    Removes a user from a project. Removing a user from a project also removes the IAM policies from that user that allowed access to the project and its resources. Disassociating a team member does not remove that user's profile from AWS CodeStar. It does not remove the user from IAM.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DisassociateTeamMember>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_team_member(
          projectId='string',
          userArn='string'
      )
    :type projectId: string
    :param projectId: **[REQUIRED]** 

      The ID of the AWS CodeStar project from which you want to remove a team member.

      

    
    :type userArn: string
    :param userArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the IAM user or group whom you want to remove from the project.

      

    
    
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

        


  .. py:method:: list_projects(**kwargs)

    

    Lists all projects in AWS CodeStar associated with your AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListProjects>`_    


    **Request Syntax** 
    ::

      response = client.list_projects(
          nextToken='string',
          maxResults=123
      )
    :type nextToken: string
    :param nextToken: 

      The continuation token to be used to return the next set of results, if the results cannot be returned in one response.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum amount of data that can be contained in a single set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'projects': [
                {
                    'projectId': 'string',
                    'projectArn': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **projects** *(list) --* 

          A list of projects.

          
          

          - *(dict) --* 

            Information about the metadata for a project.

            
            

            - **projectId** *(string) --* 

              The ID of the project.

              
            

            - **projectArn** *(string) --* 

              The Amazon Resource Name (ARN) of the project.

              
        
      
        

        - **nextToken** *(string) --* 

          The continuation token to use when requesting the next set of results, if there are more results to be returned.

          
    

  .. py:method:: list_resources(**kwargs)

    

    Lists resources associated with a project in AWS CodeStar.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListResources>`_    


    **Request Syntax** 
    ::

      response = client.list_resources(
          projectId='string',
          nextToken='string',
          maxResults=123
      )
    :type projectId: string
    :param projectId: **[REQUIRED]** 

      The ID of the project.

      

    
    :type nextToken: string
    :param nextToken: 

      The continuation token for the next set of results, if the results cannot be returned in one response.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum amount of data that can be contained in a single set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resources': [
                {
                    'id': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resources** *(list) --* 

          An array of resources associated with the project. 

          
          

          - *(dict) --* 

            Information about a resource for a project.

            
            

            - **id** *(string) --* 

              The Amazon Resource Name (ARN) of the resource.

              
        
      
        

        - **nextToken** *(string) --* 

          The continuation token to use when requesting the next set of results, if there are more results to be returned.

          
    

  .. py:method:: list_tags_for_project(**kwargs)

    

    Gets the tags for a project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListTagsForProject>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_project(
          id='string',
          nextToken='string',
          maxResults=123
      )
    :type id: string
    :param id: **[REQUIRED]** 

      The ID of the project to get tags for.

      

    
    :type nextToken: string
    :param nextToken: 

      Reserved for future use.

      

    
    :type maxResults: integer
    :param maxResults: 

      Reserved for future use.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tags': {
                'string': 'string'
            },
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tags** *(dict) --* 

          The tags for the project.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **nextToken** *(string) --* 

          Reserved for future use.

          
    

  .. py:method:: list_team_members(**kwargs)

    

    Lists all team members associated with a project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListTeamMembers>`_    


    **Request Syntax** 
    ::

      response = client.list_team_members(
          projectId='string',
          nextToken='string',
          maxResults=123
      )
    :type projectId: string
    :param projectId: **[REQUIRED]** 

      The ID of the project for which you want to list team members.

      

    
    :type nextToken: string
    :param nextToken: 

      The continuation token for the next set of results, if the results cannot be returned in one response.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of team members you want returned in a response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'teamMembers': [
                {
                    'userArn': 'string',
                    'projectRole': 'string',
                    'remoteAccessAllowed': True|False
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **teamMembers** *(list) --* 

          A list of team member objects for the project.

          
          

          - *(dict) --* 

            Information about a team member in a project.

            
            

            - **userArn** *(string) --* 

              The Amazon Resource Name (ARN) of the user in IAM.

              
            

            - **projectRole** *(string) --* 

              The role assigned to the user in the project. Project roles have different levels of access. For more information, see `Working with Teams <http://docs.aws.amazon.com/codestar/latest/userguide/working-with-teams.html>`__ in the *AWS CodeStar User Guide* . 

              
            

            - **remoteAccessAllowed** *(boolean) --* 

              Whether the user is allowed to remotely access project resources using an SSH public/private key pair.

              
        
      
        

        - **nextToken** *(string) --* 

          The continuation token to use when requesting the next set of results, if there are more results to be returned.

          
    

  .. py:method:: list_user_profiles(**kwargs)

    

    Lists all the user profiles configured for your AWS account in AWS CodeStar.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListUserProfiles>`_    


    **Request Syntax** 
    ::

      response = client.list_user_profiles(
          nextToken='string',
          maxResults=123
      )
    :type nextToken: string
    :param nextToken: 

      The continuation token for the next set of results, if the results cannot be returned in one response.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return in a response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'userProfiles': [
                {
                    'userArn': 'string',
                    'displayName': 'string',
                    'emailAddress': 'string',
                    'sshPublicKey': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **userProfiles** *(list) --* 

          All the user profiles configured in AWS CodeStar for an AWS account.

          
          

          - *(dict) --* 

            Information about a user's profile in AWS CodeStar.

            
            

            - **userArn** *(string) --* 

              The Amazon Resource Name (ARN) of the user in IAM.

              
            

            - **displayName** *(string) --* 

              The display name of a user in AWS CodeStar. For example, this could be set to both first and last name ("Mary Major") or a single name ("Mary"). The display name is also used to generate the initial icon associated with the user in AWS CodeStar projects. If spaces are included in the display name, the first character that appears after the space will be used as the second character in the user initial icon. The initial icon displays a maximum of two characters, so a display name with more than one space (for example "Mary Jane Major") would generate an initial icon using the first character and the first character after the space ("MJ", not "MM").

              
            

            - **emailAddress** *(string) --* 

              The email address associated with the user.

              
            

            - **sshPublicKey** *(string) --* 

              The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user's private key for SSH access.

              
        
      
        

        - **nextToken** *(string) --* 

          The continuation token to use when requesting the next set of results, if there are more results to be returned.

          
    

  .. py:method:: tag_project(**kwargs)

    

    Adds tags to a project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/TagProject>`_    


    **Request Syntax** 
    ::

      response = client.tag_project(
          id='string',
          tags={
              'string': 'string'
          }
      )
    :type id: string
    :param id: **[REQUIRED]** 

      The ID of the project you want to add a tag to.

      

    
    :type tags: dict
    :param tags: **[REQUIRED]** 

      The tags you want to add to the project.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tags': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tags** *(dict) --* 

          The tags for the project.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: untag_project(**kwargs)

    

    Removes tags from a project.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/UntagProject>`_    


    **Request Syntax** 
    ::

      response = client.untag_project(
          id='string',
          tags=[
              'string',
          ]
      )
    :type id: string
    :param id: **[REQUIRED]** 

      The ID of the project to remove tags from.

      

    
    :type tags: list
    :param tags: **[REQUIRED]** 

      The tags to remove from the project.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_project(**kwargs)

    

    Updates a project in AWS CodeStar.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/UpdateProject>`_    


    **Request Syntax** 
    ::

      response = client.update_project(
          id='string',
          name='string',
          description='string'
      )
    :type id: string
    :param id: **[REQUIRED]** 

      The ID of the project you want to update.

      

    
    :type name: string
    :param name: 

      The name of the project you want to update.

      

    
    :type description: string
    :param description: 

      The description of the project, if any.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_team_member(**kwargs)

    

    Updates a team member's attributes in an AWS CodeStar project. For example, you can change a team member's role in the project, or change whether they have remote access to project resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/UpdateTeamMember>`_    


    **Request Syntax** 
    ::

      response = client.update_team_member(
          projectId='string',
          userArn='string',
          projectRole='string',
          remoteAccessAllowed=True|False
      )
    :type projectId: string
    :param projectId: **[REQUIRED]** 

      The ID of the project.

      

    
    :type userArn: string
    :param userArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the user for whom you want to change team membership attributes.

      

    
    :type projectRole: string
    :param projectRole: 

      The role assigned to the user in the project. Project roles have different levels of access. For more information, see `Working with Teams <http://docs.aws.amazon.com/codestar/latest/userguide/working-with-teams.html>`__ in the *AWS CodeStar User Guide* .

      

    
    :type remoteAccessAllowed: boolean
    :param remoteAccessAllowed: 

      Whether a team member is allowed to remotely access project resources using the SSH public key associated with the user's profile. Even if this is set to True, the user must associate a public key with their profile before the user can access resources.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'userArn': 'string',
            'projectRole': 'string',
            'remoteAccessAllowed': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **userArn** *(string) --* 

          The Amazon Resource Name (ARN) of the user whose team membership attributes were updated.

          
        

        - **projectRole** *(string) --* 

          The project role granted to the user.

          
        

        - **remoteAccessAllowed** *(boolean) --* 

          Whether a team member is allowed to remotely access project resources using the SSH public key associated with the user's profile.

          
    

  .. py:method:: update_user_profile(**kwargs)

    

    Updates a user's profile in AWS CodeStar. The user profile is not project-specific. Information in the user profile is displayed wherever the user's information appears to other users in AWS CodeStar. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/UpdateUserProfile>`_    


    **Request Syntax** 
    ::

      response = client.update_user_profile(
          userArn='string',
          displayName='string',
          emailAddress='string',
          sshPublicKey='string'
      )
    :type userArn: string
    :param userArn: **[REQUIRED]** 

      The name that will be displayed as the friendly name for the user in AWS CodeStar.

      

    
    :type displayName: string
    :param displayName: 

      The name that is displayed as the friendly name for the user in AWS CodeStar.

      

    
    :type emailAddress: string
    :param emailAddress: 

      The email address that is displayed as part of the user's profile in AWS CodeStar.

      

    
    :type sshPublicKey: string
    :param sshPublicKey: 

      The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user's private key for SSH access.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'userArn': 'string',
            'displayName': 'string',
            'emailAddress': 'string',
            'sshPublicKey': 'string',
            'createdTimestamp': datetime(2015, 1, 1),
            'lastModifiedTimestamp': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **userArn** *(string) --* 

          The Amazon Resource Name (ARN) of the user in IAM.

          
        

        - **displayName** *(string) --* 

          The name that is displayed as the friendly name for the user in AWS CodeStar.

          
        

        - **emailAddress** *(string) --* 

          The email address that is displayed as part of the user's profile in AWS CodeStar.

          
        

        - **sshPublicKey** *(string) --* 

          The SSH public key associated with the user in AWS CodeStar. This is the public portion of the public/private keypair the user can use to access project resources if a project owner allows the user remote access to those resources.

          
        

        - **createdTimestamp** *(datetime) --* 

          The date the user profile was created, in timestamp format.

          
        

        - **lastModifiedTimestamp** *(datetime) --* 

          The date the user profile was last modified, in timestamp format.

          
    

==========
Paginators
==========


The available paginators are:
