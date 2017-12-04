

***************************
ApplicationDiscoveryService
***************************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ApplicationDiscoveryService.Client

  A low-level client representing AWS Application Discovery Service::

    
    import boto3
    
    client = boto3.client('discovery')

  
  These are the available methods:
  
  *   :py:meth:`~ApplicationDiscoveryService.Client.associate_configuration_items_to_application`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.can_paginate`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.create_application`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.create_tags`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.delete_applications`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.delete_tags`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.describe_agents`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.describe_configurations`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.describe_export_configurations`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.describe_export_tasks`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.describe_tags`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.disassociate_configuration_items_from_application`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.export_configurations`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.generate_presigned_url`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.get_discovery_summary`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.get_paginator`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.get_waiter`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.list_configurations`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.list_server_neighbors`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.start_data_collection_by_agent_ids`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.start_export_task`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.stop_data_collection_by_agent_ids`

  
  *   :py:meth:`~ApplicationDiscoveryService.Client.update_application`

  

  .. py:method:: associate_configuration_items_to_application(**kwargs)

    

    Associates one or more configuration items with an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/AssociateConfigurationItemsToApplication>`_    


    **Request Syntax** 
    ::

      response = client.associate_configuration_items_to_application(
          applicationConfigurationId='string',
          configurationIds=[
              'string',
          ]
      )
    :type applicationConfigurationId: string
    :param applicationConfigurationId: **[REQUIRED]** 

      The configuration ID of an application with which items are to be associated.

      

    
    :type configurationIds: list
    :param configurationIds: **[REQUIRED]** 

      The ID of each configuration item to be associated with an application.

      

    
      - *(string) --* 

      
  
    
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

    

    Creates an application with the given name and description.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/CreateApplication>`_    


    **Request Syntax** 
    ::

      response = client.create_application(
          name='string',
          description='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      Name of the application to be created.

      

    
    :type description: string
    :param description: 

      Description of the application to be created.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'configurationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **configurationId** *(string) --* 

          Configuration ID of an application to be created.

          
    

  .. py:method:: create_tags(**kwargs)

    

    Creates one or more tags for configuration items. Tags are metadata that help you categorize IT assets. This API accepts a list of multiple configuration items.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/CreateTags>`_    


    **Request Syntax** 
    ::

      response = client.create_tags(
          configurationIds=[
              'string',
          ],
          tags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type configurationIds: list
    :param configurationIds: **[REQUIRED]** 

      A list of configuration items that you want to tag.

      

    
      - *(string) --* 

      
  
    :type tags: list
    :param tags: **[REQUIRED]** 

      Tags that you want to associate with one or more configuration items. Specify the tags that you want to create in a *key* -*value* format. For example:

       

       ``{"key": "serverType", "value": "webServer"}``  

      

    
      - *(dict) --* 

        Metadata that help you categorize IT assets.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The type of tag on which to filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          A value for a tag key on which to filter.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_applications(**kwargs)

    

    Deletes a list of applications and their associations with configuration items.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DeleteApplications>`_    


    **Request Syntax** 
    ::

      response = client.delete_applications(
          configurationIds=[
              'string',
          ]
      )
    :type configurationIds: list
    :param configurationIds: **[REQUIRED]** 

      Configuration ID of an application to be deleted.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_tags(**kwargs)

    

    Deletes the association between configuration items and one or more tags. This API accepts a list of multiple configuration items.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DeleteTags>`_    


    **Request Syntax** 
    ::

      response = client.delete_tags(
          configurationIds=[
              'string',
          ],
          tags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type configurationIds: list
    :param configurationIds: **[REQUIRED]** 

      A list of configuration items with tags that you want to delete.

      

    
      - *(string) --* 

      
  
    :type tags: list
    :param tags: 

      Tags that you want to delete from one or more configuration items. Specify the tags that you want to delete in a *key* -*value* format. For example:

       

       ``{"key": "serverType", "value": "webServer"}``  

      

    
      - *(dict) --* 

        Metadata that help you categorize IT assets.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The type of tag on which to filter.

          

        
        - **value** *(string) --* **[REQUIRED]** 

          A value for a tag key on which to filter.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_agents(**kwargs)

    

    Lists agents or the Connector by ID or lists all agents/Connectors associated with your user account if you did not specify an ID.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeAgents>`_    


    **Request Syntax** 
    ::

      response = client.describe_agents(
          agentIds=[
              'string',
          ],
          filters=[
              {
                  'name': 'string',
                  'values': [
                      'string',
                  ],
                  'condition': 'string'
              },
          ],
          maxResults=123,
          nextToken='string'
      )
    :type agentIds: list
    :param agentIds: 

      The agent or the Connector IDs for which you want information. If you specify no IDs, the system returns information about all agents/Connectors associated with your AWS user account.

      

    
      - *(string) --* 

      
  
    :type filters: list
    :param filters: 

      You can filter the request using various logical operators and a *key* -*value* format. For example: 

       

       ``{"key": "collectionStatus", "value": "STARTED"}``  

      

    
      - *(dict) --* 

        A filter that can use conditional operators.

         

        For more information about filters, see `Querying Discovered Configuration Items <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html>`__ . 

        

      
        - **name** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **values** *(list) --* **[REQUIRED]** 

          A string value on which to filter. For example, if you choose the ``destinationServer.osVersion`` filter name, you could specify ``Ubuntu`` for the value.

          

        
          - *(string) --* 

          
      
        - **condition** *(string) --* **[REQUIRED]** 

          A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by *AND* . If you specify multiple values for a particular filter, the system differentiates the values using *OR* . Calling either *DescribeConfigurations* or *ListConfigurations* returns attributes of matching configuration items.

          

        
      
  
    :type maxResults: integer
    :param maxResults: 

      The total number of agents/Connectors to return in a single page of output. The maximum value is 100.

      

    
    :type nextToken: string
    :param nextToken: 

      Token to retrieve the next set of results. For example, if you previously specified 100 IDs for ``DescribeAgentsRequest$agentIds`` but set ``DescribeAgentsRequest$maxResults`` to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'agentsInfo': [
                {
                    'agentId': 'string',
                    'hostName': 'string',
                    'agentNetworkInfoList': [
                        {
                            'ipAddress': 'string',
                            'macAddress': 'string'
                        },
                    ],
                    'connectorId': 'string',
                    'version': 'string',
                    'health': 'HEALTHY'|'UNHEALTHY'|'RUNNING'|'UNKNOWN'|'BLACKLISTED'|'SHUTDOWN',
                    'lastHealthPingTime': 'string',
                    'collectionStatus': 'string',
                    'agentType': 'string',
                    'registeredTime': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **agentsInfo** *(list) --* 

          Lists agents or the Connector by ID or lists all agents/Connectors associated with your user account if you did not specify an agent/Connector ID. The output includes agent/Connector IDs, IP addresses, media access control (MAC) addresses, agent/Connector health, host name where the agent/Connector resides, and the version number of each agent/Connector.

          
          

          - *(dict) --* 

            Information about agents or connectors associated with the user’s AWS account. Information includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent or connector health, hostname where the agent or connector resides, and agent version for each agent.

            
            

            - **agentId** *(string) --* 

              The agent or connector ID.

              
            

            - **hostName** *(string) --* 

              The name of the host where the agent or connector resides. The host can be a server or virtual machine.

              
            

            - **agentNetworkInfoList** *(list) --* 

              Network details about the host where the agent or connector resides.

              
              

              - *(dict) --* 

                Network details about the host where the agent/connector resides.

                
                

                - **ipAddress** *(string) --* 

                  The IP address for the host where the agent/connector resides.

                  
                

                - **macAddress** *(string) --* 

                  The MAC address for the host where the agent/connector resides.

                  
            
          
            

            - **connectorId** *(string) --* 

              The ID of the connector.

              
            

            - **version** *(string) --* 

              The agent or connector version.

              
            

            - **health** *(string) --* 

              The health of the agent or connector.

              
            

            - **lastHealthPingTime** *(string) --* 

              Time since agent or connector health was reported.

              
            

            - **collectionStatus** *(string) --* 

              Status of the collection process for an agent or connector.

              
            

            - **agentType** *(string) --* 

              Type of agent.

              
            

            - **registeredTime** *(string) --* 

              Agent's first registration timestamp in UTC.

              
        
      
        

        - **nextToken** *(string) --* 

          Token to retrieve the next set of results. For example, if you specified 100 IDs for ``DescribeAgentsRequest$agentIds`` but set ``DescribeAgentsRequest$maxResults`` to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.

          
    

  .. py:method:: describe_configurations(**kwargs)

    

    Retrieves attributes for a list of configuration item IDs. All of the supplied IDs must be for the same asset type (server, application, process, or connection). Output fields are specific to the asset type selected. For example, the output for a *server* configuration item includes a list of attributes about the server, such as host name, operating system, and number of network cards.

     

    For a complete list of outputs for each asset type, see `Using the DescribeConfigurations Action <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html#DescribeConfigurations>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeConfigurations>`_    


    **Request Syntax** 
    ::

      response = client.describe_configurations(
          configurationIds=[
              'string',
          ]
      )
    :type configurationIds: list
    :param configurationIds: **[REQUIRED]** 

      One or more configuration IDs.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'configurations': [
                {
                    'string': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **configurations** *(list) --* 

          A key in the response map. The value is an array of data.

          
          

          - *(dict) --* 
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
    

  .. py:method:: describe_export_configurations(**kwargs)

    

    Deprecated. Use ``DescribeExportTasks`` instead.

     

    Retrieves the status of a given export process. You can retrieve status from a maximum of 100 processes.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeExportConfigurations>`_    


    **Request Syntax** 
    ::

      response = client.describe_export_configurations(
          exportIds=[
              'string',
          ],
          maxResults=123,
          nextToken='string'
      )
    :type exportIds: list
    :param exportIds: 

      A unique identifier that you can use to query the export status.

      

    
      - *(string) --* 

      
  
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results that you want to display as a part of the query.

      

    
    :type nextToken: string
    :param nextToken: 

      A token to get the next set of results. For example, if you specify 100 IDs for ``DescribeExportConfigurationsRequest$exportIds`` but set ``DescribeExportConfigurationsRequest$maxResults`` to 10, you get results in a set of 10. Use the token in the query to get the next set of 10.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'exportsInfo': [
                {
                    'exportId': 'string',
                    'exportStatus': 'FAILED'|'SUCCEEDED'|'IN_PROGRESS',
                    'statusMessage': 'string',
                    'configurationsDownloadUrl': 'string',
                    'exportRequestTime': datetime(2015, 1, 1),
                    'isTruncated': True|False,
                    'requestedStartTime': datetime(2015, 1, 1),
                    'requestedEndTime': datetime(2015, 1, 1)
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **exportsInfo** *(list) --* 

          Returns export details. When the status is complete, the response includes a URL for an Amazon S3 bucket where you can view the data in a CSV file.

          
          

          - *(dict) --* 

            Information regarding the export status of discovered data. The value is an array of objects.

            
            

            - **exportId** *(string) --* 

              A unique identifier used to query an export.

              
            

            - **exportStatus** *(string) --* 

              The status of the data export job.

              
            

            - **statusMessage** *(string) --* 

              A status message provided for API callers.

              
            

            - **configurationsDownloadUrl** *(string) --* 

              A URL for an Amazon S3 bucket where you can review the exported data. The URL is displayed only if the export succeeded.

              
            

            - **exportRequestTime** *(datetime) --* 

              The time that the data export was initiated.

              
            

            - **isTruncated** *(boolean) --* 

              If true, the export of agent information exceeded the size limit for a single export and the exported data is incomplete for the requested time range. To address this, select a smaller time range for the export by using ``startDate`` and ``endDate`` .

              
            

            - **requestedStartTime** *(datetime) --* 

              The value of ``startTime`` parameter in the ``StartExportTask`` request. If no ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

              
            

            - **requestedEndTime** *(datetime) --* 

              The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested, this result does not appear in ``ExportInfo`` .

              
        
      
        

        - **nextToken** *(string) --* 

          A token to get the next set of results. For example, if you specify 100 IDs for ``DescribeExportConfigurationsRequest$exportIds`` but set ``DescribeExportConfigurationsRequest$maxResults`` to 10, you get results in a set of 10. Use the token in the query to get the next set of 10.

          
    

  .. py:method:: describe_export_tasks(**kwargs)

    

    Retrieve status of one or more export tasks. You can retrieve the status of up to 100 export tasks.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeExportTasks>`_    


    **Request Syntax** 
    ::

      response = client.describe_export_tasks(
          exportIds=[
              'string',
          ],
          filters=[
              {
                  'name': 'string',
                  'values': [
                      'string',
                  ],
                  'condition': 'string'
              },
          ],
          maxResults=123,
          nextToken='string'
      )
    :type exportIds: list
    :param exportIds: 

      One or more unique identifiers used to query the status of an export request.

      

    
      - *(string) --* 

      
  
    :type filters: list
    :param filters: 

      One or more filters.

       

       
      * ``AgentId`` - ID of the agent whose collected data will be exported 
       

      

    
      - *(dict) --* 

        Used to select which agent's data is to be exported. A single agent ID may be selected for export using the `StartExportTask <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__ action.

        

      
        - **name** *(string) --* **[REQUIRED]** 

          A single ``ExportFilter`` name. Supported filters: ``agentId`` .

          

        
        - **values** *(list) --* **[REQUIRED]** 

          A single ``agentId`` for a Discovery Agent. An ``agentId`` can be found using the `DescribeAgents <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html>`__ action. Typically an ADS ``agentId`` is in the form ``o-0123456789abcdef0`` .

          

        
          - *(string) --* 

          
      
        - **condition** *(string) --* **[REQUIRED]** 

          Supported condition: ``EQUALS``  

          

        
      
  
    :type maxResults: integer
    :param maxResults: 

      The maximum number of volume results returned by ``DescribeExportTasks`` in paginated output. When this parameter is used, ``DescribeExportTasks`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element.

      

    
    :type nextToken: string
    :param nextToken: 

      The ``nextToken`` value returned from a previous paginated ``DescribeExportTasks`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is null when there are no more results to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'exportsInfo': [
                {
                    'exportId': 'string',
                    'exportStatus': 'FAILED'|'SUCCEEDED'|'IN_PROGRESS',
                    'statusMessage': 'string',
                    'configurationsDownloadUrl': 'string',
                    'exportRequestTime': datetime(2015, 1, 1),
                    'isTruncated': True|False,
                    'requestedStartTime': datetime(2015, 1, 1),
                    'requestedEndTime': datetime(2015, 1, 1)
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **exportsInfo** *(list) --* 

          Contains one or more sets of export request details. When the status of a request is ``SUCCEEDED`` , the response includes a URL for an Amazon S3 bucket where you can view the data in a CSV file.

          
          

          - *(dict) --* 

            Information regarding the export status of discovered data. The value is an array of objects.

            
            

            - **exportId** *(string) --* 

              A unique identifier used to query an export.

              
            

            - **exportStatus** *(string) --* 

              The status of the data export job.

              
            

            - **statusMessage** *(string) --* 

              A status message provided for API callers.

              
            

            - **configurationsDownloadUrl** *(string) --* 

              A URL for an Amazon S3 bucket where you can review the exported data. The URL is displayed only if the export succeeded.

              
            

            - **exportRequestTime** *(datetime) --* 

              The time that the data export was initiated.

              
            

            - **isTruncated** *(boolean) --* 

              If true, the export of agent information exceeded the size limit for a single export and the exported data is incomplete for the requested time range. To address this, select a smaller time range for the export by using ``startDate`` and ``endDate`` .

              
            

            - **requestedStartTime** *(datetime) --* 

              The value of ``startTime`` parameter in the ``StartExportTask`` request. If no ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

              
            

            - **requestedEndTime** *(datetime) --* 

              The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested, this result does not appear in ``ExportInfo`` .

              
        
      
        

        - **nextToken** *(string) --* 

          The ``nextToken`` value to include in a future ``DescribeExportTasks`` request. When the results of a ``DescribeExportTasks`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.

          
    

  .. py:method:: describe_tags(**kwargs)

    

    Retrieves a list of configuration items that are tagged with a specific tag. Or retrieves a list of all tags assigned to a specific configuration item.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeTags>`_    


    **Request Syntax** 
    ::

      response = client.describe_tags(
          filters=[
              {
                  'name': 'string',
                  'values': [
                      'string',
                  ]
              },
          ],
          maxResults=123,
          nextToken='string'
      )
    :type filters: list
    :param filters: 

      You can filter the list using a *key* -*value* format. You can separate these items by using logical operators. Allowed filters include ``tagKey`` , ``tagValue`` , and ``configurationId`` . 

      

    
      - *(dict) --* 

        The tag filter. Valid names are: ``tagKey`` , ``tagValue`` , ``configurationId`` .

        

      
        - **name** *(string) --* **[REQUIRED]** 

          A name of the tag filter.

          

        
        - **values** *(list) --* **[REQUIRED]** 

          Values for the tag filter.

          

        
          - *(string) --* 

          
      
      
  
    :type maxResults: integer
    :param maxResults: 

      The total number of items to return in a single page of output. The maximum value is 100.

      

    
    :type nextToken: string
    :param nextToken: 

      A token to start the list. Use this token to get the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tags': [
                {
                    'configurationType': 'SERVER'|'PROCESS'|'CONNECTION'|'APPLICATION',
                    'configurationId': 'string',
                    'key': 'string',
                    'value': 'string',
                    'timeOfCreation': datetime(2015, 1, 1)
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tags** *(list) --* 

          Depending on the input, this is a list of configuration items tagged with a specific tag, or a list of tags for a specific configuration item.

          
          

          - *(dict) --* 

            Tags for a configuration item. Tags are metadata that help you categorize IT assets.

            
            

            - **configurationType** *(string) --* 

              A type of IT asset to tag.

              
            

            - **configurationId** *(string) --* 

              The configuration ID for the item to tag. You can specify a list of keys and values.

              
            

            - **key** *(string) --* 

              A type of tag on which to filter. For example, *serverType* .

              
            

            - **value** *(string) --* 

              A value on which to filter. For example *key = serverType* and *value = web server* .

              
            

            - **timeOfCreation** *(datetime) --* 

              The time the configuration tag was created in Coordinated Universal Time (UTC).

              
        
      
        

        - **nextToken** *(string) --* 

          The call returns a token. Use this token to get the next set of results.

          
    

  .. py:method:: disassociate_configuration_items_from_application(**kwargs)

    

    Disassociates one or more configuration items from an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DisassociateConfigurationItemsFromApplication>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_configuration_items_from_application(
          applicationConfigurationId='string',
          configurationIds=[
              'string',
          ]
      )
    :type applicationConfigurationId: string
    :param applicationConfigurationId: **[REQUIRED]** 

      Configuration ID of an application from which each item is disassociated.

      

    
    :type configurationIds: list
    :param configurationIds: **[REQUIRED]** 

      Configuration ID of each item to be disassociated from an application.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: export_configurations()

    

    Deprecated. Use ``StartExportTask`` instead.

     

    Exports all discovered configuration data to an Amazon S3 bucket or an application that enables you to view and evaluate the data. Data includes tags and tag associations, processes, connections, servers, and system performance. This API returns an export ID that you can query using the *DescribeExportConfigurations* API. The system imposes a limit of two configuration exports in six hours.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/ExportConfigurations>`_    


    **Request Syntax** 

    ::

      response = client.export_configurations()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'exportId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **exportId** *(string) --* 

          A unique identifier that you can use to query the export status.

          
    

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


  .. py:method:: get_discovery_summary()

    

    Retrieves a short summary of discovered assets.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/GetDiscoverySummary>`_    


    **Request Syntax** 
    ::

      response = client.get_discovery_summary()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'servers': 123,
            'applications': 123,
            'serversMappedToApplications': 123,
            'serversMappedtoTags': 123,
            'agentSummary': {
                'activeAgents': 123,
                'healthyAgents': 123,
                'blackListedAgents': 123,
                'shutdownAgents': 123,
                'unhealthyAgents': 123,
                'totalAgents': 123,
                'unknownAgents': 123
            },
            'connectorSummary': {
                'activeConnectors': 123,
                'healthyConnectors': 123,
                'blackListedConnectors': 123,
                'shutdownConnectors': 123,
                'unhealthyConnectors': 123,
                'totalConnectors': 123,
                'unknownConnectors': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **servers** *(integer) --* 

          The number of servers discovered.

          
        

        - **applications** *(integer) --* 

          The number of applications discovered.

          
        

        - **serversMappedToApplications** *(integer) --* 

          The number of servers mapped to applications.

          
        

        - **serversMappedtoTags** *(integer) --* 

          The number of servers mapped to tags.

          
        

        - **agentSummary** *(dict) --* 

          Details about discovered agents, including agent status and health.

          
          

          - **activeAgents** *(integer) --* 

            Number of active discovery agents.

            
          

          - **healthyAgents** *(integer) --* 

            Number of healthy discovery agents

            
          

          - **blackListedAgents** *(integer) --* 

            Number of blacklisted discovery agents.

            
          

          - **shutdownAgents** *(integer) --* 

            Number of discovery agents with status SHUTDOWN.

            
          

          - **unhealthyAgents** *(integer) --* 

            Number of unhealthy discovery agents.

            
          

          - **totalAgents** *(integer) --* 

            Total number of discovery agents.

            
          

          - **unknownAgents** *(integer) --* 

            Number of unknown discovery agents.

            
      
        

        - **connectorSummary** *(dict) --* 

          Details about discovered connectors, including connector status and health.

          
          

          - **activeConnectors** *(integer) --* 

            Number of active discovery connectors.

            
          

          - **healthyConnectors** *(integer) --* 

            Number of healthy discovery connectors.

            
          

          - **blackListedConnectors** *(integer) --* 

            Number of blacklisted discovery connectors.

            
          

          - **shutdownConnectors** *(integer) --* 

            Number of discovery connectors with status SHUTDOWN,

            
          

          - **unhealthyConnectors** *(integer) --* 

            Number of unhealthy discovery connectors.

            
          

          - **totalConnectors** *(integer) --* 

            Total number of discovery connectors.

            
          

          - **unknownConnectors** *(integer) --* 

            Number of unknown discovery connectors.

            
      
    

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

        


  .. py:method:: list_configurations(**kwargs)

    

    Retrieves a list of configuration items according to criteria that you specify in a filter. The filter criteria identifies the relationship requirements.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/ListConfigurations>`_    


    **Request Syntax** 
    ::

      response = client.list_configurations(
          configurationType='SERVER'|'PROCESS'|'CONNECTION'|'APPLICATION',
          filters=[
              {
                  'name': 'string',
                  'values': [
                      'string',
                  ],
                  'condition': 'string'
              },
          ],
          maxResults=123,
          nextToken='string',
          orderBy=[
              {
                  'fieldName': 'string',
                  'sortOrder': 'ASC'|'DESC'
              },
          ]
      )
    :type configurationType: string
    :param configurationType: **[REQUIRED]** 

      A valid configuration identified by Application Discovery Service. 

      

    
    :type filters: list
    :param filters: 

      You can filter the request using various logical operators and a *key* -*value* format. For example: 

       

       ``{"key": "serverType", "value": "webServer"}``  

       

      For a complete list of filter options and guidance about using them with this action, see `Querying Discovered Configuration Items <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html#ListConfigurations>`__ . 

      

    
      - *(dict) --* 

        A filter that can use conditional operators.

         

        For more information about filters, see `Querying Discovered Configuration Items <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html>`__ . 

        

      
        - **name** *(string) --* **[REQUIRED]** 

          The name of the filter.

          

        
        - **values** *(list) --* **[REQUIRED]** 

          A string value on which to filter. For example, if you choose the ``destinationServer.osVersion`` filter name, you could specify ``Ubuntu`` for the value.

          

        
          - *(string) --* 

          
      
        - **condition** *(string) --* **[REQUIRED]** 

          A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by *AND* . If you specify multiple values for a particular filter, the system differentiates the values using *OR* . Calling either *DescribeConfigurations* or *ListConfigurations* returns attributes of matching configuration items.

          

        
      
  
    :type maxResults: integer
    :param maxResults: 

      The total number of items to return. The maximum value is 100.

      

    
    :type nextToken: string
    :param nextToken: 

      Token to retrieve the next set of results. For example, if a previous call to ListConfigurations returned 100 items, but you set ``ListConfigurationsRequest$maxResults`` to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.

      

    
    :type orderBy: list
    :param orderBy: 

      Certain filter criteria return output that can be sorted in ascending or descending order. For a list of output characteristics for each filter, see `Using the ListConfigurations Action <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html#ListConfigurations>`__ .

      

    
      - *(dict) --* 

        A field and direction for ordered output.

        

      
        - **fieldName** *(string) --* **[REQUIRED]** 

          The field on which to order.

          

        
        - **sortOrder** *(string) --* 

          Ordering direction.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'configurations': [
                {
                    'string': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **configurations** *(list) --* 

          Returns configuration details, including the configuration ID, attribute names, and attribute values.

          
          

          - *(dict) --* 
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
        

        - **nextToken** *(string) --* 

          Token to retrieve the next set of results. For example, if your call to ListConfigurations returned 100 items, but you set ``ListConfigurationsRequest$maxResults`` to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.

          
    

  .. py:method:: list_server_neighbors(**kwargs)

    

    Retrieves a list of servers that are one network hop away from a specified server.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/ListServerNeighbors>`_    


    **Request Syntax** 
    ::

      response = client.list_server_neighbors(
          configurationId='string',
          portInformationNeeded=True|False,
          neighborConfigurationIds=[
              'string',
          ],
          maxResults=123,
          nextToken='string'
      )
    :type configurationId: string
    :param configurationId: **[REQUIRED]** 

      Configuration ID of the server for which neighbors are being listed.

      

    
    :type portInformationNeeded: boolean
    :param portInformationNeeded: 

      Flag to indicate if port and protocol information is needed as part of the response.

      

    
    :type neighborConfigurationIds: list
    :param neighborConfigurationIds: 

      List of configuration IDs to test for one-hop-away.

      

    
      - *(string) --* 

      
  
    :type maxResults: integer
    :param maxResults: 

      Maximum number of results to return in a single page of output.

      

    
    :type nextToken: string
    :param nextToken: 

      Token to retrieve the next set of results. For example, if you previously specified 100 IDs for ``ListServerNeighborsRequest$neighborConfigurationIds`` but set ``ListServerNeighborsRequest$maxResults`` to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'neighbors': [
                {
                    'sourceServerId': 'string',
                    'destinationServerId': 'string',
                    'destinationPort': 123,
                    'transportProtocol': 'string',
                    'connectionsCount': 123
                },
            ],
            'nextToken': 'string',
            'knownDependencyCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **neighbors** *(list) --* 

          List of distinct servers that are one hop away from the given server.

          
          

          - *(dict) --* 

            Details about neighboring servers.

            
            

            - **sourceServerId** *(string) --* 

              The ID of the server that opened the network connection.

              
            

            - **destinationServerId** *(string) --* 

              The ID of the server that accepted the network connection.

              
            

            - **destinationPort** *(integer) --* 

              The destination network port for the connection.

              
            

            - **transportProtocol** *(string) --* 

              The network protocol used for the connection.

              
            

            - **connectionsCount** *(integer) --* 

              The number of open network connections with the neighboring server.

              
        
      
        

        - **nextToken** *(string) --* 

          Token to retrieve the next set of results. For example, if you specified 100 IDs for ``ListServerNeighborsRequest$neighborConfigurationIds`` but set ``ListServerNeighborsRequest$maxResults`` to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.

          
        

        - **knownDependencyCount** *(integer) --* 

          Count of distinct servers that are one hop away from the given server.

          
    

  .. py:method:: start_data_collection_by_agent_ids(**kwargs)

    

    Instructs the specified agents or connectors to start collecting data.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/StartDataCollectionByAgentIds>`_    


    **Request Syntax** 
    ::

      response = client.start_data_collection_by_agent_ids(
          agentIds=[
              'string',
          ]
      )
    :type agentIds: list
    :param agentIds: **[REQUIRED]** 

      The IDs of the agents or connectors from which to start collecting data. If you send a request to an agent/connector ID that you do not have permission to contact, according to your AWS account, the service does not throw an exception. Instead, it returns the error in the *Description* field. If you send a request to multiple agents/connectors and you do not have permission to contact some of those agents/connectors, the system does not throw an exception. Instead, the system shows ``Failed`` in the *Description* field.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'agentsConfigurationStatus': [
                {
                    'agentId': 'string',
                    'operationSucceeded': True|False,
                    'description': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **agentsConfigurationStatus** *(list) --* 

          Information about agents or the connector that were instructed to start collecting data. Information includes the agent/connector ID, a description of the operation performed, and whether the agent/connector configuration was updated.

          
          

          - *(dict) --* 

            Information about agents or connectors that were instructed to start collecting data. Information includes the agent/connector ID, a description of the operation, and whether the agent/connector configuration was updated.

            
            

            - **agentId** *(string) --* 

              The agent/connector ID.

              
            

            - **operationSucceeded** *(boolean) --* 

              Information about the status of the ``StartDataCollection`` and ``StopDataCollection`` operations. The system has recorded the data collection operation. The agent/connector receives this command the next time it polls for a new command. 

              
            

            - **description** *(string) --* 

              A description of the operation performed.

              
        
      
    

  .. py:method:: start_export_task(**kwargs)

    

    Begins the export of discovered data to an S3 bucket.

     

    If you specify ``agentId`` in a filter, the task exports up to 72 hours of detailed data collected by the identified Application Discovery Agent, including network, process, and performance details. A time range for exported agent data may be set by using ``startTime`` and ``endTime`` . Export of detailed agent data is limited to five concurrently running exports. 

     

    If you do not include an ``agentId`` filter, summary data is exported that includes both AWS Agentless Discovery Connector data and summary data from AWS Discovery Agents. Export of summary data is limited to two exports per day. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/StartExportTask>`_    


    **Request Syntax** 
    ::

      response = client.start_export_task(
          exportDataFormat=[
              'CSV'|'GRAPHML',
          ],
          filters=[
              {
                  'name': 'string',
                  'values': [
                      'string',
                  ],
                  'condition': 'string'
              },
          ],
          startTime=datetime(2015, 1, 1),
          endTime=datetime(2015, 1, 1)
      )
    :type exportDataFormat: list
    :param exportDataFormat: 

      The file format for the returned export data. Default value is ``CSV`` .

      

    
      - *(string) --* 

      
  
    :type filters: list
    :param filters: 

      If a filter is present, it selects the single ``agentId`` of the Application Discovery Agent for which data is exported. The ``agentId`` can be found in the results of the ``DescribeAgents`` API or CLI. If no filter is present, ``startTime`` and ``endTime`` are ignored and exported data includes both Agentless Discovery Connector data and summary data from Application Discovery agents. 

      

    
      - *(dict) --* 

        Used to select which agent's data is to be exported. A single agent ID may be selected for export using the `StartExportTask <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__ action.

        

      
        - **name** *(string) --* **[REQUIRED]** 

          A single ``ExportFilter`` name. Supported filters: ``agentId`` .

          

        
        - **values** *(list) --* **[REQUIRED]** 

          A single ``agentId`` for a Discovery Agent. An ``agentId`` can be found using the `DescribeAgents <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html>`__ action. Typically an ADS ``agentId`` is in the form ``o-0123456789abcdef0`` .

          

        
          - *(string) --* 

          
      
        - **condition** *(string) --* **[REQUIRED]** 

          Supported condition: ``EQUALS``  

          

        
      
  
    :type startTime: datetime
    :param startTime: 

      The start timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, data is exported starting from the first data collected by the agent.

      

    
    :type endTime: datetime
    :param endTime: 

      The end timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, exported data includes the most recent data collected by the agent.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'exportId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **exportId** *(string) --* 

          A unique identifier used to query the status of an export request.

          
    

  .. py:method:: stop_data_collection_by_agent_ids(**kwargs)

    

    Instructs the specified agents or connectors to stop collecting data.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/StopDataCollectionByAgentIds>`_    


    **Request Syntax** 
    ::

      response = client.stop_data_collection_by_agent_ids(
          agentIds=[
              'string',
          ]
      )
    :type agentIds: list
    :param agentIds: **[REQUIRED]** 

      The IDs of the agents or connectors from which to stop collecting data.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'agentsConfigurationStatus': [
                {
                    'agentId': 'string',
                    'operationSucceeded': True|False,
                    'description': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **agentsConfigurationStatus** *(list) --* 

          Information about the agents or connector that were instructed to stop collecting data. Information includes the agent/connector ID, a description of the operation performed, and whether the agent/connector configuration was updated.

          
          

          - *(dict) --* 

            Information about agents or connectors that were instructed to start collecting data. Information includes the agent/connector ID, a description of the operation, and whether the agent/connector configuration was updated.

            
            

            - **agentId** *(string) --* 

              The agent/connector ID.

              
            

            - **operationSucceeded** *(boolean) --* 

              Information about the status of the ``StartDataCollection`` and ``StopDataCollection`` operations. The system has recorded the data collection operation. The agent/connector receives this command the next time it polls for a new command. 

              
            

            - **description** *(string) --* 

              A description of the operation performed.

              
        
      
    

  .. py:method:: update_application(**kwargs)

    

    Updates metadata about an application.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/UpdateApplication>`_    


    **Request Syntax** 
    ::

      response = client.update_application(
          configurationId='string',
          name='string',
          description='string'
      )
    :type configurationId: string
    :param configurationId: **[REQUIRED]** 

      Configuration ID of the application to be updated.

      

    
    :type name: string
    :param name: 

      New name of the application to be updated.

      

    
    :type description: string
    :param description: 

      New description of the application to be updated.

      

    
    
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
