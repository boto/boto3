

*******
Kinesis
*******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Kinesis.Client

  A low-level client representing Amazon Kinesis::

    
    import boto3
    
    client = boto3.client('kinesis')

  
  These are the available methods:
  
  *   :py:meth:`~Kinesis.Client.add_tags_to_stream`

  
  *   :py:meth:`~Kinesis.Client.can_paginate`

  
  *   :py:meth:`~Kinesis.Client.create_stream`

  
  *   :py:meth:`~Kinesis.Client.decrease_stream_retention_period`

  
  *   :py:meth:`~Kinesis.Client.delete_stream`

  
  *   :py:meth:`~Kinesis.Client.describe_limits`

  
  *   :py:meth:`~Kinesis.Client.describe_stream`

  
  *   :py:meth:`~Kinesis.Client.describe_stream_summary`

  
  *   :py:meth:`~Kinesis.Client.disable_enhanced_monitoring`

  
  *   :py:meth:`~Kinesis.Client.enable_enhanced_monitoring`

  
  *   :py:meth:`~Kinesis.Client.generate_presigned_url`

  
  *   :py:meth:`~Kinesis.Client.get_paginator`

  
  *   :py:meth:`~Kinesis.Client.get_records`

  
  *   :py:meth:`~Kinesis.Client.get_shard_iterator`

  
  *   :py:meth:`~Kinesis.Client.get_waiter`

  
  *   :py:meth:`~Kinesis.Client.increase_stream_retention_period`

  
  *   :py:meth:`~Kinesis.Client.list_streams`

  
  *   :py:meth:`~Kinesis.Client.list_tags_for_stream`

  
  *   :py:meth:`~Kinesis.Client.merge_shards`

  
  *   :py:meth:`~Kinesis.Client.put_record`

  
  *   :py:meth:`~Kinesis.Client.put_records`

  
  *   :py:meth:`~Kinesis.Client.remove_tags_from_stream`

  
  *   :py:meth:`~Kinesis.Client.split_shard`

  
  *   :py:meth:`~Kinesis.Client.start_stream_encryption`

  
  *   :py:meth:`~Kinesis.Client.stop_stream_encryption`

  
  *   :py:meth:`~Kinesis.Client.update_shard_count`

  

  .. py:method:: add_tags_to_stream(**kwargs)

    

    Adds or updates tags for the specified Kinesis stream. Each stream can have up to 10 tags.

     

    If tags have already been assigned to the stream, ``AddTagsToStream`` overwrites any existing tags that correspond to the specified tag keys.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/AddTagsToStream>`_    


    **Request Syntax** 
    ::

      response = client.add_tags_to_stream(
          StreamName='string',
          Tags={
              'string': 'string'
          }
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream.

      

    
    :type Tags: dict
    :param Tags: **[REQUIRED]** 

      The set of key-value pairs to use to create the tags.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :returns: None

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


  .. py:method:: create_stream(**kwargs)

    

    Creates a Kinesis stream. A stream captures and transports data records that are continuously emitted from different data sources or *producers* . Scale-out within a stream is explicitly supported by means of shards, which are uniquely identified groups of data records in a stream.

     

    You specify and control the number of shards that a stream is composed of. Each shard can support reads up to 5 transactions per second, up to a maximum data read total of 2 MB per second. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second. I the amount of data input increases or decreases, you can add or remove shards.

     

    The stream name identifies the stream. The name is scoped to the AWS account used by the application. It is also scoped by region. That is, two streams in two different accounts can have the same name, and two streams in the same account, but in two different regions, can have the same name.

     

     ``CreateStream`` is an asynchronous operation. Upon receiving a ``CreateStream`` request, Kinesis Streams immediately returns and sets the stream status to ``CREATING`` . After the stream is created, Kinesis Streams sets the stream status to ``ACTIVE`` . You should perform read and write operations only on an ``ACTIVE`` stream. 

     

    You receive a ``LimitExceededException`` when making a ``CreateStream`` request when you try to do one of the following:

     

     
    * Have more than five streams in the ``CREATING`` state at any point in time. 
     
    * Create more shards than are authorized for your account. 
     

     

    For the default shard limit for an AWS account, see `Streams Limits <http://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html>`__ in the *Amazon Kinesis Streams Developer Guide* . To increase this limit, `contact AWS Support <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>`__ .

     

    You can use ``DescribeStream`` to check the stream status, which is returned in ``StreamStatus`` .

     

      CreateStream has a limit of 5 transactions per second per account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/CreateStream>`_    


    **Request Syntax** 
    ::

      response = client.create_stream(
          StreamName='string',
          ShardCount=123
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      A name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by region. That is, two streams in two different AWS accounts can have the same name. Two streams in the same AWS account but in two different regions can also have the same name.

      

    
    :type ShardCount: integer
    :param ShardCount: **[REQUIRED]** 

      The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.

       

      DefaultShardLimit;

      

    
    
    :returns: None

  .. py:method:: decrease_stream_retention_period(**kwargs)

    

    Decreases the Kinesis stream's retention period, which is the length of time data records are accessible after they are added to the stream. The minimum value of a stream's retention period is 24 hours.

     

    This operation may result in lost data. For example, if the stream's retention period is 48 hours and is decreased to 24 hours, any data already in the stream that is older than 24 hours is inaccessible.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DecreaseStreamRetentionPeriod>`_    


    **Request Syntax** 
    ::

      response = client.decrease_stream_retention_period(
          StreamName='string',
          RetentionPeriodHours=123
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to modify.

      

    
    :type RetentionPeriodHours: integer
    :param RetentionPeriodHours: **[REQUIRED]** 

      The new retention period of the stream, in hours. Must be less than the current retention period.

      

    
    
    :returns: None

  .. py:method:: delete_stream(**kwargs)

    

    Deletes a Kinesis stream and all its shards and data. You must shut down any applications that are operating on the stream before you delete the stream. If an application attempts to operate on a deleted stream, it receives the exception ``ResourceNotFoundException`` .

     

    If the stream is in the ``ACTIVE`` state, you can delete it. After a ``DeleteStream`` request, the specified stream is in the ``DELETING`` state until Kinesis Streams completes the deletion.

     

     **Note:** Kinesis Streams might continue to accept data read and write operations, such as  PutRecord ,  PutRecords , and  GetRecords , on a stream in the ``DELETING`` state until the stream deletion is complete.

     

    When you delete a stream, any shards in that stream are also deleted, and any tags are dissociated from the stream.

     

    You can use the  DescribeStream operation to check the state of the stream, which is returned in ``StreamStatus`` .

     

      DeleteStream has a limit of 5 transactions per second per account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DeleteStream>`_    


    **Request Syntax** 
    ::

      response = client.delete_stream(
          StreamName='string'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to delete.

      

    
    
    :returns: None

  .. py:method:: describe_limits()

    

    Describes the shard limits and usage for the account.

     

    If you update your account limits, the old limits might be returned for a few minutes.

     

    This operation has a limit of 1 transaction per second per account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeLimits>`_    


    **Request Syntax** 
    ::

      response = client.describe_limits()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ShardLimit': 123,
            'OpenShardCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ShardLimit** *(integer) --* 

          The maximum number of shards.

          
        

        - **OpenShardCount** *(integer) --* 

          The number of open shards.

          
    

  .. py:method:: describe_stream(**kwargs)

    

    Describes the specified Kinesis stream.

     

    The information returned includes the stream name, Amazon Resource Name (ARN), creation time, enhanced metric configuration, and shard map. The shard map is an array of shard objects. For each shard object, there is the hash key and sequence number ranges that the shard spans, and the IDs of any earlier shards that played in a role in creating the shard. Every record ingested in the stream is identified by a sequence number, which is assigned when the record is put into the stream.

     

    You can limit the number of shards returned by each call. For more information, see `Retrieving Shards from a Stream <http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-retrieve-shards.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

    There are no guarantees about the chronological order shards returned. To process shards in chronological order, use the ID of the parent shard to track the lineage to the oldest shard.

     

    This operation has a limit of 10 transactions per second per account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStream>`_    


    **Request Syntax** 
    ::

      response = client.describe_stream(
          StreamName='string',
          Limit=123,
          ExclusiveStartShardId='string'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to describe.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 shards are returned.

      

    
    :type ExclusiveStartShardId: string
    :param ExclusiveStartShardId: 

      The shard ID of the shard to start with.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamDescription': {
                'StreamName': 'string',
                'StreamARN': 'string',
                'StreamStatus': 'CREATING'|'DELETING'|'ACTIVE'|'UPDATING',
                'Shards': [
                    {
                        'ShardId': 'string',
                        'ParentShardId': 'string',
                        'AdjacentParentShardId': 'string',
                        'HashKeyRange': {
                            'StartingHashKey': 'string',
                            'EndingHashKey': 'string'
                        },
                        'SequenceNumberRange': {
                            'StartingSequenceNumber': 'string',
                            'EndingSequenceNumber': 'string'
                        }
                    },
                ],
                'HasMoreShards': True|False,
                'RetentionPeriodHours': 123,
                'StreamCreationTimestamp': datetime(2015, 1, 1),
                'EnhancedMonitoring': [
                    {
                        'ShardLevelMetrics': [
                            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
                        ]
                    },
                ],
                'EncryptionType': 'NONE'|'KMS',
                'KeyId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for ``DescribeStream`` .

        
        

        - **StreamDescription** *(dict) --* 

          The current status of the stream, the stream ARN, an array of shard objects that comprise the stream, and whether there are more shards available.

          
          

          - **StreamName** *(string) --* 

            The name of the stream being described.

            
          

          - **StreamARN** *(string) --* 

            The Amazon Resource Name (ARN) for the stream being described.

            
          

          - **StreamStatus** *(string) --* 

            The current status of the stream being described. The stream status is one of the following states:

             

             
            * ``CREATING`` - The stream is being created. Kinesis Streams immediately returns and sets ``StreamStatus`` to ``CREATING`` . 
             
            * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING`` state until Kinesis Streams completes the deletion. 
             
            * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an ``ACTIVE`` stream. 
             
            * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the ``UPDATING`` state. 
             

            
          

          - **Shards** *(list) --* 

            The shards that comprise the stream.

            
            

            - *(dict) --* 

              A uniquely identified group of data records in a Kinesis stream.

              
              

              - **ShardId** *(string) --* 

                The unique identifier of the shard within the stream.

                
              

              - **ParentShardId** *(string) --* 

                The shard ID of the shard's parent.

                
              

              - **AdjacentParentShardId** *(string) --* 

                The shard ID of the shard adjacent to the shard's parent.

                
              

              - **HashKeyRange** *(dict) --* 

                The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.

                
                

                - **StartingHashKey** *(string) --* 

                  The starting hash key of the hash key range.

                  
                

                - **EndingHashKey** *(string) --* 

                  The ending hash key of the hash key range.

                  
            
              

              - **SequenceNumberRange** *(dict) --* 

                The range of possible sequence numbers for the shard.

                
                

                - **StartingSequenceNumber** *(string) --* 

                  The starting sequence number for the range.

                  
                

                - **EndingSequenceNumber** *(string) --* 

                  The ending sequence number for the range. Shards that are in the OPEN state have an ending sequence number of ``null`` .

                  
            
          
        
          

          - **HasMoreShards** *(boolean) --* 

            If set to ``true`` , more shards in the stream are available to describe.

            
          

          - **RetentionPeriodHours** *(integer) --* 

            The current retention period, in hours.

            
          

          - **StreamCreationTimestamp** *(datetime) --* 

            The approximate time that the stream was created.

            
          

          - **EnhancedMonitoring** *(list) --* 

            Represents the current enhanced monitoring settings of the stream.

            
            

            - *(dict) --* 

              Represents enhanced metrics types.

              
              

              - **ShardLevelMetrics** *(list) --* 

                List of shard-level metrics.

                 

                The following are the valid shard-level metrics. The value "``ALL`` " enhances every metric.

                 

                 
                * ``IncomingBytes``   
                 
                * ``IncomingRecords``   
                 
                * ``OutgoingBytes``   
                 
                * ``OutgoingRecords``   
                 
                * ``WriteProvisionedThroughputExceeded``   
                 
                * ``ReadProvisionedThroughputExceeded``   
                 
                * ``IteratorAgeMilliseconds``   
                 
                * ``ALL``   
                 

                 

                For more information, see `Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

                
                

                - *(string) --* 
            
          
        
          

          - **EncryptionType** *(string) --* 

            The server-side encryption type used on the stream. This parameter can be one of the following values:

             

             
            * ``NONE`` : Do not encrypt the records in the stream. 
             
            * ``KMS`` : Use server-side encryption on the records in the stream using a customer-managed KMS key. 
             

            
          

          - **KeyId** *(string) --* 

            The GUID for the customer-managed KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Streams by specifying the alias ``aws/kinesis`` .

             

             
            * Key ARN example: ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``   
             
            * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``   
             
            * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``   
             
            * Alias name example: ``alias/MyAliasName``   
             
            * Master key owned by Kinesis Streams: ``alias/aws/kinesis``   
             

            
      
    

  .. py:method:: describe_stream_summary(**kwargs)

    

    Provides a summarized description of the specified Kinesis stream without the shard list.

     

    The information returned includes the stream name, Amazon Resource Name (ARN), status, record retention period, approximate creation time, monitoring, encryption details, and open shard count. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStreamSummary>`_    


    **Request Syntax** 
    ::

      response = client.describe_stream_summary(
          StreamName='string'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to describe.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamDescriptionSummary': {
                'StreamName': 'string',
                'StreamARN': 'string',
                'StreamStatus': 'CREATING'|'DELETING'|'ACTIVE'|'UPDATING',
                'RetentionPeriodHours': 123,
                'StreamCreationTimestamp': datetime(2015, 1, 1),
                'EnhancedMonitoring': [
                    {
                        'ShardLevelMetrics': [
                            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
                        ]
                    },
                ],
                'EncryptionType': 'NONE'|'KMS',
                'KeyId': 'string',
                'OpenShardCount': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StreamDescriptionSummary** *(dict) --* 

          A  StreamDescriptionSummary containing information about the stream.

          
          

          - **StreamName** *(string) --* 

            The name of the stream being described.

            
          

          - **StreamARN** *(string) --* 

            The Amazon Resource Name (ARN) for the stream being described.

            
          

          - **StreamStatus** *(string) --* 

            The current status of the stream being described. The stream status is one of the following states:

             

             
            * ``CREATING`` - The stream is being created. Kinesis Streams immediately returns and sets ``StreamStatus`` to ``CREATING`` . 
             
            * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING`` state until Kinesis Streams completes the deletion. 
             
            * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an ``ACTIVE`` stream. 
             
            * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the ``UPDATING`` state. 
             

            
          

          - **RetentionPeriodHours** *(integer) --* 

            The current retention period, in hours.

            
          

          - **StreamCreationTimestamp** *(datetime) --* 

            The approximate time that the stream was created.

            
          

          - **EnhancedMonitoring** *(list) --* 

            Represents the current enhanced monitoring settings of the stream.

            
            

            - *(dict) --* 

              Represents enhanced metrics types.

              
              

              - **ShardLevelMetrics** *(list) --* 

                List of shard-level metrics.

                 

                The following are the valid shard-level metrics. The value "``ALL`` " enhances every metric.

                 

                 
                * ``IncomingBytes``   
                 
                * ``IncomingRecords``   
                 
                * ``OutgoingBytes``   
                 
                * ``OutgoingRecords``   
                 
                * ``WriteProvisionedThroughputExceeded``   
                 
                * ``ReadProvisionedThroughputExceeded``   
                 
                * ``IteratorAgeMilliseconds``   
                 
                * ``ALL``   
                 

                 

                For more information, see `Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

                
                

                - *(string) --* 
            
          
        
          

          - **EncryptionType** *(string) --* 

            The encryption type used. This value is one of the following:

             

             
            * ``KMS``   
             
            * ``NONE``   
             

            
          

          - **KeyId** *(string) --* 

            The GUID for the customer-managed KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Streams by specifying the alias ``aws/kinesis`` .

             

             
            * Key ARN example: ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``   
             
            * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``   
             
            * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``   
             
            * Alias name example: ``alias/MyAliasName``   
             
            * Master key owned by Kinesis: ``alias/aws/kinesis``   
             

            
          

          - **OpenShardCount** *(integer) --* 

            The number of open shards in the stream.

            
      
    

  .. py:method:: disable_enhanced_monitoring(**kwargs)

    

    Disables enhanced monitoring.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DisableEnhancedMonitoring>`_    


    **Request Syntax** 
    ::

      response = client.disable_enhanced_monitoring(
          StreamName='string',
          ShardLevelMetrics=[
              'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
          ]
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the Kinesis stream for which to disable enhanced monitoring.

      

    
    :type ShardLevelMetrics: list
    :param ShardLevelMetrics: **[REQUIRED]** 

      List of shard-level metrics to disable.

       

      The following are the valid shard-level metrics. The value "``ALL`` " disables every metric.

       

       
      * ``IncomingBytes``   
       
      * ``IncomingRecords``   
       
      * ``OutgoingBytes``   
       
      * ``OutgoingRecords``   
       
      * ``WriteProvisionedThroughputExceeded``   
       
      * ``ReadProvisionedThroughputExceeded``   
       
      * ``IteratorAgeMilliseconds``   
       
      * ``ALL``   
       

       

      For more information, see `Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamName': 'string',
            'CurrentShardLevelMetrics': [
                'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
            ],
            'DesiredShardLevelMetrics': [
                'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for  EnableEnhancedMonitoring and  DisableEnhancedMonitoring .

        
        

        - **StreamName** *(string) --* 

          The name of the Kinesis stream.

          
        

        - **CurrentShardLevelMetrics** *(list) --* 

          Represents the current state of the metrics that are in the enhanced state before the operation.

          
          

          - *(string) --* 
      
        

        - **DesiredShardLevelMetrics** *(list) --* 

          Represents the list of all the metrics that would be in the enhanced state after the operation.

          
          

          - *(string) --* 
      
    

  .. py:method:: enable_enhanced_monitoring(**kwargs)

    

    Enables enhanced Kinesis stream monitoring for shard-level metrics.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/EnableEnhancedMonitoring>`_    


    **Request Syntax** 
    ::

      response = client.enable_enhanced_monitoring(
          StreamName='string',
          ShardLevelMetrics=[
              'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
          ]
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream for which to enable enhanced monitoring.

      

    
    :type ShardLevelMetrics: list
    :param ShardLevelMetrics: **[REQUIRED]** 

      List of shard-level metrics to enable.

       

      The following are the valid shard-level metrics. The value "``ALL`` " enables every metric.

       

       
      * ``IncomingBytes``   
       
      * ``IncomingRecords``   
       
      * ``OutgoingBytes``   
       
      * ``OutgoingRecords``   
       
      * ``WriteProvisionedThroughputExceeded``   
       
      * ``ReadProvisionedThroughputExceeded``   
       
      * ``IteratorAgeMilliseconds``   
       
      * ``ALL``   
       

       

      For more information, see `Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamName': 'string',
            'CurrentShardLevelMetrics': [
                'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
            ],
            'DesiredShardLevelMetrics': [
                'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for  EnableEnhancedMonitoring and  DisableEnhancedMonitoring .

        
        

        - **StreamName** *(string) --* 

          The name of the Kinesis stream.

          
        

        - **CurrentShardLevelMetrics** *(list) --* 

          Represents the current state of the metrics that are in the enhanced state before the operation.

          
          

          - *(string) --* 
      
        

        - **DesiredShardLevelMetrics** *(list) --* 

          Represents the list of all the metrics that would be in the enhanced state after the operation.

          
          

          - *(string) --* 
      
    

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

    

    Gets data records from a Kinesis stream's shard.

     

    Specify a shard iterator using the ``ShardIterator`` parameter. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to,  GetRecords returns an empty list. It might take multiple calls to get to a portion of the shard that contains records.

     

    You can scale by provisioning multiple shards per stream while considering service limits (for more information, see `Streams Limits <http://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html>`__ in the *Amazon Kinesis Streams Developer Guide* ). Your application should have one thread per shard, each reading continuously from its stream. To read from a stream continually, call  GetRecords in a loop. Use  GetShardIterator to get the shard iterator to specify in the first  GetRecords call.  GetRecords returns a new shard iterator in ``NextShardIterator`` . Specify the shard iterator returned in ``NextShardIterator`` in subsequent calls to  GetRecords . If the shard has been closed, the shard iterator can't return more data and  GetRecords returns ``null`` in ``NextShardIterator`` . You can terminate the loop when the shard is closed, or when the shard iterator reaches the record with the sequence number or other attribute that marks it as the last record to process.

     

    Each data record can be up to 1 MB in size, and each shard can read up to 2 MB per second. You can ensure that your calls don't exceed the maximum supported size or throughput by using the ``Limit`` parameter to specify the maximum number of records that  GetRecords can return. Consider your average record size when determining this limit.

     

    The size of the data returned by  GetRecords varies depending on the utilization of the shard. The maximum size of data that  GetRecords can return is 10 MB. If a call returns this amount of data, subsequent calls made within the next 5 seconds throw ``ProvisionedThroughputExceededException`` . If there is insufficient provisioned throughput on the shard, subsequent calls made within the next 1 second throw ``ProvisionedThroughputExceededException`` .  GetRecords won't return any data when it throws an exception. For this reason, we recommend that you wait one second between calls to  GetRecords ; however, it's possible that the application will get exceptions for longer than 1 second.

     

    To detect whether the application is falling behind in processing, you can use the ``MillisBehindLatest`` response attribute. You can also monitor the stream using CloudWatch metrics and other mechanisms (see `Monitoring <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring.html>`__ in the *Amazon Kinesis Streams Developer Guide* ).

     

    Each Amazon Kinesis record includes a value, ``ApproximateArrivalTimestamp`` , that is set when a stream successfully receives and stores a record. This is commonly referred to as a server-side time stamp, whereas a client-side time stamp is set when a data producer creates or sends the record to a stream (a data producer is any data source putting data records into a stream, for example with  PutRecords ). The time stamp has millisecond precision. There are no guarantees about the time stamp accuracy, or that the time stamp is always increasing. For example, records in a shard or across a stream might have time stamps that are out of order.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/GetRecords>`_    


    **Request Syntax** 
    ::

      response = client.get_records(
          ShardIterator='string',
          Limit=123
      )
    :type ShardIterator: string
    :param ShardIterator: **[REQUIRED]** 

      The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000,  GetRecords throws ``InvalidArgumentException`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Records': [
                {
                    'SequenceNumber': 'string',
                    'ApproximateArrivalTimestamp': datetime(2015, 1, 1),
                    'Data': b'bytes',
                    'PartitionKey': 'string',
                    'EncryptionType': 'NONE'|'KMS'
                },
            ],
            'NextShardIterator': 'string',
            'MillisBehindLatest': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for  GetRecords .

        
        

        - **Records** *(list) --* 

          The data records retrieved from the shard.

          
          

          - *(dict) --* 

            The unit of data of the Kinesis stream, which is composed of a sequence number, a partition key, and a data blob.

            
            

            - **SequenceNumber** *(string) --* 

              The unique identifier of the record within its shard.

              
            

            - **ApproximateArrivalTimestamp** *(datetime) --* 

              The approximate time that the record was inserted into the stream.

              
            

            - **Data** *(bytes) --* 

              The data blob. The data in the blob is both opaque and immutable to Kinesis Streams, which does not inspect, interpret, or change the data in the blob in any way. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).

              
            

            - **PartitionKey** *(string) --* 

              Identifies which shard in the stream the data record is assigned to.

              
            

            - **EncryptionType** *(string) --* 

              The encryption type used on the record. This parameter can be one of the following values:

               

               
              * ``NONE`` : Do not encrypt the records in the stream. 
               
              * ``KMS`` : Use server-side encryption on the records in the stream using a customer-managed KMS key. 
               

              
        
      
        

        - **NextShardIterator** *(string) --* 

          The next position in the shard from which to start sequentially reading data records. If set to ``null`` , the shard has been closed and the requested iterator does not return any more data. 

          
        

        - **MillisBehindLatest** *(integer) --* 

          The number of milliseconds the  GetRecords response is from the tip of the stream, indicating how far behind current time the consumer is. A value of zero indicates that record processing is caught up, and there are no new records to process at this moment.

          
    

  .. py:method:: get_shard_iterator(**kwargs)

    

    Gets an Amazon Kinesis shard iterator. A shard iterator expires five minutes after it is returned to the requester.

     

    A shard iterator specifies the shard position from which to start reading data records sequentially. The position is specified using the sequence number of a data record in a shard. A sequence number is the identifier associated with every record ingested in the stream, and is assigned when a record is put into the stream. Each stream has one or more shards.

     

    You must specify the shard iterator type. For example, you can set the ``ShardIteratorType`` parameter to read exactly from the position denoted by a specific sequence number by using the ``AT_SEQUENCE_NUMBER`` shard iterator type. Alternatively, the parameter can read right after the sequence number by using the ``AFTER_SEQUENCE_NUMBER`` shard iterator type, using sequence numbers returned by earlier calls to  PutRecord ,  PutRecords ,  GetRecords , or  DescribeStream . In the request, you can specify the shard iterator type ``AT_TIMESTAMP`` to read records from an arbitrary point in time, ``TRIM_HORIZON`` to cause ``ShardIterator`` to point to the last untrimmed record in the shard in the system (the oldest data record in the shard), or ``LATEST`` so that you always read the most recent data in the shard. 

     

    When you read repeatedly from a stream, use a  GetShardIterator request to get the first shard iterator for use in your first  GetRecords request and for subsequent reads use the shard iterator returned by the  GetRecords request in ``NextShardIterator`` . A new shard iterator is returned by every  GetRecords request in ``NextShardIterator`` , which you use in the ``ShardIterator`` parameter of the next  GetRecords request. 

     

    If a  GetShardIterator request is made too often, you receive a ``ProvisionedThroughputExceededException`` . For more information about throughput limits, see  GetRecords , and `Streams Limits <http://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

    If the shard is closed,  GetShardIterator returns a valid iterator for the last sequence number of the shard. A shard can be closed as a result of using  SplitShard or  MergeShards .

     

      GetShardIterator has a limit of 5 transactions per second per account per open shard.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/GetShardIterator>`_    


    **Request Syntax** 
    ::

      response = client.get_shard_iterator(
          StreamName='string',
          ShardId='string',
          ShardIteratorType='AT_SEQUENCE_NUMBER'|'AFTER_SEQUENCE_NUMBER'|'TRIM_HORIZON'|'LATEST'|'AT_TIMESTAMP',
          StartingSequenceNumber='string',
          Timestamp=datetime(2015, 1, 1)
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the Amazon Kinesis stream.

      

    
    :type ShardId: string
    :param ShardId: **[REQUIRED]** 

      The shard ID of the Kinesis Streams shard to get the iterator for.

      

    
    :type ShardIteratorType: string
    :param ShardIteratorType: **[REQUIRED]** 

      Determines how the shard iterator is used to start reading data records from the shard.

       

      The following are the valid Amazon Kinesis shard iterator types:

       

       
      * AT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value ``StartingSequenceNumber`` . 
       
      * AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value ``StartingSequenceNumber`` . 
       
      * AT_TIMESTAMP - Start reading from the position denoted by a specific time stamp, provided in the value ``Timestamp`` . 
       
      * TRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard. 
       
      * LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard. 
       

      

    
    :type StartingSequenceNumber: string
    :param StartingSequenceNumber: 

      The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT_SEQUENCE_NUMBER and AFTER_SEQUENCE_NUMBER.

      

    
    :type Timestamp: datetime
    :param Timestamp: 

      The time stamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. A time stamp is the Unix epoch date with precision in milliseconds. For example, ``2016-04-04T19:58:46.480-00:00`` or ``1459799926.480`` . If a record with this exact time stamp does not exist, the iterator returned is for the next (later) record. If the time stamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ShardIterator': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for ``GetShardIterator`` .

        
        

        - **ShardIterator** *(string) --* 

          The position in the shard from which to start reading data records sequentially. A shard iterator specifies this position using the sequence number of a data record in a shard.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: increase_stream_retention_period(**kwargs)

    

    Increases the Amazon Kinesis stream's retention period, which is the length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours (7 days).

     

    If you choose a longer stream retention period, this operation increases the time period during which records that have not yet expired are accessible. However, it does not make previous, expired data (older than the stream's previous retention period) accessible after the operation has been called. For example, if a stream's retention period is set to 24 hours and is increased to 168 hours, any data that is older than 24 hours remains inaccessible to consumer applications.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/IncreaseStreamRetentionPeriod>`_    


    **Request Syntax** 
    ::

      response = client.increase_stream_retention_period(
          StreamName='string',
          RetentionPeriodHours=123
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to modify.

      

    
    :type RetentionPeriodHours: integer
    :param RetentionPeriodHours: **[REQUIRED]** 

      The new retention period of the stream, in hours. Must be more than the current retention period.

      

    
    
    :returns: None

  .. py:method:: list_streams(**kwargs)

    

    Lists your Kinesis streams.

     

    The number of streams may be too large to return from a single call to ``ListStreams`` . You can limit the number of returned streams using the ``Limit`` parameter. If you do not specify a value for the ``Limit`` parameter, Kinesis Streams uses the default limit, which is currently 10.

     

    You can detect if there are more streams available to list by using the ``HasMoreStreams`` flag from the returned output. If there are more streams available, you can request more streams by using the name of the last stream returned by the ``ListStreams`` request in the ``ExclusiveStartStreamName`` parameter in a subsequent request to ``ListStreams`` . The group of stream names returned by the subsequent request is then added to the list. You can continue this process until all the stream names have been collected in the list. 

     

      ListStreams has a limit of 5 transactions per second per account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/ListStreams>`_    


    **Request Syntax** 
    ::

      response = client.list_streams(
          Limit=123,
          ExclusiveStartStreamName='string'
      )
    :type Limit: integer
    :param Limit: 

      The maximum number of streams to list.

      

    
    :type ExclusiveStartStreamName: string
    :param ExclusiveStartStreamName: 

      The name of the stream to start the list with.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamNames': [
                'string',
            ],
            'HasMoreStreams': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for ``ListStreams`` .

        
        

        - **StreamNames** *(list) --* 

          The names of the streams that are associated with the AWS account making the ``ListStreams`` request.

          
          

          - *(string) --* 
      
        

        - **HasMoreStreams** *(boolean) --* 

          If set to ``true`` , there are more streams available to list.

          
    

  .. py:method:: list_tags_for_stream(**kwargs)

    

    Lists the tags for the specified Kinesis stream.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/ListTagsForStream>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_stream(
          StreamName='string',
          ExclusiveStartTagKey='string',
          Limit=123
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream.

      

    
    :type ExclusiveStartTagKey: string
    :param ExclusiveStartTagKey: 

      The key to use as the starting point for the list of tags. If this parameter is set, ``ListTagsForStream`` gets all tags that occur after ``ExclusiveStartTagKey`` . 

      

    
    :type Limit: integer
    :param Limit: 

      The number of tags to return. If this number is less than the total number of tags associated with the stream, ``HasMoreTags`` is set to ``true`` . To list additional tags, set ``ExclusiveStartTagKey`` to the last key in the response.

      

    
    
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
            'HasMoreTags': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for ``ListTagsForStream`` .

        
        

        - **Tags** *(list) --* 

          A list of tags associated with ``StreamName`` , starting with the first tag after ``ExclusiveStartTagKey`` and up to the specified ``Limit`` . 

          
          

          - *(dict) --* 

            Metadata assigned to the stream, consisting of a key-value pair.

            
            

            - **Key** *(string) --* 

              A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @

              
            

            - **Value** *(string) --* 

              An optional string, typically used to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @

              
        
      
        

        - **HasMoreTags** *(boolean) --* 

          If set to ``true`` , more tags are available. To request additional tags, set ``ExclusiveStartTagKey`` to the key of the last tag returned.

          
    

  .. py:method:: merge_shards(**kwargs)

    

    Merges two adjacent shards in a Kinesis stream and combines them into a single shard to reduce the stream's capacity to ingest and transport data. Two shards are considered adjacent if the union of the hash key ranges for the two shards form a contiguous set with no gaps. For example, if you have two shards, one with a hash key range of 276...381 and the other with a hash key range of 382...454, then you could merge these two shards into a single shard that would have a hash key range of 276...454. After the merge, the single child shard receives data for all hash key values covered by the two parent shards.

     

     ``MergeShards`` is called when there is a need to reduce the overall capacity of a stream because of excess capacity that is not being used. You must specify the shard to be merged and the adjacent shard for a stream. For more information about merging shards, see `Merge Two Shards <http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-resharding-merge.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

    If the stream is in the ``ACTIVE`` state, you can call ``MergeShards`` . If a stream is in the ``CREATING`` , ``UPDATING`` , or ``DELETING`` state, ``MergeShards`` returns a ``ResourceInUseException`` . If the specified stream does not exist, ``MergeShards`` returns a ``ResourceNotFoundException`` . 

     

    You can use  DescribeStream to check the state of the stream, which is returned in ``StreamStatus`` .

     

     ``MergeShards`` is an asynchronous operation. Upon receiving a ``MergeShards`` request, Amazon Kinesis immediately returns a response and sets the ``StreamStatus`` to ``UPDATING`` . After the operation is completed, Amazon Kinesis sets the ``StreamStatus`` to ``ACTIVE`` . Read and write operations continue to work while the stream is in the ``UPDATING`` state. 

     

    You use  DescribeStream to determine the shard IDs that are specified in the ``MergeShards`` request. 

     

    If you try to operate on too many streams in parallel using  CreateStream ,  DeleteStream , ``MergeShards`` or  SplitShard , you will receive a ``LimitExceededException`` . 

     

     ``MergeShards`` has a limit of 5 transactions per second per account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/MergeShards>`_    


    **Request Syntax** 
    ::

      response = client.merge_shards(
          StreamName='string',
          ShardToMerge='string',
          AdjacentShardToMerge='string'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream for the merge.

      

    
    :type ShardToMerge: string
    :param ShardToMerge: **[REQUIRED]** 

      The shard ID of the shard to combine with the adjacent shard for the merge.

      

    
    :type AdjacentShardToMerge: string
    :param AdjacentShardToMerge: **[REQUIRED]** 

      The shard ID of the adjacent shard for the merge.

      

    
    
    :returns: None

  .. py:method:: put_record(**kwargs)

    

    Writes a single data record into an Amazon Kinesis stream. Call ``PutRecord`` to send data into the stream for real-time ingestion and subsequent processing, one record at a time. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second.

     

    You must specify the name of the stream that captures, stores, and transports the data; a partition key; and the data blob itself.

     

    The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.

     

    The partition key is used by Kinesis Streams to distribute data across shards. Kinesis Streams segregates the data records that belong to a stream into multiple shards, using the partition key associated with each data record to determine the shard to which a given data record belongs.

     

    Partition keys are Unicode strings, with a maximum length limit of 256 characters for each key. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards using the hash key ranges of the shards. You can override hashing the partition key to determine the shard by explicitly specifying a hash value using the ``ExplicitHashKey`` parameter. For more information, see `Adding Data to a Stream <http://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-add-data-to-stream>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

     ``PutRecord`` returns the shard ID of where the data record was placed and the sequence number that was assigned to the data record.

     

    Sequence numbers increase over time and are specific to a shard within a stream, not across all shards within a stream. To guarantee strictly increasing ordering, write serially to a shard and use the ``SequenceNumberForOrdering`` parameter. For more information, see `Adding Data to a Stream <http://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-add-data-to-stream>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

    If a ``PutRecord`` request cannot be processed because of insufficient provisioned throughput on the shard involved in the request, ``PutRecord`` throws ``ProvisionedThroughputExceededException`` . 

     

    By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use  IncreaseStreamRetentionPeriod or  DecreaseStreamRetentionPeriod to modify this retention period.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/PutRecord>`_    


    **Request Syntax** 
    ::

      response = client.put_record(
          StreamName='string',
          Data=b'bytes',
          PartitionKey='string',
          ExplicitHashKey='string',
          SequenceNumberForOrdering='string'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to put the data record into.

      

    
    :type Data: bytes
    :param Data: **[REQUIRED]** 

      The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).

      

    
    :type PartitionKey: string
    :param PartitionKey: **[REQUIRED]** 

      Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.

      

    
    :type ExplicitHashKey: string
    :param ExplicitHashKey: 

      The hash value used to explicitly determine the shard the data record is assigned to by overriding the partition key hash.

      

    
    :type SequenceNumberForOrdering: string
    :param SequenceNumberForOrdering: 

      Guarantees strictly increasing sequence numbers, for puts from the same client and to the same partition key. Usage: set the ``SequenceNumberForOrdering`` of record *n* to the sequence number of record *n-1* (as returned in the result when putting record *n-1* ). If this parameter is not set, records are coarsely ordered based on arrival time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ShardId': 'string',
            'SequenceNumber': 'string',
            'EncryptionType': 'NONE'|'KMS'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for ``PutRecord`` .

        
        

        - **ShardId** *(string) --* 

          The shard ID of the shard where the data record was placed.

          
        

        - **SequenceNumber** *(string) --* 

          The sequence number identifier that was assigned to the put data record. The sequence number for the record is unique across all records in the stream. A sequence number is the identifier associated with every record put into the stream.

          
        

        - **EncryptionType** *(string) --* 

          The encryption type to use on the record. This parameter can be one of the following values:

           

           
          * ``NONE`` : Do not encrypt the records in the stream. 
           
          * ``KMS`` : Use server-side encryption on the records in the stream using a customer-managed KMS key. 
           

          
    

  .. py:method:: put_records(**kwargs)

    

    Writes multiple data records into a Kinesis stream in a single call (also referred to as a ``PutRecords`` request). Use this operation to send data into the stream for data ingestion and processing. 

     

    Each ``PutRecords`` request can support up to 500 records. Each record in the request can be as large as 1 MB, up to a limit of 5 MB for the entire request, including partition keys. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second.

     

    You must specify the name of the stream that captures, stores, and transports the data; and an array of request ``Records`` , with each record in the array requiring a partition key and data blob. The record size limit applies to the total size of the partition key and data blob.

     

    The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.

     

    The partition key is used by Kinesis Streams as input to a hash function that maps the partition key and associated data to a specific shard. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream. For more information, see `Adding Data to a Stream <http://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-add-data-to-stream>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

    Each record in the ``Records`` array may include an optional parameter, ``ExplicitHashKey`` , which overrides the partition key to shard mapping. This parameter allows a data producer to determine explicitly the shard where the record is stored. For more information, see `Adding Multiple Records with PutRecords <http://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-putrecords>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

    The ``PutRecords`` response includes an array of response ``Records`` . Each record in the response array directly correlates with a record in the request array using natural ordering, from the top to the bottom of the request and response. The response ``Records`` array always includes the same number of records as the request array.

     

    The response ``Records`` array includes both successfully and unsuccessfully processed records. Amazon Kinesis attempts to process all records in each ``PutRecords`` request. A single record failure does not stop the processing of subsequent records.

     

    A successfully processed record includes ``ShardId`` and ``SequenceNumber`` values. The ``ShardId`` parameter identifies the shard in the stream where the record is stored. The ``SequenceNumber`` parameter is an identifier assigned to the put record, unique to all records in the stream.

     

    An unsuccessfully processed record includes ``ErrorCode`` and ``ErrorMessage`` values. ``ErrorCode`` reflects the type of error and can be one of the following values: ``ProvisionedThroughputExceededException`` or ``InternalFailure`` . ``ErrorMessage`` provides more detailed information about the ``ProvisionedThroughputExceededException`` exception including the account ID, stream name, and shard ID of the record that was throttled. For more information about partially successful responses, see `Adding Multiple Records with PutRecords <http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-add-data-to-stream.html#kinesis-using-sdk-java-putrecords>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

    By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use  IncreaseStreamRetentionPeriod or  DecreaseStreamRetentionPeriod to modify this retention period.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/PutRecords>`_    


    **Request Syntax** 
    ::

      response = client.put_records(
          Records=[
              {
                  'Data': b'bytes',
                  'ExplicitHashKey': 'string',
                  'PartitionKey': 'string'
              },
          ],
          StreamName='string'
      )
    :type Records: list
    :param Records: **[REQUIRED]** 

      The records associated with the request.

      

    
      - *(dict) --* 

        Represents the output for ``PutRecords`` .

        

      
        - **Data** *(bytes) --* **[REQUIRED]** 

          The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).

          

        
        - **ExplicitHashKey** *(string) --* 

          The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.

          

        
        - **PartitionKey** *(string) --* **[REQUIRED]** 

          Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.

          

        
      
  
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The stream name associated with the request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedRecordCount': 123,
            'Records': [
                {
                    'SequenceNumber': 'string',
                    'ShardId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ],
            'EncryptionType': 'NONE'|'KMS'
        }
      **Response Structure** 

      

      - *(dict) --* 

         ``PutRecords`` results.

        
        

        - **FailedRecordCount** *(integer) --* 

          The number of unsuccessfully processed records in a ``PutRecords`` request.

          
        

        - **Records** *(list) --* 

          An array of successfully and unsuccessfully processed record results, correlated with the request by natural ordering. A record that is successfully added to a stream includes ``SequenceNumber`` and ``ShardId`` in the result. A record that fails to be added to a stream includes ``ErrorCode`` and ``ErrorMessage`` in the result.

          
          

          - *(dict) --* 

            Represents the result of an individual record from a ``PutRecords`` request. A record that is successfully added to a stream includes ``SequenceNumber`` and ``ShardId`` in the result. A record that fails to be added to the stream includes ``ErrorCode`` and ``ErrorMessage`` in the result.

            
            

            - **SequenceNumber** *(string) --* 

              The sequence number for an individual record result.

              
            

            - **ShardId** *(string) --* 

              The shard ID for an individual record result.

              
            

            - **ErrorCode** *(string) --* 

              The error code for an individual record result. ``ErrorCodes`` can be either ``ProvisionedThroughputExceededException`` or ``InternalFailure`` .

              
            

            - **ErrorMessage** *(string) --* 

              The error message for an individual record result. An ``ErrorCode`` value of ``ProvisionedThroughputExceededException`` has an error message that includes the account ID, stream name, and shard ID. An ``ErrorCode`` value of ``InternalFailure`` has the error message ``"Internal Service Failure"`` .

              
        
      
        

        - **EncryptionType** *(string) --* 

          The encryption type used on the records. This parameter can be one of the following values:

           

           
          * ``NONE`` : Do not encrypt the records. 
           
          * ``KMS`` : Use server-side encryption on the records using a customer-managed KMS key. 
           

          
    

  .. py:method:: remove_tags_from_stream(**kwargs)

    

    Removes tags from the specified Kinesis stream. Removed tags are deleted and cannot be recovered after this operation successfully completes.

     

    If you specify a tag that does not exist, it is ignored.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/RemoveTagsFromStream>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags_from_stream(
          StreamName='string',
          TagKeys=[
              'string',
          ]
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream.

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      A list of tag keys. Each corresponding tag is removed from the stream.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: split_shard(**kwargs)

    

    Splits a shard into two new shards in the Kinesis stream, to increase the stream's capacity to ingest and transport data. ``SplitShard`` is called when there is a need to increase the overall capacity of a stream because of an expected increase in the volume of data records being ingested. 

     

    You can also use ``SplitShard`` when a shard appears to be approaching its maximum utilization; for example, the producers sending data into the specific shard are suddenly sending more than previously anticipated. You can also call ``SplitShard`` to increase stream capacity, so that more Kinesis Streams applications can simultaneously read data from the stream for real-time processing. 

     

    You must specify the shard to be split and the new hash key, which is the position in the shard where the shard gets split in two. In many cases, the new hash key might be the average of the beginning and ending hash key, but it can be any hash key value in the range being mapped into the shard. For more information, see `Split a Shard <http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-resharding-split.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

     

    You can use  DescribeStream to determine the shard ID and hash key values for the ``ShardToSplit`` and ``NewStartingHashKey`` parameters that are specified in the ``SplitShard`` request.

     

     ``SplitShard`` is an asynchronous operation. Upon receiving a ``SplitShard`` request, Kinesis Streams immediately returns a response and sets the stream status to ``UPDATING`` . After the operation is completed, Kinesis Streams sets the stream status to ``ACTIVE`` . Read and write operations continue to work while the stream is in the ``UPDATING`` state. 

     

    You can use ``DescribeStream`` to check the status of the stream, which is returned in ``StreamStatus`` . If the stream is in the ``ACTIVE`` state, you can call ``SplitShard`` . If a stream is in ``CREATING`` or ``UPDATING`` or ``DELETING`` states, ``DescribeStream`` returns a ``ResourceInUseException`` .

     

    If the specified stream does not exist, ``DescribeStream`` returns a ``ResourceNotFoundException`` . If you try to create more shards than are authorized for your account, you receive a ``LimitExceededException`` . 

     

    For the default shard limit for an AWS account, see `Streams Limits <http://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html>`__ in the *Amazon Kinesis Streams Developer Guide* . To increase this limit, `contact AWS Support <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>`__ .

     

    If you try to operate on too many streams simultaneously using  CreateStream ,  DeleteStream ,  MergeShards , and/or  SplitShard , you receive a ``LimitExceededException`` . 

     

     ``SplitShard`` has a limit of 5 transactions per second per account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/SplitShard>`_    


    **Request Syntax** 
    ::

      response = client.split_shard(
          StreamName='string',
          ShardToSplit='string',
          NewStartingHashKey='string'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream for the shard split.

      

    
    :type ShardToSplit: string
    :param ShardToSplit: **[REQUIRED]** 

      The shard ID of the shard to split.

      

    
    :type NewStartingHashKey: string
    :param NewStartingHashKey: **[REQUIRED]** 

      A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for ``NewStartingHashKey`` must be in the range of hash keys being mapped into the shard. The ``NewStartingHashKey`` hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.

      

    
    
    :returns: None

  .. py:method:: start_stream_encryption(**kwargs)

    

    Enables or updates server-side encryption using an AWS KMS key for a specified stream. 

     

    Starting encryption is an asynchronous operation. Upon receiving the request, Kinesis Streams returns immediately and sets the status of the stream to ``UPDATING`` . After the update is complete, Kinesis Streams sets the status of the stream back to ``ACTIVE`` . Updating or applying encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is ``UPDATING`` . Once the status of the stream is ``ACTIVE`` , encryption begins for records written to the stream. 

     

    API Limits: You can successfully apply a new AWS KMS key for server-side encryption 25 times in a rolling 24-hour period.

     

    Note: It can take up to five seconds after the stream is in an ``ACTIVE`` status before all records written to the stream are encrypted. After you enable encryption, you can verify that encryption is applied by inspecting the API response from ``PutRecord`` or ``PutRecords`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/StartStreamEncryption>`_    


    **Request Syntax** 
    ::

      response = client.start_stream_encryption(
          StreamName='string',
          EncryptionType='NONE'|'KMS',
          KeyId='string'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream for which to start encrypting records.

      

    
    :type EncryptionType: string
    :param EncryptionType: **[REQUIRED]** 

      The encryption type to use. The only valid value is ``KMS`` .

      

    
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The GUID for the customer-managed KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Streams by specifying the alias ``aws/kinesis`` .

       

       
      * Key ARN example: ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``   
       
      * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``   
       
      * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``   
       
      * Alias name example: ``alias/MyAliasName``   
       
      * Master key owned by Kinesis Streams: ``alias/aws/kinesis``   
       

      

    
    
    :returns: None

  .. py:method:: stop_stream_encryption(**kwargs)

    

    Disables server-side encryption for a specified stream. 

     

    Stopping encryption is an asynchronous operation. Upon receiving the request, Kinesis Streams returns immediately and sets the status of the stream to ``UPDATING`` . After the update is complete, Kinesis Streams sets the status of the stream back to ``ACTIVE`` . Stopping encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is ``UPDATING`` . Once the status of the stream is ``ACTIVE`` , records written to the stream are no longer encrypted by Kinesis Streams. 

     

    API Limits: You can successfully disable server-side encryption 25 times in a rolling 24-hour period. 

     

    Note: It can take up to five seconds after the stream is in an ``ACTIVE`` status before all records written to the stream are no longer subject to encryption. After you disabled encryption, you can verify that encryption is not applied by inspecting the API response from ``PutRecord`` or ``PutRecords`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/StopStreamEncryption>`_    


    **Request Syntax** 
    ::

      response = client.stop_stream_encryption(
          StreamName='string',
          EncryptionType='NONE'|'KMS',
          KeyId='string'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream on which to stop encrypting records.

      

    
    :type EncryptionType: string
    :param EncryptionType: **[REQUIRED]** 

      The encryption type. The only valid value is ``KMS`` .

      

    
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The GUID for the customer-managed KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Streams by specifying the alias ``aws/kinesis`` .

       

       
      * Key ARN example: ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``   
       
      * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``   
       
      * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``   
       
      * Alias name example: ``alias/MyAliasName``   
       
      * Master key owned by Kinesis Streams: ``alias/aws/kinesis``   
       

      

    
    
    :returns: None

  .. py:method:: update_shard_count(**kwargs)

    

    Updates the shard count of the specified stream to the specified number of shards.

     

    Updating the shard count is an asynchronous operation. Upon receiving the request, Kinesis Streams returns immediately and sets the status of the stream to ``UPDATING`` . After the update is complete, Kinesis Streams sets the status of the stream back to ``ACTIVE`` . Depending on the size of the stream, the scaling action could take a few minutes to complete. You can continue to read and write data to your stream while its status is ``UPDATING`` .

     

    To update the shard count, Kinesis Streams performs splits or merges on individual shards. This can cause short-lived shards to be created, in addition to the final shards. We recommend that you double or halve the shard count, as this results in the fewest number of splits or merges.

     

    This operation has the following limits, which are per region per account unless otherwise noted. You cannot:

     

     
    * Scale more than twice per rolling 24 hour period 
     
    * Scale up to double your current shard count 
     
    * Scale down below half your current shard count 
     
    * Scale up to more 500 shards in a stream 
     
    * Scale a stream with more than 500 shards down unless the result is less than 500 shards 
     
    * Scale up more the shard limits for your account 
     
    * 
     

     

    For the default limits for an AWS account, see `Streams Limits <http://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html>`__ in the *Amazon Kinesis Streams Developer Guide* . To increase a limit, `contact AWS Support <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/UpdateShardCount>`_    


    **Request Syntax** 
    ::

      response = client.update_shard_count(
          StreamName='string',
          TargetShardCount=123,
          ScalingType='UNIFORM_SCALING'
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream.

      

    
    :type TargetShardCount: integer
    :param TargetShardCount: **[REQUIRED]** 

      The new number of shards.

      

    
    :type ScalingType: string
    :param ScalingType: **[REQUIRED]** 

      The scaling type. Uniform scaling creates shards of equal size.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamName': 'string',
            'CurrentShardCount': 123,
            'TargetShardCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StreamName** *(string) --* 

          The name of the stream.

          
        

        - **CurrentShardCount** *(integer) --* 

          The current number of shards.

          
        

        - **TargetShardCount** *(integer) --* 

          The updated number of shards.

          
    

==========
Paginators
==========


The available paginators are:

* :py:class:`Kinesis.Paginator.DescribeStream`


* :py:class:`Kinesis.Paginator.ListStreams`



.. py:class:: Kinesis.Paginator.DescribeStream

  ::

    
    paginator = client.get_paginator('describe_stream')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Kinesis.Client.describe_stream`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStream>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          StreamName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to describe.

      

    
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
            'StreamDescription': {
                'StreamName': 'string',
                'StreamARN': 'string',
                'StreamStatus': 'CREATING'|'DELETING'|'ACTIVE'|'UPDATING',
                'Shards': [
                    {
                        'ShardId': 'string',
                        'ParentShardId': 'string',
                        'AdjacentParentShardId': 'string',
                        'HashKeyRange': {
                            'StartingHashKey': 'string',
                            'EndingHashKey': 'string'
                        },
                        'SequenceNumberRange': {
                            'StartingSequenceNumber': 'string',
                            'EndingSequenceNumber': 'string'
                        }
                    },
                ],
                'HasMoreShards': True|False,
                'RetentionPeriodHours': 123,
                'StreamCreationTimestamp': datetime(2015, 1, 1),
                'EnhancedMonitoring': [
                    {
                        'ShardLevelMetrics': [
                            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
                        ]
                    },
                ],
                'EncryptionType': 'NONE'|'KMS',
                'KeyId': 'string'
            },
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for ``DescribeStream`` .

        
        

        - **StreamDescription** *(dict) --* 

          The current status of the stream, the stream ARN, an array of shard objects that comprise the stream, and whether there are more shards available.

          
          

          - **StreamName** *(string) --* 

            The name of the stream being described.

            
          

          - **StreamARN** *(string) --* 

            The Amazon Resource Name (ARN) for the stream being described.

            
          

          - **StreamStatus** *(string) --* 

            The current status of the stream being described. The stream status is one of the following states:

             

             
            * ``CREATING`` - The stream is being created. Kinesis Streams immediately returns and sets ``StreamStatus`` to ``CREATING`` . 
             
            * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING`` state until Kinesis Streams completes the deletion. 
             
            * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an ``ACTIVE`` stream. 
             
            * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the ``UPDATING`` state. 
             

            
          

          - **Shards** *(list) --* 

            The shards that comprise the stream.

            
            

            - *(dict) --* 

              A uniquely identified group of data records in a Kinesis stream.

              
              

              - **ShardId** *(string) --* 

                The unique identifier of the shard within the stream.

                
              

              - **ParentShardId** *(string) --* 

                The shard ID of the shard's parent.

                
              

              - **AdjacentParentShardId** *(string) --* 

                The shard ID of the shard adjacent to the shard's parent.

                
              

              - **HashKeyRange** *(dict) --* 

                The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.

                
                

                - **StartingHashKey** *(string) --* 

                  The starting hash key of the hash key range.

                  
                

                - **EndingHashKey** *(string) --* 

                  The ending hash key of the hash key range.

                  
            
              

              - **SequenceNumberRange** *(dict) --* 

                The range of possible sequence numbers for the shard.

                
                

                - **StartingSequenceNumber** *(string) --* 

                  The starting sequence number for the range.

                  
                

                - **EndingSequenceNumber** *(string) --* 

                  The ending sequence number for the range. Shards that are in the OPEN state have an ending sequence number of ``null`` .

                  
            
          
        
          

          - **HasMoreShards** *(boolean) --* 

            If set to ``true`` , more shards in the stream are available to describe.

            
          

          - **RetentionPeriodHours** *(integer) --* 

            The current retention period, in hours.

            
          

          - **StreamCreationTimestamp** *(datetime) --* 

            The approximate time that the stream was created.

            
          

          - **EnhancedMonitoring** *(list) --* 

            Represents the current enhanced monitoring settings of the stream.

            
            

            - *(dict) --* 

              Represents enhanced metrics types.

              
              

              - **ShardLevelMetrics** *(list) --* 

                List of shard-level metrics.

                 

                The following are the valid shard-level metrics. The value "``ALL`` " enhances every metric.

                 

                 
                * ``IncomingBytes``   
                 
                * ``IncomingRecords``   
                 
                * ``OutgoingBytes``   
                 
                * ``OutgoingRecords``   
                 
                * ``WriteProvisionedThroughputExceeded``   
                 
                * ``ReadProvisionedThroughputExceeded``   
                 
                * ``IteratorAgeMilliseconds``   
                 
                * ``ALL``   
                 

                 

                For more information, see `Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in the *Amazon Kinesis Streams Developer Guide* .

                
                

                - *(string) --* 
            
          
        
          

          - **EncryptionType** *(string) --* 

            The server-side encryption type used on the stream. This parameter can be one of the following values:

             

             
            * ``NONE`` : Do not encrypt the records in the stream. 
             
            * ``KMS`` : Use server-side encryption on the records in the stream using a customer-managed KMS key. 
             

            
          

          - **KeyId** *(string) --* 

            The GUID for the customer-managed KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Streams by specifying the alias ``aws/kinesis`` .

             

             
            * Key ARN example: ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``   
             
            * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``   
             
            * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``   
             
            * Alias name example: ``alias/MyAliasName``   
             
            * Master key owned by Kinesis Streams: ``alias/aws/kinesis``   
             

            
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Kinesis.Paginator.ListStreams

  ::

    
    paginator = client.get_paginator('list_streams')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Kinesis.Client.list_streams`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/ListStreams>`_    


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
            'StreamNames': [
                'string',
            ],
            'HasMoreStreams': True|False,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output for ``ListStreams`` .

        
        

        - **StreamNames** *(list) --* 

          The names of the streams that are associated with the AWS account making the ``ListStreams`` request.

          
          

          - *(string) --* 
      
        

        - **HasMoreStreams** *(boolean) --* 

          If set to ``true`` , there are more streams available to list.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

=======
Waiters
=======


The available waiters are:

* :py:class:`Kinesis.Waiter.StreamExists`


* :py:class:`Kinesis.Waiter.StreamNotExists`



.. py:class:: Kinesis.Waiter.StreamExists

  ::

    
    waiter = client.get_waiter('stream_exists')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`Kinesis.Client.describe_stream` every 10 seconds until a successful state is reached. An error is returned after 18 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStream>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          StreamName='string',
          Limit=123,
          ExclusiveStartShardId='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to describe.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 shards are returned.

      

    
    :type ExclusiveStartShardId: string
    :param ExclusiveStartShardId: 

      The shard ID of the shard to start with.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 10

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 18

        

      
    
    
    :returns: None

.. py:class:: Kinesis.Waiter.StreamNotExists

  ::

    
    waiter = client.get_waiter('stream_not_exists')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`Kinesis.Client.describe_stream` every 10 seconds until a successful state is reached. An error is returned after 18 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStream>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          StreamName='string',
          Limit=123,
          ExclusiveStartShardId='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream to describe.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 shards are returned.

      

    
    :type ExclusiveStartShardId: string
    :param ExclusiveStartShardId: 

      The shard ID of the shard to start with.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 10

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 18

        

      
    
    
    :returns: None