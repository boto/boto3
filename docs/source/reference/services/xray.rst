

****
XRay
****

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: XRay.Client

  A low-level client representing AWS X-Ray::

    
    import boto3
    
    client = boto3.client('xray')

  
  These are the available methods:
  
  *   :py:meth:`~XRay.Client.batch_get_traces`

  
  *   :py:meth:`~XRay.Client.can_paginate`

  
  *   :py:meth:`~XRay.Client.generate_presigned_url`

  
  *   :py:meth:`~XRay.Client.get_paginator`

  
  *   :py:meth:`~XRay.Client.get_service_graph`

  
  *   :py:meth:`~XRay.Client.get_trace_graph`

  
  *   :py:meth:`~XRay.Client.get_trace_summaries`

  
  *   :py:meth:`~XRay.Client.get_waiter`

  
  *   :py:meth:`~XRay.Client.put_telemetry_records`

  
  *   :py:meth:`~XRay.Client.put_trace_segments`

  

  .. py:method:: batch_get_traces(**kwargs)

    

    Retrieves a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request. Use ``GetTraceSummaries`` to get a list of trace IDs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/BatchGetTraces>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_traces(
          TraceIds=[
              'string',
          ],
          NextToken='string'
      )
    :type TraceIds: list
    :param TraceIds: **[REQUIRED]** 

      Specify the trace IDs of requests for which to retrieve segments.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      Pagination token. Not used.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Traces': [
                {
                    'Id': 'string',
                    'Duration': 123.0,
                    'Segments': [
                        {
                            'Id': 'string',
                            'Document': 'string'
                        },
                    ]
                },
            ],
            'UnprocessedTraceIds': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Traces** *(list) --* 

          Full traces for the specified requests.

          
          

          - *(dict) --* 

            A collection of segment documents with matching trace IDs.

            
            

            - **Id** *(string) --* 

              The unique identifier for the request that generated the trace's segments and subsegments.

              
            

            - **Duration** *(float) --* 

              The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.

              
            

            - **Segments** *(list) --* 

              Segment documents for the segments and subsegments that comprise the trace.

              
              

              - *(dict) --* 

                A segment from a trace that has been ingested by the X-Ray service. The segment can be compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment for a downstream service, generated from a subsegment sent by the service that called it.

                
                

                - **Id** *(string) --* 

                  The segment's ID.

                  
                

                - **Document** *(string) --* 

                  The segment document

                  
            
          
        
      
        

        - **UnprocessedTraceIds** *(list) --* 

          Trace IDs of requests that haven't been processed.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          Pagination token. Not used.

          
    

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


  .. py:method:: get_service_graph(**kwargs)

    

    Retrieves a document that describes services that process incoming requests, and downstream services that they call as a result. Root services process incoming requests and make calls to downstream services. Root services are applications that use the AWS X-Ray SDK. Downstream services can be other applications, AWS resources, HTTP web APIs, or SQL databases.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetServiceGraph>`_    


    **Request Syntax** 
    ::

      response = client.get_service_graph(
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          NextToken='string'
      )
    :type StartTime: datetime
    :param StartTime: **[REQUIRED]** 

      The start of the time frame for which to generate a graph.

      

    
    :type EndTime: datetime
    :param EndTime: **[REQUIRED]** 

      The end of the time frame for which to generate a graph.

      

    
    :type NextToken: string
    :param NextToken: 

      Pagination token. Not used.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'Services': [
                {
                    'ReferenceId': 123,
                    'Name': 'string',
                    'Names': [
                        'string',
                    ],
                    'Root': True|False,
                    'AccountId': 'string',
                    'Type': 'string',
                    'State': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'Edges': [
                        {
                            'ReferenceId': 123,
                            'StartTime': datetime(2015, 1, 1),
                            'EndTime': datetime(2015, 1, 1),
                            'SummaryStatistics': {
                                'OkCount': 123,
                                'ErrorStatistics': {
                                    'ThrottleCount': 123,
                                    'OtherCount': 123,
                                    'TotalCount': 123
                                },
                                'FaultStatistics': {
                                    'OtherCount': 123,
                                    'TotalCount': 123
                                },
                                'TotalCount': 123,
                                'TotalResponseTime': 123.0
                            },
                            'ResponseTimeHistogram': [
                                {
                                    'Value': 123.0,
                                    'Count': 123
                                },
                            ],
                            'Aliases': [
                                {
                                    'Name': 'string',
                                    'Names': [
                                        'string',
                                    ],
                                    'Type': 'string'
                                },
                            ]
                        },
                    ],
                    'SummaryStatistics': {
                        'OkCount': 123,
                        'ErrorStatistics': {
                            'ThrottleCount': 123,
                            'OtherCount': 123,
                            'TotalCount': 123
                        },
                        'FaultStatistics': {
                            'OtherCount': 123,
                            'TotalCount': 123
                        },
                        'TotalCount': 123,
                        'TotalResponseTime': 123.0
                    },
                    'DurationHistogram': [
                        {
                            'Value': 123.0,
                            'Count': 123
                        },
                    ],
                    'ResponseTimeHistogram': [
                        {
                            'Value': 123.0,
                            'Count': 123
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StartTime** *(datetime) --* 

          The start of the time frame for which the graph was generated.

          
        

        - **EndTime** *(datetime) --* 

          The end of the time frame for which the graph was generated.

          
        

        - **Services** *(list) --* 

          The services that have processed a traced request during the specified time frame.

          
          

          - *(dict) --* 

            Information about an application that processed requests, users that made requests, or downstream services, resources and applications that an application used.

            
            

            - **ReferenceId** *(integer) --* 

              Identifier for the service. Unique within the service map.

              
            

            - **Name** *(string) --* 

              The canonical name of the service.

              
            

            - **Names** *(list) --* 

              A list of names for the service, including the canonical name.

              
              

              - *(string) --* 
          
            

            - **Root** *(boolean) --* 

              Indicates that the service was the first service to process a request.

              
            

            - **AccountId** *(string) --* 

              Identifier of the AWS account in which the service runs.

              
            

            - **Type** *(string) --* 

              The type of service.

               

               
              * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB table that the application used. 
               
              * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream calls to Amazon DynamoDB that didn't target a specific table. 
               
              * ``client`` - Represents the clients that sent requests to a root service. 
               
              * ``remote`` - A downstream service of indeterminate type. 
               

              
            

            - **State** *(string) --* 

              The service's state.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the first segment that the service generated.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the last segment that the service generated.

              
            

            - **Edges** *(list) --* 

              Connections to downstream services.

              
              

              - *(dict) --* 

                Information about a connection between two services.

                
                

                - **ReferenceId** *(integer) --* 

                  Identifier of the edge. Unique within a service map.

                  
                

                - **StartTime** *(datetime) --* 

                  The start time of the first segment on the edge.

                  
                

                - **EndTime** *(datetime) --* 

                  The end time of the last segment on the edge.

                  
                

                - **SummaryStatistics** *(dict) --* 

                  Response statistics for segments on the edge.

                  
                  

                  - **OkCount** *(integer) --* 

                    The number of requests that completed with a 2xx Success status code.

                    
                  

                  - **ErrorStatistics** *(dict) --* 

                    Information about requests that failed with a 4xx Client Error status code.

                    
                    

                    - **ThrottleCount** *(integer) --* 

                      The number of requests that failed with a 419 throttling status code.

                      
                    

                    - **OtherCount** *(integer) --* 

                      The number of requests that failed with untracked 4xx Client Error status codes.

                      
                    

                    - **TotalCount** *(integer) --* 

                      The total number of requests that failed with a 4xx Client Error status code.

                      
                
                  

                  - **FaultStatistics** *(dict) --* 

                    Information about requests that failed with a 5xx Server Error status code.

                    
                    

                    - **OtherCount** *(integer) --* 

                      The number of requests that failed with untracked 5xx Server Error status codes.

                      
                    

                    - **TotalCount** *(integer) --* 

                      The total number of requests that failed with a 5xx Server Error status code.

                      
                
                  

                  - **TotalCount** *(integer) --* 

                    The total number of completed requests.

                    
                  

                  - **TotalResponseTime** *(float) --* 

                    The aggregate response time of completed requests.

                    
              
                

                - **ResponseTimeHistogram** *(list) --* 

                  A histogram that maps the spread of client response times on an edge.

                  
                  

                  - *(dict) --* 

                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                    
                    

                    - **Value** *(float) --* 

                      The value of the entry.

                      
                    

                    - **Count** *(integer) --* 

                      The prevalence of the entry.

                      
                
              
                

                - **Aliases** *(list) --* 

                  Aliases for the edge.

                  
                  

                  - *(dict) --* 

                    An alias for an edge.

                    
                    

                    - **Name** *(string) --* 

                      The canonical name of the alias.

                      
                    

                    - **Names** *(list) --* 

                      A list of names for the alias, including the canonical name.

                      
                      

                      - *(string) --* 
                  
                    

                    - **Type** *(string) --* 

                      The type of the alias.

                      
                
              
            
          
            

            - **SummaryStatistics** *(dict) --* 

              Aggregated statistics for the service.

              
              

              - **OkCount** *(integer) --* 

                The number of requests that completed with a 2xx Success status code.

                
              

              - **ErrorStatistics** *(dict) --* 

                Information about requests that failed with a 4xx Client Error status code.

                
                

                - **ThrottleCount** *(integer) --* 

                  The number of requests that failed with a 419 throttling status code.

                  
                

                - **OtherCount** *(integer) --* 

                  The number of requests that failed with untracked 4xx Client Error status codes.

                  
                

                - **TotalCount** *(integer) --* 

                  The total number of requests that failed with a 4xx Client Error status code.

                  
            
              

              - **FaultStatistics** *(dict) --* 

                Information about requests that failed with a 5xx Server Error status code.

                
                

                - **OtherCount** *(integer) --* 

                  The number of requests that failed with untracked 5xx Server Error status codes.

                  
                

                - **TotalCount** *(integer) --* 

                  The total number of requests that failed with a 5xx Server Error status code.

                  
            
              

              - **TotalCount** *(integer) --* 

                The total number of completed requests.

                
              

              - **TotalResponseTime** *(float) --* 

                The aggregate response time of completed requests.

                
          
            

            - **DurationHistogram** *(list) --* 

              A histogram that maps the spread of service durations.

              
              

              - *(dict) --* 

                An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                
                

                - **Value** *(float) --* 

                  The value of the entry.

                  
                

                - **Count** *(integer) --* 

                  The prevalence of the entry.

                  
            
          
            

            - **ResponseTimeHistogram** *(list) --* 

              A histogram that maps the spread of service response times.

              
              

              - *(dict) --* 

                An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                
                

                - **Value** *(float) --* 

                  The value of the entry.

                  
                

                - **Count** *(integer) --* 

                  The prevalence of the entry.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          Pagination token. Not used.

          
    

  .. py:method:: get_trace_graph(**kwargs)

    

    Retrieves a service graph for one or more specific trace IDs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceGraph>`_    


    **Request Syntax** 
    ::

      response = client.get_trace_graph(
          TraceIds=[
              'string',
          ],
          NextToken='string'
      )
    :type TraceIds: list
    :param TraceIds: **[REQUIRED]** 

      Trace IDs of requests for which to generate a service graph.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      Pagination token. Not used.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Services': [
                {
                    'ReferenceId': 123,
                    'Name': 'string',
                    'Names': [
                        'string',
                    ],
                    'Root': True|False,
                    'AccountId': 'string',
                    'Type': 'string',
                    'State': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'Edges': [
                        {
                            'ReferenceId': 123,
                            'StartTime': datetime(2015, 1, 1),
                            'EndTime': datetime(2015, 1, 1),
                            'SummaryStatistics': {
                                'OkCount': 123,
                                'ErrorStatistics': {
                                    'ThrottleCount': 123,
                                    'OtherCount': 123,
                                    'TotalCount': 123
                                },
                                'FaultStatistics': {
                                    'OtherCount': 123,
                                    'TotalCount': 123
                                },
                                'TotalCount': 123,
                                'TotalResponseTime': 123.0
                            },
                            'ResponseTimeHistogram': [
                                {
                                    'Value': 123.0,
                                    'Count': 123
                                },
                            ],
                            'Aliases': [
                                {
                                    'Name': 'string',
                                    'Names': [
                                        'string',
                                    ],
                                    'Type': 'string'
                                },
                            ]
                        },
                    ],
                    'SummaryStatistics': {
                        'OkCount': 123,
                        'ErrorStatistics': {
                            'ThrottleCount': 123,
                            'OtherCount': 123,
                            'TotalCount': 123
                        },
                        'FaultStatistics': {
                            'OtherCount': 123,
                            'TotalCount': 123
                        },
                        'TotalCount': 123,
                        'TotalResponseTime': 123.0
                    },
                    'DurationHistogram': [
                        {
                            'Value': 123.0,
                            'Count': 123
                        },
                    ],
                    'ResponseTimeHistogram': [
                        {
                            'Value': 123.0,
                            'Count': 123
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Services** *(list) --* 

          The services that have processed one of the specified requests.

          
          

          - *(dict) --* 

            Information about an application that processed requests, users that made requests, or downstream services, resources and applications that an application used.

            
            

            - **ReferenceId** *(integer) --* 

              Identifier for the service. Unique within the service map.

              
            

            - **Name** *(string) --* 

              The canonical name of the service.

              
            

            - **Names** *(list) --* 

              A list of names for the service, including the canonical name.

              
              

              - *(string) --* 
          
            

            - **Root** *(boolean) --* 

              Indicates that the service was the first service to process a request.

              
            

            - **AccountId** *(string) --* 

              Identifier of the AWS account in which the service runs.

              
            

            - **Type** *(string) --* 

              The type of service.

               

               
              * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB table that the application used. 
               
              * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream calls to Amazon DynamoDB that didn't target a specific table. 
               
              * ``client`` - Represents the clients that sent requests to a root service. 
               
              * ``remote`` - A downstream service of indeterminate type. 
               

              
            

            - **State** *(string) --* 

              The service's state.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the first segment that the service generated.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the last segment that the service generated.

              
            

            - **Edges** *(list) --* 

              Connections to downstream services.

              
              

              - *(dict) --* 

                Information about a connection between two services.

                
                

                - **ReferenceId** *(integer) --* 

                  Identifier of the edge. Unique within a service map.

                  
                

                - **StartTime** *(datetime) --* 

                  The start time of the first segment on the edge.

                  
                

                - **EndTime** *(datetime) --* 

                  The end time of the last segment on the edge.

                  
                

                - **SummaryStatistics** *(dict) --* 

                  Response statistics for segments on the edge.

                  
                  

                  - **OkCount** *(integer) --* 

                    The number of requests that completed with a 2xx Success status code.

                    
                  

                  - **ErrorStatistics** *(dict) --* 

                    Information about requests that failed with a 4xx Client Error status code.

                    
                    

                    - **ThrottleCount** *(integer) --* 

                      The number of requests that failed with a 419 throttling status code.

                      
                    

                    - **OtherCount** *(integer) --* 

                      The number of requests that failed with untracked 4xx Client Error status codes.

                      
                    

                    - **TotalCount** *(integer) --* 

                      The total number of requests that failed with a 4xx Client Error status code.

                      
                
                  

                  - **FaultStatistics** *(dict) --* 

                    Information about requests that failed with a 5xx Server Error status code.

                    
                    

                    - **OtherCount** *(integer) --* 

                      The number of requests that failed with untracked 5xx Server Error status codes.

                      
                    

                    - **TotalCount** *(integer) --* 

                      The total number of requests that failed with a 5xx Server Error status code.

                      
                
                  

                  - **TotalCount** *(integer) --* 

                    The total number of completed requests.

                    
                  

                  - **TotalResponseTime** *(float) --* 

                    The aggregate response time of completed requests.

                    
              
                

                - **ResponseTimeHistogram** *(list) --* 

                  A histogram that maps the spread of client response times on an edge.

                  
                  

                  - *(dict) --* 

                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                    
                    

                    - **Value** *(float) --* 

                      The value of the entry.

                      
                    

                    - **Count** *(integer) --* 

                      The prevalence of the entry.

                      
                
              
                

                - **Aliases** *(list) --* 

                  Aliases for the edge.

                  
                  

                  - *(dict) --* 

                    An alias for an edge.

                    
                    

                    - **Name** *(string) --* 

                      The canonical name of the alias.

                      
                    

                    - **Names** *(list) --* 

                      A list of names for the alias, including the canonical name.

                      
                      

                      - *(string) --* 
                  
                    

                    - **Type** *(string) --* 

                      The type of the alias.

                      
                
              
            
          
            

            - **SummaryStatistics** *(dict) --* 

              Aggregated statistics for the service.

              
              

              - **OkCount** *(integer) --* 

                The number of requests that completed with a 2xx Success status code.

                
              

              - **ErrorStatistics** *(dict) --* 

                Information about requests that failed with a 4xx Client Error status code.

                
                

                - **ThrottleCount** *(integer) --* 

                  The number of requests that failed with a 419 throttling status code.

                  
                

                - **OtherCount** *(integer) --* 

                  The number of requests that failed with untracked 4xx Client Error status codes.

                  
                

                - **TotalCount** *(integer) --* 

                  The total number of requests that failed with a 4xx Client Error status code.

                  
            
              

              - **FaultStatistics** *(dict) --* 

                Information about requests that failed with a 5xx Server Error status code.

                
                

                - **OtherCount** *(integer) --* 

                  The number of requests that failed with untracked 5xx Server Error status codes.

                  
                

                - **TotalCount** *(integer) --* 

                  The total number of requests that failed with a 5xx Server Error status code.

                  
            
              

              - **TotalCount** *(integer) --* 

                The total number of completed requests.

                
              

              - **TotalResponseTime** *(float) --* 

                The aggregate response time of completed requests.

                
          
            

            - **DurationHistogram** *(list) --* 

              A histogram that maps the spread of service durations.

              
              

              - *(dict) --* 

                An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                
                

                - **Value** *(float) --* 

                  The value of the entry.

                  
                

                - **Count** *(integer) --* 

                  The prevalence of the entry.

                  
            
          
            

            - **ResponseTimeHistogram** *(list) --* 

              A histogram that maps the spread of service response times.

              
              

              - *(dict) --* 

                An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                
                

                - **Value** *(float) --* 

                  The value of the entry.

                  
                

                - **Count** *(integer) --* 

                  The prevalence of the entry.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          Pagination token. Not used.

          
    

  .. py:method:: get_trace_summaries(**kwargs)

    

    Retrieves IDs and metadata for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to ``BatchGetTraces`` .

     

    A filter expression can target traced requests that hit specific service nodes or edges, have errors, or come from a known user. For example, the following filter expression targets traces that pass through ``api.example.com`` :

     

     ``service("api.example.com")``  

     

    This filter expression finds traces that have an annotation named ``account`` with the value ``12345`` :

     

     ``annotation.account = "12345"``  

     

    For a full list of indexed fields and keywords that you can use in filter expressions, see `Using Filter Expressions <http://docs.aws.amazon.com/xray/latest/devguide/xray-console-filters.html>`__ in the *AWS X-Ray Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceSummaries>`_    


    **Request Syntax** 
    ::

      response = client.get_trace_summaries(
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          Sampling=True|False,
          FilterExpression='string',
          NextToken='string'
      )
    :type StartTime: datetime
    :param StartTime: **[REQUIRED]** 

      The start of the time frame for which to retrieve traces.

      

    
    :type EndTime: datetime
    :param EndTime: **[REQUIRED]** 

      The end of the time frame for which to retrieve traces.

      

    
    :type Sampling: boolean
    :param Sampling: 

      Set to ``true`` to get summaries for only a subset of available traces.

      

    
    :type FilterExpression: string
    :param FilterExpression: 

      Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.

      

    
    :type NextToken: string
    :param NextToken: 

      Specify the pagination token returned by a previous request to retrieve the next page of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TraceSummaries': [
                {
                    'Id': 'string',
                    'Duration': 123.0,
                    'ResponseTime': 123.0,
                    'HasFault': True|False,
                    'HasError': True|False,
                    'HasThrottle': True|False,
                    'IsPartial': True|False,
                    'Http': {
                        'HttpURL': 'string',
                        'HttpStatus': 123,
                        'HttpMethod': 'string',
                        'UserAgent': 'string',
                        'ClientIp': 'string'
                    },
                    'Annotations': {
                        'string': [
                            {
                                'AnnotationValue': {
                                    'NumberValue': 123.0,
                                    'BooleanValue': True|False,
                                    'StringValue': 'string'
                                },
                                'ServiceIds': [
                                    {
                                        'Name': 'string',
                                        'Names': [
                                            'string',
                                        ],
                                        'AccountId': 'string',
                                        'Type': 'string'
                                    },
                                ]
                            },
                        ]
                    },
                    'Users': [
                        {
                            'UserName': 'string',
                            'ServiceIds': [
                                {
                                    'Name': 'string',
                                    'Names': [
                                        'string',
                                    ],
                                    'AccountId': 'string',
                                    'Type': 'string'
                                },
                            ]
                        },
                    ],
                    'ServiceIds': [
                        {
                            'Name': 'string',
                            'Names': [
                                'string',
                            ],
                            'AccountId': 'string',
                            'Type': 'string'
                        },
                    ]
                },
            ],
            'ApproximateTime': datetime(2015, 1, 1),
            'TracesProcessedCount': 123,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TraceSummaries** *(list) --* 

          Trace IDs and metadata for traces that were found in the specified time frame.

          
          

          - *(dict) --* 

            Metadata generated from the segment documents in a trace.

            
            

            - **Id** *(string) --* 

              The unique identifier for the request that generated the trace's segments and subsegments.

              
            

            - **Duration** *(float) --* 

              The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.

              
            

            - **ResponseTime** *(float) --* 

              The length of time in seconds between the start and end times of the root segment. If the service performs work asynchronously, the response time measures the time before the response is sent to the user, while the duration measures the amount of time before the last traced activity completes.

              
            

            - **HasFault** *(boolean) --* 

              One or more of the segment documents has a 500 series error.

              
            

            - **HasError** *(boolean) --* 

              One or more of the segment documents has a 400 series error.

              
            

            - **HasThrottle** *(boolean) --* 

              One or more of the segment documents has a 429 throttling error.

              
            

            - **IsPartial** *(boolean) --* 

              One or more of the segment documents is in progress.

              
            

            - **Http** *(dict) --* 

              Information about the HTTP request served by the trace.

              
              

              - **HttpURL** *(string) --* 

                The request URL.

                
              

              - **HttpStatus** *(integer) --* 

                The response status.

                
              

              - **HttpMethod** *(string) --* 

                The request method.

                
              

              - **UserAgent** *(string) --* 

                The request's user agent string.

                
              

              - **ClientIp** *(string) --* 

                The IP address of the requestor.

                
          
            

            - **Annotations** *(dict) --* 

              Annotations from the trace's segment documents.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(dict) --* 

                    Information about a segment annotation.

                    
                    

                    - **AnnotationValue** *(dict) --* 

                      Values of the annotation.

                      
                      

                      - **NumberValue** *(float) --* 

                        Value for a Number annotation.

                        
                      

                      - **BooleanValue** *(boolean) --* 

                        Value for a Boolean annotation.

                        
                      

                      - **StringValue** *(string) --* 

                        Value for a String annotation.

                        
                  
                    

                    - **ServiceIds** *(list) --* 

                      Services to which the annotation applies.

                      
                      

                      - *(dict) --* 

                        

                        
                        

                        - **Name** *(string) --* 

                          

                          
                        

                        - **Names** *(list) --* 

                          

                          
                          

                          - *(string) --* 
                      
                        

                        - **AccountId** *(string) --* 

                          

                          
                        

                        - **Type** *(string) --* 

                          

                          
                    
                  
                
              
          
        
            

            - **Users** *(list) --* 

              Users from the trace's segment documents.

              
              

              - *(dict) --* 

                Information about a user recorded in segment documents.

                
                

                - **UserName** *(string) --* 

                  The user's name.

                  
                

                - **ServiceIds** *(list) --* 

                  Services that the user's request hit.

                  
                  

                  - *(dict) --* 

                    

                    
                    

                    - **Name** *(string) --* 

                      

                      
                    

                    - **Names** *(list) --* 

                      

                      
                      

                      - *(string) --* 
                  
                    

                    - **AccountId** *(string) --* 

                      

                      
                    

                    - **Type** *(string) --* 

                      

                      
                
              
            
          
            

            - **ServiceIds** *(list) --* 

              Service IDs from the trace's segment documents.

              
              

              - *(dict) --* 

                

                
                

                - **Name** *(string) --* 

                  

                  
                

                - **Names** *(list) --* 

                  

                  
                  

                  - *(string) --* 
              
                

                - **AccountId** *(string) --* 

                  

                  
                

                - **Type** *(string) --* 

                  

                  
            
          
        
      
        

        - **ApproximateTime** *(datetime) --* 

          The start time of this page of results.

          
        

        - **TracesProcessedCount** *(integer) --* 

          The number of traces that were processed to get this set of summaries.

          
        

        - **NextToken** *(string) --* 

          If the requested time frame contained more than one page of results, you can use this token to retrieve the next page. The first page contains the most most recent results, closest to the end of the time frame.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: put_telemetry_records(**kwargs)

    

    Used by the AWS X-Ray daemon to upload telemetry.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/PutTelemetryRecords>`_    


    **Request Syntax** 
    ::

      response = client.put_telemetry_records(
          TelemetryRecords=[
              {
                  'Timestamp': datetime(2015, 1, 1),
                  'SegmentsReceivedCount': 123,
                  'SegmentsSentCount': 123,
                  'SegmentsSpilloverCount': 123,
                  'SegmentsRejectedCount': 123,
                  'BackendConnectionErrors': {
                      'TimeoutCount': 123,
                      'ConnectionRefusedCount': 123,
                      'HTTPCode4XXCount': 123,
                      'HTTPCode5XXCount': 123,
                      'UnknownHostCount': 123,
                      'OtherCount': 123
                  }
              },
          ],
          EC2InstanceId='string',
          Hostname='string',
          ResourceARN='string'
      )
    :type TelemetryRecords: list
    :param TelemetryRecords: **[REQUIRED]** 

      

      

    
      - *(dict) --* 

        

        

      
        - **Timestamp** *(datetime) --* **[REQUIRED]** 

          

          

        
        - **SegmentsReceivedCount** *(integer) --* 

          

          

        
        - **SegmentsSentCount** *(integer) --* 

          

          

        
        - **SegmentsSpilloverCount** *(integer) --* 

          

          

        
        - **SegmentsRejectedCount** *(integer) --* 

          

          

        
        - **BackendConnectionErrors** *(dict) --* 

          

          

        
          - **TimeoutCount** *(integer) --* 

            

            

          
          - **ConnectionRefusedCount** *(integer) --* 

            

            

          
          - **HTTPCode4XXCount** *(integer) --* 

            

            

          
          - **HTTPCode5XXCount** *(integer) --* 

            

            

          
          - **UnknownHostCount** *(integer) --* 

            

            

          
          - **OtherCount** *(integer) --* 

            

            

          
        
      
  
    :type EC2InstanceId: string
    :param EC2InstanceId: 

      

      

    
    :type Hostname: string
    :param Hostname: 

      

      

    
    :type ResourceARN: string
    :param ResourceARN: 

      

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: put_trace_segments(**kwargs)

    

    Uploads segment documents to AWS X-Ray. The X-Ray SDK generates segment documents and sends them to the X-Ray daemon, which uploads them in batches. A segment document can be a completed segment, an in-progress segment, or an array of subsegments.

     

    Segments must include the following fields. For the full segment document schema, see `AWS X-Ray Segment Documents <http://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in the *AWS X-Ray Developer Guide* .

     

     **Required Segment Document Fields**  

     

     
    * ``name`` - The name of the service that handled the request. 
     
    * ``id`` - A 64-bit identifier for the segment, unique among segments in the same trace, in 16 hexadecimal digits. 
     
    * ``trace_id`` - A unique identifier that connects all segments and subsegments originating from a single client request. 
     
    * ``start_time`` - Time the segment or subsegment was created, in floating point seconds in epoch time, accurate to milliseconds. For example, ``1480615200.010`` or ``1.480615200010E9`` . 
     
    * ``end_time`` - Time the segment or subsegment was closed. For example, ``1480615200.090`` or ``1.480615200090E9`` . Specify either an ``end_time`` or ``in_progress`` . 
     
    * ``in_progress`` - Set to ``true`` instead of specifying an ``end_time`` to record that a segment has been started, but is not complete. Send an in progress segment when your application receives a request that will take a long time to serve, to trace the fact that the request was received. When the response is sent, send the complete segment to overwrite the in-progress segment. 
     

     

    A ``trace_id`` consists of three numbers separated by hyphens. For example, 1-58406520-a006649127e371903a2de979. This includes:

     

     **Trace ID Format**  

     

     
    * The version number, i.e. ``1`` . 
     
    * The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is ``1480615200`` seconds, or ``58406520`` in hexadecimal. 
     
    * A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/PutTraceSegments>`_    


    **Request Syntax** 
    ::

      response = client.put_trace_segments(
          TraceSegmentDocuments=[
              'string',
          ]
      )
    :type TraceSegmentDocuments: list
    :param TraceSegmentDocuments: **[REQUIRED]** 

      A string containing a JSON document defining one or more segments or subsegments.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedTraceSegments': [
                {
                    'Id': 'string',
                    'ErrorCode': 'string',
                    'Message': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UnprocessedTraceSegments** *(list) --* 

          Segments that failed processing.

          
          

          - *(dict) --* 

            Information about a segment that failed processing.

            
            

            - **Id** *(string) --* 

              The segment's ID.

              
            

            - **ErrorCode** *(string) --* 

              The error that caused processing to fail.

              
            

            - **Message** *(string) --* 

              The error message.

              
        
      
    

==========
Paginators
==========


The available paginators are:

* :py:class:`XRay.Paginator.BatchGetTraces`


* :py:class:`XRay.Paginator.GetServiceGraph`


* :py:class:`XRay.Paginator.GetTraceGraph`


* :py:class:`XRay.Paginator.GetTraceSummaries`



.. py:class:: XRay.Paginator.BatchGetTraces

  ::

    
    paginator = client.get_paginator('batch_get_traces')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.batch_get_traces`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/BatchGetTraces>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          TraceIds=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type TraceIds: list
    :param TraceIds: **[REQUIRED]** 

      Specify the trace IDs of requests for which to retrieve segments.

      

    
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
            'Traces': [
                {
                    'Id': 'string',
                    'Duration': 123.0,
                    'Segments': [
                        {
                            'Id': 'string',
                            'Document': 'string'
                        },
                    ]
                },
            ],
            'UnprocessedTraceIds': [
                'string',
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Traces** *(list) --* 

          Full traces for the specified requests.

          
          

          - *(dict) --* 

            A collection of segment documents with matching trace IDs.

            
            

            - **Id** *(string) --* 

              The unique identifier for the request that generated the trace's segments and subsegments.

              
            

            - **Duration** *(float) --* 

              The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.

              
            

            - **Segments** *(list) --* 

              Segment documents for the segments and subsegments that comprise the trace.

              
              

              - *(dict) --* 

                A segment from a trace that has been ingested by the X-Ray service. The segment can be compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment for a downstream service, generated from a subsegment sent by the service that called it.

                
                

                - **Id** *(string) --* 

                  The segment's ID.

                  
                

                - **Document** *(string) --* 

                  The segment document

                  
            
          
        
      
        

        - **UnprocessedTraceIds** *(list) --* 

          Trace IDs of requests that haven't been processed.

          
          

          - *(string) --* 
      
    

.. py:class:: XRay.Paginator.GetServiceGraph

  ::

    
    paginator = client.get_paginator('get_service_graph')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_service_graph`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetServiceGraph>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type StartTime: datetime
    :param StartTime: **[REQUIRED]** 

      The start of the time frame for which to generate a graph.

      

    
    :type EndTime: datetime
    :param EndTime: **[REQUIRED]** 

      The end of the time frame for which to generate a graph.

      

    
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
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'Services': [
                {
                    'ReferenceId': 123,
                    'Name': 'string',
                    'Names': [
                        'string',
                    ],
                    'Root': True|False,
                    'AccountId': 'string',
                    'Type': 'string',
                    'State': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'Edges': [
                        {
                            'ReferenceId': 123,
                            'StartTime': datetime(2015, 1, 1),
                            'EndTime': datetime(2015, 1, 1),
                            'SummaryStatistics': {
                                'OkCount': 123,
                                'ErrorStatistics': {
                                    'ThrottleCount': 123,
                                    'OtherCount': 123,
                                    'TotalCount': 123
                                },
                                'FaultStatistics': {
                                    'OtherCount': 123,
                                    'TotalCount': 123
                                },
                                'TotalCount': 123,
                                'TotalResponseTime': 123.0
                            },
                            'ResponseTimeHistogram': [
                                {
                                    'Value': 123.0,
                                    'Count': 123
                                },
                            ],
                            'Aliases': [
                                {
                                    'Name': 'string',
                                    'Names': [
                                        'string',
                                    ],
                                    'Type': 'string'
                                },
                            ]
                        },
                    ],
                    'SummaryStatistics': {
                        'OkCount': 123,
                        'ErrorStatistics': {
                            'ThrottleCount': 123,
                            'OtherCount': 123,
                            'TotalCount': 123
                        },
                        'FaultStatistics': {
                            'OtherCount': 123,
                            'TotalCount': 123
                        },
                        'TotalCount': 123,
                        'TotalResponseTime': 123.0
                    },
                    'DurationHistogram': [
                        {
                            'Value': 123.0,
                            'Count': 123
                        },
                    ],
                    'ResponseTimeHistogram': [
                        {
                            'Value': 123.0,
                            'Count': 123
                        },
                    ]
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StartTime** *(datetime) --* 

          The start of the time frame for which the graph was generated.

          
        

        - **EndTime** *(datetime) --* 

          The end of the time frame for which the graph was generated.

          
        

        - **Services** *(list) --* 

          The services that have processed a traced request during the specified time frame.

          
          

          - *(dict) --* 

            Information about an application that processed requests, users that made requests, or downstream services, resources and applications that an application used.

            
            

            - **ReferenceId** *(integer) --* 

              Identifier for the service. Unique within the service map.

              
            

            - **Name** *(string) --* 

              The canonical name of the service.

              
            

            - **Names** *(list) --* 

              A list of names for the service, including the canonical name.

              
              

              - *(string) --* 
          
            

            - **Root** *(boolean) --* 

              Indicates that the service was the first service to process a request.

              
            

            - **AccountId** *(string) --* 

              Identifier of the AWS account in which the service runs.

              
            

            - **Type** *(string) --* 

              The type of service.

               

               
              * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB table that the application used. 
               
              * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream calls to Amazon DynamoDB that didn't target a specific table. 
               
              * ``client`` - Represents the clients that sent requests to a root service. 
               
              * ``remote`` - A downstream service of indeterminate type. 
               

              
            

            - **State** *(string) --* 

              The service's state.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the first segment that the service generated.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the last segment that the service generated.

              
            

            - **Edges** *(list) --* 

              Connections to downstream services.

              
              

              - *(dict) --* 

                Information about a connection between two services.

                
                

                - **ReferenceId** *(integer) --* 

                  Identifier of the edge. Unique within a service map.

                  
                

                - **StartTime** *(datetime) --* 

                  The start time of the first segment on the edge.

                  
                

                - **EndTime** *(datetime) --* 

                  The end time of the last segment on the edge.

                  
                

                - **SummaryStatistics** *(dict) --* 

                  Response statistics for segments on the edge.

                  
                  

                  - **OkCount** *(integer) --* 

                    The number of requests that completed with a 2xx Success status code.

                    
                  

                  - **ErrorStatistics** *(dict) --* 

                    Information about requests that failed with a 4xx Client Error status code.

                    
                    

                    - **ThrottleCount** *(integer) --* 

                      The number of requests that failed with a 419 throttling status code.

                      
                    

                    - **OtherCount** *(integer) --* 

                      The number of requests that failed with untracked 4xx Client Error status codes.

                      
                    

                    - **TotalCount** *(integer) --* 

                      The total number of requests that failed with a 4xx Client Error status code.

                      
                
                  

                  - **FaultStatistics** *(dict) --* 

                    Information about requests that failed with a 5xx Server Error status code.

                    
                    

                    - **OtherCount** *(integer) --* 

                      The number of requests that failed with untracked 5xx Server Error status codes.

                      
                    

                    - **TotalCount** *(integer) --* 

                      The total number of requests that failed with a 5xx Server Error status code.

                      
                
                  

                  - **TotalCount** *(integer) --* 

                    The total number of completed requests.

                    
                  

                  - **TotalResponseTime** *(float) --* 

                    The aggregate response time of completed requests.

                    
              
                

                - **ResponseTimeHistogram** *(list) --* 

                  A histogram that maps the spread of client response times on an edge.

                  
                  

                  - *(dict) --* 

                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                    
                    

                    - **Value** *(float) --* 

                      The value of the entry.

                      
                    

                    - **Count** *(integer) --* 

                      The prevalence of the entry.

                      
                
              
                

                - **Aliases** *(list) --* 

                  Aliases for the edge.

                  
                  

                  - *(dict) --* 

                    An alias for an edge.

                    
                    

                    - **Name** *(string) --* 

                      The canonical name of the alias.

                      
                    

                    - **Names** *(list) --* 

                      A list of names for the alias, including the canonical name.

                      
                      

                      - *(string) --* 
                  
                    

                    - **Type** *(string) --* 

                      The type of the alias.

                      
                
              
            
          
            

            - **SummaryStatistics** *(dict) --* 

              Aggregated statistics for the service.

              
              

              - **OkCount** *(integer) --* 

                The number of requests that completed with a 2xx Success status code.

                
              

              - **ErrorStatistics** *(dict) --* 

                Information about requests that failed with a 4xx Client Error status code.

                
                

                - **ThrottleCount** *(integer) --* 

                  The number of requests that failed with a 419 throttling status code.

                  
                

                - **OtherCount** *(integer) --* 

                  The number of requests that failed with untracked 4xx Client Error status codes.

                  
                

                - **TotalCount** *(integer) --* 

                  The total number of requests that failed with a 4xx Client Error status code.

                  
            
              

              - **FaultStatistics** *(dict) --* 

                Information about requests that failed with a 5xx Server Error status code.

                
                

                - **OtherCount** *(integer) --* 

                  The number of requests that failed with untracked 5xx Server Error status codes.

                  
                

                - **TotalCount** *(integer) --* 

                  The total number of requests that failed with a 5xx Server Error status code.

                  
            
              

              - **TotalCount** *(integer) --* 

                The total number of completed requests.

                
              

              - **TotalResponseTime** *(float) --* 

                The aggregate response time of completed requests.

                
          
            

            - **DurationHistogram** *(list) --* 

              A histogram that maps the spread of service durations.

              
              

              - *(dict) --* 

                An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                
                

                - **Value** *(float) --* 

                  The value of the entry.

                  
                

                - **Count** *(integer) --* 

                  The prevalence of the entry.

                  
            
          
            

            - **ResponseTimeHistogram** *(list) --* 

              A histogram that maps the spread of service response times.

              
              

              - *(dict) --* 

                An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                
                

                - **Value** *(float) --* 

                  The value of the entry.

                  
                

                - **Count** *(integer) --* 

                  The prevalence of the entry.

                  
            
          
        
      
    

.. py:class:: XRay.Paginator.GetTraceGraph

  ::

    
    paginator = client.get_paginator('get_trace_graph')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_trace_graph`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceGraph>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          TraceIds=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type TraceIds: list
    :param TraceIds: **[REQUIRED]** 

      Trace IDs of requests for which to generate a service graph.

      

    
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
            'Services': [
                {
                    'ReferenceId': 123,
                    'Name': 'string',
                    'Names': [
                        'string',
                    ],
                    'Root': True|False,
                    'AccountId': 'string',
                    'Type': 'string',
                    'State': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'Edges': [
                        {
                            'ReferenceId': 123,
                            'StartTime': datetime(2015, 1, 1),
                            'EndTime': datetime(2015, 1, 1),
                            'SummaryStatistics': {
                                'OkCount': 123,
                                'ErrorStatistics': {
                                    'ThrottleCount': 123,
                                    'OtherCount': 123,
                                    'TotalCount': 123
                                },
                                'FaultStatistics': {
                                    'OtherCount': 123,
                                    'TotalCount': 123
                                },
                                'TotalCount': 123,
                                'TotalResponseTime': 123.0
                            },
                            'ResponseTimeHistogram': [
                                {
                                    'Value': 123.0,
                                    'Count': 123
                                },
                            ],
                            'Aliases': [
                                {
                                    'Name': 'string',
                                    'Names': [
                                        'string',
                                    ],
                                    'Type': 'string'
                                },
                            ]
                        },
                    ],
                    'SummaryStatistics': {
                        'OkCount': 123,
                        'ErrorStatistics': {
                            'ThrottleCount': 123,
                            'OtherCount': 123,
                            'TotalCount': 123
                        },
                        'FaultStatistics': {
                            'OtherCount': 123,
                            'TotalCount': 123
                        },
                        'TotalCount': 123,
                        'TotalResponseTime': 123.0
                    },
                    'DurationHistogram': [
                        {
                            'Value': 123.0,
                            'Count': 123
                        },
                    ],
                    'ResponseTimeHistogram': [
                        {
                            'Value': 123.0,
                            'Count': 123
                        },
                    ]
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Services** *(list) --* 

          The services that have processed one of the specified requests.

          
          

          - *(dict) --* 

            Information about an application that processed requests, users that made requests, or downstream services, resources and applications that an application used.

            
            

            - **ReferenceId** *(integer) --* 

              Identifier for the service. Unique within the service map.

              
            

            - **Name** *(string) --* 

              The canonical name of the service.

              
            

            - **Names** *(list) --* 

              A list of names for the service, including the canonical name.

              
              

              - *(string) --* 
          
            

            - **Root** *(boolean) --* 

              Indicates that the service was the first service to process a request.

              
            

            - **AccountId** *(string) --* 

              Identifier of the AWS account in which the service runs.

              
            

            - **Type** *(string) --* 

              The type of service.

               

               
              * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB table that the application used. 
               
              * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream calls to Amazon DynamoDB that didn't target a specific table. 
               
              * ``client`` - Represents the clients that sent requests to a root service. 
               
              * ``remote`` - A downstream service of indeterminate type. 
               

              
            

            - **State** *(string) --* 

              The service's state.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the first segment that the service generated.

              
            

            - **EndTime** *(datetime) --* 

              The end time of the last segment that the service generated.

              
            

            - **Edges** *(list) --* 

              Connections to downstream services.

              
              

              - *(dict) --* 

                Information about a connection between two services.

                
                

                - **ReferenceId** *(integer) --* 

                  Identifier of the edge. Unique within a service map.

                  
                

                - **StartTime** *(datetime) --* 

                  The start time of the first segment on the edge.

                  
                

                - **EndTime** *(datetime) --* 

                  The end time of the last segment on the edge.

                  
                

                - **SummaryStatistics** *(dict) --* 

                  Response statistics for segments on the edge.

                  
                  

                  - **OkCount** *(integer) --* 

                    The number of requests that completed with a 2xx Success status code.

                    
                  

                  - **ErrorStatistics** *(dict) --* 

                    Information about requests that failed with a 4xx Client Error status code.

                    
                    

                    - **ThrottleCount** *(integer) --* 

                      The number of requests that failed with a 419 throttling status code.

                      
                    

                    - **OtherCount** *(integer) --* 

                      The number of requests that failed with untracked 4xx Client Error status codes.

                      
                    

                    - **TotalCount** *(integer) --* 

                      The total number of requests that failed with a 4xx Client Error status code.

                      
                
                  

                  - **FaultStatistics** *(dict) --* 

                    Information about requests that failed with a 5xx Server Error status code.

                    
                    

                    - **OtherCount** *(integer) --* 

                      The number of requests that failed with untracked 5xx Server Error status codes.

                      
                    

                    - **TotalCount** *(integer) --* 

                      The total number of requests that failed with a 5xx Server Error status code.

                      
                
                  

                  - **TotalCount** *(integer) --* 

                    The total number of completed requests.

                    
                  

                  - **TotalResponseTime** *(float) --* 

                    The aggregate response time of completed requests.

                    
              
                

                - **ResponseTimeHistogram** *(list) --* 

                  A histogram that maps the spread of client response times on an edge.

                  
                  

                  - *(dict) --* 

                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                    
                    

                    - **Value** *(float) --* 

                      The value of the entry.

                      
                    

                    - **Count** *(integer) --* 

                      The prevalence of the entry.

                      
                
              
                

                - **Aliases** *(list) --* 

                  Aliases for the edge.

                  
                  

                  - *(dict) --* 

                    An alias for an edge.

                    
                    

                    - **Name** *(string) --* 

                      The canonical name of the alias.

                      
                    

                    - **Names** *(list) --* 

                      A list of names for the alias, including the canonical name.

                      
                      

                      - *(string) --* 
                  
                    

                    - **Type** *(string) --* 

                      The type of the alias.

                      
                
              
            
          
            

            - **SummaryStatistics** *(dict) --* 

              Aggregated statistics for the service.

              
              

              - **OkCount** *(integer) --* 

                The number of requests that completed with a 2xx Success status code.

                
              

              - **ErrorStatistics** *(dict) --* 

                Information about requests that failed with a 4xx Client Error status code.

                
                

                - **ThrottleCount** *(integer) --* 

                  The number of requests that failed with a 419 throttling status code.

                  
                

                - **OtherCount** *(integer) --* 

                  The number of requests that failed with untracked 4xx Client Error status codes.

                  
                

                - **TotalCount** *(integer) --* 

                  The total number of requests that failed with a 4xx Client Error status code.

                  
            
              

              - **FaultStatistics** *(dict) --* 

                Information about requests that failed with a 5xx Server Error status code.

                
                

                - **OtherCount** *(integer) --* 

                  The number of requests that failed with untracked 5xx Server Error status codes.

                  
                

                - **TotalCount** *(integer) --* 

                  The total number of requests that failed with a 5xx Server Error status code.

                  
            
              

              - **TotalCount** *(integer) --* 

                The total number of completed requests.

                
              

              - **TotalResponseTime** *(float) --* 

                The aggregate response time of completed requests.

                
          
            

            - **DurationHistogram** *(list) --* 

              A histogram that maps the spread of service durations.

              
              

              - *(dict) --* 

                An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                
                

                - **Value** *(float) --* 

                  The value of the entry.

                  
                

                - **Count** *(integer) --* 

                  The prevalence of the entry.

                  
            
          
            

            - **ResponseTimeHistogram** *(list) --* 

              A histogram that maps the spread of service response times.

              
              

              - *(dict) --* 

                An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

                
                

                - **Value** *(float) --* 

                  The value of the entry.

                  
                

                - **Count** *(integer) --* 

                  The prevalence of the entry.

                  
            
          
        
      
    

.. py:class:: XRay.Paginator.GetTraceSummaries

  ::

    
    paginator = client.get_paginator('get_trace_summaries')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_trace_summaries`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceSummaries>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          Sampling=True|False,
          FilterExpression='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type StartTime: datetime
    :param StartTime: **[REQUIRED]** 

      The start of the time frame for which to retrieve traces.

      

    
    :type EndTime: datetime
    :param EndTime: **[REQUIRED]** 

      The end of the time frame for which to retrieve traces.

      

    
    :type Sampling: boolean
    :param Sampling: 

      Set to ``true`` to get summaries for only a subset of available traces.

      

    
    :type FilterExpression: string
    :param FilterExpression: 

      Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.

      

    
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
            'TraceSummaries': [
                {
                    'Id': 'string',
                    'Duration': 123.0,
                    'ResponseTime': 123.0,
                    'HasFault': True|False,
                    'HasError': True|False,
                    'HasThrottle': True|False,
                    'IsPartial': True|False,
                    'Http': {
                        'HttpURL': 'string',
                        'HttpStatus': 123,
                        'HttpMethod': 'string',
                        'UserAgent': 'string',
                        'ClientIp': 'string'
                    },
                    'Annotations': {
                        'string': [
                            {
                                'AnnotationValue': {
                                    'NumberValue': 123.0,
                                    'BooleanValue': True|False,
                                    'StringValue': 'string'
                                },
                                'ServiceIds': [
                                    {
                                        'Name': 'string',
                                        'Names': [
                                            'string',
                                        ],
                                        'AccountId': 'string',
                                        'Type': 'string'
                                    },
                                ]
                            },
                        ]
                    },
                    'Users': [
                        {
                            'UserName': 'string',
                            'ServiceIds': [
                                {
                                    'Name': 'string',
                                    'Names': [
                                        'string',
                                    ],
                                    'AccountId': 'string',
                                    'Type': 'string'
                                },
                            ]
                        },
                    ],
                    'ServiceIds': [
                        {
                            'Name': 'string',
                            'Names': [
                                'string',
                            ],
                            'AccountId': 'string',
                            'Type': 'string'
                        },
                    ]
                },
            ],
            'ApproximateTime': datetime(2015, 1, 1),
            'TracesProcessedCount': 123,
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TraceSummaries** *(list) --* 

          Trace IDs and metadata for traces that were found in the specified time frame.

          
          

          - *(dict) --* 

            Metadata generated from the segment documents in a trace.

            
            

            - **Id** *(string) --* 

              The unique identifier for the request that generated the trace's segments and subsegments.

              
            

            - **Duration** *(float) --* 

              The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.

              
            

            - **ResponseTime** *(float) --* 

              The length of time in seconds between the start and end times of the root segment. If the service performs work asynchronously, the response time measures the time before the response is sent to the user, while the duration measures the amount of time before the last traced activity completes.

              
            

            - **HasFault** *(boolean) --* 

              One or more of the segment documents has a 500 series error.

              
            

            - **HasError** *(boolean) --* 

              One or more of the segment documents has a 400 series error.

              
            

            - **HasThrottle** *(boolean) --* 

              One or more of the segment documents has a 429 throttling error.

              
            

            - **IsPartial** *(boolean) --* 

              One or more of the segment documents is in progress.

              
            

            - **Http** *(dict) --* 

              Information about the HTTP request served by the trace.

              
              

              - **HttpURL** *(string) --* 

                The request URL.

                
              

              - **HttpStatus** *(integer) --* 

                The response status.

                
              

              - **HttpMethod** *(string) --* 

                The request method.

                
              

              - **UserAgent** *(string) --* 

                The request's user agent string.

                
              

              - **ClientIp** *(string) --* 

                The IP address of the requestor.

                
          
            

            - **Annotations** *(dict) --* 

              Annotations from the trace's segment documents.

              
              

              - *(string) --* 
                

                - *(list) --* 
                  

                  - *(dict) --* 

                    Information about a segment annotation.

                    
                    

                    - **AnnotationValue** *(dict) --* 

                      Values of the annotation.

                      
                      

                      - **NumberValue** *(float) --* 

                        Value for a Number annotation.

                        
                      

                      - **BooleanValue** *(boolean) --* 

                        Value for a Boolean annotation.

                        
                      

                      - **StringValue** *(string) --* 

                        Value for a String annotation.

                        
                  
                    

                    - **ServiceIds** *(list) --* 

                      Services to which the annotation applies.

                      
                      

                      - *(dict) --* 

                        

                        
                        

                        - **Name** *(string) --* 

                          

                          
                        

                        - **Names** *(list) --* 

                          

                          
                          

                          - *(string) --* 
                      
                        

                        - **AccountId** *(string) --* 

                          

                          
                        

                        - **Type** *(string) --* 

                          

                          
                    
                  
                
              
          
        
            

            - **Users** *(list) --* 

              Users from the trace's segment documents.

              
              

              - *(dict) --* 

                Information about a user recorded in segment documents.

                
                

                - **UserName** *(string) --* 

                  The user's name.

                  
                

                - **ServiceIds** *(list) --* 

                  Services that the user's request hit.

                  
                  

                  - *(dict) --* 

                    

                    
                    

                    - **Name** *(string) --* 

                      

                      
                    

                    - **Names** *(list) --* 

                      

                      
                      

                      - *(string) --* 
                  
                    

                    - **AccountId** *(string) --* 

                      

                      
                    

                    - **Type** *(string) --* 

                      

                      
                
              
            
          
            

            - **ServiceIds** *(list) --* 

              Service IDs from the trace's segment documents.

              
              

              - *(dict) --* 

                

                
                

                - **Name** *(string) --* 

                  

                  
                

                - **Names** *(list) --* 

                  

                  
                  

                  - *(string) --* 
              
                

                - **AccountId** *(string) --* 

                  

                  
                

                - **Type** *(string) --* 

                  

                  
            
          
        
      
        

        - **ApproximateTime** *(datetime) --* 

          The start time of this page of results.

          
        

        - **TracesProcessedCount** *(integer) --* 

          The number of traces that were processed to get this set of summaries.

          
    