

*************************
KinesisVideoArchivedMedia
*************************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: KinesisVideoArchivedMedia.Client

  A low-level client representing Amazon Kinesis Video Streams Archived Media (Kinesis Video Archived Media)::

    
    import boto3
    
    client = boto3.client('kinesis-video-archived-media')

  
  These are the available methods:
  
  *   :py:meth:`~KinesisVideoArchivedMedia.Client.can_paginate`

  
  *   :py:meth:`~KinesisVideoArchivedMedia.Client.generate_presigned_url`

  
  *   :py:meth:`~KinesisVideoArchivedMedia.Client.get_media_for_fragment_list`

  
  *   :py:meth:`~KinesisVideoArchivedMedia.Client.get_paginator`

  
  *   :py:meth:`~KinesisVideoArchivedMedia.Client.get_waiter`

  
  *   :py:meth:`~KinesisVideoArchivedMedia.Client.list_fragments`

  

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


  .. py:method:: get_media_for_fragment_list(**kwargs)

    

    Gets media for a list of fragments (specified by fragment number) from the archived data in a Kinesis video stream.

     

    .. note::

       

      This operation is only available for the AWS SDK for Java. It is not supported in AWS SDKs for other languages.

       

     

    The following limits apply when using the ``GetMediaForFragmentList`` API:

     

     
    * A client can call ``GetMediaForFragmentList`` up to five times per second per stream.  
     
    * Kinesis Video Streams sends media data at a rate of up to 25 megabytes per second (or 200 megabits per second) during a ``GetMediaForFragmentList`` session.  
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetMediaForFragmentList>`_    


    **Request Syntax** 
    ::

      response = client.get_media_for_fragment_list(
          StreamName='string',
          Fragments=[
              'string',
          ]
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream from which to retrieve fragment media.

      

    
    :type Fragments: list
    :param Fragments: **[REQUIRED]** 

      A list of the numbers of fragments for which to retrieve media. You retrieve these values with  ListFragments .

      

    
      - *(string) --* 

      
  
    
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

          The payload that Kinesis Video Streams returns is a sequence of chunks from the specified stream. For information about the chunks, see `PutMedia <docs.aws.amazon.com/acuity/latest/dg/API_dataplane_PutMedia.html>`__ . The chunks that Kinesis Video Streams returns in the ``GetMediaForFragmentList`` call also include the following additional Matroska (MKV) tags: 

           

           
          * AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk. 
           
          * AWS_KINESISVIDEO_SERVER_SIDE_TIMESTAMP - Server-side time stamp of the fragment. 
           
          * AWS_KINESISVIDEO_PRODUCER_SIDE_TIMESTAMP - Producer-side time stamp of the fragment. 
           

           

          The following tags will be included if an exception occurs:

           

           
          * AWS_KINESISVIDEO_FRAGMENT_NUMBER - The number of the fragment that threw the exception 
           
          * AWS_KINESISVIDEO_EXCEPTION_ERROR_CODE - The integer code of the exception 
           
          * AWS_KINESISVIDEO_EXCEPTION_MESSAGE - A text description of the exception 
           

          
    

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

        


  .. py:method:: list_fragments(**kwargs)

    

    Returns a list of  Fragment objects from the specified stream and start location within the archived data.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/ListFragments>`_    


    **Request Syntax** 
    ::

      response = client.list_fragments(
          StreamName='string',
          MaxResults=123,
          NextToken='string',
          FragmentSelector={
              'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
              'TimestampRange': {
                  'StartTimestamp': datetime(2015, 1, 1),
                  'EndTimestamp': datetime(2015, 1, 1)
              }
          }
      )
    :type StreamName: string
    :param StreamName: **[REQUIRED]** 

      The name of the stream from which to retrieve a fragment list.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The total number of fragments to return. If the total number of fragments available is more than the value specified in ``max-results`` , then a  ListFragmentsOutput$NextToken is provided in the output that you can use to resume pagination.

      

    
    :type NextToken: string
    :param NextToken: 

      A token to specify where to start paginating. This is the  ListFragmentsOutput$NextToken from a previously truncated response.

      

    
    :type FragmentSelector: dict
    :param FragmentSelector: 

      Describes the time stamp range and time stamp origin for the range of fragments to return.

      

    
      - **FragmentSelectorType** *(string) --* **[REQUIRED]** 

        The origin of the time stamps to use (Server or Producer).

        

      
      - **TimestampRange** *(dict) --* **[REQUIRED]** 

        The range of time stamps to return.

        

      
        - **StartTimestamp** *(datetime) --* **[REQUIRED]** 

          The starting time stamp in the range of time stamps for which to return fragments.

          

        
        - **EndTimestamp** *(datetime) --* **[REQUIRED]** 

          The ending time stamp in the range of time stamps for which to return fragments.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Fragments': [
                {
                    'FragmentNumber': 'string',
                    'FragmentSizeInBytes': 123,
                    'ProducerTimestamp': datetime(2015, 1, 1),
                    'ServerTimestamp': datetime(2015, 1, 1),
                    'FragmentLengthInMilliseconds': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Fragments** *(list) --* 

          A list of fragment numbers that correspond to the time stamp range provided.

          
          

          - *(dict) --* 

            Represents a segment of video or other time-delimited data.

            
            

            - **FragmentNumber** *(string) --* 

              The index value of the fragment.

              
            

            - **FragmentSizeInBytes** *(integer) --* 

              The total fragment size, including information about the fragment and contained media data.

              
            

            - **ProducerTimestamp** *(datetime) --* 

              The time stamp from the producer corresponding to the fragment.

              
            

            - **ServerTimestamp** *(datetime) --* 

              The time stamp from the AWS server corresponding to the fragment.

              
            

            - **FragmentLengthInMilliseconds** *(integer) --* 

              The playback duration or other time value associated with the fragment.

              
        
      
        

        - **NextToken** *(string) --* 

          If the returned list is truncated, the operation returns this token to use to retrieve the next page of results. This value is ``null`` when there are no more results to return.

          
    

==========
Paginators
==========


The available paginators are:
