

***************
MachineLearning
***************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: MachineLearning.Client

  A low-level client representing Amazon Machine Learning::

    
    import boto3
    
    client = boto3.client('machinelearning')

  
  These are the available methods:
  
  *   :py:meth:`~MachineLearning.Client.add_tags`

  
  *   :py:meth:`~MachineLearning.Client.can_paginate`

  
  *   :py:meth:`~MachineLearning.Client.create_batch_prediction`

  
  *   :py:meth:`~MachineLearning.Client.create_data_source_from_rds`

  
  *   :py:meth:`~MachineLearning.Client.create_data_source_from_redshift`

  
  *   :py:meth:`~MachineLearning.Client.create_data_source_from_s3`

  
  *   :py:meth:`~MachineLearning.Client.create_evaluation`

  
  *   :py:meth:`~MachineLearning.Client.create_ml_model`

  
  *   :py:meth:`~MachineLearning.Client.create_realtime_endpoint`

  
  *   :py:meth:`~MachineLearning.Client.delete_batch_prediction`

  
  *   :py:meth:`~MachineLearning.Client.delete_data_source`

  
  *   :py:meth:`~MachineLearning.Client.delete_evaluation`

  
  *   :py:meth:`~MachineLearning.Client.delete_ml_model`

  
  *   :py:meth:`~MachineLearning.Client.delete_realtime_endpoint`

  
  *   :py:meth:`~MachineLearning.Client.delete_tags`

  
  *   :py:meth:`~MachineLearning.Client.describe_batch_predictions`

  
  *   :py:meth:`~MachineLearning.Client.describe_data_sources`

  
  *   :py:meth:`~MachineLearning.Client.describe_evaluations`

  
  *   :py:meth:`~MachineLearning.Client.describe_ml_models`

  
  *   :py:meth:`~MachineLearning.Client.describe_tags`

  
  *   :py:meth:`~MachineLearning.Client.generate_presigned_url`

  
  *   :py:meth:`~MachineLearning.Client.get_batch_prediction`

  
  *   :py:meth:`~MachineLearning.Client.get_data_source`

  
  *   :py:meth:`~MachineLearning.Client.get_evaluation`

  
  *   :py:meth:`~MachineLearning.Client.get_ml_model`

  
  *   :py:meth:`~MachineLearning.Client.get_paginator`

  
  *   :py:meth:`~MachineLearning.Client.get_waiter`

  
  *   :py:meth:`~MachineLearning.Client.predict`

  
  *   :py:meth:`~MachineLearning.Client.update_batch_prediction`

  
  *   :py:meth:`~MachineLearning.Client.update_data_source`

  
  *   :py:meth:`~MachineLearning.Client.update_evaluation`

  
  *   :py:meth:`~MachineLearning.Client.update_ml_model`

  

  .. py:method:: add_tags(**kwargs)

    

    Adds one or more tags to an object, up to a limit of 10. Each tag consists of a key and an optional value. If you add a tag using a key that is already associated with the ML object, ``AddTags`` updates the tag's value.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/AddTags>`_    


    **Request Syntax** 
    ::

      response = client.add_tags(
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          ResourceId='string',
          ResourceType='BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
      )
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      The key-value pairs to use to create tags. If you specify a key without specifying a value, Amazon ML creates a tag with the specified key and a value of null.

      

    
      - *(dict) --* 

        A custom key-value pair associated with an ML object, such as an ML model.

        

      
        - **Key** *(string) --* 

          A unique identifier for the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.

          

        
        - **Value** *(string) --* 

          An optional string, typically used to describe or define the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.

          

        
      
  
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The ID of the ML object to tag. For example, ``exampleModelId`` .

      

    
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of the ML object to tag. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceId': 'string',
            'ResourceType': 'BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Amazon ML returns the following elements. 

        
        

        - **ResourceId** *(string) --* 

          The ID of the ML object that was tagged.

          
        

        - **ResourceType** *(string) --* 

          The type of the ML object that was tagged.

          
    

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


  .. py:method:: create_batch_prediction(**kwargs)

    

    Generates predictions for a group of observations. The observations to process exist in one or more data files referenced by a ``DataSource`` . This operation creates a new ``BatchPrediction`` , and uses an ``MLModel`` and the data files referenced by the ``DataSource`` as information sources. 

     

    ``CreateBatchPrediction`` is an asynchronous operation. In response to ``CreateBatchPrediction`` , Amazon Machine Learning (Amazon ML) immediately returns and sets the ``BatchPrediction`` status to ``PENDING`` . After the ``BatchPrediction`` completes, Amazon ML sets the status to ``COMPLETED`` . 

     

    You can poll for status updates by using the  GetBatchPrediction operation and checking the ``Status`` parameter of the result. After the ``COMPLETED`` status appears, the results are available in the location specified by the ``OutputUri`` parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateBatchPrediction>`_    


    **Request Syntax** 
    ::

      response = client.create_batch_prediction(
          BatchPredictionId='string',
          BatchPredictionName='string',
          MLModelId='string',
          BatchPredictionDataSourceId='string',
          OutputUri='string'
      )
    :type BatchPredictionId: string
    :param BatchPredictionId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``BatchPrediction`` .

      

    
    :type BatchPredictionName: string
    :param BatchPredictionName: 

      A user-supplied name or description of the ``BatchPrediction`` . ``BatchPredictionName`` can only use the UTF-8 character set.

      

    
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      The ID of the ``MLModel`` that will generate predictions for the group of observations. 

      

    
    :type BatchPredictionDataSourceId: string
    :param BatchPredictionDataSourceId: **[REQUIRED]** 

      The ID of the ``DataSource`` that points to the group of observations to predict.

      

    
    :type OutputUri: string
    :param OutputUri: **[REQUIRED]** 

      The location of an Amazon Simple Storage Service (Amazon S3) bucket or directory to store the batch prediction results. The following substrings are not allowed in the ``s3 key`` portion of the ``outputURI`` field: ':', '//', '/./', '/../'.

       

      Amazon ML needs permissions to store and retrieve the logs on your behalf. For information about how to set permissions, see the `Amazon Machine Learning Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BatchPredictionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``CreateBatchPrediction`` operation, and is an acknowledgement that Amazon ML received the request.

         

        The ``CreateBatchPrediction`` operation is asynchronous. You can poll for status updates by using the ``>GetBatchPrediction`` operation and checking the ``Status`` parameter of the result. 

        
        

        - **BatchPredictionId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``BatchPrediction`` . This value is identical to the value of the ``BatchPredictionId`` in the request.

          
    

  .. py:method:: create_data_source_from_rds(**kwargs)

    

    Creates a ``DataSource`` object from an `Amazon Relational Database Service <http://aws.amazon.com/rds/>`__ (Amazon RDS). A ``DataSource`` references data that can be used to perform ``CreateMLModel`` , ``CreateEvaluation`` , or ``CreateBatchPrediction`` operations.

     

    ``CreateDataSourceFromRDS`` is an asynchronous operation. In response to ``CreateDataSourceFromRDS`` , Amazon Machine Learning (Amazon ML) immediately returns and sets the ``DataSource`` status to ``PENDING`` . After the ``DataSource`` is created and ready for use, Amazon ML sets the ``Status`` parameter to ``COMPLETED`` . ``DataSource`` in the ``COMPLETED`` or ``PENDING`` state can be used only to perform ``>CreateMLModel`` >, ``CreateEvaluation`` , or ``CreateBatchPrediction`` operations. 

     

    If Amazon ML cannot accept the input source, it sets the ``Status`` parameter to ``FAILED`` and includes an error message in the ``Message`` attribute of the ``GetDataSource`` operation response. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateDataSourceFromRDS>`_    


    **Request Syntax** 
    ::

      response = client.create_data_source_from_rds(
          DataSourceId='string',
          DataSourceName='string',
          RDSData={
              'DatabaseInformation': {
                  'InstanceIdentifier': 'string',
                  'DatabaseName': 'string'
              },
              'SelectSqlQuery': 'string',
              'DatabaseCredentials': {
                  'Username': 'string',
                  'Password': 'string'
              },
              'S3StagingLocation': 'string',
              'DataRearrangement': 'string',
              'DataSchema': 'string',
              'DataSchemaUri': 'string',
              'ResourceRole': 'string',
              'ServiceRole': 'string',
              'SubnetId': 'string',
              'SecurityGroupIds': [
                  'string',
              ]
          },
          RoleARN='string',
          ComputeStatistics=True|False
      )
    :type DataSourceId: string
    :param DataSourceId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``DataSource`` . Typically, an Amazon Resource Number (ARN) becomes the ID for a ``DataSource`` .

      

    
    :type DataSourceName: string
    :param DataSourceName: 

      A user-supplied name or description of the ``DataSource`` .

      

    
    :type RDSData: dict
    :param RDSData: **[REQUIRED]** 

      The data specification of an Amazon RDS ``DataSource`` :

       

       
      * DatabaseInformation - 

         
        * ``DatabaseName`` - The name of the Amazon RDS database.
         
        * ``InstanceIdentifier`` - A unique identifier for the Amazon RDS database instance.
         

       

      
       
      * DatabaseCredentials - AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon RDS database.
       
      * ResourceRole - A role (DataPipelineDefaultResourceRole) assumed by an EC2 instance to carry out the copy task from Amazon RDS to Amazon Simple Storage Service (Amazon S3). For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.
       
      * ServiceRole - A role (DataPipelineDefaultRole) assumed by the AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.
       
      * SecurityInfo - The security information to use to access an RDS DB instance. You need to set up appropriate ingress rules for the security entity IDs provided to allow access to the Amazon RDS instance. Specify a [``SubnetId`` , ``SecurityGroupIds`` ] pair for a VPC-based RDS DB instance.
       
      * SelectSqlQuery - A query that is used to retrieve the observation data for the ``Datasource`` .
       
      * S3StagingLocation - The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using ``SelectSqlQuery`` is stored in this location.
       
      * DataSchemaUri - The Amazon S3 location of the ``DataSchema`` .
       
      * DataSchema - A JSON string representing the schema. This is not required if ``DataSchemaUri`` is specified. 
       
      * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the ``Datasource`` .   Sample - ``"{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"``   
       

      

    
      - **DatabaseInformation** *(dict) --* **[REQUIRED]** 

        Describes the ``DatabaseName`` and ``InstanceIdentifier`` of an Amazon RDS database.

        

      
        - **InstanceIdentifier** *(string) --* **[REQUIRED]** 

          The ID of an RDS DB instance.

          

        
        - **DatabaseName** *(string) --* **[REQUIRED]** 

          The name of a database hosted on an RDS DB instance.

          

        
      
      - **SelectSqlQuery** *(string) --* **[REQUIRED]** 

        The query that is used to retrieve the observation data for the ``DataSource`` .

        

      
      - **DatabaseCredentials** *(dict) --* **[REQUIRED]** 

        The AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon RDS database.

        

      
        - **Username** *(string) --* **[REQUIRED]** 

          The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.

          

        
        - **Password** *(string) --* **[REQUIRED]** 

          The password to be used by Amazon ML to connect to a database on an RDS DB instance. The password should have sufficient permissions to execute the ``RDSSelectQuery`` query.

          

        
      
      - **S3StagingLocation** *(string) --* **[REQUIRED]** 

        The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using ``SelectSqlQuery`` is stored in this location.

        

      
      - **DataRearrangement** *(string) --* 

        A JSON string that represents the splitting and rearrangement processing to be applied to a ``DataSource`` . If the ``DataRearrangement`` parameter is not provided, all of the input data is used to create the ``Datasource`` .

         

        There are multiple parameters that control what data is used to create a datasource:

         

         
        * **``percentBegin``**  Use ``percentBegin`` to indicate the beginning of the range of the data used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML includes all of the data when creating the datasource.
         
        * **``percentEnd``**  Use ``percentEnd`` to indicate the end of the range of the data used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML includes all of the data when creating the datasource.
         
        * **``complement``**  The ``complement`` parameter instructs Amazon ML to use the data that is not included in the range of ``percentBegin`` to ``percentEnd`` to create a datasource. The ``complement`` parameter is useful if you need to create complementary datasources for training and evaluation. To create a complementary datasource, use the same values for ``percentBegin`` and ``percentEnd`` , along with the ``complement`` parameter. For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first datasource has 25 percent of the data, and the second one has 75 percent of the data. Datasource for evaluation: ``{"splitting":{"percentBegin":0, "percentEnd":25}}``  Datasource for training: ``{"splitting":{"percentBegin":0, "percentEnd":25, "complement":"true"}}``  
         
        * **``strategy``**  To change how Amazon ML splits the data for a datasource, use the ``strategy`` parameter. The default value for the ``strategy`` parameter is ``sequential`` , meaning that Amazon ML takes all of the data records between the ``percentBegin`` and ``percentEnd`` parameters for the datasource, in the order that the records appear in the input data. The following two ``DataRearrangement`` lines are examples of sequentially ordered training and evaluation datasources: Datasource for evaluation: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}``  Datasource for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential", "complement":"true"}}``  To randomly split the input data into the proportions indicated by the percentBegin and percentEnd parameters, set the ``strategy`` parameter to ``random`` and provide a string that is used as the seed value for the random data splitting (for example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then selects the rows that have an assigned number between ``percentBegin`` and ``percentEnd`` . Pseudo-random numbers are assigned using both the input seed string value and the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved. The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly. It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in training and evaluation datasources containing non-similar data records. The following two ``DataRearrangement`` lines are examples of non-sequentially ordered training and evaluation datasources: Datasource for evaluation: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "randomSeed"="s3://my_s3_path/bucket/file.csv"}}``  Datasource for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}``  
         

        

      
      - **DataSchema** *(string) --* 

        A JSON string that represents the schema for an Amazon RDS ``DataSource`` . The ``DataSchema`` defines the structure of the observation data in the data file(s) referenced in the ``DataSource`` .

         

        A ``DataSchema`` is not required if you specify a ``DataSchemaUri`` 

         

        Define your ``DataSchema`` as a series of key-value pairs. ``attributes`` and ``excludedVariableNames`` have an array of key-value pairs for their value. Use the following format to define your ``DataSchema`` .

         

        { "version": "1.0",

         

        "recordAnnotationFieldName": "F1",

         

        "recordWeightFieldName": "F2",

         

        "targetFieldName": "F3",

         

        "dataFormat": "CSV",

         

        "dataFileContainsHeader": true,

         

        "attributes": [

         

        { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2", "fieldType": "NUMERIC" }, { "fieldName": "F3", "fieldType": "CATEGORICAL" }, { "fieldName": "F4", "fieldType": "NUMERIC" }, { "fieldName": "F5", "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" }, { "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName": "F8", "fieldType": "WEIGHTED_STRING_SEQUENCE" } ],

         

        "excludedVariableNames": [ "F6" ] } 

         

      
      - **DataSchemaUri** *(string) --* 

        The Amazon S3 location of the ``DataSchema`` . 

        

      
      - **ResourceRole** *(string) --* **[REQUIRED]** 

        The role (DataPipelineDefaultResourceRole) assumed by an Amazon Elastic Compute Cloud (Amazon EC2) instance to carry out the copy operation from Amazon RDS to an Amazon S3 task. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.

        

      
      - **ServiceRole** *(string) --* **[REQUIRED]** 

        The role (DataPipelineDefaultRole) assumed by AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.

        

      
      - **SubnetId** *(string) --* **[REQUIRED]** 

        The subnet ID to be used to access a VPC-based RDS DB instance. This attribute is used by Data Pipeline to carry out the copy task from Amazon RDS to Amazon S3.

        

      
      - **SecurityGroupIds** *(list) --* **[REQUIRED]** 

        The security group IDs to be used to access a VPC-based RDS DB instance. Ensure that there are appropriate ingress rules set up to allow access to the RDS DB instance. This attribute is used by Data Pipeline to carry out the copy operation from Amazon RDS to an Amazon S3 task.

        

      
        - *(string) --* 

        
    
    
    :type RoleARN: string
    :param RoleARN: **[REQUIRED]** 

      The role that Amazon ML assumes on behalf of the user to create and activate a data pipeline in the user's account and copy data using the ``SelectSqlQuery`` query from Amazon RDS to Amazon S3.

       

       

      

    
    :type ComputeStatistics: boolean
    :param ComputeStatistics: 

      The compute statistics for a ``DataSource`` . The statistics are generated from the observation data referenced by a ``DataSource`` . Amazon ML uses the statistics internally during ``MLModel`` training. This parameter must be set to ``true`` if the ```` DataSource```` needs to be used for ``MLModel`` training. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DataSourceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``CreateDataSourceFromRDS`` operation, and is an acknowledgement that Amazon ML received the request.

         

        The ``CreateDataSourceFromRDS`` > operation is asynchronous. You can poll for updates by using the ``GetBatchPrediction`` operation and checking the ``Status`` parameter. You can inspect the ``Message`` when ``Status`` shows up as ``FAILED`` . You can also check the progress of the copy operation by going to the ``DataPipeline`` console and looking up the pipeline using the ``pipelineId`` from the describe call.

        
        

        - **DataSourceId** *(string) --* 

          A user-supplied ID that uniquely identifies the datasource. This value should be identical to the value of the ``DataSourceID`` in the request. 

          
    

  .. py:method:: create_data_source_from_redshift(**kwargs)

    

    Creates a ``DataSource`` from a database hosted on an Amazon Redshift cluster. A ``DataSource`` references data that can be used to perform either ``CreateMLModel`` , ``CreateEvaluation`` , or ``CreateBatchPrediction`` operations.

     

    ``CreateDataSourceFromRedshift`` is an asynchronous operation. In response to ``CreateDataSourceFromRedshift`` , Amazon Machine Learning (Amazon ML) immediately returns and sets the ``DataSource`` status to ``PENDING`` . After the ``DataSource`` is created and ready for use, Amazon ML sets the ``Status`` parameter to ``COMPLETED`` . ``DataSource`` in ``COMPLETED`` or ``PENDING`` states can be used to perform only ``CreateMLModel`` , ``CreateEvaluation`` , or ``CreateBatchPrediction`` operations. 

     

    If Amazon ML can't accept the input source, it sets the ``Status`` parameter to ``FAILED`` and includes an error message in the ``Message`` attribute of the ``GetDataSource`` operation response. 

     

    The observations should be contained in the database hosted on an Amazon Redshift cluster and should be specified by a ``SelectSqlQuery`` query. Amazon ML executes an ``Unload`` command in Amazon Redshift to transfer the result set of the ``SelectSqlQuery`` query to ``S3StagingLocation`` .

     

    After the ``DataSource`` has been created, it's ready for use in evaluations and batch predictions. If you plan to use the ``DataSource`` to train an ``MLModel`` , the ``DataSource`` also requires a recipe. A recipe describes how each input variable will be used in training an ``MLModel`` . Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.

     

    You can't change an existing datasource, but you can copy and modify the settings from an existing Amazon Redshift datasource to create a new datasource. To do so, call ``GetDataSource`` for an existing datasource and copy the values to a ``CreateDataSource`` call. Change the settings that you want to change and make sure that all required fields have the appropriate values.

     

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateDataSourceFromRedshift>`_    


    **Request Syntax** 
    ::

      response = client.create_data_source_from_redshift(
          DataSourceId='string',
          DataSourceName='string',
          DataSpec={
              'DatabaseInformation': {
                  'DatabaseName': 'string',
                  'ClusterIdentifier': 'string'
              },
              'SelectSqlQuery': 'string',
              'DatabaseCredentials': {
                  'Username': 'string',
                  'Password': 'string'
              },
              'S3StagingLocation': 'string',
              'DataRearrangement': 'string',
              'DataSchema': 'string',
              'DataSchemaUri': 'string'
          },
          RoleARN='string',
          ComputeStatistics=True|False
      )
    :type DataSourceId: string
    :param DataSourceId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``DataSource`` .

      

    
    :type DataSourceName: string
    :param DataSourceName: 

      A user-supplied name or description of the ``DataSource`` . 

      

    
    :type DataSpec: dict
    :param DataSpec: **[REQUIRED]** 

      The data specification of an Amazon Redshift ``DataSource`` :

       

       
      * DatabaseInformation - 

         
        * ``DatabaseName`` - The name of the Amazon Redshift database. 
         
        * ``ClusterIdentifier`` - The unique ID for the Amazon Redshift cluster.
         

      

      
       
      * DatabaseCredentials - The AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon Redshift database.
       
      * SelectSqlQuery - The query that is used to retrieve the observation data for the ``Datasource`` .
       
      * S3StagingLocation - The Amazon Simple Storage Service (Amazon S3) location for staging Amazon Redshift data. The data retrieved from Amazon Redshift using the ``SelectSqlQuery`` query is stored in this location.
       
      * DataSchemaUri - The Amazon S3 location of the ``DataSchema`` .
       
      * DataSchema - A JSON string representing the schema. This is not required if ``DataSchemaUri`` is specified. 
       
      * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the ``DataSource`` . Sample - ``"{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"``   
       

      

    
      - **DatabaseInformation** *(dict) --* **[REQUIRED]** 

        Describes the ``DatabaseName`` and ``ClusterIdentifier`` for an Amazon Redshift ``DataSource`` .

        

      
        - **DatabaseName** *(string) --* **[REQUIRED]** 

          The name of a database hosted on an Amazon Redshift cluster.

          

        
        - **ClusterIdentifier** *(string) --* **[REQUIRED]** 

          The ID of an Amazon Redshift cluster.

          

        
      
      - **SelectSqlQuery** *(string) --* **[REQUIRED]** 

        Describes the SQL Query to execute on an Amazon Redshift database for an Amazon Redshift ``DataSource`` .

        

      
      - **DatabaseCredentials** *(dict) --* **[REQUIRED]** 

        Describes AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon Redshift database.

        

      
        - **Username** *(string) --* **[REQUIRED]** 

          A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

          

        
        - **Password** *(string) --* **[REQUIRED]** 

          A password to be used by Amazon ML to connect to a database on an Amazon Redshift cluster. The password should have sufficient permissions to execute a ``RedshiftSelectSqlQuery`` query. The password should be valid for an Amazon Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

          

        
      
      - **S3StagingLocation** *(string) --* **[REQUIRED]** 

        Describes an Amazon S3 location to store the result set of the ``SelectSqlQuery`` query.

        

      
      - **DataRearrangement** *(string) --* 

        A JSON string that represents the splitting and rearrangement processing to be applied to a ``DataSource`` . If the ``DataRearrangement`` parameter is not provided, all of the input data is used to create the ``Datasource`` .

         

        There are multiple parameters that control what data is used to create a datasource:

         

         
        * **``percentBegin``**  Use ``percentBegin`` to indicate the beginning of the range of the data used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML includes all of the data when creating the datasource.
         
        * **``percentEnd``**  Use ``percentEnd`` to indicate the end of the range of the data used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML includes all of the data when creating the datasource.
         
        * **``complement``**  The ``complement`` parameter instructs Amazon ML to use the data that is not included in the range of ``percentBegin`` to ``percentEnd`` to create a datasource. The ``complement`` parameter is useful if you need to create complementary datasources for training and evaluation. To create a complementary datasource, use the same values for ``percentBegin`` and ``percentEnd`` , along with the ``complement`` parameter. For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first datasource has 25 percent of the data, and the second one has 75 percent of the data. Datasource for evaluation: ``{"splitting":{"percentBegin":0, "percentEnd":25}}``  Datasource for training: ``{"splitting":{"percentBegin":0, "percentEnd":25, "complement":"true"}}``  
         
        * **``strategy``**  To change how Amazon ML splits the data for a datasource, use the ``strategy`` parameter. The default value for the ``strategy`` parameter is ``sequential`` , meaning that Amazon ML takes all of the data records between the ``percentBegin`` and ``percentEnd`` parameters for the datasource, in the order that the records appear in the input data. The following two ``DataRearrangement`` lines are examples of sequentially ordered training and evaluation datasources: Datasource for evaluation: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}``  Datasource for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential", "complement":"true"}}``  To randomly split the input data into the proportions indicated by the percentBegin and percentEnd parameters, set the ``strategy`` parameter to ``random`` and provide a string that is used as the seed value for the random data splitting (for example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then selects the rows that have an assigned number between ``percentBegin`` and ``percentEnd`` . Pseudo-random numbers are assigned using both the input seed string value and the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved. The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly. It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in training and evaluation datasources containing non-similar data records. The following two ``DataRearrangement`` lines are examples of non-sequentially ordered training and evaluation datasources: Datasource for evaluation: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "randomSeed"="s3://my_s3_path/bucket/file.csv"}}``  Datasource for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}``  
         

        

      
      - **DataSchema** *(string) --* 

        A JSON string that represents the schema for an Amazon Redshift ``DataSource`` . The ``DataSchema`` defines the structure of the observation data in the data file(s) referenced in the ``DataSource`` .

         

        A ``DataSchema`` is not required if you specify a ``DataSchemaUri`` .

         

        Define your ``DataSchema`` as a series of key-value pairs. ``attributes`` and ``excludedVariableNames`` have an array of key-value pairs for their value. Use the following format to define your ``DataSchema`` .

         

        { "version": "1.0",

         

        "recordAnnotationFieldName": "F1",

         

        "recordWeightFieldName": "F2",

         

        "targetFieldName": "F3",

         

        "dataFormat": "CSV",

         

        "dataFileContainsHeader": true,

         

        "attributes": [

         

        { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2", "fieldType": "NUMERIC" }, { "fieldName": "F3", "fieldType": "CATEGORICAL" }, { "fieldName": "F4", "fieldType": "NUMERIC" }, { "fieldName": "F5", "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" }, { "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName": "F8", "fieldType": "WEIGHTED_STRING_SEQUENCE" } ],

         

        "excludedVariableNames": [ "F6" ] } 

        

      
      - **DataSchemaUri** *(string) --* 

        Describes the schema location for an Amazon Redshift ``DataSource`` .

        

      
    
    :type RoleARN: string
    :param RoleARN: **[REQUIRED]** 

      A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the role on behalf of the user to create the following: 

       

       

       
      * A security group to allow Amazon ML to execute the ``SelectSqlQuery`` query on an Amazon Redshift cluster
       
      * An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the ``S3StagingLocation`` 
       

       

      

    
    :type ComputeStatistics: boolean
    :param ComputeStatistics: 

      The compute statistics for a ``DataSource`` . The statistics are generated from the observation data referenced by a ``DataSource`` . Amazon ML uses the statistics internally during ``MLModel`` training. This parameter must be set to ``true`` if the ``DataSource`` needs to be used for ``MLModel`` training.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DataSourceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``CreateDataSourceFromRedshift`` operation, and is an acknowledgement that Amazon ML received the request.

         

        The ``CreateDataSourceFromRedshift`` operation is asynchronous. You can poll for updates by using the ``GetBatchPrediction`` operation and checking the ``Status`` parameter. 

        
        

        - **DataSourceId** *(string) --* 

          A user-supplied ID that uniquely identifies the datasource. This value should be identical to the value of the ``DataSourceID`` in the request. 

          
    

  .. py:method:: create_data_source_from_s3(**kwargs)

    

    Creates a ``DataSource`` object. A ``DataSource`` references data that can be used to perform ``CreateMLModel`` , ``CreateEvaluation`` , or ``CreateBatchPrediction`` operations.

     

    ``CreateDataSourceFromS3`` is an asynchronous operation. In response to ``CreateDataSourceFromS3`` , Amazon Machine Learning (Amazon ML) immediately returns and sets the ``DataSource`` status to ``PENDING`` . After the ``DataSource`` has been created and is ready for use, Amazon ML sets the ``Status`` parameter to ``COMPLETED`` . ``DataSource`` in the ``COMPLETED`` or ``PENDING`` state can be used to perform only ``CreateMLModel`` , ``CreateEvaluation`` or ``CreateBatchPrediction`` operations. 

     

    If Amazon ML can't accept the input source, it sets the ``Status`` parameter to ``FAILED`` and includes an error message in the ``Message`` attribute of the ``GetDataSource`` operation response. 

     

    The observation data used in a ``DataSource`` should be ready to use; that is, it should have a consistent structure, and missing data values should be kept to a minimum. The observation data must reside in one or more .csv files in an Amazon Simple Storage Service (Amazon S3) location, along with a schema that describes the data items by name and type. The same schema must be used for all of the data files referenced by the ``DataSource`` . 

     

    After the ``DataSource`` has been created, it's ready to use in evaluations and batch predictions. If you plan to use the ``DataSource`` to train an ``MLModel`` , the ``DataSource`` also needs a recipe. A recipe describes how each input variable will be used in training an ``MLModel`` . Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateDataSourceFromS3>`_    


    **Request Syntax** 
    ::

      response = client.create_data_source_from_s3(
          DataSourceId='string',
          DataSourceName='string',
          DataSpec={
              'DataLocationS3': 'string',
              'DataRearrangement': 'string',
              'DataSchema': 'string',
              'DataSchemaLocationS3': 'string'
          },
          ComputeStatistics=True|False
      )
    :type DataSourceId: string
    :param DataSourceId: **[REQUIRED]** 

      A user-supplied identifier that uniquely identifies the ``DataSource`` . 

      

    
    :type DataSourceName: string
    :param DataSourceName: 

      A user-supplied name or description of the ``DataSource`` . 

      

    
    :type DataSpec: dict
    :param DataSpec: **[REQUIRED]** 

      The data specification of a ``DataSource`` :

       

       
      * DataLocationS3 - The Amazon S3 location of the observation data.
       
      * DataSchemaLocationS3 - The Amazon S3 location of the ``DataSchema`` .
       
      * DataSchema - A JSON string representing the schema. This is not required if ``DataSchemaUri`` is specified. 
       
      * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the ``Datasource`` .  Sample - ``"{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"``   
       

      

    
      - **DataLocationS3** *(string) --* **[REQUIRED]** 

        The location of the data file(s) used by a ``DataSource`` . The URI specifies a data file or an Amazon Simple Storage Service (Amazon S3) directory or bucket containing data files.

        

      
      - **DataRearrangement** *(string) --* 

        A JSON string that represents the splitting and rearrangement processing to be applied to a ``DataSource`` . If the ``DataRearrangement`` parameter is not provided, all of the input data is used to create the ``Datasource`` .

         

        There are multiple parameters that control what data is used to create a datasource:

         

         
        * **``percentBegin``**  Use ``percentBegin`` to indicate the beginning of the range of the data used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML includes all of the data when creating the datasource.
         
        * **``percentEnd``**  Use ``percentEnd`` to indicate the end of the range of the data used to create the Datasource. If you do not include ``percentBegin`` and ``percentEnd`` , Amazon ML includes all of the data when creating the datasource.
         
        * **``complement``**  The ``complement`` parameter instructs Amazon ML to use the data that is not included in the range of ``percentBegin`` to ``percentEnd`` to create a datasource. The ``complement`` parameter is useful if you need to create complementary datasources for training and evaluation. To create a complementary datasource, use the same values for ``percentBegin`` and ``percentEnd`` , along with the ``complement`` parameter. For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first datasource has 25 percent of the data, and the second one has 75 percent of the data. Datasource for evaluation: ``{"splitting":{"percentBegin":0, "percentEnd":25}}``  Datasource for training: ``{"splitting":{"percentBegin":0, "percentEnd":25, "complement":"true"}}``  
         
        * **``strategy``**  To change how Amazon ML splits the data for a datasource, use the ``strategy`` parameter. The default value for the ``strategy`` parameter is ``sequential`` , meaning that Amazon ML takes all of the data records between the ``percentBegin`` and ``percentEnd`` parameters for the datasource, in the order that the records appear in the input data. The following two ``DataRearrangement`` lines are examples of sequentially ordered training and evaluation datasources: Datasource for evaluation: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}``  Datasource for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential", "complement":"true"}}``  To randomly split the input data into the proportions indicated by the percentBegin and percentEnd parameters, set the ``strategy`` parameter to ``random`` and provide a string that is used as the seed value for the random data splitting (for example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then selects the rows that have an assigned number between ``percentBegin`` and ``percentEnd`` . Pseudo-random numbers are assigned using both the input seed string value and the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved. The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly. It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in training and evaluation datasources containing non-similar data records. The following two ``DataRearrangement`` lines are examples of non-sequentially ordered training and evaluation datasources: Datasource for evaluation: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "randomSeed"="s3://my_s3_path/bucket/file.csv"}}``  Datasource for training: ``{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}``  
         

        

      
      - **DataSchema** *(string) --* 

        A JSON string that represents the schema for an Amazon S3 ``DataSource`` . The ``DataSchema`` defines the structure of the observation data in the data file(s) referenced in the ``DataSource`` .

         

        You must provide either the ``DataSchema`` or the ``DataSchemaLocationS3`` .

         

        Define your ``DataSchema`` as a series of key-value pairs. ``attributes`` and ``excludedVariableNames`` have an array of key-value pairs for their value. Use the following format to define your ``DataSchema`` .

         

        { "version": "1.0",

         

        "recordAnnotationFieldName": "F1",

         

        "recordWeightFieldName": "F2",

         

        "targetFieldName": "F3",

         

        "dataFormat": "CSV",

         

        "dataFileContainsHeader": true,

         

        "attributes": [

         

        { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2", "fieldType": "NUMERIC" }, { "fieldName": "F3", "fieldType": "CATEGORICAL" }, { "fieldName": "F4", "fieldType": "NUMERIC" }, { "fieldName": "F5", "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" }, { "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName": "F8", "fieldType": "WEIGHTED_STRING_SEQUENCE" } ],

         

        "excludedVariableNames": [ "F6" ] } 

         

      
      - **DataSchemaLocationS3** *(string) --* 

        Describes the schema location in Amazon S3. You must provide either the ``DataSchema`` or the ``DataSchemaLocationS3`` .

        

      
    
    :type ComputeStatistics: boolean
    :param ComputeStatistics: 

      The compute statistics for a ``DataSource`` . The statistics are generated from the observation data referenced by a ``DataSource`` . Amazon ML uses the statistics internally during ``MLModel`` training. This parameter must be set to ``true`` if the ```` DataSource```` needs to be used for ``MLModel`` training.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DataSourceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``CreateDataSourceFromS3`` operation, and is an acknowledgement that Amazon ML received the request.

         

        The ``CreateDataSourceFromS3`` operation is asynchronous. You can poll for updates by using the ``GetBatchPrediction`` operation and checking the ``Status`` parameter. 

        
        

        - **DataSourceId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``DataSource`` . This value should be identical to the value of the ``DataSourceID`` in the request. 

          
    

  .. py:method:: create_evaluation(**kwargs)

    

    Creates a new ``Evaluation`` of an ``MLModel`` . An ``MLModel`` is evaluated on a set of observations associated to a ``DataSource`` . Like a ``DataSource`` for an ``MLModel`` , the ``DataSource`` for an ``Evaluation`` contains values for the ``Target Variable`` . The ``Evaluation`` compares the predicted result for each observation to the actual outcome and provides a summary so that you know how effective the ``MLModel`` functions on the test data. Evaluation generates a relevant performance metric, such as BinaryAUC, RegressionRMSE or MulticlassAvgFScore based on the corresponding ``MLModelType`` : ``BINARY`` , ``REGRESSION`` or ``MULTICLASS`` . 

     

    ``CreateEvaluation`` is an asynchronous operation. In response to ``CreateEvaluation`` , Amazon Machine Learning (Amazon ML) immediately returns and sets the evaluation status to ``PENDING`` . After the ``Evaluation`` is created and ready for use, Amazon ML sets the status to ``COMPLETED`` . 

     

    You can use the ``GetEvaluation`` operation to check progress of the evaluation during the creation operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateEvaluation>`_    


    **Request Syntax** 
    ::

      response = client.create_evaluation(
          EvaluationId='string',
          EvaluationName='string',
          MLModelId='string',
          EvaluationDataSourceId='string'
      )
    :type EvaluationId: string
    :param EvaluationId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``Evaluation`` .

      

    
    :type EvaluationName: string
    :param EvaluationName: 

      A user-supplied name or description of the ``Evaluation`` .

      

    
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      The ID of the ``MLModel`` to evaluate.

       

      The schema used in creating the ``MLModel`` must match the schema of the ``DataSource`` used in the ``Evaluation`` .

      

    
    :type EvaluationDataSourceId: string
    :param EvaluationDataSourceId: **[REQUIRED]** 

      The ID of the ``DataSource`` for the evaluation. The schema of the ``DataSource`` must match the schema used to create the ``MLModel`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EvaluationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``CreateEvaluation`` operation, and is an acknowledgement that Amazon ML received the request.

         

        ``CreateEvaluation`` operation is asynchronous. You can poll for status updates by using the ``GetEvcaluation`` operation and checking the ``Status`` parameter. 

        
        

        - **EvaluationId** *(string) --* 

          The user-supplied ID that uniquely identifies the ``Evaluation`` . This value should be identical to the value of the ``EvaluationId`` in the request.

          
    

  .. py:method:: create_ml_model(**kwargs)

    

    Creates a new ``MLModel`` using the ``DataSource`` and the recipe as information sources. 

     

    An ``MLModel`` is nearly immutable. Users can update only the ``MLModelName`` and the ``ScoreThreshold`` in an ``MLModel`` without creating a new ``MLModel`` . 

     

    ``CreateMLModel`` is an asynchronous operation. In response to ``CreateMLModel`` , Amazon Machine Learning (Amazon ML) immediately returns and sets the ``MLModel`` status to ``PENDING`` . After the ``MLModel`` has been created and ready is for use, Amazon ML sets the status to ``COMPLETED`` . 

     

    You can use the ``GetMLModel`` operation to check the progress of the ``MLModel`` during the creation operation.

     

     ``CreateMLModel`` requires a ``DataSource`` with computed statistics, which can be created by setting ``ComputeStatistics`` to ``true`` in ``CreateDataSourceFromRDS`` , ``CreateDataSourceFromS3`` , or ``CreateDataSourceFromRedshift`` operations. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateMLModel>`_    


    **Request Syntax** 
    ::

      response = client.create_ml_model(
          MLModelId='string',
          MLModelName='string',
          MLModelType='REGRESSION'|'BINARY'|'MULTICLASS',
          Parameters={
              'string': 'string'
          },
          TrainingDataSourceId='string',
          Recipe='string',
          RecipeUri='string'
      )
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``MLModel`` .

      

    
    :type MLModelName: string
    :param MLModelName: 

      A user-supplied name or description of the ``MLModel`` .

      

    
    :type MLModelType: string
    :param MLModelType: **[REQUIRED]** 

      The category of supervised learning that this ``MLModel`` will address. Choose from the following types:

       

       
      * Choose ``REGRESSION`` if the ``MLModel`` will be used to predict a numeric value.
       
      * Choose ``BINARY`` if the ``MLModel`` result has two possible values.
       
      * Choose ``MULTICLASS`` if the ``MLModel`` result has a limited number of values. 
       

       

      For more information, see the `Amazon Machine Learning Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ .

      

    
    :type Parameters: dict
    :param Parameters: 

      A list of the training parameters in the ``MLModel`` . The list is implemented as a map of key-value pairs.

       

      The following is the current set of training parameters: 

       

       
      * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` . 
       
      * ``sgd.maxPasses`` - The number of times that the training process traverses the observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to ``10000`` . The default value is ``10`` .
       
      * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are ``auto`` and ``none`` . The default value is ``none`` . We strongly recommend that you shuffle your data. 
       
      * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter can't be used when ``L2`` is specified. Use this parameter sparingly. 
       
      * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L2 normalization. This parameter can't be used when ``L1`` is specified. Use this parameter sparingly. 
       

      

    
      - *(string) --* 

        String type.

        

      
        - *(string) --* 

          String type.

          

        
  

    :type TrainingDataSourceId: string
    :param TrainingDataSourceId: **[REQUIRED]** 

      The ``DataSource`` that points to the training data.

      

    
    :type Recipe: string
    :param Recipe: 

      The data recipe for creating the ``MLModel`` . You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.

      

    
    :type RecipeUri: string
    :param RecipeUri: 

      The Amazon Simple Storage Service (Amazon S3) location and file name that contains the ``MLModel`` recipe. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MLModelId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``CreateMLModel`` operation, and is an acknowledgement that Amazon ML received the request.

         

        The ``CreateMLModel`` operation is asynchronous. You can poll for status updates by using the ``GetMLModel`` operation and checking the ``Status`` parameter. 

        
        

        - **MLModelId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical to the value of the ``MLModelId`` in the request. 

          
    

  .. py:method:: create_realtime_endpoint(**kwargs)

    

    Creates a real-time endpoint for the ``MLModel`` . The endpoint contains the URI of the ``MLModel`` ; that is, the location to send real-time prediction requests for the specified ``MLModel`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateRealtimeEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.create_realtime_endpoint(
          MLModelId='string'
      )
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      The ID assigned to the ``MLModel`` during creation.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MLModelId': 'string',
            'RealtimeEndpointInfo': {
                'PeakRequestsPerSecond': 123,
                'CreatedAt': datetime(2015, 1, 1),
                'EndpointUrl': 'string',
                'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of an ``CreateRealtimeEndpoint`` operation.

         

        The result contains the ``MLModelId`` and the endpoint information for the ``MLModel`` .

         

        .. note::

           

          The endpoint information includes the URI of the ``MLModel`` ; that is, the location to send online prediction requests for the specified ``MLModel`` .

           

        
        

        - **MLModelId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical to the value of the ``MLModelId`` in the request.

          
        

        - **RealtimeEndpointInfo** *(dict) --* 

          The endpoint information of the ``MLModel``  

          
          

          - **PeakRequestsPerSecond** *(integer) --* 

            The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in incoming requests per second.

            
          

          - **CreatedAt** *(datetime) --* 

            The time that the request to create the real-time endpoint for the ``MLModel`` was received. The time is expressed in epoch time.

            
          

          - **EndpointUrl** *(string) --* 

            The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

             

            .. note::

              Note 

              The application must wait until the real-time endpoint is ready before using this URI.

               

            
          

          - **EndpointStatus** *(string) --* 

            The current status of the real-time endpoint for the ``MLModel`` . This element can have one of the following values: 

             

             
            * ``NONE`` - Endpoint does not exist or was previously deleted.
             
            * ``READY`` - Endpoint is ready to be used for real-time predictions.
             
            * ``UPDATING`` - Updating/creating the endpoint. 
             

            
      
    

  .. py:method:: delete_batch_prediction(**kwargs)

    

    Assigns the DELETED status to a ``BatchPrediction`` , rendering it unusable.

     

    After using the ``DeleteBatchPrediction`` operation, you can use the  GetBatchPrediction operation to verify that the status of the ``BatchPrediction`` changed to DELETED.

     

    **Caution:** The result of the ``DeleteBatchPrediction`` operation is irreversible.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DeleteBatchPrediction>`_    


    **Request Syntax** 
    ::

      response = client.delete_batch_prediction(
          BatchPredictionId='string'
      )
    :type BatchPredictionId: string
    :param BatchPredictionId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``BatchPrediction`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BatchPredictionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DeleteBatchPrediction`` operation.

         

        You can use the ``GetBatchPrediction`` operation and check the value of the ``Status`` parameter to see whether a ``BatchPrediction`` is marked as ``DELETED`` .

        
        

        - **BatchPredictionId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``BatchPrediction`` . This value should be identical to the value of the ``BatchPredictionID`` in the request.

          
    

  .. py:method:: delete_data_source(**kwargs)

    

    Assigns the DELETED status to a ``DataSource`` , rendering it unusable.

     

    After using the ``DeleteDataSource`` operation, you can use the  GetDataSource operation to verify that the status of the ``DataSource`` changed to DELETED.

     

    **Caution:** The results of the ``DeleteDataSource`` operation are irreversible.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DeleteDataSource>`_    


    **Request Syntax** 
    ::

      response = client.delete_data_source(
          DataSourceId='string'
      )
    :type DataSourceId: string
    :param DataSourceId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``DataSource`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DataSourceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DeleteDataSource`` operation.

        
        

        - **DataSourceId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``DataSource`` . This value should be identical to the value of the ``DataSourceID`` in the request.

          
    

  .. py:method:: delete_evaluation(**kwargs)

    

    Assigns the ``DELETED`` status to an ``Evaluation`` , rendering it unusable.

     

    After invoking the ``DeleteEvaluation`` operation, you can use the ``GetEvaluation`` operation to verify that the status of the ``Evaluation`` changed to ``DELETED`` .

     Caution 

    The results of the ``DeleteEvaluation`` operation are irreversible.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DeleteEvaluation>`_    


    **Request Syntax** 
    ::

      response = client.delete_evaluation(
          EvaluationId='string'
      )
    :type EvaluationId: string
    :param EvaluationId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``Evaluation`` to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EvaluationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DeleteEvaluation`` operation. The output indicates that Amazon Machine Learning (Amazon ML) received the request.

         

        You can use the ``GetEvaluation`` operation and check the value of the ``Status`` parameter to see whether an ``Evaluation`` is marked as ``DELETED`` .

        
        

        - **EvaluationId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``Evaluation`` . This value should be identical to the value of the ``EvaluationId`` in the request.

          
    

  .. py:method:: delete_ml_model(**kwargs)

    

    Assigns the ``DELETED`` status to an ``MLModel`` , rendering it unusable.

     

    After using the ``DeleteMLModel`` operation, you can use the ``GetMLModel`` operation to verify that the status of the ``MLModel`` changed to DELETED.

     

    **Caution:** The result of the ``DeleteMLModel`` operation is irreversible.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DeleteMLModel>`_    


    **Request Syntax** 
    ::

      response = client.delete_ml_model(
          MLModelId='string'
      )
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      A user-supplied ID that uniquely identifies the ``MLModel`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MLModelId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DeleteMLModel`` operation.

         

        You can use the ``GetMLModel`` operation and check the value of the ``Status`` parameter to see whether an ``MLModel`` is marked as ``DELETED`` .

        
        

        - **MLModelId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical to the value of the ``MLModelID`` in the request.

          
    

  .. py:method:: delete_realtime_endpoint(**kwargs)

    

    Deletes a real time endpoint of an ``MLModel`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DeleteRealtimeEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.delete_realtime_endpoint(
          MLModelId='string'
      )
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      The ID assigned to the ``MLModel`` during creation.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MLModelId': 'string',
            'RealtimeEndpointInfo': {
                'PeakRequestsPerSecond': 123,
                'CreatedAt': datetime(2015, 1, 1),
                'EndpointUrl': 'string',
                'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of an ``DeleteRealtimeEndpoint`` operation.

         

        The result contains the ``MLModelId`` and the endpoint information for the ``MLModel`` . 

        
        

        - **MLModelId** *(string) --* 

          A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical to the value of the ``MLModelId`` in the request.

          
        

        - **RealtimeEndpointInfo** *(dict) --* 

          The endpoint information of the ``MLModel``  

          
          

          - **PeakRequestsPerSecond** *(integer) --* 

            The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in incoming requests per second.

            
          

          - **CreatedAt** *(datetime) --* 

            The time that the request to create the real-time endpoint for the ``MLModel`` was received. The time is expressed in epoch time.

            
          

          - **EndpointUrl** *(string) --* 

            The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

             

            .. note::

              Note 

              The application must wait until the real-time endpoint is ready before using this URI.

               

            
          

          - **EndpointStatus** *(string) --* 

            The current status of the real-time endpoint for the ``MLModel`` . This element can have one of the following values: 

             

             
            * ``NONE`` - Endpoint does not exist or was previously deleted.
             
            * ``READY`` - Endpoint is ready to be used for real-time predictions.
             
            * ``UPDATING`` - Updating/creating the endpoint. 
             

            
      
    

  .. py:method:: delete_tags(**kwargs)

    

    Deletes the specified tags associated with an ML object. After this operation is complete, you can't recover deleted tags.

     

    If you specify a tag that doesn't exist, Amazon ML ignores it.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DeleteTags>`_    


    **Request Syntax** 
    ::

      response = client.delete_tags(
          TagKeys=[
              'string',
          ],
          ResourceId='string',
          ResourceType='BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
      )
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      One or more tags to delete.

      

    
      - *(string) --* 

      
  
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The ID of the tagged ML object. For example, ``exampleModelId`` .

      

    
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of the tagged ML object.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceId': 'string',
            'ResourceType': 'BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Amazon ML returns the following elements. 

        
        

        - **ResourceId** *(string) --* 

          The ID of the ML object from which tags were deleted.

          
        

        - **ResourceType** *(string) --* 

          The type of the ML object from which tags were deleted.

          
    

  .. py:method:: describe_batch_predictions(**kwargs)

    

    Returns a list of ``BatchPrediction`` operations that match the search criteria in the request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeBatchPredictions>`_    


    **Request Syntax** 
    ::

      response = client.describe_batch_predictions(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'MLModelId'|'DataSourceId'|'DataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          NextToken='string',
          Limit=123
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``BatchPrediction`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to the ``BatchPrediction`` creation date.
       
      * ``Status`` - Sets the search criteria to the ``BatchPrediction`` status.
       
      * ``Name`` - Sets the search criteria to the contents of the ``BatchPrediction`` ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``BatchPrediction`` creation.
       
      * ``MLModelId`` - Sets the search criteria to the ``MLModel`` used in the ``BatchPrediction`` .
       
      * ``DataSourceId`` - Sets the search criteria to the ``DataSource`` used in the ``BatchPrediction`` .
       
      * ``DataURI`` - Sets the search criteria to the data file(s) used in the ``BatchPrediction`` . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, a ``Batch Prediction`` operation could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``BatchPrediction`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``MLModel`` s.

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
    :type NextToken: string
    :param NextToken: 

      An ID of the page in the paginated results.

      

    
    :type Limit: integer
    :param Limit: 

      The number of pages of information to include in the result. The range of acceptable values is ``1`` through ``100`` . The default value is ``100`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Results': [
                {
                    'BatchPredictionId': 'string',
                    'MLModelId': 'string',
                    'BatchPredictionDataSourceId': 'string',
                    'InputDataLocationS3': 'string',
                    'CreatedByIamUser': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1),
                    'Name': 'string',
                    'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                    'OutputUri': 'string',
                    'Message': 'string',
                    'ComputeTime': 123,
                    'FinishedAt': datetime(2015, 1, 1),
                    'StartedAt': datetime(2015, 1, 1),
                    'TotalRecordCount': 123,
                    'InvalidRecordCount': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeBatchPredictions`` operation. The content is essentially a list of ``BatchPrediction`` s.

        
        

        - **Results** *(list) --* 

          A list of ``BatchPrediction`` objects that meet the search criteria. 

          
          

          - *(dict) --* 

            Represents the output of a ``GetBatchPrediction`` operation.

             

            The content consists of the detailed metadata, the status, and the data file information of a ``Batch Prediction`` .

            
            

            - **BatchPredictionId** *(string) --* 

              The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to the value of the ``BatchPredictionID`` in the request. 

              
            

            - **MLModelId** *(string) --* 

              The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.

              
            

            - **BatchPredictionDataSourceId** *(string) --* 

              The ID of the ``DataSource`` that points to the group of observations to predict.

              
            

            - **InputDataLocationS3** *(string) --* 

              The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

              
            

            - **CreatedByIamUser** *(string) --* 

              The AWS user account that invoked the ``BatchPrediction`` . The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

              
            

            - **CreatedAt** *(datetime) --* 

              The time that the ``BatchPrediction`` was created. The time is expressed in epoch time.

              
            

            - **LastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in epoch time.

              
            

            - **Name** *(string) --* 

              A user-supplied name or description of the ``BatchPrediction`` .

              
            

            - **Status** *(string) --* 

              The status of the ``BatchPrediction`` . This element can have one of the following values:

               

               
              * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate predictions for a batch of observations.
               
              * ``INPROGRESS`` - The process is underway.
               
              * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is not usable.
               
              * ``COMPLETED`` - The batch prediction process completed successfully.
               
              * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.
               

              
            

            - **OutputUri** *(string) --* 

              The location of an Amazon S3 bucket or directory to receive the operation results. The following substrings are not allowed in the ``s3 key`` portion of the ``outputURI`` field: ':', '//', '/./', '/../'.

              
            

            - **Message** *(string) --* 

              A description of the most recent details about processing the batch prediction request.

              
            

            - **ComputeTime** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **FinishedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **StartedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **TotalRecordCount** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **InvalidRecordCount** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
        
      
        

        - **NextToken** *(string) --* 

          The ID of the next page in the paginated results that indicates at least one more page follows.

          
    

  .. py:method:: describe_data_sources(**kwargs)

    

    Returns a list of ``DataSource`` that match the search criteria in the request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeDataSources>`_    


    **Request Syntax** 
    ::

      response = client.describe_data_sources(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'DataLocationS3'|'IAMUser',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          NextToken='string',
          Limit=123
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``DataSource`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to ``DataSource`` creation dates.
       
      * ``Status`` - Sets the search criteria to ``DataSource`` statuses.
       
      * ``Name`` - Sets the search criteria to the contents of ``DataSource``  ****  ``Name`` .
       
      * ``DataUri`` - Sets the search criteria to the URI of data files used to create the ``DataSource`` . The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``DataSource`` creation.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``DataSource`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``DataSource`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``DataSource`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, a ``DataSource`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``DataSource`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``DataSource`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
    :type NextToken: string
    :param NextToken: 

      The ID of the page in the paginated results.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of ``DataSource`` to include in the result.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Results': [
                {
                    'DataSourceId': 'string',
                    'DataLocationS3': 'string',
                    'DataRearrangement': 'string',
                    'CreatedByIamUser': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1),
                    'DataSizeInBytes': 123,
                    'NumberOfFiles': 123,
                    'Name': 'string',
                    'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                    'Message': 'string',
                    'RedshiftMetadata': {
                        'RedshiftDatabase': {
                            'DatabaseName': 'string',
                            'ClusterIdentifier': 'string'
                        },
                        'DatabaseUserName': 'string',
                        'SelectSqlQuery': 'string'
                    },
                    'RDSMetadata': {
                        'Database': {
                            'InstanceIdentifier': 'string',
                            'DatabaseName': 'string'
                        },
                        'DatabaseUserName': 'string',
                        'SelectSqlQuery': 'string',
                        'ResourceRole': 'string',
                        'ServiceRole': 'string',
                        'DataPipelineId': 'string'
                    },
                    'RoleARN': 'string',
                    'ComputeStatistics': True|False,
                    'ComputeTime': 123,
                    'FinishedAt': datetime(2015, 1, 1),
                    'StartedAt': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the query results from a  DescribeDataSources operation. The content is essentially a list of ``DataSource`` .

        
        

        - **Results** *(list) --* 

          A list of ``DataSource`` that meet the search criteria. 

          
          

          - *(dict) --* 

            Represents the output of the ``GetDataSource`` operation. 

             

            The content consists of the detailed metadata and data file information and the current status of the ``DataSource`` . 

            
            

            - **DataSourceId** *(string) --* 

              The ID that is assigned to the ``DataSource`` during creation.

              
            

            - **DataLocationS3** *(string) --* 

              The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is used by a ``DataSource`` .

              
            

            - **DataRearrangement** *(string) --* 

              A JSON string that represents the splitting and rearrangement requirement used when this ``DataSource`` was created.

              
            

            - **CreatedByIamUser** *(string) --* 

              The AWS user account from which the ``DataSource`` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

              
            

            - **CreatedAt** *(datetime) --* 

              The time that the ``DataSource`` was created. The time is expressed in epoch time.

              
            

            - **LastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in epoch time.

              
            

            - **DataSizeInBytes** *(integer) --* 

              The total number of observations contained in the data files that the ``DataSource`` references.

              
            

            - **NumberOfFiles** *(integer) --* 

              The number of data files referenced by the ``DataSource`` .

              
            

            - **Name** *(string) --* 

              A user-supplied name or description of the ``DataSource`` .

              
            

            - **Status** *(string) --* 

              The current status of the ``DataSource`` . This element can have one of the following values: 

               

               
              * PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a ``DataSource`` .
               
              * INPROGRESS - The creation process is underway.
               
              * FAILED - The request to create a ``DataSource`` did not run to completion. It is not usable.
               
              * COMPLETED - The creation process completed successfully.
               
              * DELETED - The ``DataSource`` is marked as deleted. It is not usable.
               

              
            

            - **Message** *(string) --* 

              A description of the most recent details about creating the ``DataSource`` .

              
            

            - **RedshiftMetadata** *(dict) --* 

              Describes the ``DataSource`` details specific to Amazon Redshift.

              
              

              - **RedshiftDatabase** *(dict) --* 

                Describes the database details required to connect to an Amazon Redshift database.

                
                

                - **DatabaseName** *(string) --* 

                  The name of a database hosted on an Amazon Redshift cluster.

                  
                

                - **ClusterIdentifier** *(string) --* 

                  The ID of an Amazon Redshift cluster.

                  
            
              

              - **DatabaseUserName** *(string) --* 

                A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

                
              

              - **SelectSqlQuery** *(string) --* 

                The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if ``Verbose`` is true in GetDataSourceInput. 

                
          
            

            - **RDSMetadata** *(dict) --* 

              The datasource details that are specific to Amazon RDS.

              
              

              - **Database** *(dict) --* 

                The database details required to connect to an Amazon RDS.

                
                

                - **InstanceIdentifier** *(string) --* 

                  The ID of an RDS DB instance.

                  
                

                - **DatabaseName** *(string) --* 

                  The name of a database hosted on an RDS DB instance.

                  
            
              

              - **DatabaseUserName** *(string) --* 

                The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.

                
              

              - **SelectSqlQuery** *(string) --* 

                The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if ``Verbose`` is true in ``GetDataSourceInput`` . 

                
              

              - **ResourceRole** *(string) --* 

                The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.

                
              

              - **ServiceRole** *(string) --* 

                The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.

                
              

              - **DataPipelineId** *(string) --* 

                The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to Amazon S3. You can use the ID to find details about the instance in the Data Pipeline console.

                
          
            

            - **RoleARN** *(string) --* 

              The Amazon Resource Name (ARN) of an `AWS IAM Role <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__ , such as the following: arn:aws:iam::account:role/rolename. 

              
            

            - **ComputeStatistics** *(boolean) --* 

              The parameter is ``true`` if statistics need to be generated from the observation data. 

              
            

            - **ComputeTime** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **FinishedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **StartedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
        
      
        

        - **NextToken** *(string) --* 

          An ID of the next page in the paginated results that indicates at least one more page follows.

          
    

  .. py:method:: describe_evaluations(**kwargs)

    

    Returns a list of ``DescribeEvaluations`` that match the search criteria in the request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeEvaluations>`_    


    **Request Syntax** 
    ::

      response = client.describe_evaluations(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'MLModelId'|'DataSourceId'|'DataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          NextToken='string',
          Limit=123
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variable to filter a list of ``Evaluation`` objects:

       

       
      * ``CreatedAt`` - Sets the search criteria to the ``Evaluation`` creation date.
       
      * ``Status`` - Sets the search criteria to the ``Evaluation`` status.
       
      * ``Name`` - Sets the search criteria to the contents of ``Evaluation``  ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked an ``Evaluation`` .
       
      * ``MLModelId`` - Sets the search criteria to the ``MLModel`` that was evaluated.
       
      * ``DataSourceId`` - Sets the search criteria to the ``DataSource`` used in ``Evaluation`` .
       
      * ``DataUri`` - Sets the search criteria to the data file(s) used in ``Evaluation`` . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``Evaluation`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``Evaluation`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, an ``Evaluation`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``Evaluation`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``Evaluation`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
    :type NextToken: string
    :param NextToken: 

      The ID of the page in the paginated results.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of ``Evaluation`` to include in the result.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Results': [
                {
                    'EvaluationId': 'string',
                    'MLModelId': 'string',
                    'EvaluationDataSourceId': 'string',
                    'InputDataLocationS3': 'string',
                    'CreatedByIamUser': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1),
                    'Name': 'string',
                    'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                    'PerformanceMetrics': {
                        'Properties': {
                            'string': 'string'
                        }
                    },
                    'Message': 'string',
                    'ComputeTime': 123,
                    'FinishedAt': datetime(2015, 1, 1),
                    'StartedAt': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the query results from a ``DescribeEvaluations`` operation. The content is essentially a list of ``Evaluation`` .

        
        

        - **Results** *(list) --* 

          A list of ``Evaluation`` that meet the search criteria. 

          
          

          - *(dict) --* 

            Represents the output of ``GetEvaluation`` operation. 

             

            The content consists of the detailed metadata and data file information and the current status of the ``Evaluation`` .

            
            

            - **EvaluationId** *(string) --* 

              The ID that is assigned to the ``Evaluation`` at creation.

              
            

            - **MLModelId** *(string) --* 

              The ID of the ``MLModel`` that is the focus of the evaluation.

              
            

            - **EvaluationDataSourceId** *(string) --* 

              The ID of the ``DataSource`` that is used to evaluate the ``MLModel`` .

              
            

            - **InputDataLocationS3** *(string) --* 

              The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is used in the evaluation.

              
            

            - **CreatedByIamUser** *(string) --* 

              The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

              
            

            - **CreatedAt** *(datetime) --* 

              The time that the ``Evaluation`` was created. The time is expressed in epoch time.

              
            

            - **LastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch time.

              
            

            - **Name** *(string) --* 

              A user-supplied name or description of the ``Evaluation`` . 

              
            

            - **Status** *(string) --* 

              The status of the evaluation. This element can have one of the following values:

               

               
              * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an ``MLModel`` .
               
              * ``INPROGRESS`` - The evaluation is underway.
               
              * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is not usable.
               
              * ``COMPLETED`` - The evaluation process completed successfully.
               
              * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.
               

              
            

            - **PerformanceMetrics** *(dict) --* 

              Measurements of how well the ``MLModel`` performed, using observations referenced by the ``DataSource`` . One of the following metrics is returned, based on the type of the ``MLModel`` : 

               

               
              * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to measure performance.  
               
              * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable. 
               
              * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure performance.  
               

               

              For more information about performance metrics, please see the `Amazon Machine Learning Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ . 

              
              

              - **Properties** *(dict) --* 
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
            

            - **Message** *(string) --* 

              A description of the most recent details about evaluating the ``MLModel`` .

              
            

            - **ComputeTime** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **FinishedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **StartedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
        
      
        

        - **NextToken** *(string) --* 

          The ID of the next page in the paginated results that indicates at least one more page follows.

          
    

  .. py:method:: describe_ml_models(**kwargs)

    

    Returns a list of ``MLModel`` that match the search criteria in the request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeMLModels>`_    


    **Request Syntax** 
    ::

      response = client.describe_ml_models(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'TrainingDataSourceId'|'RealtimeEndpointStatus'|'MLModelType'|'Algorithm'|'TrainingDataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          NextToken='string',
          Limit=123
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``MLModel`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to ``MLModel`` creation date.
       
      * ``Status`` - Sets the search criteria to ``MLModel`` status.
       
      * ``Name`` - Sets the search criteria to the contents of ``MLModel`` ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``MLModel`` creation.
       
      * ``TrainingDataSourceId`` - Sets the search criteria to the ``DataSource`` used to train one or more ``MLModel`` .
       
      * ``RealtimeEndpointStatus`` - Sets the search criteria to the ``MLModel`` real-time endpoint status.
       
      * ``MLModelType`` - Sets the search criteria to ``MLModel`` type: binary, regression, or multi-class.
       
      * ``Algorithm`` - Sets the search criteria to the algorithm that the ``MLModel`` uses.
       
      * ``TrainingDataURI`` - Sets the search criteria to the data file(s) used in training a ``MLModel`` . The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``MLModel`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``MLModel`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``MLModel`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, an ``MLModel`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``MLModel`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``MLModel`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
    :type NextToken: string
    :param NextToken: 

      The ID of the page in the paginated results.

      

    
    :type Limit: integer
    :param Limit: 

      The number of pages of information to include in the result. The range of acceptable values is ``1`` through ``100`` . The default value is ``100`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Results': [
                {
                    'MLModelId': 'string',
                    'TrainingDataSourceId': 'string',
                    'CreatedByIamUser': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1),
                    'Name': 'string',
                    'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                    'SizeInBytes': 123,
                    'EndpointInfo': {
                        'PeakRequestsPerSecond': 123,
                        'CreatedAt': datetime(2015, 1, 1),
                        'EndpointUrl': 'string',
                        'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
                    },
                    'TrainingParameters': {
                        'string': 'string'
                    },
                    'InputDataLocationS3': 'string',
                    'Algorithm': 'sgd',
                    'MLModelType': 'REGRESSION'|'BINARY'|'MULTICLASS',
                    'ScoreThreshold': ...,
                    'ScoreThresholdLastUpdatedAt': datetime(2015, 1, 1),
                    'Message': 'string',
                    'ComputeTime': 123,
                    'FinishedAt': datetime(2015, 1, 1),
                    'StartedAt': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeMLModels`` operation. The content is essentially a list of ``MLModel`` .

        
        

        - **Results** *(list) --* 

          A list of ``MLModel`` that meet the search criteria.

          
          

          - *(dict) --* 

            Represents the output of a ``GetMLModel`` operation. 

             

            The content consists of the detailed metadata and the current status of the ``MLModel`` .

            
            

            - **MLModelId** *(string) --* 

              The ID assigned to the ``MLModel`` at creation.

              
            

            - **TrainingDataSourceId** *(string) --* 

              The ID of the training ``DataSource`` . The ``CreateMLModel`` operation uses the ``TrainingDataSourceId`` .

              
            

            - **CreatedByIamUser** *(string) --* 

              The AWS user account from which the ``MLModel`` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

              
            

            - **CreatedAt** *(datetime) --* 

              The time that the ``MLModel`` was created. The time is expressed in epoch time.

              
            

            - **LastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.

              
            

            - **Name** *(string) --* 

              A user-supplied name or description of the ``MLModel`` .

              
            

            - **Status** *(string) --* 

              The current status of an ``MLModel`` . This element can have one of the following values: 

               

               
              * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to create an ``MLModel`` .
               
              * ``INPROGRESS`` - The creation process is underway.
               
              * ``FAILED`` - The request to create an ``MLModel`` didn't run to completion. The model isn't usable.
               
              * ``COMPLETED`` - The creation process completed successfully.
               
              * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn't usable.
               

              
            

            - **SizeInBytes** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **EndpointInfo** *(dict) --* 

              The current endpoint of the ``MLModel`` .

              
              

              - **PeakRequestsPerSecond** *(integer) --* 

                The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in incoming requests per second.

                
              

              - **CreatedAt** *(datetime) --* 

                The time that the request to create the real-time endpoint for the ``MLModel`` was received. The time is expressed in epoch time.

                
              

              - **EndpointUrl** *(string) --* 

                The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

                 

                .. note::

                  Note 

                  The application must wait until the real-time endpoint is ready before using this URI.

                   

                
              

              - **EndpointStatus** *(string) --* 

                The current status of the real-time endpoint for the ``MLModel`` . This element can have one of the following values: 

                 

                 
                * ``NONE`` - Endpoint does not exist or was previously deleted.
                 
                * ``READY`` - Endpoint is ready to be used for real-time predictions.
                 
                * ``UPDATING`` - Updating/creating the endpoint. 
                 

                
          
            

            - **TrainingParameters** *(dict) --* 

              A list of the training parameters in the ``MLModel`` . The list is implemented as a map of key-value pairs.

               

              The following is the current set of training parameters: 

               

               
              * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` . 
               
              * ``sgd.maxPasses`` - The number of times that the training process traverses the observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to ``10000`` . The default value is ``10`` .
               
              * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are ``auto`` and ``none`` . The default value is ``none`` .
               
              * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm, which controls overfitting the data by penalizing large coefficients. This parameter tends to drive coefficients to zero, resulting in sparse feature set. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter can't be used when ``L2`` is specified. Use this parameter sparingly. 
               
              * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm, which controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L2 normalization. This parameter can't be used when ``L1`` is specified. Use this parameter sparingly. 
               

              
              

              - *(string) --* 

                String type.

                
                

                - *(string) --* 

                  String type.

                  
          
        
            

            - **InputDataLocationS3** *(string) --* 

              The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

              
            

            - **Algorithm** *(string) --* 

              The algorithm used to train the ``MLModel`` . The following algorithm is supported:

               

               
              * ``SGD`` -- Stochastic gradient descent. The goal of ``SGD`` is to minimize the gradient of the loss function. 
               

              
            

            - **MLModelType** *(string) --* 

              Identifies the ``MLModel`` category. The following are the available types:

               

               
              * ``REGRESSION`` - Produces a numeric result. For example, "What price should a house be listed at?"
               
              * ``BINARY`` - Produces one of two possible results. For example, "Is this a child-friendly web site?".
               
              * ``MULTICLASS`` - Produces one of several possible results. For example, "Is this a HIGH-, LOW-, or MEDIUM-risk trade?".
               

              
            

            - **ScoreThreshold** *(float) --* 
            

            - **ScoreThresholdLastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in epoch time.

              
            

            - **Message** *(string) --* 

              A description of the most recent details about accessing the ``MLModel`` .

              
            

            - **ComputeTime** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **FinishedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **StartedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
        
      
        

        - **NextToken** *(string) --* 

          The ID of the next page in the paginated results that indicates at least one more page follows.

          
    

  .. py:method:: describe_tags(**kwargs)

    

    Describes one or more of the tags for your Amazon ML object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeTags>`_    


    **Request Syntax** 
    ::

      response = client.describe_tags(
          ResourceId='string',
          ResourceType='BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The ID of the ML object. For example, ``exampleModelId`` . 

      

    
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of the ML object.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceId': 'string',
            'ResourceType': 'BatchPrediction'|'DataSource'|'Evaluation'|'MLModel',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Amazon ML returns the following elements. 

        
        

        - **ResourceId** *(string) --* 

          The ID of the tagged ML object.

          
        

        - **ResourceType** *(string) --* 

          The type of the tagged ML object.

          
        

        - **Tags** *(list) --* 

          A list of tags associated with the ML object.

          
          

          - *(dict) --* 

            A custom key-value pair associated with an ML object, such as an ML model.

            
            

            - **Key** *(string) --* 

              A unique identifier for the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.

              
            

            - **Value** *(string) --* 

              An optional string, typically used to describe or define the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.

              
        
      
    

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


  .. py:method:: get_batch_prediction(**kwargs)

    

    Returns a ``BatchPrediction`` that includes detailed metadata, status, and data file information for a ``Batch Prediction`` request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/GetBatchPrediction>`_    


    **Request Syntax** 
    ::

      response = client.get_batch_prediction(
          BatchPredictionId='string'
      )
    :type BatchPredictionId: string
    :param BatchPredictionId: **[REQUIRED]** 

      An ID assigned to the ``BatchPrediction`` at creation.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BatchPredictionId': 'string',
            'MLModelId': 'string',
            'BatchPredictionDataSourceId': 'string',
            'InputDataLocationS3': 'string',
            'CreatedByIamUser': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1),
            'Name': 'string',
            'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
            'OutputUri': 'string',
            'LogUri': 'string',
            'Message': 'string',
            'ComputeTime': 123,
            'FinishedAt': datetime(2015, 1, 1),
            'StartedAt': datetime(2015, 1, 1),
            'TotalRecordCount': 123,
            'InvalidRecordCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``GetBatchPrediction`` operation and describes a ``BatchPrediction`` .

        
        

        - **BatchPredictionId** *(string) --* 

          An ID assigned to the ``BatchPrediction`` at creation. This value should be identical to the value of the ``BatchPredictionID`` in the request.

          
        

        - **MLModelId** *(string) --* 

          The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.

          
        

        - **BatchPredictionDataSourceId** *(string) --* 

          The ID of the ``DataSource`` that was used to create the ``BatchPrediction`` . 

          
        

        - **InputDataLocationS3** *(string) --* 

          The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

          
        

        - **CreatedByIamUser** *(string) --* 

          The AWS user account that invoked the ``BatchPrediction`` . The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

          
        

        - **CreatedAt** *(datetime) --* 

          The time when the ``BatchPrediction`` was created. The time is expressed in epoch time.

          
        

        - **LastUpdatedAt** *(datetime) --* 

          The time of the most recent edit to ``BatchPrediction`` . The time is expressed in epoch time.

          
        

        - **Name** *(string) --* 

          A user-supplied name or description of the ``BatchPrediction`` .

          
        

        - **Status** *(string) --* 

          The status of the ``BatchPrediction`` , which can be one of the following values:

           

           
          * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate batch predictions.
           
          * ``INPROGRESS`` - The batch predictions are in progress.
           
          * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is not usable.
           
          * ``COMPLETED`` - The batch prediction process completed successfully.
           
          * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.
           

          
        

        - **OutputUri** *(string) --* 

          The location of an Amazon S3 bucket or directory to receive the operation results.

          
        

        - **LogUri** *(string) --* 

          A link to the file that contains logs of the ``CreateBatchPrediction`` operation.

          
        

        - **Message** *(string) --* 

          A description of the most recent details about processing the batch prediction request.

          
        

        - **ComputeTime** *(integer) --* 

          The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the ``BatchPrediction`` , normalized and scaled on computation resources. ``ComputeTime`` is only available if the ``BatchPrediction`` is in the ``COMPLETED`` state.

          
        

        - **FinishedAt** *(datetime) --* 

          The epoch time when Amazon Machine Learning marked the ``BatchPrediction`` as ``COMPLETED`` or ``FAILED`` . ``FinishedAt`` is only available when the ``BatchPrediction`` is in the ``COMPLETED`` or ``FAILED`` state.

          
        

        - **StartedAt** *(datetime) --* 

          The epoch time when Amazon Machine Learning marked the ``BatchPrediction`` as ``INPROGRESS`` . ``StartedAt`` isn't available if the ``BatchPrediction`` is in the ``PENDING`` state.

          
        

        - **TotalRecordCount** *(integer) --* 

          The number of total records that Amazon Machine Learning saw while processing the ``BatchPrediction`` .

          
        

        - **InvalidRecordCount** *(integer) --* 

          The number of invalid records that Amazon Machine Learning saw while processing the ``BatchPrediction`` .

          
    

  .. py:method:: get_data_source(**kwargs)

    

    Returns a ``DataSource`` that includes metadata and data file information, as well as the current status of the ``DataSource`` .

     

    ``GetDataSource`` provides results in normal or verbose format. The verbose format adds the schema description and the list of files pointed to by the DataSource to the normal format.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/GetDataSource>`_    


    **Request Syntax** 
    ::

      response = client.get_data_source(
          DataSourceId='string',
          Verbose=True|False
      )
    :type DataSourceId: string
    :param DataSourceId: **[REQUIRED]** 

      The ID assigned to the ``DataSource`` at creation.

      

    
    :type Verbose: boolean
    :param Verbose: 

      Specifies whether the ``GetDataSource`` operation should return ``DataSourceSchema`` .

       

      If true, ``DataSourceSchema`` is returned.

       

      If false, ``DataSourceSchema`` is not returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DataSourceId': 'string',
            'DataLocationS3': 'string',
            'DataRearrangement': 'string',
            'CreatedByIamUser': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1),
            'DataSizeInBytes': 123,
            'NumberOfFiles': 123,
            'Name': 'string',
            'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
            'LogUri': 'string',
            'Message': 'string',
            'RedshiftMetadata': {
                'RedshiftDatabase': {
                    'DatabaseName': 'string',
                    'ClusterIdentifier': 'string'
                },
                'DatabaseUserName': 'string',
                'SelectSqlQuery': 'string'
            },
            'RDSMetadata': {
                'Database': {
                    'InstanceIdentifier': 'string',
                    'DatabaseName': 'string'
                },
                'DatabaseUserName': 'string',
                'SelectSqlQuery': 'string',
                'ResourceRole': 'string',
                'ServiceRole': 'string',
                'DataPipelineId': 'string'
            },
            'RoleARN': 'string',
            'ComputeStatistics': True|False,
            'ComputeTime': 123,
            'FinishedAt': datetime(2015, 1, 1),
            'StartedAt': datetime(2015, 1, 1),
            'DataSourceSchema': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``GetDataSource`` operation and describes a ``DataSource`` .

        
        

        - **DataSourceId** *(string) --* 

          The ID assigned to the ``DataSource`` at creation. This value should be identical to the value of the ``DataSourceId`` in the request.

          
        

        - **DataLocationS3** *(string) --* 

          The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

          
        

        - **DataRearrangement** *(string) --* 

          A JSON string that represents the splitting and rearrangement requirement used when this ``DataSource`` was created.

          
        

        - **CreatedByIamUser** *(string) --* 

          The AWS user account from which the ``DataSource`` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

          
        

        - **CreatedAt** *(datetime) --* 

          The time that the ``DataSource`` was created. The time is expressed in epoch time.

          
        

        - **LastUpdatedAt** *(datetime) --* 

          The time of the most recent edit to the ``DataSource`` . The time is expressed in epoch time.

          
        

        - **DataSizeInBytes** *(integer) --* 

          The total size of observations in the data files.

          
        

        - **NumberOfFiles** *(integer) --* 

          The number of data files referenced by the ``DataSource`` .

          
        

        - **Name** *(string) --* 

          A user-supplied name or description of the ``DataSource`` .

          
        

        - **Status** *(string) --* 

          The current status of the ``DataSource`` . This element can have one of the following values:

           

           
          * ``PENDING`` - Amazon ML submitted a request to create a ``DataSource`` .
           
          * ``INPROGRESS`` - The creation process is underway.
           
          * ``FAILED`` - The request to create a ``DataSource`` did not run to completion. It is not usable.
           
          * ``COMPLETED`` - The creation process completed successfully.
           
          * ``DELETED`` - The ``DataSource`` is marked as deleted. It is not usable.
           

          
        

        - **LogUri** *(string) --* 

          A link to the file containing logs of ``CreateDataSourceFrom*`` operations.

          
        

        - **Message** *(string) --* 

          The user-supplied description of the most recent details about creating the ``DataSource`` .

          
        

        - **RedshiftMetadata** *(dict) --* 

          Describes the ``DataSource`` details specific to Amazon Redshift.

          
          

          - **RedshiftDatabase** *(dict) --* 

            Describes the database details required to connect to an Amazon Redshift database.

            
            

            - **DatabaseName** *(string) --* 

              The name of a database hosted on an Amazon Redshift cluster.

              
            

            - **ClusterIdentifier** *(string) --* 

              The ID of an Amazon Redshift cluster.

              
        
          

          - **DatabaseUserName** *(string) --* 

            A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

            
          

          - **SelectSqlQuery** *(string) --* 

            The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if ``Verbose`` is true in GetDataSourceInput. 

            
      
        

        - **RDSMetadata** *(dict) --* 

          The datasource details that are specific to Amazon RDS.

          
          

          - **Database** *(dict) --* 

            The database details required to connect to an Amazon RDS.

            
            

            - **InstanceIdentifier** *(string) --* 

              The ID of an RDS DB instance.

              
            

            - **DatabaseName** *(string) --* 

              The name of a database hosted on an RDS DB instance.

              
        
          

          - **DatabaseUserName** *(string) --* 

            The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.

            
          

          - **SelectSqlQuery** *(string) --* 

            The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if ``Verbose`` is true in ``GetDataSourceInput`` . 

            
          

          - **ResourceRole** *(string) --* 

            The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.

            
          

          - **ServiceRole** *(string) --* 

            The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.

            
          

          - **DataPipelineId** *(string) --* 

            The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to Amazon S3. You can use the ID to find details about the instance in the Data Pipeline console.

            
      
        

        - **RoleARN** *(string) --* 

          The Amazon Resource Name (ARN) of an `AWS IAM Role <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__ , such as the following: arn:aws:iam::account:role/rolename. 

          
        

        - **ComputeStatistics** *(boolean) --* 

          The parameter is ``true`` if statistics need to be generated from the observation data. 

          
        

        - **ComputeTime** *(integer) --* 

          The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the ``DataSource`` , normalized and scaled on computation resources. ``ComputeTime`` is only available if the ``DataSource`` is in the ``COMPLETED`` state and the ``ComputeStatistics`` is set to true.

          
        

        - **FinishedAt** *(datetime) --* 

          The epoch time when Amazon Machine Learning marked the ``DataSource`` as ``COMPLETED`` or ``FAILED`` . ``FinishedAt`` is only available when the ``DataSource`` is in the ``COMPLETED`` or ``FAILED`` state.

          
        

        - **StartedAt** *(datetime) --* 

          The epoch time when Amazon Machine Learning marked the ``DataSource`` as ``INPROGRESS`` . ``StartedAt`` isn't available if the ``DataSource`` is in the ``PENDING`` state.

          
        

        - **DataSourceSchema** *(string) --* 

          The schema used by all of the data files of this ``DataSource`` .

           

          .. note::

            Note 

            This parameter is provided as part of the verbose format.

            

          
    

  .. py:method:: get_evaluation(**kwargs)

    

    Returns an ``Evaluation`` that includes metadata as well as the current status of the ``Evaluation`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/GetEvaluation>`_    


    **Request Syntax** 
    ::

      response = client.get_evaluation(
          EvaluationId='string'
      )
    :type EvaluationId: string
    :param EvaluationId: **[REQUIRED]** 

      The ID of the ``Evaluation`` to retrieve. The evaluation of each ``MLModel`` is recorded and cataloged. The ID provides the means to access the information. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EvaluationId': 'string',
            'MLModelId': 'string',
            'EvaluationDataSourceId': 'string',
            'InputDataLocationS3': 'string',
            'CreatedByIamUser': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1),
            'Name': 'string',
            'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
            'PerformanceMetrics': {
                'Properties': {
                    'string': 'string'
                }
            },
            'LogUri': 'string',
            'Message': 'string',
            'ComputeTime': 123,
            'FinishedAt': datetime(2015, 1, 1),
            'StartedAt': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``GetEvaluation`` operation and describes an ``Evaluation`` .

        
        

        - **EvaluationId** *(string) --* 

          The evaluation ID which is same as the ``EvaluationId`` in the request.

          
        

        - **MLModelId** *(string) --* 

          The ID of the ``MLModel`` that was the focus of the evaluation.

          
        

        - **EvaluationDataSourceId** *(string) --* 

          The ``DataSource`` used for this evaluation.

          
        

        - **InputDataLocationS3** *(string) --* 

          The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

          
        

        - **CreatedByIamUser** *(string) --* 

          The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

          
        

        - **CreatedAt** *(datetime) --* 

          The time that the ``Evaluation`` was created. The time is expressed in epoch time.

          
        

        - **LastUpdatedAt** *(datetime) --* 

          The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch time.

          
        

        - **Name** *(string) --* 

          A user-supplied name or description of the ``Evaluation`` . 

          
        

        - **Status** *(string) --* 

          The status of the evaluation. This element can have one of the following values:

           

           
          * ``PENDING`` - Amazon Machine Language (Amazon ML) submitted a request to evaluate an ``MLModel`` .
           
          * ``INPROGRESS`` - The evaluation is underway.
           
          * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is not usable.
           
          * ``COMPLETED`` - The evaluation process completed successfully.
           
          * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.
           

          
        

        - **PerformanceMetrics** *(dict) --* 

          Measurements of how well the ``MLModel`` performed using observations referenced by the ``DataSource`` . One of the following metric is returned based on the type of the ``MLModel`` : 

           

           
          * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to measure performance.  
           
          * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable. 
           
          * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure performance.  
           

           

          For more information about performance metrics, please see the `Amazon Machine Learning Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ . 

          
          

          - **Properties** *(dict) --* 
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
        

        - **LogUri** *(string) --* 

          A link to the file that contains logs of the ``CreateEvaluation`` operation.

          
        

        - **Message** *(string) --* 

          A description of the most recent details about evaluating the ``MLModel`` .

          
        

        - **ComputeTime** *(integer) --* 

          The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the ``Evaluation`` , normalized and scaled on computation resources. ``ComputeTime`` is only available if the ``Evaluation`` is in the ``COMPLETED`` state.

          
        

        - **FinishedAt** *(datetime) --* 

          The epoch time when Amazon Machine Learning marked the ``Evaluation`` as ``COMPLETED`` or ``FAILED`` . ``FinishedAt`` is only available when the ``Evaluation`` is in the ``COMPLETED`` or ``FAILED`` state.

          
        

        - **StartedAt** *(datetime) --* 

          The epoch time when Amazon Machine Learning marked the ``Evaluation`` as ``INPROGRESS`` . ``StartedAt`` isn't available if the ``Evaluation`` is in the ``PENDING`` state.

          
    

  .. py:method:: get_ml_model(**kwargs)

    

    Returns an ``MLModel`` that includes detailed metadata, data source information, and the current status of the ``MLModel`` .

     

    ``GetMLModel`` provides results in normal or verbose format. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/GetMLModel>`_    


    **Request Syntax** 
    ::

      response = client.get_ml_model(
          MLModelId='string',
          Verbose=True|False
      )
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      The ID assigned to the ``MLModel`` at creation.

      

    
    :type Verbose: boolean
    :param Verbose: 

      Specifies whether the ``GetMLModel`` operation should return ``Recipe`` .

       

      If true, ``Recipe`` is returned.

       

      If false, ``Recipe`` is not returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MLModelId': 'string',
            'TrainingDataSourceId': 'string',
            'CreatedByIamUser': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1),
            'Name': 'string',
            'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
            'SizeInBytes': 123,
            'EndpointInfo': {
                'PeakRequestsPerSecond': 123,
                'CreatedAt': datetime(2015, 1, 1),
                'EndpointUrl': 'string',
                'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
            },
            'TrainingParameters': {
                'string': 'string'
            },
            'InputDataLocationS3': 'string',
            'MLModelType': 'REGRESSION'|'BINARY'|'MULTICLASS',
            'ScoreThreshold': ...,
            'ScoreThresholdLastUpdatedAt': datetime(2015, 1, 1),
            'LogUri': 'string',
            'Message': 'string',
            'ComputeTime': 123,
            'FinishedAt': datetime(2015, 1, 1),
            'StartedAt': datetime(2015, 1, 1),
            'Recipe': 'string',
            'Schema': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``GetMLModel`` operation, and provides detailed information about a ``MLModel`` .

        
        

        - **MLModelId** *(string) --* 

          The MLModel ID,which is same as the ``MLModelId`` in the request.

          
        

        - **TrainingDataSourceId** *(string) --* 

          The ID of the training ``DataSource`` .

          
        

        - **CreatedByIamUser** *(string) --* 

          The AWS user account from which the ``MLModel`` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

          
        

        - **CreatedAt** *(datetime) --* 

          The time that the ``MLModel`` was created. The time is expressed in epoch time.

          
        

        - **LastUpdatedAt** *(datetime) --* 

          The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.

          
        

        - **Name** *(string) --* 

          A user-supplied name or description of the ``MLModel`` .

          
        

        - **Status** *(string) --* 

          The current status of the ``MLModel`` . This element can have one of the following values:

           

           
          * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to describe a ``MLModel`` .
           
          * ``INPROGRESS`` - The request is processing.
           
          * ``FAILED`` - The request did not run to completion. The ML model isn't usable.
           
          * ``COMPLETED`` - The request completed successfully.
           
          * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn't usable.
           

          
        

        - **SizeInBytes** *(integer) --* 

          Long integer type that is a 64-bit signed number.

          
        

        - **EndpointInfo** *(dict) --* 

          The current endpoint of the ``MLModel`` 

          
          

          - **PeakRequestsPerSecond** *(integer) --* 

            The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in incoming requests per second.

            
          

          - **CreatedAt** *(datetime) --* 

            The time that the request to create the real-time endpoint for the ``MLModel`` was received. The time is expressed in epoch time.

            
          

          - **EndpointUrl** *(string) --* 

            The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

             

            .. note::

              Note 

              The application must wait until the real-time endpoint is ready before using this URI.

               

            
          

          - **EndpointStatus** *(string) --* 

            The current status of the real-time endpoint for the ``MLModel`` . This element can have one of the following values: 

             

             
            * ``NONE`` - Endpoint does not exist or was previously deleted.
             
            * ``READY`` - Endpoint is ready to be used for real-time predictions.
             
            * ``UPDATING`` - Updating/creating the endpoint. 
             

            
      
        

        - **TrainingParameters** *(dict) --* 

          A list of the training parameters in the ``MLModel`` . The list is implemented as a map of key-value pairs.

           

          The following is the current set of training parameters: 

           

           
          * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` . 
           
          * ``sgd.maxPasses`` - The number of times that the training process traverses the observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to ``10000`` . The default value is ``10`` .
           
          * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling data improves a model's ability to find the optimal solution for a variety of data types. The valid values are ``auto`` and ``none`` . The default value is ``none`` . We strongly recommend that you shuffle your data.
           
          * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter can't be used when ``L2`` is specified. Use this parameter sparingly. 
           
          * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L2 normalization. This parameter can't be used when ``L1`` is specified. Use this parameter sparingly. 
           

          
          

          - *(string) --* 

            String type.

            
            

            - *(string) --* 

              String type.

              
      
    
        

        - **InputDataLocationS3** *(string) --* 

          The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

          
        

        - **MLModelType** *(string) --* 

          Identifies the ``MLModel`` category. The following are the available types: 

           

           
          * REGRESSION -- Produces a numeric result. For example, "What price should a house be listed at?"
           
          * BINARY -- Produces one of two possible results. For example, "Is this an e-commerce website?"
           
          * MULTICLASS -- Produces one of several possible results. For example, "Is this a HIGH, LOW or MEDIUM risk trade?"
           

          
        

        - **ScoreThreshold** *(float) --* 

          The scoring threshold is used in binary classification ``MLModel``  models. It marks the boundary between a positive prediction and a negative prediction.

           

          Output values greater than or equal to the threshold receive a positive result from the MLModel, such as ``true`` . Output values less than the threshold receive a negative response from the MLModel, such as ``false`` .

          
        

        - **ScoreThresholdLastUpdatedAt** *(datetime) --* 

          The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in epoch time.

          
        

        - **LogUri** *(string) --* 

          A link to the file that contains logs of the ``CreateMLModel`` operation.

          
        

        - **Message** *(string) --* 

          A description of the most recent details about accessing the ``MLModel`` .

          
        

        - **ComputeTime** *(integer) --* 

          The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the ``MLModel`` , normalized and scaled on computation resources. ``ComputeTime`` is only available if the ``MLModel`` is in the ``COMPLETED`` state.

          
        

        - **FinishedAt** *(datetime) --* 

          The epoch time when Amazon Machine Learning marked the ``MLModel`` as ``COMPLETED`` or ``FAILED`` . ``FinishedAt`` is only available when the ``MLModel`` is in the ``COMPLETED`` or ``FAILED`` state.

          
        

        - **StartedAt** *(datetime) --* 

          The epoch time when Amazon Machine Learning marked the ``MLModel`` as ``INPROGRESS`` . ``StartedAt`` isn't available if the ``MLModel`` is in the ``PENDING`` state.

          
        

        - **Recipe** *(string) --* 

          The recipe to use when training the ``MLModel`` . The ``Recipe`` provides detailed information about the observation data to use during training, and manipulations to perform on the observation data during training.

           

          .. note::

            Note 

            This parameter is provided as part of the verbose format.

            

          
        

        - **Schema** *(string) --* 

          The schema used by all of the data files referenced by the ``DataSource`` .

           

          .. note::

            Note 

            This parameter is provided as part of the verbose format.

            

          
    

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

        


  .. py:method:: predict(**kwargs)

    

    Generates a prediction for the observation using the specified ``ML Model`` .

     

    .. note::

      Note 

      Not all response parameters will be populated. Whether a response parameter is populated depends on the type of model requested.

      

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/Predict>`_    


    **Request Syntax** 
    ::

      response = client.predict(
          MLModelId='string',
          Record={
              'string': 'string'
          },
          PredictEndpoint='string'
      )
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      A unique identifier of the ``MLModel`` .

      

    
    :type Record: dict
    :param Record: **[REQUIRED]** 

      A map of variable name-value pairs that represent an observation.

      

    
      - *(string) --* 

        The name of a variable. Currently it's used to specify the name of the target value, label, weight, and tags.

        

      
        - *(string) --* 

          The value of a variable. Currently it's used to specify values of the target value, weights, and tag variables and for filtering variable values.

          

        
  

    :type PredictEndpoint: string
    :param PredictEndpoint: **[REQUIRED]** 

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Prediction': {
                'predictedLabel': 'string',
                'predictedValue': ...,
                'predictedScores': {
                    'string': ...
                },
                'details': {
                    'string': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Prediction** *(dict) --* 

          The output from a ``Predict`` operation: 

           

           
          * ``Details`` - Contains the following attributes: ``DetailsAttributes.PREDICTIVE_MODEL_TYPE - REGRESSION | BINARY | MULTICLASS``  ``DetailsAttributes.ALGORITHM - SGD``   
           
          * ``PredictedLabel`` - Present for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` request.  
           
          * ``PredictedScores`` - Contains the raw classification score corresponding to each label.  
           
          * ``PredictedValue`` - Present for a ``REGRESSION``  ``MLModel`` request.  
           

          
          

          - **predictedLabel** *(string) --* 

            The prediction label for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` .

            
          

          - **predictedValue** *(float) --* The prediction value for ``REGRESSION``  ``MLModel`` .
          

          - **predictedScores** *(dict) --* Provides the raw classification score corresponding to each label.
            

            - *(string) --* 
              

              - *(float) --* 
        
      
          

          - **details** *(dict) --* Provides any additional details regarding the prediction.
            

            - *(string) --* Contains the key values of ``DetailsMap`` : ``PredictiveModelType`` - Indicates the type of the ``MLModel`` . ``Algorithm`` - Indicates the algorithm that was used for the ``MLModel`` .
              

              - *(string) --* 
        
      
      
    

  .. py:method:: update_batch_prediction(**kwargs)

    

    Updates the ``BatchPredictionName`` of a ``BatchPrediction`` .

     

    You can use the ``GetBatchPrediction`` operation to view the contents of the updated data element.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/UpdateBatchPrediction>`_    


    **Request Syntax** 
    ::

      response = client.update_batch_prediction(
          BatchPredictionId='string',
          BatchPredictionName='string'
      )
    :type BatchPredictionId: string
    :param BatchPredictionId: **[REQUIRED]** 

      The ID assigned to the ``BatchPrediction`` during creation.

      

    
    :type BatchPredictionName: string
    :param BatchPredictionName: **[REQUIRED]** 

      A new user-supplied name or description of the ``BatchPrediction`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BatchPredictionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of an ``UpdateBatchPrediction`` operation.

         

        You can see the updated content by using the ``GetBatchPrediction`` operation.

        
        

        - **BatchPredictionId** *(string) --* 

          The ID assigned to the ``BatchPrediction`` during creation. This value should be identical to the value of the ``BatchPredictionId`` in the request.

          
    

  .. py:method:: update_data_source(**kwargs)

    

    Updates the ``DataSourceName`` of a ``DataSource`` .

     

    You can use the ``GetDataSource`` operation to view the contents of the updated data element.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/UpdateDataSource>`_    


    **Request Syntax** 
    ::

      response = client.update_data_source(
          DataSourceId='string',
          DataSourceName='string'
      )
    :type DataSourceId: string
    :param DataSourceId: **[REQUIRED]** 

      The ID assigned to the ``DataSource`` during creation.

      

    
    :type DataSourceName: string
    :param DataSourceName: **[REQUIRED]** 

      A new user-supplied name or description of the ``DataSource`` that will replace the current description. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DataSourceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of an ``UpdateDataSource`` operation.

         

        You can see the updated content by using the ``GetBatchPrediction`` operation.

        
        

        - **DataSourceId** *(string) --* 

          The ID assigned to the ``DataSource`` during creation. This value should be identical to the value of the ``DataSourceID`` in the request.

          
    

  .. py:method:: update_evaluation(**kwargs)

    

    Updates the ``EvaluationName`` of an ``Evaluation`` .

     

    You can use the ``GetEvaluation`` operation to view the contents of the updated data element.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/UpdateEvaluation>`_    


    **Request Syntax** 
    ::

      response = client.update_evaluation(
          EvaluationId='string',
          EvaluationName='string'
      )
    :type EvaluationId: string
    :param EvaluationId: **[REQUIRED]** 

      The ID assigned to the ``Evaluation`` during creation.

      

    
    :type EvaluationName: string
    :param EvaluationName: **[REQUIRED]** 

      A new user-supplied name or description of the ``Evaluation`` that will replace the current content. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EvaluationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of an ``UpdateEvaluation`` operation.

         

        You can see the updated content by using the ``GetEvaluation`` operation.

        
        

        - **EvaluationId** *(string) --* 

          The ID assigned to the ``Evaluation`` during creation. This value should be identical to the value of the ``Evaluation`` in the request.

          
    

  .. py:method:: update_ml_model(**kwargs)

    

    Updates the ``MLModelName`` and the ``ScoreThreshold`` of an ``MLModel`` .

     

    You can use the ``GetMLModel`` operation to view the contents of the updated data element.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/UpdateMLModel>`_    


    **Request Syntax** 
    ::

      response = client.update_ml_model(
          MLModelId='string',
          MLModelName='string',
          ScoreThreshold=...
      )
    :type MLModelId: string
    :param MLModelId: **[REQUIRED]** 

      The ID assigned to the ``MLModel`` during creation.

      

    
    :type MLModelName: string
    :param MLModelName: 

      A user-supplied name or description of the ``MLModel`` .

      

    
    :type ScoreThreshold: float
    :param ScoreThreshold: 

      The ``ScoreThreshold`` used in binary classification ``MLModel`` that marks the boundary between a positive prediction and a negative prediction.

       

      Output values greater than or equal to the ``ScoreThreshold`` receive a positive result from the ``MLModel`` , such as ``true`` . Output values less than the ``ScoreThreshold`` receive a negative response from the ``MLModel`` , such as ``false`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MLModelId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of an ``UpdateMLModel`` operation.

         

        You can see the updated content by using the ``GetMLModel`` operation.

        
        

        - **MLModelId** *(string) --* 

          The ID assigned to the ``MLModel`` during creation. This value should be identical to the value of the ``MLModelID`` in the request.

          
    

==========
Paginators
==========


The available paginators are:

* :py:class:`MachineLearning.Paginator.DescribeBatchPredictions`


* :py:class:`MachineLearning.Paginator.DescribeDataSources`


* :py:class:`MachineLearning.Paginator.DescribeEvaluations`


* :py:class:`MachineLearning.Paginator.DescribeMLModels`



.. py:class:: MachineLearning.Paginator.DescribeBatchPredictions

  ::

    
    paginator = client.get_paginator('describe_batch_predictions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`MachineLearning.Client.describe_batch_predictions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeBatchPredictions>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'MLModelId'|'DataSourceId'|'DataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``BatchPrediction`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to the ``BatchPrediction`` creation date.
       
      * ``Status`` - Sets the search criteria to the ``BatchPrediction`` status.
       
      * ``Name`` - Sets the search criteria to the contents of the ``BatchPrediction`` ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``BatchPrediction`` creation.
       
      * ``MLModelId`` - Sets the search criteria to the ``MLModel`` used in the ``BatchPrediction`` .
       
      * ``DataSourceId`` - Sets the search criteria to the ``DataSource`` used in the ``BatchPrediction`` .
       
      * ``DataURI`` - Sets the search criteria to the data file(s) used in the ``BatchPrediction`` . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, a ``Batch Prediction`` operation could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``BatchPrediction`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``MLModel`` s.

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
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
            'Results': [
                {
                    'BatchPredictionId': 'string',
                    'MLModelId': 'string',
                    'BatchPredictionDataSourceId': 'string',
                    'InputDataLocationS3': 'string',
                    'CreatedByIamUser': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1),
                    'Name': 'string',
                    'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                    'OutputUri': 'string',
                    'Message': 'string',
                    'ComputeTime': 123,
                    'FinishedAt': datetime(2015, 1, 1),
                    'StartedAt': datetime(2015, 1, 1),
                    'TotalRecordCount': 123,
                    'InvalidRecordCount': 123
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeBatchPredictions`` operation. The content is essentially a list of ``BatchPrediction`` s.

        
        

        - **Results** *(list) --* 

          A list of ``BatchPrediction`` objects that meet the search criteria. 

          
          

          - *(dict) --* 

            Represents the output of a ``GetBatchPrediction`` operation.

             

            The content consists of the detailed metadata, the status, and the data file information of a ``Batch Prediction`` .

            
            

            - **BatchPredictionId** *(string) --* 

              The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to the value of the ``BatchPredictionID`` in the request. 

              
            

            - **MLModelId** *(string) --* 

              The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.

              
            

            - **BatchPredictionDataSourceId** *(string) --* 

              The ID of the ``DataSource`` that points to the group of observations to predict.

              
            

            - **InputDataLocationS3** *(string) --* 

              The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

              
            

            - **CreatedByIamUser** *(string) --* 

              The AWS user account that invoked the ``BatchPrediction`` . The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

              
            

            - **CreatedAt** *(datetime) --* 

              The time that the ``BatchPrediction`` was created. The time is expressed in epoch time.

              
            

            - **LastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in epoch time.

              
            

            - **Name** *(string) --* 

              A user-supplied name or description of the ``BatchPrediction`` .

              
            

            - **Status** *(string) --* 

              The status of the ``BatchPrediction`` . This element can have one of the following values:

               

               
              * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate predictions for a batch of observations.
               
              * ``INPROGRESS`` - The process is underway.
               
              * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is not usable.
               
              * ``COMPLETED`` - The batch prediction process completed successfully.
               
              * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.
               

              
            

            - **OutputUri** *(string) --* 

              The location of an Amazon S3 bucket or directory to receive the operation results. The following substrings are not allowed in the ``s3 key`` portion of the ``outputURI`` field: ':', '//', '/./', '/../'.

              
            

            - **Message** *(string) --* 

              A description of the most recent details about processing the batch prediction request.

              
            

            - **ComputeTime** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **FinishedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **StartedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **TotalRecordCount** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **InvalidRecordCount** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
        
      
    

.. py:class:: MachineLearning.Paginator.DescribeDataSources

  ::

    
    paginator = client.get_paginator('describe_data_sources')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`MachineLearning.Client.describe_data_sources`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeDataSources>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'DataLocationS3'|'IAMUser',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``DataSource`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to ``DataSource`` creation dates.
       
      * ``Status`` - Sets the search criteria to ``DataSource`` statuses.
       
      * ``Name`` - Sets the search criteria to the contents of ``DataSource``  ****  ``Name`` .
       
      * ``DataUri`` - Sets the search criteria to the URI of data files used to create the ``DataSource`` . The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``DataSource`` creation.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``DataSource`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``DataSource`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``DataSource`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, a ``DataSource`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``DataSource`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``DataSource`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
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
            'Results': [
                {
                    'DataSourceId': 'string',
                    'DataLocationS3': 'string',
                    'DataRearrangement': 'string',
                    'CreatedByIamUser': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1),
                    'DataSizeInBytes': 123,
                    'NumberOfFiles': 123,
                    'Name': 'string',
                    'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                    'Message': 'string',
                    'RedshiftMetadata': {
                        'RedshiftDatabase': {
                            'DatabaseName': 'string',
                            'ClusterIdentifier': 'string'
                        },
                        'DatabaseUserName': 'string',
                        'SelectSqlQuery': 'string'
                    },
                    'RDSMetadata': {
                        'Database': {
                            'InstanceIdentifier': 'string',
                            'DatabaseName': 'string'
                        },
                        'DatabaseUserName': 'string',
                        'SelectSqlQuery': 'string',
                        'ResourceRole': 'string',
                        'ServiceRole': 'string',
                        'DataPipelineId': 'string'
                    },
                    'RoleARN': 'string',
                    'ComputeStatistics': True|False,
                    'ComputeTime': 123,
                    'FinishedAt': datetime(2015, 1, 1),
                    'StartedAt': datetime(2015, 1, 1)
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the query results from a  DescribeDataSources operation. The content is essentially a list of ``DataSource`` .

        
        

        - **Results** *(list) --* 

          A list of ``DataSource`` that meet the search criteria. 

          
          

          - *(dict) --* 

            Represents the output of the ``GetDataSource`` operation. 

             

            The content consists of the detailed metadata and data file information and the current status of the ``DataSource`` . 

            
            

            - **DataSourceId** *(string) --* 

              The ID that is assigned to the ``DataSource`` during creation.

              
            

            - **DataLocationS3** *(string) --* 

              The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is used by a ``DataSource`` .

              
            

            - **DataRearrangement** *(string) --* 

              A JSON string that represents the splitting and rearrangement requirement used when this ``DataSource`` was created.

              
            

            - **CreatedByIamUser** *(string) --* 

              The AWS user account from which the ``DataSource`` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

              
            

            - **CreatedAt** *(datetime) --* 

              The time that the ``DataSource`` was created. The time is expressed in epoch time.

              
            

            - **LastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in epoch time.

              
            

            - **DataSizeInBytes** *(integer) --* 

              The total number of observations contained in the data files that the ``DataSource`` references.

              
            

            - **NumberOfFiles** *(integer) --* 

              The number of data files referenced by the ``DataSource`` .

              
            

            - **Name** *(string) --* 

              A user-supplied name or description of the ``DataSource`` .

              
            

            - **Status** *(string) --* 

              The current status of the ``DataSource`` . This element can have one of the following values: 

               

               
              * PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a ``DataSource`` .
               
              * INPROGRESS - The creation process is underway.
               
              * FAILED - The request to create a ``DataSource`` did not run to completion. It is not usable.
               
              * COMPLETED - The creation process completed successfully.
               
              * DELETED - The ``DataSource`` is marked as deleted. It is not usable.
               

              
            

            - **Message** *(string) --* 

              A description of the most recent details about creating the ``DataSource`` .

              
            

            - **RedshiftMetadata** *(dict) --* 

              Describes the ``DataSource`` details specific to Amazon Redshift.

              
              

              - **RedshiftDatabase** *(dict) --* 

                Describes the database details required to connect to an Amazon Redshift database.

                
                

                - **DatabaseName** *(string) --* 

                  The name of a database hosted on an Amazon Redshift cluster.

                  
                

                - **ClusterIdentifier** *(string) --* 

                  The ID of an Amazon Redshift cluster.

                  
            
              

              - **DatabaseUserName** *(string) --* 

                A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .

                
              

              - **SelectSqlQuery** *(string) --* 

                The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if ``Verbose`` is true in GetDataSourceInput. 

                
          
            

            - **RDSMetadata** *(dict) --* 

              The datasource details that are specific to Amazon RDS.

              
              

              - **Database** *(dict) --* 

                The database details required to connect to an Amazon RDS.

                
                

                - **InstanceIdentifier** *(string) --* 

                  The ID of an RDS DB instance.

                  
                

                - **DatabaseName** *(string) --* 

                  The name of a database hosted on an RDS DB instance.

                  
            
              

              - **DatabaseUserName** *(string) --* 

                The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.

                
              

              - **SelectSqlQuery** *(string) --* 

                The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if ``Verbose`` is true in ``GetDataSourceInput`` . 

                
              

              - **ResourceRole** *(string) --* 

                The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.

                
              

              - **ServiceRole** *(string) --* 

                The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.

                
              

              - **DataPipelineId** *(string) --* 

                The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to Amazon S3. You can use the ID to find details about the instance in the Data Pipeline console.

                
          
            

            - **RoleARN** *(string) --* 

              The Amazon Resource Name (ARN) of an `AWS IAM Role <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__ , such as the following: arn:aws:iam::account:role/rolename. 

              
            

            - **ComputeStatistics** *(boolean) --* 

              The parameter is ``true`` if statistics need to be generated from the observation data. 

              
            

            - **ComputeTime** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **FinishedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **StartedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
        
      
    

.. py:class:: MachineLearning.Paginator.DescribeEvaluations

  ::

    
    paginator = client.get_paginator('describe_evaluations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`MachineLearning.Client.describe_evaluations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeEvaluations>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'MLModelId'|'DataSourceId'|'DataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variable to filter a list of ``Evaluation`` objects:

       

       
      * ``CreatedAt`` - Sets the search criteria to the ``Evaluation`` creation date.
       
      * ``Status`` - Sets the search criteria to the ``Evaluation`` status.
       
      * ``Name`` - Sets the search criteria to the contents of ``Evaluation``  ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked an ``Evaluation`` .
       
      * ``MLModelId`` - Sets the search criteria to the ``MLModel`` that was evaluated.
       
      * ``DataSourceId`` - Sets the search criteria to the ``DataSource`` used in ``Evaluation`` .
       
      * ``DataUri`` - Sets the search criteria to the data file(s) used in ``Evaluation`` . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``Evaluation`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``Evaluation`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, an ``Evaluation`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``Evaluation`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``Evaluation`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
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
            'Results': [
                {
                    'EvaluationId': 'string',
                    'MLModelId': 'string',
                    'EvaluationDataSourceId': 'string',
                    'InputDataLocationS3': 'string',
                    'CreatedByIamUser': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1),
                    'Name': 'string',
                    'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                    'PerformanceMetrics': {
                        'Properties': {
                            'string': 'string'
                        }
                    },
                    'Message': 'string',
                    'ComputeTime': 123,
                    'FinishedAt': datetime(2015, 1, 1),
                    'StartedAt': datetime(2015, 1, 1)
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the query results from a ``DescribeEvaluations`` operation. The content is essentially a list of ``Evaluation`` .

        
        

        - **Results** *(list) --* 

          A list of ``Evaluation`` that meet the search criteria. 

          
          

          - *(dict) --* 

            Represents the output of ``GetEvaluation`` operation. 

             

            The content consists of the detailed metadata and data file information and the current status of the ``Evaluation`` .

            
            

            - **EvaluationId** *(string) --* 

              The ID that is assigned to the ``Evaluation`` at creation.

              
            

            - **MLModelId** *(string) --* 

              The ID of the ``MLModel`` that is the focus of the evaluation.

              
            

            - **EvaluationDataSourceId** *(string) --* 

              The ID of the ``DataSource`` that is used to evaluate the ``MLModel`` .

              
            

            - **InputDataLocationS3** *(string) --* 

              The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is used in the evaluation.

              
            

            - **CreatedByIamUser** *(string) --* 

              The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

              
            

            - **CreatedAt** *(datetime) --* 

              The time that the ``Evaluation`` was created. The time is expressed in epoch time.

              
            

            - **LastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch time.

              
            

            - **Name** *(string) --* 

              A user-supplied name or description of the ``Evaluation`` . 

              
            

            - **Status** *(string) --* 

              The status of the evaluation. This element can have one of the following values:

               

               
              * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an ``MLModel`` .
               
              * ``INPROGRESS`` - The evaluation is underway.
               
              * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is not usable.
               
              * ``COMPLETED`` - The evaluation process completed successfully.
               
              * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.
               

              
            

            - **PerformanceMetrics** *(dict) --* 

              Measurements of how well the ``MLModel`` performed, using observations referenced by the ``DataSource`` . One of the following metrics is returned, based on the type of the ``MLModel`` : 

               

               
              * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to measure performance.  
               
              * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable. 
               
              * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure performance.  
               

               

              For more information about performance metrics, please see the `Amazon Machine Learning Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ . 

              
              

              - **Properties** *(dict) --* 
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
            

            - **Message** *(string) --* 

              A description of the most recent details about evaluating the ``MLModel`` .

              
            

            - **ComputeTime** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **FinishedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **StartedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
        
      
    

.. py:class:: MachineLearning.Paginator.DescribeMLModels

  ::

    
    paginator = client.get_paginator('describe_ml_models')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`MachineLearning.Client.describe_ml_models`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeMLModels>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'TrainingDataSourceId'|'RealtimeEndpointStatus'|'MLModelType'|'Algorithm'|'TrainingDataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``MLModel`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to ``MLModel`` creation date.
       
      * ``Status`` - Sets the search criteria to ``MLModel`` status.
       
      * ``Name`` - Sets the search criteria to the contents of ``MLModel`` ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``MLModel`` creation.
       
      * ``TrainingDataSourceId`` - Sets the search criteria to the ``DataSource`` used to train one or more ``MLModel`` .
       
      * ``RealtimeEndpointStatus`` - Sets the search criteria to the ``MLModel`` real-time endpoint status.
       
      * ``MLModelType`` - Sets the search criteria to ``MLModel`` type: binary, regression, or multi-class.
       
      * ``Algorithm`` - Sets the search criteria to the algorithm that the ``MLModel`` uses.
       
      * ``TrainingDataURI`` - Sets the search criteria to the data file(s) used in training a ``MLModel`` . The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``MLModel`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``MLModel`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``MLModel`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, an ``MLModel`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``MLModel`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``MLModel`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
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
            'Results': [
                {
                    'MLModelId': 'string',
                    'TrainingDataSourceId': 'string',
                    'CreatedByIamUser': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1),
                    'Name': 'string',
                    'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                    'SizeInBytes': 123,
                    'EndpointInfo': {
                        'PeakRequestsPerSecond': 123,
                        'CreatedAt': datetime(2015, 1, 1),
                        'EndpointUrl': 'string',
                        'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
                    },
                    'TrainingParameters': {
                        'string': 'string'
                    },
                    'InputDataLocationS3': 'string',
                    'Algorithm': 'sgd',
                    'MLModelType': 'REGRESSION'|'BINARY'|'MULTICLASS',
                    'ScoreThreshold': ...,
                    'ScoreThresholdLastUpdatedAt': datetime(2015, 1, 1),
                    'Message': 'string',
                    'ComputeTime': 123,
                    'FinishedAt': datetime(2015, 1, 1),
                    'StartedAt': datetime(2015, 1, 1)
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeMLModels`` operation. The content is essentially a list of ``MLModel`` .

        
        

        - **Results** *(list) --* 

          A list of ``MLModel`` that meet the search criteria.

          
          

          - *(dict) --* 

            Represents the output of a ``GetMLModel`` operation. 

             

            The content consists of the detailed metadata and the current status of the ``MLModel`` .

            
            

            - **MLModelId** *(string) --* 

              The ID assigned to the ``MLModel`` at creation.

              
            

            - **TrainingDataSourceId** *(string) --* 

              The ID of the training ``DataSource`` . The ``CreateMLModel`` operation uses the ``TrainingDataSourceId`` .

              
            

            - **CreatedByIamUser** *(string) --* 

              The AWS user account from which the ``MLModel`` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

              
            

            - **CreatedAt** *(datetime) --* 

              The time that the ``MLModel`` was created. The time is expressed in epoch time.

              
            

            - **LastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.

              
            

            - **Name** *(string) --* 

              A user-supplied name or description of the ``MLModel`` .

              
            

            - **Status** *(string) --* 

              The current status of an ``MLModel`` . This element can have one of the following values: 

               

               
              * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to create an ``MLModel`` .
               
              * ``INPROGRESS`` - The creation process is underway.
               
              * ``FAILED`` - The request to create an ``MLModel`` didn't run to completion. The model isn't usable.
               
              * ``COMPLETED`` - The creation process completed successfully.
               
              * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn't usable.
               

              
            

            - **SizeInBytes** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **EndpointInfo** *(dict) --* 

              The current endpoint of the ``MLModel`` .

              
              

              - **PeakRequestsPerSecond** *(integer) --* 

                The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in incoming requests per second.

                
              

              - **CreatedAt** *(datetime) --* 

                The time that the request to create the real-time endpoint for the ``MLModel`` was received. The time is expressed in epoch time.

                
              

              - **EndpointUrl** *(string) --* 

                The URI that specifies where to send real-time prediction requests for the ``MLModel`` .

                 

                .. note::

                  Note 

                  The application must wait until the real-time endpoint is ready before using this URI.

                   

                
              

              - **EndpointStatus** *(string) --* 

                The current status of the real-time endpoint for the ``MLModel`` . This element can have one of the following values: 

                 

                 
                * ``NONE`` - Endpoint does not exist or was previously deleted.
                 
                * ``READY`` - Endpoint is ready to be used for real-time predictions.
                 
                * ``UPDATING`` - Updating/creating the endpoint. 
                 

                
          
            

            - **TrainingParameters** *(dict) --* 

              A list of the training parameters in the ``MLModel`` . The list is implemented as a map of key-value pairs.

               

              The following is the current set of training parameters: 

               

               
              * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` . 
               
              * ``sgd.maxPasses`` - The number of times that the training process traverses the observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to ``10000`` . The default value is ``10`` .
               
              * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are ``auto`` and ``none`` . The default value is ``none`` .
               
              * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm, which controls overfitting the data by penalizing large coefficients. This parameter tends to drive coefficients to zero, resulting in sparse feature set. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter can't be used when ``L2`` is specified. Use this parameter sparingly. 
               
              * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm, which controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L2 normalization. This parameter can't be used when ``L1`` is specified. Use this parameter sparingly. 
               

              
              

              - *(string) --* 

                String type.

                
                

                - *(string) --* 

                  String type.

                  
          
        
            

            - **InputDataLocationS3** *(string) --* 

              The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

              
            

            - **Algorithm** *(string) --* 

              The algorithm used to train the ``MLModel`` . The following algorithm is supported:

               

               
              * ``SGD`` -- Stochastic gradient descent. The goal of ``SGD`` is to minimize the gradient of the loss function. 
               

              
            

            - **MLModelType** *(string) --* 

              Identifies the ``MLModel`` category. The following are the available types:

               

               
              * ``REGRESSION`` - Produces a numeric result. For example, "What price should a house be listed at?"
               
              * ``BINARY`` - Produces one of two possible results. For example, "Is this a child-friendly web site?".
               
              * ``MULTICLASS`` - Produces one of several possible results. For example, "Is this a HIGH-, LOW-, or MEDIUM-risk trade?".
               

              
            

            - **ScoreThreshold** *(float) --* 
            

            - **ScoreThresholdLastUpdatedAt** *(datetime) --* 

              The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in epoch time.

              
            

            - **Message** *(string) --* 

              A description of the most recent details about accessing the ``MLModel`` .

              
            

            - **ComputeTime** *(integer) --* 

              Long integer type that is a 64-bit signed number.

              
            

            - **FinishedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
            

            - **StartedAt** *(datetime) --* 

              A timestamp represented in epoch time.

              
        
      
    

=======
Waiters
=======


The available waiters are:

* :py:class:`MachineLearning.Waiter.BatchPredictionAvailable`


* :py:class:`MachineLearning.Waiter.DataSourceAvailable`


* :py:class:`MachineLearning.Waiter.EvaluationAvailable`


* :py:class:`MachineLearning.Waiter.MLModelAvailable`



.. py:class:: MachineLearning.Waiter.BatchPredictionAvailable

  ::

    
    waiter = client.get_waiter('batch_prediction_available')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`MachineLearning.Client.describe_batch_predictions` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeBatchPredictions>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'MLModelId'|'DataSourceId'|'DataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          NextToken='string',
          Limit=123,
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``BatchPrediction`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to the ``BatchPrediction`` creation date.
       
      * ``Status`` - Sets the search criteria to the ``BatchPrediction`` status.
       
      * ``Name`` - Sets the search criteria to the contents of the ``BatchPrediction`` ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``BatchPrediction`` creation.
       
      * ``MLModelId`` - Sets the search criteria to the ``MLModel`` used in the ``BatchPrediction`` .
       
      * ``DataSourceId`` - Sets the search criteria to the ``DataSource`` used in the ``BatchPrediction`` .
       
      * ``DataURI`` - Sets the search criteria to the data file(s) used in the ``BatchPrediction`` . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, a ``Batch Prediction`` operation could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``BatchPrediction`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``MLModel`` s.

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
    :type NextToken: string
    :param NextToken: 

      An ID of the page in the paginated results.

      

    
    :type Limit: integer
    :param Limit: 

      The number of pages of information to include in the result. The range of acceptable values is ``1`` through ``100`` . The default value is ``100`` .

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: MachineLearning.Waiter.DataSourceAvailable

  ::

    
    waiter = client.get_waiter('data_source_available')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`MachineLearning.Client.describe_data_sources` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeDataSources>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'DataLocationS3'|'IAMUser',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          NextToken='string',
          Limit=123,
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``DataSource`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to ``DataSource`` creation dates.
       
      * ``Status`` - Sets the search criteria to ``DataSource`` statuses.
       
      * ``Name`` - Sets the search criteria to the contents of ``DataSource``  ****  ``Name`` .
       
      * ``DataUri`` - Sets the search criteria to the URI of data files used to create the ``DataSource`` . The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``DataSource`` creation.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``DataSource`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``DataSource`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``DataSource`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, a ``DataSource`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``DataSource`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``DataSource`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
    :type NextToken: string
    :param NextToken: 

      The ID of the page in the paginated results.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of ``DataSource`` to include in the result.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: MachineLearning.Waiter.EvaluationAvailable

  ::

    
    waiter = client.get_waiter('evaluation_available')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`MachineLearning.Client.describe_evaluations` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeEvaluations>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'MLModelId'|'DataSourceId'|'DataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          NextToken='string',
          Limit=123,
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variable to filter a list of ``Evaluation`` objects:

       

       
      * ``CreatedAt`` - Sets the search criteria to the ``Evaluation`` creation date.
       
      * ``Status`` - Sets the search criteria to the ``Evaluation`` status.
       
      * ``Name`` - Sets the search criteria to the contents of ``Evaluation``  ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked an ``Evaluation`` .
       
      * ``MLModelId`` - Sets the search criteria to the ``MLModel`` that was evaluated.
       
      * ``DataSourceId`` - Sets the search criteria to the ``DataSource`` used in ``Evaluation`` .
       
      * ``DataUri`` - Sets the search criteria to the data file(s) used in ``Evaluation`` . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``Evaluation`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``Evaluation`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, an ``Evaluation`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``Evaluation`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``Evaluation`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
    :type NextToken: string
    :param NextToken: 

      The ID of the page in the paginated results.

      

    
    :type Limit: integer
    :param Limit: 

      The maximum number of ``Evaluation`` to include in the result.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: MachineLearning.Waiter.MLModelAvailable

  ::

    
    waiter = client.get_waiter('ml_model_available')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`MachineLearning.Client.describe_ml_models` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeMLModels>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'TrainingDataSourceId'|'RealtimeEndpointStatus'|'MLModelType'|'Algorithm'|'TrainingDataURI',
          EQ='string',
          GT='string',
          LT='string',
          GE='string',
          LE='string',
          NE='string',
          Prefix='string',
          SortOrder='asc'|'dsc',
          NextToken='string',
          Limit=123,
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type FilterVariable: string
    :param FilterVariable: 

      Use one of the following variables to filter a list of ``MLModel`` :

       

       
      * ``CreatedAt`` - Sets the search criteria to ``MLModel`` creation date.
       
      * ``Status`` - Sets the search criteria to ``MLModel`` status.
       
      * ``Name`` - Sets the search criteria to the contents of ``MLModel`` ****  ``Name`` .
       
      * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``MLModel`` creation.
       
      * ``TrainingDataSourceId`` - Sets the search criteria to the ``DataSource`` used to train one or more ``MLModel`` .
       
      * ``RealtimeEndpointStatus`` - Sets the search criteria to the ``MLModel`` real-time endpoint status.
       
      * ``MLModelType`` - Sets the search criteria to ``MLModel`` type: binary, regression, or multi-class.
       
      * ``Algorithm`` - Sets the search criteria to the algorithm that the ``MLModel`` uses.
       
      * ``TrainingDataURI`` - Sets the search criteria to the data file(s) used in training a ``MLModel`` . The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
       

      

    
    :type EQ: string
    :param EQ: 

      The equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .

      

    
    :type GT: string
    :param GT: 

      The greater than operator. The ``MLModel`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .

      

    
    :type LT: string
    :param LT: 

      The less than operator. The ``MLModel`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .

      

    
    :type GE: string
    :param GE: 

      The greater than or equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 

      

    
    :type LE: string
    :param LE: 

      The less than or equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .

      

    
    :type NE: string
    :param NE: 

      The not equal to operator. The ``MLModel`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .

      

    
    :type Prefix: string
    :param Prefix: 

      A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .

       

      For example, an ``MLModel`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``MLModel`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 

       

       
      * 2014-09
       
      * 2014-09-09
       
      * 2014-09-09-Holiday
       

      

    
    :type SortOrder: string
    :param SortOrder: 

      A two-value parameter that determines the sequence of the resulting list of ``MLModel`` .

       

       
      * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
       
      * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
       

       

      Results are sorted by ``FilterVariable`` .

      

    
    :type NextToken: string
    :param NextToken: 

      The ID of the page in the paginated results.

      

    
    :type Limit: integer
    :param Limit: 

      The number of pages of information to include in the result. The range of acceptable values is ``1`` through ``100`` . The default value is ``100`` .

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None