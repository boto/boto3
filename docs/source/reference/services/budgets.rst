

*******
Budgets
*******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Budgets.Client

  A low-level client representing AWS Budgets::

    
    import boto3
    
    client = boto3.client('budgets')

  
  These are the available methods:
  
  *   :py:meth:`~Budgets.Client.can_paginate`

  
  *   :py:meth:`~Budgets.Client.create_budget`

  
  *   :py:meth:`~Budgets.Client.create_notification`

  
  *   :py:meth:`~Budgets.Client.create_subscriber`

  
  *   :py:meth:`~Budgets.Client.delete_budget`

  
  *   :py:meth:`~Budgets.Client.delete_notification`

  
  *   :py:meth:`~Budgets.Client.delete_subscriber`

  
  *   :py:meth:`~Budgets.Client.describe_budget`

  
  *   :py:meth:`~Budgets.Client.describe_budgets`

  
  *   :py:meth:`~Budgets.Client.describe_notifications_for_budget`

  
  *   :py:meth:`~Budgets.Client.describe_subscribers_for_notification`

  
  *   :py:meth:`~Budgets.Client.generate_presigned_url`

  
  *   :py:meth:`~Budgets.Client.get_paginator`

  
  *   :py:meth:`~Budgets.Client.get_waiter`

  
  *   :py:meth:`~Budgets.Client.update_budget`

  
  *   :py:meth:`~Budgets.Client.update_notification`

  
  *   :py:meth:`~Budgets.Client.update_subscriber`

  

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


  .. py:method:: create_budget(**kwargs)

    Create a new budget

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateBudget>`_    


    **Request Syntax** 
    ::

      response = client.create_budget(
          AccountId='string',
          Budget={
              'BudgetName': 'string',
              'BudgetLimit': {
                  'Amount': 'string',
                  'Unit': 'string'
              },
              'CostFilters': {
                  'string': [
                      'string',
                  ]
              },
              'CostTypes': {
                  'IncludeTax': True|False,
                  'IncludeSubscription': True|False,
                  'UseBlended': True|False,
                  'IncludeRefund': True|False,
                  'IncludeCredit': True|False,
                  'IncludeUpfront': True|False,
                  'IncludeRecurring': True|False,
                  'IncludeOtherSubscription': True|False,
                  'IncludeSupport': True|False
              },
              'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
              'TimePeriod': {
                  'Start': datetime(2015, 1, 1),
                  'End': datetime(2015, 1, 1)
              },
              'CalculatedSpend': {
                  'ActualSpend': {
                      'Amount': 'string',
                      'Unit': 'string'
                  },
                  'ForecastedSpend': {
                      'Amount': 'string',
                      'Unit': 'string'
                  }
              },
              'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'
          },
          NotificationsWithSubscribers=[
              {
                  'Notification': {
                      'NotificationType': 'ACTUAL'|'FORECASTED',
                      'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                      'Threshold': 123.0,
                      'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
                  },
                  'Subscribers': [
                      {
                          'SubscriptionType': 'SNS'|'EMAIL',
                          'Address': 'string'
                      },
                  ]
              },
          ]
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type Budget: dict
    :param Budget: **[REQUIRED]** AWS Budget model

    
      - **BudgetName** *(string) --* **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

      
      - **BudgetLimit** *(dict) --* **[REQUIRED]** A structure that represents either a cost spend or usage spend. Contains an amount and a unit.

      
        - **Amount** *(string) --* **[REQUIRED]** A string to represent NumericValue.

        
        - **Unit** *(string) --* **[REQUIRED]** A string to represent budget spend unit. It should be not null and not empty.

        
      
      - **CostFilters** *(dict) --* A map that represents the cost filters applied to the budget.

      
        - *(string) --* A generic String.

        
          - *(list) --* 

          
            - *(string) --* A generic String.

            
        
    
  
      - **CostTypes** *(dict) --* This includes the options for getting the cost of a budget.

      
        - **IncludeTax** *(boolean) --* A boolean value whether to include tax in the cost budget.

        
        - **IncludeSubscription** *(boolean) --* A boolean value whether to include subscriptions in the cost budget.

        
        - **UseBlended** *(boolean) --* A boolean value whether to use blended costs in the cost budget.

        
        - **IncludeRefund** *(boolean) --* A boolean value whether to include refunds in the cost budget.

        
        - **IncludeCredit** *(boolean) --* A boolean value whether to include credits in the cost budget.

        
        - **IncludeUpfront** *(boolean) --* A boolean value whether to include upfront costs in the cost budget.

        
        - **IncludeRecurring** *(boolean) --* A boolean value whether to include recurring costs in the cost budget.

        
        - **IncludeOtherSubscription** *(boolean) --* A boolean value whether to include other subscription costs in the cost budget.

        
        - **IncludeSupport** *(boolean) --* A boolean value whether to include support costs in the cost budget.

        
      
      - **TimeUnit** *(string) --* **[REQUIRED]** The time unit of the budget. e.g. MONTHLY, QUARTERLY, etc.

      
      - **TimePeriod** *(dict) --* **[REQUIRED]** A time period indicating the start date and end date of a budget.

      
        - **Start** *(datetime) --* **[REQUIRED]** A generic timestamp. In Java it is transformed to a Date object.

        
        - **End** *(datetime) --* **[REQUIRED]** A generic timestamp. In Java it is transformed to a Date object.

        
      
      - **CalculatedSpend** *(dict) --* A structure that holds the actual and forecasted spend for a budget.

      
        - **ActualSpend** *(dict) --* **[REQUIRED]** A structure that represents either a cost spend or usage spend. Contains an amount and a unit.

        
          - **Amount** *(string) --* **[REQUIRED]** A string to represent NumericValue.

          
          - **Unit** *(string) --* **[REQUIRED]** A string to represent budget spend unit. It should be not null and not empty.

          
        
        - **ForecastedSpend** *(dict) --* A structure that represents either a cost spend or usage spend. Contains an amount and a unit.

        
          - **Amount** *(string) --* **[REQUIRED]** A string to represent NumericValue.

          
          - **Unit** *(string) --* **[REQUIRED]** A string to represent budget spend unit. It should be not null and not empty.

          
        
      
      - **BudgetType** *(string) --* **[REQUIRED]** The type of a budget. It should be COST, USAGE, or RI_UTILIZATION.

      
    
    :type NotificationsWithSubscribers: list
    :param NotificationsWithSubscribers: A list of Notifications, each with a list of subscribers.

    
      - *(dict) --* A structure to relate notification and a list of subscribers who belong to the notification.

      
        - **Notification** *(dict) --* **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

        
          - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

          
          - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

          
          - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

          
          - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

          
        
        - **Subscribers** *(list) --* **[REQUIRED]** A list of subscribers.

        
          - *(dict) --* Subscriber model. Each notification may contain multiple subscribers with different addresses.

          
            - **SubscriptionType** *(string) --* **[REQUIRED]** The subscription type of the subscriber. It can be SMS or EMAIL.

            
            - **Address** *(string) --* **[REQUIRED]** String containing email or sns topic for the subscriber address.

            
          
      
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of CreateBudget
    

  .. py:method:: create_notification(**kwargs)

    Create a new Notification with subscribers for a budget

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateNotification>`_    


    **Request Syntax** 
    ::

      response = client.create_notification(
          AccountId='string',
          BudgetName='string',
          Notification={
              'NotificationType': 'ACTUAL'|'FORECASTED',
              'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
              'Threshold': 123.0,
              'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
          },
          Subscribers=[
              {
                  'SubscriptionType': 'SNS'|'EMAIL',
                  'Address': 'string'
              },
          ]
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    :type Notification: dict
    :param Notification: **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

    
      - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

      
      - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

      
      - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

      
      - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

      
    
    :type Subscribers: list
    :param Subscribers: **[REQUIRED]** A list of subscribers.

    
      - *(dict) --* Subscriber model. Each notification may contain multiple subscribers with different addresses.

      
        - **SubscriptionType** *(string) --* **[REQUIRED]** The subscription type of the subscriber. It can be SMS or EMAIL.

        
        - **Address** *(string) --* **[REQUIRED]** String containing email or sns topic for the subscriber address.

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of CreateNotification
    

  .. py:method:: create_subscriber(**kwargs)

    Create a new Subscriber for a notification

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateSubscriber>`_    


    **Request Syntax** 
    ::

      response = client.create_subscriber(
          AccountId='string',
          BudgetName='string',
          Notification={
              'NotificationType': 'ACTUAL'|'FORECASTED',
              'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
              'Threshold': 123.0,
              'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
          },
          Subscriber={
              'SubscriptionType': 'SNS'|'EMAIL',
              'Address': 'string'
          }
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    :type Notification: dict
    :param Notification: **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

    
      - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

      
      - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

      
      - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

      
      - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

      
    
    :type Subscriber: dict
    :param Subscriber: **[REQUIRED]** Subscriber model. Each notification may contain multiple subscribers with different addresses.

    
      - **SubscriptionType** *(string) --* **[REQUIRED]** The subscription type of the subscriber. It can be SMS or EMAIL.

      
      - **Address** *(string) --* **[REQUIRED]** String containing email or sns topic for the subscriber address.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of CreateSubscriber
    

  .. py:method:: delete_budget(**kwargs)

    Delete a budget and related notifications

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DeleteBudget>`_    


    **Request Syntax** 
    ::

      response = client.delete_budget(
          AccountId='string',
          BudgetName='string'
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of DeleteBudget
    

  .. py:method:: delete_notification(**kwargs)

    Delete a notification and related subscribers

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DeleteNotification>`_    


    **Request Syntax** 
    ::

      response = client.delete_notification(
          AccountId='string',
          BudgetName='string',
          Notification={
              'NotificationType': 'ACTUAL'|'FORECASTED',
              'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
              'Threshold': 123.0,
              'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
          }
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    :type Notification: dict
    :param Notification: **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

    
      - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

      
      - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

      
      - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

      
      - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of DeleteNotification
    

  .. py:method:: delete_subscriber(**kwargs)

    Delete a Subscriber for a notification

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DeleteSubscriber>`_    


    **Request Syntax** 
    ::

      response = client.delete_subscriber(
          AccountId='string',
          BudgetName='string',
          Notification={
              'NotificationType': 'ACTUAL'|'FORECASTED',
              'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
              'Threshold': 123.0,
              'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
          },
          Subscriber={
              'SubscriptionType': 'SNS'|'EMAIL',
              'Address': 'string'
          }
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    :type Notification: dict
    :param Notification: **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

    
      - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

      
      - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

      
      - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

      
      - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

      
    
    :type Subscriber: dict
    :param Subscriber: **[REQUIRED]** Subscriber model. Each notification may contain multiple subscribers with different addresses.

    
      - **SubscriptionType** *(string) --* **[REQUIRED]** The subscription type of the subscriber. It can be SMS or EMAIL.

      
      - **Address** *(string) --* **[REQUIRED]** String containing email or sns topic for the subscriber address.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of DeleteSubscriber
    

  .. py:method:: describe_budget(**kwargs)

    Get a single budget

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeBudget>`_    


    **Request Syntax** 
    ::

      response = client.describe_budget(
          AccountId='string',
          BudgetName='string'
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Budget': {
                'BudgetName': 'string',
                'BudgetLimit': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'CostFilters': {
                    'string': [
                        'string',
                    ]
                },
                'CostTypes': {
                    'IncludeTax': True|False,
                    'IncludeSubscription': True|False,
                    'UseBlended': True|False,
                    'IncludeRefund': True|False,
                    'IncludeCredit': True|False,
                    'IncludeUpfront': True|False,
                    'IncludeRecurring': True|False,
                    'IncludeOtherSubscription': True|False,
                    'IncludeSupport': True|False
                },
                'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                'TimePeriod': {
                    'Start': datetime(2015, 1, 1),
                    'End': datetime(2015, 1, 1)
                },
                'CalculatedSpend': {
                    'ActualSpend': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'ForecastedSpend': {
                        'Amount': 'string',
                        'Unit': 'string'
                    }
                },
                'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'
            }
        }
      **Response Structure** 

      

      - *(dict) --* Response of DescribeBudget
        

        - **Budget** *(dict) --* AWS Budget model
          

          - **BudgetName** *(string) --* A string represents the budget name. No ":" and "\" character is allowed.
          

          - **BudgetLimit** *(dict) --* A structure that represents either a cost spend or usage spend. Contains an amount and a unit.
            

            - **Amount** *(string) --* A string to represent NumericValue.
            

            - **Unit** *(string) --* A string to represent budget spend unit. It should be not null and not empty.
        
          

          - **CostFilters** *(dict) --* A map that represents the cost filters applied to the budget.
            

            - *(string) --* A generic String.
              

              - *(list) --* 
                

                - *(string) --* A generic String.
            
        
      
          

          - **CostTypes** *(dict) --* This includes the options for getting the cost of a budget.
            

            - **IncludeTax** *(boolean) --* A boolean value whether to include tax in the cost budget.
            

            - **IncludeSubscription** *(boolean) --* A boolean value whether to include subscriptions in the cost budget.
            

            - **UseBlended** *(boolean) --* A boolean value whether to use blended costs in the cost budget.
            

            - **IncludeRefund** *(boolean) --* A boolean value whether to include refunds in the cost budget.
            

            - **IncludeCredit** *(boolean) --* A boolean value whether to include credits in the cost budget.
            

            - **IncludeUpfront** *(boolean) --* A boolean value whether to include upfront costs in the cost budget.
            

            - **IncludeRecurring** *(boolean) --* A boolean value whether to include recurring costs in the cost budget.
            

            - **IncludeOtherSubscription** *(boolean) --* A boolean value whether to include other subscription costs in the cost budget.
            

            - **IncludeSupport** *(boolean) --* A boolean value whether to include support costs in the cost budget.
        
          

          - **TimeUnit** *(string) --* The time unit of the budget. e.g. MONTHLY, QUARTERLY, etc.
          

          - **TimePeriod** *(dict) --* A time period indicating the start date and end date of a budget.
            

            - **Start** *(datetime) --* A generic timestamp. In Java it is transformed to a Date object.
            

            - **End** *(datetime) --* A generic timestamp. In Java it is transformed to a Date object.
        
          

          - **CalculatedSpend** *(dict) --* A structure that holds the actual and forecasted spend for a budget.
            

            - **ActualSpend** *(dict) --* A structure that represents either a cost spend or usage spend. Contains an amount and a unit.
              

              - **Amount** *(string) --* A string to represent NumericValue.
              

              - **Unit** *(string) --* A string to represent budget spend unit. It should be not null and not empty.
          
            

            - **ForecastedSpend** *(dict) --* A structure that represents either a cost spend or usage spend. Contains an amount and a unit.
              

              - **Amount** *(string) --* A string to represent NumericValue.
              

              - **Unit** *(string) --* A string to represent budget spend unit. It should be not null and not empty.
          
        
          

          - **BudgetType** *(string) --* The type of a budget. It should be COST, USAGE, or RI_UTILIZATION.
      
    

  .. py:method:: describe_budgets(**kwargs)

    Get all budgets for an account

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeBudgets>`_    


    **Request Syntax** 
    ::

      response = client.describe_budgets(
          AccountId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type MaxResults: integer
    :param MaxResults: An integer to represent how many entries a paginated response contains. Maximum is set to 100.

    
    :type NextToken: string
    :param NextToken: A generic String.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Budgets': [
                {
                    'BudgetName': 'string',
                    'BudgetLimit': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'CostFilters': {
                        'string': [
                            'string',
                        ]
                    },
                    'CostTypes': {
                        'IncludeTax': True|False,
                        'IncludeSubscription': True|False,
                        'UseBlended': True|False,
                        'IncludeRefund': True|False,
                        'IncludeCredit': True|False,
                        'IncludeUpfront': True|False,
                        'IncludeRecurring': True|False,
                        'IncludeOtherSubscription': True|False,
                        'IncludeSupport': True|False
                    },
                    'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                    'TimePeriod': {
                        'Start': datetime(2015, 1, 1),
                        'End': datetime(2015, 1, 1)
                    },
                    'CalculatedSpend': {
                        'ActualSpend': {
                            'Amount': 'string',
                            'Unit': 'string'
                        },
                        'ForecastedSpend': {
                            'Amount': 'string',
                            'Unit': 'string'
                        }
                    },
                    'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Response of DescribeBudgets
        

        - **Budgets** *(list) --* A list of budgets
          

          - *(dict) --* AWS Budget model
            

            - **BudgetName** *(string) --* A string represents the budget name. No ":" and "\" character is allowed.
            

            - **BudgetLimit** *(dict) --* A structure that represents either a cost spend or usage spend. Contains an amount and a unit.
              

              - **Amount** *(string) --* A string to represent NumericValue.
              

              - **Unit** *(string) --* A string to represent budget spend unit. It should be not null and not empty.
          
            

            - **CostFilters** *(dict) --* A map that represents the cost filters applied to the budget.
              

              - *(string) --* A generic String.
                

                - *(list) --* 
                  

                  - *(string) --* A generic String.
              
          
        
            

            - **CostTypes** *(dict) --* This includes the options for getting the cost of a budget.
              

              - **IncludeTax** *(boolean) --* A boolean value whether to include tax in the cost budget.
              

              - **IncludeSubscription** *(boolean) --* A boolean value whether to include subscriptions in the cost budget.
              

              - **UseBlended** *(boolean) --* A boolean value whether to use blended costs in the cost budget.
              

              - **IncludeRefund** *(boolean) --* A boolean value whether to include refunds in the cost budget.
              

              - **IncludeCredit** *(boolean) --* A boolean value whether to include credits in the cost budget.
              

              - **IncludeUpfront** *(boolean) --* A boolean value whether to include upfront costs in the cost budget.
              

              - **IncludeRecurring** *(boolean) --* A boolean value whether to include recurring costs in the cost budget.
              

              - **IncludeOtherSubscription** *(boolean) --* A boolean value whether to include other subscription costs in the cost budget.
              

              - **IncludeSupport** *(boolean) --* A boolean value whether to include support costs in the cost budget.
          
            

            - **TimeUnit** *(string) --* The time unit of the budget. e.g. MONTHLY, QUARTERLY, etc.
            

            - **TimePeriod** *(dict) --* A time period indicating the start date and end date of a budget.
              

              - **Start** *(datetime) --* A generic timestamp. In Java it is transformed to a Date object.
              

              - **End** *(datetime) --* A generic timestamp. In Java it is transformed to a Date object.
          
            

            - **CalculatedSpend** *(dict) --* A structure that holds the actual and forecasted spend for a budget.
              

              - **ActualSpend** *(dict) --* A structure that represents either a cost spend or usage spend. Contains an amount and a unit.
                

                - **Amount** *(string) --* A string to represent NumericValue.
                

                - **Unit** *(string) --* A string to represent budget spend unit. It should be not null and not empty.
            
              

              - **ForecastedSpend** *(dict) --* A structure that represents either a cost spend or usage spend. Contains an amount and a unit.
                

                - **Amount** *(string) --* A string to represent NumericValue.
                

                - **Unit** *(string) --* A string to represent budget spend unit. It should be not null and not empty.
            
          
            

            - **BudgetType** *(string) --* The type of a budget. It should be COST, USAGE, or RI_UTILIZATION.
        
      
        

        - **NextToken** *(string) --* A generic String.
    

  .. py:method:: describe_notifications_for_budget(**kwargs)

    Get notifications of a budget

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeNotificationsForBudget>`_    


    **Request Syntax** 
    ::

      response = client.describe_notifications_for_budget(
          AccountId='string',
          BudgetName='string',
          MaxResults=123,
          NextToken='string'
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    :type MaxResults: integer
    :param MaxResults: An integer to represent how many entries a paginated response contains. Maximum is set to 100.

    
    :type NextToken: string
    :param NextToken: A generic String.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Notifications': [
                {
                    'NotificationType': 'ACTUAL'|'FORECASTED',
                    'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                    'Threshold': 123.0,
                    'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Response of GetNotificationsForBudget
        

        - **Notifications** *(list) --* A list of notifications.
          

          - *(dict) --* Notification model. Each budget may contain multiple notifications with different settings.
            

            - **NotificationType** *(string) --* The type of a notification. It should be ACTUAL or FORECASTED.
            

            - **ComparisonOperator** *(string) --* The comparison operator of a notification. Currently we support less than, equal to and greater than.
            

            - **Threshold** *(float) --* The threshold of a notification. It should be a number between 0 and 1,000,000,000.
            

            - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.
        
      
        

        - **NextToken** *(string) --* A generic String.
    

  .. py:method:: describe_subscribers_for_notification(**kwargs)

    Get subscribers of a notification

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeSubscribersForNotification>`_    


    **Request Syntax** 
    ::

      response = client.describe_subscribers_for_notification(
          AccountId='string',
          BudgetName='string',
          Notification={
              'NotificationType': 'ACTUAL'|'FORECASTED',
              'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
              'Threshold': 123.0,
              'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
          },
          MaxResults=123,
          NextToken='string'
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    :type Notification: dict
    :param Notification: **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

    
      - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

      
      - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

      
      - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

      
      - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

      
    
    :type MaxResults: integer
    :param MaxResults: An integer to represent how many entries a paginated response contains. Maximum is set to 100.

    
    :type NextToken: string
    :param NextToken: A generic String.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Subscribers': [
                {
                    'SubscriptionType': 'SNS'|'EMAIL',
                    'Address': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Response of DescribeSubscribersForNotification
        

        - **Subscribers** *(list) --* A list of subscribers.
          

          - *(dict) --* Subscriber model. Each notification may contain multiple subscribers with different addresses.
            

            - **SubscriptionType** *(string) --* The subscription type of the subscriber. It can be SMS or EMAIL.
            

            - **Address** *(string) --* String containing email or sns topic for the subscriber address.
        
      
        

        - **NextToken** *(string) --* A generic String.
    

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

        


  .. py:method:: update_budget(**kwargs)

    Update the information of a budget already created

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/UpdateBudget>`_    


    **Request Syntax** 
    ::

      response = client.update_budget(
          AccountId='string',
          NewBudget={
              'BudgetName': 'string',
              'BudgetLimit': {
                  'Amount': 'string',
                  'Unit': 'string'
              },
              'CostFilters': {
                  'string': [
                      'string',
                  ]
              },
              'CostTypes': {
                  'IncludeTax': True|False,
                  'IncludeSubscription': True|False,
                  'UseBlended': True|False,
                  'IncludeRefund': True|False,
                  'IncludeCredit': True|False,
                  'IncludeUpfront': True|False,
                  'IncludeRecurring': True|False,
                  'IncludeOtherSubscription': True|False,
                  'IncludeSupport': True|False
              },
              'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
              'TimePeriod': {
                  'Start': datetime(2015, 1, 1),
                  'End': datetime(2015, 1, 1)
              },
              'CalculatedSpend': {
                  'ActualSpend': {
                      'Amount': 'string',
                      'Unit': 'string'
                  },
                  'ForecastedSpend': {
                      'Amount': 'string',
                      'Unit': 'string'
                  }
              },
              'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'
          }
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type NewBudget: dict
    :param NewBudget: **[REQUIRED]** AWS Budget model

    
      - **BudgetName** *(string) --* **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

      
      - **BudgetLimit** *(dict) --* **[REQUIRED]** A structure that represents either a cost spend or usage spend. Contains an amount and a unit.

      
        - **Amount** *(string) --* **[REQUIRED]** A string to represent NumericValue.

        
        - **Unit** *(string) --* **[REQUIRED]** A string to represent budget spend unit. It should be not null and not empty.

        
      
      - **CostFilters** *(dict) --* A map that represents the cost filters applied to the budget.

      
        - *(string) --* A generic String.

        
          - *(list) --* 

          
            - *(string) --* A generic String.

            
        
    
  
      - **CostTypes** *(dict) --* This includes the options for getting the cost of a budget.

      
        - **IncludeTax** *(boolean) --* A boolean value whether to include tax in the cost budget.

        
        - **IncludeSubscription** *(boolean) --* A boolean value whether to include subscriptions in the cost budget.

        
        - **UseBlended** *(boolean) --* A boolean value whether to use blended costs in the cost budget.

        
        - **IncludeRefund** *(boolean) --* A boolean value whether to include refunds in the cost budget.

        
        - **IncludeCredit** *(boolean) --* A boolean value whether to include credits in the cost budget.

        
        - **IncludeUpfront** *(boolean) --* A boolean value whether to include upfront costs in the cost budget.

        
        - **IncludeRecurring** *(boolean) --* A boolean value whether to include recurring costs in the cost budget.

        
        - **IncludeOtherSubscription** *(boolean) --* A boolean value whether to include other subscription costs in the cost budget.

        
        - **IncludeSupport** *(boolean) --* A boolean value whether to include support costs in the cost budget.

        
      
      - **TimeUnit** *(string) --* **[REQUIRED]** The time unit of the budget. e.g. MONTHLY, QUARTERLY, etc.

      
      - **TimePeriod** *(dict) --* **[REQUIRED]** A time period indicating the start date and end date of a budget.

      
        - **Start** *(datetime) --* **[REQUIRED]** A generic timestamp. In Java it is transformed to a Date object.

        
        - **End** *(datetime) --* **[REQUIRED]** A generic timestamp. In Java it is transformed to a Date object.

        
      
      - **CalculatedSpend** *(dict) --* A structure that holds the actual and forecasted spend for a budget.

      
        - **ActualSpend** *(dict) --* **[REQUIRED]** A structure that represents either a cost spend or usage spend. Contains an amount and a unit.

        
          - **Amount** *(string) --* **[REQUIRED]** A string to represent NumericValue.

          
          - **Unit** *(string) --* **[REQUIRED]** A string to represent budget spend unit. It should be not null and not empty.

          
        
        - **ForecastedSpend** *(dict) --* A structure that represents either a cost spend or usage spend. Contains an amount and a unit.

        
          - **Amount** *(string) --* **[REQUIRED]** A string to represent NumericValue.

          
          - **Unit** *(string) --* **[REQUIRED]** A string to represent budget spend unit. It should be not null and not empty.

          
        
      
      - **BudgetType** *(string) --* **[REQUIRED]** The type of a budget. It should be COST, USAGE, or RI_UTILIZATION.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of UpdateBudget
    

  .. py:method:: update_notification(**kwargs)

    Update the information about a notification already created

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/UpdateNotification>`_    


    **Request Syntax** 
    ::

      response = client.update_notification(
          AccountId='string',
          BudgetName='string',
          OldNotification={
              'NotificationType': 'ACTUAL'|'FORECASTED',
              'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
              'Threshold': 123.0,
              'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
          },
          NewNotification={
              'NotificationType': 'ACTUAL'|'FORECASTED',
              'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
              'Threshold': 123.0,
              'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
          }
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    :type OldNotification: dict
    :param OldNotification: **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

    
      - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

      
      - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

      
      - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

      
      - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

      
    
    :type NewNotification: dict
    :param NewNotification: **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

    
      - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

      
      - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

      
      - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

      
      - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of UpdateNotification
    

  .. py:method:: update_subscriber(**kwargs)

    Update a subscriber

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/UpdateSubscriber>`_    


    **Request Syntax** 
    ::

      response = client.update_subscriber(
          AccountId='string',
          BudgetName='string',
          Notification={
              'NotificationType': 'ACTUAL'|'FORECASTED',
              'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
              'Threshold': 123.0,
              'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
          },
          OldSubscriber={
              'SubscriptionType': 'SNS'|'EMAIL',
              'Address': 'string'
          },
          NewSubscriber={
              'SubscriptionType': 'SNS'|'EMAIL',
              'Address': 'string'
          }
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** Account Id of the customer. It should be a 12 digit number.

    
    :type BudgetName: string
    :param BudgetName: **[REQUIRED]** A string represents the budget name. No ":" and "\" character is allowed.

    
    :type Notification: dict
    :param Notification: **[REQUIRED]** Notification model. Each budget may contain multiple notifications with different settings.

    
      - **NotificationType** *(string) --* **[REQUIRED]** The type of a notification. It should be ACTUAL or FORECASTED.

      
      - **ComparisonOperator** *(string) --* **[REQUIRED]** The comparison operator of a notification. Currently we support less than, equal to and greater than.

      
      - **Threshold** *(float) --* **[REQUIRED]** The threshold of a notification. It should be a number between 0 and 1,000,000,000.

      
      - **ThresholdType** *(string) --* The type of threshold for a notification. It can be PERCENTAGE or ABSOLUTE_VALUE.

      
    
    :type OldSubscriber: dict
    :param OldSubscriber: **[REQUIRED]** Subscriber model. Each notification may contain multiple subscribers with different addresses.

    
      - **SubscriptionType** *(string) --* **[REQUIRED]** The subscription type of the subscriber. It can be SMS or EMAIL.

      
      - **Address** *(string) --* **[REQUIRED]** String containing email or sns topic for the subscriber address.

      
    
    :type NewSubscriber: dict
    :param NewSubscriber: **[REQUIRED]** Subscriber model. Each notification may contain multiple subscribers with different addresses.

    
      - **SubscriptionType** *(string) --* **[REQUIRED]** The subscription type of the subscriber. It can be SMS or EMAIL.

      
      - **Address** *(string) --* **[REQUIRED]** String containing email or sns topic for the subscriber address.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* Response of UpdateSubscriber
    

==========
Paginators
==========


The available paginators are:
