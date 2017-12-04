

***********
CognitoSync
***********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CognitoSync.Client

  A low-level client representing Amazon Cognito Sync::

    
    import boto3
    
    client = boto3.client('cognito-sync')

  
  These are the available methods:
  
  *   :py:meth:`~CognitoSync.Client.bulk_publish`

  
  *   :py:meth:`~CognitoSync.Client.can_paginate`

  
  *   :py:meth:`~CognitoSync.Client.delete_dataset`

  
  *   :py:meth:`~CognitoSync.Client.describe_dataset`

  
  *   :py:meth:`~CognitoSync.Client.describe_identity_pool_usage`

  
  *   :py:meth:`~CognitoSync.Client.describe_identity_usage`

  
  *   :py:meth:`~CognitoSync.Client.generate_presigned_url`

  
  *   :py:meth:`~CognitoSync.Client.get_bulk_publish_details`

  
  *   :py:meth:`~CognitoSync.Client.get_cognito_events`

  
  *   :py:meth:`~CognitoSync.Client.get_identity_pool_configuration`

  
  *   :py:meth:`~CognitoSync.Client.get_paginator`

  
  *   :py:meth:`~CognitoSync.Client.get_waiter`

  
  *   :py:meth:`~CognitoSync.Client.list_datasets`

  
  *   :py:meth:`~CognitoSync.Client.list_identity_pool_usage`

  
  *   :py:meth:`~CognitoSync.Client.list_records`

  
  *   :py:meth:`~CognitoSync.Client.register_device`

  
  *   :py:meth:`~CognitoSync.Client.set_cognito_events`

  
  *   :py:meth:`~CognitoSync.Client.set_identity_pool_configuration`

  
  *   :py:meth:`~CognitoSync.Client.subscribe_to_dataset`

  
  *   :py:meth:`~CognitoSync.Client.unsubscribe_from_dataset`

  
  *   :py:meth:`~CognitoSync.Client.update_records`

  

  .. py:method:: bulk_publish(**kwargs)

    

    Initiates a bulk publish of all existing datasets for an Identity Pool to the configured stream. Customers are limited to one successful bulk publish per 24 hours. Bulk publish is an asynchronous request, customers can see the status of the request via the GetBulkPublishDetails operation.

     

    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/BulkPublish>`_    


    **Request Syntax** 
    ::

      response = client.bulk_publish(
          IdentityPoolId='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityPoolId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The output for the BulkPublish operation.
        

        - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    

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


  .. py:method:: delete_dataset(**kwargs)

    

    Deletes the specific dataset. The dataset will be deleted permanently, and the action can't be undone. Datasets that this dataset was merged with will no longer report the merge. Any subsequent operation on this dataset will result in a ResourceNotFoundException.

     

    This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/DeleteDataset>`_    


    **Request Syntax** 
    ::

      response = client.delete_dataset(
          IdentityPoolId='string',
          IdentityId='string',
          DatasetName='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type DatasetName: string
    :param DatasetName: **[REQUIRED]** A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Dataset': {
                'IdentityId': 'string',
                'DatasetName': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'LastModifiedDate': datetime(2015, 1, 1),
                'LastModifiedBy': 'string',
                'DataStorage': 123,
                'NumRecords': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* Response to a successful DeleteDataset request.
        

        - **Dataset** *(dict) --* A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don't exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
          

          - **IdentityId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
          

          - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
          

          - **CreationDate** *(datetime) --* Date on which the dataset was created.
          

          - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.
          

          - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.
          

          - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.
          

          - **NumRecords** *(integer) --* Number of records in this dataset.
      
    

  .. py:method:: describe_dataset(**kwargs)

    

    Gets meta data about a dataset by identity and dataset name. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.

     

    This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/DescribeDataset>`_    


    **Request Syntax** 
    ::

      response = client.describe_dataset(
          IdentityPoolId='string',
          IdentityId='string',
          DatasetName='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type DatasetName: string
    :param DatasetName: **[REQUIRED]** A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Dataset': {
                'IdentityId': 'string',
                'DatasetName': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'LastModifiedDate': datetime(2015, 1, 1),
                'LastModifiedBy': 'string',
                'DataStorage': 123,
                'NumRecords': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* Response to a successful DescribeDataset request.
        

        - **Dataset** *(dict) --* Meta data for a collection of data for an identity. An identity can have multiple datasets. A dataset can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don't exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
          

          - **IdentityId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
          

          - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
          

          - **CreationDate** *(datetime) --* Date on which the dataset was created.
          

          - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.
          

          - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.
          

          - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.
          

          - **NumRecords** *(integer) --* Number of records in this dataset.
      
    

  .. py:method:: describe_identity_pool_usage(**kwargs)

    

    Gets usage details (for example, data storage) about a particular identity pool.

     

    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/DescribeIdentityPoolUsage>`_    


    **Request Syntax** 
    ::

      response = client.describe_identity_pool_usage(
          IdentityPoolId='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityPoolUsage': {
                'IdentityPoolId': 'string',
                'SyncSessionsCount': 123,
                'DataStorage': 123,
                'LastModifiedDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* Response to a successful DescribeIdentityPoolUsage request.
        

        - **IdentityPoolUsage** *(dict) --* Information about the usage of the identity pool.
          

          - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
          

          - **SyncSessionsCount** *(integer) --* Number of sync sessions for the identity pool.
          

          - **DataStorage** *(integer) --* Data storage information for the identity pool.
          

          - **LastModifiedDate** *(datetime) --* Date on which the identity pool was last modified.
      
    

  .. py:method:: describe_identity_usage(**kwargs)

    

    Gets usage information for an identity, including number of datasets and data usage.

     

    This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/DescribeIdentityUsage>`_    


    **Request Syntax** 
    ::

      response = client.describe_identity_usage(
          IdentityPoolId='string',
          IdentityId='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityUsage': {
                'IdentityId': 'string',
                'IdentityPoolId': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'DatasetCount': 123,
                'DataStorage': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* The response to a successful DescribeIdentityUsage request.
        

        - **IdentityUsage** *(dict) --* Usage information for the identity.
          

          - **IdentityId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
          

          - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
          

          - **LastModifiedDate** *(datetime) --* Date on which the identity was last modified.
          

          - **DatasetCount** *(integer) --* Number of datasets for the identity.
          

          - **DataStorage** *(integer) --* Total data storage for this identity.
      
    

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


  .. py:method:: get_bulk_publish_details(**kwargs)

    

    Get the status of the last BulkPublish operation for an identity pool.

     

    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/GetBulkPublishDetails>`_    


    **Request Syntax** 
    ::

      response = client.get_bulk_publish_details(
          IdentityPoolId='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityPoolId': 'string',
            'BulkPublishStartTime': datetime(2015, 1, 1),
            'BulkPublishCompleteTime': datetime(2015, 1, 1),
            'BulkPublishStatus': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'SUCCEEDED',
            'FailureMessage': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* The output for the GetBulkPublishDetails operation.
        

        - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        

        - **BulkPublishStartTime** *(datetime) --* The date/time at which the last bulk publish was initiated.
        

        - **BulkPublishCompleteTime** *(datetime) --* If BulkPublishStatus is SUCCEEDED, the time the last bulk publish operation completed.
        

        - **BulkPublishStatus** *(string) --* Status of the last bulk publish operation, valid values are: 

          NOT_STARTED - No bulk publish has been requested for this identity pool

           

          IN_PROGRESS - Data is being published to the configured stream

           

          SUCCEEDED - All data for the identity pool has been published to the configured stream

           

          FAILED - Some portion of the data has failed to publish, check FailureMessage for the cause.

          
        

        - **FailureMessage** *(string) --* If BulkPublishStatus is FAILED this field will contain the error message that caused the bulk publish to fail.
    

  .. py:method:: get_cognito_events(**kwargs)

    

    Gets the events and the corresponding Lambda functions associated with an identity pool.

     

    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/GetCognitoEvents>`_    


    **Request Syntax** 
    ::

      response = client.get_cognito_events(
          IdentityPoolId='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** 

      The Cognito Identity Pool ID for the request

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Events': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response from the GetCognitoEvents request

        
        

        - **Events** *(dict) --* 

          The Cognito Events returned from the GetCognitoEvents request

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: get_identity_pool_configuration(**kwargs)

    

    Gets the configuration settings of an identity pool.

     

    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/GetIdentityPoolConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.get_identity_pool_configuration(
          IdentityPoolId='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** 

      A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityPoolId': 'string',
            'PushSync': {
                'ApplicationArns': [
                    'string',
                ],
                'RoleArn': 'string'
            },
            'CognitoStreams': {
                'StreamName': 'string',
                'RoleArn': 'string',
                'StreamingStatus': 'ENABLED'|'DISABLED'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the GetIdentityPoolConfiguration operation.

        
        

        - **IdentityPoolId** *(string) --* 

          A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.

          
        

        - **PushSync** *(dict) --* 

          Options to apply to this identity pool for push synchronization.

          
          

          - **ApplicationArns** *(list) --* 

            List of SNS platform application ARNs that could be used by clients.

            
            

            - *(string) --* 
        
          

          - **RoleArn** *(string) --* 

            A role configured to allow Cognito to call SNS on behalf of the developer.

            
      
        

        - **CognitoStreams** *(dict) --* Options to apply to this identity pool for Amazon Cognito streams.
          

          - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.
          

          - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.
          

          - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are: 

            ENABLED - Streaming of updates to identity pool is enabled.

             

            DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.

            
      
    

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

        


  .. py:method:: list_datasets(**kwargs)

    

    Lists datasets for an identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.

     

    ListDatasets can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use the Cognito Identity credentials to make this API call.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/ListDatasets>`_    


    **Request Syntax** 
    ::

      response = client.list_datasets(
          IdentityPoolId='string',
          IdentityId='string',
          NextToken='string',
          MaxResults=123
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type NextToken: string
    :param NextToken: A pagination token for obtaining the next page of results.

    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Datasets': [
                {
                    'IdentityId': 'string',
                    'DatasetName': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'LastModifiedBy': 'string',
                    'DataStorage': 123,
                    'NumRecords': 123
                },
            ],
            'Count': 123,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Returned for a successful ListDatasets request.
        

        - **Datasets** *(list) --* A set of datasets.
          

          - *(dict) --* A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don't exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
            

            - **IdentityId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            

            - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
            

            - **CreationDate** *(datetime) --* Date on which the dataset was created.
            

            - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.
            

            - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.
            

            - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.
            

            - **NumRecords** *(integer) --* Number of records in this dataset.
        
      
        

        - **Count** *(integer) --* Number of datasets returned.
        

        - **NextToken** *(string) --* A pagination token for obtaining the next page of results.
    

  .. py:method:: list_identity_pool_usage(**kwargs)

    

    Gets a list of identity pools registered with Cognito.

     

    ListIdentityPoolUsage can only be called with developer credentials. You cannot make this API call with the temporary user credentials provided by Cognito Identity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/ListIdentityPoolUsage>`_    


    **Request Syntax** 
    ::

      response = client.list_identity_pool_usage(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: A pagination token for obtaining the next page of results.

    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityPoolUsages': [
                {
                    'IdentityPoolId': 'string',
                    'SyncSessionsCount': 123,
                    'DataStorage': 123,
                    'LastModifiedDate': datetime(2015, 1, 1)
                },
            ],
            'MaxResults': 123,
            'Count': 123,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Returned for a successful ListIdentityPoolUsage request.
        

        - **IdentityPoolUsages** *(list) --* Usage information for the identity pools.
          

          - *(dict) --* Usage information for the identity pool.
            

            - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            

            - **SyncSessionsCount** *(integer) --* Number of sync sessions for the identity pool.
            

            - **DataStorage** *(integer) --* Data storage information for the identity pool.
            

            - **LastModifiedDate** *(datetime) --* Date on which the identity pool was last modified.
        
      
        

        - **MaxResults** *(integer) --* The maximum number of results to be returned.
        

        - **Count** *(integer) --* Total number of identities for the identity pool.
        

        - **NextToken** *(string) --* A pagination token for obtaining the next page of results.
    

  .. py:method:: list_records(**kwargs)

    

    Gets paginated records, optionally changed after a particular sync count for a dataset and identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.

     

    ListRecords can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/ListRecords>`_    


    **Request Syntax** 
    ::

      response = client.list_records(
          IdentityPoolId='string',
          IdentityId='string',
          DatasetName='string',
          LastSyncCount=123,
          NextToken='string',
          MaxResults=123,
          SyncSessionToken='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type DatasetName: string
    :param DatasetName: **[REQUIRED]** A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).

    
    :type LastSyncCount: integer
    :param LastSyncCount: The last server sync count for this record.

    
    :type NextToken: string
    :param NextToken: A pagination token for obtaining the next page of results.

    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned.

    
    :type SyncSessionToken: string
    :param SyncSessionToken: A token containing a session ID, identity ID, and expiration.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Records': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'SyncCount': 123,
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'LastModifiedBy': 'string',
                    'DeviceLastModifiedDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string',
            'Count': 123,
            'DatasetSyncCount': 123,
            'LastModifiedBy': 'string',
            'MergedDatasetNames': [
                'string',
            ],
            'DatasetExists': True|False,
            'DatasetDeletedAfterRequestedSyncCount': True|False,
            'SyncSessionToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Returned for a successful ListRecordsRequest.
        

        - **Records** *(list) --* A list of all records.
          

          - *(dict) --* The basic data structure of a dataset.
            

            - **Key** *(string) --* The key for the record.
            

            - **Value** *(string) --* The value for the record.
            

            - **SyncCount** *(integer) --* The server sync count for this record.
            

            - **LastModifiedDate** *(datetime) --* The date on which the record was last modified.
            

            - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.
            

            - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
        
      
        

        - **NextToken** *(string) --* A pagination token for obtaining the next page of results.
        

        - **Count** *(integer) --* Total number of records.
        

        - **DatasetSyncCount** *(integer) --* Server sync count for this dataset.
        

        - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.
        

        - **MergedDatasetNames** *(list) --* Names of merged datasets.
          

          - *(string) --* 
      
        

        - **DatasetExists** *(boolean) --* Indicates whether the dataset exists.
        

        - **DatasetDeletedAfterRequestedSyncCount** *(boolean) --* A boolean value specifying whether to delete the dataset locally.
        

        - **SyncSessionToken** *(string) --* A token containing a session ID, identity ID, and expiration.
    

  .. py:method:: register_device(**kwargs)

    

    Registers a device to receive push sync notifications.

     

    This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/RegisterDevice>`_    


    **Request Syntax** 
    ::

      response = client.register_device(
          IdentityPoolId='string',
          IdentityId='string',
          Platform='APNS'|'APNS_SANDBOX'|'GCM'|'ADM',
          Token='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** 

      A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.

      

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** 

      The unique ID for this identity.

      

    
    :type Platform: string
    :param Platform: **[REQUIRED]** 

      The SNS platform type (e.g. GCM, SDM, APNS, APNS_SANDBOX).

      

    
    :type Token: string
    :param Token: **[REQUIRED]** 

      The push token.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeviceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Response to a RegisterDevice request.

        
        

        - **DeviceId** *(string) --* 

          The unique ID generated for this device by Cognito.

          
    

  .. py:method:: set_cognito_events(**kwargs)

    

    Sets the AWS Lambda function for a given event type for an identity pool. This request only updates the key/value pair specified. Other key/values pairs are not updated. To remove a key value pair, pass a empty value for the particular key.

     

    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/SetCognitoEvents>`_    


    **Request Syntax** 
    ::

      response = client.set_cognito_events(
          IdentityPoolId='string',
          Events={
              'string': 'string'
          }
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** 

      The Cognito Identity Pool to use when configuring Cognito Events

      

    
    :type Events: dict
    :param Events: **[REQUIRED]** 

      The events to configure

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :returns: None

  .. py:method:: set_identity_pool_configuration(**kwargs)

    

    Sets the necessary configuration for push sync.

     

    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/SetIdentityPoolConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.set_identity_pool_configuration(
          IdentityPoolId='string',
          PushSync={
              'ApplicationArns': [
                  'string',
              ],
              'RoleArn': 'string'
          },
          CognitoStreams={
              'StreamName': 'string',
              'RoleArn': 'string',
              'StreamingStatus': 'ENABLED'|'DISABLED'
          }
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** 

      A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify.

      

    
    :type PushSync: dict
    :param PushSync: 

      Options to apply to this identity pool for push synchronization.

      

    
      - **ApplicationArns** *(list) --* 

        List of SNS platform application ARNs that could be used by clients.

        

      
        - *(string) --* 

        
    
      - **RoleArn** *(string) --* 

        A role configured to allow Cognito to call SNS on behalf of the developer.

        

      
    
    :type CognitoStreams: dict
    :param CognitoStreams: Options to apply to this identity pool for Amazon Cognito streams.

    
      - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.

      
      - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.

      
      - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are: 

        ENABLED - Streaming of updates to identity pool is enabled.

         

        DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IdentityPoolId': 'string',
            'PushSync': {
                'ApplicationArns': [
                    'string',
                ],
                'RoleArn': 'string'
            },
            'CognitoStreams': {
                'StreamName': 'string',
                'RoleArn': 'string',
                'StreamingStatus': 'ENABLED'|'DISABLED'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the SetIdentityPoolConfiguration operation

        
        

        - **IdentityPoolId** *(string) --* 

          A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.

          
        

        - **PushSync** *(dict) --* 

          Options to apply to this identity pool for push synchronization.

          
          

          - **ApplicationArns** *(list) --* 

            List of SNS platform application ARNs that could be used by clients.

            
            

            - *(string) --* 
        
          

          - **RoleArn** *(string) --* 

            A role configured to allow Cognito to call SNS on behalf of the developer.

            
      
        

        - **CognitoStreams** *(dict) --* Options to apply to this identity pool for Amazon Cognito streams.
          

          - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.
          

          - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.
          

          - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are: 

            ENABLED - Streaming of updates to identity pool is enabled.

             

            DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.

            
      
    

  .. py:method:: subscribe_to_dataset(**kwargs)

    

    Subscribes to receive notifications when a dataset is modified by another device.

     

    This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/SubscribeToDataset>`_    


    **Request Syntax** 
    ::

      response = client.subscribe_to_dataset(
          IdentityPoolId='string',
          IdentityId='string',
          DatasetName='string',
          DeviceId='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** 

      A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs.

      

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** 

      Unique ID for this identity.

      

    
    :type DatasetName: string
    :param DatasetName: **[REQUIRED]** 

      The name of the dataset to subcribe to.

      

    
    :type DeviceId: string
    :param DeviceId: **[REQUIRED]** 

      The unique ID generated for this device by Cognito.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Response to a SubscribeToDataset request.

        
    

  .. py:method:: unsubscribe_from_dataset(**kwargs)

    

    Unsubscribes from receiving notifications when a dataset is modified by another device.

     

    This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/UnsubscribeFromDataset>`_    


    **Request Syntax** 
    ::

      response = client.unsubscribe_from_dataset(
          IdentityPoolId='string',
          IdentityId='string',
          DatasetName='string',
          DeviceId='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** 

      A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.

      

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** 

      Unique ID for this identity.

      

    
    :type DatasetName: string
    :param DatasetName: **[REQUIRED]** 

      The name of the dataset from which to unsubcribe.

      

    
    :type DeviceId: string
    :param DeviceId: **[REQUIRED]** 

      The unique ID generated for this device by Cognito.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Response to an UnsubscribeFromDataset request.

        
    

  .. py:method:: update_records(**kwargs)

    

    Posts updates to records and adds and deletes records for a dataset and user.

     

    The sync count in the record patch is your last known sync count for that record. The server will reject an UpdateRecords request with a ResourceConflictException if you try to patch a record with a new value but a stale sync count.

     

    For example, if the sync count on the server is 5 for a key called highScore and you try and submit a new highScore with sync count of 4, the request will be rejected. To obtain the current sync count for a record, call ListRecords. On a successful update of the record, the response returns the new sync count for that record. You should present that sync count the next time you try to update that same record. When the record does not exist, specify the sync count as 0.

     

    This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/UpdateRecords>`_    


    **Request Syntax** 
    ::

      response = client.update_records(
          IdentityPoolId='string',
          IdentityId='string',
          DatasetName='string',
          DeviceId='string',
          RecordPatches=[
              {
                  'Op': 'replace'|'remove',
                  'Key': 'string',
                  'Value': 'string',
                  'SyncCount': 123,
                  'DeviceLastModifiedDate': datetime(2015, 1, 1)
              },
          ],
          SyncSessionToken='string',
          ClientContext='string'
      )
    :type IdentityPoolId: string
    :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type IdentityId: string
    :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    
    :type DatasetName: string
    :param DatasetName: **[REQUIRED]** A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).

    
    :type DeviceId: string
    :param DeviceId: 

      The unique ID generated for this device by Cognito.

      

    
    :type RecordPatches: list
    :param RecordPatches: A list of patch operations.

    
      - *(dict) --* An update operation for a record.

      
        - **Op** *(string) --* **[REQUIRED]** An operation, either replace or remove.

        
        - **Key** *(string) --* **[REQUIRED]** The key associated with the record patch.

        
        - **Value** *(string) --* The value associated with the record patch.

        
        - **SyncCount** *(integer) --* **[REQUIRED]** Last known server sync count for this record. Set to 0 if unknown.

        
        - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.

        
      
  
    :type SyncSessionToken: string
    :param SyncSessionToken: **[REQUIRED]** The SyncSessionToken returned by a previous call to ListRecords for this dataset and identity.

    
    :type ClientContext: string
    :param ClientContext: Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Records': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'SyncCount': 123,
                    'LastModifiedDate': datetime(2015, 1, 1),
                    'LastModifiedBy': 'string',
                    'DeviceLastModifiedDate': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* Returned for a successful UpdateRecordsRequest.
        

        - **Records** *(list) --* A list of records that have been updated.
          

          - *(dict) --* The basic data structure of a dataset.
            

            - **Key** *(string) --* The key for the record.
            

            - **Value** *(string) --* The value for the record.
            

            - **SyncCount** *(integer) --* The server sync count for this record.
            

            - **LastModifiedDate** *(datetime) --* The date on which the record was last modified.
            

            - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.
            

            - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
        
      
    