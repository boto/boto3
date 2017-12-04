

*************
ConfigService
*************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ConfigService.Client

  A low-level client representing AWS Config (Config Service)::

    
    import boto3
    
    client = boto3.client('config')

  
  These are the available methods:
  
  *   :py:meth:`~ConfigService.Client.can_paginate`

  
  *   :py:meth:`~ConfigService.Client.delete_config_rule`

  
  *   :py:meth:`~ConfigService.Client.delete_configuration_recorder`

  
  *   :py:meth:`~ConfigService.Client.delete_delivery_channel`

  
  *   :py:meth:`~ConfigService.Client.delete_evaluation_results`

  
  *   :py:meth:`~ConfigService.Client.deliver_config_snapshot`

  
  *   :py:meth:`~ConfigService.Client.describe_compliance_by_config_rule`

  
  *   :py:meth:`~ConfigService.Client.describe_compliance_by_resource`

  
  *   :py:meth:`~ConfigService.Client.describe_config_rule_evaluation_status`

  
  *   :py:meth:`~ConfigService.Client.describe_config_rules`

  
  *   :py:meth:`~ConfigService.Client.describe_configuration_recorder_status`

  
  *   :py:meth:`~ConfigService.Client.describe_configuration_recorders`

  
  *   :py:meth:`~ConfigService.Client.describe_delivery_channel_status`

  
  *   :py:meth:`~ConfigService.Client.describe_delivery_channels`

  
  *   :py:meth:`~ConfigService.Client.generate_presigned_url`

  
  *   :py:meth:`~ConfigService.Client.get_compliance_details_by_config_rule`

  
  *   :py:meth:`~ConfigService.Client.get_compliance_details_by_resource`

  
  *   :py:meth:`~ConfigService.Client.get_compliance_summary_by_config_rule`

  
  *   :py:meth:`~ConfigService.Client.get_compliance_summary_by_resource_type`

  
  *   :py:meth:`~ConfigService.Client.get_discovered_resource_counts`

  
  *   :py:meth:`~ConfigService.Client.get_paginator`

  
  *   :py:meth:`~ConfigService.Client.get_resource_config_history`

  
  *   :py:meth:`~ConfigService.Client.get_waiter`

  
  *   :py:meth:`~ConfigService.Client.list_discovered_resources`

  
  *   :py:meth:`~ConfigService.Client.put_config_rule`

  
  *   :py:meth:`~ConfigService.Client.put_configuration_recorder`

  
  *   :py:meth:`~ConfigService.Client.put_delivery_channel`

  
  *   :py:meth:`~ConfigService.Client.put_evaluations`

  
  *   :py:meth:`~ConfigService.Client.start_config_rules_evaluation`

  
  *   :py:meth:`~ConfigService.Client.start_configuration_recorder`

  
  *   :py:meth:`~ConfigService.Client.stop_configuration_recorder`

  

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


  .. py:method:: delete_config_rule(**kwargs)

    

    Deletes the specified AWS Config rule and all of its evaluation results.

     

    AWS Config sets the state of a rule to ``DELETING`` until the deletion is complete. You cannot update a rule while it is in this state. If you make a ``PutConfigRule`` or ``DeleteConfigRule`` request for the rule, you will receive a ``ResourceInUseException`` .

     

    You can check the state of a rule by using the ``DescribeConfigRules`` request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteConfigRule>`_    


    **Request Syntax** 
    ::

      response = client.delete_config_rule(
          ConfigRuleName='string'
      )
    :type ConfigRuleName: string
    :param ConfigRuleName: **[REQUIRED]** 

      The name of the AWS Config rule that you want to delete.

      

    
    
    :returns: None

  .. py:method:: delete_configuration_recorder(**kwargs)

    

    Deletes the configuration recorder.

     

    After the configuration recorder is deleted, AWS Config will not record resource configuration changes until you create a new configuration recorder.

     

    This action does not delete the configuration information that was previously recorded. You will be able to access the previously recorded information by using the ``GetResourceConfigHistory`` action, but you will not be able to access this information in the AWS Config console until you create a new configuration recorder.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteConfigurationRecorder>`_    


    **Request Syntax** 
    ::

      response = client.delete_configuration_recorder(
          ConfigurationRecorderName='string'
      )
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: **[REQUIRED]** 

      The name of the configuration recorder to be deleted. You can retrieve the name of your configuration recorder by using the ``DescribeConfigurationRecorders`` action.

      

    
    
    :returns: None

  .. py:method:: delete_delivery_channel(**kwargs)

    

    Deletes the delivery channel.

     

    Before you can delete the delivery channel, you must stop the configuration recorder by using the  StopConfigurationRecorder action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteDeliveryChannel>`_    


    **Request Syntax** 
    ::

      response = client.delete_delivery_channel(
          DeliveryChannelName='string'
      )
    :type DeliveryChannelName: string
    :param DeliveryChannelName: **[REQUIRED]** 

      The name of the delivery channel to delete.

      

    
    
    :returns: None

  .. py:method:: delete_evaluation_results(**kwargs)

    

    Deletes the evaluation results for the specified Config rule. You can specify one Config rule per request. After you delete the evaluation results, you can call the  StartConfigRulesEvaluation API to start evaluating your AWS resources against the rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteEvaluationResults>`_    


    **Request Syntax** 
    ::

      response = client.delete_evaluation_results(
          ConfigRuleName='string'
      )
    :type ConfigRuleName: string
    :param ConfigRuleName: **[REQUIRED]** 

      The name of the Config rule for which you want to delete the evaluation results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output when you delete the evaluation results for the specified Config rule.

        
    

  .. py:method:: deliver_config_snapshot(**kwargs)

    

    Schedules delivery of a configuration snapshot to the Amazon S3 bucket in the specified delivery channel. After the delivery has started, AWS Config sends following notifications using an Amazon SNS topic that you have specified.

     

     
    * Notification of starting the delivery. 
     
    * Notification of delivery completed, if the delivery was successfully completed. 
     
    * Notification of delivery failure, if the delivery failed to complete. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeliverConfigSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.deliver_config_snapshot(
          deliveryChannelName='string'
      )
    :type deliveryChannelName: string
    :param deliveryChannelName: **[REQUIRED]** 

      The name of the delivery channel through which the snapshot is delivered.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'configSnapshotId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the  DeliverConfigSnapshot action in JSON format.

        
        

        - **configSnapshotId** *(string) --* 

          The ID of the snapshot that is being created.

          
    

  .. py:method:: describe_compliance_by_config_rule(**kwargs)

    

    Indicates whether the specified AWS Config rules are compliant. If a rule is noncompliant, this action returns the number of AWS resources that do not comply with the rule.

     

    A rule is compliant if all of the evaluated resources comply with it, and it is noncompliant if any of these resources do not comply.

     

    If AWS Config has no current evaluation results for the rule, it returns ``INSUFFICIENT_DATA`` . This result might indicate one of the following conditions:

     

     
    * AWS Config has never invoked an evaluation for the rule. To check whether it has, use the ``DescribeConfigRuleEvaluationStatus`` action to get the ``LastSuccessfulInvocationTime`` and ``LastFailedInvocationTime`` . 
     
    * The rule's AWS Lambda function is failing to send evaluation results to AWS Config. Verify that the role that you assigned to your configuration recorder includes the ``config:PutEvaluations`` permission. If the rule is a custom rule, verify that the AWS Lambda execution role includes the ``config:PutEvaluations`` permission. 
     
    * The rule's AWS Lambda function has returned ``NOT_APPLICABLE`` for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByConfigRule>`_    


    **Request Syntax** 
    ::

      response = client.describe_compliance_by_config_rule(
          ConfigRuleNames=[
              'string',
          ],
          ComplianceTypes=[
              'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
          ],
          NextToken='string'
      )
    :type ConfigRuleNames: list
    :param ConfigRuleNames: 

      Specify one or more AWS Config rule names to filter the results by rule.

      

    
      - *(string) --* 

      
  
    :type ComplianceTypes: list
    :param ComplianceTypes: 

      Filters the results by compliance.

       

      The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` .

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ComplianceByConfigRules': [
                {
                    'ConfigRuleName': 'string',
                    'Compliance': {
                        'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                        'ComplianceContributorCount': {
                            'CappedCount': 123,
                            'CapExceeded': True|False
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ComplianceByConfigRules** *(list) --* 

          Indicates whether each of the specified AWS Config rules is compliant.

          
          

          - *(dict) --* 

            Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the resources that the rule evaluated comply with it, and it is noncompliant if any of these resources do not comply.

            
            

            - **ConfigRuleName** *(string) --* 

              The name of the AWS Config rule.

              
            

            - **Compliance** *(dict) --* 

              Indicates whether the AWS Config rule is compliant.

              
              

              - **ComplianceType** *(string) --* 

                Indicates whether an AWS resource or AWS Config rule is compliant.

                 

                A resource is compliant if it complies with all of the AWS Config rules that evaluate it, and it is noncompliant if it does not comply with one or more of these rules.

                 

                A rule is compliant if all of the resources that the rule evaluates comply with it, and it is noncompliant if any of these resources do not comply.

                 

                AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or Config rule.

                 

                For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

                
              

              - **ComplianceContributorCount** *(dict) --* 

                The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.

                
                

                - **CappedCount** *(integer) --* 

                  The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

                  
                

                - **CapExceeded** *(boolean) --* 

                  Indicates whether the maximum count is reached.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

  .. py:method:: describe_compliance_by_resource(**kwargs)

    

    Indicates whether the specified AWS resources are compliant. If a resource is noncompliant, this action returns the number of AWS Config rules that the resource does not comply with.

     

    A resource is compliant if it complies with all the AWS Config rules that evaluate it. It is noncompliant if it does not comply with one or more of these rules.

     

    If AWS Config has no current evaluation results for the resource, it returns ``INSUFFICIENT_DATA`` . This result might indicate one of the following conditions about the rules that evaluate the resource:

     

     
    * AWS Config has never invoked an evaluation for the rule. To check whether it has, use the ``DescribeConfigRuleEvaluationStatus`` action to get the ``LastSuccessfulInvocationTime`` and ``LastFailedInvocationTime`` . 
     
    * The rule's AWS Lambda function is failing to send evaluation results to AWS Config. Verify that the role that you assigned to your configuration recorder includes the ``config:PutEvaluations`` permission. If the rule is a custom rule, verify that the AWS Lambda execution role includes the ``config:PutEvaluations`` permission. 
     
    * The rule's AWS Lambda function has returned ``NOT_APPLICABLE`` for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByResource>`_    


    **Request Syntax** 
    ::

      response = client.describe_compliance_by_resource(
          ResourceType='string',
          ResourceId='string',
          ComplianceTypes=[
              'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
          ],
          Limit=123,
          NextToken='string'
      )
    :type ResourceType: string
    :param ResourceType: 

      The types of AWS resources for which you want compliance information; for example, ``AWS::EC2::Instance`` . For this action, you can specify that the resource type is an AWS account by specifying ``AWS::::Account`` .

      

    
    :type ResourceId: string
    :param ResourceId: 

      The ID of the AWS resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for ``ResourceType`` .

      

    
    :type ComplianceTypes: list
    :param ComplianceTypes: 

      Filters the results by compliance.

       

      The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` .

      

    
      - *(string) --* 

      
  
    :type Limit: integer
    :param Limit: 

      The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.

      

    
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ComplianceByResources': [
                {
                    'ResourceType': 'string',
                    'ResourceId': 'string',
                    'Compliance': {
                        'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                        'ComplianceContributorCount': {
                            'CappedCount': 123,
                            'CapExceeded': True|False
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ComplianceByResources** *(list) --* 

          Indicates whether the specified AWS resource complies with all of the AWS Config rules that evaluate it.

          
          

          - *(dict) --* 

            Indicates whether an AWS resource that is evaluated according to one or more AWS Config rules is compliant. A resource is compliant if it complies with all of the rules that evaluate it, and it is noncompliant if it does not comply with one or more of these rules.

            
            

            - **ResourceType** *(string) --* 

              The type of the AWS resource that was evaluated.

              
            

            - **ResourceId** *(string) --* 

              The ID of the AWS resource that was evaluated.

              
            

            - **Compliance** *(dict) --* 

              Indicates whether the AWS resource complies with all of the AWS Config rules that evaluated it.

              
              

              - **ComplianceType** *(string) --* 

                Indicates whether an AWS resource or AWS Config rule is compliant.

                 

                A resource is compliant if it complies with all of the AWS Config rules that evaluate it, and it is noncompliant if it does not comply with one or more of these rules.

                 

                A rule is compliant if all of the resources that the rule evaluates comply with it, and it is noncompliant if any of these resources do not comply.

                 

                AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or Config rule.

                 

                For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

                
              

              - **ComplianceContributorCount** *(dict) --* 

                The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.

                
                

                - **CappedCount** *(integer) --* 

                  The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

                  
                

                - **CapExceeded** *(boolean) --* 

                  Indicates whether the maximum count is reached.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

  .. py:method:: describe_config_rule_evaluation_status(**kwargs)

    

    Returns status information for each of your AWS managed Config rules. The status includes information such as the last time AWS Config invoked the rule, the last time AWS Config failed to invoke the rule, and the related error for the last failure.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRuleEvaluationStatus>`_    


    **Request Syntax** 
    ::

      response = client.describe_config_rule_evaluation_status(
          ConfigRuleNames=[
              'string',
          ],
          NextToken='string',
          Limit=123
      )
    :type ConfigRuleNames: list
    :param ConfigRuleNames: 

      The name of the AWS managed Config rules for which you want status information. If you do not specify any names, AWS Config returns status information for all AWS managed Config rules that you use.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    :type Limit: integer
    :param Limit: 

      The number of rule evaluation results that you want returned.

       

      This parameter is required if the rule limit for your account is more than the default of 50 rules.

       

      For more information about requesting a rule limit increase, see `AWS Config Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config>`__ in the *AWS General Reference Guide* .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigRulesEvaluationStatus': [
                {
                    'ConfigRuleName': 'string',
                    'ConfigRuleArn': 'string',
                    'ConfigRuleId': 'string',
                    'LastSuccessfulInvocationTime': datetime(2015, 1, 1),
                    'LastFailedInvocationTime': datetime(2015, 1, 1),
                    'LastSuccessfulEvaluationTime': datetime(2015, 1, 1),
                    'LastFailedEvaluationTime': datetime(2015, 1, 1),
                    'FirstActivatedTime': datetime(2015, 1, 1),
                    'LastErrorCode': 'string',
                    'LastErrorMessage': 'string',
                    'FirstEvaluationStarted': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ConfigRulesEvaluationStatus** *(list) --* 

          Status information about your AWS managed Config rules.

          
          

          - *(dict) --* 

            Status information for your AWS managed Config rules. The status includes information such as the last time the rule ran, the last time it failed, and the related error for the last failure.

             

            This action does not return status information about custom Config rules.

            
            

            - **ConfigRuleName** *(string) --* 

              The name of the AWS Config rule.

              
            

            - **ConfigRuleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the AWS Config rule.

              
            

            - **ConfigRuleId** *(string) --* 

              The ID of the AWS Config rule.

              
            

            - **LastSuccessfulInvocationTime** *(datetime) --* 

              The time that AWS Config last successfully invoked the AWS Config rule to evaluate your AWS resources.

              
            

            - **LastFailedInvocationTime** *(datetime) --* 

              The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS resources.

              
            

            - **LastSuccessfulEvaluationTime** *(datetime) --* 

              The time that AWS Config last successfully evaluated your AWS resources against the rule.

              
            

            - **LastFailedEvaluationTime** *(datetime) --* 

              The time that AWS Config last failed to evaluate your AWS resources against the rule.

              
            

            - **FirstActivatedTime** *(datetime) --* 

              The time that you first activated the AWS Config rule.

              
            

            - **LastErrorCode** *(string) --* 

              The error code that AWS Config returned when the rule last failed.

              
            

            - **LastErrorMessage** *(string) --* 

              The error message that AWS Config returned when the rule last failed.

              
            

            - **FirstEvaluationStarted** *(boolean) --* 

              Indicates whether AWS Config has evaluated your resources against the rule at least once.

               

               
              * ``true`` - AWS Config has evaluated your AWS resources against the rule at least once. 
               
              * ``false`` - AWS Config has not once finished evaluating your AWS resources against the rule. 
               

              
        
      
        

        - **NextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

  .. py:method:: describe_config_rules(**kwargs)

    

    Returns details about your AWS Config rules.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRules>`_    


    **Request Syntax** 
    ::

      response = client.describe_config_rules(
          ConfigRuleNames=[
              'string',
          ],
          NextToken='string'
      )
    :type ConfigRuleNames: list
    :param ConfigRuleNames: 

      The names of the AWS Config rules for which you want details. If you do not specify any names, AWS Config returns details for all your rules.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigRules': [
                {
                    'ConfigRuleName': 'string',
                    'ConfigRuleArn': 'string',
                    'ConfigRuleId': 'string',
                    'Description': 'string',
                    'Scope': {
                        'ComplianceResourceTypes': [
                            'string',
                        ],
                        'TagKey': 'string',
                        'TagValue': 'string',
                        'ComplianceResourceId': 'string'
                    },
                    'Source': {
                        'Owner': 'CUSTOM_LAMBDA'|'AWS',
                        'SourceIdentifier': 'string',
                        'SourceDetails': [
                            {
                                'EventSource': 'aws.config',
                                'MessageType': 'ConfigurationItemChangeNotification'|'ConfigurationSnapshotDeliveryCompleted'|'ScheduledNotification'|'OversizedConfigurationItemChangeNotification',
                                'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                            },
                        ]
                    },
                    'InputParameters': 'string',
                    'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                    'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ConfigRules** *(list) --* 

          The details about your AWS Config rules.

          
          

          - *(dict) --* 

            An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a predefined function for an AWS managed rule. The function evaluates configuration items to assess whether your AWS resources comply with your desired configurations. This function can run when AWS Config detects a configuration change to an AWS resource and at a periodic frequency that you choose (for example, every 24 hours).

             

            .. note::

               

              You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

               

             

            For more information about developing and using AWS Config rules, see `Evaluating AWS Resource Configurations with AWS Config <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the *AWS Config Developer Guide* .

            
            

            - **ConfigRuleName** *(string) --* 

              The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.

              
            

            - **ConfigRuleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the AWS Config rule.

              
            

            - **ConfigRuleId** *(string) --* 

              The ID of the AWS Config rule.

              
            

            - **Description** *(string) --* 

              The description that you provide for the AWS Config rule.

              
            

            - **Scope** *(dict) --* 

              Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.

              
              

              - **ComplianceResourceTypes** *(list) --* 

                The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .

                
                

                - *(string) --* 
            
              

              - **TagKey** *(string) --* 

                The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.

                
              

              - **TagValue** *(string) --* 

                The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .

                
              

              - **ComplianceResourceId** *(string) --* 

                The IDs of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .

                
          
            

            - **Source** *(dict) --* 

              Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.

              
              

              - **Owner** *(string) --* 

                Indicates whether AWS or the customer owns and manages the AWS Config rule.

                
              

              - **SourceIdentifier** *(string) --* 

                For AWS Config managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Managed Config Rules <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__ .

                 

                For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

                
              

              - **SourceDetails** *(list) --* 

                Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.

                
                

                - *(dict) --* 

                  Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for ``SourceDetail`` only for custom rules. 

                  
                  

                  - **EventSource** *(string) --* 

                    The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.

                    
                  

                  - **MessageType** *(string) --* 

                    The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:

                     

                     
                    * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. 
                     
                    * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. 
                     
                    * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` . 
                     
                    * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot. 
                     

                     

                    If you want your custom rule to be triggered by configuration changes, specify both ``ConfigurationItemChangeNotification`` and ``OversizedConfigurationItemChangeNotification`` . 

                    
                  

                  - **MaximumExecutionFrequency** *(string) --* 

                    The frequency that you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value.

                     

                    .. note::

                       

                      By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

                       

                    
              
            
          
            

            - **InputParameters** *(string) --* 

              A string in JSON format that is passed to the AWS Config rule Lambda function.

              
            

            - **MaximumExecutionFrequency** *(string) --* 

              The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when:

               

               
              * You are using an AWS managed rule that is triggered at a periodic frequency. 
               
              * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties . 
               

               

              .. note::

                 

                By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

                 

              
            

            - **ConfigRuleState** *(string) --* 

              Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the Config rule.

               

              AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the ``StartConfigRulesEvaluation`` request to evaluate your resources against the Config rule.

               

              AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use the ``DeleteEvaluationResults`` request to delete the current evaluation results for the Config rule.

               

              AWS Config sets the state of a rule to ``DELETING`` temporarily after you use the ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.

              
        
      
        

        - **NextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

  .. py:method:: describe_configuration_recorder_status(**kwargs)

    

    Returns the current status of the specified configuration recorder. If a configuration recorder is not specified, this action returns the status of all configuration recorder associated with the account.

     

    .. note::

       

      Currently, you can specify only one configuration recorder per region in your account.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationRecorderStatus>`_    


    **Request Syntax** 
    ::

      response = client.describe_configuration_recorder_status(
          ConfigurationRecorderNames=[
              'string',
          ]
      )
    :type ConfigurationRecorderNames: list
    :param ConfigurationRecorderNames: 

      The name(s) of the configuration recorder. If the name is not specified, the action returns the current status of all the configuration recorders associated with the account.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigurationRecordersStatus': [
                {
                    'name': 'string',
                    'lastStartTime': datetime(2015, 1, 1),
                    'lastStopTime': datetime(2015, 1, 1),
                    'recording': True|False,
                    'lastStatus': 'Pending'|'Success'|'Failure',
                    'lastErrorCode': 'string',
                    'lastErrorMessage': 'string',
                    'lastStatusChangeTime': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the  DescribeConfigurationRecorderStatus action in JSON format.

        
        

        - **ConfigurationRecordersStatus** *(list) --* 

          A list that contains status of the specified recorders.

          
          

          - *(dict) --* 

            The current status of the configuration recorder.

            
            

            - **name** *(string) --* 

              The name of the configuration recorder.

              
            

            - **lastStartTime** *(datetime) --* 

              The time the recorder was last started.

              
            

            - **lastStopTime** *(datetime) --* 

              The time the recorder was last stopped.

              
            

            - **recording** *(boolean) --* 

              Specifies whether the recorder is currently recording or not.

              
            

            - **lastStatus** *(string) --* 

              The last (previous) status of the recorder.

              
            

            - **lastErrorCode** *(string) --* 

              The error code indicating that the recording failed.

              
            

            - **lastErrorMessage** *(string) --* 

              The message indicating that the recording failed due to an error.

              
            

            - **lastStatusChangeTime** *(datetime) --* 

              The time when the status was last changed.

              
        
      
    

  .. py:method:: describe_configuration_recorders(**kwargs)

    

    Returns the details for the specified configuration recorders. If the configuration recorder is not specified, this action returns the details for all configuration recorders associated with the account.

     

    .. note::

       

      Currently, you can specify only one configuration recorder per region in your account.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationRecorders>`_    


    **Request Syntax** 
    ::

      response = client.describe_configuration_recorders(
          ConfigurationRecorderNames=[
              'string',
          ]
      )
    :type ConfigurationRecorderNames: list
    :param ConfigurationRecorderNames: 

      A list of configuration recorder names.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigurationRecorders': [
                {
                    'name': 'string',
                    'roleARN': 'string',
                    'recordingGroup': {
                        'allSupported': True|False,
                        'includeGlobalResourceTypes': True|False,
                        'resourceTypes': [
                            'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                        ]
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the  DescribeConfigurationRecorders action.

        
        

        - **ConfigurationRecorders** *(list) --* 

          A list that contains the descriptions of the specified configuration recorders.

          
          

          - *(dict) --* 

            An object that represents the recording of configuration changes of an AWS resource.

            
            

            - **name** *(string) --* 

              The name of the recorder. By default, AWS Config automatically assigns the name "default" when creating the configuration recorder. You cannot change the assigned name.

              
            

            - **roleARN** *(string) --* 

              Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.

              
            

            - **recordingGroup** *(dict) --* 

              Specifies the types of AWS resource for which AWS Config records configuration changes.

              
              

              - **allSupported** *(boolean) --* 

                Specifies whether AWS Config records configuration changes for every supported type of regional resource.

                 

                If you set this option to ``true`` , when AWS Config adds support for a new type of regional resource, it automatically starts recording resources of that type.

                 

                If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .

                
              

              - **includeGlobalResourceTypes** *(boolean) --* 

                Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.

                 

                Before you can set this option to ``true`` , you must set the ``allSupported`` option to ``true`` .

                 

                If you set this option to ``true`` , when AWS Config adds support for a new type of global resource, it automatically starts recording resources of that type.

                 

                The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.

                
              

              - **resourceTypes** *(list) --* 

                A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, ``AWS::EC2::Instance`` or ``AWS::CloudTrail::Trail`` ).

                 

                Before you can set this option to ``true`` , you must set the ``allSupported`` option to ``false`` .

                 

                If you set this option to ``true`` , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.

                 

                For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in `Supported AWS Resource Types <http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__ .

                
                

                - *(string) --* 
            
          
        
      
    

  .. py:method:: describe_delivery_channel_status(**kwargs)

    

    Returns the current status of the specified delivery channel. If a delivery channel is not specified, this action returns the current status of all delivery channels associated with the account.

     

    .. note::

       

      Currently, you can specify only one delivery channel per region in your account.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeDeliveryChannelStatus>`_    


    **Request Syntax** 
    ::

      response = client.describe_delivery_channel_status(
          DeliveryChannelNames=[
              'string',
          ]
      )
    :type DeliveryChannelNames: list
    :param DeliveryChannelNames: 

      A list of delivery channel names.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeliveryChannelsStatus': [
                {
                    'name': 'string',
                    'configSnapshotDeliveryInfo': {
                        'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                        'lastErrorCode': 'string',
                        'lastErrorMessage': 'string',
                        'lastAttemptTime': datetime(2015, 1, 1),
                        'lastSuccessfulTime': datetime(2015, 1, 1),
                        'nextDeliveryTime': datetime(2015, 1, 1)
                    },
                    'configHistoryDeliveryInfo': {
                        'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                        'lastErrorCode': 'string',
                        'lastErrorMessage': 'string',
                        'lastAttemptTime': datetime(2015, 1, 1),
                        'lastSuccessfulTime': datetime(2015, 1, 1),
                        'nextDeliveryTime': datetime(2015, 1, 1)
                    },
                    'configStreamDeliveryInfo': {
                        'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                        'lastErrorCode': 'string',
                        'lastErrorMessage': 'string',
                        'lastStatusChangeTime': datetime(2015, 1, 1)
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the  DescribeDeliveryChannelStatus action.

        
        

        - **DeliveryChannelsStatus** *(list) --* 

          A list that contains the status of a specified delivery channel.

          
          

          - *(dict) --* 

            The status of a specified delivery channel.

             

            Valid values: ``Success`` | ``Failure``  

            
            

            - **name** *(string) --* 

              The name of the delivery channel.

              
            

            - **configSnapshotDeliveryInfo** *(dict) --* 

              A list containing the status of the delivery of the snapshot to the specified Amazon S3 bucket.

              
              

              - **lastStatus** *(string) --* 

                Status of the last attempted delivery.

                
              

              - **lastErrorCode** *(string) --* 

                The error code from the last attempted delivery.

                
              

              - **lastErrorMessage** *(string) --* 

                The error message from the last attempted delivery.

                
              

              - **lastAttemptTime** *(datetime) --* 

                The time of the last attempted delivery.

                
              

              - **lastSuccessfulTime** *(datetime) --* 

                The time of the last successful delivery.

                
              

              - **nextDeliveryTime** *(datetime) --* 

                The time that the next delivery occurs.

                
          
            

            - **configHistoryDeliveryInfo** *(dict) --* 

              A list that contains the status of the delivery of the configuration history to the specified Amazon S3 bucket.

              
              

              - **lastStatus** *(string) --* 

                Status of the last attempted delivery.

                
              

              - **lastErrorCode** *(string) --* 

                The error code from the last attempted delivery.

                
              

              - **lastErrorMessage** *(string) --* 

                The error message from the last attempted delivery.

                
              

              - **lastAttemptTime** *(datetime) --* 

                The time of the last attempted delivery.

                
              

              - **lastSuccessfulTime** *(datetime) --* 

                The time of the last successful delivery.

                
              

              - **nextDeliveryTime** *(datetime) --* 

                The time that the next delivery occurs.

                
          
            

            - **configStreamDeliveryInfo** *(dict) --* 

              A list containing the status of the delivery of the configuration stream notification to the specified Amazon SNS topic.

              
              

              - **lastStatus** *(string) --* 

                Status of the last attempted delivery.

                 

                 **Note** Providing an SNS topic on a `DeliveryChannel <http://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html>`__ for AWS Config is optional. If the SNS delivery is turned off, the last status will be **Not_Applicable** .

                
              

              - **lastErrorCode** *(string) --* 

                The error code from the last attempted delivery.

                
              

              - **lastErrorMessage** *(string) --* 

                The error message from the last attempted delivery.

                
              

              - **lastStatusChangeTime** *(datetime) --* 

                The time from the last status change.

                
          
        
      
    

  .. py:method:: describe_delivery_channels(**kwargs)

    

    Returns details about the specified delivery channel. If a delivery channel is not specified, this action returns the details of all delivery channels associated with the account.

     

    .. note::

       

      Currently, you can specify only one delivery channel per region in your account.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeDeliveryChannels>`_    


    **Request Syntax** 
    ::

      response = client.describe_delivery_channels(
          DeliveryChannelNames=[
              'string',
          ]
      )
    :type DeliveryChannelNames: list
    :param DeliveryChannelNames: 

      A list of delivery channel names.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeliveryChannels': [
                {
                    'name': 'string',
                    's3BucketName': 'string',
                    's3KeyPrefix': 'string',
                    'snsTopicARN': 'string',
                    'configSnapshotDeliveryProperties': {
                        'deliveryFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the  DescribeDeliveryChannels action.

        
        

        - **DeliveryChannels** *(list) --* 

          A list that contains the descriptions of the specified delivery channel.

          
          

          - *(dict) --* 

            The channel through which AWS Config delivers notifications and updated configuration states.

            
            

            - **name** *(string) --* 

              The name of the delivery channel. By default, AWS Config assigns the name "default" when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.

              
            

            - **s3BucketName** *(string) --* 

              The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.

               

              If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see `Permissions for the Amazon S3 Bucket <http://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`__ in the AWS Config Developer Guide.

              
            

            - **s3KeyPrefix** *(string) --* 

              The prefix for the specified Amazon S3 bucket.

              
            

            - **snsTopicARN** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.

               

              If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see `Permissions for the Amazon SNS Topic <http://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`__ in the AWS Config Developer Guide.

              
            

            - **configSnapshotDeliveryProperties** *(dict) --* 

              The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.

              
              

              - **deliveryFrequency** *(string) --* 

                The frequency with which AWS Config delivers configuration snapshots.

                
          
        
      
    

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


  .. py:method:: get_compliance_details_by_config_rule(**kwargs)

    

    Returns the evaluation results for the specified AWS Config rule. The results indicate which AWS resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByConfigRule>`_    


    **Request Syntax** 
    ::

      response = client.get_compliance_details_by_config_rule(
          ConfigRuleName='string',
          ComplianceTypes=[
              'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
          ],
          Limit=123,
          NextToken='string'
      )
    :type ConfigRuleName: string
    :param ConfigRuleName: **[REQUIRED]** 

      The name of the AWS Config rule for which you want compliance information.

      

    
    :type ComplianceTypes: list
    :param ComplianceTypes: 

      Filters the results by compliance.

       

      The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .

      

    
      - *(string) --* 

      
  
    :type Limit: integer
    :param Limit: 

      The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.

      

    
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EvaluationResults': [
                {
                    'EvaluationResultIdentifier': {
                        'EvaluationResultQualifier': {
                            'ConfigRuleName': 'string',
                            'ResourceType': 'string',
                            'ResourceId': 'string'
                        },
                        'OrderingTimestamp': datetime(2015, 1, 1)
                    },
                    'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                    'ResultRecordedTime': datetime(2015, 1, 1),
                    'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                    'Annotation': 'string',
                    'ResultToken': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **EvaluationResults** *(list) --* 

          Indicates whether the AWS resource complies with the specified AWS Config rule.

          
          

          - *(dict) --* 

            The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related timestamps, and supplementary information.

            
            

            - **EvaluationResultIdentifier** *(dict) --* 

              Uniquely identifies the evaluation result.

              
              

              - **EvaluationResultQualifier** *(dict) --* 

                Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.

                
                

                - **ConfigRuleName** *(string) --* 

                  The name of the AWS Config rule that was used in the evaluation.

                  
                

                - **ResourceType** *(string) --* 

                  The type of AWS resource that was evaluated.

                  
                

                - **ResourceId** *(string) --* 

                  The ID of the evaluated AWS resource.

                  
            
              

              - **OrderingTimestamp** *(datetime) --* 

                The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.

                
          
            

            - **ComplianceType** *(string) --* 

              Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

               

              For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

              
            

            - **ResultRecordedTime** *(datetime) --* 

              The time when AWS Config recorded the evaluation result.

              
            

            - **ConfigRuleInvokedTime** *(datetime) --* 

              The time when the AWS Config rule evaluated the AWS resource.

              
            

            - **Annotation** *(string) --* 

              Supplementary information about how the evaluation determined the compliance.

              
            

            - **ResultToken** *(string) --* 

              An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.

              
        
      
        

        - **NextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

  .. py:method:: get_compliance_details_by_resource(**kwargs)

    

    Returns the evaluation results for the specified AWS resource. The results indicate which AWS Config rules were used to evaluate the resource, when each rule was last used, and whether the resource complies with each rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByResource>`_    


    **Request Syntax** 
    ::

      response = client.get_compliance_details_by_resource(
          ResourceType='string',
          ResourceId='string',
          ComplianceTypes=[
              'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
          ],
          NextToken='string'
      )
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of the AWS resource for which you want compliance information.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The ID of the AWS resource for which you want compliance information.

      

    
    :type ComplianceTypes: list
    :param ComplianceTypes: 

      Filters the results by compliance.

       

      The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      The ``NextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EvaluationResults': [
                {
                    'EvaluationResultIdentifier': {
                        'EvaluationResultQualifier': {
                            'ConfigRuleName': 'string',
                            'ResourceType': 'string',
                            'ResourceId': 'string'
                        },
                        'OrderingTimestamp': datetime(2015, 1, 1)
                    },
                    'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                    'ResultRecordedTime': datetime(2015, 1, 1),
                    'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                    'Annotation': 'string',
                    'ResultToken': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **EvaluationResults** *(list) --* 

          Indicates whether the specified AWS resource complies each AWS Config rule.

          
          

          - *(dict) --* 

            The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related timestamps, and supplementary information.

            
            

            - **EvaluationResultIdentifier** *(dict) --* 

              Uniquely identifies the evaluation result.

              
              

              - **EvaluationResultQualifier** *(dict) --* 

                Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.

                
                

                - **ConfigRuleName** *(string) --* 

                  The name of the AWS Config rule that was used in the evaluation.

                  
                

                - **ResourceType** *(string) --* 

                  The type of AWS resource that was evaluated.

                  
                

                - **ResourceId** *(string) --* 

                  The ID of the evaluated AWS resource.

                  
            
              

              - **OrderingTimestamp** *(datetime) --* 

                The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.

                
          
            

            - **ComplianceType** *(string) --* 

              Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

               

              For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

              
            

            - **ResultRecordedTime** *(datetime) --* 

              The time when AWS Config recorded the evaluation result.

              
            

            - **ConfigRuleInvokedTime** *(datetime) --* 

              The time when the AWS Config rule evaluated the AWS resource.

              
            

            - **Annotation** *(string) --* 

              Supplementary information about how the evaluation determined the compliance.

              
            

            - **ResultToken** *(string) --* 

              An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.

              
        
      
        

        - **NextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

  .. py:method:: get_compliance_summary_by_config_rule()

    

    Returns the number of AWS Config rules that are compliant and noncompliant, up to a maximum of 25 for each.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceSummaryByConfigRule>`_    


    **Request Syntax** 

    ::

      response = client.get_compliance_summary_by_config_rule()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ComplianceSummary': {
                'CompliantResourceCount': {
                    'CappedCount': 123,
                    'CapExceeded': True|False
                },
                'NonCompliantResourceCount': {
                    'CappedCount': 123,
                    'CapExceeded': True|False
                },
                'ComplianceSummaryTimestamp': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ComplianceSummary** *(dict) --* 

          The number of AWS Config rules that are compliant and the number that are noncompliant, up to a maximum of 25 for each.

          
          

          - **CompliantResourceCount** *(dict) --* 

            The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.

            
            

            - **CappedCount** *(integer) --* 

              The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

              
            

            - **CapExceeded** *(boolean) --* 

              Indicates whether the maximum count is reached.

              
        
          

          - **NonCompliantResourceCount** *(dict) --* 

            The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.

            
            

            - **CappedCount** *(integer) --* 

              The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

              
            

            - **CapExceeded** *(boolean) --* 

              Indicates whether the maximum count is reached.

              
        
          

          - **ComplianceSummaryTimestamp** *(datetime) --* 

            The time that AWS Config created the compliance summary.

            
      
    

  .. py:method:: get_compliance_summary_by_resource_type(**kwargs)

    

    Returns the number of resources that are compliant and the number that are noncompliant. You can specify one or more resource types to get these numbers for each resource type. The maximum number returned is 100.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceSummaryByResourceType>`_    


    **Request Syntax** 
    ::

      response = client.get_compliance_summary_by_resource_type(
          ResourceTypes=[
              'string',
          ]
      )
    :type ResourceTypes: list
    :param ResourceTypes: 

      Specify one or more resource types to get the number of resources that are compliant and the number that are noncompliant for each resource type.

       

      For this request, you can specify an AWS resource type such as ``AWS::EC2::Instance`` , and you can specify that the resource type is an AWS account by specifying ``AWS::::Account`` .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ComplianceSummariesByResourceType': [
                {
                    'ResourceType': 'string',
                    'ComplianceSummary': {
                        'CompliantResourceCount': {
                            'CappedCount': 123,
                            'CapExceeded': True|False
                        },
                        'NonCompliantResourceCount': {
                            'CappedCount': 123,
                            'CapExceeded': True|False
                        },
                        'ComplianceSummaryTimestamp': datetime(2015, 1, 1)
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ComplianceSummariesByResourceType** *(list) --* 

          The number of resources that are compliant and the number that are noncompliant. If one or more resource types were provided with the request, the numbers are returned for each resource type. The maximum number returned is 100.

          
          

          - *(dict) --* 

            The number of AWS resources of a specific type that are compliant or noncompliant, up to a maximum of 100 for each compliance.

            
            

            - **ResourceType** *(string) --* 

              The type of AWS resource.

              
            

            - **ComplianceSummary** *(dict) --* 

              The number of AWS resources that are compliant or noncompliant, up to a maximum of 100 for each compliance.

              
              

              - **CompliantResourceCount** *(dict) --* 

                The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.

                
                

                - **CappedCount** *(integer) --* 

                  The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

                  
                

                - **CapExceeded** *(boolean) --* 

                  Indicates whether the maximum count is reached.

                  
            
              

              - **NonCompliantResourceCount** *(dict) --* 

                The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.

                
                

                - **CappedCount** *(integer) --* 

                  The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

                  
                

                - **CapExceeded** *(boolean) --* 

                  Indicates whether the maximum count is reached.

                  
            
              

              - **ComplianceSummaryTimestamp** *(datetime) --* 

                The time that AWS Config created the compliance summary.

                
          
        
      
    

  .. py:method:: get_discovered_resource_counts(**kwargs)

    

    Returns the resource types, the number of each resource type, and the total number of resources that AWS Config is recording in this region for your AWS account. 

     

     **Example**  

     

     
    * AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets. 
     
    * You make a call to the ``GetDiscoveredResourceCounts`` action and specify that you want all resource types.  
     
    * AWS Config returns the following: 

       
      * The resource types (EC2 instances, IAM users, and S3 buckets) 
       
      * The number of each resource type (25, 20, and 15) 
       
      * The total number of all resources (60) 
       

     
     

     

    The response is paginated. By default, AWS Config lists 100  ResourceCount objects on each page. You can customize this number with the ``limit`` parameter. The response includes a ``nextToken`` string. To get the next page of results, run the request again and specify the string for the ``nextToken`` parameter.

     

    .. note::

       

      If you make a call to the  GetDiscoveredResourceCounts action, you may not immediately receive resource counts in the following situations:

       

       
      * You are a new AWS Config customer 
       
      * You just enabled resource recording 
       

       

      It may take a few minutes for AWS Config to record and count your resources. Wait a few minutes and then retry the  GetDiscoveredResourceCounts action. 

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetDiscoveredResourceCounts>`_    


    **Request Syntax** 
    ::

      response = client.get_discovered_resource_counts(
          resourceTypes=[
              'string',
          ],
          limit=123,
          nextToken='string'
      )
    :type resourceTypes: list
    :param resourceTypes: 

      The comma-separated list that specifies the resource types that you want the AWS Config to return. For example, (``"AWS::EC2::Instance"`` , ``"AWS::IAM::User"`` ).

       

      If a value for ``resourceTypes`` is not specified, AWS Config returns all resource types that AWS Config is recording in the region for your account.

       

      .. note::

         

        If the configuration recorder is turned off, AWS Config returns an empty list of  ResourceCount objects. If the configuration recorder is not recording a specific resource type (for example, S3 buckets), that resource type is not returned in the list of  ResourceCount objects.

         

      

    
      - *(string) --* 

      
  
    :type limit: integer
    :param limit: 

      The maximum number of  ResourceCount objects returned on each page. The default is 100. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'totalDiscoveredResources': 123,
            'resourceCounts': [
                {
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                    'count': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **totalDiscoveredResources** *(integer) --* 

          The total number of resources that AWS Config is recording in the region for your account. If you specify resource types in the request, AWS Config returns only the total number of resources for those resource types.

           

           **Example**  

           

           
          * AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets, for a total of 60 resources. 
           
          * You make a call to the ``GetDiscoveredResourceCounts`` action and specify the resource type, ``"AWS::EC2::Instances"`` in the request. 
           
          * AWS Config returns 25 for ``totalDiscoveredResources`` . 
           

          
        

        - **resourceCounts** *(list) --* 

          The list of ``ResourceCount`` objects. Each object is listed in descending order by the number of resources.

          
          

          - *(dict) --* 

            An object that contains the resource type and the number of resources.

            
            

            - **resourceType** *(string) --* 

              The resource type, for example ``"AWS::EC2::Instance"`` .

              
            

            - **count** *(integer) --* 

              The number of resources.

              
        
      
        

        - **nextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

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


  .. py:method:: get_resource_config_history(**kwargs)

    

    Returns a list of configuration items for the specified resource. The list contains details about each state of the resource during the specified time interval.

     

    The response is paginated. By default, AWS Config returns a limit of 10 configuration items per page. You can customize this number with the ``limit`` parameter. The response includes a ``nextToken`` string. To get the next page of results, run the request again and specify the string for the ``nextToken`` parameter.

     

    .. note::

       

      Each call to the API is limited to span a duration of seven days. It is likely that the number of records returned is smaller than the specified ``limit`` . In such cases, you can make another call, using the ``nextToken`` .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetResourceConfigHistory>`_    


    **Request Syntax** 
    ::

      response = client.get_resource_config_history(
          resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
          resourceId='string',
          laterTime=datetime(2015, 1, 1),
          earlierTime=datetime(2015, 1, 1),
          chronologicalOrder='Reverse'|'Forward',
          limit=123,
          nextToken='string'
      )
    :type resourceType: string
    :param resourceType: **[REQUIRED]** 

      The resource type.

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The ID of the resource (for example., ``sg-xxxxxx`` ).

      

    
    :type laterTime: datetime
    :param laterTime: 

      The time stamp that indicates a later time. If not specified, current time is taken.

      

    
    :type earlierTime: datetime
    :param earlierTime: 

      The time stamp that indicates an earlier time. If not specified, the action returns paginated results that contain configuration items that start from when the first configuration item was recorded.

      

    
    :type chronologicalOrder: string
    :param chronologicalOrder: 

      The chronological order for configuration items listed. By default the results are listed in reverse chronological order.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of configuration items returned on each page. The default is 10. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'configurationItems': [
                {
                    'version': 'string',
                    'accountId': 'string',
                    'configurationItemCaptureTime': datetime(2015, 1, 1),
                    'configurationItemStatus': 'Ok'|'Failed'|'Discovered'|'Deleted',
                    'configurationStateId': 'string',
                    'configurationItemMD5Hash': 'string',
                    'arn': 'string',
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                    'resourceId': 'string',
                    'resourceName': 'string',
                    'awsRegion': 'string',
                    'availabilityZone': 'string',
                    'resourceCreationTime': datetime(2015, 1, 1),
                    'tags': {
                        'string': 'string'
                    },
                    'relatedEvents': [
                        'string',
                    ],
                    'relationships': [
                        {
                            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                            'resourceId': 'string',
                            'resourceName': 'string',
                            'relationshipName': 'string'
                        },
                    ],
                    'configuration': 'string',
                    'supplementaryConfiguration': {
                        'string': 'string'
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the  GetResourceConfigHistory action.

        
        

        - **configurationItems** *(list) --* 

          A list that contains the configuration history of one or more resources.

          
          

          - *(dict) --* 

            A list that contains detailed configurations of a specified resource.

            
            

            - **version** *(string) --* 

              The version number of the resource configuration.

              
            

            - **accountId** *(string) --* 

              The 12 digit AWS account ID associated with the resource.

              
            

            - **configurationItemCaptureTime** *(datetime) --* 

              The time when the configuration recording was initiated.

              
            

            - **configurationItemStatus** *(string) --* 

              The configuration item status.

              
            

            - **configurationStateId** *(string) --* 

              An identifier that indicates the ordering of the configuration items of a resource.

              
            

            - **configurationItemMD5Hash** *(string) --* 

              Unique MD5 hash that represents the configuration item's state.

               

              You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the resource.

              
            

            - **resourceType** *(string) --* 

              The type of AWS resource.

              
            

            - **resourceId** *(string) --* 

              The ID of the resource (for example., ``sg-xxxxxx`` ).

              
            

            - **resourceName** *(string) --* 

              The custom name of the resource, if available.

              
            

            - **awsRegion** *(string) --* 

              The region where the resource resides.

              
            

            - **availabilityZone** *(string) --* 

              The Availability Zone associated with the resource.

              
            

            - **resourceCreationTime** *(datetime) --* 

              The time stamp when the resource was created.

              
            

            - **tags** *(dict) --* 

              A mapping of key value tags associated with the resource.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **relatedEvents** *(list) --* 

              A list of CloudTrail event IDs.

               

              A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see `What is AWS CloudTrail? <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__ .

               

              An empty field indicates that the current configuration was not initiated by any event.

              
              

              - *(string) --* 
          
            

            - **relationships** *(list) --* 

              A list of related AWS resources.

              
              

              - *(dict) --* 

                The relationship of the related resource to the main resource.

                
                

                - **resourceType** *(string) --* 

                  The resource type of the related resource.

                  
                

                - **resourceId** *(string) --* 

                  The ID of the related resource (for example, ``sg-xxxxxx`` ).

                  
                

                - **resourceName** *(string) --* 

                  The custom name of the related resource, if available.

                  
                

                - **relationshipName** *(string) --* 

                  The type of relationship with the related resource.

                  
            
          
            

            - **configuration** *(string) --* 

              The description of the resource configuration.

              
            

            - **supplementaryConfiguration** *(dict) --* 

              Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the ``configuration`` parameter.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **nextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_discovered_resources(**kwargs)

    

    Accepts a resource type and returns a list of resource identifiers for the resources of that type. A resource identifier includes the resource type, ID, and (if available) the custom resource name. The results consist of resources that AWS Config has discovered, including those that AWS Config is not currently recording. You can narrow the results to include only resources that have specific resource IDs or a resource name.

     

    .. note::

       

      You can specify either resource IDs or a resource name but not both in the same request.

       

     

    The response is paginated. By default, AWS Config lists 100 resource identifiers on each page. You can customize this number with the ``limit`` parameter. The response includes a ``nextToken`` string. To get the next page of results, run the request again and specify the string for the ``nextToken`` parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/ListDiscoveredResources>`_    


    **Request Syntax** 
    ::

      response = client.list_discovered_resources(
          resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
          resourceIds=[
              'string',
          ],
          resourceName='string',
          limit=123,
          includeDeletedResources=True|False,
          nextToken='string'
      )
    :type resourceType: string
    :param resourceType: **[REQUIRED]** 

      The type of resources that you want AWS Config to list in the response.

      

    
    :type resourceIds: list
    :param resourceIds: 

      The IDs of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.

      

    
      - *(string) --* 

      
  
    :type resourceName: string
    :param resourceName: 

      The custom name of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.

      

    
    :type includeDeletedResources: boolean
    :param includeDeletedResources: 

      Specifies whether AWS Config includes deleted resources in the results. By default, deleted resources are not included.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resourceIdentifiers': [
                {
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                    'resourceId': 'string',
                    'resourceName': 'string',
                    'resourceDeletionTime': datetime(2015, 1, 1)
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **resourceIdentifiers** *(list) --* 

          The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.

          
          

          - *(dict) --* 

            The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.

            
            

            - **resourceType** *(string) --* 

              The type of resource.

              
            

            - **resourceId** *(string) --* 

              The ID of the resource (for example., ``sg-xxxxxx`` ).

              
            

            - **resourceName** *(string) --* 

              The custom name of the resource (if available).

              
            

            - **resourceDeletionTime** *(datetime) --* 

              The time that the resource was deleted.

              
        
      
        

        - **nextToken** *(string) --* 

          The string that you use in a subsequent request to get the next page of results in a paginated response.

          
    

  .. py:method:: put_config_rule(**kwargs)

    

    Adds or updates an AWS Config rule for evaluating whether your AWS resources comply with your desired configurations.

     

    You can use this action for custom Config rules and AWS managed Config rules. A custom Config rule is a rule that you develop and maintain. An AWS managed Config rule is a customizable, predefined rule that AWS Config provides.

     

    If you are adding a new custom Config rule, you must first create the AWS Lambda function that the rule invokes to evaluate your resources. When you use the ``PutConfigRule`` action to add the rule to AWS Config, you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function. Specify the ARN for the ``SourceIdentifier`` key. This key is part of the ``Source`` object, which is part of the ``ConfigRule`` object. 

     

    If you are adding an AWS managed Config rule, specify the rule's identifier for the ``SourceIdentifier`` key. To reference AWS managed Config rule identifiers, see `About AWS Managed Config Rules <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__ .

     

    For any new rule that you add, specify the ``ConfigRuleName`` in the ``ConfigRule`` object. Do not specify the ``ConfigRuleArn`` or the ``ConfigRuleId`` . These values are generated by AWS Config for new rules.

     

    If you are updating a rule that you added previously, you can specify the rule by ``ConfigRuleName`` , ``ConfigRuleId`` , or ``ConfigRuleArn`` in the ``ConfigRule`` data type that you use in this request.

     

    The maximum number of rules that AWS Config supports is 50.

     

    For more information about requesting a rule limit increase, see `AWS Config Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config>`__ in the *AWS General Reference Guide* .

     

    For more information about developing and using AWS Config rules, see `Evaluating AWS Resource Configurations with AWS Config <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the *AWS Config Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutConfigRule>`_    


    **Request Syntax** 
    ::

      response = client.put_config_rule(
          ConfigRule={
              'ConfigRuleName': 'string',
              'ConfigRuleArn': 'string',
              'ConfigRuleId': 'string',
              'Description': 'string',
              'Scope': {
                  'ComplianceResourceTypes': [
                      'string',
                  ],
                  'TagKey': 'string',
                  'TagValue': 'string',
                  'ComplianceResourceId': 'string'
              },
              'Source': {
                  'Owner': 'CUSTOM_LAMBDA'|'AWS',
                  'SourceIdentifier': 'string',
                  'SourceDetails': [
                      {
                          'EventSource': 'aws.config',
                          'MessageType': 'ConfigurationItemChangeNotification'|'ConfigurationSnapshotDeliveryCompleted'|'ScheduledNotification'|'OversizedConfigurationItemChangeNotification',
                          'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                      },
                  ]
              },
              'InputParameters': 'string',
              'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
              'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING'
          }
      )
    :type ConfigRule: dict
    :param ConfigRule: **[REQUIRED]** 

      The rule that you want to add to your account.

      

    
      - **ConfigRuleName** *(string) --* 

        The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.

        

      
      - **ConfigRuleArn** *(string) --* 

        The Amazon Resource Name (ARN) of the AWS Config rule.

        

      
      - **ConfigRuleId** *(string) --* 

        The ID of the AWS Config rule.

        

      
      - **Description** *(string) --* 

        The description that you provide for the AWS Config rule.

        

      
      - **Scope** *(dict) --* 

        Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.

        

      
        - **ComplianceResourceTypes** *(list) --* 

          The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .

          

        
          - *(string) --* 

          
      
        - **TagKey** *(string) --* 

          The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.

          

        
        - **TagValue** *(string) --* 

          The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .

          

        
        - **ComplianceResourceId** *(string) --* 

          The IDs of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .

          

        
      
      - **Source** *(dict) --* **[REQUIRED]** 

        Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.

        

      
        - **Owner** *(string) --* **[REQUIRED]** 

          Indicates whether AWS or the customer owns and manages the AWS Config rule.

          

        
        - **SourceIdentifier** *(string) --* **[REQUIRED]** 

          For AWS Config managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Managed Config Rules <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__ .

           

          For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

          

        
        - **SourceDetails** *(list) --* 

          Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.

          

        
          - *(dict) --* 

            Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for ``SourceDetail`` only for custom rules. 

            

          
            - **EventSource** *(string) --* 

              The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.

              

            
            - **MessageType** *(string) --* 

              The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:

               

               
              * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. 
               
              * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. 
               
              * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` . 
               
              * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot. 
               

               

              If you want your custom rule to be triggered by configuration changes, specify both ``ConfigurationItemChangeNotification`` and ``OversizedConfigurationItemChangeNotification`` . 

              

            
            - **MaximumExecutionFrequency** *(string) --* 

              The frequency that you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value.

               

              .. note::

                 

                By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

                 

              

            
          
      
      
      - **InputParameters** *(string) --* 

        A string in JSON format that is passed to the AWS Config rule Lambda function.

        

      
      - **MaximumExecutionFrequency** *(string) --* 

        The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when:

         

         
        * You are using an AWS managed rule that is triggered at a periodic frequency. 
         
        * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties . 
         

         

        .. note::

           

          By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

           

        

      
      - **ConfigRuleState** *(string) --* 

        Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the Config rule.

         

        AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the ``StartConfigRulesEvaluation`` request to evaluate your resources against the Config rule.

         

        AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use the ``DeleteEvaluationResults`` request to delete the current evaluation results for the Config rule.

         

        AWS Config sets the state of a rule to ``DELETING`` temporarily after you use the ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.

        

      
    
    
    :returns: None

  .. py:method:: put_configuration_recorder(**kwargs)

    

    Creates a new configuration recorder to record the selected resource configurations.

     

    You can use this action to change the role ``roleARN`` and/or the ``recordingGroup`` of an existing recorder. To change the role, call the action on the existing configuration recorder and specify a role.

     

    .. note::

       

      Currently, you can specify only one configuration recorder per region in your account.

       

      If ``ConfigurationRecorder`` does not have the **recordingGroup** parameter specified, the default is to record all supported resource types.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutConfigurationRecorder>`_    


    **Request Syntax** 
    ::

      response = client.put_configuration_recorder(
          ConfigurationRecorder={
              'name': 'string',
              'roleARN': 'string',
              'recordingGroup': {
                  'allSupported': True|False,
                  'includeGlobalResourceTypes': True|False,
                  'resourceTypes': [
                      'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                  ]
              }
          }
      )
    :type ConfigurationRecorder: dict
    :param ConfigurationRecorder: **[REQUIRED]** 

      The configuration recorder object that records each configuration change made to the resources.

      

    
      - **name** *(string) --* 

        The name of the recorder. By default, AWS Config automatically assigns the name "default" when creating the configuration recorder. You cannot change the assigned name.

        

      
      - **roleARN** *(string) --* 

        Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.

        

      
      - **recordingGroup** *(dict) --* 

        Specifies the types of AWS resource for which AWS Config records configuration changes.

        

      
        - **allSupported** *(boolean) --* 

          Specifies whether AWS Config records configuration changes for every supported type of regional resource.

           

          If you set this option to ``true`` , when AWS Config adds support for a new type of regional resource, it automatically starts recording resources of that type.

           

          If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .

          

        
        - **includeGlobalResourceTypes** *(boolean) --* 

          Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.

           

          Before you can set this option to ``true`` , you must set the ``allSupported`` option to ``true`` .

           

          If you set this option to ``true`` , when AWS Config adds support for a new type of global resource, it automatically starts recording resources of that type.

           

          The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.

          

        
        - **resourceTypes** *(list) --* 

          A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, ``AWS::EC2::Instance`` or ``AWS::CloudTrail::Trail`` ).

           

          Before you can set this option to ``true`` , you must set the ``allSupported`` option to ``false`` .

           

          If you set this option to ``true`` , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.

           

          For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in `Supported AWS Resource Types <http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__ .

          

        
          - *(string) --* 

          
      
      
    
    
    :returns: None

  .. py:method:: put_delivery_channel(**kwargs)

    

    Creates a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic.

     

    Before you can create a delivery channel, you must create a configuration recorder.

     

    You can use this action to change the Amazon S3 bucket or an Amazon SNS topic of the existing delivery channel. To change the Amazon S3 bucket or an Amazon SNS topic, call this action and specify the changed values for the S3 bucket and the SNS topic. If you specify a different value for either the S3 bucket or the SNS topic, this action will keep the existing value for the parameter that is not changed.

     

    .. note::

       

      You can have only one delivery channel per region in your account.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutDeliveryChannel>`_    


    **Request Syntax** 
    ::

      response = client.put_delivery_channel(
          DeliveryChannel={
              'name': 'string',
              's3BucketName': 'string',
              's3KeyPrefix': 'string',
              'snsTopicARN': 'string',
              'configSnapshotDeliveryProperties': {
                  'deliveryFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
              }
          }
      )
    :type DeliveryChannel: dict
    :param DeliveryChannel: **[REQUIRED]** 

      The configuration delivery channel object that delivers the configuration information to an Amazon S3 bucket, and to an Amazon SNS topic.

      

    
      - **name** *(string) --* 

        The name of the delivery channel. By default, AWS Config assigns the name "default" when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.

        

      
      - **s3BucketName** *(string) --* 

        The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.

         

        If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see `Permissions for the Amazon S3 Bucket <http://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`__ in the AWS Config Developer Guide.

        

      
      - **s3KeyPrefix** *(string) --* 

        The prefix for the specified Amazon S3 bucket.

        

      
      - **snsTopicARN** *(string) --* 

        The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.

         

        If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see `Permissions for the Amazon SNS Topic <http://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`__ in the AWS Config Developer Guide.

        

      
      - **configSnapshotDeliveryProperties** *(dict) --* 

        The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.

        

      
        - **deliveryFrequency** *(string) --* 

          The frequency with which AWS Config delivers configuration snapshots.

          

        
      
    
    
    :returns: None

  .. py:method:: put_evaluations(**kwargs)

    

    Used by an AWS Lambda function to deliver evaluation results to AWS Config. This action is required in every AWS Lambda function that is invoked by an AWS Config rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutEvaluations>`_    


    **Request Syntax** 
    ::

      response = client.put_evaluations(
          Evaluations=[
              {
                  'ComplianceResourceType': 'string',
                  'ComplianceResourceId': 'string',
                  'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                  'Annotation': 'string',
                  'OrderingTimestamp': datetime(2015, 1, 1)
              },
          ],
          ResultToken='string',
          TestMode=True|False
      )
    :type Evaluations: list
    :param Evaluations: 

      The assessments that the AWS Lambda function performs. Each evaluation identifies an AWS resource and indicates whether it complies with the AWS Config rule that invokes the AWS Lambda function.

      

    
      - *(dict) --* 

        Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.

        

      
        - **ComplianceResourceType** *(string) --* **[REQUIRED]** 

          The type of AWS resource that was evaluated.

          

        
        - **ComplianceResourceId** *(string) --* **[REQUIRED]** 

          The ID of the AWS resource that was evaluated.

          

        
        - **ComplianceType** *(string) --* **[REQUIRED]** 

          Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.

           

          For the ``Evaluation`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for this data type.

           

          Similarly, AWS Config does not accept ``INSUFFICIENT_DATA`` as the value for ``ComplianceType`` from a ``PutEvaluations`` request. For example, an AWS Lambda function for a custom Config rule cannot pass an ``INSUFFICIENT_DATA`` value to AWS Config.

          

        
        - **Annotation** *(string) --* 

          Supplementary information about how the evaluation determined the compliance.

          

        
        - **OrderingTimestamp** *(datetime) --* **[REQUIRED]** 

          The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).

          

        
      
  
    :type ResultToken: string
    :param ResultToken: **[REQUIRED]** 

      An encrypted token that associates an evaluation with an AWS Config rule. Identifies the rule and the event that triggered the evaluation

      

    
    :type TestMode: boolean
    :param TestMode: 

      Use this parameter to specify a test run for ``PutEvaluations`` . You can verify whether your AWS Lambda function will deliver evaluation results to AWS Config. No updates occur to your existing evaluations, and evaluation results are not sent to AWS Config.

       

      .. note::

         

        When ``TestMode`` is ``true`` , ``PutEvaluations`` doesn't require a valid value for the ``ResultToken`` parameter, but the value cannot be null.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FailedEvaluations': [
                {
                    'ComplianceResourceType': 'string',
                    'ComplianceResourceId': 'string',
                    'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                    'Annotation': 'string',
                    'OrderingTimestamp': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **FailedEvaluations** *(list) --* 

          Requests that failed because of a client or server error.

          
          

          - *(dict) --* 

            Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.

            
            

            - **ComplianceResourceType** *(string) --* 

              The type of AWS resource that was evaluated.

              
            

            - **ComplianceResourceId** *(string) --* 

              The ID of the AWS resource that was evaluated.

              
            

            - **ComplianceType** *(string) --* 

              Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.

               

              For the ``Evaluation`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for this data type.

               

              Similarly, AWS Config does not accept ``INSUFFICIENT_DATA`` as the value for ``ComplianceType`` from a ``PutEvaluations`` request. For example, an AWS Lambda function for a custom Config rule cannot pass an ``INSUFFICIENT_DATA`` value to AWS Config.

              
            

            - **Annotation** *(string) --* 

              Supplementary information about how the evaluation determined the compliance.

              
            

            - **OrderingTimestamp** *(datetime) --* 

              The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).

              
        
      
    

  .. py:method:: start_config_rules_evaluation(**kwargs)

    

    Runs an on-demand evaluation for the specified Config rules against the last known configuration state of the resources. Use ``StartConfigRulesEvaluation`` when you want to test a rule that you updated is working as expected. ``StartConfigRulesEvaluation`` does not re-record the latest configuration state for your resources; it re-runs an evaluation against the last known state of your resources. 

     

    You can specify up to 25 Config rules per request. 

     

    An existing ``StartConfigRulesEvaluation`` call must complete for the specified rules before you can call the API again. If you chose to have AWS Config stream to an Amazon SNS topic, you will receive a ``ConfigRuleEvaluationStarted`` notification when the evaluation starts.

     

    .. note::

       

      You don't need to call the ``StartConfigRulesEvaluation`` API to run an evaluation for a new rule. When you create a new rule, AWS Config automatically evaluates your resources against the rule. 

       

     

    The ``StartConfigRulesEvaluation`` API is useful if you want to run on-demand evaluations, such as the following example:

     

     
    * You have a custom rule that evaluates your IAM resources every 24 hours. 
     
    * You update your Lambda function to add additional conditions to your rule. 
     
    * Instead of waiting for the next periodic evaluation, you call the ``StartConfigRulesEvaluation`` API. 
     
    * AWS Config invokes your Lambda function and evaluates your IAM resources. 
     
    * Your custom rule will still run periodic evaluations every 24 hours. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/StartConfigRulesEvaluation>`_    


    **Request Syntax** 
    ::

      response = client.start_config_rules_evaluation(
          ConfigRuleNames=[
              'string',
          ]
      )
    :type ConfigRuleNames: list
    :param ConfigRuleNames: 

      The list of names of Config rules that you want to run evaluations for.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output when you start the evaluation for the specified Config rule.

        
    

  .. py:method:: start_configuration_recorder(**kwargs)

    

    Starts recording configurations of the AWS resources you have selected to record in your AWS account.

     

    You must have created at least one delivery channel to successfully start the configuration recorder.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/StartConfigurationRecorder>`_    


    **Request Syntax** 
    ::

      response = client.start_configuration_recorder(
          ConfigurationRecorderName='string'
      )
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: **[REQUIRED]** 

      The name of the recorder object that records each configuration change made to the resources.

      

    
    
    :returns: None

  .. py:method:: stop_configuration_recorder(**kwargs)

    

    Stops recording configurations of the AWS resources you have selected to record in your AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/StopConfigurationRecorder>`_    


    **Request Syntax** 
    ::

      response = client.stop_configuration_recorder(
          ConfigurationRecorderName='string'
      )
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: **[REQUIRED]** 

      The name of the recorder object that records each configuration change made to the resources.

      

    
    
    :returns: None

==========
Paginators
==========


The available paginators are:

* :py:class:`ConfigService.Paginator.DescribeComplianceByConfigRule`


* :py:class:`ConfigService.Paginator.DescribeComplianceByResource`


* :py:class:`ConfigService.Paginator.DescribeConfigRules`


* :py:class:`ConfigService.Paginator.GetComplianceDetailsByConfigRule`


* :py:class:`ConfigService.Paginator.GetComplianceDetailsByResource`


* :py:class:`ConfigService.Paginator.GetResourceConfigHistory`


* :py:class:`ConfigService.Paginator.ListDiscoveredResources`



.. py:class:: ConfigService.Paginator.DescribeComplianceByConfigRule

  ::

    
    paginator = client.get_paginator('describe_compliance_by_config_rule')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ConfigService.Client.describe_compliance_by_config_rule`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByConfigRule>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ConfigRuleNames=[
              'string',
          ],
          ComplianceTypes=[
              'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ConfigRuleNames: list
    :param ConfigRuleNames: 

      Specify one or more AWS Config rule names to filter the results by rule.

      

    
      - *(string) --* 

      
  
    :type ComplianceTypes: list
    :param ComplianceTypes: 

      Filters the results by compliance.

       

      The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` .

      

    
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
            'ComplianceByConfigRules': [
                {
                    'ConfigRuleName': 'string',
                    'Compliance': {
                        'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                        'ComplianceContributorCount': {
                            'CappedCount': 123,
                            'CapExceeded': True|False
                        }
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ComplianceByConfigRules** *(list) --* 

          Indicates whether each of the specified AWS Config rules is compliant.

          
          

          - *(dict) --* 

            Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the resources that the rule evaluated comply with it, and it is noncompliant if any of these resources do not comply.

            
            

            - **ConfigRuleName** *(string) --* 

              The name of the AWS Config rule.

              
            

            - **Compliance** *(dict) --* 

              Indicates whether the AWS Config rule is compliant.

              
              

              - **ComplianceType** *(string) --* 

                Indicates whether an AWS resource or AWS Config rule is compliant.

                 

                A resource is compliant if it complies with all of the AWS Config rules that evaluate it, and it is noncompliant if it does not comply with one or more of these rules.

                 

                A rule is compliant if all of the resources that the rule evaluates comply with it, and it is noncompliant if any of these resources do not comply.

                 

                AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or Config rule.

                 

                For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

                
              

              - **ComplianceContributorCount** *(dict) --* 

                The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.

                
                

                - **CappedCount** *(integer) --* 

                  The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

                  
                

                - **CapExceeded** *(boolean) --* 

                  Indicates whether the maximum count is reached.

                  
            
          
        
      
    

.. py:class:: ConfigService.Paginator.DescribeComplianceByResource

  ::

    
    paginator = client.get_paginator('describe_compliance_by_resource')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ConfigService.Client.describe_compliance_by_resource`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByResource>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ResourceType='string',
          ResourceId='string',
          ComplianceTypes=[
              'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
          ],
          Limit=123,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ResourceType: string
    :param ResourceType: 

      The types of AWS resources for which you want compliance information; for example, ``AWS::EC2::Instance`` . For this action, you can specify that the resource type is an AWS account by specifying ``AWS::::Account`` .

      

    
    :type ResourceId: string
    :param ResourceId: 

      The ID of the AWS resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for ``ResourceType`` .

      

    
    :type ComplianceTypes: list
    :param ComplianceTypes: 

      Filters the results by compliance.

       

      The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` .

      

    
      - *(string) --* 

      
  
    :type Limit: integer
    :param Limit: 

      The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.

      

    
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
            'ComplianceByResources': [
                {
                    'ResourceType': 'string',
                    'ResourceId': 'string',
                    'Compliance': {
                        'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                        'ComplianceContributorCount': {
                            'CappedCount': 123,
                            'CapExceeded': True|False
                        }
                    }
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ComplianceByResources** *(list) --* 

          Indicates whether the specified AWS resource complies with all of the AWS Config rules that evaluate it.

          
          

          - *(dict) --* 

            Indicates whether an AWS resource that is evaluated according to one or more AWS Config rules is compliant. A resource is compliant if it complies with all of the rules that evaluate it, and it is noncompliant if it does not comply with one or more of these rules.

            
            

            - **ResourceType** *(string) --* 

              The type of the AWS resource that was evaluated.

              
            

            - **ResourceId** *(string) --* 

              The ID of the AWS resource that was evaluated.

              
            

            - **Compliance** *(dict) --* 

              Indicates whether the AWS resource complies with all of the AWS Config rules that evaluated it.

              
              

              - **ComplianceType** *(string) --* 

                Indicates whether an AWS resource or AWS Config rule is compliant.

                 

                A resource is compliant if it complies with all of the AWS Config rules that evaluate it, and it is noncompliant if it does not comply with one or more of these rules.

                 

                A rule is compliant if all of the resources that the rule evaluates comply with it, and it is noncompliant if any of these resources do not comply.

                 

                AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or Config rule.

                 

                For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

                
              

              - **ComplianceContributorCount** *(dict) --* 

                The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.

                
                

                - **CappedCount** *(integer) --* 

                  The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

                  
                

                - **CapExceeded** *(boolean) --* 

                  Indicates whether the maximum count is reached.

                  
            
          
        
      
    

.. py:class:: ConfigService.Paginator.DescribeConfigRules

  ::

    
    paginator = client.get_paginator('describe_config_rules')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ConfigService.Client.describe_config_rules`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRules>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ConfigRuleNames=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ConfigRuleNames: list
    :param ConfigRuleNames: 

      The names of the AWS Config rules for which you want details. If you do not specify any names, AWS Config returns details for all your rules.

      

    
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
            'ConfigRules': [
                {
                    'ConfigRuleName': 'string',
                    'ConfigRuleArn': 'string',
                    'ConfigRuleId': 'string',
                    'Description': 'string',
                    'Scope': {
                        'ComplianceResourceTypes': [
                            'string',
                        ],
                        'TagKey': 'string',
                        'TagValue': 'string',
                        'ComplianceResourceId': 'string'
                    },
                    'Source': {
                        'Owner': 'CUSTOM_LAMBDA'|'AWS',
                        'SourceIdentifier': 'string',
                        'SourceDetails': [
                            {
                                'EventSource': 'aws.config',
                                'MessageType': 'ConfigurationItemChangeNotification'|'ConfigurationSnapshotDeliveryCompleted'|'ScheduledNotification'|'OversizedConfigurationItemChangeNotification',
                                'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                            },
                        ]
                    },
                    'InputParameters': 'string',
                    'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                    'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ConfigRules** *(list) --* 

          The details about your AWS Config rules.

          
          

          - *(dict) --* 

            An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a predefined function for an AWS managed rule. The function evaluates configuration items to assess whether your AWS resources comply with your desired configurations. This function can run when AWS Config detects a configuration change to an AWS resource and at a periodic frequency that you choose (for example, every 24 hours).

             

            .. note::

               

              You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

               

             

            For more information about developing and using AWS Config rules, see `Evaluating AWS Resource Configurations with AWS Config <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the *AWS Config Developer Guide* .

            
            

            - **ConfigRuleName** *(string) --* 

              The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.

              
            

            - **ConfigRuleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the AWS Config rule.

              
            

            - **ConfigRuleId** *(string) --* 

              The ID of the AWS Config rule.

              
            

            - **Description** *(string) --* 

              The description that you provide for the AWS Config rule.

              
            

            - **Scope** *(dict) --* 

              Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.

              
              

              - **ComplianceResourceTypes** *(list) --* 

                The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .

                
                

                - *(string) --* 
            
              

              - **TagKey** *(string) --* 

                The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.

                
              

              - **TagValue** *(string) --* 

                The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .

                
              

              - **ComplianceResourceId** *(string) --* 

                The IDs of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .

                
          
            

            - **Source** *(dict) --* 

              Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.

              
              

              - **Owner** *(string) --* 

                Indicates whether AWS or the customer owns and manages the AWS Config rule.

                
              

              - **SourceIdentifier** *(string) --* 

                For AWS Config managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Managed Config Rules <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__ .

                 

                For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

                
              

              - **SourceDetails** *(list) --* 

                Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.

                
                

                - *(dict) --* 

                  Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for ``SourceDetail`` only for custom rules. 

                  
                  

                  - **EventSource** *(string) --* 

                    The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.

                    
                  

                  - **MessageType** *(string) --* 

                    The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:

                     

                     
                    * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. 
                     
                    * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. 
                     
                    * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` . 
                     
                    * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot. 
                     

                     

                    If you want your custom rule to be triggered by configuration changes, specify both ``ConfigurationItemChangeNotification`` and ``OversizedConfigurationItemChangeNotification`` . 

                    
                  

                  - **MaximumExecutionFrequency** *(string) --* 

                    The frequency that you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value.

                     

                    .. note::

                       

                      By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

                       

                    
              
            
          
            

            - **InputParameters** *(string) --* 

              A string in JSON format that is passed to the AWS Config rule Lambda function.

              
            

            - **MaximumExecutionFrequency** *(string) --* 

              The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when:

               

               
              * You are using an AWS managed rule that is triggered at a periodic frequency. 
               
              * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties . 
               

               

              .. note::

                 

                By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

                 

              
            

            - **ConfigRuleState** *(string) --* 

              Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the Config rule.

               

              AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the ``StartConfigRulesEvaluation`` request to evaluate your resources against the Config rule.

               

              AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use the ``DeleteEvaluationResults`` request to delete the current evaluation results for the Config rule.

               

              AWS Config sets the state of a rule to ``DELETING`` temporarily after you use the ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.

              
        
      
    

.. py:class:: ConfigService.Paginator.GetComplianceDetailsByConfigRule

  ::

    
    paginator = client.get_paginator('get_compliance_details_by_config_rule')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ConfigService.Client.get_compliance_details_by_config_rule`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByConfigRule>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ConfigRuleName='string',
          ComplianceTypes=[
              'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
          ],
          Limit=123,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ConfigRuleName: string
    :param ConfigRuleName: **[REQUIRED]** 

      The name of the AWS Config rule for which you want compliance information.

      

    
    :type ComplianceTypes: list
    :param ComplianceTypes: 

      Filters the results by compliance.

       

      The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .

      

    
      - *(string) --* 

      
  
    :type Limit: integer
    :param Limit: 

      The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.

      

    
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
            'EvaluationResults': [
                {
                    'EvaluationResultIdentifier': {
                        'EvaluationResultQualifier': {
                            'ConfigRuleName': 'string',
                            'ResourceType': 'string',
                            'ResourceId': 'string'
                        },
                        'OrderingTimestamp': datetime(2015, 1, 1)
                    },
                    'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                    'ResultRecordedTime': datetime(2015, 1, 1),
                    'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                    'Annotation': 'string',
                    'ResultToken': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **EvaluationResults** *(list) --* 

          Indicates whether the AWS resource complies with the specified AWS Config rule.

          
          

          - *(dict) --* 

            The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related timestamps, and supplementary information.

            
            

            - **EvaluationResultIdentifier** *(dict) --* 

              Uniquely identifies the evaluation result.

              
              

              - **EvaluationResultQualifier** *(dict) --* 

                Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.

                
                

                - **ConfigRuleName** *(string) --* 

                  The name of the AWS Config rule that was used in the evaluation.

                  
                

                - **ResourceType** *(string) --* 

                  The type of AWS resource that was evaluated.

                  
                

                - **ResourceId** *(string) --* 

                  The ID of the evaluated AWS resource.

                  
            
              

              - **OrderingTimestamp** *(datetime) --* 

                The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.

                
          
            

            - **ComplianceType** *(string) --* 

              Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

               

              For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

              
            

            - **ResultRecordedTime** *(datetime) --* 

              The time when AWS Config recorded the evaluation result.

              
            

            - **ConfigRuleInvokedTime** *(datetime) --* 

              The time when the AWS Config rule evaluated the AWS resource.

              
            

            - **Annotation** *(string) --* 

              Supplementary information about how the evaluation determined the compliance.

              
            

            - **ResultToken** *(string) --* 

              An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.

              
        
      
    

.. py:class:: ConfigService.Paginator.GetComplianceDetailsByResource

  ::

    
    paginator = client.get_paginator('get_compliance_details_by_resource')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ConfigService.Client.get_compliance_details_by_resource`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByResource>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ResourceType='string',
          ResourceId='string',
          ComplianceTypes=[
              'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of the AWS resource for which you want compliance information.

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The ID of the AWS resource for which you want compliance information.

      

    
    :type ComplianceTypes: list
    :param ComplianceTypes: 

      Filters the results by compliance.

       

      The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .

      

    
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
            'EvaluationResults': [
                {
                    'EvaluationResultIdentifier': {
                        'EvaluationResultQualifier': {
                            'ConfigRuleName': 'string',
                            'ResourceType': 'string',
                            'ResourceId': 'string'
                        },
                        'OrderingTimestamp': datetime(2015, 1, 1)
                    },
                    'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                    'ResultRecordedTime': datetime(2015, 1, 1),
                    'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                    'Annotation': 'string',
                    'ResultToken': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **EvaluationResults** *(list) --* 

          Indicates whether the specified AWS resource complies each AWS Config rule.

          
          

          - *(dict) --* 

            The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related timestamps, and supplementary information.

            
            

            - **EvaluationResultIdentifier** *(dict) --* 

              Uniquely identifies the evaluation result.

              
              

              - **EvaluationResultQualifier** *(dict) --* 

                Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.

                
                

                - **ConfigRuleName** *(string) --* 

                  The name of the AWS Config rule that was used in the evaluation.

                  
                

                - **ResourceType** *(string) --* 

                  The type of AWS resource that was evaluated.

                  
                

                - **ResourceId** *(string) --* 

                  The ID of the evaluated AWS resource.

                  
            
              

              - **OrderingTimestamp** *(datetime) --* 

                The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.

                
          
            

            - **ComplianceType** *(string) --* 

              Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

               

              For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

              
            

            - **ResultRecordedTime** *(datetime) --* 

              The time when AWS Config recorded the evaluation result.

              
            

            - **ConfigRuleInvokedTime** *(datetime) --* 

              The time when the AWS Config rule evaluated the AWS resource.

              
            

            - **Annotation** *(string) --* 

              Supplementary information about how the evaluation determined the compliance.

              
            

            - **ResultToken** *(string) --* 

              An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.

              
        
      
    

.. py:class:: ConfigService.Paginator.GetResourceConfigHistory

  ::

    
    paginator = client.get_paginator('get_resource_config_history')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ConfigService.Client.get_resource_config_history`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetResourceConfigHistory>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
          resourceId='string',
          laterTime=datetime(2015, 1, 1),
          earlierTime=datetime(2015, 1, 1),
          chronologicalOrder='Reverse'|'Forward',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type resourceType: string
    :param resourceType: **[REQUIRED]** 

      The resource type.

      

    
    :type resourceId: string
    :param resourceId: **[REQUIRED]** 

      The ID of the resource (for example., ``sg-xxxxxx`` ).

      

    
    :type laterTime: datetime
    :param laterTime: 

      The time stamp that indicates a later time. If not specified, current time is taken.

      

    
    :type earlierTime: datetime
    :param earlierTime: 

      The time stamp that indicates an earlier time. If not specified, the action returns paginated results that contain configuration items that start from when the first configuration item was recorded.

      

    
    :type chronologicalOrder: string
    :param chronologicalOrder: 

      The chronological order for configuration items listed. By default the results are listed in reverse chronological order.

      

    
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
            'configurationItems': [
                {
                    'version': 'string',
                    'accountId': 'string',
                    'configurationItemCaptureTime': datetime(2015, 1, 1),
                    'configurationItemStatus': 'Ok'|'Failed'|'Discovered'|'Deleted',
                    'configurationStateId': 'string',
                    'configurationItemMD5Hash': 'string',
                    'arn': 'string',
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                    'resourceId': 'string',
                    'resourceName': 'string',
                    'awsRegion': 'string',
                    'availabilityZone': 'string',
                    'resourceCreationTime': datetime(2015, 1, 1),
                    'tags': {
                        'string': 'string'
                    },
                    'relatedEvents': [
                        'string',
                    ],
                    'relationships': [
                        {
                            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                            'resourceId': 'string',
                            'resourceName': 'string',
                            'relationshipName': 'string'
                        },
                    ],
                    'configuration': 'string',
                    'supplementaryConfiguration': {
                        'string': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the  GetResourceConfigHistory action.

        
        

        - **configurationItems** *(list) --* 

          A list that contains the configuration history of one or more resources.

          
          

          - *(dict) --* 

            A list that contains detailed configurations of a specified resource.

            
            

            - **version** *(string) --* 

              The version number of the resource configuration.

              
            

            - **accountId** *(string) --* 

              The 12 digit AWS account ID associated with the resource.

              
            

            - **configurationItemCaptureTime** *(datetime) --* 

              The time when the configuration recording was initiated.

              
            

            - **configurationItemStatus** *(string) --* 

              The configuration item status.

              
            

            - **configurationStateId** *(string) --* 

              An identifier that indicates the ordering of the configuration items of a resource.

              
            

            - **configurationItemMD5Hash** *(string) --* 

              Unique MD5 hash that represents the configuration item's state.

               

              You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the resource.

              
            

            - **resourceType** *(string) --* 

              The type of AWS resource.

              
            

            - **resourceId** *(string) --* 

              The ID of the resource (for example., ``sg-xxxxxx`` ).

              
            

            - **resourceName** *(string) --* 

              The custom name of the resource, if available.

              
            

            - **awsRegion** *(string) --* 

              The region where the resource resides.

              
            

            - **availabilityZone** *(string) --* 

              The Availability Zone associated with the resource.

              
            

            - **resourceCreationTime** *(datetime) --* 

              The time stamp when the resource was created.

              
            

            - **tags** *(dict) --* 

              A mapping of key value tags associated with the resource.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **relatedEvents** *(list) --* 

              A list of CloudTrail event IDs.

               

              A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see `What is AWS CloudTrail? <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__ .

               

              An empty field indicates that the current configuration was not initiated by any event.

              
              

              - *(string) --* 
          
            

            - **relationships** *(list) --* 

              A list of related AWS resources.

              
              

              - *(dict) --* 

                The relationship of the related resource to the main resource.

                
                

                - **resourceType** *(string) --* 

                  The resource type of the related resource.

                  
                

                - **resourceId** *(string) --* 

                  The ID of the related resource (for example, ``sg-xxxxxx`` ).

                  
                

                - **resourceName** *(string) --* 

                  The custom name of the related resource, if available.

                  
                

                - **relationshipName** *(string) --* 

                  The type of relationship with the related resource.

                  
            
          
            

            - **configuration** *(string) --* 

              The description of the resource configuration.

              
            

            - **supplementaryConfiguration** *(dict) --* 

              Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the ``configuration`` parameter.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ConfigService.Paginator.ListDiscoveredResources

  ::

    
    paginator = client.get_paginator('list_discovered_resources')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ConfigService.Client.list_discovered_resources`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/ListDiscoveredResources>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
          resourceIds=[
              'string',
          ],
          resourceName='string',
          limit=123,
          includeDeletedResources=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type resourceType: string
    :param resourceType: **[REQUIRED]** 

      The type of resources that you want AWS Config to list in the response.

      

    
    :type resourceIds: list
    :param resourceIds: 

      The IDs of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.

      

    
      - *(string) --* 

      
  
    :type resourceName: string
    :param resourceName: 

      The custom name of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.

      

    
    :type includeDeletedResources: boolean
    :param includeDeletedResources: 

      Specifies whether AWS Config includes deleted resources in the results. By default, deleted resources are not included.

      

    
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
            'resourceIdentifiers': [
                {
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project',
                    'resourceId': 'string',
                    'resourceName': 'string',
                    'resourceDeletionTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **resourceIdentifiers** *(list) --* 

          The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.

          
          

          - *(dict) --* 

            The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.

            
            

            - **resourceType** *(string) --* 

              The type of resource.

              
            

            - **resourceId** *(string) --* 

              The ID of the resource (for example., ``sg-xxxxxx`` ).

              
            

            - **resourceName** *(string) --* 

              The custom name of the resource (if available).

              
            

            - **resourceDeletionTime** *(datetime) --* 

              The time that the resource was deleted.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    