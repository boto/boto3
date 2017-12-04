

**************
CloudWatchLogs
**************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CloudWatchLogs.Client

  A low-level client representing Amazon CloudWatch Logs::

    
    import boto3
    
    client = boto3.client('logs')

  
  These are the available methods:
  
  *   :py:meth:`~CloudWatchLogs.Client.associate_kms_key`

  
  *   :py:meth:`~CloudWatchLogs.Client.can_paginate`

  
  *   :py:meth:`~CloudWatchLogs.Client.cancel_export_task`

  
  *   :py:meth:`~CloudWatchLogs.Client.create_export_task`

  
  *   :py:meth:`~CloudWatchLogs.Client.create_log_group`

  
  *   :py:meth:`~CloudWatchLogs.Client.create_log_stream`

  
  *   :py:meth:`~CloudWatchLogs.Client.delete_destination`

  
  *   :py:meth:`~CloudWatchLogs.Client.delete_log_group`

  
  *   :py:meth:`~CloudWatchLogs.Client.delete_log_stream`

  
  *   :py:meth:`~CloudWatchLogs.Client.delete_metric_filter`

  
  *   :py:meth:`~CloudWatchLogs.Client.delete_resource_policy`

  
  *   :py:meth:`~CloudWatchLogs.Client.delete_retention_policy`

  
  *   :py:meth:`~CloudWatchLogs.Client.delete_subscription_filter`

  
  *   :py:meth:`~CloudWatchLogs.Client.describe_destinations`

  
  *   :py:meth:`~CloudWatchLogs.Client.describe_export_tasks`

  
  *   :py:meth:`~CloudWatchLogs.Client.describe_log_groups`

  
  *   :py:meth:`~CloudWatchLogs.Client.describe_log_streams`

  
  *   :py:meth:`~CloudWatchLogs.Client.describe_metric_filters`

  
  *   :py:meth:`~CloudWatchLogs.Client.describe_resource_policies`

  
  *   :py:meth:`~CloudWatchLogs.Client.describe_subscription_filters`

  
  *   :py:meth:`~CloudWatchLogs.Client.disassociate_kms_key`

  
  *   :py:meth:`~CloudWatchLogs.Client.filter_log_events`

  
  *   :py:meth:`~CloudWatchLogs.Client.generate_presigned_url`

  
  *   :py:meth:`~CloudWatchLogs.Client.get_log_events`

  
  *   :py:meth:`~CloudWatchLogs.Client.get_paginator`

  
  *   :py:meth:`~CloudWatchLogs.Client.get_waiter`

  
  *   :py:meth:`~CloudWatchLogs.Client.list_tags_log_group`

  
  *   :py:meth:`~CloudWatchLogs.Client.put_destination`

  
  *   :py:meth:`~CloudWatchLogs.Client.put_destination_policy`

  
  *   :py:meth:`~CloudWatchLogs.Client.put_log_events`

  
  *   :py:meth:`~CloudWatchLogs.Client.put_metric_filter`

  
  *   :py:meth:`~CloudWatchLogs.Client.put_resource_policy`

  
  *   :py:meth:`~CloudWatchLogs.Client.put_retention_policy`

  
  *   :py:meth:`~CloudWatchLogs.Client.put_subscription_filter`

  
  *   :py:meth:`~CloudWatchLogs.Client.tag_log_group`

  
  *   :py:meth:`~CloudWatchLogs.Client.test_metric_filter`

  
  *   :py:meth:`~CloudWatchLogs.Client.untag_log_group`

  

  .. py:method:: associate_kms_key(**kwargs)

    

    Associates the specified AWS Key Management Service (AWS KMS) customer master key (CMK) with the specified log group.

     

    Associating an AWS KMS CMK with a log group overrides any existing associations between the log group and a CMK. After a CMK is associated with a log group, all newly ingested data for the log group is encrypted using the CMK. This association is stored as long as the data encrypted with the CMK is still within Amazon CloudWatch Logs. This enables Amazon CloudWatch Logs to decrypt this data whenever it is requested.

     

    Note that it can take up to 5 minutes for this operation to take effect.

     

    If you attempt to associate a CMK with a log group but the CMK does not exist or the CMK is disabled, you will receive an ``InvalidParameterException`` error. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/AssociateKmsKey>`_    


    **Request Syntax** 
    ::

      response = client.associate_kms_key(
          logGroupName='string',
          kmsKeyId='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type kmsKeyId: string
    :param kmsKeyId: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the CMK to use when encrypting log data. For more information, see `Amazon Resource Names - AWS Key Management Service (AWS KMS) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__ .

      

    
    
    :returns: None

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


  .. py:method:: cancel_export_task(**kwargs)

    

    Cancels the specified export task.

     

    The task must be in the ``PENDING`` or ``RUNNING`` state.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/CancelExportTask>`_    


    **Request Syntax** 
    ::

      response = client.cancel_export_task(
          taskId='string'
      )
    :type taskId: string
    :param taskId: **[REQUIRED]** 

      The ID of the export task.

      

    
    
    :returns: None

  .. py:method:: create_export_task(**kwargs)

    

    Creates an export task, which allows you to efficiently export data from a log group to an Amazon S3 bucket.

     

    This is an asynchronous call. If all the required information is provided, this operation initiates an export task and responds with the ID of the task. After the task has started, you can use  DescribeExportTasks to get the status of the export task. Each account can only have one active (``RUNNING`` or ``PENDING`` ) export task at a time. To cancel an export task, use  CancelExportTask .

     

    You can export logs from multiple log groups or multiple time ranges to the same S3 bucket. To separate out log data for each export task, you can specify a prefix to be used as the Amazon S3 key prefix for all exported objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/CreateExportTask>`_    


    **Request Syntax** 
    ::

      response = client.create_export_task(
          taskName='string',
          logGroupName='string',
          logStreamNamePrefix='string',
          fromTime=123,
          to=123,
          destination='string',
          destinationPrefix='string'
      )
    :type taskName: string
    :param taskName: 

      The name of the export task.

      

    
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamNamePrefix: string
    :param logStreamNamePrefix: 

      Export only log streams that match the provided prefix. If you don't specify a value, no prefix filter is applied.

      

    
    :type fromTime: integer
    :param fromTime: **[REQUIRED]** 

      The start time of the range for the request, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp earlier than this time are not exported.

      

    
    :type to: integer
    :param to: **[REQUIRED]** 

      The end time of the range for the request, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are not exported.

      

    
    :type destination: string
    :param destination: **[REQUIRED]** 

      The name of S3 bucket for the exported log data. The bucket must be in the same AWS region.

      

    
    :type destinationPrefix: string
    :param destinationPrefix: 

      The prefix used as the start of the key for every object exported. If you don't specify a value, the default is ``exportedlogs`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskId** *(string) --* 

          The ID of the export task.

          
    

  .. py:method:: create_log_group(**kwargs)

    

    Creates a log group with the specified name.

     

    You can create up to 5000 log groups per account.

     

    You must use the following guidelines when naming a log group:

     

     
    * Log group names must be unique within a region for an AWS account. 
     
    * Log group names can be between 1 and 512 characters long. 
     
    * Log group names consist of the following characters: a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period). 
     

     

    If you associate a AWS Key Management Service (AWS KMS) customer master key (CMK) with the log group, ingested data is encrypted using the CMK. This association is stored as long as the data encrypted with the CMK is still within Amazon CloudWatch Logs. This enables Amazon CloudWatch Logs to decrypt this data whenever it is requested.

     

    If you attempt to associate a CMK with the log group but the CMK does not exist or the CMK is disabled, you will receive an ``InvalidParameterException`` error. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/CreateLogGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_log_group(
          logGroupName='string',
          kmsKeyId='string',
          tags={
              'string': 'string'
          }
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type kmsKeyId: string
    :param kmsKeyId: 

      The Amazon Resource Name (ARN) of the CMK to use when encrypting log data. For more information, see `Amazon Resource Names - AWS Key Management Service (AWS KMS) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__ .

      

    
    :type tags: dict
    :param tags: 

      The key-value pairs to use for the tags.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :returns: None

  .. py:method:: create_log_stream(**kwargs)

    

    Creates a log stream for the specified log group.

     

    There is no limit on the number of log streams that you can create for a log group.

     

    You must use the following guidelines when naming a log stream:

     

     
    * Log stream names must be unique within the log group. 
     
    * Log stream names can be between 1 and 512 characters long. 
     
    * The ':' (colon) and '*' (asterisk) characters are not allowed. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/CreateLogStream>`_    


    **Request Syntax** 
    ::

      response = client.create_log_stream(
          logGroupName='string',
          logStreamName='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamName: string
    :param logStreamName: **[REQUIRED]** 

      The name of the log stream.

      

    
    
    :returns: None

  .. py:method:: delete_destination(**kwargs)

    

    Deletes the specified destination, and eventually disables all the subscription filters that publish to it. This operation does not delete the physical resource encapsulated by the destination.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DeleteDestination>`_    


    **Request Syntax** 
    ::

      response = client.delete_destination(
          destinationName='string'
      )
    :type destinationName: string
    :param destinationName: **[REQUIRED]** 

      The name of the destination.

      

    
    
    :returns: None

  .. py:method:: delete_log_group(**kwargs)

    

    Deletes the specified log group and permanently deletes all the archived log events associated with the log group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DeleteLogGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_log_group(
          logGroupName='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    
    :returns: None

  .. py:method:: delete_log_stream(**kwargs)

    

    Deletes the specified log stream and permanently deletes all the archived log events associated with the log stream.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DeleteLogStream>`_    


    **Request Syntax** 
    ::

      response = client.delete_log_stream(
          logGroupName='string',
          logStreamName='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamName: string
    :param logStreamName: **[REQUIRED]** 

      The name of the log stream.

      

    
    
    :returns: None

  .. py:method:: delete_metric_filter(**kwargs)

    

    Deletes the specified metric filter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DeleteMetricFilter>`_    


    **Request Syntax** 
    ::

      response = client.delete_metric_filter(
          logGroupName='string',
          filterName='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type filterName: string
    :param filterName: **[REQUIRED]** 

      The name of the metric filter.

      

    
    
    :returns: None

  .. py:method:: delete_resource_policy(**kwargs)

    

    Deletes a resource policy from this account. This revokes the access of the identities in that policy to put log events to this account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DeleteResourcePolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_resource_policy(
          policyName='string'
      )
    :type policyName: string
    :param policyName: 

      The name of the policy to be revoked. This parameter is required.

      

    
    
    :returns: None

  .. py:method:: delete_retention_policy(**kwargs)

    

    Deletes the specified retention policy.

     

    Log events do not expire if they belong to log groups without a retention policy.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DeleteRetentionPolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_retention_policy(
          logGroupName='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    
    :returns: None

  .. py:method:: delete_subscription_filter(**kwargs)

    

    Deletes the specified subscription filter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DeleteSubscriptionFilter>`_    


    **Request Syntax** 
    ::

      response = client.delete_subscription_filter(
          logGroupName='string',
          filterName='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type filterName: string
    :param filterName: **[REQUIRED]** 

      The name of the subscription filter.

      

    
    
    :returns: None

  .. py:method:: describe_destinations(**kwargs)

    

    Lists all your destinations. The results are ASCII-sorted by destination name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeDestinations>`_    


    **Request Syntax** 
    ::

      response = client.describe_destinations(
          DestinationNamePrefix='string',
          nextToken='string',
          limit=123
      )
    :type DestinationNamePrefix: string
    :param DestinationNamePrefix: 

      The prefix to match. If you don't specify a value, no prefix filter is applied.

      

    
    :type nextToken: string
    :param nextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type limit: integer
    :param limit: 

      The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'destinations': [
                {
                    'destinationName': 'string',
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'accessPolicy': 'string',
                    'arn': 'string',
                    'creationTime': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **destinations** *(list) --* 

          The destinations.

          
          

          - *(dict) --* 

            Represents a cross-account destination that receives subscription log events.

            
            

            - **destinationName** *(string) --* 

              The name of the destination.

              
            

            - **targetArn** *(string) --* 

              The Amazon Resource Name (ARN) of the physical target to where the log events are delivered (for example, a Kinesis stream).

              
            

            - **roleArn** *(string) --* 

              A role for impersonation, used when delivering log events to the target.

              
            

            - **accessPolicy** *(string) --* 

              An IAM policy document that governs which AWS accounts can create subscription filters against this destination.

              
            

            - **arn** *(string) --* 

              The ARN of this destination.

              
            

            - **creationTime** *(integer) --* 

              The creation time of the destination, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of items to return. The token expires after 24 hours.

          
    

  .. py:method:: describe_export_tasks(**kwargs)

    

    Lists the specified export tasks. You can list all your export tasks or filter the results based on task ID or task status.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeExportTasks>`_    


    **Request Syntax** 
    ::

      response = client.describe_export_tasks(
          taskId='string',
          statusCode='CANCELLED'|'COMPLETED'|'FAILED'|'PENDING'|'PENDING_CANCEL'|'RUNNING',
          nextToken='string',
          limit=123
      )
    :type taskId: string
    :param taskId: 

      The ID of the export task. Specifying a task ID filters the results to zero or one export tasks.

      

    
    :type statusCode: string
    :param statusCode: 

      The status code of the export task. Specifying a status code filters the results to zero or more export tasks.

      

    
    :type nextToken: string
    :param nextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type limit: integer
    :param limit: 

      The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'exportTasks': [
                {
                    'taskId': 'string',
                    'taskName': 'string',
                    'logGroupName': 'string',
                    'from': 123,
                    'to': 123,
                    'destination': 'string',
                    'destinationPrefix': 'string',
                    'status': {
                        'code': 'CANCELLED'|'COMPLETED'|'FAILED'|'PENDING'|'PENDING_CANCEL'|'RUNNING',
                        'message': 'string'
                    },
                    'executionInfo': {
                        'creationTime': 123,
                        'completionTime': 123
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **exportTasks** *(list) --* 

          The export tasks.

          
          

          - *(dict) --* 

            Represents an export task.

            
            

            - **taskId** *(string) --* 

              The ID of the export task.

              
            

            - **taskName** *(string) --* 

              The name of the export task.

              
            

            - **logGroupName** *(string) --* 

              The name of the log group from which logs data was exported.

              
            

            - **from** *(integer) --* 

              The start time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp before this time are not exported.

              
            

            - **to** *(integer) --* 

              The end time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are not exported.

              
            

            - **destination** *(string) --* 

              The name of Amazon S3 bucket to which the log data was exported.

              
            

            - **destinationPrefix** *(string) --* 

              The prefix that was used as the start of Amazon S3 key for every object exported.

              
            

            - **status** *(dict) --* 

              The status of the export task.

              
              

              - **code** *(string) --* 

                The status code of the export task.

                
              

              - **message** *(string) --* 

                The status message related to the status code.

                
          
            

            - **executionInfo** *(dict) --* 

              Execution info about the export task.

              
              

              - **creationTime** *(integer) --* 

                The creation time of the export task, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

                
              

              - **completionTime** *(integer) --* 

                The completion time of the export task, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

                
          
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of items to return. The token expires after 24 hours.

          
    

  .. py:method:: describe_log_groups(**kwargs)

    

    Lists the specified log groups. You can list all your log groups or filter the results by prefix. The results are ASCII-sorted by log group name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeLogGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_log_groups(
          logGroupNamePrefix='string',
          nextToken='string',
          limit=123
      )
    :type logGroupNamePrefix: string
    :param logGroupNamePrefix: 

      The prefix to match.

      

    
    :type nextToken: string
    :param nextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type limit: integer
    :param limit: 

      The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'logGroups': [
                {
                    'logGroupName': 'string',
                    'creationTime': 123,
                    'retentionInDays': 123,
                    'metricFilterCount': 123,
                    'arn': 'string',
                    'storedBytes': 123,
                    'kmsKeyId': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **logGroups** *(list) --* 

          The log groups.

          
          

          - *(dict) --* 

            Represents a log group.

            
            

            - **logGroupName** *(string) --* 

              The name of the log group.

              
            

            - **creationTime** *(integer) --* 

              The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **retentionInDays** *(integer) --* 

              The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.

              
            

            - **metricFilterCount** *(integer) --* 

              The number of metric filters.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the log group.

              
            

            - **storedBytes** *(integer) --* 

              The number of bytes stored.

              
            

            - **kmsKeyId** *(string) --* 

              The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.

              
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of items to return. The token expires after 24 hours.

          
    

  .. py:method:: describe_log_streams(**kwargs)

    

    Lists the log streams for the specified log group. You can list all the log streams or filter the results by prefix. You can also control how the results are ordered.

     

    This operation has a limit of five transactions per second, after which transactions are throttled.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeLogStreams>`_    


    **Request Syntax** 
    ::

      response = client.describe_log_streams(
          logGroupName='string',
          logStreamNamePrefix='string',
          orderBy='LogStreamName'|'LastEventTime',
          descending=True|False,
          nextToken='string',
          limit=123
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamNamePrefix: string
    :param logStreamNamePrefix: 

      The prefix to match.

       

      iIf ``orderBy`` is ``LastEventTime`` ,you cannot specify this parameter.

      

    
    :type orderBy: string
    :param orderBy: 

      If the value is ``LogStreamName`` , the results are ordered by log stream name. If the value is ``LastEventTime`` , the results are ordered by the event time. The default value is ``LogStreamName`` .

       

      If you order the results by event time, you cannot specify the ``logStreamNamePrefix`` parameter.

       

      lastEventTimestamp represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTimeStamp updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.

      

    
    :type descending: boolean
    :param descending: 

      If the value is true, results are returned in descending order. If the value is to false, results are returned in ascending order. The default value is false.

      

    
    :type nextToken: string
    :param nextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type limit: integer
    :param limit: 

      The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'logStreams': [
                {
                    'logStreamName': 'string',
                    'creationTime': 123,
                    'firstEventTimestamp': 123,
                    'lastEventTimestamp': 123,
                    'lastIngestionTime': 123,
                    'uploadSequenceToken': 'string',
                    'arn': 'string',
                    'storedBytes': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **logStreams** *(list) --* 

          The log streams.

          
          

          - *(dict) --* 

            Represents a log stream, which is a sequence of log events from a single emitter of logs.

            
            

            - **logStreamName** *(string) --* 

              The name of the log stream.

              
            

            - **creationTime** *(integer) --* 

              The creation time of the stream, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **firstEventTimestamp** *(integer) --* 

              The time of the first event, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **lastEventTimestamp** *(integer) --* 

              the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTime updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.

              
            

            - **lastIngestionTime** *(integer) --* 

              The ingestion time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **uploadSequenceToken** *(string) --* 

              The sequence token.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the log stream.

              
            

            - **storedBytes** *(integer) --* 

              The number of bytes stored.

              
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of items to return. The token expires after 24 hours.

          
    

  .. py:method:: describe_metric_filters(**kwargs)

    

    Lists the specified metric filters. You can list all the metric filters or filter the results by log name, prefix, metric name, or metric namespace. The results are ASCII-sorted by filter name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeMetricFilters>`_    


    **Request Syntax** 
    ::

      response = client.describe_metric_filters(
          logGroupName='string',
          filterNamePrefix='string',
          nextToken='string',
          limit=123,
          metricName='string',
          metricNamespace='string'
      )
    :type logGroupName: string
    :param logGroupName: 

      The name of the log group.

      

    
    :type filterNamePrefix: string
    :param filterNamePrefix: 

      The prefix to match.

      

    
    :type nextToken: string
    :param nextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type limit: integer
    :param limit: 

      The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

      

    
    :type metricName: string
    :param metricName: 

      The name of the CloudWatch metric to which the monitored log information should be published. For example, you may publish to a metric called ErrorCount.

      

    
    :type metricNamespace: string
    :param metricNamespace: 

      The namespace of the CloudWatch metric.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'metricFilters': [
                {
                    'filterName': 'string',
                    'filterPattern': 'string',
                    'metricTransformations': [
                        {
                            'metricName': 'string',
                            'metricNamespace': 'string',
                            'metricValue': 'string',
                            'defaultValue': 123.0
                        },
                    ],
                    'creationTime': 123,
                    'logGroupName': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **metricFilters** *(list) --* 

          The metric filters.

          
          

          - *(dict) --* 

            Metric filters express how CloudWatch Logs would extract metric observations from ingested log events and transform them into metric data in a CloudWatch metric.

            
            

            - **filterName** *(string) --* 

              The name of the metric filter.

              
            

            - **filterPattern** *(string) --* 

              A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain time stamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.

              
            

            - **metricTransformations** *(list) --* 

              The metric transformations.

              
              

              - *(dict) --* 

                Indicates how to transform ingested log events in to metric data in a CloudWatch metric.

                
                

                - **metricName** *(string) --* 

                  The name of the CloudWatch metric.

                  
                

                - **metricNamespace** *(string) --* 

                  The namespace of the CloudWatch metric.

                  
                

                - **metricValue** *(string) --* 

                  The value to publish to the CloudWatch metric when a filter pattern matches a log event.

                  
                

                - **defaultValue** *(float) --* 

                  (Optional) The value to emit when a filter pattern does not match a log event. This value can be null.

                  
            
          
            

            - **creationTime** *(integer) --* 

              The creation time of the metric filter, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **logGroupName** *(string) --* 

              The name of the log group.

              
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of items to return. The token expires after 24 hours.

          
    

  .. py:method:: describe_resource_policies(**kwargs)

    

    Lists the resource policies in this account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeResourcePolicies>`_    


    **Request Syntax** 
    ::

      response = client.describe_resource_policies(
          nextToken='string',
          limit=123
      )
    :type nextToken: string
    :param nextToken: 

      The token for the next set of items to return. The token expires after 24 hours.

      

    
    :type limit: integer
    :param limit: 

      The maximum number of resource policies to be displayed with one call of this API.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resourcePolicies': [
                {
                    'policyName': 'string',
                    'policyDocument': 'string',
                    'lastUpdatedTime': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resourcePolicies** *(list) --* 

          The resource policies that exist in this account.

          
          

          - *(dict) --* 

            A policy enabling one or more entities to put logs to a log group in this account.

            
            

            - **policyName** *(string) --* 

              The name of the resource policy.

              
            

            - **policyDocument** *(string) --* 

              The details of the policy.

              
            

            - **lastUpdatedTime** *(integer) --* 

              Time stamp showing when this policy was last updated, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of items to return. The token expires after 24 hours.

          
    

  .. py:method:: describe_subscription_filters(**kwargs)

    

    Lists the subscription filters for the specified log group. You can list all the subscription filters or filter the results by prefix. The results are ASCII-sorted by filter name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeSubscriptionFilters>`_    


    **Request Syntax** 
    ::

      response = client.describe_subscription_filters(
          logGroupName='string',
          filterNamePrefix='string',
          nextToken='string',
          limit=123
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type filterNamePrefix: string
    :param filterNamePrefix: 

      The prefix to match. If you don't specify a value, no prefix filter is applied.

      

    
    :type nextToken: string
    :param nextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type limit: integer
    :param limit: 

      The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'subscriptionFilters': [
                {
                    'filterName': 'string',
                    'logGroupName': 'string',
                    'filterPattern': 'string',
                    'destinationArn': 'string',
                    'roleArn': 'string',
                    'distribution': 'Random'|'ByLogStream',
                    'creationTime': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **subscriptionFilters** *(list) --* 

          The subscription filters.

          
          

          - *(dict) --* 

            Represents a subscription filter.

            
            

            - **filterName** *(string) --* 

              The name of the subscription filter.

              
            

            - **logGroupName** *(string) --* 

              The name of the log group.

              
            

            - **filterPattern** *(string) --* 

              A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain time stamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.

              
            

            - **destinationArn** *(string) --* 

              The Amazon Resource Name (ARN) of the destination.

              
            

            - **roleArn** *(string) --* 

              

              
            

            - **distribution** *(string) --* 

              The method used to distribute log data to the destination, which can be either random or grouped by log stream.

              
            

            - **creationTime** *(integer) --* 

              The creation time of the subscription filter, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of items to return. The token expires after 24 hours.

          
    

  .. py:method:: disassociate_kms_key(**kwargs)

    

    Disassociates the associated AWS Key Management Service (AWS KMS) customer master key (CMK) from the specified log group.

     

    After the AWS KMS CMK is disassociated from the log group, AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires permissions for the CMK whenever the encrypted data is requested.

     

    Note that it can take up to 5 minutes for this operation to take effect.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DisassociateKmsKey>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_kms_key(
          logGroupName='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    
    :returns: None

  .. py:method:: filter_log_events(**kwargs)

    

    Lists log events from the specified log group. You can list all the log events or filter the results using a filter pattern, a time range, and the name of the log stream.

     

    By default, this operation returns as many log events as can fit in 1 MB (up to 10,000 log events), or all the events found within the time range that you specify. If the results include a token, then there are more log events available, and you can get additional results by specifying the token in a subsequent call.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/FilterLogEvents>`_    


    **Request Syntax** 
    ::

      response = client.filter_log_events(
          logGroupName='string',
          logStreamNames=[
              'string',
          ],
          startTime=123,
          endTime=123,
          filterPattern='string',
          nextToken='string',
          limit=123,
          interleaved=True|False
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamNames: list
    :param logStreamNames: 

      Optional list of log stream names.

      

    
      - *(string) --* 

      
  
    :type startTime: integer
    :param startTime: 

      The start of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp before this time are not returned.

      

    
    :type endTime: integer
    :param endTime: 

      The end of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are not returned.

      

    
    :type filterPattern: string
    :param filterPattern: 

      The filter pattern to use. If not provided, all the events are matched.

      

    
    :type nextToken: string
    :param nextToken: 

      The token for the next set of events to return. (You received this token from a previous call.)

      

    
    :type limit: integer
    :param limit: 

      The maximum number of events to return. The default is 10,000 events.

      

    
    :type interleaved: boolean
    :param interleaved: 

      If the value is true, the operation makes a best effort to provide responses that contain events from multiple log streams within the log group, interleaved in a single response. If the value is false, all the matched log events in the first log stream are searched first, then those in the next log stream, and so on. The default is false.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'events': [
                {
                    'logStreamName': 'string',
                    'timestamp': 123,
                    'message': 'string',
                    'ingestionTime': 123,
                    'eventId': 'string'
                },
            ],
            'searchedLogStreams': [
                {
                    'logStreamName': 'string',
                    'searchedCompletely': True|False
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **events** *(list) --* 

          The matched events.

          
          

          - *(dict) --* 

            Represents a matched event.

            
            

            - **logStreamName** *(string) --* 

              The name of the log stream this event belongs to.

              
            

            - **timestamp** *(integer) --* 

              The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **message** *(string) --* 

              The data contained in the log event.

              
            

            - **ingestionTime** *(integer) --* 

              The time the event was ingested, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **eventId** *(string) --* 

              The ID of the event.

              
        
      
        

        - **searchedLogStreams** *(list) --* 

          Indicates which log streams have been searched and whether each has been searched completely.

          
          

          - *(dict) --* 

            Represents the search status of a log stream.

            
            

            - **logStreamName** *(string) --* 

              The name of the log stream.

              
            

            - **searchedCompletely** *(boolean) --* 

              Indicates whether all the events in this log stream were searched.

              
        
      
        

        - **nextToken** *(string) --* 

          The token to use when requesting the next set of items. The token expires after 24 hours.

          
    

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


  .. py:method:: get_log_events(**kwargs)

    

    Lists log events from the specified log stream. You can list all the log events or filter using a time range.

     

    By default, this operation returns as many log events as can fit in a response size of 1MB (up to 10,000 log events). You can get additional log events by specifying one of the tokens in a subsequent call.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/GetLogEvents>`_    


    **Request Syntax** 
    ::

      response = client.get_log_events(
          logGroupName='string',
          logStreamName='string',
          startTime=123,
          endTime=123,
          nextToken='string',
          limit=123,
          startFromHead=True|False
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamName: string
    :param logStreamName: **[REQUIRED]** 

      The name of the log stream.

      

    
    :type startTime: integer
    :param startTime: 

      The start of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp earlier than this time are not included.

      

    
    :type endTime: integer
    :param endTime: 

      The end of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are not included.

      

    
    :type nextToken: string
    :param nextToken: 

      The token for the next set of items to return. (You received this token from a previous call.)

      

    
    :type limit: integer
    :param limit: 

      The maximum number of log events returned. If you don't specify a value, the maximum is as many log events as can fit in a response size of 1 MB, up to 10,000 log events.

      

    
    :type startFromHead: boolean
    :param startFromHead: 

      If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is false.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'events': [
                {
                    'timestamp': 123,
                    'message': 'string',
                    'ingestionTime': 123
                },
            ],
            'nextForwardToken': 'string',
            'nextBackwardToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **events** *(list) --* 

          The events.

          
          

          - *(dict) --* 

            Represents a log event.

            
            

            - **timestamp** *(integer) --* 

              The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **message** *(string) --* 

              The data contained in the log event.

              
            

            - **ingestionTime** *(integer) --* 

              The time the event was ingested, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
        
      
        

        - **nextForwardToken** *(string) --* 

          The token for the next set of items in the forward direction. The token expires after 24 hours.

          
        

        - **nextBackwardToken** *(string) --* 

          The token for the next set of items in the backward direction. The token expires after 24 hours.

          
    

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

        


  .. py:method:: list_tags_log_group(**kwargs)

    

    Lists the tags for the specified log group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/ListTagsLogGroup>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_log_group(
          logGroupName='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tags': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tags** *(dict) --* 

          The tags for the log group.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: put_destination(**kwargs)

    

    Creates or updates a destination. A destination encapsulates a physical resource (such as an Amazon Kinesis stream) and enables you to subscribe to a real-time stream of log events for a different account, ingested using  PutLogEvents . Currently, the only supported physical resource is a Kinesis stream belonging to the same account as the destination.

     

    Through an access policy, a destination controls what is written to its Kinesis stream. By default, ``PutDestination`` does not set any access policy with the destination, which means a cross-account user cannot call  PutSubscriptionFilter against this destination. To enable this, the destination owner must call  PutDestinationPolicy after ``PutDestination`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutDestination>`_    


    **Request Syntax** 
    ::

      response = client.put_destination(
          destinationName='string',
          targetArn='string',
          roleArn='string'
      )
    :type destinationName: string
    :param destinationName: **[REQUIRED]** 

      A name for the destination.

      

    
    :type targetArn: string
    :param targetArn: **[REQUIRED]** 

      The ARN of an Amazon Kinesis stream to which to deliver matching log events.

      

    
    :type roleArn: string
    :param roleArn: **[REQUIRED]** 

      The ARN of an IAM role that grants CloudWatch Logs permissions to call the Amazon Kinesis PutRecord operation on the destination stream.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'destination': {
                'destinationName': 'string',
                'targetArn': 'string',
                'roleArn': 'string',
                'accessPolicy': 'string',
                'arn': 'string',
                'creationTime': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **destination** *(dict) --* 

          The destination.

          
          

          - **destinationName** *(string) --* 

            The name of the destination.

            
          

          - **targetArn** *(string) --* 

            The Amazon Resource Name (ARN) of the physical target to where the log events are delivered (for example, a Kinesis stream).

            
          

          - **roleArn** *(string) --* 

            A role for impersonation, used when delivering log events to the target.

            
          

          - **accessPolicy** *(string) --* 

            An IAM policy document that governs which AWS accounts can create subscription filters against this destination.

            
          

          - **arn** *(string) --* 

            The ARN of this destination.

            
          

          - **creationTime** *(integer) --* 

            The creation time of the destination, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

            
      
    

  .. py:method:: put_destination_policy(**kwargs)

    

    Creates or updates an access policy associated with an existing destination. An access policy is an `IAM policy document <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies_overview.html>`__ that is used to authorize claims to register a subscription filter against a given destination.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutDestinationPolicy>`_    


    **Request Syntax** 
    ::

      response = client.put_destination_policy(
          destinationName='string',
          accessPolicy='string'
      )
    :type destinationName: string
    :param destinationName: **[REQUIRED]** 

      A name for an existing destination.

      

    
    :type accessPolicy: string
    :param accessPolicy: **[REQUIRED]** 

      An IAM policy document that authorizes cross-account users to deliver their log events to the associated destination.

      

    
    
    :returns: None

  .. py:method:: put_log_events(**kwargs)

    

    Uploads a batch of log events to the specified log stream.

     

    You must include the sequence token obtained from the response of the previous call. An upload in a newly created log stream does not require a sequence token. You can also get the sequence token using  DescribeLogStreams . If you call ``PutLogEvents`` twice within a narrow time period using the same value for ``sequenceToken`` , both calls may be successful, or one may be rejected.

     

    The batch of events must satisfy the following constraints:

     

     
    * The maximum batch size is 1,048,576 bytes, and this size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event. 
     
    * None of the log events in the batch can be more than 2 hours in the future. 
     
    * None of the log events in the batch can be older than 14 days or the retention period of the log group. 
     
    * The log events in the batch must be in chronological ordered by their time stamp (the time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC). 
     
    * The maximum number of log events in a batch is 10,000. 
     
    * A batch of log events in a single request cannot span more than 24 hours. Otherwise, the operation fails. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutLogEvents>`_    


    **Request Syntax** 
    ::

      response = client.put_log_events(
          logGroupName='string',
          logStreamName='string',
          logEvents=[
              {
                  'timestamp': 123,
                  'message': 'string'
              },
          ],
          sequenceToken='string'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamName: string
    :param logStreamName: **[REQUIRED]** 

      The name of the log stream.

      

    
    :type logEvents: list
    :param logEvents: **[REQUIRED]** 

      The log events.

      

    
      - *(dict) --* 

        Represents a log event, which is a record of activity that was recorded by the application or resource being monitored.

        

      
        - **timestamp** *(integer) --* **[REQUIRED]** 

          The time the event occurred, expressed as the number of milliseconds fter Jan 1, 1970 00:00:00 UTC.

          

        
        - **message** *(string) --* **[REQUIRED]** 

          The raw event message.

          

        
      
  
    :type sequenceToken: string
    :param sequenceToken: 

      The sequence token obtained from the response of the previous ``PutLogEvents`` call. An upload in a newly created log stream does not require a sequence token. You can also get the sequence token using  DescribeLogStreams . If you call ``PutLogEvents`` twice within a narrow time period using the same value for ``sequenceToken`` , both calls may be successful, or one may be rejected.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'nextSequenceToken': 'string',
            'rejectedLogEventsInfo': {
                'tooNewLogEventStartIndex': 123,
                'tooOldLogEventEndIndex': 123,
                'expiredLogEventEndIndex': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **nextSequenceToken** *(string) --* 

          The next sequence token.

          
        

        - **rejectedLogEventsInfo** *(dict) --* 

          The rejected events.

          
          

          - **tooNewLogEventStartIndex** *(integer) --* 

            The log events that are too new.

            
          

          - **tooOldLogEventEndIndex** *(integer) --* 

            The log events that are too old.

            
          

          - **expiredLogEventEndIndex** *(integer) --* 

            The expired log events.

            
      
    

  .. py:method:: put_metric_filter(**kwargs)

    

    Creates or updates a metric filter and associates it with the specified log group. Metric filters allow you to configure rules to extract metric data from log events ingested through  PutLogEvents .

     

    The maximum number of metric filters that can be associated with a log group is 100.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutMetricFilter>`_    


    **Request Syntax** 
    ::

      response = client.put_metric_filter(
          logGroupName='string',
          filterName='string',
          filterPattern='string',
          metricTransformations=[
              {
                  'metricName': 'string',
                  'metricNamespace': 'string',
                  'metricValue': 'string',
                  'defaultValue': 123.0
              },
          ]
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type filterName: string
    :param filterName: **[REQUIRED]** 

      A name for the metric filter.

      

    
    :type filterPattern: string
    :param filterPattern: **[REQUIRED]** 

      A filter pattern for extracting metric data out of ingested log events.

      

    
    :type metricTransformations: list
    :param metricTransformations: **[REQUIRED]** 

      A collection of information that defines how metric data gets emitted.

      

    
      - *(dict) --* 

        Indicates how to transform ingested log events in to metric data in a CloudWatch metric.

        

      
        - **metricName** *(string) --* **[REQUIRED]** 

          The name of the CloudWatch metric.

          

        
        - **metricNamespace** *(string) --* **[REQUIRED]** 

          The namespace of the CloudWatch metric.

          

        
        - **metricValue** *(string) --* **[REQUIRED]** 

          The value to publish to the CloudWatch metric when a filter pattern matches a log event.

          

        
        - **defaultValue** *(float) --* 

          (Optional) The value to emit when a filter pattern does not match a log event. This value can be null.

          

        
      
  
    
    :returns: None

  .. py:method:: put_resource_policy(**kwargs)

    

    Creates or updates a resource policy allowing other AWS services to put log events to this account, such as Amazon Route 53. An account can have up to 50 resource policies per region.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutResourcePolicy>`_    


    **Request Syntax** 
    ::

      response = client.put_resource_policy(
          policyName='string',
          policyDocument='string'
      )
    :type policyName: string
    :param policyName: 

      Name of the new policy. This parameter is required.

      

    
    :type policyDocument: string
    :param policyDocument: 

      Details of the new policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string.

       

      The following example creates a resource policy enabling the Route 53 service to put DNS query logs in to the specified log group. Replace "logArn" with the ARN of your CloudWatch Logs resource, such as a log group or log stream.

       

      { "Version": "2012-10-17" "Statement": [ { "Sid": "Route53LogsToCloudWatchLogs", "Effect": "Allow", "Principal": { "Service": [ "route53.amazonaws.com" ] }, "Action":"logs:PutLogEvents", "Resource": logArn } ] } 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resourcePolicy': {
                'policyName': 'string',
                'policyDocument': 'string',
                'lastUpdatedTime': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resourcePolicy** *(dict) --* 

          The new policy.

          
          

          - **policyName** *(string) --* 

            The name of the resource policy.

            
          

          - **policyDocument** *(string) --* 

            The details of the policy.

            
          

          - **lastUpdatedTime** *(integer) --* 

            Time stamp showing when this policy was last updated, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

            
      
    

  .. py:method:: put_retention_policy(**kwargs)

    

    Sets the retention of the specified log group. A retention policy allows you to configure the number of days for which to retain log events in the specified log group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutRetentionPolicy>`_    


    **Request Syntax** 
    ::

      response = client.put_retention_policy(
          logGroupName='string',
          retentionInDays=123
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type retentionInDays: integer
    :param retentionInDays: **[REQUIRED]** 

      The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.

      

    
    
    :returns: None

  .. py:method:: put_subscription_filter(**kwargs)

    

    Creates or updates a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events ingested through  PutLogEvents and have them delivered to a specific destination. Currently, the supported destinations are:

     

     
    * An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery. 
     
    * A logical destination that belongs to a different account, for cross-account delivery. 
     
    * An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery. 
     
    * An AWS Lambda function that belongs to the same account as the subscription filter, for same-account delivery. 
     

     

    There can only be one subscription filter associated with a log group. If you are updating an existing filter, you must specify the correct name in ``filterName`` . Otherwise, the call fails because you cannot associate a second filter with a log group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutSubscriptionFilter>`_    


    **Request Syntax** 
    ::

      response = client.put_subscription_filter(
          logGroupName='string',
          filterName='string',
          filterPattern='string',
          destinationArn='string',
          roleArn='string',
          distribution='Random'|'ByLogStream'
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type filterName: string
    :param filterName: **[REQUIRED]** 

      A name for the subscription filter. If you are updating an existing filter, you must specify the correct name in ``filterName`` . Otherwise, the call fails because you cannot associate a second filter with a log group. To find the name of the filter currently associated with a log group, use  DescribeSubscriptionFilters .

      

    
    :type filterPattern: string
    :param filterPattern: **[REQUIRED]** 

      A filter pattern for subscribing to a filtered stream of log events.

      

    
    :type destinationArn: string
    :param destinationArn: **[REQUIRED]** 

      The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:

       

       
      * An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery. 
       
      * A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery. 
       
      * An Amazon Kinesis Firehose delivery stream belonging to the same account as the subscription filter, for same-account delivery. 
       
      * An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery. 
       

      

    
    :type roleArn: string
    :param roleArn: 

      The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.

      

    
    :type distribution: string
    :param distribution: 

      The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. 

      

    
    
    :returns: None

  .. py:method:: tag_log_group(**kwargs)

    

    Adds or updates the specified tags for the specified log group.

     

    To list the tags for a log group, use  ListTagsLogGroup . To remove tags, use  UntagLogGroup .

     

    For more information about tags, see `Tag Log Groups in Amazon CloudWatch Logs <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/log-group-tagging.html>`__ in the *Amazon CloudWatch Logs User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/TagLogGroup>`_    


    **Request Syntax** 
    ::

      response = client.tag_log_group(
          logGroupName='string',
          tags={
              'string': 'string'
          }
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type tags: dict
    :param tags: **[REQUIRED]** 

      The key-value pairs to use for the tags.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :returns: None

  .. py:method:: test_metric_filter(**kwargs)

    

    Tests the filter pattern of a metric filter against a sample of log event messages. You can use this operation to validate the correctness of a metric filter pattern.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/TestMetricFilter>`_    


    **Request Syntax** 
    ::

      response = client.test_metric_filter(
          filterPattern='string',
          logEventMessages=[
              'string',
          ]
      )
    :type filterPattern: string
    :param filterPattern: **[REQUIRED]** 

      A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain time stamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.

      

    
    :type logEventMessages: list
    :param logEventMessages: **[REQUIRED]** 

      The log event messages to test.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'matches': [
                {
                    'eventNumber': 123,
                    'eventMessage': 'string',
                    'extractedValues': {
                        'string': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **matches** *(list) --* 

          The matched events.

          
          

          - *(dict) --* 

            Represents a matched event.

            
            

            - **eventNumber** *(integer) --* 

              The event number.

              
            

            - **eventMessage** *(string) --* 

              The raw event data.

              
            

            - **extractedValues** *(dict) --* 

              The values extracted from the event data by the filter.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
    

  .. py:method:: untag_log_group(**kwargs)

    

    Removes the specified tags from the specified log group.

     

    To list the tags for a log group, use  ListTagsLogGroup . To add tags, use  UntagLogGroup .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/UntagLogGroup>`_    


    **Request Syntax** 
    ::

      response = client.untag_log_group(
          logGroupName='string',
          tags=[
              'string',
          ]
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type tags: list
    :param tags: **[REQUIRED]** 

      The tag keys. The corresponding tags are removed from the log group.

      

    
      - *(string) --* 

      
  
    
    :returns: None

==========
Paginators
==========


The available paginators are:

* :py:class:`CloudWatchLogs.Paginator.DescribeDestinations`


* :py:class:`CloudWatchLogs.Paginator.DescribeLogGroups`


* :py:class:`CloudWatchLogs.Paginator.DescribeLogStreams`


* :py:class:`CloudWatchLogs.Paginator.DescribeMetricFilters`


* :py:class:`CloudWatchLogs.Paginator.DescribeSubscriptionFilters`


* :py:class:`CloudWatchLogs.Paginator.FilterLogEvents`



.. py:class:: CloudWatchLogs.Paginator.DescribeDestinations

  ::

    
    paginator = client.get_paginator('describe_destinations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatchLogs.Client.describe_destinations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeDestinations>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          DestinationNamePrefix='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type DestinationNamePrefix: string
    :param DestinationNamePrefix: 

      The prefix to match. If you don't specify a value, no prefix filter is applied.

      

    
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
            'destinations': [
                {
                    'destinationName': 'string',
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'accessPolicy': 'string',
                    'arn': 'string',
                    'creationTime': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **destinations** *(list) --* 

          The destinations.

          
          

          - *(dict) --* 

            Represents a cross-account destination that receives subscription log events.

            
            

            - **destinationName** *(string) --* 

              The name of the destination.

              
            

            - **targetArn** *(string) --* 

              The Amazon Resource Name (ARN) of the physical target to where the log events are delivered (for example, a Kinesis stream).

              
            

            - **roleArn** *(string) --* 

              A role for impersonation, used when delivering log events to the target.

              
            

            - **accessPolicy** *(string) --* 

              An IAM policy document that governs which AWS accounts can create subscription filters against this destination.

              
            

            - **arn** *(string) --* 

              The ARN of this destination.

              
            

            - **creationTime** *(integer) --* 

              The creation time of the destination, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CloudWatchLogs.Paginator.DescribeLogGroups

  ::

    
    paginator = client.get_paginator('describe_log_groups')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatchLogs.Client.describe_log_groups`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeLogGroups>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          logGroupNamePrefix='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type logGroupNamePrefix: string
    :param logGroupNamePrefix: 

      The prefix to match.

      

    
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
            'logGroups': [
                {
                    'logGroupName': 'string',
                    'creationTime': 123,
                    'retentionInDays': 123,
                    'metricFilterCount': 123,
                    'arn': 'string',
                    'storedBytes': 123,
                    'kmsKeyId': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **logGroups** *(list) --* 

          The log groups.

          
          

          - *(dict) --* 

            Represents a log group.

            
            

            - **logGroupName** *(string) --* 

              The name of the log group.

              
            

            - **creationTime** *(integer) --* 

              The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **retentionInDays** *(integer) --* 

              The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.

              
            

            - **metricFilterCount** *(integer) --* 

              The number of metric filters.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the log group.

              
            

            - **storedBytes** *(integer) --* 

              The number of bytes stored.

              
            

            - **kmsKeyId** *(string) --* 

              The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CloudWatchLogs.Paginator.DescribeLogStreams

  ::

    
    paginator = client.get_paginator('describe_log_streams')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatchLogs.Client.describe_log_streams`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeLogStreams>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          logGroupName='string',
          logStreamNamePrefix='string',
          orderBy='LogStreamName'|'LastEventTime',
          descending=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamNamePrefix: string
    :param logStreamNamePrefix: 

      The prefix to match.

       

      iIf ``orderBy`` is ``LastEventTime`` ,you cannot specify this parameter.

      

    
    :type orderBy: string
    :param orderBy: 

      If the value is ``LogStreamName`` , the results are ordered by log stream name. If the value is ``LastEventTime`` , the results are ordered by the event time. The default value is ``LogStreamName`` .

       

      If you order the results by event time, you cannot specify the ``logStreamNamePrefix`` parameter.

       

      lastEventTimestamp represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTimeStamp updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.

      

    
    :type descending: boolean
    :param descending: 

      If the value is true, results are returned in descending order. If the value is to false, results are returned in ascending order. The default value is false.

      

    
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
            'logStreams': [
                {
                    'logStreamName': 'string',
                    'creationTime': 123,
                    'firstEventTimestamp': 123,
                    'lastEventTimestamp': 123,
                    'lastIngestionTime': 123,
                    'uploadSequenceToken': 'string',
                    'arn': 'string',
                    'storedBytes': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **logStreams** *(list) --* 

          The log streams.

          
          

          - *(dict) --* 

            Represents a log stream, which is a sequence of log events from a single emitter of logs.

            
            

            - **logStreamName** *(string) --* 

              The name of the log stream.

              
            

            - **creationTime** *(integer) --* 

              The creation time of the stream, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **firstEventTimestamp** *(integer) --* 

              The time of the first event, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **lastEventTimestamp** *(integer) --* 

              the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTime updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.

              
            

            - **lastIngestionTime** *(integer) --* 

              The ingestion time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **uploadSequenceToken** *(string) --* 

              The sequence token.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the log stream.

              
            

            - **storedBytes** *(integer) --* 

              The number of bytes stored.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CloudWatchLogs.Paginator.DescribeMetricFilters

  ::

    
    paginator = client.get_paginator('describe_metric_filters')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatchLogs.Client.describe_metric_filters`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeMetricFilters>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          logGroupName='string',
          filterNamePrefix='string',
          metricName='string',
          metricNamespace='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type logGroupName: string
    :param logGroupName: 

      The name of the log group.

      

    
    :type filterNamePrefix: string
    :param filterNamePrefix: 

      The prefix to match.

      

    
    :type metricName: string
    :param metricName: 

      The name of the CloudWatch metric to which the monitored log information should be published. For example, you may publish to a metric called ErrorCount.

      

    
    :type metricNamespace: string
    :param metricNamespace: 

      The namespace of the CloudWatch metric.

      

    
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
            'metricFilters': [
                {
                    'filterName': 'string',
                    'filterPattern': 'string',
                    'metricTransformations': [
                        {
                            'metricName': 'string',
                            'metricNamespace': 'string',
                            'metricValue': 'string',
                            'defaultValue': 123.0
                        },
                    ],
                    'creationTime': 123,
                    'logGroupName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **metricFilters** *(list) --* 

          The metric filters.

          
          

          - *(dict) --* 

            Metric filters express how CloudWatch Logs would extract metric observations from ingested log events and transform them into metric data in a CloudWatch metric.

            
            

            - **filterName** *(string) --* 

              The name of the metric filter.

              
            

            - **filterPattern** *(string) --* 

              A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain time stamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.

              
            

            - **metricTransformations** *(list) --* 

              The metric transformations.

              
              

              - *(dict) --* 

                Indicates how to transform ingested log events in to metric data in a CloudWatch metric.

                
                

                - **metricName** *(string) --* 

                  The name of the CloudWatch metric.

                  
                

                - **metricNamespace** *(string) --* 

                  The namespace of the CloudWatch metric.

                  
                

                - **metricValue** *(string) --* 

                  The value to publish to the CloudWatch metric when a filter pattern matches a log event.

                  
                

                - **defaultValue** *(float) --* 

                  (Optional) The value to emit when a filter pattern does not match a log event. This value can be null.

                  
            
          
            

            - **creationTime** *(integer) --* 

              The creation time of the metric filter, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **logGroupName** *(string) --* 

              The name of the log group.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CloudWatchLogs.Paginator.DescribeSubscriptionFilters

  ::

    
    paginator = client.get_paginator('describe_subscription_filters')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatchLogs.Client.describe_subscription_filters`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeSubscriptionFilters>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          logGroupName='string',
          filterNamePrefix='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type filterNamePrefix: string
    :param filterNamePrefix: 

      The prefix to match. If you don't specify a value, no prefix filter is applied.

      

    
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
            'subscriptionFilters': [
                {
                    'filterName': 'string',
                    'logGroupName': 'string',
                    'filterPattern': 'string',
                    'destinationArn': 'string',
                    'roleArn': 'string',
                    'distribution': 'Random'|'ByLogStream',
                    'creationTime': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **subscriptionFilters** *(list) --* 

          The subscription filters.

          
          

          - *(dict) --* 

            Represents a subscription filter.

            
            

            - **filterName** *(string) --* 

              The name of the subscription filter.

              
            

            - **logGroupName** *(string) --* 

              The name of the log group.

              
            

            - **filterPattern** *(string) --* 

              A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain time stamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.

              
            

            - **destinationArn** *(string) --* 

              The Amazon Resource Name (ARN) of the destination.

              
            

            - **roleArn** *(string) --* 

              

              
            

            - **distribution** *(string) --* 

              The method used to distribute log data to the destination, which can be either random or grouped by log stream.

              
            

            - **creationTime** *(integer) --* 

              The creation time of the subscription filter, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: CloudWatchLogs.Paginator.FilterLogEvents

  ::

    
    paginator = client.get_paginator('filter_log_events')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatchLogs.Client.filter_log_events`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/FilterLogEvents>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          logGroupName='string',
          logStreamNames=[
              'string',
          ],
          startTime=123,
          endTime=123,
          filterPattern='string',
          interleaved=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type logGroupName: string
    :param logGroupName: **[REQUIRED]** 

      The name of the log group.

      

    
    :type logStreamNames: list
    :param logStreamNames: 

      Optional list of log stream names.

      

    
      - *(string) --* 

      
  
    :type startTime: integer
    :param startTime: 

      The start of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp before this time are not returned.

      

    
    :type endTime: integer
    :param endTime: 

      The end of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are not returned.

      

    
    :type filterPattern: string
    :param filterPattern: 

      The filter pattern to use. If not provided, all the events are matched.

      

    
    :type interleaved: boolean
    :param interleaved: 

      If the value is true, the operation makes a best effort to provide responses that contain events from multiple log streams within the log group, interleaved in a single response. If the value is false, all the matched log events in the first log stream are searched first, then those in the next log stream, and so on. The default is false.

      

    
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
            'events': [
                {
                    'logStreamName': 'string',
                    'timestamp': 123,
                    'message': 'string',
                    'ingestionTime': 123,
                    'eventId': 'string'
                },
            ],
            'searchedLogStreams': [
                {
                    'logStreamName': 'string',
                    'searchedCompletely': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **events** *(list) --* 

          The matched events.

          
          

          - *(dict) --* 

            Represents a matched event.

            
            

            - **logStreamName** *(string) --* 

              The name of the log stream this event belongs to.

              
            

            - **timestamp** *(integer) --* 

              The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **message** *(string) --* 

              The data contained in the log event.

              
            

            - **ingestionTime** *(integer) --* 

              The time the event was ingested, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

              
            

            - **eventId** *(string) --* 

              The ID of the event.

              
        
      
        

        - **searchedLogStreams** *(list) --* 

          Indicates which log streams have been searched and whether each has been searched completely.

          
          

          - *(dict) --* 

            Represents the search status of a log stream.

            
            

            - **logStreamName** *(string) --* 

              The name of the log stream.

              
            

            - **searchedCompletely** *(boolean) --* 

              Indicates whether all the events in this log stream were searched.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    