

************
CostExplorer
************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CostExplorer.Client

  A low-level client representing AWS Cost Explorer Service::

    
    import boto3
    
    client = boto3.client('ce')

  
  These are the available methods:
  
  *   :py:meth:`~CostExplorer.Client.can_paginate`

  
  *   :py:meth:`~CostExplorer.Client.generate_presigned_url`

  
  *   :py:meth:`~CostExplorer.Client.get_cost_and_usage`

  
  *   :py:meth:`~CostExplorer.Client.get_dimension_values`

  
  *   :py:meth:`~CostExplorer.Client.get_paginator`

  
  *   :py:meth:`~CostExplorer.Client.get_reservation_utilization`

  
  *   :py:meth:`~CostExplorer.Client.get_tags`

  
  *   :py:meth:`~CostExplorer.Client.get_waiter`

  

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


  .. py:method:: get_cost_and_usage(**kwargs)

    

    Retrieve cost and usage metrics for your account. You can specify which cost and usage-related metric, such as ``BlendedCosts`` or ``UsageQuantity`` , that you want the request to return. You can also filter and group your data by various dimensions, such as ``AWS Service`` or ``AvailabilityZone`` , in a specific time range. See the ``GetDimensionValues`` action for a complete list of the valid dimensions. Master accounts in an organization have access to all member accounts.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetCostAndUsage>`_    


    **Request Syntax** 
    ::

      response = client.get_cost_and_usage(
          TimePeriod={
              'Start': 'string',
              'End': 'string'
          },
          Granularity='DAILY'|'MONTHLY',
          Filter={
              'Or': [
                  {'... recursive ...'},
              ],
              'And': [
                  {'... recursive ...'},
              ],
              'Not': {'... recursive ...'},
              'Dimensions': {
                  'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID',
                  'Values': [
                      'string',
                  ]
              },
              'Tags': {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              }
          },
          Metrics=[
              'string',
          ],
          GroupBy=[
              {
                  'Type': 'DIMENSION'|'TAG',
                  'Key': 'string'
              },
          ],
          NextPageToken='string'
      )
    :type TimePeriod: dict
    :param TimePeriod: 

      Sets the start and end dates for retrieving AWS costs. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .

      

    
      - **Start** *(string) --* **[REQUIRED]** 

        The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , then the cost and usage data is retrieved starting at ``2017-01-01`` up to the end date.

        

      
      - **End** *(string) --* **[REQUIRED]** 

        The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if the ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from the start date but not including ``2017-05-01`` .

        

      
    
    :type Granularity: string
    :param Granularity: 

      Sets the AWS cost granularity to ``MONTHLY`` or ``DAILY`` .

      

    
    :type Filter: dict
    :param Filter: 

      Filters AWS costs by different dimensions. For example, you can specify ``Service`` and ``Linked Account`` and get the costs associated with that account's usage of that service. You can nest ``Expression`` objects to define any combination of dimension filters. For more information, see the ``Expression`` object or ``More Examples`` . 

      

    
      - **Or** *(list) --* 

        Return results that match either ``Dimension`` .

        

      
        - *(dict) --* 

          Use ``Expression`` to filter by cost or by usage. There are two patterns: 

           

           
          * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``InstanceType==m4.xlarge OR InstanceType==c4.large`` . The ``Expression`` for that looks like this.  ``{ "Dimensions": { "Key": "InstanceType", "Values": [ "m4.xlarge", “c4.large” ] } }``   The list of dimension values are OR'd together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.  
           
          * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((InstanceType == m4.large OR InstanceType == m3.large) OR (Tag.Type == Type1)) AND (UsageType != DataTransfer)`` . The ``Expression`` for that looks like this.  ``{ "And": [ {"Or": [ {"Dimensions": { "Key": "InstanceType", "Values": [ "m4.x.large", "c4.large" ] }}, {"Tag": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"dimensions": { "Key": "UsageType", "Values": ["DataTransfer"] }}} ] }``   

          .. note::

             Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that will create an error. 

            ``{ "And": [ ... ], "DimensionValues": { "Dimension": "UsageType", "Values": [ "DataTransfer" ] } }``   
           

          

        
    
      - **And** *(list) --* 

        Return results that match both ``Dimension`` objects.

        

      
        - *(dict) --* 

          Use ``Expression`` to filter by cost or by usage. There are two patterns: 

           

           
          * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``InstanceType==m4.xlarge OR InstanceType==c4.large`` . The ``Expression`` for that looks like this.  ``{ "Dimensions": { "Key": "InstanceType", "Values": [ "m4.xlarge", “c4.large” ] } }``   The list of dimension values are OR'd together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.  
           
          * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((InstanceType == m4.large OR InstanceType == m3.large) OR (Tag.Type == Type1)) AND (UsageType != DataTransfer)`` . The ``Expression`` for that looks like this.  ``{ "And": [ {"Or": [ {"Dimensions": { "Key": "InstanceType", "Values": [ "m4.x.large", "c4.large" ] }}, {"Tag": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"dimensions": { "Key": "UsageType", "Values": ["DataTransfer"] }}} ] }``   

          .. note::

             Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that will create an error. 

            ``{ "And": [ ... ], "DimensionValues": { "Dimension": "UsageType", "Values": [ "DataTransfer" ] } }``   
           

          

        
    
      - **Not** *(dict) --* 

        Return results that don't match ``Dimension`` .

        

      
      - **Dimensions** *(dict) --* 

        The specific ``Dimension`` to use for ``Expression`` .

        

      
        - **Key** *(string) --* 

          The names of the metadata types that you can use to filter and group your results. For example, ``AZ`` returns a list of Availability Zones.

          

        
        - **Values** *(list) --* 

          The metadata values that you can use to filter and group your results. You can use ``GetDimensionValues`` to find specific values.

          

        
          - *(string) --* 

          
      
      
      - **Tags** *(dict) --* 

        The specific ``Tag`` to use for ``Expression`` .

        

      
        - **Key** *(string) --* 

          The key for a tag.

          

        
        - **Values** *(list) --* 

          The specific value of a tag.

          

        
          - *(string) --* 

          
      
      
    
    :type Metrics: list
    :param Metrics: 

      Which metrics are returned in the query. For more information about blended and unblended rates, see https://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/. 

       

      Valid values are ``BlendedCost`` , ``UnblendedCost`` , and ``UsageQuantity`` .

       

      .. note::

         

        If you return the ``UsageQuantity`` metric, the service aggregates all usage numbers without taking into account the units. For example, if you aggregate ``usageQuantity`` across all of EC2, the results aren't meaningful because EC2 compute hours and data transfer are measured in different units (for example, hours vs. GB). To get more meaningful ``UsageQuantity`` metrics, filter by ``UsageType`` or ``UsageTypeGroups`` . 

         

      

    
      - *(string) --* 

      
  
    :type GroupBy: list
    :param GroupBy: 

      You can group AWS costs using up to two different groups, either dimensions, tag keys, or both.

       

      When you group by tag key, you get all tag values, including empty strings.

       

      Valid values are: ``AZ`` , ``INSTANCE_TYPE`` , ``LINKED_ACCCOUNT`` , ``OPERATION`` , ``PURCHASE_TYPE`` , ``SERVICE`` , ``USAGE_TYPE`` , ``TAGS`` , and ``PLATFORM`` .

      

    
      - *(dict) --* 

        Represents a group when you specify a group by criteria, or in the response to a query with a specific grouping.

        

      
        - **Type** *(string) --* 

          The string that represents the type of group.

          

        
        - **Key** *(string) --* 

          The string that represents a key for a specified group.

          

        
      
  
    :type NextPageToken: string
    :param NextPageToken: 

      The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextPageToken': 'string',
            'GroupDefinitions': [
                {
                    'Type': 'DIMENSION'|'TAG',
                    'Key': 'string'
                },
            ],
            'ResultsByTime': [
                {
                    'TimePeriod': {
                        'Start': 'string',
                        'End': 'string'
                    },
                    'Total': {
                        'string': {
                            'Amount': 'string',
                            'Unit': 'string'
                        }
                    },
                    'Groups': [
                        {
                            'Keys': [
                                'string',
                            ],
                            'Metrics': {
                                'string': {
                                    'Amount': 'string',
                                    'Unit': 'string'
                                }
                            }
                        },
                    ],
                    'Estimated': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextPageToken** *(string) --* 

          The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.

          
        

        - **GroupDefinitions** *(list) --* 

          The groups specified by the the ``Filter`` or ``GroupBy`` parameters in the request.

          
          

          - *(dict) --* 

            Represents a group when you specify a group by criteria, or in the response to a query with a specific grouping.

            
            

            - **Type** *(string) --* 

              The string that represents the type of group.

              
            

            - **Key** *(string) --* 

              The string that represents a key for a specified group.

              
        
      
        

        - **ResultsByTime** *(list) --* 

          The time period covered by the results in the response.

          
          

          - *(dict) --* 

            The result that is associated with a time period.

            
            

            - **TimePeriod** *(dict) --* 

              The time period covered by a result.

              
              

              - **Start** *(string) --* 

                The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , then the cost and usage data is retrieved starting at ``2017-01-01`` up to the end date.

                
              

              - **End** *(string) --* 

                The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if the ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from the start date but not including ``2017-05-01`` .

                
          
            

            - **Total** *(dict) --* 

              The total amount of cost or usage accrued during the time period.

              
              

              - *(string) --* 
                

                - *(dict) --* 

                  The aggregated value for a metric.

                  
                  

                  - **Amount** *(string) --* 

                    The actual number that represents the metric.

                    
                  

                  - **Unit** *(string) --* 

                    The unit that the metric is given in.

                    
              
          
        
            

            - **Groups** *(list) --* 

              The groups that are included in this time period.

              
              

              - *(dict) --* 

                One level of grouped data within the results.

                
                

                - **Keys** *(list) --* 

                  The keys included in this group.

                  
                  

                  - *(string) --* 
              
                

                - **Metrics** *(dict) --* 

                  The metrics included in this group.

                  
                  

                  - *(string) --* 
                    

                    - *(dict) --* 

                      The aggregated value for a metric.

                      
                      

                      - **Amount** *(string) --* 

                        The actual number that represents the metric.

                        
                      

                      - **Unit** *(string) --* 

                        The unit that the metric is given in.

                        
                  
              
            
            
          
            

            - **Estimated** *(boolean) --* 

              Whether or not this result is estimated.

              
        
      
    

  .. py:method:: get_dimension_values(**kwargs)

    

    You can use ``GetDimensionValues`` to retrieve all available filter values for a specific filter over a period of time. You can search the dimension values for an arbitrary string. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetDimensionValues>`_    


    **Request Syntax** 
    ::

      response = client.get_dimension_values(
          SearchString='string',
          TimePeriod={
              'Start': 'string',
              'End': 'string'
          },
          Dimension='AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID',
          Context='COST_AND_USAGE'|'RESERVATIONS',
          NextPageToken='string'
      )
    :type SearchString: string
    :param SearchString: 

      The value that you want to search the filter values for.

      

    
    :type TimePeriod: dict
    :param TimePeriod: **[REQUIRED]** 

      The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .

      

    
      - **Start** *(string) --* **[REQUIRED]** 

        The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , then the cost and usage data is retrieved starting at ``2017-01-01`` up to the end date.

        

      
      - **End** *(string) --* **[REQUIRED]** 

        The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if the ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from the start date but not including ``2017-05-01`` .

        

      
    
    :type Dimension: string
    :param Dimension: **[REQUIRED]** 

      The name of the dimension. Different ``Dimensions`` are available for different ``Context`` s. For more information, see ``Context`` .

      

    
    :type Context: string
    :param Context: 

      The context for the call to ``GetDimensionValues`` . This can be ``RESERVED_INSTANCE`` or ``COST_AND_USAGE`` . The default value is ``COST_AND_USAGE`` . If the context is set to ``RESERVED_INSTANCE`` , the resulting dimension values can be used in the ``GetReservationUtilization`` action. If the context is set to ``COST_AND_USAGE`` , , the resulting dimension values can be used in the ``GetCostAndUsage`` operation.

       

      If you set the context to ``CostAndUsage`` , you can use the following dimensions for searching:

       

       
      * AZ - The Availability Zone. An example is us-east-1a. 
       
      * InstanceType - The type of EC2 instance. An example is m4.xlarge. 
       
      * LinkedAccount - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account 
       
      * Operation - The action performed. Examples include RunInstance and CreateBucket. 
       
      * PurchaseType - The reservation type of the purchase to which this usage is related. Examples include: On Demand Instances and Standard Reserved Instances 
       
      * Service - The AWS service such as DynamoDB. 
       
      * UsageType -The type of usage. An example is DataTransfer-In-Bytes. The response for the GetDimensionValues action includes a unit attribute, examples of which include GB and Hrs. 
       
      * UsageTypeGroup - The grouping of common usage types. An example is EC2: CloudWatch – Alarms. The response for this action includes a unit attribute. 
       
      * RecordType - The different types of charges such as RI fees, usage costs, tax refunds, and credits 
       

       

      If you set the context to ``ReservedInstance`` , you can use the following dimensions for searching:

       

       
      * AZ - The Availability Zone. An example is us-east-1a. 
       
      * InstanceType - The type of EC2 instance. An example is m4.xlarge. 
       
      * LinkedAccount - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account 
       
      * Platform - The operating system. Examples are Windows or Linux. 
       
      * Region - The AWS region. 
       
      * Scope - The scope of a reserved instance (RI). Values are regional or a single availability zone. 
       
      * Tenancy - The tenancy of a resource. Examples are shared or dedicated. 
       

      

    
    :type NextPageToken: string
    :param NextPageToken: 

      The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DimensionValues': [
                {
                    'Value': 'string',
                    'Attributes': {
                        'string': 'string'
                    }
                },
            ],
            'ReturnSize': 123,
            'TotalSize': 123,
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DimensionValues** *(list) --* 

          The filters that you used to filter your request. Some dimensions are available only for a specific context:

           

          If you set the context to ``CostAndUsage`` , you can use the following dimensions for searching:

           

           
          * AZ - The Availability Zone. An example is us-east-1a. 
           
          * InstanceType - The type of EC2 instance. An example is m4.xlarge. 
           
          * LinkedAccount - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account 
           
          * Operation - The action performed. Examples include RunInstance and CreateBucket. 
           
          * PurchaseType - The reservation type of the purchase to which this usage is related. Examples include: On Demand Instances and Standard Reserved Instances 
           
          * Service - The AWS service such as DynamoDB. 
           
          * UsageType -The type of usage. An example is DataTransfer-In-Bytes. The response for the GetDimensionValues action includes a unit attribute, examples of which include GB and Hrs. 
           
          * UsageTypeGroup - The grouping of common usage types. An example is EC2: CloudWatch – Alarms. The response for this action includes a unit attribute. 
           
          * RecordType - The different types of charges such as RI fees, usage costs, tax refunds, and credits 
           

           

          If you set the context to ``ReservedInstance`` , you can use the following dimensions for searching:

           

           
          * AZ - The Availability Zone. An example is us-east-1a. 
           
          * InstanceType - The type of EC2 instance. An example is m4.xlarge. 
           
          * LinkedAccount - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account 
           
          * Platform - The operating system. Examples are Windows or Linux. 
           
          * Region - The AWS region. 
           
          * Scope - The scope of a reserved instance (RI). Values are regional or a single availability zone. 
           
          * Tenancy - The tenancy of a resource. Examples are shared or dedicated. 
           

          
          

          - *(dict) --* 

            The metadata of a specific type that you can use to filter and group your results. You can use ``GetDimensionValues`` to find specific values.

            
            

            - **Value** *(string) --* 

              The value of a dimension with a specific attribute.

              
            

            - **Attributes** *(dict) --* 

              The attribute that applies to a specific ``Dimension`` .

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **ReturnSize** *(integer) --* 

          The number of results that AWS returned at one time.

          
        

        - **TotalSize** *(integer) --* 

          The total number of search results.

          
        

        - **NextPageToken** *(string) --* 

          The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.

          
    

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


  .. py:method:: get_reservation_utilization(**kwargs)

    

    You can retrieve the Reservation utilization for your account. Master accounts in an organization have access to their associated member accounts. You can filter data by dimensions in a time period. You can use ``GetDimensionValues`` to determine the possible dimension values. Currently, you can group only by ``SUBSCRIPTION_ID`` . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetReservationUtilization>`_    


    **Request Syntax** 
    ::

      response = client.get_reservation_utilization(
          TimePeriod={
              'Start': 'string',
              'End': 'string'
          },
          GroupBy=[
              {
                  'Type': 'DIMENSION'|'TAG',
                  'Key': 'string'
              },
          ],
          Granularity='DAILY'|'MONTHLY',
          Filter={
              'Or': [
                  {'... recursive ...'},
              ],
              'And': [
                  {'... recursive ...'},
              ],
              'Not': {'... recursive ...'},
              'Dimensions': {
                  'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID',
                  'Values': [
                      'string',
                  ]
              },
              'Tags': {
                  'Key': 'string',
                  'Values': [
                      'string',
                  ]
              }
          },
          NextPageToken='string'
      )
    :type TimePeriod: dict
    :param TimePeriod: **[REQUIRED]** 

      Sets the start and end dates for retrieving reserve instance (RI) utilization. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` . 

      

    
      - **Start** *(string) --* **[REQUIRED]** 

        The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , then the cost and usage data is retrieved starting at ``2017-01-01`` up to the end date.

        

      
      - **End** *(string) --* **[REQUIRED]** 

        The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if the ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from the start date but not including ``2017-05-01`` .

        

      
    
    :type GroupBy: list
    :param GroupBy: 

      Groups only by ``SubscriptionId`` . Metadata is included.

      

    
      - *(dict) --* 

        Represents a group when you specify a group by criteria, or in the response to a query with a specific grouping.

        

      
        - **Type** *(string) --* 

          The string that represents the type of group.

          

        
        - **Key** *(string) --* 

          The string that represents a key for a specified group.

          

        
      
  
    :type Granularity: string
    :param Granularity: 

      Sets the AWS cost granularity to ``MONTHLY`` or ``DAILY`` . If both ``GroupBy`` and ``granularity`` are not set, ``GetReservationUtilization`` defaults to ``DAILY`` . If ``GroupBy`` is set, ``Granularity`` can't be set, and the response object doesn't include ``MONTHLY`` or ``DAILY`` granularity.

      

    
    :type Filter: dict
    :param Filter: 

      Filters utilization data by using different dimensions. ``GetReservationUtilization`` uses the same ``Expression`` object as the other operations, but only ``AND`` is supported among each dimension, and nesting is supported up to only one level deep. If there are multiple values for a dimension, they are OR'd together.

      

    
      - **Or** *(list) --* 

        Return results that match either ``Dimension`` .

        

      
        - *(dict) --* 

          Use ``Expression`` to filter by cost or by usage. There are two patterns: 

           

           
          * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``InstanceType==m4.xlarge OR InstanceType==c4.large`` . The ``Expression`` for that looks like this.  ``{ "Dimensions": { "Key": "InstanceType", "Values": [ "m4.xlarge", “c4.large” ] } }``   The list of dimension values are OR'd together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.  
           
          * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((InstanceType == m4.large OR InstanceType == m3.large) OR (Tag.Type == Type1)) AND (UsageType != DataTransfer)`` . The ``Expression`` for that looks like this.  ``{ "And": [ {"Or": [ {"Dimensions": { "Key": "InstanceType", "Values": [ "m4.x.large", "c4.large" ] }}, {"Tag": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"dimensions": { "Key": "UsageType", "Values": ["DataTransfer"] }}} ] }``   

          .. note::

             Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that will create an error. 

            ``{ "And": [ ... ], "DimensionValues": { "Dimension": "UsageType", "Values": [ "DataTransfer" ] } }``   
           

          

        
    
      - **And** *(list) --* 

        Return results that match both ``Dimension`` objects.

        

      
        - *(dict) --* 

          Use ``Expression`` to filter by cost or by usage. There are two patterns: 

           

           
          * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``InstanceType==m4.xlarge OR InstanceType==c4.large`` . The ``Expression`` for that looks like this.  ``{ "Dimensions": { "Key": "InstanceType", "Values": [ "m4.xlarge", “c4.large” ] } }``   The list of dimension values are OR'd together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.  
           
          * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((InstanceType == m4.large OR InstanceType == m3.large) OR (Tag.Type == Type1)) AND (UsageType != DataTransfer)`` . The ``Expression`` for that looks like this.  ``{ "And": [ {"Or": [ {"Dimensions": { "Key": "InstanceType", "Values": [ "m4.x.large", "c4.large" ] }}, {"Tag": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"dimensions": { "Key": "UsageType", "Values": ["DataTransfer"] }}} ] }``   

          .. note::

             Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that will create an error. 

            ``{ "And": [ ... ], "DimensionValues": { "Dimension": "UsageType", "Values": [ "DataTransfer" ] } }``   
           

          

        
    
      - **Not** *(dict) --* 

        Return results that don't match ``Dimension`` .

        

      
      - **Dimensions** *(dict) --* 

        The specific ``Dimension`` to use for ``Expression`` .

        

      
        - **Key** *(string) --* 

          The names of the metadata types that you can use to filter and group your results. For example, ``AZ`` returns a list of Availability Zones.

          

        
        - **Values** *(list) --* 

          The metadata values that you can use to filter and group your results. You can use ``GetDimensionValues`` to find specific values.

          

        
          - *(string) --* 

          
      
      
      - **Tags** *(dict) --* 

        The specific ``Tag`` to use for ``Expression`` .

        

      
        - **Key** *(string) --* 

          The key for a tag.

          

        
        - **Values** *(list) --* 

          The specific value of a tag.

          

        
          - *(string) --* 

          
      
      
    
    :type NextPageToken: string
    :param NextPageToken: 

      The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UtilizationsByTime': [
                {
                    'TimePeriod': {
                        'Start': 'string',
                        'End': 'string'
                    },
                    'Groups': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Attributes': {
                                'string': 'string'
                            },
                            'Utilization': {
                                'UtilizationPercentage': 'string',
                                'PurchasedHours': 'string',
                                'TotalActualHours': 'string',
                                'UnusedHours': 'string'
                            }
                        },
                    ],
                    'Total': {
                        'UtilizationPercentage': 'string',
                        'PurchasedHours': 'string',
                        'TotalActualHours': 'string',
                        'UnusedHours': 'string'
                    }
                },
            ],
            'Total': {
                'UtilizationPercentage': 'string',
                'PurchasedHours': 'string',
                'TotalActualHours': 'string',
                'UnusedHours': 'string'
            },
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **UtilizationsByTime** *(list) --* 

          The amount of time that you utilized your RIs.

          
          

          - *(dict) --* 

            The amount of utilization, in hours.

            
            

            - **TimePeriod** *(dict) --* 

              The period of time over which this utilization was used.

              
              

              - **Start** *(string) --* 

                The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , then the cost and usage data is retrieved starting at ``2017-01-01`` up to the end date.

                
              

              - **End** *(string) --* 

                The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if the ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from the start date but not including ``2017-05-01`` .

                
          
            

            - **Groups** *(list) --* 

              The groups that are included in this utilization result.

              
              

              - *(dict) --* 

                A group of RIs that share a set of attributes.

                
                

                - **Key** *(string) --* 

                  The key for a specific RI attribute.

                  
                

                - **Value** *(string) --* 

                  The value of a specific RI attribute.

                  
                

                - **Attributes** *(dict) --* 

                  The attributes for this group of RIs.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **Utilization** *(dict) --* 

                  How much you used this group of RIs.

                  
                  

                  - **UtilizationPercentage** *(string) --* 

                    The percentage of RI time that you used.

                    
                  

                  - **PurchasedHours** *(string) --* 

                    How many RI hours you purchased.

                    
                  

                  - **TotalActualHours** *(string) --* 

                    The total number of RI hours that you used.

                    
                  

                  - **UnusedHours** *(string) --* 

                    The number of RI hours that you didn't use.

                    
              
            
          
            

            - **Total** *(dict) --* 

              The total number of RI hours that were used.

              
              

              - **UtilizationPercentage** *(string) --* 

                The percentage of RI time that you used.

                
              

              - **PurchasedHours** *(string) --* 

                How many RI hours you purchased.

                
              

              - **TotalActualHours** *(string) --* 

                The total number of RI hours that you used.

                
              

              - **UnusedHours** *(string) --* 

                The number of RI hours that you didn't use.

                
          
        
      
        

        - **Total** *(dict) --* 

          The total amount of time that you utilized your RIs.

          
          

          - **UtilizationPercentage** *(string) --* 

            The percentage of RI time that you used.

            
          

          - **PurchasedHours** *(string) --* 

            How many RI hours you purchased.

            
          

          - **TotalActualHours** *(string) --* 

            The total number of RI hours that you used.

            
          

          - **UnusedHours** *(string) --* 

            The number of RI hours that you didn't use.

            
      
        

        - **NextPageToken** *(string) --* 

          The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.

          
    

  .. py:method:: get_tags(**kwargs)

    

    You can query for available tag keys and tag values for a specified period. You can search the tag values for an arbitrary string. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetTags>`_    


    **Request Syntax** 
    ::

      response = client.get_tags(
          SearchString='string',
          TimePeriod={
              'Start': 'string',
              'End': 'string'
          },
          TagKey='string',
          NextPageToken='string'
      )
    :type SearchString: string
    :param SearchString: 

      The value that you want to search for.

      

    
    :type TimePeriod: dict
    :param TimePeriod: **[REQUIRED]** 

      The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .

      

    
      - **Start** *(string) --* **[REQUIRED]** 

        The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , then the cost and usage data is retrieved starting at ``2017-01-01`` up to the end date.

        

      
      - **End** *(string) --* **[REQUIRED]** 

        The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if the ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from the start date but not including ``2017-05-01`` .

        

      
    
    :type TagKey: string
    :param TagKey: 

      The key of the tag that you want to return values for.

      

    
    :type NextPageToken: string
    :param NextPageToken: 

      The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextPageToken': 'string',
            'Tags': [
                'string',
            ],
            'ReturnSize': 123,
            'TotalSize': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextPageToken** *(string) --* 

          The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.

          
        

        - **Tags** *(list) --* 

          The tags that match your request.

          
          

          - *(string) --* 
      
        

        - **ReturnSize** *(integer) --* 

          The number of query results that AWS returns at a time.

          
        

        - **TotalSize** *(integer) --* 

          The total number of query results.

          
    

  .. py:method:: get_waiter(waiter_name)

        


==========
Paginators
==========


The available paginators are:
