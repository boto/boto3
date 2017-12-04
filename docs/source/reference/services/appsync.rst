

*******
AppSync
*******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: AppSync.Client

  A low-level client representing AWS AppSync::

    
    import boto3
    
    client = boto3.client('appsync')

  
  These are the available methods:
  
  *   :py:meth:`~AppSync.Client.can_paginate`

  
  *   :py:meth:`~AppSync.Client.create_api_key`

  
  *   :py:meth:`~AppSync.Client.create_data_source`

  
  *   :py:meth:`~AppSync.Client.create_graphql_api`

  
  *   :py:meth:`~AppSync.Client.create_resolver`

  
  *   :py:meth:`~AppSync.Client.create_type`

  
  *   :py:meth:`~AppSync.Client.delete_api_key`

  
  *   :py:meth:`~AppSync.Client.delete_data_source`

  
  *   :py:meth:`~AppSync.Client.delete_graphql_api`

  
  *   :py:meth:`~AppSync.Client.delete_resolver`

  
  *   :py:meth:`~AppSync.Client.delete_type`

  
  *   :py:meth:`~AppSync.Client.generate_presigned_url`

  
  *   :py:meth:`~AppSync.Client.get_data_source`

  
  *   :py:meth:`~AppSync.Client.get_graphql_api`

  
  *   :py:meth:`~AppSync.Client.get_introspection_schema`

  
  *   :py:meth:`~AppSync.Client.get_paginator`

  
  *   :py:meth:`~AppSync.Client.get_resolver`

  
  *   :py:meth:`~AppSync.Client.get_schema_creation_status`

  
  *   :py:meth:`~AppSync.Client.get_type`

  
  *   :py:meth:`~AppSync.Client.get_waiter`

  
  *   :py:meth:`~AppSync.Client.list_api_keys`

  
  *   :py:meth:`~AppSync.Client.list_data_sources`

  
  *   :py:meth:`~AppSync.Client.list_graphql_apis`

  
  *   :py:meth:`~AppSync.Client.list_resolvers`

  
  *   :py:meth:`~AppSync.Client.list_types`

  
  *   :py:meth:`~AppSync.Client.start_schema_creation`

  
  *   :py:meth:`~AppSync.Client.update_data_source`

  
  *   :py:meth:`~AppSync.Client.update_graphql_api`

  
  *   :py:meth:`~AppSync.Client.update_resolver`

  
  *   :py:meth:`~AppSync.Client.update_type`

  

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


  .. py:method:: create_api_key(**kwargs)

    

    Creates a unique key that you can distribute to clients who are executing your API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateApiKey>`_    


    **Request Syntax** 
    ::

      response = client.create_api_key(
          apiId='string',
          description='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The ID for your GraphQL API.

      

    
    :type description: string
    :param description: 

      A description of the purpose of the API key.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'apiKey': {
                'id': 'string',
                'description': 'string',
                'expires': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **apiKey** *(dict) --* 

          The API key.

          
          

          - **id** *(string) --* 

            The API key ID.

            
          

          - **description** *(string) --* 

            A description of the purpose of the API key.

            
          

          - **expires** *(integer) --* 

            The time when the API key expires.

            
      
    

  .. py:method:: create_data_source(**kwargs)

    

    Creates a ``DataSource`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateDataSource>`_    


    **Request Syntax** 
    ::

      response = client.create_data_source(
          apiId='string',
          name='string',
          description='string',
          type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH',
          serviceRoleArn='string',
          dynamodbConfig={
              'tableName': 'string',
              'awsRegion': 'string',
              'useCallerCredentials': True|False
          },
          lambdaConfig={
              'lambdaFunctionArn': 'string'
          },
          elasticsearchConfig={
              'endpoint': 'string',
              'awsRegion': 'string'
          }
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID for the GraphQL API for the ``DataSource`` .

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      A user-supplied name for the ``DataSource`` .

      

    
    :type description: string
    :param description: 

      A description of the ``DataSource`` .

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      The type of the ``DataSource`` .

      

    
    :type serviceRoleArn: string
    :param serviceRoleArn: 

      The IAM service role ARN for the data source. The system assumes this role when accessing the data source.

      

    
    :type dynamodbConfig: dict
    :param dynamodbConfig: 

      DynamoDB settings.

      

    
      - **tableName** *(string) --* **[REQUIRED]** 

        The table name.

        

      
      - **awsRegion** *(string) --* **[REQUIRED]** 

        The AWS region.

        

      
      - **useCallerCredentials** *(boolean) --* 

        Set to TRUE to use Amazon Cognito credentials with this data source.

        

      
    
    :type lambdaConfig: dict
    :param lambdaConfig: 

      AWS Lambda settings.

      

    
      - **lambdaFunctionArn** *(string) --* **[REQUIRED]** 

        The ARN for the Lambda function.

        

      
    
    :type elasticsearchConfig: dict
    :param elasticsearchConfig: 

      Amazon Elasticsearch settings.

      

    
      - **endpoint** *(string) --* **[REQUIRED]** 

        The endpoint.

        

      
      - **awsRegion** *(string) --* **[REQUIRED]** 

        The AWS region.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'dataSource': {
                'dataSourceArn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH',
                'serviceRoleArn': 'string',
                'dynamodbConfig': {
                    'tableName': 'string',
                    'awsRegion': 'string',
                    'useCallerCredentials': True|False
                },
                'lambdaConfig': {
                    'lambdaFunctionArn': 'string'
                },
                'elasticsearchConfig': {
                    'endpoint': 'string',
                    'awsRegion': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **dataSource** *(dict) --* 

          The ``DataSource`` object.

          
          

          - **dataSourceArn** *(string) --* 

            The data source ARN.

            
          

          - **name** *(string) --* 

            The name of the data source.

            
          

          - **description** *(string) --* 

            The description of the data source.

            
          

          - **type** *(string) --* 

            The type of the data source.

            
          

          - **serviceRoleArn** *(string) --* 

            The IAM service role ARN for the data source. The system assumes this role when accessing the data source.

            
          

          - **dynamodbConfig** *(dict) --* 

            DynamoDB settings.

            
            

            - **tableName** *(string) --* 

              The table name.

              
            

            - **awsRegion** *(string) --* 

              The AWS region.

              
            

            - **useCallerCredentials** *(boolean) --* 

              Set to TRUE to use Amazon Cognito credentials with this data source.

              
        
          

          - **lambdaConfig** *(dict) --* 

            Lambda settings.

            
            

            - **lambdaFunctionArn** *(string) --* 

              The ARN for the Lambda function.

              
        
          

          - **elasticsearchConfig** *(dict) --* 

            Amazon Elasticsearch settings.

            
            

            - **endpoint** *(string) --* 

              The endpoint.

              
            

            - **awsRegion** *(string) --* 

              The AWS region.

              
        
      
    

  .. py:method:: create_graphql_api(**kwargs)

    

    Creates a ``GraphqlApi`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateGraphqlApi>`_    


    **Request Syntax** 
    ::

      response = client.create_graphql_api(
          name='string',
          authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
          userPoolConfig={
              'userPoolId': 'string',
              'awsRegion': 'string',
              'defaultAction': 'ALLOW'|'DENY',
              'appIdClientRegex': 'string'
          }
      )
    :type name: string
    :param name: **[REQUIRED]** 

      A user-supplied name for the ``GraphqlApi`` .

      

    
    :type authenticationType: string
    :param authenticationType: **[REQUIRED]** 

      The authentication type: API key, IAM, or Amazon Cognito User Pools.

      

    
    :type userPoolConfig: dict
    :param userPoolConfig: 

      The Amazon Cognito User Pool configuration.

      

    
      - **userPoolId** *(string) --* **[REQUIRED]** 

        The user pool ID.

        

      
      - **awsRegion** *(string) --* **[REQUIRED]** 

        The AWS region in which the user pool was created.

        

      
      - **defaultAction** *(string) --* **[REQUIRED]** 

        The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration.

        

      
      - **appIdClientRegex** *(string) --* 

        A regular expression for validating the incoming Amazon Cognito User Pool app client ID.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'graphqlApi': {
                'name': 'string',
                'apiId': 'string',
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'defaultAction': 'ALLOW'|'DENY',
                    'appIdClientRegex': 'string'
                },
                'arn': 'string',
                'uris': {
                    'string': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **graphqlApi** *(dict) --* 

          The ``GraphqlApi`` .

          
          

          - **name** *(string) --* 

            The API name.

            
          

          - **apiId** *(string) --* 

            The API ID.

            
          

          - **authenticationType** *(string) --* 

            The authentication type.

            
          

          - **userPoolConfig** *(dict) --* 

            The Amazon Cognito User Pool configuration.

            
            

            - **userPoolId** *(string) --* 

              The user pool ID.

              
            

            - **awsRegion** *(string) --* 

              The AWS region in which the user pool was created.

              
            

            - **defaultAction** *(string) --* 

              The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration.

              
            

            - **appIdClientRegex** *(string) --* 

              A regular expression for validating the incoming Amazon Cognito User Pool app client ID.

              
        
          

          - **arn** *(string) --* 

            The ARN.

            
          

          - **uris** *(dict) --* 

            The URIs.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
    

  .. py:method:: create_resolver(**kwargs)

    

    Creates a ``Resolver`` object.

     

    A resolver converts incoming requests into a format that a data source can understand and converts the data source's responses into GraphQL.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateResolver>`_    


    **Request Syntax** 
    ::

      response = client.create_resolver(
          apiId='string',
          typeName='string',
          fieldName='string',
          dataSourceName='string',
          requestMappingTemplate='string',
          responseMappingTemplate='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The ID for the GraphQL API for which the resolver is being created.

      

    
    :type typeName: string
    :param typeName: **[REQUIRED]** 

      The name of the ``Type`` .

      

    
    :type fieldName: string
    :param fieldName: **[REQUIRED]** 

      The name of the field to attach the resolver to.

      

    
    :type dataSourceName: string
    :param dataSourceName: **[REQUIRED]** 

      The name of the data source for which the resolver is being created.

      

    
    :type requestMappingTemplate: string
    :param requestMappingTemplate: **[REQUIRED]** 

      The mapping template to be used for requests.

       

      A resolver use a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).

      

    
    :type responseMappingTemplate: string
    :param responseMappingTemplate: 

      The mapping template to be used for responses from the data source.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resolver': {
                'typeName': 'string',
                'fieldName': 'string',
                'dataSourceName': 'string',
                'resolverArn': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resolver** *(dict) --* 

          The ``Resolver`` object.

          
          

          - **typeName** *(string) --* 

            The resolver type name.

            
          

          - **fieldName** *(string) --* 

            The resolver field name.

            
          

          - **dataSourceName** *(string) --* 

            The resolver data source name.

            
          

          - **resolverArn** *(string) --* 

            The resolver ARN.

            
          

          - **requestMappingTemplate** *(string) --* 

            The request mapping template.

            
          

          - **responseMappingTemplate** *(string) --* 

            The response mapping template.

            
      
    

  .. py:method:: create_type(**kwargs)

    

    Creates a ``Type`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateType>`_    


    **Request Syntax** 
    ::

      response = client.create_type(
          apiId='string',
          definition='string',
          format='SDL'|'JSON'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type definition: string
    :param definition: **[REQUIRED]** 

      The type definition, in GraphQL Schema Definition Language (SDL) format.

       

      For more information, see the `GraphQL SDL documentation <http://graphql.org/learn/schema/>`__ .

      

    
    :type format: string
    :param format: **[REQUIRED]** 

      The type format: SDL or JSON.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'type': {
                'name': 'string',
                'description': 'string',
                'arn': 'string',
                'definition': 'string',
                'format': 'SDL'|'JSON'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **type** *(dict) --* 

          The ``Type`` object.

          
          

          - **name** *(string) --* 

            The type name.

            
          

          - **description** *(string) --* 

            The type description.

            
          

          - **arn** *(string) --* 

            The type ARN.

            
          

          - **definition** *(string) --* 

            The type definition.

            
          

          - **format** *(string) --* 

            The type format: SDL or JSON.

            
      
    

  .. py:method:: delete_api_key(**kwargs)

    

    Deletes an API key.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteApiKey>`_    


    **Request Syntax** 
    ::

      response = client.delete_api_key(
          apiId='string',
          id='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type id: string
    :param id: **[REQUIRED]** 

      The ID for the API key.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_data_source(**kwargs)

    

    Deletes a ``DataSource`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteDataSource>`_    


    **Request Syntax** 
    ::

      response = client.delete_data_source(
          apiId='string',
          name='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the data source.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_graphql_api(**kwargs)

    

    Deletes a ``GraphqlApi`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteGraphqlApi>`_    


    **Request Syntax** 
    ::

      response = client.delete_graphql_api(
          apiId='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_resolver(**kwargs)

    

    Deletes a ``Resolver`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteResolver>`_    


    **Request Syntax** 
    ::

      response = client.delete_resolver(
          apiId='string',
          typeName='string',
          fieldName='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type typeName: string
    :param typeName: **[REQUIRED]** 

      The name of the resolver type.

      

    
    :type fieldName: string
    :param fieldName: **[REQUIRED]** 

      The resolver field name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_type(**kwargs)

    

    Deletes a ``Type`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteType>`_    


    **Request Syntax** 
    ::

      response = client.delete_type(
          apiId='string',
          typeName='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type typeName: string
    :param typeName: **[REQUIRED]** 

      The type name.

      

    
    
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


  .. py:method:: get_data_source(**kwargs)

    

    Retrieves a ``DataSource`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetDataSource>`_    


    **Request Syntax** 
    ::

      response = client.get_data_source(
          apiId='string',
          name='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the data source.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'dataSource': {
                'dataSourceArn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH',
                'serviceRoleArn': 'string',
                'dynamodbConfig': {
                    'tableName': 'string',
                    'awsRegion': 'string',
                    'useCallerCredentials': True|False
                },
                'lambdaConfig': {
                    'lambdaFunctionArn': 'string'
                },
                'elasticsearchConfig': {
                    'endpoint': 'string',
                    'awsRegion': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **dataSource** *(dict) --* 

          The ``DataSource`` object.

          
          

          - **dataSourceArn** *(string) --* 

            The data source ARN.

            
          

          - **name** *(string) --* 

            The name of the data source.

            
          

          - **description** *(string) --* 

            The description of the data source.

            
          

          - **type** *(string) --* 

            The type of the data source.

            
          

          - **serviceRoleArn** *(string) --* 

            The IAM service role ARN for the data source. The system assumes this role when accessing the data source.

            
          

          - **dynamodbConfig** *(dict) --* 

            DynamoDB settings.

            
            

            - **tableName** *(string) --* 

              The table name.

              
            

            - **awsRegion** *(string) --* 

              The AWS region.

              
            

            - **useCallerCredentials** *(boolean) --* 

              Set to TRUE to use Amazon Cognito credentials with this data source.

              
        
          

          - **lambdaConfig** *(dict) --* 

            Lambda settings.

            
            

            - **lambdaFunctionArn** *(string) --* 

              The ARN for the Lambda function.

              
        
          

          - **elasticsearchConfig** *(dict) --* 

            Amazon Elasticsearch settings.

            
            

            - **endpoint** *(string) --* 

              The endpoint.

              
            

            - **awsRegion** *(string) --* 

              The AWS region.

              
        
      
    

  .. py:method:: get_graphql_api(**kwargs)

    

    Retrieves a ``GraphqlApi`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetGraphqlApi>`_    


    **Request Syntax** 
    ::

      response = client.get_graphql_api(
          apiId='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID for the GraphQL API.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'graphqlApi': {
                'name': 'string',
                'apiId': 'string',
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'defaultAction': 'ALLOW'|'DENY',
                    'appIdClientRegex': 'string'
                },
                'arn': 'string',
                'uris': {
                    'string': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **graphqlApi** *(dict) --* 

          The ``GraphqlApi`` object.

          
          

          - **name** *(string) --* 

            The API name.

            
          

          - **apiId** *(string) --* 

            The API ID.

            
          

          - **authenticationType** *(string) --* 

            The authentication type.

            
          

          - **userPoolConfig** *(dict) --* 

            The Amazon Cognito User Pool configuration.

            
            

            - **userPoolId** *(string) --* 

              The user pool ID.

              
            

            - **awsRegion** *(string) --* 

              The AWS region in which the user pool was created.

              
            

            - **defaultAction** *(string) --* 

              The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration.

              
            

            - **appIdClientRegex** *(string) --* 

              A regular expression for validating the incoming Amazon Cognito User Pool app client ID.

              
        
          

          - **arn** *(string) --* 

            The ARN.

            
          

          - **uris** *(dict) --* 

            The URIs.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
    

  .. py:method:: get_introspection_schema(**kwargs)

    

    Retrieves the introspection schema for a GraphQL API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetIntrospectionSchema>`_    


    **Request Syntax** 
    ::

      response = client.get_introspection_schema(
          apiId='string',
          format='SDL'|'JSON'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type format: string
    :param format: **[REQUIRED]** 

      The schema format: SDL or JSON.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'schema': StreamingBody()
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **schema** (:class:`.StreamingBody`) -- 

          The schema, in GraphQL Schema Definition Language (SDL) format.

           

          For more information, see the `GraphQL SDL documentation <http://graphql.org/learn/schema/>`__ .

          
    

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


  .. py:method:: get_resolver(**kwargs)

    

    Retrieves a ``Resolver`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetResolver>`_    


    **Request Syntax** 
    ::

      response = client.get_resolver(
          apiId='string',
          typeName='string',
          fieldName='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type typeName: string
    :param typeName: **[REQUIRED]** 

      The resolver type name.

      

    
    :type fieldName: string
    :param fieldName: **[REQUIRED]** 

      The resolver field name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resolver': {
                'typeName': 'string',
                'fieldName': 'string',
                'dataSourceName': 'string',
                'resolverArn': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resolver** *(dict) --* 

          The ``Resolver`` object.

          
          

          - **typeName** *(string) --* 

            The resolver type name.

            
          

          - **fieldName** *(string) --* 

            The resolver field name.

            
          

          - **dataSourceName** *(string) --* 

            The resolver data source name.

            
          

          - **resolverArn** *(string) --* 

            The resolver ARN.

            
          

          - **requestMappingTemplate** *(string) --* 

            The request mapping template.

            
          

          - **responseMappingTemplate** *(string) --* 

            The response mapping template.

            
      
    

  .. py:method:: get_schema_creation_status(**kwargs)

    

    Retrieves the current status of a schema creation operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetSchemaCreationStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_schema_creation_status(
          apiId='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'status': 'PROCESSING'|'ACTIVE'|'DELETING',
            'details': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **status** *(string) --* 

          The current state of the schema (PROCESSING, ACTIVE, or DELETING). Once the schema is in the ACTIVE state, you can add data.

          
        

        - **details** *(string) --* 

          Detailed information about the status of the schema creation operation.

          
    

  .. py:method:: get_type(**kwargs)

    

    Retrieves a ``Type`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetType>`_    


    **Request Syntax** 
    ::

      response = client.get_type(
          apiId='string',
          typeName='string',
          format='SDL'|'JSON'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type typeName: string
    :param typeName: **[REQUIRED]** 

      The type name.

      

    
    :type format: string
    :param format: **[REQUIRED]** 

      The type format: SDL or JSON.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'type': {
                'name': 'string',
                'description': 'string',
                'arn': 'string',
                'definition': 'string',
                'format': 'SDL'|'JSON'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **type** *(dict) --* 

          The ``Type`` object.

          
          

          - **name** *(string) --* 

            The type name.

            
          

          - **description** *(string) --* 

            The type description.

            
          

          - **arn** *(string) --* 

            The type ARN.

            
          

          - **definition** *(string) --* 

            The type definition.

            
          

          - **format** *(string) --* 

            The type format: SDL or JSON.

            
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_api_keys(**kwargs)

    

    Lists the API keys for a given API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListApiKeys>`_    


    **Request Syntax** 
    ::

      response = client.list_api_keys(
          apiId='string',
          nextToken='string',
          maxResults=123
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results you want the request to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'apiKeys': [
                {
                    'id': 'string',
                    'description': 'string',
                    'expires': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **apiKeys** *(list) --* 

          The ``ApiKey`` objects.

          
          

          - *(dict) --* 

            Describes an API key.

            
            

            - **id** *(string) --* 

              The API key ID.

              
            

            - **description** *(string) --* 

              A description of the purpose of the API key.

              
            

            - **expires** *(integer) --* 

              The time when the API key expires.

              
        
      
        

        - **nextToken** *(string) --* 

          An identifier to be passed in the next request to this operation to return the next set of items in the list.

          
    

  .. py:method:: list_data_sources(**kwargs)

    

    Lists the data sources for a given API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListDataSources>`_    


    **Request Syntax** 
    ::

      response = client.list_data_sources(
          apiId='string',
          nextToken='string',
          maxResults=123
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results you want the request to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'dataSources': [
                {
                    'dataSourceArn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH',
                    'serviceRoleArn': 'string',
                    'dynamodbConfig': {
                        'tableName': 'string',
                        'awsRegion': 'string',
                        'useCallerCredentials': True|False
                    },
                    'lambdaConfig': {
                        'lambdaFunctionArn': 'string'
                    },
                    'elasticsearchConfig': {
                        'endpoint': 'string',
                        'awsRegion': 'string'
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **dataSources** *(list) --* 

          The ``DataSource`` objects.

          
          

          - *(dict) --* 

            Describes a data source.

            
            

            - **dataSourceArn** *(string) --* 

              The data source ARN.

              
            

            - **name** *(string) --* 

              The name of the data source.

              
            

            - **description** *(string) --* 

              The description of the data source.

              
            

            - **type** *(string) --* 

              The type of the data source.

              
            

            - **serviceRoleArn** *(string) --* 

              The IAM service role ARN for the data source. The system assumes this role when accessing the data source.

              
            

            - **dynamodbConfig** *(dict) --* 

              DynamoDB settings.

              
              

              - **tableName** *(string) --* 

                The table name.

                
              

              - **awsRegion** *(string) --* 

                The AWS region.

                
              

              - **useCallerCredentials** *(boolean) --* 

                Set to TRUE to use Amazon Cognito credentials with this data source.

                
          
            

            - **lambdaConfig** *(dict) --* 

              Lambda settings.

              
              

              - **lambdaFunctionArn** *(string) --* 

                The ARN for the Lambda function.

                
          
            

            - **elasticsearchConfig** *(dict) --* 

              Amazon Elasticsearch settings.

              
              

              - **endpoint** *(string) --* 

                The endpoint.

                
              

              - **awsRegion** *(string) --* 

                The AWS region.

                
          
        
      
        

        - **nextToken** *(string) --* 

          An identifier to be passed in the next request to this operation to return the next set of items in the list.

          
    

  .. py:method:: list_graphql_apis(**kwargs)

    

    Lists your GraphQL APIs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListGraphqlApis>`_    


    **Request Syntax** 
    ::

      response = client.list_graphql_apis(
          nextToken='string',
          maxResults=123
      )
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results you want the request to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'graphqlApis': [
                {
                    'name': 'string',
                    'apiId': 'string',
                    'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
                    'userPoolConfig': {
                        'userPoolId': 'string',
                        'awsRegion': 'string',
                        'defaultAction': 'ALLOW'|'DENY',
                        'appIdClientRegex': 'string'
                    },
                    'arn': 'string',
                    'uris': {
                        'string': 'string'
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **graphqlApis** *(list) --* 

          The ``GraphqlApi`` objects.

          
          

          - *(dict) --* 

            Describes a GraphQL API.

            
            

            - **name** *(string) --* 

              The API name.

              
            

            - **apiId** *(string) --* 

              The API ID.

              
            

            - **authenticationType** *(string) --* 

              The authentication type.

              
            

            - **userPoolConfig** *(dict) --* 

              The Amazon Cognito User Pool configuration.

              
              

              - **userPoolId** *(string) --* 

                The user pool ID.

                
              

              - **awsRegion** *(string) --* 

                The AWS region in which the user pool was created.

                
              

              - **defaultAction** *(string) --* 

                The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration.

                
              

              - **appIdClientRegex** *(string) --* 

                A regular expression for validating the incoming Amazon Cognito User Pool app client ID.

                
          
            

            - **arn** *(string) --* 

              The ARN.

              
            

            - **uris** *(dict) --* 

              The URIs.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **nextToken** *(string) --* 

          An identifier to be passed in the next request to this operation to return the next set of items in the list.

          
    

  .. py:method:: list_resolvers(**kwargs)

    

    Lists the resolvers for a given API and type.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListResolvers>`_    


    **Request Syntax** 
    ::

      response = client.list_resolvers(
          apiId='string',
          typeName='string',
          nextToken='string',
          maxResults=123
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type typeName: string
    :param typeName: **[REQUIRED]** 

      The type name.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results you want the request to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resolvers': [
                {
                    'typeName': 'string',
                    'fieldName': 'string',
                    'dataSourceName': 'string',
                    'resolverArn': 'string',
                    'requestMappingTemplate': 'string',
                    'responseMappingTemplate': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resolvers** *(list) --* 

          The ``Resolver`` objects.

          
          

          - *(dict) --* 

            Describes a resolver.

            
            

            - **typeName** *(string) --* 

              The resolver type name.

              
            

            - **fieldName** *(string) --* 

              The resolver field name.

              
            

            - **dataSourceName** *(string) --* 

              The resolver data source name.

              
            

            - **resolverArn** *(string) --* 

              The resolver ARN.

              
            

            - **requestMappingTemplate** *(string) --* 

              The request mapping template.

              
            

            - **responseMappingTemplate** *(string) --* 

              The response mapping template.

              
        
      
        

        - **nextToken** *(string) --* 

          An identifier to be passed in the next request to this operation to return the next set of items in the list.

          
    

  .. py:method:: list_types(**kwargs)

    

    Lists the types for a given API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListTypes>`_    


    **Request Syntax** 
    ::

      response = client.list_types(
          apiId='string',
          format='SDL'|'JSON',
          nextToken='string',
          maxResults=123
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type format: string
    :param format: **[REQUIRED]** 

      The type format: SDL or JSON.

      

    
    :type nextToken: string
    :param nextToken: 

      An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results you want the request to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'types': [
                {
                    'name': 'string',
                    'description': 'string',
                    'arn': 'string',
                    'definition': 'string',
                    'format': 'SDL'|'JSON'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **types** *(list) --* 

          The ``Type`` objects.

          
          

          - *(dict) --* 

            Describes a type.

            
            

            - **name** *(string) --* 

              The type name.

              
            

            - **description** *(string) --* 

              The type description.

              
            

            - **arn** *(string) --* 

              The type ARN.

              
            

            - **definition** *(string) --* 

              The type definition.

              
            

            - **format** *(string) --* 

              The type format: SDL or JSON.

              
        
      
        

        - **nextToken** *(string) --* 

          An identifier to be passed in the next request to this operation to return the next set of items in the list.

          
    

  .. py:method:: start_schema_creation(**kwargs)

    

    Adds a new schema to your GraphQL API.

     

    This operation is asynchronous. Use to determine when it has completed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/StartSchemaCreation>`_    


    **Request Syntax** 
    ::

      response = client.start_schema_creation(
          apiId='string',
          definition=b'bytes'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type definition: bytes
    :param definition: **[REQUIRED]** 

      The schema definition, in GraphQL schema language format.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'status': 'PROCESSING'|'ACTIVE'|'DELETING'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **status** *(string) --* 

          The current state of the schema (PROCESSING, ACTIVE, or DELETING). Once the schema is in the ACTIVE state, you can add data.

          
    

  .. py:method:: update_data_source(**kwargs)

    

    Updates a ``DataSource`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateDataSource>`_    


    **Request Syntax** 
    ::

      response = client.update_data_source(
          apiId='string',
          name='string',
          description='string',
          type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH',
          serviceRoleArn='string',
          dynamodbConfig={
              'tableName': 'string',
              'awsRegion': 'string',
              'useCallerCredentials': True|False
          },
          lambdaConfig={
              'lambdaFunctionArn': 'string'
          },
          elasticsearchConfig={
              'endpoint': 'string',
              'awsRegion': 'string'
          }
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      The new name for the data source.

      

    
    :type description: string
    :param description: 

      The new description for the data source.

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      The new data source type.

      

    
    :type serviceRoleArn: string
    :param serviceRoleArn: 

      The new service role ARN for the data source.

      

    
    :type dynamodbConfig: dict
    :param dynamodbConfig: 

      The new DynamoDB configuration.

      

    
      - **tableName** *(string) --* **[REQUIRED]** 

        The table name.

        

      
      - **awsRegion** *(string) --* **[REQUIRED]** 

        The AWS region.

        

      
      - **useCallerCredentials** *(boolean) --* 

        Set to TRUE to use Amazon Cognito credentials with this data source.

        

      
    
    :type lambdaConfig: dict
    :param lambdaConfig: 

      The new Lambda configuration.

      

    
      - **lambdaFunctionArn** *(string) --* **[REQUIRED]** 

        The ARN for the Lambda function.

        

      
    
    :type elasticsearchConfig: dict
    :param elasticsearchConfig: 

      The new Elasticsearch configuration.

      

    
      - **endpoint** *(string) --* **[REQUIRED]** 

        The endpoint.

        

      
      - **awsRegion** *(string) --* **[REQUIRED]** 

        The AWS region.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'dataSource': {
                'dataSourceArn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH',
                'serviceRoleArn': 'string',
                'dynamodbConfig': {
                    'tableName': 'string',
                    'awsRegion': 'string',
                    'useCallerCredentials': True|False
                },
                'lambdaConfig': {
                    'lambdaFunctionArn': 'string'
                },
                'elasticsearchConfig': {
                    'endpoint': 'string',
                    'awsRegion': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **dataSource** *(dict) --* 

          The updated ``DataSource`` object.

          
          

          - **dataSourceArn** *(string) --* 

            The data source ARN.

            
          

          - **name** *(string) --* 

            The name of the data source.

            
          

          - **description** *(string) --* 

            The description of the data source.

            
          

          - **type** *(string) --* 

            The type of the data source.

            
          

          - **serviceRoleArn** *(string) --* 

            The IAM service role ARN for the data source. The system assumes this role when accessing the data source.

            
          

          - **dynamodbConfig** *(dict) --* 

            DynamoDB settings.

            
            

            - **tableName** *(string) --* 

              The table name.

              
            

            - **awsRegion** *(string) --* 

              The AWS region.

              
            

            - **useCallerCredentials** *(boolean) --* 

              Set to TRUE to use Amazon Cognito credentials with this data source.

              
        
          

          - **lambdaConfig** *(dict) --* 

            Lambda settings.

            
            

            - **lambdaFunctionArn** *(string) --* 

              The ARN for the Lambda function.

              
        
          

          - **elasticsearchConfig** *(dict) --* 

            Amazon Elasticsearch settings.

            
            

            - **endpoint** *(string) --* 

              The endpoint.

              
            

            - **awsRegion** *(string) --* 

              The AWS region.

              
        
      
    

  .. py:method:: update_graphql_api(**kwargs)

    

    Updates a ``GraphqlApi`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateGraphqlApi>`_    


    **Request Syntax** 
    ::

      response = client.update_graphql_api(
          apiId='string',
          name='string',
          authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
          userPoolConfig={
              'userPoolId': 'string',
              'awsRegion': 'string',
              'defaultAction': 'ALLOW'|'DENY',
              'appIdClientRegex': 'string'
          }
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      The new name for the ``GraphqlApi`` object.

      

    
    :type authenticationType: string
    :param authenticationType: 

      The new authentication type for the ``GraphqlApi`` object.

      

    
    :type userPoolConfig: dict
    :param userPoolConfig: 

      The new Amazon Cognito User Pool configuration for the ``GraphqlApi`` object.

      

    
      - **userPoolId** *(string) --* **[REQUIRED]** 

        The user pool ID.

        

      
      - **awsRegion** *(string) --* **[REQUIRED]** 

        The AWS region in which the user pool was created.

        

      
      - **defaultAction** *(string) --* **[REQUIRED]** 

        The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration.

        

      
      - **appIdClientRegex** *(string) --* 

        A regular expression for validating the incoming Amazon Cognito User Pool app client ID.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'graphqlApi': {
                'name': 'string',
                'apiId': 'string',
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'defaultAction': 'ALLOW'|'DENY',
                    'appIdClientRegex': 'string'
                },
                'arn': 'string',
                'uris': {
                    'string': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **graphqlApi** *(dict) --* 

          The udpated ``GraphqlApi`` object.

          
          

          - **name** *(string) --* 

            The API name.

            
          

          - **apiId** *(string) --* 

            The API ID.

            
          

          - **authenticationType** *(string) --* 

            The authentication type.

            
          

          - **userPoolConfig** *(dict) --* 

            The Amazon Cognito User Pool configuration.

            
            

            - **userPoolId** *(string) --* 

              The user pool ID.

              
            

            - **awsRegion** *(string) --* 

              The AWS region in which the user pool was created.

              
            

            - **defaultAction** *(string) --* 

              The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration.

              
            

            - **appIdClientRegex** *(string) --* 

              A regular expression for validating the incoming Amazon Cognito User Pool app client ID.

              
        
          

          - **arn** *(string) --* 

            The ARN.

            
          

          - **uris** *(dict) --* 

            The URIs.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
    

  .. py:method:: update_resolver(**kwargs)

    

    Updates a ``Resolver`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateResolver>`_    


    **Request Syntax** 
    ::

      response = client.update_resolver(
          apiId='string',
          typeName='string',
          fieldName='string',
          dataSourceName='string',
          requestMappingTemplate='string',
          responseMappingTemplate='string'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type typeName: string
    :param typeName: **[REQUIRED]** 

      The new type name.

      

    
    :type fieldName: string
    :param fieldName: **[REQUIRED]** 

      The new field name.

      

    
    :type dataSourceName: string
    :param dataSourceName: **[REQUIRED]** 

      The new data source name.

      

    
    :type requestMappingTemplate: string
    :param requestMappingTemplate: **[REQUIRED]** 

      The new request mapping template.

      

    
    :type responseMappingTemplate: string
    :param responseMappingTemplate: 

      The new response mapping template.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resolver': {
                'typeName': 'string',
                'fieldName': 'string',
                'dataSourceName': 'string',
                'resolverArn': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resolver** *(dict) --* 

          The updated ``Resolver`` object.

          
          

          - **typeName** *(string) --* 

            The resolver type name.

            
          

          - **fieldName** *(string) --* 

            The resolver field name.

            
          

          - **dataSourceName** *(string) --* 

            The resolver data source name.

            
          

          - **resolverArn** *(string) --* 

            The resolver ARN.

            
          

          - **requestMappingTemplate** *(string) --* 

            The request mapping template.

            
          

          - **responseMappingTemplate** *(string) --* 

            The response mapping template.

            
      
    

  .. py:method:: update_type(**kwargs)

    

    Updates a ``Type`` object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateType>`_    


    **Request Syntax** 
    ::

      response = client.update_type(
          apiId='string',
          typeName='string',
          definition='string',
          format='SDL'|'JSON'
      )
    :type apiId: string
    :param apiId: **[REQUIRED]** 

      The API ID.

      

    
    :type typeName: string
    :param typeName: **[REQUIRED]** 

      The new type name.

      

    
    :type definition: string
    :param definition: 

      The new definition.

      

    
    :type format: string
    :param format: **[REQUIRED]** 

      The new type format: SDL or JSON.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'type': {
                'name': 'string',
                'description': 'string',
                'arn': 'string',
                'definition': 'string',
                'format': 'SDL'|'JSON'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **type** *(dict) --* 

          The updated ``Type`` object.

          
          

          - **name** *(string) --* 

            The type name.

            
          

          - **description** *(string) --* 

            The type description.

            
          

          - **arn** *(string) --* 

            The type ARN.

            
          

          - **definition** *(string) --* 

            The type definition.

            
          

          - **format** *(string) --* 

            The type format: SDL or JSON.

            
      
    

==========
Paginators
==========


The available paginators are:
