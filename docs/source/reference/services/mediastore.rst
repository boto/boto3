

**********
MediaStore
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: MediaStore.Client

  A low-level client representing AWS Elemental MediaStore::

    
    import boto3
    
    client = boto3.client('mediastore')

  
  These are the available methods:
  
  *   :py:meth:`~MediaStore.Client.can_paginate`

  
  *   :py:meth:`~MediaStore.Client.create_container`

  
  *   :py:meth:`~MediaStore.Client.delete_container`

  
  *   :py:meth:`~MediaStore.Client.delete_container_policy`

  
  *   :py:meth:`~MediaStore.Client.describe_container`

  
  *   :py:meth:`~MediaStore.Client.generate_presigned_url`

  
  *   :py:meth:`~MediaStore.Client.get_container_policy`

  
  *   :py:meth:`~MediaStore.Client.get_paginator`

  
  *   :py:meth:`~MediaStore.Client.get_waiter`

  
  *   :py:meth:`~MediaStore.Client.list_containers`

  
  *   :py:meth:`~MediaStore.Client.put_container_policy`

  

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


  .. py:method:: create_container(**kwargs)

    

    Creates a storage container to hold objects. A container is similar to a bucket in the Amazon S3 service.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/CreateContainer>`_    


    **Request Syntax** 
    ::

      response = client.create_container(
          ContainerName='string'
      )
    :type ContainerName: string
    :param ContainerName: **[REQUIRED]** 

      The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named ``movies`` in every region, as long as you don’t have an existing container with that name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Container': {
                'Endpoint': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'ARN': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'CREATING'|'DELETING'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Container** *(dict) --* 

          ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN has the following format: arn:aws:<region>:<account that owns this container>:container/<name of container>. For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 

           

          ContainerName: The container name as specified in the request.

           

          CreationTime: Unix timestamp.

           

          Status: The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When an endpoint is available, the status changes to ``ACTIVE`` .

           

          The return value does not include the container's endpoint. To make downstream requests, you must obtain this value by using  DescribeContainer or  ListContainers .

          
          

          - **Endpoint** *(string) --* 

            The DNS endpoint of the container. Use from 1 to 255 characters. Use this endpoint to identify this container when sending requests to the data plane. 

            
          

          - **CreationTime** *(datetime) --* 

            Unix timestamp.

            
          

          - **ARN** *(string) --* 

            The Amazon Resource Name (ARN) of the container. The ARN has the following format:

             

            arn:aws:<region>:<account that owns this container>:container/<name of container> 

             

            For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 

            
          

          - **Name** *(string) --* 

            The name of the container.

            
          

          - **Status** *(string) --* 

            The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When the endpoint is available, the status changes to ``ACTIVE`` .

            
      
    

  .. py:method:: delete_container(**kwargs)

    

    Deletes the specified container. Before you make a ``DeleteContainer`` request, delete any objects in the container or in any folders in the container. You can delete only empty containers. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteContainer>`_    


    **Request Syntax** 
    ::

      response = client.delete_container(
          ContainerName='string'
      )
    :type ContainerName: string
    :param ContainerName: **[REQUIRED]** 

      The name of the container to delete. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_container_policy(**kwargs)

    

    Deletes the access policy that is associated with the specified container.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteContainerPolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_container_policy(
          ContainerName='string'
      )
    :type ContainerName: string
    :param ContainerName: **[REQUIRED]** 

      The name of the container that holds the policy.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_container(**kwargs)

    

    Retrieves the properties of the requested container. This returns a single ``Container`` object based on ``ContainerName`` . To return all ``Container`` objects that are associated with a specified AWS account, use  ListContainers .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DescribeContainer>`_    


    **Request Syntax** 
    ::

      response = client.describe_container(
          ContainerName='string'
      )
    :type ContainerName: string
    :param ContainerName: 

      The name of the container to query.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Container': {
                'Endpoint': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'ARN': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'CREATING'|'DELETING'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Container** *(dict) --* 

          The name of the queried container.

          
          

          - **Endpoint** *(string) --* 

            The DNS endpoint of the container. Use from 1 to 255 characters. Use this endpoint to identify this container when sending requests to the data plane. 

            
          

          - **CreationTime** *(datetime) --* 

            Unix timestamp.

            
          

          - **ARN** *(string) --* 

            The Amazon Resource Name (ARN) of the container. The ARN has the following format:

             

            arn:aws:<region>:<account that owns this container>:container/<name of container> 

             

            For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 

            
          

          - **Name** *(string) --* 

            The name of the container.

            
          

          - **Status** *(string) --* 

            The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When the endpoint is available, the status changes to ``ACTIVE`` .

            
      
    

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


  .. py:method:: get_container_policy(**kwargs)

    

    Retrieves the access policy for the specified container. For information about the data that is included in an access policy, see the `AWS Identity and Access Management User Guide <https://aws.amazon.com/documentation/iam/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/GetContainerPolicy>`_    


    **Request Syntax** 
    ::

      response = client.get_container_policy(
          ContainerName='string'
      )
    :type ContainerName: string
    :param ContainerName: **[REQUIRED]** 

      The name of the container. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policy': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policy** *(string) --* 

          The contents of the access policy.

          
    

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

        


  .. py:method:: list_containers(**kwargs)

    

    Lists the properties of all containers in AWS Elemental MediaStore. 

     

    You can query to receive all the containers in one response. Or you can include the ``MaxResults`` parameter to receive a limited number of containers in each response. In this case, the response includes a token. To get the next set of containers, send the command again, this time with the ``NextToken`` parameter (with the returned token as its value). The next set of responses appears, with a token if there are still more containers to receive. 

     

    See also  DescribeContainer , which gets the properties of one container. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/ListContainers>`_    


    **Request Syntax** 
    ::

      response = client.list_containers(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      Only if you used ``MaxResults`` in the first command, enter the token (which was included in the previous response) to obtain the next set of containers. This token is included in a response only if there actually are more containers to list.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Enter the maximum number of containers in the response. Use from 1 to 255 characters. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Containers': [
                {
                    'Endpoint': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'ARN': 'string',
                    'Name': 'string',
                    'Status': 'ACTIVE'|'CREATING'|'DELETING'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Containers** *(list) --* 

          The names of the containers.

          
          

          - *(dict) --* 

            This section describes operations that you can perform on an AWS Elemental MediaStore container.

            
            

            - **Endpoint** *(string) --* 

              The DNS endpoint of the container. Use from 1 to 255 characters. Use this endpoint to identify this container when sending requests to the data plane. 

              
            

            - **CreationTime** *(datetime) --* 

              Unix timestamp.

              
            

            - **ARN** *(string) --* 

              The Amazon Resource Name (ARN) of the container. The ARN has the following format:

               

              arn:aws:<region>:<account that owns this container>:container/<name of container> 

               

              For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 

              
            

            - **Name** *(string) --* 

              The name of the container.

              
            

            - **Status** *(string) --* 

              The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When the endpoint is available, the status changes to ``ACTIVE`` .

              
        
      
        

        - **NextToken** *(string) --* 

           ``NextToken`` is the token to use in the next call to ``ListContainers`` . This token is returned only if you included the ``MaxResults`` tag in the original command, and only if there are still containers to return. 

          
    

  .. py:method:: put_container_policy(**kwargs)

    

    Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the `AWS Identity and Access Management User Guide <https://aws.amazon.com/documentation/iam/>`__ .

     

    For this release of the REST API, you can create only one policy for a container. If you enter ``PutContainerPolicy`` twice, the second command modifies the existing policy. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/PutContainerPolicy>`_    


    **Request Syntax** 
    ::

      response = client.put_container_policy(
          ContainerName='string',
          Policy='string'
      )
    :type ContainerName: string
    :param ContainerName: **[REQUIRED]** 

      The name of the container.

      

    
    :type Policy: string
    :param Policy: **[REQUIRED]** 

      The contents of the policy, which includes the following: 

       

       
      * One ``Version`` tag 
       
      * One ``Statement`` tag that contains the standard tags for the policy. 
       

      

    
    
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
