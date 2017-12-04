

*****************
KinesisVideoMedia
*****************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: KinesisVideoMedia.Client

  A low-level client representing Amazon Kinesis Video Streams Media (Kinesis Video Media)::

    
    import boto3
    
    client = boto3.client('kinesis-video-media')

  
  These are the available methods:
  
  *   :py:meth:`~KinesisVideoMedia.Client.can_paginate`

  
  *   :py:meth:`~KinesisVideoMedia.Client.generate_presigned_url`

  
  *   :py:meth:`~KinesisVideoMedia.Client.get_media`

  
  *   :py:meth:`~KinesisVideoMedia.Client.get_paginator`

  
  *   :py:meth:`~KinesisVideoMedia.Client.get_waiter`

  

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


  .. py:method:: get_media(**kwargs)

    

    Use this API to retrieve media content from a Kinesis video stream. In the request, you identify stream name or stream Amazon Resource Name (ARN), and the starting chunk. Kinesis Video Streams then returns a stream of chunks in order by fragment number.

     

    .. note::

       

      You must first call the ``GetDataEndpoint`` API to get an endpoint to which you can then send the ``GetMedia`` requests. 

       

     

    When you put media data (fragments) on a stream, Kinesis Video Streams stores each incoming fragment and related metadata in what is called a "chunk." For more information, see . The ``GetMedia`` API returns a stream of these chunks starting from the chunk that you specify in the request. 

     

    The following limits apply when using the ``GetMedia`` API:

     

     
    * A client can call ``GetMedia`` up to five times per second per stream.  
     
    * Kinesis Video Streams sends media data at a rate of up to 25 megabytes per second (or 200 megabits per second) during a ``GetMedia`` session.  
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-media-2017-09-30/GetMedia>`_    


    **Request Syntax** 
    ::

      response = client.get_media(
          StreamName='string',
          StreamARN='string',
          StartSelector={
              'StartSelectorType': 'FRAGMENT_NUMBER'|'SERVER_TIMESTAMP'|'PRODUCER_TIMESTAMP'|'NOW'|'EARLIEST'|'CONTINUATION_TOKEN',
              'AfterFragmentNumber': 'string',
              'StartTimestamp': datetime(2015, 1, 1),
              'ContinuationToken': 'string'
          }
      )
    :type StreamName: string
    :param StreamName: 

      The Kinesis video stream name from where you want to get the media content. If you don't specify the ``streamName`` , you must specify the ``streamARN`` .

      

    
    :type StreamARN: string
    :param StreamARN: 

      The ARN of the stream from where you want to get the media content. If you don't specify the ``streamARN`` , you must specify the ``streamName`` .

      

    
    :type StartSelector: dict
    :param StartSelector: **[REQUIRED]** 

      Identifies the starting chunk to get from the specified stream. 

      

    
      - **StartSelectorType** *(string) --* **[REQUIRED]** 

        Identifies the fragment on the Kinesis video stream where you want to start getting the data from.

         

         
        * NOW - Start with the latest chunk on the stream. 
         
        * EARLIEST - Start with earliest available chunk on the stream. 
         
        * FRAGMENT_NUMBER - Start with the chunk containing the specific fragment. You must also specify the ``StartFragmentNumber`` . 
         
        * PRODUCER_TIMESTAMP or SERVER_TIMESTAMP - Start with the chunk containing a fragment with the specified producer or server time stamp. You specify the time stamp by adding ``StartTimestamp`` . 
         
        * CONTINUATION_TOKEN - Read using the specified continuation token.  
         

         

        .. note::

           

          If you choose the NOW, EARLIEST, or CONTINUATION_TOKEN as the ``startSelectorType`` , you don't provide any additional information in the ``startSelector`` .

           

        

      
      - **AfterFragmentNumber** *(string) --* 

        Specifies the fragment number from where you want the ``GetMedia`` API to start returning the fragments. 

        

      
      - **StartTimestamp** *(datetime) --* 

        A time stamp value. This value is required if you choose the PRODUCER_TIMESTAMP or the SERVER_TIMESTAMP as the ``startSelectorType`` . The ``GetMedia`` API then starts with the chunk containing the fragment that has the specified time stamp.

        

      
      - **ContinuationToken** *(string) --* 

        Continuation token that Kinesis Video Streams returned in the previous ``GetMedia`` response. The ``GetMedia`` API then starts with the chunk identified by the continuation token.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ContentType': 'string',
            'Payload': StreamingBody()
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ContentType** *(string) --* 

          The content type of the requested media.

          
        

        - **Payload** (:class:`.StreamingBody`) -- 

          The payload Kinesis Video Streams returns is a sequence of chunks from the specified stream. For information about the chunks, see . The chunks that Kinesis Video Streams returns in the ``GetMedia`` call also include the following additional Matroska (MKV) tags: 

           

           
          * AWS_KINESISVIDEO_CONTINUATION_TOKEN (UTF-8 string) - In the event your ``GetMedia`` call terminates, you can use this continuation token in your next request to get the next chunk where the last request terminated. 
           
          * AWS_KINESISVIDEO_MILLIS_BEHIND_NOW (UTF-8 string) - Client applications can use this tag value to determine how far behind the chunk returned in the response is from the latest chunk on the stream.  
           
          * AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk. 
           
          * AWS_KINESISVIDEO_SERVER_TIMESTAMP - Server time stamp of the fragment. 
           
          * AWS_KINESISVIDEO_PRODUCER_TIMESTAMP - Producer time stamp of the fragment. 
           

           

          The following tags will be present if an error occurs:

           

           
          * AWS_KINESISVIDEO_ERROR_CODE - String description of an error that caused GetMedia to stop. 
           
          * AWS_KINESISVIDEO_ERROR_ID: Integer code of the error. 
           

           

          The error codes are as follows:

           

           
          * 3002 - Error writing to the stream 
           
          * 4000 - Requested fragment is not found 
           
          * 4500 - Access denied for the stream's KMS key 
           
          * 4501 - Stream's KMS key is disabled 
           
          * 4502 - Validation error on the Stream's KMS key 
           
          * 4503 - KMS key specified in the stream is unavailable 
           
          * 4504 - Invalid usage of the KMS key specified in the stream 
           
          * 4505 - Invalid state of the KMS key specified in the stream 
           
          * 4506 - Unable to find the KMS key specified in the stream 
           
          * 5000 - Internal error 
           

          
    

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

        


==========
Paginators
==========


The available paginators are:
