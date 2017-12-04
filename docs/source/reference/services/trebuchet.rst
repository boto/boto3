

*********
Trebuchet
*********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Trebuchet.Client

  A low-level client representing AWS Trebuchet::

    
    import boto3
    
    client = boto3.client('trebuchet')

  
  These are the available methods:
  
  *   :py:meth:`can_paginate`

  
  *   :py:meth:`create_feature_release`

  
  *   :py:meth:`generate_presigned_url`

  
  *   :py:meth:`get_artifacts`

  
  *   :py:meth:`get_assigned_activities`

  
  *   :py:meth:`get_feature_release`

  
  *   :py:meth:`get_paginator`

  
  *   :py:meth:`get_waiter`

  
  *   :py:meth:`list_feature_releases`

  
  *   :py:meth:`put_artifacts`

  
  *   :py:meth:`update_activity`

  
  *   :py:meth:`update_feature`

  

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


  .. py:method:: create_feature_release(**kwargs)

    

    **Request Syntax** 
    ::

      response = client.create_feature_release(
          featureName='string',
          serviceName='string',
          description='string',
          serviceOwner='string',
          sdkOwner='string',
          serviceReleaseDate=datetime(2015, 1, 1),
          sdkReleaseDate=datetime(2015, 1, 1),
          type='CUSTOM_SDK_WORK'|'NEW_SERVICE'|'NEW_FEATURE'|'DOC_UPDATE'
      )
    :type featureName: string
    :param featureName: 

    
    :type serviceName: string
    :param serviceName: 

    
    :type description: string
    :param description: 

    
    :type serviceOwner: string
    :param serviceOwner: 

    
    :type sdkOwner: string
    :param sdkOwner: 

    
    :type serviceReleaseDate: datetime
    :param serviceReleaseDate: 

    
    :type sdkReleaseDate: datetime
    :param sdkReleaseDate: 

    
    :type type: string
    :param type: 

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'featureArn': 'string',
            'creationTime': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **featureArn** *(string) --* 
        

        - **creationTime** *(datetime) --* 
    

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


  .. py:method:: get_artifacts(**kwargs)

    

    **Request Syntax** 
    ::

      response = client.get_artifacts(
          featureArn='string'
      )
    :type featureArn: string
    :param featureArn: **[REQUIRED]** 

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'artifacts': [
                {
                    'name': 'string',
                    'type': 'string',
                    'description': 'string',
                    'data': b'bytes',
                    'processState': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **artifacts** *(list) --* 
          

          - *(dict) --* 
            

            - **name** *(string) --* 
            

            - **type** *(string) --* 
            

            - **description** *(string) --* 
            

            - **data** *(bytes) --* 
            

            - **processState** *(string) --* 
        
      
    

  .. py:method:: get_assigned_activities(**kwargs)

    

    **Request Syntax** 
    ::

      response = client.get_assigned_activities(
          user='string'
      )
    :type user: string
    :param user: **[REQUIRED]** 

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'activities': [
                {
                    'activityArn': 'string',
                    'parent': 'string',
                    'featureArn': 'string',
                    'description': 'string',
                    'status': 'string',
                    'statusReason': 'string',
                    'assignee': 'string',
                    'approver': 'string',
                    'leadtime': {
                        'unit': 'string',
                        'value': 123
                    },
                    'details': {
                        'relatedItems': [
                            {
                                'type': 'string',
                                'value': b'bytes'
                            },
                        ],
                        'timeline': {
                            'start': datetime(2015, 1, 1),
                            'estimatedFinish': datetime(2015, 1, 1),
                            'actualFinish': datetime(2015, 1, 1)
                        }
                    }
                },
            ],
            'featureSummaries': {
                'string': {
                    'name': 'string',
                    'service': 'string',
                    'type': 'string',
                    'description': 'string',
                    'sdkOwner': 'string',
                    'serviceOwner': 'string',
                    'serviceReleaseDate': datetime(2015, 1, 1),
                    'sdkReleaseDate': datetime(2015, 1, 1)
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **activities** *(list) --* 
          

          - *(dict) --* 
            

            - **activityArn** *(string) --* 
            

            - **parent** *(string) --* 
            

            - **featureArn** *(string) --* 
            

            - **description** *(string) --* 
            

            - **status** *(string) --* 
            

            - **statusReason** *(string) --* 
            

            - **assignee** *(string) --* 
            

            - **approver** *(string) --* 
            

            - **leadtime** *(dict) --* 
              

              - **unit** *(string) --* 
              

              - **value** *(integer) --* 
          
            

            - **details** *(dict) --* 
              

              - **relatedItems** *(list) --* 
                

                - *(dict) --* 
                  

                  - **type** *(string) --* 
                  

                  - **value** *(bytes) --* 
              
            
              

              - **timeline** *(dict) --* 
                

                - **start** *(datetime) --* 
                

                - **estimatedFinish** *(datetime) --* 
                

                - **actualFinish** *(datetime) --* 
            
          
        
      
        

        - **featureSummaries** *(dict) --* 
          

          - *(string) --* 
            

            - *(dict) --* 
              

              - **name** *(string) --* 
              

              - **service** *(string) --* 
              

              - **type** *(string) --* 
              

              - **description** *(string) --* 
              

              - **sdkOwner** *(string) --* 
              

              - **serviceOwner** *(string) --* 
              

              - **serviceReleaseDate** *(datetime) --* 
              

              - **sdkReleaseDate** *(datetime) --* 
          
      
    
    

  .. py:method:: get_feature_release(**kwargs)

    

    **Request Syntax** 
    ::

      response = client.get_feature_release(
          featureArn='string'
      )
    :type featureArn: string
    :param featureArn: **[REQUIRED]** 

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'feature': {
                'featureArn': 'string',
                'name': 'string',
                'service': 'string',
                'type': 'string',
                'description': 'string',
                'serviceOwner': 'string',
                'sdkOwner': 'string',
                'serviceReleaseDate': datetime(2015, 1, 1),
                'sdkReleaseDate': datetime(2015, 1, 1),
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'activities': [
                    {
                        'activityArn': 'string',
                        'parent': 'string',
                        'featureArn': 'string',
                        'description': 'string',
                        'status': 'string',
                        'statusReason': 'string',
                        'assignee': 'string',
                        'approver': 'string',
                        'leadtime': {
                            'unit': 'string',
                            'value': 123
                        },
                        'details': {
                            'relatedItems': [
                                {
                                    'type': 'string',
                                    'value': b'bytes'
                                },
                            ],
                            'timeline': {
                                'start': datetime(2015, 1, 1),
                                'estimatedFinish': datetime(2015, 1, 1),
                                'actualFinish': datetime(2015, 1, 1)
                            }
                        }
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **feature** *(dict) --* 
          

          - **featureArn** *(string) --* 
          

          - **name** *(string) --* 
          

          - **service** *(string) --* 
          

          - **type** *(string) --* 
          

          - **description** *(string) --* 
          

          - **serviceOwner** *(string) --* 
          

          - **sdkOwner** *(string) --* 
          

          - **serviceReleaseDate** *(datetime) --* 
          

          - **sdkReleaseDate** *(datetime) --* 
          

          - **creationTime** *(datetime) --* 
          

          - **lastUpdatedTime** *(datetime) --* 
          

          - **activities** *(list) --* 
            

            - *(dict) --* 
              

              - **activityArn** *(string) --* 
              

              - **parent** *(string) --* 
              

              - **featureArn** *(string) --* 
              

              - **description** *(string) --* 
              

              - **status** *(string) --* 
              

              - **statusReason** *(string) --* 
              

              - **assignee** *(string) --* 
              

              - **approver** *(string) --* 
              

              - **leadtime** *(dict) --* 
                

                - **unit** *(string) --* 
                

                - **value** *(integer) --* 
            
              

              - **details** *(dict) --* 
                

                - **relatedItems** *(list) --* 
                  

                  - *(dict) --* 
                    

                    - **type** *(string) --* 
                    

                    - **value** *(bytes) --* 
                
              
                

                - **timeline** *(dict) --* 
                  

                  - **start** *(datetime) --* 
                  

                  - **estimatedFinish** *(datetime) --* 
                  

                  - **actualFinish** *(datetime) --* 
              
            
          
        
      
    

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

        


  .. py:method:: list_feature_releases(**kwargs)

    

    **Request Syntax** 
    ::

      response = client.list_feature_releases(
          filter={
              'service': 'string',
              'serviceOwner': 'string',
              'sdkOwner': 'string',
              'serviceReleaseDateRange': {
                  'From': datetime(2015, 1, 1),
                  'To': datetime(2015, 1, 1)
              },
              'sdkReleaseDateRange': {
                  'From': datetime(2015, 1, 1),
                  'To': datetime(2015, 1, 1)
              }
          }
      )
    :type filter: dict
    :param filter: 

    
      - **service** *(string) --* 

      
      - **serviceOwner** *(string) --* 

      
      - **sdkOwner** *(string) --* 

      
      - **serviceReleaseDateRange** *(dict) --* 

      
        - **From** *(datetime) --* 

        
        - **To** *(datetime) --* 

        
      
      - **sdkReleaseDateRange** *(dict) --* 

      
        - **From** *(datetime) --* 

        
        - **To** *(datetime) --* 

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'featureSummaries': {
                'string': {
                    'name': 'string',
                    'service': 'string',
                    'type': 'string',
                    'description': 'string',
                    'sdkOwner': 'string',
                    'serviceOwner': 'string',
                    'serviceReleaseDate': datetime(2015, 1, 1),
                    'sdkReleaseDate': datetime(2015, 1, 1)
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **featureSummaries** *(dict) --* 
          

          - *(string) --* 
            

            - *(dict) --* 
              

              - **name** *(string) --* 
              

              - **service** *(string) --* 
              

              - **type** *(string) --* 
              

              - **description** *(string) --* 
              

              - **sdkOwner** *(string) --* 
              

              - **serviceOwner** *(string) --* 
              

              - **serviceReleaseDate** *(datetime) --* 
              

              - **sdkReleaseDate** *(datetime) --* 
          
      
    
    

  .. py:method:: put_artifacts(**kwargs)

    

    **Request Syntax** 
    ::

      response = client.put_artifacts(
          featureArn='string',
          activityArn='string',
          artifacts=[
              {
                  'name': 'string',
                  'type': 'string',
                  'description': 'string',
                  'data': b'bytes',
                  'processState': 'string'
              },
          ]
      )
    :type featureArn: string
    :param featureArn: **[REQUIRED]** 

    
    :type activityArn: string
    :param activityArn: 

    
    :type artifacts: list
    :param artifacts: **[REQUIRED]** 

    
      - *(dict) --* 

      
        - **name** *(string) --* **[REQUIRED]** 

        
        - **type** *(string) --* 

        
        - **description** *(string) --* 

        
        - **data** *(bytes) --* 

        
        - **processState** *(string) --* 

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_activity(**kwargs)

    

    **Request Syntax** 
    ::

      response = client.update_activity(
          activityArn='string',
          status='string',
          statusReason='string',
          description='string',
          assignee='string',
          approver='string'
      )
    :type activityArn: string
    :param activityArn: **[REQUIRED]** 

    
    :type status: string
    :param status: 

    
    :type statusReason: string
    :param statusReason: 

    
    :type description: string
    :param description: 

    
    :type assignee: string
    :param assignee: 

    
    :type approver: string
    :param approver: 

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_feature(**kwargs)

    

    **Request Syntax** 
    ::

      response = client.update_feature(
          featureArn='string',
          featureName='string',
          serviceName='string',
          description='string',
          serviceOwner='string',
          sdkOwner='string',
          serviceReleaseDate=datetime(2015, 1, 1),
          sdkReleaseDate=datetime(2015, 1, 1)
      )
    :type featureArn: string
    :param featureArn: **[REQUIRED]** 

    
    :type featureName: string
    :param featureName: 

    
    :type serviceName: string
    :param serviceName: 

    
    :type description: string
    :param description: 

    
    :type serviceOwner: string
    :param serviceOwner: 

    
    :type sdkOwner: string
    :param sdkOwner: 

    
    :type serviceReleaseDate: datetime
    :param serviceReleaseDate: 

    
    :type sdkReleaseDate: datetime
    :param sdkReleaseDate: 

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'feature': {
                'featureArn': 'string',
                'name': 'string',
                'service': 'string',
                'type': 'string',
                'description': 'string',
                'serviceOwner': 'string',
                'sdkOwner': 'string',
                'serviceReleaseDate': datetime(2015, 1, 1),
                'sdkReleaseDate': datetime(2015, 1, 1),
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'activities': [
                    {
                        'activityArn': 'string',
                        'parent': 'string',
                        'featureArn': 'string',
                        'description': 'string',
                        'status': 'string',
                        'statusReason': 'string',
                        'assignee': 'string',
                        'approver': 'string',
                        'leadtime': {
                            'unit': 'string',
                            'value': 123
                        },
                        'details': {
                            'relatedItems': [
                                {
                                    'type': 'string',
                                    'value': b'bytes'
                                },
                            ],
                            'timeline': {
                                'start': datetime(2015, 1, 1),
                                'estimatedFinish': datetime(2015, 1, 1),
                                'actualFinish': datetime(2015, 1, 1)
                            }
                        }
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **feature** *(dict) --* 
          

          - **featureArn** *(string) --* 
          

          - **name** *(string) --* 
          

          - **service** *(string) --* 
          

          - **type** *(string) --* 
          

          - **description** *(string) --* 
          

          - **serviceOwner** *(string) --* 
          

          - **sdkOwner** *(string) --* 
          

          - **serviceReleaseDate** *(datetime) --* 
          

          - **sdkReleaseDate** *(datetime) --* 
          

          - **creationTime** *(datetime) --* 
          

          - **lastUpdatedTime** *(datetime) --* 
          

          - **activities** *(list) --* 
            

            - *(dict) --* 
              

              - **activityArn** *(string) --* 
              

              - **parent** *(string) --* 
              

              - **featureArn** *(string) --* 
              

              - **description** *(string) --* 
              

              - **status** *(string) --* 
              

              - **statusReason** *(string) --* 
              

              - **assignee** *(string) --* 
              

              - **approver** *(string) --* 
              

              - **leadtime** *(dict) --* 
                

                - **unit** *(string) --* 
                

                - **value** *(integer) --* 
            
              

              - **details** *(dict) --* 
                

                - **relatedItems** *(list) --* 
                  

                  - *(dict) --* 
                    

                    - **type** *(string) --* 
                    

                    - **value** *(bytes) --* 
                
              
                

                - **timeline** *(dict) --* 
                  

                  - **start** *(datetime) --* 
                  

                  - **estimatedFinish** *(datetime) --* 
                  

                  - **actualFinish** *(datetime) --* 
              
            
          
        
      
    