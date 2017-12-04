

****
Glue
****

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Glue.Client

  A low-level client representing AWS Glue::

    
    import boto3
    
    client = boto3.client('glue')

  
  These are the available methods:
  
  *   :py:meth:`~Glue.Client.batch_create_partition`

  
  *   :py:meth:`~Glue.Client.batch_delete_connection`

  
  *   :py:meth:`~Glue.Client.batch_delete_partition`

  
  *   :py:meth:`~Glue.Client.batch_delete_table`

  
  *   :py:meth:`~Glue.Client.batch_get_partition`

  
  *   :py:meth:`~Glue.Client.batch_stop_job_run`

  
  *   :py:meth:`~Glue.Client.can_paginate`

  
  *   :py:meth:`~Glue.Client.create_classifier`

  
  *   :py:meth:`~Glue.Client.create_connection`

  
  *   :py:meth:`~Glue.Client.create_crawler`

  
  *   :py:meth:`~Glue.Client.create_database`

  
  *   :py:meth:`~Glue.Client.create_dev_endpoint`

  
  *   :py:meth:`~Glue.Client.create_job`

  
  *   :py:meth:`~Glue.Client.create_partition`

  
  *   :py:meth:`~Glue.Client.create_script`

  
  *   :py:meth:`~Glue.Client.create_table`

  
  *   :py:meth:`~Glue.Client.create_trigger`

  
  *   :py:meth:`~Glue.Client.create_user_defined_function`

  
  *   :py:meth:`~Glue.Client.delete_classifier`

  
  *   :py:meth:`~Glue.Client.delete_connection`

  
  *   :py:meth:`~Glue.Client.delete_crawler`

  
  *   :py:meth:`~Glue.Client.delete_database`

  
  *   :py:meth:`~Glue.Client.delete_dev_endpoint`

  
  *   :py:meth:`~Glue.Client.delete_job`

  
  *   :py:meth:`~Glue.Client.delete_partition`

  
  *   :py:meth:`~Glue.Client.delete_table`

  
  *   :py:meth:`~Glue.Client.delete_trigger`

  
  *   :py:meth:`~Glue.Client.delete_user_defined_function`

  
  *   :py:meth:`~Glue.Client.generate_presigned_url`

  
  *   :py:meth:`~Glue.Client.get_catalog_import_status`

  
  *   :py:meth:`~Glue.Client.get_classifier`

  
  *   :py:meth:`~Glue.Client.get_classifiers`

  
  *   :py:meth:`~Glue.Client.get_connection`

  
  *   :py:meth:`~Glue.Client.get_connections`

  
  *   :py:meth:`~Glue.Client.get_crawler`

  
  *   :py:meth:`~Glue.Client.get_crawler_metrics`

  
  *   :py:meth:`~Glue.Client.get_crawlers`

  
  *   :py:meth:`~Glue.Client.get_database`

  
  *   :py:meth:`~Glue.Client.get_databases`

  
  *   :py:meth:`~Glue.Client.get_dataflow_graph`

  
  *   :py:meth:`~Glue.Client.get_dev_endpoint`

  
  *   :py:meth:`~Glue.Client.get_dev_endpoints`

  
  *   :py:meth:`~Glue.Client.get_job`

  
  *   :py:meth:`~Glue.Client.get_job_run`

  
  *   :py:meth:`~Glue.Client.get_job_runs`

  
  *   :py:meth:`~Glue.Client.get_jobs`

  
  *   :py:meth:`~Glue.Client.get_mapping`

  
  *   :py:meth:`~Glue.Client.get_paginator`

  
  *   :py:meth:`~Glue.Client.get_partition`

  
  *   :py:meth:`~Glue.Client.get_partitions`

  
  *   :py:meth:`~Glue.Client.get_plan`

  
  *   :py:meth:`~Glue.Client.get_table`

  
  *   :py:meth:`~Glue.Client.get_table_versions`

  
  *   :py:meth:`~Glue.Client.get_tables`

  
  *   :py:meth:`~Glue.Client.get_trigger`

  
  *   :py:meth:`~Glue.Client.get_triggers`

  
  *   :py:meth:`~Glue.Client.get_user_defined_function`

  
  *   :py:meth:`~Glue.Client.get_user_defined_functions`

  
  *   :py:meth:`~Glue.Client.get_waiter`

  
  *   :py:meth:`~Glue.Client.import_catalog_to_glue`

  
  *   :py:meth:`~Glue.Client.reset_job_bookmark`

  
  *   :py:meth:`~Glue.Client.start_crawler`

  
  *   :py:meth:`~Glue.Client.start_crawler_schedule`

  
  *   :py:meth:`~Glue.Client.start_job_run`

  
  *   :py:meth:`~Glue.Client.start_trigger`

  
  *   :py:meth:`~Glue.Client.stop_crawler`

  
  *   :py:meth:`~Glue.Client.stop_crawler_schedule`

  
  *   :py:meth:`~Glue.Client.stop_trigger`

  
  *   :py:meth:`~Glue.Client.update_classifier`

  
  *   :py:meth:`~Glue.Client.update_connection`

  
  *   :py:meth:`~Glue.Client.update_crawler`

  
  *   :py:meth:`~Glue.Client.update_crawler_schedule`

  
  *   :py:meth:`~Glue.Client.update_database`

  
  *   :py:meth:`~Glue.Client.update_dev_endpoint`

  
  *   :py:meth:`~Glue.Client.update_job`

  
  *   :py:meth:`~Glue.Client.update_partition`

  
  *   :py:meth:`~Glue.Client.update_table`

  
  *   :py:meth:`~Glue.Client.update_trigger`

  
  *   :py:meth:`~Glue.Client.update_user_defined_function`

  

  .. py:method:: batch_create_partition(**kwargs)

    

    Creates one or more partitions in a batch operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchCreatePartition>`_    


    **Request Syntax** 
    ::

      response = client.batch_create_partition(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          PartitionInputList=[
              {
                  'Values': [
                      'string',
                  ],
                  'LastAccessTime': datetime(2015, 1, 1),
                  'StorageDescriptor': {
                      'Columns': [
                          {
                              'Name': 'string',
                              'Type': 'string',
                              'Comment': 'string'
                          },
                      ],
                      'Location': 'string',
                      'InputFormat': 'string',
                      'OutputFormat': 'string',
                      'Compressed': True|False,
                      'NumberOfBuckets': 123,
                      'SerdeInfo': {
                          'Name': 'string',
                          'SerializationLibrary': 'string',
                          'Parameters': {
                              'string': 'string'
                          }
                      },
                      'BucketColumns': [
                          'string',
                      ],
                      'SortColumns': [
                          {
                              'Column': 'string',
                              'SortOrder': 123
                          },
                      ],
                      'Parameters': {
                          'string': 'string'
                      },
                      'SkewedInfo': {
                          'SkewedColumnNames': [
                              'string',
                          ],
                          'SkewedColumnValues': [
                              'string',
                          ],
                          'SkewedColumnValueLocationMaps': {
                              'string': 'string'
                          }
                      },
                      'StoredAsSubDirectories': True|False
                  },
                  'Parameters': {
                      'string': 'string'
                  },
                  'LastAnalyzedTime': datetime(2015, 1, 1)
              },
          ]
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the catalog in which the partion is to be created. Currently, this should be the AWS account ID.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the metadata database in which the partition is to be created.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the metadata table in which the partition is to be created.

      

    
    :type PartitionInputList: list
    :param PartitionInputList: **[REQUIRED]** 

      A list of ``PartitionInput`` structures that define the partitions to be created.

      

    
      - *(dict) --* 

        The structure used to create and update a partion.

        

      
        - **Values** *(list) --* 

          The values of the partition.

          

        
          - *(string) --* 

          
      
        - **LastAccessTime** *(datetime) --* 

          The last time at which the partition was accessed.

          

        
        - **StorageDescriptor** *(dict) --* 

          Provides information about the physical location where the partition is stored.

          

        
          - **Columns** *(list) --* 

            A list of the ``Columns`` in the table.

            

          
            - *(dict) --* 

              A column in a ``Table`` .

              

            
              - **Name** *(string) --* **[REQUIRED]** 

                The name of the ``Column`` .

                

              
              - **Type** *(string) --* 

                The datatype of data in the ``Column`` .

                

              
              - **Comment** *(string) --* 

                Free-form text comment.

                

              
            
        
          - **Location** *(string) --* 

            The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

            

          
          - **InputFormat** *(string) --* 

            The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

            

          
          - **OutputFormat** *(string) --* 

            The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

            

          
          - **Compressed** *(boolean) --* 

            True if the data in the table is compressed, or False if not.

            

          
          - **NumberOfBuckets** *(integer) --* 

            Must be specified if the table contains any dimension columns.

            

          
          - **SerdeInfo** *(dict) --* 

            Serialization/deserialization (SerDe) information.

            

          
            - **Name** *(string) --* 

              Name of the SerDe.

              

            
            - **SerializationLibrary** *(string) --* 

              Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

              

            
            - **Parameters** *(dict) --* 

              A list of initialization parameters for the SerDe, in key-value form.

              

            
              - *(string) --* 

              
                - *(string) --* 

                
          
        
          
          - **BucketColumns** *(list) --* 

            A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

            

          
            - *(string) --* 

            
        
          - **SortColumns** *(list) --* 

            A list specifying the sort order of each bucket in the table.

            

          
            - *(dict) --* 

              Specifies the sort order of a sorted column.

              

            
              - **Column** *(string) --* **[REQUIRED]** 

                The name of the column.

                

              
              - **SortOrder** *(integer) --* **[REQUIRED]** 

                Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

                

              
            
        
          - **Parameters** *(dict) --* 

            User-supplied properties in key-value form.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
          - **SkewedInfo** *(dict) --* 

            Information about values that appear very frequently in a column (skewed values).

            

          
            - **SkewedColumnNames** *(list) --* 

              A list of names of columns that contain skewed values.

              

            
              - *(string) --* 

              
          
            - **SkewedColumnValues** *(list) --* 

              A list of values that appear so frequently as to be considered skewed.

              

            
              - *(string) --* 

              
          
            - **SkewedColumnValueLocationMaps** *(dict) --* 

              A mapping of skewed values to the columns that contain them.

              

            
              - *(string) --* 

              
                - *(string) --* 

                
          
        
          
          - **StoredAsSubDirectories** *(boolean) --* 

            True if the table data is stored in subdirectories, or False if not.

            

          
        
        - **Parameters** *(dict) --* 

          Partition parameters, in the form of a list of key-value pairs.

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
        - **LastAnalyzedTime** *(datetime) --* 

          The last time at which column statistics were computed for this partition.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Errors': [
                {
                    'PartitionValues': [
                        'string',
                    ],
                    'ErrorDetail': {
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Errors** *(list) --* 

          Errors encountered when trying to create the requested partitions.

          
          

          - *(dict) --* 

            Contains information about a partition error.

            
            

            - **PartitionValues** *(list) --* 

              The values that define the partition.

              
              

              - *(string) --* 
          
            

            - **ErrorDetail** *(dict) --* 

              Details about the partition error.

              
              

              - **ErrorCode** *(string) --* 

                The code associated with this error.

                
              

              - **ErrorMessage** *(string) --* 

                A message describing the error.

                
          
        
      
    

  .. py:method:: batch_delete_connection(**kwargs)

    

    Deletes a list of connection definitions from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchDeleteConnection>`_    


    **Request Syntax** 
    ::

      response = client.batch_delete_connection(
          CatalogId='string',
          ConnectionNameList=[
              'string',
          ]
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which the connections reside. If none is supplied, the AWS account ID is used by default.

      

    
    :type ConnectionNameList: list
    :param ConnectionNameList: **[REQUIRED]** 

      A list of names of the connections to delete.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Succeeded': [
                'string',
            ],
            'Errors': {
                'string': {
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Succeeded** *(list) --* 

          A list of names of the connection definitions that were successfully deleted.

          
          

          - *(string) --* 
      
        

        - **Errors** *(dict) --* 

          A map of the names of connections that were not successfully deleted to error details.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Contains details about an error.

              
              

              - **ErrorCode** *(string) --* 

                The code associated with this error.

                
              

              - **ErrorMessage** *(string) --* 

                A message describing the error.

                
          
      
    
    

  .. py:method:: batch_delete_partition(**kwargs)

    

    Deletes one or more partitions in a batch operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchDeletePartition>`_    


    **Request Syntax** 
    ::

      response = client.batch_delete_partition(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          PartitionsToDelete=[
              {
                  'Values': [
                      'string',
                  ]
              },
          ]
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the partition to be deleted resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database in which the table in question resides.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the table where the partitions to be deleted is located.

      

    
    :type PartitionsToDelete: list
    :param PartitionsToDelete: **[REQUIRED]** 

      A list of ``PartitionInput`` structures that define the partitions to be deleted.

      

    
      - *(dict) --* 

        Contains a list of values defining partitions.

        

      
        - **Values** *(list) --* **[REQUIRED]** 

          The list of values.

          

        
          - *(string) --* 

          
      
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Errors': [
                {
                    'PartitionValues': [
                        'string',
                    ],
                    'ErrorDetail': {
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Errors** *(list) --* 

          Errors encountered when trying to delete the requested partitions.

          
          

          - *(dict) --* 

            Contains information about a partition error.

            
            

            - **PartitionValues** *(list) --* 

              The values that define the partition.

              
              

              - *(string) --* 
          
            

            - **ErrorDetail** *(dict) --* 

              Details about the partition error.

              
              

              - **ErrorCode** *(string) --* 

                The code associated with this error.

                
              

              - **ErrorMessage** *(string) --* 

                A message describing the error.

                
          
        
      
    

  .. py:method:: batch_delete_table(**kwargs)

    

    Deletes multiple tables at once.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchDeleteTable>`_    


    **Request Syntax** 
    ::

      response = client.batch_delete_table(
          CatalogId='string',
          DatabaseName='string',
          TablesToDelete=[
              'string',
          ]
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database where the tables to delete reside.

      

    
    :type TablesToDelete: list
    :param TablesToDelete: **[REQUIRED]** 

      A list of the table to delete.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Errors': [
                {
                    'TableName': 'string',
                    'ErrorDetail': {
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Errors** *(list) --* 

          A list of errors encountered in attempting to delete the specified tables.

          
          

          - *(dict) --* 

            An error record for table operations.

            
            

            - **TableName** *(string) --* 

              Name of the table.

              
            

            - **ErrorDetail** *(dict) --* 

              Detail about the error.

              
              

              - **ErrorCode** *(string) --* 

                The code associated with this error.

                
              

              - **ErrorMessage** *(string) --* 

                A message describing the error.

                
          
        
      
    

  .. py:method:: batch_get_partition(**kwargs)

    

    Retrieves partitions in a batch request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchGetPartition>`_    


    **Request Syntax** 
    ::

      response = client.batch_get_partition(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          PartitionsToGet=[
              {
                  'Values': [
                      'string',
                  ]
              },
          ]
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database where the partitions reside.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the partitions' table.

      

    
    :type PartitionsToGet: list
    :param PartitionsToGet: **[REQUIRED]** 

      A list of partition values identifying the partitions to retrieve.

      

    
      - *(dict) --* 

        Contains a list of values defining partitions.

        

      
        - **Values** *(list) --* **[REQUIRED]** 

          The list of values.

          

        
          - *(string) --* 

          
      
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Partitions': [
                {
                    'Values': [
                        'string',
                    ],
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastAccessTime': datetime(2015, 1, 1),
                    'StorageDescriptor': {
                        'Columns': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string'
                            },
                        ],
                        'Location': 'string',
                        'InputFormat': 'string',
                        'OutputFormat': 'string',
                        'Compressed': True|False,
                        'NumberOfBuckets': 123,
                        'SerdeInfo': {
                            'Name': 'string',
                            'SerializationLibrary': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                        'BucketColumns': [
                            'string',
                        ],
                        'SortColumns': [
                            {
                                'Column': 'string',
                                'SortOrder': 123
                            },
                        ],
                        'Parameters': {
                            'string': 'string'
                        },
                        'SkewedInfo': {
                            'SkewedColumnNames': [
                                'string',
                            ],
                            'SkewedColumnValues': [
                                'string',
                            ],
                            'SkewedColumnValueLocationMaps': {
                                'string': 'string'
                            }
                        },
                        'StoredAsSubDirectories': True|False
                    },
                    'Parameters': {
                        'string': 'string'
                    },
                    'LastAnalyzedTime': datetime(2015, 1, 1)
                },
            ],
            'UnprocessedKeys': [
                {
                    'Values': [
                        'string',
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Partitions** *(list) --* 

          A list of the requested partitions.

          
          

          - *(dict) --* 

            Represents a slice of table data.

            
            

            - **Values** *(list) --* 

              The values of the partition.

              
              

              - *(string) --* 
          
            

            - **DatabaseName** *(string) --* 

              The name of the catalog database where the table in question is located.

              
            

            - **TableName** *(string) --* 

              The name of the table in question.

              
            

            - **CreationTime** *(datetime) --* 

              The time at which the partition was created.

              
            

            - **LastAccessTime** *(datetime) --* 

              The last time at which the partition was accessed.

              
            

            - **StorageDescriptor** *(dict) --* 

              Provides information about the physical location where the partition is stored.

              
              

              - **Columns** *(list) --* 

                A list of the ``Columns`` in the table.

                
                

                - *(dict) --* 

                  A column in a ``Table`` .

                  
                  

                  - **Name** *(string) --* 

                    The name of the ``Column`` .

                    
                  

                  - **Type** *(string) --* 

                    The datatype of data in the ``Column`` .

                    
                  

                  - **Comment** *(string) --* 

                    Free-form text comment.

                    
              
            
              

              - **Location** *(string) --* 

                The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

                
              

              - **InputFormat** *(string) --* 

                The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

                
              

              - **OutputFormat** *(string) --* 

                The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

                
              

              - **Compressed** *(boolean) --* 

                True if the data in the table is compressed, or False if not.

                
              

              - **NumberOfBuckets** *(integer) --* 

                Must be specified if the table contains any dimension columns.

                
              

              - **SerdeInfo** *(dict) --* 

                Serialization/deserialization (SerDe) information.

                
                

                - **Name** *(string) --* 

                  Name of the SerDe.

                  
                

                - **SerializationLibrary** *(string) --* 

                  Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                  
                

                - **Parameters** *(dict) --* 

                  A list of initialization parameters for the SerDe, in key-value form.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
              

              - **BucketColumns** *(list) --* 

                A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

                
                

                - *(string) --* 
            
              

              - **SortColumns** *(list) --* 

                A list specifying the sort order of each bucket in the table.

                
                

                - *(dict) --* 

                  Specifies the sort order of a sorted column.

                  
                  

                  - **Column** *(string) --* 

                    The name of the column.

                    
                  

                  - **SortOrder** *(integer) --* 

                    Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

                    
              
            
              

              - **Parameters** *(dict) --* 

                User-supplied properties in key-value form.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **SkewedInfo** *(dict) --* 

                Information about values that appear very frequently in a column (skewed values).

                
                

                - **SkewedColumnNames** *(list) --* 

                  A list of names of columns that contain skewed values.

                  
                  

                  - *(string) --* 
              
                

                - **SkewedColumnValues** *(list) --* 

                  A list of values that appear so frequently as to be considered skewed.

                  
                  

                  - *(string) --* 
              
                

                - **SkewedColumnValueLocationMaps** *(dict) --* 

                  A mapping of skewed values to the columns that contain them.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
              

              - **StoredAsSubDirectories** *(boolean) --* 

                True if the table data is stored in subdirectories, or False if not.

                
          
            

            - **Parameters** *(dict) --* 

              Partition parameters, in the form of a list of key-value pairs.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **LastAnalyzedTime** *(datetime) --* 

              The last time at which column statistics were computed for this partition.

              
        
      
        

        - **UnprocessedKeys** *(list) --* 

          A list of the partition values in the request for which partions were not returned.

          
          

          - *(dict) --* 

            Contains a list of values defining partitions.

            
            

            - **Values** *(list) --* 

              The list of values.

              
              

              - *(string) --* 
          
        
      
    

  .. py:method:: batch_stop_job_run(**kwargs)

    

    Stops a batch of job runs for a given job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/BatchStopJobRun>`_    


    **Request Syntax** 
    ::

      response = client.batch_stop_job_run(
          JobName='string',
          JobRunIds=[
              'string',
          ]
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      The name of the job whose job runs are to be stopped.

      

    
    :type JobRunIds: list
    :param JobRunIds: **[REQUIRED]** 

      A list of job run Ids of the given job to be stopped.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SuccessfulSubmissions': [
                {
                    'JobName': 'string',
                    'JobRunId': 'string'
                },
            ],
            'Errors': [
                {
                    'JobName': 'string',
                    'JobRunId': 'string',
                    'ErrorDetail': {
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SuccessfulSubmissions** *(list) --* 

          A list of job runs which are successfully submitted for stopping.

          
          

          - *(dict) --* 

            Details about the job run which is submitted successfully for stopping.

            
            

            - **JobName** *(string) --* 

              The name of the job.

              
            

            - **JobRunId** *(string) --* 

              The job run Id.

              
        
      
        

        - **Errors** *(list) --* 

          A list containing the job run Ids and details of the error that occurred for each job run while submitting to stop.

          
          

          - *(dict) --* 

            Details about the job run and the error that occurred while trying to submit it for stopping.

            
            

            - **JobName** *(string) --* 

              The name of the job.

              
            

            - **JobRunId** *(string) --* 

              The job run Id.

              
            

            - **ErrorDetail** *(dict) --* 

              The details of the error that occurred.

              
              

              - **ErrorCode** *(string) --* 

                The code associated with this error.

                
              

              - **ErrorMessage** *(string) --* 

                A message describing the error.

                
          
        
      
    

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


  .. py:method:: create_classifier(**kwargs)

    

    Creates a classifier in the user's account. This may be either a ``GrokClassifier`` or an ``XMLClassifier`` . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateClassifier>`_    


    **Request Syntax** 
    ::

      response = client.create_classifier(
          GrokClassifier={
              'Classification': 'string',
              'Name': 'string',
              'GrokPattern': 'string',
              'CustomPatterns': 'string'
          },
          XMLClassifier={
              'Classification': 'string',
              'Name': 'string',
              'RowTag': 'string'
          }
      )
    :type GrokClassifier: dict
    :param GrokClassifier: 

      A ``GrokClassifier`` object specifying the classifier to create.

      

    
      - **Classification** *(string) --* **[REQUIRED]** 

        An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.

        

      
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the new classifier.

        

      
      - **GrokPattern** *(string) --* **[REQUIRED]** 

        The grok pattern used by this classifier.

        

      
      - **CustomPatterns** *(string) --* 

        Optional custom grok patterns used by this classifier.

        

      
    
    :type XMLClassifier: dict
    :param XMLClassifier: 

      An ``XMLClassifier`` object specifying the classifier to create.

      

    
      - **Classification** *(string) --* **[REQUIRED]** 

        An identifier of the data format that the classifier matches.

        

      
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the classifier.

        

      
      - **RowTag** *(string) --* 

        The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot be an empty element. It must contain child elements representing fields in the record.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_connection(**kwargs)

    

    Creates a connection definition in the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateConnection>`_    


    **Request Syntax** 
    ::

      response = client.create_connection(
          CatalogId='string',
          ConnectionInput={
              'Name': 'string',
              'Description': 'string',
              'ConnectionType': 'JDBC'|'SFTP',
              'MatchCriteria': [
                  'string',
              ],
              'ConnectionProperties': {
                  'string': 'string'
              },
              'PhysicalConnectionRequirements': {
                  'SubnetId': 'string',
                  'SecurityGroupIdList': [
                      'string',
                  ],
                  'AvailabilityZone': 'string'
              }
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.

      

    
    :type ConnectionInput: dict
    :param ConnectionInput: **[REQUIRED]** 

      A ``ConnectionInput`` object defining the connection to create.

      

    
      - **Name** *(string) --* 

        The name of the connection.

        

      
      - **Description** *(string) --* 

        Description of the connection.

        

      
      - **ConnectionType** *(string) --* 

        The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

        

      
      - **MatchCriteria** *(list) --* 

        A list of criteria that can be used in selecting this connection.

        

      
        - *(string) --* 

        
    
      - **ConnectionProperties** *(dict) --* 

        A list of key-value pairs used as parameters for this connection.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **PhysicalConnectionRequirements** *(dict) --* 

        A map of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.

        

      
        - **SubnetId** *(string) --* 

          The subnet ID used by the connection.

          

        
        - **SecurityGroupIdList** *(list) --* 

          The security group ID list used by the connection.

          

        
          - *(string) --* 

          
      
        - **AvailabilityZone** *(string) --* 

          The connection's availability zone.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_crawler(**kwargs)

    

    Creates a new crawler with specified targets, role, configuration, and optional schedule. At least one crawl target must be specified, in either the *s3Targets* or the *jdbcTargets* field.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateCrawler>`_    


    **Request Syntax** 
    ::

      response = client.create_crawler(
          Name='string',
          Role='string',
          DatabaseName='string',
          Description='string',
          Targets={
              'S3Targets': [
                  {
                      'Path': 'string',
                      'Exclusions': [
                          'string',
                      ]
                  },
              ],
              'JdbcTargets': [
                  {
                      'ConnectionName': 'string',
                      'Path': 'string',
                      'Exclusions': [
                          'string',
                      ]
                  },
              ]
          },
          Schedule='string',
          Classifiers=[
              'string',
          ],
          TablePrefix='string',
          SchemaChangePolicy={
              'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
              'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
          },
          Configuration='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the new crawler.

      

    
    :type Role: string
    :param Role: **[REQUIRED]** 

      The IAM role (or ARN of an IAM role) used by the new crawler to access customer resources.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The AWS Glue database where results are written, such as: ``arn:aws:daylight:us-east-1::database/sometable/*`` .

      

    
    :type Description: string
    :param Description: 

      A description of the new crawler.

      

    
    :type Targets: dict
    :param Targets: **[REQUIRED]** 

      A list of collection of targets to crawl.

      

    
      - **S3Targets** *(list) --* 

        Specifies Amazon S3 targets.

        

      
        - *(dict) --* 

          Specifies a data store in Amazon S3.

          

        
          - **Path** *(string) --* 

            The path to the Amazon S3 target.

            

          
          - **Exclusions** *(list) --* 

            A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

            

          
            - *(string) --* 

            
        
        
    
      - **JdbcTargets** *(list) --* 

        Specifies JDBC targets.

        

      
        - *(dict) --* 

          Specifies a JDBC data store to crawl.

          

        
          - **ConnectionName** *(string) --* 

            The name of the connection to use to connect to the JDBC target.

            

          
          - **Path** *(string) --* 

            The path of the JDBC target.

            

          
          - **Exclusions** *(list) --* 

            A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

            

          
            - *(string) --* 

            
        
        
    
    
    :type Schedule: string
    :param Schedule: 

      A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

      

    
    :type Classifiers: list
    :param Classifiers: 

      A list of custom classifiers that the user has registered. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.

      

    
      - *(string) --* 

      
  
    :type TablePrefix: string
    :param TablePrefix: 

      The table prefix used for catalog tables that are created.

      

    
    :type SchemaChangePolicy: dict
    :param SchemaChangePolicy: 

      Policy for the crawler's update and deletion behavior.

      

    
      - **UpdateBehavior** *(string) --* 

        The update behavior when the crawler finds a changed schema.

        

      
      - **DeleteBehavior** *(string) --* 

        The deletion behavior when the crawler finds a deleted object.

        

      
    
    :type Configuration: string
    :param Configuration: 

      Crawler configuration information. This versioned JSON string allows users to specify aspects of a Crawler's behavior.

       

      You can use this field to force partitions to inherit metadata such as classification, input format, output format, serde information, and schema from their parent table, rather than detect this information separately for each partition.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_database(**kwargs)

    

    Creates a new database in a Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateDatabase>`_    


    **Request Syntax** 
    ::

      response = client.create_database(
          CatalogId='string',
          DatabaseInput={
              'Name': 'string',
              'Description': 'string',
              'LocationUri': 'string',
              'Parameters': {
                  'string': 'string'
              }
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which to create the database. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseInput: dict
    :param DatabaseInput: **[REQUIRED]** 

      A ``DatabaseInput`` object defining the metadata database to create in the catalog.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        Name of the database.

        

      
      - **Description** *(string) --* 

        Description of the database

        

      
      - **LocationUri** *(string) --* 

        The location of the database (for example, an HDFS path).

        

      
      - **Parameters** *(dict) --* 

        A list of key-value pairs that define parameters and properties of the database.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_dev_endpoint(**kwargs)

    

    Creates a new DevEndpoint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateDevEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.create_dev_endpoint(
          EndpointName='string',
          RoleArn='string',
          SecurityGroupIds=[
              'string',
          ],
          SubnetId='string',
          PublicKey='string',
          NumberOfNodes=123,
          ExtraPythonLibsS3Path='string',
          ExtraJarsS3Path='string'
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name to be assigned to the new DevEndpoint.

      

    
    :type RoleArn: string
    :param RoleArn: **[REQUIRED]** 

      The IAM role for the DevEndpoint.

      

    
    :type SecurityGroupIds: list
    :param SecurityGroupIds: 

      Security group IDs for the security groups to be used by the new DevEndpoint.

      

    
      - *(string) --* 

      
  
    :type SubnetId: string
    :param SubnetId: 

      The subnet ID for the new DevEndpoint to use.

      

    
    :type PublicKey: string
    :param PublicKey: **[REQUIRED]** 

      The public key to use for authentication.

      

    
    :type NumberOfNodes: integer
    :param NumberOfNodes: 

      The number of AWS Glue Data Processing Units (DPUs) to allocate to this DevEndpoint.

      

    
    :type ExtraPythonLibsS3Path: string
    :param ExtraPythonLibsS3Path: 

      Path(s) to one or more Python libraries in an S3 bucket that should be loaded in your DevEndpoint. Multiple values must be complete paths separated by a comma.

       

      Please note that only pure Python libraries can currently be used on a DevEndpoint. Libraries that rely on C extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis library, are not yet supported.

      

    
    :type ExtraJarsS3Path: string
    :param ExtraJarsS3Path: 

      Path to one or more Java Jars in an S3 bucket that should be loaded in your DevEndpoint.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EndpointName': 'string',
            'Status': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'SubnetId': 'string',
            'RoleArn': 'string',
            'YarnEndpointAddress': 'string',
            'ZeppelinRemoteSparkInterpreterPort': 123,
            'NumberOfNodes': 123,
            'AvailabilityZone': 'string',
            'VpcId': 'string',
            'ExtraPythonLibsS3Path': 'string',
            'ExtraJarsS3Path': 'string',
            'FailureReason': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EndpointName** *(string) --* 

          The name assigned to the new DevEndpoint.

          
        

        - **Status** *(string) --* 

          The current status of the new DevEndpoint.

          
        

        - **SecurityGroupIds** *(list) --* 

          The security groups assigned to the new DevEndpoint.

          
          

          - *(string) --* 
      
        

        - **SubnetId** *(string) --* 

          The subnet ID assigned to the new DevEndpoint.

          
        

        - **RoleArn** *(string) --* 

          The AWS ARN of the role assigned to the new DevEndpoint.

          
        

        - **YarnEndpointAddress** *(string) --* 

          The address of the YARN endpoint used by this DevEndpoint.

          
        

        - **ZeppelinRemoteSparkInterpreterPort** *(integer) --* 

          The Apache Zeppelin port for the remote Apache Spark interpreter.

          
        

        - **NumberOfNodes** *(integer) --* 

          The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint.

          
        

        - **AvailabilityZone** *(string) --* 

          The AWS availability zone where this DevEndpoint is located.

          
        

        - **VpcId** *(string) --* 

          The ID of the VPC used by this DevEndpoint.

          
        

        - **ExtraPythonLibsS3Path** *(string) --* 

          Path(s) to one or more Python libraries in an S3 bucket that will be loaded in your DevEndpoint.

          
        

        - **ExtraJarsS3Path** *(string) --* 

          Path to one or more Java Jars in an S3 bucket that will be loaded in your DevEndpoint.

          
        

        - **FailureReason** *(string) --* 

          The reason for a current failure in this DevEndpoint.

          
        

        - **CreatedTimestamp** *(datetime) --* 

          The point in time at which this DevEndpoint was created.

          
    

  .. py:method:: create_job(**kwargs)

    

    Creates a new job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateJob>`_    


    **Request Syntax** 
    ::

      response = client.create_job(
          Name='string',
          Description='string',
          LogUri='string',
          Role='string',
          ExecutionProperty={
              'MaxConcurrentRuns': 123
          },
          Command={
              'Name': 'string',
              'ScriptLocation': 'string'
          },
          DefaultArguments={
              'string': 'string'
          },
          Connections={
              'Connections': [
                  'string',
              ]
          },
          MaxRetries=123,
          AllocatedCapacity=123
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name you assign to this job.

      

    
    :type Description: string
    :param Description: 

      Description of the job.

      

    
    :type LogUri: string
    :param LogUri: 

      This field is reserved for future use.

      

    
    :type Role: string
    :param Role: **[REQUIRED]** 

      The role associated with this job.

      

    
    :type ExecutionProperty: dict
    :param ExecutionProperty: 

      An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.

      

    
      - **MaxConcurrentRuns** *(integer) --* 

        The maximum number of concurrent runs allowed for a job.

        

      
    
    :type Command: dict
    :param Command: **[REQUIRED]** 

      The JobCommand that executes this job.

      

    
      - **Name** *(string) --* 

        The name of this job command.

        

      
      - **ScriptLocation** *(string) --* 

        Specifies the location of a script that executes a job.

        

      
    
    :type DefaultArguments: dict
    :param DefaultArguments: 

      The default parameters for this job.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type Connections: dict
    :param Connections: 

      The connections used for this job.

      

    
      - **Connections** *(list) --* 

        A list of connections used by the job.

        

      
        - *(string) --* 

        
    
    
    :type MaxRetries: integer
    :param MaxRetries: 

      The maximum number of times to retry this job if it fails.

      

    
    :type AllocatedCapacity: integer
    :param AllocatedCapacity: 

      The number of capacity units allocated to this job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          The unique name of the new job that has been created.

          
    

  .. py:method:: create_partition(**kwargs)

    

    Creates a new partition.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreatePartition>`_    


    **Request Syntax** 
    ::

      response = client.create_partition(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          PartitionInput={
              'Values': [
                  'string',
              ],
              'LastAccessTime': datetime(2015, 1, 1),
              'StorageDescriptor': {
                  'Columns': [
                      {
                          'Name': 'string',
                          'Type': 'string',
                          'Comment': 'string'
                      },
                  ],
                  'Location': 'string',
                  'InputFormat': 'string',
                  'OutputFormat': 'string',
                  'Compressed': True|False,
                  'NumberOfBuckets': 123,
                  'SerdeInfo': {
                      'Name': 'string',
                      'SerializationLibrary': 'string',
                      'Parameters': {
                          'string': 'string'
                      }
                  },
                  'BucketColumns': [
                      'string',
                  ],
                  'SortColumns': [
                      {
                          'Column': 'string',
                          'SortOrder': 123
                      },
                  ],
                  'Parameters': {
                      'string': 'string'
                  },
                  'SkewedInfo': {
                      'SkewedColumnNames': [
                          'string',
                      ],
                      'SkewedColumnValues': [
                          'string',
                      ],
                      'SkewedColumnValueLocationMaps': {
                          'string': 'string'
                      }
                  },
                  'StoredAsSubDirectories': True|False
              },
              'Parameters': {
                  'string': 'string'
              },
              'LastAnalyzedTime': datetime(2015, 1, 1)
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the catalog in which the partion is to be created. Currently, this should be the AWS account ID.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the metadata database in which the partition is to be created.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the metadata table in which the partition is to be created.

      

    
    :type PartitionInput: dict
    :param PartitionInput: **[REQUIRED]** 

      A ``PartitionInput`` structure defining the partition to be created.

      

    
      - **Values** *(list) --* 

        The values of the partition.

        

      
        - *(string) --* 

        
    
      - **LastAccessTime** *(datetime) --* 

        The last time at which the partition was accessed.

        

      
      - **StorageDescriptor** *(dict) --* 

        Provides information about the physical location where the partition is stored.

        

      
        - **Columns** *(list) --* 

          A list of the ``Columns`` in the table.

          

        
          - *(dict) --* 

            A column in a ``Table`` .

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the ``Column`` .

              

            
            - **Type** *(string) --* 

              The datatype of data in the ``Column`` .

              

            
            - **Comment** *(string) --* 

              Free-form text comment.

              

            
          
      
        - **Location** *(string) --* 

          The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

          

        
        - **InputFormat** *(string) --* 

          The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

          

        
        - **OutputFormat** *(string) --* 

          The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

          

        
        - **Compressed** *(boolean) --* 

          True if the data in the table is compressed, or False if not.

          

        
        - **NumberOfBuckets** *(integer) --* 

          Must be specified if the table contains any dimension columns.

          

        
        - **SerdeInfo** *(dict) --* 

          Serialization/deserialization (SerDe) information.

          

        
          - **Name** *(string) --* 

            Name of the SerDe.

            

          
          - **SerializationLibrary** *(string) --* 

            Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

            

          
          - **Parameters** *(dict) --* 

            A list of initialization parameters for the SerDe, in key-value form.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
        - **BucketColumns** *(list) --* 

          A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

          

        
          - *(string) --* 

          
      
        - **SortColumns** *(list) --* 

          A list specifying the sort order of each bucket in the table.

          

        
          - *(dict) --* 

            Specifies the sort order of a sorted column.

            

          
            - **Column** *(string) --* **[REQUIRED]** 

              The name of the column.

              

            
            - **SortOrder** *(integer) --* **[REQUIRED]** 

              Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

              

            
          
      
        - **Parameters** *(dict) --* 

          User-supplied properties in key-value form.

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
        - **SkewedInfo** *(dict) --* 

          Information about values that appear very frequently in a column (skewed values).

          

        
          - **SkewedColumnNames** *(list) --* 

            A list of names of columns that contain skewed values.

            

          
            - *(string) --* 

            
        
          - **SkewedColumnValues** *(list) --* 

            A list of values that appear so frequently as to be considered skewed.

            

          
            - *(string) --* 

            
        
          - **SkewedColumnValueLocationMaps** *(dict) --* 

            A mapping of skewed values to the columns that contain them.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
        - **StoredAsSubDirectories** *(boolean) --* 

          True if the table data is stored in subdirectories, or False if not.

          

        
      
      - **Parameters** *(dict) --* 

        Partition parameters, in the form of a list of key-value pairs.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **LastAnalyzedTime** *(datetime) --* 

        The last time at which column statistics were computed for this partition.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_script(**kwargs)

    

    Transforms a directed acyclic graph (DAG) into a Python script.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateScript>`_    


    **Request Syntax** 
    ::

      response = client.create_script(
          DagNodes=[
              {
                  'Id': 'string',
                  'NodeType': 'string',
                  'Args': [
                      {
                          'Name': 'string',
                          'Value': 'string',
                          'Param': True|False
                      },
                  ],
                  'LineNumber': 123
              },
          ],
          DagEdges=[
              {
                  'Source': 'string',
                  'Target': 'string',
                  'TargetParameter': 'string'
              },
          ]
      )
    :type DagNodes: list
    :param DagNodes: 

      A list of the nodes in the DAG.

      

    
      - *(dict) --* 

        Represents a node in a directed acyclic graph (DAG)

        

      
        - **Id** *(string) --* **[REQUIRED]** 

          A node identifier that is unique within the node's graph.

          

        
        - **NodeType** *(string) --* **[REQUIRED]** 

          The type of node this is.

          

        
        - **Args** *(list) --* **[REQUIRED]** 

          Properties of the node, in the form of name-value pairs.

          

        
          - *(dict) --* 

            An argument or property of a node.

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the argument or property.

              

            
            - **Value** *(string) --* **[REQUIRED]** 

              The value of the argument or property.

              

            
            - **Param** *(boolean) --* 

              True if the value is used as a parameter.

              

            
          
      
        - **LineNumber** *(integer) --* 

          The line number of the node.

          

        
      
  
    :type DagEdges: list
    :param DagEdges: 

      A list of the edges in the DAG.

      

    
      - *(dict) --* 

        Represents a directional edge in a directed acyclic graph (DAG).

        

      
        - **Source** *(string) --* **[REQUIRED]** 

          The ID of the node at which the edge starts.

          

        
        - **Target** *(string) --* **[REQUIRED]** 

          The ID of the node at which the edge ends.

          

        
        - **TargetParameter** *(string) --* 

          The target of the edge.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PythonScript': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PythonScript** *(string) --* 

          The Python script generated from the DAG.

          
    

  .. py:method:: create_table(**kwargs)

    

    Creates a new table definition in the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateTable>`_    


    **Request Syntax** 
    ::

      response = client.create_table(
          CatalogId='string',
          DatabaseName='string',
          TableInput={
              'Name': 'string',
              'Description': 'string',
              'Owner': 'string',
              'LastAccessTime': datetime(2015, 1, 1),
              'LastAnalyzedTime': datetime(2015, 1, 1),
              'Retention': 123,
              'StorageDescriptor': {
                  'Columns': [
                      {
                          'Name': 'string',
                          'Type': 'string',
                          'Comment': 'string'
                      },
                  ],
                  'Location': 'string',
                  'InputFormat': 'string',
                  'OutputFormat': 'string',
                  'Compressed': True|False,
                  'NumberOfBuckets': 123,
                  'SerdeInfo': {
                      'Name': 'string',
                      'SerializationLibrary': 'string',
                      'Parameters': {
                          'string': 'string'
                      }
                  },
                  'BucketColumns': [
                      'string',
                  ],
                  'SortColumns': [
                      {
                          'Column': 'string',
                          'SortOrder': 123
                      },
                  ],
                  'Parameters': {
                      'string': 'string'
                  },
                  'SkewedInfo': {
                      'SkewedColumnNames': [
                          'string',
                      ],
                      'SkewedColumnValues': [
                          'string',
                      ],
                      'SkewedColumnValueLocationMaps': {
                          'string': 'string'
                      }
                  },
                  'StoredAsSubDirectories': True|False
              },
              'PartitionKeys': [
                  {
                      'Name': 'string',
                      'Type': 'string',
                      'Comment': 'string'
                  },
              ],
              'ViewOriginalText': 'string',
              'ViewExpandedText': 'string',
              'TableType': 'string',
              'Parameters': {
                  'string': 'string'
              }
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which to create the ``Table`` . If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The catalog database in which to create the new table.

      

    
    :type TableInput: dict
    :param TableInput: **[REQUIRED]** 

      The ``TableInput`` object that defines the metadata table to create in the catalog.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        Name of the table.

        

      
      - **Description** *(string) --* 

        Description of the table.

        

      
      - **Owner** *(string) --* 

        Owner of the table.

        

      
      - **LastAccessTime** *(datetime) --* 

        Last time the table was accessed.

        

      
      - **LastAnalyzedTime** *(datetime) --* 

        Last time column statistics were computed for this table.

        

      
      - **Retention** *(integer) --* 

        Retention time for this table.

        

      
      - **StorageDescriptor** *(dict) --* 

        A storage descriptor containing information about the physical storage of this table.

        

      
        - **Columns** *(list) --* 

          A list of the ``Columns`` in the table.

          

        
          - *(dict) --* 

            A column in a ``Table`` .

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the ``Column`` .

              

            
            - **Type** *(string) --* 

              The datatype of data in the ``Column`` .

              

            
            - **Comment** *(string) --* 

              Free-form text comment.

              

            
          
      
        - **Location** *(string) --* 

          The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

          

        
        - **InputFormat** *(string) --* 

          The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

          

        
        - **OutputFormat** *(string) --* 

          The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

          

        
        - **Compressed** *(boolean) --* 

          True if the data in the table is compressed, or False if not.

          

        
        - **NumberOfBuckets** *(integer) --* 

          Must be specified if the table contains any dimension columns.

          

        
        - **SerdeInfo** *(dict) --* 

          Serialization/deserialization (SerDe) information.

          

        
          - **Name** *(string) --* 

            Name of the SerDe.

            

          
          - **SerializationLibrary** *(string) --* 

            Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

            

          
          - **Parameters** *(dict) --* 

            A list of initialization parameters for the SerDe, in key-value form.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
        - **BucketColumns** *(list) --* 

          A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

          

        
          - *(string) --* 

          
      
        - **SortColumns** *(list) --* 

          A list specifying the sort order of each bucket in the table.

          

        
          - *(dict) --* 

            Specifies the sort order of a sorted column.

            

          
            - **Column** *(string) --* **[REQUIRED]** 

              The name of the column.

              

            
            - **SortOrder** *(integer) --* **[REQUIRED]** 

              Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

              

            
          
      
        - **Parameters** *(dict) --* 

          User-supplied properties in key-value form.

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
        - **SkewedInfo** *(dict) --* 

          Information about values that appear very frequently in a column (skewed values).

          

        
          - **SkewedColumnNames** *(list) --* 

            A list of names of columns that contain skewed values.

            

          
            - *(string) --* 

            
        
          - **SkewedColumnValues** *(list) --* 

            A list of values that appear so frequently as to be considered skewed.

            

          
            - *(string) --* 

            
        
          - **SkewedColumnValueLocationMaps** *(dict) --* 

            A mapping of skewed values to the columns that contain them.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
        - **StoredAsSubDirectories** *(boolean) --* 

          True if the table data is stored in subdirectories, or False if not.

          

        
      
      - **PartitionKeys** *(list) --* 

        A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

        

      
        - *(dict) --* 

          A column in a ``Table`` .

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The name of the ``Column`` .

            

          
          - **Type** *(string) --* 

            The datatype of data in the ``Column`` .

            

          
          - **Comment** *(string) --* 

            Free-form text comment.

            

          
        
    
      - **ViewOriginalText** *(string) --* 

        If the table is a view, the original text of the view; otherwise ``null`` .

        

      
      - **ViewExpandedText** *(string) --* 

        If the table is a view, the expanded text of the view; otherwise ``null`` .

        

      
      - **TableType** *(string) --* 

        The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

        

      
      - **Parameters** *(dict) --* 

        Properties associated with this table, as a list of key-value pairs.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_trigger(**kwargs)

    

    Creates a new trigger.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateTrigger>`_    


    **Request Syntax** 
    ::

      response = client.create_trigger(
          Name='string',
          Type='SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
          Schedule='string',
          Predicate={
              'Logical': 'AND',
              'Conditions': [
                  {
                      'LogicalOperator': 'EQUALS',
                      'JobName': 'string',
                      'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                  },
              ]
          },
          Actions=[
              {
                  'JobName': 'string',
                  'Arguments': {
                      'string': 'string'
                  }
              },
          ],
          Description='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name to assign to the new trigger.

      

    
    :type Type: string
    :param Type: **[REQUIRED]** 

      The type of the new trigger.

      

    
    :type Schedule: string
    :param Schedule: 

      A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

      

    
    :type Predicate: dict
    :param Predicate: 

      A predicate to specify when the new trigger should fire.

      

    
      - **Logical** *(string) --* 

        Currently "OR" is not supported.

        

      
      - **Conditions** *(list) --* 

        A list of the conditions that determine when the trigger will fire.

        

      
        - *(dict) --* 

          Defines a condition under which a trigger fires.

          

        
          - **LogicalOperator** *(string) --* 

            A logical operator.

            

          
          - **JobName** *(string) --* 

            The name of the job in question.

            

          
          - **State** *(string) --* 

            The condition state.

            

          
        
    
    
    :type Actions: list
    :param Actions: **[REQUIRED]** 

      The actions initiated by this trigger when it fires.

      

    
      - *(dict) --* 

        Defines an action to be initiated by a trigger.

        

      
        - **JobName** *(string) --* 

          The name of a job to be executed.

          

        
        - **Arguments** *(dict) --* 

          Arguments to be passed to the job.

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
      
  
    :type Description: string
    :param Description: 

      A description of the new trigger.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          The name assigned to the new trigger.

          
    

  .. py:method:: create_user_defined_function(**kwargs)

    

    Creates a new function definition in the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateUserDefinedFunction>`_    


    **Request Syntax** 
    ::

      response = client.create_user_defined_function(
          CatalogId='string',
          DatabaseName='string',
          FunctionInput={
              'FunctionName': 'string',
              'ClassName': 'string',
              'OwnerName': 'string',
              'OwnerType': 'USER'|'ROLE'|'GROUP',
              'ResourceUris': [
                  {
                      'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                      'Uri': 'string'
                  },
              ]
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which to create the function. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database in which to create the function.

      

    
    :type FunctionInput: dict
    :param FunctionInput: **[REQUIRED]** 

      A ``FunctionInput`` object that defines the function to create in the Data Catalog.

      

    
      - **FunctionName** *(string) --* 

        The name of the function.

        

      
      - **ClassName** *(string) --* 

        The Java class that contains the function code.

        

      
      - **OwnerName** *(string) --* 

        The owner of the function.

        

      
      - **OwnerType** *(string) --* 

        The owner type.

        

      
      - **ResourceUris** *(list) --* 

        The resource URIs for the function.

        

      
        - *(dict) --* 

          URIs for function resources.

          

        
          - **ResourceType** *(string) --* 

            The type of the resource.

            

          
          - **Uri** *(string) --* 

            The URI for accessing the resource.

            

          
        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_classifier(**kwargs)

    

    Removes a classifier from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteClassifier>`_    


    **Request Syntax** 
    ::

      response = client.delete_classifier(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the classifier to remove.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_connection(**kwargs)

    

    Deletes a connection from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteConnection>`_    


    **Request Syntax** 
    ::

      response = client.delete_connection(
          CatalogId='string',
          ConnectionName='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which the connection resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type ConnectionName: string
    :param ConnectionName: **[REQUIRED]** 

      The name of the connection to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_crawler(**kwargs)

    

    Removes a specified crawler from the Data Catalog, unless the crawler state is ``RUNNING`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteCrawler>`_    


    **Request Syntax** 
    ::

      response = client.delete_crawler(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the crawler to remove.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_database(**kwargs)

    

    Removes a specified Database from a Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteDatabase>`_    


    **Request Syntax** 
    ::

      response = client.delete_database(
          CatalogId='string',
          Name='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which the database resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the Database to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_dev_endpoint(**kwargs)

    

    Deletes a specified DevEndpoint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteDevEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.delete_dev_endpoint(
          EndpointName='string'
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the DevEndpoint.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_job(**kwargs)

    

    Deletes a specified job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteJob>`_    


    **Request Syntax** 
    ::

      response = client.delete_job(
          JobName='string'
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      The name of the job to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobName': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobName** *(string) --* 

          The name of the job that was deleted.

          
    

  .. py:method:: delete_partition(**kwargs)

    

    Deletes a specified partition.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeletePartition>`_    


    **Request Syntax** 
    ::

      response = client.delete_partition(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          PartitionValues=[
              'string',
          ]
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the partition to be deleted resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database in which the table in question resides.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the table where the partition to be deleted is located.

      

    
    :type PartitionValues: list
    :param PartitionValues: **[REQUIRED]** 

      The values that define the partition.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_table(**kwargs)

    

    Removes a table definition from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteTable>`_    


    **Request Syntax** 
    ::

      response = client.delete_table(
          CatalogId='string',
          DatabaseName='string',
          Name='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database in which the table resides.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the table to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_trigger(**kwargs)

    

    Deletes a specified trigger.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteTrigger>`_    


    **Request Syntax** 
    ::

      response = client.delete_trigger(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the trigger to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          The name of the trigger that was deleted.

          
    

  .. py:method:: delete_user_defined_function(**kwargs)

    

    Deletes an existing function definition from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DeleteUserDefinedFunction>`_    


    **Request Syntax** 
    ::

      response = client.delete_user_defined_function(
          CatalogId='string',
          DatabaseName='string',
          FunctionName='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the function to be deleted is located. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database where the function is located.

      

    
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The name of the function definition to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

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


  .. py:method:: get_catalog_import_status(**kwargs)

    

    Retrieves the status of a migration operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCatalogImportStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_catalog_import_status(
          CatalogId='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the catalog to migrate. Currently, this should be the AWS account ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ImportStatus': {
                'ImportCompleted': True|False,
                'ImportTime': datetime(2015, 1, 1),
                'ImportedBy': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ImportStatus** *(dict) --* 

          The status of the specified catalog migration.

          
          

          - **ImportCompleted** *(boolean) --* 

            True if the migration has completed, or False otherwise.

            
          

          - **ImportTime** *(datetime) --* 

            The time that the migration was started.

            
          

          - **ImportedBy** *(string) --* 

            The name of the person who initiated the migration.

            
      
    

  .. py:method:: get_classifier(**kwargs)

    

    Retrieve a classifier by name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetClassifier>`_    


    **Request Syntax** 
    ::

      response = client.get_classifier(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the classifier to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Classifier': {
                'GrokClassifier': {
                    'Name': 'string',
                    'Classification': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'Version': 123,
                    'GrokPattern': 'string',
                    'CustomPatterns': 'string'
                },
                'XMLClassifier': {
                    'Name': 'string',
                    'Classification': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'Version': 123,
                    'RowTag': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Classifier** *(dict) --* 

          The requested classifier.

          
          

          - **GrokClassifier** *(dict) --* 

            A ``GrokClassifier`` object.

            
            

            - **Name** *(string) --* 

              The name of the classifier.

              
            

            - **Classification** *(string) --* 

              An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.

              
            

            - **CreationTime** *(datetime) --* 

              The time this classifier was registered.

              
            

            - **LastUpdated** *(datetime) --* 

              The time this classifier was last updated.

              
            

            - **Version** *(integer) --* 

              The version of this classifier.

              
            

            - **GrokPattern** *(string) --* 

              The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in `Writing Custom Classifers <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

              
            

            - **CustomPatterns** *(string) --* 

              Optional custom grok patterns defined by this classifier. For more information, see custom patterns in `Writing Custom Classifers <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

              
        
          

          - **XMLClassifier** *(dict) --* 

            An ``XMLClassifier`` object.

            
            

            - **Name** *(string) --* 

              The name of the classifier.

              
            

            - **Classification** *(string) --* 

              An identifier of the data format that the classifier matches.

              
            

            - **CreationTime** *(datetime) --* 

              The time this classifier was registered.

              
            

            - **LastUpdated** *(datetime) --* 

              The time this classifier was last updated.

              
            

            - **Version** *(integer) --* 

              The version of this classifier.

              
            

            - **RowTag** *(string) --* 

              The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot be an empty element. It must contain child elements representing fields in the record.

              
        
      
    

  .. py:method:: get_classifiers(**kwargs)

    

    Lists all classifier objects in the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetClassifiers>`_    


    **Request Syntax** 
    ::

      response = client.get_classifiers(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: 

      Size of the list to return (optional).

      

    
    :type NextToken: string
    :param NextToken: 

      An optional continuation token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Classifiers': [
                {
                    'GrokClassifier': {
                        'Name': 'string',
                        'Classification': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'Version': 123,
                        'GrokPattern': 'string',
                        'CustomPatterns': 'string'
                    },
                    'XMLClassifier': {
                        'Name': 'string',
                        'Classification': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'Version': 123,
                        'RowTag': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Classifiers** *(list) --* 

          The requested list of classifier objects.

          
          

          - *(dict) --* 

            Classifiers are written in Python and triggered during a crawl task. You can write your own classifiers to best categorize your data sources and specify the appropriate schemas to use for them. A classifier checks whether a given file is in a format it can handle, and if it is, the classifier creates a schema in the form of a ``StructType`` object that matches that data format.

             

            A classifier can be either a ``grok`` classifier or an XML classifier, specified in one or the other field of the ``Classifier`` object.

            
            

            - **GrokClassifier** *(dict) --* 

              A ``GrokClassifier`` object.

              
              

              - **Name** *(string) --* 

                The name of the classifier.

                
              

              - **Classification** *(string) --* 

                An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.

                
              

              - **CreationTime** *(datetime) --* 

                The time this classifier was registered.

                
              

              - **LastUpdated** *(datetime) --* 

                The time this classifier was last updated.

                
              

              - **Version** *(integer) --* 

                The version of this classifier.

                
              

              - **GrokPattern** *(string) --* 

                The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in `Writing Custom Classifers <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

                
              

              - **CustomPatterns** *(string) --* 

                Optional custom grok patterns defined by this classifier. For more information, see custom patterns in `Writing Custom Classifers <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

                
          
            

            - **XMLClassifier** *(dict) --* 

              An ``XMLClassifier`` object.

              
              

              - **Name** *(string) --* 

                The name of the classifier.

                
              

              - **Classification** *(string) --* 

                An identifier of the data format that the classifier matches.

                
              

              - **CreationTime** *(datetime) --* 

                The time this classifier was registered.

                
              

              - **LastUpdated** *(datetime) --* 

                The time this classifier was last updated.

                
              

              - **Version** *(integer) --* 

                The version of this classifier.

                
              

              - **RowTag** *(string) --* 

                The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot be an empty element. It must contain child elements representing fields in the record.

                
          
        
      
        

        - **NextToken** *(string) --* 

          A continuation token.

          
    

  .. py:method:: get_connection(**kwargs)

    

    Retrieves a connection definition from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetConnection>`_    


    **Request Syntax** 
    ::

      response = client.get_connection(
          CatalogId='string',
          Name='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which the connection resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the connection definition to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Connection': {
                'Name': 'string',
                'Description': 'string',
                'ConnectionType': 'JDBC'|'SFTP',
                'MatchCriteria': [
                    'string',
                ],
                'ConnectionProperties': {
                    'string': 'string'
                },
                'PhysicalConnectionRequirements': {
                    'SubnetId': 'string',
                    'SecurityGroupIdList': [
                        'string',
                    ],
                    'AvailabilityZone': 'string'
                },
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'LastUpdatedBy': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Connection** *(dict) --* 

          The requested connection definition.

          
          

          - **Name** *(string) --* 

            The name of the connection definition.

            
          

          - **Description** *(string) --* 

            Description of the connection.

            
          

          - **ConnectionType** *(string) --* 

            The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

            
          

          - **MatchCriteria** *(list) --* 

            A list of criteria that can be used in selecting this connection.

            
            

            - *(string) --* 
        
          

          - **ConnectionProperties** *(dict) --* 

            A list of key-value pairs used as parameters for this connection.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **PhysicalConnectionRequirements** *(dict) --* 

            A map of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.

            
            

            - **SubnetId** *(string) --* 

              The subnet ID used by the connection.

              
            

            - **SecurityGroupIdList** *(list) --* 

              The security group ID list used by the connection.

              
              

              - *(string) --* 
          
            

            - **AvailabilityZone** *(string) --* 

              The connection's availability zone.

              
        
          

          - **CreationTime** *(datetime) --* 

            The time this connection definition was created.

            
          

          - **LastUpdatedTime** *(datetime) --* 

            The last time this connection definition was updated.

            
          

          - **LastUpdatedBy** *(string) --* 

            The user, group or role that last updated this connection definition.

            
      
    

  .. py:method:: get_connections(**kwargs)

    

    Retrieves a list of connection definitions from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetConnections>`_    


    **Request Syntax** 
    ::

      response = client.get_connections(
          CatalogId='string',
          Filter={
              'MatchCriteria': [
                  'string',
              ],
              'ConnectionType': 'JDBC'|'SFTP'
          },
          NextToken='string',
          MaxResults=123
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which the connections reside. If none is supplied, the AWS account ID is used by default.

      

    
    :type Filter: dict
    :param Filter: 

      A filter that controls which connections will be returned.

      

    
      - **MatchCriteria** *(list) --* 

        A criteria string that must match the criteria recorded in the connection definition for that connection definition to be returned.

        

      
        - *(string) --* 

        
    
      - **ConnectionType** *(string) --* 

        The type of connections to return. Currently, only JDBC is supported; SFTP is not supported.

        

      
    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of connections to return in one response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConnectionList': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'ConnectionType': 'JDBC'|'SFTP',
                    'MatchCriteria': [
                        'string',
                    ],
                    'ConnectionProperties': {
                        'string': 'string'
                    },
                    'PhysicalConnectionRequirements': {
                        'SubnetId': 'string',
                        'SecurityGroupIdList': [
                            'string',
                        ],
                        'AvailabilityZone': 'string'
                    },
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdatedTime': datetime(2015, 1, 1),
                    'LastUpdatedBy': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ConnectionList** *(list) --* 

          A list of requested connection definitions.

          
          

          - *(dict) --* 

            Defines a connection to a data source.

            
            

            - **Name** *(string) --* 

              The name of the connection definition.

              
            

            - **Description** *(string) --* 

              Description of the connection.

              
            

            - **ConnectionType** *(string) --* 

              The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

              
            

            - **MatchCriteria** *(list) --* 

              A list of criteria that can be used in selecting this connection.

              
              

              - *(string) --* 
          
            

            - **ConnectionProperties** *(dict) --* 

              A list of key-value pairs used as parameters for this connection.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **PhysicalConnectionRequirements** *(dict) --* 

              A map of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.

              
              

              - **SubnetId** *(string) --* 

                The subnet ID used by the connection.

                
              

              - **SecurityGroupIdList** *(list) --* 

                The security group ID list used by the connection.

                
                

                - *(string) --* 
            
              

              - **AvailabilityZone** *(string) --* 

                The connection's availability zone.

                
          
            

            - **CreationTime** *(datetime) --* 

              The time this connection definition was created.

              
            

            - **LastUpdatedTime** *(datetime) --* 

              The last time this connection definition was updated.

              
            

            - **LastUpdatedBy** *(string) --* 

              The user, group or role that last updated this connection definition.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if the list of connections returned does not include the last of the filtered connections.

          
    

  .. py:method:: get_crawler(**kwargs)

    

    Retrieves metadata for a specified crawler.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawler>`_    


    **Request Syntax** 
    ::

      response = client.get_crawler(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the crawler to retrieve metadata for.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Crawler': {
                'Name': 'string',
                'Role': 'string',
                'Targets': {
                    'S3Targets': [
                        {
                            'Path': 'string',
                            'Exclusions': [
                                'string',
                            ]
                        },
                    ],
                    'JdbcTargets': [
                        {
                            'ConnectionName': 'string',
                            'Path': 'string',
                            'Exclusions': [
                                'string',
                            ]
                        },
                    ]
                },
                'DatabaseName': 'string',
                'Description': 'string',
                'Classifiers': [
                    'string',
                ],
                'SchemaChangePolicy': {
                    'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                    'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
                },
                'State': 'READY'|'RUNNING'|'STOPPING',
                'TablePrefix': 'string',
                'Schedule': {
                    'ScheduleExpression': 'string',
                    'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
                },
                'CrawlElapsedTime': 123,
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'LastCrawl': {
                    'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                    'ErrorMessage': 'string',
                    'LogGroup': 'string',
                    'LogStream': 'string',
                    'MessagePrefix': 'string',
                    'StartTime': datetime(2015, 1, 1)
                },
                'Version': 123,
                'Configuration': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Crawler** *(dict) --* 

          The metadata for the specified crawler.

          
          

          - **Name** *(string) --* 

            The crawler name.

            
          

          - **Role** *(string) --* 

            The IAM role (or ARN of an IAM role) used to access customer resources, such as data in Amazon S3.

            
          

          - **Targets** *(dict) --* 

            A collection of targets to crawl.

            
            

            - **S3Targets** *(list) --* 

              Specifies Amazon S3 targets.

              
              

              - *(dict) --* 

                Specifies a data store in Amazon S3.

                
                

                - **Path** *(string) --* 

                  The path to the Amazon S3 target.

                  
                

                - **Exclusions** *(list) --* 

                  A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
            

            - **JdbcTargets** *(list) --* 

              Specifies JDBC targets.

              
              

              - *(dict) --* 

                Specifies a JDBC data store to crawl.

                
                

                - **ConnectionName** *(string) --* 

                  The name of the connection to use to connect to the JDBC target.

                  
                

                - **Path** *(string) --* 

                  The path of the JDBC target.

                  
                

                - **Exclusions** *(list) --* 

                  A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                  
                  

                  - *(string) --* 
              
            
          
        
          

          - **DatabaseName** *(string) --* 

            The database where metadata is written by this crawler.

            
          

          - **Description** *(string) --* 

            A description of the crawler.

            
          

          - **Classifiers** *(list) --* 

            A list of custom classifiers associated with the crawler.

            
            

            - *(string) --* 
        
          

          - **SchemaChangePolicy** *(dict) --* 

            Sets the behavior when the crawler finds a changed or deleted object.

            
            

            - **UpdateBehavior** *(string) --* 

              The update behavior when the crawler finds a changed schema.

              
            

            - **DeleteBehavior** *(string) --* 

              The deletion behavior when the crawler finds a deleted object.

              
        
          

          - **State** *(string) --* 

            Indicates whether the crawler is running, or whether a run is pending.

            
          

          - **TablePrefix** *(string) --* 

            The prefix added to the names of tables that are created.

            
          

          - **Schedule** *(dict) --* 

            For scheduled crawlers, the schedule when the crawler runs.

            
            

            - **ScheduleExpression** *(string) --* 

              A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

              
            

            - **State** *(string) --* 

              The state of the schedule.

              
        
          

          - **CrawlElapsedTime** *(integer) --* 

            If the crawler is running, contains the total time elapsed since the last crawl began.

            
          

          - **CreationTime** *(datetime) --* 

            The time when the crawler was created.

            
          

          - **LastUpdated** *(datetime) --* 

            The time the crawler was last updated.

            
          

          - **LastCrawl** *(dict) --* 

            The status of the last crawl, and potentially error information if an error occurred.

            
            

            - **Status** *(string) --* 

              Status of the last crawl.

              
            

            - **ErrorMessage** *(string) --* 

              If an error occurred, the error information about the last crawl.

              
            

            - **LogGroup** *(string) --* 

              The log group for the last crawl.

              
            

            - **LogStream** *(string) --* 

              The log stream for the last crawl.

              
            

            - **MessagePrefix** *(string) --* 

              The prefix for a message about this crawl.

              
            

            - **StartTime** *(datetime) --* 

              The time at which the crawl started.

              
        
          

          - **Version** *(integer) --* 

            The version of the crawler.

            
          

          - **Configuration** *(string) --* 

            Crawler configuration information. This versioned JSON string allows users to specify aspects of a Crawler's behavior.

             

            You can use this field to force partitions to inherit metadata such as classification, input format, output format, serde information, and schema from their parent table, rather than detect this information separately for each partition. Use the following JSON string to specify that behavior:

            
      
    

  .. py:method:: get_crawler_metrics(**kwargs)

    

    Retrieves metrics about specified crawlers.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawlerMetrics>`_    


    **Request Syntax** 
    ::

      response = client.get_crawler_metrics(
          CrawlerNameList=[
              'string',
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type CrawlerNameList: list
    :param CrawlerNameList: 

      A list of the names of crawlers about which to retrieve metrics.

      

    
      - *(string) --* 

      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum size of a list to return.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CrawlerMetricsList': [
                {
                    'CrawlerName': 'string',
                    'TimeLeftSeconds': 123.0,
                    'StillEstimating': True|False,
                    'LastRuntimeSeconds': 123.0,
                    'MedianRuntimeSeconds': 123.0,
                    'TablesCreated': 123,
                    'TablesUpdated': 123,
                    'TablesDeleted': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CrawlerMetricsList** *(list) --* 

          A list of metrics for the specified crawler.

          
          

          - *(dict) --* 

            Metrics for a specified crawler.

            
            

            - **CrawlerName** *(string) --* 

              The name of the crawler.

              
            

            - **TimeLeftSeconds** *(float) --* 

              The estimated time left to complete a running crawl.

              
            

            - **StillEstimating** *(boolean) --* 

              True if the crawler is still estimating how long it will take to complete this run.

              
            

            - **LastRuntimeSeconds** *(float) --* 

              The duration of the crawler's most recent run, in seconds.

              
            

            - **MedianRuntimeSeconds** *(float) --* 

              The median duration of this crawler's runs, in seconds.

              
            

            - **TablesCreated** *(integer) --* 

              The number of tables created by this crawler.

              
            

            - **TablesUpdated** *(integer) --* 

              The number of tables updated by this crawler.

              
            

            - **TablesDeleted** *(integer) --* 

              The number of tables deleted by this crawler.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if the returned list does not contain the last metric available.

          
    

  .. py:method:: get_crawlers(**kwargs)

    

    Retrieves metadata for all crawlers defined in the customer account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawlers>`_    


    **Request Syntax** 
    ::

      response = client.get_crawlers(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: 

      The number of crawlers to return on each call.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Crawlers': [
                {
                    'Name': 'string',
                    'Role': 'string',
                    'Targets': {
                        'S3Targets': [
                            {
                                'Path': 'string',
                                'Exclusions': [
                                    'string',
                                ]
                            },
                        ],
                        'JdbcTargets': [
                            {
                                'ConnectionName': 'string',
                                'Path': 'string',
                                'Exclusions': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'DatabaseName': 'string',
                    'Description': 'string',
                    'Classifiers': [
                        'string',
                    ],
                    'SchemaChangePolicy': {
                        'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                        'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
                    },
                    'State': 'READY'|'RUNNING'|'STOPPING',
                    'TablePrefix': 'string',
                    'Schedule': {
                        'ScheduleExpression': 'string',
                        'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
                    },
                    'CrawlElapsedTime': 123,
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'LastCrawl': {
                        'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                        'ErrorMessage': 'string',
                        'LogGroup': 'string',
                        'LogStream': 'string',
                        'MessagePrefix': 'string',
                        'StartTime': datetime(2015, 1, 1)
                    },
                    'Version': 123,
                    'Configuration': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Crawlers** *(list) --* 

          A list of crawler metadata.

          
          

          - *(dict) --* 

            Specifies a crawler program that examines a data source and uses classifiers to try to determine its schema. If successful, the crawler records metadata concerning the data source in the AWS Glue Data Catalog.

            
            

            - **Name** *(string) --* 

              The crawler name.

              
            

            - **Role** *(string) --* 

              The IAM role (or ARN of an IAM role) used to access customer resources, such as data in Amazon S3.

              
            

            - **Targets** *(dict) --* 

              A collection of targets to crawl.

              
              

              - **S3Targets** *(list) --* 

                Specifies Amazon S3 targets.

                
                

                - *(dict) --* 

                  Specifies a data store in Amazon S3.

                  
                  

                  - **Path** *(string) --* 

                    The path to the Amazon S3 target.

                    
                  

                  - **Exclusions** *(list) --* 

                    A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                    
                    

                    - *(string) --* 
                
              
            
              

              - **JdbcTargets** *(list) --* 

                Specifies JDBC targets.

                
                

                - *(dict) --* 

                  Specifies a JDBC data store to crawl.

                  
                  

                  - **ConnectionName** *(string) --* 

                    The name of the connection to use to connect to the JDBC target.

                    
                  

                  - **Path** *(string) --* 

                    The path of the JDBC target.

                    
                  

                  - **Exclusions** *(list) --* 

                    A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                    
                    

                    - *(string) --* 
                
              
            
          
            

            - **DatabaseName** *(string) --* 

              The database where metadata is written by this crawler.

              
            

            - **Description** *(string) --* 

              A description of the crawler.

              
            

            - **Classifiers** *(list) --* 

              A list of custom classifiers associated with the crawler.

              
              

              - *(string) --* 
          
            

            - **SchemaChangePolicy** *(dict) --* 

              Sets the behavior when the crawler finds a changed or deleted object.

              
              

              - **UpdateBehavior** *(string) --* 

                The update behavior when the crawler finds a changed schema.

                
              

              - **DeleteBehavior** *(string) --* 

                The deletion behavior when the crawler finds a deleted object.

                
          
            

            - **State** *(string) --* 

              Indicates whether the crawler is running, or whether a run is pending.

              
            

            - **TablePrefix** *(string) --* 

              The prefix added to the names of tables that are created.

              
            

            - **Schedule** *(dict) --* 

              For scheduled crawlers, the schedule when the crawler runs.

              
              

              - **ScheduleExpression** *(string) --* 

                A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

                
              

              - **State** *(string) --* 

                The state of the schedule.

                
          
            

            - **CrawlElapsedTime** *(integer) --* 

              If the crawler is running, contains the total time elapsed since the last crawl began.

              
            

            - **CreationTime** *(datetime) --* 

              The time when the crawler was created.

              
            

            - **LastUpdated** *(datetime) --* 

              The time the crawler was last updated.

              
            

            - **LastCrawl** *(dict) --* 

              The status of the last crawl, and potentially error information if an error occurred.

              
              

              - **Status** *(string) --* 

                Status of the last crawl.

                
              

              - **ErrorMessage** *(string) --* 

                If an error occurred, the error information about the last crawl.

                
              

              - **LogGroup** *(string) --* 

                The log group for the last crawl.

                
              

              - **LogStream** *(string) --* 

                The log stream for the last crawl.

                
              

              - **MessagePrefix** *(string) --* 

                The prefix for a message about this crawl.

                
              

              - **StartTime** *(datetime) --* 

                The time at which the crawl started.

                
          
            

            - **Version** *(integer) --* 

              The version of the crawler.

              
            

            - **Configuration** *(string) --* 

              Crawler configuration information. This versioned JSON string allows users to specify aspects of a Crawler's behavior.

               

              You can use this field to force partitions to inherit metadata such as classification, input format, output format, serde information, and schema from their parent table, rather than detect this information separately for each partition. Use the following JSON string to specify that behavior:

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if the returned list has not reached the end of those defined in this customer account.

          
    

  .. py:method:: get_database(**kwargs)

    

    Retrieves the definition of a specified database.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDatabase>`_    


    **Request Syntax** 
    ::

      response = client.get_database(
          CatalogId='string',
          Name='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which the database resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the database to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Database': {
                'Name': 'string',
                'Description': 'string',
                'LocationUri': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreateTime': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Database** *(dict) --* 

          The definition of the specified database in the catalog.

          
          

          - **Name** *(string) --* 

            Name of the database.

            
          

          - **Description** *(string) --* 

            Description of the database.

            
          

          - **LocationUri** *(string) --* 

            The location of the database (for example, an HDFS path).

            
          

          - **Parameters** *(dict) --* 

            A list of key-value pairs that define parameters and properties of the database.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **CreateTime** *(datetime) --* 

            The time at which the metadata database was created in the catalog.

            
      
    

  .. py:method:: get_databases(**kwargs)

    

    Retrieves all Databases defined in a given Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDatabases>`_    


    **Request Syntax** 
    ::

      response = client.get_databases(
          CatalogId='string',
          NextToken='string',
          MaxResults=123
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog from which to retrieve ``Databases`` . If none is supplied, the AWS account ID is used by default.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of databases to return in one response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DatabaseList': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'LocationUri': 'string',
                    'Parameters': {
                        'string': 'string'
                    },
                    'CreateTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DatabaseList** *(list) --* 

          A list of ``Database`` objects from the specified catalog.

          
          

          - *(dict) --* 

            The ``Database`` object represents a logical grouping of tables that may reside in a Hive metastore or an RDBMS.

            
            

            - **Name** *(string) --* 

              Name of the database.

              
            

            - **Description** *(string) --* 

              Description of the database.

              
            

            - **LocationUri** *(string) --* 

              The location of the database (for example, an HDFS path).

              
            

            - **Parameters** *(dict) --* 

              A list of key-value pairs that define parameters and properties of the database.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **CreateTime** *(datetime) --* 

              The time at which the metadata database was created in the catalog.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.

          
    

  .. py:method:: get_dataflow_graph(**kwargs)

    

    Transforms a Python script into a directed acyclic graph (DAG). 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDataflowGraph>`_    


    **Request Syntax** 
    ::

      response = client.get_dataflow_graph(
          PythonScript='string'
      )
    :type PythonScript: string
    :param PythonScript: 

      The Python script to transform.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DagNodes': [
                {
                    'Id': 'string',
                    'NodeType': 'string',
                    'Args': [
                        {
                            'Name': 'string',
                            'Value': 'string',
                            'Param': True|False
                        },
                    ],
                    'LineNumber': 123
                },
            ],
            'DagEdges': [
                {
                    'Source': 'string',
                    'Target': 'string',
                    'TargetParameter': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DagNodes** *(list) --* 

          A list of the nodes in the resulting DAG.

          
          

          - *(dict) --* 

            Represents a node in a directed acyclic graph (DAG)

            
            

            - **Id** *(string) --* 

              A node identifier that is unique within the node's graph.

              
            

            - **NodeType** *(string) --* 

              The type of node this is.

              
            

            - **Args** *(list) --* 

              Properties of the node, in the form of name-value pairs.

              
              

              - *(dict) --* 

                An argument or property of a node.

                
                

                - **Name** *(string) --* 

                  The name of the argument or property.

                  
                

                - **Value** *(string) --* 

                  The value of the argument or property.

                  
                

                - **Param** *(boolean) --* 

                  True if the value is used as a parameter.

                  
            
          
            

            - **LineNumber** *(integer) --* 

              The line number of the node.

              
        
      
        

        - **DagEdges** *(list) --* 

          A list of the edges in the resulting DAG.

          
          

          - *(dict) --* 

            Represents a directional edge in a directed acyclic graph (DAG).

            
            

            - **Source** *(string) --* 

              The ID of the node at which the edge starts.

              
            

            - **Target** *(string) --* 

              The ID of the node at which the edge ends.

              
            

            - **TargetParameter** *(string) --* 

              The target of the edge.

              
        
      
    

  .. py:method:: get_dev_endpoint(**kwargs)

    

    Retrieves information about a specified DevEndpoint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDevEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.get_dev_endpoint(
          EndpointName='string'
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      Name of the DevEndpoint for which to retrieve information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DevEndpoint': {
                'EndpointName': 'string',
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string',
                'YarnEndpointAddress': 'string',
                'ZeppelinRemoteSparkInterpreterPort': 123,
                'PublicAddress': 'string',
                'Status': 'string',
                'NumberOfNodes': 123,
                'AvailabilityZone': 'string',
                'VpcId': 'string',
                'ExtraPythonLibsS3Path': 'string',
                'ExtraJarsS3Path': 'string',
                'FailureReason': 'string',
                'LastUpdateStatus': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'LastModifiedTimestamp': datetime(2015, 1, 1),
                'PublicKey': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DevEndpoint** *(dict) --* 

          A DevEndpoint definition.

          
          

          - **EndpointName** *(string) --* 

            The name of the DevEndpoint.

            
          

          - **RoleArn** *(string) --* 

            The AWS ARN of the IAM role used in this DevEndpoint.

            
          

          - **SecurityGroupIds** *(list) --* 

            A list of security group identifiers used in this DevEndpoint.

            
            

            - *(string) --* 
        
          

          - **SubnetId** *(string) --* 

            The subnet ID for this DevEndpoint.

            
          

          - **YarnEndpointAddress** *(string) --* 

            The YARN endpoint address used by this DevEndpoint.

            
          

          - **ZeppelinRemoteSparkInterpreterPort** *(integer) --* 

            The Apache Zeppelin port for the remote Apache Spark interpreter.

            
          

          - **PublicAddress** *(string) --* 

            The public address used by this DevEndpoint.

            
          

          - **Status** *(string) --* 

            The current status of this DevEndpoint.

            
          

          - **NumberOfNodes** *(integer) --* 

            The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint.

            
          

          - **AvailabilityZone** *(string) --* 

            The AWS availability zone where this DevEndpoint is located.

            
          

          - **VpcId** *(string) --* 

            The ID of the virtual private cloud (VPC) used by this DevEndpoint.

            
          

          - **ExtraPythonLibsS3Path** *(string) --* 

            Path(s) to one or more Python libraries in an S3 bucket that should be loaded in your DevEndpoint. Multiple values must be complete paths separated by a comma.

             

            Please note that only pure Python libraries can currently be used on a DevEndpoint. Libraries that rely on C extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis library, are not yet supported.

            
          

          - **ExtraJarsS3Path** *(string) --* 

            Path to one or more Java Jars in an S3 bucket that should be loaded in your DevEndpoint.

             

            Please note that only pure Java/Scala libraries can currently be used on a DevEndpoint.

            
          

          - **FailureReason** *(string) --* 

            The reason for a current failure in this DevEndpoint.

            
          

          - **LastUpdateStatus** *(string) --* 

            The status of the last update.

            
          

          - **CreatedTimestamp** *(datetime) --* 

            The point in time at which this DevEndpoint was created.

            
          

          - **LastModifiedTimestamp** *(datetime) --* 

            The point in time at which this DevEndpoint was last modified.

            
          

          - **PublicKey** *(string) --* 

            The public key to be used by this DevEndpoint for authentication.

            
      
    

  .. py:method:: get_dev_endpoints(**kwargs)

    

    Retrieves all the DevEndpoints in this AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDevEndpoints>`_    


    **Request Syntax** 
    ::

      response = client.get_dev_endpoints(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: 

      The maximum size of information to return.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DevEndpoints': [
                {
                    'EndpointName': 'string',
                    'RoleArn': 'string',
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'SubnetId': 'string',
                    'YarnEndpointAddress': 'string',
                    'ZeppelinRemoteSparkInterpreterPort': 123,
                    'PublicAddress': 'string',
                    'Status': 'string',
                    'NumberOfNodes': 123,
                    'AvailabilityZone': 'string',
                    'VpcId': 'string',
                    'ExtraPythonLibsS3Path': 'string',
                    'ExtraJarsS3Path': 'string',
                    'FailureReason': 'string',
                    'LastUpdateStatus': 'string',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'LastModifiedTimestamp': datetime(2015, 1, 1),
                    'PublicKey': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DevEndpoints** *(list) --* 

          A list of DevEndpoint definitions.

          
          

          - *(dict) --* 

            A development endpoint where a developer can remotely debug ETL scripts.

            
            

            - **EndpointName** *(string) --* 

              The name of the DevEndpoint.

              
            

            - **RoleArn** *(string) --* 

              The AWS ARN of the IAM role used in this DevEndpoint.

              
            

            - **SecurityGroupIds** *(list) --* 

              A list of security group identifiers used in this DevEndpoint.

              
              

              - *(string) --* 
          
            

            - **SubnetId** *(string) --* 

              The subnet ID for this DevEndpoint.

              
            

            - **YarnEndpointAddress** *(string) --* 

              The YARN endpoint address used by this DevEndpoint.

              
            

            - **ZeppelinRemoteSparkInterpreterPort** *(integer) --* 

              The Apache Zeppelin port for the remote Apache Spark interpreter.

              
            

            - **PublicAddress** *(string) --* 

              The public address used by this DevEndpoint.

              
            

            - **Status** *(string) --* 

              The current status of this DevEndpoint.

              
            

            - **NumberOfNodes** *(integer) --* 

              The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint.

              
            

            - **AvailabilityZone** *(string) --* 

              The AWS availability zone where this DevEndpoint is located.

              
            

            - **VpcId** *(string) --* 

              The ID of the virtual private cloud (VPC) used by this DevEndpoint.

              
            

            - **ExtraPythonLibsS3Path** *(string) --* 

              Path(s) to one or more Python libraries in an S3 bucket that should be loaded in your DevEndpoint. Multiple values must be complete paths separated by a comma.

               

              Please note that only pure Python libraries can currently be used on a DevEndpoint. Libraries that rely on C extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis library, are not yet supported.

              
            

            - **ExtraJarsS3Path** *(string) --* 

              Path to one or more Java Jars in an S3 bucket that should be loaded in your DevEndpoint.

               

              Please note that only pure Java/Scala libraries can currently be used on a DevEndpoint.

              
            

            - **FailureReason** *(string) --* 

              The reason for a current failure in this DevEndpoint.

              
            

            - **LastUpdateStatus** *(string) --* 

              The status of the last update.

              
            

            - **CreatedTimestamp** *(datetime) --* 

              The point in time at which this DevEndpoint was created.

              
            

            - **LastModifiedTimestamp** *(datetime) --* 

              The point in time at which this DevEndpoint was last modified.

              
            

            - **PublicKey** *(string) --* 

              The public key to be used by this DevEndpoint for authentication.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if not all DevEndpoint definitions have yet been returned.

          
    

  .. py:method:: get_job(**kwargs)

    

    Retrieves an existing job definition.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJob>`_    


    **Request Syntax** 
    ::

      response = client.get_job(
          JobName='string'
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      The name of the job to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Job': {
                'Name': 'string',
                'Description': 'string',
                'LogUri': 'string',
                'Role': 'string',
                'CreatedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'ExecutionProperty': {
                    'MaxConcurrentRuns': 123
                },
                'Command': {
                    'Name': 'string',
                    'ScriptLocation': 'string'
                },
                'DefaultArguments': {
                    'string': 'string'
                },
                'Connections': {
                    'Connections': [
                        'string',
                    ]
                },
                'MaxRetries': 123,
                'AllocatedCapacity': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Job** *(dict) --* 

          The requested job definition.

          
          

          - **Name** *(string) --* 

            The name you assign to this job.

            
          

          - **Description** *(string) --* 

            Description of this job.

            
          

          - **LogUri** *(string) --* 

            This field is reserved for future use.

            
          

          - **Role** *(string) --* 

            The role associated with this job.

            
          

          - **CreatedOn** *(datetime) --* 

            The time and date that this job specification was created.

            
          

          - **LastModifiedOn** *(datetime) --* 

            The last point in time when this job specification was modified.

            
          

          - **ExecutionProperty** *(dict) --* 

            An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.

            
            

            - **MaxConcurrentRuns** *(integer) --* 

              The maximum number of concurrent runs allowed for a job.

              
        
          

          - **Command** *(dict) --* 

            The JobCommand that executes this job.

            
            

            - **Name** *(string) --* 

              The name of this job command.

              
            

            - **ScriptLocation** *(string) --* 

              Specifies the location of a script that executes a job.

              
        
          

          - **DefaultArguments** *(dict) --* 

            The default parameters for this job.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **Connections** *(dict) --* 

            The connections used for this job.

            
            

            - **Connections** *(list) --* 

              A list of connections used by the job.

              
              

              - *(string) --* 
          
        
          

          - **MaxRetries** *(integer) --* 

            The maximum number of times to retry this job if it fails.

            
          

          - **AllocatedCapacity** *(integer) --* 

            The number of capacity units allocated to this job.

            
      
    

  .. py:method:: get_job_run(**kwargs)

    

    Retrieves the metadata for a given job run.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobRun>`_    


    **Request Syntax** 
    ::

      response = client.get_job_run(
          JobName='string',
          RunId='string',
          PredecessorsIncluded=True|False
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      Name of the job being run.

      

    
    :type RunId: string
    :param RunId: **[REQUIRED]** 

      The ID of the job run.

      

    
    :type PredecessorsIncluded: boolean
    :param PredecessorsIncluded: 

      A list of the predecessor runs to return as well.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobRun': {
                'Id': 'string',
                'Attempt': 123,
                'PreviousRunId': 'string',
                'TriggerName': 'string',
                'JobName': 'string',
                'StartedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'CompletedOn': datetime(2015, 1, 1),
                'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED',
                'Arguments': {
                    'string': 'string'
                },
                'ErrorMessage': 'string',
                'PredecessorRuns': [
                    {
                        'JobName': 'string',
                        'RunId': 'string'
                    },
                ],
                'AllocatedCapacity': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobRun** *(dict) --* 

          The requested job-run metadata.

          
          

          - **Id** *(string) --* 

            The ID of this job run.

            
          

          - **Attempt** *(integer) --* 

            The number or the attempt to run this job.

            
          

          - **PreviousRunId** *(string) --* 

            The ID of the previous run of this job.

            
          

          - **TriggerName** *(string) --* 

            The name of the trigger for this job run.

            
          

          - **JobName** *(string) --* 

            The name of the job being run.

            
          

          - **StartedOn** *(datetime) --* 

            The date and time at which this job run was started.

            
          

          - **LastModifiedOn** *(datetime) --* 

            The last time this job run was modified.

            
          

          - **CompletedOn** *(datetime) --* 

            The date and time this job run completed.

            
          

          - **JobRunState** *(string) --* 

            The current state of the job run.

            
          

          - **Arguments** *(dict) --* 

            The job arguments associated with this run.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **ErrorMessage** *(string) --* 

            An error message associated with this job run.

            
          

          - **PredecessorRuns** *(list) --* 

            A list of predecessors to this job run.

            
            

            - *(dict) --* 

              A job run that preceded this one.

              
              

              - **JobName** *(string) --* 

                The name of the predecessor job.

                
              

              - **RunId** *(string) --* 

                The job-run ID of the precessor job run.

                
          
        
          

          - **AllocatedCapacity** *(integer) --* 

            The amount of infrastructure capacity allocated to this job run.

            
      
    

  .. py:method:: get_job_runs(**kwargs)

    

    Retrieves metadata for all runs of a given job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobRuns>`_    


    **Request Syntax** 
    ::

      response = client.get_job_runs(
          JobName='string',
          NextToken='string',
          MaxResults=123
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      The name of the job for which to retrieve all job runs.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum size of the response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobRuns': [
                {
                    'Id': 'string',
                    'Attempt': 123,
                    'PreviousRunId': 'string',
                    'TriggerName': 'string',
                    'JobName': 'string',
                    'StartedOn': datetime(2015, 1, 1),
                    'LastModifiedOn': datetime(2015, 1, 1),
                    'CompletedOn': datetime(2015, 1, 1),
                    'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED',
                    'Arguments': {
                        'string': 'string'
                    },
                    'ErrorMessage': 'string',
                    'PredecessorRuns': [
                        {
                            'JobName': 'string',
                            'RunId': 'string'
                        },
                    ],
                    'AllocatedCapacity': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobRuns** *(list) --* 

          A list of job-run metatdata objects.

          
          

          - *(dict) --* 

            Contains information about a job run.

            
            

            - **Id** *(string) --* 

              The ID of this job run.

              
            

            - **Attempt** *(integer) --* 

              The number or the attempt to run this job.

              
            

            - **PreviousRunId** *(string) --* 

              The ID of the previous run of this job.

              
            

            - **TriggerName** *(string) --* 

              The name of the trigger for this job run.

              
            

            - **JobName** *(string) --* 

              The name of the job being run.

              
            

            - **StartedOn** *(datetime) --* 

              The date and time at which this job run was started.

              
            

            - **LastModifiedOn** *(datetime) --* 

              The last time this job run was modified.

              
            

            - **CompletedOn** *(datetime) --* 

              The date and time this job run completed.

              
            

            - **JobRunState** *(string) --* 

              The current state of the job run.

              
            

            - **Arguments** *(dict) --* 

              The job arguments associated with this run.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **ErrorMessage** *(string) --* 

              An error message associated with this job run.

              
            

            - **PredecessorRuns** *(list) --* 

              A list of predecessors to this job run.

              
              

              - *(dict) --* 

                A job run that preceded this one.

                
                

                - **JobName** *(string) --* 

                  The name of the predecessor job.

                  
                

                - **RunId** *(string) --* 

                  The job-run ID of the precessor job run.

                  
            
          
            

            - **AllocatedCapacity** *(integer) --* 

              The amount of infrastructure capacity allocated to this job run.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if not all reequested job runs have been returned.

          
    

  .. py:method:: get_jobs(**kwargs)

    

    Retrieves all current jobs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobs>`_    


    **Request Syntax** 
    ::

      response = client.get_jobs(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum size of the response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Jobs': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'LogUri': 'string',
                    'Role': 'string',
                    'CreatedOn': datetime(2015, 1, 1),
                    'LastModifiedOn': datetime(2015, 1, 1),
                    'ExecutionProperty': {
                        'MaxConcurrentRuns': 123
                    },
                    'Command': {
                        'Name': 'string',
                        'ScriptLocation': 'string'
                    },
                    'DefaultArguments': {
                        'string': 'string'
                    },
                    'Connections': {
                        'Connections': [
                            'string',
                        ]
                    },
                    'MaxRetries': 123,
                    'AllocatedCapacity': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Jobs** *(list) --* 

          A list of jobs.

          
          

          - *(dict) --* 

            Specifies a job in the Data Catalog.

            
            

            - **Name** *(string) --* 

              The name you assign to this job.

              
            

            - **Description** *(string) --* 

              Description of this job.

              
            

            - **LogUri** *(string) --* 

              This field is reserved for future use.

              
            

            - **Role** *(string) --* 

              The role associated with this job.

              
            

            - **CreatedOn** *(datetime) --* 

              The time and date that this job specification was created.

              
            

            - **LastModifiedOn** *(datetime) --* 

              The last point in time when this job specification was modified.

              
            

            - **ExecutionProperty** *(dict) --* 

              An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.

              
              

              - **MaxConcurrentRuns** *(integer) --* 

                The maximum number of concurrent runs allowed for a job.

                
          
            

            - **Command** *(dict) --* 

              The JobCommand that executes this job.

              
              

              - **Name** *(string) --* 

                The name of this job command.

                
              

              - **ScriptLocation** *(string) --* 

                Specifies the location of a script that executes a job.

                
          
            

            - **DefaultArguments** *(dict) --* 

              The default parameters for this job.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **Connections** *(dict) --* 

              The connections used for this job.

              
              

              - **Connections** *(list) --* 

                A list of connections used by the job.

                
                

                - *(string) --* 
            
          
            

            - **MaxRetries** *(integer) --* 

              The maximum number of times to retry this job if it fails.

              
            

            - **AllocatedCapacity** *(integer) --* 

              The number of capacity units allocated to this job.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if not all jobs have yet been returned.

          
    

  .. py:method:: get_mapping(**kwargs)

    

    Creates mappings.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetMapping>`_    


    **Request Syntax** 
    ::

      response = client.get_mapping(
          Source={
              'DatabaseName': 'string',
              'TableName': 'string'
          },
          Sinks=[
              {
                  'DatabaseName': 'string',
                  'TableName': 'string'
              },
          ],
          Location={
              'Jdbc': [
                  {
                      'Name': 'string',
                      'Value': 'string',
                      'Param': True|False
                  },
              ],
              'S3': [
                  {
                      'Name': 'string',
                      'Value': 'string',
                      'Param': True|False
                  },
              ]
          }
      )
    :type Source: dict
    :param Source: **[REQUIRED]** 

      Specifies the source table.

      

    
      - **DatabaseName** *(string) --* **[REQUIRED]** 

        The database in which the table metadata resides.

        

      
      - **TableName** *(string) --* **[REQUIRED]** 

        The name of the table in question.

        

      
    
    :type Sinks: list
    :param Sinks: 

      A list of target tables.

      

    
      - *(dict) --* 

        Specifies a table definition in the Data Catalog.

        

      
        - **DatabaseName** *(string) --* **[REQUIRED]** 

          The database in which the table metadata resides.

          

        
        - **TableName** *(string) --* **[REQUIRED]** 

          The name of the table in question.

          

        
      
  
    :type Location: dict
    :param Location: 

      Parameters for the mapping.

      

    
      - **Jdbc** *(list) --* 

        A JDBC location.

        

      
        - *(dict) --* 

          An argument or property of a node.

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The name of the argument or property.

            

          
          - **Value** *(string) --* **[REQUIRED]** 

            The value of the argument or property.

            

          
          - **Param** *(boolean) --* 

            True if the value is used as a parameter.

            

          
        
    
      - **S3** *(list) --* 

        An Amazon S3 location.

        

      
        - *(dict) --* 

          An argument or property of a node.

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The name of the argument or property.

            

          
          - **Value** *(string) --* **[REQUIRED]** 

            The value of the argument or property.

            

          
          - **Param** *(boolean) --* 

            True if the value is used as a parameter.

            

          
        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Mapping': [
                {
                    'SourceTable': 'string',
                    'SourcePath': 'string',
                    'SourceType': 'string',
                    'TargetTable': 'string',
                    'TargetPath': 'string',
                    'TargetType': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Mapping** *(list) --* 

          A list of mappings to the specified targets.

          
          

          - *(dict) --* 

            Defines a mapping.

            
            

            - **SourceTable** *(string) --* 

              The name of the source table.

              
            

            - **SourcePath** *(string) --* 

              The source path.

              
            

            - **SourceType** *(string) --* 

              The source type.

              
            

            - **TargetTable** *(string) --* 

              The target table.

              
            

            - **TargetPath** *(string) --* 

              The target path.

              
            

            - **TargetType** *(string) --* 

              The target type.

              
        
      
    

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


  .. py:method:: get_partition(**kwargs)

    

    Retrieves information about a specified partition.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPartition>`_    


    **Request Syntax** 
    ::

      response = client.get_partition(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          PartitionValues=[
              'string',
          ]
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the partition in question resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database where the partition resides.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the partition's table.

      

    
    :type PartitionValues: list
    :param PartitionValues: **[REQUIRED]** 

      The values that define the partition.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Partition': {
                'Values': [
                    'string',
                ],
                'DatabaseName': 'string',
                'TableName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string'
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'Parameters': {
                    'string': 'string'
                },
                'LastAnalyzedTime': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Partition** *(dict) --* 

          The requested information, in the form of a ``Partition`` object.

          
          

          - **Values** *(list) --* 

            The values of the partition.

            
            

            - *(string) --* 
        
          

          - **DatabaseName** *(string) --* 

            The name of the catalog database where the table in question is located.

            
          

          - **TableName** *(string) --* 

            The name of the table in question.

            
          

          - **CreationTime** *(datetime) --* 

            The time at which the partition was created.

            
          

          - **LastAccessTime** *(datetime) --* 

            The last time at which the partition was accessed.

            
          

          - **StorageDescriptor** *(dict) --* 

            Provides information about the physical location where the partition is stored.

            
            

            - **Columns** *(list) --* 

              A list of the ``Columns`` in the table.

              
              

              - *(dict) --* 

                A column in a ``Table`` .

                
                

                - **Name** *(string) --* 

                  The name of the ``Column`` .

                  
                

                - **Type** *(string) --* 

                  The datatype of data in the ``Column`` .

                  
                

                - **Comment** *(string) --* 

                  Free-form text comment.

                  
            
          
            

            - **Location** *(string) --* 

              The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

              
            

            - **InputFormat** *(string) --* 

              The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

              
            

            - **OutputFormat** *(string) --* 

              The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

              
            

            - **Compressed** *(boolean) --* 

              True if the data in the table is compressed, or False if not.

              
            

            - **NumberOfBuckets** *(integer) --* 

              Must be specified if the table contains any dimension columns.

              
            

            - **SerdeInfo** *(dict) --* 

              Serialization/deserialization (SerDe) information.

              
              

              - **Name** *(string) --* 

                Name of the SerDe.

                
              

              - **SerializationLibrary** *(string) --* 

                Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                
              

              - **Parameters** *(dict) --* 

                A list of initialization parameters for the SerDe, in key-value form.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
            

            - **BucketColumns** *(list) --* 

              A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

              
              

              - *(string) --* 
          
            

            - **SortColumns** *(list) --* 

              A list specifying the sort order of each bucket in the table.

              
              

              - *(dict) --* 

                Specifies the sort order of a sorted column.

                
                

                - **Column** *(string) --* 

                  The name of the column.

                  
                

                - **SortOrder** *(integer) --* 

                  Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

                  
            
          
            

            - **Parameters** *(dict) --* 

              User-supplied properties in key-value form.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **SkewedInfo** *(dict) --* 

              Information about values that appear very frequently in a column (skewed values).

              
              

              - **SkewedColumnNames** *(list) --* 

                A list of names of columns that contain skewed values.

                
                

                - *(string) --* 
            
              

              - **SkewedColumnValues** *(list) --* 

                A list of values that appear so frequently as to be considered skewed.

                
                

                - *(string) --* 
            
              

              - **SkewedColumnValueLocationMaps** *(dict) --* 

                A mapping of skewed values to the columns that contain them.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
            

            - **StoredAsSubDirectories** *(boolean) --* 

              True if the table data is stored in subdirectories, or False if not.

              
        
          

          - **Parameters** *(dict) --* 

            Partition parameters, in the form of a list of key-value pairs.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **LastAnalyzedTime** *(datetime) --* 

            The last time at which column statistics were computed for this partition.

            
      
    

  .. py:method:: get_partitions(**kwargs)

    

    Retrieves information about the partitions in a table.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPartitions>`_    


    **Request Syntax** 
    ::

      response = client.get_partitions(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          Expression='string',
          NextToken='string',
          Segment={
              'SegmentNumber': 123,
              'TotalSegments': 123
          },
          MaxResults=123
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database where the partitions reside.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the partitions' table.

      

    
    :type Expression: string
    :param Expression: 

      An expression filtering the partitions to be returned.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is not the first call to retrieve these partitions.

      

    
    :type Segment: dict
    :param Segment: 

      The segment of the table's partitions to scan in this request.

      

    
      - **SegmentNumber** *(integer) --* **[REQUIRED]** 

        The zero-based index number of the this segment. For example, if the total number of segments is 4, SegmentNumber values will range from zero through three.

        

      
      - **TotalSegments** *(integer) --* **[REQUIRED]** 

        The total numer of segments.

        

      
    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of partitions to return in a single response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Partitions': [
                {
                    'Values': [
                        'string',
                    ],
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastAccessTime': datetime(2015, 1, 1),
                    'StorageDescriptor': {
                        'Columns': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string'
                            },
                        ],
                        'Location': 'string',
                        'InputFormat': 'string',
                        'OutputFormat': 'string',
                        'Compressed': True|False,
                        'NumberOfBuckets': 123,
                        'SerdeInfo': {
                            'Name': 'string',
                            'SerializationLibrary': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                        'BucketColumns': [
                            'string',
                        ],
                        'SortColumns': [
                            {
                                'Column': 'string',
                                'SortOrder': 123
                            },
                        ],
                        'Parameters': {
                            'string': 'string'
                        },
                        'SkewedInfo': {
                            'SkewedColumnNames': [
                                'string',
                            ],
                            'SkewedColumnValues': [
                                'string',
                            ],
                            'SkewedColumnValueLocationMaps': {
                                'string': 'string'
                            }
                        },
                        'StoredAsSubDirectories': True|False
                    },
                    'Parameters': {
                        'string': 'string'
                    },
                    'LastAnalyzedTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Partitions** *(list) --* 

          A list of requested partitions.

          
          

          - *(dict) --* 

            Represents a slice of table data.

            
            

            - **Values** *(list) --* 

              The values of the partition.

              
              

              - *(string) --* 
          
            

            - **DatabaseName** *(string) --* 

              The name of the catalog database where the table in question is located.

              
            

            - **TableName** *(string) --* 

              The name of the table in question.

              
            

            - **CreationTime** *(datetime) --* 

              The time at which the partition was created.

              
            

            - **LastAccessTime** *(datetime) --* 

              The last time at which the partition was accessed.

              
            

            - **StorageDescriptor** *(dict) --* 

              Provides information about the physical location where the partition is stored.

              
              

              - **Columns** *(list) --* 

                A list of the ``Columns`` in the table.

                
                

                - *(dict) --* 

                  A column in a ``Table`` .

                  
                  

                  - **Name** *(string) --* 

                    The name of the ``Column`` .

                    
                  

                  - **Type** *(string) --* 

                    The datatype of data in the ``Column`` .

                    
                  

                  - **Comment** *(string) --* 

                    Free-form text comment.

                    
              
            
              

              - **Location** *(string) --* 

                The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

                
              

              - **InputFormat** *(string) --* 

                The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

                
              

              - **OutputFormat** *(string) --* 

                The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

                
              

              - **Compressed** *(boolean) --* 

                True if the data in the table is compressed, or False if not.

                
              

              - **NumberOfBuckets** *(integer) --* 

                Must be specified if the table contains any dimension columns.

                
              

              - **SerdeInfo** *(dict) --* 

                Serialization/deserialization (SerDe) information.

                
                

                - **Name** *(string) --* 

                  Name of the SerDe.

                  
                

                - **SerializationLibrary** *(string) --* 

                  Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                  
                

                - **Parameters** *(dict) --* 

                  A list of initialization parameters for the SerDe, in key-value form.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
              

              - **BucketColumns** *(list) --* 

                A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

                
                

                - *(string) --* 
            
              

              - **SortColumns** *(list) --* 

                A list specifying the sort order of each bucket in the table.

                
                

                - *(dict) --* 

                  Specifies the sort order of a sorted column.

                  
                  

                  - **Column** *(string) --* 

                    The name of the column.

                    
                  

                  - **SortOrder** *(integer) --* 

                    Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

                    
              
            
              

              - **Parameters** *(dict) --* 

                User-supplied properties in key-value form.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **SkewedInfo** *(dict) --* 

                Information about values that appear very frequently in a column (skewed values).

                
                

                - **SkewedColumnNames** *(list) --* 

                  A list of names of columns that contain skewed values.

                  
                  

                  - *(string) --* 
              
                

                - **SkewedColumnValues** *(list) --* 

                  A list of values that appear so frequently as to be considered skewed.

                  
                  

                  - *(string) --* 
              
                

                - **SkewedColumnValueLocationMaps** *(dict) --* 

                  A mapping of skewed values to the columns that contain them.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
              

              - **StoredAsSubDirectories** *(boolean) --* 

                True if the table data is stored in subdirectories, or False if not.

                
          
            

            - **Parameters** *(dict) --* 

              Partition parameters, in the form of a list of key-value pairs.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **LastAnalyzedTime** *(datetime) --* 

              The last time at which column statistics were computed for this partition.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if the returned list of partitions does not does not include the last one.

          
    

  .. py:method:: get_plan(**kwargs)

    

    Gets a Python script to perform a specified mapping.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPlan>`_    


    **Request Syntax** 
    ::

      response = client.get_plan(
          Mapping=[
              {
                  'SourceTable': 'string',
                  'SourcePath': 'string',
                  'SourceType': 'string',
                  'TargetTable': 'string',
                  'TargetPath': 'string',
                  'TargetType': 'string'
              },
          ],
          Source={
              'DatabaseName': 'string',
              'TableName': 'string'
          },
          Sinks=[
              {
                  'DatabaseName': 'string',
                  'TableName': 'string'
              },
          ],
          Location={
              'Jdbc': [
                  {
                      'Name': 'string',
                      'Value': 'string',
                      'Param': True|False
                  },
              ],
              'S3': [
                  {
                      'Name': 'string',
                      'Value': 'string',
                      'Param': True|False
                  },
              ]
          }
      )
    :type Mapping: list
    :param Mapping: **[REQUIRED]** 

      The list of mappings from a source table to target tables.

      

    
      - *(dict) --* 

        Defines a mapping.

        

      
        - **SourceTable** *(string) --* 

          The name of the source table.

          

        
        - **SourcePath** *(string) --* 

          The source path.

          

        
        - **SourceType** *(string) --* 

          The source type.

          

        
        - **TargetTable** *(string) --* 

          The target table.

          

        
        - **TargetPath** *(string) --* 

          The target path.

          

        
        - **TargetType** *(string) --* 

          The target type.

          

        
      
  
    :type Source: dict
    :param Source: **[REQUIRED]** 

      The source table.

      

    
      - **DatabaseName** *(string) --* **[REQUIRED]** 

        The database in which the table metadata resides.

        

      
      - **TableName** *(string) --* **[REQUIRED]** 

        The name of the table in question.

        

      
    
    :type Sinks: list
    :param Sinks: 

      The target tables.

      

    
      - *(dict) --* 

        Specifies a table definition in the Data Catalog.

        

      
        - **DatabaseName** *(string) --* **[REQUIRED]** 

          The database in which the table metadata resides.

          

        
        - **TableName** *(string) --* **[REQUIRED]** 

          The name of the table in question.

          

        
      
  
    :type Location: dict
    :param Location: 

      Parameters for the mapping.

      

    
      - **Jdbc** *(list) --* 

        A JDBC location.

        

      
        - *(dict) --* 

          An argument or property of a node.

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The name of the argument or property.

            

          
          - **Value** *(string) --* **[REQUIRED]** 

            The value of the argument or property.

            

          
          - **Param** *(boolean) --* 

            True if the value is used as a parameter.

            

          
        
    
      - **S3** *(list) --* 

        An Amazon S3 location.

        

      
        - *(dict) --* 

          An argument or property of a node.

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The name of the argument or property.

            

          
          - **Value** *(string) --* **[REQUIRED]** 

            The value of the argument or property.

            

          
          - **Param** *(boolean) --* 

            True if the value is used as a parameter.

            

          
        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PythonScript': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PythonScript** *(string) --* 

          A Python script to perform the mapping.

          
    

  .. py:method:: get_table(**kwargs)

    

    Retrieves the ``Table`` definition in a Data Catalog for a specified table.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTable>`_    


    **Request Syntax** 
    ::

      response = client.get_table(
          CatalogId='string',
          DatabaseName='string',
          Name='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the database in the catalog in which the table resides.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the table for which to retrieve the definition.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Table': {
                'Name': 'string',
                'DatabaseName': 'string',
                'Description': 'string',
                'Owner': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'UpdateTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'LastAnalyzedTime': datetime(2015, 1, 1),
                'Retention': 123,
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string'
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'PartitionKeys': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string'
                    },
                ],
                'ViewOriginalText': 'string',
                'ViewExpandedText': 'string',
                'TableType': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreatedBy': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Table** *(dict) --* 

          The ``Table`` object that defines the specified table.

          
          

          - **Name** *(string) --* 

            Name of the table.

            
          

          - **DatabaseName** *(string) --* 

            Name of the metadata database where the table metadata resides.

            
          

          - **Description** *(string) --* 

            Description of the table.

            
          

          - **Owner** *(string) --* 

            Owner of the table.

            
          

          - **CreateTime** *(datetime) --* 

            Time when the table definition was created in the Data Catalog.

            
          

          - **UpdateTime** *(datetime) --* 

            Last time the table was updated.

            
          

          - **LastAccessTime** *(datetime) --* 

            Last time the table was accessed. This is usually taken from HDFS, and may not be reliable.

            
          

          - **LastAnalyzedTime** *(datetime) --* 

            Last time column statistics were computed for this table.

            
          

          - **Retention** *(integer) --* 

            Retention time for this table.

            
          

          - **StorageDescriptor** *(dict) --* 

            A storage descriptor containing information about the physical storage of this table.

            
            

            - **Columns** *(list) --* 

              A list of the ``Columns`` in the table.

              
              

              - *(dict) --* 

                A column in a ``Table`` .

                
                

                - **Name** *(string) --* 

                  The name of the ``Column`` .

                  
                

                - **Type** *(string) --* 

                  The datatype of data in the ``Column`` .

                  
                

                - **Comment** *(string) --* 

                  Free-form text comment.

                  
            
          
            

            - **Location** *(string) --* 

              The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

              
            

            - **InputFormat** *(string) --* 

              The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

              
            

            - **OutputFormat** *(string) --* 

              The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

              
            

            - **Compressed** *(boolean) --* 

              True if the data in the table is compressed, or False if not.

              
            

            - **NumberOfBuckets** *(integer) --* 

              Must be specified if the table contains any dimension columns.

              
            

            - **SerdeInfo** *(dict) --* 

              Serialization/deserialization (SerDe) information.

              
              

              - **Name** *(string) --* 

                Name of the SerDe.

                
              

              - **SerializationLibrary** *(string) --* 

                Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                
              

              - **Parameters** *(dict) --* 

                A list of initialization parameters for the SerDe, in key-value form.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
            

            - **BucketColumns** *(list) --* 

              A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

              
              

              - *(string) --* 
          
            

            - **SortColumns** *(list) --* 

              A list specifying the sort order of each bucket in the table.

              
              

              - *(dict) --* 

                Specifies the sort order of a sorted column.

                
                

                - **Column** *(string) --* 

                  The name of the column.

                  
                

                - **SortOrder** *(integer) --* 

                  Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

                  
            
          
            

            - **Parameters** *(dict) --* 

              User-supplied properties in key-value form.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **SkewedInfo** *(dict) --* 

              Information about values that appear very frequently in a column (skewed values).

              
              

              - **SkewedColumnNames** *(list) --* 

                A list of names of columns that contain skewed values.

                
                

                - *(string) --* 
            
              

              - **SkewedColumnValues** *(list) --* 

                A list of values that appear so frequently as to be considered skewed.

                
                

                - *(string) --* 
            
              

              - **SkewedColumnValueLocationMaps** *(dict) --* 

                A mapping of skewed values to the columns that contain them.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
            

            - **StoredAsSubDirectories** *(boolean) --* 

              True if the table data is stored in subdirectories, or False if not.

              
        
          

          - **PartitionKeys** *(list) --* 

            A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

            
            

            - *(dict) --* 

              A column in a ``Table`` .

              
              

              - **Name** *(string) --* 

                The name of the ``Column`` .

                
              

              - **Type** *(string) --* 

                The datatype of data in the ``Column`` .

                
              

              - **Comment** *(string) --* 

                Free-form text comment.

                
          
        
          

          - **ViewOriginalText** *(string) --* 

            If the table is a view, the original text of the view; otherwise ``null`` .

            
          

          - **ViewExpandedText** *(string) --* 

            If the table is a view, the expanded text of the view; otherwise ``null`` .

            
          

          - **TableType** *(string) --* 

            The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

            
          

          - **Parameters** *(dict) --* 

            Properties associated with this table, as a list of key-value pairs.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **CreatedBy** *(string) --* 

            Person or entity who created the table.

            
      
    

  .. py:method:: get_table_versions(**kwargs)

    

    Retrieves a list of strings that identify available versions of a specified table.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTableVersions>`_    


    **Request Syntax** 
    ::

      response = client.get_table_versions(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          NextToken='string',
          MaxResults=123
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The database in the catalog in which the table resides.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the table.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is not the first call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of table versions to return in one response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TableVersions': [
                {
                    'Table': {
                        'Name': 'string',
                        'DatabaseName': 'string',
                        'Description': 'string',
                        'Owner': 'string',
                        'CreateTime': datetime(2015, 1, 1),
                        'UpdateTime': datetime(2015, 1, 1),
                        'LastAccessTime': datetime(2015, 1, 1),
                        'LastAnalyzedTime': datetime(2015, 1, 1),
                        'Retention': 123,
                        'StorageDescriptor': {
                            'Columns': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string'
                                },
                            ],
                            'Location': 'string',
                            'InputFormat': 'string',
                            'OutputFormat': 'string',
                            'Compressed': True|False,
                            'NumberOfBuckets': 123,
                            'SerdeInfo': {
                                'Name': 'string',
                                'SerializationLibrary': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                            'BucketColumns': [
                                'string',
                            ],
                            'SortColumns': [
                                {
                                    'Column': 'string',
                                    'SortOrder': 123
                                },
                            ],
                            'Parameters': {
                                'string': 'string'
                            },
                            'SkewedInfo': {
                                'SkewedColumnNames': [
                                    'string',
                                ],
                                'SkewedColumnValues': [
                                    'string',
                                ],
                                'SkewedColumnValueLocationMaps': {
                                    'string': 'string'
                                }
                            },
                            'StoredAsSubDirectories': True|False
                        },
                        'PartitionKeys': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string'
                            },
                        ],
                        'ViewOriginalText': 'string',
                        'ViewExpandedText': 'string',
                        'TableType': 'string',
                        'Parameters': {
                            'string': 'string'
                        },
                        'CreatedBy': 'string'
                    },
                    'VersionId': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TableVersions** *(list) --* 

          A list of strings identifying available versions of the specified table.

          
          

          - *(dict) --* 

            Specifies a version of a table.

            
            

            - **Table** *(dict) --* 

              The table in question

              
              

              - **Name** *(string) --* 

                Name of the table.

                
              

              - **DatabaseName** *(string) --* 

                Name of the metadata database where the table metadata resides.

                
              

              - **Description** *(string) --* 

                Description of the table.

                
              

              - **Owner** *(string) --* 

                Owner of the table.

                
              

              - **CreateTime** *(datetime) --* 

                Time when the table definition was created in the Data Catalog.

                
              

              - **UpdateTime** *(datetime) --* 

                Last time the table was updated.

                
              

              - **LastAccessTime** *(datetime) --* 

                Last time the table was accessed. This is usually taken from HDFS, and may not be reliable.

                
              

              - **LastAnalyzedTime** *(datetime) --* 

                Last time column statistics were computed for this table.

                
              

              - **Retention** *(integer) --* 

                Retention time for this table.

                
              

              - **StorageDescriptor** *(dict) --* 

                A storage descriptor containing information about the physical storage of this table.

                
                

                - **Columns** *(list) --* 

                  A list of the ``Columns`` in the table.

                  
                  

                  - *(dict) --* 

                    A column in a ``Table`` .

                    
                    

                    - **Name** *(string) --* 

                      The name of the ``Column`` .

                      
                    

                    - **Type** *(string) --* 

                      The datatype of data in the ``Column`` .

                      
                    

                    - **Comment** *(string) --* 

                      Free-form text comment.

                      
                
              
                

                - **Location** *(string) --* 

                  The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

                  
                

                - **InputFormat** *(string) --* 

                  The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

                  
                

                - **OutputFormat** *(string) --* 

                  The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

                  
                

                - **Compressed** *(boolean) --* 

                  True if the data in the table is compressed, or False if not.

                  
                

                - **NumberOfBuckets** *(integer) --* 

                  Must be specified if the table contains any dimension columns.

                  
                

                - **SerdeInfo** *(dict) --* 

                  Serialization/deserialization (SerDe) information.

                  
                  

                  - **Name** *(string) --* 

                    Name of the SerDe.

                    
                  

                  - **SerializationLibrary** *(string) --* 

                    Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                    
                  

                  - **Parameters** *(dict) --* 

                    A list of initialization parameters for the SerDe, in key-value form.

                    
                    

                    - *(string) --* 
                      

                      - *(string) --* 
                
              
              
                

                - **BucketColumns** *(list) --* 

                  A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

                  
                  

                  - *(string) --* 
              
                

                - **SortColumns** *(list) --* 

                  A list specifying the sort order of each bucket in the table.

                  
                  

                  - *(dict) --* 

                    Specifies the sort order of a sorted column.

                    
                    

                    - **Column** *(string) --* 

                      The name of the column.

                      
                    

                    - **SortOrder** *(integer) --* 

                      Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

                      
                
              
                

                - **Parameters** *(dict) --* 

                  User-supplied properties in key-value form.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **SkewedInfo** *(dict) --* 

                  Information about values that appear very frequently in a column (skewed values).

                  
                  

                  - **SkewedColumnNames** *(list) --* 

                    A list of names of columns that contain skewed values.

                    
                    

                    - *(string) --* 
                
                  

                  - **SkewedColumnValues** *(list) --* 

                    A list of values that appear so frequently as to be considered skewed.

                    
                    

                    - *(string) --* 
                
                  

                  - **SkewedColumnValueLocationMaps** *(dict) --* 

                    A mapping of skewed values to the columns that contain them.

                    
                    

                    - *(string) --* 
                      

                      - *(string) --* 
                
              
              
                

                - **StoredAsSubDirectories** *(boolean) --* 

                  True if the table data is stored in subdirectories, or False if not.

                  
            
              

              - **PartitionKeys** *(list) --* 

                A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

                
                

                - *(dict) --* 

                  A column in a ``Table`` .

                  
                  

                  - **Name** *(string) --* 

                    The name of the ``Column`` .

                    
                  

                  - **Type** *(string) --* 

                    The datatype of data in the ``Column`` .

                    
                  

                  - **Comment** *(string) --* 

                    Free-form text comment.

                    
              
            
              

              - **ViewOriginalText** *(string) --* 

                If the table is a view, the original text of the view; otherwise ``null`` .

                
              

              - **ViewExpandedText** *(string) --* 

                If the table is a view, the expanded text of the view; otherwise ``null`` .

                
              

              - **TableType** *(string) --* 

                The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

                
              

              - **Parameters** *(dict) --* 

                Properties associated with this table, as a list of key-value pairs.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **CreatedBy** *(string) --* 

                Person or entity who created the table.

                
          
            

            - **VersionId** *(string) --* 

              The ID value that identifies this table version.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if the list of available versions does not include the last one.

          
    

  .. py:method:: get_tables(**kwargs)

    

    Retrieves the definitions of some or all of the tables in a given ``Database`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTables>`_    


    **Request Syntax** 
    ::

      response = client.get_tables(
          CatalogId='string',
          DatabaseName='string',
          Expression='string',
          NextToken='string',
          MaxResults=123
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The database in the catalog whose tables to list.

      

    
    :type Expression: string
    :param Expression: 

      A regular expression pattern. If present, only those tables whose names match the pattern are returned.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, included if this is a continuation call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of tables to return in a single response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TableList': [
                {
                    'Name': 'string',
                    'DatabaseName': 'string',
                    'Description': 'string',
                    'Owner': 'string',
                    'CreateTime': datetime(2015, 1, 1),
                    'UpdateTime': datetime(2015, 1, 1),
                    'LastAccessTime': datetime(2015, 1, 1),
                    'LastAnalyzedTime': datetime(2015, 1, 1),
                    'Retention': 123,
                    'StorageDescriptor': {
                        'Columns': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string'
                            },
                        ],
                        'Location': 'string',
                        'InputFormat': 'string',
                        'OutputFormat': 'string',
                        'Compressed': True|False,
                        'NumberOfBuckets': 123,
                        'SerdeInfo': {
                            'Name': 'string',
                            'SerializationLibrary': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                        'BucketColumns': [
                            'string',
                        ],
                        'SortColumns': [
                            {
                                'Column': 'string',
                                'SortOrder': 123
                            },
                        ],
                        'Parameters': {
                            'string': 'string'
                        },
                        'SkewedInfo': {
                            'SkewedColumnNames': [
                                'string',
                            ],
                            'SkewedColumnValues': [
                                'string',
                            ],
                            'SkewedColumnValueLocationMaps': {
                                'string': 'string'
                            }
                        },
                        'StoredAsSubDirectories': True|False
                    },
                    'PartitionKeys': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string'
                        },
                    ],
                    'ViewOriginalText': 'string',
                    'ViewExpandedText': 'string',
                    'TableType': 'string',
                    'Parameters': {
                        'string': 'string'
                    },
                    'CreatedBy': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TableList** *(list) --* 

          A list of the requested ``Table`` objects.

          
          

          - *(dict) --* 

            Represents a collection of related data organized in columns and rows.

            
            

            - **Name** *(string) --* 

              Name of the table.

              
            

            - **DatabaseName** *(string) --* 

              Name of the metadata database where the table metadata resides.

              
            

            - **Description** *(string) --* 

              Description of the table.

              
            

            - **Owner** *(string) --* 

              Owner of the table.

              
            

            - **CreateTime** *(datetime) --* 

              Time when the table definition was created in the Data Catalog.

              
            

            - **UpdateTime** *(datetime) --* 

              Last time the table was updated.

              
            

            - **LastAccessTime** *(datetime) --* 

              Last time the table was accessed. This is usually taken from HDFS, and may not be reliable.

              
            

            - **LastAnalyzedTime** *(datetime) --* 

              Last time column statistics were computed for this table.

              
            

            - **Retention** *(integer) --* 

              Retention time for this table.

              
            

            - **StorageDescriptor** *(dict) --* 

              A storage descriptor containing information about the physical storage of this table.

              
              

              - **Columns** *(list) --* 

                A list of the ``Columns`` in the table.

                
                

                - *(dict) --* 

                  A column in a ``Table`` .

                  
                  

                  - **Name** *(string) --* 

                    The name of the ``Column`` .

                    
                  

                  - **Type** *(string) --* 

                    The datatype of data in the ``Column`` .

                    
                  

                  - **Comment** *(string) --* 

                    Free-form text comment.

                    
              
            
              

              - **Location** *(string) --* 

                The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

                
              

              - **InputFormat** *(string) --* 

                The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

                
              

              - **OutputFormat** *(string) --* 

                The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

                
              

              - **Compressed** *(boolean) --* 

                True if the data in the table is compressed, or False if not.

                
              

              - **NumberOfBuckets** *(integer) --* 

                Must be specified if the table contains any dimension columns.

                
              

              - **SerdeInfo** *(dict) --* 

                Serialization/deserialization (SerDe) information.

                
                

                - **Name** *(string) --* 

                  Name of the SerDe.

                  
                

                - **SerializationLibrary** *(string) --* 

                  Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                  
                

                - **Parameters** *(dict) --* 

                  A list of initialization parameters for the SerDe, in key-value form.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
              

              - **BucketColumns** *(list) --* 

                A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

                
                

                - *(string) --* 
            
              

              - **SortColumns** *(list) --* 

                A list specifying the sort order of each bucket in the table.

                
                

                - *(dict) --* 

                  Specifies the sort order of a sorted column.

                  
                  

                  - **Column** *(string) --* 

                    The name of the column.

                    
                  

                  - **SortOrder** *(integer) --* 

                    Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

                    
              
            
              

              - **Parameters** *(dict) --* 

                User-supplied properties in key-value form.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **SkewedInfo** *(dict) --* 

                Information about values that appear very frequently in a column (skewed values).

                
                

                - **SkewedColumnNames** *(list) --* 

                  A list of names of columns that contain skewed values.

                  
                  

                  - *(string) --* 
              
                

                - **SkewedColumnValues** *(list) --* 

                  A list of values that appear so frequently as to be considered skewed.

                  
                  

                  - *(string) --* 
              
                

                - **SkewedColumnValueLocationMaps** *(dict) --* 

                  A mapping of skewed values to the columns that contain them.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
              

              - **StoredAsSubDirectories** *(boolean) --* 

                True if the table data is stored in subdirectories, or False if not.

                
          
            

            - **PartitionKeys** *(list) --* 

              A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

              
              

              - *(dict) --* 

                A column in a ``Table`` .

                
                

                - **Name** *(string) --* 

                  The name of the ``Column`` .

                  
                

                - **Type** *(string) --* 

                  The datatype of data in the ``Column`` .

                  
                

                - **Comment** *(string) --* 

                  Free-form text comment.

                  
            
          
            

            - **ViewOriginalText** *(string) --* 

              If the table is a view, the original text of the view; otherwise ``null`` .

              
            

            - **ViewExpandedText** *(string) --* 

              If the table is a view, the expanded text of the view; otherwise ``null`` .

              
            

            - **TableType** *(string) --* 

              The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

              
            

            - **Parameters** *(dict) --* 

              Properties associated with this table, as a list of key-value pairs.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **CreatedBy** *(string) --* 

              Person or entity who created the table.

              
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, present if the current list segment is not the last.

          
    

  .. py:method:: get_trigger(**kwargs)

    

    Retrieves the definition of a trigger.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTrigger>`_    


    **Request Syntax** 
    ::

      response = client.get_trigger(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the trigger to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Trigger': {
                'Name': 'string',
                'Id': 'string',
                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                'Description': 'string',
                'Schedule': 'string',
                'Actions': [
                    {
                        'JobName': 'string',
                        'Arguments': {
                            'string': 'string'
                        }
                    },
                ],
                'Predicate': {
                    'Logical': 'AND',
                    'Conditions': [
                        {
                            'LogicalOperator': 'EQUALS',
                            'JobName': 'string',
                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                        },
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Trigger** *(dict) --* 

          The requested trigger definition.

          
          

          - **Name** *(string) --* 

            Name of the trigger.

            
          

          - **Id** *(string) --* 

            The trigger ID.

            
          

          - **Type** *(string) --* 

            The type of trigger that this is.

            
          

          - **State** *(string) --* 

            The current state of the trigger.

            
          

          - **Description** *(string) --* 

            A description of this trigger.

            
          

          - **Schedule** *(string) --* 

            A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

            
          

          - **Actions** *(list) --* 

            The actions initiated by this trigger.

            
            

            - *(dict) --* 

              Defines an action to be initiated by a trigger.

              
              

              - **JobName** *(string) --* 

                The name of a job to be executed.

                
              

              - **Arguments** *(dict) --* 

                Arguments to be passed to the job.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
        
          

          - **Predicate** *(dict) --* 

            The predicate of this trigger.

            
            

            - **Logical** *(string) --* 

              Currently "OR" is not supported.

              
            

            - **Conditions** *(list) --* 

              A list of the conditions that determine when the trigger will fire.

              
              

              - *(dict) --* 

                Defines a condition under which a trigger fires.

                
                

                - **LogicalOperator** *(string) --* 

                  A logical operator.

                  
                

                - **JobName** *(string) --* 

                  The name of the job in question.

                  
                

                - **State** *(string) --* 

                  The condition state.

                  
            
          
        
      
    

  .. py:method:: get_triggers(**kwargs)

    

    Gets all the triggers associated with a job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTriggers>`_    


    **Request Syntax** 
    ::

      response = client.get_triggers(
          NextToken='string',
          DependentJobName='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation call.

      

    
    :type DependentJobName: string
    :param DependentJobName: 

      The name of the job for which to retrieve triggers.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum size of the response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Triggers': [
                {
                    'Name': 'string',
                    'Id': 'string',
                    'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                    'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                    'Description': 'string',
                    'Schedule': 'string',
                    'Actions': [
                        {
                            'JobName': 'string',
                            'Arguments': {
                                'string': 'string'
                            }
                        },
                    ],
                    'Predicate': {
                        'Logical': 'AND',
                        'Conditions': [
                            {
                                'LogicalOperator': 'EQUALS',
                                'JobName': 'string',
                                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                            },
                        ]
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Triggers** *(list) --* 

          A list of triggers for the specified job.

          
          

          - *(dict) --* 

            Information about a specific trigger.

            
            

            - **Name** *(string) --* 

              Name of the trigger.

              
            

            - **Id** *(string) --* 

              The trigger ID.

              
            

            - **Type** *(string) --* 

              The type of trigger that this is.

              
            

            - **State** *(string) --* 

              The current state of the trigger.

              
            

            - **Description** *(string) --* 

              A description of this trigger.

              
            

            - **Schedule** *(string) --* 

              A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

              
            

            - **Actions** *(list) --* 

              The actions initiated by this trigger.

              
              

              - *(dict) --* 

                Defines an action to be initiated by a trigger.

                
                

                - **JobName** *(string) --* 

                  The name of a job to be executed.

                  
                

                - **Arguments** *(dict) --* 

                  Arguments to be passed to the job.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
          
            

            - **Predicate** *(dict) --* 

              The predicate of this trigger.

              
              

              - **Logical** *(string) --* 

                Currently "OR" is not supported.

                
              

              - **Conditions** *(list) --* 

                A list of the conditions that determine when the trigger will fire.

                
                

                - *(dict) --* 

                  Defines a condition under which a trigger fires.

                  
                  

                  - **LogicalOperator** *(string) --* 

                    A logical operator.

                    
                  

                  - **JobName** *(string) --* 

                    The name of the job in question.

                    
                  

                  - **State** *(string) --* 

                    The condition state.

                    
              
            
          
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if not all the requested triggers have yet been returned.

          
    

  .. py:method:: get_user_defined_function(**kwargs)

    

    Retrieves a specified function definition from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetUserDefinedFunction>`_    


    **Request Syntax** 
    ::

      response = client.get_user_defined_function(
          CatalogId='string',
          DatabaseName='string',
          FunctionName='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the function to be retrieved is located. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database where the function is located.

      

    
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The name of the function.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserDefinedFunction': {
                'FunctionName': 'string',
                'ClassName': 'string',
                'OwnerName': 'string',
                'OwnerType': 'USER'|'ROLE'|'GROUP',
                'CreateTime': datetime(2015, 1, 1),
                'ResourceUris': [
                    {
                        'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                        'Uri': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UserDefinedFunction** *(dict) --* 

          The requested function definition.

          
          

          - **FunctionName** *(string) --* 

            The name of the function.

            
          

          - **ClassName** *(string) --* 

            The Java class that contains the function code.

            
          

          - **OwnerName** *(string) --* 

            The owner of the function.

            
          

          - **OwnerType** *(string) --* 

            The owner type.

            
          

          - **CreateTime** *(datetime) --* 

            The time at which the function was created.

            
          

          - **ResourceUris** *(list) --* 

            The resource URIs for the function.

            
            

            - *(dict) --* 

              URIs for function resources.

              
              

              - **ResourceType** *(string) --* 

                The type of the resource.

                
              

              - **Uri** *(string) --* 

                The URI for accessing the resource.

                
          
        
      
    

  .. py:method:: get_user_defined_functions(**kwargs)

    

    Retrieves a multiple function definitions from the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetUserDefinedFunctions>`_    


    **Request Syntax** 
    ::

      response = client.get_user_defined_functions(
          CatalogId='string',
          DatabaseName='string',
          Pattern='string',
          NextToken='string',
          MaxResults=123
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the functions to be retrieved are located. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database where the functions are located.

      

    
    :type Pattern: string
    :param Pattern: **[REQUIRED]** 

      An optional function-name pattern string that filters the function definitions returned.

      

    
    :type NextToken: string
    :param NextToken: 

      A continuation token, if this is a continuation call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of functions to return in one response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserDefinedFunctions': [
                {
                    'FunctionName': 'string',
                    'ClassName': 'string',
                    'OwnerName': 'string',
                    'OwnerType': 'USER'|'ROLE'|'GROUP',
                    'CreateTime': datetime(2015, 1, 1),
                    'ResourceUris': [
                        {
                            'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                            'Uri': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UserDefinedFunctions** *(list) --* 

          A list of requested function definitions.

          
          

          - *(dict) --* 

            Represents the equivalent of a Hive user-defined function (``UDF`` ) definition.

            
            

            - **FunctionName** *(string) --* 

              The name of the function.

              
            

            - **ClassName** *(string) --* 

              The Java class that contains the function code.

              
            

            - **OwnerName** *(string) --* 

              The owner of the function.

              
            

            - **OwnerType** *(string) --* 

              The owner type.

              
            

            - **CreateTime** *(datetime) --* 

              The time at which the function was created.

              
            

            - **ResourceUris** *(list) --* 

              The resource URIs for the function.

              
              

              - *(dict) --* 

                URIs for function resources.

                
                

                - **ResourceType** *(string) --* 

                  The type of the resource.

                  
                

                - **Uri** *(string) --* 

                  The URI for accessing the resource.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A continuation token, if the list of functions returned does not include the last requested function.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: import_catalog_to_glue(**kwargs)

    

    Imports an existing Athena Data Catalog to AWS Glue

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ImportCatalogToGlue>`_    


    **Request Syntax** 
    ::

      response = client.import_catalog_to_glue(
          CatalogId='string'
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the catalog to import. Currently, this should be the AWS account ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: reset_job_bookmark(**kwargs)

    

    Resets a bookmark entry.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ResetJobBookmark>`_    


    **Request Syntax** 
    ::

      response = client.reset_job_bookmark(
          JobName='string'
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      The name of the job in question.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobBookmarkEntry': {
                'JobName': 'string',
                'Version': 123,
                'Run': 123,
                'Attempt': 123,
                'JobBookmark': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobBookmarkEntry** *(dict) --* 

          The reset bookmark entry.

          
          

          - **JobName** *(string) --* 

            Name of the job in question.

            
          

          - **Version** *(integer) --* 

            Version of the job.

            
          

          - **Run** *(integer) --* 

            The run ID number.

            
          

          - **Attempt** *(integer) --* 

            The attempt ID number.

            
          

          - **JobBookmark** *(string) --* 

            The bookmark itself.

            
      
    

  .. py:method:: start_crawler(**kwargs)

    

    Starts a crawl using the specified crawler, regardless of what is scheduled. If the crawler is already running, does nothing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartCrawler>`_    


    **Request Syntax** 
    ::

      response = client.start_crawler(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the crawler to start.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: start_crawler_schedule(**kwargs)

    

    Changes the schedule state of the specified crawler to ``SCHEDULED`` , unless the crawler is already running or the schedule state is already ``SCHEDULED`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartCrawlerSchedule>`_    


    **Request Syntax** 
    ::

      response = client.start_crawler_schedule(
          CrawlerName='string'
      )
    :type CrawlerName: string
    :param CrawlerName: **[REQUIRED]** 

      Name of the crawler to schedule.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: start_job_run(**kwargs)

    

    Runs a job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartJobRun>`_    


    **Request Syntax** 
    ::

      response = client.start_job_run(
          JobName='string',
          JobRunId='string',
          Arguments={
              'string': 'string'
          },
          AllocatedCapacity=123
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      The name of the job to start.

      

    
    :type JobRunId: string
    :param JobRunId: 

      The ID of the job run to start.

      

    
    :type Arguments: dict
    :param Arguments: 

      Specific arguments for this job run.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AllocatedCapacity: integer
    :param AllocatedCapacity: 

      The infrastructure capacity to allocate to this job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobRunId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobRunId** *(string) --* 

          The ID assigned to this job run.

          
    

  .. py:method:: start_trigger(**kwargs)

    

    Starts an existing trigger.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StartTrigger>`_    


    **Request Syntax** 
    ::

      response = client.start_trigger(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the trigger to start.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          The name of the trigger that was started.

          
    

  .. py:method:: stop_crawler(**kwargs)

    

    If the specified crawler is running, stops the crawl.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StopCrawler>`_    


    **Request Syntax** 
    ::

      response = client.stop_crawler(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the crawler to stop.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: stop_crawler_schedule(**kwargs)

    

    Sets the schedule state of the specified crawler to ``NOT_SCHEDULED`` , but does not stop the crawler if it is already running.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StopCrawlerSchedule>`_    


    **Request Syntax** 
    ::

      response = client.stop_crawler_schedule(
          CrawlerName='string'
      )
    :type CrawlerName: string
    :param CrawlerName: **[REQUIRED]** 

      Name of the crawler whose schedule state to set.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: stop_trigger(**kwargs)

    

    Stops a specified trigger.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/StopTrigger>`_    


    **Request Syntax** 
    ::

      response = client.stop_trigger(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the trigger to stop.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          The name of the trigger that was stopped.

          
    

  .. py:method:: update_classifier(**kwargs)

    

    Modifies an existing classifier (either a ``GrokClassifier`` or an ``XMLClassifier`` ).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateClassifier>`_    


    **Request Syntax** 
    ::

      response = client.update_classifier(
          GrokClassifier={
              'Name': 'string',
              'Classification': 'string',
              'GrokPattern': 'string',
              'CustomPatterns': 'string'
          },
          XMLClassifier={
              'Name': 'string',
              'Classification': 'string',
              'RowTag': 'string'
          }
      )
    :type GrokClassifier: dict
    :param GrokClassifier: 

      A ``GrokClassifier`` object with updated fields.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the ``GrokClassifier`` .

        

      
      - **Classification** *(string) --* 

        An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.

        

      
      - **GrokPattern** *(string) --* 

        The grok pattern used by this classifier.

        

      
      - **CustomPatterns** *(string) --* 

        Optional custom grok patterns used by this classifier.

        

      
    
    :type XMLClassifier: dict
    :param XMLClassifier: 

      An ``XMLClassifier`` object with updated fields.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the classifier.

        

      
      - **Classification** *(string) --* 

        An identifier of the data format that the classifier matches.

        

      
      - **RowTag** *(string) --* 

        The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot be an empty element. It must contain child elements representing fields in the record.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_connection(**kwargs)

    

    Updates a connection definition in the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateConnection>`_    


    **Request Syntax** 
    ::

      response = client.update_connection(
          CatalogId='string',
          Name='string',
          ConnectionInput={
              'Name': 'string',
              'Description': 'string',
              'ConnectionType': 'JDBC'|'SFTP',
              'MatchCriteria': [
                  'string',
              ],
              'ConnectionProperties': {
                  'string': 'string'
              },
              'PhysicalConnectionRequirements': {
                  'SubnetId': 'string',
                  'SecurityGroupIdList': [
                      'string',
                  ],
                  'AvailabilityZone': 'string'
              }
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which the connection resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the connection definition to update.

      

    
    :type ConnectionInput: dict
    :param ConnectionInput: **[REQUIRED]** 

      A ``ConnectionInput`` object that redefines the connection in question.

      

    
      - **Name** *(string) --* 

        The name of the connection.

        

      
      - **Description** *(string) --* 

        Description of the connection.

        

      
      - **ConnectionType** *(string) --* 

        The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

        

      
      - **MatchCriteria** *(list) --* 

        A list of criteria that can be used in selecting this connection.

        

      
        - *(string) --* 

        
    
      - **ConnectionProperties** *(dict) --* 

        A list of key-value pairs used as parameters for this connection.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **PhysicalConnectionRequirements** *(dict) --* 

        A map of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.

        

      
        - **SubnetId** *(string) --* 

          The subnet ID used by the connection.

          

        
        - **SecurityGroupIdList** *(list) --* 

          The security group ID list used by the connection.

          

        
          - *(string) --* 

          
      
        - **AvailabilityZone** *(string) --* 

          The connection's availability zone.

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_crawler(**kwargs)

    

    Updates a crawler. If a crawler is running, you must stop it using ``StopCrawler`` before updating it.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateCrawler>`_    


    **Request Syntax** 
    ::

      response = client.update_crawler(
          Name='string',
          Role='string',
          DatabaseName='string',
          Description='string',
          Targets={
              'S3Targets': [
                  {
                      'Path': 'string',
                      'Exclusions': [
                          'string',
                      ]
                  },
              ],
              'JdbcTargets': [
                  {
                      'ConnectionName': 'string',
                      'Path': 'string',
                      'Exclusions': [
                          'string',
                      ]
                  },
              ]
          },
          Schedule='string',
          Classifiers=[
              'string',
          ],
          TablePrefix='string',
          SchemaChangePolicy={
              'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
              'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
          },
          Configuration='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the new crawler.

      

    
    :type Role: string
    :param Role: 

      The IAM role (or ARN of an IAM role) used by the new crawler to access customer resources.

      

    
    :type DatabaseName: string
    :param DatabaseName: 

      The AWS Glue database where results are stored, such as: ``arn:aws:daylight:us-east-1::database/sometable/*`` .

      

    
    :type Description: string
    :param Description: 

      A description of the new crawler.

      

    
    :type Targets: dict
    :param Targets: 

      A list of targets to crawl.

      

    
      - **S3Targets** *(list) --* 

        Specifies Amazon S3 targets.

        

      
        - *(dict) --* 

          Specifies a data store in Amazon S3.

          

        
          - **Path** *(string) --* 

            The path to the Amazon S3 target.

            

          
          - **Exclusions** *(list) --* 

            A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

            

          
            - *(string) --* 

            
        
        
    
      - **JdbcTargets** *(list) --* 

        Specifies JDBC targets.

        

      
        - *(dict) --* 

          Specifies a JDBC data store to crawl.

          

        
          - **ConnectionName** *(string) --* 

            The name of the connection to use to connect to the JDBC target.

            

          
          - **Path** *(string) --* 

            The path of the JDBC target.

            

          
          - **Exclusions** *(list) --* 

            A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

            

          
            - *(string) --* 

            
        
        
    
    
    :type Schedule: string
    :param Schedule: 

      A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

      

    
    :type Classifiers: list
    :param Classifiers: 

      A list of custom classifiers that the user has registered. By default, all classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.

      

    
      - *(string) --* 

      
  
    :type TablePrefix: string
    :param TablePrefix: 

      The table prefix used for catalog tables that are created.

      

    
    :type SchemaChangePolicy: dict
    :param SchemaChangePolicy: 

      Policy for the crawler's update and deletion behavior.

      

    
      - **UpdateBehavior** *(string) --* 

        The update behavior when the crawler finds a changed schema.

        

      
      - **DeleteBehavior** *(string) --* 

        The deletion behavior when the crawler finds a deleted object.

        

      
    
    :type Configuration: string
    :param Configuration: 

      Crawler configuration information. This versioned JSON string allows users to specify aspects of a Crawler's behavior.

       

      You can use this field to force partitions to inherit metadata such as classification, input format, output format, serde information, and schema from their parent table, rather than detect this information separately for each partition. Use the following JSON string to specify that behavior:

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_crawler_schedule(**kwargs)

    

    Updates the schedule of a crawler using a ``cron`` expression. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateCrawlerSchedule>`_    


    **Request Syntax** 
    ::

      response = client.update_crawler_schedule(
          CrawlerName='string',
          Schedule='string'
      )
    :type CrawlerName: string
    :param CrawlerName: **[REQUIRED]** 

      Name of the crawler whose schedule to update.

      

    
    :type Schedule: string
    :param Schedule: 

      The updated ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_database(**kwargs)

    

    Updates an existing database definition in a Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateDatabase>`_    


    **Request Syntax** 
    ::

      response = client.update_database(
          CatalogId='string',
          Name='string',
          DatabaseInput={
              'Name': 'string',
              'Description': 'string',
              'LocationUri': 'string',
              'Parameters': {
                  'string': 'string'
              }
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog in which the metadata database resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the metadata database to update in the catalog.

      

    
    :type DatabaseInput: dict
    :param DatabaseInput: **[REQUIRED]** 

      A ``DatabaseInput`` object specifying the new definition of the metadata database in the catalog.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        Name of the database.

        

      
      - **Description** *(string) --* 

        Description of the database

        

      
      - **LocationUri** *(string) --* 

        The location of the database (for example, an HDFS path).

        

      
      - **Parameters** *(dict) --* 

        A list of key-value pairs that define parameters and properties of the database.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_dev_endpoint(**kwargs)

    

    Updates a specified DevEndpoint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateDevEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.update_dev_endpoint(
          EndpointName='string',
          PublicKey='string',
          CustomLibraries={
              'ExtraPythonLibsS3Path': 'string',
              'ExtraJarsS3Path': 'string'
          },
          UpdateEtlLibraries=True|False
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the DevEndpoint to be updated.

      

    
    :type PublicKey: string
    :param PublicKey: 

      The public key for the DevEndpoint to use.

      

    
    :type CustomLibraries: dict
    :param CustomLibraries: 

      Custom Python or Java libraries to be loaded in the DevEndpoint.

      

    
      - **ExtraPythonLibsS3Path** *(string) --* 

        Path(s) to one or more Python libraries in an S3 bucket that should be loaded in your DevEndpoint. Multiple values must be complete paths separated by a comma.

         

        Please note that only pure Python libraries can currently be used on a DevEndpoint. Libraries that rely on C extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis library, are not yet supported.

        

      
      - **ExtraJarsS3Path** *(string) --* 

        Path to one or more Java Jars in an S3 bucket that should be loaded in your DevEndpoint.

         

        Please note that only pure Java/Scala libraries can currently be used on a DevEndpoint.

        

      
    
    :type UpdateEtlLibraries: boolean
    :param UpdateEtlLibraries: 

      True if the list of custom libraries to be loaded in the development endpoint needs to be updated, or False otherwise.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_job(**kwargs)

    

    Updates an existing job definition.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateJob>`_    


    **Request Syntax** 
    ::

      response = client.update_job(
          JobName='string',
          JobUpdate={
              'Description': 'string',
              'LogUri': 'string',
              'Role': 'string',
              'ExecutionProperty': {
                  'MaxConcurrentRuns': 123
              },
              'Command': {
                  'Name': 'string',
                  'ScriptLocation': 'string'
              },
              'DefaultArguments': {
                  'string': 'string'
              },
              'Connections': {
                  'Connections': [
                      'string',
                  ]
              },
              'MaxRetries': 123,
              'AllocatedCapacity': 123
          }
      )
    :type JobName: string
    :param JobName: **[REQUIRED]** 

      Name of the job definition to update.

      

    
    :type JobUpdate: dict
    :param JobUpdate: **[REQUIRED]** 

      Specifies the values with which to update the job.

      

    
      - **Description** *(string) --* 

        Description of the job.

        

      
      - **LogUri** *(string) --* 

        This field is reserved for future use.

        

      
      - **Role** *(string) --* 

        The role associated with this job.

        

      
      - **ExecutionProperty** *(dict) --* 

        An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.

        

      
        - **MaxConcurrentRuns** *(integer) --* 

          The maximum number of concurrent runs allowed for a job.

          

        
      
      - **Command** *(dict) --* 

        The JobCommand that executes this job.

        

      
        - **Name** *(string) --* 

          The name of this job command.

          

        
        - **ScriptLocation** *(string) --* 

          Specifies the location of a script that executes a job.

          

        
      
      - **DefaultArguments** *(dict) --* 

        The default parameters for this job.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Connections** *(dict) --* 

        The connections used for this job.

        

      
        - **Connections** *(list) --* 

          A list of connections used by the job.

          

        
          - *(string) --* 

          
      
      
      - **MaxRetries** *(integer) --* 

        The maximum number of times to retry this job if it fails.

        

      
      - **AllocatedCapacity** *(integer) --* 

        The number of capacity units allocated to this job.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobName': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobName** *(string) --* 

          Returns the name of the updated job.

          
    

  .. py:method:: update_partition(**kwargs)

    

    Updates a partition.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdatePartition>`_    


    **Request Syntax** 
    ::

      response = client.update_partition(
          CatalogId='string',
          DatabaseName='string',
          TableName='string',
          PartitionValueList=[
              'string',
          ],
          PartitionInput={
              'Values': [
                  'string',
              ],
              'LastAccessTime': datetime(2015, 1, 1),
              'StorageDescriptor': {
                  'Columns': [
                      {
                          'Name': 'string',
                          'Type': 'string',
                          'Comment': 'string'
                      },
                  ],
                  'Location': 'string',
                  'InputFormat': 'string',
                  'OutputFormat': 'string',
                  'Compressed': True|False,
                  'NumberOfBuckets': 123,
                  'SerdeInfo': {
                      'Name': 'string',
                      'SerializationLibrary': 'string',
                      'Parameters': {
                          'string': 'string'
                      }
                  },
                  'BucketColumns': [
                      'string',
                  ],
                  'SortColumns': [
                      {
                          'Column': 'string',
                          'SortOrder': 123
                      },
                  ],
                  'Parameters': {
                      'string': 'string'
                  },
                  'SkewedInfo': {
                      'SkewedColumnNames': [
                          'string',
                      ],
                      'SkewedColumnValues': [
                          'string',
                      ],
                      'SkewedColumnValueLocationMaps': {
                          'string': 'string'
                      }
                  },
                  'StoredAsSubDirectories': True|False
              },
              'Parameters': {
                  'string': 'string'
              },
              'LastAnalyzedTime': datetime(2015, 1, 1)
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the partition to be updated resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database in which the table in question resides.

      

    
    :type TableName: string
    :param TableName: **[REQUIRED]** 

      The name of the table where the partition to be updated is located.

      

    
    :type PartitionValueList: list
    :param PartitionValueList: **[REQUIRED]** 

      A list of the values defining the partition.

      

    
      - *(string) --* 

      
  
    :type PartitionInput: dict
    :param PartitionInput: **[REQUIRED]** 

      The new partition object to which to update the partition.

      

    
      - **Values** *(list) --* 

        The values of the partition.

        

      
        - *(string) --* 

        
    
      - **LastAccessTime** *(datetime) --* 

        The last time at which the partition was accessed.

        

      
      - **StorageDescriptor** *(dict) --* 

        Provides information about the physical location where the partition is stored.

        

      
        - **Columns** *(list) --* 

          A list of the ``Columns`` in the table.

          

        
          - *(dict) --* 

            A column in a ``Table`` .

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the ``Column`` .

              

            
            - **Type** *(string) --* 

              The datatype of data in the ``Column`` .

              

            
            - **Comment** *(string) --* 

              Free-form text comment.

              

            
          
      
        - **Location** *(string) --* 

          The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

          

        
        - **InputFormat** *(string) --* 

          The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

          

        
        - **OutputFormat** *(string) --* 

          The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

          

        
        - **Compressed** *(boolean) --* 

          True if the data in the table is compressed, or False if not.

          

        
        - **NumberOfBuckets** *(integer) --* 

          Must be specified if the table contains any dimension columns.

          

        
        - **SerdeInfo** *(dict) --* 

          Serialization/deserialization (SerDe) information.

          

        
          - **Name** *(string) --* 

            Name of the SerDe.

            

          
          - **SerializationLibrary** *(string) --* 

            Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

            

          
          - **Parameters** *(dict) --* 

            A list of initialization parameters for the SerDe, in key-value form.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
        - **BucketColumns** *(list) --* 

          A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

          

        
          - *(string) --* 

          
      
        - **SortColumns** *(list) --* 

          A list specifying the sort order of each bucket in the table.

          

        
          - *(dict) --* 

            Specifies the sort order of a sorted column.

            

          
            - **Column** *(string) --* **[REQUIRED]** 

              The name of the column.

              

            
            - **SortOrder** *(integer) --* **[REQUIRED]** 

              Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

              

            
          
      
        - **Parameters** *(dict) --* 

          User-supplied properties in key-value form.

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
        - **SkewedInfo** *(dict) --* 

          Information about values that appear very frequently in a column (skewed values).

          

        
          - **SkewedColumnNames** *(list) --* 

            A list of names of columns that contain skewed values.

            

          
            - *(string) --* 

            
        
          - **SkewedColumnValues** *(list) --* 

            A list of values that appear so frequently as to be considered skewed.

            

          
            - *(string) --* 

            
        
          - **SkewedColumnValueLocationMaps** *(dict) --* 

            A mapping of skewed values to the columns that contain them.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
        - **StoredAsSubDirectories** *(boolean) --* 

          True if the table data is stored in subdirectories, or False if not.

          

        
      
      - **Parameters** *(dict) --* 

        Partition parameters, in the form of a list of key-value pairs.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **LastAnalyzedTime** *(datetime) --* 

        The last time at which column statistics were computed for this partition.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_table(**kwargs)

    

    Updates a metadata table in the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateTable>`_    


    **Request Syntax** 
    ::

      response = client.update_table(
          CatalogId='string',
          DatabaseName='string',
          TableInput={
              'Name': 'string',
              'Description': 'string',
              'Owner': 'string',
              'LastAccessTime': datetime(2015, 1, 1),
              'LastAnalyzedTime': datetime(2015, 1, 1),
              'Retention': 123,
              'StorageDescriptor': {
                  'Columns': [
                      {
                          'Name': 'string',
                          'Type': 'string',
                          'Comment': 'string'
                      },
                  ],
                  'Location': 'string',
                  'InputFormat': 'string',
                  'OutputFormat': 'string',
                  'Compressed': True|False,
                  'NumberOfBuckets': 123,
                  'SerdeInfo': {
                      'Name': 'string',
                      'SerializationLibrary': 'string',
                      'Parameters': {
                          'string': 'string'
                      }
                  },
                  'BucketColumns': [
                      'string',
                  ],
                  'SortColumns': [
                      {
                          'Column': 'string',
                          'SortOrder': 123
                      },
                  ],
                  'Parameters': {
                      'string': 'string'
                  },
                  'SkewedInfo': {
                      'SkewedColumnNames': [
                          'string',
                      ],
                      'SkewedColumnValues': [
                          'string',
                      ],
                      'SkewedColumnValueLocationMaps': {
                          'string': 'string'
                      }
                  },
                  'StoredAsSubDirectories': True|False
              },
              'PartitionKeys': [
                  {
                      'Name': 'string',
                      'Type': 'string',
                      'Comment': 'string'
                  },
              ],
              'ViewOriginalText': 'string',
              'ViewExpandedText': 'string',
              'TableType': 'string',
              'Parameters': {
                  'string': 'string'
              }
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database in which the table resides.

      

    
    :type TableInput: dict
    :param TableInput: **[REQUIRED]** 

      An updated ``TableInput`` object to define the metadata table in the catalog.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        Name of the table.

        

      
      - **Description** *(string) --* 

        Description of the table.

        

      
      - **Owner** *(string) --* 

        Owner of the table.

        

      
      - **LastAccessTime** *(datetime) --* 

        Last time the table was accessed.

        

      
      - **LastAnalyzedTime** *(datetime) --* 

        Last time column statistics were computed for this table.

        

      
      - **Retention** *(integer) --* 

        Retention time for this table.

        

      
      - **StorageDescriptor** *(dict) --* 

        A storage descriptor containing information about the physical storage of this table.

        

      
        - **Columns** *(list) --* 

          A list of the ``Columns`` in the table.

          

        
          - *(dict) --* 

            A column in a ``Table`` .

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the ``Column`` .

              

            
            - **Type** *(string) --* 

              The datatype of data in the ``Column`` .

              

            
            - **Comment** *(string) --* 

              Free-form text comment.

              

            
          
      
        - **Location** *(string) --* 

          The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

          

        
        - **InputFormat** *(string) --* 

          The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

          

        
        - **OutputFormat** *(string) --* 

          The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

          

        
        - **Compressed** *(boolean) --* 

          True if the data in the table is compressed, or False if not.

          

        
        - **NumberOfBuckets** *(integer) --* 

          Must be specified if the table contains any dimension columns.

          

        
        - **SerdeInfo** *(dict) --* 

          Serialization/deserialization (SerDe) information.

          

        
          - **Name** *(string) --* 

            Name of the SerDe.

            

          
          - **SerializationLibrary** *(string) --* 

            Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

            

          
          - **Parameters** *(dict) --* 

            A list of initialization parameters for the SerDe, in key-value form.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
        - **BucketColumns** *(list) --* 

          A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

          

        
          - *(string) --* 

          
      
        - **SortColumns** *(list) --* 

          A list specifying the sort order of each bucket in the table.

          

        
          - *(dict) --* 

            Specifies the sort order of a sorted column.

            

          
            - **Column** *(string) --* **[REQUIRED]** 

              The name of the column.

              

            
            - **SortOrder** *(integer) --* **[REQUIRED]** 

              Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).

              

            
          
      
        - **Parameters** *(dict) --* 

          User-supplied properties in key-value form.

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
        - **SkewedInfo** *(dict) --* 

          Information about values that appear very frequently in a column (skewed values).

          

        
          - **SkewedColumnNames** *(list) --* 

            A list of names of columns that contain skewed values.

            

          
            - *(string) --* 

            
        
          - **SkewedColumnValues** *(list) --* 

            A list of values that appear so frequently as to be considered skewed.

            

          
            - *(string) --* 

            
        
          - **SkewedColumnValueLocationMaps** *(dict) --* 

            A mapping of skewed values to the columns that contain them.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
        - **StoredAsSubDirectories** *(boolean) --* 

          True if the table data is stored in subdirectories, or False if not.

          

        
      
      - **PartitionKeys** *(list) --* 

        A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

        

      
        - *(dict) --* 

          A column in a ``Table`` .

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The name of the ``Column`` .

            

          
          - **Type** *(string) --* 

            The datatype of data in the ``Column`` .

            

          
          - **Comment** *(string) --* 

            Free-form text comment.

            

          
        
    
      - **ViewOriginalText** *(string) --* 

        If the table is a view, the original text of the view; otherwise ``null`` .

        

      
      - **ViewExpandedText** *(string) --* 

        If the table is a view, the expanded text of the view; otherwise ``null`` .

        

      
      - **TableType** *(string) --* 

        The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

        

      
      - **Parameters** *(dict) --* 

        Properties associated with this table, as a list of key-value pairs.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_trigger(**kwargs)

    

    Updates a trigger definition.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateTrigger>`_    


    **Request Syntax** 
    ::

      response = client.update_trigger(
          Name='string',
          TriggerUpdate={
              'Name': 'string',
              'Description': 'string',
              'Schedule': 'string',
              'Actions': [
                  {
                      'JobName': 'string',
                      'Arguments': {
                          'string': 'string'
                      }
                  },
              ],
              'Predicate': {
                  'Logical': 'AND',
                  'Conditions': [
                      {
                          'LogicalOperator': 'EQUALS',
                          'JobName': 'string',
                          'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                      },
                  ]
              }
          }
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the trigger to update.

      

    
    :type TriggerUpdate: dict
    :param TriggerUpdate: **[REQUIRED]** 

      The new values with which to update the trigger.

      

    
      - **Name** *(string) --* 

        The name of the trigger.

        

      
      - **Description** *(string) --* 

        A description of this trigger.

        

      
      - **Schedule** *(string) --* 

        An updated ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

        

      
      - **Actions** *(list) --* 

        The actions initiated by this trigger.

        

      
        - *(dict) --* 

          Defines an action to be initiated by a trigger.

          

        
          - **JobName** *(string) --* 

            The name of a job to be executed.

            

          
          - **Arguments** *(dict) --* 

            Arguments to be passed to the job.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
        
    
      - **Predicate** *(dict) --* 

        The predicate of this trigger, which defines when it will fire.

        

      
        - **Logical** *(string) --* 

          Currently "OR" is not supported.

          

        
        - **Conditions** *(list) --* 

          A list of the conditions that determine when the trigger will fire.

          

        
          - *(dict) --* 

            Defines a condition under which a trigger fires.

            

          
            - **LogicalOperator** *(string) --* 

              A logical operator.

              

            
            - **JobName** *(string) --* 

              The name of the job in question.

              

            
            - **State** *(string) --* 

              The condition state.

              

            
          
      
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Trigger': {
                'Name': 'string',
                'Id': 'string',
                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                'Description': 'string',
                'Schedule': 'string',
                'Actions': [
                    {
                        'JobName': 'string',
                        'Arguments': {
                            'string': 'string'
                        }
                    },
                ],
                'Predicate': {
                    'Logical': 'AND',
                    'Conditions': [
                        {
                            'LogicalOperator': 'EQUALS',
                            'JobName': 'string',
                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'
                        },
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Trigger** *(dict) --* 

          The resulting trigger definition.

          
          

          - **Name** *(string) --* 

            Name of the trigger.

            
          

          - **Id** *(string) --* 

            The trigger ID.

            
          

          - **Type** *(string) --* 

            The type of trigger that this is.

            
          

          - **State** *(string) --* 

            The current state of the trigger.

            
          

          - **Description** *(string) --* 

            A description of this trigger.

            
          

          - **Schedule** *(string) --* 

            A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .

            
          

          - **Actions** *(list) --* 

            The actions initiated by this trigger.

            
            

            - *(dict) --* 

              Defines an action to be initiated by a trigger.

              
              

              - **JobName** *(string) --* 

                The name of a job to be executed.

                
              

              - **Arguments** *(dict) --* 

                Arguments to be passed to the job.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
        
          

          - **Predicate** *(dict) --* 

            The predicate of this trigger.

            
            

            - **Logical** *(string) --* 

              Currently "OR" is not supported.

              
            

            - **Conditions** *(list) --* 

              A list of the conditions that determine when the trigger will fire.

              
              

              - *(dict) --* 

                Defines a condition under which a trigger fires.

                
                

                - **LogicalOperator** *(string) --* 

                  A logical operator.

                  
                

                - **JobName** *(string) --* 

                  The name of the job in question.

                  
                

                - **State** *(string) --* 

                  The condition state.

                  
            
          
        
      
    

  .. py:method:: update_user_defined_function(**kwargs)

    

    Updates an existing function definition in the Data Catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateUserDefinedFunction>`_    


    **Request Syntax** 
    ::

      response = client.update_user_defined_function(
          CatalogId='string',
          DatabaseName='string',
          FunctionName='string',
          FunctionInput={
              'FunctionName': 'string',
              'ClassName': 'string',
              'OwnerName': 'string',
              'OwnerType': 'USER'|'ROLE'|'GROUP',
              'ResourceUris': [
                  {
                      'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                      'Uri': 'string'
                  },
              ]
          }
      )
    :type CatalogId: string
    :param CatalogId: 

      The ID of the Data Catalog where the function to be updated is located. If none is supplied, the AWS account ID is used by default.

      

    
    :type DatabaseName: string
    :param DatabaseName: **[REQUIRED]** 

      The name of the catalog database where the function to be updated is located.

      

    
    :type FunctionName: string
    :param FunctionName: **[REQUIRED]** 

      The name of the function.

      

    
    :type FunctionInput: dict
    :param FunctionInput: **[REQUIRED]** 

      A ``FunctionInput`` object that re-defines the function in the Data Catalog.

      

    
      - **FunctionName** *(string) --* 

        The name of the function.

        

      
      - **ClassName** *(string) --* 

        The Java class that contains the function code.

        

      
      - **OwnerName** *(string) --* 

        The owner of the function.

        

      
      - **OwnerType** *(string) --* 

        The owner type.

        

      
      - **ResourceUris** *(list) --* 

        The resource URIs for the function.

        

      
        - *(dict) --* 

          URIs for function resources.

          

        
          - **ResourceType** *(string) --* 

            The type of the resource.

            

          
          - **Uri** *(string) --* 

            The URI for accessing the resource.

            

          
        
    
    
    
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
