

***
SMS
***

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: SMS.Client

  A low-level client representing AWS Server Migration Service (SMS)::

    
    import boto3
    
    client = boto3.client('sms')

  
  These are the available methods:
  
  *   :py:meth:`~SMS.Client.can_paginate`

  
  *   :py:meth:`~SMS.Client.create_replication_job`

  
  *   :py:meth:`~SMS.Client.delete_replication_job`

  
  *   :py:meth:`~SMS.Client.delete_server_catalog`

  
  *   :py:meth:`~SMS.Client.disassociate_connector`

  
  *   :py:meth:`~SMS.Client.generate_presigned_url`

  
  *   :py:meth:`~SMS.Client.get_connectors`

  
  *   :py:meth:`~SMS.Client.get_paginator`

  
  *   :py:meth:`~SMS.Client.get_replication_jobs`

  
  *   :py:meth:`~SMS.Client.get_replication_runs`

  
  *   :py:meth:`~SMS.Client.get_servers`

  
  *   :py:meth:`~SMS.Client.get_waiter`

  
  *   :py:meth:`~SMS.Client.import_server_catalog`

  
  *   :py:meth:`~SMS.Client.start_on_demand_replication_run`

  
  *   :py:meth:`~SMS.Client.update_replication_job`

  

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


  .. py:method:: create_replication_job(**kwargs)

    The CreateReplicationJob API is used to create a ReplicationJob to replicate a server on AWS. Call this API to first create a ReplicationJob, which will then schedule periodic ReplicationRuns to replicate your server to AWS. Each ReplicationRun will result in the creation of an AWS AMI.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/CreateReplicationJob>`_    


    **Request Syntax** 
    ::

      response = client.create_replication_job(
          serverId='string',
          seedReplicationTime=datetime(2015, 1, 1),
          frequency=123,
          licenseType='AWS'|'BYOL',
          roleName='string',
          description='string'
      )
    :type serverId: string
    :param serverId: **[REQUIRED]** Unique Identifier for a server

    
    :type seedReplicationTime: datetime
    :param seedReplicationTime: **[REQUIRED]** Timestamp of an operation

    
    :type frequency: integer
    :param frequency: **[REQUIRED]** Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.

    
    :type licenseType: string
    :param licenseType: The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.

    
    :type roleName: string
    :param roleName: Name of service role in customer's account to be used by SMS service.

    
    :type description: string
    :param description: The description for a Replication Job/Run.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'replicationJobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
    

  .. py:method:: delete_replication_job(**kwargs)

    The DeleteReplicationJob API is used to delete a ReplicationJob, resulting in no further ReplicationRuns. This will delete the contents of the S3 bucket used to store SMS artifacts, but will not delete any AMIs created by the SMS service.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteReplicationJob>`_    


    **Request Syntax** 
    ::

      response = client.delete_replication_job(
          replicationJobId='string'
      )
    :type replicationJobId: string
    :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_server_catalog()

    The DeleteServerCatalog API clears all servers from your server catalog. This means that these servers will no longer be accessible to the Server Migration Service.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteServerCatalog>`_    


    **Request Syntax** 
    ::

      response = client.delete_server_catalog()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: disassociate_connector(**kwargs)

    The DisassociateConnector API will disassociate a connector from the Server Migration Service, rendering it unavailable to support replication jobs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DisassociateConnector>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_connector(
          connectorId='string'
      )
    :type connectorId: string
    :param connectorId: **[REQUIRED]** Unique Identifier for Connector

    
    
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


  .. py:method:: get_connectors(**kwargs)

    The GetConnectors API returns a list of connectors that are registered with the Server Migration Service.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetConnectors>`_    


    **Request Syntax** 
    ::

      response = client.get_connectors(
          nextToken='string',
          maxResults=123
      )
    :type nextToken: string
    :param nextToken: Pagination token to pass as input to API call

    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'connectorList': [
                {
                    'connectorId': 'string',
                    'version': 'string',
                    'status': 'HEALTHY'|'UNHEALTHY',
                    'capabilityList': [
                        'VSPHERE',
                    ],
                    'vmManagerName': 'string',
                    'vmManagerType': 'VSPHERE',
                    'vmManagerId': 'string',
                    'ipAddress': 'string',
                    'macAddress': 'string',
                    'associatedOn': datetime(2015, 1, 1)
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **connectorList** *(list) --* List of connectors
          

          - *(dict) --* Object representing a Connector
            

            - **connectorId** *(string) --* Unique Identifier for Connector
            

            - **version** *(string) --* Connector version string
            

            - **status** *(string) --* Status of on-premise Connector
            

            - **capabilityList** *(list) --* List of Connector Capabilities
              

              - *(string) --* Capabilities for a Connector
          
            

            - **vmManagerName** *(string) --* VM Manager Name
            

            - **vmManagerType** *(string) --* VM Management Product
            

            - **vmManagerId** *(string) --* Unique Identifier for VM Manager
            

            - **ipAddress** *(string) --* Internet Protocol (IP) Address
            

            - **macAddress** *(string) --* Hardware (MAC) address
            

            - **associatedOn** *(datetime) --* Timestamp of an operation
        
      
        

        - **nextToken** *(string) --* Pagination token to pass as input to API call
    

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


  .. py:method:: get_replication_jobs(**kwargs)

    The GetReplicationJobs API will return all of your ReplicationJobs and their details. This API returns a paginated list, that may be consecutively called with nextToken to retrieve all ReplicationJobs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationJobs>`_    


    **Request Syntax** 
    ::

      response = client.get_replication_jobs(
          replicationJobId='string',
          nextToken='string',
          maxResults=123
      )
    :type replicationJobId: string
    :param replicationJobId: The unique identifier for a Replication Job.

    
    :type nextToken: string
    :param nextToken: Pagination token to pass as input to API call

    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'replicationJobList': [
                {
                    'replicationJobId': 'string',
                    'serverId': 'string',
                    'serverType': 'VIRTUAL_MACHINE',
                    'vmServer': {
                        'vmServerAddress': {
                            'vmManagerId': 'string',
                            'vmId': 'string'
                        },
                        'vmName': 'string',
                        'vmManagerName': 'string',
                        'vmManagerType': 'VSPHERE',
                        'vmPath': 'string'
                    },
                    'seedReplicationTime': datetime(2015, 1, 1),
                    'frequency': 123,
                    'nextReplicationRunStartTime': datetime(2015, 1, 1),
                    'licenseType': 'AWS'|'BYOL',
                    'roleName': 'string',
                    'latestAmiId': 'string',
                    'state': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                    'statusMessage': 'string',
                    'description': 'string',
                    'replicationRunList': [
                        {
                            'replicationRunId': 'string',
                            'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                            'type': 'ON_DEMAND'|'AUTOMATIC',
                            'statusMessage': 'string',
                            'amiId': 'string',
                            'scheduledStartTime': datetime(2015, 1, 1),
                            'completedTime': datetime(2015, 1, 1),
                            'description': 'string'
                        },
                    ]
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **replicationJobList** *(list) --* List of Replication Jobs
          

          - *(dict) --* Object representing a Replication Job
            

            - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
            

            - **serverId** *(string) --* Unique Identifier for a server
            

            - **serverType** *(string) --* Type of server.
            

            - **vmServer** *(dict) --* Object representing a VM server
              

              - **vmServerAddress** *(dict) --* Object representing a server's location
                

                - **vmManagerId** *(string) --* Unique Identifier for VM Manager
                

                - **vmId** *(string) --* Unique Identifier for a VM
            
              

              - **vmName** *(string) --* Name of Virtual Machine
              

              - **vmManagerName** *(string) --* VM Manager Name
              

              - **vmManagerType** *(string) --* VM Management Product
              

              - **vmPath** *(string) --* Path to VM
          
            

            - **seedReplicationTime** *(datetime) --* Timestamp of an operation
            

            - **frequency** *(integer) --* Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
            

            - **nextReplicationRunStartTime** *(datetime) --* Timestamp of an operation
            

            - **licenseType** *(string) --* The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
            

            - **roleName** *(string) --* Name of service role in customer's account to be used by SMS service.
            

            - **latestAmiId** *(string) --* The AMI id for the image resulting from a Replication Run.
            

            - **state** *(string) --* Current state of Replication Job
            

            - **statusMessage** *(string) --* String describing current status of Replication Job
            

            - **description** *(string) --* The description for a Replication Job/Run.
            

            - **replicationRunList** *(list) --* List of Replication Runs
              

              - *(dict) --* Object representing a Replication Run
                

                - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
                

                - **state** *(string) --* Current state of Replication Run
                

                - **type** *(string) --* Type of Replication Run
                

                - **statusMessage** *(string) --* String describing current status of Replication Run
                

                - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
                

                - **scheduledStartTime** *(datetime) --* Timestamp of an operation
                

                - **completedTime** *(datetime) --* Timestamp of an operation
                

                - **description** *(string) --* The description for a Replication Job/Run.
            
          
        
      
        

        - **nextToken** *(string) --* Pagination token to pass as input to API call
    

  .. py:method:: get_replication_runs(**kwargs)

    The GetReplicationRuns API will return all ReplicationRuns for a given ReplicationJob. This API returns a paginated list, that may be consecutively called with nextToken to retrieve all ReplicationRuns for a ReplicationJob.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationRuns>`_    


    **Request Syntax** 
    ::

      response = client.get_replication_runs(
          replicationJobId='string',
          nextToken='string',
          maxResults=123
      )
    :type replicationJobId: string
    :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.

    
    :type nextToken: string
    :param nextToken: Pagination token to pass as input to API call

    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'replicationJob': {
                'replicationJobId': 'string',
                'serverId': 'string',
                'serverType': 'VIRTUAL_MACHINE',
                'vmServer': {
                    'vmServerAddress': {
                        'vmManagerId': 'string',
                        'vmId': 'string'
                    },
                    'vmName': 'string',
                    'vmManagerName': 'string',
                    'vmManagerType': 'VSPHERE',
                    'vmPath': 'string'
                },
                'seedReplicationTime': datetime(2015, 1, 1),
                'frequency': 123,
                'nextReplicationRunStartTime': datetime(2015, 1, 1),
                'licenseType': 'AWS'|'BYOL',
                'roleName': 'string',
                'latestAmiId': 'string',
                'state': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                'statusMessage': 'string',
                'description': 'string',
                'replicationRunList': [
                    {
                        'replicationRunId': 'string',
                        'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                        'type': 'ON_DEMAND'|'AUTOMATIC',
                        'statusMessage': 'string',
                        'amiId': 'string',
                        'scheduledStartTime': datetime(2015, 1, 1),
                        'completedTime': datetime(2015, 1, 1),
                        'description': 'string'
                    },
                ]
            },
            'replicationRunList': [
                {
                    'replicationRunId': 'string',
                    'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                    'type': 'ON_DEMAND'|'AUTOMATIC',
                    'statusMessage': 'string',
                    'amiId': 'string',
                    'scheduledStartTime': datetime(2015, 1, 1),
                    'completedTime': datetime(2015, 1, 1),
                    'description': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **replicationJob** *(dict) --* Object representing a Replication Job
          

          - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
          

          - **serverId** *(string) --* Unique Identifier for a server
          

          - **serverType** *(string) --* Type of server.
          

          - **vmServer** *(dict) --* Object representing a VM server
            

            - **vmServerAddress** *(dict) --* Object representing a server's location
              

              - **vmManagerId** *(string) --* Unique Identifier for VM Manager
              

              - **vmId** *(string) --* Unique Identifier for a VM
          
            

            - **vmName** *(string) --* Name of Virtual Machine
            

            - **vmManagerName** *(string) --* VM Manager Name
            

            - **vmManagerType** *(string) --* VM Management Product
            

            - **vmPath** *(string) --* Path to VM
        
          

          - **seedReplicationTime** *(datetime) --* Timestamp of an operation
          

          - **frequency** *(integer) --* Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
          

          - **nextReplicationRunStartTime** *(datetime) --* Timestamp of an operation
          

          - **licenseType** *(string) --* The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
          

          - **roleName** *(string) --* Name of service role in customer's account to be used by SMS service.
          

          - **latestAmiId** *(string) --* The AMI id for the image resulting from a Replication Run.
          

          - **state** *(string) --* Current state of Replication Job
          

          - **statusMessage** *(string) --* String describing current status of Replication Job
          

          - **description** *(string) --* The description for a Replication Job/Run.
          

          - **replicationRunList** *(list) --* List of Replication Runs
            

            - *(dict) --* Object representing a Replication Run
              

              - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
              

              - **state** *(string) --* Current state of Replication Run
              

              - **type** *(string) --* Type of Replication Run
              

              - **statusMessage** *(string) --* String describing current status of Replication Run
              

              - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
              

              - **scheduledStartTime** *(datetime) --* Timestamp of an operation
              

              - **completedTime** *(datetime) --* Timestamp of an operation
              

              - **description** *(string) --* The description for a Replication Job/Run.
          
        
      
        

        - **replicationRunList** *(list) --* List of Replication Runs
          

          - *(dict) --* Object representing a Replication Run
            

            - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
            

            - **state** *(string) --* Current state of Replication Run
            

            - **type** *(string) --* Type of Replication Run
            

            - **statusMessage** *(string) --* String describing current status of Replication Run
            

            - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
            

            - **scheduledStartTime** *(datetime) --* Timestamp of an operation
            

            - **completedTime** *(datetime) --* Timestamp of an operation
            

            - **description** *(string) --* The description for a Replication Job/Run.
        
      
        

        - **nextToken** *(string) --* Pagination token to pass as input to API call
    

  .. py:method:: get_servers(**kwargs)

    The GetServers API returns a list of all servers in your server catalog. For this call to succeed, you must previously have called ImportServerCatalog.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetServers>`_    


    **Request Syntax** 
    ::

      response = client.get_servers(
          nextToken='string',
          maxResults=123
      )
    :type nextToken: string
    :param nextToken: Pagination token to pass as input to API call

    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'lastModifiedOn': datetime(2015, 1, 1),
            'serverCatalogStatus': 'NOT_IMPORTED'|'IMPORTING'|'AVAILABLE'|'DELETED'|'EXPIRED',
            'serverList': [
                {
                    'serverId': 'string',
                    'serverType': 'VIRTUAL_MACHINE',
                    'vmServer': {
                        'vmServerAddress': {
                            'vmManagerId': 'string',
                            'vmId': 'string'
                        },
                        'vmName': 'string',
                        'vmManagerName': 'string',
                        'vmManagerType': 'VSPHERE',
                        'vmPath': 'string'
                    },
                    'replicationJobId': 'string',
                    'replicationJobTerminated': True|False
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **lastModifiedOn** *(datetime) --* Timestamp of an operation
        

        - **serverCatalogStatus** *(string) --* Status of Server catalog
        

        - **serverList** *(list) --* List of servers from catalog
          

          - *(dict) --* Object representing a server
            

            - **serverId** *(string) --* Unique Identifier for a server
            

            - **serverType** *(string) --* Type of server.
            

            - **vmServer** *(dict) --* Object representing a VM server
              

              - **vmServerAddress** *(dict) --* Object representing a server's location
                

                - **vmManagerId** *(string) --* Unique Identifier for VM Manager
                

                - **vmId** *(string) --* Unique Identifier for a VM
            
              

              - **vmName** *(string) --* Name of Virtual Machine
              

              - **vmManagerName** *(string) --* VM Manager Name
              

              - **vmManagerType** *(string) --* VM Management Product
              

              - **vmPath** *(string) --* Path to VM
          
            

            - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
            

            - **replicationJobTerminated** *(boolean) --* An indicator of the Replication Job being deleted or failed.
        
      
        

        - **nextToken** *(string) --* Pagination token to pass as input to API call
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: import_server_catalog()

    The ImportServerCatalog API is used to gather the complete list of on-premises servers on your premises. This API call requires connectors to be installed and monitoring all servers you would like imported. This API call returns immediately, but may take some time to retrieve all of the servers.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/ImportServerCatalog>`_    


    **Request Syntax** 
    ::

      response = client.import_server_catalog()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: start_on_demand_replication_run(**kwargs)

    The StartOnDemandReplicationRun API is used to start a ReplicationRun on demand (in addition to those that are scheduled based on your frequency). This ReplicationRun will start immediately. StartOnDemandReplicationRun is subject to limits on how many on demand ReplicationRuns you may call per 24-hour period.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/StartOnDemandReplicationRun>`_    


    **Request Syntax** 
    ::

      response = client.start_on_demand_replication_run(
          replicationJobId='string',
          description='string'
      )
    :type replicationJobId: string
    :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.

    
    :type description: string
    :param description: The description for a Replication Job/Run.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'replicationRunId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
    

  .. py:method:: update_replication_job(**kwargs)

    The UpdateReplicationJob API is used to change the settings of your existing ReplicationJob created using CreateReplicationJob. Calling this API will affect the next scheduled ReplicationRun.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/UpdateReplicationJob>`_    


    **Request Syntax** 
    ::

      response = client.update_replication_job(
          replicationJobId='string',
          frequency=123,
          nextReplicationRunStartTime=datetime(2015, 1, 1),
          licenseType='AWS'|'BYOL',
          roleName='string',
          description='string'
      )
    :type replicationJobId: string
    :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.

    
    :type frequency: integer
    :param frequency: Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.

    
    :type nextReplicationRunStartTime: datetime
    :param nextReplicationRunStartTime: Timestamp of an operation

    
    :type licenseType: string
    :param licenseType: The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.

    
    :type roleName: string
    :param roleName: Name of service role in customer's account to be used by SMS service.

    
    :type description: string
    :param description: The description for a Replication Job/Run.

    
    
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

* :py:class:`SMS.Paginator.GetConnectors`


* :py:class:`SMS.Paginator.GetReplicationJobs`


* :py:class:`SMS.Paginator.GetReplicationRuns`


* :py:class:`SMS.Paginator.GetServers`



.. py:class:: SMS.Paginator.GetConnectors

  ::

    
    paginator = client.get_paginator('get_connectors')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.get_connectors`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetConnectors>`_    


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
            'connectorList': [
                {
                    'connectorId': 'string',
                    'version': 'string',
                    'status': 'HEALTHY'|'UNHEALTHY',
                    'capabilityList': [
                        'VSPHERE',
                    ],
                    'vmManagerName': 'string',
                    'vmManagerType': 'VSPHERE',
                    'vmManagerId': 'string',
                    'ipAddress': 'string',
                    'macAddress': 'string',
                    'associatedOn': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **connectorList** *(list) --* List of connectors
          

          - *(dict) --* Object representing a Connector
            

            - **connectorId** *(string) --* Unique Identifier for Connector
            

            - **version** *(string) --* Connector version string
            

            - **status** *(string) --* Status of on-premise Connector
            

            - **capabilityList** *(list) --* List of Connector Capabilities
              

              - *(string) --* Capabilities for a Connector
          
            

            - **vmManagerName** *(string) --* VM Manager Name
            

            - **vmManagerType** *(string) --* VM Management Product
            

            - **vmManagerId** *(string) --* Unique Identifier for VM Manager
            

            - **ipAddress** *(string) --* Internet Protocol (IP) Address
            

            - **macAddress** *(string) --* Hardware (MAC) address
            

            - **associatedOn** *(datetime) --* Timestamp of an operation
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: SMS.Paginator.GetReplicationJobs

  ::

    
    paginator = client.get_paginator('get_replication_jobs')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.get_replication_jobs`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationJobs>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          replicationJobId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type replicationJobId: string
    :param replicationJobId: The unique identifier for a Replication Job.

    
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
            'replicationJobList': [
                {
                    'replicationJobId': 'string',
                    'serverId': 'string',
                    'serverType': 'VIRTUAL_MACHINE',
                    'vmServer': {
                        'vmServerAddress': {
                            'vmManagerId': 'string',
                            'vmId': 'string'
                        },
                        'vmName': 'string',
                        'vmManagerName': 'string',
                        'vmManagerType': 'VSPHERE',
                        'vmPath': 'string'
                    },
                    'seedReplicationTime': datetime(2015, 1, 1),
                    'frequency': 123,
                    'nextReplicationRunStartTime': datetime(2015, 1, 1),
                    'licenseType': 'AWS'|'BYOL',
                    'roleName': 'string',
                    'latestAmiId': 'string',
                    'state': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                    'statusMessage': 'string',
                    'description': 'string',
                    'replicationRunList': [
                        {
                            'replicationRunId': 'string',
                            'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                            'type': 'ON_DEMAND'|'AUTOMATIC',
                            'statusMessage': 'string',
                            'amiId': 'string',
                            'scheduledStartTime': datetime(2015, 1, 1),
                            'completedTime': datetime(2015, 1, 1),
                            'description': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **replicationJobList** *(list) --* List of Replication Jobs
          

          - *(dict) --* Object representing a Replication Job
            

            - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
            

            - **serverId** *(string) --* Unique Identifier for a server
            

            - **serverType** *(string) --* Type of server.
            

            - **vmServer** *(dict) --* Object representing a VM server
              

              - **vmServerAddress** *(dict) --* Object representing a server's location
                

                - **vmManagerId** *(string) --* Unique Identifier for VM Manager
                

                - **vmId** *(string) --* Unique Identifier for a VM
            
              

              - **vmName** *(string) --* Name of Virtual Machine
              

              - **vmManagerName** *(string) --* VM Manager Name
              

              - **vmManagerType** *(string) --* VM Management Product
              

              - **vmPath** *(string) --* Path to VM
          
            

            - **seedReplicationTime** *(datetime) --* Timestamp of an operation
            

            - **frequency** *(integer) --* Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
            

            - **nextReplicationRunStartTime** *(datetime) --* Timestamp of an operation
            

            - **licenseType** *(string) --* The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
            

            - **roleName** *(string) --* Name of service role in customer's account to be used by SMS service.
            

            - **latestAmiId** *(string) --* The AMI id for the image resulting from a Replication Run.
            

            - **state** *(string) --* Current state of Replication Job
            

            - **statusMessage** *(string) --* String describing current status of Replication Job
            

            - **description** *(string) --* The description for a Replication Job/Run.
            

            - **replicationRunList** *(list) --* List of Replication Runs
              

              - *(dict) --* Object representing a Replication Run
                

                - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
                

                - **state** *(string) --* Current state of Replication Run
                

                - **type** *(string) --* Type of Replication Run
                

                - **statusMessage** *(string) --* String describing current status of Replication Run
                

                - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
                

                - **scheduledStartTime** *(datetime) --* Timestamp of an operation
                

                - **completedTime** *(datetime) --* Timestamp of an operation
                

                - **description** *(string) --* The description for a Replication Job/Run.
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: SMS.Paginator.GetReplicationRuns

  ::

    
    paginator = client.get_paginator('get_replication_runs')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.get_replication_runs`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationRuns>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          replicationJobId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type replicationJobId: string
    :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.

    
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
            'replicationJob': {
                'replicationJobId': 'string',
                'serverId': 'string',
                'serverType': 'VIRTUAL_MACHINE',
                'vmServer': {
                    'vmServerAddress': {
                        'vmManagerId': 'string',
                        'vmId': 'string'
                    },
                    'vmName': 'string',
                    'vmManagerName': 'string',
                    'vmManagerType': 'VSPHERE',
                    'vmPath': 'string'
                },
                'seedReplicationTime': datetime(2015, 1, 1),
                'frequency': 123,
                'nextReplicationRunStartTime': datetime(2015, 1, 1),
                'licenseType': 'AWS'|'BYOL',
                'roleName': 'string',
                'latestAmiId': 'string',
                'state': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                'statusMessage': 'string',
                'description': 'string',
                'replicationRunList': [
                    {
                        'replicationRunId': 'string',
                        'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                        'type': 'ON_DEMAND'|'AUTOMATIC',
                        'statusMessage': 'string',
                        'amiId': 'string',
                        'scheduledStartTime': datetime(2015, 1, 1),
                        'completedTime': datetime(2015, 1, 1),
                        'description': 'string'
                    },
                ]
            },
            'replicationRunList': [
                {
                    'replicationRunId': 'string',
                    'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                    'type': 'ON_DEMAND'|'AUTOMATIC',
                    'statusMessage': 'string',
                    'amiId': 'string',
                    'scheduledStartTime': datetime(2015, 1, 1),
                    'completedTime': datetime(2015, 1, 1),
                    'description': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **replicationJob** *(dict) --* Object representing a Replication Job
          

          - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
          

          - **serverId** *(string) --* Unique Identifier for a server
          

          - **serverType** *(string) --* Type of server.
          

          - **vmServer** *(dict) --* Object representing a VM server
            

            - **vmServerAddress** *(dict) --* Object representing a server's location
              

              - **vmManagerId** *(string) --* Unique Identifier for VM Manager
              

              - **vmId** *(string) --* Unique Identifier for a VM
          
            

            - **vmName** *(string) --* Name of Virtual Machine
            

            - **vmManagerName** *(string) --* VM Manager Name
            

            - **vmManagerType** *(string) --* VM Management Product
            

            - **vmPath** *(string) --* Path to VM
        
          

          - **seedReplicationTime** *(datetime) --* Timestamp of an operation
          

          - **frequency** *(integer) --* Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
          

          - **nextReplicationRunStartTime** *(datetime) --* Timestamp of an operation
          

          - **licenseType** *(string) --* The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
          

          - **roleName** *(string) --* Name of service role in customer's account to be used by SMS service.
          

          - **latestAmiId** *(string) --* The AMI id for the image resulting from a Replication Run.
          

          - **state** *(string) --* Current state of Replication Job
          

          - **statusMessage** *(string) --* String describing current status of Replication Job
          

          - **description** *(string) --* The description for a Replication Job/Run.
          

          - **replicationRunList** *(list) --* List of Replication Runs
            

            - *(dict) --* Object representing a Replication Run
              

              - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
              

              - **state** *(string) --* Current state of Replication Run
              

              - **type** *(string) --* Type of Replication Run
              

              - **statusMessage** *(string) --* String describing current status of Replication Run
              

              - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
              

              - **scheduledStartTime** *(datetime) --* Timestamp of an operation
              

              - **completedTime** *(datetime) --* Timestamp of an operation
              

              - **description** *(string) --* The description for a Replication Job/Run.
          
        
      
        

        - **replicationRunList** *(list) --* List of Replication Runs
          

          - *(dict) --* Object representing a Replication Run
            

            - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
            

            - **state** *(string) --* Current state of Replication Run
            

            - **type** *(string) --* Type of Replication Run
            

            - **statusMessage** *(string) --* String describing current status of Replication Run
            

            - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
            

            - **scheduledStartTime** *(datetime) --* Timestamp of an operation
            

            - **completedTime** *(datetime) --* Timestamp of an operation
            

            - **description** *(string) --* The description for a Replication Job/Run.
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: SMS.Paginator.GetServers

  ::

    
    paginator = client.get_paginator('get_servers')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.get_servers`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetServers>`_    


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
            'lastModifiedOn': datetime(2015, 1, 1),
            'serverCatalogStatus': 'NOT_IMPORTED'|'IMPORTING'|'AVAILABLE'|'DELETED'|'EXPIRED',
            'serverList': [
                {
                    'serverId': 'string',
                    'serverType': 'VIRTUAL_MACHINE',
                    'vmServer': {
                        'vmServerAddress': {
                            'vmManagerId': 'string',
                            'vmId': 'string'
                        },
                        'vmName': 'string',
                        'vmManagerName': 'string',
                        'vmManagerType': 'VSPHERE',
                        'vmPath': 'string'
                    },
                    'replicationJobId': 'string',
                    'replicationJobTerminated': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **lastModifiedOn** *(datetime) --* Timestamp of an operation
        

        - **serverCatalogStatus** *(string) --* Status of Server catalog
        

        - **serverList** *(list) --* List of servers from catalog
          

          - *(dict) --* Object representing a server
            

            - **serverId** *(string) --* Unique Identifier for a server
            

            - **serverType** *(string) --* Type of server.
            

            - **vmServer** *(dict) --* Object representing a VM server
              

              - **vmServerAddress** *(dict) --* Object representing a server's location
                

                - **vmManagerId** *(string) --* Unique Identifier for VM Manager
                

                - **vmId** *(string) --* Unique Identifier for a VM
            
              

              - **vmName** *(string) --* Name of Virtual Machine
              

              - **vmManagerName** *(string) --* VM Manager Name
              

              - **vmManagerType** *(string) --* VM Management Product
              

              - **vmPath** *(string) --* Path to VM
          
            

            - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
            

            - **replicationJobTerminated** *(boolean) --* An indicator of the Replication Job being deleted or failed.
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    