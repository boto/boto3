

************
DataPipeline
************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: DataPipeline.Client

  A low-level client representing AWS Data Pipeline::

    
    import boto3
    
    client = boto3.client('datapipeline')

  
  These are the available methods:
  
  *   :py:meth:`~DataPipeline.Client.activate_pipeline`

  
  *   :py:meth:`~DataPipeline.Client.add_tags`

  
  *   :py:meth:`~DataPipeline.Client.can_paginate`

  
  *   :py:meth:`~DataPipeline.Client.create_pipeline`

  
  *   :py:meth:`~DataPipeline.Client.deactivate_pipeline`

  
  *   :py:meth:`~DataPipeline.Client.delete_pipeline`

  
  *   :py:meth:`~DataPipeline.Client.describe_objects`

  
  *   :py:meth:`~DataPipeline.Client.describe_pipelines`

  
  *   :py:meth:`~DataPipeline.Client.evaluate_expression`

  
  *   :py:meth:`~DataPipeline.Client.generate_presigned_url`

  
  *   :py:meth:`~DataPipeline.Client.get_paginator`

  
  *   :py:meth:`~DataPipeline.Client.get_pipeline_definition`

  
  *   :py:meth:`~DataPipeline.Client.get_waiter`

  
  *   :py:meth:`~DataPipeline.Client.list_pipelines`

  
  *   :py:meth:`~DataPipeline.Client.poll_for_task`

  
  *   :py:meth:`~DataPipeline.Client.put_pipeline_definition`

  
  *   :py:meth:`~DataPipeline.Client.query_objects`

  
  *   :py:meth:`~DataPipeline.Client.remove_tags`

  
  *   :py:meth:`~DataPipeline.Client.report_task_progress`

  
  *   :py:meth:`~DataPipeline.Client.report_task_runner_heartbeat`

  
  *   :py:meth:`~DataPipeline.Client.set_status`

  
  *   :py:meth:`~DataPipeline.Client.set_task_status`

  
  *   :py:meth:`~DataPipeline.Client.validate_pipeline_definition`

  

  .. py:method:: activate_pipeline(**kwargs)

    

    Validates the specified pipeline and starts processing pipeline tasks. If the pipeline does not pass validation, activation fails.

     

    If you need to pause the pipeline to investigate an issue with a component, such as a data source or script, call  DeactivatePipeline .

     

    To activate a finished pipeline, modify the end date for the pipeline and then activate it.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/ActivatePipeline>`_    


    **Request Syntax** 
    ::

      response = client.activate_pipeline(
          pipelineId='string',
          parameterValues=[
              {
                  'id': 'string',
                  'stringValue': 'string'
              },
          ],
          startTimestamp=datetime(2015, 1, 1)
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type parameterValues: list
    :param parameterValues: 

      A list of parameter values to pass to the pipeline at activation.

      

    
      - *(dict) --* 

        A value or list of parameter values. 

        

      
        - **id** *(string) --* **[REQUIRED]** 

          The ID of the parameter value.

          

        
        - **stringValue** *(string) --* **[REQUIRED]** 

          The field value, expressed as a String.

          

        
      
  
    :type startTimestamp: datetime
    :param startTimestamp: 

      The date and time to resume the pipeline. By default, the pipeline resumes from the last completed execution.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of ActivatePipeline.

        
    

  .. py:method:: add_tags(**kwargs)

    

    Adds or modifies tags for the specified pipeline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/AddTags>`_    


    **Request Syntax** 
    ::

      response = client.add_tags(
          pipelineId='string',
          tags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type tags: list
    :param tags: **[REQUIRED]** 

      The tags to add, as key/value pairs.

      

    
      - *(dict) --* 

        Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The key name of a tag defined by a user. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The optional value portion of a tag defined by a user. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of AddTags.

        
    

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


  .. py:method:: create_pipeline(**kwargs)

    

    Creates a new, empty pipeline. Use  PutPipelineDefinition to populate the pipeline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/CreatePipeline>`_    


    **Request Syntax** 
    ::

      response = client.create_pipeline(
          name='string',
          uniqueId='string',
          description='string',
          tags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name for the pipeline. You can use the same name for multiple pipelines associated with your AWS account, because AWS Data Pipeline assigns each pipeline a unique pipeline identifier.

      

    
    :type uniqueId: string
    :param uniqueId: **[REQUIRED]** 

      A unique identifier. This identifier is not the same as the pipeline identifier assigned by AWS Data Pipeline. You are responsible for defining the format and ensuring the uniqueness of this identifier. You use this parameter to ensure idempotency during repeated calls to ``CreatePipeline`` . For example, if the first call to ``CreatePipeline`` does not succeed, you can pass in the same unique identifier and pipeline name combination on a subsequent call to ``CreatePipeline`` . ``CreatePipeline`` ensures that if a pipeline already exists with the same name and unique identifier, a new pipeline is not created. Instead, you'll receive the pipeline identifier from the previous attempt. The uniqueness of the name and unique identifier combination is scoped to the AWS account or IAM user credentials.

      

    
    :type description: string
    :param description: 

      The description for the pipeline.

      

    
    :type tags: list
    :param tags: 

      A list of tags to associate with the pipeline at creation. Tags let you control access to pipelines. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

      

    
      - *(dict) --* 

        Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The key name of a tag defined by a user. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

          

        
        - **value** *(string) --* **[REQUIRED]** 

          The optional value portion of a tag defined by a user. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'pipelineId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of CreatePipeline.

        
        

        - **pipelineId** *(string) --* 

          The ID that AWS Data Pipeline assigns the newly created pipeline. For example, ``df-06372391ZG65EXAMPLE`` .

          
    

  .. py:method:: deactivate_pipeline(**kwargs)

    

    Deactivates the specified running pipeline. The pipeline is set to the ``DEACTIVATING`` state until the deactivation process completes.

     

    To resume a deactivated pipeline, use  ActivatePipeline . By default, the pipeline resumes from the last completed execution. Optionally, you can specify the date and time to resume the pipeline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/DeactivatePipeline>`_    


    **Request Syntax** 
    ::

      response = client.deactivate_pipeline(
          pipelineId='string',
          cancelActive=True|False
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type cancelActive: boolean
    :param cancelActive: 

      Indicates whether to cancel any running objects. The default is true, which sets the state of any running objects to ``CANCELED`` . If this value is false, the pipeline is deactivated after all running objects finish.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of DeactivatePipeline.

        
    

  .. py:method:: delete_pipeline(**kwargs)

    

    Deletes a pipeline, its pipeline definition, and its run history. AWS Data Pipeline attempts to cancel instances associated with the pipeline that are currently being processed by task runners.

     

    Deleting a pipeline cannot be undone. You cannot query or restore a deleted pipeline. To temporarily pause a pipeline instead of deleting it, call  SetStatus with the status set to ``PAUSE`` on individual components. Components that are paused by  SetStatus can be resumed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/DeletePipeline>`_    


    **Request Syntax** 
    ::

      response = client.delete_pipeline(
          pipelineId='string'
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    
    :returns: None

  .. py:method:: describe_objects(**kwargs)

    

    Gets the object definitions for a set of objects associated with the pipeline. Object definitions are composed of a set of fields that define the properties of the object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/DescribeObjects>`_    


    **Request Syntax** 
    ::

      response = client.describe_objects(
          pipelineId='string',
          objectIds=[
              'string',
          ],
          evaluateExpressions=True|False,
          marker='string'
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline that contains the object definitions.

      

    
    :type objectIds: list
    :param objectIds: **[REQUIRED]** 

      The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to ``DescribeObjects`` .

      

    
      - *(string) --* 

      
  
    :type evaluateExpressions: boolean
    :param evaluateExpressions: 

      Indicates whether any expressions in the object should be evaluated when the object descriptions are returned.

      

    
    :type marker: string
    :param marker: 

      The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call ``DescribeObjects`` with the marker value from the previous call to retrieve the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'pipelineObjects': [
                {
                    'id': 'string',
                    'name': 'string',
                    'fields': [
                        {
                            'key': 'string',
                            'stringValue': 'string',
                            'refValue': 'string'
                        },
                    ]
                },
            ],
            'marker': 'string',
            'hasMoreResults': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of DescribeObjects.

        
        

        - **pipelineObjects** *(list) --* 

          An array of object definitions.

          
          

          - *(dict) --* 

            Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

            
            

            - **id** *(string) --* 

              The ID of the object.

              
            

            - **name** *(string) --* 

              The name of the object.

              
            

            - **fields** *(list) --* 

              Key-value pairs that define the properties of the object.

              
              

              - *(dict) --* 

                A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.

                
                

                - **key** *(string) --* 

                  The field identifier.

                  
                

                - **stringValue** *(string) --* 

                  The field value, expressed as a String.

                  
                

                - **refValue** *(string) --* 

                  The field value, expressed as the identifier of another object.

                  
            
          
        
      
        

        - **marker** *(string) --* 

          The starting point for the next page of results. To view the next page of results, call ``DescribeObjects`` again with this marker value. If the value is null, there are no more results.

          
        

        - **hasMoreResults** *(boolean) --* 

          Indicates whether there are more results to return.

          
    

  .. py:method:: describe_pipelines(**kwargs)

    

    Retrieves metadata about one or more pipelines. The information retrieved includes the name of the pipeline, the pipeline identifier, its current state, and the user account that owns the pipeline. Using account credentials, you can retrieve metadata about pipelines that you or your IAM users have created. If you are using an IAM user account, you can retrieve metadata about only those pipelines for which you have read permissions.

     

    To retrieve the full pipeline definition instead of metadata about the pipeline, call  GetPipelineDefinition .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/DescribePipelines>`_    


    **Request Syntax** 
    ::

      response = client.describe_pipelines(
          pipelineIds=[
              'string',
          ]
      )
    :type pipelineIds: list
    :param pipelineIds: **[REQUIRED]** 

      The IDs of the pipelines to describe. You can pass as many as 25 identifiers in a single call. To obtain pipeline IDs, call  ListPipelines .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'pipelineDescriptionList': [
                {
                    'pipelineId': 'string',
                    'name': 'string',
                    'fields': [
                        {
                            'key': 'string',
                            'stringValue': 'string',
                            'refValue': 'string'
                        },
                    ],
                    'description': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of DescribePipelines.

        
        

        - **pipelineDescriptionList** *(list) --* 

          An array of descriptions for the specified pipelines.

          
          

          - *(dict) --* 

            Contains pipeline metadata.

            
            

            - **pipelineId** *(string) --* 

              The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the form ``df-297EG78HU43EEXAMPLE`` .

              
            

            - **name** *(string) --* 

              The name of the pipeline.

              
            

            - **fields** *(list) --* 

              A list of read-only fields that contain metadata about the pipeline: @userId, @accountId, and @pipelineState.

              
              

              - *(dict) --* 

                A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.

                
                

                - **key** *(string) --* 

                  The field identifier.

                  
                

                - **stringValue** *(string) --* 

                  The field value, expressed as a String.

                  
                

                - **refValue** *(string) --* 

                  The field value, expressed as the identifier of another object.

                  
            
          
            

            - **description** *(string) --* 

              Description of the pipeline.

              
            

            - **tags** *(list) --* 

              A list of tags to associated with a pipeline. Tags let you control access to pipelines. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

              
              

              - *(dict) --* 

                Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

                
                

                - **key** *(string) --* 

                  The key name of a tag defined by a user. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

                  
                

                - **value** *(string) --* 

                  The optional value portion of a tag defined by a user. For more information, see `Controlling User Access to Pipelines <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in the *AWS Data Pipeline Developer Guide* .

                  
            
          
        
      
    

  .. py:method:: evaluate_expression(**kwargs)

    

    Task runners call ``EvaluateExpression`` to evaluate a string in the context of the specified object. For example, a task runner can evaluate SQL queries stored in Amazon S3.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/EvaluateExpression>`_    


    **Request Syntax** 
    ::

      response = client.evaluate_expression(
          pipelineId='string',
          objectId='string',
          expression='string'
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type objectId: string
    :param objectId: **[REQUIRED]** 

      The ID of the object.

      

    
    :type expression: string
    :param expression: **[REQUIRED]** 

      The expression to evaluate.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'evaluatedExpression': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of EvaluateExpression.

        
        

        - **evaluatedExpression** *(string) --* 

          The evaluated expression.

          
    

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


  .. py:method:: get_pipeline_definition(**kwargs)

    

    Gets the definition of the specified pipeline. You can call ``GetPipelineDefinition`` to retrieve the pipeline definition that you provided using  PutPipelineDefinition .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/GetPipelineDefinition>`_    


    **Request Syntax** 
    ::

      response = client.get_pipeline_definition(
          pipelineId='string',
          version='string'
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type version: string
    :param version: 

      The version of the pipeline definition to retrieve. Set this parameter to ``latest`` (default) to use the last definition saved to the pipeline or ``active`` to use the last definition that was activated.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'pipelineObjects': [
                {
                    'id': 'string',
                    'name': 'string',
                    'fields': [
                        {
                            'key': 'string',
                            'stringValue': 'string',
                            'refValue': 'string'
                        },
                    ]
                },
            ],
            'parameterObjects': [
                {
                    'id': 'string',
                    'attributes': [
                        {
                            'key': 'string',
                            'stringValue': 'string'
                        },
                    ]
                },
            ],
            'parameterValues': [
                {
                    'id': 'string',
                    'stringValue': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of GetPipelineDefinition.

        
        

        - **pipelineObjects** *(list) --* 

          The objects defined in the pipeline.

          
          

          - *(dict) --* 

            Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

            
            

            - **id** *(string) --* 

              The ID of the object.

              
            

            - **name** *(string) --* 

              The name of the object.

              
            

            - **fields** *(list) --* 

              Key-value pairs that define the properties of the object.

              
              

              - *(dict) --* 

                A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.

                
                

                - **key** *(string) --* 

                  The field identifier.

                  
                

                - **stringValue** *(string) --* 

                  The field value, expressed as a String.

                  
                

                - **refValue** *(string) --* 

                  The field value, expressed as the identifier of another object.

                  
            
          
        
      
        

        - **parameterObjects** *(list) --* 

          The parameter objects used in the pipeline definition.

          
          

          - *(dict) --* 

            Contains information about a parameter object.

            
            

            - **id** *(string) --* 

              The ID of the parameter object. 

              
            

            - **attributes** *(list) --* 

              The attributes of the parameter object.

              
              

              - *(dict) --* 

                The attributes allowed or specified with a parameter object.

                
                

                - **key** *(string) --* 

                  The field identifier.

                  
                

                - **stringValue** *(string) --* 

                  The field value, expressed as a String.

                  
            
          
        
      
        

        - **parameterValues** *(list) --* 

          The parameter values used in the pipeline definition.

          
          

          - *(dict) --* 

            A value or list of parameter values. 

            
            

            - **id** *(string) --* 

              The ID of the parameter value.

              
            

            - **stringValue** *(string) --* 

              The field value, expressed as a String.

              
        
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_pipelines(**kwargs)

    

    Lists the pipeline identifiers for all active pipelines that you have permission to access.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/ListPipelines>`_    


    **Request Syntax** 
    ::

      response = client.list_pipelines(
          marker='string'
      )
    :type marker: string
    :param marker: 

      The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call ``ListPipelines`` with the marker value from the previous call to retrieve the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'pipelineIdList': [
                {
                    'id': 'string',
                    'name': 'string'
                },
            ],
            'marker': 'string',
            'hasMoreResults': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of ListPipelines.

        
        

        - **pipelineIdList** *(list) --* 

          The pipeline identifiers. If you require additional information about the pipelines, you can use these identifiers to call  DescribePipelines and  GetPipelineDefinition .

          
          

          - *(dict) --* 

            Contains the name and identifier of a pipeline.

            
            

            - **id** *(string) --* 

              The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the form ``df-297EG78HU43EEXAMPLE`` .

              
            

            - **name** *(string) --* 

              The name of the pipeline.

              
        
      
        

        - **marker** *(string) --* 

          The starting point for the next page of results. To view the next page of results, call ``ListPipelinesOutput`` again with this marker value. If the value is null, there are no more results.

          
        

        - **hasMoreResults** *(boolean) --* 

          Indicates whether there are more results that can be obtained by a subsequent call.

          
    

  .. py:method:: poll_for_task(**kwargs)

    

    Task runners call ``PollForTask`` to receive a task to perform from AWS Data Pipeline. The task runner specifies which tasks it can perform by setting a value for the ``workerGroup`` parameter. The task returned can come from any of the pipelines that match the ``workerGroup`` value passed in by the task runner and that was launched using the IAM user credentials specified by the task runner.

     

    If tasks are ready in the work queue, ``PollForTask`` returns a response immediately. If no tasks are available in the queue, ``PollForTask`` uses long-polling and holds on to a poll connection for up to a 90 seconds, during which time the first newly scheduled task is handed to the task runner. To accomodate this, set the socket timeout in your task runner to 90 seconds. The task runner should not call ``PollForTask`` again on the same ``workerGroup`` until it receives a response, and this can take up to 90 seconds. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/PollForTask>`_    


    **Request Syntax** 
    ::

      response = client.poll_for_task(
          workerGroup='string',
          hostname='string',
          instanceIdentity={
              'document': 'string',
              'signature': 'string'
          }
      )
    :type workerGroup: string
    :param workerGroup: **[REQUIRED]** 

      The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for ``workerGroup`` in the call to ``PollForTask`` . There are no wildcard values permitted in ``workerGroup`` ; the string must be an exact, case-sensitive, match.

      

    
    :type hostname: string
    :param hostname: 

      The public DNS name of the calling task runner.

      

    
    :type instanceIdentity: dict
    :param instanceIdentity: 

      Identity information for the EC2 instance that is hosting the task runner. You can get this value from the instance using ``http://169.254.169.254/latest/meta-data/instance-id`` . For more information, see `Instance Metadata <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html>`__ in the *Amazon Elastic Compute Cloud User Guide.* Passing in this value proves that your task runner is running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied to your pipeline.

      

    
      - **document** *(string) --* 

        A description of an EC2 instance that is generated when the instance is launched and exposed to the instance via the instance metadata service in the form of a JSON representation of an object.

        

      
      - **signature** *(string) --* 

        A signature which can be used to verify the accuracy and authenticity of the information provided in the instance identity document.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskObject': {
                'taskId': 'string',
                'pipelineId': 'string',
                'attemptId': 'string',
                'objects': {
                    'string': {
                        'id': 'string',
                        'name': 'string',
                        'fields': [
                            {
                                'key': 'string',
                                'stringValue': 'string',
                                'refValue': 'string'
                            },
                        ]
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of PollForTask.

        
        

        - **taskObject** *(dict) --* 

          The information needed to complete the task that is being assigned to the task runner. One of the fields returned in this object is ``taskId`` , which contains an identifier for the task being assigned. The calling task runner uses ``taskId`` in subsequent calls to  ReportTaskProgress and  SetTaskStatus .

          
          

          - **taskId** *(string) --* 

            An internal identifier for the task. This ID is passed to the  SetTaskStatus and  ReportTaskProgress actions.

            
          

          - **pipelineId** *(string) --* 

            The ID of the pipeline that provided the task.

            
          

          - **attemptId** *(string) --* 

            The ID of the pipeline task attempt object. AWS Data Pipeline uses this value to track how many times a task is attempted.

            
          

          - **objects** *(dict) --* 

            Connection information for the location where the task runner will publish the output of the task.

            
            

            - *(string) --* 
              

              - *(dict) --* 

                Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

                
                

                - **id** *(string) --* 

                  The ID of the object.

                  
                

                - **name** *(string) --* 

                  The name of the object.

                  
                

                - **fields** *(list) --* 

                  Key-value pairs that define the properties of the object.

                  
                  

                  - *(dict) --* 

                    A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.

                    
                    

                    - **key** *(string) --* 

                      The field identifier.

                      
                    

                    - **stringValue** *(string) --* 

                      The field value, expressed as a String.

                      
                    

                    - **refValue** *(string) --* 

                      The field value, expressed as the identifier of another object.

                      
                
              
            
        
      
      
    

  .. py:method:: put_pipeline_definition(**kwargs)

    

    Adds tasks, schedules, and preconditions to the specified pipeline. You can use ``PutPipelineDefinition`` to populate a new pipeline.

     

     ``PutPipelineDefinition`` also validates the configuration as it adds it to the pipeline. Changes to the pipeline are saved unless one of the following three validation errors exists in the pipeline. 

     

     
    * An object is missing a name or identifier field.
     
    * A string or reference field is empty.
     
    * The number of objects in the pipeline exceeds the maximum allowed objects.
     
    * The pipeline is in a FINISHED state.
     

     

    Pipeline object definitions are passed to the ``PutPipelineDefinition`` action and returned by the  GetPipelineDefinition action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/PutPipelineDefinition>`_    


    **Request Syntax** 
    ::

      response = client.put_pipeline_definition(
          pipelineId='string',
          pipelineObjects=[
              {
                  'id': 'string',
                  'name': 'string',
                  'fields': [
                      {
                          'key': 'string',
                          'stringValue': 'string',
                          'refValue': 'string'
                      },
                  ]
              },
          ],
          parameterObjects=[
              {
                  'id': 'string',
                  'attributes': [
                      {
                          'key': 'string',
                          'stringValue': 'string'
                      },
                  ]
              },
          ],
          parameterValues=[
              {
                  'id': 'string',
                  'stringValue': 'string'
              },
          ]
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type pipelineObjects: list
    :param pipelineObjects: **[REQUIRED]** 

      The objects that define the pipeline. These objects overwrite the existing pipeline definition.

      

    
      - *(dict) --* 

        Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

        

      
        - **id** *(string) --* **[REQUIRED]** 

          The ID of the object.

          

        
        - **name** *(string) --* **[REQUIRED]** 

          The name of the object.

          

        
        - **fields** *(list) --* **[REQUIRED]** 

          Key-value pairs that define the properties of the object.

          

        
          - *(dict) --* 

            A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.

            

          
            - **key** *(string) --* **[REQUIRED]** 

              The field identifier.

              

            
            - **stringValue** *(string) --* 

              The field value, expressed as a String.

              

            
            - **refValue** *(string) --* 

              The field value, expressed as the identifier of another object.

              

            
          
      
      
  
    :type parameterObjects: list
    :param parameterObjects: 

      The parameter objects used with the pipeline.

      

    
      - *(dict) --* 

        Contains information about a parameter object.

        

      
        - **id** *(string) --* **[REQUIRED]** 

          The ID of the parameter object. 

          

        
        - **attributes** *(list) --* **[REQUIRED]** 

          The attributes of the parameter object.

          

        
          - *(dict) --* 

            The attributes allowed or specified with a parameter object.

            

          
            - **key** *(string) --* **[REQUIRED]** 

              The field identifier.

              

            
            - **stringValue** *(string) --* **[REQUIRED]** 

              The field value, expressed as a String.

              

            
          
      
      
  
    :type parameterValues: list
    :param parameterValues: 

      The parameter values used with the pipeline.

      

    
      - *(dict) --* 

        A value or list of parameter values. 

        

      
        - **id** *(string) --* **[REQUIRED]** 

          The ID of the parameter value.

          

        
        - **stringValue** *(string) --* **[REQUIRED]** 

          The field value, expressed as a String.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'validationErrors': [
                {
                    'id': 'string',
                    'errors': [
                        'string',
                    ]
                },
            ],
            'validationWarnings': [
                {
                    'id': 'string',
                    'warnings': [
                        'string',
                    ]
                },
            ],
            'errored': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of PutPipelineDefinition.

        
        

        - **validationErrors** *(list) --* 

          The validation errors that are associated with the objects defined in ``pipelineObjects`` .

          
          

          - *(dict) --* 

            Defines a validation error. Validation errors prevent pipeline activation. The set of validation errors that can be returned are defined by AWS Data Pipeline.

            
            

            - **id** *(string) --* 

              The identifier of the object that contains the validation error.

              
            

            - **errors** *(list) --* 

              A description of the validation error.

              
              

              - *(string) --* 
          
        
      
        

        - **validationWarnings** *(list) --* 

          The validation warnings that are associated with the objects defined in ``pipelineObjects`` .

          
          

          - *(dict) --* 

            Defines a validation warning. Validation warnings do not prevent pipeline activation. The set of validation warnings that can be returned are defined by AWS Data Pipeline.

            
            

            - **id** *(string) --* 

              The identifier of the object that contains the validation warning.

              
            

            - **warnings** *(list) --* 

              A description of the validation warning.

              
              

              - *(string) --* 
          
        
      
        

        - **errored** *(boolean) --* 

          Indicates whether there were validation errors, and the pipeline definition is stored but cannot be activated until you correct the pipeline and call ``PutPipelineDefinition`` to commit the corrected pipeline.

          
    

  .. py:method:: query_objects(**kwargs)

    

    Queries the specified pipeline for the names of objects that match the specified set of conditions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/QueryObjects>`_    


    **Request Syntax** 
    ::

      response = client.query_objects(
          pipelineId='string',
          query={
              'selectors': [
                  {
                      'fieldName': 'string',
                      'operator': {
                          'type': 'EQ'|'REF_EQ'|'LE'|'GE'|'BETWEEN',
                          'values': [
                              'string',
                          ]
                      }
                  },
              ]
          },
          sphere='string',
          marker='string',
          limit=123
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type query: dict
    :param query: 

      The query that defines the objects to be returned. The ``Query`` object can contain a maximum of ten selectors. The conditions in the query are limited to top-level String fields in the object. These filters can be applied to components, instances, and attempts.

      

    
      - **selectors** *(list) --* 

        List of selectors that define the query. An object must satisfy all of the selectors to match the query.

        

      
        - *(dict) --* 

          A comparision that is used to determine whether a query should return this object.

          

        
          - **fieldName** *(string) --* 

            The name of the field that the operator will be applied to. The field name is the "key" portion of the field definition in the pipeline definition syntax that is used by the AWS Data Pipeline API. If the field is not set on the object, the condition fails.

            

          
          - **operator** *(dict) --* 

            Contains a logical operation for comparing the value of a field with a specified value.

            

          
            - **type** *(string) --* 

              The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ), less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ). Equal reference (``REF_EQ`` ) can be used only with reference fields. The other comparison types can be used only with String fields. The comparison types you can use apply only to certain object fields, as detailed below. 

               

              The comparison operators EQ and REF_EQ act on the following fields: 

               

               
              * name
               
              * @sphere
               
              * parent
               
              * @componentParent
               
              * @instanceParent
               
              * @status
               
              * @scheduledStartTime
               
              * @scheduledEndTime
               
              * @actualStartTime
               
              * @actualEndTime
               

               

              The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields: 

               

               
              * @scheduledStartTime
               
              * @scheduledEndTime
               
              * @actualStartTime
               
              * @actualEndTime
               

               

              Note that fields beginning with the at sign (@) are read-only and set by the web service. When you name fields, you should choose names containing only alpha-numeric values, as symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a pipeline should prefix their name with the string "my".

              

            
            - **values** *(list) --* 

              The value that the actual field value will be compared with.

              

            
              - *(string) --* 

              
          
          
        
    
    
    :type sphere: string
    :param sphere: **[REQUIRED]** 

      Indicates whether the query applies to components or instances. The possible values are: ``COMPONENT`` , ``INSTANCE`` , and ``ATTEMPT`` .

      

    
    :type marker: string
    :param marker: 

      The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call ``QueryObjects`` with the marker value from the previous call to retrieve the next set of results.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of object names that ``QueryObjects`` will return in a single call. The default value is 100. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ids': [
                'string',
            ],
            'marker': 'string',
            'hasMoreResults': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of QueryObjects.

        
        

        - **ids** *(list) --* 

          The identifiers that match the query selectors.

          
          

          - *(string) --* 
      
        

        - **marker** *(string) --* 

          The starting point for the next page of results. To view the next page of results, call ``QueryObjects`` again with this marker value. If the value is null, there are no more results.

          
        

        - **hasMoreResults** *(boolean) --* 

          Indicates whether there are more results that can be obtained by a subsequent call.

          
    

  .. py:method:: remove_tags(**kwargs)

    

    Removes existing tags from the specified pipeline.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/RemoveTags>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags(
          pipelineId='string',
          tagKeys=[
              'string',
          ]
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type tagKeys: list
    :param tagKeys: **[REQUIRED]** 

      The keys of the tags to remove.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of RemoveTags.

        
    

  .. py:method:: report_task_progress(**kwargs)

    

    Task runners call ``ReportTaskProgress`` when assigned a task to acknowledge that it has the task. If the web service does not receive this acknowledgement within 2 minutes, it assigns the task in a subsequent  PollForTask call. After this initial acknowledgement, the task runner only needs to report progress every 15 minutes to maintain its ownership of the task. You can change this reporting time from 15 minutes by specifying a ``reportProgressTimeout`` field in your pipeline.

     

    If a task runner does not report its status after 5 minutes, AWS Data Pipeline assumes that the task runner is unable to process the task and reassigns the task in a subsequent response to  PollForTask . Task runners should call ``ReportTaskProgress`` every 60 seconds.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/ReportTaskProgress>`_    


    **Request Syntax** 
    ::

      response = client.report_task_progress(
          taskId='string',
          fields=[
              {
                  'key': 'string',
                  'stringValue': 'string',
                  'refValue': 'string'
              },
          ]
      )
    :type taskId: string
    :param taskId: **[REQUIRED]** 

      The ID of the task assigned to the task runner. This value is provided in the response for  PollForTask .

      

    
    :type fields: list
    :param fields: 

      Key-value pairs that define the properties of the ReportTaskProgressInput object.

      

    
      - *(dict) --* 

        A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The field identifier.

          

        
        - **stringValue** *(string) --* 

          The field value, expressed as a String.

          

        
        - **refValue** *(string) --* 

          The field value, expressed as the identifier of another object.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'canceled': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of ReportTaskProgress.

        
        

        - **canceled** *(boolean) --* 

          If true, the calling task runner should cancel processing of the task. The task runner does not need to call  SetTaskStatus for canceled tasks.

          
    

  .. py:method:: report_task_runner_heartbeat(**kwargs)

    

    Task runners call ``ReportTaskRunnerHeartbeat`` every 15 minutes to indicate that they are operational. If the AWS Data Pipeline Task Runner is launched on a resource managed by AWS Data Pipeline, the web service can use this call to detect when the task runner application has failed and restart a new instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat>`_    


    **Request Syntax** 
    ::

      response = client.report_task_runner_heartbeat(
          taskrunnerId='string',
          workerGroup='string',
          hostname='string'
      )
    :type taskrunnerId: string
    :param taskrunnerId: **[REQUIRED]** 

      The ID of the task runner. This value should be unique across your AWS account. In the case of AWS Data Pipeline Task Runner launched on a resource managed by AWS Data Pipeline, the web service provides a unique identifier when it launches the application. If you have written a custom task runner, you should assign a unique identifier for the task runner.

      

    
    :type workerGroup: string
    :param workerGroup: 

      The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for ``workerGroup`` . There are no wildcard values permitted in ``workerGroup`` ; the string must be an exact, case-sensitive, match.

      

    
    :type hostname: string
    :param hostname: 

      The public DNS name of the task runner.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'terminate': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of ReportTaskRunnerHeartbeat.

        
        

        - **terminate** *(boolean) --* 

          Indicates whether the calling task runner should terminate.

          
    

  .. py:method:: set_status(**kwargs)

    

    Requests that the status of the specified physical or logical pipeline objects be updated in the specified pipeline. This update might not occur immediately, but is eventually consistent. The status that can be set depends on the type of object (for example, DataNode or Activity). You cannot perform this operation on ``FINISHED`` pipelines and attempting to do so returns ``InvalidRequestException`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/SetStatus>`_    


    **Request Syntax** 
    ::

      response = client.set_status(
          pipelineId='string',
          objectIds=[
              'string',
          ],
          status='string'
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline that contains the objects.

      

    
    :type objectIds: list
    :param objectIds: **[REQUIRED]** 

      The IDs of the objects. The corresponding objects can be either physical or components, but not a mix of both types.

      

    
      - *(string) --* 

      
  
    :type status: string
    :param status: **[REQUIRED]** 

      The status to be set on all the objects specified in ``objectIds`` . For components, use ``PAUSE`` or ``RESUME`` . For instances, use ``TRY_CANCEL`` , ``RERUN`` , or ``MARK_FINISHED`` .

      

    
    
    :returns: None

  .. py:method:: set_task_status(**kwargs)

    

    Task runners call ``SetTaskStatus`` to notify AWS Data Pipeline that a task is completed and provide information about the final status. A task runner makes this call regardless of whether the task was sucessful. A task runner does not need to call ``SetTaskStatus`` for tasks that are canceled by the web service during a call to  ReportTaskProgress .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/SetTaskStatus>`_    


    **Request Syntax** 
    ::

      response = client.set_task_status(
          taskId='string',
          taskStatus='FINISHED'|'FAILED'|'FALSE',
          errorId='string',
          errorMessage='string',
          errorStackTrace='string'
      )
    :type taskId: string
    :param taskId: **[REQUIRED]** 

      The ID of the task assigned to the task runner. This value is provided in the response for  PollForTask .

      

    
    :type taskStatus: string
    :param taskStatus: **[REQUIRED]** 

      If ``FINISHED`` , the task successfully completed. If ``FAILED`` , the task ended unsuccessfully. Preconditions use false.

      

    
    :type errorId: string
    :param errorId: 

      If an error occurred during the task, this value specifies the error code. This value is set on the physical attempt object. It is used to display error information to the user. It should not start with string "Service_" which is reserved by the system.

      

    
    :type errorMessage: string
    :param errorMessage: 

      If an error occurred during the task, this value specifies a text description of the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.

      

    
    :type errorStackTrace: string
    :param errorStackTrace: 

      If an error occurred during the task, this value specifies the stack trace associated with the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of SetTaskStatus.

        
    

  .. py:method:: validate_pipeline_definition(**kwargs)

    

    Validates the specified pipeline definition to ensure that it is well formed and can be run without error.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/ValidatePipelineDefinition>`_    


    **Request Syntax** 
    ::

      response = client.validate_pipeline_definition(
          pipelineId='string',
          pipelineObjects=[
              {
                  'id': 'string',
                  'name': 'string',
                  'fields': [
                      {
                          'key': 'string',
                          'stringValue': 'string',
                          'refValue': 'string'
                      },
                  ]
              },
          ],
          parameterObjects=[
              {
                  'id': 'string',
                  'attributes': [
                      {
                          'key': 'string',
                          'stringValue': 'string'
                      },
                  ]
              },
          ],
          parameterValues=[
              {
                  'id': 'string',
                  'stringValue': 'string'
              },
          ]
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type pipelineObjects: list
    :param pipelineObjects: **[REQUIRED]** 

      The objects that define the pipeline changes to validate against the pipeline.

      

    
      - *(dict) --* 

        Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

        

      
        - **id** *(string) --* **[REQUIRED]** 

          The ID of the object.

          

        
        - **name** *(string) --* **[REQUIRED]** 

          The name of the object.

          

        
        - **fields** *(list) --* **[REQUIRED]** 

          Key-value pairs that define the properties of the object.

          

        
          - *(dict) --* 

            A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.

            

          
            - **key** *(string) --* **[REQUIRED]** 

              The field identifier.

              

            
            - **stringValue** *(string) --* 

              The field value, expressed as a String.

              

            
            - **refValue** *(string) --* 

              The field value, expressed as the identifier of another object.

              

            
          
      
      
  
    :type parameterObjects: list
    :param parameterObjects: 

      The parameter objects used with the pipeline.

      

    
      - *(dict) --* 

        Contains information about a parameter object.

        

      
        - **id** *(string) --* **[REQUIRED]** 

          The ID of the parameter object. 

          

        
        - **attributes** *(list) --* **[REQUIRED]** 

          The attributes of the parameter object.

          

        
          - *(dict) --* 

            The attributes allowed or specified with a parameter object.

            

          
            - **key** *(string) --* **[REQUIRED]** 

              The field identifier.

              

            
            - **stringValue** *(string) --* **[REQUIRED]** 

              The field value, expressed as a String.

              

            
          
      
      
  
    :type parameterValues: list
    :param parameterValues: 

      The parameter values used with the pipeline.

      

    
      - *(dict) --* 

        A value or list of parameter values. 

        

      
        - **id** *(string) --* **[REQUIRED]** 

          The ID of the parameter value.

          

        
        - **stringValue** *(string) --* **[REQUIRED]** 

          The field value, expressed as a String.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'validationErrors': [
                {
                    'id': 'string',
                    'errors': [
                        'string',
                    ]
                },
            ],
            'validationWarnings': [
                {
                    'id': 'string',
                    'warnings': [
                        'string',
                    ]
                },
            ],
            'errored': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of ValidatePipelineDefinition.

        
        

        - **validationErrors** *(list) --* 

          Any validation errors that were found.

          
          

          - *(dict) --* 

            Defines a validation error. Validation errors prevent pipeline activation. The set of validation errors that can be returned are defined by AWS Data Pipeline.

            
            

            - **id** *(string) --* 

              The identifier of the object that contains the validation error.

              
            

            - **errors** *(list) --* 

              A description of the validation error.

              
              

              - *(string) --* 
          
        
      
        

        - **validationWarnings** *(list) --* 

          Any validation warnings that were found.

          
          

          - *(dict) --* 

            Defines a validation warning. Validation warnings do not prevent pipeline activation. The set of validation warnings that can be returned are defined by AWS Data Pipeline.

            
            

            - **id** *(string) --* 

              The identifier of the object that contains the validation warning.

              
            

            - **warnings** *(list) --* 

              A description of the validation warning.

              
              

              - *(string) --* 
          
        
      
        

        - **errored** *(boolean) --* 

          Indicates whether there were validation errors.

          
    

==========
Paginators
==========


The available paginators are:

* :py:class:`DataPipeline.Paginator.DescribeObjects`


* :py:class:`DataPipeline.Paginator.ListPipelines`


* :py:class:`DataPipeline.Paginator.QueryObjects`



.. py:class:: DataPipeline.Paginator.DescribeObjects

  ::

    
    paginator = client.get_paginator('describe_objects')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DataPipeline.Client.describe_objects`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/DescribeObjects>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          pipelineId='string',
          objectIds=[
              'string',
          ],
          evaluateExpressions=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline that contains the object definitions.

      

    
    :type objectIds: list
    :param objectIds: **[REQUIRED]** 

      The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to ``DescribeObjects`` .

      

    
      - *(string) --* 

      
  
    :type evaluateExpressions: boolean
    :param evaluateExpressions: 

      Indicates whether any expressions in the object should be evaluated when the object descriptions are returned.

      

    
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
            'pipelineObjects': [
                {
                    'id': 'string',
                    'name': 'string',
                    'fields': [
                        {
                            'key': 'string',
                            'stringValue': 'string',
                            'refValue': 'string'
                        },
                    ]
                },
            ],
            'hasMoreResults': True|False,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of DescribeObjects.

        
        

        - **pipelineObjects** *(list) --* 

          An array of object definitions.

          
          

          - *(dict) --* 

            Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

            
            

            - **id** *(string) --* 

              The ID of the object.

              
            

            - **name** *(string) --* 

              The name of the object.

              
            

            - **fields** *(list) --* 

              Key-value pairs that define the properties of the object.

              
              

              - *(dict) --* 

                A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.

                
                

                - **key** *(string) --* 

                  The field identifier.

                  
                

                - **stringValue** *(string) --* 

                  The field value, expressed as a String.

                  
                

                - **refValue** *(string) --* 

                  The field value, expressed as the identifier of another object.

                  
            
          
        
      
        

        - **hasMoreResults** *(boolean) --* 

          Indicates whether there are more results to return.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DataPipeline.Paginator.ListPipelines

  ::

    
    paginator = client.get_paginator('list_pipelines')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DataPipeline.Client.list_pipelines`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/ListPipelines>`_    


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
            'pipelineIdList': [
                {
                    'id': 'string',
                    'name': 'string'
                },
            ],
            'hasMoreResults': True|False,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of ListPipelines.

        
        

        - **pipelineIdList** *(list) --* 

          The pipeline identifiers. If you require additional information about the pipelines, you can use these identifiers to call  DescribePipelines and  GetPipelineDefinition .

          
          

          - *(dict) --* 

            Contains the name and identifier of a pipeline.

            
            

            - **id** *(string) --* 

              The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the form ``df-297EG78HU43EEXAMPLE`` .

              
            

            - **name** *(string) --* 

              The name of the pipeline.

              
        
      
        

        - **hasMoreResults** *(boolean) --* 

          Indicates whether there are more results that can be obtained by a subsequent call.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: DataPipeline.Paginator.QueryObjects

  ::

    
    paginator = client.get_paginator('query_objects')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`DataPipeline.Client.query_objects`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/QueryObjects>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          pipelineId='string',
          query={
              'selectors': [
                  {
                      'fieldName': 'string',
                      'operator': {
                          'type': 'EQ'|'REF_EQ'|'LE'|'GE'|'BETWEEN',
                          'values': [
                              'string',
                          ]
                      }
                  },
              ]
          },
          sphere='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type pipelineId: string
    :param pipelineId: **[REQUIRED]** 

      The ID of the pipeline.

      

    
    :type query: dict
    :param query: 

      The query that defines the objects to be returned. The ``Query`` object can contain a maximum of ten selectors. The conditions in the query are limited to top-level String fields in the object. These filters can be applied to components, instances, and attempts.

      

    
      - **selectors** *(list) --* 

        List of selectors that define the query. An object must satisfy all of the selectors to match the query.

        

      
        - *(dict) --* 

          A comparision that is used to determine whether a query should return this object.

          

        
          - **fieldName** *(string) --* 

            The name of the field that the operator will be applied to. The field name is the "key" portion of the field definition in the pipeline definition syntax that is used by the AWS Data Pipeline API. If the field is not set on the object, the condition fails.

            

          
          - **operator** *(dict) --* 

            Contains a logical operation for comparing the value of a field with a specified value.

            

          
            - **type** *(string) --* 

              The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ), less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ). Equal reference (``REF_EQ`` ) can be used only with reference fields. The other comparison types can be used only with String fields. The comparison types you can use apply only to certain object fields, as detailed below. 

               

              The comparison operators EQ and REF_EQ act on the following fields: 

               

               
              * name
               
              * @sphere
               
              * parent
               
              * @componentParent
               
              * @instanceParent
               
              * @status
               
              * @scheduledStartTime
               
              * @scheduledEndTime
               
              * @actualStartTime
               
              * @actualEndTime
               

               

              The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields: 

               

               
              * @scheduledStartTime
               
              * @scheduledEndTime
               
              * @actualStartTime
               
              * @actualEndTime
               

               

              Note that fields beginning with the at sign (@) are read-only and set by the web service. When you name fields, you should choose names containing only alpha-numeric values, as symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a pipeline should prefix their name with the string "my".

              

            
            - **values** *(list) --* 

              The value that the actual field value will be compared with.

              

            
              - *(string) --* 

              
          
          
        
    
    
    :type sphere: string
    :param sphere: **[REQUIRED]** 

      Indicates whether the query applies to components or instances. The possible values are: ``COMPONENT`` , ``INSTANCE`` , and ``ATTEMPT`` .

      

    
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
            'ids': [
                'string',
            ],
            'hasMoreResults': True|False,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the output of QueryObjects.

        
        

        - **ids** *(list) --* 

          The identifiers that match the query selectors.

          
          

          - *(string) --* 
      
        

        - **hasMoreResults** *(boolean) --* 

          Indicates whether there are more results that can be obtained by a subsequent call.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    