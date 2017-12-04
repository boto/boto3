

*************
EC2ManagedNAT
*************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: EC2ManagedNAT.Client

  A low-level client representing EC2 Managed NAT::

    
    import boto3
    
    client = boto3.client('managednat')

  
  These are the available methods:
  
  *   :py:meth:`~EC2ManagedNAT.Client.can_paginate`

  
  *   :py:meth:`~EC2ManagedNAT.Client.create_nat_gateway`

  
  *   :py:meth:`~EC2ManagedNAT.Client.delete_nat_gateway`

  
  *   :py:meth:`~EC2ManagedNAT.Client.describe_nat_gateway_supported_zones`

  
  *   :py:meth:`~EC2ManagedNAT.Client.describe_nat_gateways`

  
  *   :py:meth:`~EC2ManagedNAT.Client.generate_presigned_url`

  
  *   :py:meth:`~EC2ManagedNAT.Client.get_nat_gateway_count`

  
  *   :py:meth:`~EC2ManagedNAT.Client.get_paginator`

  
  *   :py:meth:`~EC2ManagedNAT.Client.get_waiter`

  

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


  .. py:method:: create_nat_gateway(**kwargs)

    Starts the creation of NAT Gateway in the specified subnet, the provided EIP will be attached. Once the NAT Gateway is in the AVAILABLE state it is ready to be used. This call is idempotent if called with a clientToken.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/managednat-2015-10-01/CreateNatGateway>`_    


    **Request Syntax** 
    ::

      response = client.create_nat_gateway(
          clientToken='string',
          subnetId='string',
          allocationId='string'
      )
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. Constraints: Maximum 64 ASCII characters.

    
    :type subnetId: string
    :param subnetId: **[REQUIRED]** A subnet in which the NAT Gateway will be created. NAT Gateway will place an Elastic Network Interface in this subnet and take one private IP address from the subnets IP range. If you want to use a NAT Gateway to access the Internet or other AWS services outside EC2, please launch it in a public subnet.

    
    :type allocationId: string
    :param allocationId: **[REQUIRED]** The allocation ID of an Elastic IP Address which will be associated with the NAT Gateway.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'clientToken': 'string',
            'NatGateway': {
                'VpcId': 'string',
                'SubnetId': 'string',
                'NatGatewayId': 'string',
                'createTime': datetime(2015, 1, 1),
                'deleteTime': datetime(2015, 1, 1),
                'NatGatewayAddresses': [
                    {
                        'PublicIp': 'string',
                        'AllocationId': 'string',
                        'PrivateIp': 'string',
                        'NetworkInterfaceId': 'string'
                    },
                ],
                'State': 'pending'|'failed'|'available'|'deleting'|'deleted',
                'failureCode': 'string',
                'failureMessage': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **clientToken** *(string) --* Unique, case-sensitive identifier you provide to ensure the idempotency of the request.
        

        - **NatGateway** *(dict) --* Information about the NAT Gateway.
          

          - **VpcId** *(string) --* 
          

          - **SubnetId** *(string) --* 
          

          - **NatGatewayId** *(string) --* 
          

          - **createTime** *(datetime) --* 
          

          - **deleteTime** *(datetime) --* 
          

          - **NatGatewayAddresses** *(list) --* 
            

            - *(dict) --* 
              

              - **PublicIp** *(string) --* 
              

              - **AllocationId** *(string) --* 
              

              - **PrivateIp** *(string) --* 
              

              - **NetworkInterfaceId** *(string) --* 
          
        
          

          - **State** *(string) --* State the NAT Gateway is currently in. 

             
            * 'pending' means the NAT Gateway is still being created and is not ready to serve traffic.
             
            * 'failed' means that the NAT Gateway could not be created. The failureCode/failureMessage will contain the reason.
             
            * 'available' means the NAT Gateway is able to serve traffic.
             
            * 'deleting' means the NAT Gateway may still be serving traffic, but is in the process of tearing down.
             
            * 'deleted' means all NAT Gateway resources have been cleaned up.
             

            
          

          - **failureCode** *(string) --* 
          

          - **failureMessage** *(string) --* Detailed reason for why the NAT Gateway is in the FAILED state.
      
    

  .. py:method:: delete_nat_gateway(**kwargs)

    Deletes a specified NAT Gateway. Deleting the NAT Gateway doesn't delete the NAT Gateway routes in route tables. These routes will be blackholed before manually removed or updated. Deleting the NAT Gateway will disassociate the Elastic IP addresses. If you do not need these addresses any more, please release them to avoid additional cost for keeping these addresses idle.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/managednat-2015-10-01/DeleteNatGateway>`_    


    **Request Syntax** 
    ::

      response = client.delete_nat_gateway(
          natGatewayId='string'
      )
    :type natGatewayId: string
    :param natGatewayId: **[REQUIRED]** The NatGateway ID to delete.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NatGatewayId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NatGatewayId** *(string) --* The deleted NatGateway ID.
    

  .. py:method:: describe_nat_gateway_supported_zones()

    Return the list of zones that are supported by Managed Nat

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/managednat-2015-10-01/DescribeNatGatewaySupportedZones>`_    


    **Request Syntax** 
    ::

      response = client.describe_nat_gateway_supported_zones()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'supportedZones': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **supportedZones** *(list) --* List of supported zones.
          

          - *(string) --* 
      
    

  .. py:method:: describe_nat_gateways(**kwargs)

    Describes one or more NAT Gateways. Call is create/read consistent but the state of the NAT Gateway is updated asynchronously.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/managednat-2015-10-01/DescribeNatGateways>`_    


    **Request Syntax** 
    ::

      response = client.describe_nat_gateways(
          natGatewayId=[
              'string',
          ],
          filters=[
              {
                  'name': 'string',
                  'value': [
                      'string',
                  ]
              },
          ],
          maxResults=123,
          nextToken='string'
      )
    :type natGatewayId: list
    :param natGatewayId: One or more NAT Gateway IDs.

    
      - *(string) --* 

      
  
    :type filters: list
    :param filters: 

    
      - *(dict) --* 

      
        - **name** *(string) --* 

        
        - **value** *(list) --* 

        
          - *(string) --* 

          
      
      
  
    :type maxResults: integer
    :param maxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results. Constraint: Minimum value of 5 and if the value is greater than 1000, we return only 1000 items.

    
    :type nextToken: string
    :param nextToken: The token for the next set of items to return. (You received this token from a prior DescribeNatGateways call)

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'nextToken': 'string',
            'NatGateways': [
                {
                    'VpcId': 'string',
                    'SubnetId': 'string',
                    'NatGatewayId': 'string',
                    'createTime': datetime(2015, 1, 1),
                    'deleteTime': datetime(2015, 1, 1),
                    'NatGatewayAddresses': [
                        {
                            'PublicIp': 'string',
                            'AllocationId': 'string',
                            'PrivateIp': 'string',
                            'NetworkInterfaceId': 'string'
                        },
                    ],
                    'State': 'pending'|'failed'|'available'|'deleting'|'deleted',
                    'failureCode': 'string',
                    'failureMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **nextToken** *(string) --* The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        

        - **NatGateways** *(list) --* Information about the endpoints.
          

          - *(dict) --* 
            

            - **VpcId** *(string) --* 
            

            - **SubnetId** *(string) --* 
            

            - **NatGatewayId** *(string) --* 
            

            - **createTime** *(datetime) --* 
            

            - **deleteTime** *(datetime) --* 
            

            - **NatGatewayAddresses** *(list) --* 
              

              - *(dict) --* 
                

                - **PublicIp** *(string) --* 
                

                - **AllocationId** *(string) --* 
                

                - **PrivateIp** *(string) --* 
                

                - **NetworkInterfaceId** *(string) --* 
            
          
            

            - **State** *(string) --* State the NAT Gateway is currently in. 

               
              * 'pending' means the NAT Gateway is still being created and is not ready to serve traffic.
               
              * 'failed' means that the NAT Gateway could not be created. The failureCode/failureMessage will contain the reason.
               
              * 'available' means the NAT Gateway is able to serve traffic.
               
              * 'deleting' means the NAT Gateway may still be serving traffic, but is in the process of tearing down.
               
              * 'deleted' means all NAT Gateway resources have been cleaned up.
               

              
            

            - **failureCode** *(string) --* 
            

            - **failureMessage** *(string) --* Detailed reason for why the NAT Gateway is in the FAILED state.
        
      
    

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


  .. py:method:: get_nat_gateway_count(**kwargs)

    Get the count of NAT Gateways in the region (Not exposed via Xino). The returned count is eventually consistent.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/managednat-2015-10-01/GetNatGatewayCount>`_    


    **Request Syntax** 
    ::

      response = client.get_nat_gateway_count(
          accountId='string'
      )
    :type accountId: string
    :param accountId: **[REQUIRED]** The customer account Id.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'natGatewayCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **natGatewayCount** *(integer) --* Number of NAT Gateways for the supplied account. This count is eventually consistent.
    

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

        
