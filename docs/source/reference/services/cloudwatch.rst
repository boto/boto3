

**********
CloudWatch
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CloudWatch.Client

  A low-level client representing Amazon CloudWatch::

    
    import boto3
    
    client = boto3.client('cloudwatch')

  
  These are the available methods:
  
  *   :py:meth:`~CloudWatch.Client.can_paginate`

  
  *   :py:meth:`~CloudWatch.Client.delete_alarms`

  
  *   :py:meth:`~CloudWatch.Client.delete_dashboards`

  
  *   :py:meth:`~CloudWatch.Client.describe_alarm_history`

  
  *   :py:meth:`~CloudWatch.Client.describe_alarms`

  
  *   :py:meth:`~CloudWatch.Client.describe_alarms_for_metric`

  
  *   :py:meth:`~CloudWatch.Client.disable_alarm_actions`

  
  *   :py:meth:`~CloudWatch.Client.enable_alarm_actions`

  
  *   :py:meth:`~CloudWatch.Client.generate_presigned_url`

  
  *   :py:meth:`~CloudWatch.Client.get_dashboard`

  
  *   :py:meth:`~CloudWatch.Client.get_metric_statistics`

  
  *   :py:meth:`~CloudWatch.Client.get_paginator`

  
  *   :py:meth:`~CloudWatch.Client.get_waiter`

  
  *   :py:meth:`~CloudWatch.Client.list_dashboards`

  
  *   :py:meth:`~CloudWatch.Client.list_metrics`

  
  *   :py:meth:`~CloudWatch.Client.put_dashboard`

  
  *   :py:meth:`~CloudWatch.Client.put_metric_alarm`

  
  *   :py:meth:`~CloudWatch.Client.put_metric_data`

  
  *   :py:meth:`~CloudWatch.Client.set_alarm_state`

  

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


  .. py:method:: delete_alarms(**kwargs)

    

    Deletes the specified alarms. In the event of an error, no alarms are deleted.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_    


    **Request Syntax** 
    ::

      response = client.delete_alarms(
          AlarmNames=[
              'string',
          ]
      )
    :type AlarmNames: list
    :param AlarmNames: **[REQUIRED]** 

      The alarms to be deleted.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: delete_dashboards(**kwargs)

    

    Deletes all dashboards that you specify. You may specify up to 100 dashboards to delete. If there is an error during this call, no dashboards are deleted.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteDashboards>`_    


    **Request Syntax** 
    ::

      response = client.delete_dashboards(
          DashboardNames=[
              'string',
          ]
      )
    :type DashboardNames: list
    :param DashboardNames: **[REQUIRED]** 

      The dashboards to be deleted. This parameter is required.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_alarm_history(**kwargs)

    

    Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for all alarms are returned.

     

    CloudWatch retains the history of an alarm even if you delete the alarm.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmHistory>`_    


    **Request Syntax** 
    ::

      response = client.describe_alarm_history(
          AlarmName='string',
          HistoryItemType='ConfigurationUpdate'|'StateUpdate'|'Action',
          StartDate=datetime(2015, 1, 1),
          EndDate=datetime(2015, 1, 1),
          MaxRecords=123,
          NextToken='string'
      )
    :type AlarmName: string
    :param AlarmName: 

      The name of the alarm.

      

    
    :type HistoryItemType: string
    :param HistoryItemType: 

      The type of alarm histories to retrieve.

      

    
    :type StartDate: datetime
    :param StartDate: 

      The starting date to retrieve alarm history.

      

    
    :type EndDate: datetime
    :param EndDate: 

      The ending date to retrieve alarm history.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of alarm history records to retrieve.

      

    
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to indicate that there is more data available.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AlarmHistoryItems': [
                {
                    'AlarmName': 'string',
                    'Timestamp': datetime(2015, 1, 1),
                    'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
                    'HistorySummary': 'string',
                    'HistoryData': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AlarmHistoryItems** *(list) --* 

          The alarm histories, in JSON format.

          
          

          - *(dict) --* 

            Represents the history of a specific alarm.

            
            

            - **AlarmName** *(string) --* 

              The descriptive name for the alarm.

              
            

            - **Timestamp** *(datetime) --* 

              The time stamp for the alarm history item.

              
            

            - **HistoryItemType** *(string) --* 

              The type of alarm history item.

              
            

            - **HistorySummary** *(string) --* 

              A summary of the alarm history, in text format.

              
            

            - **HistoryData** *(string) --* 

              Data about the alarm, in JSON format.

              
        
      
        

        - **NextToken** *(string) --* 

          The token that marks the start of the next batch of returned results.

          
    

  .. py:method:: describe_alarms(**kwargs)

    

    Retrieves the specified alarms. If no alarms are specified, all alarms are returned. Alarms can be retrieved by using only a prefix for the alarm name, the alarm state, or a prefix for any action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_    


    **Request Syntax** 
    ::

      response = client.describe_alarms(
          AlarmNames=[
              'string',
          ],
          AlarmNamePrefix='string',
          StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
          ActionPrefix='string',
          MaxRecords=123,
          NextToken='string'
      )
    :type AlarmNames: list
    :param AlarmNames: 

      The names of the alarms.

      

    
      - *(string) --* 

      
  
    :type AlarmNamePrefix: string
    :param AlarmNamePrefix: 

      The alarm name prefix. If this parameter is specified, you cannot specify ``AlarmNames`` .

      

    
    :type StateValue: string
    :param StateValue: 

      The state value to be used in matching alarms.

      

    
    :type ActionPrefix: string
    :param ActionPrefix: 

      The action name prefix.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of alarm descriptions to retrieve.

      

    
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to indicate that there is more data available.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MetricAlarms': [
                {
                    'AlarmName': 'string',
                    'AlarmArn': 'string',
                    'AlarmDescription': 'string',
                    'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                    'ActionsEnabled': True|False,
                    'OKActions': [
                        'string',
                    ],
                    'AlarmActions': [
                        'string',
                    ],
                    'InsufficientDataActions': [
                        'string',
                    ],
                    'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                    'StateReason': 'string',
                    'StateReasonData': 'string',
                    'StateUpdatedTimestamp': datetime(2015, 1, 1),
                    'MetricName': 'string',
                    'Namespace': 'string',
                    'Statistic': 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
                    'ExtendedStatistic': 'string',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'Period': 123,
                    'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                    'EvaluationPeriods': 123,
                    'DatapointsToAlarm': 123,
                    'Threshold': 123.0,
                    'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                    'TreatMissingData': 'string',
                    'EvaluateLowSampleCountPercentile': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **MetricAlarms** *(list) --* 

          The information for the specified alarms.

          
          

          - *(dict) --* 

            Represents an alarm.

            
            

            - **AlarmName** *(string) --* 

              The name of the alarm.

              
            

            - **AlarmArn** *(string) --* 

              The Amazon Resource Name (ARN) of the alarm.

              
            

            - **AlarmDescription** *(string) --* 

              The description of the alarm.

              
            

            - **AlarmConfigurationUpdatedTimestamp** *(datetime) --* 

              The time stamp of the last update to the alarm configuration.

              
            

            - **ActionsEnabled** *(boolean) --* 

              Indicates whether actions should be executed during any changes to the alarm state.

              
            

            - **OKActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **AlarmActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``ALARM`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **InsufficientDataActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **StateValue** *(string) --* 

              The state value for the alarm.

              
            

            - **StateReason** *(string) --* 

              An explanation for the alarm state, in text format.

              
            

            - **StateReasonData** *(string) --* 

              An explanation for the alarm state, in JSON format.

              
            

            - **StateUpdatedTimestamp** *(datetime) --* 

              The time stamp of the last update to the alarm state.

              
            

            - **MetricName** *(string) --* 

              The name of the metric associated with the alarm.

              
            

            - **Namespace** *(string) --* 

              The namespace of the metric associated with the alarm.

              
            

            - **Statistic** *(string) --* 

              The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` .

              
            

            - **ExtendedStatistic** *(string) --* 

              The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

              
            

            - **Dimensions** *(list) --* 

              The dimensions for the metric associated with the alarm.

              
              

              - *(dict) --* 

                Expands the identity of a metric.

                
                

                - **Name** *(string) --* 

                  The name of the dimension.

                  
                

                - **Value** *(string) --* 

                  The value representing the dimension measurement.

                  
            
          
            

            - **Period** *(integer) --* 

              The period, in seconds, over which the statistic is applied.

              
            

            - **Unit** *(string) --* 

              The unit of the metric associated with the alarm.

              
            

            - **EvaluationPeriods** *(integer) --* 

              The number of periods over which data is compared to the specified threshold.

              
            

            - **DatapointsToAlarm** *(integer) --* 

              The number of datapoints that must be breaching to trigger the alarm.

              
            

            - **Threshold** *(float) --* 

              The value to compare with the specified statistic.

              
            

            - **ComparisonOperator** *(string) --* 

              The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

              
            

            - **TreatMissingData** *(string) --* 

              Sets how this alarm is to handle missing data points. If this parameter is omitted, the default behavior of ``missing`` is used.

              
            

            - **EvaluateLowSampleCountPercentile** *(string) --* 

              Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

              
        
      
        

        - **NextToken** *(string) --* 

          The token that marks the start of the next batch of returned results.

          
    

  .. py:method:: describe_alarms_for_metric(**kwargs)

    

    Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_    


    **Request Syntax** 
    ::

      response = client.describe_alarms_for_metric(
          MetricName='string',
          Namespace='string',
          Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
          ExtendedStatistic='string',
          Dimensions=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          Period=123,
          Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
      )
    :type MetricName: string
    :param MetricName: **[REQUIRED]** 

      The name of the metric.

      

    
    :type Namespace: string
    :param Namespace: **[REQUIRED]** 

      The namespace of the metric.

      

    
    :type Statistic: string
    :param Statistic: 

      The statistic for the metric, other than percentiles. For percentile statistics, use ``ExtendedStatistics`` .

      

    
    :type ExtendedStatistic: string
    :param ExtendedStatistic: 

      The percentile statistic for the metric. Specify a value between p0.0 and p100.

      

    
    :type Dimensions: list
    :param Dimensions: 

      The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.

      

    
      - *(dict) --* 

        Expands the identity of a metric.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the dimension.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value representing the dimension measurement.

          

        
      
  
    :type Period: integer
    :param Period: 

      The period, in seconds, over which the statistic is applied.

      

    
    :type Unit: string
    :param Unit: 

      The unit for the metric.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MetricAlarms': [
                {
                    'AlarmName': 'string',
                    'AlarmArn': 'string',
                    'AlarmDescription': 'string',
                    'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                    'ActionsEnabled': True|False,
                    'OKActions': [
                        'string',
                    ],
                    'AlarmActions': [
                        'string',
                    ],
                    'InsufficientDataActions': [
                        'string',
                    ],
                    'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                    'StateReason': 'string',
                    'StateReasonData': 'string',
                    'StateUpdatedTimestamp': datetime(2015, 1, 1),
                    'MetricName': 'string',
                    'Namespace': 'string',
                    'Statistic': 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
                    'ExtendedStatistic': 'string',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'Period': 123,
                    'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                    'EvaluationPeriods': 123,
                    'DatapointsToAlarm': 123,
                    'Threshold': 123.0,
                    'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                    'TreatMissingData': 'string',
                    'EvaluateLowSampleCountPercentile': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **MetricAlarms** *(list) --* 

          The information for each alarm with the specified metric.

          
          

          - *(dict) --* 

            Represents an alarm.

            
            

            - **AlarmName** *(string) --* 

              The name of the alarm.

              
            

            - **AlarmArn** *(string) --* 

              The Amazon Resource Name (ARN) of the alarm.

              
            

            - **AlarmDescription** *(string) --* 

              The description of the alarm.

              
            

            - **AlarmConfigurationUpdatedTimestamp** *(datetime) --* 

              The time stamp of the last update to the alarm configuration.

              
            

            - **ActionsEnabled** *(boolean) --* 

              Indicates whether actions should be executed during any changes to the alarm state.

              
            

            - **OKActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **AlarmActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``ALARM`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **InsufficientDataActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **StateValue** *(string) --* 

              The state value for the alarm.

              
            

            - **StateReason** *(string) --* 

              An explanation for the alarm state, in text format.

              
            

            - **StateReasonData** *(string) --* 

              An explanation for the alarm state, in JSON format.

              
            

            - **StateUpdatedTimestamp** *(datetime) --* 

              The time stamp of the last update to the alarm state.

              
            

            - **MetricName** *(string) --* 

              The name of the metric associated with the alarm.

              
            

            - **Namespace** *(string) --* 

              The namespace of the metric associated with the alarm.

              
            

            - **Statistic** *(string) --* 

              The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` .

              
            

            - **ExtendedStatistic** *(string) --* 

              The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

              
            

            - **Dimensions** *(list) --* 

              The dimensions for the metric associated with the alarm.

              
              

              - *(dict) --* 

                Expands the identity of a metric.

                
                

                - **Name** *(string) --* 

                  The name of the dimension.

                  
                

                - **Value** *(string) --* 

                  The value representing the dimension measurement.

                  
            
          
            

            - **Period** *(integer) --* 

              The period, in seconds, over which the statistic is applied.

              
            

            - **Unit** *(string) --* 

              The unit of the metric associated with the alarm.

              
            

            - **EvaluationPeriods** *(integer) --* 

              The number of periods over which data is compared to the specified threshold.

              
            

            - **DatapointsToAlarm** *(integer) --* 

              The number of datapoints that must be breaching to trigger the alarm.

              
            

            - **Threshold** *(float) --* 

              The value to compare with the specified statistic.

              
            

            - **ComparisonOperator** *(string) --* 

              The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

              
            

            - **TreatMissingData** *(string) --* 

              Sets how this alarm is to handle missing data points. If this parameter is omitted, the default behavior of ``missing`` is used.

              
            

            - **EvaluateLowSampleCountPercentile** *(string) --* 

              Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

              
        
      
    

  .. py:method:: disable_alarm_actions(**kwargs)

    

    Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_    


    **Request Syntax** 
    ::

      response = client.disable_alarm_actions(
          AlarmNames=[
              'string',
          ]
      )
    :type AlarmNames: list
    :param AlarmNames: **[REQUIRED]** 

      The names of the alarms.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: enable_alarm_actions(**kwargs)

    

    Enables the actions for the specified alarms.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_    


    **Request Syntax** 
    ::

      response = client.enable_alarm_actions(
          AlarmNames=[
              'string',
          ]
      )
    :type AlarmNames: list
    :param AlarmNames: **[REQUIRED]** 

      The names of the alarms.

      

    
      - *(string) --* 

      
  
    
    :returns: None

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


  .. py:method:: get_dashboard(**kwargs)

    

    Displays the details of the dashboard that you specify.

     

    To copy an existing dashboard, use ``GetDashboard`` , and then use the data returned within ``DashboardBody`` as the template for the new dashboard when you call ``PutDashboard`` to create the copy.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetDashboard>`_    


    **Request Syntax** 
    ::

      response = client.get_dashboard(
          DashboardName='string'
      )
    :type DashboardName: string
    :param DashboardName: **[REQUIRED]** 

      The name of the dashboard to be described.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DashboardArn': 'string',
            'DashboardBody': 'string',
            'DashboardName': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DashboardArn** *(string) --* 

          The Amazon Resource Name (ARN) of the dashboard.

          
        

        - **DashboardBody** *(string) --* 

          The detailed information about the dashboard, including what widgets are included and their location on the dashboard. For more information about the ``DashboardBody`` syntax, see  CloudWatch-Dashboard-Body-Structure . 

          
        

        - **DashboardName** *(string) --* 

          The name of the dashboard.

          
    

  .. py:method:: get_metric_statistics(**kwargs)

    

    Gets statistics for the specified metric.

     

    The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order.

     

    CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.

     

    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:

     

     
    * The SampleCount value of the statistic set is 1. 
     
    * The Min and the Max values of the statistic set are equal. 
     

     

    Amazon CloudWatch retains metric data as follows:

     

     
    * Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a ``StorageResolution`` of 1. 
     
    * Data points with a period of 60 seconds (1-minute) are available for 15 days. 
     
    * Data points with a period of 300 seconds (5-minute) are available for 63 days. 
     
    * Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months). 
     

     

    Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.

     

    CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.

     

    For information about metrics and dimensions supported by AWS services, see the `Amazon CloudWatch Metrics and Dimensions Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetMetricStatistics>`_    


    **Request Syntax** 
    ::

      response = client.get_metric_statistics(
          Namespace='string',
          MetricName='string',
          Dimensions=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          Period=123,
          Statistics=[
              'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
          ],
          ExtendedStatistics=[
              'string',
          ],
          Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
      )
    :type Namespace: string
    :param Namespace: **[REQUIRED]** 

      The namespace of the metric, with or without spaces.

      

    
    :type MetricName: string
    :param MetricName: **[REQUIRED]** 

      The name of the metric, with or without spaces.

      

    
    :type Dimensions: list
    :param Dimensions: 

      The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can't retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see `Dimension Combinations <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-combinations>`__ in the *Amazon CloudWatch User Guide* . For more information about specifying dimensions, see `Publishing Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__ in the *Amazon CloudWatch User Guide* .

      

    
      - *(dict) --* 

        Expands the identity of a metric.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the dimension.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value representing the dimension measurement.

          

        
      
  
    :type StartTime: datetime
    :param StartTime: **[REQUIRED]** 

      The time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request.

       

      The value specified is inclusive; results include data points with the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).

       

      CloudWatch rounds the specified time stamp as follows:

       

       
      * Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00. 
       
      * Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00. 
       
      * Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00. 
       

       

      If you set ``Period`` to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. 

      

    
    :type EndTime: datetime
    :param EndTime: **[REQUIRED]** 

      The time stamp that determines the last data point to return.

       

      The value specified is exclusive; results include data points up to the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).

      

    
    :type Period: integer
    :param Period: **[REQUIRED]** 

      The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.

       

      If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

       

       
      * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute). 
       
      * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes). 
       
      * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour). 
       

      

    
    :type Statistics: list
    :param Statistics: 

      The metric statistics, other than percentile. For percentile statistics, use ``ExtendedStatistics`` . When calling ``GetMetricStatistics`` , you must specify either ``Statistics`` or ``ExtendedStatistics`` , but not both.

      

    
      - *(string) --* 

      
  
    :type ExtendedStatistics: list
    :param ExtendedStatistics: 

      The percentile statistics. Specify values between p0.0 and p100. When calling ``GetMetricStatistics`` , you must specify either ``Statistics`` or ``ExtendedStatistics`` , but not both.

      

    
      - *(string) --* 

      
  
    :type Unit: string
    :param Unit: 

      The unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If the metric only ever reports one unit, specifying a unit has no effect.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Label': 'string',
            'Datapoints': [
                {
                    'Timestamp': datetime(2015, 1, 1),
                    'SampleCount': 123.0,
                    'Average': 123.0,
                    'Sum': 123.0,
                    'Minimum': 123.0,
                    'Maximum': 123.0,
                    'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                    'ExtendedStatistics': {
                        'string': 123.0
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Label** *(string) --* 

          A label for the specified metric.

          
        

        - **Datapoints** *(list) --* 

          The data points for the specified metric.

          
          

          - *(dict) --* 

            Encapsulates the statistical data that CloudWatch computes from metric data.

            
            

            - **Timestamp** *(datetime) --* 

              The time stamp used for the data point.

              
            

            - **SampleCount** *(float) --* 

              The number of metric values that contributed to the aggregate value of this data point.

              
            

            - **Average** *(float) --* 

              The average of the metric values that correspond to the data point.

              
            

            - **Sum** *(float) --* 

              The sum of the metric values for the data point.

              
            

            - **Minimum** *(float) --* 

              The minimum metric value for the data point.

              
            

            - **Maximum** *(float) --* 

              The maximum metric value for the data point.

              
            

            - **Unit** *(string) --* 

              The standard unit for the data point.

              
            

            - **ExtendedStatistics** *(dict) --* 

              The percentile statistic for the data point.

              
              

              - *(string) --* 
                

                - *(float) --* 
          
        
        
      
    

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

        


  .. py:method:: list_dashboards(**kwargs)

    

    Returns a list of the dashboards for your account. If you include ``DashboardNamePrefix`` , only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListDashboards>`_    


    **Request Syntax** 
    ::

      response = client.list_dashboards(
          DashboardNamePrefix='string',
          NextToken='string'
      )
    :type DashboardNamePrefix: string
    :param DashboardNamePrefix: 

      If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, ".", "-", and "_". 

      

    
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to indicate that there is more data available.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DashboardEntries': [
                {
                    'DashboardName': 'string',
                    'DashboardArn': 'string',
                    'LastModified': datetime(2015, 1, 1),
                    'Size': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DashboardEntries** *(list) --* 

          The list of matching dashboards.

          
          

          - *(dict) --* 

            Represents a specific dashboard.

            
            

            - **DashboardName** *(string) --* 

              The name of the dashboard.

              
            

            - **DashboardArn** *(string) --* 

              The Amazon Resource Name (ARN) of the dashboard.

              
            

            - **LastModified** *(datetime) --* 

              The time stamp of when the dashboard was last modified, either by an API call or through the console. This number is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.

              
            

            - **Size** *(integer) --* 

              The size of the dashboard, in bytes.

              
        
      
        

        - **NextToken** *(string) --* 

          The token that marks the start of the next batch of returned results.

          
    

  .. py:method:: list_metrics(**kwargs)

    

    List the specified metrics. You can use the returned metrics with  GetMetricStatistics to obtain statistical data.

     

    Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls.

     

    After you create a metric, allow up to fifteen minutes before the metric appears. Statistics about the metric, however, are available sooner using  GetMetricStatistics .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_    


    **Request Syntax** 
    ::

      response = client.list_metrics(
          Namespace='string',
          MetricName='string',
          Dimensions=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          NextToken='string'
      )
    :type Namespace: string
    :param Namespace: 

      The namespace to filter against.

      

    
    :type MetricName: string
    :param MetricName: 

      The name of the metric to filter against.

      

    
    :type Dimensions: list
    :param Dimensions: 

      The dimensions to filter against.

      

    
      - *(dict) --* 

        Represents filters for a dimension.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The dimension name to be matched.

          

        
        - **Value** *(string) --* 

          The value of the dimension to be matched.

          

        
      
  
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to indicate that there is more data available.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Metrics': [
                {
                    'Namespace': 'string',
                    'MetricName': 'string',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Metrics** *(list) --* 

          The metrics.

          
          

          - *(dict) --* 

            Represents a specific metric.

            
            

            - **Namespace** *(string) --* 

              The namespace of the metric.

              
            

            - **MetricName** *(string) --* 

              The name of the metric.

              
            

            - **Dimensions** *(list) --* 

              The dimensions for the metric.

              
              

              - *(dict) --* 

                Expands the identity of a metric.

                
                

                - **Name** *(string) --* 

                  The name of the dimension.

                  
                

                - **Value** *(string) --* 

                  The value representing the dimension measurement.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          The token that marks the start of the next batch of returned results.

          
    

  .. py:method:: put_dashboard(**kwargs)

    

    Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here.

     

    You can have up to 500 dashboards per account. All dashboards in your account are global, not region-specific.

     

    A simple way to create a dashboard using ``PutDashboard`` is to copy an existing dashboard. To copy an existing dashboard using the console, you can load the dashboard and then use the View/edit source command in the Actions menu to display the JSON block for that dashboard. Another way to copy a dashboard is to use ``GetDashboard`` , and then use the data returned within ``DashboardBody`` as the template for the new dashboard when you call ``PutDashboard`` .

     

    When you create a dashboard with ``PutDashboard`` , a good practice is to add a text widget at the top of the dashboard with a message that the dashboard was created by script and should not be changed in the console. This message could also point console users to the location of the ``DashboardBody`` script or the CloudFormation template used to create the dashboard.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutDashboard>`_    


    **Request Syntax** 
    ::

      response = client.put_dashboard(
          DashboardName='string',
          DashboardBody='string'
      )
    :type DashboardName: string
    :param DashboardName: **[REQUIRED]** 

      The name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, "-", and "_". This parameter is required.

      

    
    :type DashboardBody: string
    :param DashboardBody: **[REQUIRED]** 

      The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required.

       

      For more information about the syntax, see  CloudWatch-Dashboard-Body-Structure .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DashboardValidationMessages': [
                {
                    'DataPath': 'string',
                    'Message': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DashboardValidationMessages** *(list) --* 

          If the input for ``PutDashboard`` was correct and the dashboard was successfully created or modified, this result is empty.

           

          If this result includes only warning messages, then the input was valid enough for the dashboard to be created or modified, but some elements of the dashboard may not render.

           

          If this result includes error messages, the input was not valid and the operation failed.

          
          

          - *(dict) --* 

            An error or warning for the operation.

            
            

            - **DataPath** *(string) --* 

              The data path related to the message.

              
            

            - **Message** *(string) --* 

              A message describing the error or warning.

              
        
      
    

  .. py:method:: put_metric_alarm(**kwargs)

    

    Creates or updates an alarm and associates it with the specified metric. Optionally, this operation can associate one or more Amazon SNS resources with the alarm.

     

    When this operation creates an alarm, the alarm state is immediately set to ``INSUFFICIENT_DATA`` . The alarm is evaluated and its state is set appropriately. Any actions associated with the state are then executed.

     

    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.

     

    If you are an IAM user, you must have Amazon EC2 permissions for some operations:

     

     
    * ``ec2:DescribeInstanceStatus`` and ``ec2:DescribeInstances`` for all alarms on EC2 instance status metrics 
     
    * ``ec2:StopInstances`` for alarms with stop actions 
     
    * ``ec2:TerminateInstances`` for alarms with terminate actions 
     
    * ``ec2:DescribeInstanceRecoveryAttribute`` and ``ec2:RecoverInstances`` for alarms with recover actions 
     

     

    If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still create an alarm, but the stop or terminate actions are not performed. However, if you are later granted the required permissions, the alarm actions that you created earlier are performed.

     

    If you are using an IAM role (for example, an EC2 instance profile), you cannot stop or terminate the instance using alarm actions. However, you can still see the alarm state and perform any other actions such as Amazon SNS notifications or Auto Scaling policies.

     

    If you are using temporary security credentials granted using AWS STS, you cannot stop or terminate an EC2 instance using alarm actions.

     

    You must create at least one stop, terminate, or reboot alarm using either the Amazon EC2 or CloudWatch consoles to create the **EC2ActionsAccess** IAM role. After this IAM role is created, you can create stop, terminate, or reboot alarms using a command-line interface or API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricAlarm>`_    


    **Request Syntax** 
    ::

      response = client.put_metric_alarm(
          AlarmName='string',
          AlarmDescription='string',
          ActionsEnabled=True|False,
          OKActions=[
              'string',
          ],
          AlarmActions=[
              'string',
          ],
          InsufficientDataActions=[
              'string',
          ],
          MetricName='string',
          Namespace='string',
          Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
          ExtendedStatistic='string',
          Dimensions=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          Period=123,
          Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
          EvaluationPeriods=123,
          DatapointsToAlarm=123,
          Threshold=123.0,
          ComparisonOperator='GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
          TreatMissingData='string',
          EvaluateLowSampleCountPercentile='string'
      )
    :type AlarmName: string
    :param AlarmName: **[REQUIRED]** 

      The name for the alarm. This name must be unique within the AWS account.

      

    
    :type AlarmDescription: string
    :param AlarmDescription: 

      The description for the alarm.

      

    
    :type ActionsEnabled: boolean
    :param ActionsEnabled: 

      Indicates whether actions should be executed during any changes to the alarm state.

      

    
    :type OKActions: list
    :param OKActions: 

      The actions to execute when this alarm transitions to an ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

       

      Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:sns:*region* :*account-id* :*sns-topic-name* | arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name*  

       

      Valid Values (for use with IAM roles): arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Reboot/1.0

      

    
      - *(string) --* 

      
  
    :type AlarmActions: list
    :param AlarmActions: 

      The actions to execute when this alarm transitions to the ``ALARM`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

       

      Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:sns:*region* :*account-id* :*sns-topic-name* | arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name*  

       

      Valid Values (for use with IAM roles): arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Reboot/1.0

      

    
      - *(string) --* 

      
  
    :type InsufficientDataActions: list
    :param InsufficientDataActions: 

      The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

       

      Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:sns:*region* :*account-id* :*sns-topic-name* | arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name*  

       

      Valid Values (for use with IAM roles): arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Reboot/1.0

      

    
      - *(string) --* 

      
  
    :type MetricName: string
    :param MetricName: **[REQUIRED]** 

      The name for the metric associated with the alarm.

      

    
    :type Namespace: string
    :param Namespace: **[REQUIRED]** 

      The namespace for the metric associated with the alarm.

      

    
    :type Statistic: string
    :param Statistic: 

      The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` . When you call ``PutMetricAlarm`` , you must specify either ``Statistic`` or ``ExtendedStatistic,`` but not both.

      

    
    :type ExtendedStatistic: string
    :param ExtendedStatistic: 

      The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. When you call ``PutMetricAlarm`` , you must specify either ``Statistic`` or ``ExtendedStatistic,`` but not both.

      

    
    :type Dimensions: list
    :param Dimensions: 

      The dimensions for the metric associated with the alarm.

      

    
      - *(dict) --* 

        Expands the identity of a metric.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the dimension.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value representing the dimension measurement.

          

        
      
  
    :type Period: integer
    :param Period: **[REQUIRED]** 

      The period, in seconds, over which the specified statistic is applied. Valid values are 10, 30, and any multiple of 60.

       

      Be sure to specify 10 or 30 only for metrics that are stored by a ``PutMetricData`` call with a ``StorageResolution`` of 1. If you specify a Period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see `Amazon CloudWatch Pricing <https://aws.amazon.com/cloudwatch/pricing/>`__ .

       

      An alarm's total current evaluation period can be no longer than one day, so ``Period`` multiplied by ``EvaluationPeriods`` cannot be more than 86,400 seconds.

      

    
    :type Unit: string
    :param Unit: 

      The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.

       

      If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, the CloudWatch alarm can get stuck in the ``INSUFFICIENT DATA`` state. 

      

    
    :type EvaluationPeriods: integer
    :param EvaluationPeriods: **[REQUIRED]** 

      The number of periods over which data is compared to the specified threshold. An alarm's total current evaluation period can be no longer than one day, so this number multiplied by ``Period`` cannot be more than 86,400 seconds.

      

    
    :type DatapointsToAlarm: integer
    :param DatapointsToAlarm: 

      The number of datapoints that must be breaching to trigger the alarm.

      

    
    :type Threshold: float
    :param Threshold: **[REQUIRED]** 

      The value against which the specified statistic is compared.

      

    
    :type ComparisonOperator: string
    :param ComparisonOperator: **[REQUIRED]** 

      The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

      

    
    :type TreatMissingData: string
    :param TreatMissingData: 

      Sets how this alarm is to handle missing data points. If ``TreatMissingData`` is omitted, the default behavior of ``missing`` is used. For more information, see `Configuring How CloudWatch Alarms Treats Missing Data <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`__ .

       

      Valid Values: ``breaching | notBreaching | ignore | missing``  

      

    
    :type EvaluateLowSampleCountPercentile: string
    :param EvaluateLowSampleCountPercentile: 

      Used only for alarms based on percentiles. If you specify ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If you specify ``evaluate`` or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see `Percentile-Based CloudWatch Alarms and Low Data Samples <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples>`__ .

       

      Valid Values: ``evaluate | ignore``  

      

    
    
    :returns: None

  .. py:method:: put_metric_data(**kwargs)

    

    Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to  ListMetrics .

     

    Each ``PutMetricData`` request is limited to 40 KB in size for HTTP POST requests.

     

    Although the ``Value`` parameter accepts numbers of type ``Double`` , CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.

     

    You can use up to 10 dimensions per metric to further clarify what data the metric collects. For more information about specifying dimensions, see `Publishing Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__ in the *Amazon CloudWatch User Guide* .

     

    Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for  GetMetricStatistics from the time they are submitted.

     

    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:

     

     
    * The SampleCount value of the statistic set is 1 
     
    * The Min and the Max values of the statistic set are equal 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricData>`_    


    **Request Syntax** 
    ::

      response = client.put_metric_data(
          Namespace='string',
          MetricData=[
              {
                  'MetricName': 'string',
                  'Dimensions': [
                      {
                          'Name': 'string',
                          'Value': 'string'
                      },
                  ],
                  'Timestamp': datetime(2015, 1, 1),
                  'Value': 123.0,
                  'StatisticValues': {
                      'SampleCount': 123.0,
                      'Sum': 123.0,
                      'Minimum': 123.0,
                      'Maximum': 123.0
                  },
                  'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                  'StorageResolution': 123
              },
          ]
      )
    :type Namespace: string
    :param Namespace: **[REQUIRED]** 

      The namespace for the metric data.

       

      You cannot specify a namespace that begins with "AWS/". Namespaces that begin with "AWS/" are reserved for use by Amazon Web Services products.

      

    
    :type MetricData: list
    :param MetricData: **[REQUIRED]** 

      The data for the metric.

      

    
      - *(dict) --* 

        Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.

        

      
        - **MetricName** *(string) --* **[REQUIRED]** 

          The name of the metric.

          

        
        - **Dimensions** *(list) --* 

          The dimensions associated with the metric.

          

        
          - *(dict) --* 

            Expands the identity of a metric.

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the dimension.

              

            
            - **Value** *(string) --* **[REQUIRED]** 

              The value representing the dimension measurement.

              

            
          
      
        - **Timestamp** *(datetime) --* 

          The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.

          

        
        - **Value** *(float) --* 

          The value for the metric.

           

          Although the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.

          

        
        - **StatisticValues** *(dict) --* 

          The statistical values for the metric.

          

        
          - **SampleCount** *(float) --* **[REQUIRED]** 

            The number of samples used for the statistic set.

            

          
          - **Sum** *(float) --* **[REQUIRED]** 

            The sum of values for the sample set.

            

          
          - **Minimum** *(float) --* **[REQUIRED]** 

            The minimum value of the sample set.

            

          
          - **Maximum** *(float) --* **[REQUIRED]** 

            The maximum value of the sample set.

            

          
        
        - **Unit** *(string) --* 

          The unit of the metric.

          

        
        - **StorageResolution** *(integer) --* 

          Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see `High-Resolution Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#high-resolution-metrics>`__ in the *Amazon CloudWatch User Guide* . 

           

          This field is optional, if you do not specify it the default of 60 is used.

          

        
      
  
    
    :returns: None

  .. py:method:: set_alarm_state(**kwargs)

    

    Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ``ALARM`` sends an SNS message. The alarm returns to its actual state (often within seconds). Because the alarm state change happens quickly, it is typically only visible in the alarm's **History** tab in the Amazon CloudWatch console or through  DescribeAlarmHistory .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/SetAlarmState>`_    


    **Request Syntax** 
    ::

      response = client.set_alarm_state(
          AlarmName='string',
          StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
          StateReason='string',
          StateReasonData='string'
      )
    :type AlarmName: string
    :param AlarmName: **[REQUIRED]** 

      The name for the alarm. This name must be unique within the AWS account. The maximum length is 255 characters.

      

    
    :type StateValue: string
    :param StateValue: **[REQUIRED]** 

      The value of the state.

      

    
    :type StateReason: string
    :param StateReason: **[REQUIRED]** 

      The reason that this alarm is set to this specific state, in text format.

      

    
    :type StateReasonData: string
    :param StateReasonData: 

      The reason that this alarm is set to this specific state, in JSON format.

      

    
    
    :returns: None

==========
Paginators
==========


The available paginators are:

* :py:class:`CloudWatch.Paginator.DescribeAlarmHistory`


* :py:class:`CloudWatch.Paginator.DescribeAlarms`


* :py:class:`CloudWatch.Paginator.ListMetrics`



.. py:class:: CloudWatch.Paginator.DescribeAlarmHistory

  ::

    
    paginator = client.get_paginator('describe_alarm_history')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatch.Client.describe_alarm_history`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmHistory>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          AlarmName='string',
          HistoryItemType='ConfigurationUpdate'|'StateUpdate'|'Action',
          StartDate=datetime(2015, 1, 1),
          EndDate=datetime(2015, 1, 1),
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type AlarmName: string
    :param AlarmName: 

      The name of the alarm.

      

    
    :type HistoryItemType: string
    :param HistoryItemType: 

      The type of alarm histories to retrieve.

      

    
    :type StartDate: datetime
    :param StartDate: 

      The starting date to retrieve alarm history.

      

    
    :type EndDate: datetime
    :param EndDate: 

      The ending date to retrieve alarm history.

      

    
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
            'AlarmHistoryItems': [
                {
                    'AlarmName': 'string',
                    'Timestamp': datetime(2015, 1, 1),
                    'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
                    'HistorySummary': 'string',
                    'HistoryData': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AlarmHistoryItems** *(list) --* 

          The alarm histories, in JSON format.

          
          

          - *(dict) --* 

            Represents the history of a specific alarm.

            
            

            - **AlarmName** *(string) --* 

              The descriptive name for the alarm.

              
            

            - **Timestamp** *(datetime) --* 

              The time stamp for the alarm history item.

              
            

            - **HistoryItemType** *(string) --* 

              The type of alarm history item.

              
            

            - **HistorySummary** *(string) --* 

              A summary of the alarm history, in text format.

              
            

            - **HistoryData** *(string) --* 

              Data about the alarm, in JSON format.

              
        
      
    

.. py:class:: CloudWatch.Paginator.DescribeAlarms

  ::

    
    paginator = client.get_paginator('describe_alarms')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatch.Client.describe_alarms`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          AlarmNames=[
              'string',
          ],
          AlarmNamePrefix='string',
          StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
          ActionPrefix='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type AlarmNames: list
    :param AlarmNames: 

      The names of the alarms.

      

    
      - *(string) --* 

      
  
    :type AlarmNamePrefix: string
    :param AlarmNamePrefix: 

      The alarm name prefix. If this parameter is specified, you cannot specify ``AlarmNames`` .

      

    
    :type StateValue: string
    :param StateValue: 

      The state value to be used in matching alarms.

      

    
    :type ActionPrefix: string
    :param ActionPrefix: 

      The action name prefix.

      

    
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
            'MetricAlarms': [
                {
                    'AlarmName': 'string',
                    'AlarmArn': 'string',
                    'AlarmDescription': 'string',
                    'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                    'ActionsEnabled': True|False,
                    'OKActions': [
                        'string',
                    ],
                    'AlarmActions': [
                        'string',
                    ],
                    'InsufficientDataActions': [
                        'string',
                    ],
                    'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                    'StateReason': 'string',
                    'StateReasonData': 'string',
                    'StateUpdatedTimestamp': datetime(2015, 1, 1),
                    'MetricName': 'string',
                    'Namespace': 'string',
                    'Statistic': 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
                    'ExtendedStatistic': 'string',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'Period': 123,
                    'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                    'EvaluationPeriods': 123,
                    'DatapointsToAlarm': 123,
                    'Threshold': 123.0,
                    'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                    'TreatMissingData': 'string',
                    'EvaluateLowSampleCountPercentile': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **MetricAlarms** *(list) --* 

          The information for the specified alarms.

          
          

          - *(dict) --* 

            Represents an alarm.

            
            

            - **AlarmName** *(string) --* 

              The name of the alarm.

              
            

            - **AlarmArn** *(string) --* 

              The Amazon Resource Name (ARN) of the alarm.

              
            

            - **AlarmDescription** *(string) --* 

              The description of the alarm.

              
            

            - **AlarmConfigurationUpdatedTimestamp** *(datetime) --* 

              The time stamp of the last update to the alarm configuration.

              
            

            - **ActionsEnabled** *(boolean) --* 

              Indicates whether actions should be executed during any changes to the alarm state.

              
            

            - **OKActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **AlarmActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``ALARM`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **InsufficientDataActions** *(list) --* 

              The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

              
              

              - *(string) --* 
          
            

            - **StateValue** *(string) --* 

              The state value for the alarm.

              
            

            - **StateReason** *(string) --* 

              An explanation for the alarm state, in text format.

              
            

            - **StateReasonData** *(string) --* 

              An explanation for the alarm state, in JSON format.

              
            

            - **StateUpdatedTimestamp** *(datetime) --* 

              The time stamp of the last update to the alarm state.

              
            

            - **MetricName** *(string) --* 

              The name of the metric associated with the alarm.

              
            

            - **Namespace** *(string) --* 

              The namespace of the metric associated with the alarm.

              
            

            - **Statistic** *(string) --* 

              The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` .

              
            

            - **ExtendedStatistic** *(string) --* 

              The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

              
            

            - **Dimensions** *(list) --* 

              The dimensions for the metric associated with the alarm.

              
              

              - *(dict) --* 

                Expands the identity of a metric.

                
                

                - **Name** *(string) --* 

                  The name of the dimension.

                  
                

                - **Value** *(string) --* 

                  The value representing the dimension measurement.

                  
            
          
            

            - **Period** *(integer) --* 

              The period, in seconds, over which the statistic is applied.

              
            

            - **Unit** *(string) --* 

              The unit of the metric associated with the alarm.

              
            

            - **EvaluationPeriods** *(integer) --* 

              The number of periods over which data is compared to the specified threshold.

              
            

            - **DatapointsToAlarm** *(integer) --* 

              The number of datapoints that must be breaching to trigger the alarm.

              
            

            - **Threshold** *(float) --* 

              The value to compare with the specified statistic.

              
            

            - **ComparisonOperator** *(string) --* 

              The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

              
            

            - **TreatMissingData** *(string) --* 

              Sets how this alarm is to handle missing data points. If this parameter is omitted, the default behavior of ``missing`` is used.

              
            

            - **EvaluateLowSampleCountPercentile** *(string) --* 

              Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

              
        
      
    

.. py:class:: CloudWatch.Paginator.ListMetrics

  ::

    
    paginator = client.get_paginator('list_metrics')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudWatch.Client.list_metrics`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Namespace='string',
          MetricName='string',
          Dimensions=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type Namespace: string
    :param Namespace: 

      The namespace to filter against.

      

    
    :type MetricName: string
    :param MetricName: 

      The name of the metric to filter against.

      

    
    :type Dimensions: list
    :param Dimensions: 

      The dimensions to filter against.

      

    
      - *(dict) --* 

        Represents filters for a dimension.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The dimension name to be matched.

          

        
        - **Value** *(string) --* 

          The value of the dimension to be matched.

          

        
      
  
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
            'Metrics': [
                {
                    'Namespace': 'string',
                    'MetricName': 'string',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Metrics** *(list) --* 

          The metrics.

          
          

          - *(dict) --* 

            Represents a specific metric.

            
            

            - **Namespace** *(string) --* 

              The namespace of the metric.

              
            

            - **MetricName** *(string) --* 

              The name of the metric.

              
            

            - **Dimensions** *(list) --* 

              The dimensions for the metric.

              
              

              - *(dict) --* 

                Expands the identity of a metric.

                
                

                - **Name** *(string) --* 

                  The name of the dimension.

                  
                

                - **Value** *(string) --* 

                  The value representing the dimension measurement.

                  
            
          
        
      
    

=======
Waiters
=======


The available waiters are:

* :py:class:`CloudWatch.Waiter.AlarmExists`



.. py:class:: CloudWatch.Waiter.AlarmExists

  ::

    
    waiter = client.get_waiter('alarm_exists')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`CloudWatch.Client.describe_alarms` every 5 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          AlarmNames=[
              'string',
          ],
          AlarmNamePrefix='string',
          StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
          ActionPrefix='string',
          MaxRecords=123,
          NextToken='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type AlarmNames: list
    :param AlarmNames: 

      The names of the alarms.

      

    
      - *(string) --* 

      
  
    :type AlarmNamePrefix: string
    :param AlarmNamePrefix: 

      The alarm name prefix. If this parameter is specified, you cannot specify ``AlarmNames`` .

      

    
    :type StateValue: string
    :param StateValue: 

      The state value to be used in matching alarms.

      

    
    :type ActionPrefix: string
    :param ActionPrefix: 

      The action name prefix.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of alarm descriptions to retrieve.

      

    
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to indicate that there is more data available.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 5

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

================
Service Resource
================



.. py:class:: CloudWatch.ServiceResource()

  A resource representing Amazon CloudWatch::

    
    import boto3
    
    cloudwatch = boto3.resource('cloudwatch')

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Alarm()`

  
  *   :py:meth:`Metric()`

  
  These are the resource's available collections:
  
  *   :py:attr:`alarms`

  
  *   :py:attr:`metrics`

  
  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Alarm(name)

    Creates a Alarm resource.::

      alarm = cloudwatch.Alarm('name')

    :type name: string
    :param name: The Alarm's name identifier. This **must** be set.
    
    :rtype: :py:class:`CloudWatch.Alarm`
    :returns: A Alarm resource
    

  .. py:method:: Metric(namespace,name)

    Creates a Metric resource.::

      metric = cloudwatch.Metric('namespace','name')

    :type namespace: string
    :param namespace: The Metric's namespace identifier. This **must** be set.
    :type name: string
    :param name: The Metric's name identifier. This **must** be set.
    
    :rtype: :py:class:`CloudWatch.Metric`
    :returns: A Metric resource
    
  .. rst-class:: admonition-title
  
  Collections
  
  Collections provide an interface to iterate over and manipulate groups of resources. 
  For more information about collections refer to the :ref:`Resources Introduction Guide<guide_collections>`.
  

  .. py:attribute:: alarms

    A collection of Alarm resources

    .. py:method:: all()

      Creates an iterable of all Alarm resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_      


      **Request Syntax** 
      ::

        alarm_iterator = cloudwatch.alarms.all()
        
      
      :rtype: list(:py:class:`cloudwatch.Alarm`)
      :returns: A list of Alarm resources
      

    .. py:method:: delete()

      

      Deletes the specified alarms. In the event of an error, no alarms are deleted.

      

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_      


      **Request Syntax** 
      ::

        response = cloudwatch.alarms.delete()
        
      
      :returns: None

    .. py:method:: disable_actions()

      

      Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.

      

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_      


      **Request Syntax** 
      ::

        response = cloudwatch.alarms.disable_actions()
        
      
      :returns: None

    .. py:method:: enable_actions()

      

      Enables the actions for the specified alarms.

      

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_      


      **Request Syntax** 
      ::

        response = cloudwatch.alarms.enable_actions()
        
      
      :returns: None

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Alarm resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_      


      **Request Syntax** 
      ::

        alarm_iterator = cloudwatch.alarms.filter(
            AlarmNames=[
                'string',
            ],
            AlarmNamePrefix='string',
            StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
            ActionPrefix='string',
            MaxRecords=123,
            NextToken='string'
        )
      :type AlarmNames: list
      :param AlarmNames: 

        The names of the alarms.

        

      
        - *(string) --* 

        
    
      :type AlarmNamePrefix: string
      :param AlarmNamePrefix: 

        The alarm name prefix. If this parameter is specified, you cannot specify ``AlarmNames`` .

        

      
      :type StateValue: string
      :param StateValue: 

        The state value to be used in matching alarms.

        

      
      :type ActionPrefix: string
      :param ActionPrefix: 

        The action name prefix.

        

      
      :type MaxRecords: integer
      :param MaxRecords: 

        The maximum number of alarm descriptions to retrieve.

        

      
      :type NextToken: string
      :param NextToken: 

        The token returned by a previous call to indicate that there is more data available.

        

      
      
      :rtype: list(:py:class:`cloudwatch.Alarm`)
      :returns: A list of Alarm resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Alarm resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_      


      **Request Syntax** 
      ::

        alarm_iterator = cloudwatch.alarms.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`cloudwatch.Alarm`)
      :returns: A list of Alarm resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Alarm resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_      


      **Request Syntax** 
      ::

        alarm_iterator = cloudwatch.alarms.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`cloudwatch.Alarm`)
      :returns: A list of Alarm resources
      

  .. py:attribute:: metrics

    A collection of Metric resources

    .. py:method:: all()

      Creates an iterable of all Metric resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_      


      **Request Syntax** 
      ::

        metric_iterator = cloudwatch.metrics.all()
        
      
      :rtype: list(:py:class:`cloudwatch.Metric`)
      :returns: A list of Metric resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Metric resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_      


      **Request Syntax** 
      ::

        metric_iterator = cloudwatch.metrics.filter(
            Namespace='string',
            MetricName='string',
            Dimensions=[
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            NextToken='string'
        )
      :type Namespace: string
      :param Namespace: 

        The namespace to filter against.

        

      
      :type MetricName: string
      :param MetricName: 

        The name of the metric to filter against.

        

      
      :type Dimensions: list
      :param Dimensions: 

        The dimensions to filter against.

        

      
        - *(dict) --* 

          Represents filters for a dimension.

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The dimension name to be matched.

            

          
          - **Value** *(string) --* 

            The value of the dimension to be matched.

            

          
        
    
      :type NextToken: string
      :param NextToken: 

        The token returned by a previous call to indicate that there is more data available.

        

      
      
      :rtype: list(:py:class:`cloudwatch.Metric`)
      :returns: A list of Metric resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Metric resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_      


      **Request Syntax** 
      ::

        metric_iterator = cloudwatch.metrics.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`cloudwatch.Metric`)
      :returns: A list of Metric resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Metric resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_      


      **Request Syntax** 
      ::

        metric_iterator = cloudwatch.metrics.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`cloudwatch.Metric`)
      :returns: A list of Metric resources
      

=====
Alarm
=====



.. py:class:: CloudWatch.Alarm(name)

  A resource representing an Amazon CloudWatch Alarm::

    
    import boto3
    
    cloudwatch = boto3.resource('cloudwatch')
    alarm = cloudwatch.Alarm('name')

  :type name: string
  :param name: The Alarm's name identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`name`

  
  These are the resource's available attributes:
  
  *   :py:attr:`actions_enabled`

  
  *   :py:attr:`alarm_actions`

  
  *   :py:attr:`alarm_arn`

  
  *   :py:attr:`alarm_configuration_updated_timestamp`

  
  *   :py:attr:`alarm_description`

  
  *   :py:attr:`alarm_name`

  
  *   :py:attr:`comparison_operator`

  
  *   :py:attr:`datapoints_to_alarm`

  
  *   :py:attr:`dimensions`

  
  *   :py:attr:`evaluate_low_sample_count_percentile`

  
  *   :py:attr:`evaluation_periods`

  
  *   :py:attr:`extended_statistic`

  
  *   :py:attr:`insufficient_data_actions`

  
  *   :py:attr:`metric_name`

  
  *   :py:attr:`namespace`

  
  *   :py:attr:`ok_actions`

  
  *   :py:attr:`period`

  
  *   :py:attr:`state_reason`

  
  *   :py:attr:`state_reason_data`

  
  *   :py:attr:`state_updated_timestamp`

  
  *   :py:attr:`state_value`

  
  *   :py:attr:`statistic`

  
  *   :py:attr:`threshold`

  
  *   :py:attr:`treat_missing_data`

  
  *   :py:attr:`unit`

  
  These are the resource's available references:
  
  *   :py:attr:`metric`

  
  These are the resource's available actions:
  
  *   :py:meth:`delete()`

  
  *   :py:meth:`describe_history()`

  
  *   :py:meth:`disable_actions()`

  
  *   :py:meth:`enable_actions()`

  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`load()`

  
  *   :py:meth:`reload()`

  
  *   :py:meth:`set_state()`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: name

    *(string)* The Alarm's name identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: actions_enabled

    

    - *(boolean) --* 

      Indicates whether actions should be executed during any changes to the alarm state.

      

  .. py:attribute:: alarm_actions

    

    - *(list) --* 

      The actions to execute when this alarm transitions to the ``ALARM`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

      
      

      - *(string) --* 
  

  .. py:attribute:: alarm_arn

    

    - *(string) --* 

      The Amazon Resource Name (ARN) of the alarm.

      

  .. py:attribute:: alarm_configuration_updated_timestamp

    

    - *(datetime) --* 

      The time stamp of the last update to the alarm configuration.

      

  .. py:attribute:: alarm_description

    

    - *(string) --* 

      The description of the alarm.

      

  .. py:attribute:: alarm_name

    

    - *(string) --* 

      The name of the alarm.

      

  .. py:attribute:: comparison_operator

    

    - *(string) --* 

      The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

      

  .. py:attribute:: datapoints_to_alarm

    

    - *(integer) --* 

      The number of datapoints that must be breaching to trigger the alarm.

      

  .. py:attribute:: dimensions

    

    - *(list) --* 

      The dimensions for the metric associated with the alarm.

      
      

      - *(dict) --* 

        Expands the identity of a metric.

        
        

        - **Name** *(string) --* 

          The name of the dimension.

          
        

        - **Value** *(string) --* 

          The value representing the dimension measurement.

          
    
  

  .. py:attribute:: evaluate_low_sample_count_percentile

    

    - *(string) --* 

      Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

      

  .. py:attribute:: evaluation_periods

    

    - *(integer) --* 

      The number of periods over which data is compared to the specified threshold.

      

  .. py:attribute:: extended_statistic

    

    - *(string) --* 

      The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

      

  .. py:attribute:: insufficient_data_actions

    

    - *(list) --* 

      The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

      
      

      - *(string) --* 
  

  .. py:attribute:: metric_name

    

    - *(string) --* 

      The name of the metric associated with the alarm.

      

  .. py:attribute:: namespace

    

    - *(string) --* 

      The namespace of the metric associated with the alarm.

      

  .. py:attribute:: ok_actions

    

    - *(list) --* 

      The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

      
      

      - *(string) --* 
  

  .. py:attribute:: period

    

    - *(integer) --* 

      The period, in seconds, over which the statistic is applied.

      

  .. py:attribute:: state_reason

    

    - *(string) --* 

      An explanation for the alarm state, in text format.

      

  .. py:attribute:: state_reason_data

    

    - *(string) --* 

      An explanation for the alarm state, in JSON format.

      

  .. py:attribute:: state_updated_timestamp

    

    - *(datetime) --* 

      The time stamp of the last update to the alarm state.

      

  .. py:attribute:: state_value

    

    - *(string) --* 

      The state value for the alarm.

      

  .. py:attribute:: statistic

    

    - *(string) --* 

      The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` .

      

  .. py:attribute:: threshold

    

    - *(float) --* 

      The value to compare with the specified statistic.

      

  .. py:attribute:: treat_missing_data

    

    - *(string) --* 

      Sets how this alarm is to handle missing data points. If this parameter is omitted, the default behavior of ``missing`` is used.

      

  .. py:attribute:: unit

    

    - *(string) --* 

      The unit of the metric associated with the alarm.

      
  .. rst-class:: admonition-title
  
  References
  
  References are related resource instances that have a belongs-to relationship.
  For more information about references refer to the :ref:`Resources Introduction Guide<references_intro>`.
  

  .. py:attribute:: metric

    (:py:class:`Metric`) The related metric if set, otherwise ``None``.
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: delete()

    

    Deletes the specified alarms. In the event of an error, no alarms are deleted.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_    


    **Request Syntax** 
    ::

      response = alarm.delete()
      
    
    :returns: None

  .. py:method:: describe_history(**kwargs)

    

    Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for all alarms are returned.

     

    CloudWatch retains the history of an alarm even if you delete the alarm.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmHistory>`_    


    **Request Syntax** 
    ::

      response = alarm.describe_history(
          HistoryItemType='ConfigurationUpdate'|'StateUpdate'|'Action',
          StartDate=datetime(2015, 1, 1),
          EndDate=datetime(2015, 1, 1),
          MaxRecords=123,
          NextToken='string'
      )
    :type HistoryItemType: string
    :param HistoryItemType: 

      The type of alarm histories to retrieve.

      

    
    :type StartDate: datetime
    :param StartDate: 

      The starting date to retrieve alarm history.

      

    
    :type EndDate: datetime
    :param EndDate: 

      The ending date to retrieve alarm history.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of alarm history records to retrieve.

      

    
    :type NextToken: string
    :param NextToken: 

      The token returned by a previous call to indicate that there is more data available.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AlarmHistoryItems': [
                {
                    'AlarmName': 'string',
                    'Timestamp': datetime(2015, 1, 1),
                    'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
                    'HistorySummary': 'string',
                    'HistoryData': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AlarmHistoryItems** *(list) --* 

          The alarm histories, in JSON format.

          
          

          - *(dict) --* 

            Represents the history of a specific alarm.

            
            

            - **AlarmName** *(string) --* 

              The descriptive name for the alarm.

              
            

            - **Timestamp** *(datetime) --* 

              The time stamp for the alarm history item.

              
            

            - **HistoryItemType** *(string) --* 

              The type of alarm history item.

              
            

            - **HistorySummary** *(string) --* 

              A summary of the alarm history, in text format.

              
            

            - **HistoryData** *(string) --* 

              Data about the alarm, in JSON format.

              
        
      
        

        - **NextToken** *(string) --* 

          The token that marks the start of the next batch of returned results.

          
    

  .. py:method:: disable_actions()

    

    Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_    


    **Request Syntax** 
    ::

      response = alarm.disable_actions()
      
    
    :returns: None

  .. py:method:: enable_actions()

    

    Enables the actions for the specified alarms.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_    


    **Request Syntax** 
    ::

      response = alarm.enable_actions()
      
    
    :returns: None

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: load()

    Calls :py:meth:`CloudWatch.Client.describe_alarms` to update the attributes of the Alarm resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_    


    **Request Syntax** 

    ::

      alarm.load()
    :returns: None

  .. py:method:: reload()

    Calls :py:meth:`CloudWatch.Client.describe_alarms` to update the attributes of the Alarm resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_    


    **Request Syntax** 

    ::

      alarm.reload()
    :returns: None

  .. py:method:: set_state(**kwargs)

    

    Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ``ALARM`` sends an SNS message. The alarm returns to its actual state (often within seconds). Because the alarm state change happens quickly, it is typically only visible in the alarm's **History** tab in the Amazon CloudWatch console or through  DescribeAlarmHistory .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/SetAlarmState>`_    


    **Request Syntax** 
    ::

      response = alarm.set_state(
          StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
          StateReason='string',
          StateReasonData='string'
      )
    :type StateValue: string
    :param StateValue: **[REQUIRED]** 

      The value of the state.

      

    
    :type StateReason: string
    :param StateReason: **[REQUIRED]** 

      The reason that this alarm is set to this specific state, in text format.

      

    
    :type StateReasonData: string
    :param StateReasonData: 

      The reason that this alarm is set to this specific state, in JSON format.

      

    
    
    :returns: None

======
Metric
======



.. py:class:: CloudWatch.Metric(namespace,name)

  A resource representing an Amazon CloudWatch Metric::

    
    import boto3
    
    cloudwatch = boto3.resource('cloudwatch')
    metric = cloudwatch.Metric('namespace','name')

  :type namespace: string
  :param namespace: The Metric's namespace identifier. This **must** be set.
  :type name: string
  :param name: The Metric's name identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`namespace`

  
  *   :py:attr:`name`

  
  These are the resource's available attributes:
  
  *   :py:attr:`dimensions`

  
  *   :py:attr:`metric_name`

  
  These are the resource's available actions:
  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`get_statistics()`

  
  *   :py:meth:`load()`

  
  *   :py:meth:`put_alarm()`

  
  *   :py:meth:`put_data()`

  
  *   :py:meth:`reload()`

  
  These are the resource's available collections:
  
  *   :py:attr:`alarms`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: namespace

    *(string)* The Metric's namespace identifier. This **must** be set.

  .. py:attribute:: name

    *(string)* The Metric's name identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: dimensions

    

    - *(list) --* 

      The dimensions for the metric.

      
      

      - *(dict) --* 

        Expands the identity of a metric.

        
        

        - **Name** *(string) --* 

          The name of the dimension.

          
        

        - **Value** *(string) --* 

          The value representing the dimension measurement.

          
    
  

  .. py:attribute:: metric_name

    

    - *(string) --* 

      The name of the metric.

      
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: get_statistics(**kwargs)

    

    Gets statistics for the specified metric.

     

    The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order.

     

    CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.

     

    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:

     

     
    * The SampleCount value of the statistic set is 1. 
     
    * The Min and the Max values of the statistic set are equal. 
     

     

    Amazon CloudWatch retains metric data as follows:

     

     
    * Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a ``StorageResolution`` of 1. 
     
    * Data points with a period of 60 seconds (1-minute) are available for 15 days. 
     
    * Data points with a period of 300 seconds (5-minute) are available for 63 days. 
     
    * Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months). 
     

     

    Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.

     

    CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.

     

    For information about metrics and dimensions supported by AWS services, see the `Amazon CloudWatch Metrics and Dimensions Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetMetricStatistics>`_    


    **Request Syntax** 
    ::

      response = metric.get_statistics(
          Dimensions=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          Period=123,
          Statistics=[
              'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
          ],
          ExtendedStatistics=[
              'string',
          ],
          Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
      )
    :type Dimensions: list
    :param Dimensions: 

      The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can't retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see `Dimension Combinations <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-combinations>`__ in the *Amazon CloudWatch User Guide* . For more information about specifying dimensions, see `Publishing Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__ in the *Amazon CloudWatch User Guide* .

      

    
      - *(dict) --* 

        Expands the identity of a metric.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the dimension.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value representing the dimension measurement.

          

        
      
  
    :type StartTime: datetime
    :param StartTime: **[REQUIRED]** 

      The time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request.

       

      The value specified is inclusive; results include data points with the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).

       

      CloudWatch rounds the specified time stamp as follows:

       

       
      * Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00. 
       
      * Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00. 
       
      * Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00. 
       

       

      If you set ``Period`` to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. 

      

    
    :type EndTime: datetime
    :param EndTime: **[REQUIRED]** 

      The time stamp that determines the last data point to return.

       

      The value specified is exclusive; results include data points up to the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).

      

    
    :type Period: integer
    :param Period: **[REQUIRED]** 

      The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.

       

      If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

       

       
      * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute). 
       
      * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes). 
       
      * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour). 
       

      

    
    :type Statistics: list
    :param Statistics: 

      The metric statistics, other than percentile. For percentile statistics, use ``ExtendedStatistics`` . When calling ``GetMetricStatistics`` , you must specify either ``Statistics`` or ``ExtendedStatistics`` , but not both.

      

    
      - *(string) --* 

      
  
    :type ExtendedStatistics: list
    :param ExtendedStatistics: 

      The percentile statistics. Specify values between p0.0 and p100. When calling ``GetMetricStatistics`` , you must specify either ``Statistics`` or ``ExtendedStatistics`` , but not both.

      

    
      - *(string) --* 

      
  
    :type Unit: string
    :param Unit: 

      The unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If the metric only ever reports one unit, specifying a unit has no effect.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Label': 'string',
            'Datapoints': [
                {
                    'Timestamp': datetime(2015, 1, 1),
                    'SampleCount': 123.0,
                    'Average': 123.0,
                    'Sum': 123.0,
                    'Minimum': 123.0,
                    'Maximum': 123.0,
                    'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                    'ExtendedStatistics': {
                        'string': 123.0
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Label** *(string) --* 

          A label for the specified metric.

          
        

        - **Datapoints** *(list) --* 

          The data points for the specified metric.

          
          

          - *(dict) --* 

            Encapsulates the statistical data that CloudWatch computes from metric data.

            
            

            - **Timestamp** *(datetime) --* 

              The time stamp used for the data point.

              
            

            - **SampleCount** *(float) --* 

              The number of metric values that contributed to the aggregate value of this data point.

              
            

            - **Average** *(float) --* 

              The average of the metric values that correspond to the data point.

              
            

            - **Sum** *(float) --* 

              The sum of the metric values for the data point.

              
            

            - **Minimum** *(float) --* 

              The minimum metric value for the data point.

              
            

            - **Maximum** *(float) --* 

              The maximum metric value for the data point.

              
            

            - **Unit** *(string) --* 

              The standard unit for the data point.

              
            

            - **ExtendedStatistics** *(dict) --* 

              The percentile statistic for the data point.

              
              

              - *(string) --* 
                

                - *(float) --* 
          
        
        
      
    

  .. py:method:: load()

    Calls :py:meth:`CloudWatch.Client.list_metrics` to update the attributes of the Metric resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_    


    **Request Syntax** 

    ::

      metric.load()
    :returns: None

  .. py:method:: put_alarm(**kwargs)

    

    Creates or updates an alarm and associates it with the specified metric. Optionally, this operation can associate one or more Amazon SNS resources with the alarm.

     

    When this operation creates an alarm, the alarm state is immediately set to ``INSUFFICIENT_DATA`` . The alarm is evaluated and its state is set appropriately. Any actions associated with the state are then executed.

     

    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.

     

    If you are an IAM user, you must have Amazon EC2 permissions for some operations:

     

     
    * ``ec2:DescribeInstanceStatus`` and ``ec2:DescribeInstances`` for all alarms on EC2 instance status metrics 
     
    * ``ec2:StopInstances`` for alarms with stop actions 
     
    * ``ec2:TerminateInstances`` for alarms with terminate actions 
     
    * ``ec2:DescribeInstanceRecoveryAttribute`` and ``ec2:RecoverInstances`` for alarms with recover actions 
     

     

    If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still create an alarm, but the stop or terminate actions are not performed. However, if you are later granted the required permissions, the alarm actions that you created earlier are performed.

     

    If you are using an IAM role (for example, an EC2 instance profile), you cannot stop or terminate the instance using alarm actions. However, you can still see the alarm state and perform any other actions such as Amazon SNS notifications or Auto Scaling policies.

     

    If you are using temporary security credentials granted using AWS STS, you cannot stop or terminate an EC2 instance using alarm actions.

     

    You must create at least one stop, terminate, or reboot alarm using either the Amazon EC2 or CloudWatch consoles to create the **EC2ActionsAccess** IAM role. After this IAM role is created, you can create stop, terminate, or reboot alarms using a command-line interface or API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricAlarm>`_    


    **Request Syntax** 
    ::

      alarm = metric.put_alarm(
          AlarmName='string',
          AlarmDescription='string',
          ActionsEnabled=True|False,
          OKActions=[
              'string',
          ],
          AlarmActions=[
              'string',
          ],
          InsufficientDataActions=[
              'string',
          ],
          Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
          ExtendedStatistic='string',
          Dimensions=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          Period=123,
          Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
          EvaluationPeriods=123,
          DatapointsToAlarm=123,
          Threshold=123.0,
          ComparisonOperator='GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
          TreatMissingData='string',
          EvaluateLowSampleCountPercentile='string'
      )
    :type AlarmName: string
    :param AlarmName: **[REQUIRED]** 

      The name for the alarm. This name must be unique within the AWS account.

      

    
    :type AlarmDescription: string
    :param AlarmDescription: 

      The description for the alarm.

      

    
    :type ActionsEnabled: boolean
    :param ActionsEnabled: 

      Indicates whether actions should be executed during any changes to the alarm state.

      

    
    :type OKActions: list
    :param OKActions: 

      The actions to execute when this alarm transitions to an ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

       

      Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:sns:*region* :*account-id* :*sns-topic-name* | arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name*  

       

      Valid Values (for use with IAM roles): arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Reboot/1.0

      

    
      - *(string) --* 

      
  
    :type AlarmActions: list
    :param AlarmActions: 

      The actions to execute when this alarm transitions to the ``ALARM`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

       

      Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:sns:*region* :*account-id* :*sns-topic-name* | arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name*  

       

      Valid Values (for use with IAM roles): arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Reboot/1.0

      

    
      - *(string) --* 

      
  
    :type InsufficientDataActions: list
    :param InsufficientDataActions: 

      The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

       

      Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:sns:*region* :*account-id* :*sns-topic-name* | arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name*  

       

      Valid Values (for use with IAM roles): arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :{*account-id* }:action/actions/AWS_EC2.InstanceId.Reboot/1.0

      

    
      - *(string) --* 

      
  
    :type Statistic: string
    :param Statistic: 

      The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` . When you call ``PutMetricAlarm`` , you must specify either ``Statistic`` or ``ExtendedStatistic,`` but not both.

      

    
    :type ExtendedStatistic: string
    :param ExtendedStatistic: 

      The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. When you call ``PutMetricAlarm`` , you must specify either ``Statistic`` or ``ExtendedStatistic,`` but not both.

      

    
    :type Dimensions: list
    :param Dimensions: 

      The dimensions for the metric associated with the alarm.

      

    
      - *(dict) --* 

        Expands the identity of a metric.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the dimension.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value representing the dimension measurement.

          

        
      
  
    :type Period: integer
    :param Period: **[REQUIRED]** 

      The period, in seconds, over which the specified statistic is applied. Valid values are 10, 30, and any multiple of 60.

       

      Be sure to specify 10 or 30 only for metrics that are stored by a ``PutMetricData`` call with a ``StorageResolution`` of 1. If you specify a Period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see `Amazon CloudWatch Pricing <https://aws.amazon.com/cloudwatch/pricing/>`__ .

       

      An alarm's total current evaluation period can be no longer than one day, so ``Period`` multiplied by ``EvaluationPeriods`` cannot be more than 86,400 seconds.

      

    
    :type Unit: string
    :param Unit: 

      The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.

       

      If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, the CloudWatch alarm can get stuck in the ``INSUFFICIENT DATA`` state. 

      

    
    :type EvaluationPeriods: integer
    :param EvaluationPeriods: **[REQUIRED]** 

      The number of periods over which data is compared to the specified threshold. An alarm's total current evaluation period can be no longer than one day, so this number multiplied by ``Period`` cannot be more than 86,400 seconds.

      

    
    :type DatapointsToAlarm: integer
    :param DatapointsToAlarm: 

      The number of datapoints that must be breaching to trigger the alarm.

      

    
    :type Threshold: float
    :param Threshold: **[REQUIRED]** 

      The value against which the specified statistic is compared.

      

    
    :type ComparisonOperator: string
    :param ComparisonOperator: **[REQUIRED]** 

      The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

      

    
    :type TreatMissingData: string
    :param TreatMissingData: 

      Sets how this alarm is to handle missing data points. If ``TreatMissingData`` is omitted, the default behavior of ``missing`` is used. For more information, see `Configuring How CloudWatch Alarms Treats Missing Data <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`__ .

       

      Valid Values: ``breaching | notBreaching | ignore | missing``  

      

    
    :type EvaluateLowSampleCountPercentile: string
    :param EvaluateLowSampleCountPercentile: 

      Used only for alarms based on percentiles. If you specify ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If you specify ``evaluate`` or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see `Percentile-Based CloudWatch Alarms and Low Data Samples <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples>`__ .

       

      Valid Values: ``evaluate | ignore``  

      

    
    
    :rtype: :py:class:`cloudwatch.Alarm`
    :returns: Alarm resource
    

  .. py:method:: put_data()

    

    Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to  ListMetrics .

     

    Each ``PutMetricData`` request is limited to 40 KB in size for HTTP POST requests.

     

    Although the ``Value`` parameter accepts numbers of type ``Double`` , CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.

     

    You can use up to 10 dimensions per metric to further clarify what data the metric collects. For more information about specifying dimensions, see `Publishing Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__ in the *Amazon CloudWatch User Guide* .

     

    Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for  GetMetricStatistics from the time they are submitted.

     

    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:

     

     
    * The SampleCount value of the statistic set is 1 
     
    * The Min and the Max values of the statistic set are equal 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricData>`_    


    **Request Syntax** 
    ::

      response = metric.put_data()
      
    
    :returns: None

  .. py:method:: reload()

    Calls :py:meth:`CloudWatch.Client.list_metrics` to update the attributes of the Metric resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_    


    **Request Syntax** 

    ::

      metric.reload()
    :returns: None
  .. rst-class:: admonition-title
  
  Collections
  
  Collections provide an interface to iterate over and manipulate groups of resources. 
  For more information about collections refer to the :ref:`Resources Introduction Guide<guide_collections>`.
  

  .. py:attribute:: alarms

    A collection of Alarm resources

    .. py:method:: all()

      Creates an iterable of all Alarm resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_      


      **Request Syntax** 
      ::

        alarm_iterator = metric.alarms.all()
        
      
      :rtype: list(:py:class:`cloudwatch.Alarm`)
      :returns: A list of Alarm resources
      

    .. py:method:: delete()

      

      Deletes the specified alarms. In the event of an error, no alarms are deleted.

      

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_      


      **Request Syntax** 
      ::

        response = metric.alarms.delete()
        
      
      :returns: None

    .. py:method:: disable_actions()

      

      Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.

      

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_      


      **Request Syntax** 
      ::

        response = metric.alarms.disable_actions()
        
      
      :returns: None

    .. py:method:: enable_actions()

      

      Enables the actions for the specified alarms.

      

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_      


      **Request Syntax** 
      ::

        response = metric.alarms.enable_actions()
        
      
      :returns: None

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Alarm resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_      


      **Request Syntax** 
      ::

        alarm_iterator = metric.alarms.filter(
            Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
            ExtendedStatistic='string',
            Dimensions=[
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            Period=123,
            Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
        )
      :type Statistic: string
      :param Statistic: 

        The statistic for the metric, other than percentiles. For percentile statistics, use ``ExtendedStatistics`` .

        

      
      :type ExtendedStatistic: string
      :param ExtendedStatistic: 

        The percentile statistic for the metric. Specify a value between p0.0 and p100.

        

      
      :type Dimensions: list
      :param Dimensions: 

        The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.

        

      
        - *(dict) --* 

          Expands the identity of a metric.

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The name of the dimension.

            

          
          - **Value** *(string) --* **[REQUIRED]** 

            The value representing the dimension measurement.

            

          
        
    
      :type Period: integer
      :param Period: 

        The period, in seconds, over which the statistic is applied.

        

      
      :type Unit: string
      :param Unit: 

        The unit for the metric.

        

      
      
      :rtype: list(:py:class:`cloudwatch.Alarm`)
      :returns: A list of Alarm resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Alarm resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_      


      **Request Syntax** 
      ::

        alarm_iterator = metric.alarms.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`cloudwatch.Alarm`)
      :returns: A list of Alarm resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Alarm resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_      


      **Request Syntax** 
      ::

        alarm_iterator = metric.alarms.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`cloudwatch.Alarm`)
      :returns: A list of Alarm resources
      