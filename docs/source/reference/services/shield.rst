

******
Shield
******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Shield.Client

  A low-level client representing AWS Shield::

    
    import boto3
    
    client = boto3.client('shield')

  
  These are the available methods:
  
  *   :py:meth:`~Shield.Client.can_paginate`

  
  *   :py:meth:`~Shield.Client.create_protection`

  
  *   :py:meth:`~Shield.Client.create_subscription`

  
  *   :py:meth:`~Shield.Client.delete_protection`

  
  *   :py:meth:`~Shield.Client.delete_subscription`

  
  *   :py:meth:`~Shield.Client.describe_attack`

  
  *   :py:meth:`~Shield.Client.describe_protection`

  
  *   :py:meth:`~Shield.Client.describe_subscription`

  
  *   :py:meth:`~Shield.Client.generate_presigned_url`

  
  *   :py:meth:`~Shield.Client.get_paginator`

  
  *   :py:meth:`~Shield.Client.get_subscription_state`

  
  *   :py:meth:`~Shield.Client.get_waiter`

  
  *   :py:meth:`~Shield.Client.list_attacks`

  
  *   :py:meth:`~Shield.Client.list_protections`

  

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


  .. py:method:: create_protection(**kwargs)

    

    Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Elastic Load Balancing load balancer, Elastic IP Address, or an Amazon Route 53 hosted zone.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/CreateProtection>`_    


    **Request Syntax** 
    ::

      response = client.create_protection(
          Name='string',
          ResourceArn='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Friendly name for the ``Protection`` you are creating.

      

    
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The ARN (Amazon Resource Name) of the resource to be protected.

       

      The ARN should be in one of the following formats:

       

       
      * For an Application Load Balancer: ``arn:aws:elasticloadbalancing:*region* :*account-id* :loadbalancer/app/*load-balancer-name* /*load-balancer-id* ``   
       
      * For an Elastic Load Balancer (Classic Load Balancer): ``arn:aws:elasticloadbalancing:*region* :*account-id* :loadbalancer/*load-balancer-name* ``   
       
      * For AWS CloudFront distribution: ``arn:aws:cloudfront::*account-id* :distribution/*distribution-id* ``   
       
      * For Amazon Route 53: ``arn:aws:route53::*account-id* :hostedzone/*hosted-zone-id* ``   
       
      * For an Elastic IP address: ``arn:aws:ec2:*region* :*account-id* :eip-allocation/*allocation-id* ``   
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProtectionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProtectionId** *(string) --* 

          The unique identifier (ID) for the  Protection object that is created.

          
    

  .. py:method:: create_subscription()

    

    Activates AWS Shield Advanced for an account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/CreateSubscription>`_    


    **Request Syntax** 
    ::

      response = client.create_subscription()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_protection(**kwargs)

    

    Deletes an AWS Shield Advanced  Protection .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DeleteProtection>`_    


    **Request Syntax** 
    ::

      response = client.delete_protection(
          ProtectionId='string'
      )
    :type ProtectionId: string
    :param ProtectionId: **[REQUIRED]** 

      The unique identifier (ID) for the  Protection object to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_subscription()

    

    Removes AWS Shield Advanced from an account. AWS Shield Advanced requires a 1-year subscription commitment. You cannot delete a subscription prior to the completion of that commitment. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DeleteSubscription>`_    


    **Request Syntax** 
    ::

      response = client.delete_subscription()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_attack(**kwargs)

    

    Describes the details of a DDoS attack. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeAttack>`_    


    **Request Syntax** 
    ::

      response = client.describe_attack(
          AttackId='string'
      )
    :type AttackId: string
    :param AttackId: **[REQUIRED]** 

      The unique identifier (ID) for the attack that to be described.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Attack': {
                'AttackId': 'string',
                'ResourceArn': 'string',
                'SubResources': [
                    {
                        'Type': 'IP'|'URL',
                        'Id': 'string',
                        'AttackVectors': [
                            {
                                'VectorType': 'string',
                                'VectorCounters': [
                                    {
                                        'Name': 'string',
                                        'Max': 123.0,
                                        'Average': 123.0,
                                        'Sum': 123.0,
                                        'N': 123,
                                        'Unit': 'string'
                                    },
                                ]
                            },
                        ],
                        'Counters': [
                            {
                                'Name': 'string',
                                'Max': 123.0,
                                'Average': 123.0,
                                'Sum': 123.0,
                                'N': 123,
                                'Unit': 'string'
                            },
                        ]
                    },
                ],
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'AttackCounters': [
                    {
                        'Name': 'string',
                        'Max': 123.0,
                        'Average': 123.0,
                        'Sum': 123.0,
                        'N': 123,
                        'Unit': 'string'
                    },
                ],
                'AttackProperties': [
                    {
                        'AttackLayer': 'NETWORK'|'APPLICATION',
                        'AttackPropertyIdentifier': 'DESTINATION_URL'|'REFERRER'|'SOURCE_ASN'|'SOURCE_COUNTRY'|'SOURCE_IP_ADDRESS'|'SOURCE_USER_AGENT',
                        'TopContributors': [
                            {
                                'Name': 'string',
                                'Value': 123
                            },
                        ],
                        'Unit': 'BITS'|'BYTES'|'PACKETS'|'REQUESTS',
                        'Total': 123
                    },
                ],
                'Mitigations': [
                    {
                        'MitigationName': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Attack** *(dict) --* 

          The attack that is described.

          
          

          - **AttackId** *(string) --* 

            The unique identifier (ID) of the attack.

            
          

          - **ResourceArn** *(string) --* 

            The ARN (Amazon Resource Name) of the resource that was attacked.

            
          

          - **SubResources** *(list) --* 

            If applicable, additional detail about the resource being attacked, for example, IP address or URL.

            
            

            - *(dict) --* 

              The attack information for the specified SubResource.

              
              

              - **Type** *(string) --* 

                The ``SubResource`` type.

                
              

              - **Id** *(string) --* 

                The unique identifier (ID) of the ``SubResource`` .

                
              

              - **AttackVectors** *(list) --* 

                The list of attack types and associated counters.

                
                

                - *(dict) --* 

                  A summary of information about the attack.

                  
                  

                  - **VectorType** *(string) --* 

                    The attack type, for example, SNMP reflection or SYN flood.

                    
                  

                  - **VectorCounters** *(list) --* 

                    The list of counters that describe the details of the attack.

                    
                    

                    - *(dict) --* 

                      The counter that describes a DDoS attack.

                      
                      

                      - **Name** *(string) --* 

                        The counter name.

                        
                      

                      - **Max** *(float) --* 

                        The maximum value of the counter for a specified time period.

                        
                      

                      - **Average** *(float) --* 

                        The average value of the counter for a specified time period.

                        
                      

                      - **Sum** *(float) --* 

                        The total of counter values for a specified time period.

                        
                      

                      - **N** *(integer) --* 

                        The number of counters for a specified time period.

                        
                      

                      - **Unit** *(string) --* 

                        The unit of the counters.

                        
                  
                
              
            
              

              - **Counters** *(list) --* 

                The counters that describe the details of the attack.

                
                

                - *(dict) --* 

                  The counter that describes a DDoS attack.

                  
                  

                  - **Name** *(string) --* 

                    The counter name.

                    
                  

                  - **Max** *(float) --* 

                    The maximum value of the counter for a specified time period.

                    
                  

                  - **Average** *(float) --* 

                    The average value of the counter for a specified time period.

                    
                  

                  - **Sum** *(float) --* 

                    The total of counter values for a specified time period.

                    
                  

                  - **N** *(integer) --* 

                    The number of counters for a specified time period.

                    
                  

                  - **Unit** *(string) --* 

                    The unit of the counters.

                    
              
            
          
        
          

          - **StartTime** *(datetime) --* 

            The time the attack started, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

            
          

          - **EndTime** *(datetime) --* 

            The time the attack ended, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

            
          

          - **AttackCounters** *(list) --* 

            List of counters that describe the attack for the specified time period.

            
            

            - *(dict) --* 

              The counter that describes a DDoS attack.

              
              

              - **Name** *(string) --* 

                The counter name.

                
              

              - **Max** *(float) --* 

                The maximum value of the counter for a specified time period.

                
              

              - **Average** *(float) --* 

                The average value of the counter for a specified time period.

                
              

              - **Sum** *(float) --* 

                The total of counter values for a specified time period.

                
              

              - **N** *(integer) --* 

                The number of counters for a specified time period.

                
              

              - **Unit** *(string) --* 

                The unit of the counters.

                
          
        
          

          - **AttackProperties** *(list) --* 

            The array of  AttackProperty objects.

            
            

            - *(dict) --* 

              Details of the described attack.

              
              

              - **AttackLayer** *(string) --* 

                The type of DDoS event that was observed. ``NETWORK`` indicates layer 3 and layer 4 events and ``APPLICATION`` indicates layer 7 events.

                
              

              - **AttackPropertyIdentifier** *(string) --* 

                Defines the DDoS attack property information that is provided.

                
              

              - **TopContributors** *(list) --* 

                The array of  Contributor objects that includes the top five contributors to an attack. 

                
                

                - *(dict) --* 

                  A contributor to the attack and their contribution.

                  
                  

                  - **Name** *(string) --* 

                    The name of the contributor. This is dependent on the ``AttackPropertyIdentifier`` . For example, if the ``AttackPropertyIdentifier`` is ``SOURCE_COUNTRY`` , the ``Name`` could be ``United States`` .

                    
                  

                  - **Value** *(integer) --* 

                    The contribution of this contributor expressed in  Protection units. For example ``10,000`` .

                    
              
            
              

              - **Unit** *(string) --* 

                The unit of the ``Value`` of the contributions.

                
              

              - **Total** *(integer) --* 

                The total contributions made to this attack by all contributors, not just the five listed in the ``TopContributors`` list.

                
          
        
          

          - **Mitigations** *(list) --* 

            List of mitigation actions taken for the attack.

            
            

            - *(dict) --* 

              The mitigation applied to a DDoS attack.

              
              

              - **MitigationName** *(string) --* 

                The name of the mitigation taken for this attack.

                
          
        
      
    

  .. py:method:: describe_protection(**kwargs)

    

    Lists the details of a  Protection object.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeProtection>`_    


    **Request Syntax** 
    ::

      response = client.describe_protection(
          ProtectionId='string'
      )
    :type ProtectionId: string
    :param ProtectionId: **[REQUIRED]** 

      The unique identifier (ID) for the  Protection object that is described.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Protection': {
                'Id': 'string',
                'Name': 'string',
                'ResourceArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Protection** *(dict) --* 

          The  Protection object that is described.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of the protection.

            
          

          - **Name** *(string) --* 

            The friendly name of the protection. For example, ``My CloudFront distributions`` .

            
          

          - **ResourceArn** *(string) --* 

            The ARN (Amazon Resource Name) of the AWS resource that is protected.

            
      
    

  .. py:method:: describe_subscription()

    

    Provides details about the AWS Shield Advanced subscription for an account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeSubscription>`_    


    **Request Syntax** 
    ::

      response = client.describe_subscription()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Subscription': {
                'StartTime': datetime(2015, 1, 1),
                'TimeCommitmentInSeconds': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Subscription** *(dict) --* 

          The AWS Shield Advanced subscription details for an account.

          
          

          - **StartTime** *(datetime) --* 

            The start time of the subscription, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

            
          

          - **TimeCommitmentInSeconds** *(integer) --* 

            The length, in seconds, of the AWS Shield Advanced subscription for the account.

            
      
    

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


  .. py:method:: get_subscription_state()

    

    Returns the ``SubscriptionState`` , either ``Active`` or ``Inactive`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/GetSubscriptionState>`_    


    **Request Syntax** 
    ::

      response = client.get_subscription_state()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SubscriptionState': 'ACTIVE'|'INACTIVE'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SubscriptionState** *(string) --* 

          The status of the subscription.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_attacks(**kwargs)

    

    Returns all ongoing DDoS attacks or all DDoS attacks during a specified time period.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/ListAttacks>`_    


    **Request Syntax** 
    ::

      response = client.list_attacks(
          ResourceArns=[
              'string',
          ],
          StartTime={
              'FromInclusive': datetime(2015, 1, 1),
              'ToExclusive': datetime(2015, 1, 1)
          },
          EndTime={
              'FromInclusive': datetime(2015, 1, 1),
              'ToExclusive': datetime(2015, 1, 1)
          },
          NextToken='string',
          MaxResults=123
      )
    :type ResourceArns: list
    :param ResourceArns: 

      The ARN (Amazon Resource Name) of the resource that was attacked. If this is left blank, all applicable resources for this account will be included.

      

    
      - *(string) --* 

      
  
    :type StartTime: dict
    :param StartTime: 

      The start of the time period for the attacks. This is a ``timestamp`` type. The sample request above indicates a ``number`` type because the default used by WAF is Unix time in seconds. However any valid `timestamp format <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is allowed. 

      

    
      - **FromInclusive** *(datetime) --* 

        The start time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

        

      
      - **ToExclusive** *(datetime) --* 

        The end time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

        

      
    
    :type EndTime: dict
    :param EndTime: 

      The end of the time period for the attacks. This is a ``timestamp`` type. The sample request above indicates a ``number`` type because the default used by WAF is Unix time in seconds. However any valid `timestamp format <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is allowed. 

      

    
      - **FromInclusive** *(datetime) --* 

        The start time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

        

      
      - **ToExclusive** *(datetime) --* 

        The end time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

        

      
    
    :type NextToken: string
    :param NextToken: 

      The ``ListAttacksRequest.NextMarker`` value from a previous call to ``ListAttacksRequest`` . Pass null if this is the first call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of  AttackSummary objects to be returned. If this is left blank, the first 20 results will be returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AttackSummaries': [
                {
                    'AttackId': 'string',
                    'ResourceArn': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'AttackVectors': [
                        {
                            'VectorType': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AttackSummaries** *(list) --* 

          The attack information for the specified time range.

          
          

          - *(dict) --* 

            Summarizes all DDoS attacks for a specified time period.

            
            

            - **AttackId** *(string) --* 

              The unique identifier (ID) of the attack.

              
            

            - **ResourceArn** *(string) --* 

              The ARN (Amazon Resource Name) of the resource that was attacked.

              
            

            - **StartTime** *(datetime) --* 

              The start time of the attack, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

              
            

            - **EndTime** *(datetime) --* 

              The end time of the attack, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

              
            

            - **AttackVectors** *(list) --* 

              The list of attacks for a specified time period.

              
              

              - *(dict) --* 

                Describes the attack.

                
                

                - **VectorType** *(string) --* 

                  The attack type. Valid values:

                   

                   
                  * UDP_TRAFFIC 
                   
                  * UDP_FRAGMENT 
                   
                  * GENERIC_UDP_REFLECTION 
                   
                  * DNS_REFLECTION 
                   
                  * NTP_REFLECTION 
                   
                  * CHARGEN_REFLECTION 
                   
                  * SSDP_REFLECTION 
                   
                  * PORT_MAPPER 
                   
                  * RIP_REFLECTION 
                   
                  * SNMP_REFLECTION 
                   
                  * MSSQL_REFLECTION 
                   
                  * NET_BIOS_REFLECTION 
                   
                  * SYN_FLOOD 
                   
                  * ACK_FLOOD 
                   
                  * REQUEST_FLOOD 
                   

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          The token returned by a previous call to indicate that there is more data available. If not null, more results are available. Pass this value for the ``NextMarker`` parameter in a subsequent call to ``ListAttacks`` to retrieve the next set of items.

          
    

  .. py:method:: list_protections(**kwargs)

    

    Lists all  Protection objects for the account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/ListProtections>`_    


    **Request Syntax** 
    ::

      response = client.list_protections(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      The ``ListProtectionsRequest.NextToken`` value from a previous call to ``ListProtections`` . Pass null if this is the first call.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of  Protection objects to be returned. If this is left blank the first 20 results will be returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Protections': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'ResourceArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Protections** *(list) --* 

          The array of enabled  Protection objects.

          
          

          - *(dict) --* 

            An object that represents a resource that is under DDoS protection.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the protection.

              
            

            - **Name** *(string) --* 

              The friendly name of the protection. For example, ``My CloudFront distributions`` .

              
            

            - **ResourceArn** *(string) --* 

              The ARN (Amazon Resource Name) of the AWS resource that is protected.

              
        
      
        

        - **NextToken** *(string) --* 

          If you specify a value for ``MaxResults`` and you have more Protections than the value of MaxResults, AWS Shield Advanced returns a NextToken value in the response that allows you to list another group of Protections. For the second and subsequent ListProtections requests, specify the value of NextToken from the previous response to get information about another batch of Protections.

          
    

==========
Paginators
==========


The available paginators are:
