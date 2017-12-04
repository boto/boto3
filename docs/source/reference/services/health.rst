

******
Health
******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Health.Client

  A low-level client representing AWS Health APIs and Notifications::

    
    import boto3
    
    client = boto3.client('health')

  
  These are the available methods:
  
  *   :py:meth:`~Health.Client.can_paginate`

  
  *   :py:meth:`~Health.Client.describe_affected_entities`

  
  *   :py:meth:`~Health.Client.describe_entity_aggregates`

  
  *   :py:meth:`~Health.Client.describe_event_aggregates`

  
  *   :py:meth:`~Health.Client.describe_event_details`

  
  *   :py:meth:`~Health.Client.describe_event_types`

  
  *   :py:meth:`~Health.Client.describe_events`

  
  *   :py:meth:`~Health.Client.generate_presigned_url`

  
  *   :py:meth:`~Health.Client.get_paginator`

  
  *   :py:meth:`~Health.Client.get_waiter`

  

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


  .. py:method:: describe_affected_entities(**kwargs)

    

    Returns a list of entities that have been affected by the specified events, based on the specified filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the AWS service. Events that have impact beyond that of the affected entities, or where the extent of impact is unknown, include at least one entity indicating this.

     

    At least one event ARN is required. Results are sorted by the ``lastUpdatedTime`` of the entity, starting with the most recent.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeAffectedEntities>`_    


    **Request Syntax** 
    ::

      response = client.describe_affected_entities(
          filter={
              'eventArns': [
                  'string',
              ],
              'entityArns': [
                  'string',
              ],
              'entityValues': [
                  'string',
              ],
              'lastUpdatedTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'tags': [
                  {
                      'string': 'string'
                  },
              ],
              'statusCodes': [
                  'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
              ]
          },
          locale='string',
          nextToken='string',
          maxResults=123
      )
    :type filter: dict
    :param filter: **[REQUIRED]** 

      Values to narrow the results returned. At least one event ARN is required. 

      

    
      - **eventArns** *(list) --* **[REQUIRED]** 

        A list of event ARNs (unique identifiers). For example: ``"arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331", "arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz"``  

        

      
        - *(string) --* 

        
    
      - **entityArns** *(list) --* 

        A list of entity ARNs (unique identifiers).

        

      
        - *(string) --* 

        
    
      - **entityValues** *(list) --* 

        A list of IDs for affected entities.

        

      
        - *(string) --* 

        
    
      - **lastUpdatedTimes** *(list) --* 

        A list of the most recent dates and times that the entity was updated.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **tags** *(list) --* 

        A map of entity tags attached to the affected entity.

        

      
        - *(dict) --* 

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
    
      - **statusCodes** *(list) --* 

        A list of entity status codes (``IMPAIRED`` , ``UNIMPAIRED`` , or ``UNKNOWN`` ).

        

      
        - *(string) --* 

        
    
    
    :type locale: string
    :param locale: 

      The locale (language) to return information in. English (en) is the default and the only supported value at this time.

      

    
    :type nextToken: string
    :param nextToken: 

      If the results of a search are large, only a portion of the results are returned, and a ``nextToken`` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of items to return in one batch, between 10 and 100, inclusive.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'entities': [
                {
                    'entityArn': 'string',
                    'eventArn': 'string',
                    'entityValue': 'string',
                    'awsAccountId': 'string',
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'statusCode': 'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
                    'tags': {
                        'string': 'string'
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **entities** *(list) --* 

          The entities that match the filter criteria.

          
          

          - *(dict) --* 

            Information about an entity that is affected by a Health event.

            
            

            - **entityArn** *(string) --* 

              The unique identifier for the entity. Format: ``arn:aws:health:*entity-region* :*aws-account* :entity/*entity-id* `` . Example: ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K``  

              
            

            - **eventArn** *(string) --* 

              The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*EVENT_TYPE_PLUS_ID* `` . Example: ``arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331``  

              
            

            - **entityValue** *(string) --* 

              The ID of the affected entity.

              
            

            - **awsAccountId** *(string) --* 

              The 12-digit AWS account number that contains the affected entity.

              
            

            - **lastUpdatedTime** *(datetime) --* 

              The most recent time that the entity was updated.

              
            

            - **statusCode** *(string) --* 

              The most recent status of the entity affected by the event. The possible values are ``IMPAIRED`` , ``UNIMPAIRED`` , and ``UNKNOWN`` .

              
            

            - **tags** *(dict) --* 

              A map of entity tags attached to the affected entity.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **nextToken** *(string) --* 

          If the results of a search are large, only a portion of the results are returned, and a ``nextToken`` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

          
    

  .. py:method:: describe_entity_aggregates(**kwargs)

    

    Returns the number of entities that are affected by each of the specified events. If no events are specified, the counts of all affected entities are returned.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEntityAggregates>`_    


    **Request Syntax** 
    ::

      response = client.describe_entity_aggregates(
          eventArns=[
              'string',
          ]
      )
    :type eventArns: list
    :param eventArns: 

      A list of event ARNs (unique identifiers). For example: ``"arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331", "arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz"``  

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'entityAggregates': [
                {
                    'eventArn': 'string',
                    'count': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **entityAggregates** *(list) --* 

          The number of entities that are affected by each of the specified events.

          
          

          - *(dict) --* 

            The number of entities that are affected by one or more events. Returned by the  DescribeEntityAggregates operation.

            
            

            - **eventArn** *(string) --* 

              The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*EVENT_TYPE_PLUS_ID* `` . Example: ``arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331``  

              
            

            - **count** *(integer) --* 

              The number entities that match the criteria for the specified events.

              
        
      
    

  .. py:method:: describe_event_aggregates(**kwargs)

    

    Returns the number of events of each event type (issue, scheduled change, and account notification). If no filter is specified, the counts of all events in each category are returned.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventAggregates>`_    


    **Request Syntax** 
    ::

      response = client.describe_event_aggregates(
          filter={
              'eventArns': [
                  'string',
              ],
              'eventTypeCodes': [
                  'string',
              ],
              'services': [
                  'string',
              ],
              'regions': [
                  'string',
              ],
              'availabilityZones': [
                  'string',
              ],
              'startTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'endTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'lastUpdatedTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'entityArns': [
                  'string',
              ],
              'entityValues': [
                  'string',
              ],
              'eventTypeCategories': [
                  'issue'|'accountNotification'|'scheduledChange',
              ],
              'tags': [
                  {
                      'string': 'string'
                  },
              ],
              'eventStatusCodes': [
                  'open'|'closed'|'upcoming',
              ]
          },
          aggregateField='eventTypeCategory',
          maxResults=123,
          nextToken='string'
      )
    :type filter: dict
    :param filter: 

      Values to narrow the results returned.

      

    
      - **eventArns** *(list) --* 

        A list of event ARNs (unique identifiers). For example: ``"arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331", "arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz"``  

        

      
        - *(string) --* 

        
    
      - **eventTypeCodes** *(list) --* 

        A list of unique identifiers for event types. For example, ``"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"``  

        

      
        - *(string) --* 

        
    
      - **services** *(list) --* 

        The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

        

      
        - *(string) --* 

        
    
      - **regions** *(list) --* 

        A list of AWS regions.

        

      
        - *(string) --* 

        
    
      - **availabilityZones** *(list) --* 

        A list of AWS availability zones.

        

      
        - *(string) --* 

        
    
      - **startTimes** *(list) --* 

        A list of dates and times that the event began.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **endTimes** *(list) --* 

        A list of dates and times that the event ended.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **lastUpdatedTimes** *(list) --* 

        A list of dates and times that the event was last updated.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **entityArns** *(list) --* 

        A list of entity ARNs (unique identifiers).

        

      
        - *(string) --* 

        
    
      - **entityValues** *(list) --* 

        A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes (``vol-426ab23e`` ).

        

      
        - *(string) --* 

        
    
      - **eventTypeCategories** *(list) --* 

        A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).

        

      
        - *(string) --* 

        
    
      - **tags** *(list) --* 

        A map of entity tags attached to the affected entity.

        

      
        - *(dict) --* 

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
    
      - **eventStatusCodes** *(list) --* 

        A list of event status codes.

        

      
        - *(string) --* 

        
    
    
    :type aggregateField: string
    :param aggregateField: **[REQUIRED]** 

      The only currently supported value is ``eventTypeCategory`` .

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of items to return in one batch, between 10 and 100, inclusive.

      

    
    :type nextToken: string
    :param nextToken: 

      If the results of a search are large, only a portion of the results are returned, and a ``nextToken`` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'eventAggregates': [
                {
                    'aggregateValue': 'string',
                    'count': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **eventAggregates** *(list) --* 

          The number of events in each category that meet the optional filter criteria.

          
          

          - *(dict) --* 

            The number of events of each issue type. Returned by the  DescribeEventAggregates operation.

            
            

            - **aggregateValue** *(string) --* 

              The issue type for the associated count.

              
            

            - **count** *(integer) --* 

              The number of events of the associated issue type.

              
        
      
        

        - **nextToken** *(string) --* 

          If the results of a search are large, only a portion of the results are returned, and a ``nextToken`` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

          
    

  .. py:method:: describe_event_details(**kwargs)

    

    Returns detailed information about one or more specified events. Information includes standard event data (region, service, etc., as returned by  DescribeEvents ), a detailed event description, and possible additional metadata that depends upon the nature of the event. Affected entities are not included; to retrieve those, use the  DescribeAffectedEntities operation.

     

    If a specified event cannot be retrieved, an error message is returned for that event.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventDetails>`_    


    **Request Syntax** 
    ::

      response = client.describe_event_details(
          eventArns=[
              'string',
          ],
          locale='string'
      )
    :type eventArns: list
    :param eventArns: **[REQUIRED]** 

      A list of event ARNs (unique identifiers). For example: ``"arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331", "arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz"``  

      

    
      - *(string) --* 

      
  
    :type locale: string
    :param locale: 

      The locale (language) to return information in. English (en) is the default and the only supported value at this time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'successfulSet': [
                {
                    'event': {
                        'arn': 'string',
                        'service': 'string',
                        'eventTypeCode': 'string',
                        'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange',
                        'region': 'string',
                        'availabilityZone': 'string',
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'statusCode': 'open'|'closed'|'upcoming'
                    },
                    'eventDescription': {
                        'latestDescription': 'string'
                    },
                    'eventMetadata': {
                        'string': 'string'
                    }
                },
            ],
            'failedSet': [
                {
                    'eventArn': 'string',
                    'errorName': 'string',
                    'errorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **successfulSet** *(list) --* 

          Information about the events that could be retrieved.

          
          

          - *(dict) --* 

            Detailed information about an event. A combination of an  Event object, an  EventDescription object, and additional metadata about the event. Returned by the  DescribeEventDetails operation.

            
            

            - **event** *(dict) --* 

              Summary information about the event.

              
              

              - **arn** *(string) --* 

                The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*EVENT_TYPE_PLUS_ID* `` . Example: ``arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331``  

                
              

              - **service** *(string) --* 

                The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

                
              

              - **eventTypeCode** *(string) --* 

                The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

                
              

              - **eventTypeCategory** *(string) --* 

                The 

                
              

              - **region** *(string) --* 

                The AWS region name of the event.

                
              

              - **availabilityZone** *(string) --* 

                The AWS Availability Zone of the event. For example, us-east-1a.

                
              

              - **startTime** *(datetime) --* 

                The date and time that the event began.

                
              

              - **endTime** *(datetime) --* 

                The date and time that the event ended.

                
              

              - **lastUpdatedTime** *(datetime) --* 

                The most recent date and time that the event was updated.

                
              

              - **statusCode** *(string) --* 

                The most recent status of the event. Possible values are ``open`` , ``closed`` , and ``upcoming`` .

                
          
            

            - **eventDescription** *(dict) --* 

              The most recent description of the event.

              
              

              - **latestDescription** *(string) --* 

                The most recent description of the event.

                
          
            

            - **eventMetadata** *(dict) --* 

              Additional metadata about the event.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **failedSet** *(list) --* 

          Error messages for any events that could not be retrieved.

          
          

          - *(dict) --* 

            Error information returned when a  DescribeEventDetails operation cannot find a specified event.

            
            

            - **eventArn** *(string) --* 

              The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*EVENT_TYPE_PLUS_ID* `` . Example: ``arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331``  

              
            

            - **errorName** *(string) --* 

              The name of the error.

              
            

            - **errorMessage** *(string) --* 

              A message that describes the error.

              
        
      
    

  .. py:method:: describe_event_types(**kwargs)

    

    Returns the event types that meet the specified filter criteria. If no filter criteria are specified, all event types are returned, in no particular order.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventTypes>`_    


    **Request Syntax** 
    ::

      response = client.describe_event_types(
          filter={
              'eventTypeCodes': [
                  'string',
              ],
              'services': [
                  'string',
              ],
              'eventTypeCategories': [
                  'issue'|'accountNotification'|'scheduledChange',
              ]
          },
          locale='string',
          nextToken='string',
          maxResults=123
      )
    :type filter: dict
    :param filter: 

      Values to narrow the results returned.

      

    
      - **eventTypeCodes** *(list) --* 

        A list of event type codes.

        

      
        - *(string) --* 

        
    
      - **services** *(list) --* 

        The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

        

      
        - *(string) --* 

        
    
      - **eventTypeCategories** *(list) --* 

        A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).

        

      
        - *(string) --* 

        
    
    
    :type locale: string
    :param locale: 

      The locale (language) to return information in. English (en) is the default and the only supported value at this time.

      

    
    :type nextToken: string
    :param nextToken: 

      If the results of a search are large, only a portion of the results are returned, and a ``nextToken`` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of items to return in one batch, between 10 and 100, inclusive.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'eventTypes': [
                {
                    'service': 'string',
                    'code': 'string',
                    'category': 'issue'|'accountNotification'|'scheduledChange'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **eventTypes** *(list) --* 

          A list of event types that match the filter criteria. Event types have a category (``issue`` , ``accountNotification`` , or ``scheduledChange`` ), a service (for example, ``EC2`` , ``RDS`` , ``DATAPIPELINE`` , ``BILLING`` ), and a code (in the format ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

          
          

          - *(dict) --* 

            Metadata about a type of event that is reported by AWS Health. Data consists of the category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

            
            

            - **service** *(string) --* 

              The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

              
            

            - **code** *(string) --* 

              The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

              
            

            - **category** *(string) --* 

              A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).

              
        
      
        

        - **nextToken** *(string) --* 

          If the results of a search are large, only a portion of the results are returned, and a ``nextToken`` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

          
    

  .. py:method:: describe_events(**kwargs)

    

    Returns information about events that meet the specified filter criteria. Events are returned in a summary form and do not include the detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the  DescribeEventDetails and  DescribeAffectedEntities operations.

     

    If no filter criteria are specified, all events are returned. Results are sorted by ``lastModifiedTime`` , starting with the most recent.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEvents>`_    


    **Request Syntax** 
    ::

      response = client.describe_events(
          filter={
              'eventArns': [
                  'string',
              ],
              'eventTypeCodes': [
                  'string',
              ],
              'services': [
                  'string',
              ],
              'regions': [
                  'string',
              ],
              'availabilityZones': [
                  'string',
              ],
              'startTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'endTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'lastUpdatedTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'entityArns': [
                  'string',
              ],
              'entityValues': [
                  'string',
              ],
              'eventTypeCategories': [
                  'issue'|'accountNotification'|'scheduledChange',
              ],
              'tags': [
                  {
                      'string': 'string'
                  },
              ],
              'eventStatusCodes': [
                  'open'|'closed'|'upcoming',
              ]
          },
          nextToken='string',
          maxResults=123,
          locale='string'
      )
    :type filter: dict
    :param filter: 

      Values to narrow the results returned.

      

    
      - **eventArns** *(list) --* 

        A list of event ARNs (unique identifiers). For example: ``"arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331", "arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz"``  

        

      
        - *(string) --* 

        
    
      - **eventTypeCodes** *(list) --* 

        A list of unique identifiers for event types. For example, ``"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"``  

        

      
        - *(string) --* 

        
    
      - **services** *(list) --* 

        The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

        

      
        - *(string) --* 

        
    
      - **regions** *(list) --* 

        A list of AWS regions.

        

      
        - *(string) --* 

        
    
      - **availabilityZones** *(list) --* 

        A list of AWS availability zones.

        

      
        - *(string) --* 

        
    
      - **startTimes** *(list) --* 

        A list of dates and times that the event began.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **endTimes** *(list) --* 

        A list of dates and times that the event ended.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **lastUpdatedTimes** *(list) --* 

        A list of dates and times that the event was last updated.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **entityArns** *(list) --* 

        A list of entity ARNs (unique identifiers).

        

      
        - *(string) --* 

        
    
      - **entityValues** *(list) --* 

        A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes (``vol-426ab23e`` ).

        

      
        - *(string) --* 

        
    
      - **eventTypeCategories** *(list) --* 

        A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).

        

      
        - *(string) --* 

        
    
      - **tags** *(list) --* 

        A map of entity tags attached to the affected entity.

        

      
        - *(dict) --* 

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
    
      - **eventStatusCodes** *(list) --* 

        A list of event status codes.

        

      
        - *(string) --* 

        
    
    
    :type nextToken: string
    :param nextToken: 

      If the results of a search are large, only a portion of the results are returned, and a ``nextToken`` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of items to return in one batch, between 10 and 100, inclusive.

      

    
    :type locale: string
    :param locale: 

      The locale (language) to return information in. English (en) is the default and the only supported value at this time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'events': [
                {
                    'arn': 'string',
                    'service': 'string',
                    'eventTypeCode': 'string',
                    'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange',
                    'region': 'string',
                    'availabilityZone': 'string',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'statusCode': 'open'|'closed'|'upcoming'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **events** *(list) --* 

          The events that match the specified filter criteria.

          
          

          - *(dict) --* 

            Summary information about an event, returned by the  DescribeEvents operation. The  DescribeEventDetails operation also returns this information, as well as the  EventDescription and additional event metadata.

            
            

            - **arn** *(string) --* 

              The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*EVENT_TYPE_PLUS_ID* `` . Example: ``arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331``  

              
            

            - **service** *(string) --* 

              The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

              
            

            - **eventTypeCode** *(string) --* 

              The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

              
            

            - **eventTypeCategory** *(string) --* 

              The 

              
            

            - **region** *(string) --* 

              The AWS region name of the event.

              
            

            - **availabilityZone** *(string) --* 

              The AWS Availability Zone of the event. For example, us-east-1a.

              
            

            - **startTime** *(datetime) --* 

              The date and time that the event began.

              
            

            - **endTime** *(datetime) --* 

              The date and time that the event ended.

              
            

            - **lastUpdatedTime** *(datetime) --* 

              The most recent date and time that the event was updated.

              
            

            - **statusCode** *(string) --* 

              The most recent status of the event. Possible values are ``open`` , ``closed`` , and ``upcoming`` .

              
        
      
        

        - **nextToken** *(string) --* 

          If the results of a search are large, only a portion of the results are returned, and a ``nextToken`` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

          
    

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

        


==========
Paginators
==========


The available paginators are:

* :py:class:`Health.Paginator.DescribeAffectedEntities`


* :py:class:`Health.Paginator.DescribeEventAggregates`


* :py:class:`Health.Paginator.DescribeEventTypes`


* :py:class:`Health.Paginator.DescribeEvents`



.. py:class:: Health.Paginator.DescribeAffectedEntities

  ::

    
    paginator = client.get_paginator('describe_affected_entities')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Health.Client.describe_affected_entities`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeAffectedEntities>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          filter={
              'eventArns': [
                  'string',
              ],
              'entityArns': [
                  'string',
              ],
              'entityValues': [
                  'string',
              ],
              'lastUpdatedTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'tags': [
                  {
                      'string': 'string'
                  },
              ],
              'statusCodes': [
                  'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
              ]
          },
          locale='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type filter: dict
    :param filter: **[REQUIRED]** 

      Values to narrow the results returned. At least one event ARN is required. 

      

    
      - **eventArns** *(list) --* **[REQUIRED]** 

        A list of event ARNs (unique identifiers). For example: ``"arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331", "arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz"``  

        

      
        - *(string) --* 

        
    
      - **entityArns** *(list) --* 

        A list of entity ARNs (unique identifiers).

        

      
        - *(string) --* 

        
    
      - **entityValues** *(list) --* 

        A list of IDs for affected entities.

        

      
        - *(string) --* 

        
    
      - **lastUpdatedTimes** *(list) --* 

        A list of the most recent dates and times that the entity was updated.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **tags** *(list) --* 

        A map of entity tags attached to the affected entity.

        

      
        - *(dict) --* 

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
    
      - **statusCodes** *(list) --* 

        A list of entity status codes (``IMPAIRED`` , ``UNIMPAIRED`` , or ``UNKNOWN`` ).

        

      
        - *(string) --* 

        
    
    
    :type locale: string
    :param locale: 

      The locale (language) to return information in. English (en) is the default and the only supported value at this time.

      

    
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
            'entities': [
                {
                    'entityArn': 'string',
                    'eventArn': 'string',
                    'entityValue': 'string',
                    'awsAccountId': 'string',
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'statusCode': 'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
                    'tags': {
                        'string': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **entities** *(list) --* 

          The entities that match the filter criteria.

          
          

          - *(dict) --* 

            Information about an entity that is affected by a Health event.

            
            

            - **entityArn** *(string) --* 

              The unique identifier for the entity. Format: ``arn:aws:health:*entity-region* :*aws-account* :entity/*entity-id* `` . Example: ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K``  

              
            

            - **eventArn** *(string) --* 

              The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*EVENT_TYPE_PLUS_ID* `` . Example: ``arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331``  

              
            

            - **entityValue** *(string) --* 

              The ID of the affected entity.

              
            

            - **awsAccountId** *(string) --* 

              The 12-digit AWS account number that contains the affected entity.

              
            

            - **lastUpdatedTime** *(datetime) --* 

              The most recent time that the entity was updated.

              
            

            - **statusCode** *(string) --* 

              The most recent status of the entity affected by the event. The possible values are ``IMPAIRED`` , ``UNIMPAIRED`` , and ``UNKNOWN`` .

              
            

            - **tags** *(dict) --* 

              A map of entity tags attached to the affected entity.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Health.Paginator.DescribeEventAggregates

  ::

    
    paginator = client.get_paginator('describe_event_aggregates')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Health.Client.describe_event_aggregates`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventAggregates>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          filter={
              'eventArns': [
                  'string',
              ],
              'eventTypeCodes': [
                  'string',
              ],
              'services': [
                  'string',
              ],
              'regions': [
                  'string',
              ],
              'availabilityZones': [
                  'string',
              ],
              'startTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'endTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'lastUpdatedTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'entityArns': [
                  'string',
              ],
              'entityValues': [
                  'string',
              ],
              'eventTypeCategories': [
                  'issue'|'accountNotification'|'scheduledChange',
              ],
              'tags': [
                  {
                      'string': 'string'
                  },
              ],
              'eventStatusCodes': [
                  'open'|'closed'|'upcoming',
              ]
          },
          aggregateField='eventTypeCategory',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type filter: dict
    :param filter: 

      Values to narrow the results returned.

      

    
      - **eventArns** *(list) --* 

        A list of event ARNs (unique identifiers). For example: ``"arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331", "arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz"``  

        

      
        - *(string) --* 

        
    
      - **eventTypeCodes** *(list) --* 

        A list of unique identifiers for event types. For example, ``"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"``  

        

      
        - *(string) --* 

        
    
      - **services** *(list) --* 

        The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

        

      
        - *(string) --* 

        
    
      - **regions** *(list) --* 

        A list of AWS regions.

        

      
        - *(string) --* 

        
    
      - **availabilityZones** *(list) --* 

        A list of AWS availability zones.

        

      
        - *(string) --* 

        
    
      - **startTimes** *(list) --* 

        A list of dates and times that the event began.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **endTimes** *(list) --* 

        A list of dates and times that the event ended.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **lastUpdatedTimes** *(list) --* 

        A list of dates and times that the event was last updated.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **entityArns** *(list) --* 

        A list of entity ARNs (unique identifiers).

        

      
        - *(string) --* 

        
    
      - **entityValues** *(list) --* 

        A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes (``vol-426ab23e`` ).

        

      
        - *(string) --* 

        
    
      - **eventTypeCategories** *(list) --* 

        A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).

        

      
        - *(string) --* 

        
    
      - **tags** *(list) --* 

        A map of entity tags attached to the affected entity.

        

      
        - *(dict) --* 

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
    
      - **eventStatusCodes** *(list) --* 

        A list of event status codes.

        

      
        - *(string) --* 

        
    
    
    :type aggregateField: string
    :param aggregateField: **[REQUIRED]** 

      The only currently supported value is ``eventTypeCategory`` .

      

    
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
            'eventAggregates': [
                {
                    'aggregateValue': 'string',
                    'count': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **eventAggregates** *(list) --* 

          The number of events in each category that meet the optional filter criteria.

          
          

          - *(dict) --* 

            The number of events of each issue type. Returned by the  DescribeEventAggregates operation.

            
            

            - **aggregateValue** *(string) --* 

              The issue type for the associated count.

              
            

            - **count** *(integer) --* 

              The number of events of the associated issue type.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Health.Paginator.DescribeEventTypes

  ::

    
    paginator = client.get_paginator('describe_event_types')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Health.Client.describe_event_types`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventTypes>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          filter={
              'eventTypeCodes': [
                  'string',
              ],
              'services': [
                  'string',
              ],
              'eventTypeCategories': [
                  'issue'|'accountNotification'|'scheduledChange',
              ]
          },
          locale='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type filter: dict
    :param filter: 

      Values to narrow the results returned.

      

    
      - **eventTypeCodes** *(list) --* 

        A list of event type codes.

        

      
        - *(string) --* 

        
    
      - **services** *(list) --* 

        The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

        

      
        - *(string) --* 

        
    
      - **eventTypeCategories** *(list) --* 

        A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).

        

      
        - *(string) --* 

        
    
    
    :type locale: string
    :param locale: 

      The locale (language) to return information in. English (en) is the default and the only supported value at this time.

      

    
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
            'eventTypes': [
                {
                    'service': 'string',
                    'code': 'string',
                    'category': 'issue'|'accountNotification'|'scheduledChange'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **eventTypes** *(list) --* 

          A list of event types that match the filter criteria. Event types have a category (``issue`` , ``accountNotification`` , or ``scheduledChange`` ), a service (for example, ``EC2`` , ``RDS`` , ``DATAPIPELINE`` , ``BILLING`` ), and a code (in the format ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

          
          

          - *(dict) --* 

            Metadata about a type of event that is reported by AWS Health. Data consists of the category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

            
            

            - **service** *(string) --* 

              The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

              
            

            - **code** *(string) --* 

              The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

              
            

            - **category** *(string) --* 

              A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Health.Paginator.DescribeEvents

  ::

    
    paginator = client.get_paginator('describe_events')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Health.Client.describe_events`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEvents>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          filter={
              'eventArns': [
                  'string',
              ],
              'eventTypeCodes': [
                  'string',
              ],
              'services': [
                  'string',
              ],
              'regions': [
                  'string',
              ],
              'availabilityZones': [
                  'string',
              ],
              'startTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'endTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'lastUpdatedTimes': [
                  {
                      'from': datetime(2015, 1, 1),
                      'to': datetime(2015, 1, 1)
                  },
              ],
              'entityArns': [
                  'string',
              ],
              'entityValues': [
                  'string',
              ],
              'eventTypeCategories': [
                  'issue'|'accountNotification'|'scheduledChange',
              ],
              'tags': [
                  {
                      'string': 'string'
                  },
              ],
              'eventStatusCodes': [
                  'open'|'closed'|'upcoming',
              ]
          },
          locale='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type filter: dict
    :param filter: 

      Values to narrow the results returned.

      

    
      - **eventArns** *(list) --* 

        A list of event ARNs (unique identifiers). For example: ``"arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331", "arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz"``  

        

      
        - *(string) --* 

        
    
      - **eventTypeCodes** *(list) --* 

        A list of unique identifiers for event types. For example, ``"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"``  

        

      
        - *(string) --* 

        
    
      - **services** *(list) --* 

        The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

        

      
        - *(string) --* 

        
    
      - **regions** *(list) --* 

        A list of AWS regions.

        

      
        - *(string) --* 

        
    
      - **availabilityZones** *(list) --* 

        A list of AWS availability zones.

        

      
        - *(string) --* 

        
    
      - **startTimes** *(list) --* 

        A list of dates and times that the event began.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **endTimes** *(list) --* 

        A list of dates and times that the event ended.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **lastUpdatedTimes** *(list) --* 

        A list of dates and times that the event was last updated.

        

      
        - *(dict) --* 

          A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .

          

        
          - **from** *(datetime) --* 

            The starting date and time of a time range.

            

          
          - **to** *(datetime) --* 

            The ending date and time of a time range.

            

          
        
    
      - **entityArns** *(list) --* 

        A list of entity ARNs (unique identifiers).

        

      
        - *(string) --* 

        
    
      - **entityValues** *(list) --* 

        A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes (``vol-426ab23e`` ).

        

      
        - *(string) --* 

        
    
      - **eventTypeCategories** *(list) --* 

        A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).

        

      
        - *(string) --* 

        
    
      - **tags** *(list) --* 

        A map of entity tags attached to the affected entity.

        

      
        - *(dict) --* 

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
    
      - **eventStatusCodes** *(list) --* 

        A list of event status codes.

        

      
        - *(string) --* 

        
    
    
    :type locale: string
    :param locale: 

      The locale (language) to return information in. English (en) is the default and the only supported value at this time.

      

    
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
                    'arn': 'string',
                    'service': 'string',
                    'eventTypeCode': 'string',
                    'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange',
                    'region': 'string',
                    'availabilityZone': 'string',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'statusCode': 'open'|'closed'|'upcoming'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **events** *(list) --* 

          The events that match the specified filter criteria.

          
          

          - *(dict) --* 

            Summary information about an event, returned by the  DescribeEvents operation. The  DescribeEventDetails operation also returns this information, as well as the  EventDescription and additional event metadata.

            
            

            - **arn** *(string) --* 

              The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*EVENT_TYPE_PLUS_ID* `` . Example: ``arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331``  

              
            

            - **service** *(string) --* 

              The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

              
            

            - **eventTypeCode** *(string) --* 

              The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

              
            

            - **eventTypeCategory** *(string) --* 

              The 

              
            

            - **region** *(string) --* 

              The AWS region name of the event.

              
            

            - **availabilityZone** *(string) --* 

              The AWS Availability Zone of the event. For example, us-east-1a.

              
            

            - **startTime** *(datetime) --* 

              The date and time that the event began.

              
            

            - **endTime** *(datetime) --* 

              The date and time that the event ended.

              
            

            - **lastUpdatedTime** *(datetime) --* 

              The most recent date and time that the event was updated.

              
            

            - **statusCode** *(string) --* 

              The most recent status of the event. Possible values are ``open`` , ``closed`` , and ``upcoming`` .

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    