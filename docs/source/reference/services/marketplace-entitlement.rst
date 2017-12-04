

*****************************
MarketplaceEntitlementService
*****************************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: MarketplaceEntitlementService.Client

  A low-level client representing AWS Marketplace Entitlement Service::

    
    import boto3
    
    client = boto3.client('marketplace-entitlement')

  
  These are the available methods:
  
  *   :py:meth:`~MarketplaceEntitlementService.Client.can_paginate`

  
  *   :py:meth:`~MarketplaceEntitlementService.Client.generate_presigned_url`

  
  *   :py:meth:`~MarketplaceEntitlementService.Client.get_entitlements`

  
  *   :py:meth:`~MarketplaceEntitlementService.Client.get_paginator`

  
  *   :py:meth:`~MarketplaceEntitlementService.Client.get_waiter`

  

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


  .. py:method:: get_entitlements(**kwargs)

    

    GetEntitlements retrieves entitlement values for a given product. The results can be filtered based on customer identifier or product dimensions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/entitlement.marketplace-2017-01-11/GetEntitlements>`_    


    **Request Syntax** 
    ::

      response = client.get_entitlements(
          ProductCode='string',
          Filter={
              'string': [
                  'string',
              ]
          },
          NextToken='string',
          MaxResults=123
      )
    :type ProductCode: string
    :param ProductCode: **[REQUIRED]** 

      Product code is used to uniquely identify a product in AWS Marketplace. The product code will be provided by AWS Marketplace when the product listing is created.

      

    
    :type Filter: dict
    :param Filter: 

      Filter is used to return entitlements for a specific customer or for a specific dimension. Filters are described as keys mapped to a lists of values. Filtered requests are *unioned* for each value in the value list, and then *intersected* for each filter key.

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(string) --* 

          
      
  

    :type NextToken: string
    :param NextToken: 

      For paginated calls to GetEntitlements, pass the NextToken from the previous GetEntitlementsResult.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items to retrieve from the GetEntitlements operation. For pagination, use the NextToken field in subsequent calls to GetEntitlements.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Entitlements': [
                {
                    'ProductCode': 'string',
                    'Dimension': 'string',
                    'CustomerIdentifier': 'string',
                    'Value': {
                        'IntegerValue': 123,
                        'DoubleValue': 123.0,
                        'BooleanValue': True|False,
                        'StringValue': 'string'
                    },
                    'ExpirationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The GetEntitlementsRequest contains results from the GetEntitlements operation.

        
        

        - **Entitlements** *(list) --* 

          The set of entitlements found through the GetEntitlements operation. If the result contains an empty set of entitlements, NextToken might still be present and should be used.

          
          

          - *(dict) --* 

            An entitlement represents capacity in a product owned by the customer. For example, a customer might own some number of users or seats in an SaaS application or some amount of data capacity in a multi-tenant database.

            
            

            - **ProductCode** *(string) --* 

              The product code for which the given entitlement applies. Product codes are provided by AWS Marketplace when the product listing is created.

              
            

            - **Dimension** *(string) --* 

              The dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.

              
            

            - **CustomerIdentifier** *(string) --* 

              The customer identifier is a handle to each unique customer in an application. Customer identifiers are obtained through the ResolveCustomer operation in AWS Marketplace Metering Service.

              
            

            - **Value** *(dict) --* 

              The EntitlementValue represents the amount of capacity that the customer is entitled to for the product.

              
              

              - **IntegerValue** *(integer) --* 

                The IntegerValue field will be populated with an integer value when the entitlement is an integer type. Otherwise, the field will not be set.

                
              

              - **DoubleValue** *(float) --* 

                The DoubleValue field will be populated with a double value when the entitlement is a double type. Otherwise, the field will not be set.

                
              

              - **BooleanValue** *(boolean) --* 

                The BooleanValue field will be populated with a boolean value when the entitlement is a boolean type. Otherwise, the field will not be set.

                
              

              - **StringValue** *(string) --* 

                The StringValue field will be populated with a string value when the entitlement is a string type. Otherwise, the field will not be set.

                
          
            

            - **ExpirationDate** *(datetime) --* 

              The expiration date represents the minimum date through which this entitlement is expected to remain valid. For contractual products listed on AWS Marketplace, the expiration date is the date at which the customer will renew or cancel their contract. Customers who are opting to renew their contract will still have entitlements with an expiration date.

              
        
      
        

        - **NextToken** *(string) --* 

          For paginated results, use NextToken in subsequent calls to GetEntitlements. If the result contains an empty set of entitlements, NextToken might still be present and should be used.

          
    

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
