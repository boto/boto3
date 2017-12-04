

*************************
CostandUsageReportService
*************************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CostandUsageReportService.Client

  A low-level client representing AWS Cost and Usage Report Service::

    
    import boto3
    
    client = boto3.client('cur')

  
  These are the available methods:
  
  *   :py:meth:`~CostandUsageReportService.Client.can_paginate`

  
  *   :py:meth:`~CostandUsageReportService.Client.delete_report_definition`

  
  *   :py:meth:`~CostandUsageReportService.Client.describe_report_definitions`

  
  *   :py:meth:`~CostandUsageReportService.Client.generate_presigned_url`

  
  *   :py:meth:`~CostandUsageReportService.Client.get_paginator`

  
  *   :py:meth:`~CostandUsageReportService.Client.get_waiter`

  
  *   :py:meth:`~CostandUsageReportService.Client.put_report_definition`

  

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


  .. py:method:: delete_report_definition(**kwargs)

    Delete a specified report definition

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/DeleteReportDefinition>`_    


    **Request Syntax** 
    ::

      response = client.delete_report_definition(
          ReportName='string'
      )
    :type ReportName: string
    :param ReportName: Preferred name for a report, it has to be unique. Must starts with a number/letter, case sensitive. Limited to 256 characters.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResponseMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Response of DeleteReportDefinition
        

        - **ResponseMessage** *(string) --* A message indicates if the deletion is successful.
    

  .. py:method:: describe_report_definitions(**kwargs)

    Describe a list of report definitions owned by the account

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/DescribeReportDefinitions>`_    


    **Request Syntax** 
    ::

      response = client.describe_report_definitions(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: The max number of results returned by the operation.

    
    :type NextToken: string
    :param NextToken: A generic string.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ReportDefinitions': [
                {
                    'ReportName': 'string',
                    'TimeUnit': 'HOURLY'|'DAILY',
                    'Format': 'textORcsv',
                    'Compression': 'ZIP'|'GZIP',
                    'AdditionalSchemaElements': [
                        'RESOURCES',
                    ],
                    'S3Bucket': 'string',
                    'S3Prefix': 'string',
                    'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1',
                    'AdditionalArtifacts': [
                        'REDSHIFT'|'QUICKSIGHT',
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Response of DescribeReportDefinitions
        

        - **ReportDefinitions** *(list) --* A list of report definitions.
          

          - *(dict) --* The definition of AWS Cost and Usage Report. Customer can specify the report name, time unit, report format, compression format, S3 bucket and additional artifacts and schema elements in the definition.
            

            - **ReportName** *(string) --* Preferred name for a report, it has to be unique. Must starts with a number/letter, case sensitive. Limited to 256 characters.
            

            - **TimeUnit** *(string) --* The frequency on which report data are measured and displayed.
            

            - **Format** *(string) --* Preferred format for report.
            

            - **Compression** *(string) --* Preferred compression format for report.
            

            - **AdditionalSchemaElements** *(list) --* A list of schema elements.
              

              - *(string) --* Preference of including Resource IDs. You can include additional details about individual resource IDs in your report.
          
            

            - **S3Bucket** *(string) --* Name of customer S3 bucket.
            

            - **S3Prefix** *(string) --* Preferred report path prefix. Limited to 256 characters.
            

            - **S3Region** *(string) --* Region of customer S3 bucket.
            

            - **AdditionalArtifacts** *(list) --* A list of additional artifacts.
              

              - *(string) --* Enable support for Redshift and/or QuickSight.
          
        
      
        

        - **NextToken** *(string) --* A generic string.
    

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

        


  .. py:method:: put_report_definition(**kwargs)

    Create a new report definition

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/PutReportDefinition>`_    


    **Request Syntax** 
    ::

      response = client.put_report_definition(
          ReportDefinition={
              'ReportName': 'string',
              'TimeUnit': 'HOURLY'|'DAILY',
              'Format': 'textORcsv',
              'Compression': 'ZIP'|'GZIP',
              'AdditionalSchemaElements': [
                  'RESOURCES',
              ],
              'S3Bucket': 'string',
              'S3Prefix': 'string',
              'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1',
              'AdditionalArtifacts': [
                  'REDSHIFT'|'QUICKSIGHT',
              ]
          }
      )
    :type ReportDefinition: dict
    :param ReportDefinition: **[REQUIRED]** The definition of AWS Cost and Usage Report. Customer can specify the report name, time unit, report format, compression format, S3 bucket and additional artifacts and schema elements in the definition.

    
      - **ReportName** *(string) --* **[REQUIRED]** Preferred name for a report, it has to be unique. Must starts with a number/letter, case sensitive. Limited to 256 characters.

      
      - **TimeUnit** *(string) --* **[REQUIRED]** The frequency on which report data are measured and displayed.

      
      - **Format** *(string) --* **[REQUIRED]** Preferred format for report.

      
      - **Compression** *(string) --* **[REQUIRED]** Preferred compression format for report.

      
      - **AdditionalSchemaElements** *(list) --* **[REQUIRED]** A list of schema elements.

      
        - *(string) --* Preference of including Resource IDs. You can include additional details about individual resource IDs in your report.

        
    
      - **S3Bucket** *(string) --* **[REQUIRED]** Name of customer S3 bucket.

      
      - **S3Prefix** *(string) --* **[REQUIRED]** Preferred report path prefix. Limited to 256 characters.

      
      - **S3Region** *(string) --* **[REQUIRED]** Region of customer S3 bucket.

      
      - **AdditionalArtifacts** *(list) --* A list of additional artifacts.

      
        - *(string) --* Enable support for Redshift and/or QuickSight.

        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of PutReportDefinition
    

==========
Paginators
==========


The available paginators are:

* :py:class:`CostandUsageReportService.Paginator.DescribeReportDefinitions`



.. py:class:: CostandUsageReportService.Paginator.DescribeReportDefinitions

  ::

    
    paginator = client.get_paginator('describe_report_definitions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CostandUsageReportService.Client.describe_report_definitions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/DescribeReportDefinitions>`_    


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
            'ReportDefinitions': [
                {
                    'ReportName': 'string',
                    'TimeUnit': 'HOURLY'|'DAILY',
                    'Format': 'textORcsv',
                    'Compression': 'ZIP'|'GZIP',
                    'AdditionalSchemaElements': [
                        'RESOURCES',
                    ],
                    'S3Bucket': 'string',
                    'S3Prefix': 'string',
                    'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1',
                    'AdditionalArtifacts': [
                        'REDSHIFT'|'QUICKSIGHT',
                    ]
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* Response of DescribeReportDefinitions
        

        - **ReportDefinitions** *(list) --* A list of report definitions.
          

          - *(dict) --* The definition of AWS Cost and Usage Report. Customer can specify the report name, time unit, report format, compression format, S3 bucket and additional artifacts and schema elements in the definition.
            

            - **ReportName** *(string) --* Preferred name for a report, it has to be unique. Must starts with a number/letter, case sensitive. Limited to 256 characters.
            

            - **TimeUnit** *(string) --* The frequency on which report data are measured and displayed.
            

            - **Format** *(string) --* Preferred format for report.
            

            - **Compression** *(string) --* Preferred compression format for report.
            

            - **AdditionalSchemaElements** *(list) --* A list of schema elements.
              

              - *(string) --* Preference of including Resource IDs. You can include additional details about individual resource IDs in your report.
          
            

            - **S3Bucket** *(string) --* Name of customer S3 bucket.
            

            - **S3Prefix** *(string) --* Preferred report path prefix. Limited to 256 characters.
            

            - **S3Region** *(string) --* Region of customer S3 bucket.
            

            - **AdditionalArtifacts** *(list) --* A list of additional artifacts.
              

              - *(string) --* Enable support for Redshift and/or QuickSight.
          
        
      
    