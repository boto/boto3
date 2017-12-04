

**************
ResourceGroups
**************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ResourceGroups.Client

  A low-level client representing AWS Resource Groups::

    
    import boto3
    
    client = boto3.client('resource-groups')

  
  These are the available methods:
  
  *   :py:meth:`~ResourceGroups.Client.can_paginate`

  
  *   :py:meth:`~ResourceGroups.Client.create_group`

  
  *   :py:meth:`~ResourceGroups.Client.delete_group`

  
  *   :py:meth:`~ResourceGroups.Client.generate_presigned_url`

  
  *   :py:meth:`~ResourceGroups.Client.get_group`

  
  *   :py:meth:`~ResourceGroups.Client.get_group_query`

  
  *   :py:meth:`~ResourceGroups.Client.get_paginator`

  
  *   :py:meth:`~ResourceGroups.Client.get_tags`

  
  *   :py:meth:`~ResourceGroups.Client.get_waiter`

  
  *   :py:meth:`~ResourceGroups.Client.list_group_resources`

  
  *   :py:meth:`~ResourceGroups.Client.list_groups`

  
  *   :py:meth:`~ResourceGroups.Client.search_resources`

  
  *   :py:meth:`~ResourceGroups.Client.tag`

  
  *   :py:meth:`~ResourceGroups.Client.untag`

  
  *   :py:meth:`~ResourceGroups.Client.update_group`

  
  *   :py:meth:`~ResourceGroups.Client.update_group_query`

  

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


  .. py:method:: create_group(**kwargs)

    

    Creates a group with a specified name, description, and resource query.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/CreateGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_group(
          Name='string',
          Description='string',
          ResourceQuery={
              'Type': 'TAG_FILTERS_1_0',
              'Query': 'string'
          },
          Tags={
              'string': 'string'
          }
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the group, which is the identifier of the group in other operations. A resource group name cannot be updated after it is created. A resource group name can have a maximum of 127 characters, including letters, numbers, hyphens, dots, and underscores. The name cannot start with ``AWS`` or ``aws`` ; these are reserved. A resource group name must be unique within your account.

      

    
    :type Description: string
    :param Description: 

      The description of the resource group. Descriptions can have a maximum of 511 characters, including letters, numbers, hyphens, underscores, punctuation, and spaces.

      

    
    :type ResourceQuery: dict
    :param ResourceQuery: **[REQUIRED]** 

      The resource query that determines which AWS resources are members of this group.

      

    
      - **Type** *(string) --* **[REQUIRED]** 

        The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .

         

         * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.

        

      
      - **Query** *(string) --* **[REQUIRED]** 

        The query that defines a group or a search.

        

      
    
    :type Tags: dict
    :param Tags: 

      The tags to add to the group. A tag is a string-to-string map of key-value pairs. Tag keys can have a maximum character length of 127 characters, and tag values can have a maximum length of 255 characters.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Group': {
                'GroupArn': 'string',
                'Name': 'string',
                'Description': 'string'
            },
            'ResourceQuery': {
                'Type': 'TAG_FILTERS_1_0',
                'Query': 'string'
            },
            'Tags': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Group** *(dict) --* 

          A full description of the resource group after it is created.

          
          

          - **GroupArn** *(string) --* 

            The ARN of a resource group.

            
          

          - **Name** *(string) --* 

            The name of a resource group.

            
          

          - **Description** *(string) --* 

            The description of the resource group.

            
      
        

        - **ResourceQuery** *(dict) --* 

          The resource query associated with the group.

          
          

          - **Type** *(string) --* 

            The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .

             

             * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.

            
          

          - **Query** *(string) --* 

            The query that defines a group or a search.

            
      
        

        - **Tags** *(dict) --* 

          The tags associated with the group.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: delete_group(**kwargs)

    

    Deletes a specified resource group. Deleting a resource group does not delete resources that are members of the group; it only deletes the group structure.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/DeleteGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_group(
          GroupName='string'
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the resource group to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Group': {
                'GroupArn': 'string',
                'Name': 'string',
                'Description': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Group** *(dict) --* 

          A full description of the deleted resource group.

          
          

          - **GroupArn** *(string) --* 

            The ARN of a resource group.

            
          

          - **Name** *(string) --* 

            The name of a resource group.

            
          

          - **Description** *(string) --* 

            The description of the resource group.

            
      
    

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


  .. py:method:: get_group(**kwargs)

    

    Returns information about a specified resource group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/GetGroup>`_    


    **Request Syntax** 
    ::

      response = client.get_group(
          GroupName='string'
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the resource group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Group': {
                'GroupArn': 'string',
                'Name': 'string',
                'Description': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Group** *(dict) --* 

          A full description of the resource group.

          
          

          - **GroupArn** *(string) --* 

            The ARN of a resource group.

            
          

          - **Name** *(string) --* 

            The name of a resource group.

            
          

          - **Description** *(string) --* 

            The description of the resource group.

            
      
    

  .. py:method:: get_group_query(**kwargs)

    

    Returns the resource query associated with the specified resource group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/GetGroupQuery>`_    


    **Request Syntax** 
    ::

      response = client.get_group_query(
          GroupName='string'
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the resource group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GroupQuery': {
                'GroupName': 'string',
                'ResourceQuery': {
                    'Type': 'TAG_FILTERS_1_0',
                    'Query': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **GroupQuery** *(dict) --* 

          The resource query associated with the specified group.

          
          

          - **GroupName** *(string) --* 

            The name of a resource group that is associated with a specific resource query.

            
          

          - **ResourceQuery** *(dict) --* 

            The resource query which determines which AWS resources are members of the associated resource group.

            
            

            - **Type** *(string) --* 

              The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .

               

               * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.

              
            

            - **Query** *(string) --* 

              The query that defines a group or a search.

              
        
      
    

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


  .. py:method:: get_tags(**kwargs)

    

    Returns a list of tags that are associated with a resource, specified by an ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/GetTags>`_    


    **Request Syntax** 
    ::

      response = client.get_tags(
          Arn='string'
      )
    :type Arn: string
    :param Arn: **[REQUIRED]** 

      The ARN of the resource for which you want a list of tags. The resource must exist within the account you are using.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'Tags': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* 

          The ARN of the tagged resource.

          
        

        - **Tags** *(dict) --* 

          The tags associated with the specified resource.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_group_resources(**kwargs)

    

    Returns a list of ARNs of resources that are members of a specified resource group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroupResources>`_    


    **Request Syntax** 
    ::

      response = client.list_group_resources(
          GroupName='string',
          MaxResults=123,
          NextToken='string'
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the resource group.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of group member ARNs that are returned in a single call by ListGroupResources, in paginated output. By default, this number is 50.

      

    
    :type NextToken: string
    :param NextToken: 

      The NextToken value that is returned in a paginated ListGroupResources request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceIdentifiers': [
                {
                    'ResourceArn': 'string',
                    'ResourceType': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceIdentifiers** *(list) --* 

          The ARNs and resource types of resources that are members of the group that you specified.

          
          

          - *(dict) --* 

            The ARN of a resource, and its resource type.

            
            

            - **ResourceArn** *(string) --* 

              The ARN of a resource.

              
            

            - **ResourceType** *(string) --* 

              The resource type of a resource, such as ``AWS::EC2::Instance`` .

              
        
      
        

        - **NextToken** *(string) --* 

          The NextToken value to include in a subsequent ``ListGroupResources`` request, to get more results.

          
    

  .. py:method:: list_groups(**kwargs)

    

    Returns a list of existing resource groups in your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroups>`_    


    **Request Syntax** 
    ::

      response = client.list_groups(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of resource group results that are returned by ListGroups in paginated output. By default, this number is 50.

      

    
    :type NextToken: string
    :param NextToken: 

      The NextToken value that is returned in a paginated ``ListGroups`` request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Groups': [
                {
                    'GroupArn': 'string',
                    'Name': 'string',
                    'Description': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Groups** *(list) --* 

          A list of resource groups.

          
          

          - *(dict) --* 

            A resource group.

            
            

            - **GroupArn** *(string) --* 

              The ARN of a resource group.

              
            

            - **Name** *(string) --* 

              The name of a resource group.

              
            

            - **Description** *(string) --* 

              The description of the resource group.

              
        
      
        

        - **NextToken** *(string) --* 

          The NextToken value to include in a subsequent ``ListGroups`` request, to get more results.

          
    

  .. py:method:: search_resources(**kwargs)

    

    Returns a list of AWS resource identifiers that matches a specified query. The query uses the same format as a resource query in a CreateGroup or UpdateGroupQuery operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/SearchResources>`_    


    **Request Syntax** 
    ::

      response = client.search_resources(
          ResourceQuery={
              'Type': 'TAG_FILTERS_1_0',
              'Query': 'string'
          },
          MaxResults=123,
          NextToken='string'
      )
    :type ResourceQuery: dict
    :param ResourceQuery: **[REQUIRED]** 

      The search query, using the same formats that are supported for resource group definition.

      

    
      - **Type** *(string) --* **[REQUIRED]** 

        The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .

         

         * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.

        

      
      - **Query** *(string) --* **[REQUIRED]** 

        The query that defines a group or a search.

        

      
    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of group member ARNs returned by ``SearchResources`` in paginated output. By default, this number is 50.

      

    
    :type NextToken: string
    :param NextToken: 

      The NextToken value that is returned in a paginated ``SearchResources`` request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceIdentifiers': [
                {
                    'ResourceArn': 'string',
                    'ResourceType': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceIdentifiers** *(list) --* 

          The ARNs and resource types of resources that are members of the group that you specified.

          
          

          - *(dict) --* 

            The ARN of a resource, and its resource type.

            
            

            - **ResourceArn** *(string) --* 

              The ARN of a resource.

              
            

            - **ResourceType** *(string) --* 

              The resource type of a resource, such as ``AWS::EC2::Instance`` .

              
        
      
        

        - **NextToken** *(string) --* 

          The NextToken value to include in a subsequent ``SearchResources`` request, to get more results.

          
    

  .. py:method:: tag(**kwargs)

    

    Adds specified tags to a resource with the specified ARN. Existing tags on a resource are not changed if they are not specified in the request parameters.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/Tag>`_    


    **Request Syntax** 
    ::

      response = client.tag(
          Arn='string',
          Tags={
              'string': 'string'
          }
      )
    :type Arn: string
    :param Arn: **[REQUIRED]** 

      The ARN of the resource to which to add tags.

      

    
    :type Tags: dict
    :param Tags: **[REQUIRED]** 

      The tags to add to the specified resource. A tag is a string-to-string map of key-value pairs. Tag keys can have a maximum character length of 127 characters, and tag values can have a maximum length of 255 characters.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'Tags': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* 

          The ARN of the tagged resource.

          
        

        - **Tags** *(dict) --* 

          The tags that have been added to the specified resource.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: untag(**kwargs)

    

    Deletes specified tags from a specified resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/Untag>`_    


    **Request Syntax** 
    ::

      response = client.untag(
          Arn='string',
          Keys=[
              'string',
          ]
      )
    :type Arn: string
    :param Arn: **[REQUIRED]** 

      The ARN of the resource from which to remove tags.

      

    
    :type Keys: list
    :param Keys: **[REQUIRED]** 

      The keys of the tags to be removed.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Arn': 'string',
            'Keys': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Arn** *(string) --* 

          The ARN of the resource from which tags have been removed.

          
        

        - **Keys** *(list) --* 

          The keys of tags that have been removed.

          
          

          - *(string) --* 
      
    

  .. py:method:: update_group(**kwargs)

    

    Updates an existing group with a new or changed description. You cannot update the name of a resource group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/UpdateGroup>`_    


    **Request Syntax** 
    ::

      response = client.update_group(
          GroupName='string',
          Description='string'
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the resource group for which you want to update its description.

      

    
    :type Description: string
    :param Description: 

      The description of the resource group. Descriptions can have a maximum of 511 characters, including letters, numbers, hyphens, underscores, punctuation, and spaces.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Group': {
                'GroupArn': 'string',
                'Name': 'string',
                'Description': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Group** *(dict) --* 

          The full description of the resource group after it has been updated.

          
          

          - **GroupArn** *(string) --* 

            The ARN of a resource group.

            
          

          - **Name** *(string) --* 

            The name of a resource group.

            
          

          - **Description** *(string) --* 

            The description of the resource group.

            
      
    

  .. py:method:: update_group_query(**kwargs)

    

    Updates the resource query of a group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/UpdateGroupQuery>`_    


    **Request Syntax** 
    ::

      response = client.update_group_query(
          GroupName='string',
          ResourceQuery={
              'Type': 'TAG_FILTERS_1_0',
              'Query': 'string'
          }
      )
    :type GroupName: string
    :param GroupName: **[REQUIRED]** 

      The name of the resource group for which you want to edit the query.

      

    
    :type ResourceQuery: dict
    :param ResourceQuery: **[REQUIRED]** 

      The resource query that determines which AWS resources are members of the resource group.

      

    
      - **Type** *(string) --* **[REQUIRED]** 

        The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .

         

         * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.

        

      
      - **Query** *(string) --* **[REQUIRED]** 

        The query that defines a group or a search.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GroupQuery': {
                'GroupName': 'string',
                'ResourceQuery': {
                    'Type': 'TAG_FILTERS_1_0',
                    'Query': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **GroupQuery** *(dict) --* 

          The resource query associated with the resource group after the update.

          
          

          - **GroupName** *(string) --* 

            The name of a resource group that is associated with a specific resource query.

            
          

          - **ResourceQuery** *(dict) --* 

            The resource query which determines which AWS resources are members of the associated resource group.

            
            

            - **Type** *(string) --* 

              The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .

               

               * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.

              
            

            - **Query** *(string) --* 

              The query that defines a group or a search.

              
        
      
    

==========
Paginators
==========


The available paginators are:
