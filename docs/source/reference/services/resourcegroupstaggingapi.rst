

************************
ResourceGroupsTaggingAPI
************************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ResourceGroupsTaggingAPI.Client

  A low-level client representing AWS Resource Groups Tagging API::

    
    import boto3
    
    client = boto3.client('resourcegroupstaggingapi')

  
  These are the available methods:
  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.can_paginate`

  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.generate_presigned_url`

  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.get_paginator`

  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.get_resources`

  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.get_tag_keys`

  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.get_tag_values`

  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.get_waiter`

  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.tag_resources`

  
  *   :py:meth:`~ResourceGroupsTaggingAPI.Client.untag_resources`

  

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


  .. py:method:: get_resources(**kwargs)

    

    Returns all the tagged resources that are associated with the specified tags (keys and values) located in the specified region for the AWS account. The tags and the resource types that you specify in the request are known as *filters* . The response includes all tags that are associated with the requested resources. If no filter is provided, this action returns a paginated resource list with the associated tags.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetResources>`_    


    **Request Syntax** 
    ::

      response = client.get_resources(
          PaginationToken='string',
          TagFilters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          ResourcesPerPage=123,
          TagsPerPage=123,
          ResourceTypeFilters=[
              'string',
          ]
      )
    :type PaginationToken: string
    :param PaginationToken: 

      A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a ``PaginationToken`` , use that string for this value to request an additional page of data.

      

    
    :type TagFilters: list
    :param TagFilters: 

      A list of tags (keys and values). A request can include up to 50 keys, and each key can include up to 20 values.

       

      If you specify multiple filters connected by an AND operator in a single request, the response returns only those resources that are associated with every specified filter.

       

      If you specify multiple filters connected by an OR operator in a single request, the response returns all resources that are associated with at least one or possibly more of the specified filters.

      

    
      - *(dict) --* 

        A list of tags (keys and values) that are used to specify the associated resources.

        

      
        - **Key** *(string) --* 

          One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

          

        
        - **Values** *(list) --* 

          The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

          

        
          - *(string) --* 

          
      
      
  
    :type ResourcesPerPage: integer
    :param ResourcesPerPage: 

      A limit that restricts the number of resources returned by GetResources in paginated output. You can set ResourcesPerPage to a minimum of 1 item and the maximum of 50 items. 

      

    
    :type TagsPerPage: integer
    :param TagsPerPage: 

      A limit that restricts the number of tags (key and value pairs) returned by GetResources in paginated output. A resource with no tags is counted as having one tag (one key and value pair).

       

       ``GetResources`` does not split a resource and its associated tags across pages. If the specified ``TagsPerPage`` would cause such a break, a ``PaginationToken`` is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a ``TagsPerPage`` of ``100`` and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of 3 pages, with the first page displaying the first 10 resources, each with its 10 tags, the second page displaying the next 10 resources each with its 10 tags, and the third page displaying the remaining 2 resources, each with its 10 tags.

       

      

       

      You can set ``TagsPerPage`` to a minimum of 100 items and the maximum of 500 items.

      

    
    :type ResourceTypeFilters: list
    :param ResourceTypeFilters: 

      The constraints on the resources that you want returned. The format of each resource type is ``service[:resourceType]`` . For example, specifying a resource type of ``ec2`` returns all tagged Amazon EC2 resources (which includes tagged EC2 instances). Specifying a resource type of ``ec2:instance`` returns only EC2 instances. 

       

      The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN). Consult the *AWS General Reference* for the following:

       

       
      * For a list of service name strings, see `AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__ . 
       
      * For resource type strings, see `Example ARNs <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax>`__ . 
       
      * For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ . 
       

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PaginationToken': 'string',
            'ResourceTagMappingList': [
                {
                    'ResourceARN': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PaginationToken** *(string) --* 

          A string that indicates that the response contains more data than can be returned in a single response. To receive additional data, specify this string for the ``PaginationToken`` value in a subsequent request.

          
        

        - **ResourceTagMappingList** *(list) --* 

          A list of resource ARNs and the tags (keys and values) associated with each.

          
          

          - *(dict) --* 

            A list of resource ARNs and the tags (keys and values) that are associated with each.

            
            

            - **ResourceARN** *(string) --* 

              An array of resource ARN(s).

              
            

            - **Tags** *(list) --* 

              The tags that have been applied to one or more AWS resources.

              
              

              - *(dict) --* 

                The metadata that you apply to AWS resources to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information, see `Tag Basics <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in the *Amazon EC2 User Guide for Linux Instances* .

                
                

                - **Key** *(string) --* 

                  One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

                  
                

                - **Value** *(string) --* 

                  The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

                  
            
          
        
      
    

  .. py:method:: get_tag_keys(**kwargs)

    

    Returns all tag keys in the specified region for the AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetTagKeys>`_    


    **Request Syntax** 
    ::

      response = client.get_tag_keys(
          PaginationToken='string'
      )
    :type PaginationToken: string
    :param PaginationToken: 

      A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken, use that string for this value to request an additional page of data.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PaginationToken': 'string',
            'TagKeys': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PaginationToken** *(string) --* 

          A string that indicates that the response contains more data than can be returned in a single response. To receive additional data, specify this string for the ``PaginationToken`` value in a subsequent request.

          
        

        - **TagKeys** *(list) --* 

          A list of all tag keys in the AWS account.

          
          

          - *(string) --* 
      
    

  .. py:method:: get_tag_values(**kwargs)

    

    Returns all tag values for the specified key in the specified region for the AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetTagValues>`_    


    **Request Syntax** 
    ::

      response = client.get_tag_values(
          PaginationToken='string',
          Key='string'
      )
    :type PaginationToken: string
    :param PaginationToken: 

      A string that indicates that additional data is available. Leave this value empty for your initial request. If the response includes a PaginationToken, use that string for this value to request an additional page of data.

      

    
    :type Key: string
    :param Key: **[REQUIRED]** 

      The key for which you want to list all existing values in the specified region for the AWS account.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PaginationToken': 'string',
            'TagValues': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PaginationToken** *(string) --* 

          A string that indicates that the response contains more data than can be returned in a single response. To receive additional data, specify this string for the ``PaginationToken`` value in a subsequent request.

          
        

        - **TagValues** *(list) --* 

          A list of all tag values for the specified key in the AWS account.

          
          

          - *(string) --* 
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: tag_resources(**kwargs)

    

    Applies one or more tags to the specified resources. Note the following:

     

     
    * Not all resources can have tags. For a list of resources that support tagging, see `Supported Resources <http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/supported-resources.html>`__ in the *AWS Resource Groups and Tag Editor User Guide* . 
     
    * Each resource can have up to 50 tags. For other limits, see `Tag Restrictions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions>`__ in the *Amazon EC2 User Guide for Linux Instances* . 
     
    * You can only tag resources that are located in the specified region for the AWS account. 
     
    * To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see `Obtaining Permissions for Tagging <http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/obtaining-permissions-for-tagging.html>`__ in the *AWS Resource Groups and Tag Editor User Guide* . 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/TagResources>`_    


    **Request Syntax** 
    ::

      response = client.tag_resources(
          ResourceARNList=[
              'string',
          ],
          Tags={
              'string': 'string'
          }
      )
    :type ResourceARNList: list
    :param ResourceARNList: **[REQUIRED]** 

      A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. You can specify a minimum of 1 and a maximum of 20 ARNs (resources) to tag. An ARN can be set to a maximum of 1600 characters. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .

      

    
      - *(string) --* 

      
  
    :type Tags: dict
    :param Tags: **[REQUIRED]** 

      The tags that you want to add to the specified resources. A tag consists of a key and a value that you define.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedResourcesMap': {
                'string': {
                    'StatusCode': 123,
                    'ErrorCode': 'InternalServiceException'|'InvalidParameterException',
                    'ErrorMessage': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FailedResourcesMap** *(dict) --* 

          Details of resources that could not be tagged. An error code, status code, and error message are returned for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Details of the common errors that all actions return.

              
              

              - **StatusCode** *(integer) --* 

                The HTTP status code of the common error.

                
              

              - **ErrorCode** *(string) --* 

                The code of the common error. Valid values include ``InternalServiceException`` , ``InvalidParameterException`` , and any valid error code returned by the AWS service that hosts the resource that you want to tag.

                
              

              - **ErrorMessage** *(string) --* 

                The message of the common error.

                
          
      
    
    

  .. py:method:: untag_resources(**kwargs)

    

    Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:

     

     
    * To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see `Obtaining Permissions for Tagging <http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/obtaining-permissions-for-tagging.html>`__ in the *AWS Resource Groups and Tag Editor User Guide* . 
     
    * You can only tag resources that are located in the specified region for the AWS account. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/UntagResources>`_    


    **Request Syntax** 
    ::

      response = client.untag_resources(
          ResourceARNList=[
              'string',
          ],
          TagKeys=[
              'string',
          ]
      )
    :type ResourceARNList: list
    :param ResourceARNList: **[REQUIRED]** 

      A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a resource. You can specify a minimum of 1 and a maximum of 20 ARNs (resources) to untag. An ARN can be set to a maximum of 1600 characters. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .

      

    
      - *(string) --* 

      
  
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      A list of the tag keys that you want to remove from the specified resources.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedResourcesMap': {
                'string': {
                    'StatusCode': 123,
                    'ErrorCode': 'InternalServiceException'|'InvalidParameterException',
                    'ErrorMessage': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FailedResourcesMap** *(dict) --* 

          Details of resources that could not be untagged. An error code, status code, and error message are returned for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Details of the common errors that all actions return.

              
              

              - **StatusCode** *(integer) --* 

                The HTTP status code of the common error.

                
              

              - **ErrorCode** *(string) --* 

                The code of the common error. Valid values include ``InternalServiceException`` , ``InvalidParameterException`` , and any valid error code returned by the AWS service that hosts the resource that you want to tag.

                
              

              - **ErrorMessage** *(string) --* 

                The message of the common error.

                
          
      
    
    

==========
Paginators
==========


The available paginators are:

* :py:class:`ResourceGroupsTaggingAPI.Paginator.GetResources`


* :py:class:`ResourceGroupsTaggingAPI.Paginator.GetTagKeys`


* :py:class:`ResourceGroupsTaggingAPI.Paginator.GetTagValues`



.. py:class:: ResourceGroupsTaggingAPI.Paginator.GetResources

  ::

    
    paginator = client.get_paginator('get_resources')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ResourceGroupsTaggingAPI.Client.get_resources`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetResources>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          TagFilters=[
              {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          TagsPerPage=123,
          ResourceTypeFilters=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type TagFilters: list
    :param TagFilters: 

      A list of tags (keys and values). A request can include up to 50 keys, and each key can include up to 20 values.

       

      If you specify multiple filters connected by an AND operator in a single request, the response returns only those resources that are associated with every specified filter.

       

      If you specify multiple filters connected by an OR operator in a single request, the response returns all resources that are associated with at least one or possibly more of the specified filters.

      

    
      - *(dict) --* 

        A list of tags (keys and values) that are used to specify the associated resources.

        

      
        - **Key** *(string) --* 

          One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

          

        
        - **Values** *(list) --* 

          The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

          

        
          - *(string) --* 

          
      
      
  
    :type TagsPerPage: integer
    :param TagsPerPage: 

      A limit that restricts the number of tags (key and value pairs) returned by GetResources in paginated output. A resource with no tags is counted as having one tag (one key and value pair).

       

       ``GetResources`` does not split a resource and its associated tags across pages. If the specified ``TagsPerPage`` would cause such a break, a ``PaginationToken`` is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a ``TagsPerPage`` of ``100`` and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of 3 pages, with the first page displaying the first 10 resources, each with its 10 tags, the second page displaying the next 10 resources each with its 10 tags, and the third page displaying the remaining 2 resources, each with its 10 tags.

       

      

       

      You can set ``TagsPerPage`` to a minimum of 100 items and the maximum of 500 items.

      

    
    :type ResourceTypeFilters: list
    :param ResourceTypeFilters: 

      The constraints on the resources that you want returned. The format of each resource type is ``service[:resourceType]`` . For example, specifying a resource type of ``ec2`` returns all tagged Amazon EC2 resources (which includes tagged EC2 instances). Specifying a resource type of ``ec2:instance`` returns only EC2 instances. 

       

      The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN). Consult the *AWS General Reference* for the following:

       

       
      * For a list of service name strings, see `AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__ . 
       
      * For resource type strings, see `Example ARNs <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax>`__ . 
       
      * For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ . 
       

      

    
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
            'ResourceTagMappingList': [
                {
                    'ResourceARN': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceTagMappingList** *(list) --* 

          A list of resource ARNs and the tags (keys and values) associated with each.

          
          

          - *(dict) --* 

            A list of resource ARNs and the tags (keys and values) that are associated with each.

            
            

            - **ResourceARN** *(string) --* 

              An array of resource ARN(s).

              
            

            - **Tags** *(list) --* 

              The tags that have been applied to one or more AWS resources.

              
              

              - *(dict) --* 

                The metadata that you apply to AWS resources to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information, see `Tag Basics <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in the *Amazon EC2 User Guide for Linux Instances* .

                
                

                - **Key** *(string) --* 

                  One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

                  
                

                - **Value** *(string) --* 

                  The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ResourceGroupsTaggingAPI.Paginator.GetTagKeys

  ::

    
    paginator = client.get_paginator('get_tag_keys')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ResourceGroupsTaggingAPI.Client.get_tag_keys`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetTagKeys>`_    


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
            'TagKeys': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TagKeys** *(list) --* 

          A list of all tag keys in the AWS account.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ResourceGroupsTaggingAPI.Paginator.GetTagValues

  ::

    
    paginator = client.get_paginator('get_tag_values')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ResourceGroupsTaggingAPI.Client.get_tag_values`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetTagValues>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Key='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type Key: string
    :param Key: **[REQUIRED]** 

      The key for which you want to list all existing values in the specified region for the AWS account.

      

    
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
            'TagValues': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TagValues** *(list) --* 

          A list of all tag values for the specified key in the AWS account.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    