

**********
APIGateway
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: APIGateway.Client

  A low-level client representing Amazon API Gateway::

    
    import boto3
    
    client = boto3.client('apigateway')

  
  These are the available methods:
  
  *   :py:meth:`~APIGateway.Client.can_paginate`

  
  *   :py:meth:`~APIGateway.Client.create_api_key`

  
  *   :py:meth:`~APIGateway.Client.create_authorizer`

  
  *   :py:meth:`~APIGateway.Client.create_base_path_mapping`

  
  *   :py:meth:`~APIGateway.Client.create_deployment`

  
  *   :py:meth:`~APIGateway.Client.create_documentation_part`

  
  *   :py:meth:`~APIGateway.Client.create_documentation_version`

  
  *   :py:meth:`~APIGateway.Client.create_domain_name`

  
  *   :py:meth:`~APIGateway.Client.create_model`

  
  *   :py:meth:`~APIGateway.Client.create_request_validator`

  
  *   :py:meth:`~APIGateway.Client.create_resource`

  
  *   :py:meth:`~APIGateway.Client.create_rest_api`

  
  *   :py:meth:`~APIGateway.Client.create_stage`

  
  *   :py:meth:`~APIGateway.Client.create_usage_plan`

  
  *   :py:meth:`~APIGateway.Client.create_usage_plan_key`

  
  *   :py:meth:`~APIGateway.Client.create_vpc_link`

  
  *   :py:meth:`~APIGateway.Client.delete_api_key`

  
  *   :py:meth:`~APIGateway.Client.delete_authorizer`

  
  *   :py:meth:`~APIGateway.Client.delete_base_path_mapping`

  
  *   :py:meth:`~APIGateway.Client.delete_client_certificate`

  
  *   :py:meth:`~APIGateway.Client.delete_deployment`

  
  *   :py:meth:`~APIGateway.Client.delete_documentation_part`

  
  *   :py:meth:`~APIGateway.Client.delete_documentation_version`

  
  *   :py:meth:`~APIGateway.Client.delete_domain_name`

  
  *   :py:meth:`~APIGateway.Client.delete_gateway_response`

  
  *   :py:meth:`~APIGateway.Client.delete_integration`

  
  *   :py:meth:`~APIGateway.Client.delete_integration_response`

  
  *   :py:meth:`~APIGateway.Client.delete_method`

  
  *   :py:meth:`~APIGateway.Client.delete_method_response`

  
  *   :py:meth:`~APIGateway.Client.delete_model`

  
  *   :py:meth:`~APIGateway.Client.delete_request_validator`

  
  *   :py:meth:`~APIGateway.Client.delete_resource`

  
  *   :py:meth:`~APIGateway.Client.delete_rest_api`

  
  *   :py:meth:`~APIGateway.Client.delete_stage`

  
  *   :py:meth:`~APIGateway.Client.delete_usage_plan`

  
  *   :py:meth:`~APIGateway.Client.delete_usage_plan_key`

  
  *   :py:meth:`~APIGateway.Client.delete_vpc_link`

  
  *   :py:meth:`~APIGateway.Client.flush_stage_authorizers_cache`

  
  *   :py:meth:`~APIGateway.Client.flush_stage_cache`

  
  *   :py:meth:`~APIGateway.Client.generate_client_certificate`

  
  *   :py:meth:`~APIGateway.Client.generate_presigned_url`

  
  *   :py:meth:`~APIGateway.Client.get_account`

  
  *   :py:meth:`~APIGateway.Client.get_api_key`

  
  *   :py:meth:`~APIGateway.Client.get_api_keys`

  
  *   :py:meth:`~APIGateway.Client.get_authorizer`

  
  *   :py:meth:`~APIGateway.Client.get_authorizers`

  
  *   :py:meth:`~APIGateway.Client.get_base_path_mapping`

  
  *   :py:meth:`~APIGateway.Client.get_base_path_mappings`

  
  *   :py:meth:`~APIGateway.Client.get_client_certificate`

  
  *   :py:meth:`~APIGateway.Client.get_client_certificates`

  
  *   :py:meth:`~APIGateway.Client.get_deployment`

  
  *   :py:meth:`~APIGateway.Client.get_deployments`

  
  *   :py:meth:`~APIGateway.Client.get_documentation_part`

  
  *   :py:meth:`~APIGateway.Client.get_documentation_parts`

  
  *   :py:meth:`~APIGateway.Client.get_documentation_version`

  
  *   :py:meth:`~APIGateway.Client.get_documentation_versions`

  
  *   :py:meth:`~APIGateway.Client.get_domain_name`

  
  *   :py:meth:`~APIGateway.Client.get_domain_names`

  
  *   :py:meth:`~APIGateway.Client.get_export`

  
  *   :py:meth:`~APIGateway.Client.get_gateway_response`

  
  *   :py:meth:`~APIGateway.Client.get_gateway_responses`

  
  *   :py:meth:`~APIGateway.Client.get_integration`

  
  *   :py:meth:`~APIGateway.Client.get_integration_response`

  
  *   :py:meth:`~APIGateway.Client.get_method`

  
  *   :py:meth:`~APIGateway.Client.get_method_response`

  
  *   :py:meth:`~APIGateway.Client.get_model`

  
  *   :py:meth:`~APIGateway.Client.get_model_template`

  
  *   :py:meth:`~APIGateway.Client.get_models`

  
  *   :py:meth:`~APIGateway.Client.get_paginator`

  
  *   :py:meth:`~APIGateway.Client.get_request_validator`

  
  *   :py:meth:`~APIGateway.Client.get_request_validators`

  
  *   :py:meth:`~APIGateway.Client.get_resource`

  
  *   :py:meth:`~APIGateway.Client.get_resources`

  
  *   :py:meth:`~APIGateway.Client.get_rest_api`

  
  *   :py:meth:`~APIGateway.Client.get_rest_apis`

  
  *   :py:meth:`~APIGateway.Client.get_sdk`

  
  *   :py:meth:`~APIGateway.Client.get_sdk_type`

  
  *   :py:meth:`~APIGateway.Client.get_sdk_types`

  
  *   :py:meth:`~APIGateway.Client.get_stage`

  
  *   :py:meth:`~APIGateway.Client.get_stages`

  
  *   :py:meth:`~APIGateway.Client.get_usage`

  
  *   :py:meth:`~APIGateway.Client.get_usage_plan`

  
  *   :py:meth:`~APIGateway.Client.get_usage_plan_key`

  
  *   :py:meth:`~APIGateway.Client.get_usage_plan_keys`

  
  *   :py:meth:`~APIGateway.Client.get_usage_plans`

  
  *   :py:meth:`~APIGateway.Client.get_vpc_link`

  
  *   :py:meth:`~APIGateway.Client.get_vpc_links`

  
  *   :py:meth:`~APIGateway.Client.get_waiter`

  
  *   :py:meth:`~APIGateway.Client.import_api_keys`

  
  *   :py:meth:`~APIGateway.Client.import_documentation_parts`

  
  *   :py:meth:`~APIGateway.Client.import_rest_api`

  
  *   :py:meth:`~APIGateway.Client.put_gateway_response`

  
  *   :py:meth:`~APIGateway.Client.put_integration`

  
  *   :py:meth:`~APIGateway.Client.put_integration_response`

  
  *   :py:meth:`~APIGateway.Client.put_method`

  
  *   :py:meth:`~APIGateway.Client.put_method_response`

  
  *   :py:meth:`~APIGateway.Client.put_rest_api`

  
  *   :py:meth:`~APIGateway.Client.test_invoke_authorizer`

  
  *   :py:meth:`~APIGateway.Client.test_invoke_method`

  
  *   :py:meth:`~APIGateway.Client.update_account`

  
  *   :py:meth:`~APIGateway.Client.update_api_key`

  
  *   :py:meth:`~APIGateway.Client.update_authorizer`

  
  *   :py:meth:`~APIGateway.Client.update_base_path_mapping`

  
  *   :py:meth:`~APIGateway.Client.update_client_certificate`

  
  *   :py:meth:`~APIGateway.Client.update_deployment`

  
  *   :py:meth:`~APIGateway.Client.update_documentation_part`

  
  *   :py:meth:`~APIGateway.Client.update_documentation_version`

  
  *   :py:meth:`~APIGateway.Client.update_domain_name`

  
  *   :py:meth:`~APIGateway.Client.update_gateway_response`

  
  *   :py:meth:`~APIGateway.Client.update_integration`

  
  *   :py:meth:`~APIGateway.Client.update_integration_response`

  
  *   :py:meth:`~APIGateway.Client.update_method`

  
  *   :py:meth:`~APIGateway.Client.update_method_response`

  
  *   :py:meth:`~APIGateway.Client.update_model`

  
  *   :py:meth:`~APIGateway.Client.update_request_validator`

  
  *   :py:meth:`~APIGateway.Client.update_resource`

  
  *   :py:meth:`~APIGateway.Client.update_rest_api`

  
  *   :py:meth:`~APIGateway.Client.update_stage`

  
  *   :py:meth:`~APIGateway.Client.update_usage`

  
  *   :py:meth:`~APIGateway.Client.update_usage_plan`

  
  *   :py:meth:`~APIGateway.Client.update_vpc_link`

  

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

    

    Create an  ApiKey resource. 

     `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/create-api-key.html>`__ 

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateApiKey>`_    


    **Request Syntax** 
    ::

      response = client.create_api_key(
          name='string',
          description='string',
          enabled=True|False,
          generateDistinctId=True|False,
          value='string',
          stageKeys=[
              {
                  'restApiId': 'string',
                  'stageName': 'string'
              },
          ],
          customerId='string'
      )
    :type name: string
    :param name: 

      The name of the  ApiKey .

      

    
    :type description: string
    :param description: 

      The description of the  ApiKey .

      

    
    :type enabled: boolean
    :param enabled: 

      Specifies whether the  ApiKey can be used by callers.

      

    
    :type generateDistinctId: boolean
    :param generateDistinctId: 

      Specifies whether (``true`` ) or not (``false`` ) the key identifier is distinct from the created API key value.

      

    
    :type value: string
    :param value: 

      Specifies a value of the API key.

      

    
    :type stageKeys: list
    :param stageKeys: 

      DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.

      

    
      - *(dict) --* 

        A reference to a unique stage identified in the format ``{restApiId}/{stage}`` .

        

      
        - **restApiId** *(string) --* 

          The string identifier of the associated  RestApi .

          

        
        - **stageName** *(string) --* 

          The stage name associated with the stage key.

          

        
      
  
    :type customerId: string
    :param customerId: 

      An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'value': 'string',
            'name': 'string',
            'customerId': 'string',
            'description': 'string',
            'enabled': True|False,
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1),
            'stageKeys': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A resource that can be distributed to callers for executing  Method resources that require an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the callers with the API key can make requests to that stage.

          `Use API Keys <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__  
        

        - **id** *(string) --* 

          The identifier of the API Key.

          
        

        - **value** *(string) --* 

          The value of the API Key.

          
        

        - **name** *(string) --* 

          The name of the API Key.

          
        

        - **customerId** *(string) --* 

          An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

          
        

        - **description** *(string) --* 

          The description of the API Key.

          
        

        - **enabled** *(boolean) --* 

          Specifies whether the API Key can be used by callers.

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the API Key was created.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The timestamp when the API Key was last updated.

          
        

        - **stageKeys** *(list) --* 

          A list of  Stage resources that are associated with the  ApiKey resource.

          
          

          - *(string) --* 
      
    

  .. py:method:: create_authorizer(**kwargs)

    

    Adds a new  Authorizer resource to an existing  RestApi resource.

     `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/create-authorizer.html>`__ 

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.create_authorizer(
          restApiId='string',
          name='string',
          type='TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
          providerARNs=[
              'string',
          ],
          authType='string',
          authorizerUri='string',
          authorizerCredentials='string',
          identitySource='string',
          identityValidationExpression='string',
          authorizerResultTtlInSeconds=123
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      [Required] The name of the authorizer.

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      [Required] The authorizer type. Valid values are ``TOKEN`` for a Lambda function using a single authorization token submitted in a custom header, ``REQUEST`` for a Lambda function using incoming request parameters, and ``COGNITO_USER_POOLS`` for using an Amazon Cognito user pool.

      

    
    :type providerARNs: list
    :param providerARNs: 

      A list of the Amazon Cognito user pool ARNs for the ``COGNITO_USER_POOLS`` authorizer. Each element is of this format: ``arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`` . For a ``TOKEN`` or ``REQUEST`` authorizer, this is not defined. 

      

    
      - *(string) --* 

      
  
    :type authType: string
    :param authType: 

      Optional customer-defined field, used in Swagger imports and exports without functional impact.

      

    
    :type authorizerUri: string
    :param authorizerUri: 

      Specifies the authorizer's Uniform Resource Identifier (URI). For ``TOKEN`` or ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations`` . In general, the URI has this form ``arn:aws:apigateway:{region}:lambda:path/{service_api}`` , where ``{region}`` is the same as the region hosting the Lambda function, ``path`` indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``/`` . For Lambda functions, this is usually of the form ``/2015-03-31/functions/[FunctionARN]/invocations`` .

      

    
    :type authorizerCredentials: string
    :param authorizerCredentials: 

      Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.

      

    
    :type identitySource: string
    :param identitySource: 

      The identity source for which authorization is requested. 

      
      * For a ``TOKEN`` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is ``Auth`` , the header mapping expression is ``method.request.header.Auth`` .
      
      * For the ``REQUEST`` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an ``Auth`` header, a ``Name`` query string parameter are defined as identity sources, this value is ``method.request.header.Auth, method.request.querystring.Name`` . These parameters will be used to derive the authorization caching key and to perform runtime validation of the ``REQUEST`` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
      
      * For a ``COGNITO_USER_POOLS`` authorizer, this property is not used.
      

      

      

    
    :type identityValidationExpression: string
    :param identityValidationExpression: 

      A validation expression for the incoming identity token. For ``TOKEN`` authorizers, this value is a regular expression. API Gateway will match the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the ``REQUEST`` authorizer.

      

    
    :type authorizerResultTtlInSeconds: integer
    :param authorizerResultTtlInSeconds: 

      The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
            'providerARNs': [
                'string',
            ],
            'authType': 'string',
            'authorizerUri': 'string',
            'authorizerCredentials': 'string',
            'identitySource': 'string',
            'identityValidationExpression': 'string',
            'authorizerResultTtlInSeconds': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an authorization layer for methods. If enabled on a method, API Gateway will activate the authorizer when a client calls the method.

          `Enable custom authorization <http://docs.aws.amazon.com/apigateway/latest/developerguide/use-custom-authorizer.html>`__  
        

        - **id** *(string) --* 

          The identifier for the authorizer resource.

          
        

        - **name** *(string) --* 

          [Required] The name of the authorizer.

          
        

        - **type** *(string) --* 

          [Required] The authorizer type. Valid values are ``TOKEN`` for a Lambda function using a single authorization token submitted in a custom header, ``REQUEST`` for a Lambda function using incoming request parameters, and ``COGNITO_USER_POOLS`` for using an Amazon Cognito user pool.

          
        

        - **providerARNs** *(list) --* 

          A list of the Amazon Cognito user pool ARNs for the ``COGNITO_USER_POOLS`` authorizer. Each element is of this format: ``arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`` . For a ``TOKEN`` or ``REQUEST`` authorizer, this is not defined. 

          
          

          - *(string) --* 
      
        

        - **authType** *(string) --* 

          Optional customer-defined field, used in Swagger imports and exports without functional impact.

          
        

        - **authorizerUri** *(string) --* 

          Specifies the authorizer's Uniform Resource Identifier (URI). For ``TOKEN`` or ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations`` . In general, the URI has this form ``arn:aws:apigateway:{region}:lambda:path/{service_api}`` , where ``{region}`` is the same as the region hosting the Lambda function, ``path`` indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``/`` . For Lambda functions, this is usually of the form ``/2015-03-31/functions/[FunctionARN]/invocations`` .

          
        

        - **authorizerCredentials** *(string) --* 

          Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.

          
        

        - **identitySource** *(string) --* 

          The identity source for which authorization is requested. 

          
          * For a ``TOKEN`` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is ``Auth`` , the header mapping expression is ``method.request.header.Auth`` .
          
          * For the ``REQUEST`` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an ``Auth`` header, a ``Name`` query string parameter are defined as identity sources, this value is ``method.request.header.Auth, method.request.querystring.Name`` . These parameters will be used to derive the authorization caching key and to perform runtime validation of the ``REQUEST`` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
          
          * For a ``COGNITO_USER_POOLS`` authorizer, this property is not used.
          

          

          
        

        - **identityValidationExpression** *(string) --* 

          A validation expression for the incoming identity token. For ``TOKEN`` authorizers, this value is a regular expression. API Gateway will match the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the ``REQUEST`` authorizer.

          
        

        - **authorizerResultTtlInSeconds** *(integer) --* 

          The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.

          
    

  .. py:method:: create_base_path_mapping(**kwargs)

    

    Creates a new  BasePathMapping resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateBasePathMapping>`_    


    **Request Syntax** 
    ::

      response = client.create_base_path_mapping(
          domainName='string',
          basePath='string',
          restApiId='string',
          stage='string'
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name of the  BasePathMapping resource to create.

      

    
    :type basePath: string
    :param basePath: 

      The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify a base path name after the domain name.

      

    
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stage: string
    :param stage: 

      The name of the API's stage that you want to use for this mapping. Leave this blank if you do not want callers to explicitly specify the stage name after any base path name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'basePath': 'string',
            'restApiId': 'string',
            'stage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the base path that callers of the API must provide as part of the URL after the domain name.

         A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi in a given stage of the owner  Account .  `Use Custom Domain Names <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **basePath** *(string) --* 

          The base path name that callers of the API must provide as part of the URL after the domain name.

          
        

        - **restApiId** *(string) --* 

          The string identifier of the associated  RestApi .

          
        

        - **stage** *(string) --* 

          The name of the associated stage.

          
    

  .. py:method:: create_deployment(**kwargs)

    

    Creates a  Deployment resource, which makes a specified  RestApi callable over the internet.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateDeployment>`_    


    **Request Syntax** 
    ::

      response = client.create_deployment(
          restApiId='string',
          stageName='string',
          stageDescription='string',
          description='string',
          cacheClusterEnabled=True|False,
          cacheClusterSize='0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
          variables={
              'string': 'string'
          },
          canarySettings={
              'percentTraffic': 123.0,
              'stageVariableOverrides': {
                  'string': 'string'
              },
              'useStageCache': True|False
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: 

      The name of the  Stage resource for the  Deployment resource to create.

      

    
    :type stageDescription: string
    :param stageDescription: 

      The description of the  Stage resource for the  Deployment resource to create.

      

    
    :type description: string
    :param description: 

      The description for the  Deployment resource to create.

      

    
    :type cacheClusterEnabled: boolean
    :param cacheClusterEnabled: 

      Enables a cache cluster for the  Stage resource specified in the input.

      

    
    :type cacheClusterSize: string
    :param cacheClusterSize: 

      Specifies the cache cluster size for the  Stage resource specified in the input, if a cache cluster is enabled.

      

    
    :type variables: dict
    :param variables: 

      A map that defines the stage variables for the  Stage resource that is associated with the new deployment. Variable names can have alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+`` .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type canarySettings: dict
    :param canarySettings: 

      The input configuration for the canary deployment when the deployment is a canary release deployment. 

      

    
      - **percentTraffic** *(float) --* 

        The percentage (0.0-100.0) of traffic routed to the canary deployment.

        

      
      - **stageVariableOverrides** *(dict) --* 

        A stage variable overrides used for the canary release deployment. They can override existing stage variables or add new stage variables for the canary release deployment. These stage variables are represented as a string-to-string map between stage variable names and their values.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **useStageCache** *(boolean) --* 

        A Boolean flag to indicate whether the canary release deployment uses the stage cache or not.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'apiSummary': {
                'string': {
                    'string': {
                        'authorizationType': 'string',
                        'apiKeyRequired': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        An immutable representation of a  RestApi resource that can be called by users using  Stages . A deployment must be associated with a  Stage for it to be callable over the Internet.

         To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,  Deployments ,  Stage , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS SDKs <https://aws.amazon.com/tools/>`__  
        

        - **id** *(string) --* 

          The identifier for the deployment resource.

          
        

        - **description** *(string) --* 

          The description for the deployment resource.

          
        

        - **createdDate** *(datetime) --* 

          The date and time that the deployment resource was created.

          
        

        - **apiSummary** *(dict) --* 

          A summary of the  RestApi at the date and time that the deployment resource was created.

          
          

          - *(string) --* 
            

            - *(dict) --* 
              

              - *(string) --* 
                

                - *(dict) --* 

                  Represents a summary of a  Method resource, given a particular date and time.

                  
                  

                  - **authorizationType** *(string) --* 

                    The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                    
                  

                  - **apiKeyRequired** *(boolean) --* 

                    Specifies whether the method requires a valid  ApiKey .

                    
              
          
        
      
    
    

  .. py:method:: create_documentation_part(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateDocumentationPart>`_    


    **Request Syntax** 
    ::

      response = client.create_documentation_part(
          restApiId='string',
          location={
              'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
              'path': 'string',
              'method': 'string',
              'statusCode': 'string',
              'name': 'string'
          },
          properties='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type location: dict
    :param location: **[REQUIRED]** 

      [Required] The location of the targeted API entity of the to-be-created documentation part.

      

    
      - **type** *(string) --* **[REQUIRED]** 

        The type of API entity to which the documentation content applies. It is a valid and required field for API entity types of ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or ``RESOURCE`` type.

        

      
      - **path** *(string) --* 

        The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an applicable child entity inherits the content of another entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``path`` attribute must match that of the parent entity as a prefix.

        

      
      - **method** *(string) --* 

        The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any method. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``method`` attribute must match that of the parent entity exactly.

        

      
      - **statusCode** *(string) --* 

        The HTTP status code of a response. It is a valid field for the API entity types of ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any status code. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``statusCode`` attribute must match that of the parent entity exactly.

        

      
      - **name** *(string) --* 

        The name of the targeted API entity. It is a valid and required field for the API entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for any other entity type.

        

      
    
    :type properties: string
    :param properties: **[REQUIRED]** 

      [Required] The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only Swagger-compliant key-value pairs can be exported and, hence, published.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'location': {
                'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
                'path': 'string',
                'method': 'string',
                'statusCode': 'string',
                'name': 'string'
            },
            'properties': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A documentation part for a targeted API entity.

          

        A documentation part consists of a content map (``properties`` ) and a target (``location`` ). The target specifies an API entity to which the documentation content applies. The supported API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend on the API entity type. All valid fields are not required.

         

        The content map is a JSON string of API-specific key-value pairs. Although an API can use any shape for the content map, only the Swagger-compliant documentation fields will be injected into the associated API entity definition in the exported Swagger definition file.

          `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationParts  
        

        - **id** *(string) --* 

          The  DocumentationPart identifier, generated by API Gateway when the ``DocumentationPart`` is created.

          
        

        - **location** *(dict) --* 

          The location of the API entity to which the documentation applies. Valid fields depend on the targeted API entity type. All the valid location fields are not required. If not explicitly specified, a valid location field is treated as a wildcard and associated documentation content may be inherited by matching entities, unless overridden.

          
          

          - **type** *(string) --* 

            The type of API entity to which the documentation content applies. It is a valid and required field for API entity types of ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or ``RESOURCE`` type.

            
          

          - **path** *(string) --* 

            The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an applicable child entity inherits the content of another entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``path`` attribute must match that of the parent entity as a prefix.

            
          

          - **method** *(string) --* 

            The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any method. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``method`` attribute must match that of the parent entity exactly.

            
          

          - **statusCode** *(string) --* 

            The HTTP status code of a response. It is a valid field for the API entity types of ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any status code. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``statusCode`` attribute must match that of the parent entity exactly.

            
          

          - **name** *(string) --* 

            The name of the targeted API entity. It is a valid and required field for the API entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for any other entity type.

            
      
        

        - **properties** *(string) --* 

          A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., ``"{ \"description\": \"The API does ...\" }"`` . Only Swagger-compliant documentation-related fields from the propertiesmap are exported and, hence, published as part of the API entity definitions, while the original documentation parts are exported in a Swagger extension of ``x-amazon-apigateway-documentation`` .

          
    

  .. py:method:: create_documentation_version(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateDocumentationVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_documentation_version(
          restApiId='string',
          documentationVersion='string',
          stageName='string',
          description='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type documentationVersion: string
    :param documentationVersion: **[REQUIRED]** 

      [Required] The version identifier of the new snapshot.

      

    
    :type stageName: string
    :param stageName: 

      The stage name to be associated with the new documentation snapshot.

      

    
    :type description: string
    :param description: 

      A description about the new documentation snapshot.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'version': 'string',
            'createdDate': datetime(2015, 1, 1),
            'description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A snapshot of the documentation of an API.

         

        Publishing API documentation involves creating a documentation version associated with an API stage and exporting the versioned documentation to an external (e.g., Swagger) file.

          `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationPart ,  DocumentationVersions  
        

        - **version** *(string) --* 

          The version identifier of the API documentation snapshot.

          
        

        - **createdDate** *(datetime) --* 

          The date when the API documentation snapshot is created.

          
        

        - **description** *(string) --* 

          The description of the API documentation snapshot.

          
    

  .. py:method:: create_domain_name(**kwargs)

    

    Creates a new domain name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateDomainName>`_    


    **Request Syntax** 
    ::

      response = client.create_domain_name(
          domainName='string',
          certificateName='string',
          certificateBody='string',
          certificatePrivateKey='string',
          certificateChain='string',
          certificateArn='string',
          regionalCertificateName='string',
          regionalCertificateArn='string',
          endpointConfiguration={
              'types': [
                  'REGIONAL'|'EDGE',
              ]
          }
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      (Required) The name of the  DomainName resource.

      

    
    :type certificateName: string
    :param certificateName: 

      The user-friendly name of the certificate that will be used by edge-optimized endpoint for this domain name.

      

    
    :type certificateBody: string
    :param certificateBody: 

      [Deprecated] The body of the server certificate that will be used by edge-optimized endpoint for this domain name provided by your certificate authority.

      

    
    :type certificatePrivateKey: string
    :param certificatePrivateKey: 

      [Deprecated] Your edge-optimized endpoint's domain name certificate's private key.

      

    
    :type certificateChain: string
    :param certificateChain: 

      [Deprecated] The intermediate certificates and optionally the root certificate, one after the other without any blank lines, used by an edge-optimized endpoint for this domain name. If you include the root certificate, your certificate chain must start with intermediate certificates and end with the root certificate. Use the intermediate certificates that were provided by your certificate authority. Do not include any intermediaries that are not in the chain of trust path.

      

    
    :type certificateArn: string
    :param certificateArn: 

      The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

      

    
    :type regionalCertificateName: string
    :param regionalCertificateName: 

      The user-friendly name of the certificate that will be used by regional endpoint for this domain name.

      

    
    :type regionalCertificateArn: string
    :param regionalCertificateArn: 

      The reference to an AWS-managed certificate that will be used by regional endpoint for this domain name. AWS Certificate Manager is the only supported source.

      

    
    :type endpointConfiguration: dict
    :param endpointConfiguration: 

      The endpoint configuration of this  DomainName showing the endpoint types of the domain name. 

      

    
      - **types** *(list) --* 

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

        

      
        - *(string) --* 

          The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

          

        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'domainName': 'string',
            'certificateName': 'string',
            'certificateArn': 'string',
            'certificateUploadDate': datetime(2015, 1, 1),
            'regionalDomainName': 'string',
            'regionalHostedZoneId': 'string',
            'regionalCertificateName': 'string',
            'regionalCertificateArn': 'string',
            'distributionDomainName': 'string',
            'distributionHostedZoneId': 'string',
            'endpointConfiguration': {
                'types': [
                    'REGIONAL'|'EDGE',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

          

        When you deploy an API, API Gateway creates a default host name for the API. This default API host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the default host name, you can access the API's root resource with the URL of ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a custom domain name of ``apis.example.com`` for this API, you can then access the same resource using the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path mapping ( BasePathMapping ) of your API under the custom domain name. 

           `Set a Custom Host Name for an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **domainName** *(string) --* 

          The name of the  DomainName resource.

          
        

        - **certificateName** *(string) --* 

          The name of the certificate that will be used by edge-optimized endpoint for this domain name.

          
        

        - **certificateArn** *(string) --* 

          The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

          
        

        - **certificateUploadDate** *(datetime) --* 

          The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

          
        

        - **regionalDomainName** *(string) --* 

          The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.

          
        

        - **regionalHostedZoneId** *(string) --* 

          The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

          
        

        - **regionalCertificateName** *(string) --* 

          The name of the certificate that will be used for validating the regional domain name.

          
        

        - **regionalCertificateArn** *(string) --* 

          The reference to an AWS-managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.

          
        

        - **distributionDomainName** *(string) --* 

          The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the `Amazon CloudFront documentation <http://aws.amazon.com/documentation/cloudfront/>`__ .

          
        

        - **distributionHostedZoneId** *(string) --* 

          The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is ``Z2FDTNDATAQYW2`` for all the regions. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

          
        

        - **endpointConfiguration** *(dict) --* 

          The endpoint configuration of this  DomainName showing the endpoint types of the domain name. 

          
          

          - **types** *(list) --* 

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

            
            

            - *(string) --* 

              The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

              
        
      
    

  .. py:method:: create_model(**kwargs)

    

    Adds a new  Model resource to an existing  RestApi resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateModel>`_    


    **Request Syntax** 
    ::

      response = client.create_model(
          restApiId='string',
          name='string',
          description='string',
          schema='string',
          contentType='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The  RestApi identifier under which the  Model will be created.

      

    
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the model. Must be alphanumeric.

      

    
    :type description: string
    :param description: 

      The description of the model.

      

    
    :type schema: string
    :param schema: 

      The schema for the model. For ``application/json`` models, this should be `JSON-schema draft v4 <http://json-schema.org/documentation.html>`__ model.

      

    
    :type contentType: string
    :param contentType: **[REQUIRED]** 

      The content-type for the model.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'schema': 'string',
            'contentType': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the data structure of a method's request or response payload.

          

        A request model defines the data structure of the client-supplied request payload. A response model defines the data structure of the response payload returned by the back end. Although not required, models are useful for mapping payloads between the front end and back end.

         

        A model is used for generating an API's SDK, validating the input request body, and creating a skeletal mapping template.

            Method ,  MethodResponse , `Models and Mappings <http://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__  
        

        - **id** *(string) --* 

          The identifier for the model resource.

          
        

        - **name** *(string) --* 

          The name of the model. Must be an alphanumeric string.

          
        

        - **description** *(string) --* 

          The description of the model.

          
        

        - **schema** *(string) --* 

          The schema for the model. For ``application/json`` models, this should be `JSON-schema draft v4 <http://json-schema.org/documentation.html>`__ model. Do not include "\*/" characters in the description of any properties because such "\*/" characters may be interpreted as the closing marker for comments in some languages, such as Java or JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

          
        

        - **contentType** *(string) --* 

          The content-type for the model.

          
    

  .. py:method:: create_request_validator(**kwargs)

    

    Creates a  ReqeustValidator of a given  RestApi .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateRequestValidator>`_    


    **Request Syntax** 
    ::

      response = client.create_request_validator(
          restApiId='string',
          name='string',
          validateRequestBody=True|False,
          validateRequestParameters=True|False
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type name: string
    :param name: 

      The name of the to-be-created  RequestValidator .

      

    
    :type validateRequestBody: boolean
    :param validateRequestBody: 

      A Boolean flag to indicate whether to validate request body according to the configured model schema for the method (``true`` ) or not (``false`` ).

      

    
    :type validateRequestParameters: boolean
    :param validateRequestParameters: 

      A Boolean flag to indicate whether to validate request parameters, ``true`` , or not ``false`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'validateRequestBody': True|False,
            'validateRequestParameters': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        A set of validation rules for incoming  Method requests.

          

        In Swagger, a  RequestValidator of an API is defined by the `x-amazon-apigateway-request-validators.requestValidator <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.requestValidator.html>`__ object. It the referenced using the `x-amazon-apigateway-request-validator <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validator>`__ property.

          `Enable Basic Request Validation in API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__ 
        

        - **id** *(string) --* 

          The identifier of this  RequestValidator .

          
        

        - **name** *(string) --* 

          The name of this  RequestValidator 

          
        

        - **validateRequestBody** *(boolean) --* 

          A Boolean flag to indicate whether to validate a request body according to the configured  Model schema.

          
        

        - **validateRequestParameters** *(boolean) --* 

          A Boolean flag to indicate whether to validate request parameters (``true`` ) or not (``false`` ).

          
    

  .. py:method:: create_resource(**kwargs)

    

    Creates a  Resource resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateResource>`_    


    **Request Syntax** 
    ::

      response = client.create_resource(
          restApiId='string',
          parentId='string',
          pathPart='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type parentId: string
    :param parentId: **[REQUIRED]** 

      The parent resource's identifier.

      

    
    :type pathPart: string
    :param pathPart: **[REQUIRED]** 

      The last path segment for this resource.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'parentId': 'string',
            'pathPart': 'string',
            'path': 'string',
            'resourceMethods': {
                'string': {
                    'httpMethod': 'string',
                    'authorizationType': 'string',
                    'authorizerId': 'string',
                    'apiKeyRequired': True|False,
                    'requestValidatorId': 'string',
                    'operationName': 'string',
                    'requestParameters': {
                        'string': True|False
                    },
                    'requestModels': {
                        'string': 'string'
                    },
                    'methodResponses': {
                        'string': {
                            'statusCode': 'string',
                            'responseParameters': {
                                'string': True|False
                            },
                            'responseModels': {
                                'string': 'string'
                            }
                        }
                    },
                    'methodIntegration': {
                        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                        'httpMethod': 'string',
                        'uri': 'string',
                        'connectionType': 'INTERNET'|'VPC_LINK',
                        'connectionId': 'string',
                        'credentials': 'string',
                        'requestParameters': {
                            'string': 'string'
                        },
                        'requestTemplates': {
                            'string': 'string'
                        },
                        'passthroughBehavior': 'string',
                        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                        'timeoutInMillis': 123,
                        'cacheNamespace': 'string',
                        'cacheKeyParameters': [
                            'string',
                        ],
                        'integrationResponses': {
                            'string': {
                                'statusCode': 'string',
                                'selectionPattern': 'string',
                                'responseParameters': {
                                    'string': 'string'
                                },
                                'responseTemplates': {
                                    'string': 'string'
                                },
                                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                            }
                        }
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an API resource.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **id** *(string) --* 

          The resource's identifier.

          
        

        - **parentId** *(string) --* 

          The parent resource's identifier.

          
        

        - **pathPart** *(string) --* 

          The last path segment for this resource.

          
        

        - **path** *(string) --* 

          The full path for this resource.

          
        

        - **resourceMethods** *(dict) --* 

          Gets an API resource's method of a given HTTP verb.

            

          The resource methods are a map of methods indexed by methods' HTTP verbs enabled on the resource. This method map is included in the ``200 OK`` response of the ``GET /restapis/{restapi_id}/resources/{resource_id}`` or ``GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods`` request.

           Example: Get the GET method of an API resource Request ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20170223T031827Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": false, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

          If the ``OPTIONS`` is enabled on the resource, you can follow the example here to get that method. Just replace the ``GET`` of the last path segment in the request URL with ``OPTIONS`` .

             
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents a client-facing interface by which the client calls the API to access back-end resources. A **Method** resource is integrated with an  Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a **Method** resource, whereas an integration request is embodied in an  Integration resource. On the other hand, a method response is represented by a  MethodResponse resource, whereas an integration response is represented by an  IntegrationResponse resource. 

                

              

               Example: Retrive the GET method on a specified resource Request 

              The following example request retrieves the information about the GET method on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ). 

               ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

              The successful response returns a ``200 OK`` status code and a payload similar to the following:

               ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

              In the example above, the response template for the ``200 OK`` response maps the JSON output from the ``ListStreams`` action in the back end to an XML output. The mapping template is URL-encoded as ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`` and the output is decoded using the `$util.urlDecode() <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__ helper function.

                  MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up an API's method <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__  
              

              - **httpMethod** *(string) --* 

                The method's HTTP verb.

                
              

              - **authorizationType** *(string) --* 

                The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                
              

              - **authorizerId** *(string) --* 

                The identifier of an  Authorizer to use on this method. The ``authorizationType`` must be ``CUSTOM`` .

                
              

              - **apiKeyRequired** *(boolean) --* 

                A boolean flag specifying whether a valid  ApiKey is required to invoke this method.

                
              

              - **requestValidatorId** *(string) --* 

                The identifier of a  RequestValidator for request validation.

                
              

              - **operationName** *(string) --* 

                A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

                
              

              - **requestParameters** *(dict) --* 

                A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or templates.

                
                

                - *(string) --* 
                  

                  - *(boolean) --* 
            
          
              

              - **requestModels** *(dict) --* 

                A key-value map specifying data schemas, represented by  Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **methodResponses** *(dict) --* 

                Gets a method response associated with a given HTTP status code. 

                  

                The collection of method responses are encapsulated in a key-value map, where the key is a response's HTTP status code and the value is a  MethodResponse resource that specifies the response returned to the caller from the back end through the integration response.

                 Example: Get a 200 OK response of a GET method Request 

                

                 ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                The successful response returns a ``200 OK`` status code and a payload similar to the following:

                 ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }``  

                

                   `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__  
                

                - *(string) --* 
                  

                  - *(dict) --* 

                    Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

                      

                    

                     Example: A **MethodResponse** instance of an API Request 

                    The example request retrieves a **MethodResponse** of the 200 status code.

                     ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                    The successful response returns ``200 OK`` status and a payload as follows:

                     ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

                    

                        Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                    

                    - **statusCode** *(string) --* 

                      The method response's status code.

                      
                    

                    - **responseParameters** *(dict) --* 

                      A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

                      
                      

                      - *(string) --* 
                        

                        - *(boolean) --* 
                  
                
                    

                    - **responseModels** *(dict) --* 

                      Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

                      
                      

                      - *(string) --* 
                        

                        - *(string) --* 
                  
                
                
            
          
              

              - **methodIntegration** *(dict) --* 

                Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.

                  

                

                 Example:  Request 

                

                 ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                The successful response returns a ``200 OK`` status code and a payload similar to the following:

                 ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }``  

                

                   `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__  
                

                - **type** *(string) --* 

                  Specifies an API method integration type. The valid value is one of the following:

                   

                   
                  * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
                   
                  * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
                   
                  * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
                   
                  * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
                   
                  * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
                   

                   

                  For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

                  
                

                - **httpMethod** *(string) --* 

                  Specifies the integration's HTTP method type.

                  
                

                - **uri** *(string) --* 

                  Specifies Uniform Resource Identifier (URI) of the integration endpoint.

                   

                   
                  * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
                   
                  * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
                  

                  
                

                - **connectionType** *(string) --* 

                  The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

                  
                

                - **connectionId** *(string) --* 

                  The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

                  
                

                - **credentials** *(string) --* 

                  Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

                  
                

                - **requestParameters** *(dict) --* 

                  A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **requestTemplates** *(dict) --* 

                  Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **passthroughBehavior** *(string) --*  

                  Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

                   

                   
                  * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
                   
                  * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
                   
                  * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
                   

                   
                

                - **contentHandling** *(string) --* 

                  Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                   

                   
                  * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
                   
                  * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
                   

                   

                  If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

                  
                

                - **timeoutInMillis** *(integer) --* 

                  Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

                  
                

                - **cacheNamespace** *(string) --* 

                  Specifies the integration's cache namespace.

                  
                

                - **cacheKeyParameters** *(list) --* 

                  Specifies the integration's cache key parameters.

                  
                  

                  - *(string) --* 
              
                

                - **integrationResponses** *(dict) --* 

                  Specifies the integration's responses.

                    

                  

                   Example: Get integration responses of a method Request 

                  

                   ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                  The successful response returns ``200 OK`` status and a payload as follows:

                   ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

                  

                     `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                  

                  - *(string) --* 
                    

                    - *(dict) --* 

                      Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                        `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                      

                      - **statusCode** *(string) --* 

                        Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                        
                      

                      - **selectionPattern** *(string) --* 

                        Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                        
                      

                      - **responseParameters** *(dict) --* 

                        A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                        
                        

                        - *(string) --* 
                          

                          - *(string) --* 
                    
                  
                      

                      - **responseTemplates** *(dict) --* 

                        Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                        
                        

                        - *(string) --* 
                          

                          - *(string) --* 
                    
                  
                      

                      - **contentHandling** *(string) --* 

                        Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                         

                         
                        * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                         
                        * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                         

                         

                        If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                        
                  
              
            
            
          
      
    
    

  .. py:method:: create_rest_api(**kwargs)

    

    Creates a new  RestApi resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateRestApi>`_    


    **Request Syntax** 
    ::

      response = client.create_rest_api(
          name='string',
          description='string',
          version='string',
          cloneFrom='string',
          binaryMediaTypes=[
              'string',
          ],
          endpointConfiguration={
              'types': [
                  'REGIONAL'|'EDGE',
              ]
          }
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the  RestApi .

      

    
    :type description: string
    :param description: 

      The description of the  RestApi .

      

    
    :type version: string
    :param version: 

      A version identifier for the API.

      

    
    :type cloneFrom: string
    :param cloneFrom: 

      The ID of the  RestApi that you want to clone from.

      

    
    :type binaryMediaTypes: list
    :param binaryMediaTypes: 

      The list of binary media types supported by the  RestApi . By default, the  RestApi supports only UTF-8-encoded text payloads.

      

    
      - *(string) --* 

      
  
    :type endpointConfiguration: dict
    :param endpointConfiguration: 

      The endpoint configuration of this  RestApi showing the endpoint types of the API. 

      

    
      - **types** *(list) --* 

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

        

      
        - *(string) --* 

          The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

          

        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'warnings': [
                'string',
            ],
            'binaryMediaTypes': [
                'string',
            ],
            'endpointConfiguration': {
                'types': [
                    'REGIONAL'|'EDGE',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a REST API.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **id** *(string) --* 

          The API's identifier. This identifier is unique across all of your APIs in API Gateway.

          
        

        - **name** *(string) --* 

          The API's name.

          
        

        - **description** *(string) --* 

          The API's description.

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the API was created.

          
        

        - **version** *(string) --* 

          A version identifier for the API.

          
        

        - **warnings** *(list) --* 

          The warning messages reported when ``failonwarnings`` is turned on during API import.

          
          

          - *(string) --* 
      
        

        - **binaryMediaTypes** *(list) --* 

          The list of binary media types supported by the  RestApi . By default, the  RestApi supports only UTF-8-encoded text payloads.

          
          

          - *(string) --* 
      
        

        - **endpointConfiguration** *(dict) --* 

          The endpoint configuration of this  RestApi showing the endpoint types of the API. 

          
          

          - **types** *(list) --* 

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

            
            

            - *(string) --* 

              The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

              
        
      
    

  .. py:method:: create_stage(**kwargs)

    

    Creates a new  Stage resource that references a pre-existing  Deployment for the API. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateStage>`_    


    **Request Syntax** 
    ::

      response = client.create_stage(
          restApiId='string',
          stageName='string',
          deploymentId='string',
          description='string',
          cacheClusterEnabled=True|False,
          cacheClusterSize='0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
          variables={
              'string': 'string'
          },
          documentationVersion='string',
          canarySettings={
              'percentTraffic': 123.0,
              'deploymentId': 'string',
              'stageVariableOverrides': {
                  'string': 'string'
              },
              'useStageCache': True|False
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: **[REQUIRED]** 

      [Required] The name for the  Stage resource.

      

    
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      [Required] The identifier of the  Deployment resource for the  Stage resource.

      

    
    :type description: string
    :param description: 

      The description of the  Stage resource.

      

    
    :type cacheClusterEnabled: boolean
    :param cacheClusterEnabled: 

      Whether cache clustering is enabled for the stage.

      

    
    :type cacheClusterSize: string
    :param cacheClusterSize: 

      The stage's cache cluster size.

      

    
    :type variables: dict
    :param variables: 

      A map that defines the stage variables for the new  Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+`` .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type documentationVersion: string
    :param documentationVersion: 

      The version of the associated API documentation.

      

    
    :type canarySettings: dict
    :param canarySettings: 

      The canary deployment settings of this stage.

      

    
      - **percentTraffic** *(float) --* 

        The percent (0-100) of traffic diverted to a canary deployment.

        

      
      - **deploymentId** *(string) --* 

        The ID of the canary deployment.

        

      
      - **stageVariableOverrides** *(dict) --* 

        Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **useStageCache** *(boolean) --* 

        A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentId': 'string',
            'clientCertificateId': 'string',
            'stageName': 'string',
            'description': 'string',
            'cacheClusterEnabled': True|False,
            'cacheClusterSize': '0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
            'cacheClusterStatus': 'CREATE_IN_PROGRESS'|'AVAILABLE'|'DELETE_IN_PROGRESS'|'NOT_AVAILABLE'|'FLUSH_IN_PROGRESS',
            'methodSettings': {
                'string': {
                    'metricsEnabled': True|False,
                    'loggingLevel': 'string',
                    'dataTraceEnabled': True|False,
                    'throttlingBurstLimit': 123,
                    'throttlingRateLimit': 123.0,
                    'cachingEnabled': True|False,
                    'cacheTtlInSeconds': 123,
                    'cacheDataEncrypted': True|False,
                    'requireAuthorizationForCacheControl': True|False,
                    'unauthorizedCacheControlHeaderStrategy': 'FAIL_WITH_403'|'SUCCEED_WITH_RESPONSE_HEADER'|'SUCCEED_WITHOUT_RESPONSE_HEADER'
                }
            },
            'variables': {
                'string': 'string'
            },
            'documentationVersion': 'string',
            'accessLogSettings': {
                'format': 'string',
                'destinationArn': 'string'
            },
            'canarySettings': {
                'percentTraffic': 123.0,
                'deploymentId': 'string',
                'stageVariableOverrides': {
                    'string': 'string'
                },
                'useStageCache': True|False
            },
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

          `Deploy an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__  
        

        - **deploymentId** *(string) --* 

          The identifier of the  Deployment that the stage points to.

          
        

        - **clientCertificateId** *(string) --* 

          The identifier of a client certificate for an API stage.

          
        

        - **stageName** *(string) --* 

          The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway.

          
        

        - **description** *(string) --* 

          The stage's description.

          
        

        - **cacheClusterEnabled** *(boolean) --* 

          Specifies whether a cache cluster is enabled for the stage.

          
        

        - **cacheClusterSize** *(string) --* 

          The size of the cache cluster for the stage, if enabled.

          
        

        - **cacheClusterStatus** *(string) --* 

          The status of the cache cluster for the stage, if enabled.

          
        

        - **methodSettings** *(dict) --* 

          A map that defines the method settings for a  Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\*/\*`` for overriding all methods in the stage. 

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Specifies the method setting properties.

              
              

              - **metricsEnabled** *(boolean) --* 

                Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a Boolean.

                
              

              - **loggingLevel** *(string) --* 

                Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` , ``ERROR`` , and ``INFO`` .

                
              

              - **dataTraceEnabled** *(boolean) --* 

                Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

                
              

              - **throttlingBurstLimit** *(integer) --* 

                Specifies the throttling burst limit. The PATCH path for this setting is ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

                
              

              - **throttlingRateLimit** *(float) --* 

                Specifies the throttling rate limit. The PATCH path for this setting is ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

                
              

              - **cachingEnabled** *(boolean) --* 

                Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached. The PATCH path for this setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

                
              

              - **cacheTtlInSeconds** *(integer) --* 

                Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached. The PATCH path for this setting is ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

                
              

              - **cacheDataEncrypted** *(boolean) --* 

                Specifies whether the cached responses are encrypted. The PATCH path for this setting is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

                
              

              - **requireAuthorizationForCacheControl** *(boolean) --* 

                Specifies whether authorization is required for a cache invalidation request. The PATCH path for this setting is ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value is a Boolean.

                
              

              - **unauthorizedCacheControlHeaderStrategy** *(string) --* 

                Specifies how to handle unauthorized requests for cache invalidation. The PATCH path for this setting is ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` , ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

                
          
      
    
        

        - **variables** *(dict) --* 

          A map that defines the stage variables for a  Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+`` .

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **documentationVersion** *(string) --* 

          The version of the associated API documentation.

          
        

        - **accessLogSettings** *(dict) --* 

          Settings for logging access in this stage.

          
          

          - **format** *(string) --* 

            A single line format of the access logs of data, as specified by selected `$context variables <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__ . The format must include at least ``$context.requestId`` .

            
          

          - **destinationArn** *(string) --* 

            The ARN of the CloudWatch Logs log group to receive access logs.

            
      
        

        - **canarySettings** *(dict) --* 

          Settings for the canary deployment in this stage.

          
          

          - **percentTraffic** *(float) --* 

            The percent (0-100) of traffic diverted to a canary deployment.

            
          

          - **deploymentId** *(string) --* 

            The ID of the canary deployment.

            
          

          - **stageVariableOverrides** *(dict) --* 

            Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **useStageCache** *(boolean) --* 

            A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

            
      
        

        - **createdDate** *(datetime) --* 

          The timestamp when the stage was created.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The timestamp when the stage last updated.

          
    

  .. py:method:: create_usage_plan(**kwargs)

    

    Creates a usage plan with the throttle and quota limits, as well as the associated API stages, specified in the payload. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateUsagePlan>`_    


    **Request Syntax** 
    ::

      response = client.create_usage_plan(
          name='string',
          description='string',
          apiStages=[
              {
                  'apiId': 'string',
                  'stage': 'string'
              },
          ],
          throttle={
              'burstLimit': 123,
              'rateLimit': 123.0
          },
          quota={
              'limit': 123,
              'offset': 123,
              'period': 'DAY'|'WEEK'|'MONTH'
          }
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the usage plan.

      

    
    :type description: string
    :param description: 

      The description of the usage plan.

      

    
    :type apiStages: list
    :param apiStages: 

      The associated API stages of the usage plan.

      

    
      - *(dict) --* 

        API stage name of the associated API stage in a usage plan.

        

      
        - **apiId** *(string) --* 

          API Id of the associated API stage in a usage plan.

          

        
        - **stage** *(string) --* 

          API stage name of the associated API stage in a usage plan.

          

        
      
  
    :type throttle: dict
    :param throttle: 

      The throttling limits of the usage plan.

      

    
      - **burstLimit** *(integer) --* 

        The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.

        

      
      - **rateLimit** *(float) --* 

        The API request steady-state rate limit.

        

      
    
    :type quota: dict
    :param quota: 

      The quota of the usage plan.

      

    
      - **limit** *(integer) --* 

        The maximum number of requests that can be made in a given time period.

        

      
      - **offset** *(integer) --* 

        The number of requests subtracted from the given limit in the initial time period.

        

      
      - **period** *(string) --* 

        The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'apiStages': [
                {
                    'apiId': 'string',
                    'stage': 'string'
                },
            ],
            'throttle': {
                'burstLimit': 123,
                'rateLimit': 123.0
            },
            'quota': {
                'limit': 123,
                'offset': 123,
                'period': 'DAY'|'WEEK'|'MONTH'
            },
            'productCode': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a usage plan than can specify who can assess associated API stages with specified request limits and quotas.

          

        In a usage plan, you associate an API by specifying the API's Id and a stage name of the specified API. You add plan customers by adding API keys to the plan. 

           `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **id** *(string) --* 

          The identifier of a  UsagePlan resource.

          
        

        - **name** *(string) --* 

          The name of a usage plan.

          
        

        - **description** *(string) --* 

          The description of a usage plan.

          
        

        - **apiStages** *(list) --* 

          The associated API stages of a usage plan.

          
          

          - *(dict) --* 

            API stage name of the associated API stage in a usage plan.

            
            

            - **apiId** *(string) --* 

              API Id of the associated API stage in a usage plan.

              
            

            - **stage** *(string) --* 

              API stage name of the associated API stage in a usage plan.

              
        
      
        

        - **throttle** *(dict) --* 

          The request throttle limits of a usage plan.

          
          

          - **burstLimit** *(integer) --* 

            The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.

            
          

          - **rateLimit** *(float) --* 

            The API request steady-state rate limit.

            
      
        

        - **quota** *(dict) --* 

          The maximum number of permitted requests per a given unit time interval.

          
          

          - **limit** *(integer) --* 

            The maximum number of requests that can be made in a given time period.

            
          

          - **offset** *(integer) --* 

            The number of requests subtracted from the given limit in the initial time period.

            
          

          - **period** *(string) --* 

            The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".

            
      
        

        - **productCode** *(string) --* 

          The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

          
    

  .. py:method:: create_usage_plan_key(**kwargs)

    

    Creates a usage plan key for adding an existing API key to a usage plan.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateUsagePlanKey>`_    


    **Request Syntax** 
    ::

      response = client.create_usage_plan_key(
          usagePlanId='string',
          keyId='string',
          keyType='string'
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the  UsagePlan resource representing the usage plan containing the to-be-created  UsagePlanKey resource representing a plan customer.

      

    
    :type keyId: string
    :param keyId: **[REQUIRED]** 

      The identifier of a  UsagePlanKey resource for a plan customer.

      

    
    :type keyType: string
    :param keyType: **[REQUIRED]** 

      The type of a  UsagePlanKey resource for a plan customer.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'type': 'string',
            'value': 'string',
            'name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a usage plan key to identify a plan customer.

          

        To associate an API stage with a selected API key in a usage plan, you must create a UsagePlanKey resource to represent the selected  ApiKey .

         "  `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **id** *(string) --* 

          The Id of a usage plan key.

          
        

        - **type** *(string) --* 

          The type of a usage plan key. Currently, the valid key type is ``API_KEY`` .

          
        

        - **value** *(string) --* 

          The value of a usage plan key.

          
        

        - **name** *(string) --* 

          The name of a usage plan key.

          
    

  .. py:method:: create_vpc_link(**kwargs)

    

    Creates a VPC link, under the caller's account in a selected region, in an asynchronous operation that typically takes 2-4 minutes to complete and become operational. The caller must have permissions to create and update VPC Endpoint services.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateVpcLink>`_    


    **Request Syntax** 
    ::

      response = client.create_vpc_link(
          name='string',
          description='string',
          targetArns=[
              'string',
          ]
      )
    :type name: string
    :param name: **[REQUIRED]** 

      [Required] The name used to label and identify the VPC link.

      

    
    :type description: string
    :param description: 

      The description of the VPC link.

      

    
    :type targetArns: list
    :param targetArns: **[REQUIRED]** 

      [Required] The ARNs of network load balancers of the VPC targeted by the VPC link. The network load balancers must be owned by the same AWS account of the API owner.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'targetArns': [
                'string',
            ],
            'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
            'statusMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud (VPC).

          

        

        To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway, you, as an API developer, create a  VpcLink resource targeted for one or more network load balancers of the VPC and then integrate an API method with a private integration that uses the  VpcLink . The private integraiton has an integration type of ``HTTP`` or ``HTTP_PROXY`` and has a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to identify the  VpcLink used.

         

         
        

        - **id** *(string) --* 

          The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

          
        

        - **name** *(string) --* 

          The name used to label and identify the VPC link.

          
        

        - **description** *(string) --* 

          The description of the VPC link.

          
        

        - **targetArns** *(list) --* 

          The ARNs of network load balancers of the VPC targeted by the VPC link. The network load balancers must be owned by the same AWS account of the API owner.

          
          

          - *(string) --* 
      
        

        - **status** *(string) --* 

          The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` , ``DELETING`` , or ``FAILED`` . Deploying an API will wait if the status is ``PENDING`` and will fail if the status is ``DELETING`` . 

          
        

        - **statusMessage** *(string) --* 

          A description about the VPC link status.

          
    

  .. py:method:: delete_api_key(**kwargs)

    

    Deletes the  ApiKey resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteApiKey>`_    


    **Request Syntax** 
    ::

      response = client.delete_api_key(
          apiKey='string'
      )
    :type apiKey: string
    :param apiKey: **[REQUIRED]** 

      The identifier of the  ApiKey resource to be deleted.

      

    
    
    :returns: None

  .. py:method:: delete_authorizer(**kwargs)

    

    Deletes an existing  Authorizer resource.

     `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/delete-authorizer.html>`__ 

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.delete_authorizer(
          restApiId='string',
          authorizerId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type authorizerId: string
    :param authorizerId: **[REQUIRED]** 

      The identifier of the  Authorizer resource.

      

    
    
    :returns: None

  .. py:method:: delete_base_path_mapping(**kwargs)

    

    Deletes the  BasePathMapping resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteBasePathMapping>`_    


    **Request Syntax** 
    ::

      response = client.delete_base_path_mapping(
          domainName='string',
          basePath='string'
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name of the  BasePathMapping resource to delete.

      

    
    :type basePath: string
    :param basePath: **[REQUIRED]** 

      The base path name of the  BasePathMapping resource to delete.

      

    
    
    :returns: None

  .. py:method:: delete_client_certificate(**kwargs)

    

    Deletes the  ClientCertificate resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteClientCertificate>`_    


    **Request Syntax** 
    ::

      response = client.delete_client_certificate(
          clientCertificateId='string'
      )
    :type clientCertificateId: string
    :param clientCertificateId: **[REQUIRED]** 

      The identifier of the  ClientCertificate resource to be deleted.

      

    
    
    :returns: None

  .. py:method:: delete_deployment(**kwargs)

    

    Deletes a  Deployment resource. Deleting a deployment will only succeed if there are no  Stage resources associated with it.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteDeployment>`_    


    **Request Syntax** 
    ::

      response = client.delete_deployment(
          restApiId='string',
          deploymentId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      The identifier of the  Deployment resource to delete.

      

    
    
    :returns: None

  .. py:method:: delete_documentation_part(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteDocumentationPart>`_    


    **Request Syntax** 
    ::

      response = client.delete_documentation_part(
          restApiId='string',
          documentationPartId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type documentationPartId: string
    :param documentationPartId: **[REQUIRED]** 

      [Required] The identifier of the to-be-deleted documentation part.

      

    
    
    :returns: None

  .. py:method:: delete_documentation_version(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteDocumentationVersion>`_    


    **Request Syntax** 
    ::

      response = client.delete_documentation_version(
          restApiId='string',
          documentationVersion='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type documentationVersion: string
    :param documentationVersion: **[REQUIRED]** 

      [Required] The version identifier of a to-be-deleted documentation snapshot.

      

    
    
    :returns: None

  .. py:method:: delete_domain_name(**kwargs)

    

    Deletes the  DomainName resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteDomainName>`_    


    **Request Syntax** 
    ::

      response = client.delete_domain_name(
          domainName='string'
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The name of the  DomainName resource to be deleted.

      

    
    
    :returns: None

  .. py:method:: delete_gateway_response(**kwargs)

    

    Clears any customization of a  GatewayResponse of a specified response type on the given  RestApi and resets it with the default settings.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteGatewayResponse>`_    


    **Request Syntax** 
    ::

      response = client.delete_gateway_response(
          restApiId='string',
          responseType='DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type responseType: string
    :param responseType: **[REQUIRED]** 

      

      The response type of the associated  GatewayResponse . Valid values are 

      
      * ACCESS_DENIED
      
      * API_CONFIGURATION_ERROR
      
      * AUTHORIZER_FAILURE
      
      * AUTHORIZER_CONFIGURATION_ERROR
      
      * BAD_REQUEST_PARAMETERS
      
      * BAD_REQUEST_BODY
      
      * DEFAULT_4XX
      
      * DEFAULT_5XX
      
      * EXPIRED_TOKEN
      
      * INVALID_SIGNATURE
      
      * INTEGRATION_FAILURE
      
      * INTEGRATION_TIMEOUT
      
      * INVALID_API_KEY
      
      * MISSING_AUTHENTICATION_TOKEN
      
      * QUOTA_EXCEEDED
      
      * REQUEST_TOO_LARGE
      
      * RESOURCE_NOT_FOUND
      
      * THROTTLED
      
      * UNAUTHORIZED
      
      * UNSUPPORTED_MEDIA_TYPES
      

       

      

      

    
    
    :returns: None

  .. py:method:: delete_integration(**kwargs)

    

    Represents a delete integration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteIntegration>`_    


    **Request Syntax** 
    ::

      response = client.delete_integration(
          restApiId='string',
          resourceId='string',
          httpMethod='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Specifies a delete integration request's resource identifier.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies a delete integration request's HTTP method.

      

    
    
    :returns: None

  .. py:method:: delete_integration_response(**kwargs)

    

    Represents a delete integration response.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteIntegrationResponse>`_    


    **Request Syntax** 
    ::

      response = client.delete_integration_response(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          statusCode='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Specifies a delete integration response request's resource identifier.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies a delete integration response request's HTTP method.

      

    
    :type statusCode: string
    :param statusCode: **[REQUIRED]** 

      Specifies a delete integration response request's status code.

      

    
    
    :returns: None

  .. py:method:: delete_method(**kwargs)

    

    Deletes an existing  Method resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteMethod>`_    


    **Request Syntax** 
    ::

      response = client.delete_method(
          restApiId='string',
          resourceId='string',
          httpMethod='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The  Resource identifier for the  Method resource.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      The HTTP verb of the  Method resource.

      

    
    
    :returns: None

  .. py:method:: delete_method_response(**kwargs)

    

    Deletes an existing  MethodResponse resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteMethodResponse>`_    


    **Request Syntax** 
    ::

      response = client.delete_method_response(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          statusCode='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The  Resource identifier for the  MethodResponse resource.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      The HTTP verb of the  Method resource.

      

    
    :type statusCode: string
    :param statusCode: **[REQUIRED]** 

      The status code identifier for the  MethodResponse resource.

      

    
    
    :returns: None

  .. py:method:: delete_model(**kwargs)

    

    Deletes a model.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteModel>`_    


    **Request Syntax** 
    ::

      response = client.delete_model(
          restApiId='string',
          modelName='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type modelName: string
    :param modelName: **[REQUIRED]** 

      The name of the model to delete.

      

    
    
    :returns: None

  .. py:method:: delete_request_validator(**kwargs)

    

    Deletes a  RequestValidator of a given  RestApi .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteRequestValidator>`_    


    **Request Syntax** 
    ::

      response = client.delete_request_validator(
          restApiId='string',
          requestValidatorId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type requestValidatorId: string
    :param requestValidatorId: **[REQUIRED]** 

      [Required] The identifier of the  RequestValidator to be deleted.

      

    
    
    :returns: None

  .. py:method:: delete_resource(**kwargs)

    

    Deletes a  Resource resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteResource>`_    


    **Request Syntax** 
    ::

      response = client.delete_resource(
          restApiId='string',
          resourceId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The identifier of the  Resource resource.

      

    
    
    :returns: None

  .. py:method:: delete_rest_api(**kwargs)

    

    Deletes the specified API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteRestApi>`_    


    **Request Syntax** 
    ::

      response = client.delete_rest_api(
          restApiId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    
    :returns: None

  .. py:method:: delete_stage(**kwargs)

    

    Deletes a  Stage resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteStage>`_    


    **Request Syntax** 
    ::

      response = client.delete_stage(
          restApiId='string',
          stageName='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: **[REQUIRED]** 

      The name of the  Stage resource to delete.

      

    
    
    :returns: None

  .. py:method:: delete_usage_plan(**kwargs)

    

    Deletes a usage plan of a given plan Id.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteUsagePlan>`_    


    **Request Syntax** 
    ::

      response = client.delete_usage_plan(
          usagePlanId='string'
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the to-be-deleted usage plan.

      

    
    
    :returns: None

  .. py:method:: delete_usage_plan_key(**kwargs)

    

    Deletes a usage plan key and remove the underlying API key from the associated usage plan.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteUsagePlanKey>`_    


    **Request Syntax** 
    ::

      response = client.delete_usage_plan_key(
          usagePlanId='string',
          keyId='string'
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the  UsagePlan resource representing the usage plan containing the to-be-deleted  UsagePlanKey resource representing a plan customer.

      

    
    :type keyId: string
    :param keyId: **[REQUIRED]** 

      The Id of the  UsagePlanKey resource to be deleted.

      

    
    
    :returns: None

  .. py:method:: delete_vpc_link(**kwargs)

    

    Deletes an existing  VpcLink of a specified identifier.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteVpcLink>`_    


    **Request Syntax** 
    ::

      response = client.delete_vpc_link(
          vpcLinkId='string'
      )
    :type vpcLinkId: string
    :param vpcLinkId: **[REQUIRED]** 

      [Required] The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

      

    
    
    :returns: None

  .. py:method:: flush_stage_authorizers_cache(**kwargs)

    

    Flushes all authorizer cache entries on a stage.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/FlushStageAuthorizersCache>`_    


    **Request Syntax** 
    ::

      response = client.flush_stage_authorizers_cache(
          restApiId='string',
          stageName='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: **[REQUIRED]** 

      The name of the stage to flush.

      

    
    
    :returns: None

  .. py:method:: flush_stage_cache(**kwargs)

    

    Flushes a stage's cache.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/FlushStageCache>`_    


    **Request Syntax** 
    ::

      response = client.flush_stage_cache(
          restApiId='string',
          stageName='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: **[REQUIRED]** 

      The name of the stage to flush its cache.

      

    
    
    :returns: None

  .. py:method:: generate_client_certificate(**kwargs)

    

    Generates a  ClientCertificate resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GenerateClientCertificate>`_    


    **Request Syntax** 
    ::

      response = client.generate_client_certificate(
          description='string'
      )
    :type description: string
    :param description: 

      The description of the  ClientCertificate .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'clientCertificateId': 'string',
            'description': 'string',
            'pemEncodedCertificate': 'string',
            'createdDate': datetime(2015, 1, 1),
            'expirationDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a client certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.

         Client certificates are used to authenticate an API by the backend server. To authenticate an API client (or user), use IAM roles and policies, a custom  Authorizer or an Amazon Cognito user pool.  `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__  
        

        - **clientCertificateId** *(string) --* 

          The identifier of the client certificate.

          
        

        - **description** *(string) --* 

          The description of the client certificate.

          
        

        - **pemEncodedCertificate** *(string) --* 

          The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the client certificate was created.

          
        

        - **expirationDate** *(datetime) --* 

          The timestamp when the client certificate will expire.

          
    

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


  .. py:method:: get_account()

    

    Gets information about the current  Account resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetAccount>`_    


    **Request Syntax** 
    ::

      response = client.get_account()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'cloudwatchRoleArn': 'string',
            'throttleSettings': {
                'burstLimit': 123,
                'rateLimit': 123.0
            },
            'features': [
                'string',
            ],
            'apiKeyVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an AWS account that is associated with API Gateway.

          

        To view the account info, call ``GET`` on this resource.

         Error Codes 

        The following exception may be thrown when the request fails.

         

         
        * UnauthorizedException
         
        * NotFoundException
         
        * TooManyRequestsException
         

         

        For detailed error code information, including the corresponding HTTP Status Codes, see `API Gateway Error Codes <http://docs.aws.amazon.com/apigateway/api-reference/handling-errors/#api-error-codes>`__ 

         Example: Get the information about an account. Request ``GET /account HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160531T184618Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

        The successful response returns a ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/account-apigateway-{rel}.html", "name": "account", "templated": true }, "self": { "href": "/account" }, "account:update": { "href": "/account" } }, "cloudwatchRoleArn": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "throttleSettings": { "rateLimit": 500, "burstLimit": 1000 } }``  

        In addition to making the REST API call directly, you can use the AWS CLI and an AWS SDK to access this resource.

           `API Gateway Limits <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-limits.html>`__  `Developer Guide <http://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>`__ , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-account.html>`__  
        

        - **cloudwatchRoleArn** *(string) --* 

          The ARN of an Amazon CloudWatch role for the current  Account . 

          
        

        - **throttleSettings** *(dict) --* 

          Specifies the API request limits configured for the current  Account .

          
          

          - **burstLimit** *(integer) --* 

            The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.

            
          

          - **rateLimit** *(float) --* 

            The API request steady-state rate limit.

            
      
        

        - **features** *(list) --* 

          A list of features supported for the account. When usage plans are enabled, the features list will include an entry of ``"UsagePlans"`` .

          
          

          - *(string) --* 
      
        

        - **apiKeyVersion** *(string) --* 

          The version of the API keys used for the account.

          
    

  .. py:method:: get_api_key(**kwargs)

    

    Gets information about the current  ApiKey resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetApiKey>`_    


    **Request Syntax** 
    ::

      response = client.get_api_key(
          apiKey='string',
          includeValue=True|False
      )
    :type apiKey: string
    :param apiKey: **[REQUIRED]** 

      The identifier of the  ApiKey resource.

      

    
    :type includeValue: boolean
    :param includeValue: 

      A boolean flag to specify whether (``true`` ) or not (``false`` ) the result contains the key value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'value': 'string',
            'name': 'string',
            'customerId': 'string',
            'description': 'string',
            'enabled': True|False,
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1),
            'stageKeys': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A resource that can be distributed to callers for executing  Method resources that require an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the callers with the API key can make requests to that stage.

          `Use API Keys <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__  
        

        - **id** *(string) --* 

          The identifier of the API Key.

          
        

        - **value** *(string) --* 

          The value of the API Key.

          
        

        - **name** *(string) --* 

          The name of the API Key.

          
        

        - **customerId** *(string) --* 

          An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

          
        

        - **description** *(string) --* 

          The description of the API Key.

          
        

        - **enabled** *(boolean) --* 

          Specifies whether the API Key can be used by callers.

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the API Key was created.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The timestamp when the API Key was last updated.

          
        

        - **stageKeys** *(list) --* 

          A list of  Stage resources that are associated with the  ApiKey resource.

          
          

          - *(string) --* 
      
    

  .. py:method:: get_api_keys(**kwargs)

    

    Gets information about the current  ApiKeys resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetApiKeys>`_    


    **Request Syntax** 
    ::

      response = client.get_api_keys(
          position='string',
          limit=123,
          nameQuery='string',
          customerId='string',
          includeValues=True|False
      )
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    :type nameQuery: string
    :param nameQuery: 

      The name of queried API keys.

      

    
    :type customerId: string
    :param customerId: 

      The identifier of a customer in AWS Marketplace or an external system, such as a developer portal.

      

    
    :type includeValues: boolean
    :param includeValues: 

      A boolean flag to specify whether (``true`` ) or not (``false`` ) the result contains key values.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'warnings': [
                'string',
            ],
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'value': 'string',
                    'name': 'string',
                    'customerId': 'string',
                    'description': 'string',
                    'enabled': True|False,
                    'createdDate': datetime(2015, 1, 1),
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'stageKeys': [
                        'string',
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of API keys as represented by an  ApiKeys resource.

          `Use API Keys <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__  
        

        - **warnings** *(list) --* 

          A list of warning messages logged during the import of API keys when the ``failOnWarnings`` option is set to true.

          
          

          - *(string) --* 
      
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            A resource that can be distributed to callers for executing  Method resources that require an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the callers with the API key can make requests to that stage.

              `Use API Keys <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__  
            

            - **id** *(string) --* 

              The identifier of the API Key.

              
            

            - **value** *(string) --* 

              The value of the API Key.

              
            

            - **name** *(string) --* 

              The name of the API Key.

              
            

            - **customerId** *(string) --* 

              An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

              
            

            - **description** *(string) --* 

              The description of the API Key.

              
            

            - **enabled** *(boolean) --* 

              Specifies whether the API Key can be used by callers.

              
            

            - **createdDate** *(datetime) --* 

              The timestamp when the API Key was created.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The timestamp when the API Key was last updated.

              
            

            - **stageKeys** *(list) --* 

              A list of  Stage resources that are associated with the  ApiKey resource.

              
              

              - *(string) --* 
          
        
      
    

  .. py:method:: get_authorizer(**kwargs)

    

    Describe an existing  Authorizer resource.

     `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-authorizer.html>`__ 

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.get_authorizer(
          restApiId='string',
          authorizerId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type authorizerId: string
    :param authorizerId: **[REQUIRED]** 

      The identifier of the  Authorizer resource.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
            'providerARNs': [
                'string',
            ],
            'authType': 'string',
            'authorizerUri': 'string',
            'authorizerCredentials': 'string',
            'identitySource': 'string',
            'identityValidationExpression': 'string',
            'authorizerResultTtlInSeconds': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an authorization layer for methods. If enabled on a method, API Gateway will activate the authorizer when a client calls the method.

          `Enable custom authorization <http://docs.aws.amazon.com/apigateway/latest/developerguide/use-custom-authorizer.html>`__  
        

        - **id** *(string) --* 

          The identifier for the authorizer resource.

          
        

        - **name** *(string) --* 

          [Required] The name of the authorizer.

          
        

        - **type** *(string) --* 

          [Required] The authorizer type. Valid values are ``TOKEN`` for a Lambda function using a single authorization token submitted in a custom header, ``REQUEST`` for a Lambda function using incoming request parameters, and ``COGNITO_USER_POOLS`` for using an Amazon Cognito user pool.

          
        

        - **providerARNs** *(list) --* 

          A list of the Amazon Cognito user pool ARNs for the ``COGNITO_USER_POOLS`` authorizer. Each element is of this format: ``arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`` . For a ``TOKEN`` or ``REQUEST`` authorizer, this is not defined. 

          
          

          - *(string) --* 
      
        

        - **authType** *(string) --* 

          Optional customer-defined field, used in Swagger imports and exports without functional impact.

          
        

        - **authorizerUri** *(string) --* 

          Specifies the authorizer's Uniform Resource Identifier (URI). For ``TOKEN`` or ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations`` . In general, the URI has this form ``arn:aws:apigateway:{region}:lambda:path/{service_api}`` , where ``{region}`` is the same as the region hosting the Lambda function, ``path`` indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``/`` . For Lambda functions, this is usually of the form ``/2015-03-31/functions/[FunctionARN]/invocations`` .

          
        

        - **authorizerCredentials** *(string) --* 

          Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.

          
        

        - **identitySource** *(string) --* 

          The identity source for which authorization is requested. 

          
          * For a ``TOKEN`` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is ``Auth`` , the header mapping expression is ``method.request.header.Auth`` .
          
          * For the ``REQUEST`` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an ``Auth`` header, a ``Name`` query string parameter are defined as identity sources, this value is ``method.request.header.Auth, method.request.querystring.Name`` . These parameters will be used to derive the authorization caching key and to perform runtime validation of the ``REQUEST`` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
          
          * For a ``COGNITO_USER_POOLS`` authorizer, this property is not used.
          

          

          
        

        - **identityValidationExpression** *(string) --* 

          A validation expression for the incoming identity token. For ``TOKEN`` authorizers, this value is a regular expression. API Gateway will match the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the ``REQUEST`` authorizer.

          
        

        - **authorizerResultTtlInSeconds** *(integer) --* 

          The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.

          
    

  .. py:method:: get_authorizers(**kwargs)

    

    Describe an existing  Authorizers resource.

     `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-authorizers.html>`__ 

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetAuthorizers>`_    


    **Request Syntax** 
    ::

      response = client.get_authorizers(
          restApiId='string',
          position='string',
          limit=123
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
                    'providerARNs': [
                        'string',
                    ],
                    'authType': 'string',
                    'authorizerUri': 'string',
                    'authorizerCredentials': 'string',
                    'identitySource': 'string',
                    'identityValidationExpression': 'string',
                    'authorizerResultTtlInSeconds': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  Authorizer resources.

          `Enable custom authorization <http://docs.aws.amazon.com/apigateway/latest/developerguide/use-custom-authorizer.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents an authorization layer for methods. If enabled on a method, API Gateway will activate the authorizer when a client calls the method.

              `Enable custom authorization <http://docs.aws.amazon.com/apigateway/latest/developerguide/use-custom-authorizer.html>`__  
            

            - **id** *(string) --* 

              The identifier for the authorizer resource.

              
            

            - **name** *(string) --* 

              [Required] The name of the authorizer.

              
            

            - **type** *(string) --* 

              [Required] The authorizer type. Valid values are ``TOKEN`` for a Lambda function using a single authorization token submitted in a custom header, ``REQUEST`` for a Lambda function using incoming request parameters, and ``COGNITO_USER_POOLS`` for using an Amazon Cognito user pool.

              
            

            - **providerARNs** *(list) --* 

              A list of the Amazon Cognito user pool ARNs for the ``COGNITO_USER_POOLS`` authorizer. Each element is of this format: ``arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`` . For a ``TOKEN`` or ``REQUEST`` authorizer, this is not defined. 

              
              

              - *(string) --* 
          
            

            - **authType** *(string) --* 

              Optional customer-defined field, used in Swagger imports and exports without functional impact.

              
            

            - **authorizerUri** *(string) --* 

              Specifies the authorizer's Uniform Resource Identifier (URI). For ``TOKEN`` or ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations`` . In general, the URI has this form ``arn:aws:apigateway:{region}:lambda:path/{service_api}`` , where ``{region}`` is the same as the region hosting the Lambda function, ``path`` indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``/`` . For Lambda functions, this is usually of the form ``/2015-03-31/functions/[FunctionARN]/invocations`` .

              
            

            - **authorizerCredentials** *(string) --* 

              Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.

              
            

            - **identitySource** *(string) --* 

              The identity source for which authorization is requested. 

              
              * For a ``TOKEN`` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is ``Auth`` , the header mapping expression is ``method.request.header.Auth`` .
              
              * For the ``REQUEST`` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an ``Auth`` header, a ``Name`` query string parameter are defined as identity sources, this value is ``method.request.header.Auth, method.request.querystring.Name`` . These parameters will be used to derive the authorization caching key and to perform runtime validation of the ``REQUEST`` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
              
              * For a ``COGNITO_USER_POOLS`` authorizer, this property is not used.
              

              

              
            

            - **identityValidationExpression** *(string) --* 

              A validation expression for the incoming identity token. For ``TOKEN`` authorizers, this value is a regular expression. API Gateway will match the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the ``REQUEST`` authorizer.

              
            

            - **authorizerResultTtlInSeconds** *(integer) --* 

              The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.

              
        
      
    

  .. py:method:: get_base_path_mapping(**kwargs)

    

    Describe a  BasePathMapping resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetBasePathMapping>`_    


    **Request Syntax** 
    ::

      response = client.get_base_path_mapping(
          domainName='string',
          basePath='string'
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name of the  BasePathMapping resource to be described.

      

    
    :type basePath: string
    :param basePath: **[REQUIRED]** 

      The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify any base path name after the domain name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'basePath': 'string',
            'restApiId': 'string',
            'stage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the base path that callers of the API must provide as part of the URL after the domain name.

         A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi in a given stage of the owner  Account .  `Use Custom Domain Names <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **basePath** *(string) --* 

          The base path name that callers of the API must provide as part of the URL after the domain name.

          
        

        - **restApiId** *(string) --* 

          The string identifier of the associated  RestApi .

          
        

        - **stage** *(string) --* 

          The name of the associated stage.

          
    

  .. py:method:: get_base_path_mappings(**kwargs)

    

    Represents a collection of  BasePathMapping resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetBasePathMappings>`_    


    **Request Syntax** 
    ::

      response = client.get_base_path_mappings(
          domainName='string',
          position='string',
          limit=123
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name of a  BasePathMapping resource.

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'basePath': 'string',
                    'restApiId': 'string',
                    'stage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  BasePathMapping resources.

          `Use Custom Domain Names <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents the base path that callers of the API must provide as part of the URL after the domain name.

             A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi in a given stage of the owner  Account .  `Use Custom Domain Names <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
            

            - **basePath** *(string) --* 

              The base path name that callers of the API must provide as part of the URL after the domain name.

              
            

            - **restApiId** *(string) --* 

              The string identifier of the associated  RestApi .

              
            

            - **stage** *(string) --* 

              The name of the associated stage.

              
        
      
    

  .. py:method:: get_client_certificate(**kwargs)

    

    Gets information about the current  ClientCertificate resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetClientCertificate>`_    


    **Request Syntax** 
    ::

      response = client.get_client_certificate(
          clientCertificateId='string'
      )
    :type clientCertificateId: string
    :param clientCertificateId: **[REQUIRED]** 

      The identifier of the  ClientCertificate resource to be described.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'clientCertificateId': 'string',
            'description': 'string',
            'pemEncodedCertificate': 'string',
            'createdDate': datetime(2015, 1, 1),
            'expirationDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a client certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.

         Client certificates are used to authenticate an API by the backend server. To authenticate an API client (or user), use IAM roles and policies, a custom  Authorizer or an Amazon Cognito user pool.  `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__  
        

        - **clientCertificateId** *(string) --* 

          The identifier of the client certificate.

          
        

        - **description** *(string) --* 

          The description of the client certificate.

          
        

        - **pemEncodedCertificate** *(string) --* 

          The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the client certificate was created.

          
        

        - **expirationDate** *(datetime) --* 

          The timestamp when the client certificate will expire.

          
    

  .. py:method:: get_client_certificates(**kwargs)

    

    Gets a collection of  ClientCertificate resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetClientCertificates>`_    


    **Request Syntax** 
    ::

      response = client.get_client_certificates(
          position='string',
          limit=123
      )
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'clientCertificateId': 'string',
                    'description': 'string',
                    'pemEncodedCertificate': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'expirationDate': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  ClientCertificate resources.

          `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a client certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.

             Client certificates are used to authenticate an API by the backend server. To authenticate an API client (or user), use IAM roles and policies, a custom  Authorizer or an Amazon Cognito user pool.  `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__  
            

            - **clientCertificateId** *(string) --* 

              The identifier of the client certificate.

              
            

            - **description** *(string) --* 

              The description of the client certificate.

              
            

            - **pemEncodedCertificate** *(string) --* 

              The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .

              
            

            - **createdDate** *(datetime) --* 

              The timestamp when the client certificate was created.

              
            

            - **expirationDate** *(datetime) --* 

              The timestamp when the client certificate will expire.

              
        
      
    

  .. py:method:: get_deployment(**kwargs)

    

    Gets information about a  Deployment resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDeployment>`_    


    **Request Syntax** 
    ::

      response = client.get_deployment(
          restApiId='string',
          deploymentId='string',
          embed=[
              'string',
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      The identifier of the  Deployment resource to get information about.

      

    
    :type embed: list
    :param embed: 

      A query parameter to retrieve the specified embedded resources of the returned  Deployment resource in the response. In a REST API call, this ``embed`` parameter value is a list of comma-separated strings, as in ``GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=var1,var2`` . The SDK and other platform-dependent libraries might use a different format for the list. Currently, this request supports only retrieval of the embedded API summary this way. Hence, the parameter value must be a single-valued list containing only the ``"apisummary"`` string. For example, ``GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=apisummary`` .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'apiSummary': {
                'string': {
                    'string': {
                        'authorizationType': 'string',
                        'apiKeyRequired': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        An immutable representation of a  RestApi resource that can be called by users using  Stages . A deployment must be associated with a  Stage for it to be callable over the Internet.

         To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,  Deployments ,  Stage , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS SDKs <https://aws.amazon.com/tools/>`__  
        

        - **id** *(string) --* 

          The identifier for the deployment resource.

          
        

        - **description** *(string) --* 

          The description for the deployment resource.

          
        

        - **createdDate** *(datetime) --* 

          The date and time that the deployment resource was created.

          
        

        - **apiSummary** *(dict) --* 

          A summary of the  RestApi at the date and time that the deployment resource was created.

          
          

          - *(string) --* 
            

            - *(dict) --* 
              

              - *(string) --* 
                

                - *(dict) --* 

                  Represents a summary of a  Method resource, given a particular date and time.

                  
                  

                  - **authorizationType** *(string) --* 

                    The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                    
                  

                  - **apiKeyRequired** *(boolean) --* 

                    Specifies whether the method requires a valid  ApiKey .

                    
              
          
        
      
    
    

  .. py:method:: get_deployments(**kwargs)

    

    Gets information about a  Deployments collection.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDeployments>`_    


    **Request Syntax** 
    ::

      response = client.get_deployments(
          restApiId='string',
          position='string',
          limit=123
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'description': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'apiSummary': {
                        'string': {
                            'string': {
                                'authorizationType': 'string',
                                'apiKeyRequired': True|False
                            }
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection resource that contains zero or more references to your existing deployments, and links that guide you on how to interact with your collection. The collection offers a paginated view of the contained deployments.

         To create a new deployment of a  RestApi , make a ``POST`` request against this resource. To view, update, or delete an existing deployment, make a ``GET`` , ``PATCH`` , or ``DELETE`` request, respectively, on a specified  Deployment resource.  `Deploying an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__ , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS SDKs <https://aws.amazon.com/tools/>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            An immutable representation of a  RestApi resource that can be called by users using  Stages . A deployment must be associated with a  Stage for it to be callable over the Internet.

             To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,  Deployments ,  Stage , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS SDKs <https://aws.amazon.com/tools/>`__  
            

            - **id** *(string) --* 

              The identifier for the deployment resource.

              
            

            - **description** *(string) --* 

              The description for the deployment resource.

              
            

            - **createdDate** *(datetime) --* 

              The date and time that the deployment resource was created.

              
            

            - **apiSummary** *(dict) --* 

              A summary of the  RestApi at the date and time that the deployment resource was created.

              
              

              - *(string) --* 
                

                - *(dict) --* 
                  

                  - *(string) --* 
                    

                    - *(dict) --* 

                      Represents a summary of a  Method resource, given a particular date and time.

                      
                      

                      - **authorizationType** *(string) --* 

                        The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                        
                      

                      - **apiKeyRequired** *(boolean) --* 

                        Specifies whether the method requires a valid  ApiKey .

                        
                  
              
            
          
        
        
      
    

  .. py:method:: get_documentation_part(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDocumentationPart>`_    


    **Request Syntax** 
    ::

      response = client.get_documentation_part(
          restApiId='string',
          documentationPartId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type documentationPartId: string
    :param documentationPartId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'location': {
                'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
                'path': 'string',
                'method': 'string',
                'statusCode': 'string',
                'name': 'string'
            },
            'properties': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A documentation part for a targeted API entity.

          

        A documentation part consists of a content map (``properties`` ) and a target (``location`` ). The target specifies an API entity to which the documentation content applies. The supported API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend on the API entity type. All valid fields are not required.

         

        The content map is a JSON string of API-specific key-value pairs. Although an API can use any shape for the content map, only the Swagger-compliant documentation fields will be injected into the associated API entity definition in the exported Swagger definition file.

          `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationParts  
        

        - **id** *(string) --* 

          The  DocumentationPart identifier, generated by API Gateway when the ``DocumentationPart`` is created.

          
        

        - **location** *(dict) --* 

          The location of the API entity to which the documentation applies. Valid fields depend on the targeted API entity type. All the valid location fields are not required. If not explicitly specified, a valid location field is treated as a wildcard and associated documentation content may be inherited by matching entities, unless overridden.

          
          

          - **type** *(string) --* 

            The type of API entity to which the documentation content applies. It is a valid and required field for API entity types of ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or ``RESOURCE`` type.

            
          

          - **path** *(string) --* 

            The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an applicable child entity inherits the content of another entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``path`` attribute must match that of the parent entity as a prefix.

            
          

          - **method** *(string) --* 

            The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any method. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``method`` attribute must match that of the parent entity exactly.

            
          

          - **statusCode** *(string) --* 

            The HTTP status code of a response. It is a valid field for the API entity types of ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any status code. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``statusCode`` attribute must match that of the parent entity exactly.

            
          

          - **name** *(string) --* 

            The name of the targeted API entity. It is a valid and required field for the API entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for any other entity type.

            
      
        

        - **properties** *(string) --* 

          A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., ``"{ \"description\": \"The API does ...\" }"`` . Only Swagger-compliant documentation-related fields from the propertiesmap are exported and, hence, published as part of the API entity definitions, while the original documentation parts are exported in a Swagger extension of ``x-amazon-apigateway-documentation`` .

          
    

  .. py:method:: get_documentation_parts(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDocumentationParts>`_    


    **Request Syntax** 
    ::

      response = client.get_documentation_parts(
          restApiId='string',
          type='API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
          nameQuery='string',
          path='string',
          position='string',
          limit=123,
          locationStatus='DOCUMENTED'|'UNDOCUMENTED'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type type: string
    :param type: 

      The type of API entities of the to-be-retrieved documentation parts. 

      

    
    :type nameQuery: string
    :param nameQuery: 

      The name of API entities of the to-be-retrieved documentation parts.

      

    
    :type path: string
    :param path: 

      The path of API entities of the to-be-retrieved documentation parts.

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    :type locationStatus: string
    :param locationStatus: 

      The status of the API documentation parts to retrieve. Valid values are ``DOCUMENTED`` for retrieving  DocumentationPart resources with content and ``UNDOCUMENTED`` for  DocumentationPart resources without content.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'location': {
                        'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
                        'path': 'string',
                        'method': 'string',
                        'statusCode': 'string',
                        'name': 'string'
                    },
                    'properties': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The collection of documentation parts of an API.

           `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationPart  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            A documentation part for a targeted API entity.

              

            A documentation part consists of a content map (``properties`` ) and a target (``location`` ). The target specifies an API entity to which the documentation content applies. The supported API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend on the API entity type. All valid fields are not required.

             

            The content map is a JSON string of API-specific key-value pairs. Although an API can use any shape for the content map, only the Swagger-compliant documentation fields will be injected into the associated API entity definition in the exported Swagger definition file.

              `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationParts  
            

            - **id** *(string) --* 

              The  DocumentationPart identifier, generated by API Gateway when the ``DocumentationPart`` is created.

              
            

            - **location** *(dict) --* 

              The location of the API entity to which the documentation applies. Valid fields depend on the targeted API entity type. All the valid location fields are not required. If not explicitly specified, a valid location field is treated as a wildcard and associated documentation content may be inherited by matching entities, unless overridden.

              
              

              - **type** *(string) --* 

                The type of API entity to which the documentation content applies. It is a valid and required field for API entity types of ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or ``RESOURCE`` type.

                
              

              - **path** *(string) --* 

                The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an applicable child entity inherits the content of another entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``path`` attribute must match that of the parent entity as a prefix.

                
              

              - **method** *(string) --* 

                The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any method. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``method`` attribute must match that of the parent entity exactly.

                
              

              - **statusCode** *(string) --* 

                The HTTP status code of a response. It is a valid field for the API entity types of ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any status code. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``statusCode`` attribute must match that of the parent entity exactly.

                
              

              - **name** *(string) --* 

                The name of the targeted API entity. It is a valid and required field for the API entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for any other entity type.

                
          
            

            - **properties** *(string) --* 

              A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., ``"{ \"description\": \"The API does ...\" }"`` . Only Swagger-compliant documentation-related fields from the propertiesmap are exported and, hence, published as part of the API entity definitions, while the original documentation parts are exported in a Swagger extension of ``x-amazon-apigateway-documentation`` .

              
        
      
    

  .. py:method:: get_documentation_version(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDocumentationVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_documentation_version(
          restApiId='string',
          documentationVersion='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type documentationVersion: string
    :param documentationVersion: **[REQUIRED]** 

      [Required] The version identifier of the to-be-retrieved documentation snapshot.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'version': 'string',
            'createdDate': datetime(2015, 1, 1),
            'description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A snapshot of the documentation of an API.

         

        Publishing API documentation involves creating a documentation version associated with an API stage and exporting the versioned documentation to an external (e.g., Swagger) file.

          `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationPart ,  DocumentationVersions  
        

        - **version** *(string) --* 

          The version identifier of the API documentation snapshot.

          
        

        - **createdDate** *(datetime) --* 

          The date when the API documentation snapshot is created.

          
        

        - **description** *(string) --* 

          The description of the API documentation snapshot.

          
    

  .. py:method:: get_documentation_versions(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDocumentationVersions>`_    


    **Request Syntax** 
    ::

      response = client.get_documentation_versions(
          restApiId='string',
          position='string',
          limit=123
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'version': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'description': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The collection of documentation snapshots of an API. 

         

        Use the  DocumentationVersions to manage documentation snapshots associated with various API stages.

          `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationPart ,  DocumentationVersion  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            A snapshot of the documentation of an API.

             

            Publishing API documentation involves creating a documentation version associated with an API stage and exporting the versioned documentation to an external (e.g., Swagger) file.

              `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationPart ,  DocumentationVersions  
            

            - **version** *(string) --* 

              The version identifier of the API documentation snapshot.

              
            

            - **createdDate** *(datetime) --* 

              The date when the API documentation snapshot is created.

              
            

            - **description** *(string) --* 

              The description of the API documentation snapshot.

              
        
      
    

  .. py:method:: get_domain_name(**kwargs)

    

    Represents a domain name that is contained in a simpler, more intuitive URL that can be called.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDomainName>`_    


    **Request Syntax** 
    ::

      response = client.get_domain_name(
          domainName='string'
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The name of the  DomainName resource.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'domainName': 'string',
            'certificateName': 'string',
            'certificateArn': 'string',
            'certificateUploadDate': datetime(2015, 1, 1),
            'regionalDomainName': 'string',
            'regionalHostedZoneId': 'string',
            'regionalCertificateName': 'string',
            'regionalCertificateArn': 'string',
            'distributionDomainName': 'string',
            'distributionHostedZoneId': 'string',
            'endpointConfiguration': {
                'types': [
                    'REGIONAL'|'EDGE',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

          

        When you deploy an API, API Gateway creates a default host name for the API. This default API host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the default host name, you can access the API's root resource with the URL of ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a custom domain name of ``apis.example.com`` for this API, you can then access the same resource using the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path mapping ( BasePathMapping ) of your API under the custom domain name. 

           `Set a Custom Host Name for an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **domainName** *(string) --* 

          The name of the  DomainName resource.

          
        

        - **certificateName** *(string) --* 

          The name of the certificate that will be used by edge-optimized endpoint for this domain name.

          
        

        - **certificateArn** *(string) --* 

          The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

          
        

        - **certificateUploadDate** *(datetime) --* 

          The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

          
        

        - **regionalDomainName** *(string) --* 

          The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.

          
        

        - **regionalHostedZoneId** *(string) --* 

          The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

          
        

        - **regionalCertificateName** *(string) --* 

          The name of the certificate that will be used for validating the regional domain name.

          
        

        - **regionalCertificateArn** *(string) --* 

          The reference to an AWS-managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.

          
        

        - **distributionDomainName** *(string) --* 

          The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the `Amazon CloudFront documentation <http://aws.amazon.com/documentation/cloudfront/>`__ .

          
        

        - **distributionHostedZoneId** *(string) --* 

          The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is ``Z2FDTNDATAQYW2`` for all the regions. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

          
        

        - **endpointConfiguration** *(dict) --* 

          The endpoint configuration of this  DomainName showing the endpoint types of the domain name. 

          
          

          - **types** *(list) --* 

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

            
            

            - *(string) --* 

              The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

              
        
      
    

  .. py:method:: get_domain_names(**kwargs)

    

    Represents a collection of  DomainName resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDomainNames>`_    


    **Request Syntax** 
    ::

      response = client.get_domain_names(
          position='string',
          limit=123
      )
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'domainName': 'string',
                    'certificateName': 'string',
                    'certificateArn': 'string',
                    'certificateUploadDate': datetime(2015, 1, 1),
                    'regionalDomainName': 'string',
                    'regionalHostedZoneId': 'string',
                    'regionalCertificateName': 'string',
                    'regionalCertificateArn': 'string',
                    'distributionDomainName': 'string',
                    'distributionHostedZoneId': 'string',
                    'endpointConfiguration': {
                        'types': [
                            'REGIONAL'|'EDGE',
                        ]
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  DomainName resources.

          `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

              

            When you deploy an API, API Gateway creates a default host name for the API. This default API host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the default host name, you can access the API's root resource with the URL of ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a custom domain name of ``apis.example.com`` for this API, you can then access the same resource using the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path mapping ( BasePathMapping ) of your API under the custom domain name. 

               `Set a Custom Host Name for an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
            

            - **domainName** *(string) --* 

              The name of the  DomainName resource.

              
            

            - **certificateName** *(string) --* 

              The name of the certificate that will be used by edge-optimized endpoint for this domain name.

              
            

            - **certificateArn** *(string) --* 

              The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

              
            

            - **certificateUploadDate** *(datetime) --* 

              The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

              
            

            - **regionalDomainName** *(string) --* 

              The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.

              
            

            - **regionalHostedZoneId** *(string) --* 

              The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

              
            

            - **regionalCertificateName** *(string) --* 

              The name of the certificate that will be used for validating the regional domain name.

              
            

            - **regionalCertificateArn** *(string) --* 

              The reference to an AWS-managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.

              
            

            - **distributionDomainName** *(string) --* 

              The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the `Amazon CloudFront documentation <http://aws.amazon.com/documentation/cloudfront/>`__ .

              
            

            - **distributionHostedZoneId** *(string) --* 

              The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is ``Z2FDTNDATAQYW2`` for all the regions. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

              
            

            - **endpointConfiguration** *(dict) --* 

              The endpoint configuration of this  DomainName showing the endpoint types of the domain name. 

              
              

              - **types** *(list) --* 

                A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

                
                

                - *(string) --* 

                  The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

                  
            
          
        
      
    

  .. py:method:: get_export(**kwargs)

    

    Exports a deployed version of a  RestApi in a specified format.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetExport>`_    


    **Request Syntax** 
    ::

      response = client.get_export(
          restApiId='string',
          stageName='string',
          exportType='string',
          parameters={
              'string': 'string'
          },
          accepts='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: **[REQUIRED]** 

      The name of the  Stage that will be exported.

      

    
    :type exportType: string
    :param exportType: **[REQUIRED]** 

      The type of export. Currently only 'swagger' is supported.

      

    
    :type parameters: dict
    :param parameters: 

      A key-value map of query string parameters that specify properties of the export, depending on the requested ``exportType`` . For ``exportType``  ``swagger`` , any combination of the following parameters are supported: ``integrations`` will export the API with x-amazon-apigateway-integration extensions. ``authorizers`` will export the API with x-amazon-apigateway-authorizer extensions. ``postman`` will export the API with Postman extensions, allowing for import to the Postman tool

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type accepts: string
    :param accepts: 

      The content-type of the export, for example ``application/json`` . Currently ``application/json`` and ``application/yaml`` are supported for ``exportType`` of ``swagger`` . This should be specified in the ``Accept`` header for direct API requests.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'contentType': 'string',
            'contentDisposition': 'string',
            'body': StreamingBody()
        }
      **Response Structure** 

      

      - *(dict) --* 

        The binary blob response to  GetExport , which contains the generated SDK.

        
        

        - **contentType** *(string) --* 

          The content-type header value in the HTTP response. This will correspond to a valid 'accept' type in the request.

          
        

        - **contentDisposition** *(string) --* 

          The content-disposition header value in the HTTP response.

          
        

        - **body** (:class:`.StreamingBody`) -- 

          The binary blob response to  GetExport , which contains the export.

          
    

  .. py:method:: get_gateway_response(**kwargs)

    

    Gets a  GatewayResponse of a specified response type on the given  RestApi .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetGatewayResponse>`_    


    **Request Syntax** 
    ::

      response = client.get_gateway_response(
          restApiId='string',
          responseType='DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type responseType: string
    :param responseType: **[REQUIRED]** 

      

      The response type of the associated  GatewayResponse . Valid values are 

      
      * ACCESS_DENIED
      
      * API_CONFIGURATION_ERROR
      
      * AUTHORIZER_FAILURE
      
      * AUTHORIZER_CONFIGURATION_ERROR
      
      * BAD_REQUEST_PARAMETERS
      
      * BAD_REQUEST_BODY
      
      * DEFAULT_4XX
      
      * DEFAULT_5XX
      
      * EXPIRED_TOKEN
      
      * INVALID_SIGNATURE
      
      * INTEGRATION_FAILURE
      
      * INTEGRATION_TIMEOUT
      
      * INVALID_API_KEY
      
      * MISSING_AUTHENTICATION_TOKEN
      
      * QUOTA_EXCEEDED
      
      * REQUEST_TOO_LARGE
      
      * RESOURCE_NOT_FOUND
      
      * THROTTLED
      
      * UNAUTHORIZED
      
      * UNSUPPORTED_MEDIA_TYPES
      

       

      

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'responseType': 'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
            'statusCode': 'string',
            'responseParameters': {
                'string': 'string'
            },
            'responseTemplates': {
                'string': 'string'
            },
            'defaultResponse': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        A gateway response of a given response type and status code, with optional response parameters and mapping templates.

         For more information about valid gateway response types, see `Gateway Response Types Supported by API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__   Example: Get a Gateway Response of a given response type Request 

        This example shows how to get a gateway response of the ``MISSING_AUTHNETICATION_TOKEN`` type.

         ``GET /restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN HTTP/1.1 Host: beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json X-Amz-Date: 20170503T202516Z Authorization: AWS4-HMAC-SHA256 Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=1b52460e3159c1a26cff29093855d50ea141c1c5b937528fecaf60f51129697a Cache-Control: no-cache Postman-Token: 3b2a1ce9-c848-2e26-2e2f-9c2caefbed45``  

        The response type is specified as a URL path.

         Response 

        The successful operation returns the ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html", "name": "gatewayresponse", "templated": true }, "self": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:delete": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } }, "defaultResponse": false, "responseParameters": { "gatewayresponse.header.x-request-path": "method.request.path.petId", "gatewayresponse.header.Access-Control-Allow-Origin": "'a.b.c'", "gatewayresponse.header.x-request-query": "method.request.querystring.q", "gatewayresponse.header.x-request-header": "method.request.header.Accept" }, "responseTemplates": { "application/json": "{\n \"message\": $context.error.messageString,\n \"type\": \"$context.error.responseType\",\n \"stage\": \"$context.stage\",\n \"resourcePath\": \"$context.resourcePath\",\n \"stageVariables.a\": \"$stageVariables.a\",\n \"statusCode\": \"'404'\"\n}" }, "responseType": "MISSING_AUTHENTICATION_TOKEN", "statusCode": "404" }``  

        

            `Customize Gateway Responses <http://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html>`__  
        

        - **responseType** *(string) --* 

          The response type of the associated  GatewayResponse . Valid values are 

          
          * ACCESS_DENIED
          
          * API_CONFIGURATION_ERROR
          
          * AUTHORIZER_FAILURE
          
          * AUTHORIZER_CONFIGURATION_ERROR
          
          * BAD_REQUEST_PARAMETERS
          
          * BAD_REQUEST_BODY
          
          * DEFAULT_4XX
          
          * DEFAULT_5XX
          
          * EXPIRED_TOKEN
          
          * INVALID_SIGNATURE
          
          * INTEGRATION_FAILURE
          
          * INTEGRATION_TIMEOUT
          
          * INVALID_API_KEY
          
          * MISSING_AUTHENTICATION_TOKEN
          
          * QUOTA_EXCEEDED
          
          * REQUEST_TOO_LARGE
          
          * RESOURCE_NOT_FOUND
          
          * THROTTLED
          
          * UNAUTHORIZED
          
          * UNSUPPORTED_MEDIA_TYPES
          

           

          
        

        - **statusCode** *(string) --* 

          The HTTP status code for this  GatewayResponse .

          
        

        - **responseParameters** *(dict) --* 

          Response parameters (paths, query strings and headers) of the  GatewayResponse as a string-to-string map of key-value pairs.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **responseTemplates** *(dict) --* 

          Response templates of the  GatewayResponse as a string-to-string map of key-value pairs.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **defaultResponse** *(boolean) --* 

          A Boolean flag to indicate whether this  GatewayResponse is the default gateway response (``true`` ) or not (``false`` ). A default gateway response is one generated by API Gateway without any customization by an API developer. 

          
    

  .. py:method:: get_gateway_responses(**kwargs)

    

    Gets the  GatewayResponses collection on the given  RestApi . If an API developer has not added any definitions for gateway responses, the result will be the API Gateway-generated default  GatewayResponses collection for the supported response types.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetGatewayResponses>`_    


    **Request Syntax** 
    ::

      response = client.get_gateway_responses(
          restApiId='string',
          position='string',
          limit=123
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set. The  GatewayResponse collection does not support pagination and the position does not apply here.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page. The  GatewayResponses collection does not support pagination and the limit does not apply here.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'responseType': 'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
                    'statusCode': 'string',
                    'responseParameters': {
                        'string': 'string'
                    },
                    'responseTemplates': {
                        'string': 'string'
                    },
                    'defaultResponse': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The collection of the  GatewayResponse instances of a  RestApi as a ``responseType`` -to- GatewayResponse object map of key-value pairs. As such, pagination is not supported for querying this collection.

         For more information about valid gateway response types, see `Gateway Response Types Supported by API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__   Example: Get the collection of gateway responses of an API Request 

        This example request shows how to retrieve the  GatewayResponses collection from an API.

         ``GET /restapis/o81lxisefl/gatewayresponses HTTP/1.1 Host: beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json X-Amz-Date: 20170503T220604Z Authorization: AWS4-HMAC-SHA256 Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=59b42fe54a76a5de8adf2c67baa6d39206f8e9ad49a1d77ccc6a5da3103a398a Cache-Control: no-cache Postman-Token: 5637af27-dc29-fc5c-9dfe-0645d52cb515``  

        

         Response 

        The successful operation returns the ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html", "name": "gatewayresponse", "templated": true }, "self": { "href": "/restapis/o81lxisefl/gatewayresponses" }, "first": { "href": "/restapis/o81lxisefl/gatewayresponses" }, "gatewayresponse:by-type": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "item": [ { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" }, { "href": "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" }, { "href": "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" }, { "href": "/restapis/o81lxisefl/gatewayresponses/THROTTLED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" }, { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" }, { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX" }, { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX" }, { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" }, { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" }, { "href": "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" }, { "href": "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" }, { "href": "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" }, { "href": "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" }, { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" }, { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" } ] }, "_embedded": { "item": [ { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "INTEGRATION_FAILURE", "statusCode": "504" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "RESOURCE_NOT_FOUND", "statusCode": "404" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "REQUEST_TOO_LARGE", "statusCode": "413" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/THROTTLED" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/THROTTLED" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "THROTTLED", "statusCode": "429" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "UNSUPPORTED_MEDIA_TYPE", "statusCode": "415" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "AUTHORIZER_CONFIGURATION_ERROR", "statusCode": "500" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "DEFAULT_5XX" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "DEFAULT_4XX" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "BAD_REQUEST_PARAMETERS", "statusCode": "400" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "BAD_REQUEST_BODY", "statusCode": "400" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "EXPIRED_TOKEN", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "ACCESS_DENIED", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "INVALID_API_KEY", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "UNAUTHORIZED", "statusCode": "401" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "API_CONFIGURATION_ERROR", "statusCode": "500" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "QUOTA_EXCEEDED", "statusCode": "429" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "INTEGRATION_TIMEOUT", "statusCode": "504" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "MISSING_AUTHENTICATION_TOKEN", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "INVALID_SIGNATURE", "statusCode": "403" }, { "_links": { "self": { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": { "application/json": "{\"message\":$context.error.messageString}" }, "responseType": "AUTHORIZER_FAILURE", "statusCode": "500" } ] } }``  

        

            `Customize Gateway Responses <http://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          Returns the entire collection, because of no pagination support.

          
          

          - *(dict) --* 

            A gateway response of a given response type and status code, with optional response parameters and mapping templates.

             For more information about valid gateway response types, see `Gateway Response Types Supported by API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__   Example: Get a Gateway Response of a given response type Request 

            This example shows how to get a gateway response of the ``MISSING_AUTHNETICATION_TOKEN`` type.

             ``GET /restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN HTTP/1.1 Host: beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json X-Amz-Date: 20170503T202516Z Authorization: AWS4-HMAC-SHA256 Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=1b52460e3159c1a26cff29093855d50ea141c1c5b937528fecaf60f51129697a Cache-Control: no-cache Postman-Token: 3b2a1ce9-c848-2e26-2e2f-9c2caefbed45``  

            The response type is specified as a URL path.

             Response 

            The successful operation returns the ``200 OK`` status code and a payload similar to the following:

             ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html", "name": "gatewayresponse", "templated": true }, "self": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:delete": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } }, "defaultResponse": false, "responseParameters": { "gatewayresponse.header.x-request-path": "method.request.path.petId", "gatewayresponse.header.Access-Control-Allow-Origin": "'a.b.c'", "gatewayresponse.header.x-request-query": "method.request.querystring.q", "gatewayresponse.header.x-request-header": "method.request.header.Accept" }, "responseTemplates": { "application/json": "{\n \"message\": $context.error.messageString,\n \"type\": \"$context.error.responseType\",\n \"stage\": \"$context.stage\",\n \"resourcePath\": \"$context.resourcePath\",\n \"stageVariables.a\": \"$stageVariables.a\",\n \"statusCode\": \"'404'\"\n}" }, "responseType": "MISSING_AUTHENTICATION_TOKEN", "statusCode": "404" }``  

            

                `Customize Gateway Responses <http://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html>`__  
            

            - **responseType** *(string) --* 

              The response type of the associated  GatewayResponse . Valid values are 

              
              * ACCESS_DENIED
              
              * API_CONFIGURATION_ERROR
              
              * AUTHORIZER_FAILURE
              
              * AUTHORIZER_CONFIGURATION_ERROR
              
              * BAD_REQUEST_PARAMETERS
              
              * BAD_REQUEST_BODY
              
              * DEFAULT_4XX
              
              * DEFAULT_5XX
              
              * EXPIRED_TOKEN
              
              * INVALID_SIGNATURE
              
              * INTEGRATION_FAILURE
              
              * INTEGRATION_TIMEOUT
              
              * INVALID_API_KEY
              
              * MISSING_AUTHENTICATION_TOKEN
              
              * QUOTA_EXCEEDED
              
              * REQUEST_TOO_LARGE
              
              * RESOURCE_NOT_FOUND
              
              * THROTTLED
              
              * UNAUTHORIZED
              
              * UNSUPPORTED_MEDIA_TYPES
              

               

              
            

            - **statusCode** *(string) --* 

              The HTTP status code for this  GatewayResponse .

              
            

            - **responseParameters** *(dict) --* 

              Response parameters (paths, query strings and headers) of the  GatewayResponse as a string-to-string map of key-value pairs.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **responseTemplates** *(dict) --* 

              Response templates of the  GatewayResponse as a string-to-string map of key-value pairs.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **defaultResponse** *(boolean) --* 

              A Boolean flag to indicate whether this  GatewayResponse is the default gateway response (``true`` ) or not (``false`` ). A default gateway response is one generated by API Gateway without any customization by an API developer. 

              
        
      
    

  .. py:method:: get_integration(**kwargs)

    

    Get the integration settings.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetIntegration>`_    


    **Request Syntax** 
    ::

      response = client.get_integration(
          restApiId='string',
          resourceId='string',
          httpMethod='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Specifies a get integration request's resource identifier

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies a get integration request's HTTP method.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
            'httpMethod': 'string',
            'uri': 'string',
            'connectionType': 'INTERNET'|'VPC_LINK',
            'connectionId': 'string',
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
            'timeoutInMillis': 123,
            'cacheNamespace': 'string',
            'cacheKeyParameters': [
                'string',
            ],
            'integrationResponses': {
                'string': {
                    'statusCode': 'string',
                    'selectionPattern': 'string',
                    'responseParameters': {
                        'string': 'string'
                    },
                    'responseTemplates': {
                        'string': 'string'
                    },
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

         In the API Gateway console, the built-in Lambda integration is an AWS integration.  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **type** *(string) --* 

          Specifies an API method integration type. The valid value is one of the following:

           

           
          * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
           
          * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
           
          * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
           
          * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
           
          * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
           

           

          For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

          
        

        - **httpMethod** *(string) --* 

          Specifies the integration's HTTP method type.

          
        

        - **uri** *(string) --* 

          Specifies Uniform Resource Identifier (URI) of the integration endpoint.

           

           
          * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
           
          * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
          

          
        

        - **connectionType** *(string) --* 

          The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

          
        

        - **connectionId** *(string) --* 

          The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

          
        

        - **credentials** *(string) --* 

          Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

          
        

        - **requestParameters** *(dict) --* 

          A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **requestTemplates** *(dict) --* 

          Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **passthroughBehavior** *(string) --*  

          Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

           

           
          * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
           
          * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
           
          * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
           

           
        

        - **contentHandling** *(string) --* 

          Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

           

           
          * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
           
          * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
           

           

          If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

          
        

        - **timeoutInMillis** *(integer) --* 

          Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

          
        

        - **cacheNamespace** *(string) --* 

          Specifies the integration's cache namespace.

          
        

        - **cacheKeyParameters** *(list) --* 

          Specifies the integration's cache key parameters.

          
          

          - *(string) --* 
      
        

        - **integrationResponses** *(dict) --* 

          Specifies the integration's responses.

            

          

           Example: Get integration responses of a method Request 

          

           ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns ``200 OK`` status and a payload as follows:

           ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

          

             `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
              

              - **statusCode** *(string) --* 

                Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                
              

              - **selectionPattern** *(string) --* 

                Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                
              

              - **responseParameters** *(dict) --* 

                A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **responseTemplates** *(dict) --* 

                Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **contentHandling** *(string) --* 

                Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                 

                 
                * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                 
                * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                 

                 

                If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                
          
      
    
    

  .. py:method:: get_integration_response(**kwargs)

    

    Represents a get integration response.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetIntegrationResponse>`_    


    **Request Syntax** 
    ::

      response = client.get_integration_response(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          statusCode='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Specifies a get integration response request's resource identifier.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies a get integration response request's HTTP method.

      

    
    :type statusCode: string
    :param statusCode: **[REQUIRED]** 

      Specifies a get integration response request's status code.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'statusCode': 'string',
            'selectionPattern': 'string',
            'responseParameters': {
                'string': 'string'
            },
            'responseTemplates': {
                'string': 'string'
            },
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

          `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **statusCode** *(string) --* 

          Specifies the status code that is used to map the integration response to an existing  MethodResponse .

          
        

        - **selectionPattern** *(string) --* 

          Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

          
        

        - **responseParameters** *(dict) --* 

          A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **responseTemplates** *(dict) --* 

          Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **contentHandling** *(string) --* 

          Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

           

           
          * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
           
          * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
           

           

          If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

          
    

  .. py:method:: get_method(**kwargs)

    

    Describe an existing  Method resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetMethod>`_    


    **Request Syntax** 
    ::

      response = client.get_method(
          restApiId='string',
          resourceId='string',
          httpMethod='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The  Resource identifier for the  Method resource.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies the method request's HTTP method type.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'httpMethod': 'string',
            'authorizationType': 'string',
            'authorizerId': 'string',
            'apiKeyRequired': True|False,
            'requestValidatorId': 'string',
            'operationName': 'string',
            'requestParameters': {
                'string': True|False
            },
            'requestModels': {
                'string': 'string'
            },
            'methodResponses': {
                'string': {
                    'statusCode': 'string',
                    'responseParameters': {
                        'string': True|False
                    },
                    'responseModels': {
                        'string': 'string'
                    }
                }
            },
            'methodIntegration': {
                'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                'httpMethod': 'string',
                'uri': 'string',
                'connectionType': 'INTERNET'|'VPC_LINK',
                'connectionId': 'string',
                'credentials': 'string',
                'requestParameters': {
                    'string': 'string'
                },
                'requestTemplates': {
                    'string': 'string'
                },
                'passthroughBehavior': 'string',
                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'timeoutInMillis': 123,
                'cacheNamespace': 'string',
                'cacheKeyParameters': [
                    'string',
                ],
                'integrationResponses': {
                    'string': {
                        'statusCode': 'string',
                        'selectionPattern': 'string',
                        'responseParameters': {
                            'string': 'string'
                        },
                        'responseTemplates': {
                            'string': 'string'
                        },
                        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a client-facing interface by which the client calls the API to access back-end resources. A **Method** resource is integrated with an  Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a **Method** resource, whereas an integration request is embodied in an  Integration resource. On the other hand, a method response is represented by a  MethodResponse resource, whereas an integration response is represented by an  IntegrationResponse resource. 

          

        

         Example: Retrive the GET method on a specified resource Request 

        The following example request retrieves the information about the GET method on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ). 

         ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

        The successful response returns a ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

        In the example above, the response template for the ``200 OK`` response maps the JSON output from the ``ListStreams`` action in the back end to an XML output. The mapping template is URL-encoded as ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`` and the output is decoded using the `$util.urlDecode() <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__ helper function.

            MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up an API's method <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__  
        

        - **httpMethod** *(string) --* 

          The method's HTTP verb.

          
        

        - **authorizationType** *(string) --* 

          The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

          
        

        - **authorizerId** *(string) --* 

          The identifier of an  Authorizer to use on this method. The ``authorizationType`` must be ``CUSTOM`` .

          
        

        - **apiKeyRequired** *(boolean) --* 

          A boolean flag specifying whether a valid  ApiKey is required to invoke this method.

          
        

        - **requestValidatorId** *(string) --* 

          The identifier of a  RequestValidator for request validation.

          
        

        - **operationName** *(string) --* 

          A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

          
        

        - **requestParameters** *(dict) --* 

          A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or templates.

          
          

          - *(string) --* 
            

            - *(boolean) --* 
      
    
        

        - **requestModels** *(dict) --* 

          A key-value map specifying data schemas, represented by  Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **methodResponses** *(dict) --* 

          Gets a method response associated with a given HTTP status code. 

            

          The collection of method responses are encapsulated in a key-value map, where the key is a response's HTTP status code and the value is a  MethodResponse resource that specifies the response returned to the caller from the back end through the integration response.

           Example: Get a 200 OK response of a GET method Request 

          

           ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns a ``200 OK`` status code and a payload similar to the following:

           ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }``  

          

             `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__  
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

                

              

               Example: A **MethodResponse** instance of an API Request 

              The example request retrieves a **MethodResponse** of the 200 status code.

               ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

              The successful response returns ``200 OK`` status and a payload as follows:

               ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

              

                  Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
              

              - **statusCode** *(string) --* 

                The method response's status code.

                
              

              - **responseParameters** *(dict) --* 

                A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

                
                

                - *(string) --* 
                  

                  - *(boolean) --* 
            
          
              

              - **responseModels** *(dict) --* 

                Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
      
    
        

        - **methodIntegration** *(dict) --* 

          Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.

            

          

           Example:  Request 

          

           ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns a ``200 OK`` status code and a payload similar to the following:

           ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }``  

          

             `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__  
          

          - **type** *(string) --* 

            Specifies an API method integration type. The valid value is one of the following:

             

             
            * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
             
            * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
             
            * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
             
            * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
             
            * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
             

             

            For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

            
          

          - **httpMethod** *(string) --* 

            Specifies the integration's HTTP method type.

            
          

          - **uri** *(string) --* 

            Specifies Uniform Resource Identifier (URI) of the integration endpoint.

             

             
            * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
             
            * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
            

            
          

          - **connectionType** *(string) --* 

            The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

            
          

          - **connectionId** *(string) --* 

            The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

            
          

          - **credentials** *(string) --* 

            Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

            
          

          - **requestParameters** *(dict) --* 

            A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **requestTemplates** *(dict) --* 

            Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **passthroughBehavior** *(string) --*  

            Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

             

             
            * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
             
            * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
             
            * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
             

             
          

          - **contentHandling** *(string) --* 

            Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

             

             
            * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
             
            * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
             

             

            If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

            
          

          - **timeoutInMillis** *(integer) --* 

            Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

            
          

          - **cacheNamespace** *(string) --* 

            Specifies the integration's cache namespace.

            
          

          - **cacheKeyParameters** *(list) --* 

            Specifies the integration's cache key parameters.

            
            

            - *(string) --* 
        
          

          - **integrationResponses** *(dict) --* 

            Specifies the integration's responses.

              

            

             Example: Get integration responses of a method Request 

            

             ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

            The successful response returns ``200 OK`` status and a payload as follows:

             ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

            

               `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
            

            - *(string) --* 
              

              - *(dict) --* 

                Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                

                - **statusCode** *(string) --* 

                  Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                  
                

                - **selectionPattern** *(string) --* 

                  Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                  
                

                - **responseParameters** *(dict) --* 

                  A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **responseTemplates** *(dict) --* 

                  Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **contentHandling** *(string) --* 

                  Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                   

                   
                  * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                   
                  * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                   

                   

                  If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                  
            
        
      
      
    

  .. py:method:: get_method_response(**kwargs)

    

    Describes a  MethodResponse resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetMethodResponse>`_    


    **Request Syntax** 
    ::

      response = client.get_method_response(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          statusCode='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The  Resource identifier for the  MethodResponse resource.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      The HTTP verb of the  Method resource.

      

    
    :type statusCode: string
    :param statusCode: **[REQUIRED]** 

      The status code for the  MethodResponse resource.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'statusCode': 'string',
            'responseParameters': {
                'string': True|False
            },
            'responseModels': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

          

        

         Example: A **MethodResponse** instance of an API Request 

        The example request retrieves a **MethodResponse** of the 200 status code.

         ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

        The successful response returns ``200 OK`` status and a payload as follows:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

        

            Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **statusCode** *(string) --* 

          The method response's status code.

          
        

        - **responseParameters** *(dict) --* 

          A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

          
          

          - *(string) --* 
            

            - *(boolean) --* 
      
    
        

        - **responseModels** *(dict) --* 

          Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: get_model(**kwargs)

    

    Describes an existing model defined for a  RestApi resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetModel>`_    


    **Request Syntax** 
    ::

      response = client.get_model(
          restApiId='string',
          modelName='string',
          flatten=True|False
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The  RestApi identifier under which the  Model exists.

      

    
    :type modelName: string
    :param modelName: **[REQUIRED]** 

      The name of the model as an identifier.

      

    
    :type flatten: boolean
    :param flatten: 

      A query parameter of a Boolean value to resolve (``true`` ) all external model references and returns a flattened model schema or not (``false`` ) The default is ``false`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'schema': 'string',
            'contentType': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the data structure of a method's request or response payload.

          

        A request model defines the data structure of the client-supplied request payload. A response model defines the data structure of the response payload returned by the back end. Although not required, models are useful for mapping payloads between the front end and back end.

         

        A model is used for generating an API's SDK, validating the input request body, and creating a skeletal mapping template.

            Method ,  MethodResponse , `Models and Mappings <http://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__  
        

        - **id** *(string) --* 

          The identifier for the model resource.

          
        

        - **name** *(string) --* 

          The name of the model. Must be an alphanumeric string.

          
        

        - **description** *(string) --* 

          The description of the model.

          
        

        - **schema** *(string) --* 

          The schema for the model. For ``application/json`` models, this should be `JSON-schema draft v4 <http://json-schema.org/documentation.html>`__ model. Do not include "\*/" characters in the description of any properties because such "\*/" characters may be interpreted as the closing marker for comments in some languages, such as Java or JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

          
        

        - **contentType** *(string) --* 

          The content-type for the model.

          
    

  .. py:method:: get_model_template(**kwargs)

    

    Generates a sample mapping template that can be used to transform a payload into the structure of a model.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetModelTemplate>`_    


    **Request Syntax** 
    ::

      response = client.get_model_template(
          restApiId='string',
          modelName='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type modelName: string
    :param modelName: **[REQUIRED]** 

      The name of the model for which to generate a template.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'value': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a mapping template used to transform a payload.

          `Mapping Templates <http://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html#models-mappings-mappings>`__  
        

        - **value** *(string) --* 

          The Apache `Velocity Template Language (VTL) <http://velocity.apache.org/engine/devel/vtl-reference-guide.html>`__ template content used for the template resource.

          
    

  .. py:method:: get_models(**kwargs)

    

    Describes existing  Models defined for a  RestApi resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetModels>`_    


    **Request Syntax** 
    ::

      response = client.get_models(
          restApiId='string',
          position='string',
          limit=123
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'description': 'string',
                    'schema': 'string',
                    'contentType': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  Model resources.

           Method ,  MethodResponse , `Models and Mappings <http://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents the data structure of a method's request or response payload.

              

            A request model defines the data structure of the client-supplied request payload. A response model defines the data structure of the response payload returned by the back end. Although not required, models are useful for mapping payloads between the front end and back end.

             

            A model is used for generating an API's SDK, validating the input request body, and creating a skeletal mapping template.

                Method ,  MethodResponse , `Models and Mappings <http://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__  
            

            - **id** *(string) --* 

              The identifier for the model resource.

              
            

            - **name** *(string) --* 

              The name of the model. Must be an alphanumeric string.

              
            

            - **description** *(string) --* 

              The description of the model.

              
            

            - **schema** *(string) --* 

              The schema for the model. For ``application/json`` models, this should be `JSON-schema draft v4 <http://json-schema.org/documentation.html>`__ model. Do not include "\*/" characters in the description of any properties because such "\*/" characters may be interpreted as the closing marker for comments in some languages, such as Java or JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

              
            

            - **contentType** *(string) --* 

              The content-type for the model.

              
        
      
    

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


  .. py:method:: get_request_validator(**kwargs)

    

    Gets a  RequestValidator of a given  RestApi .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetRequestValidator>`_    


    **Request Syntax** 
    ::

      response = client.get_request_validator(
          restApiId='string',
          requestValidatorId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type requestValidatorId: string
    :param requestValidatorId: **[REQUIRED]** 

      [Required] The identifier of the  RequestValidator to be retrieved.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'validateRequestBody': True|False,
            'validateRequestParameters': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        A set of validation rules for incoming  Method requests.

          

        In Swagger, a  RequestValidator of an API is defined by the `x-amazon-apigateway-request-validators.requestValidator <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.requestValidator.html>`__ object. It the referenced using the `x-amazon-apigateway-request-validator <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validator>`__ property.

          `Enable Basic Request Validation in API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__ 
        

        - **id** *(string) --* 

          The identifier of this  RequestValidator .

          
        

        - **name** *(string) --* 

          The name of this  RequestValidator 

          
        

        - **validateRequestBody** *(boolean) --* 

          A Boolean flag to indicate whether to validate a request body according to the configured  Model schema.

          
        

        - **validateRequestParameters** *(boolean) --* 

          A Boolean flag to indicate whether to validate request parameters (``true`` ) or not (``false`` ).

          
    

  .. py:method:: get_request_validators(**kwargs)

    

    Gets the  RequestValidators collection of a given  RestApi .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetRequestValidators>`_    


    **Request Syntax** 
    ::

      response = client.get_request_validators(
          restApiId='string',
          position='string',
          limit=123
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'validateRequestBody': True|False,
                    'validateRequestParameters': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A collection of  RequestValidator resources of a given  RestApi .

          

        In Swagger, the  RequestValidators of an API is defined by the `x-amazon-apigateway-request-validators <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.html>`__ extension.

          `Enable Basic Request Validation in API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__ 
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            A set of validation rules for incoming  Method requests.

              

            In Swagger, a  RequestValidator of an API is defined by the `x-amazon-apigateway-request-validators.requestValidator <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.requestValidator.html>`__ object. It the referenced using the `x-amazon-apigateway-request-validator <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validator>`__ property.

              `Enable Basic Request Validation in API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__ 
            

            - **id** *(string) --* 

              The identifier of this  RequestValidator .

              
            

            - **name** *(string) --* 

              The name of this  RequestValidator 

              
            

            - **validateRequestBody** *(boolean) --* 

              A Boolean flag to indicate whether to validate a request body according to the configured  Model schema.

              
            

            - **validateRequestParameters** *(boolean) --* 

              A Boolean flag to indicate whether to validate request parameters (``true`` ) or not (``false`` ).

              
        
      
    

  .. py:method:: get_resource(**kwargs)

    

    Lists information about a resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetResource>`_    


    **Request Syntax** 
    ::

      response = client.get_resource(
          restApiId='string',
          resourceId='string',
          embed=[
              'string',
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The identifier for the  Resource resource.

      

    
    :type embed: list
    :param embed: 

      A query parameter to retrieve the specified resources embedded in the returned  Resource representation in the response. This ``embed`` parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded  Method resources this way. The query parameter value must be a single-valued list and contain the ``"methods"`` string. For example, ``GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods`` .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'parentId': 'string',
            'pathPart': 'string',
            'path': 'string',
            'resourceMethods': {
                'string': {
                    'httpMethod': 'string',
                    'authorizationType': 'string',
                    'authorizerId': 'string',
                    'apiKeyRequired': True|False,
                    'requestValidatorId': 'string',
                    'operationName': 'string',
                    'requestParameters': {
                        'string': True|False
                    },
                    'requestModels': {
                        'string': 'string'
                    },
                    'methodResponses': {
                        'string': {
                            'statusCode': 'string',
                            'responseParameters': {
                                'string': True|False
                            },
                            'responseModels': {
                                'string': 'string'
                            }
                        }
                    },
                    'methodIntegration': {
                        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                        'httpMethod': 'string',
                        'uri': 'string',
                        'connectionType': 'INTERNET'|'VPC_LINK',
                        'connectionId': 'string',
                        'credentials': 'string',
                        'requestParameters': {
                            'string': 'string'
                        },
                        'requestTemplates': {
                            'string': 'string'
                        },
                        'passthroughBehavior': 'string',
                        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                        'timeoutInMillis': 123,
                        'cacheNamespace': 'string',
                        'cacheKeyParameters': [
                            'string',
                        ],
                        'integrationResponses': {
                            'string': {
                                'statusCode': 'string',
                                'selectionPattern': 'string',
                                'responseParameters': {
                                    'string': 'string'
                                },
                                'responseTemplates': {
                                    'string': 'string'
                                },
                                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                            }
                        }
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an API resource.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **id** *(string) --* 

          The resource's identifier.

          
        

        - **parentId** *(string) --* 

          The parent resource's identifier.

          
        

        - **pathPart** *(string) --* 

          The last path segment for this resource.

          
        

        - **path** *(string) --* 

          The full path for this resource.

          
        

        - **resourceMethods** *(dict) --* 

          Gets an API resource's method of a given HTTP verb.

            

          The resource methods are a map of methods indexed by methods' HTTP verbs enabled on the resource. This method map is included in the ``200 OK`` response of the ``GET /restapis/{restapi_id}/resources/{resource_id}`` or ``GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods`` request.

           Example: Get the GET method of an API resource Request ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20170223T031827Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": false, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

          If the ``OPTIONS`` is enabled on the resource, you can follow the example here to get that method. Just replace the ``GET`` of the last path segment in the request URL with ``OPTIONS`` .

             
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents a client-facing interface by which the client calls the API to access back-end resources. A **Method** resource is integrated with an  Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a **Method** resource, whereas an integration request is embodied in an  Integration resource. On the other hand, a method response is represented by a  MethodResponse resource, whereas an integration response is represented by an  IntegrationResponse resource. 

                

              

               Example: Retrive the GET method on a specified resource Request 

              The following example request retrieves the information about the GET method on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ). 

               ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

              The successful response returns a ``200 OK`` status code and a payload similar to the following:

               ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

              In the example above, the response template for the ``200 OK`` response maps the JSON output from the ``ListStreams`` action in the back end to an XML output. The mapping template is URL-encoded as ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`` and the output is decoded using the `$util.urlDecode() <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__ helper function.

                  MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up an API's method <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__  
              

              - **httpMethod** *(string) --* 

                The method's HTTP verb.

                
              

              - **authorizationType** *(string) --* 

                The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                
              

              - **authorizerId** *(string) --* 

                The identifier of an  Authorizer to use on this method. The ``authorizationType`` must be ``CUSTOM`` .

                
              

              - **apiKeyRequired** *(boolean) --* 

                A boolean flag specifying whether a valid  ApiKey is required to invoke this method.

                
              

              - **requestValidatorId** *(string) --* 

                The identifier of a  RequestValidator for request validation.

                
              

              - **operationName** *(string) --* 

                A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

                
              

              - **requestParameters** *(dict) --* 

                A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or templates.

                
                

                - *(string) --* 
                  

                  - *(boolean) --* 
            
          
              

              - **requestModels** *(dict) --* 

                A key-value map specifying data schemas, represented by  Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **methodResponses** *(dict) --* 

                Gets a method response associated with a given HTTP status code. 

                  

                The collection of method responses are encapsulated in a key-value map, where the key is a response's HTTP status code and the value is a  MethodResponse resource that specifies the response returned to the caller from the back end through the integration response.

                 Example: Get a 200 OK response of a GET method Request 

                

                 ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                The successful response returns a ``200 OK`` status code and a payload similar to the following:

                 ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }``  

                

                   `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__  
                

                - *(string) --* 
                  

                  - *(dict) --* 

                    Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

                      

                    

                     Example: A **MethodResponse** instance of an API Request 

                    The example request retrieves a **MethodResponse** of the 200 status code.

                     ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                    The successful response returns ``200 OK`` status and a payload as follows:

                     ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

                    

                        Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                    

                    - **statusCode** *(string) --* 

                      The method response's status code.

                      
                    

                    - **responseParameters** *(dict) --* 

                      A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

                      
                      

                      - *(string) --* 
                        

                        - *(boolean) --* 
                  
                
                    

                    - **responseModels** *(dict) --* 

                      Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

                      
                      

                      - *(string) --* 
                        

                        - *(string) --* 
                  
                
                
            
          
              

              - **methodIntegration** *(dict) --* 

                Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.

                  

                

                 Example:  Request 

                

                 ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                The successful response returns a ``200 OK`` status code and a payload similar to the following:

                 ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }``  

                

                   `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__  
                

                - **type** *(string) --* 

                  Specifies an API method integration type. The valid value is one of the following:

                   

                   
                  * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
                   
                  * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
                   
                  * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
                   
                  * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
                   
                  * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
                   

                   

                  For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

                  
                

                - **httpMethod** *(string) --* 

                  Specifies the integration's HTTP method type.

                  
                

                - **uri** *(string) --* 

                  Specifies Uniform Resource Identifier (URI) of the integration endpoint.

                   

                   
                  * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
                   
                  * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
                  

                  
                

                - **connectionType** *(string) --* 

                  The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

                  
                

                - **connectionId** *(string) --* 

                  The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

                  
                

                - **credentials** *(string) --* 

                  Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

                  
                

                - **requestParameters** *(dict) --* 

                  A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **requestTemplates** *(dict) --* 

                  Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **passthroughBehavior** *(string) --*  

                  Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

                   

                   
                  * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
                   
                  * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
                   
                  * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
                   

                   
                

                - **contentHandling** *(string) --* 

                  Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                   

                   
                  * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
                   
                  * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
                   

                   

                  If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

                  
                

                - **timeoutInMillis** *(integer) --* 

                  Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

                  
                

                - **cacheNamespace** *(string) --* 

                  Specifies the integration's cache namespace.

                  
                

                - **cacheKeyParameters** *(list) --* 

                  Specifies the integration's cache key parameters.

                  
                  

                  - *(string) --* 
              
                

                - **integrationResponses** *(dict) --* 

                  Specifies the integration's responses.

                    

                  

                   Example: Get integration responses of a method Request 

                  

                   ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                  The successful response returns ``200 OK`` status and a payload as follows:

                   ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

                  

                     `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                  

                  - *(string) --* 
                    

                    - *(dict) --* 

                      Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                        `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                      

                      - **statusCode** *(string) --* 

                        Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                        
                      

                      - **selectionPattern** *(string) --* 

                        Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                        
                      

                      - **responseParameters** *(dict) --* 

                        A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                        
                        

                        - *(string) --* 
                          

                          - *(string) --* 
                    
                  
                      

                      - **responseTemplates** *(dict) --* 

                        Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                        
                        

                        - *(string) --* 
                          

                          - *(string) --* 
                    
                  
                      

                      - **contentHandling** *(string) --* 

                        Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                         

                         
                        * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                         
                        * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                         

                         

                        If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                        
                  
              
            
            
          
      
    
    

  .. py:method:: get_resources(**kwargs)

    

    Lists information about a collection of  Resource resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetResources>`_    


    **Request Syntax** 
    ::

      response = client.get_resources(
          restApiId='string',
          position='string',
          limit=123,
          embed=[
              'string',
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

      

    
    :type embed: list
    :param embed: 

      A query parameter used to retrieve the specified resources embedded in the returned  Resources resource in the response. This ``embed`` parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded  Method resources this way. The query parameter value must be a single-valued list and contain the ``"methods"`` string. For example, ``GET /restapis/{restapi_id}/resources?embed=methods`` .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'parentId': 'string',
                    'pathPart': 'string',
                    'path': 'string',
                    'resourceMethods': {
                        'string': {
                            'httpMethod': 'string',
                            'authorizationType': 'string',
                            'authorizerId': 'string',
                            'apiKeyRequired': True|False,
                            'requestValidatorId': 'string',
                            'operationName': 'string',
                            'requestParameters': {
                                'string': True|False
                            },
                            'requestModels': {
                                'string': 'string'
                            },
                            'methodResponses': {
                                'string': {
                                    'statusCode': 'string',
                                    'responseParameters': {
                                        'string': True|False
                                    },
                                    'responseModels': {
                                        'string': 'string'
                                    }
                                }
                            },
                            'methodIntegration': {
                                'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                                'httpMethod': 'string',
                                'uri': 'string',
                                'connectionType': 'INTERNET'|'VPC_LINK',
                                'connectionId': 'string',
                                'credentials': 'string',
                                'requestParameters': {
                                    'string': 'string'
                                },
                                'requestTemplates': {
                                    'string': 'string'
                                },
                                'passthroughBehavior': 'string',
                                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                                'timeoutInMillis': 123,
                                'cacheNamespace': 'string',
                                'cacheKeyParameters': [
                                    'string',
                                ],
                                'integrationResponses': {
                                    'string': {
                                        'statusCode': 'string',
                                        'selectionPattern': 'string',
                                        'responseParameters': {
                                            'string': 'string'
                                        },
                                        'responseTemplates': {
                                            'string': 'string'
                                        },
                                        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                                    }
                                }
                            }
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  Resource resources.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents an API resource.

              `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
            

            - **id** *(string) --* 

              The resource's identifier.

              
            

            - **parentId** *(string) --* 

              The parent resource's identifier.

              
            

            - **pathPart** *(string) --* 

              The last path segment for this resource.

              
            

            - **path** *(string) --* 

              The full path for this resource.

              
            

            - **resourceMethods** *(dict) --* 

              Gets an API resource's method of a given HTTP verb.

                

              The resource methods are a map of methods indexed by methods' HTTP verbs enabled on the resource. This method map is included in the ``200 OK`` response of the ``GET /restapis/{restapi_id}/resources/{resource_id}`` or ``GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods`` request.

               Example: Get the GET method of an API resource Request ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20170223T031827Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": false, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

              If the ``OPTIONS`` is enabled on the resource, you can follow the example here to get that method. Just replace the ``GET`` of the last path segment in the request URL with ``OPTIONS`` .

                 
              

              - *(string) --* 
                

                - *(dict) --* 

                  Represents a client-facing interface by which the client calls the API to access back-end resources. A **Method** resource is integrated with an  Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a **Method** resource, whereas an integration request is embodied in an  Integration resource. On the other hand, a method response is represented by a  MethodResponse resource, whereas an integration response is represented by an  IntegrationResponse resource. 

                    

                  

                   Example: Retrive the GET method on a specified resource Request 

                  The following example request retrieves the information about the GET method on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ). 

                   ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                  The successful response returns a ``200 OK`` status code and a payload similar to the following:

                   ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

                  In the example above, the response template for the ``200 OK`` response maps the JSON output from the ``ListStreams`` action in the back end to an XML output. The mapping template is URL-encoded as ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`` and the output is decoded using the `$util.urlDecode() <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__ helper function.

                      MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up an API's method <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__  
                  

                  - **httpMethod** *(string) --* 

                    The method's HTTP verb.

                    
                  

                  - **authorizationType** *(string) --* 

                    The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                    
                  

                  - **authorizerId** *(string) --* 

                    The identifier of an  Authorizer to use on this method. The ``authorizationType`` must be ``CUSTOM`` .

                    
                  

                  - **apiKeyRequired** *(boolean) --* 

                    A boolean flag specifying whether a valid  ApiKey is required to invoke this method.

                    
                  

                  - **requestValidatorId** *(string) --* 

                    The identifier of a  RequestValidator for request validation.

                    
                  

                  - **operationName** *(string) --* 

                    A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

                    
                  

                  - **requestParameters** *(dict) --* 

                    A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or templates.

                    
                    

                    - *(string) --* 
                      

                      - *(boolean) --* 
                
              
                  

                  - **requestModels** *(dict) --* 

                    A key-value map specifying data schemas, represented by  Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).

                    
                    

                    - *(string) --* 
                      

                      - *(string) --* 
                
              
                  

                  - **methodResponses** *(dict) --* 

                    Gets a method response associated with a given HTTP status code. 

                      

                    The collection of method responses are encapsulated in a key-value map, where the key is a response's HTTP status code and the value is a  MethodResponse resource that specifies the response returned to the caller from the back end through the integration response.

                     Example: Get a 200 OK response of a GET method Request 

                    

                     ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                    The successful response returns a ``200 OK`` status code and a payload similar to the following:

                     ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }``  

                    

                       `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__  
                    

                    - *(string) --* 
                      

                      - *(dict) --* 

                        Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

                          

                        

                         Example: A **MethodResponse** instance of an API Request 

                        The example request retrieves a **MethodResponse** of the 200 status code.

                         ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                        The successful response returns ``200 OK`` status and a payload as follows:

                         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

                        

                            Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                        

                        - **statusCode** *(string) --* 

                          The method response's status code.

                          
                        

                        - **responseParameters** *(dict) --* 

                          A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

                          
                          

                          - *(string) --* 
                            

                            - *(boolean) --* 
                      
                    
                        

                        - **responseModels** *(dict) --* 

                          Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

                          
                          

                          - *(string) --* 
                            

                            - *(string) --* 
                      
                    
                    
                
              
                  

                  - **methodIntegration** *(dict) --* 

                    Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.

                      

                    

                     Example:  Request 

                    

                     ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                    The successful response returns a ``200 OK`` status code and a payload similar to the following:

                     ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }``  

                    

                       `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__  
                    

                    - **type** *(string) --* 

                      Specifies an API method integration type. The valid value is one of the following:

                       

                       
                      * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
                       
                      * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
                       
                      * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
                       
                      * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
                       
                      * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
                       

                       

                      For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

                      
                    

                    - **httpMethod** *(string) --* 

                      Specifies the integration's HTTP method type.

                      
                    

                    - **uri** *(string) --* 

                      Specifies Uniform Resource Identifier (URI) of the integration endpoint.

                       

                       
                      * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
                       
                      * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
                      

                      
                    

                    - **connectionType** *(string) --* 

                      The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

                      
                    

                    - **connectionId** *(string) --* 

                      The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

                      
                    

                    - **credentials** *(string) --* 

                      Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

                      
                    

                    - **requestParameters** *(dict) --* 

                      A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

                      
                      

                      - *(string) --* 
                        

                        - *(string) --* 
                  
                
                    

                    - **requestTemplates** *(dict) --* 

                      Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

                      
                      

                      - *(string) --* 
                        

                        - *(string) --* 
                  
                
                    

                    - **passthroughBehavior** *(string) --*  

                      Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

                       

                       
                      * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
                       
                      * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
                       
                      * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
                       

                       
                    

                    - **contentHandling** *(string) --* 

                      Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                       

                       
                      * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
                       
                      * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
                       

                       

                      If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

                      
                    

                    - **timeoutInMillis** *(integer) --* 

                      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

                      
                    

                    - **cacheNamespace** *(string) --* 

                      Specifies the integration's cache namespace.

                      
                    

                    - **cacheKeyParameters** *(list) --* 

                      Specifies the integration's cache key parameters.

                      
                      

                      - *(string) --* 
                  
                    

                    - **integrationResponses** *(dict) --* 

                      Specifies the integration's responses.

                        

                      

                       Example: Get integration responses of a method Request 

                      

                       ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                      The successful response returns ``200 OK`` status and a payload as follows:

                       ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

                      

                         `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                      

                      - *(string) --* 
                        

                        - *(dict) --* 

                          Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                            `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                          

                          - **statusCode** *(string) --* 

                            Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                            
                          

                          - **selectionPattern** *(string) --* 

                            Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                            
                          

                          - **responseParameters** *(dict) --* 

                            A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                            
                            

                            - *(string) --* 
                              

                              - *(string) --* 
                        
                      
                          

                          - **responseTemplates** *(dict) --* 

                            Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                            
                            

                            - *(string) --* 
                              

                              - *(string) --* 
                        
                      
                          

                          - **contentHandling** *(string) --* 

                            Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                             

                             
                            * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                             
                            * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                             

                             

                            If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                            
                      
                  
                
                
              
          
        
        
      
    

  .. py:method:: get_rest_api(**kwargs)

    

    Lists the  RestApi resource in the collection.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetRestApi>`_    


    **Request Syntax** 
    ::

      response = client.get_rest_api(
          restApiId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The identifier of the  RestApi resource.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'warnings': [
                'string',
            ],
            'binaryMediaTypes': [
                'string',
            ],
            'endpointConfiguration': {
                'types': [
                    'REGIONAL'|'EDGE',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a REST API.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **id** *(string) --* 

          The API's identifier. This identifier is unique across all of your APIs in API Gateway.

          
        

        - **name** *(string) --* 

          The API's name.

          
        

        - **description** *(string) --* 

          The API's description.

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the API was created.

          
        

        - **version** *(string) --* 

          A version identifier for the API.

          
        

        - **warnings** *(list) --* 

          The warning messages reported when ``failonwarnings`` is turned on during API import.

          
          

          - *(string) --* 
      
        

        - **binaryMediaTypes** *(list) --* 

          The list of binary media types supported by the  RestApi . By default, the  RestApi supports only UTF-8-encoded text payloads.

          
          

          - *(string) --* 
      
        

        - **endpointConfiguration** *(dict) --* 

          The endpoint configuration of this  RestApi showing the endpoint types of the API. 

          
          

          - **types** *(list) --* 

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

            
            

            - *(string) --* 

              The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

              
        
      
    

  .. py:method:: get_rest_apis(**kwargs)

    

    Lists the  RestApis resources for your collection.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetRestApis>`_    


    **Request Syntax** 
    ::

      response = client.get_rest_apis(
          position='string',
          limit=123
      )
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'description': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'version': 'string',
                    'warnings': [
                        'string',
                    ],
                    'binaryMediaTypes': [
                        'string',
                    ],
                    'endpointConfiguration': {
                        'types': [
                            'REGIONAL'|'EDGE',
                        ]
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains references to your APIs and links that guide you in how to interact with your collection. A collection offers a paginated view of your APIs.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a REST API.

              `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
            

            - **id** *(string) --* 

              The API's identifier. This identifier is unique across all of your APIs in API Gateway.

              
            

            - **name** *(string) --* 

              The API's name.

              
            

            - **description** *(string) --* 

              The API's description.

              
            

            - **createdDate** *(datetime) --* 

              The timestamp when the API was created.

              
            

            - **version** *(string) --* 

              A version identifier for the API.

              
            

            - **warnings** *(list) --* 

              The warning messages reported when ``failonwarnings`` is turned on during API import.

              
              

              - *(string) --* 
          
            

            - **binaryMediaTypes** *(list) --* 

              The list of binary media types supported by the  RestApi . By default, the  RestApi supports only UTF-8-encoded text payloads.

              
              

              - *(string) --* 
          
            

            - **endpointConfiguration** *(dict) --* 

              The endpoint configuration of this  RestApi showing the endpoint types of the API. 

              
              

              - **types** *(list) --* 

                A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

                
                

                - *(string) --* 

                  The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

                  
            
          
        
      
    

  .. py:method:: get_sdk(**kwargs)

    

    Generates a client SDK for a  RestApi and  Stage .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetSdk>`_    


    **Request Syntax** 
    ::

      response = client.get_sdk(
          restApiId='string',
          stageName='string',
          sdkType='string',
          parameters={
              'string': 'string'
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: **[REQUIRED]** 

      The name of the  Stage that the SDK will use.

      

    
    :type sdkType: string
    :param sdkType: **[REQUIRED]** 

      The language for the generated SDK. Currently ``java`` , ``javascript`` , ``android`` , ``objectivec`` (for iOS), ``swift`` (for iOS), and ``ruby`` are supported.

      

    
    :type parameters: dict
    :param parameters: 

      A string-to-string key-value map of query parameters ``sdkType`` -dependent properties of the SDK. For ``sdkType`` of ``objectivec`` or ``swift`` , a parameter named ``classPrefix`` is required. For ``sdkType`` of ``android`` , parameters named ``groupId`` , ``artifactId`` , ``artifactVersion`` , and ``invokerPackage`` are required. For ``sdkType`` of ``java`` , parameters named ``serviceName`` and ``javaPackageName`` are required. 

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'contentType': 'string',
            'contentDisposition': 'string',
            'body': StreamingBody()
        }
      **Response Structure** 

      

      - *(dict) --* 

        The binary blob response to  GetSdk , which contains the generated SDK.

        
        

        - **contentType** *(string) --* 

          The content-type header value in the HTTP response.

          
        

        - **contentDisposition** *(string) --* 

          The content-disposition header value in the HTTP response.

          
        

        - **body** (:class:`.StreamingBody`) -- 

          The binary blob response to  GetSdk , which contains the generated SDK.

          
    

  .. py:method:: get_sdk_type(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetSdkType>`_    


    **Request Syntax** 
    ::

      response = client.get_sdk_type(
          id='string'
      )
    :type id: string
    :param id: **[REQUIRED]** 

      The identifier of the queried  SdkType instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'friendlyName': 'string',
            'description': 'string',
            'configurationProperties': [
                {
                    'name': 'string',
                    'friendlyName': 'string',
                    'description': 'string',
                    'required': True|False,
                    'defaultValue': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A type of SDK that API Gateway can generate.

        
        

        - **id** *(string) --* 

          The identifier of an  SdkType instance.

          
        

        - **friendlyName** *(string) --* 

          The user-friendly name of an  SdkType instance.

          
        

        - **description** *(string) --* 

          The description of an  SdkType .

          
        

        - **configurationProperties** *(list) --* 

          A list of configuration properties of an  SdkType .

          
          

          - *(dict) --* 

            A configuration property of an SDK type.

            
            

            - **name** *(string) --* 

              The name of a an  SdkType configuration property.

              
            

            - **friendlyName** *(string) --* 

              The user-friendly name of an  SdkType configuration property.

              
            

            - **description** *(string) --* 

              The description of an  SdkType configuration property.

              
            

            - **required** *(boolean) --* 

              A boolean flag of an  SdkType configuration property to indicate if the associated SDK configuration property is required (``true`` ) or not (``false`` ).

              
            

            - **defaultValue** *(string) --* 

              The default value of an  SdkType configuration property.

              
        
      
    

  .. py:method:: get_sdk_types(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetSdkTypes>`_    


    **Request Syntax** 
    ::

      response = client.get_sdk_types(
          position='string',
          limit=123
      )
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'friendlyName': 'string',
                    'description': 'string',
                    'configurationProperties': [
                        {
                            'name': 'string',
                            'friendlyName': 'string',
                            'description': 'string',
                            'required': True|False,
                            'defaultValue': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The collection of  SdkType instances.

        
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            A type of SDK that API Gateway can generate.

            
            

            - **id** *(string) --* 

              The identifier of an  SdkType instance.

              
            

            - **friendlyName** *(string) --* 

              The user-friendly name of an  SdkType instance.

              
            

            - **description** *(string) --* 

              The description of an  SdkType .

              
            

            - **configurationProperties** *(list) --* 

              A list of configuration properties of an  SdkType .

              
              

              - *(dict) --* 

                A configuration property of an SDK type.

                
                

                - **name** *(string) --* 

                  The name of a an  SdkType configuration property.

                  
                

                - **friendlyName** *(string) --* 

                  The user-friendly name of an  SdkType configuration property.

                  
                

                - **description** *(string) --* 

                  The description of an  SdkType configuration property.

                  
                

                - **required** *(boolean) --* 

                  A boolean flag of an  SdkType configuration property to indicate if the associated SDK configuration property is required (``true`` ) or not (``false`` ).

                  
                

                - **defaultValue** *(string) --* 

                  The default value of an  SdkType configuration property.

                  
            
          
        
      
    

  .. py:method:: get_stage(**kwargs)

    

    Gets information about a  Stage resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetStage>`_    


    **Request Syntax** 
    ::

      response = client.get_stage(
          restApiId='string',
          stageName='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: **[REQUIRED]** 

      The name of the  Stage resource to get information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentId': 'string',
            'clientCertificateId': 'string',
            'stageName': 'string',
            'description': 'string',
            'cacheClusterEnabled': True|False,
            'cacheClusterSize': '0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
            'cacheClusterStatus': 'CREATE_IN_PROGRESS'|'AVAILABLE'|'DELETE_IN_PROGRESS'|'NOT_AVAILABLE'|'FLUSH_IN_PROGRESS',
            'methodSettings': {
                'string': {
                    'metricsEnabled': True|False,
                    'loggingLevel': 'string',
                    'dataTraceEnabled': True|False,
                    'throttlingBurstLimit': 123,
                    'throttlingRateLimit': 123.0,
                    'cachingEnabled': True|False,
                    'cacheTtlInSeconds': 123,
                    'cacheDataEncrypted': True|False,
                    'requireAuthorizationForCacheControl': True|False,
                    'unauthorizedCacheControlHeaderStrategy': 'FAIL_WITH_403'|'SUCCEED_WITH_RESPONSE_HEADER'|'SUCCEED_WITHOUT_RESPONSE_HEADER'
                }
            },
            'variables': {
                'string': 'string'
            },
            'documentationVersion': 'string',
            'accessLogSettings': {
                'format': 'string',
                'destinationArn': 'string'
            },
            'canarySettings': {
                'percentTraffic': 123.0,
                'deploymentId': 'string',
                'stageVariableOverrides': {
                    'string': 'string'
                },
                'useStageCache': True|False
            },
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

          `Deploy an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__  
        

        - **deploymentId** *(string) --* 

          The identifier of the  Deployment that the stage points to.

          
        

        - **clientCertificateId** *(string) --* 

          The identifier of a client certificate for an API stage.

          
        

        - **stageName** *(string) --* 

          The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway.

          
        

        - **description** *(string) --* 

          The stage's description.

          
        

        - **cacheClusterEnabled** *(boolean) --* 

          Specifies whether a cache cluster is enabled for the stage.

          
        

        - **cacheClusterSize** *(string) --* 

          The size of the cache cluster for the stage, if enabled.

          
        

        - **cacheClusterStatus** *(string) --* 

          The status of the cache cluster for the stage, if enabled.

          
        

        - **methodSettings** *(dict) --* 

          A map that defines the method settings for a  Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\*/\*`` for overriding all methods in the stage. 

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Specifies the method setting properties.

              
              

              - **metricsEnabled** *(boolean) --* 

                Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a Boolean.

                
              

              - **loggingLevel** *(string) --* 

                Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` , ``ERROR`` , and ``INFO`` .

                
              

              - **dataTraceEnabled** *(boolean) --* 

                Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

                
              

              - **throttlingBurstLimit** *(integer) --* 

                Specifies the throttling burst limit. The PATCH path for this setting is ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

                
              

              - **throttlingRateLimit** *(float) --* 

                Specifies the throttling rate limit. The PATCH path for this setting is ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

                
              

              - **cachingEnabled** *(boolean) --* 

                Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached. The PATCH path for this setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

                
              

              - **cacheTtlInSeconds** *(integer) --* 

                Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached. The PATCH path for this setting is ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

                
              

              - **cacheDataEncrypted** *(boolean) --* 

                Specifies whether the cached responses are encrypted. The PATCH path for this setting is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

                
              

              - **requireAuthorizationForCacheControl** *(boolean) --* 

                Specifies whether authorization is required for a cache invalidation request. The PATCH path for this setting is ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value is a Boolean.

                
              

              - **unauthorizedCacheControlHeaderStrategy** *(string) --* 

                Specifies how to handle unauthorized requests for cache invalidation. The PATCH path for this setting is ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` , ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

                
          
      
    
        

        - **variables** *(dict) --* 

          A map that defines the stage variables for a  Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+`` .

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **documentationVersion** *(string) --* 

          The version of the associated API documentation.

          
        

        - **accessLogSettings** *(dict) --* 

          Settings for logging access in this stage.

          
          

          - **format** *(string) --* 

            A single line format of the access logs of data, as specified by selected `$context variables <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__ . The format must include at least ``$context.requestId`` .

            
          

          - **destinationArn** *(string) --* 

            The ARN of the CloudWatch Logs log group to receive access logs.

            
      
        

        - **canarySettings** *(dict) --* 

          Settings for the canary deployment in this stage.

          
          

          - **percentTraffic** *(float) --* 

            The percent (0-100) of traffic diverted to a canary deployment.

            
          

          - **deploymentId** *(string) --* 

            The ID of the canary deployment.

            
          

          - **stageVariableOverrides** *(dict) --* 

            Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **useStageCache** *(boolean) --* 

            A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

            
      
        

        - **createdDate** *(datetime) --* 

          The timestamp when the stage was created.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The timestamp when the stage last updated.

          
    

  .. py:method:: get_stages(**kwargs)

    

    Gets information about one or more  Stage resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetStages>`_    


    **Request Syntax** 
    ::

      response = client.get_stages(
          restApiId='string',
          deploymentId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type deploymentId: string
    :param deploymentId: 

      The stages' deployment identifiers.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'item': [
                {
                    'deploymentId': 'string',
                    'clientCertificateId': 'string',
                    'stageName': 'string',
                    'description': 'string',
                    'cacheClusterEnabled': True|False,
                    'cacheClusterSize': '0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
                    'cacheClusterStatus': 'CREATE_IN_PROGRESS'|'AVAILABLE'|'DELETE_IN_PROGRESS'|'NOT_AVAILABLE'|'FLUSH_IN_PROGRESS',
                    'methodSettings': {
                        'string': {
                            'metricsEnabled': True|False,
                            'loggingLevel': 'string',
                            'dataTraceEnabled': True|False,
                            'throttlingBurstLimit': 123,
                            'throttlingRateLimit': 123.0,
                            'cachingEnabled': True|False,
                            'cacheTtlInSeconds': 123,
                            'cacheDataEncrypted': True|False,
                            'requireAuthorizationForCacheControl': True|False,
                            'unauthorizedCacheControlHeaderStrategy': 'FAIL_WITH_403'|'SUCCEED_WITH_RESPONSE_HEADER'|'SUCCEED_WITHOUT_RESPONSE_HEADER'
                        }
                    },
                    'variables': {
                        'string': 'string'
                    },
                    'documentationVersion': 'string',
                    'accessLogSettings': {
                        'format': 'string',
                        'destinationArn': 'string'
                    },
                    'canarySettings': {
                        'percentTraffic': 123.0,
                        'deploymentId': 'string',
                        'stageVariableOverrides': {
                            'string': 'string'
                        },
                        'useStageCache': True|False
                    },
                    'createdDate': datetime(2015, 1, 1),
                    'lastUpdatedDate': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of  Stage resources that are associated with the  ApiKey resource.

         `Deploying API in Stages <http://docs.aws.amazon.com/apigateway/latest/developerguide/stages.html>`__ 
        

        - **item** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

              `Deploy an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__  
            

            - **deploymentId** *(string) --* 

              The identifier of the  Deployment that the stage points to.

              
            

            - **clientCertificateId** *(string) --* 

              The identifier of a client certificate for an API stage.

              
            

            - **stageName** *(string) --* 

              The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway.

              
            

            - **description** *(string) --* 

              The stage's description.

              
            

            - **cacheClusterEnabled** *(boolean) --* 

              Specifies whether a cache cluster is enabled for the stage.

              
            

            - **cacheClusterSize** *(string) --* 

              The size of the cache cluster for the stage, if enabled.

              
            

            - **cacheClusterStatus** *(string) --* 

              The status of the cache cluster for the stage, if enabled.

              
            

            - **methodSettings** *(dict) --* 

              A map that defines the method settings for a  Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\*/\*`` for overriding all methods in the stage. 

              
              

              - *(string) --* 
                

                - *(dict) --* 

                  Specifies the method setting properties.

                  
                  

                  - **metricsEnabled** *(boolean) --* 

                    Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a Boolean.

                    
                  

                  - **loggingLevel** *(string) --* 

                    Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` , ``ERROR`` , and ``INFO`` .

                    
                  

                  - **dataTraceEnabled** *(boolean) --* 

                    Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

                    
                  

                  - **throttlingBurstLimit** *(integer) --* 

                    Specifies the throttling burst limit. The PATCH path for this setting is ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

                    
                  

                  - **throttlingRateLimit** *(float) --* 

                    Specifies the throttling rate limit. The PATCH path for this setting is ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

                    
                  

                  - **cachingEnabled** *(boolean) --* 

                    Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached. The PATCH path for this setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

                    
                  

                  - **cacheTtlInSeconds** *(integer) --* 

                    Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached. The PATCH path for this setting is ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

                    
                  

                  - **cacheDataEncrypted** *(boolean) --* 

                    Specifies whether the cached responses are encrypted. The PATCH path for this setting is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

                    
                  

                  - **requireAuthorizationForCacheControl** *(boolean) --* 

                    Specifies whether authorization is required for a cache invalidation request. The PATCH path for this setting is ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value is a Boolean.

                    
                  

                  - **unauthorizedCacheControlHeaderStrategy** *(string) --* 

                    Specifies how to handle unauthorized requests for cache invalidation. The PATCH path for this setting is ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` , ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

                    
              
          
        
            

            - **variables** *(dict) --* 

              A map that defines the stage variables for a  Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+`` .

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **documentationVersion** *(string) --* 

              The version of the associated API documentation.

              
            

            - **accessLogSettings** *(dict) --* 

              Settings for logging access in this stage.

              
              

              - **format** *(string) --* 

                A single line format of the access logs of data, as specified by selected `$context variables <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__ . The format must include at least ``$context.requestId`` .

                
              

              - **destinationArn** *(string) --* 

                The ARN of the CloudWatch Logs log group to receive access logs.

                
          
            

            - **canarySettings** *(dict) --* 

              Settings for the canary deployment in this stage.

              
              

              - **percentTraffic** *(float) --* 

                The percent (0-100) of traffic diverted to a canary deployment.

                
              

              - **deploymentId** *(string) --* 

                The ID of the canary deployment.

                
              

              - **stageVariableOverrides** *(dict) --* 

                Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **useStageCache** *(boolean) --* 

                A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

                
          
            

            - **createdDate** *(datetime) --* 

              The timestamp when the stage was created.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The timestamp when the stage last updated.

              
        
      
    

  .. py:method:: get_usage(**kwargs)

    

    Gets the usage data of a usage plan in a specified time interval.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsage>`_    


    **Request Syntax** 
    ::

      response = client.get_usage(
          usagePlanId='string',
          keyId='string',
          startDate='string',
          endDate='string',
          position='string',
          limit=123
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the usage plan associated with the usage data.

      

    
    :type keyId: string
    :param keyId: 

      The Id of the API key associated with the resultant usage data.

      

    
    :type startDate: string
    :param startDate: **[REQUIRED]** 

      The starting date (e.g., 2016-01-01) of the usage data.

      

    
    :type endDate: string
    :param endDate: **[REQUIRED]** 

      The ending date (e.g., 2016-12-31) of the usage data.

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'usagePlanId': 'string',
            'startDate': 'string',
            'endDate': 'string',
            'position': 'string',
            'items': {
                'string': [
                    [
                        123,
                    ],
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the usage data of a usage plan.

           `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__ , `Manage Usage in a Usage Plan <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans-with-console.html#api-gateway-usage-plan-manage-usage>`__  
        

        - **usagePlanId** *(string) --* 

          The plan Id associated with this usage data.

          
        

        - **startDate** *(string) --* 

          The starting date of the usage data.

          
        

        - **endDate** *(string) --* 

          The ending date of the usage data.

          
        

        - **position** *(string) --* 
        

        - **items** *(dict) --* 

          The usage data, as daily logs of used and remaining quotas, over the specified time interval indexed over the API keys in a usage plan. For example, ``{..., "values" : { "{api_key}" : [ [0, 100], [10, 90], [100, 10]]}`` , where ``{api_key}`` stands for an API key value and the daily log entry is of the format ``[used quota, remaining quota]`` .

          
          

          - *(string) --* 
            

            - *(list) --* 
              

              - *(list) --* 
                

                - *(integer) --* 
            
          
      
    
    

  .. py:method:: get_usage_plan(**kwargs)

    

    Gets a usage plan of a given plan identifier.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsagePlan>`_    


    **Request Syntax** 
    ::

      response = client.get_usage_plan(
          usagePlanId='string'
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The identifier of the  UsagePlan resource to be retrieved.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'apiStages': [
                {
                    'apiId': 'string',
                    'stage': 'string'
                },
            ],
            'throttle': {
                'burstLimit': 123,
                'rateLimit': 123.0
            },
            'quota': {
                'limit': 123,
                'offset': 123,
                'period': 'DAY'|'WEEK'|'MONTH'
            },
            'productCode': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a usage plan than can specify who can assess associated API stages with specified request limits and quotas.

          

        In a usage plan, you associate an API by specifying the API's Id and a stage name of the specified API. You add plan customers by adding API keys to the plan. 

           `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **id** *(string) --* 

          The identifier of a  UsagePlan resource.

          
        

        - **name** *(string) --* 

          The name of a usage plan.

          
        

        - **description** *(string) --* 

          The description of a usage plan.

          
        

        - **apiStages** *(list) --* 

          The associated API stages of a usage plan.

          
          

          - *(dict) --* 

            API stage name of the associated API stage in a usage plan.

            
            

            - **apiId** *(string) --* 

              API Id of the associated API stage in a usage plan.

              
            

            - **stage** *(string) --* 

              API stage name of the associated API stage in a usage plan.

              
        
      
        

        - **throttle** *(dict) --* 

          The request throttle limits of a usage plan.

          
          

          - **burstLimit** *(integer) --* 

            The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.

            
          

          - **rateLimit** *(float) --* 

            The API request steady-state rate limit.

            
      
        

        - **quota** *(dict) --* 

          The maximum number of permitted requests per a given unit time interval.

          
          

          - **limit** *(integer) --* 

            The maximum number of requests that can be made in a given time period.

            
          

          - **offset** *(integer) --* 

            The number of requests subtracted from the given limit in the initial time period.

            
          

          - **period** *(string) --* 

            The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".

            
      
        

        - **productCode** *(string) --* 

          The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

          
    

  .. py:method:: get_usage_plan_key(**kwargs)

    

    Gets a usage plan key of a given key identifier.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsagePlanKey>`_    


    **Request Syntax** 
    ::

      response = client.get_usage_plan_key(
          usagePlanId='string',
          keyId='string'
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the  UsagePlan resource representing the usage plan containing the to-be-retrieved  UsagePlanKey resource representing a plan customer.

      

    
    :type keyId: string
    :param keyId: **[REQUIRED]** 

      The key Id of the to-be-retrieved  UsagePlanKey resource representing a plan customer.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'type': 'string',
            'value': 'string',
            'name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a usage plan key to identify a plan customer.

          

        To associate an API stage with a selected API key in a usage plan, you must create a UsagePlanKey resource to represent the selected  ApiKey .

         "  `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **id** *(string) --* 

          The Id of a usage plan key.

          
        

        - **type** *(string) --* 

          The type of a usage plan key. Currently, the valid key type is ``API_KEY`` .

          
        

        - **value** *(string) --* 

          The value of a usage plan key.

          
        

        - **name** *(string) --* 

          The name of a usage plan key.

          
    

  .. py:method:: get_usage_plan_keys(**kwargs)

    

    Gets all the usage plan keys representing the API keys added to a specified usage plan.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsagePlanKeys>`_    


    **Request Syntax** 
    ::

      response = client.get_usage_plan_keys(
          usagePlanId='string',
          position='string',
          limit=123,
          nameQuery='string'
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the  UsagePlan resource representing the usage plan containing the to-be-retrieved  UsagePlanKey resource representing a plan customer.

      

    
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    :type nameQuery: string
    :param nameQuery: 

      A query parameter specifying the name of the to-be-returned usage plan keys.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'type': 'string',
                    'value': 'string',
                    'name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the collection of usage plan keys added to usage plans for the associated API keys and, possibly, other types of keys.

          `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a usage plan key to identify a plan customer.

              

            To associate an API stage with a selected API key in a usage plan, you must create a UsagePlanKey resource to represent the selected  ApiKey .

             "  `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
            

            - **id** *(string) --* 

              The Id of a usage plan key.

              
            

            - **type** *(string) --* 

              The type of a usage plan key. Currently, the valid key type is ``API_KEY`` .

              
            

            - **value** *(string) --* 

              The value of a usage plan key.

              
            

            - **name** *(string) --* 

              The name of a usage plan key.

              
        
      
    

  .. py:method:: get_usage_plans(**kwargs)

    

    Gets all the usage plans of the caller's account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsagePlans>`_    


    **Request Syntax** 
    ::

      response = client.get_usage_plans(
          position='string',
          keyId='string',
          limit=123
      )
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type keyId: string
    :param keyId: 

      The identifier of the API key associated with the usage plans.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'description': 'string',
                    'apiStages': [
                        {
                            'apiId': 'string',
                            'stage': 'string'
                        },
                    ],
                    'throttle': {
                        'burstLimit': 123,
                        'rateLimit': 123.0
                    },
                    'quota': {
                        'limit': 123,
                        'offset': 123,
                        'period': 'DAY'|'WEEK'|'MONTH'
                    },
                    'productCode': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of usage plans for an AWS account.

          `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a usage plan than can specify who can assess associated API stages with specified request limits and quotas.

              

            In a usage plan, you associate an API by specifying the API's Id and a stage name of the specified API. You add plan customers by adding API keys to the plan. 

               `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
            

            - **id** *(string) --* 

              The identifier of a  UsagePlan resource.

              
            

            - **name** *(string) --* 

              The name of a usage plan.

              
            

            - **description** *(string) --* 

              The description of a usage plan.

              
            

            - **apiStages** *(list) --* 

              The associated API stages of a usage plan.

              
              

              - *(dict) --* 

                API stage name of the associated API stage in a usage plan.

                
                

                - **apiId** *(string) --* 

                  API Id of the associated API stage in a usage plan.

                  
                

                - **stage** *(string) --* 

                  API stage name of the associated API stage in a usage plan.

                  
            
          
            

            - **throttle** *(dict) --* 

              The request throttle limits of a usage plan.

              
              

              - **burstLimit** *(integer) --* 

                The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.

                
              

              - **rateLimit** *(float) --* 

                The API request steady-state rate limit.

                
          
            

            - **quota** *(dict) --* 

              The maximum number of permitted requests per a given unit time interval.

              
              

              - **limit** *(integer) --* 

                The maximum number of requests that can be made in a given time period.

                
              

              - **offset** *(integer) --* 

                The number of requests subtracted from the given limit in the initial time period.

                
              

              - **period** *(string) --* 

                The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".

                
          
            

            - **productCode** *(string) --* 

              The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

              
        
      
    

  .. py:method:: get_vpc_link(**kwargs)

    

    Gets a specified VPC link under the caller's account in a region.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetVpcLink>`_    


    **Request Syntax** 
    ::

      response = client.get_vpc_link(
          vpcLinkId='string'
      )
    :type vpcLinkId: string
    :param vpcLinkId: **[REQUIRED]** 

      [Required] The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'targetArns': [
                'string',
            ],
            'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
            'statusMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud (VPC).

          

        

        To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway, you, as an API developer, create a  VpcLink resource targeted for one or more network load balancers of the VPC and then integrate an API method with a private integration that uses the  VpcLink . The private integraiton has an integration type of ``HTTP`` or ``HTTP_PROXY`` and has a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to identify the  VpcLink used.

         

         
        

        - **id** *(string) --* 

          The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

          
        

        - **name** *(string) --* 

          The name used to label and identify the VPC link.

          
        

        - **description** *(string) --* 

          The description of the VPC link.

          
        

        - **targetArns** *(list) --* 

          The ARNs of network load balancers of the VPC targeted by the VPC link. The network load balancers must be owned by the same AWS account of the API owner.

          
          

          - *(string) --* 
      
        

        - **status** *(string) --* 

          The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` , ``DELETING`` , or ``FAILED`` . Deploying an API will wait if the status is ``PENDING`` and will fail if the status is ``DELETING`` . 

          
        

        - **statusMessage** *(string) --* 

          A description about the VPC link status.

          
    

  .. py:method:: get_vpc_links(**kwargs)

    

    Gets the  VpcLinks collection under the caller's account in a selected region.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetVpcLinks>`_    


    **Request Syntax** 
    ::

      response = client.get_vpc_links(
          position='string',
          limit=123
      )
    :type position: string
    :param position: 

      The current pagination position in the paged result set.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of returned results per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'position': 'string',
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'description': 'string',
                    'targetArns': [
                        'string',
                    ],
                    'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
                    'statusMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The collection of VPC links under the caller's account in a region.

          `Getting Started with Private Integrations <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-private-integration.html>`__ , `Set up Private Integrations <http://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html>`__  
        

        - **position** *(string) --* 
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud (VPC).

              

            

            To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway, you, as an API developer, create a  VpcLink resource targeted for one or more network load balancers of the VPC and then integrate an API method with a private integration that uses the  VpcLink . The private integraiton has an integration type of ``HTTP`` or ``HTTP_PROXY`` and has a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to identify the  VpcLink used.

             

             
            

            - **id** *(string) --* 

              The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

              
            

            - **name** *(string) --* 

              The name used to label and identify the VPC link.

              
            

            - **description** *(string) --* 

              The description of the VPC link.

              
            

            - **targetArns** *(list) --* 

              The ARNs of network load balancers of the VPC targeted by the VPC link. The network load balancers must be owned by the same AWS account of the API owner.

              
              

              - *(string) --* 
          
            

            - **status** *(string) --* 

              The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` , ``DELETING`` , or ``FAILED`` . Deploying an API will wait if the status is ``PENDING`` and will fail if the status is ``DELETING`` . 

              
            

            - **statusMessage** *(string) --* 

              A description about the VPC link status.

              
        
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: import_api_keys(**kwargs)

    

    Import API keys from an external source, such as a CSV-formatted file.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/ImportApiKeys>`_    


    **Request Syntax** 
    ::

      response = client.import_api_keys(
          body=b'bytes'|file,
          format='csv',
          failOnWarnings=True|False
      )
    :type body: bytes or seekable file-like object
    :param body: **[REQUIRED]** 

      The payload of the POST request to import API keys. For the payload format, see `API Key File Format <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-key-file-format.html>`__ .

      

    
    :type format: string
    :param format: **[REQUIRED]** 

      A query parameter to specify the input format to imported API keys. Currently, only the ``csv`` format is supported.

      

    
    :type failOnWarnings: boolean
    :param failOnWarnings: 

      A query parameter to indicate whether to rollback  ApiKey importation (``true`` ) or not (``false`` ) when error is encountered.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ids': [
                'string',
            ],
            'warnings': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The identifier of an  ApiKey used in a  UsagePlan .

        
        

        - **ids** *(list) --* 

          A list of all the  ApiKey identifiers.

          
          

          - *(string) --* 
      
        

        - **warnings** *(list) --* 

          A list of warning messages.

          
          

          - *(string) --* 
      
    

  .. py:method:: import_documentation_parts(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/ImportDocumentationParts>`_    


    **Request Syntax** 
    ::

      response = client.import_documentation_parts(
          restApiId='string',
          mode='merge'|'overwrite',
          failOnWarnings=True|False,
          body=b'bytes'|file
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type mode: string
    :param mode: 

      A query parameter to indicate whether to overwrite (``OVERWRITE`` ) any existing  DocumentationParts definition or to merge (``MERGE`` ) the new definition into the existing one. The default value is ``MERGE`` .

      

    
    :type failOnWarnings: boolean
    :param failOnWarnings: 

      A query parameter to specify whether to rollback the documentation importation (``true`` ) or not (``false`` ) when a warning is encountered. The default value is ``false`` .

      

    
    :type body: bytes or seekable file-like object
    :param body: **[REQUIRED]** 

      [Required] Raw byte array representing the to-be-imported documentation parts. To import from a Swagger file, this is a JSON object.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ids': [
                'string',
            ],
            'warnings': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A collection of the imported  DocumentationPart identifiers.

         This is used to return the result when documentation parts in an external (e.g., Swagger) file are imported into API Gateway  `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ , `documentationpart\:import <http://docs.aws.amazon.com/apigateway/api-reference/link-relation/documentationpart-import/>`__ ,  DocumentationPart  
        

        - **ids** *(list) --* 

          A list of the returned documentation part identifiers.

          
          

          - *(string) --* 
      
        

        - **warnings** *(list) --* 

          A list of warning messages reported during import of documentation parts.

          
          

          - *(string) --* 
      
    

  .. py:method:: import_rest_api(**kwargs)

    

    A feature of the API Gateway control service for creating a new API from an external API definition file.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/ImportRestApi>`_    


    **Request Syntax** 
    ::

      response = client.import_rest_api(
          failOnWarnings=True|False,
          parameters={
              'string': 'string'
          },
          body=b'bytes'|file
      )
    :type failOnWarnings: boolean
    :param failOnWarnings: 

      A query parameter to indicate whether to rollback the API creation (``true`` ) or not (``false`` ) when a warning is encountered. The default value is ``false`` .

      

    
    :type parameters: dict
    :param parameters: 

      A key-value map of context-specific query string parameters specifying the behavior of different API importing operations. The following shows operation-specific parameters and their supported values.

       

      To exclude  DocumentationParts from the import, set ``parameters`` as ``ignore=documentation`` .

       

      To configure the endpoint type, set ``parameters`` as ``endpointConfigurationTypes=EDGE`` or``endpointConfigurationTypes=REGIONAL`` . The default endpoint type is ``EDGE`` .

       

      To handle imported ``basePath`` , set ``parameters`` as ``basePath=ignore`` , ``basePath=prepend`` or ``basePath=split`` .

       

      For example, the AWS CLI command to exclude documentation from the imported API is:

       ``aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json``  

      The AWS CLI command to set the regional endpoint on the imported API is:

       ``aws apigateway import-rest-api --parameters endpointConfigurationTypes=REGIONAL --body 'file:///path/to/imported-api-body.json`` 

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type body: bytes or seekable file-like object
    :param body: **[REQUIRED]** 

      The POST request body containing external API definitions. Currently, only Swagger definition JSON files are supported. The maximum size of the API definition file is 2MB.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'warnings': [
                'string',
            ],
            'binaryMediaTypes': [
                'string',
            ],
            'endpointConfiguration': {
                'types': [
                    'REGIONAL'|'EDGE',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a REST API.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **id** *(string) --* 

          The API's identifier. This identifier is unique across all of your APIs in API Gateway.

          
        

        - **name** *(string) --* 

          The API's name.

          
        

        - **description** *(string) --* 

          The API's description.

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the API was created.

          
        

        - **version** *(string) --* 

          A version identifier for the API.

          
        

        - **warnings** *(list) --* 

          The warning messages reported when ``failonwarnings`` is turned on during API import.

          
          

          - *(string) --* 
      
        

        - **binaryMediaTypes** *(list) --* 

          The list of binary media types supported by the  RestApi . By default, the  RestApi supports only UTF-8-encoded text payloads.

          
          

          - *(string) --* 
      
        

        - **endpointConfiguration** *(dict) --* 

          The endpoint configuration of this  RestApi showing the endpoint types of the API. 

          
          

          - **types** *(list) --* 

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

            
            

            - *(string) --* 

              The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

              
        
      
    

  .. py:method:: put_gateway_response(**kwargs)

    

    Creates a customization of a  GatewayResponse of a specified response type and status code on the given  RestApi .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/PutGatewayResponse>`_    


    **Request Syntax** 
    ::

      response = client.put_gateway_response(
          restApiId='string',
          responseType='DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
          statusCode='string',
          responseParameters={
              'string': 'string'
          },
          responseTemplates={
              'string': 'string'
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type responseType: string
    :param responseType: **[REQUIRED]** 

      

      The response type of the associated  GatewayResponse . Valid values are 

      
      * ACCESS_DENIED
      
      * API_CONFIGURATION_ERROR
      
      * AUTHORIZER_FAILURE
      
      * AUTHORIZER_CONFIGURATION_ERROR
      
      * BAD_REQUEST_PARAMETERS
      
      * BAD_REQUEST_BODY
      
      * DEFAULT_4XX
      
      * DEFAULT_5XX
      
      * EXPIRED_TOKEN
      
      * INVALID_SIGNATURE
      
      * INTEGRATION_FAILURE
      
      * INTEGRATION_TIMEOUT
      
      * INVALID_API_KEY
      
      * MISSING_AUTHENTICATION_TOKEN
      
      * QUOTA_EXCEEDED
      
      * REQUEST_TOO_LARGE
      
      * RESOURCE_NOT_FOUND
      
      * THROTTLED
      
      * UNAUTHORIZED
      
      * UNSUPPORTED_MEDIA_TYPES
      

       

      

      

    
    :type statusCode: string
    :param statusCode: The HTTP status code of the  GatewayResponse .

    
    :type responseParameters: dict
    :param responseParameters: 

      

      Response parameters (paths, query strings and headers) of the  GatewayResponse as a string-to-string map of key-value pairs.

      

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type responseTemplates: dict
    :param responseTemplates: 

      

      Response templates of the  GatewayResponse as a string-to-string map of key-value pairs.

      

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'responseType': 'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
            'statusCode': 'string',
            'responseParameters': {
                'string': 'string'
            },
            'responseTemplates': {
                'string': 'string'
            },
            'defaultResponse': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        A gateway response of a given response type and status code, with optional response parameters and mapping templates.

         For more information about valid gateway response types, see `Gateway Response Types Supported by API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__   Example: Get a Gateway Response of a given response type Request 

        This example shows how to get a gateway response of the ``MISSING_AUTHNETICATION_TOKEN`` type.

         ``GET /restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN HTTP/1.1 Host: beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json X-Amz-Date: 20170503T202516Z Authorization: AWS4-HMAC-SHA256 Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=1b52460e3159c1a26cff29093855d50ea141c1c5b937528fecaf60f51129697a Cache-Control: no-cache Postman-Token: 3b2a1ce9-c848-2e26-2e2f-9c2caefbed45``  

        The response type is specified as a URL path.

         Response 

        The successful operation returns the ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html", "name": "gatewayresponse", "templated": true }, "self": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:delete": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } }, "defaultResponse": false, "responseParameters": { "gatewayresponse.header.x-request-path": "method.request.path.petId", "gatewayresponse.header.Access-Control-Allow-Origin": "'a.b.c'", "gatewayresponse.header.x-request-query": "method.request.querystring.q", "gatewayresponse.header.x-request-header": "method.request.header.Accept" }, "responseTemplates": { "application/json": "{\n \"message\": $context.error.messageString,\n \"type\": \"$context.error.responseType\",\n \"stage\": \"$context.stage\",\n \"resourcePath\": \"$context.resourcePath\",\n \"stageVariables.a\": \"$stageVariables.a\",\n \"statusCode\": \"'404'\"\n}" }, "responseType": "MISSING_AUTHENTICATION_TOKEN", "statusCode": "404" }``  

        

            `Customize Gateway Responses <http://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html>`__  
        

        - **responseType** *(string) --* 

          The response type of the associated  GatewayResponse . Valid values are 

          
          * ACCESS_DENIED
          
          * API_CONFIGURATION_ERROR
          
          * AUTHORIZER_FAILURE
          
          * AUTHORIZER_CONFIGURATION_ERROR
          
          * BAD_REQUEST_PARAMETERS
          
          * BAD_REQUEST_BODY
          
          * DEFAULT_4XX
          
          * DEFAULT_5XX
          
          * EXPIRED_TOKEN
          
          * INVALID_SIGNATURE
          
          * INTEGRATION_FAILURE
          
          * INTEGRATION_TIMEOUT
          
          * INVALID_API_KEY
          
          * MISSING_AUTHENTICATION_TOKEN
          
          * QUOTA_EXCEEDED
          
          * REQUEST_TOO_LARGE
          
          * RESOURCE_NOT_FOUND
          
          * THROTTLED
          
          * UNAUTHORIZED
          
          * UNSUPPORTED_MEDIA_TYPES
          

           

          
        

        - **statusCode** *(string) --* 

          The HTTP status code for this  GatewayResponse .

          
        

        - **responseParameters** *(dict) --* 

          Response parameters (paths, query strings and headers) of the  GatewayResponse as a string-to-string map of key-value pairs.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **responseTemplates** *(dict) --* 

          Response templates of the  GatewayResponse as a string-to-string map of key-value pairs.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **defaultResponse** *(boolean) --* 

          A Boolean flag to indicate whether this  GatewayResponse is the default gateway response (``true`` ) or not (``false`` ). A default gateway response is one generated by API Gateway without any customization by an API developer. 

          
    

  .. py:method:: put_integration(**kwargs)

    

    Sets up a method's integration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/PutIntegration>`_    


    **Request Syntax** 
    ::

      response = client.put_integration(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          type='HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
          integrationHttpMethod='string',
          uri='string',
          connectionType='INTERNET'|'VPC_LINK',
          connectionId='string',
          credentials='string',
          requestParameters={
              'string': 'string'
          },
          requestTemplates={
              'string': 'string'
          },
          passthroughBehavior='string',
          cacheNamespace='string',
          cacheKeyParameters=[
              'string',
          ],
          contentHandling='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
          timeoutInMillis=123
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Specifies a put integration request's resource ID.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies a put integration request's HTTP method.

      

    
    :type type: string
    :param type: **[REQUIRED]** 

      Specifies a put integration input's type.

      

    
    :type integrationHttpMethod: string
    :param integrationHttpMethod: 

      Specifies a put integration HTTP method. When the integration type is HTTP or AWS, this field is required.

      

    
    :type uri: string
    :param uri: 

      Specifies Uniform Resource Identifier (URI) of the integration endpoint.

       

       
      * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
       
      * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
      

      

    
    :type connectionType: string
    :param connectionType: 

      The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

      

    
    :type connectionId: string
    :param connectionId: 

      The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

      

    
    :type credentials: string
    :param credentials: 

      Specifies whether credentials are required for a put integration.

      

    
    :type requestParameters: dict
    :param requestParameters: 

      A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type requestTemplates: dict
    :param requestTemplates: 

      Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type passthroughBehavior: string
    :param passthroughBehavior: 

      Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the ``requestTemplates`` property on the Integration resource. There are three valid values: ``WHEN_NO_MATCH`` , ``WHEN_NO_TEMPLATES`` , and ``NEVER`` . 

       

       
      * ``WHEN_NO_MATCH`` passes the request body for unmapped content types through to the integration back end without transformation.
       
      * ``NEVER`` rejects unmapped content types with an HTTP 415 'Unsupported Media Type' response.
       
      * ``WHEN_NO_TEMPLATES`` allows pass-through when the integration has NO content types mapped to templates. However if there is at least one content type defined, unmapped content types will be rejected with the same 415 response.
       

      

    
    :type cacheNamespace: string
    :param cacheNamespace: 

      Specifies a put integration input's cache namespace.

      

    
    :type cacheKeyParameters: list
    :param cacheKeyParameters: 

      Specifies a put integration input's cache key parameters.

      

    
      - *(string) --* 

      
  
    :type contentHandling: string
    :param contentHandling: 

      Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

       

       
      * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
       
      * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
       

       

      If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

      

    
    :type timeoutInMillis: integer
    :param timeoutInMillis: 

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
            'httpMethod': 'string',
            'uri': 'string',
            'connectionType': 'INTERNET'|'VPC_LINK',
            'connectionId': 'string',
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
            'timeoutInMillis': 123,
            'cacheNamespace': 'string',
            'cacheKeyParameters': [
                'string',
            ],
            'integrationResponses': {
                'string': {
                    'statusCode': 'string',
                    'selectionPattern': 'string',
                    'responseParameters': {
                        'string': 'string'
                    },
                    'responseTemplates': {
                        'string': 'string'
                    },
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

         In the API Gateway console, the built-in Lambda integration is an AWS integration.  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **type** *(string) --* 

          Specifies an API method integration type. The valid value is one of the following:

           

           
          * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
           
          * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
           
          * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
           
          * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
           
          * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
           

           

          For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

          
        

        - **httpMethod** *(string) --* 

          Specifies the integration's HTTP method type.

          
        

        - **uri** *(string) --* 

          Specifies Uniform Resource Identifier (URI) of the integration endpoint.

           

           
          * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
           
          * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
          

          
        

        - **connectionType** *(string) --* 

          The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

          
        

        - **connectionId** *(string) --* 

          The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

          
        

        - **credentials** *(string) --* 

          Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

          
        

        - **requestParameters** *(dict) --* 

          A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **requestTemplates** *(dict) --* 

          Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **passthroughBehavior** *(string) --*  

          Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

           

           
          * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
           
          * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
           
          * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
           

           
        

        - **contentHandling** *(string) --* 

          Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

           

           
          * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
           
          * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
           

           

          If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

          
        

        - **timeoutInMillis** *(integer) --* 

          Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

          
        

        - **cacheNamespace** *(string) --* 

          Specifies the integration's cache namespace.

          
        

        - **cacheKeyParameters** *(list) --* 

          Specifies the integration's cache key parameters.

          
          

          - *(string) --* 
      
        

        - **integrationResponses** *(dict) --* 

          Specifies the integration's responses.

            

          

           Example: Get integration responses of a method Request 

          

           ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns ``200 OK`` status and a payload as follows:

           ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

          

             `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
              

              - **statusCode** *(string) --* 

                Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                
              

              - **selectionPattern** *(string) --* 

                Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                
              

              - **responseParameters** *(dict) --* 

                A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **responseTemplates** *(dict) --* 

                Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **contentHandling** *(string) --* 

                Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                 

                 
                * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                 
                * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                 

                 

                If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                
          
      
    
    

  .. py:method:: put_integration_response(**kwargs)

    

    Represents a put integration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/PutIntegrationResponse>`_    


    **Request Syntax** 
    ::

      response = client.put_integration_response(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          statusCode='string',
          selectionPattern='string',
          responseParameters={
              'string': 'string'
          },
          responseTemplates={
              'string': 'string'
          },
          contentHandling='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Specifies a put integration response request's resource identifier.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies a put integration response request's HTTP method.

      

    
    :type statusCode: string
    :param statusCode: **[REQUIRED]** 

      Specifies the status code that is used to map the integration response to an existing  MethodResponse .

      

    
    :type selectionPattern: string
    :param selectionPattern: 

      Specifies the selection pattern of a put integration response.

      

    
    :type responseParameters: dict
    :param responseParameters: 

      A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` must be a valid and unique response header name and ``JSON-expression`` a valid JSON expression without the ``$`` prefix.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type responseTemplates: dict
    :param responseTemplates: 

      Specifies a put integration response's templates.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type contentHandling: string
    :param contentHandling: 

      Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

       

       
      * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
       
      * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
       

       

      If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'statusCode': 'string',
            'selectionPattern': 'string',
            'responseParameters': {
                'string': 'string'
            },
            'responseTemplates': {
                'string': 'string'
            },
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

          `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **statusCode** *(string) --* 

          Specifies the status code that is used to map the integration response to an existing  MethodResponse .

          
        

        - **selectionPattern** *(string) --* 

          Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

          
        

        - **responseParameters** *(dict) --* 

          A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **responseTemplates** *(dict) --* 

          Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **contentHandling** *(string) --* 

          Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

           

           
          * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
           
          * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
           

           

          If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

          
    

  .. py:method:: put_method(**kwargs)

    

    Add a method to an existing  Resource resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/PutMethod>`_    


    **Request Syntax** 
    ::

      response = client.put_method(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          authorizationType='string',
          authorizerId='string',
          apiKeyRequired=True|False,
          operationName='string',
          requestParameters={
              'string': True|False
          },
          requestModels={
              'string': 'string'
          },
          requestValidatorId='string'
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The  Resource identifier for the new  Method resource.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies the method request's HTTP method type.

      

    
    :type authorizationType: string
    :param authorizationType: **[REQUIRED]** 

      The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

      

    
    :type authorizerId: string
    :param authorizerId: 

      Specifies the identifier of an  Authorizer to use on this Method, if the type is CUSTOM.

      

    
    :type apiKeyRequired: boolean
    :param apiKeyRequired: 

      Specifies whether the method required a valid  ApiKey .

      

    
    :type operationName: string
    :param operationName: 

      A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

      

    
    :type requestParameters: dict
    :param requestParameters: 

      A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key defines a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or body-mapping templates.

      

    
      - *(string) --* 

      
        - *(boolean) --* 

        
  

    :type requestModels: dict
    :param requestModels: 

      Specifies the  Model resources used for the request's content type. Request models are represented as a key/value map, with a content type as the key and a  Model name as the value.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type requestValidatorId: string
    :param requestValidatorId: 

      The identifier of a  RequestValidator for validating the method request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'httpMethod': 'string',
            'authorizationType': 'string',
            'authorizerId': 'string',
            'apiKeyRequired': True|False,
            'requestValidatorId': 'string',
            'operationName': 'string',
            'requestParameters': {
                'string': True|False
            },
            'requestModels': {
                'string': 'string'
            },
            'methodResponses': {
                'string': {
                    'statusCode': 'string',
                    'responseParameters': {
                        'string': True|False
                    },
                    'responseModels': {
                        'string': 'string'
                    }
                }
            },
            'methodIntegration': {
                'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                'httpMethod': 'string',
                'uri': 'string',
                'connectionType': 'INTERNET'|'VPC_LINK',
                'connectionId': 'string',
                'credentials': 'string',
                'requestParameters': {
                    'string': 'string'
                },
                'requestTemplates': {
                    'string': 'string'
                },
                'passthroughBehavior': 'string',
                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'timeoutInMillis': 123,
                'cacheNamespace': 'string',
                'cacheKeyParameters': [
                    'string',
                ],
                'integrationResponses': {
                    'string': {
                        'statusCode': 'string',
                        'selectionPattern': 'string',
                        'responseParameters': {
                            'string': 'string'
                        },
                        'responseTemplates': {
                            'string': 'string'
                        },
                        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a client-facing interface by which the client calls the API to access back-end resources. A **Method** resource is integrated with an  Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a **Method** resource, whereas an integration request is embodied in an  Integration resource. On the other hand, a method response is represented by a  MethodResponse resource, whereas an integration response is represented by an  IntegrationResponse resource. 

          

        

         Example: Retrive the GET method on a specified resource Request 

        The following example request retrieves the information about the GET method on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ). 

         ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

        The successful response returns a ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

        In the example above, the response template for the ``200 OK`` response maps the JSON output from the ``ListStreams`` action in the back end to an XML output. The mapping template is URL-encoded as ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`` and the output is decoded using the `$util.urlDecode() <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__ helper function.

            MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up an API's method <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__  
        

        - **httpMethod** *(string) --* 

          The method's HTTP verb.

          
        

        - **authorizationType** *(string) --* 

          The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

          
        

        - **authorizerId** *(string) --* 

          The identifier of an  Authorizer to use on this method. The ``authorizationType`` must be ``CUSTOM`` .

          
        

        - **apiKeyRequired** *(boolean) --* 

          A boolean flag specifying whether a valid  ApiKey is required to invoke this method.

          
        

        - **requestValidatorId** *(string) --* 

          The identifier of a  RequestValidator for request validation.

          
        

        - **operationName** *(string) --* 

          A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

          
        

        - **requestParameters** *(dict) --* 

          A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or templates.

          
          

          - *(string) --* 
            

            - *(boolean) --* 
      
    
        

        - **requestModels** *(dict) --* 

          A key-value map specifying data schemas, represented by  Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **methodResponses** *(dict) --* 

          Gets a method response associated with a given HTTP status code. 

            

          The collection of method responses are encapsulated in a key-value map, where the key is a response's HTTP status code and the value is a  MethodResponse resource that specifies the response returned to the caller from the back end through the integration response.

           Example: Get a 200 OK response of a GET method Request 

          

           ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns a ``200 OK`` status code and a payload similar to the following:

           ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }``  

          

             `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__  
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

                

              

               Example: A **MethodResponse** instance of an API Request 

              The example request retrieves a **MethodResponse** of the 200 status code.

               ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

              The successful response returns ``200 OK`` status and a payload as follows:

               ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

              

                  Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
              

              - **statusCode** *(string) --* 

                The method response's status code.

                
              

              - **responseParameters** *(dict) --* 

                A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

                
                

                - *(string) --* 
                  

                  - *(boolean) --* 
            
          
              

              - **responseModels** *(dict) --* 

                Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
      
    
        

        - **methodIntegration** *(dict) --* 

          Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.

            

          

           Example:  Request 

          

           ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns a ``200 OK`` status code and a payload similar to the following:

           ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }``  

          

             `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__  
          

          - **type** *(string) --* 

            Specifies an API method integration type. The valid value is one of the following:

             

             
            * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
             
            * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
             
            * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
             
            * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
             
            * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
             

             

            For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

            
          

          - **httpMethod** *(string) --* 

            Specifies the integration's HTTP method type.

            
          

          - **uri** *(string) --* 

            Specifies Uniform Resource Identifier (URI) of the integration endpoint.

             

             
            * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
             
            * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
            

            
          

          - **connectionType** *(string) --* 

            The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

            
          

          - **connectionId** *(string) --* 

            The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

            
          

          - **credentials** *(string) --* 

            Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

            
          

          - **requestParameters** *(dict) --* 

            A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **requestTemplates** *(dict) --* 

            Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **passthroughBehavior** *(string) --*  

            Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

             

             
            * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
             
            * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
             
            * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
             

             
          

          - **contentHandling** *(string) --* 

            Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

             

             
            * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
             
            * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
             

             

            If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

            
          

          - **timeoutInMillis** *(integer) --* 

            Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

            
          

          - **cacheNamespace** *(string) --* 

            Specifies the integration's cache namespace.

            
          

          - **cacheKeyParameters** *(list) --* 

            Specifies the integration's cache key parameters.

            
            

            - *(string) --* 
        
          

          - **integrationResponses** *(dict) --* 

            Specifies the integration's responses.

              

            

             Example: Get integration responses of a method Request 

            

             ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

            The successful response returns ``200 OK`` status and a payload as follows:

             ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

            

               `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
            

            - *(string) --* 
              

              - *(dict) --* 

                Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                

                - **statusCode** *(string) --* 

                  Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                  
                

                - **selectionPattern** *(string) --* 

                  Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                  
                

                - **responseParameters** *(dict) --* 

                  A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **responseTemplates** *(dict) --* 

                  Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **contentHandling** *(string) --* 

                  Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                   

                   
                  * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                   
                  * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                   

                   

                  If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                  
            
        
      
      
    

  .. py:method:: put_method_response(**kwargs)

    

    Adds a  MethodResponse to an existing  Method resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/PutMethodResponse>`_    


    **Request Syntax** 
    ::

      response = client.put_method_response(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          statusCode='string',
          responseParameters={
              'string': True|False
          },
          responseModels={
              'string': 'string'
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The  Resource identifier for the  Method resource.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      The HTTP verb of the  Method resource.

      

    
    :type statusCode: string
    :param statusCode: **[REQUIRED]** 

      The method response's status code.

      

    
    :type responseParameters: dict
    :param responseParameters: 

      A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header name and the associated value is a Boolean flag indicating whether the method response parameter is required or not. The method response header names must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The response parameter names defined here are available in the integration response to be mapped from an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

      

    
      - *(string) --* 

      
        - *(boolean) --* 

        
  

    :type responseModels: dict
    :param responseModels: 

      Specifies the  Model resources used for the response's content type. Response models are represented as a key/value map, with a content type as the key and a  Model name as the value.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'statusCode': 'string',
            'responseParameters': {
                'string': True|False
            },
            'responseModels': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

          

        

         Example: A **MethodResponse** instance of an API Request 

        The example request retrieves a **MethodResponse** of the 200 status code.

         ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

        The successful response returns ``200 OK`` status and a payload as follows:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

        

            Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **statusCode** *(string) --* 

          The method response's status code.

          
        

        - **responseParameters** *(dict) --* 

          A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

          
          

          - *(string) --* 
            

            - *(boolean) --* 
      
    
        

        - **responseModels** *(dict) --* 

          Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: put_rest_api(**kwargs)

    

    A feature of the API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/PutRestApi>`_    


    **Request Syntax** 
    ::

      response = client.put_rest_api(
          restApiId='string',
          mode='merge'|'overwrite',
          failOnWarnings=True|False,
          parameters={
              'string': 'string'
          },
          body=b'bytes'|file
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type mode: string
    :param mode: 

      The ``mode`` query parameter to specify the update mode. Valid values are "merge" and "overwrite". By default, the update mode is "merge".

      

    
    :type failOnWarnings: boolean
    :param failOnWarnings: 

      A query parameter to indicate whether to rollback the API update (``true`` ) or not (``false`` ) when a warning is encountered. The default value is ``false`` .

      

    
    :type parameters: dict
    :param parameters: 

      Custom header parameters as part of the request. For example, to exclude  DocumentationParts from an imported API, set ``ignore=documentation`` as a ``parameters`` value, as in the AWS CLI command of ``aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json`` .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type body: bytes or seekable file-like object
    :param body: **[REQUIRED]** 

      The PUT request body containing external API definitions. Currently, only Swagger definition JSON files are supported. The maximum size of the API definition file is 2MB.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'warnings': [
                'string',
            ],
            'binaryMediaTypes': [
                'string',
            ],
            'endpointConfiguration': {
                'types': [
                    'REGIONAL'|'EDGE',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a REST API.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **id** *(string) --* 

          The API's identifier. This identifier is unique across all of your APIs in API Gateway.

          
        

        - **name** *(string) --* 

          The API's name.

          
        

        - **description** *(string) --* 

          The API's description.

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the API was created.

          
        

        - **version** *(string) --* 

          A version identifier for the API.

          
        

        - **warnings** *(list) --* 

          The warning messages reported when ``failonwarnings`` is turned on during API import.

          
          

          - *(string) --* 
      
        

        - **binaryMediaTypes** *(list) --* 

          The list of binary media types supported by the  RestApi . By default, the  RestApi supports only UTF-8-encoded text payloads.

          
          

          - *(string) --* 
      
        

        - **endpointConfiguration** *(dict) --* 

          The endpoint configuration of this  RestApi showing the endpoint types of the API. 

          
          

          - **types** *(list) --* 

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

            
            

            - *(string) --* 

              The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

              
        
      
    

  .. py:method:: test_invoke_authorizer(**kwargs)

    

    Simulate the execution of an  Authorizer in your  RestApi with headers, parameters, and an incoming request body.

      `Enable custom authorizers <http://docs.aws.amazon.com/apigateway/latest/developerguide/use-custom-authorizer.html>`__  

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/TestInvokeAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.test_invoke_authorizer(
          restApiId='string',
          authorizerId='string',
          headers={
              'string': 'string'
          },
          pathWithQueryString='string',
          body='string',
          stageVariables={
              'string': 'string'
          },
          additionalContext={
              'string': 'string'
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type authorizerId: string
    :param authorizerId: **[REQUIRED]** 

      Specifies a test invoke authorizer request's  Authorizer ID.

      

    
    :type headers: dict
    :param headers: 

      [Required] A key-value map of headers to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, should be specified.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type pathWithQueryString: string
    :param pathWithQueryString: 

      [Optional] The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.

      

    
    :type body: string
    :param body: 

      [Optional] The simulated request body of an incoming invocation request.

      

    
    :type stageVariables: dict
    :param stageVariables: 

      A key-value map of stage variables to simulate an invocation on a deployed  Stage .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type additionalContext: dict
    :param additionalContext: 

      [Optional] A key-value map of additional context variables.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'clientStatus': 123,
            'log': 'string',
            'latency': 123,
            'principalId': 'string',
            'policy': 'string',
            'authorization': {
                'string': [
                    'string',
                ]
            },
            'claims': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response of the test invoke request for a custom  Authorizer 

        
        

        - **clientStatus** *(integer) --* 

          The HTTP status code that the client would have received. Value is 0 if the authorizer succeeded.

          
        

        - **log** *(string) --* 

          The API Gateway execution log for the test authorizer request.

          
        

        - **latency** *(integer) --* 

          The execution latency of the test authorizer request.

          
        

        - **principalId** *(string) --* 

          The principal identity returned by the  Authorizer 

          
        

        - **policy** *(string) --* 

          The JSON policy document returned by the  Authorizer 

          
        

        - **authorization** *(dict) --* 
          

          - *(string) --* 
            

            - *(list) --* 
              

              - *(string) --* 
          
      
    
        

        - **claims** *(dict) --* 

          The `open identity claims <http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims>`__ , with any supported custom attributes, returned from the Cognito Your User Pool configured for the API.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: test_invoke_method(**kwargs)

    

    Simulate the execution of a  Method in your  RestApi with headers, parameters, and an incoming request body.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/TestInvokeMethod>`_    


    **Request Syntax** 
    ::

      response = client.test_invoke_method(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          pathWithQueryString='string',
          body='string',
          headers={
              'string': 'string'
          },
          clientCertificateId='string',
          stageVariables={
              'string': 'string'
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Specifies a test invoke method request's resource ID.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies a test invoke method request's HTTP method.

      

    
    :type pathWithQueryString: string
    :param pathWithQueryString: 

      The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.

      

    
    :type body: string
    :param body: 

      The simulated request body of an incoming invocation request.

      

    
    :type headers: dict
    :param headers: 

      A key-value map of headers to simulate an incoming invocation request.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type clientCertificateId: string
    :param clientCertificateId: 

      A  ClientCertificate identifier to use in the test invocation. API Gateway will use the certificate when making the HTTPS request to the defined back-end endpoint.

      

    
    :type stageVariables: dict
    :param stageVariables: 

      A key-value map of stage variables to simulate an invocation on a deployed  Stage .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'status': 123,
            'body': 'string',
            'headers': {
                'string': 'string'
            },
            'log': 'string',
            'latency': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the response of the test invoke request in the HTTP method.

          `Test API using the API Gateway console <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-test-method.html#how-to-test-method-console>`__  
        

        - **status** *(integer) --* 

          The HTTP status code.

          
        

        - **body** *(string) --* 

          The body of the HTTP response.

          
        

        - **headers** *(dict) --* 

          The headers of the HTTP response.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **log** *(string) --* 

          The API Gateway execution log for the test invoke request.

          
        

        - **latency** *(integer) --* 

          The execution latency of the test invoke request.

          
    

  .. py:method:: update_account(**kwargs)

    

    Changes information about the current  Account resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateAccount>`_    


    **Request Syntax** 
    ::

      response = client.update_account(
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'cloudwatchRoleArn': 'string',
            'throttleSettings': {
                'burstLimit': 123,
                'rateLimit': 123.0
            },
            'features': [
                'string',
            ],
            'apiKeyVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an AWS account that is associated with API Gateway.

          

        To view the account info, call ``GET`` on this resource.

         Error Codes 

        The following exception may be thrown when the request fails.

         

         
        * UnauthorizedException
         
        * NotFoundException
         
        * TooManyRequestsException
         

         

        For detailed error code information, including the corresponding HTTP Status Codes, see `API Gateway Error Codes <http://docs.aws.amazon.com/apigateway/api-reference/handling-errors/#api-error-codes>`__ 

         Example: Get the information about an account. Request ``GET /account HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160531T184618Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

        The successful response returns a ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/account-apigateway-{rel}.html", "name": "account", "templated": true }, "self": { "href": "/account" }, "account:update": { "href": "/account" } }, "cloudwatchRoleArn": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "throttleSettings": { "rateLimit": 500, "burstLimit": 1000 } }``  

        In addition to making the REST API call directly, you can use the AWS CLI and an AWS SDK to access this resource.

           `API Gateway Limits <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-limits.html>`__  `Developer Guide <http://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>`__ , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-account.html>`__  
        

        - **cloudwatchRoleArn** *(string) --* 

          The ARN of an Amazon CloudWatch role for the current  Account . 

          
        

        - **throttleSettings** *(dict) --* 

          Specifies the API request limits configured for the current  Account .

          
          

          - **burstLimit** *(integer) --* 

            The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.

            
          

          - **rateLimit** *(float) --* 

            The API request steady-state rate limit.

            
      
        

        - **features** *(list) --* 

          A list of features supported for the account. When usage plans are enabled, the features list will include an entry of ``"UsagePlans"`` .

          
          

          - *(string) --* 
      
        

        - **apiKeyVersion** *(string) --* 

          The version of the API keys used for the account.

          
    

  .. py:method:: update_api_key(**kwargs)

    

    Changes information about an  ApiKey resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateApiKey>`_    


    **Request Syntax** 
    ::

      response = client.update_api_key(
          apiKey='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type apiKey: string
    :param apiKey: **[REQUIRED]** 

      The identifier of the  ApiKey resource to be updated.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'value': 'string',
            'name': 'string',
            'customerId': 'string',
            'description': 'string',
            'enabled': True|False,
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1),
            'stageKeys': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A resource that can be distributed to callers for executing  Method resources that require an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the callers with the API key can make requests to that stage.

          `Use API Keys <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__  
        

        - **id** *(string) --* 

          The identifier of the API Key.

          
        

        - **value** *(string) --* 

          The value of the API Key.

          
        

        - **name** *(string) --* 

          The name of the API Key.

          
        

        - **customerId** *(string) --* 

          An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

          
        

        - **description** *(string) --* 

          The description of the API Key.

          
        

        - **enabled** *(boolean) --* 

          Specifies whether the API Key can be used by callers.

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the API Key was created.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The timestamp when the API Key was last updated.

          
        

        - **stageKeys** *(list) --* 

          A list of  Stage resources that are associated with the  ApiKey resource.

          
          

          - *(string) --* 
      
    

  .. py:method:: update_authorizer(**kwargs)

    

    Updates an existing  Authorizer resource.

     `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/update-authorizer.html>`__ 

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.update_authorizer(
          restApiId='string',
          authorizerId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type authorizerId: string
    :param authorizerId: **[REQUIRED]** 

      The identifier of the  Authorizer resource.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
            'providerARNs': [
                'string',
            ],
            'authType': 'string',
            'authorizerUri': 'string',
            'authorizerCredentials': 'string',
            'identitySource': 'string',
            'identityValidationExpression': 'string',
            'authorizerResultTtlInSeconds': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an authorization layer for methods. If enabled on a method, API Gateway will activate the authorizer when a client calls the method.

          `Enable custom authorization <http://docs.aws.amazon.com/apigateway/latest/developerguide/use-custom-authorizer.html>`__  
        

        - **id** *(string) --* 

          The identifier for the authorizer resource.

          
        

        - **name** *(string) --* 

          [Required] The name of the authorizer.

          
        

        - **type** *(string) --* 

          [Required] The authorizer type. Valid values are ``TOKEN`` for a Lambda function using a single authorization token submitted in a custom header, ``REQUEST`` for a Lambda function using incoming request parameters, and ``COGNITO_USER_POOLS`` for using an Amazon Cognito user pool.

          
        

        - **providerARNs** *(list) --* 

          A list of the Amazon Cognito user pool ARNs for the ``COGNITO_USER_POOLS`` authorizer. Each element is of this format: ``arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`` . For a ``TOKEN`` or ``REQUEST`` authorizer, this is not defined. 

          
          

          - *(string) --* 
      
        

        - **authType** *(string) --* 

          Optional customer-defined field, used in Swagger imports and exports without functional impact.

          
        

        - **authorizerUri** *(string) --* 

          Specifies the authorizer's Uniform Resource Identifier (URI). For ``TOKEN`` or ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations`` . In general, the URI has this form ``arn:aws:apigateway:{region}:lambda:path/{service_api}`` , where ``{region}`` is the same as the region hosting the Lambda function, ``path`` indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``/`` . For Lambda functions, this is usually of the form ``/2015-03-31/functions/[FunctionARN]/invocations`` .

          
        

        - **authorizerCredentials** *(string) --* 

          Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.

          
        

        - **identitySource** *(string) --* 

          The identity source for which authorization is requested. 

          
          * For a ``TOKEN`` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is ``Auth`` , the header mapping expression is ``method.request.header.Auth`` .
          
          * For the ``REQUEST`` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an ``Auth`` header, a ``Name`` query string parameter are defined as identity sources, this value is ``method.request.header.Auth, method.request.querystring.Name`` . These parameters will be used to derive the authorization caching key and to perform runtime validation of the ``REQUEST`` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
          
          * For a ``COGNITO_USER_POOLS`` authorizer, this property is not used.
          

          

          
        

        - **identityValidationExpression** *(string) --* 

          A validation expression for the incoming identity token. For ``TOKEN`` authorizers, this value is a regular expression. API Gateway will match the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the ``REQUEST`` authorizer.

          
        

        - **authorizerResultTtlInSeconds** *(integer) --* 

          The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.

          
    

  .. py:method:: update_base_path_mapping(**kwargs)

    

    Changes information about the  BasePathMapping resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateBasePathMapping>`_    


    **Request Syntax** 
    ::

      response = client.update_base_path_mapping(
          domainName='string',
          basePath='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name of the  BasePathMapping resource to change.

      

    
    :type basePath: string
    :param basePath: **[REQUIRED]** 

      The base path of the  BasePathMapping resource to change.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'basePath': 'string',
            'restApiId': 'string',
            'stage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the base path that callers of the API must provide as part of the URL after the domain name.

         A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi in a given stage of the owner  Account .  `Use Custom Domain Names <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **basePath** *(string) --* 

          The base path name that callers of the API must provide as part of the URL after the domain name.

          
        

        - **restApiId** *(string) --* 

          The string identifier of the associated  RestApi .

          
        

        - **stage** *(string) --* 

          The name of the associated stage.

          
    

  .. py:method:: update_client_certificate(**kwargs)

    

    Changes information about an  ClientCertificate resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateClientCertificate>`_    


    **Request Syntax** 
    ::

      response = client.update_client_certificate(
          clientCertificateId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type clientCertificateId: string
    :param clientCertificateId: **[REQUIRED]** 

      The identifier of the  ClientCertificate resource to be updated.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'clientCertificateId': 'string',
            'description': 'string',
            'pemEncodedCertificate': 'string',
            'createdDate': datetime(2015, 1, 1),
            'expirationDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a client certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.

         Client certificates are used to authenticate an API by the backend server. To authenticate an API client (or user), use IAM roles and policies, a custom  Authorizer or an Amazon Cognito user pool.  `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__  
        

        - **clientCertificateId** *(string) --* 

          The identifier of the client certificate.

          
        

        - **description** *(string) --* 

          The description of the client certificate.

          
        

        - **pemEncodedCertificate** *(string) --* 

          The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the client certificate was created.

          
        

        - **expirationDate** *(datetime) --* 

          The timestamp when the client certificate will expire.

          
    

  .. py:method:: update_deployment(**kwargs)

    

    Changes information about a  Deployment resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateDeployment>`_    


    **Request Syntax** 
    ::

      response = client.update_deployment(
          restApiId='string',
          deploymentId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type deploymentId: string
    :param deploymentId: **[REQUIRED]** 

      The replacement identifier for the  Deployment resource to change information about.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'apiSummary': {
                'string': {
                    'string': {
                        'authorizationType': 'string',
                        'apiKeyRequired': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        An immutable representation of a  RestApi resource that can be called by users using  Stages . A deployment must be associated with a  Stage for it to be callable over the Internet.

         To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,  Deployments ,  Stage , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS SDKs <https://aws.amazon.com/tools/>`__  
        

        - **id** *(string) --* 

          The identifier for the deployment resource.

          
        

        - **description** *(string) --* 

          The description for the deployment resource.

          
        

        - **createdDate** *(datetime) --* 

          The date and time that the deployment resource was created.

          
        

        - **apiSummary** *(dict) --* 

          A summary of the  RestApi at the date and time that the deployment resource was created.

          
          

          - *(string) --* 
            

            - *(dict) --* 
              

              - *(string) --* 
                

                - *(dict) --* 

                  Represents a summary of a  Method resource, given a particular date and time.

                  
                  

                  - **authorizationType** *(string) --* 

                    The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                    
                  

                  - **apiKeyRequired** *(boolean) --* 

                    Specifies whether the method requires a valid  ApiKey .

                    
              
          
        
      
    
    

  .. py:method:: update_documentation_part(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateDocumentationPart>`_    


    **Request Syntax** 
    ::

      response = client.update_documentation_part(
          restApiId='string',
          documentationPartId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi .

      

    
    :type documentationPartId: string
    :param documentationPartId: **[REQUIRED]** 

      [Required] The identifier of the to-be-updated documentation part.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'location': {
                'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
                'path': 'string',
                'method': 'string',
                'statusCode': 'string',
                'name': 'string'
            },
            'properties': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A documentation part for a targeted API entity.

          

        A documentation part consists of a content map (``properties`` ) and a target (``location`` ). The target specifies an API entity to which the documentation content applies. The supported API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend on the API entity type. All valid fields are not required.

         

        The content map is a JSON string of API-specific key-value pairs. Although an API can use any shape for the content map, only the Swagger-compliant documentation fields will be injected into the associated API entity definition in the exported Swagger definition file.

          `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationParts  
        

        - **id** *(string) --* 

          The  DocumentationPart identifier, generated by API Gateway when the ``DocumentationPart`` is created.

          
        

        - **location** *(dict) --* 

          The location of the API entity to which the documentation applies. Valid fields depend on the targeted API entity type. All the valid location fields are not required. If not explicitly specified, a valid location field is treated as a wildcard and associated documentation content may be inherited by matching entities, unless overridden.

          
          

          - **type** *(string) --* 

            The type of API entity to which the documentation content applies. It is a valid and required field for API entity types of ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or ``RESOURCE`` type.

            
          

          - **path** *(string) --* 

            The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an applicable child entity inherits the content of another entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``path`` attribute must match that of the parent entity as a prefix.

            
          

          - **method** *(string) --* 

            The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any method. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``method`` attribute must match that of the parent entity exactly.

            
          

          - **statusCode** *(string) --* 

            The HTTP status code of a response. It is a valid field for the API entity types of ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any status code. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other ``location`` attributes, the child entity's ``statusCode`` attribute must match that of the parent entity exactly.

            
          

          - **name** *(string) --* 

            The name of the targeted API entity. It is a valid and required field for the API entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for any other entity type.

            
      
        

        - **properties** *(string) --* 

          A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., ``"{ \"description\": \"The API does ...\" }"`` . Only Swagger-compliant documentation-related fields from the propertiesmap are exported and, hence, published as part of the API entity definitions, while the original documentation parts are exported in a Swagger extension of ``x-amazon-apigateway-documentation`` .

          
    

  .. py:method:: update_documentation_version(**kwargs)

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateDocumentationVersion>`_    


    **Request Syntax** 
    ::

      response = client.update_documentation_version(
          restApiId='string',
          documentationVersion='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      [Required] The string identifier of the associated  RestApi ..

      

    
    :type documentationVersion: string
    :param documentationVersion: **[REQUIRED]** 

      [Required] The version identifier of the to-be-updated documentation version.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'version': 'string',
            'createdDate': datetime(2015, 1, 1),
            'description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A snapshot of the documentation of an API.

         

        Publishing API documentation involves creating a documentation version associated with an API stage and exporting the versioned documentation to an external (e.g., Swagger) file.

          `Documenting an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__ ,  DocumentationPart ,  DocumentationVersions  
        

        - **version** *(string) --* 

          The version identifier of the API documentation snapshot.

          
        

        - **createdDate** *(datetime) --* 

          The date when the API documentation snapshot is created.

          
        

        - **description** *(string) --* 

          The description of the API documentation snapshot.

          
    

  .. py:method:: update_domain_name(**kwargs)

    

    Changes information about the  DomainName resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateDomainName>`_    


    **Request Syntax** 
    ::

      response = client.update_domain_name(
          domainName='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The name of the  DomainName resource to be changed.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'domainName': 'string',
            'certificateName': 'string',
            'certificateArn': 'string',
            'certificateUploadDate': datetime(2015, 1, 1),
            'regionalDomainName': 'string',
            'regionalHostedZoneId': 'string',
            'regionalCertificateName': 'string',
            'regionalCertificateArn': 'string',
            'distributionDomainName': 'string',
            'distributionHostedZoneId': 'string',
            'endpointConfiguration': {
                'types': [
                    'REGIONAL'|'EDGE',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

          

        When you deploy an API, API Gateway creates a default host name for the API. This default API host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the default host name, you can access the API's root resource with the URL of ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a custom domain name of ``apis.example.com`` for this API, you can then access the same resource using the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path mapping ( BasePathMapping ) of your API under the custom domain name. 

           `Set a Custom Host Name for an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **domainName** *(string) --* 

          The name of the  DomainName resource.

          
        

        - **certificateName** *(string) --* 

          The name of the certificate that will be used by edge-optimized endpoint for this domain name.

          
        

        - **certificateArn** *(string) --* 

          The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

          
        

        - **certificateUploadDate** *(datetime) --* 

          The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

          
        

        - **regionalDomainName** *(string) --* 

          The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.

          
        

        - **regionalHostedZoneId** *(string) --* 

          The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

          
        

        - **regionalCertificateName** *(string) --* 

          The name of the certificate that will be used for validating the regional domain name.

          
        

        - **regionalCertificateArn** *(string) --* 

          The reference to an AWS-managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.

          
        

        - **distributionDomainName** *(string) --* 

          The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the `Amazon CloudFront documentation <http://aws.amazon.com/documentation/cloudfront/>`__ .

          
        

        - **distributionHostedZoneId** *(string) --* 

          The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is ``Z2FDTNDATAQYW2`` for all the regions. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

          
        

        - **endpointConfiguration** *(dict) --* 

          The endpoint configuration of this  DomainName showing the endpoint types of the domain name. 

          
          

          - **types** *(list) --* 

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

            
            

            - *(string) --* 

              The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

              
        
      
    

  .. py:method:: update_gateway_response(**kwargs)

    

    Updates a  GatewayResponse of a specified response type on the given  RestApi .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateGatewayResponse>`_    


    **Request Syntax** 
    ::

      response = client.update_gateway_response(
          restApiId='string',
          responseType='DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type responseType: string
    :param responseType: **[REQUIRED]** 

      

      The response type of the associated  GatewayResponse . Valid values are 

      
      * ACCESS_DENIED
      
      * API_CONFIGURATION_ERROR
      
      * AUTHORIZER_FAILURE
      
      * AUTHORIZER_CONFIGURATION_ERROR
      
      * BAD_REQUEST_PARAMETERS
      
      * BAD_REQUEST_BODY
      
      * DEFAULT_4XX
      
      * DEFAULT_5XX
      
      * EXPIRED_TOKEN
      
      * INVALID_SIGNATURE
      
      * INTEGRATION_FAILURE
      
      * INTEGRATION_TIMEOUT
      
      * INVALID_API_KEY
      
      * MISSING_AUTHENTICATION_TOKEN
      
      * QUOTA_EXCEEDED
      
      * REQUEST_TOO_LARGE
      
      * RESOURCE_NOT_FOUND
      
      * THROTTLED
      
      * UNAUTHORIZED
      
      * UNSUPPORTED_MEDIA_TYPES
      

       

      

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'responseType': 'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
            'statusCode': 'string',
            'responseParameters': {
                'string': 'string'
            },
            'responseTemplates': {
                'string': 'string'
            },
            'defaultResponse': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        A gateway response of a given response type and status code, with optional response parameters and mapping templates.

         For more information about valid gateway response types, see `Gateway Response Types Supported by API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__   Example: Get a Gateway Response of a given response type Request 

        This example shows how to get a gateway response of the ``MISSING_AUTHNETICATION_TOKEN`` type.

         ``GET /restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN HTTP/1.1 Host: beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json X-Amz-Date: 20170503T202516Z Authorization: AWS4-HMAC-SHA256 Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=1b52460e3159c1a26cff29093855d50ea141c1c5b937528fecaf60f51129697a Cache-Control: no-cache Postman-Token: 3b2a1ce9-c848-2e26-2e2f-9c2caefbed45``  

        The response type is specified as a URL path.

         Response 

        The successful operation returns the ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html", "name": "gatewayresponse", "templated": true }, "self": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:delete": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, "gatewayresponse:put": { "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } }, "defaultResponse": false, "responseParameters": { "gatewayresponse.header.x-request-path": "method.request.path.petId", "gatewayresponse.header.Access-Control-Allow-Origin": "'a.b.c'", "gatewayresponse.header.x-request-query": "method.request.querystring.q", "gatewayresponse.header.x-request-header": "method.request.header.Accept" }, "responseTemplates": { "application/json": "{\n \"message\": $context.error.messageString,\n \"type\": \"$context.error.responseType\",\n \"stage\": \"$context.stage\",\n \"resourcePath\": \"$context.resourcePath\",\n \"stageVariables.a\": \"$stageVariables.a\",\n \"statusCode\": \"'404'\"\n}" }, "responseType": "MISSING_AUTHENTICATION_TOKEN", "statusCode": "404" }``  

        

            `Customize Gateway Responses <http://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html>`__  
        

        - **responseType** *(string) --* 

          The response type of the associated  GatewayResponse . Valid values are 

          
          * ACCESS_DENIED
          
          * API_CONFIGURATION_ERROR
          
          * AUTHORIZER_FAILURE
          
          * AUTHORIZER_CONFIGURATION_ERROR
          
          * BAD_REQUEST_PARAMETERS
          
          * BAD_REQUEST_BODY
          
          * DEFAULT_4XX
          
          * DEFAULT_5XX
          
          * EXPIRED_TOKEN
          
          * INVALID_SIGNATURE
          
          * INTEGRATION_FAILURE
          
          * INTEGRATION_TIMEOUT
          
          * INVALID_API_KEY
          
          * MISSING_AUTHENTICATION_TOKEN
          
          * QUOTA_EXCEEDED
          
          * REQUEST_TOO_LARGE
          
          * RESOURCE_NOT_FOUND
          
          * THROTTLED
          
          * UNAUTHORIZED
          
          * UNSUPPORTED_MEDIA_TYPES
          

           

          
        

        - **statusCode** *(string) --* 

          The HTTP status code for this  GatewayResponse .

          
        

        - **responseParameters** *(dict) --* 

          Response parameters (paths, query strings and headers) of the  GatewayResponse as a string-to-string map of key-value pairs.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **responseTemplates** *(dict) --* 

          Response templates of the  GatewayResponse as a string-to-string map of key-value pairs.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **defaultResponse** *(boolean) --* 

          A Boolean flag to indicate whether this  GatewayResponse is the default gateway response (``true`` ) or not (``false`` ). A default gateway response is one generated by API Gateway without any customization by an API developer. 

          
    

  .. py:method:: update_integration(**kwargs)

    

    Represents an update integration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateIntegration>`_    


    **Request Syntax** 
    ::

      response = client.update_integration(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Represents an update integration request's resource identifier.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Represents an update integration request's HTTP method.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
            'httpMethod': 'string',
            'uri': 'string',
            'connectionType': 'INTERNET'|'VPC_LINK',
            'connectionId': 'string',
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
            'timeoutInMillis': 123,
            'cacheNamespace': 'string',
            'cacheKeyParameters': [
                'string',
            ],
            'integrationResponses': {
                'string': {
                    'statusCode': 'string',
                    'selectionPattern': 'string',
                    'responseParameters': {
                        'string': 'string'
                    },
                    'responseTemplates': {
                        'string': 'string'
                    },
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

         In the API Gateway console, the built-in Lambda integration is an AWS integration.  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **type** *(string) --* 

          Specifies an API method integration type. The valid value is one of the following:

           

           
          * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
           
          * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
           
          * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
           
          * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
           
          * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
           

           

          For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

          
        

        - **httpMethod** *(string) --* 

          Specifies the integration's HTTP method type.

          
        

        - **uri** *(string) --* 

          Specifies Uniform Resource Identifier (URI) of the integration endpoint.

           

           
          * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
           
          * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
          

          
        

        - **connectionType** *(string) --* 

          The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

          
        

        - **connectionId** *(string) --* 

          The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

          
        

        - **credentials** *(string) --* 

          Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

          
        

        - **requestParameters** *(dict) --* 

          A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **requestTemplates** *(dict) --* 

          Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **passthroughBehavior** *(string) --*  

          Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

           

           
          * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
           
          * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
           
          * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
           

           
        

        - **contentHandling** *(string) --* 

          Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

           

           
          * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
           
          * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
           

           

          If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

          
        

        - **timeoutInMillis** *(integer) --* 

          Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

          
        

        - **cacheNamespace** *(string) --* 

          Specifies the integration's cache namespace.

          
        

        - **cacheKeyParameters** *(list) --* 

          Specifies the integration's cache key parameters.

          
          

          - *(string) --* 
      
        

        - **integrationResponses** *(dict) --* 

          Specifies the integration's responses.

            

          

           Example: Get integration responses of a method Request 

          

           ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns ``200 OK`` status and a payload as follows:

           ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

          

             `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
              

              - **statusCode** *(string) --* 

                Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                
              

              - **selectionPattern** *(string) --* 

                Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                
              

              - **responseParameters** *(dict) --* 

                A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **responseTemplates** *(dict) --* 

                Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **contentHandling** *(string) --* 

                Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                 

                 
                * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                 
                * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                 

                 

                If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                
          
      
    
    

  .. py:method:: update_integration_response(**kwargs)

    

    Represents an update integration response.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateIntegrationResponse>`_    


    **Request Syntax** 
    ::

      response = client.update_integration_response(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          statusCode='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      Specifies an update integration response request's resource identifier.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      Specifies an update integration response request's HTTP method.

      

    
    :type statusCode: string
    :param statusCode: **[REQUIRED]** 

      Specifies an update integration response request's status code.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'statusCode': 'string',
            'selectionPattern': 'string',
            'responseParameters': {
                'string': 'string'
            },
            'responseTemplates': {
                'string': 'string'
            },
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

          `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **statusCode** *(string) --* 

          Specifies the status code that is used to map the integration response to an existing  MethodResponse .

          
        

        - **selectionPattern** *(string) --* 

          Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

          
        

        - **responseParameters** *(dict) --* 

          A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **responseTemplates** *(dict) --* 

          Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **contentHandling** *(string) --* 

          Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

           

           
          * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
           
          * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
           

           

          If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

          
    

  .. py:method:: update_method(**kwargs)

    

    Updates an existing  Method resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateMethod>`_    


    **Request Syntax** 
    ::

      response = client.update_method(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The  Resource identifier for the  Method resource.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      The HTTP verb of the  Method resource.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'httpMethod': 'string',
            'authorizationType': 'string',
            'authorizerId': 'string',
            'apiKeyRequired': True|False,
            'requestValidatorId': 'string',
            'operationName': 'string',
            'requestParameters': {
                'string': True|False
            },
            'requestModels': {
                'string': 'string'
            },
            'methodResponses': {
                'string': {
                    'statusCode': 'string',
                    'responseParameters': {
                        'string': True|False
                    },
                    'responseModels': {
                        'string': 'string'
                    }
                }
            },
            'methodIntegration': {
                'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                'httpMethod': 'string',
                'uri': 'string',
                'connectionType': 'INTERNET'|'VPC_LINK',
                'connectionId': 'string',
                'credentials': 'string',
                'requestParameters': {
                    'string': 'string'
                },
                'requestTemplates': {
                    'string': 'string'
                },
                'passthroughBehavior': 'string',
                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'timeoutInMillis': 123,
                'cacheNamespace': 'string',
                'cacheKeyParameters': [
                    'string',
                ],
                'integrationResponses': {
                    'string': {
                        'statusCode': 'string',
                        'selectionPattern': 'string',
                        'responseParameters': {
                            'string': 'string'
                        },
                        'responseTemplates': {
                            'string': 'string'
                        },
                        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a client-facing interface by which the client calls the API to access back-end resources. A **Method** resource is integrated with an  Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a **Method** resource, whereas an integration request is embodied in an  Integration resource. On the other hand, a method response is represented by a  MethodResponse resource, whereas an integration response is represented by an  IntegrationResponse resource. 

          

        

         Example: Retrive the GET method on a specified resource Request 

        The following example request retrieves the information about the GET method on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ). 

         ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

        The successful response returns a ``200 OK`` status code and a payload similar to the following:

         ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

        In the example above, the response template for the ``200 OK`` response maps the JSON output from the ``ListStreams`` action in the back end to an XML output. The mapping template is URL-encoded as ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`` and the output is decoded using the `$util.urlDecode() <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__ helper function.

            MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up an API's method <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__  
        

        - **httpMethod** *(string) --* 

          The method's HTTP verb.

          
        

        - **authorizationType** *(string) --* 

          The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

          
        

        - **authorizerId** *(string) --* 

          The identifier of an  Authorizer to use on this method. The ``authorizationType`` must be ``CUSTOM`` .

          
        

        - **apiKeyRequired** *(boolean) --* 

          A boolean flag specifying whether a valid  ApiKey is required to invoke this method.

          
        

        - **requestValidatorId** *(string) --* 

          The identifier of a  RequestValidator for request validation.

          
        

        - **operationName** *(string) --* 

          A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

          
        

        - **requestParameters** *(dict) --* 

          A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or templates.

          
          

          - *(string) --* 
            

            - *(boolean) --* 
      
    
        

        - **requestModels** *(dict) --* 

          A key-value map specifying data schemas, represented by  Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **methodResponses** *(dict) --* 

          Gets a method response associated with a given HTTP status code. 

            

          The collection of method responses are encapsulated in a key-value map, where the key is a response's HTTP status code and the value is a  MethodResponse resource that specifies the response returned to the caller from the back end through the integration response.

           Example: Get a 200 OK response of a GET method Request 

          

           ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns a ``200 OK`` status code and a payload similar to the following:

           ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }``  

          

             `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__  
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

                

              

               Example: A **MethodResponse** instance of an API Request 

              The example request retrieves a **MethodResponse** of the 200 status code.

               ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

              The successful response returns ``200 OK`` status and a payload as follows:

               ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

              

                  Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
              

              - **statusCode** *(string) --* 

                The method response's status code.

                
              

              - **responseParameters** *(dict) --* 

                A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

                
                

                - *(string) --* 
                  

                  - *(boolean) --* 
            
          
              

              - **responseModels** *(dict) --* 

                Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
      
    
        

        - **methodIntegration** *(dict) --* 

          Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.

            

          

           Example:  Request 

          

           ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

          The successful response returns a ``200 OK`` status code and a payload similar to the following:

           ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }``  

          

             `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__  
          

          - **type** *(string) --* 

            Specifies an API method integration type. The valid value is one of the following:

             

             
            * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
             
            * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
             
            * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
             
            * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
             
            * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
             

             

            For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

            
          

          - **httpMethod** *(string) --* 

            Specifies the integration's HTTP method type.

            
          

          - **uri** *(string) --* 

            Specifies Uniform Resource Identifier (URI) of the integration endpoint.

             

             
            * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
             
            * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
            

            
          

          - **connectionType** *(string) --* 

            The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

            
          

          - **connectionId** *(string) --* 

            The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

            
          

          - **credentials** *(string) --* 

            Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

            
          

          - **requestParameters** *(dict) --* 

            A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **requestTemplates** *(dict) --* 

            Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **passthroughBehavior** *(string) --*  

            Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

             

             
            * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
             
            * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
             
            * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
             

             
          

          - **contentHandling** *(string) --* 

            Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

             

             
            * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
             
            * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
             

             

            If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

            
          

          - **timeoutInMillis** *(integer) --* 

            Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

            
          

          - **cacheNamespace** *(string) --* 

            Specifies the integration's cache namespace.

            
          

          - **cacheKeyParameters** *(list) --* 

            Specifies the integration's cache key parameters.

            
            

            - *(string) --* 
        
          

          - **integrationResponses** *(dict) --* 

            Specifies the integration's responses.

              

            

             Example: Get integration responses of a method Request 

            

             ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

            The successful response returns ``200 OK`` status and a payload as follows:

             ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

            

               `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
            

            - *(string) --* 
              

              - *(dict) --* 

                Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                

                - **statusCode** *(string) --* 

                  Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                  
                

                - **selectionPattern** *(string) --* 

                  Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                  
                

                - **responseParameters** *(dict) --* 

                  A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **responseTemplates** *(dict) --* 

                  Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **contentHandling** *(string) --* 

                  Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                   

                   
                  * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                   
                  * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                   

                   

                  If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                  
            
        
      
      
    

  .. py:method:: update_method_response(**kwargs)

    

    Updates an existing  MethodResponse resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateMethodResponse>`_    


    **Request Syntax** 
    ::

      response = client.update_method_response(
          restApiId='string',
          resourceId='string',
          httpMethod='string',
          statusCode='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The  Resource identifier for the  MethodResponse resource.

      

    
    :type httpMethod: string
    :param httpMethod: **[REQUIRED]** 

      The HTTP verb of the  Method resource.

      

    
    :type statusCode: string
    :param statusCode: **[REQUIRED]** 

      The status code for the  MethodResponse resource.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'statusCode': 'string',
            'responseParameters': {
                'string': True|False
            },
            'responseModels': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

          

        

         Example: A **MethodResponse** instance of an API Request 

        The example request retrieves a **MethodResponse** of the 200 status code.

         ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

        The successful response returns ``200 OK`` status and a payload as follows:

         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

        

            Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **statusCode** *(string) --* 

          The method response's status code.

          
        

        - **responseParameters** *(dict) --* 

          A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

          
          

          - *(string) --* 
            

            - *(boolean) --* 
      
    
        

        - **responseModels** *(dict) --* 

          Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: update_model(**kwargs)

    

    Changes information about a model.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateModel>`_    


    **Request Syntax** 
    ::

      response = client.update_model(
          restApiId='string',
          modelName='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type modelName: string
    :param modelName: **[REQUIRED]** 

      The name of the model to update.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'schema': 'string',
            'contentType': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the data structure of a method's request or response payload.

          

        A request model defines the data structure of the client-supplied request payload. A response model defines the data structure of the response payload returned by the back end. Although not required, models are useful for mapping payloads between the front end and back end.

         

        A model is used for generating an API's SDK, validating the input request body, and creating a skeletal mapping template.

            Method ,  MethodResponse , `Models and Mappings <http://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__  
        

        - **id** *(string) --* 

          The identifier for the model resource.

          
        

        - **name** *(string) --* 

          The name of the model. Must be an alphanumeric string.

          
        

        - **description** *(string) --* 

          The description of the model.

          
        

        - **schema** *(string) --* 

          The schema for the model. For ``application/json`` models, this should be `JSON-schema draft v4 <http://json-schema.org/documentation.html>`__ model. Do not include "\*/" characters in the description of any properties because such "\*/" characters may be interpreted as the closing marker for comments in some languages, such as Java or JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

          
        

        - **contentType** *(string) --* 

          The content-type for the model.

          
    

  .. py:method:: update_request_validator(**kwargs)

    

    Updates a  RequestValidator of a given  RestApi .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateRequestValidator>`_    


    **Request Syntax** 
    ::

      response = client.update_request_validator(
          restApiId='string',
          requestValidatorId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type requestValidatorId: string
    :param requestValidatorId: **[REQUIRED]** 

      [Required] The identifier of  RequestValidator to be updated.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'validateRequestBody': True|False,
            'validateRequestParameters': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        A set of validation rules for incoming  Method requests.

          

        In Swagger, a  RequestValidator of an API is defined by the `x-amazon-apigateway-request-validators.requestValidator <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.requestValidator.html>`__ object. It the referenced using the `x-amazon-apigateway-request-validator <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validator>`__ property.

          `Enable Basic Request Validation in API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__ 
        

        - **id** *(string) --* 

          The identifier of this  RequestValidator .

          
        

        - **name** *(string) --* 

          The name of this  RequestValidator 

          
        

        - **validateRequestBody** *(boolean) --* 

          A Boolean flag to indicate whether to validate a request body according to the configured  Model schema.

          
        

        - **validateRequestParameters** *(boolean) --* 

          A Boolean flag to indicate whether to validate request parameters (``true`` ) or not (``false`` ).

          
    

  .. py:method:: update_resource(**kwargs)

    

    Changes information about a  Resource resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateResource>`_    


    **Request Syntax** 
    ::

      response = client.update_resource(
          restApiId='string',
          resourceId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The identifier of the  Resource resource.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'parentId': 'string',
            'pathPart': 'string',
            'path': 'string',
            'resourceMethods': {
                'string': {
                    'httpMethod': 'string',
                    'authorizationType': 'string',
                    'authorizerId': 'string',
                    'apiKeyRequired': True|False,
                    'requestValidatorId': 'string',
                    'operationName': 'string',
                    'requestParameters': {
                        'string': True|False
                    },
                    'requestModels': {
                        'string': 'string'
                    },
                    'methodResponses': {
                        'string': {
                            'statusCode': 'string',
                            'responseParameters': {
                                'string': True|False
                            },
                            'responseModels': {
                                'string': 'string'
                            }
                        }
                    },
                    'methodIntegration': {
                        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                        'httpMethod': 'string',
                        'uri': 'string',
                        'connectionType': 'INTERNET'|'VPC_LINK',
                        'connectionId': 'string',
                        'credentials': 'string',
                        'requestParameters': {
                            'string': 'string'
                        },
                        'requestTemplates': {
                            'string': 'string'
                        },
                        'passthroughBehavior': 'string',
                        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                        'timeoutInMillis': 123,
                        'cacheNamespace': 'string',
                        'cacheKeyParameters': [
                            'string',
                        ],
                        'integrationResponses': {
                            'string': {
                                'statusCode': 'string',
                                'selectionPattern': 'string',
                                'responseParameters': {
                                    'string': 'string'
                                },
                                'responseTemplates': {
                                    'string': 'string'
                                },
                                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                            }
                        }
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents an API resource.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **id** *(string) --* 

          The resource's identifier.

          
        

        - **parentId** *(string) --* 

          The parent resource's identifier.

          
        

        - **pathPart** *(string) --* 

          The last path segment for this resource.

          
        

        - **path** *(string) --* 

          The full path for this resource.

          
        

        - **resourceMethods** *(dict) --* 

          Gets an API resource's method of a given HTTP verb.

            

          The resource methods are a map of methods indexed by methods' HTTP verbs enabled on the resource. This method map is included in the ``200 OK`` response of the ``GET /restapis/{restapi_id}/resources/{resource_id}`` or ``GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods`` request.

           Example: Get the GET method of an API resource Request ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20170223T031827Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": false, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

          If the ``OPTIONS`` is enabled on the resource, you can follow the example here to get that method. Just replace the ``GET`` of the last path segment in the request URL with ``OPTIONS`` .

             
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents a client-facing interface by which the client calls the API to access back-end resources. A **Method** resource is integrated with an  Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a **Method** resource, whereas an integration request is embodied in an  Integration resource. On the other hand, a method response is represented by a  MethodResponse resource, whereas an integration response is represented by an  IntegrationResponse resource. 

                

              

               Example: Retrive the GET method on a specified resource Request 

              The following example request retrieves the information about the GET method on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ). 

               ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

              The successful response returns a ``200 OK`` status code and a payload similar to the following:

               ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

              In the example above, the response template for the ``200 OK`` response maps the JSON output from the ``ListStreams`` action in the back end to an XML output. The mapping template is URL-encoded as ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`` and the output is decoded using the `$util.urlDecode() <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__ helper function.

                  MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up an API's method <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__  
              

              - **httpMethod** *(string) --* 

                The method's HTTP verb.

                
              

              - **authorizationType** *(string) --* 

                The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                
              

              - **authorizerId** *(string) --* 

                The identifier of an  Authorizer to use on this method. The ``authorizationType`` must be ``CUSTOM`` .

                
              

              - **apiKeyRequired** *(boolean) --* 

                A boolean flag specifying whether a valid  ApiKey is required to invoke this method.

                
              

              - **requestValidatorId** *(string) --* 

                The identifier of a  RequestValidator for request validation.

                
              

              - **operationName** *(string) --* 

                A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

                
              

              - **requestParameters** *(dict) --* 

                A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or templates.

                
                

                - *(string) --* 
                  

                  - *(boolean) --* 
            
          
              

              - **requestModels** *(dict) --* 

                A key-value map specifying data schemas, represented by  Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **methodResponses** *(dict) --* 

                Gets a method response associated with a given HTTP status code. 

                  

                The collection of method responses are encapsulated in a key-value map, where the key is a response's HTTP status code and the value is a  MethodResponse resource that specifies the response returned to the caller from the back end through the integration response.

                 Example: Get a 200 OK response of a GET method Request 

                

                 ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                The successful response returns a ``200 OK`` status code and a payload similar to the following:

                 ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }``  

                

                   `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__  
                

                - *(string) --* 
                  

                  - *(dict) --* 

                    Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

                      

                    

                     Example: A **MethodResponse** instance of an API Request 

                    The example request retrieves a **MethodResponse** of the 200 status code.

                     ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                    The successful response returns ``200 OK`` status and a payload as follows:

                     ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

                    

                        Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                    

                    - **statusCode** *(string) --* 

                      The method response's status code.

                      
                    

                    - **responseParameters** *(dict) --* 

                      A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

                      
                      

                      - *(string) --* 
                        

                        - *(boolean) --* 
                  
                
                    

                    - **responseModels** *(dict) --* 

                      Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

                      
                      

                      - *(string) --* 
                        

                        - *(string) --* 
                  
                
                
            
          
              

              - **methodIntegration** *(dict) --* 

                Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.

                  

                

                 Example:  Request 

                

                 ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                The successful response returns a ``200 OK`` status code and a payload similar to the following:

                 ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }``  

                

                   `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__  
                

                - **type** *(string) --* 

                  Specifies an API method integration type. The valid value is one of the following:

                   

                   
                  * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
                   
                  * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
                   
                  * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
                   
                  * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
                   
                  * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
                   

                   

                  For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

                  
                

                - **httpMethod** *(string) --* 

                  Specifies the integration's HTTP method type.

                  
                

                - **uri** *(string) --* 

                  Specifies Uniform Resource Identifier (URI) of the integration endpoint.

                   

                   
                  * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
                   
                  * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
                  

                  
                

                - **connectionType** *(string) --* 

                  The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

                  
                

                - **connectionId** *(string) --* 

                  The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

                  
                

                - **credentials** *(string) --* 

                  Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

                  
                

                - **requestParameters** *(dict) --* 

                  A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **requestTemplates** *(dict) --* 

                  Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **passthroughBehavior** *(string) --*  

                  Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

                   

                   
                  * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
                   
                  * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
                   
                  * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
                   

                   
                

                - **contentHandling** *(string) --* 

                  Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                   

                   
                  * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
                   
                  * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
                   

                   

                  If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

                  
                

                - **timeoutInMillis** *(integer) --* 

                  Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

                  
                

                - **cacheNamespace** *(string) --* 

                  Specifies the integration's cache namespace.

                  
                

                - **cacheKeyParameters** *(list) --* 

                  Specifies the integration's cache key parameters.

                  
                  

                  - *(string) --* 
              
                

                - **integrationResponses** *(dict) --* 

                  Specifies the integration's responses.

                    

                  

                   Example: Get integration responses of a method Request 

                  

                   ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                  The successful response returns ``200 OK`` status and a payload as follows:

                   ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

                  

                     `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                  

                  - *(string) --* 
                    

                    - *(dict) --* 

                      Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                        `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                      

                      - **statusCode** *(string) --* 

                        Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                        
                      

                      - **selectionPattern** *(string) --* 

                        Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                        
                      

                      - **responseParameters** *(dict) --* 

                        A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                        
                        

                        - *(string) --* 
                          

                          - *(string) --* 
                    
                  
                      

                      - **responseTemplates** *(dict) --* 

                        Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                        
                        

                        - *(string) --* 
                          

                          - *(string) --* 
                    
                  
                      

                      - **contentHandling** *(string) --* 

                        Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                         

                         
                        * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                         
                        * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                         

                         

                        If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                        
                  
              
            
            
          
      
    
    

  .. py:method:: update_rest_api(**kwargs)

    

    Changes information about the specified API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateRestApi>`_    


    **Request Syntax** 
    ::

      response = client.update_rest_api(
          restApiId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'warnings': [
                'string',
            ],
            'binaryMediaTypes': [
                'string',
            ],
            'endpointConfiguration': {
                'types': [
                    'REGIONAL'|'EDGE',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a REST API.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **id** *(string) --* 

          The API's identifier. This identifier is unique across all of your APIs in API Gateway.

          
        

        - **name** *(string) --* 

          The API's name.

          
        

        - **description** *(string) --* 

          The API's description.

          
        

        - **createdDate** *(datetime) --* 

          The timestamp when the API was created.

          
        

        - **version** *(string) --* 

          A version identifier for the API.

          
        

        - **warnings** *(list) --* 

          The warning messages reported when ``failonwarnings`` is turned on during API import.

          
          

          - *(string) --* 
      
        

        - **binaryMediaTypes** *(list) --* 

          The list of binary media types supported by the  RestApi . By default, the  RestApi supports only UTF-8-encoded text payloads.

          
          

          - *(string) --* 
      
        

        - **endpointConfiguration** *(dict) --* 

          The endpoint configuration of this  RestApi showing the endpoint types of the API. 

          
          

          - **types** *(list) --* 

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

            
            

            - *(string) --* 

              The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

              
        
      
    

  .. py:method:: update_stage(**kwargs)

    

    Changes information about a  Stage resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateStage>`_    


    **Request Syntax** 
    ::

      response = client.update_stage(
          restApiId='string',
          stageName='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type stageName: string
    :param stageName: **[REQUIRED]** 

      The name of the  Stage resource to change information about.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'deploymentId': 'string',
            'clientCertificateId': 'string',
            'stageName': 'string',
            'description': 'string',
            'cacheClusterEnabled': True|False,
            'cacheClusterSize': '0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
            'cacheClusterStatus': 'CREATE_IN_PROGRESS'|'AVAILABLE'|'DELETE_IN_PROGRESS'|'NOT_AVAILABLE'|'FLUSH_IN_PROGRESS',
            'methodSettings': {
                'string': {
                    'metricsEnabled': True|False,
                    'loggingLevel': 'string',
                    'dataTraceEnabled': True|False,
                    'throttlingBurstLimit': 123,
                    'throttlingRateLimit': 123.0,
                    'cachingEnabled': True|False,
                    'cacheTtlInSeconds': 123,
                    'cacheDataEncrypted': True|False,
                    'requireAuthorizationForCacheControl': True|False,
                    'unauthorizedCacheControlHeaderStrategy': 'FAIL_WITH_403'|'SUCCEED_WITH_RESPONSE_HEADER'|'SUCCEED_WITHOUT_RESPONSE_HEADER'
                }
            },
            'variables': {
                'string': 'string'
            },
            'documentationVersion': 'string',
            'accessLogSettings': {
                'format': 'string',
                'destinationArn': 'string'
            },
            'canarySettings': {
                'percentTraffic': 123.0,
                'deploymentId': 'string',
                'stageVariableOverrides': {
                    'string': 'string'
                },
                'useStageCache': True|False
            },
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

          `Deploy an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__  
        

        - **deploymentId** *(string) --* 

          The identifier of the  Deployment that the stage points to.

          
        

        - **clientCertificateId** *(string) --* 

          The identifier of a client certificate for an API stage.

          
        

        - **stageName** *(string) --* 

          The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway.

          
        

        - **description** *(string) --* 

          The stage's description.

          
        

        - **cacheClusterEnabled** *(boolean) --* 

          Specifies whether a cache cluster is enabled for the stage.

          
        

        - **cacheClusterSize** *(string) --* 

          The size of the cache cluster for the stage, if enabled.

          
        

        - **cacheClusterStatus** *(string) --* 

          The status of the cache cluster for the stage, if enabled.

          
        

        - **methodSettings** *(dict) --* 

          A map that defines the method settings for a  Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\*/\*`` for overriding all methods in the stage. 

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Specifies the method setting properties.

              
              

              - **metricsEnabled** *(boolean) --* 

                Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a Boolean.

                
              

              - **loggingLevel** *(string) --* 

                Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` , ``ERROR`` , and ``INFO`` .

                
              

              - **dataTraceEnabled** *(boolean) --* 

                Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

                
              

              - **throttlingBurstLimit** *(integer) --* 

                Specifies the throttling burst limit. The PATCH path for this setting is ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

                
              

              - **throttlingRateLimit** *(float) --* 

                Specifies the throttling rate limit. The PATCH path for this setting is ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

                
              

              - **cachingEnabled** *(boolean) --* 

                Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached. The PATCH path for this setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

                
              

              - **cacheTtlInSeconds** *(integer) --* 

                Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached. The PATCH path for this setting is ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

                
              

              - **cacheDataEncrypted** *(boolean) --* 

                Specifies whether the cached responses are encrypted. The PATCH path for this setting is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

                
              

              - **requireAuthorizationForCacheControl** *(boolean) --* 

                Specifies whether authorization is required for a cache invalidation request. The PATCH path for this setting is ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value is a Boolean.

                
              

              - **unauthorizedCacheControlHeaderStrategy** *(string) --* 

                Specifies how to handle unauthorized requests for cache invalidation. The PATCH path for this setting is ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` , ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

                
          
      
    
        

        - **variables** *(dict) --* 

          A map that defines the stage variables for a  Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+`` .

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **documentationVersion** *(string) --* 

          The version of the associated API documentation.

          
        

        - **accessLogSettings** *(dict) --* 

          Settings for logging access in this stage.

          
          

          - **format** *(string) --* 

            A single line format of the access logs of data, as specified by selected `$context variables <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__ . The format must include at least ``$context.requestId`` .

            
          

          - **destinationArn** *(string) --* 

            The ARN of the CloudWatch Logs log group to receive access logs.

            
      
        

        - **canarySettings** *(dict) --* 

          Settings for the canary deployment in this stage.

          
          

          - **percentTraffic** *(float) --* 

            The percent (0-100) of traffic diverted to a canary deployment.

            
          

          - **deploymentId** *(string) --* 

            The ID of the canary deployment.

            
          

          - **stageVariableOverrides** *(dict) --* 

            Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **useStageCache** *(boolean) --* 

            A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

            
      
        

        - **createdDate** *(datetime) --* 

          The timestamp when the stage was created.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The timestamp when the stage last updated.

          
    

  .. py:method:: update_usage(**kwargs)

    

    Grants a temporary extension to the remaining quota of a usage plan associated with a specified API key.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateUsage>`_    


    **Request Syntax** 
    ::

      response = client.update_usage(
          usagePlanId='string',
          keyId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the usage plan associated with the usage data.

      

    
    :type keyId: string
    :param keyId: **[REQUIRED]** 

      The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'usagePlanId': 'string',
            'startDate': 'string',
            'endDate': 'string',
            'position': 'string',
            'items': {
                'string': [
                    [
                        123,
                    ],
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the usage data of a usage plan.

           `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__ , `Manage Usage in a Usage Plan <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans-with-console.html#api-gateway-usage-plan-manage-usage>`__  
        

        - **usagePlanId** *(string) --* 

          The plan Id associated with this usage data.

          
        

        - **startDate** *(string) --* 

          The starting date of the usage data.

          
        

        - **endDate** *(string) --* 

          The ending date of the usage data.

          
        

        - **position** *(string) --* 
        

        - **items** *(dict) --* 

          The usage data, as daily logs of used and remaining quotas, over the specified time interval indexed over the API keys in a usage plan. For example, ``{..., "values" : { "{api_key}" : [ [0, 100], [10, 90], [100, 10]]}`` , where ``{api_key}`` stands for an API key value and the daily log entry is of the format ``[used quota, remaining quota]`` .

          
          

          - *(string) --* 
            

            - *(list) --* 
              

              - *(list) --* 
                

                - *(integer) --* 
            
          
      
    
    

  .. py:method:: update_usage_plan(**kwargs)

    

    Updates a usage plan of a given plan Id.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateUsagePlan>`_    


    **Request Syntax** 
    ::

      response = client.update_usage_plan(
          usagePlanId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the to-be-updated usage plan.

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'apiStages': [
                {
                    'apiId': 'string',
                    'stage': 'string'
                },
            ],
            'throttle': {
                'burstLimit': 123,
                'rateLimit': 123.0
            },
            'quota': {
                'limit': 123,
                'offset': 123,
                'period': 'DAY'|'WEEK'|'MONTH'
            },
            'productCode': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a usage plan than can specify who can assess associated API stages with specified request limits and quotas.

          

        In a usage plan, you associate an API by specifying the API's Id and a stage name of the specified API. You add plan customers by adding API keys to the plan. 

           `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **id** *(string) --* 

          The identifier of a  UsagePlan resource.

          
        

        - **name** *(string) --* 

          The name of a usage plan.

          
        

        - **description** *(string) --* 

          The description of a usage plan.

          
        

        - **apiStages** *(list) --* 

          The associated API stages of a usage plan.

          
          

          - *(dict) --* 

            API stage name of the associated API stage in a usage plan.

            
            

            - **apiId** *(string) --* 

              API Id of the associated API stage in a usage plan.

              
            

            - **stage** *(string) --* 

              API stage name of the associated API stage in a usage plan.

              
        
      
        

        - **throttle** *(dict) --* 

          The request throttle limits of a usage plan.

          
          

          - **burstLimit** *(integer) --* 

            The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.

            
          

          - **rateLimit** *(float) --* 

            The API request steady-state rate limit.

            
      
        

        - **quota** *(dict) --* 

          The maximum number of permitted requests per a given unit time interval.

          
          

          - **limit** *(integer) --* 

            The maximum number of requests that can be made in a given time period.

            
          

          - **offset** *(integer) --* 

            The number of requests subtracted from the given limit in the initial time period.

            
          

          - **period** *(string) --* 

            The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".

            
      
        

        - **productCode** *(string) --* 

          The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

          
    

  .. py:method:: update_vpc_link(**kwargs)

    

    Updates an existing  VpcLink of a specified identifier.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateVpcLink>`_    


    **Request Syntax** 
    ::

      response = client.update_vpc_link(
          vpcLinkId='string',
          patchOperations=[
              {
                  'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                  'path': 'string',
                  'value': 'string',
                  'from': 'string'
              },
          ]
      )
    :type vpcLinkId: string
    :param vpcLinkId: **[REQUIRED]** 

      [Required] The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

      

    
    :type patchOperations: list
    :param patchOperations: 

      A list of update operations to be applied to the specified resource and in the order specified in this list.

      

    
      - *(dict) --* A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      
        - **op** *(string) --* 

          An update operation to be performed with this PATCH request. The valid value can be ``add`` , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.

          

        
        - **path** *(string) --* 

          The ``op`` operation's target, as identified by a `JSON Pointer <https://tools.ietf.org/html/draft-ietf-appsawg-json-pointer-08>`__ value that references a location within the targeted resource. For example, if the target resource has an updateable property of ``{"name":"value"}`` , the path for this property is ``/name`` . If the ``name`` property value is a JSON object (e.g., ``{"name": {"child/name": "child-value"}}`` ), the path for the ``child/name`` property will be ``/name/child~1name`` . Any slash ("/") character appearing in path names must be escaped with "~1", as shown in the example above. Each ``op`` operation can have only one ``path`` associated with it.

          

        
        - **value** *(string) --* 

          The new target value of the update operation. It is applicable for the ``add`` or ``replace`` operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{"a": ...}'. In a Windows shell, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ .

          

        
        - **from** *(string) --* 

          The ``copy`` update operation's source as identified by a ``JSON-Pointer`` value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a  Stage resource with ``"op":"copy"`` , ``"from":"/canarySettings/deploymentId"`` and ``"path":"/deploymentId"`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'targetArns': [
                'string',
            ],
            'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
            'statusMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud (VPC).

          

        

        To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway, you, as an API developer, create a  VpcLink resource targeted for one or more network load balancers of the VPC and then integrate an API method with a private integration that uses the  VpcLink . The private integraiton has an integration type of ``HTTP`` or ``HTTP_PROXY`` and has a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to identify the  VpcLink used.

         

         
        

        - **id** *(string) --* 

          The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

          
        

        - **name** *(string) --* 

          The name used to label and identify the VPC link.

          
        

        - **description** *(string) --* 

          The description of the VPC link.

          
        

        - **targetArns** *(list) --* 

          The ARNs of network load balancers of the VPC targeted by the VPC link. The network load balancers must be owned by the same AWS account of the API owner.

          
          

          - *(string) --* 
      
        

        - **status** *(string) --* 

          The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` , ``DELETING`` , or ``FAILED`` . Deploying an API will wait if the status is ``PENDING`` and will fail if the status is ``DELETING`` . 

          
        

        - **statusMessage** *(string) --* 

          A description about the VPC link status.

          
    

==========
Paginators
==========


The available paginators are:

* :py:class:`APIGateway.Paginator.GetApiKeys`


* :py:class:`APIGateway.Paginator.GetBasePathMappings`


* :py:class:`APIGateway.Paginator.GetClientCertificates`


* :py:class:`APIGateway.Paginator.GetDeployments`


* :py:class:`APIGateway.Paginator.GetDomainNames`


* :py:class:`APIGateway.Paginator.GetModels`


* :py:class:`APIGateway.Paginator.GetResources`


* :py:class:`APIGateway.Paginator.GetRestApis`


* :py:class:`APIGateway.Paginator.GetUsage`


* :py:class:`APIGateway.Paginator.GetUsagePlanKeys`


* :py:class:`APIGateway.Paginator.GetUsagePlans`


* :py:class:`APIGateway.Paginator.GetVpcLinks`



.. py:class:: APIGateway.Paginator.GetApiKeys

  ::

    
    paginator = client.get_paginator('get_api_keys')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_api_keys`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetApiKeys>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          nameQuery='string',
          customerId='string',
          includeValues=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type nameQuery: string
    :param nameQuery: 

      The name of queried API keys.

      

    
    :type customerId: string
    :param customerId: 

      The identifier of a customer in AWS Marketplace or an external system, such as a developer portal.

      

    
    :type includeValues: boolean
    :param includeValues: 

      A boolean flag to specify whether (``true`` ) or not (``false`` ) the result contains key values.

      

    
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
            'warnings': [
                'string',
            ],
            'items': [
                {
                    'id': 'string',
                    'value': 'string',
                    'name': 'string',
                    'customerId': 'string',
                    'description': 'string',
                    'enabled': True|False,
                    'createdDate': datetime(2015, 1, 1),
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'stageKeys': [
                        'string',
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of API keys as represented by an  ApiKeys resource.

          `Use API Keys <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__  
        

        - **warnings** *(list) --* 

          A list of warning messages logged during the import of API keys when the ``failOnWarnings`` option is set to true.

          
          

          - *(string) --* 
      
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            A resource that can be distributed to callers for executing  Method resources that require an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the callers with the API key can make requests to that stage.

              `Use API Keys <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__  
            

            - **id** *(string) --* 

              The identifier of the API Key.

              
            

            - **value** *(string) --* 

              The value of the API Key.

              
            

            - **name** *(string) --* 

              The name of the API Key.

              
            

            - **customerId** *(string) --* 

              An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

              
            

            - **description** *(string) --* 

              The description of the API Key.

              
            

            - **enabled** *(boolean) --* 

              Specifies whether the API Key can be used by callers.

              
            

            - **createdDate** *(datetime) --* 

              The timestamp when the API Key was created.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The timestamp when the API Key was last updated.

              
            

            - **stageKeys** *(list) --* 

              A list of  Stage resources that are associated with the  ApiKey resource.

              
              

              - *(string) --* 
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetBasePathMappings

  ::

    
    paginator = client.get_paginator('get_base_path_mappings')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_base_path_mappings`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetBasePathMappings>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          domainName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name of a  BasePathMapping resource.

      

    
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
            'items': [
                {
                    'basePath': 'string',
                    'restApiId': 'string',
                    'stage': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  BasePathMapping resources.

          `Use Custom Domain Names <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents the base path that callers of the API must provide as part of the URL after the domain name.

             A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi in a given stage of the owner  Account .  `Use Custom Domain Names <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
            

            - **basePath** *(string) --* 

              The base path name that callers of the API must provide as part of the URL after the domain name.

              
            

            - **restApiId** *(string) --* 

              The string identifier of the associated  RestApi .

              
            

            - **stage** *(string) --* 

              The name of the associated stage.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetClientCertificates

  ::

    
    paginator = client.get_paginator('get_client_certificates')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_client_certificates`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetClientCertificates>`_    


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
            'items': [
                {
                    'clientCertificateId': 'string',
                    'description': 'string',
                    'pemEncodedCertificate': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'expirationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  ClientCertificate resources.

          `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a client certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.

             Client certificates are used to authenticate an API by the backend server. To authenticate an API client (or user), use IAM roles and policies, a custom  Authorizer or an Amazon Cognito user pool.  `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__  
            

            - **clientCertificateId** *(string) --* 

              The identifier of the client certificate.

              
            

            - **description** *(string) --* 

              The description of the client certificate.

              
            

            - **pemEncodedCertificate** *(string) --* 

              The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .

              
            

            - **createdDate** *(datetime) --* 

              The timestamp when the client certificate was created.

              
            

            - **expirationDate** *(datetime) --* 

              The timestamp when the client certificate will expire.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetDeployments

  ::

    
    paginator = client.get_paginator('get_deployments')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_deployments`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDeployments>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          restApiId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
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
            'items': [
                {
                    'id': 'string',
                    'description': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'apiSummary': {
                        'string': {
                            'string': {
                                'authorizationType': 'string',
                                'apiKeyRequired': True|False
                            }
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection resource that contains zero or more references to your existing deployments, and links that guide you on how to interact with your collection. The collection offers a paginated view of the contained deployments.

         To create a new deployment of a  RestApi , make a ``POST`` request against this resource. To view, update, or delete an existing deployment, make a ``GET`` , ``PATCH`` , or ``DELETE`` request, respectively, on a specified  Deployment resource.  `Deploying an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__ , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS SDKs <https://aws.amazon.com/tools/>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            An immutable representation of a  RestApi resource that can be called by users using  Stages . A deployment must be associated with a  Stage for it to be callable over the Internet.

             To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,  Deployments ,  Stage , `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS SDKs <https://aws.amazon.com/tools/>`__  
            

            - **id** *(string) --* 

              The identifier for the deployment resource.

              
            

            - **description** *(string) --* 

              The description for the deployment resource.

              
            

            - **createdDate** *(datetime) --* 

              The date and time that the deployment resource was created.

              
            

            - **apiSummary** *(dict) --* 

              A summary of the  RestApi at the date and time that the deployment resource was created.

              
              

              - *(string) --* 
                

                - *(dict) --* 
                  

                  - *(string) --* 
                    

                    - *(dict) --* 

                      Represents a summary of a  Method resource, given a particular date and time.

                      
                      

                      - **authorizationType** *(string) --* 

                        The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                        
                      

                      - **apiKeyRequired** *(boolean) --* 

                        Specifies whether the method requires a valid  ApiKey .

                        
                  
              
            
          
        
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetDomainNames

  ::

    
    paginator = client.get_paginator('get_domain_names')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_domain_names`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDomainNames>`_    


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
            'items': [
                {
                    'domainName': 'string',
                    'certificateName': 'string',
                    'certificateArn': 'string',
                    'certificateUploadDate': datetime(2015, 1, 1),
                    'regionalDomainName': 'string',
                    'regionalHostedZoneId': 'string',
                    'regionalCertificateName': 'string',
                    'regionalCertificateArn': 'string',
                    'distributionDomainName': 'string',
                    'distributionHostedZoneId': 'string',
                    'endpointConfiguration': {
                        'types': [
                            'REGIONAL'|'EDGE',
                        ]
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  DomainName resources.

          `Use Client-Side Certificate <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

              

            When you deploy an API, API Gateway creates a default host name for the API. This default API host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the default host name, you can access the API's root resource with the URL of ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a custom domain name of ``apis.example.com`` for this API, you can then access the same resource using the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path mapping ( BasePathMapping ) of your API under the custom domain name. 

               `Set a Custom Host Name for an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__  
            

            - **domainName** *(string) --* 

              The name of the  DomainName resource.

              
            

            - **certificateName** *(string) --* 

              The name of the certificate that will be used by edge-optimized endpoint for this domain name.

              
            

            - **certificateArn** *(string) --* 

              The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

              
            

            - **certificateUploadDate** *(datetime) --* 

              The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

              
            

            - **regionalDomainName** *(string) --* 

              The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.

              
            

            - **regionalHostedZoneId** *(string) --* 

              The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

              
            

            - **regionalCertificateName** *(string) --* 

              The name of the certificate that will be used for validating the regional domain name.

              
            

            - **regionalCertificateArn** *(string) --* 

              The reference to an AWS-managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.

              
            

            - **distributionDomainName** *(string) --* 

              The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the `Amazon CloudFront documentation <http://aws.amazon.com/documentation/cloudfront/>`__ .

              
            

            - **distributionHostedZoneId** *(string) --* 

              The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is ``Z2FDTNDATAQYW2`` for all the regions. For more information, see `Set up a Regional Custom Domain Name <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__ and `AWS Regions and Endpoints for API Gateway <http://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ . 

              
            

            - **endpointConfiguration** *(dict) --* 

              The endpoint configuration of this  DomainName showing the endpoint types of the domain name. 

              
              

              - **types** *(list) --* 

                A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

                
                

                - *(string) --* 

                  The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetModels

  ::

    
    paginator = client.get_paginator('get_models')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_models`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetModels>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          restApiId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
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
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'description': 'string',
                    'schema': 'string',
                    'contentType': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  Model resources.

           Method ,  MethodResponse , `Models and Mappings <http://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents the data structure of a method's request or response payload.

              

            A request model defines the data structure of the client-supplied request payload. A response model defines the data structure of the response payload returned by the back end. Although not required, models are useful for mapping payloads between the front end and back end.

             

            A model is used for generating an API's SDK, validating the input request body, and creating a skeletal mapping template.

                Method ,  MethodResponse , `Models and Mappings <http://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__  
            

            - **id** *(string) --* 

              The identifier for the model resource.

              
            

            - **name** *(string) --* 

              The name of the model. Must be an alphanumeric string.

              
            

            - **description** *(string) --* 

              The description of the model.

              
            

            - **schema** *(string) --* 

              The schema for the model. For ``application/json`` models, this should be `JSON-schema draft v4 <http://json-schema.org/documentation.html>`__ model. Do not include "\*/" characters in the description of any properties because such "\*/" characters may be interpreted as the closing marker for comments in some languages, such as Java or JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

              
            

            - **contentType** *(string) --* 

              The content-type for the model.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetResources

  ::

    
    paginator = client.get_paginator('get_resources')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_resources`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetResources>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          restApiId='string',
          embed=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type restApiId: string
    :param restApiId: **[REQUIRED]** 

      The string identifier of the associated  RestApi .

      

    
    :type embed: list
    :param embed: 

      A query parameter used to retrieve the specified resources embedded in the returned  Resources resource in the response. This ``embed`` parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded  Method resources this way. The query parameter value must be a single-valued list and contain the ``"methods"`` string. For example, ``GET /restapis/{restapi_id}/resources?embed=methods`` .

      

    
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
            'items': [
                {
                    'id': 'string',
                    'parentId': 'string',
                    'pathPart': 'string',
                    'path': 'string',
                    'resourceMethods': {
                        'string': {
                            'httpMethod': 'string',
                            'authorizationType': 'string',
                            'authorizerId': 'string',
                            'apiKeyRequired': True|False,
                            'requestValidatorId': 'string',
                            'operationName': 'string',
                            'requestParameters': {
                                'string': True|False
                            },
                            'requestModels': {
                                'string': 'string'
                            },
                            'methodResponses': {
                                'string': {
                                    'statusCode': 'string',
                                    'responseParameters': {
                                        'string': True|False
                                    },
                                    'responseModels': {
                                        'string': 'string'
                                    }
                                }
                            },
                            'methodIntegration': {
                                'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                                'httpMethod': 'string',
                                'uri': 'string',
                                'connectionType': 'INTERNET'|'VPC_LINK',
                                'connectionId': 'string',
                                'credentials': 'string',
                                'requestParameters': {
                                    'string': 'string'
                                },
                                'requestTemplates': {
                                    'string': 'string'
                                },
                                'passthroughBehavior': 'string',
                                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                                'timeoutInMillis': 123,
                                'cacheNamespace': 'string',
                                'cacheKeyParameters': [
                                    'string',
                                ],
                                'integrationResponses': {
                                    'string': {
                                        'statusCode': 'string',
                                        'selectionPattern': 'string',
                                        'responseParameters': {
                                            'string': 'string'
                                        },
                                        'responseTemplates': {
                                            'string': 'string'
                                        },
                                        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                                    }
                                }
                            }
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of  Resource resources.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents an API resource.

              `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
            

            - **id** *(string) --* 

              The resource's identifier.

              
            

            - **parentId** *(string) --* 

              The parent resource's identifier.

              
            

            - **pathPart** *(string) --* 

              The last path segment for this resource.

              
            

            - **path** *(string) --* 

              The full path for this resource.

              
            

            - **resourceMethods** *(dict) --* 

              Gets an API resource's method of a given HTTP verb.

                

              The resource methods are a map of methods indexed by methods' HTTP verbs enabled on the resource. This method map is included in the ``200 OK`` response of the ``GET /restapis/{restapi_id}/resources/{resource_id}`` or ``GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods`` request.

               Example: Get the GET method of an API resource Request ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20170223T031827Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": false, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

              If the ``OPTIONS`` is enabled on the resource, you can follow the example here to get that method. Just replace the ``GET`` of the last path segment in the request URL with ``OPTIONS`` .

                 
              

              - *(string) --* 
                

                - *(dict) --* 

                  Represents a client-facing interface by which the client calls the API to access back-end resources. A **Method** resource is integrated with an  Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a **Method** resource, whereas an integration request is embodied in an  Integration resource. On the other hand, a method response is represented by a  MethodResponse resource, whereas an integration response is represented by an  IntegrationResponse resource. 

                    

                  

                   Example: Retrive the GET method on a specified resource Request 

                  The following example request retrieves the information about the GET method on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ). 

                   ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                  The successful response returns a ``200 OK`` status code and a payload similar to the following:

                   ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html", "name": "method", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true } ], "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title": "GET" }, "integration:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "method:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "method:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}", "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE", "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integration:responses": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": { "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" }, "requestTemplates": { "application/json": "{\n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\")" }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name": "200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" } } }``  

                  In the example above, the response template for the ``200 OK`` response maps the JSON output from the ``ListStreams`` action in the back end to an XML output. The mapping template is URL-encoded as ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E`` and the output is decoded using the `$util.urlDecode() <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__ helper function.

                      MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up an API's method <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__  
                  

                  - **httpMethod** *(string) --* 

                    The method's HTTP verb.

                    
                  

                  - **authorizationType** *(string) --* 

                    The method's authorization type. Valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                    
                  

                  - **authorizerId** *(string) --* 

                    The identifier of an  Authorizer to use on this method. The ``authorizationType`` must be ``CUSTOM`` .

                    
                  

                  - **apiKeyRequired** *(boolean) --* 

                    A boolean flag specifying whether a valid  ApiKey is required to invoke this method.

                    
                  

                  - **requestValidatorId** *(string) --* 

                    The identifier of a  RequestValidator for request validation.

                    
                  

                  - **operationName** *(string) --* 

                    A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in `PetStore <http://petstore-demo-endpoint.execute-api.com/petstore/pets>`__ example.

                    
                  

                  - **requestParameters** *(dict) --* 

                    A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true`` ) or optional (``false`` ). The method request parameter names defined here are available in  Integration to be mapped to integration request parameters or templates.

                    
                    

                    - *(string) --* 
                      

                      - *(boolean) --* 
                
              
                  

                  - **requestModels** *(dict) --* 

                    A key-value map specifying data schemas, represented by  Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).

                    
                    

                    - *(string) --* 
                      

                      - *(string) --* 
                
              
                  

                  - **methodResponses** *(dict) --* 

                    Gets a method response associated with a given HTTP status code. 

                      

                    The collection of method responses are encapsulated in a key-value map, where the key is a response's HTTP status code and the value is a  MethodResponse resource that specifies the response returned to the caller from the back end through the integration response.

                     Example: Get a 200 OK response of a GET method Request 

                    

                     ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T215008Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                    The successful response returns a ``200 OK`` status code and a payload similar to the following:

                     ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.operator": false, "method.response.header.operand_2": false, "method.response.header.operand_1": false }, "statusCode": "200" }``  

                    

                       `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__  
                    

                    - *(string) --* 
                      

                      - *(dict) --* 

                        Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template. 

                          

                        

                         Example: A **MethodResponse** instance of an API Request 

                        The example request retrieves a **MethodResponse** of the 200 status code.

                         ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                        The successful response returns ``200 OK`` status and a payload as follows:

                         ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html", "name": "methodresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" }, "methodresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }, "methodresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": { "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type": false }, "statusCode": "200" }``  

                        

                            Method ,  IntegrationResponse ,  Integration  `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                        

                        - **statusCode** *(string) --* 

                          The method response's status code.

                          
                        

                        - **responseParameters** *(dict) --* 

                          A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's  IntegrationResponse . The integration response data that can be mapped include an integration response header expressed in ``integration.response.header.{name}`` , a static value enclosed within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the back-end response payload in the form of ``integration.response.body.{JSON-expression}`` , where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

                          
                          

                          - *(string) --* 
                            

                            - *(boolean) --* 
                      
                    
                        

                        - **responseModels** *(dict) --* 

                          Specifies the  Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a  Model name as the value.

                          
                          

                          - *(string) --* 
                            

                            - *(string) --* 
                      
                    
                    
                
              
                  

                  - **methodIntegration** *(dict) --* 

                    Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.

                      

                    

                     Example:  Request 

                    

                     ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date: 20160613T213210Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                    The successful response returns a ``200 OK`` status code and a payload similar to the following:

                     ``{ "_links": { "curies": [ { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html", "name": "integration", "templated": true }, { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true } ], "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integration:responses": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integration:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" }, "integrationresponse:put": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}", "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestTemplates": { "application/json": "{\n \"a\": \"$input.params('operand1')\",\n \"b\": \"$input.params('operand2')\", \n \"op\": \"$input.params('operator')\" \n}" }, "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations", "_embedded": { "integration:responses": { "_links": { "self": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200", "name": "200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.operator": "integration.response.body.op", "method.response.header.operand_2": "integration.response.body.b", "method.response.header.operand_1": "integration.response.body.a" }, "responseTemplates": { "application/json": "#set($res = $input.path('$'))\n{\n \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n \"a\" : \"$res.a\",\n \"b\" : \"$res.b\",\n \"op\" : \"$res.op\",\n \"c\" : \"$res.c\"\n}" }, "selectionPattern": "", "statusCode": "200" } } }``  

                    

                       `AWS CLI <http://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__  
                    

                    - **type** *(string) --* 

                      Specifies an API method integration type. The valid value is one of the following:

                       

                       
                      * ``AWS`` : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
                       
                      * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
                       
                      * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
                       
                      * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
                       
                      * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
                       

                       

                      For the HTTP and HTTP proxy integrations, each integration can specify a protocol (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a private integration and uses a  VpcLink to connect API Gateway to a network load balancer of a VPC.

                      
                    

                    - **httpMethod** *(string) --* 

                      Specifies the integration's HTTP method type.

                      
                    

                    - **uri** *(string) --* 

                      Specifies Uniform Resource Identifier (URI) of the integration endpoint.

                       

                       
                      * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for routing.  
                       
                      * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The ensuing ``service_api`` refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of ```GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the ``uri`` can be either ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``  
                      

                      
                    

                    - **connectionType** *(string) --* 

                      The type of the network connection to the integration endpoint. The valid value is ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and an network load balancer in a VPC. The default value is ``INTERNET`` .

                      
                    

                    - **connectionId** *(string) --* 

                      The (```id`` <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined, otherwise.

                      
                    

                    - **credentials** *(string) --* 

                      Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::\*:user/\*`` . To use resource-based permissions on supported AWS services, specify null.

                      
                    

                    - **requestParameters** *(dict) --* 

                      A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter name.

                      
                      

                      - *(string) --* 
                        

                        - *(string) --* 
                  
                
                    

                    - **requestTemplates** *(dict) --* 

                      Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.

                      
                      

                      - *(string) --* 
                        

                        - *(string) --* 
                  
                
                    

                    - **passthroughBehavior** *(string) --*  

                      Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in ``requestTemplates`` . The valid value is one of the following: 

                       

                       
                      * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. 
                       
                      * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response. 
                       
                      * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request. 
                       

                       
                    

                    - **contentHandling** *(string) --* 

                      Specifies how to handle request payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                       

                       
                      * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
                       
                      * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded string.
                       

                       

                      If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the ``passthroughBehaviors`` is configured to support payload pass-through.

                      
                    

                    - **timeoutInMillis** *(integer) --* 

                      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

                      
                    

                    - **cacheNamespace** *(string) --* 

                      Specifies the integration's cache namespace.

                      
                    

                    - **cacheKeyParameters** *(list) --* 

                      Specifies the integration's cache key parameters.

                      
                      

                      - *(string) --* 
                  
                    

                    - **integrationResponses** *(dict) --* 

                      Specifies the integration's responses.

                        

                      

                       Example: Get integration responses of a method Request 

                      

                       ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200 HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response 

                      The successful response returns ``200 OK`` status and a payload as follows:

                       ``{ "_links": { "curies": { "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html", "name": "integrationresponse", "templated": true }, "self": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title": "200" }, "integrationresponse:delete": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" }, "integrationresponse:update": { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } }, "responseParameters": { "method.response.header.Content-Type": "'application/xml'" }, "responseTemplates": { "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n" }, "statusCode": "200" }``  

                      

                         `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                      

                      - *(string) --* 
                        

                        - *(dict) --* 

                          Represents an integration response. The status code must map to an existing  MethodResponse , and parameters and templates can be used to transform the back-end response.

                            `Creating an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
                          

                          - **statusCode** *(string) --* 

                            Specifies the status code that is used to map the integration response to an existing  MethodResponse .

                            
                          

                          - **selectionPattern** *(string) --* 

                            Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the ``.+`` regex to match error response. However, make sure that the error response does not contain any newline (``\n`` ) character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function error header is matched. For all other HTTP and AWS back ends, the HTTP status code is matched.

                            
                          

                          - **responseParameters** *(dict) --* 

                            A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique response header name and ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.

                            
                            

                            - *(string) --* 
                              

                              - *(string) --* 
                        
                      
                          

                          - **responseTemplates** *(dict) --* 

                            Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

                            
                            

                            - *(string) --* 
                              

                              - *(string) --* 
                        
                      
                          

                          - **contentHandling** *(string) --* 

                            Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

                             

                             
                            * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                             
                            * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.
                             

                             

                            If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

                            
                      
                  
                
                
              
          
        
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetRestApis

  ::

    
    paginator = client.get_paginator('get_rest_apis')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_rest_apis`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetRestApis>`_    


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
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'description': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'version': 'string',
                    'warnings': [
                        'string',
                    ],
                    'binaryMediaTypes': [
                        'string',
                    ],
                    'endpointConfiguration': {
                        'types': [
                            'REGIONAL'|'EDGE',
                        ]
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains references to your APIs and links that guide you in how to interact with your collection. A collection offers a paginated view of your APIs.

          `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a REST API.

              `Create an API <http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__  
            

            - **id** *(string) --* 

              The API's identifier. This identifier is unique across all of your APIs in API Gateway.

              
            

            - **name** *(string) --* 

              The API's name.

              
            

            - **description** *(string) --* 

              The API's description.

              
            

            - **createdDate** *(datetime) --* 

              The timestamp when the API was created.

              
            

            - **version** *(string) --* 

              A version identifier for the API.

              
            

            - **warnings** *(list) --* 

              The warning messages reported when ``failonwarnings`` is turned on during API import.

              
              

              - *(string) --* 
          
            

            - **binaryMediaTypes** *(list) --* 

              The list of binary media types supported by the  RestApi . By default, the  RestApi supports only UTF-8-encoded text payloads.

              
              

              - *(string) --* 
          
            

            - **endpointConfiguration** *(dict) --* 

              The endpoint configuration of this  RestApi showing the endpoint types of the API. 

              
              

              - **types** *(list) --* 

                A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is ``REGIONAL`` .

                
                

                - *(string) --* 

                  The endpoint type. The valid value is ``EDGE`` for edge-optimized API setup, most suitable for mobile applications, ``REGIONAL`` for regional API endpoint setup, most suitable for calling from AWS Region

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetUsage

  ::

    
    paginator = client.get_paginator('get_usage')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_usage`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsage>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          usagePlanId='string',
          keyId='string',
          startDate='string',
          endDate='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the usage plan associated with the usage data.

      

    
    :type keyId: string
    :param keyId: 

      The Id of the API key associated with the resultant usage data.

      

    
    :type startDate: string
    :param startDate: **[REQUIRED]** 

      The starting date (e.g., 2016-01-01) of the usage data.

      

    
    :type endDate: string
    :param endDate: **[REQUIRED]** 

      The ending date (e.g., 2016-12-31) of the usage data.

      

    
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
            'usagePlanId': 'string',
            'startDate': 'string',
            'endDate': 'string',
            'items': {
                'string': [
                    [
                        123,
                    ],
                ]
            },
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the usage data of a usage plan.

           `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__ , `Manage Usage in a Usage Plan <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans-with-console.html#api-gateway-usage-plan-manage-usage>`__  
        

        - **usagePlanId** *(string) --* 

          The plan Id associated with this usage data.

          
        

        - **startDate** *(string) --* 

          The starting date of the usage data.

          
        

        - **endDate** *(string) --* 

          The ending date of the usage data.

          
        

        - **items** *(dict) --* 

          The usage data, as daily logs of used and remaining quotas, over the specified time interval indexed over the API keys in a usage plan. For example, ``{..., "values" : { "{api_key}" : [ [0, 100], [10, 90], [100, 10]]}`` , where ``{api_key}`` stands for an API key value and the daily log entry is of the format ``[used quota, remaining quota]`` .

          
          

          - *(string) --* 
            

            - *(list) --* 
              

              - *(list) --* 
                

                - *(integer) --* 
            
          
      
    
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetUsagePlanKeys

  ::

    
    paginator = client.get_paginator('get_usage_plan_keys')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_usage_plan_keys`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsagePlanKeys>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          usagePlanId='string',
          nameQuery='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type usagePlanId: string
    :param usagePlanId: **[REQUIRED]** 

      The Id of the  UsagePlan resource representing the usage plan containing the to-be-retrieved  UsagePlanKey resource representing a plan customer.

      

    
    :type nameQuery: string
    :param nameQuery: 

      A query parameter specifying the name of the to-be-returned usage plan keys.

      

    
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
            'items': [
                {
                    'id': 'string',
                    'type': 'string',
                    'value': 'string',
                    'name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the collection of usage plan keys added to usage plans for the associated API keys and, possibly, other types of keys.

          `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a usage plan key to identify a plan customer.

              

            To associate an API stage with a selected API key in a usage plan, you must create a UsagePlanKey resource to represent the selected  ApiKey .

             "  `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
            

            - **id** *(string) --* 

              The Id of a usage plan key.

              
            

            - **type** *(string) --* 

              The type of a usage plan key. Currently, the valid key type is ``API_KEY`` .

              
            

            - **value** *(string) --* 

              The value of a usage plan key.

              
            

            - **name** *(string) --* 

              The name of a usage plan key.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetUsagePlans

  ::

    
    paginator = client.get_paginator('get_usage_plans')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_usage_plans`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsagePlans>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          keyId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type keyId: string
    :param keyId: 

      The identifier of the API key associated with the usage plans.

      

    
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
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'description': 'string',
                    'apiStages': [
                        {
                            'apiId': 'string',
                            'stage': 'string'
                        },
                    ],
                    'throttle': {
                        'burstLimit': 123,
                        'rateLimit': 123.0
                    },
                    'quota': {
                        'limit': 123,
                        'offset': 123,
                        'period': 'DAY'|'WEEK'|'MONTH'
                    },
                    'productCode': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a collection of usage plans for an AWS account.

          `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            Represents a usage plan than can specify who can assess associated API stages with specified request limits and quotas.

              

            In a usage plan, you associate an API by specifying the API's Id and a stage name of the specified API. You add plan customers by adding API keys to the plan. 

               `Create and Use Usage Plans <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__  
            

            - **id** *(string) --* 

              The identifier of a  UsagePlan resource.

              
            

            - **name** *(string) --* 

              The name of a usage plan.

              
            

            - **description** *(string) --* 

              The description of a usage plan.

              
            

            - **apiStages** *(list) --* 

              The associated API stages of a usage plan.

              
              

              - *(dict) --* 

                API stage name of the associated API stage in a usage plan.

                
                

                - **apiId** *(string) --* 

                  API Id of the associated API stage in a usage plan.

                  
                

                - **stage** *(string) --* 

                  API stage name of the associated API stage in a usage plan.

                  
            
          
            

            - **throttle** *(dict) --* 

              The request throttle limits of a usage plan.

              
              

              - **burstLimit** *(integer) --* 

                The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.

                
              

              - **rateLimit** *(float) --* 

                The API request steady-state rate limit.

                
          
            

            - **quota** *(dict) --* 

              The maximum number of permitted requests per a given unit time interval.

              
              

              - **limit** *(integer) --* 

                The maximum number of requests that can be made in a given time period.

                
              

              - **offset** *(integer) --* 

                The number of requests subtracted from the given limit in the initial time period.

                
              

              - **period** *(string) --* 

                The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".

                
          
            

            - **productCode** *(string) --* 

              The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: APIGateway.Paginator.GetVpcLinks

  ::

    
    paginator = client.get_paginator('get_vpc_links')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`APIGateway.Client.get_vpc_links`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetVpcLinks>`_    


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
            'items': [
                {
                    'id': 'string',
                    'name': 'string',
                    'description': 'string',
                    'targetArns': [
                        'string',
                    ],
                    'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
                    'statusMessage': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The collection of VPC links under the caller's account in a region.

          `Getting Started with Private Integrations <http://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-private-integration.html>`__ , `Set up Private Integrations <http://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html>`__  
        

        - **items** *(list) --* 

          The current page of elements from this collection.

          
          

          - *(dict) --* 

            A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud (VPC).

              

            

            To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway, you, as an API developer, create a  VpcLink resource targeted for one or more network load balancers of the VPC and then integrate an API method with a private integration that uses the  VpcLink . The private integraiton has an integration type of ``HTTP`` or ``HTTP_PROXY`` and has a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to identify the  VpcLink used.

             

             
            

            - **id** *(string) --* 

              The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

              
            

            - **name** *(string) --* 

              The name used to label and identify the VPC link.

              
            

            - **description** *(string) --* 

              The description of the VPC link.

              
            

            - **targetArns** *(list) --* 

              The ARNs of network load balancers of the VPC targeted by the VPC link. The network load balancers must be owned by the same AWS account of the API owner.

              
              

              - *(string) --* 
          
            

            - **status** *(string) --* 

              The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` , ``DELETING`` , or ``FAILED`` . Deploying an API will wait if the status is ``PENDING`` and will fail if the status is ``DELETING`` . 

              
            

            - **statusMessage** *(string) --* 

              A description about the VPC link status.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    