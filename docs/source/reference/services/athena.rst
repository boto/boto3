

******
Athena
******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Athena.Client

  A low-level client representing Amazon Athena::

    
    import boto3
    
    client = boto3.client('athena')

  
  These are the available methods:
  
  *   :py:meth:`~Athena.Client.batch_get_named_query`

  
  *   :py:meth:`~Athena.Client.batch_get_query_execution`

  
  *   :py:meth:`~Athena.Client.can_paginate`

  
  *   :py:meth:`~Athena.Client.create_named_query`

  
  *   :py:meth:`~Athena.Client.delete_named_query`

  
  *   :py:meth:`~Athena.Client.generate_presigned_url`

  
  *   :py:meth:`~Athena.Client.get_named_query`

  
  *   :py:meth:`~Athena.Client.get_paginator`

  
  *   :py:meth:`~Athena.Client.get_query_execution`

  
  *   :py:meth:`~Athena.Client.get_query_results`

  
  *   :py:meth:`~Athena.Client.get_waiter`

  
  *   :py:meth:`~Athena.Client.list_named_queries`

  
  *   :py:meth:`~Athena.Client.list_query_executions`

  
  *   :py:meth:`~Athena.Client.start_query_execution`

  
  *   :py:meth:`~Athena.Client.stop_query_execution`

  

  .. py:method:: batch_get_named_query(**kwargs)

    

    Returns the details of a single named query or a list of up to 50 queries, which you provide as an array of query ID strings. Use  ListNamedQueries to get the list of named query IDs. If information could not be retrieved for a submitted query ID, information about the query ID submitted is listed under  UnprocessedNamedQueryId . Named queries are different from executed queries. Use  BatchGetQueryExecution to get details about each unique query execution, and  ListQueryExecutions to get a list of query execution IDs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/BatchGetNamedQuery>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_named_query(
          NamedQueryIds=[
              'string',
          ]
      )
    :type NamedQueryIds: list
    :param NamedQueryIds: **[REQUIRED]** 

      An array of query IDs.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NamedQueries': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'Database': 'string',
                    'QueryString': 'string',
                    'NamedQueryId': 'string'
                },
            ],
            'UnprocessedNamedQueryIds': [
                {
                    'NamedQueryId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NamedQueries** *(list) --* 

          Information about the named query IDs submitted.

          
          

          - *(dict) --* 

            A query, where ``QueryString`` is the SQL query statements that comprise the query.

            
            

            - **Name** *(string) --* 

              The plain-language name of the query.

              
            

            - **Description** *(string) --* 

              A brief description of the query.

              
            

            - **Database** *(string) --* 

              The database to which the query belongs.

              
            

            - **QueryString** *(string) --* 

              The SQL query statements that comprise the query.

              
            

            - **NamedQueryId** *(string) --* 

              The unique identifier of the query.

              
        
      
        

        - **UnprocessedNamedQueryIds** *(list) --* 

          Information about provided query IDs.

          
          

          - *(dict) --* 

            Information about a named query ID that could not be processed.

            
            

            - **NamedQueryId** *(string) --* 

              The unique identifier of the named query.

              
            

            - **ErrorCode** *(string) --* 

              The error code returned when the processing request for the named query failed, if applicable.

              
            

            - **ErrorMessage** *(string) --* 

              The error message returned when the processing request for the named query failed, if applicable.

              
        
      
    

  .. py:method:: batch_get_query_execution(**kwargs)

    

    Returns the details of a single query execution or a list of up to 50 query executions, which you provide as an array of query execution ID strings. To get a list of query execution IDs, use  ListQueryExecutions . Query executions are different from named (saved) queries. Use  BatchGetNamedQuery to get details about named queries.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/BatchGetQueryExecution>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_query_execution(
          QueryExecutionIds=[
              'string',
          ]
      )
    :type QueryExecutionIds: list
    :param QueryExecutionIds: **[REQUIRED]** 

      An array of query execution IDs.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'QueryExecutions': [
                {
                    'QueryExecutionId': 'string',
                    'Query': 'string',
                    'ResultConfiguration': {
                        'OutputLocation': 'string',
                        'EncryptionConfiguration': {
                            'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                            'KmsKey': 'string'
                        }
                    },
                    'QueryExecutionContext': {
                        'Database': 'string'
                    },
                    'Status': {
                        'State': 'QUEUED'|'RUNNING'|'SUCCEEDED'|'FAILED'|'CANCELLED',
                        'StateChangeReason': 'string',
                        'SubmissionDateTime': datetime(2015, 1, 1),
                        'CompletionDateTime': datetime(2015, 1, 1)
                    },
                    'Statistics': {
                        'EngineExecutionTimeInMillis': 123,
                        'DataScannedInBytes': 123
                    }
                },
            ],
            'UnprocessedQueryExecutionIds': [
                {
                    'QueryExecutionId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **QueryExecutions** *(list) --* 

          Information about a query execution.

          
          

          - *(dict) --* 

            Information about a single instance of a query execution.

            
            

            - **QueryExecutionId** *(string) --* 

              The unique identifier for each query execution.

              
            

            - **Query** *(string) --* 

              The SQL query statements which the query execution ran.

              
            

            - **ResultConfiguration** *(dict) --* 

              The location in Amazon S3 where query results were stored and the encryption option, if any, used for query results.

              
              

              - **OutputLocation** *(string) --* 

                The location in S3 where query results are stored.

                
              

              - **EncryptionConfiguration** *(dict) --* 

                If query results are encrypted in S3, indicates the S3 encryption option used (for example, ``SSE-KMS`` or ``CSE-KMS`` and key information.

                
                

                - **EncryptionOption** *(string) --* 

                  Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.

                  
                

                - **KmsKey** *(string) --* 

                  For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

                  
            
          
            

            - **QueryExecutionContext** *(dict) --* 

              The database in which the query execution occurred.

              
              

              - **Database** *(string) --* 

                The name of the database.

                
          
            

            - **Status** *(dict) --* 

              The completion date, current state, submission time, and state change reason (if applicable) for the query execution.

              
              

              - **State** *(string) --* 

                The state of query execution. ``SUBMITTED`` indicates that the query is queued for execution. ``RUNNING`` indicates that the query is scanning data and returning results. ``SUCCEEDED`` indicates that the query completed without error. ``FAILED`` indicates that the query experienced an error and did not complete processing. ``CANCELLED`` indicates that user input interrupted query execution.

                
              

              - **StateChangeReason** *(string) --* 

                Further detail about the status of the query.

                
              

              - **SubmissionDateTime** *(datetime) --* 

                The date and time that the query was submitted.

                
              

              - **CompletionDateTime** *(datetime) --* 

                The date and time that the query completed.

                
          
            

            - **Statistics** *(dict) --* 

              The amount of data scanned during the query execution and the amount of time that it took to execute.

              
              

              - **EngineExecutionTimeInMillis** *(integer) --* 

                The number of milliseconds that the query took to execute.

                
              

              - **DataScannedInBytes** *(integer) --* 

                The number of bytes in the data that was queried.

                
          
        
      
        

        - **UnprocessedQueryExecutionIds** *(list) --* 

          Information about the query executions that failed to run.

          
          

          - *(dict) --* 

            Describes a query execution that failed to process.

            
            

            - **QueryExecutionId** *(string) --* 

              The unique identifier of the query execution.

              
            

            - **ErrorCode** *(string) --* 

              The error code returned when the query execution failed to process, if applicable.

              
            

            - **ErrorMessage** *(string) --* 

              The error message returned when the query execution failed to process, if applicable.

              
        
      
    

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


  .. py:method:: create_named_query(**kwargs)

    

    Creates a named query.

     

    For code samples using the AWS SDK for Java, see `Examples and Code Samples <http://docs.aws.amazon.com/athena/latest/ug/code-samples.html>`__ in the *Amazon Athena User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/CreateNamedQuery>`_    


    **Request Syntax** 
    ::

      response = client.create_named_query(
          Name='string',
          Description='string',
          Database='string',
          QueryString='string',
          ClientRequestToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The plain language name for the query.

      

    
    :type Description: string
    :param Description: 

      A brief explanation of the query.

      

    
    :type Database: string
    :param Database: **[REQUIRED]** 

      The database to which the query belongs.

      

    
    :type QueryString: string
    :param QueryString: **[REQUIRED]** 

      The text of the query itself. In other words, all query statements.

      

    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another ``CreateNamedQuery`` request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the ``QueryString`` , an error is returned.

       

      .. warning::

         

        This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.

         

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NamedQueryId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NamedQueryId** *(string) --* 

          The unique ID of the query.

          
    

  .. py:method:: delete_named_query(**kwargs)

    

    Deletes a named query.

     

    For code samples using the AWS SDK for Java, see `Examples and Code Samples <http://docs.aws.amazon.com/athena/latest/ug/code-samples.html>`__ in the *Amazon Athena User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/DeleteNamedQuery>`_    


    **Request Syntax** 
    ::

      response = client.delete_named_query(
          NamedQueryId='string'
      )
    :type NamedQueryId: string
    :param NamedQueryId: **[REQUIRED]** 

      The unique ID of the query to delete.

      This field is autopopulated if not provided.

    
    
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


  .. py:method:: get_named_query(**kwargs)

    

    Returns information about a single query.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/GetNamedQuery>`_    


    **Request Syntax** 
    ::

      response = client.get_named_query(
          NamedQueryId='string'
      )
    :type NamedQueryId: string
    :param NamedQueryId: **[REQUIRED]** 

      The unique ID of the query. Use  ListNamedQueries to get query IDs.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NamedQuery': {
                'Name': 'string',
                'Description': 'string',
                'Database': 'string',
                'QueryString': 'string',
                'NamedQueryId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NamedQuery** *(dict) --* 

          Information about the query.

          
          

          - **Name** *(string) --* 

            The plain-language name of the query.

            
          

          - **Description** *(string) --* 

            A brief description of the query.

            
          

          - **Database** *(string) --* 

            The database to which the query belongs.

            
          

          - **QueryString** *(string) --* 

            The SQL query statements that comprise the query.

            
          

          - **NamedQueryId** *(string) --* 

            The unique identifier of the query.

            
      
    

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


  .. py:method:: get_query_execution(**kwargs)

    

    Returns information about a single execution of a query. Each time a query executes, information about the query execution is saved with a unique ID.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/GetQueryExecution>`_    


    **Request Syntax** 
    ::

      response = client.get_query_execution(
          QueryExecutionId='string'
      )
    :type QueryExecutionId: string
    :param QueryExecutionId: **[REQUIRED]** 

      The unique ID of the query execution.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'QueryExecution': {
                'QueryExecutionId': 'string',
                'Query': 'string',
                'ResultConfiguration': {
                    'OutputLocation': 'string',
                    'EncryptionConfiguration': {
                        'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                        'KmsKey': 'string'
                    }
                },
                'QueryExecutionContext': {
                    'Database': 'string'
                },
                'Status': {
                    'State': 'QUEUED'|'RUNNING'|'SUCCEEDED'|'FAILED'|'CANCELLED',
                    'StateChangeReason': 'string',
                    'SubmissionDateTime': datetime(2015, 1, 1),
                    'CompletionDateTime': datetime(2015, 1, 1)
                },
                'Statistics': {
                    'EngineExecutionTimeInMillis': 123,
                    'DataScannedInBytes': 123
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **QueryExecution** *(dict) --* 

          Information about the query execution.

          
          

          - **QueryExecutionId** *(string) --* 

            The unique identifier for each query execution.

            
          

          - **Query** *(string) --* 

            The SQL query statements which the query execution ran.

            
          

          - **ResultConfiguration** *(dict) --* 

            The location in Amazon S3 where query results were stored and the encryption option, if any, used for query results.

            
            

            - **OutputLocation** *(string) --* 

              The location in S3 where query results are stored.

              
            

            - **EncryptionConfiguration** *(dict) --* 

              If query results are encrypted in S3, indicates the S3 encryption option used (for example, ``SSE-KMS`` or ``CSE-KMS`` and key information.

              
              

              - **EncryptionOption** *(string) --* 

                Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.

                
              

              - **KmsKey** *(string) --* 

                For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

                
          
        
          

          - **QueryExecutionContext** *(dict) --* 

            The database in which the query execution occurred.

            
            

            - **Database** *(string) --* 

              The name of the database.

              
        
          

          - **Status** *(dict) --* 

            The completion date, current state, submission time, and state change reason (if applicable) for the query execution.

            
            

            - **State** *(string) --* 

              The state of query execution. ``SUBMITTED`` indicates that the query is queued for execution. ``RUNNING`` indicates that the query is scanning data and returning results. ``SUCCEEDED`` indicates that the query completed without error. ``FAILED`` indicates that the query experienced an error and did not complete processing. ``CANCELLED`` indicates that user input interrupted query execution.

              
            

            - **StateChangeReason** *(string) --* 

              Further detail about the status of the query.

              
            

            - **SubmissionDateTime** *(datetime) --* 

              The date and time that the query was submitted.

              
            

            - **CompletionDateTime** *(datetime) --* 

              The date and time that the query completed.

              
        
          

          - **Statistics** *(dict) --* 

            The amount of data scanned during the query execution and the amount of time that it took to execute.

            
            

            - **EngineExecutionTimeInMillis** *(integer) --* 

              The number of milliseconds that the query took to execute.

              
            

            - **DataScannedInBytes** *(integer) --* 

              The number of bytes in the data that was queried.

              
        
      
    

  .. py:method:: get_query_results(**kwargs)

    

    Returns the results of a single query execution specified by ``QueryExecutionId`` . This request does not execute the query but returns results. Use  StartQueryExecution to run a query.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/GetQueryResults>`_    


    **Request Syntax** 
    ::

      response = client.get_query_results(
          QueryExecutionId='string',
          NextToken='string',
          MaxResults=123
      )
    :type QueryExecutionId: string
    :param QueryExecutionId: **[REQUIRED]** 

      The unique ID of the query execution.

      

    
    :type NextToken: string
    :param NextToken: 

      The token that specifies where to start pagination if a previous request was truncated.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results (rows) to return in this request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResultSet': {
                'Rows': [
                    {
                        'Data': [
                            {
                                'VarCharValue': 'string'
                            },
                        ]
                    },
                ],
                'ResultSetMetadata': {
                    'ColumnInfo': [
                        {
                            'CatalogName': 'string',
                            'SchemaName': 'string',
                            'TableName': 'string',
                            'Name': 'string',
                            'Label': 'string',
                            'Type': 'string',
                            'Precision': 123,
                            'Scale': 123,
                            'Nullable': 'NOT_NULL'|'NULLABLE'|'UNKNOWN',
                            'CaseSensitive': True|False
                        },
                    ]
                }
            },
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResultSet** *(dict) --* 

          The results of the query execution.

          
          

          - **Rows** *(list) --* 

            The rows in the table.

            
            

            - *(dict) --* 

              The rows that comprise a query result table.

              
              

              - **Data** *(list) --* 

                The data that populates a row in a query result table.

                
                

                - *(dict) --* 

                  A piece of data (a field in the table).

                  
                  

                  - **VarCharValue** *(string) --* 

                    The value of the datum.

                    
              
            
          
        
          

          - **ResultSetMetadata** *(dict) --* 

            The metadata that describes the column structure and data types of a table of query results.

            
            

            - **ColumnInfo** *(list) --* 

              Information about the columns in a query execution result.

              
              

              - *(dict) --* 

                Information about the columns in a query execution result.

                
                

                - **CatalogName** *(string) --* 

                  The catalog to which the query results belong.

                  
                

                - **SchemaName** *(string) --* 

                  The schema name (database name) to which the query results belong.

                  
                

                - **TableName** *(string) --* 

                  The table name for the query results.

                  
                

                - **Name** *(string) --* 

                  The name of the column.

                  
                

                - **Label** *(string) --* 

                  A column label.

                  
                

                - **Type** *(string) --* 

                  The data type of the column.

                  
                

                - **Precision** *(integer) --* 

                  For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For performance reasons, we recommend up to 18 digits.

                  
                

                - **Scale** *(integer) --* 

                  For ``DECIMAL`` data types, specifies the total number of digits in the fractional part of the value. Defaults to 0.

                  
                

                - **Nullable** *(string) --* 

                  Indicates the column's nullable status.

                  
                

                - **CaseSensitive** *(boolean) --* 

                  Indicates whether values in the column are case-sensitive.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to be used by the next request if this request is truncated.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_named_queries(**kwargs)

    

    Provides a list of all available query IDs.

     

    For code samples using the AWS SDK for Java, see `Examples and Code Samples <http://docs.aws.amazon.com/athena/latest/ug/code-samples.html>`__ in the *Amazon Athena User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/ListNamedQueries>`_    


    **Request Syntax** 
    ::

      response = client.list_named_queries(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      The token that specifies where to start pagination if a previous request was truncated.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of queries to return in this request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NamedQueryIds': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NamedQueryIds** *(list) --* 

          The list of unique query IDs.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to be used by the next request if this request is truncated.

          
    

  .. py:method:: list_query_executions(**kwargs)

    

    Provides a list of all available query execution IDs.

     

    For code samples using the AWS SDK for Java, see `Examples and Code Samples <http://docs.aws.amazon.com/athena/latest/ug/code-samples.html>`__ in the *Amazon Athena User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/ListQueryExecutions>`_    


    **Request Syntax** 
    ::

      response = client.list_query_executions(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      The token that specifies where to start pagination if a previous request was truncated.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of query executions to return in this request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'QueryExecutionIds': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **QueryExecutionIds** *(list) --* 

          The unique IDs of each query execution as an array of strings.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to be used by the next request if this request is truncated.

          
    

  .. py:method:: start_query_execution(**kwargs)

    

    Runs (executes) the SQL query statements contained in the ``Query`` string.

     

    For code samples using the AWS SDK for Java, see `Examples and Code Samples <http://docs.aws.amazon.com/athena/latest/ug/code-samples.html>`__ in the *Amazon Athena User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/StartQueryExecution>`_    


    **Request Syntax** 
    ::

      response = client.start_query_execution(
          QueryString='string',
          ClientRequestToken='string',
          QueryExecutionContext={
              'Database': 'string'
          },
          ResultConfiguration={
              'OutputLocation': 'string',
              'EncryptionConfiguration': {
                  'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                  'KmsKey': 'string'
              }
          }
      )
    :type QueryString: string
    :param QueryString: **[REQUIRED]** 

      The SQL query statements to be executed.

      

    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another ``StartQueryExecution`` request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the ``QueryString`` , an error is returned.

       

      .. warning::

         

        This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.

         

      This field is autopopulated if not provided.

    
    :type QueryExecutionContext: dict
    :param QueryExecutionContext: 

      The database within which the query executes.

      

    
      - **Database** *(string) --* 

        The name of the database.

        

      
    
    :type ResultConfiguration: dict
    :param ResultConfiguration: **[REQUIRED]** 

      Specifies information about where and how to save the results of the query execution.

      

    
      - **OutputLocation** *(string) --* **[REQUIRED]** 

        The location in S3 where query results are stored.

        

      
      - **EncryptionConfiguration** *(dict) --* 

        If query results are encrypted in S3, indicates the S3 encryption option used (for example, ``SSE-KMS`` or ``CSE-KMS`` and key information.

        

      
        - **EncryptionOption** *(string) --* **[REQUIRED]** 

          Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.

          

        
        - **KmsKey** *(string) --* 

          For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'QueryExecutionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **QueryExecutionId** *(string) --* 

          The unique ID of the query that ran as a result of this request.

          
    

  .. py:method:: stop_query_execution(**kwargs)

    

    Stops a query execution.

     

    For code samples using the AWS SDK for Java, see `Examples and Code Samples <http://docs.aws.amazon.com/athena/latest/ug/code-samples.html>`__ in the *Amazon Athena User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/StopQueryExecution>`_    


    **Request Syntax** 
    ::

      response = client.stop_query_execution(
          QueryExecutionId='string'
      )
    :type QueryExecutionId: string
    :param QueryExecutionId: **[REQUIRED]** 

      The unique ID of the query execution to stop.

      This field is autopopulated if not provided.

    
    
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

* :py:class:`Athena.Paginator.GetQueryResults`


* :py:class:`Athena.Paginator.ListNamedQueries`


* :py:class:`Athena.Paginator.ListQueryExecutions`



.. py:class:: Athena.Paginator.GetQueryResults

  ::

    
    paginator = client.get_paginator('get_query_results')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Athena.Client.get_query_results`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/GetQueryResults>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          QueryExecutionId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type QueryExecutionId: string
    :param QueryExecutionId: **[REQUIRED]** 

      The unique ID of the query execution.

      

    
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
            'ResultSet': {
                'Rows': [
                    {
                        'Data': [
                            {
                                'VarCharValue': 'string'
                            },
                        ]
                    },
                ],
                'ResultSetMetadata': {
                    'ColumnInfo': [
                        {
                            'CatalogName': 'string',
                            'SchemaName': 'string',
                            'TableName': 'string',
                            'Name': 'string',
                            'Label': 'string',
                            'Type': 'string',
                            'Precision': 123,
                            'Scale': 123,
                            'Nullable': 'NOT_NULL'|'NULLABLE'|'UNKNOWN',
                            'CaseSensitive': True|False
                        },
                    ]
                }
            },
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResultSet** *(dict) --* 

          The results of the query execution.

          
          

          - **Rows** *(list) --* 

            The rows in the table.

            
            

            - *(dict) --* 

              The rows that comprise a query result table.

              
              

              - **Data** *(list) --* 

                The data that populates a row in a query result table.

                
                

                - *(dict) --* 

                  A piece of data (a field in the table).

                  
                  

                  - **VarCharValue** *(string) --* 

                    The value of the datum.

                    
              
            
          
        
          

          - **ResultSetMetadata** *(dict) --* 

            The metadata that describes the column structure and data types of a table of query results.

            
            

            - **ColumnInfo** *(list) --* 

              Information about the columns in a query execution result.

              
              

              - *(dict) --* 

                Information about the columns in a query execution result.

                
                

                - **CatalogName** *(string) --* 

                  The catalog to which the query results belong.

                  
                

                - **SchemaName** *(string) --* 

                  The schema name (database name) to which the query results belong.

                  
                

                - **TableName** *(string) --* 

                  The table name for the query results.

                  
                

                - **Name** *(string) --* 

                  The name of the column.

                  
                

                - **Label** *(string) --* 

                  A column label.

                  
                

                - **Type** *(string) --* 

                  The data type of the column.

                  
                

                - **Precision** *(integer) --* 

                  For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For performance reasons, we recommend up to 18 digits.

                  
                

                - **Scale** *(integer) --* 

                  For ``DECIMAL`` data types, specifies the total number of digits in the fractional part of the value. Defaults to 0.

                  
                

                - **Nullable** *(string) --* 

                  Indicates the column's nullable status.

                  
                

                - **CaseSensitive** *(boolean) --* 

                  Indicates whether values in the column are case-sensitive.

                  
            
          
        
      
    

.. py:class:: Athena.Paginator.ListNamedQueries

  ::

    
    paginator = client.get_paginator('list_named_queries')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Athena.Client.list_named_queries`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/ListNamedQueries>`_    


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
            'NamedQueryIds': [
                'string',
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NamedQueryIds** *(list) --* 

          The list of unique query IDs.

          
          

          - *(string) --* 
      
    

.. py:class:: Athena.Paginator.ListQueryExecutions

  ::

    
    paginator = client.get_paginator('list_query_executions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Athena.Client.list_query_executions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/ListQueryExecutions>`_    


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
            'QueryExecutionIds': [
                'string',
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **QueryExecutionIds** *(list) --* 

          The unique IDs of each query execution as an array of strings.

          
          

          - *(string) --* 
      
    