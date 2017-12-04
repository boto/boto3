

****************
CloudWatchEvents
****************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CloudWatchEvents.Client

  A low-level client representing Amazon CloudWatch Events::

    
    import boto3
    
    client = boto3.client('events')

  
  These are the available methods:
  
  *   :py:meth:`~CloudWatchEvents.Client.can_paginate`

  
  *   :py:meth:`~CloudWatchEvents.Client.delete_rule`

  
  *   :py:meth:`~CloudWatchEvents.Client.describe_event_bus`

  
  *   :py:meth:`~CloudWatchEvents.Client.describe_rule`

  
  *   :py:meth:`~CloudWatchEvents.Client.disable_rule`

  
  *   :py:meth:`~CloudWatchEvents.Client.enable_rule`

  
  *   :py:meth:`~CloudWatchEvents.Client.generate_presigned_url`

  
  *   :py:meth:`~CloudWatchEvents.Client.get_paginator`

  
  *   :py:meth:`~CloudWatchEvents.Client.get_waiter`

  
  *   :py:meth:`~CloudWatchEvents.Client.list_rule_names_by_target`

  
  *   :py:meth:`~CloudWatchEvents.Client.list_rules`

  
  *   :py:meth:`~CloudWatchEvents.Client.list_targets_by_rule`

  
  *   :py:meth:`~CloudWatchEvents.Client.put_events`

  
  *   :py:meth:`~CloudWatchEvents.Client.put_permission`

  
  *   :py:meth:`~CloudWatchEvents.Client.put_rule`

  
  *   :py:meth:`~CloudWatchEvents.Client.put_targets`

  
  *   :py:meth:`~CloudWatchEvents.Client.remove_permission`

  
  *   :py:meth:`~CloudWatchEvents.Client.remove_targets`

  
  *   :py:meth:`~CloudWatchEvents.Client.test_event_pattern`

  

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


  .. py:method:: delete_rule(**kwargs)

    

    Deletes the specified rule.

     

    You must remove all targets from a rule using  RemoveTargets before you can delete the rule.

     

    When you delete a rule, incoming events might continue to match to the deleted rule. Please allow a short period of time for changes to take effect.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/DeleteRule>`_    


    **Request Syntax** 
    ::

      response = client.delete_rule(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the rule.

      

    
    
    :returns: None

  .. py:method:: describe_event_bus()

    

    Displays the external AWS accounts that are permitted to write events to your account using your account's event bus, and the associated policy. To enable your account to receive events from other accounts, use  PutPermission .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/DescribeEventBus>`_    


    **Request Syntax** 
    ::

      response = client.describe_event_bus()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string',
            'Arn': 'string',
            'Policy': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          The name of the event bus. Currently, this is always ``default`` .

          
        

        - **Arn** *(string) --* 

          The Amazon Resource Name (ARN) of the account permitted to write events to the current account.

          
        

        - **Policy** *(string) --* 

          The policy that enables the external account to send events to your account.

          
    

  .. py:method:: describe_rule(**kwargs)

    

    Describes the specified rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/DescribeRule>`_    


    **Request Syntax** 
    ::

      response = client.describe_rule(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the rule.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string',
            'Arn': 'string',
            'EventPattern': 'string',
            'ScheduleExpression': 'string',
            'State': 'ENABLED'|'DISABLED',
            'Description': 'string',
            'RoleArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          The name of the rule.

          
        

        - **Arn** *(string) --* 

          The Amazon Resource Name (ARN) of the rule.

          
        

        - **EventPattern** *(string) --* 

          The event pattern. For more information, see `Events and Event Patterns <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html>`__ in the *Amazon CloudWatch Events User Guide* .

          
        

        - **ScheduleExpression** *(string) --* 

          The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)".

          
        

        - **State** *(string) --* 

          Specifies whether the rule is enabled or disabled.

          
        

        - **Description** *(string) --* 

          The description of the rule.

          
        

        - **RoleArn** *(string) --* 

          The Amazon Resource Name (ARN) of the IAM role associated with the rule.

          
    

  .. py:method:: disable_rule(**kwargs)

    

    Disables the specified rule. A disabled rule won't match any events, and won't self-trigger if it has a schedule expression.

     

    When you disable a rule, incoming events might continue to match to the disabled rule. Please allow a short period of time for changes to take effect.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/DisableRule>`_    


    **Request Syntax** 
    ::

      response = client.disable_rule(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the rule.

      

    
    
    :returns: None

  .. py:method:: enable_rule(**kwargs)

    

    Enables the specified rule. If the rule does not exist, the operation fails.

     

    When you enable a rule, incoming events might not immediately start matching to a newly enabled rule. Please allow a short period of time for changes to take effect.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/EnableRule>`_    


    **Request Syntax** 
    ::

      response = client.enable_rule(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the rule.

      

    
    
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

        


  .. py:method:: list_rule_names_by_target(**kwargs)

    

    Lists the rules for the specified target. You can see which of the rules in Amazon CloudWatch Events can invoke a specific target in your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/ListRuleNamesByTarget>`_    


    **Request Syntax** 
    ::

      response = client.list_rule_names_by_target(
          TargetArn='string',
          NextToken='string',
          Limit=123
      )
    :type TargetArn: string
    :param TargetArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the target resource.

      

    
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to retrieve the next set of results.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of results to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RuleNames': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RuleNames** *(list) --* 

          The names of the rules that can invoke the given target.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          Indicates whether there are additional results to retrieve. If there are no more results, the value is null.

          
    

  .. py:method:: list_rules(**kwargs)

    

    Lists your Amazon CloudWatch Events rules. You can either list all the rules or you can provide a prefix to match to the rule names.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/ListRules>`_    


    **Request Syntax** 
    ::

      response = client.list_rules(
          NamePrefix='string',
          NextToken='string',
          Limit=123
      )
    :type NamePrefix: string
    :param NamePrefix: 

      The prefix matching the rule name.

      

    
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to retrieve the next set of results.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of results to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rules': [
                {
                    'Name': 'string',
                    'Arn': 'string',
                    'EventPattern': 'string',
                    'State': 'ENABLED'|'DISABLED',
                    'Description': 'string',
                    'ScheduleExpression': 'string',
                    'RoleArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rules** *(list) --* 

          The rules that match the specified criteria.

          
          

          - *(dict) --* 

            Contains information about a rule in Amazon CloudWatch Events.

            
            

            - **Name** *(string) --* 

              The name of the rule.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the rule.

              
            

            - **EventPattern** *(string) --* 

              The event pattern of the rule. For more information, see `Events and Event Patterns <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html>`__ in the *Amazon CloudWatch Events User Guide* .

              
            

            - **State** *(string) --* 

              The state of the rule.

              
            

            - **Description** *(string) --* 

              The description of the rule.

              
            

            - **ScheduleExpression** *(string) --* 

              The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)".

              
            

            - **RoleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the role that is used for target invocation.

              
        
      
        

        - **NextToken** *(string) --* 

          Indicates whether there are additional results to retrieve. If there are no more results, the value is null.

          
    

  .. py:method:: list_targets_by_rule(**kwargs)

    

    Lists the targets assigned to the specified rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/ListTargetsByRule>`_    


    **Request Syntax** 
    ::

      response = client.list_targets_by_rule(
          Rule='string',
          NextToken='string',
          Limit=123
      )
    :type Rule: string
    :param Rule: **[REQUIRED]** 

      The name of the rule.

      

    
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to retrieve the next set of results.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of results to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Targets': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'RoleArn': 'string',
                    'Input': 'string',
                    'InputPath': 'string',
                    'InputTransformer': {
                        'InputPathsMap': {
                            'string': 'string'
                        },
                        'InputTemplate': 'string'
                    },
                    'KinesisParameters': {
                        'PartitionKeyPath': 'string'
                    },
                    'RunCommandParameters': {
                        'RunCommandTargets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'EcsParameters': {
                        'TaskDefinitionArn': 'string',
                        'TaskCount': 123
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Targets** *(list) --* 

          The targets assigned to the rule.

          
          

          - *(dict) --* 

            Targets are the resources to be invoked when a rule is triggered. Target types include EC2 instances, AWS Lambda functions, Amazon Kinesis streams, Amazon ECS tasks, AWS Step Functions state machines, Run Command, and built-in targets.

            
            

            - **Id** *(string) --* 

              The ID of the target.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the target.

              
            

            - **RoleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.

              
            

            - **Input** *(string) --* 

              Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. You must use JSON dot notation, not bracket notation. For more information, see `The JavaScript Object Notation (JSON) Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .

              
            

            - **InputPath** *(string) --* 

              The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .

              
            

            - **InputTransformer** *(dict) --* 

              Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.

              
              

              - **InputPathsMap** *(dict) --* 

                Map of JSON paths to be extracted from the event. These are key-value pairs, where each value is a JSON path. You must use JSON dot notation, not bracket notation.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **InputTemplate** *(string) --* 

                Input template where you can use the values of the keys from ``InputPathsMap`` to customize the data sent to the target.

                
          
            

            - **KinesisParameters** *(dict) --* 

              The custom parameter you can use to control shard assignment, when the target is an Amazon Kinesis stream. If you do not include this parameter, the default is to use the ``eventId`` as the partition key.

              
              

              - **PartitionKeyPath** *(string) --* 

                The JSON path to be extracted from the event and used as the partition key. For more information, see `Amazon Kinesis Streams Key Concepts <http://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in the *Amazon Kinesis Streams Developer Guide* .

                
          
            

            - **RunCommandParameters** *(dict) --* 

              Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

              
              

              - **RunCommandTargets** *(list) --* 

                Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.

                
                

                - *(dict) --* 

                  Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this key may specify multiple values.

                  
                  

                  - **Key** *(string) --* 

                    Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

                    
                  

                  - **Values** *(list) --* 

                    If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key`` is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

                    
                    

                    - *(string) --* 
                
              
            
          
            

            - **EcsParameters** *(dict) --* 

              Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon EC2 Container Service Developer Guide* .

              
              

              - **TaskDefinitionArn** *(string) --* 

                The ARN of the task definition to use if the event target is an Amazon ECS cluster. 

                
              

              - **TaskCount** *(integer) --* 

                The number of tasks to create based on the ``TaskDefinition`` . The default is one.

                
          
        
      
        

        - **NextToken** *(string) --* 

          Indicates whether there are additional results to retrieve. If there are no more results, the value is null.

          
    

  .. py:method:: put_events(**kwargs)

    

    Sends custom events to Amazon CloudWatch Events so that they can be matched to rules.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/PutEvents>`_    


    **Request Syntax** 
    ::

      response = client.put_events(
          Entries=[
              {
                  'Time': datetime(2015, 1, 1),
                  'Source': 'string',
                  'Resources': [
                      'string',
                  ],
                  'DetailType': 'string',
                  'Detail': 'string'
              },
          ]
      )
    :type Entries: list
    :param Entries: **[REQUIRED]** 

      The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.

      

    
      - *(dict) --* 

        Represents an event to be submitted.

        

      
        - **Time** *(datetime) --* 

          The timestamp of the event, per `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339.txt>`__ . If no timestamp is provided, the timestamp of the  PutEvents call is used.

          

        
        - **Source** *(string) --* 

          The source of the event.

          

        
        - **Resources** *(list) --* 

          AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.

          

        
          - *(string) --* 

          
      
        - **DetailType** *(string) --* 

          Free-form string used to decide what fields to expect in the event detail.

          

        
        - **Detail** *(string) --* 

          In the JSON sense, an object containing fields, which may also contain nested subobjects. No constraints are imposed on its contents.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedEntryCount': 123,
            'Entries': [
                {
                    'EventId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FailedEntryCount** *(integer) --* 

          The number of failed entries.

          
        

        - **Entries** *(list) --* 

          The successfully and unsuccessfully ingested events results. If the ingestion was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.

          
          

          - *(dict) --* 

            Represents an event that failed to be submitted.

            
            

            - **EventId** *(string) --* 

              The ID of the event.

              
            

            - **ErrorCode** *(string) --* 

              The error code that indicates why the event submission failed.

              
            

            - **ErrorMessage** *(string) --* 

              The error message that explains why the event submission failed.

              
        
      
    

  .. py:method:: put_permission(**kwargs)

    

    Running ``PutPermission`` permits the specified AWS account to put events to your account's default *event bus* . CloudWatch Events rules in your account are triggered by these events arriving to your default event bus. 

     

    For another account to send events to your account, that external account must have a CloudWatch Events rule with your account's default event bus as a target.

     

    To enable multiple AWS accounts to put events to your default event bus, run ``PutPermission`` once for each of these accounts.

     

    The permission policy on the default event bus cannot exceed 10KB in size.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/PutPermission>`_    


    **Request Syntax** 
    ::

      response = client.put_permission(
          Action='string',
          Principal='string',
          StatementId='string'
      )
    :type Action: string
    :param Action: **[REQUIRED]** 

      The action that you are enabling the other account to perform. Currently, this must be ``events:PutEvents`` .

      

    
    :type Principal: string
    :param Principal: **[REQUIRED]** 

      The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify "*" to permit any account to put events to your default event bus.

       

      If you specify "*", avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an ``account`` field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.

      

    
    :type StatementId: string
    :param StatementId: **[REQUIRED]** 

      An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this ``StatementId`` when you run  RemovePermission .

      

    
    
    :returns: None

  .. py:method:: put_rule(**kwargs)

    

    Creates or updates the specified rule. Rules are enabled by default, or based on value of the state. You can disable a rule using  DisableRule .

     

    When you create or update a rule, incoming events might not immediately start matching to new or updated rules. Please allow a short period of time for changes to take effect.

     

    A rule must contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered when a matching event is observed. Rules with ScheduleExpressions self-trigger based on the given schedule. A rule can have both an EventPattern and a ScheduleExpression, in which case the rule triggers on matching events as well as on a schedule.

     

    Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, CloudWatch Events uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/PutRule>`_    


    **Request Syntax** 
    ::

      response = client.put_rule(
          Name='string',
          ScheduleExpression='string',
          EventPattern='string',
          State='ENABLED'|'DISABLED',
          Description='string',
          RoleArn='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the rule that you are creating or updating.

      

    
    :type ScheduleExpression: string
    :param ScheduleExpression: 

      The scheduling expression. For example, "cron(0 20 * * ? *)" or "rate(5 minutes)".

      

    
    :type EventPattern: string
    :param EventPattern: 

      The event pattern. For more information, see `Events and Event Patterns <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html>`__ in the *Amazon CloudWatch Events User Guide* .

      

    
    :type State: string
    :param State: 

      Indicates whether the rule is enabled or disabled.

      

    
    :type Description: string
    :param Description: 

      A description of the rule.

      

    
    :type RoleArn: string
    :param RoleArn: 

      The Amazon Resource Name (ARN) of the IAM role associated with the rule.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RuleArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RuleArn** *(string) --* 

          The Amazon Resource Name (ARN) of the rule.

          
    

  .. py:method:: put_targets(**kwargs)

    

    Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.

     

    Targets are the resources that are invoked when a rule is triggered.

     

    You can configure the following as targets for CloudWatch Events:

     

     
    * EC2 instances 
     
    * AWS Lambda functions 
     
    * Streams in Amazon Kinesis Streams 
     
    * Delivery streams in Amazon Kinesis Firehose 
     
    * Amazon ECS tasks 
     
    * AWS Step Functions state machines 
     
    * Pipelines in Amazon Code Pipeline 
     
    * Amazon Inspector assessment templates 
     
    * Amazon SNS topics 
     
    * Amazon SQS queues 
     
    * The default event bus of another AWS account 
     

     

    Note that creating rules with built-in targets is supported only in the AWS Management Console.

     

    For some target types, ``PutTargets`` provides target-specific parameters. If the target is an Amazon Kinesis stream, you can optionally specify which shard the event goes to by using the ``KinesisParameters`` argument. To invoke a command on multiple EC2 instances with one rule, you can use the ``RunCommandParameters`` field.

     

    To be able to make API calls against the resources that you own, Amazon CloudWatch Events needs the appropriate permissions. For AWS Lambda and Amazon SNS resources, CloudWatch Events relies on resource-based policies. For EC2 instances, Amazon Kinesis streams, and AWS Step Functions state machines, CloudWatch Events relies on IAM roles that you specify in the ``RoleARN`` argument in ``PutTargets`` . For more information, see `Authentication and Access Control <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/auth-and-access-control-cwe.html>`__ in the *Amazon CloudWatch Events User Guide* .

     

    If another AWS account is in the same region and has granted you permission (using ``PutPermission`` ), you can send events to that account by setting that account's event bus as a target of the rules in your account. To send the matched events to the other account, specify that account's event bus as the ``Arn`` when you run ``PutTargets`` . If your account sends events to another account, your account is charged for each sent event. Each event sent to antoher account is charged as a custom event. The account receiving the event is not charged. For more information on pricing, see `Amazon CloudWatch Pricing <https://aws.amazon.com/cloudwatch/pricing/>`__ .

     

    For more information about enabling cross-account events, see  PutPermission .

     

     **Input** , **InputPath** and **InputTransformer** are mutually exclusive and optional parameters of a target. When a rule is triggered due to a matched event:

     

     
    * If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON form (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target). 
     
    * If **Input** is specified in the form of valid JSON, then the matched event is overridden with this constant. 
     
    * If **InputPath** is specified in the form of JSONPath (for example, ``$.detail`` ), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed). 
     
    * If **InputTransformer** is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target. 
     

     

    When you specify ``Input`` , ``InputPath`` , or ``InputTransformer`` , you must use JSON dot notation, not bracket notation.

     

    When you add targets to a rule and the associated rule triggers soon after, new or updated targets might not be immediately invoked. Please allow a short period of time for changes to take effect.

     

    This action can partially fail if too many requests are made at the same time. If that happens, ``FailedEntryCount`` is non-zero in the response and each entry in ``FailedEntries`` provides the ID of the failed target and the error code.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/PutTargets>`_    


    **Request Syntax** 
    ::

      response = client.put_targets(
          Rule='string',
          Targets=[
              {
                  'Id': 'string',
                  'Arn': 'string',
                  'RoleArn': 'string',
                  'Input': 'string',
                  'InputPath': 'string',
                  'InputTransformer': {
                      'InputPathsMap': {
                          'string': 'string'
                      },
                      'InputTemplate': 'string'
                  },
                  'KinesisParameters': {
                      'PartitionKeyPath': 'string'
                  },
                  'RunCommandParameters': {
                      'RunCommandTargets': [
                          {
                              'Key': 'string',
                              'Values': [
                                  'string',
                              ]
                          },
                      ]
                  },
                  'EcsParameters': {
                      'TaskDefinitionArn': 'string',
                      'TaskCount': 123
                  }
              },
          ]
      )
    :type Rule: string
    :param Rule: **[REQUIRED]** 

      The name of the rule.

      

    
    :type Targets: list
    :param Targets: **[REQUIRED]** 

      The targets to update or add to the rule.

      

    
      - *(dict) --* 

        Targets are the resources to be invoked when a rule is triggered. Target types include EC2 instances, AWS Lambda functions, Amazon Kinesis streams, Amazon ECS tasks, AWS Step Functions state machines, Run Command, and built-in targets.

        

      
        - **Id** *(string) --* **[REQUIRED]** 

          The ID of the target.

          

        
        - **Arn** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the target.

          

        
        - **RoleArn** *(string) --* 

          The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.

          

        
        - **Input** *(string) --* 

          Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. You must use JSON dot notation, not bracket notation. For more information, see `The JavaScript Object Notation (JSON) Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .

          

        
        - **InputPath** *(string) --* 

          The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .

          

        
        - **InputTransformer** *(dict) --* 

          Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.

          

        
          - **InputPathsMap** *(dict) --* 

            Map of JSON paths to be extracted from the event. These are key-value pairs, where each value is a JSON path. You must use JSON dot notation, not bracket notation.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
          - **InputTemplate** *(string) --* **[REQUIRED]** 

            Input template where you can use the values of the keys from ``InputPathsMap`` to customize the data sent to the target.

            

          
        
        - **KinesisParameters** *(dict) --* 

          The custom parameter you can use to control shard assignment, when the target is an Amazon Kinesis stream. If you do not include this parameter, the default is to use the ``eventId`` as the partition key.

          

        
          - **PartitionKeyPath** *(string) --* **[REQUIRED]** 

            The JSON path to be extracted from the event and used as the partition key. For more information, see `Amazon Kinesis Streams Key Concepts <http://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in the *Amazon Kinesis Streams Developer Guide* .

            

          
        
        - **RunCommandParameters** *(dict) --* 

          Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

          

        
          - **RunCommandTargets** *(list) --* **[REQUIRED]** 

            Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.

            

          
            - *(dict) --* 

              Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this key may specify multiple values.

              

            
              - **Key** *(string) --* **[REQUIRED]** 

                Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

                

              
              - **Values** *(list) --* **[REQUIRED]** 

                If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key`` is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

                

              
                - *(string) --* 

                
            
            
        
        
        - **EcsParameters** *(dict) --* 

          Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon EC2 Container Service Developer Guide* .

          

        
          - **TaskDefinitionArn** *(string) --* **[REQUIRED]** 

            The ARN of the task definition to use if the event target is an Amazon ECS cluster. 

            

          
          - **TaskCount** *(integer) --* 

            The number of tasks to create based on the ``TaskDefinition`` . The default is one.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedEntryCount': 123,
            'FailedEntries': [
                {
                    'TargetId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FailedEntryCount** *(integer) --* 

          The number of failed entries.

          
        

        - **FailedEntries** *(list) --* 

          The failed target entries.

          
          

          - *(dict) --* 

            Represents a target that failed to be added to a rule.

            
            

            - **TargetId** *(string) --* 

              The ID of the target.

              
            

            - **ErrorCode** *(string) --* 

              The error code that indicates why the target addition failed. If the value is ``ConcurrentModificationException`` , too many requests were made at the same time.

              
            

            - **ErrorMessage** *(string) --* 

              The error message that explains why the target addition failed.

              
        
      
    

  .. py:method:: remove_permission(**kwargs)

    

    Revokes the permission of another AWS account to be able to put events to your default event bus. Specify the account to revoke by the ``StatementId`` value that you associated with the account when you granted it permission with ``PutPermission`` . You can find the ``StatementId`` by using  DescribeEventBus .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/RemovePermission>`_    


    **Request Syntax** 
    ::

      response = client.remove_permission(
          StatementId='string'
      )
    :type StatementId: string
    :param StatementId: **[REQUIRED]** 

      The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.

      

    
    
    :returns: None

  .. py:method:: remove_targets(**kwargs)

    

    Removes the specified targets from the specified rule. When the rule is triggered, those targets are no longer be invoked.

     

    When you remove a target, when the associated rule triggers, removed targets might continue to be invoked. Please allow a short period of time for changes to take effect.

     

    This action can partially fail if too many requests are made at the same time. If that happens, ``FailedEntryCount`` is non-zero in the response and each entry in ``FailedEntries`` provides the ID of the failed target and the error code.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/RemoveTargets>`_    


    **Request Syntax** 
    ::

      response = client.remove_targets(
          Rule='string',
          Ids=[
              'string',
          ]
      )
    :type Rule: string
    :param Rule: **[REQUIRED]** 

      The name of the rule.

      

    
    :type Ids: list
    :param Ids: **[REQUIRED]** 

      The IDs of the targets to remove from the rule.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedEntryCount': 123,
            'FailedEntries': [
                {
                    'TargetId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FailedEntryCount** *(integer) --* 

          The number of failed entries.

          
        

        - **FailedEntries** *(list) --* 

          The failed target entries.

          
          

          - *(dict) --* 

            Represents a target that failed to be removed from a rule.

            
            

            - **TargetId** *(string) --* 

              The ID of the target.

              
            

            - **ErrorCode** *(string) --* 

              The error code that indicates why the target removal failed. If the value is ``ConcurrentModificationException`` , too many requests were made at the same time.

              
            

            - **ErrorMessage** *(string) --* 

              The error message that explains why the target removal failed.

              
        
      
    

  .. py:method:: test_event_pattern(**kwargs)

    

    Tests whether the specified event pattern matches the provided event.

     

    Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, CloudWatch Events uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/TestEventPattern>`_    


    **Request Syntax** 
    ::

      response = client.test_event_pattern(
          EventPattern='string',
          Event='string'
      )
    :type EventPattern: string
    :param EventPattern: **[REQUIRED]** 

      The event pattern. For more information, see `Events and Event Patterns <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html>`__ in the *Amazon CloudWatch Events User Guide* .

      

    
    :type Event: string
    :param Event: **[REQUIRED]** 

      The event, in JSON format, to test against the event pattern.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Result': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Result** *(boolean) --* 

          Indicates whether the event matches the event pattern.

          
    

==========
Paginators
==========


The available paginators are:
