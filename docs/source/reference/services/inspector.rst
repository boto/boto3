

*********
Inspector
*********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Inspector.Client

  A low-level client representing Amazon Inspector::

    
    import boto3
    
    client = boto3.client('inspector')

  
  These are the available methods:
  
  *   :py:meth:`~Inspector.Client.add_attributes_to_findings`

  
  *   :py:meth:`~Inspector.Client.can_paginate`

  
  *   :py:meth:`~Inspector.Client.create_assessment_target`

  
  *   :py:meth:`~Inspector.Client.create_assessment_template`

  
  *   :py:meth:`~Inspector.Client.create_resource_group`

  
  *   :py:meth:`~Inspector.Client.delete_assessment_run`

  
  *   :py:meth:`~Inspector.Client.delete_assessment_target`

  
  *   :py:meth:`~Inspector.Client.delete_assessment_template`

  
  *   :py:meth:`~Inspector.Client.describe_assessment_runs`

  
  *   :py:meth:`~Inspector.Client.describe_assessment_targets`

  
  *   :py:meth:`~Inspector.Client.describe_assessment_templates`

  
  *   :py:meth:`~Inspector.Client.describe_cross_account_access_role`

  
  *   :py:meth:`~Inspector.Client.describe_findings`

  
  *   :py:meth:`~Inspector.Client.describe_resource_groups`

  
  *   :py:meth:`~Inspector.Client.describe_rules_packages`

  
  *   :py:meth:`~Inspector.Client.generate_presigned_url`

  
  *   :py:meth:`~Inspector.Client.get_assessment_report`

  
  *   :py:meth:`~Inspector.Client.get_paginator`

  
  *   :py:meth:`~Inspector.Client.get_telemetry_metadata`

  
  *   :py:meth:`~Inspector.Client.get_waiter`

  
  *   :py:meth:`~Inspector.Client.list_assessment_run_agents`

  
  *   :py:meth:`~Inspector.Client.list_assessment_runs`

  
  *   :py:meth:`~Inspector.Client.list_assessment_targets`

  
  *   :py:meth:`~Inspector.Client.list_assessment_templates`

  
  *   :py:meth:`~Inspector.Client.list_event_subscriptions`

  
  *   :py:meth:`~Inspector.Client.list_findings`

  
  *   :py:meth:`~Inspector.Client.list_rules_packages`

  
  *   :py:meth:`~Inspector.Client.list_tags_for_resource`

  
  *   :py:meth:`~Inspector.Client.preview_agents`

  
  *   :py:meth:`~Inspector.Client.register_cross_account_access_role`

  
  *   :py:meth:`~Inspector.Client.remove_attributes_from_findings`

  
  *   :py:meth:`~Inspector.Client.set_tags_for_resource`

  
  *   :py:meth:`~Inspector.Client.start_assessment_run`

  
  *   :py:meth:`~Inspector.Client.stop_assessment_run`

  
  *   :py:meth:`~Inspector.Client.subscribe_to_event`

  
  *   :py:meth:`~Inspector.Client.unsubscribe_from_event`

  
  *   :py:meth:`~Inspector.Client.update_assessment_target`

  

  .. py:method:: add_attributes_to_findings(**kwargs)

    

    Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/AddAttributesToFindings>`_    


    **Request Syntax** 
    ::

      response = client.add_attributes_to_findings(
          findingArns=[
              'string',
          ],
          attributes=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type findingArns: list
    :param findingArns: **[REQUIRED]** 

      The ARNs that specify the findings that you want to assign attributes to.

      

    
      - *(string) --* 

      
  
    :type attributes: list
    :param attributes: **[REQUIRED]** 

      The array of attributes that you want to assign to specified findings.

      

    
      - *(dict) --* 

        This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The attribute key.

          

        
        - **value** *(string) --* 

          The value assigned to the attribute key.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'failedItems': {
                'string': {
                    'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                    'retryable': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **failedItems** *(dict) --* 

          Attribute details that cannot be described. An error code is provided for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Includes details about the failed items.

              
              

              - **failureCode** *(string) --* 

                The status code of a failed item.

                
              

              - **retryable** *(boolean) --* 

                Indicates whether you can immediately retry a request for this item for a specified resource.

                
          
      
    
    

    **Examples** 

    Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.
    ::

      response = client.add_attributes_to_findings(
          attributes=[
              {
                  'key': 'Example',
                  'value': 'example',
              },
          ],
          findingArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'failedItems': {
          },
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


  .. py:method:: create_assessment_target(**kwargs)

    

    Creates a new assessment target using the ARN of the resource group that is generated by  CreateResourceGroup . You can create up to 50 assessment targets per AWS account. You can run up to 500 concurrent agents per AWS account. For more information, see `Amazon Inspector Assessment Targets <http://docs.aws.amazon.com/inspector/latest/userguide/inspector_applications.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/CreateAssessmentTarget>`_    


    **Request Syntax** 
    ::

      response = client.create_assessment_target(
          assessmentTargetName='string',
          resourceGroupArn='string'
      )
    :type assessmentTargetName: string
    :param assessmentTargetName: **[REQUIRED]** 

      The user-defined name that identifies the assessment target that you want to create. The name must be unique within the AWS account.

      

    
    :type resourceGroupArn: string
    :param resourceGroupArn: **[REQUIRED]** 

      The ARN that specifies the resource group that is used to create the assessment target.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentTargetArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentTargetArn** *(string) --* 

          The ARN that specifies the assessment target that is created.

          
    

    **Examples** 

    Creates a new assessment target using the ARN of the resource group that is generated by CreateResourceGroup. You can create up to 50 assessment targets per AWS account. You can run up to 500 concurrent agents per AWS account.
    ::

      response = client.create_assessment_target(
          assessmentTargetName='ExampleAssessmentTarget',
          resourceGroupArn='arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentTargetArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_assessment_template(**kwargs)

    

    Creates an assessment template for the assessment target that is specified by the ARN of the assessment target.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/CreateAssessmentTemplate>`_    


    **Request Syntax** 
    ::

      response = client.create_assessment_template(
          assessmentTargetArn='string',
          assessmentTemplateName='string',
          durationInSeconds=123,
          rulesPackageArns=[
              'string',
          ],
          userAttributesForFindings=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type assessmentTargetArn: string
    :param assessmentTargetArn: **[REQUIRED]** 

      The ARN that specifies the assessment target for which you want to create the assessment template.

      

    
    :type assessmentTemplateName: string
    :param assessmentTemplateName: **[REQUIRED]** 

      The user-defined name that identifies the assessment template that you want to create. You can create several assessment templates for an assessment target. The names of the assessment templates that correspond to a particular assessment target must be unique.

      

    
    :type durationInSeconds: integer
    :param durationInSeconds: **[REQUIRED]** 

      The duration of the assessment run in seconds. The default value is 3600 seconds (one hour).

      

    
    :type rulesPackageArns: list
    :param rulesPackageArns: **[REQUIRED]** 

      The ARNs that specify the rules packages that you want to attach to the assessment template.

      

    
      - *(string) --* 

      
  
    :type userAttributesForFindings: list
    :param userAttributesForFindings: 

      The user-defined attributes that are assigned to every finding that is generated by the assessment run that uses this assessment template. An attribute is a key and value pair (an  Attribute object). Within an assessment template, each key must be unique.

      

    
      - *(dict) --* 

        This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The attribute key.

          

        
        - **value** *(string) --* 

          The value assigned to the attribute key.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentTemplateArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentTemplateArn** *(string) --* 

          The ARN that specifies the assessment template that is created.

          
    

    **Examples** 

    Creates an assessment template for the assessment target that is specified by the ARN of the assessment target.
    ::

      response = client.create_assessment_template(
          assessmentTargetArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX',
          assessmentTemplateName='ExampleAssessmentTemplate',
          durationInSeconds=180,
          rulesPackageArns=[
              'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-11B9DBXp',
          ],
          userAttributesForFindings=[
              {
                  'key': 'Example',
                  'value': 'example',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentTemplateArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_resource_group(**kwargs)

    

    Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target. The created resource group is then used to create an Amazon Inspector assessment target. For more information, see  CreateAssessmentTarget .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/CreateResourceGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_resource_group(
          resourceGroupTags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type resourceGroupTags: list
    :param resourceGroupTags: **[REQUIRED]** 

      A collection of keys and an array of possible values, '[{"key":"key1","values":["Value1","Value2"]},{"key":"Key2","values":["Value3"]}]'.

       

      For example,'[{"key":"Name","values":["TestEC2Instance"]}]'.

      

    
      - *(dict) --* 

        This data type is used as one of the elements of the  ResourceGroup data type.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          A tag key.

          

        
        - **value** *(string) --* 

          The value assigned to a tag key.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resourceGroupArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resourceGroupArn** *(string) --* 

          The ARN that specifies the resource group that is created.

          
    

    **Examples** 

    Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target. The created resource group is then used to create an Amazon Inspector assessment target. 
    ::

      response = client.create_resource_group(
          resourceGroupTags=[
              {
                  'key': 'Name',
                  'value': 'example',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'resourceGroupArn': 'arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_assessment_run(**kwargs)

    

    Deletes the assessment run that is specified by the ARN of the assessment run.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DeleteAssessmentRun>`_    


    **Request Syntax** 
    ::

      response = client.delete_assessment_run(
          assessmentRunArn='string'
      )
    :type assessmentRunArn: string
    :param assessmentRunArn: **[REQUIRED]** 

      The ARN that specifies the assessment run that you want to delete.

      

    
    
    :returns: None

    **Examples** 

    Deletes the assessment run that is specified by the ARN of the assessment run.
    ::

      response = client.delete_assessment_run(
          assessmentRunArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_assessment_target(**kwargs)

    

    Deletes the assessment target that is specified by the ARN of the assessment target.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DeleteAssessmentTarget>`_    


    **Request Syntax** 
    ::

      response = client.delete_assessment_target(
          assessmentTargetArn='string'
      )
    :type assessmentTargetArn: string
    :param assessmentTargetArn: **[REQUIRED]** 

      The ARN that specifies the assessment target that you want to delete.

      

    
    
    :returns: None

    **Examples** 

    Deletes the assessment target that is specified by the ARN of the assessment target.
    ::

      response = client.delete_assessment_target(
          assessmentTargetArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_assessment_template(**kwargs)

    

    Deletes the assessment template that is specified by the ARN of the assessment template.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DeleteAssessmentTemplate>`_    


    **Request Syntax** 
    ::

      response = client.delete_assessment_template(
          assessmentTemplateArn='string'
      )
    :type assessmentTemplateArn: string
    :param assessmentTemplateArn: **[REQUIRED]** 

      The ARN that specifies the assessment template that you want to delete.

      

    
    
    :returns: None

    **Examples** 

    Deletes the assessment template that is specified by the ARN of the assessment template.
    ::

      response = client.delete_assessment_template(
          assessmentTemplateArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_assessment_runs(**kwargs)

    

    Describes the assessment runs that are specified by the ARNs of the assessment runs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeAssessmentRuns>`_    


    **Request Syntax** 
    ::

      response = client.describe_assessment_runs(
          assessmentRunArns=[
              'string',
          ]
      )
    :type assessmentRunArns: list
    :param assessmentRunArns: **[REQUIRED]** 

      The ARN that specifies the assessment run that you want to describe.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentRuns': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'assessmentTemplateArn': 'string',
                    'state': 'CREATED'|'START_DATA_COLLECTION_PENDING'|'START_DATA_COLLECTION_IN_PROGRESS'|'COLLECTING_DATA'|'STOP_DATA_COLLECTION_PENDING'|'DATA_COLLECTED'|'START_EVALUATING_RULES_PENDING'|'EVALUATING_RULES'|'FAILED'|'ERROR'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'CANCELED',
                    'durationInSeconds': 123,
                    'rulesPackageArns': [
                        'string',
                    ],
                    'userAttributesForFindings': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'completedAt': datetime(2015, 1, 1),
                    'stateChangedAt': datetime(2015, 1, 1),
                    'dataCollected': True|False,
                    'stateChanges': [
                        {
                            'stateChangedAt': datetime(2015, 1, 1),
                            'state': 'CREATED'|'START_DATA_COLLECTION_PENDING'|'START_DATA_COLLECTION_IN_PROGRESS'|'COLLECTING_DATA'|'STOP_DATA_COLLECTION_PENDING'|'DATA_COLLECTED'|'START_EVALUATING_RULES_PENDING'|'EVALUATING_RULES'|'FAILED'|'ERROR'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'CANCELED'
                        },
                    ],
                    'notifications': [
                        {
                            'date': datetime(2015, 1, 1),
                            'event': 'ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
                            'message': 'string',
                            'error': True|False,
                            'snsTopicArn': 'string',
                            'snsPublishStatusCode': 'SUCCESS'|'TOPIC_DOES_NOT_EXIST'|'ACCESS_DENIED'|'INTERNAL_ERROR'
                        },
                    ],
                    'findingCounts': {
                        'string': 123
                    }
                },
            ],
            'failedItems': {
                'string': {
                    'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                    'retryable': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentRuns** *(list) --* 

          Information about the assessment run.

          
          

          - *(dict) --* 

            A snapshot of an Amazon Inspector assessment run that contains the findings of the assessment run .

             

            Used as the response element in the  DescribeAssessmentRuns action.

            
            

            - **arn** *(string) --* 

              The ARN of the assessment run.

              
            

            - **name** *(string) --* 

              The auto-generated name for the assessment run.

              
            

            - **assessmentTemplateArn** *(string) --* 

              The ARN of the assessment template that is associated with the assessment run.

              
            

            - **state** *(string) --* 

              The state of the assessment run.

              
            

            - **durationInSeconds** *(integer) --* 

              The duration of the assessment run.

              
            

            - **rulesPackageArns** *(list) --* 

              The rules packages selected for the assessment run.

              
              

              - *(string) --* 
          
            

            - **userAttributesForFindings** *(list) --* 

              The user-defined attributes that are assigned to every generated finding.

              
              

              - *(dict) --* 

                This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

                
                

                - **key** *(string) --* 

                  The attribute key.

                  
                

                - **value** *(string) --* 

                  The value assigned to the attribute key.

                  
            
          
            

            - **createdAt** *(datetime) --* 

              The time when  StartAssessmentRun was called.

              
            

            - **startedAt** *(datetime) --* 

              The time when  StartAssessmentRun was called.

              
            

            - **completedAt** *(datetime) --* 

              The assessment run completion time that corresponds to the rules packages evaluation completion time or failure.

              
            

            - **stateChangedAt** *(datetime) --* 

              The last time when the assessment run's state changed.

              
            

            - **dataCollected** *(boolean) --* 

              A Boolean value (true or false) that specifies whether the process of collecting data from the agents is completed.

              
            

            - **stateChanges** *(list) --* 

              A list of the assessment run state changes.

              
              

              - *(dict) --* 

                Used as one of the elements of the  AssessmentRun data type.

                
                

                - **stateChangedAt** *(datetime) --* 

                  The last time the assessment run state changed.

                  
                

                - **state** *(string) --* 

                  The assessment run state.

                  
            
          
            

            - **notifications** *(list) --* 

              A list of notifications for the event subscriptions. A notification about a particular generated finding is added to this list only once.

              
              

              - *(dict) --* 

                Used as one of the elements of the  AssessmentRun data type.

                
                

                - **date** *(datetime) --* 

                  The date of the notification.

                  
                

                - **event** *(string) --* 

                  The event for which a notification is sent.

                  
                

                - **message** *(string) --* 

                  The message included in the notification.

                  
                

                - **error** *(boolean) --* 

                  The Boolean value that specifies whether the notification represents an error.

                  
                

                - **snsTopicArn** *(string) --* 

                  The SNS topic to which the SNS notification is sent.

                  
                

                - **snsPublishStatusCode** *(string) --* 

                  The status code of the SNS notification.

                  
            
          
            

            - **findingCounts** *(dict) --* 

              Provides a total count of generated findings per severity.

              
              

              - *(string) --* 
                

                - *(integer) --* 
          
        
        
      
        

        - **failedItems** *(dict) --* 

          Assessment run details that cannot be described. An error code is provided for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Includes details about the failed items.

              
              

              - **failureCode** *(string) --* 

                The status code of a failed item.

                
              

              - **retryable** *(boolean) --* 

                Indicates whether you can immediately retry a request for this item for a specified resource.

                
          
      
    
    

    **Examples** 

    Describes the assessment runs that are specified by the ARNs of the assessment runs.
    ::

      response = client.describe_assessment_runs(
          assessmentRunArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentRuns': [
              {
                  'name': 'Run 1 for ExampleAssessmentTemplate',
                  'arn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
                  'assessmentTemplateArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
                  'completedAt': datetime(2016, 3, 22, 13, 58, 21, 1, 82, 1),
                  'createdAt': datetime(2016, 3, 22, 13, 56, 10, 1, 82, 1),
                  'dataCollected': True,
                  'durationInSeconds': 3600,
                  'notifications': [
                  ],
                  'rulesPackageArns': [
                      'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP',
                  ],
                  'startedAt': datetime(2016, 3, 22, 13, 56, 10, 1, 82, 1),
                  'state': 'COMPLETED',
                  'stateChangedAt': datetime(2016, 3, 22, 13, 58, 21, 1, 82, 1),
                  'stateChanges': [
                      {
                          'state': 'CREATED',
                          'stateChangedAt': datetime(2016, 3, 22, 13, 56, 10, 1, 82, 1),
                      },
                      {
                          'state': 'START_DATA_COLLECTION_PENDING',
                          'stateChangedAt': datetime(2016, 3, 22, 13, 56, 10, 1, 82, 1),
                      },
                      {
                          'state': 'START_DATA_COLLECTION_IN_PROGRESS',
                          'stateChangedAt': datetime(2016, 3, 22, 13, 56, 10, 1, 82, 1),
                      },
                      {
                          'state': 'COLLECTING_DATA',
                          'stateChangedAt': datetime(2016, 3, 22, 13, 56, 10, 1, 82, 1),
                      },
                      {
                          'state': 'STOP_DATA_COLLECTION_PENDING',
                          'stateChangedAt': datetime(2016, 3, 22, 13, 57, 19, 1, 82, 1),
                      },
                      {
                          'state': 'DATA_COLLECTED',
                          'stateChangedAt': datetime(2016, 3, 22, 13, 58, 19, 1, 82, 1),
                      },
                      {
                          'state': 'EVALUATING_RULES',
                          'stateChangedAt': datetime(2016, 3, 22, 13, 58, 20, 1, 82, 1),
                      },
                      {
                          'state': 'COMPLETED',
                          'stateChangedAt': datetime(2016, 3, 22, 13, 58, 21, 1, 82, 1),
                      },
                  ],
                  'userAttributesForFindings': [
                  ],
              },
          ],
          'failedItems': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_assessment_targets(**kwargs)

    

    Describes the assessment targets that are specified by the ARNs of the assessment targets.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeAssessmentTargets>`_    


    **Request Syntax** 
    ::

      response = client.describe_assessment_targets(
          assessmentTargetArns=[
              'string',
          ]
      )
    :type assessmentTargetArns: list
    :param assessmentTargetArns: **[REQUIRED]** 

      The ARNs that specifies the assessment targets that you want to describe.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentTargets': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'resourceGroupArn': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1)
                },
            ],
            'failedItems': {
                'string': {
                    'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                    'retryable': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentTargets** *(list) --* 

          Information about the assessment targets.

          
          

          - *(dict) --* 

            Contains information about an Amazon Inspector application. This data type is used as the response element in the  DescribeAssessmentTargets action.

            
            

            - **arn** *(string) --* 

              The ARN that specifies the Amazon Inspector assessment target.

              
            

            - **name** *(string) --* 

              The name of the Amazon Inspector assessment target.

              
            

            - **resourceGroupArn** *(string) --* 

              The ARN that specifies the resource group that is associated with the assessment target.

              
            

            - **createdAt** *(datetime) --* 

              The time at which the assessment target is created.

              
            

            - **updatedAt** *(datetime) --* 

              The time at which  UpdateAssessmentTarget is called.

              
        
      
        

        - **failedItems** *(dict) --* 

          Assessment target details that cannot be described. An error code is provided for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Includes details about the failed items.

              
              

              - **failureCode** *(string) --* 

                The status code of a failed item.

                
              

              - **retryable** *(boolean) --* 

                Indicates whether you can immediately retry a request for this item for a specified resource.

                
          
      
    
    

    **Examples** 

    Describes the assessment targets that are specified by the ARNs of the assessment targets.
    ::

      response = client.describe_assessment_targets(
          assessmentTargetArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentTargets': [
              {
                  'name': 'ExampleAssessmentTarget',
                  'arn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
                  'createdAt': datetime(2016, 3, 15, 13, 36, 31, 1, 75, 1),
                  'resourceGroupArn': 'arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI',
                  'updatedAt': datetime(2016, 3, 15, 13, 36, 31, 1, 75, 1),
              },
          ],
          'failedItems': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_assessment_templates(**kwargs)

    

    Describes the assessment templates that are specified by the ARNs of the assessment templates.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeAssessmentTemplates>`_    


    **Request Syntax** 
    ::

      response = client.describe_assessment_templates(
          assessmentTemplateArns=[
              'string',
          ]
      )
    :type assessmentTemplateArns: list
    :param assessmentTemplateArns: **[REQUIRED]** 

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentTemplates': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'assessmentTargetArn': 'string',
                    'durationInSeconds': 123,
                    'rulesPackageArns': [
                        'string',
                    ],
                    'userAttributesForFindings': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1)
                },
            ],
            'failedItems': {
                'string': {
                    'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                    'retryable': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentTemplates** *(list) --* 

          Information about the assessment templates.

          
          

          - *(dict) --* 

            Contains information about an Amazon Inspector assessment template. This data type is used as the response element in the  DescribeAssessmentTemplates action.

            
            

            - **arn** *(string) --* 

              The ARN of the assessment template.

              
            

            - **name** *(string) --* 

              The name of the assessment template.

              
            

            - **assessmentTargetArn** *(string) --* 

              The ARN of the assessment target that corresponds to this assessment template.

              
            

            - **durationInSeconds** *(integer) --* 

              The duration in seconds specified for this assessment tempate. The default value is 3600 seconds (one hour). The maximum value is 86400 seconds (one day).

              
            

            - **rulesPackageArns** *(list) --* 

              The rules packages that are specified for this assessment template.

              
              

              - *(string) --* 
          
            

            - **userAttributesForFindings** *(list) --* 

              The user-defined attributes that are assigned to every generated finding from the assessment run that uses this assessment template.

              
              

              - *(dict) --* 

                This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

                
                

                - **key** *(string) --* 

                  The attribute key.

                  
                

                - **value** *(string) --* 

                  The value assigned to the attribute key.

                  
            
          
            

            - **createdAt** *(datetime) --* 

              The time at which the assessment template is created.

              
        
      
        

        - **failedItems** *(dict) --* 

          Assessment template details that cannot be described. An error code is provided for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Includes details about the failed items.

              
              

              - **failureCode** *(string) --* 

                The status code of a failed item.

                
              

              - **retryable** *(boolean) --* 

                Indicates whether you can immediately retry a request for this item for a specified resource.

                
          
      
    
    

    **Examples** 

    Describes the assessment templates that are specified by the ARNs of the assessment templates.
    ::

      response = client.describe_assessment_templates(
          assessmentTemplateArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentTemplates': [
              {
                  'name': 'ExampleAssessmentTemplate',
                  'arn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
                  'assessmentTargetArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
                  'createdAt': datetime(2016, 3, 15, 13, 36, 31, 1, 75, 1),
                  'durationInSeconds': 3600,
                  'rulesPackageArns': [
                      'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP',
                  ],
                  'userAttributesForFindings': [
                  ],
              },
          ],
          'failedItems': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_cross_account_access_role()

    

    Describes the IAM role that enables Amazon Inspector to access your AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeCrossAccountAccessRole>`_    


    **Request Syntax** 

    ::

      response = client.describe_cross_account_access_role()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'roleArn': 'string',
            'valid': True|False,
            'registeredAt': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **roleArn** *(string) --* 

          The ARN that specifies the IAM role that Amazon Inspector uses to access your AWS account.

          
        

        - **valid** *(boolean) --* 

          A Boolean value that specifies whether the IAM role has the necessary policies attached to enable Amazon Inspector to access your AWS account.

          
        

        - **registeredAt** *(datetime) --* 

          The date when the cross-account access role was registered.

          
    

    **Examples** 

    Describes the IAM role that enables Amazon Inspector to access your AWS account.
    ::

      response = client.describe_cross_account_access_role(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'registeredAt': datetime(2016, 3, 15, 12, 13, 2, 1, 75, 1),
          'roleArn': 'arn:aws:iam::123456789012:role/inspector',
          'valid': True,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_findings(**kwargs)

    

    Describes the findings that are specified by the ARNs of the findings.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeFindings>`_    


    **Request Syntax** 
    ::

      response = client.describe_findings(
          findingArns=[
              'string',
          ],
          locale='EN_US'
      )
    :type findingArns: list
    :param findingArns: **[REQUIRED]** 

      The ARN that specifies the finding that you want to describe.

      

    
      - *(string) --* 

      
  
    :type locale: string
    :param locale: 

      The locale into which you want to translate a finding description, recommendation, and the short description that identifies the finding.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'findings': [
                {
                    'arn': 'string',
                    'schemaVersion': 123,
                    'service': 'string',
                    'serviceAttributes': {
                        'schemaVersion': 123,
                        'assessmentRunArn': 'string',
                        'rulesPackageArn': 'string'
                    },
                    'assetType': 'ec2-instance',
                    'assetAttributes': {
                        'schemaVersion': 123,
                        'agentId': 'string',
                        'autoScalingGroup': 'string',
                        'amiId': 'string',
                        'hostname': 'string',
                        'ipv4Addresses': [
                            'string',
                        ]
                    },
                    'id': 'string',
                    'title': 'string',
                    'description': 'string',
                    'recommendation': 'string',
                    'severity': 'Low'|'Medium'|'High'|'Informational'|'Undefined',
                    'numericSeverity': 123.0,
                    'confidence': 123,
                    'indicatorOfCompromise': True|False,
                    'attributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'userAttributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1)
                },
            ],
            'failedItems': {
                'string': {
                    'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                    'retryable': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **findings** *(list) --* 

          Information about the finding.

          
          

          - *(dict) --* 

            Contains information about an Amazon Inspector finding. This data type is used as the response element in the  DescribeFindings action.

            
            

            - **arn** *(string) --* 

              The ARN that specifies the finding.

              
            

            - **schemaVersion** *(integer) --* 

              The schema version of this data type.

              
            

            - **service** *(string) --* 

              The data element is set to "Inspector".

              
            

            - **serviceAttributes** *(dict) --* 

              This data type is used in the  Finding data type.

              
              

              - **schemaVersion** *(integer) --* 

                The schema version of this data type.

                
              

              - **assessmentRunArn** *(string) --* 

                The ARN of the assessment run during which the finding is generated.

                
              

              - **rulesPackageArn** *(string) --* 

                The ARN of the rules package that is used to generate the finding.

                
          
            

            - **assetType** *(string) --* 

              The type of the host from which the finding is generated.

              
            

            - **assetAttributes** *(dict) --* 

              A collection of attributes of the host from which the finding is generated.

              
              

              - **schemaVersion** *(integer) --* 

                The schema version of this data type.

                
              

              - **agentId** *(string) --* 

                The ID of the agent that is installed on the EC2 instance where the finding is generated.

                
              

              - **autoScalingGroup** *(string) --* 

                The Auto Scaling group of the EC2 instance where the finding is generated.

                
              

              - **amiId** *(string) --* 

                The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where the finding is generated.

                
              

              - **hostname** *(string) --* 

                The hostname of the EC2 instance where the finding is generated.

                
              

              - **ipv4Addresses** *(list) --* 

                The list of IP v4 addresses of the EC2 instance where the finding is generated.

                
                

                - *(string) --* 
            
          
            

            - **id** *(string) --* 

              The ID of the finding.

              
            

            - **title** *(string) --* 

              The name of the finding.

              
            

            - **description** *(string) --* 

              The description of the finding.

              
            

            - **recommendation** *(string) --* 

              The recommendation for the finding.

              
            

            - **severity** *(string) --* 

              The finding severity. Values can be set to High, Medium, Low, and Informational.

              
            

            - **numericSeverity** *(float) --* 

              The numeric value of the finding severity.

              
            

            - **confidence** *(integer) --* 

              This data element is currently not used.

              
            

            - **indicatorOfCompromise** *(boolean) --* 

              This data element is currently not used.

              
            

            - **attributes** *(list) --* 

              The system-defined attributes for the finding.

              
              

              - *(dict) --* 

                This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

                
                

                - **key** *(string) --* 

                  The attribute key.

                  
                

                - **value** *(string) --* 

                  The value assigned to the attribute key.

                  
            
          
            

            - **userAttributes** *(list) --* 

              The user-defined attributes that are assigned to the finding.

              
              

              - *(dict) --* 

                This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

                
                

                - **key** *(string) --* 

                  The attribute key.

                  
                

                - **value** *(string) --* 

                  The value assigned to the attribute key.

                  
            
          
            

            - **createdAt** *(datetime) --* 

              The time when the finding was generated.

              
            

            - **updatedAt** *(datetime) --* 

              The time when  AddAttributesToFindings is called.

              
        
      
        

        - **failedItems** *(dict) --* 

          Finding details that cannot be described. An error code is provided for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Includes details about the failed items.

              
              

              - **failureCode** *(string) --* 

                The status code of a failed item.

                
              

              - **retryable** *(boolean) --* 

                Indicates whether you can immediately retry a request for this item for a specified resource.

                
          
      
    
    

    **Examples** 

    Describes the findings that are specified by the ARNs of the findings.
    ::

      response = client.describe_findings(
          findingArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'failedItems': {
          },
          'findings': [
              {
                  'arn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4',
                  'assetAttributes': {
                      'ipv4Addresses': [
                      ],
                      'schemaVersion': 1,
                  },
                  'assetType': 'ec2-instance',
                  'attributes': [
                  ],
                  'confidence': 10,
                  'createdAt': datetime(2016, 3, 22, 13, 58, 21, 1, 82, 1),
                  'description': 'Amazon Inspector did not find any potential security issues during this assessment.',
                  'indicatorOfCompromise': False,
                  'numericSeverity': 0,
                  'recommendation': 'No remediation needed.',
                  'schemaVersion': 1,
                  'service': 'Inspector',
                  'serviceAttributes': {
                      'assessmentRunArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
                      'rulesPackageArn': 'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP',
                      'schemaVersion': 1,
                  },
                  'severity': 'Informational',
                  'title': 'No potential security issues found',
                  'updatedAt': datetime(2016, 3, 22, 13, 58, 21, 1, 82, 1),
                  'userAttributes': [
                  ],
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_resource_groups(**kwargs)

    

    Describes the resource groups that are specified by the ARNs of the resource groups.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeResourceGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_resource_groups(
          resourceGroupArns=[
              'string',
          ]
      )
    :type resourceGroupArns: list
    :param resourceGroupArns: **[REQUIRED]** 

      The ARN that specifies the resource group that you want to describe.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resourceGroups': [
                {
                    'arn': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1)
                },
            ],
            'failedItems': {
                'string': {
                    'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                    'retryable': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resourceGroups** *(list) --* 

          Information about a resource group.

          
          

          - *(dict) --* 

            Contains information about a resource group. The resource group defines a set of tags that, when queried, identify the AWS resources that make up the assessment target. This data type is used as the response element in the  DescribeResourceGroups action.

            
            

            - **arn** *(string) --* 

              The ARN of the resource group.

              
            

            - **tags** *(list) --* 

              The tags (key and value pairs) of the resource group. This data type property is used in the  CreateResourceGroup action.

              
              

              - *(dict) --* 

                This data type is used as one of the elements of the  ResourceGroup data type.

                
                

                - **key** *(string) --* 

                  A tag key.

                  
                

                - **value** *(string) --* 

                  The value assigned to a tag key.

                  
            
          
            

            - **createdAt** *(datetime) --* 

              The time at which resource group is created.

              
        
      
        

        - **failedItems** *(dict) --* 

          Resource group details that cannot be described. An error code is provided for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Includes details about the failed items.

              
              

              - **failureCode** *(string) --* 

                The status code of a failed item.

                
              

              - **retryable** *(boolean) --* 

                Indicates whether you can immediately retry a request for this item for a specified resource.

                
          
      
    
    

    **Examples** 

    Describes the resource groups that are specified by the ARNs of the resource groups.
    ::

      response = client.describe_resource_groups(
          resourceGroupArns=[
              'arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'failedItems': {
          },
          'resourceGroups': [
              {
                  'arn': 'arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI',
                  'createdAt': datetime(2016, 3, 15, 13, 36, 31, 1, 75, 1),
                  'tags': [
                      {
                          'key': 'Name',
                          'value': 'example',
                      },
                  ],
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_rules_packages(**kwargs)

    

    Describes the rules packages that are specified by the ARNs of the rules packages.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeRulesPackages>`_    


    **Request Syntax** 
    ::

      response = client.describe_rules_packages(
          rulesPackageArns=[
              'string',
          ],
          locale='EN_US'
      )
    :type rulesPackageArns: list
    :param rulesPackageArns: **[REQUIRED]** 

      The ARN that specifies the rules package that you want to describe.

      

    
      - *(string) --* 

      
  
    :type locale: string
    :param locale: 

      The locale that you want to translate a rules package description into.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'rulesPackages': [
                {
                    'arn': 'string',
                    'name': 'string',
                    'version': 'string',
                    'provider': 'string',
                    'description': 'string'
                },
            ],
            'failedItems': {
                'string': {
                    'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                    'retryable': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **rulesPackages** *(list) --* 

          Information about the rules package.

          
          

          - *(dict) --* 

            Contains information about an Amazon Inspector rules package. This data type is used as the response element in the  DescribeRulesPackages action.

            
            

            - **arn** *(string) --* 

              The ARN of the rules package.

              
            

            - **name** *(string) --* 

              The name of the rules package.

              
            

            - **version** *(string) --* 

              The version ID of the rules package.

              
            

            - **provider** *(string) --* 

              The provider of the rules package.

              
            

            - **description** *(string) --* 

              The description of the rules package.

              
        
      
        

        - **failedItems** *(dict) --* 

          Rules package details that cannot be described. An error code is provided for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Includes details about the failed items.

              
              

              - **failureCode** *(string) --* 

                The status code of a failed item.

                
              

              - **retryable** *(boolean) --* 

                Indicates whether you can immediately retry a request for this item for a specified resource.

                
          
      
    
    

    **Examples** 

    Describes the rules packages that are specified by the ARNs of the rules packages.
    ::

      response = client.describe_rules_packages(
          rulesPackageArns=[
              'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'failedItems': {
          },
          'rulesPackages': [
              {
                  'version': '1.1',
                  'name': 'Security Best Practices',
                  'arn': 'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ',
                  'description': 'The rules in this package help determine whether your systems are configured securely.',
                  'provider': 'Amazon Web Services, Inc.',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

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


  .. py:method:: get_assessment_report(**kwargs)

    

    Produces an assessment report that includes detailed and comprehensive results of a specified assessment run. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/GetAssessmentReport>`_    


    **Request Syntax** 
    ::

      response = client.get_assessment_report(
          assessmentRunArn='string',
          reportFileFormat='HTML'|'PDF',
          reportType='FINDING'|'FULL'
      )
    :type assessmentRunArn: string
    :param assessmentRunArn: **[REQUIRED]** 

      The ARN that specifies the assessment run for which you want to generate a report.

      

    
    :type reportFileFormat: string
    :param reportFileFormat: **[REQUIRED]** 

      Specifies the file format (html or pdf) of the assessment report that you want to generate.

      

    
    :type reportType: string
    :param reportType: **[REQUIRED]** 

      Specifies the type of the assessment report that you want to generate. There are two types of assessment reports: a finding report and a full report. For more information, see `Assessment Reports <http://docs.aws.amazon.com/inspector/latest/userguide/inspector_reports.html>`__ . 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'status': 'WORK_IN_PROGRESS'|'FAILED'|'COMPLETED',
            'url': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **status** *(string) --* 

          Specifies the status of the request to generate an assessment report. 

          
        

        - **url** *(string) --* 

          Specifies the URL where you can find the generated assessment report. This parameter is only returned if the report is successfully generated.

          
    

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


  .. py:method:: get_telemetry_metadata(**kwargs)

    

    Information about the data that is collected for the specified assessment run.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/GetTelemetryMetadata>`_    


    **Request Syntax** 
    ::

      response = client.get_telemetry_metadata(
          assessmentRunArn='string'
      )
    :type assessmentRunArn: string
    :param assessmentRunArn: **[REQUIRED]** 

      The ARN that specifies the assessment run that has the telemetry data that you want to obtain.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'telemetryMetadata': [
                {
                    'messageType': 'string',
                    'count': 123,
                    'dataSize': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **telemetryMetadata** *(list) --* 

          Telemetry details.

          
          

          - *(dict) --* 

            The metadata about the Amazon Inspector application data metrics collected by the agent. This data type is used as the response element in the  GetTelemetryMetadata action.

            
            

            - **messageType** *(string) --* 

              A specific type of behavioral data that is collected by the agent.

              
            

            - **count** *(integer) --* 

              The count of messages that the agent sends to the Amazon Inspector service.

              
            

            - **dataSize** *(integer) --* 

              The data size of messages that the agent sends to the Amazon Inspector service.

              
        
      
    

    **Examples** 

    Information about the data that is collected for the specified assessment run.
    ::

      response = client.get_telemetry_metadata(
          assessmentRunArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'telemetryMetadata': [
              {
                  'count': 2,
                  'dataSize': 345,
                  'messageType': 'InspectorDuplicateProcess',
              },
              {
                  'count': 3,
                  'dataSize': 255,
                  'messageType': 'InspectorTimeEventMsg',
              },
              {
                  'count': 4,
                  'dataSize': 1082,
                  'messageType': 'InspectorNetworkInterface',
              },
              {
                  'count': 2,
                  'dataSize': 349,
                  'messageType': 'InspectorDnsEntry',
              },
              {
                  'count': 11,
                  'dataSize': 2514,
                  'messageType': 'InspectorDirectoryInfoMsg',
              },
              {
                  'count': 1,
                  'dataSize': 179,
                  'messageType': 'InspectorTcpV6ListeningPort',
              },
              {
                  'count': 101,
                  'dataSize': 10949,
                  'messageType': 'InspectorTerminal',
              },
              {
                  'count': 26,
                  'dataSize': 5916,
                  'messageType': 'InspectorUser',
              },
              {
                  'count': 282,
                  'dataSize': 32148,
                  'messageType': 'InspectorDynamicallyLoadedCodeModule',
              },
              {
                  'count': 18,
                  'dataSize': 10172,
                  'messageType': 'InspectorCreateProcess',
              },
              {
                  'count': 3,
                  'dataSize': 8001,
                  'messageType': 'InspectorProcessPerformance',
              },
              {
                  'count': 1,
                  'dataSize': 360,
                  'messageType': 'InspectorOperatingSystem',
              },
              {
                  'count': 6,
                  'dataSize': 546,
                  'messageType': 'InspectorStopProcess',
              },
              {
                  'count': 1,
                  'dataSize': 1553,
                  'messageType': 'InspectorInstanceMetaData',
              },
              {
                  'count': 2,
                  'dataSize': 434,
                  'messageType': 'InspectorTcpV4Connection',
              },
              {
                  'count': 474,
                  'dataSize': 2960322,
                  'messageType': 'InspectorPackageInfo',
              },
              {
                  'count': 3,
                  'dataSize': 2235,
                  'messageType': 'InspectorSystemPerformance',
              },
              {
                  'count': 105,
                  'dataSize': 46048,
                  'messageType': 'InspectorCodeModule',
              },
              {
                  'count': 1,
                  'dataSize': 182,
                  'messageType': 'InspectorUdpV6ListeningPort',
              },
              {
                  'count': 2,
                  'dataSize': 371,
                  'messageType': 'InspectorUdpV4ListeningPort',
              },
              {
                  'count': 18,
                  'dataSize': 8362,
                  'messageType': 'InspectorKernelModule',
              },
              {
                  'count': 29,
                  'dataSize': 48788,
                  'messageType': 'InspectorConfigurationInfo',
              },
              {
                  'count': 1,
                  'dataSize': 79,
                  'messageType': 'InspectorMonitoringStart',
              },
              {
                  'count': 5,
                  'dataSize': 0,
                  'messageType': 'InspectorSplitMsgBegin',
              },
              {
                  'count': 51,
                  'dataSize': 4593,
                  'messageType': 'InspectorGroup',
              },
              {
                  'count': 1,
                  'dataSize': 184,
                  'messageType': 'InspectorTcpV4ListeningPort',
              },
              {
                  'count': 1159,
                  'dataSize': 3146579,
                  'messageType': 'Total',
              },
              {
                  'count': 5,
                  'dataSize': 0,
                  'messageType': 'InspectorSplitMsgEnd',
              },
              {
                  'count': 1,
                  'dataSize': 612,
                  'messageType': 'InspectorLoadImageInProcess',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_assessment_run_agents(**kwargs)

    

    Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentRunAgents>`_    


    **Request Syntax** 
    ::

      response = client.list_assessment_run_agents(
          assessmentRunArn='string',
          filter={
              'agentHealths': [
                  'HEALTHY'|'UNHEALTHY',
              ],
              'agentHealthCodes': [
                  'IDLE'|'RUNNING'|'SHUTDOWN'|'UNHEALTHY'|'THROTTLED'|'UNKNOWN',
              ]
          },
          nextToken='string',
          maxResults=123
      )
    :type assessmentRunArn: string
    :param assessmentRunArn: **[REQUIRED]** 

      The ARN that specifies the assessment run whose agents you want to list.

      

    
    :type filter: dict
    :param filter: 

      You can use this parameter to specify a subset of data to be included in the action's response.

       

      For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.

      

    
      - **agentHealths** *(list) --* **[REQUIRED]** 

        The current health state of the agent. Values can be set to **HEALTHY** or **UNHEALTHY** .

        

      
        - *(string) --* 

        
    
      - **agentHealthCodes** *(list) --* **[REQUIRED]** 

        The detailed health state of the agent. Values can be set to **IDLE** , **RUNNING** , **SHUTDOWN** , **UNHEALTHY** , **THROTTLED** , and **UNKNOWN** . 

        

      
        - *(string) --* 

        
    
    
    :type nextToken: string
    :param nextToken: 

      You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentRunAgents** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.

      

    
    :type maxResults: integer
    :param maxResults: 

      You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentRunAgents': [
                {
                    'agentId': 'string',
                    'assessmentRunArn': 'string',
                    'agentHealth': 'HEALTHY'|'UNHEALTHY',
                    'agentHealthCode': 'IDLE'|'RUNNING'|'SHUTDOWN'|'UNHEALTHY'|'THROTTLED'|'UNKNOWN',
                    'agentHealthDetails': 'string',
                    'autoScalingGroup': 'string',
                    'telemetryMetadata': [
                        {
                            'messageType': 'string',
                            'count': 123,
                            'dataSize': 123
                        },
                    ]
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentRunAgents** *(list) --* 

          A list of ARNs that specifies the agents returned by the action.

          
          

          - *(dict) --* 

            Contains information about an Amazon Inspector agent. This data type is used as a response element in the  ListAssessmentRunAgents action.

            
            

            - **agentId** *(string) --* 

              The AWS account of the EC2 instance where the agent is installed.

              
            

            - **assessmentRunArn** *(string) --* 

              The ARN of the assessment run that is associated with the agent.

              
            

            - **agentHealth** *(string) --* 

              The current health state of the agent.

              
            

            - **agentHealthCode** *(string) --* 

              The detailed health state of the agent.

              
            

            - **agentHealthDetails** *(string) --* 

              The description for the agent health code.

              
            

            - **autoScalingGroup** *(string) --* 

              The Auto Scaling group of the EC2 instance that is specified by the agent ID.

              
            

            - **telemetryMetadata** *(list) --* 

              The Amazon Inspector application data metrics that are collected by the agent.

              
              

              - *(dict) --* 

                The metadata about the Amazon Inspector application data metrics collected by the agent. This data type is used as the response element in the  GetTelemetryMetadata action.

                
                

                - **messageType** *(string) --* 

                  A specific type of behavioral data that is collected by the agent.

                  
                

                - **count** *(integer) --* 

                  The count of messages that the agent sends to the Amazon Inspector service.

                  
                

                - **dataSize** *(integer) --* 

                  The data size of messages that the agent sends to the Amazon Inspector service.

                  
            
          
        
      
        

        - **nextToken** *(string) --* 

          When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.

          
    

    **Examples** 

    Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.
    ::

      response = client.list_assessment_run_agents(
          assessmentRunArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
          maxResults=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentRunAgents': [
              {
                  'agentHealth': 'HEALTHY',
                  'agentHealthCode': 'RUNNING',
                  'agentId': 'i-49113b93',
                  'assessmentRunArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
                  'telemetryMetadata': [
                      {
                          'count': 2,
                          'dataSize': 345,
                          'messageType': 'InspectorDuplicateProcess',
                      },
                      {
                          'count': 3,
                          'dataSize': 255,
                          'messageType': 'InspectorTimeEventMsg',
                      },
                      {
                          'count': 4,
                          'dataSize': 1082,
                          'messageType': 'InspectorNetworkInterface',
                      },
                      {
                          'count': 2,
                          'dataSize': 349,
                          'messageType': 'InspectorDnsEntry',
                      },
                      {
                          'count': 11,
                          'dataSize': 2514,
                          'messageType': 'InspectorDirectoryInfoMsg',
                      },
                      {
                          'count': 1,
                          'dataSize': 179,
                          'messageType': 'InspectorTcpV6ListeningPort',
                      },
                      {
                          'count': 101,
                          'dataSize': 10949,
                          'messageType': 'InspectorTerminal',
                      },
                      {
                          'count': 26,
                          'dataSize': 5916,
                          'messageType': 'InspectorUser',
                      },
                      {
                          'count': 282,
                          'dataSize': 32148,
                          'messageType': 'InspectorDynamicallyLoadedCodeModule',
                      },
                      {
                          'count': 18,
                          'dataSize': 10172,
                          'messageType': 'InspectorCreateProcess',
                      },
                      {
                          'count': 3,
                          'dataSize': 8001,
                          'messageType': 'InspectorProcessPerformance',
                      },
                      {
                          'count': 1,
                          'dataSize': 360,
                          'messageType': 'InspectorOperatingSystem',
                      },
                      {
                          'count': 6,
                          'dataSize': 546,
                          'messageType': 'InspectorStopProcess',
                      },
                      {
                          'count': 1,
                          'dataSize': 1553,
                          'messageType': 'InspectorInstanceMetaData',
                      },
                      {
                          'count': 2,
                          'dataSize': 434,
                          'messageType': 'InspectorTcpV4Connection',
                      },
                      {
                          'count': 474,
                          'dataSize': 2960322,
                          'messageType': 'InspectorPackageInfo',
                      },
                      {
                          'count': 3,
                          'dataSize': 2235,
                          'messageType': 'InspectorSystemPerformance',
                      },
                      {
                          'count': 105,
                          'dataSize': 46048,
                          'messageType': 'InspectorCodeModule',
                      },
                      {
                          'count': 1,
                          'dataSize': 182,
                          'messageType': 'InspectorUdpV6ListeningPort',
                      },
                      {
                          'count': 2,
                          'dataSize': 371,
                          'messageType': 'InspectorUdpV4ListeningPort',
                      },
                      {
                          'count': 18,
                          'dataSize': 8362,
                          'messageType': 'InspectorKernelModule',
                      },
                      {
                          'count': 29,
                          'dataSize': 48788,
                          'messageType': 'InspectorConfigurationInfo',
                      },
                      {
                          'count': 1,
                          'dataSize': 79,
                          'messageType': 'InspectorMonitoringStart',
                      },
                      {
                          'count': 5,
                          'dataSize': 0,
                          'messageType': 'InspectorSplitMsgBegin',
                      },
                      {
                          'count': 51,
                          'dataSize': 4593,
                          'messageType': 'InspectorGroup',
                      },
                      {
                          'count': 1,
                          'dataSize': 184,
                          'messageType': 'InspectorTcpV4ListeningPort',
                      },
                      {
                          'count': 1159,
                          'dataSize': 3146579,
                          'messageType': 'Total',
                      },
                      {
                          'count': 5,
                          'dataSize': 0,
                          'messageType': 'InspectorSplitMsgEnd',
                      },
                      {
                          'count': 1,
                          'dataSize': 612,
                          'messageType': 'InspectorLoadImageInProcess',
                      },
                  ],
              },
          ],
          'nextToken': '1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_assessment_runs(**kwargs)

    

    Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentRuns>`_    


    **Request Syntax** 
    ::

      response = client.list_assessment_runs(
          assessmentTemplateArns=[
              'string',
          ],
          filter={
              'namePattern': 'string',
              'states': [
                  'CREATED'|'START_DATA_COLLECTION_PENDING'|'START_DATA_COLLECTION_IN_PROGRESS'|'COLLECTING_DATA'|'STOP_DATA_COLLECTION_PENDING'|'DATA_COLLECTED'|'START_EVALUATING_RULES_PENDING'|'EVALUATING_RULES'|'FAILED'|'ERROR'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'CANCELED',
              ],
              'durationRange': {
                  'minSeconds': 123,
                  'maxSeconds': 123
              },
              'rulesPackageArns': [
                  'string',
              ],
              'startTimeRange': {
                  'beginDate': datetime(2015, 1, 1),
                  'endDate': datetime(2015, 1, 1)
              },
              'completionTimeRange': {
                  'beginDate': datetime(2015, 1, 1),
                  'endDate': datetime(2015, 1, 1)
              },
              'stateChangeTimeRange': {
                  'beginDate': datetime(2015, 1, 1),
                  'endDate': datetime(2015, 1, 1)
              }
          },
          nextToken='string',
          maxResults=123
      )
    :type assessmentTemplateArns: list
    :param assessmentTemplateArns: 

      The ARNs that specify the assessment templates whose assessment runs you want to list.

      

    
      - *(string) --* 

      
  
    :type filter: dict
    :param filter: 

      You can use this parameter to specify a subset of data to be included in the action's response.

       

      For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.

      

    
      - **namePattern** *(string) --* 

        For a record to match a filter, an explicit value or a string containing a wildcard that is specified for this data type property must match the value of the **assessmentRunName** property of the  AssessmentRun data type.

        

      
      - **states** *(list) --* 

        For a record to match a filter, one of the values specified for this data type property must be the exact match of the value of the **assessmentRunState** property of the  AssessmentRun data type.

        

      
        - *(string) --* 

        
    
      - **durationRange** *(dict) --* 

        For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **durationInSeconds** property of the  AssessmentRun data type.

        

      
        - **minSeconds** *(integer) --* 

          The minimum value of the duration range. Must be greater than zero.

          

        
        - **maxSeconds** *(integer) --* 

          The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).

          

        
      
      - **rulesPackageArns** *(list) --* 

        For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the **rulesPackages** property of the  AssessmentRun data type.

        

      
        - *(string) --* 

        
    
      - **startTimeRange** *(dict) --* 

        For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **startTime** property of the  AssessmentRun data type.

        

      
        - **beginDate** *(datetime) --* 

          The minimum value of the timestamp range.

          

        
        - **endDate** *(datetime) --* 

          The maximum value of the timestamp range.

          

        
      
      - **completionTimeRange** *(dict) --* 

        For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **completedAt** property of the  AssessmentRun data type.

        

      
        - **beginDate** *(datetime) --* 

          The minimum value of the timestamp range.

          

        
        - **endDate** *(datetime) --* 

          The maximum value of the timestamp range.

          

        
      
      - **stateChangeTimeRange** *(dict) --* 

        For a record to match a filter, the value that is specified for this data type property must match the **stateChangedAt** property of the  AssessmentRun data type.

        

      
        - **beginDate** *(datetime) --* 

          The minimum value of the timestamp range.

          

        
        - **endDate** *(datetime) --* 

          The maximum value of the timestamp range.

          

        
      
    
    :type nextToken: string
    :param nextToken: 

      You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentRuns** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.

      

    
    :type maxResults: integer
    :param maxResults: 

      You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentRunArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentRunArns** *(list) --* 

          A list of ARNs that specifies the assessment runs that are returned by the action.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.

          
    

    **Examples** 

    Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.
    ::

      response = client.list_assessment_runs(
          assessmentTemplateArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
          ],
          maxResults=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentRunArns': [
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-v5D6fI3v',
          ],
          'nextToken': '1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_assessment_targets(**kwargs)

    

    Lists the ARNs of the assessment targets within this AWS account. For more information about assessment targets, see `Amazon Inspector Assessment Targets <http://docs.aws.amazon.com/inspector/latest/userguide/inspector_applications.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentTargets>`_    


    **Request Syntax** 
    ::

      response = client.list_assessment_targets(
          filter={
              'assessmentTargetNamePattern': 'string'
          },
          nextToken='string',
          maxResults=123
      )
    :type filter: dict
    :param filter: 

      You can use this parameter to specify a subset of data to be included in the action's response.

       

      For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.

      

    
      - **assessmentTargetNamePattern** *(string) --* 

        For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the **assessmentTargetName** property of the  AssessmentTarget data type.

        

      
    
    :type nextToken: string
    :param nextToken: 

      You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentTargets** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.

      

    
    :type maxResults: integer
    :param maxResults: 

      You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentTargetArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentTargetArns** *(list) --* 

          A list of ARNs that specifies the assessment targets that are returned by the action.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.

          
    

    **Examples** 

    Lists the ARNs of the assessment targets within this AWS account. 
    ::

      response = client.list_assessment_targets(
          maxResults=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentTargetArns': [
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
          ],
          'nextToken': '1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_assessment_templates(**kwargs)

    

    Lists the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentTemplates>`_    


    **Request Syntax** 
    ::

      response = client.list_assessment_templates(
          assessmentTargetArns=[
              'string',
          ],
          filter={
              'namePattern': 'string',
              'durationRange': {
                  'minSeconds': 123,
                  'maxSeconds': 123
              },
              'rulesPackageArns': [
                  'string',
              ]
          },
          nextToken='string',
          maxResults=123
      )
    :type assessmentTargetArns: list
    :param assessmentTargetArns: 

      A list of ARNs that specifies the assessment targets whose assessment templates you want to list.

      

    
      - *(string) --* 

      
  
    :type filter: dict
    :param filter: 

      You can use this parameter to specify a subset of data to be included in the action's response.

       

      For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.

      

    
      - **namePattern** *(string) --* 

        For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the **assessmentTemplateName** property of the  AssessmentTemplate data type.

        

      
      - **durationRange** *(dict) --* 

        For a record to match a filter, the value specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **durationInSeconds** property of the  AssessmentTemplate data type.

        

      
        - **minSeconds** *(integer) --* 

          The minimum value of the duration range. Must be greater than zero.

          

        
        - **maxSeconds** *(integer) --* 

          The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).

          

        
      
      - **rulesPackageArns** *(list) --* 

        For a record to match a filter, the values that are specified for this data type property must be contained in the list of values of the **rulesPackageArns** property of the  AssessmentTemplate data type.

        

      
        - *(string) --* 

        
    
    
    :type nextToken: string
    :param nextToken: 

      You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentTemplates** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.

      

    
    :type maxResults: integer
    :param maxResults: 

      You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentTemplateArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentTemplateArns** *(list) --* 

          A list of ARNs that specifies the assessment templates returned by the action.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.

          
    

    **Examples** 

    Lists the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets.
    ::

      response = client.list_assessment_templates(
          assessmentTargetArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
          ],
          maxResults=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentTemplateArns': [
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-Uza6ihLh',
          ],
          'nextToken': '1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_event_subscriptions(**kwargs)

    

    Lists all the event subscriptions for the assessment template that is specified by the ARN of the assessment template. For more information, see  SubscribeToEvent and  UnsubscribeFromEvent .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListEventSubscriptions>`_    


    **Request Syntax** 
    ::

      response = client.list_event_subscriptions(
          resourceArn='string',
          nextToken='string',
          maxResults=123
      )
    :type resourceArn: string
    :param resourceArn: 

      The ARN of the assessment template for which you want to list the existing event subscriptions.

      

    
    :type nextToken: string
    :param nextToken: 

      You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListEventSubscriptions** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.

      

    
    :type maxResults: integer
    :param maxResults: 

      You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'subscriptions': [
                {
                    'resourceArn': 'string',
                    'topicArn': 'string',
                    'eventSubscriptions': [
                        {
                            'event': 'ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
                            'subscribedAt': datetime(2015, 1, 1)
                        },
                    ]
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **subscriptions** *(list) --* 

          Details of the returned event subscriptions.

          
          

          - *(dict) --* 

            This data type is used as a response element in the  ListEventSubscriptions action.

            
            

            - **resourceArn** *(string) --* 

              The ARN of the assessment template that is used during the event for which the SNS notification is sent.

              
            

            - **topicArn** *(string) --* 

              The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS notifications are sent.

              
            

            - **eventSubscriptions** *(list) --* 

              The list of existing event subscriptions.

              
              

              - *(dict) --* 

                This data type is used in the  Subscription data type.

                
                

                - **event** *(string) --* 

                  The event for which Amazon Simple Notification Service (SNS) notifications are sent.

                  
                

                - **subscribedAt** *(datetime) --* 

                  The time at which  SubscribeToEvent is called.

                  
            
          
        
      
        

        - **nextToken** *(string) --* 

          When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.

          
    

    **Examples** 

    Lists all the event subscriptions for the assessment template that is specified by the ARN of the assessment template. 
    ::

      response = client.list_event_subscriptions(
          maxResults=123,
          resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'nextToken': '1',
          'subscriptions': [
              {
                  'eventSubscriptions': [
                      {
                          'event': 'ASSESSMENT_RUN_COMPLETED',
                          'subscribedAt': datetime(2016, 3, 31, 13, 17, 20, 3, 91, 1),
                      },
                  ],
                  'resourceArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
                  'topicArn': 'arn:aws:sns:us-west-2:123456789012:exampletopic',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_findings(**kwargs)

    

    Lists findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListFindings>`_    


    **Request Syntax** 
    ::

      response = client.list_findings(
          assessmentRunArns=[
              'string',
          ],
          filter={
              'agentIds': [
                  'string',
              ],
              'autoScalingGroups': [
                  'string',
              ],
              'ruleNames': [
                  'string',
              ],
              'severities': [
                  'Low'|'Medium'|'High'|'Informational'|'Undefined',
              ],
              'rulesPackageArns': [
                  'string',
              ],
              'attributes': [
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              'userAttributes': [
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              'creationTimeRange': {
                  'beginDate': datetime(2015, 1, 1),
                  'endDate': datetime(2015, 1, 1)
              }
          },
          nextToken='string',
          maxResults=123
      )
    :type assessmentRunArns: list
    :param assessmentRunArns: 

      The ARNs of the assessment runs that generate the findings that you want to list.

      

    
      - *(string) --* 

      
  
    :type filter: dict
    :param filter: 

      You can use this parameter to specify a subset of data to be included in the action's response.

       

      For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.

      

    
      - **agentIds** *(list) --* 

        For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **agentId** property of the  Finding data type.

        

      
        - *(string) --* 

        
    
      - **autoScalingGroups** *(list) --* 

        For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **autoScalingGroup** property of the  Finding data type.

        

      
        - *(string) --* 

        
    
      - **ruleNames** *(list) --* 

        For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **ruleName** property of the  Finding data type.

        

      
        - *(string) --* 

        
    
      - **severities** *(list) --* 

        For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **severity** property of the  Finding data type.

        

      
        - *(string) --* 

        
    
      - **rulesPackageArns** *(list) --* 

        For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **rulesPackageArn** property of the  Finding data type.

        

      
        - *(string) --* 

        
    
      - **attributes** *(list) --* 

        For a record to match a filter, the list of values that are specified for this data type property must be contained in the list of values of the **attributes** property of the  Finding data type.

        

      
        - *(dict) --* 

          This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

          

        
          - **key** *(string) --* **[REQUIRED]** 

            The attribute key.

            

          
          - **value** *(string) --* 

            The value assigned to the attribute key.

            

          
        
    
      - **userAttributes** *(list) --* 

        For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the **userAttributes** property of the  Finding data type.

        

      
        - *(dict) --* 

          This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

          

        
          - **key** *(string) --* **[REQUIRED]** 

            The attribute key.

            

          
          - **value** *(string) --* 

            The value assigned to the attribute key.

            

          
        
    
      - **creationTimeRange** *(dict) --* 

        The time range during which the finding is generated.

        

      
        - **beginDate** *(datetime) --* 

          The minimum value of the timestamp range.

          

        
        - **endDate** *(datetime) --* 

          The maximum value of the timestamp range.

          

        
      
    
    :type nextToken: string
    :param nextToken: 

      You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListFindings** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.

      

    
    :type maxResults: integer
    :param maxResults: 

      You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'findingArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **findingArns** *(list) --* 

          A list of ARNs that specifies the findings returned by the action.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.

          
    

    **Examples** 

    Lists findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs.
    ::

      response = client.list_findings(
          assessmentRunArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
          ],
          maxResults=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'findingArns': [
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4',
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-v5D6fI3v/finding/0-tyvmqBLy',
          ],
          'nextToken': '1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_rules_packages(**kwargs)

    

    Lists all available Amazon Inspector rules packages.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListRulesPackages>`_    


    **Request Syntax** 
    ::

      response = client.list_rules_packages(
          nextToken='string',
          maxResults=123
      )
    :type nextToken: string
    :param nextToken: 

      You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListRulesPackages** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.

      

    
    :type maxResults: integer
    :param maxResults: 

      You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'rulesPackageArns': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **rulesPackageArns** *(list) --* 

          The list of ARNs that specifies the rules packages returned by the action.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.

          
    

    **Examples** 

    Lists all available Amazon Inspector rules packages.
    ::

      response = client.list_rules_packages(
          maxResults=123,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'nextToken': '1',
          'rulesPackageArns': [
              'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p',
              'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-H5hpSawc',
              'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ',
              'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-vg5GGHSD',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_tags_for_resource(**kwargs)

    

    Lists all tags associated with an assessment template.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListTagsForResource>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_resource(
          resourceArn='string'
      )
    :type resourceArn: string
    :param resourceArn: **[REQUIRED]** 

      The ARN that specifies the assessment template whose tags you want to list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tags** *(list) --* 

          A collection of key and value pairs.

          
          

          - *(dict) --* 

            A key and value pair. This data type is used as a request parameter in the  SetTagsForResource action and a response element in the  ListTagsForResource action.

            
            

            - **key** *(string) --* 

              A tag key.

              
            

            - **value** *(string) --* 

              A value assigned to a tag key.

              
        
      
    

    **Examples** 

    Lists all tags associated with an assessment template.
    ::

      response = client.list_tags_for_resource(
          resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-gcwFliYu',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'tags': [
              {
                  'key': 'Name',
                  'value': 'Example',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: preview_agents(**kwargs)

    

    Previews the agents installed on the EC2 instances that are part of the specified assessment target.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/PreviewAgents>`_    


    **Request Syntax** 
    ::

      response = client.preview_agents(
          previewAgentsArn='string',
          nextToken='string',
          maxResults=123
      )
    :type previewAgentsArn: string
    :param previewAgentsArn: **[REQUIRED]** 

      The ARN of the assessment target whose agents you want to preview.

      

    
    :type nextToken: string
    :param nextToken: 

      You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **PreviewAgents** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.

      

    
    :type maxResults: integer
    :param maxResults: 

      You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'agentPreviews': [
                {
                    'agentId': 'string',
                    'autoScalingGroup': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **agentPreviews** *(list) --* 

          The resulting list of agents.

          
          

          - *(dict) --* 

            Used as a response element in the  PreviewAgents action.

            
            

            - **agentId** *(string) --* 

              The ID of the EC2 instance where the agent is installed.

              
            

            - **autoScalingGroup** *(string) --* 

              The Auto Scaling group for the EC2 instance where the agent is installed.

              
        
      
        

        - **nextToken** *(string) --* 

          When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.

          
    

    **Examples** 

    Previews the agents installed on the EC2 instances that are part of the specified assessment target.
    ::

      response = client.preview_agents(
          maxResults=123,
          previewAgentsArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'agentPreviews': [
              {
                  'agentId': 'i-49113b93',
              },
          ],
          'nextToken': '1',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: register_cross_account_access_role(**kwargs)

    

    Registers the IAM role that Amazon Inspector uses to list your EC2 instances at the start of the assessment run or when you call the  PreviewAgents action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/RegisterCrossAccountAccessRole>`_    


    **Request Syntax** 
    ::

      response = client.register_cross_account_access_role(
          roleArn='string'
      )
    :type roleArn: string
    :param roleArn: **[REQUIRED]** 

      The ARN of the IAM role that Amazon Inspector uses to list your EC2 instances during the assessment run or when you call the  PreviewAgents action. 

      

    
    
    :returns: None

    **Examples** 

    Registers the IAM role that Amazon Inspector uses to list your EC2 instances at the start of the assessment run or when you call the PreviewAgents action.
    ::

      response = client.register_cross_account_access_role(
          roleArn='arn:aws:iam::123456789012:role/inspector',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: remove_attributes_from_findings(**kwargs)

    

    Removes entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/RemoveAttributesFromFindings>`_    


    **Request Syntax** 
    ::

      response = client.remove_attributes_from_findings(
          findingArns=[
              'string',
          ],
          attributeKeys=[
              'string',
          ]
      )
    :type findingArns: list
    :param findingArns: **[REQUIRED]** 

      The ARNs that specify the findings that you want to remove attributes from.

      

    
      - *(string) --* 

      
  
    :type attributeKeys: list
    :param attributeKeys: **[REQUIRED]** 

      The array of attribute keys that you want to remove from specified findings.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'failedItems': {
                'string': {
                    'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                    'retryable': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **failedItems** *(dict) --* 

          Attributes details that cannot be described. An error code is provided for each failed item.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Includes details about the failed items.

              
              

              - **failureCode** *(string) --* 

                The status code of a failed item.

                
              

              - **retryable** *(boolean) --* 

                Indicates whether you can immediately retry a request for this item for a specified resource.

                
          
      
    
    

    **Examples** 

    Removes entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists.
    ::

      response = client.remove_attributes_from_findings(
          attributeKeys=[
              'key=Example,value=example',
          ],
          findingArns=[
              'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'failedItems': {
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_tags_for_resource(**kwargs)

    

    Sets tags (key and value pairs) to the assessment template that is specified by the ARN of the assessment template.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/SetTagsForResource>`_    


    **Request Syntax** 
    ::

      response = client.set_tags_for_resource(
          resourceArn='string',
          tags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type resourceArn: string
    :param resourceArn: **[REQUIRED]** 

      The ARN of the assessment template that you want to set tags to.

      

    
    :type tags: list
    :param tags: 

      A collection of key and value pairs that you want to set to the assessment template.

      

    
      - *(dict) --* 

        A key and value pair. This data type is used as a request parameter in the  SetTagsForResource action and a response element in the  ListTagsForResource action.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          A tag key.

          

        
        - **value** *(string) --* 

          A value assigned to a tag key.

          

        
      
  
    
    :returns: None

    **Examples** 

    Sets tags (key and value pairs) to the assessment template that is specified by the ARN of the assessment template.
    ::

      response = client.set_tags_for_resource(
          resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
          tags=[
              {
                  'key': 'Example',
                  'value': 'example',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: start_assessment_run(**kwargs)

    

    Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/StartAssessmentRun>`_    


    **Request Syntax** 
    ::

      response = client.start_assessment_run(
          assessmentTemplateArn='string',
          assessmentRunName='string'
      )
    :type assessmentTemplateArn: string
    :param assessmentTemplateArn: **[REQUIRED]** 

      The ARN of the assessment template of the assessment run that you want to start.

      

    
    :type assessmentRunName: string
    :param assessmentRunName: 

      You can specify the name for the assessment run. The name must be unique for the assessment template whose ARN is used to start the assessment run.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'assessmentRunArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **assessmentRunArn** *(string) --* 

          The ARN of the assessment run that has been started.

          
    

    **Examples** 

    Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.
    ::

      response = client.start_assessment_run(
          assessmentRunName='examplerun',
          assessmentTemplateArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'assessmentRunArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-jOoroxyY',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: stop_assessment_run(**kwargs)

    

    Stops the assessment run that is specified by the ARN of the assessment run.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/StopAssessmentRun>`_    


    **Request Syntax** 
    ::

      response = client.stop_assessment_run(
          assessmentRunArn='string',
          stopAction='START_EVALUATION'|'SKIP_EVALUATION'
      )
    :type assessmentRunArn: string
    :param assessmentRunArn: **[REQUIRED]** 

      The ARN of the assessment run that you want to stop.

      

    
    :type stopAction: string
    :param stopAction: 

      An input option that can be set to either START_EVALUATION or SKIP_EVALUATION. START_EVALUATION (the default value), stops the AWS agent from collecting data and begins the results evaluation and the findings generation process. SKIP_EVALUATION cancels the assessment run immediately, after which no findings are generated.

      

    
    
    :returns: None

    **Examples** 

    Stops the assessment run that is specified by the ARN of the assessment run.
    ::

      response = client.stop_assessment_run(
          assessmentRunArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: subscribe_to_event(**kwargs)

    

    Enables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/SubscribeToEvent>`_    


    **Request Syntax** 
    ::

      response = client.subscribe_to_event(
          resourceArn='string',
          event='ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
          topicArn='string'
      )
    :type resourceArn: string
    :param resourceArn: **[REQUIRED]** 

      The ARN of the assessment template that is used during the event for which you want to receive SNS notifications.

      

    
    :type event: string
    :param event: **[REQUIRED]** 

      The event for which you want to receive SNS notifications.

      

    
    :type topicArn: string
    :param topicArn: **[REQUIRED]** 

      The ARN of the SNS topic to which the SNS notifications are sent.

      

    
    
    :returns: None

    **Examples** 

    Enables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.
    ::

      response = client.subscribe_to_event(
          event='ASSESSMENT_RUN_COMPLETED',
          resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
          topicArn='arn:aws:sns:us-west-2:123456789012:exampletopic',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: unsubscribe_from_event(**kwargs)

    

    Disables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/UnsubscribeFromEvent>`_    


    **Request Syntax** 
    ::

      response = client.unsubscribe_from_event(
          resourceArn='string',
          event='ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
          topicArn='string'
      )
    :type resourceArn: string
    :param resourceArn: **[REQUIRED]** 

      The ARN of the assessment template that is used during the event for which you want to stop receiving SNS notifications.

      

    
    :type event: string
    :param event: **[REQUIRED]** 

      The event for which you want to stop receiving SNS notifications.

      

    
    :type topicArn: string
    :param topicArn: **[REQUIRED]** 

      The ARN of the SNS topic to which SNS notifications are sent.

      

    
    
    :returns: None

    **Examples** 

    Disables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.
    ::

      response = client.unsubscribe_from_event(
          event='ASSESSMENT_RUN_COMPLETED',
          resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
          topicArn='arn:aws:sns:us-west-2:123456789012:exampletopic',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_assessment_target(**kwargs)

    

    Updates the assessment target that is specified by the ARN of the assessment target.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/UpdateAssessmentTarget>`_    


    **Request Syntax** 
    ::

      response = client.update_assessment_target(
          assessmentTargetArn='string',
          assessmentTargetName='string',
          resourceGroupArn='string'
      )
    :type assessmentTargetArn: string
    :param assessmentTargetArn: **[REQUIRED]** 

      The ARN of the assessment target that you want to update.

      

    
    :type assessmentTargetName: string
    :param assessmentTargetName: **[REQUIRED]** 

      The name of the assessment target that you want to update.

      

    
    :type resourceGroupArn: string
    :param resourceGroupArn: **[REQUIRED]** 

      The ARN of the resource group that is used to specify the new resource group to associate with the assessment target.

      

    
    
    :returns: None

    **Examples** 

    Updates the assessment target that is specified by the ARN of the assessment target.
    ::

      response = client.update_assessment_target(
          assessmentTargetArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX',
          assessmentTargetName='Example',
          resourceGroupArn='arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-yNbgL5Pt',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:
