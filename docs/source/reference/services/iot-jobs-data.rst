

****************
IoTJobsDataPlane
****************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: IoTJobsDataPlane.Client

  A low-level client representing AWS IoT Jobs Data Plane::

    
    import boto3
    
    client = boto3.client('iot-jobs-data')

  
  These are the available methods:
  
  *   :py:meth:`~IoTJobsDataPlane.Client.can_paginate`

  
  *   :py:meth:`~IoTJobsDataPlane.Client.describe_job_execution`

  
  *   :py:meth:`~IoTJobsDataPlane.Client.generate_presigned_url`

  
  *   :py:meth:`~IoTJobsDataPlane.Client.get_paginator`

  
  *   :py:meth:`~IoTJobsDataPlane.Client.get_pending_job_executions`

  
  *   :py:meth:`~IoTJobsDataPlane.Client.get_waiter`

  
  *   :py:meth:`~IoTJobsDataPlane.Client.start_next_pending_job_execution`

  
  *   :py:meth:`~IoTJobsDataPlane.Client.update_job_execution`

  

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


  .. py:method:: describe_job_execution(**kwargs)

    

    Gets details of a job execution.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/DescribeJobExecution>`_    


    **Request Syntax** 
    ::

      response = client.describe_job_execution(
          jobId='string',
          thingName='string',
          includeJobDocument=True|False,
          executionNumber=123
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The unique identifier assigned to this job when it was created.

      

    
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The thing name associated with the device the job execution is running on.

      

    
    :type includeJobDocument: boolean
    :param includeJobDocument: 

      Optional. When set to true, the response contains the job document. The default is false.

      

    
    :type executionNumber: integer
    :param executionNumber: 

      Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'execution': {
                'jobId': 'string',
                'thingName': 'string',
                'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
                'statusDetails': {
                    'string': 'string'
                },
                'queuedAt': 123,
                'startedAt': 123,
                'lastUpdatedAt': 123,
                'versionNumber': 123,
                'executionNumber': 123,
                'jobDocument': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **execution** *(dict) --* 

          Contains data about a job execution.

          
          

          - **jobId** *(string) --* 

            The unique identifier you assigned to this job when it was created.

            
          

          - **thingName** *(string) --* 

            The name of the thing that is executing the job.

            
          

          - **status** *(string) --* 

            The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED", "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

            
          

          - **statusDetails** *(dict) --* 

            A collection of name/value pairs that describe the status of the job execution.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **queuedAt** *(integer) --* 

            The time, in milliseconds since the epoch, when the job execution was enqueued.

            
          

          - **startedAt** *(integer) --* 

            The time, in milliseconds since the epoch, when the job execution was started.

            
          

          - **lastUpdatedAt** *(integer) --* 

            The time, in milliseconds since the epoch, when the job execution was last updated. 

            
          

          - **versionNumber** *(integer) --* 

            The version of the job execution. Job execution versions are incremented each time they are updated by a device.

            
          

          - **executionNumber** *(integer) --* 

            A number that identifies a particular job execution on a particular device. It can be used later in commands that return or update job execution information.

            
          

          - **jobDocument** *(string) --* 

            The content of the job document.

            
      
    

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


  .. py:method:: get_pending_job_executions(**kwargs)

    

    Gets the list of all jobs for a thing that are not in a terminal status.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/GetPendingJobExecutions>`_    


    **Request Syntax** 
    ::

      response = client.get_pending_job_executions(
          thingName='string'
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing that is executing the job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'inProgressJobs': [
                {
                    'jobId': 'string',
                    'queuedAt': 123,
                    'startedAt': 123,
                    'lastUpdatedAt': 123,
                    'versionNumber': 123,
                    'executionNumber': 123
                },
            ],
            'queuedJobs': [
                {
                    'jobId': 'string',
                    'queuedAt': 123,
                    'startedAt': 123,
                    'lastUpdatedAt': 123,
                    'versionNumber': 123,
                    'executionNumber': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **inProgressJobs** *(list) --* 

          A list of JobExecutionSummary objects with status IN_PROGRESS.

          
          

          - *(dict) --* 

            Contains a subset of information about a job execution.

            
            

            - **jobId** *(string) --* 

              The unique identifier you assigned to this job when it was created.

              
            

            - **queuedAt** *(integer) --* 

              The time, in milliseconds since the epoch, when the job execution was enqueued.

              
            

            - **startedAt** *(integer) --* 

              The time, in milliseconds since the epoch, when the job execution started.

              
            

            - **lastUpdatedAt** *(integer) --* 

              The time, in milliseconds since the epoch, when the job execution was last updated.

              
            

            - **versionNumber** *(integer) --* 

              The version of the job execution. Job execution versions are incremented each time AWS IoT Jobs receives an update from a device.

              
            

            - **executionNumber** *(integer) --* 

              A number that identifies a particular job execution on a particular device.

              
        
      
        

        - **queuedJobs** *(list) --* 

          A list of JobExecutionSummary objects with status QUEUED.

          
          

          - *(dict) --* 

            Contains a subset of information about a job execution.

            
            

            - **jobId** *(string) --* 

              The unique identifier you assigned to this job when it was created.

              
            

            - **queuedAt** *(integer) --* 

              The time, in milliseconds since the epoch, when the job execution was enqueued.

              
            

            - **startedAt** *(integer) --* 

              The time, in milliseconds since the epoch, when the job execution started.

              
            

            - **lastUpdatedAt** *(integer) --* 

              The time, in milliseconds since the epoch, when the job execution was last updated.

              
            

            - **versionNumber** *(integer) --* 

              The version of the job execution. Job execution versions are incremented each time AWS IoT Jobs receives an update from a device.

              
            

            - **executionNumber** *(integer) --* 

              A number that identifies a particular job execution on a particular device.

              
        
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: start_next_pending_job_execution(**kwargs)

    

    Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution for a thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/StartNextPendingJobExecution>`_    


    **Request Syntax** 
    ::

      response = client.start_next_pending_job_execution(
          thingName='string',
          statusDetails={
              'string': 'string'
          }
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing associated with the device.

      

    
    :type statusDetails: dict
    :param statusDetails: 

      A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'execution': {
                'jobId': 'string',
                'thingName': 'string',
                'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
                'statusDetails': {
                    'string': 'string'
                },
                'queuedAt': 123,
                'startedAt': 123,
                'lastUpdatedAt': 123,
                'versionNumber': 123,
                'executionNumber': 123,
                'jobDocument': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **execution** *(dict) --* 

          A JobExecution object.

          
          

          - **jobId** *(string) --* 

            The unique identifier you assigned to this job when it was created.

            
          

          - **thingName** *(string) --* 

            The name of the thing that is executing the job.

            
          

          - **status** *(string) --* 

            The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED", "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

            
          

          - **statusDetails** *(dict) --* 

            A collection of name/value pairs that describe the status of the job execution.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **queuedAt** *(integer) --* 

            The time, in milliseconds since the epoch, when the job execution was enqueued.

            
          

          - **startedAt** *(integer) --* 

            The time, in milliseconds since the epoch, when the job execution was started.

            
          

          - **lastUpdatedAt** *(integer) --* 

            The time, in milliseconds since the epoch, when the job execution was last updated. 

            
          

          - **versionNumber** *(integer) --* 

            The version of the job execution. Job execution versions are incremented each time they are updated by a device.

            
          

          - **executionNumber** *(integer) --* 

            A number that identifies a particular job execution on a particular device. It can be used later in commands that return or update job execution information.

            
          

          - **jobDocument** *(string) --* 

            The content of the job document.

            
      
    

  .. py:method:: update_job_execution(**kwargs)

    

    Updates the status of a job execution.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/UpdateJobExecution>`_    


    **Request Syntax** 
    ::

      response = client.update_job_execution(
          jobId='string',
          thingName='string',
          status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
          statusDetails={
              'string': 'string'
          },
          expectedVersion=123,
          includeJobExecutionState=True|False,
          includeJobDocument=True|False,
          executionNumber=123
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The unique identifier assigned to this job when it was created.

      

    
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing associated with the device.

      

    
    :type status: string
    :param status: **[REQUIRED]** 

      The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.

      

    
    :type statusDetails: dict
    :param statusDetails: 

      Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type expectedVersion: integer
    :param expectedVersion: 

      Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)

      

    
    :type includeJobExecutionState: boolean
    :param includeJobExecutionState: 

      Optional. When included and set to true, the response contains the JobExecutionState data. The default is false.

      

    
    :type includeJobDocument: boolean
    :param includeJobDocument: 

      Optional. When set to true, the response contains the job document. The default is false.

      

    
    :type executionNumber: integer
    :param executionNumber: 

      Optional. A number that identifies a particular job execution on a particular device.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'executionState': {
                'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
                'statusDetails': {
                    'string': 'string'
                },
                'versionNumber': 123
            },
            'jobDocument': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **executionState** *(dict) --* 

          A JobExecutionState object.

          
          

          - **status** *(string) --* 

            The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED", "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

            
          

          - **statusDetails** *(dict) --* 

            A collection of name/value pairs that describe the status of the job execution.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **versionNumber** *(integer) --* 

            The version of the job execution. Job execution versions are incremented each time they are updated by a device.

            
      
        

        - **jobDocument** *(string) --* 

          The contents of the Job Documents.

          
    

==========
Paginators
==========


The available paginators are:
