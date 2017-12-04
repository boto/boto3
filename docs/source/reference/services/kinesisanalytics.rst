

****************
KinesisAnalytics
****************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: KinesisAnalytics.Client

  A low-level client representing Amazon Kinesis Analytics::

    
    import boto3
    
    client = boto3.client('kinesisanalytics')

  
  These are the available methods:
  
  *   :py:meth:`~KinesisAnalytics.Client.add_application_cloud_watch_logging_option`

  
  *   :py:meth:`~KinesisAnalytics.Client.add_application_input`

  
  *   :py:meth:`~KinesisAnalytics.Client.add_application_input_processing_configuration`

  
  *   :py:meth:`~KinesisAnalytics.Client.add_application_output`

  
  *   :py:meth:`~KinesisAnalytics.Client.add_application_reference_data_source`

  
  *   :py:meth:`~KinesisAnalytics.Client.can_paginate`

  
  *   :py:meth:`~KinesisAnalytics.Client.create_application`

  
  *   :py:meth:`~KinesisAnalytics.Client.delete_application`

  
  *   :py:meth:`~KinesisAnalytics.Client.delete_application_cloud_watch_logging_option`

  
  *   :py:meth:`~KinesisAnalytics.Client.delete_application_input_processing_configuration`

  
  *   :py:meth:`~KinesisAnalytics.Client.delete_application_output`

  
  *   :py:meth:`~KinesisAnalytics.Client.delete_application_reference_data_source`

  
  *   :py:meth:`~KinesisAnalytics.Client.describe_application`

  
  *   :py:meth:`~KinesisAnalytics.Client.discover_input_schema`

  
  *   :py:meth:`~KinesisAnalytics.Client.generate_presigned_url`

  
  *   :py:meth:`~KinesisAnalytics.Client.get_paginator`

  
  *   :py:meth:`~KinesisAnalytics.Client.get_waiter`

  
  *   :py:meth:`~KinesisAnalytics.Client.list_applications`

  
  *   :py:meth:`~KinesisAnalytics.Client.start_application`

  
  *   :py:meth:`~KinesisAnalytics.Client.stop_application`

  
  *   :py:meth:`~KinesisAnalytics.Client.update_application`

  

  .. py:method:: add_application_cloud_watch_logging_option(**kwargs)

    

    Adds a CloudWatch log stream to monitor application configuration errors. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see `Working with Amazon CloudWatch Logs <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/AddApplicationCloudWatchLoggingOption>`_    


    **Request Syntax** 
    ::

      response = client.add_application_cloud_watch_logging_option(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          CloudWatchLoggingOption={
              'LogStreamARN': 'string',
              'RoleARN': 'string'
          }
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The Kinesis Analytics application name.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      The version ID of the Kinesis Analytics application.

      

    
    :type CloudWatchLoggingOption: dict
    :param CloudWatchLoggingOption: **[REQUIRED]** 

      Provides the CloudWatch log stream Amazon Resource Name (ARN) and the IAM role ARN. Note: To write application messages to CloudWatch, the IAM role that is used must have the ``PutLogEvents`` policy action enabled.

      

    
      - **LogStreamARN** *(string) --* **[REQUIRED]** 

        ARN of the CloudWatch log to receive application messages.

        

      
      - **RoleARN** *(string) --* **[REQUIRED]** 

        IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role that is used must have the ``PutLogEvents`` policy action enabled.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: add_application_input(**kwargs)

    

    Adds a streaming source to your Amazon Kinesis application. For conceptual information, see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ . 

     

    You can add a streaming source either when you create an application or you can use this operation to add a streaming source after you create an application. For more information, see  CreateApplication .

     

    Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the  DescribeApplication operation to find the current application version. 

     

    This operation requires permissions to perform the ``kinesisanalytics:AddApplicationInput`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/AddApplicationInput>`_    


    **Request Syntax** 
    ::

      response = client.add_application_input(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          Input={
              'NamePrefix': 'string',
              'InputProcessingConfiguration': {
                  'InputLambdaProcessor': {
                      'ResourceARN': 'string',
                      'RoleARN': 'string'
                  }
              },
              'KinesisStreamsInput': {
                  'ResourceARN': 'string',
                  'RoleARN': 'string'
              },
              'KinesisFirehoseInput': {
                  'ResourceARN': 'string',
                  'RoleARN': 'string'
              },
              'InputParallelism': {
                  'Count': 123
              },
              'InputSchema': {
                  'RecordFormat': {
                      'RecordFormatType': 'JSON'|'CSV',
                      'MappingParameters': {
                          'JSONMappingParameters': {
                              'RecordRowPath': 'string'
                          },
                          'CSVMappingParameters': {
                              'RecordRowDelimiter': 'string',
                              'RecordColumnDelimiter': 'string'
                          }
                      }
                  },
                  'RecordEncoding': 'string',
                  'RecordColumns': [
                      {
                          'Name': 'string',
                          'Mapping': 'string',
                          'SqlType': 'string'
                      },
                  ]
              }
          }
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of your existing Amazon Kinesis Analytics application to which you want to add the streaming source.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      Current version of your Amazon Kinesis Analytics application. You can use the  DescribeApplication operation to find the current application version.

      

    
    :type Input: dict
    :param Input: **[REQUIRED]** 

      The  Input to add.

      

    
      - **NamePrefix** *(string) --* **[REQUIRED]** 

        Name prefix to use when creating in-application stream. Suppose you specify a prefix "MyInApplicationStream". Amazon Kinesis Analytics will then create one or more (as per the ``InputParallelism`` count you specified) in-application streams with names "MyInApplicationStream_001", "MyInApplicationStream_002" and so on. 

        

      
      - **InputProcessingConfiguration** *(dict) --* 

        The  InputProcessingConfiguration for the Input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is  InputLambdaProcessor .

        

      
        - **InputLambdaProcessor** *(dict) --* **[REQUIRED]** 

          The  InputLambdaProcessor that is used to preprocess the records in the stream prior to being processed by your application code.

          

        
          - **ResourceARN** *(string) --* **[REQUIRED]** 

            The ARN of the `AWS Lambda <https://aws.amazon.com/documentation/lambda/>`__ function that operates on records in the stream.

            

          
          - **RoleARN** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role used to access the AWS Lambda function.

            

          
        
      
      - **KinesisStreamsInput** *(dict) --* 

        If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

         

        Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

        

      
        - **ResourceARN** *(string) --* **[REQUIRED]** 

          ARN of the input Amazon Kinesis stream to read.

          

        
        - **RoleARN** *(string) --* **[REQUIRED]** 

          ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

          

        
      
      - **KinesisFirehoseInput** *(dict) --* 

        If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the Firehose delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

         

        Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

        

      
        - **ResourceARN** *(string) --* **[REQUIRED]** 

          ARN of the input Firehose delivery stream.

          

        
        - **RoleARN** *(string) --* **[REQUIRED]** 

          ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure the role has necessary permissions to access the stream.

          

        
      
      - **InputParallelism** *(dict) --* 

        Describes the number of in-application streams to create. 

         

        Data from your source will be routed to these in-application input streams.

         

        (see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

        

      
        - **Count** *(integer) --* 

          Number of in-application streams to create. For more information, see `Limits <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ . 

          

        
      
      - **InputSchema** *(dict) --* **[REQUIRED]** 

        Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

         

        Also used to describe the format of the reference data source.

        

      
        - **RecordFormat** *(dict) --* **[REQUIRED]** 

          Specifies the format of the records on the streaming source.

          

        
          - **RecordFormatType** *(string) --* **[REQUIRED]** 

            The type of record format.

            

          
          - **MappingParameters** *(dict) --* 

            When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            

          
            - **JSONMappingParameters** *(dict) --* 

              Provides additional mapping information when JSON is the record format on the streaming source.

              

            
              - **RecordRowPath** *(string) --* **[REQUIRED]** 

                Path to the top-level parent that contains the records.

                

              
            
            - **CSVMappingParameters** *(dict) --* 

              Provides additional mapping information when the record format uses delimiters (for example, CSV).

              

            
              - **RecordRowDelimiter** *(string) --* **[REQUIRED]** 

                Row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.

                

              
              - **RecordColumnDelimiter** *(string) --* **[REQUIRED]** 

                Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.

                

              
            
          
        
        - **RecordEncoding** *(string) --* 

          Specifies the encoding of the records in the streaming source. For example, UTF-8.

          

        
        - **RecordColumns** *(list) --* **[REQUIRED]** 

          A list of ``RecordColumn`` objects.

          

        
          - *(dict) --* 

            Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

             

            Also used to describe the format of the reference data source.

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              Name of the column created in the in-application input stream or reference table.

              

            
            - **Mapping** *(string) --* 

              Reference to the data element in the streaming input of the reference data source.

              

            
            - **SqlType** *(string) --* **[REQUIRED]** 

              Type of column created in the in-application input stream or reference table.

              

            
          
      
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        

        
    

  .. py:method:: add_application_input_processing_configuration(**kwargs)

    

    Adds an  InputProcessingConfiguration to an application. An input processor preprocesses records on the input stream before the application's SQL code executes. Currently, the only input processor available is `AWS Lambda <https://aws.amazon.com/documentation/lambda/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/AddApplicationInputProcessingConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.add_application_input_processing_configuration(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          InputId='string',
          InputProcessingConfiguration={
              'InputLambdaProcessor': {
                  'ResourceARN': 'string',
                  'RoleARN': 'string'
              }
          }
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of the application to which you want to add the input processing configuration.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      Version of the application to which you want to add the input processing configuration. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.

      

    
    :type InputId: string
    :param InputId: **[REQUIRED]** 

      The ID of the input configuration to which to add the input configuration. You can get a list of the input IDs for an application using the  DescribeApplication operation.

      

    
    :type InputProcessingConfiguration: dict
    :param InputProcessingConfiguration: **[REQUIRED]** 

      The  InputProcessingConfiguration to add to the application.

      

    
      - **InputLambdaProcessor** *(dict) --* **[REQUIRED]** 

        The  InputLambdaProcessor that is used to preprocess the records in the stream prior to being processed by your application code.

        

      
        - **ResourceARN** *(string) --* **[REQUIRED]** 

          The ARN of the `AWS Lambda <https://aws.amazon.com/documentation/lambda/>`__ function that operates on records in the stream.

          

        
        - **RoleARN** *(string) --* **[REQUIRED]** 

          The ARN of the IAM role used to access the AWS Lambda function.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: add_application_output(**kwargs)

    

    Adds an external destination to your Amazon Kinesis Analytics application.

     

    If you want Amazon Kinesis Analytics to deliver data from an in-application stream within your application to an external destination (such as an Amazon Kinesis stream or a Firehose delivery stream), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.

     

    You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. For conceptual information, see `Understanding Application Output (Destination) <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ . 

     

    Note that any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the  DescribeApplication operation to find the current application version.

     

    For the limits on the number of application inputs and outputs you can configure, see `Limits <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .

     

    This operation requires permissions to perform the ``kinesisanalytics:AddApplicationOutput`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/AddApplicationOutput>`_    


    **Request Syntax** 
    ::

      response = client.add_application_output(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          Output={
              'Name': 'string',
              'KinesisStreamsOutput': {
                  'ResourceARN': 'string',
                  'RoleARN': 'string'
              },
              'KinesisFirehoseOutput': {
                  'ResourceARN': 'string',
                  'RoleARN': 'string'
              },
              'DestinationSchema': {
                  'RecordFormatType': 'JSON'|'CSV'
              }
          }
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of the application to which you want to add the output configuration.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      Version of the application to which you want add the output configuration. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned. 

      

    
    :type Output: dict
    :param Output: **[REQUIRED]** 

      An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream), and record the formation to use when writing to the destination.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        Name of the in-application stream.

        

      
      - **KinesisStreamsOutput** *(dict) --* 

        Identifies an Amazon Kinesis stream as the destination.

        

      
        - **ResourceARN** *(string) --* **[REQUIRED]** 

          ARN of the destination Amazon Kinesis stream to write to.

          

        
        - **RoleARN** *(string) --* **[REQUIRED]** 

          ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.

          

        
      
      - **KinesisFirehoseOutput** *(dict) --* 

        Identifies an Amazon Kinesis Firehose delivery stream as the destination.

        

      
        - **ResourceARN** *(string) --* **[REQUIRED]** 

          ARN of the destination Amazon Kinesis Firehose delivery stream to write to.

          

        
        - **RoleARN** *(string) --* **[REQUIRED]** 

          ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.

          

        
      
      - **DestinationSchema** *(dict) --* **[REQUIRED]** 

        Describes the data format when records are written to the destination. For more information, see `Configuring Application Output <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ . 

        

      
        - **RecordFormatType** *(string) --* 

          Specifies the format of the records on the output stream.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        

        
    

  .. py:method:: add_application_reference_data_source(**kwargs)

    

    Adds a reference data source to an existing application.

     

    Amazon Kinesis Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in Amazon S3 object maps to columns in the resulting in-application table.

     

    For conceptual information, see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ . For the limits on data sources you can add to your application, see `Limits <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ . 

     

    This operation requires permissions to perform the ``kinesisanalytics:AddApplicationOutput`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource>`_    


    **Request Syntax** 
    ::

      response = client.add_application_reference_data_source(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          ReferenceDataSource={
              'TableName': 'string',
              'S3ReferenceDataSource': {
                  'BucketARN': 'string',
                  'FileKey': 'string',
                  'ReferenceRoleARN': 'string'
              },
              'ReferenceSchema': {
                  'RecordFormat': {
                      'RecordFormatType': 'JSON'|'CSV',
                      'MappingParameters': {
                          'JSONMappingParameters': {
                              'RecordRowPath': 'string'
                          },
                          'CSVMappingParameters': {
                              'RecordRowDelimiter': 'string',
                              'RecordColumnDelimiter': 'string'
                          }
                      }
                  },
                  'RecordEncoding': 'string',
                  'RecordColumns': [
                      {
                          'Name': 'string',
                          'Mapping': 'string',
                          'SqlType': 'string'
                      },
                  ]
              }
          }
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of an existing application.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      Version of the application for which you are adding the reference data source. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.

      

    
    :type ReferenceDataSource: dict
    :param ReferenceDataSource: **[REQUIRED]** 

      The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.

      

    
      - **TableName** *(string) --* **[REQUIRED]** 

        Name of the in-application table to create.

        

      
      - **S3ReferenceDataSource** *(dict) --* 

        Identifies the S3 bucket and object that contains the reference data. Also identifies the IAM role Amazon Kinesis Analytics can assume to read this object on your behalf.

         

        An Amazon Kinesis Analytics application loads reference data only once. If the data changes, you call the  UpdateApplication operation to trigger reloading of data into your application.

        

      
        - **BucketARN** *(string) --* **[REQUIRED]** 

          Amazon Resource Name (ARN) of the S3 bucket.

          

        
        - **FileKey** *(string) --* **[REQUIRED]** 

          Object key name containing reference data.

          

        
        - **ReferenceRoleARN** *(string) --* **[REQUIRED]** 

          ARN of the IAM role that the service can assume to read data on your behalf. This role must have permission for the ``s3:GetObject`` action on the object and trust policy that allows Amazon Kinesis Analytics service principal to assume this role.

          

        
      
      - **ReferenceSchema** *(dict) --* **[REQUIRED]** 

        Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

        

      
        - **RecordFormat** *(dict) --* **[REQUIRED]** 

          Specifies the format of the records on the streaming source.

          

        
          - **RecordFormatType** *(string) --* **[REQUIRED]** 

            The type of record format.

            

          
          - **MappingParameters** *(dict) --* 

            When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            

          
            - **JSONMappingParameters** *(dict) --* 

              Provides additional mapping information when JSON is the record format on the streaming source.

              

            
              - **RecordRowPath** *(string) --* **[REQUIRED]** 

                Path to the top-level parent that contains the records.

                

              
            
            - **CSVMappingParameters** *(dict) --* 

              Provides additional mapping information when the record format uses delimiters (for example, CSV).

              

            
              - **RecordRowDelimiter** *(string) --* **[REQUIRED]** 

                Row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.

                

              
              - **RecordColumnDelimiter** *(string) --* **[REQUIRED]** 

                Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.

                

              
            
          
        
        - **RecordEncoding** *(string) --* 

          Specifies the encoding of the records in the streaming source. For example, UTF-8.

          

        
        - **RecordColumns** *(list) --* **[REQUIRED]** 

          A list of ``RecordColumn`` objects.

          

        
          - *(dict) --* 

            Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

             

            Also used to describe the format of the reference data source.

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              Name of the column created in the in-application input stream or reference table.

              

            
            - **Mapping** *(string) --* 

              Reference to the data element in the streaming input of the reference data source.

              

            
            - **SqlType** *(string) --* **[REQUIRED]** 

              Type of column created in the in-application input stream or reference table.

              

            
          
      
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        

        
    

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


  .. py:method:: create_application(**kwargs)

    

    Creates an Amazon Kinesis Analytics application. You can configure each application with one streaming source as input, application code to process the input, and up to five streaming destinations where you want Amazon Kinesis Analytics to write the output data from your application. For an overview, see `How it Works <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html>`__ . 

     

    In the input configuration, you map the streaming source to an in-application stream, which you can think of as a constantly updating table. In the mapping, you must provide a schema for the in-application stream and map each data column in the in-application stream to a data element in the streaming source.

     

    Your application code is one or more SQL statements that read input data, transform it, and generate output. Your application code can create one or more SQL artifacts like SQL streams or pumps.

     

    In the output configuration, you can configure the application to write data from in-application streams created in your applications to up to five streaming destinations.

     

    To read data from your source stream or write data to destination streams, Amazon Kinesis Analytics needs your permissions. You grant these permissions by creating IAM roles. This operation requires permissions to perform the ``kinesisanalytics:CreateApplication`` action. 

     

    For introductory exercises to create an Amazon Kinesis Analytics application, see `Getting Started <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/getting-started.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/CreateApplication>`_    


    **Request Syntax** 
    ::

      response = client.create_application(
          ApplicationName='string',
          ApplicationDescription='string',
          Inputs=[
              {
                  'NamePrefix': 'string',
                  'InputProcessingConfiguration': {
                      'InputLambdaProcessor': {
                          'ResourceARN': 'string',
                          'RoleARN': 'string'
                      }
                  },
                  'KinesisStreamsInput': {
                      'ResourceARN': 'string',
                      'RoleARN': 'string'
                  },
                  'KinesisFirehoseInput': {
                      'ResourceARN': 'string',
                      'RoleARN': 'string'
                  },
                  'InputParallelism': {
                      'Count': 123
                  },
                  'InputSchema': {
                      'RecordFormat': {
                          'RecordFormatType': 'JSON'|'CSV',
                          'MappingParameters': {
                              'JSONMappingParameters': {
                                  'RecordRowPath': 'string'
                              },
                              'CSVMappingParameters': {
                                  'RecordRowDelimiter': 'string',
                                  'RecordColumnDelimiter': 'string'
                              }
                          }
                      },
                      'RecordEncoding': 'string',
                      'RecordColumns': [
                          {
                              'Name': 'string',
                              'Mapping': 'string',
                              'SqlType': 'string'
                          },
                      ]
                  }
              },
          ],
          Outputs=[
              {
                  'Name': 'string',
                  'KinesisStreamsOutput': {
                      'ResourceARN': 'string',
                      'RoleARN': 'string'
                  },
                  'KinesisFirehoseOutput': {
                      'ResourceARN': 'string',
                      'RoleARN': 'string'
                  },
                  'DestinationSchema': {
                      'RecordFormatType': 'JSON'|'CSV'
                  }
              },
          ],
          CloudWatchLoggingOptions=[
              {
                  'LogStreamARN': 'string',
                  'RoleARN': 'string'
              },
          ],
          ApplicationCode='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of your Amazon Kinesis Analytics application (for example, ``sample-app`` ).

      

    
    :type ApplicationDescription: string
    :param ApplicationDescription: 

      Summary description of the application.

      

    
    :type Inputs: list
    :param Inputs: 

      Use this parameter to configure the application input.

       

      You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table).

       

      For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf.

       

      To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.

      

    
      - *(dict) --* 

        When you configure the application input, you specify the streaming source, the in-application stream name that is created, and the mapping between the two. For more information, see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ . 

        

      
        - **NamePrefix** *(string) --* **[REQUIRED]** 

          Name prefix to use when creating in-application stream. Suppose you specify a prefix "MyInApplicationStream". Amazon Kinesis Analytics will then create one or more (as per the ``InputParallelism`` count you specified) in-application streams with names "MyInApplicationStream_001", "MyInApplicationStream_002" and so on. 

          

        
        - **InputProcessingConfiguration** *(dict) --* 

          The  InputProcessingConfiguration for the Input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is  InputLambdaProcessor .

          

        
          - **InputLambdaProcessor** *(dict) --* **[REQUIRED]** 

            The  InputLambdaProcessor that is used to preprocess the records in the stream prior to being processed by your application code.

            

          
            - **ResourceARN** *(string) --* **[REQUIRED]** 

              The ARN of the `AWS Lambda <https://aws.amazon.com/documentation/lambda/>`__ function that operates on records in the stream.

              

            
            - **RoleARN** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role used to access the AWS Lambda function.

              

            
          
        
        - **KinesisStreamsInput** *(dict) --* 

          If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

           

          Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

          

        
          - **ResourceARN** *(string) --* **[REQUIRED]** 

            ARN of the input Amazon Kinesis stream to read.

            

          
          - **RoleARN** *(string) --* **[REQUIRED]** 

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

            

          
        
        - **KinesisFirehoseInput** *(dict) --* 

          If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the Firehose delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

           

          Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

          

        
          - **ResourceARN** *(string) --* **[REQUIRED]** 

            ARN of the input Firehose delivery stream.

            

          
          - **RoleARN** *(string) --* **[REQUIRED]** 

            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure the role has necessary permissions to access the stream.

            

          
        
        - **InputParallelism** *(dict) --* 

          Describes the number of in-application streams to create. 

           

          Data from your source will be routed to these in-application input streams.

           

          (see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .

          

        
          - **Count** *(integer) --* 

            Number of in-application streams to create. For more information, see `Limits <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ . 

            

          
        
        - **InputSchema** *(dict) --* **[REQUIRED]** 

          Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

           

          Also used to describe the format of the reference data source.

          

        
          - **RecordFormat** *(dict) --* **[REQUIRED]** 

            Specifies the format of the records on the streaming source.

            

          
            - **RecordFormatType** *(string) --* **[REQUIRED]** 

              The type of record format.

              

            
            - **MappingParameters** *(dict) --* 

              When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

              

            
              - **JSONMappingParameters** *(dict) --* 

                Provides additional mapping information when JSON is the record format on the streaming source.

                

              
                - **RecordRowPath** *(string) --* **[REQUIRED]** 

                  Path to the top-level parent that contains the records.

                  

                
              
              - **CSVMappingParameters** *(dict) --* 

                Provides additional mapping information when the record format uses delimiters (for example, CSV).

                

              
                - **RecordRowDelimiter** *(string) --* **[REQUIRED]** 

                  Row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.

                  

                
                - **RecordColumnDelimiter** *(string) --* **[REQUIRED]** 

                  Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.

                  

                
              
            
          
          - **RecordEncoding** *(string) --* 

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

            

          
          - **RecordColumns** *(list) --* **[REQUIRED]** 

            A list of ``RecordColumn`` objects.

            

          
            - *(dict) --* 

              Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

               

              Also used to describe the format of the reference data source.

              

            
              - **Name** *(string) --* **[REQUIRED]** 

                Name of the column created in the in-application input stream or reference table.

                

              
              - **Mapping** *(string) --* 

                Reference to the data element in the streaming input of the reference data source.

                

              
              - **SqlType** *(string) --* **[REQUIRED]** 

                Type of column created in the in-application input stream or reference table.

                

              
            
        
        
      
  
    :type Outputs: list
    :param Outputs: 

      You can configure application output to write data from any of the in-application streams to up to five destinations.

       

      These destinations can be Amazon Kinesis streams, Amazon Kinesis Firehose delivery streams, or both.

       

      In the configuration, you specify the in-application stream name, the destination stream Amazon Resource Name (ARN), and the format to use when writing data. You must also provide an IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf.

       

      In the output configuration, you also provide the output stream Amazon Resource Name (ARN) and the format of data in the stream (for example, JSON, CSV). You also must provide an IAM role that Amazon Kinesis Analytics can assume to write to this stream on your behalf.

      

    
      - *(dict) --* 

        Describes application output configuration in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream. 

         

        

         

        For limits on how many destinations an application can write and other limitations, see `Limits <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ . 

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          Name of the in-application stream.

          

        
        - **KinesisStreamsOutput** *(dict) --* 

          Identifies an Amazon Kinesis stream as the destination.

          

        
          - **ResourceARN** *(string) --* **[REQUIRED]** 

            ARN of the destination Amazon Kinesis stream to write to.

            

          
          - **RoleARN** *(string) --* **[REQUIRED]** 

            ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.

            

          
        
        - **KinesisFirehoseOutput** *(dict) --* 

          Identifies an Amazon Kinesis Firehose delivery stream as the destination.

          

        
          - **ResourceARN** *(string) --* **[REQUIRED]** 

            ARN of the destination Amazon Kinesis Firehose delivery stream to write to.

            

          
          - **RoleARN** *(string) --* **[REQUIRED]** 

            ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.

            

          
        
        - **DestinationSchema** *(dict) --* **[REQUIRED]** 

          Describes the data format when records are written to the destination. For more information, see `Configuring Application Output <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ . 

          

        
          - **RecordFormatType** *(string) --* 

            Specifies the format of the records on the output stream.

            

          
        
      
  
    :type CloudWatchLoggingOptions: list
    :param CloudWatchLoggingOptions: 

      Use this parameter to configure a CloudWatch log stream to monitor application configuration errors. For more information, see `Working with Amazon CloudWatch Logs <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html>`__ .

      

    
      - *(dict) --* 

        Provides a description of CloudWatch logging options, including the log stream Amazon Resource Name (ARN) and the role ARN.

        

      
        - **LogStreamARN** *(string) --* **[REQUIRED]** 

          ARN of the CloudWatch log to receive application messages.

          

        
        - **RoleARN** *(string) --* **[REQUIRED]** 

          IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role that is used must have the ``PutLogEvents`` policy action enabled.

          

        
      
  
    :type ApplicationCode: string
    :param ApplicationCode: 

      One or more SQL statements that read input data, transform it, and generate output. For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more inforamtion about the typical pattern, see `Application Code <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html>`__ . 

       

      You can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps.

       

      Note that the application code must create the streams with names specified in the ``Outputs`` . For example, if your ``Outputs`` defines output streams named ``ExampleOutputStream1`` and ``ExampleOutputStream2`` , then your application code must create these streams. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationSummary': {
                'ApplicationName': 'string',
                'ApplicationARN': 'string',
                'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        TBD

        
        

        - **ApplicationSummary** *(dict) --* 

          In response to your ``CreateApplication`` request, Amazon Kinesis Analytics returns a response with a summary of the application it created, including the application Amazon Resource Name (ARN), name, and status.

          
          

          - **ApplicationName** *(string) --* 

            Name of the application.

            
          

          - **ApplicationARN** *(string) --* 

            ARN of the application.

            
          

          - **ApplicationStatus** *(string) --* 

            Status of the application.

            
      
    

  .. py:method:: delete_application(**kwargs)

    

    Deletes the specified application. Amazon Kinesis Analytics halts application execution and deletes the application, including any application artifacts (such as in-application streams, reference table, and application code).

     

    This operation requires permissions to perform the ``kinesisanalytics:DeleteApplication`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/DeleteApplication>`_    


    **Request Syntax** 
    ::

      response = client.delete_application(
          ApplicationName='string',
          CreateTimestamp=datetime(2015, 1, 1)
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of the Amazon Kinesis Analytics application to delete.

      

    
    :type CreateTimestamp: datetime
    :param CreateTimestamp: **[REQUIRED]** 

      You can use the ``DescribeApplication`` operation to get this value. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        

        
    

  .. py:method:: delete_application_cloud_watch_logging_option(**kwargs)

    

    Deletes a CloudWatch log stream from an application. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see `Working with Amazon CloudWatch Logs <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/DeleteApplicationCloudWatchLoggingOption>`_    


    **Request Syntax** 
    ::

      response = client.delete_application_cloud_watch_logging_option(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          CloudWatchLoggingOptionId='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The Kinesis Analytics application name.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      The version ID of the Kinesis Analytics application.

      

    
    :type CloudWatchLoggingOptionId: string
    :param CloudWatchLoggingOptionId: **[REQUIRED]** 

      The ``CloudWatchLoggingOptionId`` of the CloudWatch logging option to delete. You can use the  DescribeApplication operation to get the ``CloudWatchLoggingOptionId`` . 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_application_input_processing_configuration(**kwargs)

    

    Deletes an  InputProcessingConfiguration from an input.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/DeleteApplicationInputProcessingConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.delete_application_input_processing_configuration(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          InputId='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      The Kinesis Analytics application name.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      The version ID of the Kinesis Analytics application.

      

    
    :type InputId: string
    :param InputId: **[REQUIRED]** 

      The ID of the input configuration from which to delete the input configuration. You can get a list of the input IDs for an application using the  DescribeApplication operation.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_application_output(**kwargs)

    

    Deletes output destination configuration from your application configuration. Amazon Kinesis Analytics will no longer write data from the corresponding in-application stream to the external output destination.

     

    This operation requires permissions to perform the ``kinesisanalytics:DeleteApplicationOutput`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/DeleteApplicationOutput>`_    


    **Request Syntax** 
    ::

      response = client.delete_application_output(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          OutputId='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Amazon Kinesis Analytics application name.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      Amazon Kinesis Analytics application version. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned. 

      

    
    :type OutputId: string
    :param OutputId: **[REQUIRED]** 

      The ID of the configuration to delete. Each output configuration that is added to the application, either when the application is created or later using the  AddApplicationOutput operation, has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the  DescribeApplication operation to get the specific ``OutputId`` . 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        

        
    

  .. py:method:: delete_application_reference_data_source(**kwargs)

    

    Deletes a reference data source configuration from the specified application configuration.

     

    If the application is running, Amazon Kinesis Analytics immediately removes the in-application table that you created using the  AddApplicationReferenceDataSource operation. 

     

    This operation requires permissions to perform the ``kinesisanalytics.DeleteApplicationReferenceDataSource`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource>`_    


    **Request Syntax** 
    ::

      response = client.delete_application_reference_data_source(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          ReferenceId='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of an existing application.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      Version of the application. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.

      

    
    :type ReferenceId: string
    :param ReferenceId: **[REQUIRED]** 

      ID of the reference data source. When you add a reference data source to your application using the  AddApplicationReferenceDataSource , Amazon Kinesis Analytics assigns an ID. You can use the  DescribeApplication operation to get the reference ID. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_application(**kwargs)

    

    Returns information about a specific Amazon Kinesis Analytics application.

     

    If you want to retrieve a list of all applications in your account, use the  ListApplications operation.

     

    This operation requires permissions to perform the ``kinesisanalytics:DescribeApplication`` action. You can use ``DescribeApplication`` to get the current application versionId, which you need to call other operations such as ``Update`` . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/DescribeApplication>`_    


    **Request Syntax** 
    ::

      response = client.describe_application(
          ApplicationName='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of the application.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationDetail': {
                'ApplicationName': 'string',
                'ApplicationDescription': 'string',
                'ApplicationARN': 'string',
                'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
                'CreateTimestamp': datetime(2015, 1, 1),
                'LastUpdateTimestamp': datetime(2015, 1, 1),
                'InputDescriptions': [
                    {
                        'InputId': 'string',
                        'NamePrefix': 'string',
                        'InAppStreamNames': [
                            'string',
                        ],
                        'InputProcessingConfigurationDescription': {
                            'InputLambdaProcessorDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            }
                        },
                        'KinesisStreamsInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'InputSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        },
                        'InputParallelism': {
                            'Count': 123
                        },
                        'InputStartingPositionConfiguration': {
                            'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                        }
                    },
                ],
                'OutputDescriptions': [
                    {
                        'OutputId': 'string',
                        'Name': 'string',
                        'KinesisStreamsOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'DestinationSchema': {
                            'RecordFormatType': 'JSON'|'CSV'
                        }
                    },
                ],
                'ReferenceDataSourceDescriptions': [
                    {
                        'ReferenceId': 'string',
                        'TableName': 'string',
                        'S3ReferenceDataSourceDescription': {
                            'BucketARN': 'string',
                            'FileKey': 'string',
                            'ReferenceRoleARN': 'string'
                        },
                        'ReferenceSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        }
                    },
                ],
                'CloudWatchLoggingOptionDescriptions': [
                    {
                        'CloudWatchLoggingOptionId': 'string',
                        'LogStreamARN': 'string',
                        'RoleARN': 'string'
                    },
                ],
                'ApplicationCode': 'string',
                'ApplicationVersionId': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ApplicationDetail** *(dict) --* 

          Provides a description of the application, such as the application Amazon Resource Name (ARN), status, latest version, and input and output configuration details.

          
          

          - **ApplicationName** *(string) --* 

            Name of the application.

            
          

          - **ApplicationDescription** *(string) --* 

            Description of the application.

            
          

          - **ApplicationARN** *(string) --* 

            ARN of the application.

            
          

          - **ApplicationStatus** *(string) --* 

            Status of the application.

            
          

          - **CreateTimestamp** *(datetime) --* 

            Timestamp when the application version was created.

            
          

          - **LastUpdateTimestamp** *(datetime) --* 

            Timestamp when the application was last updated.

            
          

          - **InputDescriptions** *(list) --* 

            Describes the application input configuration. For more information, see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ . 

            
            

            - *(dict) --* 

              Describes the application input configuration. For more information, see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ . 

              
              

              - **InputId** *(string) --* 

                Input ID associated with the application input. This is the ID that Amazon Kinesis Analytics assigns to each input configuration you add to your application. 

                
              

              - **NamePrefix** *(string) --* 

                In-application name prefix.

                
              

              - **InAppStreamNames** *(list) --* 

                Returns the in-application stream names that are mapped to the stream source.

                
                

                - *(string) --* 
            
              

              - **InputProcessingConfigurationDescription** *(dict) --* 

                The description of the preprocessor that executes on records in this input before the application's code is run.

                
                

                - **InputLambdaProcessorDescription** *(dict) --* 

                  Provides configuration information about the associated  InputLambdaProcessorDescription .

                  
                  

                  - **ResourceARN** *(string) --* 

                    The ARN of the `AWS Lambda <https://aws.amazon.com/documentation/lambda/>`__ function that is used to preprocess the records in the stream.

                    
                  

                  - **RoleARN** *(string) --* 

                    The ARN of the IAM role used to access the AWS Lambda function.

                    
              
            
              

              - **KinesisStreamsInputDescription** *(dict) --* 

                If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

                
                

                - **ResourceARN** *(string) --* 

                  Amazon Resource Name (ARN) of the Amazon Kinesis stream.

                  
                

                - **RoleARN** *(string) --* 

                  ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

                  
            
              

              - **KinesisFirehoseInputDescription** *(dict) --* 

                If an Amazon Kinesis Firehose delivery stream is configured as a streaming source, provides the Firehose delivery stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

                
                

                - **ResourceARN** *(string) --* 

                  Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

                  
                

                - **RoleARN** *(string) --* 

                  ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.

                  
            
              

              - **InputSchema** *(dict) --* 

                Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. 

                
                

                - **RecordFormat** *(dict) --* 

                  Specifies the format of the records on the streaming source.

                  
                  

                  - **RecordFormatType** *(string) --* 

                    The type of record format.

                    
                  

                  - **MappingParameters** *(dict) --* 

                    When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

                    
                    

                    - **JSONMappingParameters** *(dict) --* 

                      Provides additional mapping information when JSON is the record format on the streaming source.

                      
                      

                      - **RecordRowPath** *(string) --* 

                        Path to the top-level parent that contains the records.

                        
                  
                    

                    - **CSVMappingParameters** *(dict) --* 

                      Provides additional mapping information when the record format uses delimiters (for example, CSV).

                      
                      

                      - **RecordRowDelimiter** *(string) --* 

                        Row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.

                        
                      

                      - **RecordColumnDelimiter** *(string) --* 

                        Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.

                        
                  
                
              
                

                - **RecordEncoding** *(string) --* 

                  Specifies the encoding of the records in the streaming source. For example, UTF-8.

                  
                

                - **RecordColumns** *(list) --* 

                  A list of ``RecordColumn`` objects.

                  
                  

                  - *(dict) --* 

                    Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

                     

                    Also used to describe the format of the reference data source.

                    
                    

                    - **Name** *(string) --* 

                      Name of the column created in the in-application input stream or reference table.

                      
                    

                    - **Mapping** *(string) --* 

                      Reference to the data element in the streaming input of the reference data source.

                      
                    

                    - **SqlType** *(string) --* 

                      Type of column created in the in-application input stream or reference table.

                      
                
              
            
              

              - **InputParallelism** *(dict) --* 

                Describes the configured parallelism (number of in-application streams mapped to the streaming source).

                
                

                - **Count** *(integer) --* 

                  Number of in-application streams to create. For more information, see `Limits <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ . 

                  
            
              

              - **InputStartingPositionConfiguration** *(dict) --* 

                Point at which the application is configured to read from the input stream.

                
                

                - **InputStartingPosition** *(string) --* 

                  The starting position on the stream.

                   

                   
                  * ``NOW`` - Start reading just after the most recent record in the stream, start at the request timestamp that the customer issued. 
                   
                  * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream. 
                   
                  * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading. 
                   

                  
            
          
        
          

          - **OutputDescriptions** *(list) --* 

            Describes the application output configuration. For more information, see `Configuring Application Output <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ . 

            
            

            - *(dict) --* 

              Describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream. 

              
              

              - **OutputId** *(string) --* 

                A unique identifier for the output configuration.

                
              

              - **Name** *(string) --* 

                Name of the in-application stream configured as output.

                
              

              - **KinesisStreamsOutputDescription** *(dict) --* 

                Describes Amazon Kinesis stream configured as the destination where output is written.

                
                

                - **ResourceARN** *(string) --* 

                  Amazon Resource Name (ARN) of the Amazon Kinesis stream.

                  
                

                - **RoleARN** *(string) --* 

                  ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

                  
            
              

              - **KinesisFirehoseOutputDescription** *(dict) --* 

                Describes the Amazon Kinesis Firehose delivery stream configured as the destination where output is written.

                
                

                - **ResourceARN** *(string) --* 

                  Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

                  
                

                - **RoleARN** *(string) --* 

                  ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

                  
            
              

              - **DestinationSchema** *(dict) --* 

                Data format used for writing data to the destination.

                
                

                - **RecordFormatType** *(string) --* 

                  Specifies the format of the records on the output stream.

                  
            
          
        
          

          - **ReferenceDataSourceDescriptions** *(list) --* 

            Describes reference data sources configured for the application. For more information, see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ . 

            
            

            - *(dict) --* 

              Describes the reference data source configured for an application.

              
              

              - **ReferenceId** *(string) --* 

                ID of the reference data source. This is the ID that Amazon Kinesis Analytics assigns when you add the reference data source to your application using the  AddApplicationReferenceDataSource operation.

                
              

              - **TableName** *(string) --* 

                The in-application table name created by the specific reference data source configuration.

                
              

              - **S3ReferenceDataSourceDescription** *(dict) --* 

                Provides the S3 bucket name, the object key name that contains the reference data. It also provides the Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application reference table.

                
                

                - **BucketARN** *(string) --* 

                  Amazon Resource Name (ARN) of the S3 bucket.

                  
                

                - **FileKey** *(string) --* 

                  Amazon S3 object key name.

                  
                

                - **ReferenceRoleARN** *(string) --* 

                  ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.

                  
            
              

              - **ReferenceSchema** *(dict) --* 

                Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

                
                

                - **RecordFormat** *(dict) --* 

                  Specifies the format of the records on the streaming source.

                  
                  

                  - **RecordFormatType** *(string) --* 

                    The type of record format.

                    
                  

                  - **MappingParameters** *(dict) --* 

                    When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

                    
                    

                    - **JSONMappingParameters** *(dict) --* 

                      Provides additional mapping information when JSON is the record format on the streaming source.

                      
                      

                      - **RecordRowPath** *(string) --* 

                        Path to the top-level parent that contains the records.

                        
                  
                    

                    - **CSVMappingParameters** *(dict) --* 

                      Provides additional mapping information when the record format uses delimiters (for example, CSV).

                      
                      

                      - **RecordRowDelimiter** *(string) --* 

                        Row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.

                        
                      

                      - **RecordColumnDelimiter** *(string) --* 

                        Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.

                        
                  
                
              
                

                - **RecordEncoding** *(string) --* 

                  Specifies the encoding of the records in the streaming source. For example, UTF-8.

                  
                

                - **RecordColumns** *(list) --* 

                  A list of ``RecordColumn`` objects.

                  
                  

                  - *(dict) --* 

                    Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

                     

                    Also used to describe the format of the reference data source.

                    
                    

                    - **Name** *(string) --* 

                      Name of the column created in the in-application input stream or reference table.

                      
                    

                    - **Mapping** *(string) --* 

                      Reference to the data element in the streaming input of the reference data source.

                      
                    

                    - **SqlType** *(string) --* 

                      Type of column created in the in-application input stream or reference table.

                      
                
              
            
          
        
          

          - **CloudWatchLoggingOptionDescriptions** *(list) --* 

            Describes the CloudWatch log streams that are configured to receive application messages. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see `Working with Amazon CloudWatch Logs <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html>`__ . 

            
            

            - *(dict) --* 

              Description of the CloudWatch logging option.

              
              

              - **CloudWatchLoggingOptionId** *(string) --* 

                ID of the CloudWatch logging option description.

                
              

              - **LogStreamARN** *(string) --* 

                ARN of the CloudWatch log to receive application messages.

                
              

              - **RoleARN** *(string) --* 

                IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the ``PutLogEvents`` policy action enabled.

                
          
        
          

          - **ApplicationCode** *(string) --* 

            Returns the application code that you provided to perform data analysis on any of the in-application streams in your application.

            
          

          - **ApplicationVersionId** *(integer) --* 

            Provides the current application version.

            
      
    

  .. py:method:: discover_input_schema(**kwargs)

    

    Infers a schema by evaluating sample records on the specified streaming source (Amazon Kinesis stream or Amazon Kinesis Firehose delivery stream). In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.

     

    You can use the inferred schema when configuring a streaming source for your application. For conceptual information, see `Configuring Application Input <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ . Note that when you create an application using the Amazon Kinesis Analytics console, the console uses this operation to infer a schema and show it in the console user interface. 

     

    This operation requires permissions to perform the ``kinesisanalytics:DiscoverInputSchema`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/DiscoverInputSchema>`_    


    **Request Syntax** 
    ::

      response = client.discover_input_schema(
          ResourceARN='string',
          RoleARN='string',
          InputStartingPositionConfiguration={
              'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
          },
          S3Configuration={
              'RoleARN': 'string',
              'BucketARN': 'string',
              'FileKey': 'string'
          },
          InputProcessingConfiguration={
              'InputLambdaProcessor': {
                  'ResourceARN': 'string',
                  'RoleARN': 'string'
              }
          }
      )
    :type ResourceARN: string
    :param ResourceARN: 

      Amazon Resource Name (ARN) of the streaming source.

      

    
    :type RoleARN: string
    :param RoleARN: 

      ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf.

      

    
    :type InputStartingPositionConfiguration: dict
    :param InputStartingPositionConfiguration: 

      Point at which you want Amazon Kinesis Analytics to start reading records from the specified streaming source discovery purposes.

      

    
      - **InputStartingPosition** *(string) --* 

        The starting position on the stream.

         

         
        * ``NOW`` - Start reading just after the most recent record in the stream, start at the request timestamp that the customer issued. 
         
        * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream. 
         
        * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading. 
         

        

      
    
    :type S3Configuration: dict
    :param S3Configuration: 

    
      - **RoleARN** *(string) --* **[REQUIRED]** 

      
      - **BucketARN** *(string) --* **[REQUIRED]** 

      
      - **FileKey** *(string) --* **[REQUIRED]** 

      
    
    :type InputProcessingConfiguration: dict
    :param InputProcessingConfiguration: 

      The  InputProcessingConfiguration to use to preprocess the records before discovering the schema of the records.

      

    
      - **InputLambdaProcessor** *(dict) --* **[REQUIRED]** 

        The  InputLambdaProcessor that is used to preprocess the records in the stream prior to being processed by your application code.

        

      
        - **ResourceARN** *(string) --* **[REQUIRED]** 

          The ARN of the `AWS Lambda <https://aws.amazon.com/documentation/lambda/>`__ function that operates on records in the stream.

          

        
        - **RoleARN** *(string) --* **[REQUIRED]** 

          The ARN of the IAM role used to access the AWS Lambda function.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InputSchema': {
                'RecordFormat': {
                    'RecordFormatType': 'JSON'|'CSV',
                    'MappingParameters': {
                        'JSONMappingParameters': {
                            'RecordRowPath': 'string'
                        },
                        'CSVMappingParameters': {
                            'RecordRowDelimiter': 'string',
                            'RecordColumnDelimiter': 'string'
                        }
                    }
                },
                'RecordEncoding': 'string',
                'RecordColumns': [
                    {
                        'Name': 'string',
                        'Mapping': 'string',
                        'SqlType': 'string'
                    },
                ]
            },
            'ParsedInputRecords': [
                [
                    'string',
                ],
            ],
            'ProcessedInputRecords': [
                'string',
            ],
            'RawInputRecords': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **InputSchema** *(dict) --* 

          Schema inferred from the streaming source. It identifies the format of the data in the streaming source and how each data element maps to corresponding columns in the in-application stream that you can create.

          
          

          - **RecordFormat** *(dict) --* 

            Specifies the format of the records on the streaming source.

            
            

            - **RecordFormatType** *(string) --* 

              The type of record format.

              
            

            - **MappingParameters** *(dict) --* 

              When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

              
              

              - **JSONMappingParameters** *(dict) --* 

                Provides additional mapping information when JSON is the record format on the streaming source.

                
                

                - **RecordRowPath** *(string) --* 

                  Path to the top-level parent that contains the records.

                  
            
              

              - **CSVMappingParameters** *(dict) --* 

                Provides additional mapping information when the record format uses delimiters (for example, CSV).

                
                

                - **RecordRowDelimiter** *(string) --* 

                  Row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.

                  
                

                - **RecordColumnDelimiter** *(string) --* 

                  Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.

                  
            
          
        
          

          - **RecordEncoding** *(string) --* 

            Specifies the encoding of the records in the streaming source. For example, UTF-8.

            
          

          - **RecordColumns** *(list) --* 

            A list of ``RecordColumn`` objects.

            
            

            - *(dict) --* 

              Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

               

              Also used to describe the format of the reference data source.

              
              

              - **Name** *(string) --* 

                Name of the column created in the in-application input stream or reference table.

                
              

              - **Mapping** *(string) --* 

                Reference to the data element in the streaming input of the reference data source.

                
              

              - **SqlType** *(string) --* 

                Type of column created in the in-application input stream or reference table.

                
          
        
      
        

        - **ParsedInputRecords** *(list) --* 

          An array of elements, where each element corresponds to a row in a stream record (a stream record can have more than one row).

          
          

          - *(list) --* 
            

            - *(string) --* 
        
      
        

        - **ProcessedInputRecords** *(list) --* 

          Stream data that was modified by the processor specified in the ``InputProcessingConfiguration`` parameter.

          
          

          - *(string) --* 
      
        

        - **RawInputRecords** *(list) --* 

          Raw stream data that was sampled to infer the schema.

          
          

          - *(string) --* 
      
    

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

        


  .. py:method:: list_applications(**kwargs)

    

    Returns a list of Amazon Kinesis Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. If the response returns the ``HasMoreApplications`` value as true, you can send another request by adding the ``ExclusiveStartApplicationName`` in the request body, and set the value of this to the last application name from the previous response. 

     

    If you want detailed information about a specific application, use  DescribeApplication .

     

    This operation requires permissions to perform the ``kinesisanalytics:ListApplications`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/ListApplications>`_    


    **Request Syntax** 
    ::

      response = client.list_applications(
          Limit=123,
          ExclusiveStartApplicationName='string'
      )
    :type Limit: integer
    :param Limit: 

      Maximum number of applications to list.

      

    
    :type ExclusiveStartApplicationName: string
    :param ExclusiveStartApplicationName: 

      Name of the application to start the list with. When using pagination to retrieve the list, you don't need to specify this parameter in the first request. However, in subsequent requests, you add the last application name from the previous response to get the next page of applications.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationSummaries': [
                {
                    'ApplicationName': 'string',
                    'ApplicationARN': 'string',
                    'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING'
                },
            ],
            'HasMoreApplications': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **ApplicationSummaries** *(list) --* 

          List of ``ApplicationSummary`` objects. 

          
          

          - *(dict) --* 

            Provides application summary information, including the application Amazon Resource Name (ARN), name, and status.

            
            

            - **ApplicationName** *(string) --* 

              Name of the application.

              
            

            - **ApplicationARN** *(string) --* 

              ARN of the application.

              
            

            - **ApplicationStatus** *(string) --* 

              Status of the application.

              
        
      
        

        - **HasMoreApplications** *(boolean) --* 

          Returns true if there are more applications to retrieve.

          
    

  .. py:method:: start_application(**kwargs)

    

    Starts the specified Amazon Kinesis Analytics application. After creating an application, you must exclusively call this operation to start your application.

     

    After the application starts, it begins consuming the input data, processes it, and writes the output to the configured destination.

     

    The application status must be ``READY`` for you to start an application. You can get the application status in the console or using the  DescribeApplication operation.

     

    After you start the application, you can stop the application from processing the input by calling the  StopApplication operation.

     

    This operation requires permissions to perform the ``kinesisanalytics:StartApplication`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/StartApplication>`_    


    **Request Syntax** 
    ::

      response = client.start_application(
          ApplicationName='string',
          InputConfigurations=[
              {
                  'Id': 'string',
                  'InputStartingPositionConfiguration': {
                      'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                  }
              },
          ]
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of the application.

      

    
    :type InputConfigurations: list
    :param InputConfigurations: **[REQUIRED]** 

      Identifies the specific input, by ID, that the application starts consuming. Amazon Kinesis Analytics starts reading the streaming source associated with the input. You can also specify where in the streaming source you want Amazon Kinesis Analytics to start reading.

      

    
      - *(dict) --* 

        When you start your application, you provide this configuration, which identifies the input source and the point in the input source at which you want the application to start processing records.

        

      
        - **Id** *(string) --* **[REQUIRED]** 

          Input source ID. You can get this ID by calling the  DescribeApplication operation.

          

        
        - **InputStartingPositionConfiguration** *(dict) --* **[REQUIRED]** 

          Point at which you want the application to start processing records from the streaming source.

          

        
          - **InputStartingPosition** *(string) --* 

            The starting position on the stream.

             

             
            * ``NOW`` - Start reading just after the most recent record in the stream, start at the request timestamp that the customer issued. 
             
            * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream. 
             
            * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading. 
             

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        

        
    

  .. py:method:: stop_application(**kwargs)

    

    Stops the application from processing input data. You can stop an application only if it is in the running state. You can use the  DescribeApplication operation to find the application state. After the application is stopped, Amazon Kinesis Analytics stops reading data from the input, the application stops processing data, and there is no output written to the destination. 

     

    This operation requires permissions to perform the ``kinesisanalytics:StopApplication`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/StopApplication>`_    


    **Request Syntax** 
    ::

      response = client.stop_application(
          ApplicationName='string'
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of the running application to stop.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        

        
    

  .. py:method:: update_application(**kwargs)

    

    Updates an existing Amazon Kinesis Analytics application. Using this API, you can update application code, input configuration, and output configuration. 

     

    Note that Amazon Kinesis Analytics updates the ``CurrentApplicationVersionId`` each time you update your application. 

     

    This operation requires permission for the ``kinesisanalytics:UpdateApplication`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/UpdateApplication>`_    


    **Request Syntax** 
    ::

      response = client.update_application(
          ApplicationName='string',
          CurrentApplicationVersionId=123,
          ApplicationUpdate={
              'InputUpdates': [
                  {
                      'InputId': 'string',
                      'NamePrefixUpdate': 'string',
                      'InputProcessingConfigurationUpdate': {
                          'InputLambdaProcessorUpdate': {
                              'ResourceARNUpdate': 'string',
                              'RoleARNUpdate': 'string'
                          }
                      },
                      'KinesisStreamsInputUpdate': {
                          'ResourceARNUpdate': 'string',
                          'RoleARNUpdate': 'string'
                      },
                      'KinesisFirehoseInputUpdate': {
                          'ResourceARNUpdate': 'string',
                          'RoleARNUpdate': 'string'
                      },
                      'InputSchemaUpdate': {
                          'RecordFormatUpdate': {
                              'RecordFormatType': 'JSON'|'CSV',
                              'MappingParameters': {
                                  'JSONMappingParameters': {
                                      'RecordRowPath': 'string'
                                  },
                                  'CSVMappingParameters': {
                                      'RecordRowDelimiter': 'string',
                                      'RecordColumnDelimiter': 'string'
                                  }
                              }
                          },
                          'RecordEncodingUpdate': 'string',
                          'RecordColumnUpdates': [
                              {
                                  'Name': 'string',
                                  'Mapping': 'string',
                                  'SqlType': 'string'
                              },
                          ]
                      },
                      'InputParallelismUpdate': {
                          'CountUpdate': 123
                      }
                  },
              ],
              'ApplicationCodeUpdate': 'string',
              'OutputUpdates': [
                  {
                      'OutputId': 'string',
                      'NameUpdate': 'string',
                      'KinesisStreamsOutputUpdate': {
                          'ResourceARNUpdate': 'string',
                          'RoleARNUpdate': 'string'
                      },
                      'KinesisFirehoseOutputUpdate': {
                          'ResourceARNUpdate': 'string',
                          'RoleARNUpdate': 'string'
                      },
                      'DestinationSchemaUpdate': {
                          'RecordFormatType': 'JSON'|'CSV'
                      }
                  },
              ],
              'ReferenceDataSourceUpdates': [
                  {
                      'ReferenceId': 'string',
                      'TableNameUpdate': 'string',
                      'S3ReferenceDataSourceUpdate': {
                          'BucketARNUpdate': 'string',
                          'FileKeyUpdate': 'string',
                          'ReferenceRoleARNUpdate': 'string'
                      },
                      'ReferenceSchemaUpdate': {
                          'RecordFormat': {
                              'RecordFormatType': 'JSON'|'CSV',
                              'MappingParameters': {
                                  'JSONMappingParameters': {
                                      'RecordRowPath': 'string'
                                  },
                                  'CSVMappingParameters': {
                                      'RecordRowDelimiter': 'string',
                                      'RecordColumnDelimiter': 'string'
                                  }
                              }
                          },
                          'RecordEncoding': 'string',
                          'RecordColumns': [
                              {
                                  'Name': 'string',
                                  'Mapping': 'string',
                                  'SqlType': 'string'
                              },
                          ]
                      }
                  },
              ],
              'CloudWatchLoggingOptionUpdates': [
                  {
                      'CloudWatchLoggingOptionId': 'string',
                      'LogStreamARNUpdate': 'string',
                      'RoleARNUpdate': 'string'
                  },
              ]
          }
      )
    :type ApplicationName: string
    :param ApplicationName: **[REQUIRED]** 

      Name of the Amazon Kinesis Analytics application to update.

      

    
    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: **[REQUIRED]** 

      The current application version ID. You can use the  DescribeApplication operation to get this value.

      

    
    :type ApplicationUpdate: dict
    :param ApplicationUpdate: **[REQUIRED]** 

      Describes application updates.

      

    
      - **InputUpdates** *(list) --* 

        Describes application input configuration updates.

        

      
        - *(dict) --* 

          Describes updates to a specific input configuration (identified by the ``InputId`` of an application). 

          

        
          - **InputId** *(string) --* **[REQUIRED]** 

            Input ID of the application input to be updated.

            

          
          - **NamePrefixUpdate** *(string) --* 

            Name prefix for in-application streams that Amazon Kinesis Analytics creates for the specific streaming source.

            

          
          - **InputProcessingConfigurationUpdate** *(dict) --* 

            Describes updates for an input processing configuration.

            

          
            - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]** 

              Provides update information for an  InputLambdaProcessor .

              

            
              - **ResourceARNUpdate** *(string) --* 

                The ARN of the new `AWS Lambda <https://aws.amazon.com/documentation/lambda/>`__ function that is used to preprocess the records in the stream.

                

              
              - **RoleARNUpdate** *(string) --* 

                The ARN of the new IAM role used to access the AWS Lambda function.

                

              
            
          
          - **KinesisStreamsInputUpdate** *(dict) --* 

            If a Amazon Kinesis stream is the streaming source to be updated, provides an updated stream ARN and IAM role ARN.

            

          
            - **ResourceARNUpdate** *(string) --* 

              Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.

              

            
            - **RoleARNUpdate** *(string) --* 

              ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

              

            
          
          - **KinesisFirehoseInputUpdate** *(dict) --* 

            If an Amazon Kinesis Firehose delivery stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN) and IAM role ARN.

            

          
            - **ResourceARNUpdate** *(string) --* 

              ARN of the input Amazon Kinesis Firehose delivery stream to read.

              

            
            - **RoleARNUpdate** *(string) --* 

              Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant necessary permissions to this role.

              

            
          
          - **InputSchemaUpdate** *(dict) --* 

            Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.

            

          
            - **RecordFormatUpdate** *(dict) --* 

              Specifies the format of the records on the streaming source.

              

            
              - **RecordFormatType** *(string) --* **[REQUIRED]** 

                The type of record format.

                

              
              - **MappingParameters** *(dict) --* 

                When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

                

              
                - **JSONMappingParameters** *(dict) --* 

                  Provides additional mapping information when JSON is the record format on the streaming source.

                  

                
                  - **RecordRowPath** *(string) --* **[REQUIRED]** 

                    Path to the top-level parent that contains the records.

                    

                  
                
                - **CSVMappingParameters** *(dict) --* 

                  Provides additional mapping information when the record format uses delimiters (for example, CSV).

                  

                
                  - **RecordRowDelimiter** *(string) --* **[REQUIRED]** 

                    Row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.

                    

                  
                  - **RecordColumnDelimiter** *(string) --* **[REQUIRED]** 

                    Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.

                    

                  
                
              
            
            - **RecordEncodingUpdate** *(string) --* 

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

              

            
            - **RecordColumnUpdates** *(list) --* 

              A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream. 

              

            
              - *(dict) --* 

                Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

                 

                Also used to describe the format of the reference data source.

                

              
                - **Name** *(string) --* **[REQUIRED]** 

                  Name of the column created in the in-application input stream or reference table.

                  

                
                - **Mapping** *(string) --* 

                  Reference to the data element in the streaming input of the reference data source.

                  

                
                - **SqlType** *(string) --* **[REQUIRED]** 

                  Type of column created in the in-application input stream or reference table.

                  

                
              
          
          
          - **InputParallelismUpdate** *(dict) --* 

            Describes the parallelism updates (the number in-application streams Amazon Kinesis Analytics creates for the specific streaming source).

            

          
            - **CountUpdate** *(integer) --* 

              Number of in-application streams to create for the specified streaming source.

              

            
          
        
    
      - **ApplicationCodeUpdate** *(string) --* 

        Describes application code updates.

        

      
      - **OutputUpdates** *(list) --* 

        Describes application output configuration updates.

        

      
        - *(dict) --* 

          Describes updates to the output configuration identified by the ``OutputId`` . 

          

        
          - **OutputId** *(string) --* **[REQUIRED]** 

            Identifies the specific output configuration that you want to update.

            

          
          - **NameUpdate** *(string) --* 

            If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.

            

          
          - **KinesisStreamsOutputUpdate** *(dict) --* 

            Describes an Amazon Kinesis stream as the destination for the output.

            

          
            - **ResourceARNUpdate** *(string) --* 

              Amazon Resource Name (ARN) of the Amazon Kinesis stream where you want to write the output.

              

            
            - **RoleARNUpdate** *(string) --* 

              ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

              

            
          
          - **KinesisFirehoseOutputUpdate** *(dict) --* 

            Describes a Amazon Kinesis Firehose delivery stream as the destination for the output.

            

          
            - **ResourceARNUpdate** *(string) --* 

              Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream to write to.

              

            
            - **RoleARNUpdate** *(string) --* 

              ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant necessary permissions to this role.

              

            
          
          - **DestinationSchemaUpdate** *(dict) --* 

            Describes the data format when records are written to the destination. For more information, see `Configuring Application Output <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ . 

            

          
            - **RecordFormatType** *(string) --* 

              Specifies the format of the records on the output stream.

              

            
          
        
    
      - **ReferenceDataSourceUpdates** *(list) --* 

        Describes application reference data source updates.

        

      
        - *(dict) --* 

          When you update a reference data source configuration for an application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.

          

        
          - **ReferenceId** *(string) --* **[REQUIRED]** 

            ID of the reference data source being updated. You can use the  DescribeApplication operation to get this value.

            

          
          - **TableNameUpdate** *(string) --* 

            In-application table name that is created by this update.

            

          
          - **S3ReferenceDataSourceUpdate** *(dict) --* 

            Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.

            

          
            - **BucketARNUpdate** *(string) --* 

              Amazon Resource Name (ARN) of the S3 bucket.

              

            
            - **FileKeyUpdate** *(string) --* 

              Object key name.

              

            
            - **ReferenceRoleARNUpdate** *(string) --* 

              ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application.

              

            
          
          - **ReferenceSchemaUpdate** *(dict) --* 

            Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

            

          
            - **RecordFormat** *(dict) --* **[REQUIRED]** 

              Specifies the format of the records on the streaming source.

              

            
              - **RecordFormatType** *(string) --* **[REQUIRED]** 

                The type of record format.

                

              
              - **MappingParameters** *(dict) --* 

                When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

                

              
                - **JSONMappingParameters** *(dict) --* 

                  Provides additional mapping information when JSON is the record format on the streaming source.

                  

                
                  - **RecordRowPath** *(string) --* **[REQUIRED]** 

                    Path to the top-level parent that contains the records.

                    

                  
                
                - **CSVMappingParameters** *(dict) --* 

                  Provides additional mapping information when the record format uses delimiters (for example, CSV).

                  

                
                  - **RecordRowDelimiter** *(string) --* **[REQUIRED]** 

                    Row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.

                    

                  
                  - **RecordColumnDelimiter** *(string) --* **[REQUIRED]** 

                    Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.

                    

                  
                
              
            
            - **RecordEncoding** *(string) --* 

              Specifies the encoding of the records in the streaming source. For example, UTF-8.

              

            
            - **RecordColumns** *(list) --* **[REQUIRED]** 

              A list of ``RecordColumn`` objects.

              

            
              - *(dict) --* 

                Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

                 

                Also used to describe the format of the reference data source.

                

              
                - **Name** *(string) --* **[REQUIRED]** 

                  Name of the column created in the in-application input stream or reference table.

                  

                
                - **Mapping** *(string) --* 

                  Reference to the data element in the streaming input of the reference data source.

                  

                
                - **SqlType** *(string) --* **[REQUIRED]** 

                  Type of column created in the in-application input stream or reference table.

                  

                
              
          
          
        
    
      - **CloudWatchLoggingOptionUpdates** *(list) --* 

        Describes application CloudWatch logging option updates.

        

      
        - *(dict) --* 

          Describes CloudWatch logging option updates.

          

        
          - **CloudWatchLoggingOptionId** *(string) --* **[REQUIRED]** 

            ID of the CloudWatch logging option to update

            

          
          - **LogStreamARNUpdate** *(string) --* 

            ARN of the CloudWatch log to receive application messages.

            

          
          - **RoleARNUpdate** *(string) --* 

            IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the ``PutLogEvents`` policy action enabled.

            

          
        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

==========
Paginators
==========


The available paginators are:
