

**************
MediaStoreData
**************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: MediaStoreData.Client

  A low-level client representing AWS Elemental MediaStore Data Plane::

    
    import boto3
    
    client = boto3.client('mediastore-data')

  
  These are the available methods:
  
  *   :py:meth:`~MediaStoreData.Client.can_paginate`

  
  *   :py:meth:`~MediaStoreData.Client.delete_object`

  
  *   :py:meth:`~MediaStoreData.Client.describe_object`

  
  *   :py:meth:`~MediaStoreData.Client.generate_presigned_url`

  
  *   :py:meth:`~MediaStoreData.Client.get_object`

  
  *   :py:meth:`~MediaStoreData.Client.get_paginator`

  
  *   :py:meth:`~MediaStoreData.Client.get_waiter`

  
  *   :py:meth:`~MediaStoreData.Client.list_items`

  
  *   :py:meth:`~MediaStoreData.Client.put_object`

  

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


  .. py:method:: delete_object(**kwargs)

    

    Deletes an object at the specified path.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/DeleteObject>`_    


    **Request Syntax** 
    ::

      response = client.delete_object(
          Path='string'
      )
    :type Path: string
    :param Path: **[REQUIRED]** 

      The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_object(**kwargs)

    

    Gets the header for an object at the specified path.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/DescribeObject>`_    


    **Request Syntax** 
    ::

      response = client.describe_object(
          Path='string'
      )
    :type Path: string
    :param Path: **[REQUIRED]** 

      The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ETag': 'string',
            'ContentType': 'string',
            'ContentLength': 123,
            'CacheControl': 'string',
            'LastModified': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ETag** *(string) --* 

          The ETag that represents a unique instance of the object.

          
        

        - **ContentType** *(string) --* 

          The content type of the object.

          
        

        - **ContentLength** *(integer) --* 

          The length of the object in bytes.

          
        

        - **CacheControl** *(string) --* 

          An optional ``CacheControl`` header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP at `https\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .

           

          Headers with a custom user-defined value are also accepted.

          
        

        - **LastModified** *(datetime) --* 

          The date and time that the object was last modified.

          
    

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


  .. py:method:: get_object(**kwargs)

    

    Downloads the object at the specified path.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/GetObject>`_    


    **Request Syntax** 
    ::

      response = client.get_object(
          Path='string',
          Range='string'
      )
    :type Path: string
    :param Path: **[REQUIRED]** 

      The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>

       

      For example, to upload the file ``mlaw.avi`` to the folder path ``premium\canada`` in the container ``movies`` , enter the path ``premium/canada/mlaw.avi`` .

       

      Do not include the container name in this path.

       

      If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing ``premium/usa`` subfolder. If you specify ``premium/canada`` , the service creates a ``canada`` subfolder in the ``premium`` folder. You then have two subfolders, ``usa`` and ``canada`` , in the ``premium`` folder. 

       

      There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.

       

      For more information about folders and how they exist in a container, see the `AWS Elemental MediaStore User Guide <http://docs.aws.amazon.com/mediastore/latest/ug/>`__ .

       

      The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. 

      

    
    :type Range: string
    :param Range: 

      The range bytes of an object to retrieve. For more information about the ``Range`` header, go to `http\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35>`__ .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Body': StreamingBody(),
            'CacheControl': 'string',
            'ContentRange': 'string',
            'ContentLength': 123,
            'ContentType': 'string',
            'ETag': 'string',
            'LastModified': datetime(2015, 1, 1),
            'StatusCode': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Body** (:class:`.StreamingBody`) -- 

          The path to the file outside of the container. The file name can include or omit an extension. 

           

          Example 1: If the file is stored on a remote server that has been mounted to the workstation on which the REST API command is being run, the path could be the absolute path ``\mount\assets\mlaw.avi`` or the relative path ``..\..\mount\assets\movies\premium\mlaw.avi`` .

           

          Example 2: If the file is stored on a remote server that is not mounted, the path could be ``https:\\192.0.2.15\movies\premium\mlaw.avi`` .

          
        

        - **CacheControl** *(string) --* 

          An optional ``CacheControl`` header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP spec at `https\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .

           

          Headers with a custom user-defined value are also accepted.

          
        

        - **ContentRange** *(string) --* 

          The range of bytes to retrieve.

          
        

        - **ContentLength** *(integer) --* 

          The length of the object in bytes.

          
        

        - **ContentType** *(string) --* 

          The content type of the object.

          
        

        - **ETag** *(string) --* 

          The ETag that represents a unique instance of the object.

          
        

        - **LastModified** *(datetime) --* 

          The date and time that the object was last modified.

          
        

        - **StatusCode** *(integer) --* 

          The HTML status code of the request. Status codes ranging from 200 to 299 indicate success. All other status codes indicate the type of error that occurred.

          
    

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

        


  .. py:method:: list_items(**kwargs)

    

    Provides a list of metadata entries about folders and objects in the specified folder.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/ListItems>`_    


    **Request Syntax** 
    ::

      response = client.list_items(
          Path='string',
          MaxResults=123,
          NextToken='string'
      )
    :type Path: string
    :param Path: 

      The path in the container from which to retrieve items. Format: <folder name>/<folder name>/<file name>

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum results to return. The service might return fewer results.

      

    
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` received in the ``ListItemsResponse`` for the same container and path. Tokens expire after 15 minutes.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Items': [
                {
                    'Name': 'string',
                    'Type': 'OBJECT'|'FOLDER',
                    'ETag': 'string',
                    'LastModified': datetime(2015, 1, 1),
                    'ContentType': 'string',
                    'ContentLength': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Items** *(list) --* 

          Metadata entries for the folders and objects at the requested path.

          
          

          - *(dict) --* 

            A metadata entry for a folder or object.

            
            

            - **Name** *(string) --* 

              The name of the item.

              
            

            - **Type** *(string) --* 

              The item type (folder or object).

              
            

            - **ETag** *(string) --* 

              The ETag that represents a unique instance of the item.

              
            

            - **LastModified** *(datetime) --* 

              The date and time that the item was last modified.

              
            

            - **ContentType** *(string) --* 

              The content type of the item.

              
            

            - **ContentLength** *(integer) --* 

              The length of the item in bytes.

              
        
      
        

        - **NextToken** *(string) --* 

          The ``NextToken`` used to request the next page of results using ``ListItems`` .

          
    

  .. py:method:: put_object(**kwargs)

    

    Uploads an object to the specified path. Object sizes are limited to 10 MB.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/PutObject>`_    


    **Request Syntax** 
    ::

      response = client.put_object(
          Body=b'bytes'|file,
          Path='string',
          ContentType='string',
          CacheControl='string',
          StorageClass='TEMPORAL'
      )
    :type Body: bytes or seekable file-like object
    :param Body: **[REQUIRED]** 

      The path to the file outside of the container. The file name can include or omit an extension. 

       

      Example 1: If the file is stored on a remote server that has been mounted to the workstation on which the REST API command is being run, the path could be the absolute path ``\mount\assets\mlaw.avi`` or the relative path ``..\..\mount\assets\movies\premium\mlaw.avi`` .

       

      Example 2: If the file is stored on a remote server that is not mounted, the path could be ``https:\\192.0.2.15\movies\premium\mlaw.avi`` .

      

    
    :type Path: string
    :param Path: **[REQUIRED]** 

      The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>

       

      For example, to upload the file ``mlaw.avi`` to the folder path ``premium\canada`` in the container ``movies`` , enter the path ``premium/canada/mlaw.avi`` .

       

      Do not include the container name in this path.

       

      If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing ``premium/usa`` subfolder. If you specify ``premium/canada`` , the service creates a ``canada`` subfolder in the ``premium`` folder. You then have two subfolders, ``usa`` and ``canada`` , in the ``premium`` folder. 

       

      There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.

       

      For more information about folders and how they exist in a container, see the `AWS Elemental MediaStore User Guide <http://docs.aws.amazon.com/mediastore/latest/ug/>`__ .

       

      The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. 

      

    
    :type ContentType: string
    :param ContentType: 

      The content type of the object.

      

    
    :type CacheControl: string
    :param CacheControl: 

      An optional ``CacheControl`` header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP at `https\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .

       

      Headers with a custom user-defined value are also accepted.

      

    
    :type StorageClass: string
    :param StorageClass: 

      Indicates the storage class of a ``Put`` request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ContentSHA256': 'string',
            'ETag': 'string',
            'StorageClass': 'TEMPORAL'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ContentSHA256** *(string) --* 

          The SHA256 digest of the object that is persisted.

          
        

        - **ETag** *(string) --* 

          Unique identifier of the object in the container.

          
        

        - **StorageClass** *(string) --* 

          The storage class where the object was persisted. Should be “Temporal”.

          
    

==========
Paginators
==========


The available paginators are:
