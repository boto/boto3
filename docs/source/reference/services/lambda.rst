

******
Lambda
******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Lambda.Client

  A low-level client representing AWS Lambda::

    
    import boto3
    
    client = boto3.client('lambda')

  
  These are the available methods:
  
  *   :py:meth:`~Lambda.Client.add_permission`

  
  *   :py:meth:`~Lambda.Client.can_paginate`

  
  *   :py:meth:`~Lambda.Client.create_alias`

  
  *   :py:meth:`~Lambda.Client.create_event_source_mapping`

  
  *   :py:meth:`~Lambda.Client.create_function`

  
  *   :py:meth:`~Lambda.Client.delete_alias`

  
  *   :py:meth:`~Lambda.Client.delete_event_source_mapping`

  
  *   :py:meth:`~Lambda.Client.delete_function`

  
  *   :py:meth:`~Lambda.Client.delete_function_concurrency`

  
  *   :py:meth:`~Lambda.Client.generate_presigned_url`

  
  *   :py:meth:`~Lambda.Client.get_account_settings`

  
  *   :py:meth:`~Lambda.Client.get_alias`

  
  *   :py:meth:`~Lambda.Client.get_event_source_mapping`

  
  *   :py:meth:`~Lambda.Client.get_function`

  
  *   :py:meth:`~Lambda.Client.get_function_configuration`

  
  *   :py:meth:`~Lambda.Client.get_paginator`

  
  *   :py:meth:`~Lambda.Client.get_policy`

  
  *   :py:meth:`~Lambda.Client.get_waiter`

  
  *   :py:meth:`~Lambda.Client.invoke`

  
  *   :py:meth:`~Lambda.Client.invoke_async`

  
  *   :py:meth:`~Lambda.Client.list_aliases`

  
  *   :py:meth:`~Lambda.Client.list_event_source_mappings`

  
  *   :py:meth:`~Lambda.Client.list_functions`

  
  *   :py:meth:`~Lambda.Client.list_tags`

  
  *   :py:meth:`~Lambda.Client.list_versions_by_function`

  
  *   :py:meth:`~Lambda.Client.publish_version`

  
  *   :py:meth:`~Lambda.Client.put_function_concurrency`

  
  *   :py:meth:`~Lambda.Client.remove_permission`

  
  *   :py:meth:`~Lambda.Client.tag_resource`

  
  *   :py:meth:`~Lambda.Client.untag_resource`

  
  *   :py:meth:`~Lambda.Client.update_alias`

  
  *   :py:meth:`~Lambda.Client.update_event_source_mapping`

  
  *   :py:meth:`~Lambda.Client.update_function_code`

  
  *   :py:meth:`~Lambda.Client.update_function_configuration`

  

  .. py:method:: add_permission(**kwargs)

    

    Adds a permission to the resource policy associated with the specified AWS Lambda function. You use resource policies to grant permissions to event sources that use *push* model. In a *push* model, event sources (such as Amazon S3 and custom applications) invoke your Lambda function. Each permission you add to the resource policy allows an event source, permission to invoke the Lambda function. 

     

    For information about the push model, see `AWS Lambda\: How it Works <http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction.html>`__ . 

     

    If you are using versioning, the permissions you add are specific to the Lambda function version or alias you specify in the ``AddPermission`` request via the ``Qualifier`` parameter. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    This operation requires permission for the ``lambda:AddPermission`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/AddPermission>`_    


    **Request Syntax** 
    ::

      response = client.add_permission(
          FunctionName='string',
          StatementId='string',
          Action='string',
          Principal='string',
          SourceArn='string',
          SourceAccount='string',
          EventSourceToken='string',
          Qualifier='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      Name of the Lambda function whose resource policy you are updating by adding a new permission.

       

      You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type StatementId: string
    :param StatementId: **[REQUIRED]** 

      A unique statement identifier.

      

    
    :type Action: string
    :param Action: **[REQUIRED]** 

      The AWS Lambda action you want to allow in this statement. Each Lambda action is a string starting with ``lambda:`` followed by the API name . For example, ``lambda:CreateFunction`` . You can use wildcard (``lambda:*`` ) to grant permission for all AWS Lambda actions. 

      

    
    :type Principal: string
    :param Principal: **[REQUIRED]** 

      The principal who is getting this permission. It can be Amazon S3 service Principal (``s3.amazonaws.com`` ) if you want Amazon S3 to invoke the function, an AWS account ID if you are granting cross-account permission, or any valid AWS service principal such as ``sns.amazonaws.com`` . For example, you might want to allow a custom application in another AWS account to push events to AWS Lambda by invoking your function. 

      

    
    :type SourceArn: string
    :param SourceArn: 

      This is optional; however, when granting permission to invoke your function, you should specify this field with the Amazon Resource Name (ARN) as its value. This ensures that only events generated from the specified source can invoke the function.

       

      .. warning::

         

        If you add a permission without providing the source ARN, any AWS account that creates a mapping to your function ARN can send events to invoke your Lambda function.

         

      

    
    :type SourceAccount: string
    :param SourceAccount: 

      This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner. For example, if the ``SourceArn`` identifies a bucket, then this is the bucket owner's account ID. You can use this additional condition to ensure the bucket you specify is owned by a specific account (it is possible the bucket owner deleted the bucket and some other AWS account created the bucket). You can also use this condition to specify all sources (that is, you don't specify the ``SourceArn`` ) owned by a specific account. 

      

    
    :type EventSourceToken: string
    :param EventSourceToken: 

      A unique token that must be supplied by the principal invoking the function. This is currently only used for Alexa Smart Home functions.

      

    
    :type Qualifier: string
    :param Qualifier: 

      You can use this optional query parameter to describe a qualified ARN using a function version or an alias name. The permission will then apply to the specific qualified ARN. For example, if you specify function version 2 as the qualifier, then permission applies only when request is made using qualified function ARN:

       

       ``arn:aws:lambda:aws-region:acct-id:function:function-name:2``  

       

      If you specify an alias name, for example ``PROD`` , then the permission is valid only for requests made using the alias ARN:

       

       ``arn:aws:lambda:aws-region:acct-id:function:function-name:PROD``  

       

      If the qualifier is not specified, the permission is valid only when requests is made using unqualified function ARN.

       

       ``arn:aws:lambda:aws-region:acct-id:function:function-name``  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Statement': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **Statement** *(string) --* 

          The permission statement you specified in the request. The response returns the same as a string using a backslash ("\") as an escape character in the JSON.

          
    

    **Examples** 

    This example adds a permission for an S3 bucket to invoke a Lambda function.
    ::

      response = client.add_permission(
          Action='lambda:InvokeFunction',
          FunctionName='MyFunction',
          Principal='s3.amazonaws.com',
          SourceAccount='123456789012',
          SourceArn='arn:aws:s3:::examplebucket/*',
          StatementId='ID-1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Statement': 'ID-1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

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


  .. py:method:: create_alias(**kwargs)

    

    Creates an alias that points to the specified Lambda function version. For more information, see `Introduction to AWS Lambda Aliases <http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

     

    Alias names are unique for a given function. This requires permission for the lambda:CreateAlias action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateAlias>`_    


    **Request Syntax** 
    ::

      response = client.create_alias(
          FunctionName='string',
          Name='string',
          FunctionVersion='string',
          Description='string',
          RoutingConfig={
              'AdditionalVersionWeights': {
                  'string': 123.0
              }
          }
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      Name of the Lambda function for which you want to create an alias. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name for the alias you are creating.

      

    
    :type FunctionVersion: string
    :param FunctionVersion: **[REQUIRED]** 

      Lambda function version for which you are creating the alias.

      

    
    :type Description: string
    :param Description: 

      Description of the alias.

      

    
    :type RoutingConfig: dict
    :param RoutingConfig: 

      Specifies an additional version your alias can point to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see  lambda-traffic-shifting-using-aliases .

      

    
      - **AdditionalVersionWeights** *(dict) --* 

        Set this property value to dictate what percentage of traffic will invoke the updated function version. If set to an empty string, 100 percent of traffic will invoke ``function-version`` .

        

      
        - *(string) --* 

        
          - *(float) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AliasArn': 'string',
            'Name': 'string',
            'FunctionVersion': 'string',
            'Description': 'string',
            'RoutingConfig': {
                'AdditionalVersionWeights': {
                    'string': 123.0
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Provides configuration information about a Lambda function version alias.

        
        

        - **AliasArn** *(string) --* 

          Lambda function ARN that is qualified using the alias name as the suffix. For example, if you create an alias called ``BETA`` that points to a helloworld function version, the ARN is ``arn:aws:lambda:aws-regions:acct-id:function:helloworld:BETA`` .

          
        

        - **Name** *(string) --* 

          Alias name.

          
        

        - **FunctionVersion** *(string) --* 

          Function version to which the alias points.

          
        

        - **Description** *(string) --* 

          Alias description.

          
        

        - **RoutingConfig** *(dict) --* 

          Specifies an additional function versions the alias points to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see  lambda-traffic-shifting-using-aliases .

          
          

          - **AdditionalVersionWeights** *(dict) --* 

            Set this property value to dictate what percentage of traffic will invoke the updated function version. If set to an empty string, 100 percent of traffic will invoke ``function-version`` .

            
            

            - *(string) --* 
              

              - *(float) --* 
        
      
      
    

  .. py:method:: create_event_source_mapping(**kwargs)

    

    Identifies a stream as an event source for a Lambda function. It can be either an Amazon Kinesis stream or an Amazon DynamoDB stream. AWS Lambda invokes the specified function when records are posted to the stream.

     

    This association between a stream source and a Lambda function is called the event source mapping.

     

    .. warning::

       

      This event source mapping is relevant only in the AWS Lambda pull model, where AWS Lambda invokes the function. For more information, see `AWS Lambda\: How it Works <http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction.html>`__ in the *AWS Lambda Developer Guide* .

       

     

    You provide mapping information (for example, which stream to read from and which Lambda function to invoke) in the request body.

     

    Each event source, such as an Amazon Kinesis or a DynamoDB stream, can be associated with multiple AWS Lambda function. A given Lambda function can be associated with multiple AWS event sources.

     

    If you are using versioning, you can specify a specific function version or an alias via the function name parameter. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    This operation requires permission for the ``lambda:CreateEventSourceMapping`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateEventSourceMapping>`_    


    **Request Syntax** 
    ::

      response = client.create_event_source_mapping(
          EventSourceArn='string',
          FunctionName='string',
          Enabled=True|False,
          BatchSize=123,
          StartingPosition='TRIM_HORIZON'|'LATEST'|'AT_TIMESTAMP',
          StartingPositionTimestamp=datetime(2015, 1, 1)
      )
    :type EventSourceArn: string
    :param EventSourceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the Amazon Kinesis or the Amazon DynamoDB stream that is the event source. Any record added to this stream could cause AWS Lambda to invoke your Lambda function, it depends on the ``BatchSize`` . AWS Lambda POSTs the Amazon Kinesis event, containing records, to your Lambda function as JSON.

      

    
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The Lambda function to invoke when AWS Lambda detects an event on the stream.

       

      You can specify the function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). 

       

      If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__  

       

      AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, ``account-id:Thumbnail`` ). 

       

      Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

      

    
    :type Enabled: boolean
    :param Enabled: 

      Indicates whether AWS Lambda should begin polling the event source. By default, ``Enabled`` is true. 

      

    
    :type BatchSize: integer
    :param BatchSize: 

      The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. The default is 100 records.

      

    
    :type StartingPosition: string
    :param StartingPosition: **[REQUIRED]** 

      The position in the stream where AWS Lambda should start reading. Valid only for Kinesis streams. For more information, see `ShardIteratorType <http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType>`__ in the *Amazon Kinesis API Reference* . 

      

    
    :type StartingPositionTimestamp: datetime
    :param StartingPositionTimestamp: 

      The timestamp of the data record from which to start reading. Used with `shard iterator type <http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType>`__ AT_TIMESTAMP. If a record with this exact timestamp does not exist, the iterator returned is for the next (later) record. If the timestamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON). Valid only for Kinesis streams. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UUID': 'string',
            'BatchSize': 123,
            'EventSourceArn': 'string',
            'FunctionArn': 'string',
            'LastModified': datetime(2015, 1, 1),
            'LastProcessingResult': 'string',
            'State': 'string',
            'StateTransitionReason': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes mapping between an Amazon Kinesis stream and a Lambda function.

        
        

        - **UUID** *(string) --* 

          The AWS Lambda assigned opaque identifier for the mapping.

          
        

        - **BatchSize** *(integer) --* 

          The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.

          
        

        - **EventSourceArn** *(string) --* 

          The Amazon Resource Name (ARN) of the Amazon Kinesis stream that is the source of events.

          
        

        - **FunctionArn** *(string) --* 

          The Lambda function to invoke when AWS Lambda detects an event on the stream.

          
        

        - **LastModified** *(datetime) --* 

          The UTC time string indicating the last time the event mapping was updated.

          
        

        - **LastProcessingResult** *(string) --* 

          The result of the last AWS Lambda invocation of your Lambda function.

          
        

        - **State** *(string) --* 

          The state of the event source mapping. It can be ``Creating`` , ``Enabled`` , ``Disabled`` , ``Enabling`` , ``Disabling`` , ``Updating`` , or ``Deleting`` .

          
        

        - **StateTransitionReason** *(string) --* 

          The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.

          
    

  .. py:method:: create_function(**kwargs)

    

    Creates a new Lambda function. The function metadata is created from the request parameters, and the code for the function is provided by a .zip file in the request body. If the function name already exists, the operation will fail. Note that the function name is case-sensitive.

     

    If you are using versioning, you can also publish a version of the Lambda function you are creating using the ``Publish`` parameter. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    This operation requires permission for the ``lambda:CreateFunction`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateFunction>`_    


    **Request Syntax** 
    ::

      response = client.create_function(
          FunctionName='string',
          Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
          Role='string',
          Handler='string',
          Code={
              'ZipFile': b'bytes',
              'S3Bucket': 'string',
              'S3Key': 'string',
              'S3ObjectVersion': 'string'
          },
          Description='string',
          Timeout=123,
          MemorySize=123,
          Publish=True|False,
          VpcConfig={
              'SubnetIds': [
                  'string',
              ],
              'SecurityGroupIds': [
                  'string',
              ]
          },
          DeadLetterConfig={
              'TargetArn': 'string'
          },
          Environment={
              'Variables': {
                  'string': 'string'
              }
          },
          KMSKeyArn='string',
          TracingConfig={
              'Mode': 'Active'|'PassThrough'
          },
          Tags={
              'string': 'string'
          }
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The name you want to assign to the function you are uploading. The function names appear in the console and are returned in the  ListFunctions API. Function names are used to specify functions to other AWS Lambda API operations, such as  Invoke . Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type Runtime: string
    :param Runtime: **[REQUIRED]** 

      The runtime environment for the Lambda function you are uploading.

       

      To use the Python runtime v3.6, set the value to "python3.6". To use the Python runtime v2.7, set the value to "python2.7". To use the Node.js runtime v6.10, set the value to "nodejs6.10". To use the Node.js runtime v4.3, set the value to "nodejs4.3".

       

      .. note::

         

        Node v0.10.42 is currently marked as deprecated. You must migrate existing functions to the newer Node.js runtime versions available on AWS Lambda (nodejs4.3 or nodejs6.10) as soon as possible. Failure to do so will result in an invalid parmaeter error being returned. Note that you will have to follow this procedure for each region that contains functions written in the Node v0.10.42 runtime.

         

      

    
    :type Role: string
    :param Role: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources. For more information, see `AWS Lambda\: How it Works <http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction.html>`__ . 

      

    
    :type Handler: string
    :param Handler: **[REQUIRED]** 

      The function within your code that Lambda calls to begin execution. For Node.js, it is the *module-name* .*export* value in your function. For Java, it can be ``package.class-name::handler`` or ``package.class-name`` . For more information, see `Lambda Function Handler (Java) <http://docs.aws.amazon.com/lambda/latest/dg/java-programming-model-handler-types.html>`__ . 

      

    
    :type Code: dict
    :param Code: **[REQUIRED]** 

      The code for the Lambda function.

      

    
      - **ZipFile** *(bytes) --* 

        The contents of your zip file containing your deployment package. If you are using the web API directly, the contents of the zip file must be base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or CLI will do the encoding for you. For more information about creating a .zip file, see `Execution Permissions <http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role.html>`__ in the *AWS Lambda Developer Guide* . 

        

      
      - **S3Bucket** *(string) --* 

        Amazon S3 bucket name where the .zip file containing your deployment package is stored. This bucket must reside in the same AWS region where you are creating the Lambda function.

        

      
      - **S3Key** *(string) --* 

        The Amazon S3 object (the deployment package) key name you want to upload.

        

      
      - **S3ObjectVersion** *(string) --* 

        The Amazon S3 object (the deployment package) version you want to upload.

        

      
    
    :type Description: string
    :param Description: 

      A short, user-defined function description. Lambda does not use this value. Assign a meaningful description as you see fit.

      

    
    :type Timeout: integer
    :param Timeout: 

      The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

      

    
    :type MemorySize: integer
    :param MemorySize: 

      The amount of memory, in MB, your Lambda function is given. Lambda uses this memory size to infer the amount of CPU and memory allocated to your function. Your function use-case determines your CPU and memory requirements. For example, a database operation might need less memory compared to an image processing function. The default value is 128 MB. The value must be a multiple of 64 MB.

      

    
    :type Publish: boolean
    :param Publish: 

      This boolean parameter can be used to request AWS Lambda to create the Lambda function and publish a version as an atomic operation.

      

    
    :type VpcConfig: dict
    :param VpcConfig: 

      If your Lambda function accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.

      

    
      - **SubnetIds** *(list) --* 

        A list of one or more subnet IDs in your VPC.

        

      
        - *(string) --* 

        
    
      - **SecurityGroupIds** *(list) --* 

        A list of one or more security groups IDs in your VPC.

        

      
        - *(string) --* 

        
    
    
    :type DeadLetterConfig: dict
    :param DeadLetterConfig: 

      The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic. 

      

    
      - **TargetArn** *(string) --* 

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

        

      
    
    :type Environment: dict
    :param Environment: 

      The parent object that contains your environment's configuration settings.

      

    
      - **Variables** *(dict) --* 

        The key-value pairs that represent your environment's configuration settings.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    :type KMSKeyArn: string
    :param KMSKeyArn: 

      The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If not provided, AWS Lambda will use a default service key.

      

    
    :type TracingConfig: dict
    :param TracingConfig: 

      The parent object that contains your function's tracing settings.

      

    
      - **Mode** *(string) --* 

        Can be either PassThrough or Active. If PassThrough, Lambda will only trace the request from an upstream service if it contains a tracing header with "sampled=1". If Active, Lambda will respect any tracing header it receives from an upstream service. If no tracing header is received, Lambda will call X-Ray for a tracing decision.

        

      
    
    :type Tags: dict
    :param Tags: 

      The list of tags (key-value pairs) assigned to the new function.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that describes function metadata.

        
        

        - **FunctionName** *(string) --* 

          The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

          
        

        - **FunctionArn** *(string) --* 

          The Amazon Resource Name (ARN) assigned to the function.

          
        

        - **Runtime** *(string) --* 

          The runtime environment for the Lambda function.

          
        

        - **Role** *(string) --* 

          The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

          
        

        - **Handler** *(string) --* 

          The function Lambda calls to begin executing your function.

          
        

        - **CodeSize** *(integer) --* 

          The size, in bytes, of the function .zip file you uploaded.

          
        

        - **Description** *(string) --* 

          The user-provided description.

          
        

        - **Timeout** *(integer) --* 

          The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

          
        

        - **MemorySize** *(integer) --* 

          The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

          
        

        - **LastModified** *(string) --* 

          The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

          
        

        - **CodeSha256** *(string) --* 

          It is the SHA256 hash of your function deployment package.

          
        

        - **Version** *(string) --* 

          The version of the Lambda function.

          
        

        - **VpcConfig** *(dict) --* 

          VPC configuration associated with your Lambda function.

          
          

          - **SubnetIds** *(list) --* 

            A list of subnet IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **SecurityGroupIds** *(list) --* 

            A list of security group IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **VpcId** *(string) --* 

            The VPC ID associated with you Lambda function.

            
      
        

        - **DeadLetterConfig** *(dict) --* 

          The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

          
          

          - **TargetArn** *(string) --* 

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

            
      
        

        - **Environment** *(dict) --* 

          The parent object that contains your environment's configuration settings.

          
          

          - **Variables** *(dict) --* 

            The key-value pairs returned that represent your environment's configuration settings or error information.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **Error** *(dict) --* 

            The parent object that contains error information associated with your configuration settings.

            
            

            - **ErrorCode** *(string) --* 

              The error code returned by the environment error object.

              
            

            - **Message** *(string) --* 

              The message returned by the environment error object.

              
        
      
        

        - **KMSKeyArn** *(string) --* 

          The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

          
        

        - **TracingConfig** *(dict) --* 

          The parent object that contains your function's tracing settings.

          
          

          - **Mode** *(string) --* 

            The tracing mode associated with your Lambda function.

            
      
        

        - **MasterArn** *(string) --* 

          Returns the ARN (Amazon Resource Name) of the master function.

          
    

    **Examples** 

    This example creates a Lambda function.
    ::

      response = client.create_function(
          Code={
          },
          Description='',
          FunctionName='MyFunction',
          # is of the form of the name of your source file and then name of your function handler
          Handler='souce_file.handler_name',
          MemorySize=128,
          Publish=True,
          # replace with the actual arn of the execution role you created
          Role='arn:aws:iam::123456789012:role/service-role/role-name',
          Runtime='nodejs4.3',
          Timeout=15,
          VpcConfig={
          },
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CodeSha256': '',
          'CodeSize': 123,
          'Description': '',
          'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:MyFunction',
          'FunctionName': 'MyFunction',
          'Handler': 'source_file.handler_name',
          'LastModified': '2016-11-21T19:49:20.006+0000',
          'MemorySize': 128,
          'Role': 'arn:aws:iam::123456789012:role/service-role/role-name',
          'Runtime': 'nodejs4.3',
          'Timeout': 123,
          'Version': '1',
          'VpcConfig': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_alias(**kwargs)

    

    Deletes the specified Lambda function alias. For more information, see `Introduction to AWS Lambda Aliases <http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

     

    This requires permission for the lambda:DeleteAlias action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteAlias>`_    


    **Request Syntax** 
    ::

      response = client.delete_alias(
          FunctionName='string',
          Name='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The Lambda function name for which the alias is created. Deleting an alias does not delete the function version to which it is pointing. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the alias to delete.

      

    
    
    :returns: None

    **Examples** 

    This operation deletes a Lambda function alias
    ::

      response = client.delete_alias(
          FunctionName='myFunction',
          Name='alias',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_event_source_mapping(**kwargs)

    

    Removes an event source mapping. This means AWS Lambda will no longer invoke the function for events in the associated source.

     

    This operation requires permission for the ``lambda:DeleteEventSourceMapping`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteEventSourceMapping>`_    


    **Request Syntax** 
    ::

      response = client.delete_event_source_mapping(
          UUID='string'
      )
    :type UUID: string
    :param UUID: **[REQUIRED]** 

      The event source mapping ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UUID': 'string',
            'BatchSize': 123,
            'EventSourceArn': 'string',
            'FunctionArn': 'string',
            'LastModified': datetime(2015, 1, 1),
            'LastProcessingResult': 'string',
            'State': 'string',
            'StateTransitionReason': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes mapping between an Amazon Kinesis stream and a Lambda function.

        
        

        - **UUID** *(string) --* 

          The AWS Lambda assigned opaque identifier for the mapping.

          
        

        - **BatchSize** *(integer) --* 

          The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.

          
        

        - **EventSourceArn** *(string) --* 

          The Amazon Resource Name (ARN) of the Amazon Kinesis stream that is the source of events.

          
        

        - **FunctionArn** *(string) --* 

          The Lambda function to invoke when AWS Lambda detects an event on the stream.

          
        

        - **LastModified** *(datetime) --* 

          The UTC time string indicating the last time the event mapping was updated.

          
        

        - **LastProcessingResult** *(string) --* 

          The result of the last AWS Lambda invocation of your Lambda function.

          
        

        - **State** *(string) --* 

          The state of the event source mapping. It can be ``Creating`` , ``Enabled`` , ``Disabled`` , ``Enabling`` , ``Disabling`` , ``Updating`` , or ``Deleting`` .

          
        

        - **StateTransitionReason** *(string) --* 

          The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.

          
    

    **Examples** 

    This operation deletes a Lambda function event source mapping
    ::

      response = client.delete_event_source_mapping(
          UUID='12345kxodurf3443',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'BatchSize': 123,
          'EventSourceArn': 'arn:aws:s3:::examplebucket/*',
          'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction',
          'LastModified': datetime(2016, 11, 21, 19, 49, 20, 0, 326, 0),
          'LastProcessingResult': '',
          'State': '',
          'StateTransitionReason': '',
          'UUID': '12345kxodurf3443',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_function(**kwargs)

    

    Deletes the specified Lambda function code and configuration.

     

    If you are using the versioning feature and you don't specify a function version in your ``DeleteFunction`` request, AWS Lambda will delete the function, including all its versions, and any aliases pointing to the function versions. To delete a specific function version, you must provide the function version via the ``Qualifier`` parameter. For information about function versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    When you delete a function the associated resource policy is also deleted. You will need to delete the event source mappings explicitly.

     

    This operation requires permission for the ``lambda:DeleteFunction`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteFunction>`_    


    **Request Syntax** 
    ::

      response = client.delete_function(
          FunctionName='string',
          Qualifier='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The Lambda function to delete.

       

      You can specify the function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type Qualifier: string
    :param Qualifier: 

      Using this optional parameter you can specify a function version (but not the ``$LATEST`` version) to direct AWS Lambda to delete a specific function version. If the function version has one or more aliases pointing to it, you will get an error because you cannot have aliases pointing to it. You can delete any function version but not the ``$LATEST`` , that is, you cannot specify ``$LATEST`` as the value of this parameter. The ``$LATEST`` version can be deleted only when you want to delete all the function versions and aliases.

       

      You can only specify a function version, not an alias name, using this parameter. You cannot delete a function version using its alias.

       

      If you don't specify this parameter, AWS Lambda will delete the function, including all of its versions and aliases.

      

    
    
    :returns: None

    **Examples** 

    This operation deletes a Lambda function
    ::

      response = client.delete_function(
          FunctionName='myFunction',
          Qualifier='1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_function_concurrency(**kwargs)

    

    Removes concurrent execution limits from this function.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteFunctionConcurrency>`_    


    **Request Syntax** 
    ::

      response = client.delete_function_concurrency(
          FunctionName='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The name of the function you are removing concurrent execution limits from.

      

    
    
    :returns: None

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


  .. py:method:: get_account_settings()

    

    Returns a customer's account settings.

     

    You can use this operation to retrieve Lambda limits information, such as code size and concurrency limits. For more information about limits, see `AWS Lambda Limits <http://docs.aws.amazon.com/lambda/latest/dg/limits.html>`__ . You can also retrieve resource usage statistics, such as code storage usage and function count.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetAccountSettings>`_    


    **Request Syntax** 
    ::

      response = client.get_account_settings()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AccountLimit': {
                'TotalCodeSize': 123,
                'CodeSizeUnzipped': 123,
                'CodeSizeZipped': 123,
                'ConcurrentExecutions': 123,
                'UnreservedConcurrentExecutions': 123
            },
            'AccountUsage': {
                'TotalCodeSize': 123,
                'FunctionCount': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AccountLimit** *(dict) --* 

          Provides limits of code size and concurrency associated with the current account and region.

          
          

          - **TotalCodeSize** *(integer) --* 

            Maximum size, in bytes, of a code package you can upload per region. The default size is 75 GB. 

            
          

          - **CodeSizeUnzipped** *(integer) --* 

            Size, in bytes, of code/dependencies that you can zip into a deployment package (uncompressed zip/jar size) for uploading. The default limit is 250 MB.

            
          

          - **CodeSizeZipped** *(integer) --* 

            Size, in bytes, of a single zipped code/dependencies package you can upload for your Lambda function(.zip/.jar file). Try using Amazon S3 for uploading larger files. Default limit is 50 MB.

            
          

          - **ConcurrentExecutions** *(integer) --* 

            Number of simultaneous executions of your function per region. For more information or to request a limit increase for concurrent executions, see `Lambda Function Concurrent Executions <http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ . The default limit is 1000.

            
          

          - **UnreservedConcurrentExecutions** *(integer) --* 

            The number of concurrent executions available to functions that do not have concurrency limits set.

            
      
        

        - **AccountUsage** *(dict) --* 

          Provides code size usage and function count associated with the current account and region.

          
          

          - **TotalCodeSize** *(integer) --* 

            Total size, in bytes, of the account's deployment packages per region.

            
          

          - **FunctionCount** *(integer) --* 

            The number of your account's existing functions per region.

            
      
    

    **Examples** 

    This operation retrieves a Lambda customer's account settings
    ::

      response = client.get_account_settings(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AccountLimit': {
          },
          'AccountUsage': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_alias(**kwargs)

    

    Returns the specified alias information such as the alias ARN, description, and function version it is pointing to. For more information, see `Introduction to AWS Lambda Aliases <http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

     

    This requires permission for the ``lambda:GetAlias`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetAlias>`_    


    **Request Syntax** 
    ::

      response = client.get_alias(
          FunctionName='string',
          Name='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      Function name for which the alias is created. An alias is a subresource that exists only in the context of an existing Lambda function so you must specify the function name. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the alias for which you want to retrieve information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AliasArn': 'string',
            'Name': 'string',
            'FunctionVersion': 'string',
            'Description': 'string',
            'RoutingConfig': {
                'AdditionalVersionWeights': {
                    'string': 123.0
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Provides configuration information about a Lambda function version alias.

        
        

        - **AliasArn** *(string) --* 

          Lambda function ARN that is qualified using the alias name as the suffix. For example, if you create an alias called ``BETA`` that points to a helloworld function version, the ARN is ``arn:aws:lambda:aws-regions:acct-id:function:helloworld:BETA`` .

          
        

        - **Name** *(string) --* 

          Alias name.

          
        

        - **FunctionVersion** *(string) --* 

          Function version to which the alias points.

          
        

        - **Description** *(string) --* 

          Alias description.

          
        

        - **RoutingConfig** *(dict) --* 

          Specifies an additional function versions the alias points to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see  lambda-traffic-shifting-using-aliases .

          
          

          - **AdditionalVersionWeights** *(dict) --* 

            Set this property value to dictate what percentage of traffic will invoke the updated function version. If set to an empty string, 100 percent of traffic will invoke ``function-version`` .

            
            

            - *(string) --* 
              

              - *(float) --* 
        
      
      
    

    **Examples** 

    This operation retrieves a Lambda function alias
    ::

      response = client.get_alias(
          FunctionName='myFunction',
          Name='myFunctionAlias',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AliasArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunctionAlias',
          'Description': '',
          'FunctionVersion': '1',
          'Name': 'myFunctionAlias',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_event_source_mapping(**kwargs)

    

    Returns configuration information for the specified event source mapping (see  CreateEventSourceMapping ).

     

    This operation requires permission for the ``lambda:GetEventSourceMapping`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetEventSourceMapping>`_    


    **Request Syntax** 
    ::

      response = client.get_event_source_mapping(
          UUID='string'
      )
    :type UUID: string
    :param UUID: **[REQUIRED]** 

      The AWS Lambda assigned ID of the event source mapping.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UUID': 'string',
            'BatchSize': 123,
            'EventSourceArn': 'string',
            'FunctionArn': 'string',
            'LastModified': datetime(2015, 1, 1),
            'LastProcessingResult': 'string',
            'State': 'string',
            'StateTransitionReason': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes mapping between an Amazon Kinesis stream and a Lambda function.

        
        

        - **UUID** *(string) --* 

          The AWS Lambda assigned opaque identifier for the mapping.

          
        

        - **BatchSize** *(integer) --* 

          The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.

          
        

        - **EventSourceArn** *(string) --* 

          The Amazon Resource Name (ARN) of the Amazon Kinesis stream that is the source of events.

          
        

        - **FunctionArn** *(string) --* 

          The Lambda function to invoke when AWS Lambda detects an event on the stream.

          
        

        - **LastModified** *(datetime) --* 

          The UTC time string indicating the last time the event mapping was updated.

          
        

        - **LastProcessingResult** *(string) --* 

          The result of the last AWS Lambda invocation of your Lambda function.

          
        

        - **State** *(string) --* 

          The state of the event source mapping. It can be ``Creating`` , ``Enabled`` , ``Disabled`` , ``Enabling`` , ``Disabling`` , ``Updating`` , or ``Deleting`` .

          
        

        - **StateTransitionReason** *(string) --* 

          The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.

          
    

    **Examples** 

    This operation retrieves a Lambda function's event source mapping
    ::

      response = client.get_event_source_mapping(
          UUID='123489-xxxxx-kdla8d89d7',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'BatchSize': 123,
          'EventSourceArn': 'arn:aws:iam::123456789012:eventsource',
          'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction',
          'LastModified': datetime(2016, 11, 21, 19, 49, 20, 0, 326, 0),
          'LastProcessingResult': '',
          'State': '',
          'StateTransitionReason': '',
          'UUID': '123489-xxxxx-kdla8d89d7',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_function(**kwargs)

    

    Returns the configuration information of the Lambda function and a presigned URL link to the .zip file you uploaded with  CreateFunction so you can download the .zip file. Note that the URL is valid for up to 10 minutes. The configuration information is the same information you provided as parameters when uploading the function.

     

    Using the optional ``Qualifier`` parameter, you can specify a specific function version for which you want this information. If you don't specify this parameter, the API uses unqualified function ARN which return information about the ``$LATEST`` version of the Lambda function. For more information, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

     

    This operation requires permission for the ``lambda:GetFunction`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunction>`_    


    **Request Syntax** 
    ::

      response = client.get_function(
          FunctionName='string',
          Qualifier='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The Lambda function name.

       

      You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type Qualifier: string
    :param Qualifier: 

      Use this optional parameter to specify a function version or an alias name. If you specify function version, the API uses qualified function ARN for the request and returns information about the specific Lambda function version. If you specify an alias name, the API uses the alias ARN and returns information about the function version to which the alias points. If you don't provide this parameter, the API uses unqualified function ARN and returns information about the ``$LATEST`` version of the Lambda function. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Configuration': {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string'
            },
            'Code': {
                'RepositoryType': 'string',
                'Location': 'string'
            },
            'Tags': {
                'string': 'string'
            },
            'Concurrency': {
                'ReservedConcurrentExecutions': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        This response contains the object for the Lambda function location (see  FunctionCodeLocation .

        
        

        - **Configuration** *(dict) --* 

          A complex type that describes function metadata.

          
          

          - **FunctionName** *(string) --* 

            The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

            
          

          - **FunctionArn** *(string) --* 

            The Amazon Resource Name (ARN) assigned to the function.

            
          

          - **Runtime** *(string) --* 

            The runtime environment for the Lambda function.

            
          

          - **Role** *(string) --* 

            The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

            
          

          - **Handler** *(string) --* 

            The function Lambda calls to begin executing your function.

            
          

          - **CodeSize** *(integer) --* 

            The size, in bytes, of the function .zip file you uploaded.

            
          

          - **Description** *(string) --* 

            The user-provided description.

            
          

          - **Timeout** *(integer) --* 

            The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

            
          

          - **MemorySize** *(integer) --* 

            The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

            
          

          - **LastModified** *(string) --* 

            The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

            
          

          - **CodeSha256** *(string) --* 

            It is the SHA256 hash of your function deployment package.

            
          

          - **Version** *(string) --* 

            The version of the Lambda function.

            
          

          - **VpcConfig** *(dict) --* 

            VPC configuration associated with your Lambda function.

            
            

            - **SubnetIds** *(list) --* 

              A list of subnet IDs associated with the Lambda function.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              A list of security group IDs associated with the Lambda function.

              
              

              - *(string) --* 
          
            

            - **VpcId** *(string) --* 

              The VPC ID associated with you Lambda function.

              
        
          

          - **DeadLetterConfig** *(dict) --* 

            The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

            
            

            - **TargetArn** *(string) --* 

              The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

              
        
          

          - **Environment** *(dict) --* 

            The parent object that contains your environment's configuration settings.

            
            

            - **Variables** *(dict) --* 

              The key-value pairs returned that represent your environment's configuration settings or error information.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **Error** *(dict) --* 

              The parent object that contains error information associated with your configuration settings.

              
              

              - **ErrorCode** *(string) --* 

                The error code returned by the environment error object.

                
              

              - **Message** *(string) --* 

                The message returned by the environment error object.

                
          
        
          

          - **KMSKeyArn** *(string) --* 

            The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

            
          

          - **TracingConfig** *(dict) --* 

            The parent object that contains your function's tracing settings.

            
            

            - **Mode** *(string) --* 

              The tracing mode associated with your Lambda function.

              
        
          

          - **MasterArn** *(string) --* 

            Returns the ARN (Amazon Resource Name) of the master function.

            
      
        

        - **Code** *(dict) --* 

          The object for the Lambda function location.

          
          

          - **RepositoryType** *(string) --* 

            The repository from which you can download the function.

            
          

          - **Location** *(string) --* 

            The presigned URL you can use to download the function's .zip file that you previously uploaded. The URL is valid for up to 10 minutes.

            
      
        

        - **Tags** *(dict) --* 

          Returns the list of tags associated with the function.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **Concurrency** *(dict) --* 

          The concurrent execution limit set for this function.

          
          

          - **ReservedConcurrentExecutions** *(integer) --* 

            The number of concurrent executions reserved for this function.

            
      
    

    **Examples** 

    This operation retrieves a Lambda function's event source mapping
    ::

      response = client.get_function(
          FunctionName='myFunction',
          Qualifier='1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Code': {
              'Location': 'somelocation',
              'RepositoryType': 'S3',
          },
          'Configuration': {
              'CodeSha256': 'LQT+0DHxxxxcfwLyQjzoEFKZtdqQjHXanlSdfXBlEW0VA=',
              'CodeSize': 262,
              'Description': 'A starter AWS Lambda function.',
              'Environment': {
                  'Variables': {
                      'S3_BUCKET': 'test',
                  },
              },
              'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction',
              'FunctionName': 'myFunction',
              'Handler': 'index.handler',
              'LastModified': '2016-11-21T19:49:20.006+0000',
              'MemorySize': 128,
              'Role': 'arn:aws:iam::123456789012:role/lambda_basic_execution',
              'Runtime': 'nodejs4.3',
              'Timeout': 3,
              'Version': '$LATEST',
              'VpcConfig': {
                  'SecurityGroupIds': [
                  ],
                  'SubnetIds': [
                  ],
              },
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_function_configuration(**kwargs)

    

    Returns the configuration information of the Lambda function. This the same information you provided as parameters when uploading the function by using  CreateFunction .

     

    If you are using the versioning feature, you can retrieve this information for a specific function version by using the optional ``Qualifier`` parameter and specifying the function version or alias that points to it. If you don't provide it, the API returns information about the $LATEST version of the function. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

     

    This operation requires permission for the ``lambda:GetFunctionConfiguration`` operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunctionConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.get_function_configuration(
          FunctionName='string',
          Qualifier='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The name of the Lambda function for which you want to retrieve the configuration information.

       

      You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type Qualifier: string
    :param Qualifier: 

      Using this optional parameter you can specify a function version or an alias name. If you specify function version, the API uses qualified function ARN and returns information about the specific function version. If you specify an alias name, the API uses the alias ARN and returns information about the function version to which the alias points.

       

      If you don't specify this parameter, the API uses unqualified function ARN, and returns information about the ``$LATEST`` function version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that describes function metadata.

        
        

        - **FunctionName** *(string) --* 

          The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

          
        

        - **FunctionArn** *(string) --* 

          The Amazon Resource Name (ARN) assigned to the function.

          
        

        - **Runtime** *(string) --* 

          The runtime environment for the Lambda function.

          
        

        - **Role** *(string) --* 

          The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

          
        

        - **Handler** *(string) --* 

          The function Lambda calls to begin executing your function.

          
        

        - **CodeSize** *(integer) --* 

          The size, in bytes, of the function .zip file you uploaded.

          
        

        - **Description** *(string) --* 

          The user-provided description.

          
        

        - **Timeout** *(integer) --* 

          The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

          
        

        - **MemorySize** *(integer) --* 

          The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

          
        

        - **LastModified** *(string) --* 

          The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

          
        

        - **CodeSha256** *(string) --* 

          It is the SHA256 hash of your function deployment package.

          
        

        - **Version** *(string) --* 

          The version of the Lambda function.

          
        

        - **VpcConfig** *(dict) --* 

          VPC configuration associated with your Lambda function.

          
          

          - **SubnetIds** *(list) --* 

            A list of subnet IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **SecurityGroupIds** *(list) --* 

            A list of security group IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **VpcId** *(string) --* 

            The VPC ID associated with you Lambda function.

            
      
        

        - **DeadLetterConfig** *(dict) --* 

          The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

          
          

          - **TargetArn** *(string) --* 

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

            
      
        

        - **Environment** *(dict) --* 

          The parent object that contains your environment's configuration settings.

          
          

          - **Variables** *(dict) --* 

            The key-value pairs returned that represent your environment's configuration settings or error information.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **Error** *(dict) --* 

            The parent object that contains error information associated with your configuration settings.

            
            

            - **ErrorCode** *(string) --* 

              The error code returned by the environment error object.

              
            

            - **Message** *(string) --* 

              The message returned by the environment error object.

              
        
      
        

        - **KMSKeyArn** *(string) --* 

          The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

          
        

        - **TracingConfig** *(dict) --* 

          The parent object that contains your function's tracing settings.

          
          

          - **Mode** *(string) --* 

            The tracing mode associated with your Lambda function.

            
      
        

        - **MasterArn** *(string) --* 

          Returns the ARN (Amazon Resource Name) of the master function.

          
    

    **Examples** 

    This operation retrieves a Lambda function's event source mapping
    ::

      response = client.get_function_configuration(
          FunctionName='myFunction',
          Qualifier='1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CodeSha256': 'LQT+0DHxxxxcfwLyQjzoEFKZtdqQjHXanlSdfXBlEW0VA=',
          'CodeSize': 123,
          'DeadLetterConfig': {
          },
          'Description': '',
          'Environment': {
          },
          'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction',
          'FunctionName': 'myFunction',
          'Handler': 'index.handler',
          'KMSKeyArn': '',
          'LastModified': '2016-11-21T19:49:20.006+0000',
          'MemorySize': 128,
          'Role': 'arn:aws:iam::123456789012:role/lambda_basic_execution',
          'Runtime': 'python2.7',
          'Timeout': 123,
          'Version': '1',
          'VpcConfig': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

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


  .. py:method:: get_policy(**kwargs)

    

    Returns the resource policy associated with the specified Lambda function.

     

    If you are using the versioning feature, you can get the resource policy associated with the specific Lambda function version or alias by specifying the version or alias name using the ``Qualifier`` parameter. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    You need permission for the ``lambda:GetPolicy action.``  

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetPolicy>`_    


    **Request Syntax** 
    ::

      response = client.get_policy(
          FunctionName='string',
          Qualifier='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      Function name whose resource policy you want to retrieve.

       

      You can specify the function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type Qualifier: string
    :param Qualifier: 

      You can specify this optional query parameter to specify a function version or an alias name in which case this API will return all permissions associated with the specific qualified ARN. If you don't provide this parameter, the API will return permissions that apply to the unqualified function ARN.

      

    
    
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

          The resource policy associated with the specified function. The response returns the same as a string using a backslash ("\") as an escape character in the JSON.

          
    

    **Examples** 

    This operation retrieves a Lambda function policy
    ::

      response = client.get_policy(
          FunctionName='myFunction',
          Qualifier='1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Policy': '',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: invoke(**kwargs)

    

    Invokes a specific Lambda function. For an example, see `Create the Lambda Function and Test It Manually <http://docs.aws.amazon.com/lambda/latest/dg/with-dynamodb-create-function.html#with-dbb-invoke-manually>`__ . 

     

    If you are using the versioning feature, you can invoke the specific function version by providing function version or alias name that is pointing to the function version using the ``Qualifier`` parameter in the request. If you don't provide the ``Qualifier`` parameter, the ``$LATEST`` version of the Lambda function is invoked. Invocations occur at least once in response to an event and functions must be idempotent to handle this. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    This operation requires permission for the ``lambda:InvokeFunction`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/Invoke>`_    


    **Request Syntax** 
    ::

      response = client.invoke(
          FunctionName='string',
          InvocationType='Event'|'RequestResponse'|'DryRun',
          LogType='None'|'Tail',
          ClientContext='string',
          Payload=b'bytes'|file,
          Qualifier='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The Lambda function name.

       

      You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type InvocationType: string
    :param InvocationType: 

      By default, the ``Invoke`` API assumes ``RequestResponse`` invocation type. You can optionally request asynchronous execution by specifying ``Event`` as the ``InvocationType`` . You can also use this parameter to request AWS Lambda to not execute the function but do some verification, such as if the caller is authorized to invoke the function and if the inputs are valid. You request this by specifying ``DryRun`` as the ``InvocationType`` . This is useful in a cross-account scenario when you want to verify access to a function without running it. 

      

    
    :type LogType: string
    :param LogType: 

      You can set this optional parameter to ``Tail`` in the request only if you specify the ``InvocationType`` parameter with value ``RequestResponse`` . In this case, AWS Lambda returns the base64-encoded last 4 KB of log data produced by your Lambda function in the ``x-amz-log-result`` header. 

      

    
    :type ClientContext: string
    :param ClientContext: 

      Using the ``ClientContext`` you can pass client-specific information to the Lambda function you are invoking. You can then process the client information in your Lambda function as you choose through the context variable. For an example of a ``ClientContext`` JSON, see `PutEvents <http://docs.aws.amazon.com/mobileanalytics/latest/ug/PutEvents.html>`__ in the *Amazon Mobile Analytics API Reference and User Guide* .

       

      The ClientContext JSON must be base64-encoded and has a maximum size of 3583 bytes.

      

    
    :type Payload: bytes or seekable file-like object
    :param Payload: 

      JSON that you want to provide to your Lambda function as input.

      

    
    :type Qualifier: string
    :param Qualifier: 

      You can use this optional parameter to specify a Lambda function version or alias name. If you specify a function version, the API uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the API uses the alias ARN to invoke the Lambda function version to which the alias points.

       

      If you don't provide this parameter, then the API uses unqualified function ARN which results in invocation of the ``$LATEST`` version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StatusCode': 123,
            'FunctionError': 'string',
            'LogResult': 'string',
            'Payload': StreamingBody(),
            'ExecutedVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Upon success, returns an empty response. Otherwise, throws an exception.

        
        

        - **StatusCode** *(integer) --* 

          The HTTP status code will be in the 200 range for successful request. For the ``RequestResponse`` invocation type this status code will be 200. For the ``Event`` invocation type this status code will be 202. For the ``DryRun`` invocation type the status code will be 204. 

          
        

        - **FunctionError** *(string) --* 

          Indicates whether an error occurred while executing the Lambda function. If an error occurred this field will have one of two values; ``Handled`` or ``Unhandled`` . ``Handled`` errors are errors that are reported by the function while the ``Unhandled`` errors are those detected and reported by AWS Lambda. Unhandled errors include out of memory errors and function timeouts. For information about how to report an ``Handled`` error, see `Programming Model <http://docs.aws.amazon.com/lambda/latest/dg/programming-model.html>`__ . 

          
        

        - **LogResult** *(string) --* 

          It is the base64-encoded logs for the Lambda function invocation. This is present only if the invocation type is ``RequestResponse`` and the logs were requested. 

          
        

        - **Payload** (:class:`.StreamingBody`) -- 

          It is the JSON representation of the object returned by the Lambda function. This is present only if the invocation type is ``RequestResponse`` . 

           

          In the event of a function error this field contains a message describing the error. For the ``Handled`` errors the Lambda function will report this message. For ``Unhandled`` errors AWS Lambda reports the message. 

          
        

        - **ExecutedVersion** *(string) --* 

          The function version that has been executed. This value is returned only if the invocation type is ``RequestResponse`` .

          
    

    **Examples** 

    This operation invokes a Lambda function
    ::

      response = client.invoke(
          ClientContext='MyApp',
          FunctionName='MyFunction',
          InvocationType='Event',
          LogType='Tail',
          Payload='fileb://file-path/input.json',
          Qualifier='1',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'FunctionError': '',
          'LogResult': '',
          'Payload': '?',
          'StatusCode': 123,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: invoke_async(**kwargs)

    

    .. warning::

       

      This API is deprecated. We recommend you use ``Invoke`` API (see  Invoke ).

       

     

    Submits an invocation request to AWS Lambda. Upon receiving the request, Lambda executes the specified function asynchronously. To see the logs generated by the Lambda function execution, see the CloudWatch Logs console.

     

    This operation requires permission for the ``lambda:InvokeFunction`` action.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/InvokeAsync>`_    


    **Request Syntax** 
    ::

      response = client.invoke_async(
          FunctionName='string',
          InvokeArgs=b'bytes'|file
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The Lambda function name. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

      

    
    :type InvokeArgs: bytes or seekable file-like object
    :param InvokeArgs: **[REQUIRED]** 

      JSON that you want to provide to your Lambda function as input.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Status': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        Upon success, it returns empty response. Otherwise, throws an exception.

        
        

        - **Status** *(integer) --* 

          It will be 202 upon success.

          
    

    **Examples** 

    This operation invokes a Lambda function asynchronously
    ::

      response = client.invoke_async(
          FunctionName='myFunction',
          InvokeArgs='fileb://file-path/input.json',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Status': 123,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_aliases(**kwargs)

    

    Returns list of aliases created for a Lambda function. For each alias, the response includes information such as the alias ARN, description, alias name, and the function version to which it points. For more information, see `Introduction to AWS Lambda Aliases <http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

     

    This requires permission for the lambda:ListAliases action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListAliases>`_    


    **Request Syntax** 
    ::

      response = client.list_aliases(
          FunctionName='string',
          FunctionVersion='string',
          Marker='string',
          MaxItems=123
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      Lambda function name for which the alias is created. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

      

    
    :type FunctionVersion: string
    :param FunctionVersion: 

      If you specify this optional parameter, the API returns only the aliases that are pointing to the specific Lambda function version, otherwise the API returns all of the aliases created for the Lambda function.

      

    
    :type Marker: string
    :param Marker: 

      Optional string. An opaque pagination token returned from a previous ``ListAliases`` operation. If present, indicates where to continue the listing.

      

    
    :type MaxItems: integer
    :param MaxItems: 

      Optional integer. Specifies the maximum number of aliases to return in response. This parameter value must be greater than 0.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'Aliases': [
                {
                    'AliasArn': 'string',
                    'Name': 'string',
                    'FunctionVersion': 'string',
                    'Description': 'string',
                    'RoutingConfig': {
                        'AdditionalVersionWeights': {
                            'string': 123.0
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          A string, present if there are more aliases.

          
        

        - **Aliases** *(list) --* 

          A list of aliases.

          
          

          - *(dict) --* 

            Provides configuration information about a Lambda function version alias.

            
            

            - **AliasArn** *(string) --* 

              Lambda function ARN that is qualified using the alias name as the suffix. For example, if you create an alias called ``BETA`` that points to a helloworld function version, the ARN is ``arn:aws:lambda:aws-regions:acct-id:function:helloworld:BETA`` .

              
            

            - **Name** *(string) --* 

              Alias name.

              
            

            - **FunctionVersion** *(string) --* 

              Function version to which the alias points.

              
            

            - **Description** *(string) --* 

              Alias description.

              
            

            - **RoutingConfig** *(dict) --* 

              Specifies an additional function versions the alias points to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see  lambda-traffic-shifting-using-aliases .

              
              

              - **AdditionalVersionWeights** *(dict) --* 

                Set this property value to dictate what percentage of traffic will invoke the updated function version. If set to an empty string, 100 percent of traffic will invoke ``function-version`` .

                
                

                - *(string) --* 
                  

                  - *(float) --* 
            
          
          
        
      
    

    **Examples** 

    This operation retrieves a Lambda function's aliases
    ::

      response = client.list_aliases(
          FunctionName='myFunction',
          FunctionVersion='1',
          Marker='',
          MaxItems=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Aliases': [
          ],
          'NextMarker': '',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_event_source_mappings(**kwargs)

    

    Returns a list of event source mappings you created using the ``CreateEventSourceMapping`` (see  CreateEventSourceMapping ). 

     

    For each mapping, the API returns configuration information. You can optionally specify filters to retrieve specific event source mappings.

     

    If you are using the versioning feature, you can get list of event source mappings for a specific Lambda function version or an alias as described in the ``FunctionName`` parameter. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    This operation requires permission for the ``lambda:ListEventSourceMappings`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListEventSourceMappings>`_    


    **Request Syntax** 
    ::

      response = client.list_event_source_mappings(
          EventSourceArn='string',
          FunctionName='string',
          Marker='string',
          MaxItems=123
      )
    :type EventSourceArn: string
    :param EventSourceArn: 

      The Amazon Resource Name (ARN) of the Amazon Kinesis stream. (This parameter is optional.)

      

    
    :type FunctionName: string
    :param FunctionName: 

      The name of the Lambda function.

       

      You can specify the function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type Marker: string
    :param Marker: 

      Optional string. An opaque pagination token returned from a previous ``ListEventSourceMappings`` operation. If present, specifies to continue the list from where the returning call left off. 

      

    
    :type MaxItems: integer
    :param MaxItems: 

      Optional integer. Specifies the maximum number of event sources to return in response. This value must be greater than 0.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'EventSourceMappings': [
                {
                    'UUID': 'string',
                    'BatchSize': 123,
                    'EventSourceArn': 'string',
                    'FunctionArn': 'string',
                    'LastModified': datetime(2015, 1, 1),
                    'LastProcessingResult': 'string',
                    'State': 'string',
                    'StateTransitionReason': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains a list of event sources (see  EventSourceMappingConfiguration )

        
        

        - **NextMarker** *(string) --* 

          A string, present if there are more event source mappings.

          
        

        - **EventSourceMappings** *(list) --* 

          An array of ``EventSourceMappingConfiguration`` objects.

          
          

          - *(dict) --* 

            Describes mapping between an Amazon Kinesis stream and a Lambda function.

            
            

            - **UUID** *(string) --* 

              The AWS Lambda assigned opaque identifier for the mapping.

              
            

            - **BatchSize** *(integer) --* 

              The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.

              
            

            - **EventSourceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon Kinesis stream that is the source of events.

              
            

            - **FunctionArn** *(string) --* 

              The Lambda function to invoke when AWS Lambda detects an event on the stream.

              
            

            - **LastModified** *(datetime) --* 

              The UTC time string indicating the last time the event mapping was updated.

              
            

            - **LastProcessingResult** *(string) --* 

              The result of the last AWS Lambda invocation of your Lambda function.

              
            

            - **State** *(string) --* 

              The state of the event source mapping. It can be ``Creating`` , ``Enabled`` , ``Disabled`` , ``Enabling`` , ``Disabling`` , ``Updating`` , or ``Deleting`` .

              
            

            - **StateTransitionReason** *(string) --* 

              The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.

              
        
      
    

  .. py:method:: list_functions(**kwargs)

    

    Returns a list of your Lambda functions. For each function, the response includes the function configuration information. You must use  GetFunction to retrieve the code for your function.

     

    This operation requires permission for the ``lambda:ListFunctions`` action.

     

    If you are using the versioning feature, you can list all of your functions or only ``$LATEST`` versions. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListFunctions>`_    


    **Request Syntax** 
    ::

      response = client.list_functions(
          MasterRegion='string',
          FunctionVersion='ALL',
          Marker='string',
          MaxItems=123
      )
    :type MasterRegion: string
    :param MasterRegion: 

      Optional string. If not specified, will return only regular function versions (i.e., non-replicated versions).

       

      Valid values are:

       

      The region from which the functions are replicated. For example, if you specify ``us-east-1`` , only functions replicated from that region will be returned.

       

       ``ALL`` : Will return all functions from any region. If specified, you also must specify a valid FunctionVersion parameter.

      

    
    :type FunctionVersion: string
    :param FunctionVersion: 

      Optional string. If not specified, only the unqualified functions ARNs (Amazon Resource Names) will be returned.

       

      Valid value:

       

       ``ALL`` : Will return all versions, including ``$LATEST`` which will have fully qualified ARNs (Amazon Resource Names).

      

    
    :type Marker: string
    :param Marker: 

      Optional string. An opaque pagination token returned from a previous ``ListFunctions`` operation. If present, indicates where to continue the listing. 

      

    
    :type MaxItems: integer
    :param MaxItems: 

      Optional integer. Specifies the maximum number of AWS Lambda functions to return in response. This parameter value must be greater than 0.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'Functions': [
                {
                    'FunctionName': 'string',
                    'FunctionArn': 'string',
                    'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
                    'Role': 'string',
                    'Handler': 'string',
                    'CodeSize': 123,
                    'Description': 'string',
                    'Timeout': 123,
                    'MemorySize': 123,
                    'LastModified': 'string',
                    'CodeSha256': 'string',
                    'Version': 'string',
                    'VpcConfig': {
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'VpcId': 'string'
                    },
                    'DeadLetterConfig': {
                        'TargetArn': 'string'
                    },
                    'Environment': {
                        'Variables': {
                            'string': 'string'
                        },
                        'Error': {
                            'ErrorCode': 'string',
                            'Message': 'string'
                        }
                    },
                    'KMSKeyArn': 'string',
                    'TracingConfig': {
                        'Mode': 'Active'|'PassThrough'
                    },
                    'MasterArn': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains a list of AWS Lambda function configurations (see  FunctionConfiguration .

        
        

        - **NextMarker** *(string) --* 

          A string, present if there are more functions.

          
        

        - **Functions** *(list) --* 

          A list of Lambda functions.

          
          

          - *(dict) --* 

            A complex type that describes function metadata.

            
            

            - **FunctionName** *(string) --* 

              The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

              
            

            - **FunctionArn** *(string) --* 

              The Amazon Resource Name (ARN) assigned to the function.

              
            

            - **Runtime** *(string) --* 

              The runtime environment for the Lambda function.

              
            

            - **Role** *(string) --* 

              The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

              
            

            - **Handler** *(string) --* 

              The function Lambda calls to begin executing your function.

              
            

            - **CodeSize** *(integer) --* 

              The size, in bytes, of the function .zip file you uploaded.

              
            

            - **Description** *(string) --* 

              The user-provided description.

              
            

            - **Timeout** *(integer) --* 

              The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

              
            

            - **MemorySize** *(integer) --* 

              The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

              
            

            - **LastModified** *(string) --* 

              The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

              
            

            - **CodeSha256** *(string) --* 

              It is the SHA256 hash of your function deployment package.

              
            

            - **Version** *(string) --* 

              The version of the Lambda function.

              
            

            - **VpcConfig** *(dict) --* 

              VPC configuration associated with your Lambda function.

              
              

              - **SubnetIds** *(list) --* 

                A list of subnet IDs associated with the Lambda function.

                
                

                - *(string) --* 
            
              

              - **SecurityGroupIds** *(list) --* 

                A list of security group IDs associated with the Lambda function.

                
                

                - *(string) --* 
            
              

              - **VpcId** *(string) --* 

                The VPC ID associated with you Lambda function.

                
          
            

            - **DeadLetterConfig** *(dict) --* 

              The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

              
              

              - **TargetArn** *(string) --* 

                The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

                
          
            

            - **Environment** *(dict) --* 

              The parent object that contains your environment's configuration settings.

              
              

              - **Variables** *(dict) --* 

                The key-value pairs returned that represent your environment's configuration settings or error information.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Error** *(dict) --* 

                The parent object that contains error information associated with your configuration settings.

                
                

                - **ErrorCode** *(string) --* 

                  The error code returned by the environment error object.

                  
                

                - **Message** *(string) --* 

                  The message returned by the environment error object.

                  
            
          
            

            - **KMSKeyArn** *(string) --* 

              The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

              
            

            - **TracingConfig** *(dict) --* 

              The parent object that contains your function's tracing settings.

              
              

              - **Mode** *(string) --* 

                The tracing mode associated with your Lambda function.

                
          
            

            - **MasterArn** *(string) --* 

              Returns the ARN (Amazon Resource Name) of the master function.

              
        
      
    

    **Examples** 

    This operation retrieves a Lambda functions
    ::

      response = client.list_functions(
          Marker='',
          MaxItems=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Functions': [
          ],
          'NextMarker': '',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_tags(**kwargs)

    

    Returns a list of tags assigned to a function when supplied the function ARN (Amazon Resource Name).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListTags>`_    


    **Request Syntax** 
    ::

      response = client.list_tags(
          Resource='string'
      )
    :type Resource: string
    :param Resource: **[REQUIRED]** 

      The ARN (Amazon Resource Name) of the function.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tags': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Tags** *(dict) --* 

          The list of tags assigned to the function.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: list_versions_by_function(**kwargs)

    

    List all versions of a function. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListVersionsByFunction>`_    


    **Request Syntax** 
    ::

      response = client.list_versions_by_function(
          FunctionName='string',
          Marker='string',
          MaxItems=123
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      Function name whose versions to list. You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type Marker: string
    :param Marker: 

      Optional string. An opaque pagination token returned from a previous ``ListVersionsByFunction`` operation. If present, indicates where to continue the listing. 

      

    
    :type MaxItems: integer
    :param MaxItems: 

      Optional integer. Specifies the maximum number of AWS Lambda function versions to return in response. This parameter value must be greater than 0.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'Versions': [
                {
                    'FunctionName': 'string',
                    'FunctionArn': 'string',
                    'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
                    'Role': 'string',
                    'Handler': 'string',
                    'CodeSize': 123,
                    'Description': 'string',
                    'Timeout': 123,
                    'MemorySize': 123,
                    'LastModified': 'string',
                    'CodeSha256': 'string',
                    'Version': 'string',
                    'VpcConfig': {
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'VpcId': 'string'
                    },
                    'DeadLetterConfig': {
                        'TargetArn': 'string'
                    },
                    'Environment': {
                        'Variables': {
                            'string': 'string'
                        },
                        'Error': {
                            'ErrorCode': 'string',
                            'Message': 'string'
                        }
                    },
                    'KMSKeyArn': 'string',
                    'TracingConfig': {
                        'Mode': 'Active'|'PassThrough'
                    },
                    'MasterArn': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **NextMarker** *(string) --* 

          A string, present if there are more function versions.

          
        

        - **Versions** *(list) --* 

          A list of Lambda function versions.

          
          

          - *(dict) --* 

            A complex type that describes function metadata.

            
            

            - **FunctionName** *(string) --* 

              The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

              
            

            - **FunctionArn** *(string) --* 

              The Amazon Resource Name (ARN) assigned to the function.

              
            

            - **Runtime** *(string) --* 

              The runtime environment for the Lambda function.

              
            

            - **Role** *(string) --* 

              The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

              
            

            - **Handler** *(string) --* 

              The function Lambda calls to begin executing your function.

              
            

            - **CodeSize** *(integer) --* 

              The size, in bytes, of the function .zip file you uploaded.

              
            

            - **Description** *(string) --* 

              The user-provided description.

              
            

            - **Timeout** *(integer) --* 

              The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

              
            

            - **MemorySize** *(integer) --* 

              The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

              
            

            - **LastModified** *(string) --* 

              The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

              
            

            - **CodeSha256** *(string) --* 

              It is the SHA256 hash of your function deployment package.

              
            

            - **Version** *(string) --* 

              The version of the Lambda function.

              
            

            - **VpcConfig** *(dict) --* 

              VPC configuration associated with your Lambda function.

              
              

              - **SubnetIds** *(list) --* 

                A list of subnet IDs associated with the Lambda function.

                
                

                - *(string) --* 
            
              

              - **SecurityGroupIds** *(list) --* 

                A list of security group IDs associated with the Lambda function.

                
                

                - *(string) --* 
            
              

              - **VpcId** *(string) --* 

                The VPC ID associated with you Lambda function.

                
          
            

            - **DeadLetterConfig** *(dict) --* 

              The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

              
              

              - **TargetArn** *(string) --* 

                The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

                
          
            

            - **Environment** *(dict) --* 

              The parent object that contains your environment's configuration settings.

              
              

              - **Variables** *(dict) --* 

                The key-value pairs returned that represent your environment's configuration settings or error information.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Error** *(dict) --* 

                The parent object that contains error information associated with your configuration settings.

                
                

                - **ErrorCode** *(string) --* 

                  The error code returned by the environment error object.

                  
                

                - **Message** *(string) --* 

                  The message returned by the environment error object.

                  
            
          
            

            - **KMSKeyArn** *(string) --* 

              The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

              
            

            - **TracingConfig** *(dict) --* 

              The parent object that contains your function's tracing settings.

              
              

              - **Mode** *(string) --* 

                The tracing mode associated with your Lambda function.

                
          
            

            - **MasterArn** *(string) --* 

              Returns the ARN (Amazon Resource Name) of the master function.

              
        
      
    

    **Examples** 

    This operation retrieves a Lambda function versions
    ::

      response = client.list_versions_by_function(
          FunctionName='myFunction',
          Marker='',
          MaxItems=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'NextMarker': '',
          'Versions': [
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: publish_version(**kwargs)

    

    Publishes a version of your function from the current snapshot of $LATEST. That is, AWS Lambda takes a snapshot of the function code and configuration information from $LATEST and publishes a new version. The code and configuration cannot be modified after publication. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PublishVersion>`_    


    **Request Syntax** 
    ::

      response = client.publish_version(
          FunctionName='string',
          CodeSha256='string',
          Description='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The Lambda function name. You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type CodeSha256: string
    :param CodeSha256: 

      The SHA256 hash of the deployment package you want to publish. This provides validation on the code you are publishing. If you provide this parameter, the value must match the SHA256 of the $LATEST version for the publication to succeed. You can use the **DryRun** parameter of  UpdateFunctionCode to verify the hash value that will be returned before publishing your new version.

      

    
    :type Description: string
    :param Description: 

      The description for the version you are publishing. If not provided, AWS Lambda copies the description from the $LATEST version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that describes function metadata.

        
        

        - **FunctionName** *(string) --* 

          The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

          
        

        - **FunctionArn** *(string) --* 

          The Amazon Resource Name (ARN) assigned to the function.

          
        

        - **Runtime** *(string) --* 

          The runtime environment for the Lambda function.

          
        

        - **Role** *(string) --* 

          The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

          
        

        - **Handler** *(string) --* 

          The function Lambda calls to begin executing your function.

          
        

        - **CodeSize** *(integer) --* 

          The size, in bytes, of the function .zip file you uploaded.

          
        

        - **Description** *(string) --* 

          The user-provided description.

          
        

        - **Timeout** *(integer) --* 

          The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

          
        

        - **MemorySize** *(integer) --* 

          The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

          
        

        - **LastModified** *(string) --* 

          The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

          
        

        - **CodeSha256** *(string) --* 

          It is the SHA256 hash of your function deployment package.

          
        

        - **Version** *(string) --* 

          The version of the Lambda function.

          
        

        - **VpcConfig** *(dict) --* 

          VPC configuration associated with your Lambda function.

          
          

          - **SubnetIds** *(list) --* 

            A list of subnet IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **SecurityGroupIds** *(list) --* 

            A list of security group IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **VpcId** *(string) --* 

            The VPC ID associated with you Lambda function.

            
      
        

        - **DeadLetterConfig** *(dict) --* 

          The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

          
          

          - **TargetArn** *(string) --* 

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

            
      
        

        - **Environment** *(dict) --* 

          The parent object that contains your environment's configuration settings.

          
          

          - **Variables** *(dict) --* 

            The key-value pairs returned that represent your environment's configuration settings or error information.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **Error** *(dict) --* 

            The parent object that contains error information associated with your configuration settings.

            
            

            - **ErrorCode** *(string) --* 

              The error code returned by the environment error object.

              
            

            - **Message** *(string) --* 

              The message returned by the environment error object.

              
        
      
        

        - **KMSKeyArn** *(string) --* 

          The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

          
        

        - **TracingConfig** *(dict) --* 

          The parent object that contains your function's tracing settings.

          
          

          - **Mode** *(string) --* 

            The tracing mode associated with your Lambda function.

            
      
        

        - **MasterArn** *(string) --* 

          Returns the ARN (Amazon Resource Name) of the master function.

          
    

    **Examples** 

    This operation publishes a version of a Lambda function
    ::

      response = client.publish_version(
          CodeSha256='',
          Description='',
          FunctionName='myFunction',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CodeSha256': '',
          'CodeSize': 123,
          'Description': '',
          'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction:1',
          'FunctionName': 'myFunction',
          'Handler': 'index.handler',
          'LastModified': '2016-11-21T19:49:20.006+0000',
          'MemorySize': 128,
          'Role': 'arn:aws:iam::123456789012:role/lambda_basic_execution',
          'Runtime': 'python2.7',
          'Timeout': 123,
          'Version': '1',
          'VpcConfig': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: put_function_concurrency(**kwargs)

    

    Sets a limit on the number of concurrent executions available to this function. It is a subset of your account's total concurrent execution limit per region. Note that Lambda automatically reserves a buffer of 100 concurrent executions for functions without any reserved concurrency limit. This means if your account limit is 1000, you have a total of 900 available to allocate to individual functions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PutFunctionConcurrency>`_    


    **Request Syntax** 
    ::

      response = client.put_function_concurrency(
          FunctionName='string',
          ReservedConcurrentExecutions=123
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The name of the function you are setting concurrent execution limits on.

      

    
    :type ReservedConcurrentExecutions: integer
    :param ReservedConcurrentExecutions: **[REQUIRED]** 

      The concurrent execution limit reserved for this function.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ReservedConcurrentExecutions': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ReservedConcurrentExecutions** *(integer) --* 

          The number of concurrent executions reserved for this function.

          
    

  .. py:method:: remove_permission(**kwargs)

    

    You can remove individual permissions from an resource policy associated with a Lambda function by providing a statement ID that you provided when you added the permission.

     

    If you are using versioning, the permissions you remove are specific to the Lambda function version or alias you specify in the ``AddPermission`` request via the ``Qualifier`` parameter. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    Note that removal of a permission will cause an active event source to lose permission to the function.

     

    You need permission for the ``lambda:RemovePermission`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/RemovePermission>`_    


    **Request Syntax** 
    ::

      response = client.remove_permission(
          FunctionName='string',
          StatementId='string',
          Qualifier='string'
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      Lambda function whose resource policy you want to remove a permission from.

       

      You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type StatementId: string
    :param StatementId: **[REQUIRED]** 

      Statement ID of the permission to remove.

      

    
    :type Qualifier: string
    :param Qualifier: 

      You can specify this optional parameter to remove permission associated with a specific function version or function alias. If you don't specify this parameter, the API removes permission associated with the unqualified function ARN.

      

    
    
    :returns: None

    **Examples** 

    This operation removes a Lambda function's permissions
    ::

      response = client.remove_permission(
          FunctionName='myFunction',
          Qualifier='1',
          StatementId='role-statement-id',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: tag_resource(**kwargs)

    

    Creates a list of tags (key-value pairs) on the Lambda function. Requires the Lambda function ARN (Amazon Resource Name). If a key is specified without a value, Lambda creates a tag with the specified key and a value of null. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/TagResource>`_    


    **Request Syntax** 
    ::

      response = client.tag_resource(
          Resource='string',
          Tags={
              'string': 'string'
          }
      )
    :type Resource: string
    :param Resource: **[REQUIRED]** 

      The ARN (Amazon Resource Name) of the Lambda function.

      

    
    :type Tags: dict
    :param Tags: **[REQUIRED]** 

      The list of tags (key-value pairs) you are assigning to the Lambda function.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :returns: None

  .. py:method:: untag_resource(**kwargs)

    

    Removes tags from a Lambda function. Requires the function ARN (Amazon Resource Name). 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UntagResource>`_    


    **Request Syntax** 
    ::

      response = client.untag_resource(
          Resource='string',
          TagKeys=[
              'string',
          ]
      )
    :type Resource: string
    :param Resource: **[REQUIRED]** 

      The ARN (Amazon Resource Name) of the function.

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      The list of tag keys to be deleted from the function.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: update_alias(**kwargs)

    

    Using this API you can update the function version to which the alias points and the alias description. For more information, see `Introduction to AWS Lambda Aliases <http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

     

    This requires permission for the lambda:UpdateAlias action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateAlias>`_    


    **Request Syntax** 
    ::

      response = client.update_alias(
          FunctionName='string',
          Name='string',
          FunctionVersion='string',
          Description='string',
          RoutingConfig={
              'AdditionalVersionWeights': {
                  'string': 123.0
              }
          }
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The function name for which the alias is created. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The alias name.

      

    
    :type FunctionVersion: string
    :param FunctionVersion: 

      Using this parameter you can change the Lambda function version to which the alias points.

      

    
    :type Description: string
    :param Description: 

      You can change the description of the alias using this parameter.

      

    
    :type RoutingConfig: dict
    :param RoutingConfig: 

      Specifies an additional version your alias can point to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see  lambda-traffic-shifting-using-aliases .

      

    
      - **AdditionalVersionWeights** *(dict) --* 

        Set this property value to dictate what percentage of traffic will invoke the updated function version. If set to an empty string, 100 percent of traffic will invoke ``function-version`` .

        

      
        - *(string) --* 

        
          - *(float) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AliasArn': 'string',
            'Name': 'string',
            'FunctionVersion': 'string',
            'Description': 'string',
            'RoutingConfig': {
                'AdditionalVersionWeights': {
                    'string': 123.0
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Provides configuration information about a Lambda function version alias.

        
        

        - **AliasArn** *(string) --* 

          Lambda function ARN that is qualified using the alias name as the suffix. For example, if you create an alias called ``BETA`` that points to a helloworld function version, the ARN is ``arn:aws:lambda:aws-regions:acct-id:function:helloworld:BETA`` .

          
        

        - **Name** *(string) --* 

          Alias name.

          
        

        - **FunctionVersion** *(string) --* 

          Function version to which the alias points.

          
        

        - **Description** *(string) --* 

          Alias description.

          
        

        - **RoutingConfig** *(dict) --* 

          Specifies an additional function versions the alias points to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see  lambda-traffic-shifting-using-aliases .

          
          

          - **AdditionalVersionWeights** *(dict) --* 

            Set this property value to dictate what percentage of traffic will invoke the updated function version. If set to an empty string, 100 percent of traffic will invoke ``function-version`` .

            
            

            - *(string) --* 
              

              - *(float) --* 
        
      
      
    

    **Examples** 

    This operation updates a Lambda function alias
    ::

      response = client.update_alias(
          Description='',
          FunctionName='myFunction',
          FunctionVersion='1',
          Name='functionAlias',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AliasArn': 'arn:aws:lambda:us-west-2:123456789012:function:functionAlias',
          'Description': '',
          'FunctionVersion': '1',
          'Name': 'functionAlias',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_event_source_mapping(**kwargs)

    

    You can update an event source mapping. This is useful if you want to change the parameters of the existing mapping without losing your position in the stream. You can change which function will receive the stream records, but to change the stream itself, you must create a new mapping.

     

    If you are using the versioning feature, you can update the event source mapping to map to a specific Lambda function version or alias as described in the ``FunctionName`` parameter. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    If you disable the event source mapping, AWS Lambda stops polling. If you enable again, it will resume polling from the time it had stopped polling, so you don't lose processing of any records. However, if you delete event source mapping and create it again, it will reset.

     

    This operation requires permission for the ``lambda:UpdateEventSourceMapping`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateEventSourceMapping>`_    


    **Request Syntax** 
    ::

      response = client.update_event_source_mapping(
          UUID='string',
          FunctionName='string',
          Enabled=True|False,
          BatchSize=123
      )
    :type UUID: string
    :param UUID: **[REQUIRED]** 

      The event source mapping identifier.

      

    
    :type FunctionName: string
    :param FunctionName: 

      The Lambda function to which you want the stream records sent.

       

      You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

       

      If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__  

       

      Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length.

      

    
    :type Enabled: boolean
    :param Enabled: 

      Specifies whether AWS Lambda should actively poll the stream or not. If disabled, AWS Lambda will not poll the stream.

      

    
    :type BatchSize: integer
    :param BatchSize: 

      The maximum number of stream records that can be sent to your Lambda function for a single invocation.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UUID': 'string',
            'BatchSize': 123,
            'EventSourceArn': 'string',
            'FunctionArn': 'string',
            'LastModified': datetime(2015, 1, 1),
            'LastProcessingResult': 'string',
            'State': 'string',
            'StateTransitionReason': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes mapping between an Amazon Kinesis stream and a Lambda function.

        
        

        - **UUID** *(string) --* 

          The AWS Lambda assigned opaque identifier for the mapping.

          
        

        - **BatchSize** *(integer) --* 

          The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.

          
        

        - **EventSourceArn** *(string) --* 

          The Amazon Resource Name (ARN) of the Amazon Kinesis stream that is the source of events.

          
        

        - **FunctionArn** *(string) --* 

          The Lambda function to invoke when AWS Lambda detects an event on the stream.

          
        

        - **LastModified** *(datetime) --* 

          The UTC time string indicating the last time the event mapping was updated.

          
        

        - **LastProcessingResult** *(string) --* 

          The result of the last AWS Lambda invocation of your Lambda function.

          
        

        - **State** *(string) --* 

          The state of the event source mapping. It can be ``Creating`` , ``Enabled`` , ``Disabled`` , ``Enabling`` , ``Disabling`` , ``Updating`` , or ``Deleting`` .

          
        

        - **StateTransitionReason** *(string) --* 

          The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.

          
    

    **Examples** 

    This operation updates a Lambda function event source mapping
    ::

      response = client.update_event_source_mapping(
          BatchSize=123,
          Enabled=True,
          FunctionName='myFunction',
          UUID='1234xCy789012',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'BatchSize': 123,
          'EventSourceArn': 'arn:aws:s3:::examplebucket/*',
          'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction',
          'LastModified': datetime(2016, 11, 21, 19, 49, 20, 0, 326, 0),
          'LastProcessingResult': '',
          'State': '',
          'StateTransitionReason': '',
          'UUID': '1234xCy789012',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_function_code(**kwargs)

    

    Updates the code for the specified Lambda function. This operation must only be used on an existing Lambda function and cannot be used to update the function configuration.

     

    If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    This operation requires permission for the ``lambda:UpdateFunctionCode`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateFunctionCode>`_    


    **Request Syntax** 
    ::

      response = client.update_function_code(
          FunctionName='string',
          ZipFile=b'bytes',
          S3Bucket='string',
          S3Key='string',
          S3ObjectVersion='string',
          Publish=True|False,
          DryRun=True|False
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The existing Lambda function name whose code you want to replace.

       

      You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
    :type ZipFile: bytes
    :param ZipFile: 

      The contents of your zip file containing your deployment package. If you are using the web API directly, the contents of the zip file must be base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or CLI will do the encoding for you. For more information about creating a .zip file, see `Execution Permissions <http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role.html>`__ in the *AWS Lambda Developer Guide* . 

            **This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.**


    
    :type S3Bucket: string
    :param S3Bucket: 

      Amazon S3 bucket name where the .zip file containing your deployment package is stored. This bucket must reside in the same AWS Region where you are creating the Lambda function.

      

    
    :type S3Key: string
    :param S3Key: 

      The Amazon S3 object (the deployment package) key name you want to upload.

      

    
    :type S3ObjectVersion: string
    :param S3ObjectVersion: 

      The Amazon S3 object (the deployment package) version you want to upload.

      

    
    :type Publish: boolean
    :param Publish: 

      This boolean parameter can be used to request AWS Lambda to update the Lambda function and publish a version as an atomic operation.

      

    
    :type DryRun: boolean
    :param DryRun: 

      This boolean parameter can be used to test your request to AWS Lambda to update the Lambda function and publish a version as an atomic operation. It will do all necessary computation and validation of your code but will not upload it or a publish a version. Each time this operation is invoked, the ``CodeSha256`` hash value of the provided code will also be computed and returned in the response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that describes function metadata.

        
        

        - **FunctionName** *(string) --* 

          The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

          
        

        - **FunctionArn** *(string) --* 

          The Amazon Resource Name (ARN) assigned to the function.

          
        

        - **Runtime** *(string) --* 

          The runtime environment for the Lambda function.

          
        

        - **Role** *(string) --* 

          The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

          
        

        - **Handler** *(string) --* 

          The function Lambda calls to begin executing your function.

          
        

        - **CodeSize** *(integer) --* 

          The size, in bytes, of the function .zip file you uploaded.

          
        

        - **Description** *(string) --* 

          The user-provided description.

          
        

        - **Timeout** *(integer) --* 

          The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

          
        

        - **MemorySize** *(integer) --* 

          The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

          
        

        - **LastModified** *(string) --* 

          The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

          
        

        - **CodeSha256** *(string) --* 

          It is the SHA256 hash of your function deployment package.

          
        

        - **Version** *(string) --* 

          The version of the Lambda function.

          
        

        - **VpcConfig** *(dict) --* 

          VPC configuration associated with your Lambda function.

          
          

          - **SubnetIds** *(list) --* 

            A list of subnet IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **SecurityGroupIds** *(list) --* 

            A list of security group IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **VpcId** *(string) --* 

            The VPC ID associated with you Lambda function.

            
      
        

        - **DeadLetterConfig** *(dict) --* 

          The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

          
          

          - **TargetArn** *(string) --* 

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

            
      
        

        - **Environment** *(dict) --* 

          The parent object that contains your environment's configuration settings.

          
          

          - **Variables** *(dict) --* 

            The key-value pairs returned that represent your environment's configuration settings or error information.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **Error** *(dict) --* 

            The parent object that contains error information associated with your configuration settings.

            
            

            - **ErrorCode** *(string) --* 

              The error code returned by the environment error object.

              
            

            - **Message** *(string) --* 

              The message returned by the environment error object.

              
        
      
        

        - **KMSKeyArn** *(string) --* 

          The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

          
        

        - **TracingConfig** *(dict) --* 

          The parent object that contains your function's tracing settings.

          
          

          - **Mode** *(string) --* 

            The tracing mode associated with your Lambda function.

            
      
        

        - **MasterArn** *(string) --* 

          Returns the ARN (Amazon Resource Name) of the master function.

          
    

    **Examples** 

    This operation updates a Lambda function's code
    ::

      response = client.update_function_code(
          FunctionName='myFunction',
          Publish=True,
          S3Bucket='myBucket',
          S3Key='myKey',
          S3ObjectVersion='1',
          ZipFile='fileb://file-path/file.zip',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CodeSha256': 'LQT+0DHxxxxcfwLyQjzoEFKZtdqQjHXanlSdfXBlEW0VA=',
          'CodeSize': 123,
          'Description': '',
          'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction',
          'FunctionName': 'myFunction',
          'Handler': 'index.handler',
          'LastModified': '2016-11-21T19:49:20.006+0000',
          'MemorySize': 128,
          'Role': 'arn:aws:iam::123456789012:role/lambda_basic_execution',
          'Runtime': 'python2.7',
          'Timeout': 123,
          'Version': '1',
          'VpcConfig': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_function_configuration(**kwargs)

    

    Updates the configuration parameters for the specified Lambda function by using the values provided in the request. You provide only the parameters you want to change. This operation must only be used on an existing Lambda function and cannot be used to update the function's code.

     

    If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 

     

    This operation requires permission for the ``lambda:UpdateFunctionConfiguration`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateFunctionConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.update_function_configuration(
          FunctionName='string',
          Role='string',
          Handler='string',
          Description='string',
          Timeout=123,
          MemorySize=123,
          VpcConfig={
              'SubnetIds': [
                  'string',
              ],
              'SecurityGroupIds': [
                  'string',
              ]
          },
          Environment={
              'Variables': {
                  'string': 'string'
              }
          },
          Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
          DeadLetterConfig={
              'TargetArn': 'string'
          },
          KMSKeyArn='string',
          TracingConfig={
              'Mode': 'Active'|'PassThrough'
          }
      )
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The name of the Lambda function.

       

      You can specify a function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). AWS Lambda also allows you to specify a partial ARN (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 character in length. 

      

    
    :type Role: string
    :param Role: 

      The Amazon Resource Name (ARN) of the IAM role that Lambda will assume when it executes your function.

      

    
    :type Handler: string
    :param Handler: 

      The function that Lambda calls to begin executing your function. For Node.js, it is the ``module-name.export`` value in your function. 

      

    
    :type Description: string
    :param Description: 

      A short user-defined function description. AWS Lambda does not use this value. Assign a meaningful description as you see fit.

      

    
    :type Timeout: integer
    :param Timeout: 

      The function execution time at which AWS Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

      

    
    :type MemorySize: integer
    :param MemorySize: 

      The amount of memory, in MB, your Lambda function is given. AWS Lambda uses this memory size to infer the amount of CPU allocated to your function. Your function use-case determines your CPU and memory requirements. For example, a database operation might need less memory compared to an image processing function. The default value is 128 MB. The value must be a multiple of 64 MB.

      

    
    :type VpcConfig: dict
    :param VpcConfig: 

      If your Lambda function accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.

      

    
      - **SubnetIds** *(list) --* 

        A list of one or more subnet IDs in your VPC.

        

      
        - *(string) --* 

        
    
      - **SecurityGroupIds** *(list) --* 

        A list of one or more security groups IDs in your VPC.

        

      
        - *(string) --* 

        
    
    
    :type Environment: dict
    :param Environment: 

      The parent object that contains your environment's configuration settings.

      

    
      - **Variables** *(dict) --* 

        The key-value pairs that represent your environment's configuration settings.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    :type Runtime: string
    :param Runtime: 

      The runtime environment for the Lambda function.

       

      To use the Python runtime v3.6, set the value to "python3.6". To use the Python runtime v2.7, set the value to "python2.7". To use the Node.js runtime v6.10, set the value to "nodejs6.10". To use the Node.js runtime v4.3, set the value to "nodejs4.3". To use the Python runtime v3.6, set the value to "python3.6".

       

      .. note::

         

        Node v0.10.42 is currently marked as deprecated. You must migrate existing functions to the newer Node.js runtime versions available on AWS Lambda (nodejs4.3 or nodejs6.10) as soon as possible. Failure to do so will result in an invalid parameter error being returned. Note that you will have to follow this procedure for each region that contains functions written in the Node v0.10.42 runtime.

         

      

    
    :type DeadLetterConfig: dict
    :param DeadLetterConfig: 

      The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

      

    
      - **TargetArn** *(string) --* 

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

        

      
    
    :type KMSKeyArn: string
    :param KMSKeyArn: 

      The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If you elect to use the AWS Lambda default service key, pass in an empty string ("") for this parameter.

      

    
    :type TracingConfig: dict
    :param TracingConfig: 

      The parent object that contains your function's tracing settings.

      

    
      - **Mode** *(string) --* 

        Can be either PassThrough or Active. If PassThrough, Lambda will only trace the request from an upstream service if it contains a tracing header with "sampled=1". If Active, Lambda will respect any tracing header it receives from an upstream service. If no tracing header is received, Lambda will call X-Ray for a tracing decision.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that describes function metadata.

        
        

        - **FunctionName** *(string) --* 

          The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

          
        

        - **FunctionArn** *(string) --* 

          The Amazon Resource Name (ARN) assigned to the function.

          
        

        - **Runtime** *(string) --* 

          The runtime environment for the Lambda function.

          
        

        - **Role** *(string) --* 

          The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

          
        

        - **Handler** *(string) --* 

          The function Lambda calls to begin executing your function.

          
        

        - **CodeSize** *(integer) --* 

          The size, in bytes, of the function .zip file you uploaded.

          
        

        - **Description** *(string) --* 

          The user-provided description.

          
        

        - **Timeout** *(integer) --* 

          The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

          
        

        - **MemorySize** *(integer) --* 

          The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

          
        

        - **LastModified** *(string) --* 

          The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

          
        

        - **CodeSha256** *(string) --* 

          It is the SHA256 hash of your function deployment package.

          
        

        - **Version** *(string) --* 

          The version of the Lambda function.

          
        

        - **VpcConfig** *(dict) --* 

          VPC configuration associated with your Lambda function.

          
          

          - **SubnetIds** *(list) --* 

            A list of subnet IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **SecurityGroupIds** *(list) --* 

            A list of security group IDs associated with the Lambda function.

            
            

            - *(string) --* 
        
          

          - **VpcId** *(string) --* 

            The VPC ID associated with you Lambda function.

            
      
        

        - **DeadLetterConfig** *(dict) --* 

          The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

          
          

          - **TargetArn** *(string) --* 

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

            
      
        

        - **Environment** *(dict) --* 

          The parent object that contains your environment's configuration settings.

          
          

          - **Variables** *(dict) --* 

            The key-value pairs returned that represent your environment's configuration settings or error information.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **Error** *(dict) --* 

            The parent object that contains error information associated with your configuration settings.

            
            

            - **ErrorCode** *(string) --* 

              The error code returned by the environment error object.

              
            

            - **Message** *(string) --* 

              The message returned by the environment error object.

              
        
      
        

        - **KMSKeyArn** *(string) --* 

          The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

          
        

        - **TracingConfig** *(dict) --* 

          The parent object that contains your function's tracing settings.

          
          

          - **Mode** *(string) --* 

            The tracing mode associated with your Lambda function.

            
      
        

        - **MasterArn** *(string) --* 

          Returns the ARN (Amazon Resource Name) of the master function.

          
    

    **Examples** 

    This operation updates a Lambda function's configuration
    ::

      response = client.update_function_configuration(
          Description='',
          FunctionName='myFunction',
          Handler='index.handler',
          MemorySize=128,
          Role='arn:aws:iam::123456789012:role/lambda_basic_execution',
          Runtime='python2.7',
          Timeout=123,
          VpcConfig={
          },
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CodeSha256': 'LQT+0DHxxxxcfwLyQjzoEFKZtdqQjHXanlSdfXBlEW0VA=',
          'CodeSize': 123,
          'Description': '',
          'FunctionArn': 'arn:aws:lambda:us-west-2:123456789012:function:myFunction',
          'FunctionName': 'myFunction',
          'Handler': 'index.handler',
          'LastModified': '2016-11-21T19:49:20.006+0000',
          'MemorySize': 128,
          'Role': 'arn:aws:iam::123456789012:role/lambda_basic_execution',
          'Runtime': 'python2.7',
          'Timeout': 123,
          'Version': '1',
          'VpcConfig': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:

* :py:class:`Lambda.Paginator.ListEventSourceMappings`


* :py:class:`Lambda.Paginator.ListFunctions`



.. py:class:: Lambda.Paginator.ListEventSourceMappings

  ::

    
    paginator = client.get_paginator('list_event_source_mappings')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lambda.Client.list_event_source_mappings`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListEventSourceMappings>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          EventSourceArn='string',
          FunctionName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type EventSourceArn: string
    :param EventSourceArn: 

      The Amazon Resource Name (ARN) of the Amazon Kinesis stream. (This parameter is optional.)

      

    
    :type FunctionName: string
    :param FunctionName: 

      The name of the Lambda function.

       

      You can specify the function name (for example, ``Thumbnail`` ) or you can specify Amazon Resource Name (ARN) of the function (for example, ``arn:aws:lambda:us-west-2:account-id:function:ThumbNail`` ). If you are using versioning, you can also provide a qualified function ARN (ARN that is qualified with function version or alias name as suffix). AWS Lambda also allows you to specify only the function name with the account ID qualifier (for example, ``account-id:Thumbnail`` ). Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length. 

      

    
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
            'EventSourceMappings': [
                {
                    'UUID': 'string',
                    'BatchSize': 123,
                    'EventSourceArn': 'string',
                    'FunctionArn': 'string',
                    'LastModified': datetime(2015, 1, 1),
                    'LastProcessingResult': 'string',
                    'State': 'string',
                    'StateTransitionReason': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains a list of event sources (see  EventSourceMappingConfiguration )

        
        

        - **EventSourceMappings** *(list) --* 

          An array of ``EventSourceMappingConfiguration`` objects.

          
          

          - *(dict) --* 

            Describes mapping between an Amazon Kinesis stream and a Lambda function.

            
            

            - **UUID** *(string) --* 

              The AWS Lambda assigned opaque identifier for the mapping.

              
            

            - **BatchSize** *(integer) --* 

              The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.

              
            

            - **EventSourceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon Kinesis stream that is the source of events.

              
            

            - **FunctionArn** *(string) --* 

              The Lambda function to invoke when AWS Lambda detects an event on the stream.

              
            

            - **LastModified** *(datetime) --* 

              The UTC time string indicating the last time the event mapping was updated.

              
            

            - **LastProcessingResult** *(string) --* 

              The result of the last AWS Lambda invocation of your Lambda function.

              
            

            - **State** *(string) --* 

              The state of the event source mapping. It can be ``Creating`` , ``Enabled`` , ``Disabled`` , ``Enabling`` , ``Disabling`` , ``Updating`` , or ``Deleting`` .

              
            

            - **StateTransitionReason** *(string) --* 

              The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lambda.Paginator.ListFunctions

  ::

    
    paginator = client.get_paginator('list_functions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lambda.Client.list_functions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListFunctions>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          MasterRegion='string',
          FunctionVersion='ALL',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type MasterRegion: string
    :param MasterRegion: 

      Optional string. If not specified, will return only regular function versions (i.e., non-replicated versions).

       

      Valid values are:

       

      The region from which the functions are replicated. For example, if you specify ``us-east-1`` , only functions replicated from that region will be returned.

       

       ``ALL`` : Will return all functions from any region. If specified, you also must specify a valid FunctionVersion parameter.

      

    
    :type FunctionVersion: string
    :param FunctionVersion: 

      Optional string. If not specified, only the unqualified functions ARNs (Amazon Resource Names) will be returned.

       

      Valid value:

       

       ``ALL`` : Will return all versions, including ``$LATEST`` which will have fully qualified ARNs (Amazon Resource Names).

      

    
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
            'Functions': [
                {
                    'FunctionName': 'string',
                    'FunctionArn': 'string',
                    'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
                    'Role': 'string',
                    'Handler': 'string',
                    'CodeSize': 123,
                    'Description': 'string',
                    'Timeout': 123,
                    'MemorySize': 123,
                    'LastModified': 'string',
                    'CodeSha256': 'string',
                    'Version': 'string',
                    'VpcConfig': {
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'VpcId': 'string'
                    },
                    'DeadLetterConfig': {
                        'TargetArn': 'string'
                    },
                    'Environment': {
                        'Variables': {
                            'string': 'string'
                        },
                        'Error': {
                            'ErrorCode': 'string',
                            'Message': 'string'
                        }
                    },
                    'KMSKeyArn': 'string',
                    'TracingConfig': {
                        'Mode': 'Active'|'PassThrough'
                    },
                    'MasterArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains a list of AWS Lambda function configurations (see  FunctionConfiguration .

        
        

        - **Functions** *(list) --* 

          A list of Lambda functions.

          
          

          - *(dict) --* 

            A complex type that describes function metadata.

            
            

            - **FunctionName** *(string) --* 

              The name of the function. Note that the length constraint applies only to the ARN. If you specify only the function name, it is limited to 64 characters in length.

              
            

            - **FunctionArn** *(string) --* 

              The Amazon Resource Name (ARN) assigned to the function.

              
            

            - **Runtime** *(string) --* 

              The runtime environment for the Lambda function.

              
            

            - **Role** *(string) --* 

              The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources.

              
            

            - **Handler** *(string) --* 

              The function Lambda calls to begin executing your function.

              
            

            - **CodeSize** *(integer) --* 

              The size, in bytes, of the function .zip file you uploaded.

              
            

            - **Description** *(string) --* 

              The user-provided description.

              
            

            - **Timeout** *(integer) --* 

              The function execution time at which Lambda should terminate the function. Because the execution time has cost implications, we recommend you set this value based on your expected execution time. The default is 3 seconds.

              
            

            - **MemorySize** *(integer) --* 

              The memory size, in MB, you configured for the function. Must be a multiple of 64 MB.

              
            

            - **LastModified** *(string) --* 

              The time stamp of the last time you updated the function. The time stamp is conveyed as a string complying with ISO-8601 in this way YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see `Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`__ .

              
            

            - **CodeSha256** *(string) --* 

              It is the SHA256 hash of your function deployment package.

              
            

            - **Version** *(string) --* 

              The version of the Lambda function.

              
            

            - **VpcConfig** *(dict) --* 

              VPC configuration associated with your Lambda function.

              
              

              - **SubnetIds** *(list) --* 

                A list of subnet IDs associated with the Lambda function.

                
                

                - *(string) --* 
            
              

              - **SecurityGroupIds** *(list) --* 

                A list of security group IDs associated with the Lambda function.

                
                

                - *(string) --* 
            
              

              - **VpcId** *(string) --* 

                The VPC ID associated with you Lambda function.

                
          
            

            - **DeadLetterConfig** *(dict) --* 

              The parent object that contains the target ARN (Amazon Resource Name) of an Amazon SQS queue or Amazon SNS topic.

              
              

              - **TargetArn** *(string) --* 

                The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you specify as your Dead Letter Queue (DLQ).

                
          
            

            - **Environment** *(dict) --* 

              The parent object that contains your environment's configuration settings.

              
              

              - **Variables** *(dict) --* 

                The key-value pairs returned that represent your environment's configuration settings or error information.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Error** *(dict) --* 

                The parent object that contains error information associated with your configuration settings.

                
                

                - **ErrorCode** *(string) --* 

                  The error code returned by the environment error object.

                  
                

                - **Message** *(string) --* 

                  The message returned by the environment error object.

                  
            
          
            

            - **KMSKeyArn** *(string) --* 

              The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If empty, it means you are using the AWS Lambda default service key.

              
            

            - **TracingConfig** *(dict) --* 

              The parent object that contains your function's tracing settings.

              
              

              - **Mode** *(string) --* 

                The tracing mode associated with your Lambda function.

                
          
            

            - **MasterArn** *(string) --* 

              Returns the ARN (Amazon Resource Name) of the master function.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    