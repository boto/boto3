

***************
DynamoDBStreams
***************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: DynamoDBStreams.Client

  A low-level client representing Amazon DynamoDB Streams::

    
    import boto3
    
    client = boto3.client('dynamodbstreams')

  
  These are the available methods:
  
  *   :py:meth:`~DynamoDBStreams.Client.can_paginate`

  
  *   :py:meth:`~DynamoDBStreams.Client.describe_stream`

  
  *   :py:meth:`~DynamoDBStreams.Client.generate_presigned_url`

  
  *   :py:meth:`~DynamoDBStreams.Client.get_paginator`

  
  *   :py:meth:`~DynamoDBStreams.Client.get_records`

  
  *   :py:meth:`~DynamoDBStreams.Client.get_shard_iterator`

  
  *   :py:meth:`~DynamoDBStreams.Client.get_waiter`

  
  *   :py:meth:`~DynamoDBStreams.Client.list_streams`

  

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


  .. py:method:: describe_stream(**kwargs)

    

    Returns information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table.

     

    .. note::

       

      You can call ``DescribeStream`` at a maximum rate of 10 times per second.

       

     

    Each shard in the stream has a ``SequenceNumberRange`` associated with it. If the ``SequenceNumberRange`` has a ``StartingSequenceNumber`` but no ``EndingSequenceNumber`` , then the shard is still open (able to receive more stream records). If both ``StartingSequenceNumber`` and ``EndingSequenceNumber`` are present, then that shard is closed and can no longer receive more data.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/streams-dynamodb-2012-08-10/DescribeStream>`_    


    **Request Syntax** 
    ::

      response = client.describe_stream(
          StreamArn='string',
          Limit=123,
          ExclusiveStartShardId='string'
      )
    :type StreamArn: string
    :param StreamArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) for the stream.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of shard objects to return. The upper limit is 100.

      

    
    :type ExclusiveStartShardId: string
    :param ExclusiveStartShardId: 

      The shard ID of the first item that this operation will evaluate. Use the value that was returned for ``LastEvaluatedShardId`` in the previous operation. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamDescription': {
                'StreamArn': 'string',
                'StreamLabel': 'string',
                'StreamStatus': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED',
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY',
                'CreationRequestDateTime': datetime(2015, 1, 1),
                'TableName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Shards': [
                    {
                        'ShardId': 'string',
                        'SequenceNumberRange': {
                            'StartingSequenceNumber': 'string',
                            'EndingSequenceNumber': 'string'
                        },
                        'ParentShardId': 'string'
                    },
                ],
                'LastEvaluatedShardId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeStream`` operation.

        
        

        - **StreamDescription** *(dict) --* 

          A complete description of the stream, including its creation date and time, the DynamoDB table associated with the stream, the shard IDs within the stream, and the beginning and ending sequence numbers of stream records within the shards.

          
          

          - **StreamArn** *(string) --* 

            The Amazon Resource Name (ARN) for the stream.

            
          

          - **StreamLabel** *(string) --* 

            A timestamp, in ISO 8601 format, for this stream.

             

            Note that ``LatestStreamLabel`` is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

             

             
            * the AWS customer ID. 
             
            * the table name 
             
            * the ``StreamLabel``   
             

            
          

          - **StreamStatus** *(string) --* 

            Indicates the current status of the stream:

             

             
            * ``ENABLING`` - Streams is currently being enabled on the DynamoDB table. 
             
            * ``ENABLED`` - the stream is enabled. 
             
            * ``DISABLING`` - Streams is currently being disabled on the DynamoDB table. 
             
            * ``DISABLED`` - the stream is disabled. 
             

            
          

          - **StreamViewType** *(string) --* 

            Indicates the format of the records within this stream:

             

             
            * ``KEYS_ONLY`` - only the key attributes of items that were modified in the DynamoDB table. 
             
            * ``NEW_IMAGE`` - entire items from the table, as they appeared after they were modified. 
             
            * ``OLD_IMAGE`` - entire items from the table, as they appeared before they were modified. 
             
            * ``NEW_AND_OLD_IMAGES`` - both the new and the old images of the items from the table. 
             

            
          

          - **CreationRequestDateTime** *(datetime) --* 

            The date and time when the request to create this stream was issued.

            
          

          - **TableName** *(string) --* 

            The DynamoDB table with which the stream is associated.

            
          

          - **KeySchema** *(list) --* 

            The key attribute(s) of the stream's DynamoDB table.

            
            

            - *(dict) --* 

              Represents *a single element* of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.

               

              A ``KeySchemaElement`` represents exactly one attribute of the primary key. For example, a simple primary key (partition key) would be represented by one ``KeySchemaElement`` . A composite primary key (partition key and sort key) would require one ``KeySchemaElement`` for the partition key, and another ``KeySchemaElement`` for the sort key.

               

              .. note::

                 

                The partition key of an item is also known as its *hash attribute* . The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

                 

                The sort key of an item is also known as its *range attribute* . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

                 

              
              

              - **AttributeName** *(string) --* 

                The name of a key attribute.

                
              

              - **KeyType** *(string) --* 

                The attribute data, consisting of the data type and the attribute value itself.

                
          
        
          

          - **Shards** *(list) --* 

            The shards that comprise the stream.

            
            

            - *(dict) --* 

              A uniquely identified group of stream records within a stream.

              
              

              - **ShardId** *(string) --* 

                The system-generated identifier for this shard.

                
              

              - **SequenceNumberRange** *(dict) --* 

                The range of possible sequence numbers for the shard.

                
                

                - **StartingSequenceNumber** *(string) --* 

                  The first sequence number.

                  
                

                - **EndingSequenceNumber** *(string) --* 

                  The last sequence number.

                  
            
              

              - **ParentShardId** *(string) --* 

                The shard ID of the current shard's parent.

                
          
        
          

          - **LastEvaluatedShardId** *(string) --* 

            The shard ID of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.

             

            If ``LastEvaluatedShardId`` is empty, then the "last page" of results has been processed and there is currently no more data to be retrieved.

             

            If ``LastEvaluatedShardId`` is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when ``LastEvaluatedShardId`` is empty.

            
      
    

    **Examples** 

    The following example describes a stream with a given stream ARN.
    ::

      response = client.describe_stream(
          StreamArn='arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'StreamDescription': {
              'CreationRequestDateTime': datetime(2015, 5, 20, 13, 51, 10, 2, 140, 1),
              'KeySchema': [
                  {
                      'AttributeName': 'ForumName',
                      'KeyType': 'HASH',
                  },
                  {
                      'AttributeName': 'Subject',
                      'KeyType': 'RANGE',
                  },
              ],
              'Shards': [
                  {
                      'SequenceNumberRange': {
                          'EndingSequenceNumber': '20500000000000000910398',
                          'StartingSequenceNumber': '20500000000000000910398',
                      },
                      'ShardId': 'shardId-00000001414562045508-2bac9cd2',
                  },
                  {
                      'ParentShardId': 'shardId-00000001414562045508-2bac9cd2',
                      'SequenceNumberRange': {
                          'EndingSequenceNumber': '820400000000000001192334',
                          'StartingSequenceNumber': '820400000000000001192334',
                      },
                      'ShardId': 'shardId-00000001414576573621-f55eea83',
                  },
                  {
                      'ParentShardId': 'shardId-00000001414576573621-f55eea83',
                      'SequenceNumberRange': {
                          'EndingSequenceNumber': '1683700000000000001135967',
                          'StartingSequenceNumber': '1683700000000000001135967',
                      },
                      'ShardId': 'shardId-00000001414592258131-674fd923',
                  },
                  {
                      'ParentShardId': 'shardId-00000001414592258131-674fd923',
                      'SequenceNumberRange': {
                          'StartingSequenceNumber': '2574600000000000000935255',
                      },
                      'ShardId': 'shardId-00000001414608446368-3a1afbaf',
                  },
              ],
              'StreamArn': 'arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252',
              'StreamLabel': '2015-05-20T20:51:10.252',
              'StreamStatus': 'ENABLED',
              'StreamViewType': 'NEW_AND_OLD_IMAGES',
              'TableName': 'Forum',
          },
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


  .. py:method:: get_records(**kwargs)

    

    Retrieves the stream records from a given shard.

     

    Specify a shard iterator using the ``ShardIterator`` parameter. The shard iterator specifies the position in the shard from which you want to start reading stream records sequentially. If there are no stream records available in the portion of the shard that the iterator points to, ``GetRecords`` returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains stream records.

     

    .. note::

       

       ``GetRecords`` can retrieve a maximum of 1 MB of data or 1000 stream records, whichever comes first.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/streams-dynamodb-2012-08-10/GetRecords>`_    


    **Request Syntax** 
    ::

      response = client.get_records(
          ShardIterator='string',
          Limit=123
      )
    :type ShardIterator: string
    :param ShardIterator: **[REQUIRED]** 

      A shard iterator that was retrieved from a previous GetShardIterator operation. This iterator can be used to access the stream records in this shard.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of records to return from the shard. The upper limit is 1000.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Records': [
                {
                    'eventID': 'string',
                    'eventName': 'INSERT'|'MODIFY'|'REMOVE',
                    'eventVersion': 'string',
                    'eventSource': 'string',
                    'awsRegion': 'string',
                    'dynamodb': {
                        'ApproximateCreationDateTime': datetime(2015, 1, 1),
                        'Keys': {
                            'string': {
                                'S': 'string',
                                'N': 'string',
                                'B': b'bytes',
                                'SS': [
                                    'string',
                                ],
                                'NS': [
                                    'string',
                                ],
                                'BS': [
                                    b'bytes',
                                ],
                                'M': {
                                    'string': {'... recursive ...'}
                                },
                                'L': [
                                    {'... recursive ...'},
                                ],
                                'NULL': True|False,
                                'BOOL': True|False
                            }
                        },
                        'NewImage': {
                            'string': {
                                'S': 'string',
                                'N': 'string',
                                'B': b'bytes',
                                'SS': [
                                    'string',
                                ],
                                'NS': [
                                    'string',
                                ],
                                'BS': [
                                    b'bytes',
                                ],
                                'M': {
                                    'string': {'... recursive ...'}
                                },
                                'L': [
                                    {'... recursive ...'},
                                ],
                                'NULL': True|False,
                                'BOOL': True|False
                            }
                        },
                        'OldImage': {
                            'string': {
                                'S': 'string',
                                'N': 'string',
                                'B': b'bytes',
                                'SS': [
                                    'string',
                                ],
                                'NS': [
                                    'string',
                                ],
                                'BS': [
                                    b'bytes',
                                ],
                                'M': {
                                    'string': {'... recursive ...'}
                                },
                                'L': [
                                    {'... recursive ...'},
                                ],
                                'NULL': True|False,
                                'BOOL': True|False
                            }
                        },
                        'SequenceNumber': 'string',
                        'SizeBytes': 123,
                        'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
                    },
                    'userIdentity': {
                        'PrincipalId': 'string',
                        'Type': 'string'
                    }
                },
            ],
            'NextShardIterator': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``GetRecords`` operation.

        
        

        - **Records** *(list) --* 

          The stream records from the shard, which were retrieved using the shard iterator.

          
          

          - *(dict) --* 

            A description of a unique event within a stream.

            
            

            - **eventID** *(string) --* 

              A globally unique identifier for the event that was recorded in this stream record.

              
            

            - **eventName** *(string) --* 

              The type of data modification that was performed on the DynamoDB table:

               

               
              * ``INSERT`` - a new item was added to the table. 
               
              * ``MODIFY`` - one or more of an existing item's attributes were modified. 
               
              * ``REMOVE`` - the item was deleted from the table 
               

              
            

            - **eventVersion** *(string) --* 

              The version number of the stream record format. This number is updated whenever the structure of ``Record`` is modified.

               

              Client applications must not assume that ``eventVersion`` will remain at a particular value, as this number is subject to change at any time. In general, ``eventVersion`` will only increase as the low-level DynamoDB Streams API evolves.

              
            

            - **eventSource** *(string) --* 

              The AWS service from which the stream record originated. For DynamoDB Streams, this is ``aws:dynamodb`` .

              
            

            - **awsRegion** *(string) --* 

              The region in which the ``GetRecords`` request was received.

              
            

            - **dynamodb** *(dict) --* 

              The main body of the stream record, containing all of the DynamoDB-specific fields.

              
              

              - **ApproximateCreationDateTime** *(datetime) --* 

                The approximate date and time when the stream record was created, in `UNIX epoch time <http://www.epochconverter.com/>`__ format.

                
              

              - **Keys** *(dict) --* 

                The primary key attribute(s) for the DynamoDB item that was modified.

                
                

                - *(string) --* 
                  

                  - *(dict) --* 

                    Represents the data for an attribute. You can set one, and only one, of the elements.

                     

                    Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                    
                    

                    - **S** *(string) --* 

                      A String data type.

                      
                    

                    - **N** *(string) --* 

                      A Number data type.

                      
                    

                    - **B** *(bytes) --* 

                      A Binary data type.

                      
                    

                    - **SS** *(list) --* 

                      A String Set data type.

                      
                      

                      - *(string) --* 
                  
                    

                    - **NS** *(list) --* 

                      A Number Set data type.

                      
                      

                      - *(string) --* 
                  
                    

                    - **BS** *(list) --* 

                      A Binary Set data type.

                      
                      

                      - *(bytes) --* 
                  
                    

                    - **M** *(dict) --* 

                      A Map data type.

                      
                      

                      - *(string) --* 
                        

                        - *(dict) --* 

                          Represents the data for an attribute. You can set one, and only one, of the elements.

                           

                          Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                          
                  
                
                    

                    - **L** *(list) --* 

                      A List data type.

                      
                      

                      - *(dict) --* 

                        Represents the data for an attribute. You can set one, and only one, of the elements.

                         

                        Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                        
                  
                    

                    - **NULL** *(boolean) --* 

                      A Null data type.

                      
                    

                    - **BOOL** *(boolean) --* 

                      A Boolean data type.

                      
                
            
          
              

              - **NewImage** *(dict) --* 

                The item in the DynamoDB table as it appeared after it was modified.

                
                

                - *(string) --* 
                  

                  - *(dict) --* 

                    Represents the data for an attribute. You can set one, and only one, of the elements.

                     

                    Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                    
                    

                    - **S** *(string) --* 

                      A String data type.

                      
                    

                    - **N** *(string) --* 

                      A Number data type.

                      
                    

                    - **B** *(bytes) --* 

                      A Binary data type.

                      
                    

                    - **SS** *(list) --* 

                      A String Set data type.

                      
                      

                      - *(string) --* 
                  
                    

                    - **NS** *(list) --* 

                      A Number Set data type.

                      
                      

                      - *(string) --* 
                  
                    

                    - **BS** *(list) --* 

                      A Binary Set data type.

                      
                      

                      - *(bytes) --* 
                  
                    

                    - **M** *(dict) --* 

                      A Map data type.

                      
                      

                      - *(string) --* 
                        

                        - *(dict) --* 

                          Represents the data for an attribute. You can set one, and only one, of the elements.

                           

                          Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                          
                  
                
                    

                    - **L** *(list) --* 

                      A List data type.

                      
                      

                      - *(dict) --* 

                        Represents the data for an attribute. You can set one, and only one, of the elements.

                         

                        Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                        
                  
                    

                    - **NULL** *(boolean) --* 

                      A Null data type.

                      
                    

                    - **BOOL** *(boolean) --* 

                      A Boolean data type.

                      
                
            
          
              

              - **OldImage** *(dict) --* 

                The item in the DynamoDB table as it appeared before it was modified.

                
                

                - *(string) --* 
                  

                  - *(dict) --* 

                    Represents the data for an attribute. You can set one, and only one, of the elements.

                     

                    Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                    
                    

                    - **S** *(string) --* 

                      A String data type.

                      
                    

                    - **N** *(string) --* 

                      A Number data type.

                      
                    

                    - **B** *(bytes) --* 

                      A Binary data type.

                      
                    

                    - **SS** *(list) --* 

                      A String Set data type.

                      
                      

                      - *(string) --* 
                  
                    

                    - **NS** *(list) --* 

                      A Number Set data type.

                      
                      

                      - *(string) --* 
                  
                    

                    - **BS** *(list) --* 

                      A Binary Set data type.

                      
                      

                      - *(bytes) --* 
                  
                    

                    - **M** *(dict) --* 

                      A Map data type.

                      
                      

                      - *(string) --* 
                        

                        - *(dict) --* 

                          Represents the data for an attribute. You can set one, and only one, of the elements.

                           

                          Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                          
                  
                
                    

                    - **L** *(list) --* 

                      A List data type.

                      
                      

                      - *(dict) --* 

                        Represents the data for an attribute. You can set one, and only one, of the elements.

                         

                        Each attribute in an item is a name-value pair. An attribute can be single-valued or multi-valued set. For example, a book item can have title and authors attributes. Each book has one title but can have many authors. The multi-valued attribute is a set; duplicate values are not allowed.

                        
                  
                    

                    - **NULL** *(boolean) --* 

                      A Null data type.

                      
                    

                    - **BOOL** *(boolean) --* 

                      A Boolean data type.

                      
                
            
          
              

              - **SequenceNumber** *(string) --* 

                The sequence number of the stream record.

                
              

              - **SizeBytes** *(integer) --* 

                The size of the stream record, in bytes.

                
              

              - **StreamViewType** *(string) --* 

                The type of data from the modified DynamoDB item that was captured in this stream record:

                 

                 
                * ``KEYS_ONLY`` - only the key attributes of the modified item. 
                 
                * ``NEW_IMAGE`` - the entire item, as it appeared after it was modified. 
                 
                * ``OLD_IMAGE`` - the entire item, as it appeared before it was modified. 
                 
                * ``NEW_AND_OLD_IMAGES`` - both the new and the old item images of the item. 
                 

                
          
            

            - **userIdentity** *(dict) --* 

              Items that are deleted by the Time to Live process after expiration have the following fields: 

               

               
              * Records[].userIdentity.type "Service" 
               
              * Records[].userIdentity.principalId "dynamodb.amazonaws.com" 
               

              
              

              - **PrincipalId** *(string) --* 

                A unique identifier for the entity that made the call. For Time To Live, the principalId is "dynamodb.amazonaws.com".

                
              

              - **Type** *(string) --* 

                The type of the identity. For Time To Live, the type is "Service".

                
          
        
      
        

        - **NextShardIterator** *(string) --* 

          The next position in the shard from which to start sequentially reading stream records. If set to ``null`` , the shard has been closed and the requested iterator will not return any more data.

          
    

    **Examples** 

    The following example retrieves all the stream records from a shard.
    ::

      response = client.get_records(
          ShardIterator='arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252|1|AAAAAAAAAAEvJp6D+zaQ...  <remaining characters omitted> ...',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'NextShardIterator': 'arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252|1|AAAAAAAAAAGQBYshYDEe ... <remaining characters omitted> ...',
          'Records': [
              {
                  'awsRegion': 'us-west-2',
                  'dynamodb': {
                      'ApproximateCreationDateTime': datetime(2016, 6, 1, 11, 41, 0, 2, 153, 1),
                      'Keys': {
                          'ForumName': {
                              'S': 'DynamoDB',
                          },
                          'Subject': {
                              'S': 'DynamoDB Thread 3',
                          },
                      },
                      'SequenceNumber': '300000000000000499659',
                      'SizeBytes': 41,
                      'StreamViewType': 'KEYS_ONLY',
                  },
                  'eventID': 'e2fd9c34eff2d779b297b26f5fef4206',
                  'eventName': 'INSERT',
                  'eventSource': 'aws:dynamodb',
                  'eventVersion': '1.0',
              },
              {
                  'awsRegion': 'us-west-2',
                  'dynamodb': {
                      'ApproximateCreationDateTime': datetime(2016, 6, 1, 11, 21, 10, 2, 153, 1),
                      'Keys': {
                          'ForumName': {
                              'S': 'DynamoDB',
                          },
                          'Subject': {
                              'S': 'DynamoDB Thread 1',
                          },
                      },
                      'SequenceNumber': '400000000000000499660',
                      'SizeBytes': 41,
                      'StreamViewType': 'KEYS_ONLY',
                  },
                  'eventID': '4b25bd0da9a181a155114127e4837252',
                  'eventName': 'MODIFY',
                  'eventSource': 'aws:dynamodb',
                  'eventVersion': '1.0',
              },
              {
                  'awsRegion': 'us-west-2',
                  'dynamodb': {
                      'ApproximateCreationDateTime': datetime(2016, 6, 1, 11, 41, 0, 2, 153, 1),
                      'Keys': {
                          'ForumName': {
                              'S': 'DynamoDB',
                          },
                          'Subject': {
                              'S': 'DynamoDB Thread 2',
                          },
                      },
                      'SequenceNumber': '500000000000000499661',
                      'SizeBytes': 41,
                      'StreamViewType': 'KEYS_ONLY',
                  },
                  'eventID': '740280c73a3df7842edab3548a1b08ad',
                  'eventName': 'REMOVE',
                  'eventSource': 'aws:dynamodb',
                  'eventVersion': '1.0',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_shard_iterator(**kwargs)

    

    Returns a shard iterator. A shard iterator provides information about how to retrieve the stream records from within a shard. Use the shard iterator in a subsequent ``GetRecords`` request to read the stream records from the shard.

     

    .. note::

       

      A shard iterator expires 15 minutes after it is returned to the requester.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/streams-dynamodb-2012-08-10/GetShardIterator>`_    


    **Request Syntax** 
    ::

      response = client.get_shard_iterator(
          StreamArn='string',
          ShardId='string',
          ShardIteratorType='TRIM_HORIZON'|'LATEST'|'AT_SEQUENCE_NUMBER'|'AFTER_SEQUENCE_NUMBER',
          SequenceNumber='string'
      )
    :type StreamArn: string
    :param StreamArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) for the stream.

      

    
    :type ShardId: string
    :param ShardId: **[REQUIRED]** 

      The identifier of the shard. The iterator will be returned for this shard ID.

      

    
    :type ShardIteratorType: string
    :param ShardIteratorType: **[REQUIRED]** 

      Determines how the shard iterator is used to start reading stream records from the shard:

       

       
      * ``AT_SEQUENCE_NUMBER`` - Start reading exactly from the position denoted by a specific sequence number. 
       
      * ``AFTER_SEQUENCE_NUMBER`` - Start reading right after the position denoted by a specific sequence number. 
       
      * ``TRIM_HORIZON`` - Start reading at the last (untrimmed) stream record, which is the oldest record in the shard. In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream. 
       
      * ``LATEST`` - Start reading just after the most recent stream record in the shard, so that you always read the most recent data in the shard. 
       

      

    
    :type SequenceNumber: string
    :param SequenceNumber: 

      The sequence number of a stream record in the shard from which to start reading.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ShardIterator': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``GetShardIterator`` operation.

        
        

        - **ShardIterator** *(string) --* 

          The position in the shard from which to start reading stream records sequentially. A shard iterator specifies this position using the sequence number of a stream record in a shard.

          
    

    **Examples** 

    The following example returns a shard iterator for the provided stream ARN and shard ID.
    ::

      response = client.get_shard_iterator(
          ShardId='00000001414576573621-f55eea83',
          ShardIteratorType='TRIM_HORIZON',
          StreamArn='arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ShardIterator': 'arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252|1|AAAAAAAAAAEvJp6D+zaQ...  <remaining characters omitted> ...',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_streams(**kwargs)

    

    Returns an array of stream ARNs associated with the current account and endpoint. If the ``TableName`` parameter is present, then ``ListStreams`` will return only the streams ARNs for that table.

     

    .. note::

       

      You can call ``ListStreams`` at a maximum rate of 5 times per second.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/streams-dynamodb-2012-08-10/ListStreams>`_    


    **Request Syntax** 
    ::

      response = client.list_streams(
          TableName='string',
          Limit=123,
          ExclusiveStartStreamArn='string'
      )
    :type TableName: string
    :param TableName: 

      If this parameter is provided, then only the streams associated with this table name are returned.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of streams to return. The upper limit is 100.

      

    
    :type ExclusiveStartStreamArn: string
    :param ExclusiveStartStreamArn: 

      The ARN (Amazon Resource Name) of the first item that this operation will evaluate. Use the value that was returned for ``LastEvaluatedStreamArn`` in the previous operation. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Streams': [
                {
                    'StreamArn': 'string',
                    'TableName': 'string',
                    'StreamLabel': 'string'
                },
            ],
            'LastEvaluatedStreamArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``ListStreams`` operation.

        
        

        - **Streams** *(list) --* 

          A list of stream descriptors associated with the current account and endpoint.

          
          

          - *(dict) --* 

            Represents all of the data describing a particular stream.

            
            

            - **StreamArn** *(string) --* 

              The Amazon Resource Name (ARN) for the stream.

              
            

            - **TableName** *(string) --* 

              The DynamoDB table with which the stream is associated.

              
            

            - **StreamLabel** *(string) --* 

              A timestamp, in ISO 8601 format, for this stream.

               

              Note that ``LatestStreamLabel`` is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

               

               
              * the AWS customer ID. 
               
              * the table name 
               
              * the ``StreamLabel``   
               

              
        
      
        

        - **LastEvaluatedStreamArn** *(string) --* 

          The stream ARN of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.

           

          If ``LastEvaluatedStreamArn`` is empty, then the "last page" of results has been processed and there is no more data to be retrieved.

           

          If ``LastEvaluatedStreamArn`` is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when ``LastEvaluatedStreamArn`` is empty.

          
    

    **Examples** 

    The following example lists all of the stream ARNs.
    ::

      response = client.list_streams(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Streams': [
              {
                  'StreamArn': 'arn:aws:dynamodb:us-wesst-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252',
                  'StreamLabel': '2015-05-20T20:51:10.252',
                  'TableName': 'Forum',
              },
              {
                  'StreamArn': 'arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:50:02.714',
                  'StreamLabel': '2015-05-20T20:50:02.714',
                  'TableName': 'Forum',
              },
              {
                  'StreamArn': 'arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-19T23:03:50.641',
                  'StreamLabel': '2015-05-19T23:03:50.641',
                  'TableName': 'Forum',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:
