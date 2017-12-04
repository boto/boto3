

*************
DirectConnect
*************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: DirectConnect.Client

  A low-level client representing AWS Direct Connect::

    
    import boto3
    
    client = boto3.client('directconnect')

  
  These are the available methods:
  
  *   :py:meth:`~DirectConnect.Client.allocate_connection_on_interconnect`

  
  *   :py:meth:`~DirectConnect.Client.allocate_hosted_connection`

  
  *   :py:meth:`~DirectConnect.Client.allocate_private_virtual_interface`

  
  *   :py:meth:`~DirectConnect.Client.allocate_public_virtual_interface`

  
  *   :py:meth:`~DirectConnect.Client.associate_connection_with_lag`

  
  *   :py:meth:`~DirectConnect.Client.associate_hosted_connection`

  
  *   :py:meth:`~DirectConnect.Client.associate_virtual_interface`

  
  *   :py:meth:`~DirectConnect.Client.can_paginate`

  
  *   :py:meth:`~DirectConnect.Client.confirm_connection`

  
  *   :py:meth:`~DirectConnect.Client.confirm_private_virtual_interface`

  
  *   :py:meth:`~DirectConnect.Client.confirm_public_virtual_interface`

  
  *   :py:meth:`~DirectConnect.Client.create_bgp_peer`

  
  *   :py:meth:`~DirectConnect.Client.create_connection`

  
  *   :py:meth:`~DirectConnect.Client.create_direct_connect_gateway`

  
  *   :py:meth:`~DirectConnect.Client.create_direct_connect_gateway_association`

  
  *   :py:meth:`~DirectConnect.Client.create_interconnect`

  
  *   :py:meth:`~DirectConnect.Client.create_lag`

  
  *   :py:meth:`~DirectConnect.Client.create_private_virtual_interface`

  
  *   :py:meth:`~DirectConnect.Client.create_public_virtual_interface`

  
  *   :py:meth:`~DirectConnect.Client.delete_bgp_peer`

  
  *   :py:meth:`~DirectConnect.Client.delete_connection`

  
  *   :py:meth:`~DirectConnect.Client.delete_direct_connect_gateway`

  
  *   :py:meth:`~DirectConnect.Client.delete_direct_connect_gateway_association`

  
  *   :py:meth:`~DirectConnect.Client.delete_interconnect`

  
  *   :py:meth:`~DirectConnect.Client.delete_lag`

  
  *   :py:meth:`~DirectConnect.Client.delete_virtual_interface`

  
  *   :py:meth:`~DirectConnect.Client.describe_connection_loa`

  
  *   :py:meth:`~DirectConnect.Client.describe_connections`

  
  *   :py:meth:`~DirectConnect.Client.describe_connections_on_interconnect`

  
  *   :py:meth:`~DirectConnect.Client.describe_direct_connect_gateway_associations`

  
  *   :py:meth:`~DirectConnect.Client.describe_direct_connect_gateway_attachments`

  
  *   :py:meth:`~DirectConnect.Client.describe_direct_connect_gateways`

  
  *   :py:meth:`~DirectConnect.Client.describe_hosted_connections`

  
  *   :py:meth:`~DirectConnect.Client.describe_interconnect_loa`

  
  *   :py:meth:`~DirectConnect.Client.describe_interconnects`

  
  *   :py:meth:`~DirectConnect.Client.describe_lags`

  
  *   :py:meth:`~DirectConnect.Client.describe_loa`

  
  *   :py:meth:`~DirectConnect.Client.describe_locations`

  
  *   :py:meth:`~DirectConnect.Client.describe_tags`

  
  *   :py:meth:`~DirectConnect.Client.describe_virtual_gateways`

  
  *   :py:meth:`~DirectConnect.Client.describe_virtual_interfaces`

  
  *   :py:meth:`~DirectConnect.Client.disassociate_connection_from_lag`

  
  *   :py:meth:`~DirectConnect.Client.generate_presigned_url`

  
  *   :py:meth:`~DirectConnect.Client.get_paginator`

  
  *   :py:meth:`~DirectConnect.Client.get_waiter`

  
  *   :py:meth:`~DirectConnect.Client.tag_resource`

  
  *   :py:meth:`~DirectConnect.Client.untag_resource`

  
  *   :py:meth:`~DirectConnect.Client.update_lag`

  

  .. py:method:: allocate_connection_on_interconnect(**kwargs)

    

    Deprecated in favor of  AllocateHostedConnection .

     

    Creates a hosted connection on an interconnect.

     

    Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the given interconnect.

     

    .. note::

       

      This is intended for use by AWS Direct Connect partners only.

       

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AllocateConnectionOnInterconnect>`_    


    **Request Syntax** 
    ::

      response = client.allocate_connection_on_interconnect(
          bandwidth='string',
          connectionName='string',
          ownerAccount='string',
          interconnectId='string',
          vlan=123
      )
    :type bandwidth: string
    :param bandwidth: **[REQUIRED]** 

      Bandwidth of the connection.

       

      Example: "*500Mbps* "

       

      Default: None

       

      Values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, or 500Mbps

      

    
    :type connectionName: string
    :param connectionName: **[REQUIRED]** 

      Name of the provisioned connection.

       

      Example: "*500M Connection to AWS* "

       

      Default: None

      

    
    :type ownerAccount: string
    :param ownerAccount: **[REQUIRED]** 

      Numeric account Id of the customer for whom the connection will be provisioned.

       

      Example: 123443215678

       

      Default: None

      

    
    :type interconnectId: string
    :param interconnectId: **[REQUIRED]** 

      ID of the interconnect on which the connection will be provisioned.

       

      Example: dxcon-456abc78

       

      Default: None

      

    
    :type vlan: integer
    :param vlan: **[REQUIRED]** 

      The dedicated VLAN provisioned to the connection.

       

      Example: 101

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A connection represents the physical network connection between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new connection.

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **connectionName** *(string) --* 

          The name of the connection.

           

          Example: "*My Connection to AWS* "

           

          Default: None

          
        

        - **connectionState** *(string) --* 

          State of the connection.

           

           
          * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
           
          * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The connection has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the connection is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The connection is in the process of being deleted. 
           
          * **Deleted** : The connection has been deleted. 
           
          * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
           

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **bandwidth** *(string) --* 

          Bandwidth of the connection.

           

          Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

           

          Default: None

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **partnerName** *(string) --* 

          The name of the AWS Direct Connect service provider associated with the connection.

          
        

        - **loaIssueTime** *(datetime) --* 

          The time of the most recent call to  DescribeLoa for this connection.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **awsDevice** *(string) --* 

          The Direct Connection endpoint which the physical connection terminates on.

          
    

  .. py:method:: allocate_hosted_connection(**kwargs)

    

    Creates a hosted connection on an interconnect or a link aggregation group (LAG).

     

    Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the given interconnect or LAG.

     

    .. note::

       

      This is intended for use by AWS Direct Connect partners only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AllocateHostedConnection>`_    


    **Request Syntax** 
    ::

      response = client.allocate_hosted_connection(
          connectionId='string',
          ownerAccount='string',
          bandwidth='string',
          connectionName='string',
          vlan=123
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the interconnect or LAG on which the connection will be provisioned.

       

      Example: dxcon-456abc78 or dxlag-abc123

       

      Default: None

      

    
    :type ownerAccount: string
    :param ownerAccount: **[REQUIRED]** 

      The numeric account ID of the customer for whom the connection will be provisioned.

       

      Example: 123443215678

       

      Default: None

      

    
    :type bandwidth: string
    :param bandwidth: **[REQUIRED]** 

      The bandwidth of the connection.

       

      Example: ``500Mbps``  

       

      Default: None

       

      Values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, or 500Mbps

      

    
    :type connectionName: string
    :param connectionName: **[REQUIRED]** 

      The name of the provisioned connection.

       

      Example: "``500M Connection to AWS`` "

       

      Default: None

      

    
    :type vlan: integer
    :param vlan: **[REQUIRED]** 

      The dedicated VLAN provisioned to the hosted connection.

       

      Example: 101

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A connection represents the physical network connection between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new connection.

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **connectionName** *(string) --* 

          The name of the connection.

           

          Example: "*My Connection to AWS* "

           

          Default: None

          
        

        - **connectionState** *(string) --* 

          State of the connection.

           

           
          * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
           
          * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The connection has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the connection is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The connection is in the process of being deleted. 
           
          * **Deleted** : The connection has been deleted. 
           
          * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
           

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **bandwidth** *(string) --* 

          Bandwidth of the connection.

           

          Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

           

          Default: None

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **partnerName** *(string) --* 

          The name of the AWS Direct Connect service provider associated with the connection.

          
        

        - **loaIssueTime** *(datetime) --* 

          The time of the most recent call to  DescribeLoa for this connection.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **awsDevice** *(string) --* 

          The Direct Connection endpoint which the physical connection terminates on.

          
    

  .. py:method:: allocate_private_virtual_interface(**kwargs)

    

    Provisions a private virtual interface to be owned by another AWS customer.

     

    Virtual interfaces created using this action must be confirmed by the virtual interface owner by using the  ConfirmPrivateVirtualInterface action. Until then, the virtual interface will be in 'Confirming' state, and will not be available for handling traffic.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AllocatePrivateVirtualInterface>`_    


    **Request Syntax** 
    ::

      response = client.allocate_private_virtual_interface(
          connectionId='string',
          ownerAccount='string',
          newPrivateVirtualInterfaceAllocation={
              'virtualInterfaceName': 'string',
              'vlan': 123,
              'asn': 123,
              'authKey': 'string',
              'amazonAddress': 'string',
              'addressFamily': 'ipv4'|'ipv6',
              'customerAddress': 'string'
          }
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The connection ID on which the private virtual interface is provisioned.

       

      Default: None

      

    
    :type ownerAccount: string
    :param ownerAccount: **[REQUIRED]** 

      The AWS account that will own the new private virtual interface.

       

      Default: None

      

    
    :type newPrivateVirtualInterfaceAllocation: dict
    :param newPrivateVirtualInterfaceAllocation: **[REQUIRED]** 

      Detailed information for the private virtual interface to be provisioned.

       

      Default: None

      

    
      - **virtualInterfaceName** *(string) --* **[REQUIRED]** 

        The name of the virtual interface assigned by the customer.

         

        Example: "My VPC"

        

      
      - **vlan** *(integer) --* **[REQUIRED]** 

        The VLAN ID.

         

        Example: 101

        

      
      - **asn** *(integer) --* **[REQUIRED]** 

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

         

        Example: 65000

        

      
      - **authKey** *(string) --* 

        The authentication key for BGP configuration.

         

        Example: asdf34example

        

      
      - **amazonAddress** *(string) --* 

        IP address assigned to the Amazon interface.

         

        Example: 192.168.1.1/30 or 2001:db8::1/125

        

      
      - **addressFamily** *(string) --* 

        Indicates the address family for the BGP peer.

         

         
        * **ipv4** : IPv4 address family 
         
        * **ipv6** : IPv6 address family 
         

        

      
      - **customerAddress** *(string) --* 

        IP address assigned to the customer interface.

         

        Example: 192.168.1.2/30 or 2001:db8::2/125

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new virtual interface.

          
        

        - **virtualInterfaceId** *(string) --* 

          The ID of the virtual interface.

           

          Example: dxvif-123dfg56

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **virtualInterfaceType** *(string) --* 

          The type of virtual interface.

           

          Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so on.)

          
        

        - **virtualInterfaceName** *(string) --* 

          The name of the virtual interface assigned by the customer.

           

          Example: "My VPC"

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **asn** *(integer) --* 

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

           

          Example: 65000

          
        

        - **amazonSideAsn** *(integer) --* 

          The autonomous system number (ASN) for the Amazon side of the connection.

          
        

        - **authKey** *(string) --* 

          The authentication key for BGP configuration.

           

          Example: asdf34example

          
        

        - **amazonAddress** *(string) --* 

          IP address assigned to the Amazon interface.

           

          Example: 192.168.1.1/30 or 2001:db8::1/125

          
        

        - **customerAddress** *(string) --* 

          IP address assigned to the customer interface.

           

          Example: 192.168.1.2/30 or 2001:db8::2/125

          
        

        - **addressFamily** *(string) --* 

          Indicates the address family for the BGP peer.

           

           
          * **ipv4** : IPv4 address family 
           
          * **ipv6** : IPv6 address family 
           

          
        

        - **virtualInterfaceState** *(string) --* 

          State of the virtual interface.

           

           
          * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
           
          * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
           
          * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
           
          * **Available** : A virtual interface that is able to forward traffic. 
           
          * **Down** : A virtual interface that is BGP down. 
           
          * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
           
          * **Deleted** : A virtual interface that cannot forward traffic. 
           
          * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
           

          
        

        - **customerRouterConfig** *(string) --* 

          Information for generating the customer router configuration.

          
        

        - **virtualGatewayId** *(string) --* 

          The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

           

          Example: vgw-123er56

          
        

        - **directConnectGatewayId** *(string) --* 

          The ID of the direct connect gateway.

           

          Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

          
        

        - **routeFilterPrefixes** *(list) --* 

          A list of routes to be advertised to the AWS network in this region (public virtual interface).

          
          

          - *(dict) --* 

            A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

            
            

            - **cidr** *(string) --* 

              CIDR notation for the advertised route. Multiple routes are separated by commas.

               

              IPv6 CIDRs must be at least a /64 or shorter

               

              Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

              
        
      
        

        - **bgpPeers** *(list) --* 

          A list of the BGP peers configured on this virtual interface.

          
          

          - *(dict) --* 

            A structure containing information about a BGP peer.

            
            

            - **asn** *(integer) --* 

              The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

               

              Example: 65000

              
            

            - **authKey** *(string) --* 

              The authentication key for BGP configuration.

               

              Example: asdf34example

              
            

            - **addressFamily** *(string) --* 

              Indicates the address family for the BGP peer.

               

               
              * **ipv4** : IPv4 address family 
               
              * **ipv6** : IPv6 address family 
               

              
            

            - **amazonAddress** *(string) --* 

              IP address assigned to the Amazon interface.

               

              Example: 192.168.1.1/30 or 2001:db8::1/125

              
            

            - **customerAddress** *(string) --* 

              IP address assigned to the customer interface.

               

              Example: 192.168.1.2/30 or 2001:db8::2/125

              
            

            - **bgpPeerState** *(string) --* 

              The state of the BGP peer.

               

               
              * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.  
               
              * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established. 
               
              * **Available** : The BGP peer can be established. 
               
              * **Deleting** : The BGP peer is in the process of being deleted. 
               
              * **Deleted** : The BGP peer has been deleted and cannot be established. 
               

              
            

            - **bgpStatus** *(string) --* 

              The Up/Down state of the BGP peer.

               

               
              * **Up** : The BGP peer is established. 
               
              * **Down** : The BGP peer is down. 
               

              
        
      
    

  .. py:method:: allocate_public_virtual_interface(**kwargs)

    

    Provisions a public virtual interface to be owned by a different customer.

     

    The owner of a connection calls this function to provision a public virtual interface which will be owned by another AWS customer.

     

    Virtual interfaces created using this function must be confirmed by the virtual interface owner by calling ConfirmPublicVirtualInterface. Until this step has been completed, the virtual interface will be in 'Confirming' state, and will not be available for handling traffic.

     

    When creating an IPv6 public virtual interface (addressFamily is 'ipv6'), the customer and amazon address fields should be left blank to use auto-assigned IPv6 space. Custom IPv6 Addresses are currently not supported.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AllocatePublicVirtualInterface>`_    


    **Request Syntax** 
    ::

      response = client.allocate_public_virtual_interface(
          connectionId='string',
          ownerAccount='string',
          newPublicVirtualInterfaceAllocation={
              'virtualInterfaceName': 'string',
              'vlan': 123,
              'asn': 123,
              'authKey': 'string',
              'amazonAddress': 'string',
              'customerAddress': 'string',
              'addressFamily': 'ipv4'|'ipv6',
              'routeFilterPrefixes': [
                  {
                      'cidr': 'string'
                  },
              ]
          }
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The connection ID on which the public virtual interface is provisioned.

       

      Default: None

      

    
    :type ownerAccount: string
    :param ownerAccount: **[REQUIRED]** 

      The AWS account that will own the new public virtual interface.

       

      Default: None

      

    
    :type newPublicVirtualInterfaceAllocation: dict
    :param newPublicVirtualInterfaceAllocation: **[REQUIRED]** 

      Detailed information for the public virtual interface to be provisioned.

       

      Default: None

      

    
      - **virtualInterfaceName** *(string) --* **[REQUIRED]** 

        The name of the virtual interface assigned by the customer.

         

        Example: "My VPC"

        

      
      - **vlan** *(integer) --* **[REQUIRED]** 

        The VLAN ID.

         

        Example: 101

        

      
      - **asn** *(integer) --* **[REQUIRED]** 

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

         

        Example: 65000

        

      
      - **authKey** *(string) --* 

        The authentication key for BGP configuration.

         

        Example: asdf34example

        

      
      - **amazonAddress** *(string) --* 

        IP address assigned to the Amazon interface.

         

        Example: 192.168.1.1/30 or 2001:db8::1/125

        

      
      - **customerAddress** *(string) --* 

        IP address assigned to the customer interface.

         

        Example: 192.168.1.2/30 or 2001:db8::2/125

        

      
      - **addressFamily** *(string) --* 

        Indicates the address family for the BGP peer.

         

         
        * **ipv4** : IPv4 address family 
         
        * **ipv6** : IPv6 address family 
         

        

      
      - **routeFilterPrefixes** *(list) --* 

        A list of routes to be advertised to the AWS network in this region (public virtual interface).

        

      
        - *(dict) --* 

          A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

          

        
          - **cidr** *(string) --* 

            CIDR notation for the advertised route. Multiple routes are separated by commas.

             

            IPv6 CIDRs must be at least a /64 or shorter

             

            Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

            

          
        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new virtual interface.

          
        

        - **virtualInterfaceId** *(string) --* 

          The ID of the virtual interface.

           

          Example: dxvif-123dfg56

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **virtualInterfaceType** *(string) --* 

          The type of virtual interface.

           

          Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so on.)

          
        

        - **virtualInterfaceName** *(string) --* 

          The name of the virtual interface assigned by the customer.

           

          Example: "My VPC"

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **asn** *(integer) --* 

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

           

          Example: 65000

          
        

        - **amazonSideAsn** *(integer) --* 

          The autonomous system number (ASN) for the Amazon side of the connection.

          
        

        - **authKey** *(string) --* 

          The authentication key for BGP configuration.

           

          Example: asdf34example

          
        

        - **amazonAddress** *(string) --* 

          IP address assigned to the Amazon interface.

           

          Example: 192.168.1.1/30 or 2001:db8::1/125

          
        

        - **customerAddress** *(string) --* 

          IP address assigned to the customer interface.

           

          Example: 192.168.1.2/30 or 2001:db8::2/125

          
        

        - **addressFamily** *(string) --* 

          Indicates the address family for the BGP peer.

           

           
          * **ipv4** : IPv4 address family 
           
          * **ipv6** : IPv6 address family 
           

          
        

        - **virtualInterfaceState** *(string) --* 

          State of the virtual interface.

           

           
          * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
           
          * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
           
          * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
           
          * **Available** : A virtual interface that is able to forward traffic. 
           
          * **Down** : A virtual interface that is BGP down. 
           
          * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
           
          * **Deleted** : A virtual interface that cannot forward traffic. 
           
          * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
           

          
        

        - **customerRouterConfig** *(string) --* 

          Information for generating the customer router configuration.

          
        

        - **virtualGatewayId** *(string) --* 

          The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

           

          Example: vgw-123er56

          
        

        - **directConnectGatewayId** *(string) --* 

          The ID of the direct connect gateway.

           

          Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

          
        

        - **routeFilterPrefixes** *(list) --* 

          A list of routes to be advertised to the AWS network in this region (public virtual interface).

          
          

          - *(dict) --* 

            A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

            
            

            - **cidr** *(string) --* 

              CIDR notation for the advertised route. Multiple routes are separated by commas.

               

              IPv6 CIDRs must be at least a /64 or shorter

               

              Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

              
        
      
        

        - **bgpPeers** *(list) --* 

          A list of the BGP peers configured on this virtual interface.

          
          

          - *(dict) --* 

            A structure containing information about a BGP peer.

            
            

            - **asn** *(integer) --* 

              The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

               

              Example: 65000

              
            

            - **authKey** *(string) --* 

              The authentication key for BGP configuration.

               

              Example: asdf34example

              
            

            - **addressFamily** *(string) --* 

              Indicates the address family for the BGP peer.

               

               
              * **ipv4** : IPv4 address family 
               
              * **ipv6** : IPv6 address family 
               

              
            

            - **amazonAddress** *(string) --* 

              IP address assigned to the Amazon interface.

               

              Example: 192.168.1.1/30 or 2001:db8::1/125

              
            

            - **customerAddress** *(string) --* 

              IP address assigned to the customer interface.

               

              Example: 192.168.1.2/30 or 2001:db8::2/125

              
            

            - **bgpPeerState** *(string) --* 

              The state of the BGP peer.

               

               
              * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.  
               
              * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established. 
               
              * **Available** : The BGP peer can be established. 
               
              * **Deleting** : The BGP peer is in the process of being deleted. 
               
              * **Deleted** : The BGP peer has been deleted and cannot be established. 
               

              
            

            - **bgpStatus** *(string) --* 

              The Up/Down state of the BGP peer.

               

               
              * **Up** : The BGP peer is established. 
               
              * **Down** : The BGP peer is down. 
               

              
        
      
    

  .. py:method:: associate_connection_with_lag(**kwargs)

    

    Associates an existing connection with a link aggregation group (LAG). The connection is interrupted and re-established as a member of the LAG (connectivity to AWS will be interrupted). The connection must be hosted on the same AWS Direct Connect endpoint as the LAG, and its bandwidth must match the bandwidth for the LAG. You can reassociate a connection that's currently associated with a different LAG; however, if removing the connection will cause the original LAG to fall below its setting for minimum number of operational connections, the request fails.

     

    Any virtual interfaces that are directly associated with the connection are automatically re-associated with the LAG. If the connection was originally associated with a different LAG, the virtual interfaces remain associated with the original LAG.

     

    For interconnects, any hosted connections are automatically re-associated with the LAG. If the interconnect was originally associated with a different LAG, the hosted connections remain associated with the original LAG.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AssociateConnectionWithLag>`_    


    **Request Syntax** 
    ::

      response = client.associate_connection_with_lag(
          connectionId='string',
          lagId='string'
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the connection.

       

      Example: dxcon-abc123

       

      Default: None

      

    
    :type lagId: string
    :param lagId: **[REQUIRED]** 

      The ID of the LAG with which to associate the connection.

       

      Example: dxlag-abc123

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A connection represents the physical network connection between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new connection.

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **connectionName** *(string) --* 

          The name of the connection.

           

          Example: "*My Connection to AWS* "

           

          Default: None

          
        

        - **connectionState** *(string) --* 

          State of the connection.

           

           
          * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
           
          * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The connection has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the connection is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The connection is in the process of being deleted. 
           
          * **Deleted** : The connection has been deleted. 
           
          * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
           

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **bandwidth** *(string) --* 

          Bandwidth of the connection.

           

          Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

           

          Default: None

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **partnerName** *(string) --* 

          The name of the AWS Direct Connect service provider associated with the connection.

          
        

        - **loaIssueTime** *(datetime) --* 

          The time of the most recent call to  DescribeLoa for this connection.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **awsDevice** *(string) --* 

          The Direct Connection endpoint which the physical connection terminates on.

          
    

  .. py:method:: associate_hosted_connection(**kwargs)

    

    Associates a hosted connection and its virtual interfaces with a link aggregation group (LAG) or interconnect. If the target interconnect or LAG has an existing hosted connection with a conflicting VLAN number or IP address, the operation fails. This action temporarily interrupts the hosted connection's connectivity to AWS as it is being migrated.

     

    .. note::

       

      This is intended for use by AWS Direct Connect partners only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AssociateHostedConnection>`_    


    **Request Syntax** 
    ::

      response = client.associate_hosted_connection(
          connectionId='string',
          parentConnectionId='string'
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the hosted connection.

       

      Example: dxcon-abc123

       

      Default: None

      

    
    :type parentConnectionId: string
    :param parentConnectionId: **[REQUIRED]** 

      The ID of the interconnect or the LAG.

       

      Example: dxcon-abc123 or dxlag-abc123

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A connection represents the physical network connection between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new connection.

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **connectionName** *(string) --* 

          The name of the connection.

           

          Example: "*My Connection to AWS* "

           

          Default: None

          
        

        - **connectionState** *(string) --* 

          State of the connection.

           

           
          * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
           
          * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The connection has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the connection is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The connection is in the process of being deleted. 
           
          * **Deleted** : The connection has been deleted. 
           
          * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
           

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **bandwidth** *(string) --* 

          Bandwidth of the connection.

           

          Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

           

          Default: None

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **partnerName** *(string) --* 

          The name of the AWS Direct Connect service provider associated with the connection.

          
        

        - **loaIssueTime** *(datetime) --* 

          The time of the most recent call to  DescribeLoa for this connection.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **awsDevice** *(string) --* 

          The Direct Connection endpoint which the physical connection terminates on.

          
    

  .. py:method:: associate_virtual_interface(**kwargs)

    

    Associates a virtual interface with a specified link aggregation group (LAG) or connection. Connectivity to AWS is temporarily interrupted as the virtual interface is being migrated. If the target connection or LAG has an associated virtual interface with a conflicting VLAN number or a conflicting IP address, the operation fails. 

     

    Virtual interfaces associated with a hosted connection cannot be associated with a LAG; hosted connections must be migrated along with their virtual interfaces using  AssociateHostedConnection .

     

    In order to reassociate a virtual interface to a new connection or LAG, the requester must own either the virtual interface itself or the connection to which the virtual interface is currently associated. Additionally, the requester must own the connection or LAG to which the virtual interface will be newly associated.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AssociateVirtualInterface>`_    


    **Request Syntax** 
    ::

      response = client.associate_virtual_interface(
          virtualInterfaceId='string',
          connectionId='string'
      )
    :type virtualInterfaceId: string
    :param virtualInterfaceId: **[REQUIRED]** 

      The ID of the virtual interface.

       

      Example: dxvif-123dfg56

       

      Default: None

      

    
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the LAG or connection with which to associate the virtual interface.

       

      Example: dxlag-abc123 or dxcon-abc123

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new virtual interface.

          
        

        - **virtualInterfaceId** *(string) --* 

          The ID of the virtual interface.

           

          Example: dxvif-123dfg56

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **virtualInterfaceType** *(string) --* 

          The type of virtual interface.

           

          Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so on.)

          
        

        - **virtualInterfaceName** *(string) --* 

          The name of the virtual interface assigned by the customer.

           

          Example: "My VPC"

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **asn** *(integer) --* 

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

           

          Example: 65000

          
        

        - **amazonSideAsn** *(integer) --* 

          The autonomous system number (ASN) for the Amazon side of the connection.

          
        

        - **authKey** *(string) --* 

          The authentication key for BGP configuration.

           

          Example: asdf34example

          
        

        - **amazonAddress** *(string) --* 

          IP address assigned to the Amazon interface.

           

          Example: 192.168.1.1/30 or 2001:db8::1/125

          
        

        - **customerAddress** *(string) --* 

          IP address assigned to the customer interface.

           

          Example: 192.168.1.2/30 or 2001:db8::2/125

          
        

        - **addressFamily** *(string) --* 

          Indicates the address family for the BGP peer.

           

           
          * **ipv4** : IPv4 address family 
           
          * **ipv6** : IPv6 address family 
           

          
        

        - **virtualInterfaceState** *(string) --* 

          State of the virtual interface.

           

           
          * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
           
          * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
           
          * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
           
          * **Available** : A virtual interface that is able to forward traffic. 
           
          * **Down** : A virtual interface that is BGP down. 
           
          * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
           
          * **Deleted** : A virtual interface that cannot forward traffic. 
           
          * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
           

          
        

        - **customerRouterConfig** *(string) --* 

          Information for generating the customer router configuration.

          
        

        - **virtualGatewayId** *(string) --* 

          The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

           

          Example: vgw-123er56

          
        

        - **directConnectGatewayId** *(string) --* 

          The ID of the direct connect gateway.

           

          Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

          
        

        - **routeFilterPrefixes** *(list) --* 

          A list of routes to be advertised to the AWS network in this region (public virtual interface).

          
          

          - *(dict) --* 

            A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

            
            

            - **cidr** *(string) --* 

              CIDR notation for the advertised route. Multiple routes are separated by commas.

               

              IPv6 CIDRs must be at least a /64 or shorter

               

              Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

              
        
      
        

        - **bgpPeers** *(list) --* 

          A list of the BGP peers configured on this virtual interface.

          
          

          - *(dict) --* 

            A structure containing information about a BGP peer.

            
            

            - **asn** *(integer) --* 

              The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

               

              Example: 65000

              
            

            - **authKey** *(string) --* 

              The authentication key for BGP configuration.

               

              Example: asdf34example

              
            

            - **addressFamily** *(string) --* 

              Indicates the address family for the BGP peer.

               

               
              * **ipv4** : IPv4 address family 
               
              * **ipv6** : IPv6 address family 
               

              
            

            - **amazonAddress** *(string) --* 

              IP address assigned to the Amazon interface.

               

              Example: 192.168.1.1/30 or 2001:db8::1/125

              
            

            - **customerAddress** *(string) --* 

              IP address assigned to the customer interface.

               

              Example: 192.168.1.2/30 or 2001:db8::2/125

              
            

            - **bgpPeerState** *(string) --* 

              The state of the BGP peer.

               

               
              * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.  
               
              * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established. 
               
              * **Available** : The BGP peer can be established. 
               
              * **Deleting** : The BGP peer is in the process of being deleted. 
               
              * **Deleted** : The BGP peer has been deleted and cannot be established. 
               

              
            

            - **bgpStatus** *(string) --* 

              The Up/Down state of the BGP peer.

               

               
              * **Up** : The BGP peer is established. 
               
              * **Down** : The BGP peer is down. 
               

              
        
      
    

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


  .. py:method:: confirm_connection(**kwargs)

    

    Confirm the creation of a hosted connection on an interconnect.

     

    Upon creation, the hosted connection is initially in the 'Ordering' state, and will remain in this state until the owner calls ConfirmConnection to confirm creation of the hosted connection.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/ConfirmConnection>`_    


    **Request Syntax** 
    ::

      response = client.confirm_connection(
          connectionId='string'
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

       

      Example: dxcon-fg5678gh

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when ConfirmConnection is called.

        
        

        - **connectionState** *(string) --* 

          State of the connection.

           

           
          * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
           
          * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The connection has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the connection is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The connection is in the process of being deleted. 
           
          * **Deleted** : The connection has been deleted. 
           
          * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
           

          
    

  .. py:method:: confirm_private_virtual_interface(**kwargs)

    

    Accept ownership of a private virtual interface created by another customer.

     

    After the virtual interface owner calls this function, the virtual interface will be created and attached to the given virtual private gateway or direct connect gateway, and will be available for handling traffic.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/ConfirmPrivateVirtualInterface>`_    


    **Request Syntax** 
    ::

      response = client.confirm_private_virtual_interface(
          virtualInterfaceId='string',
          virtualGatewayId='string',
          directConnectGatewayId='string'
      )
    :type virtualInterfaceId: string
    :param virtualInterfaceId: **[REQUIRED]** 

      The ID of the virtual interface.

       

      Example: dxvif-123dfg56

       

      Default: None

      

    
    :type virtualGatewayId: string
    :param virtualGatewayId: 

      ID of the virtual private gateway that will be attached to the virtual interface.

       

      A virtual private gateway can be managed via the Amazon Virtual Private Cloud (VPC) console or the `EC2 CreateVpnGateway <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-CreateVpnGateway.html>`__ action.

       

      Default: None

      

    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: 

      ID of the direct connect gateway that will be attached to the virtual interface.

       

      A direct connect gateway can be managed via the AWS Direct Connect console or the  CreateDirectConnectGateway action.

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when ConfirmPrivateVirtualInterface is called.

        
        

        - **virtualInterfaceState** *(string) --* 

          State of the virtual interface.

           

           
          * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
           
          * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
           
          * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
           
          * **Available** : A virtual interface that is able to forward traffic. 
           
          * **Down** : A virtual interface that is BGP down. 
           
          * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
           
          * **Deleted** : A virtual interface that cannot forward traffic. 
           
          * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
           

          
    

  .. py:method:: confirm_public_virtual_interface(**kwargs)

    

    Accept ownership of a public virtual interface created by another customer.

     

    After the virtual interface owner calls this function, the specified virtual interface will be created and made available for handling traffic.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/ConfirmPublicVirtualInterface>`_    


    **Request Syntax** 
    ::

      response = client.confirm_public_virtual_interface(
          virtualInterfaceId='string'
      )
    :type virtualInterfaceId: string
    :param virtualInterfaceId: **[REQUIRED]** 

      The ID of the virtual interface.

       

      Example: dxvif-123dfg56

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when ConfirmPublicVirtualInterface is called.

        
        

        - **virtualInterfaceState** *(string) --* 

          State of the virtual interface.

           

           
          * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
           
          * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
           
          * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
           
          * **Available** : A virtual interface that is able to forward traffic. 
           
          * **Down** : A virtual interface that is BGP down. 
           
          * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
           
          * **Deleted** : A virtual interface that cannot forward traffic. 
           
          * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
           

          
    

  .. py:method:: create_bgp_peer(**kwargs)

    

    Creates a new BGP peer on a specified virtual interface. The BGP peer cannot be in the same address family (IPv4/IPv6) of an existing BGP peer on the virtual interface.

     

    You must create a BGP peer for the corresponding address family in order to access AWS resources that also use that address family.

     

    When creating a IPv6 BGP peer, the Amazon address and customer address fields must be left blank. IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses; you cannot specify custom IPv6 addresses.

     

    For a public virtual interface, the Autonomous System Number (ASN) must be private or already whitelisted for the virtual interface.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreateBGPPeer>`_    


    **Request Syntax** 
    ::

      response = client.create_bgp_peer(
          virtualInterfaceId='string',
          newBGPPeer={
              'asn': 123,
              'authKey': 'string',
              'addressFamily': 'ipv4'|'ipv6',
              'amazonAddress': 'string',
              'customerAddress': 'string'
          }
      )
    :type virtualInterfaceId: string
    :param virtualInterfaceId: 

      The ID of the virtual interface on which the BGP peer will be provisioned.

       

      Example: dxvif-456abc78

       

      Default: None

      

    
    :type newBGPPeer: dict
    :param newBGPPeer: 

      Detailed information for the BGP peer to be created.

       

      Default: None

      

    
      - **asn** *(integer) --* 

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

         

        Example: 65000

        

      
      - **authKey** *(string) --* 

        The authentication key for BGP configuration.

         

        Example: asdf34example

        

      
      - **addressFamily** *(string) --* 

        Indicates the address family for the BGP peer.

         

         
        * **ipv4** : IPv4 address family 
         
        * **ipv6** : IPv6 address family 
         

        

      
      - **amazonAddress** *(string) --* 

        IP address assigned to the Amazon interface.

         

        Example: 192.168.1.1/30 or 2001:db8::1/125

        

      
      - **customerAddress** *(string) --* 

        IP address assigned to the customer interface.

         

        Example: 192.168.1.2/30 or 2001:db8::2/125

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'virtualInterface': {
                'ownerAccount': 'string',
                'virtualInterfaceId': 'string',
                'location': 'string',
                'connectionId': 'string',
                'virtualInterfaceType': 'string',
                'virtualInterfaceName': 'string',
                'vlan': 123,
                'asn': 123,
                'amazonSideAsn': 123,
                'authKey': 'string',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'customerRouterConfig': 'string',
                'virtualGatewayId': 'string',
                'directConnectGatewayId': 'string',
                'routeFilterPrefixes': [
                    {
                        'cidr': 'string'
                    },
                ],
                'bgpPeers': [
                    {
                        'asn': 123,
                        'authKey': 'string',
                        'addressFamily': 'ipv4'|'ipv6',
                        'amazonAddress': 'string',
                        'customerAddress': 'string',
                        'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                        'bgpStatus': 'up'|'down'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when CreateBGPPeer is called.

        
        

        - **virtualInterface** *(dict) --* 

          A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

          
          

          - **ownerAccount** *(string) --* 

            The AWS account that will own the new virtual interface.

            
          

          - **virtualInterfaceId** *(string) --* 

            The ID of the virtual interface.

             

            Example: dxvif-123dfg56

             

            Default: None

            
          

          - **location** *(string) --* 

            Where the connection is located.

             

            Example: EqSV5

             

            Default: None

            
          

          - **connectionId** *(string) --* 

            The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

             

            Example: dxcon-fg5678gh

             

            Default: None

            
          

          - **virtualInterfaceType** *(string) --* 

            The type of virtual interface.

             

            Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so on.)

            
          

          - **virtualInterfaceName** *(string) --* 

            The name of the virtual interface assigned by the customer.

             

            Example: "My VPC"

            
          

          - **vlan** *(integer) --* 

            The VLAN ID.

             

            Example: 101

            
          

          - **asn** *(integer) --* 

            The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

             

            Example: 65000

            
          

          - **amazonSideAsn** *(integer) --* 

            The autonomous system number (ASN) for the Amazon side of the connection.

            
          

          - **authKey** *(string) --* 

            The authentication key for BGP configuration.

             

            Example: asdf34example

            
          

          - **amazonAddress** *(string) --* 

            IP address assigned to the Amazon interface.

             

            Example: 192.168.1.1/30 or 2001:db8::1/125

            
          

          - **customerAddress** *(string) --* 

            IP address assigned to the customer interface.

             

            Example: 192.168.1.2/30 or 2001:db8::2/125

            
          

          - **addressFamily** *(string) --* 

            Indicates the address family for the BGP peer.

             

             
            * **ipv4** : IPv4 address family 
             
            * **ipv6** : IPv6 address family 
             

            
          

          - **virtualInterfaceState** *(string) --* 

            State of the virtual interface.

             

             
            * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
             
            * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
             
            * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
             
            * **Available** : A virtual interface that is able to forward traffic. 
             
            * **Down** : A virtual interface that is BGP down. 
             
            * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
             
            * **Deleted** : A virtual interface that cannot forward traffic. 
             
            * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
             

            
          

          - **customerRouterConfig** *(string) --* 

            Information for generating the customer router configuration.

            
          

          - **virtualGatewayId** *(string) --* 

            The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

             

            Example: vgw-123er56

            
          

          - **directConnectGatewayId** *(string) --* 

            The ID of the direct connect gateway.

             

            Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

            
          

          - **routeFilterPrefixes** *(list) --* 

            A list of routes to be advertised to the AWS network in this region (public virtual interface).

            
            

            - *(dict) --* 

              A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

              
              

              - **cidr** *(string) --* 

                CIDR notation for the advertised route. Multiple routes are separated by commas.

                 

                IPv6 CIDRs must be at least a /64 or shorter

                 

                Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

                
          
        
          

          - **bgpPeers** *(list) --* 

            A list of the BGP peers configured on this virtual interface.

            
            

            - *(dict) --* 

              A structure containing information about a BGP peer.

              
              

              - **asn** *(integer) --* 

                The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

                 

                Example: 65000

                
              

              - **authKey** *(string) --* 

                The authentication key for BGP configuration.

                 

                Example: asdf34example

                
              

              - **addressFamily** *(string) --* 

                Indicates the address family for the BGP peer.

                 

                 
                * **ipv4** : IPv4 address family 
                 
                * **ipv6** : IPv6 address family 
                 

                
              

              - **amazonAddress** *(string) --* 

                IP address assigned to the Amazon interface.

                 

                Example: 192.168.1.1/30 or 2001:db8::1/125

                
              

              - **customerAddress** *(string) --* 

                IP address assigned to the customer interface.

                 

                Example: 192.168.1.2/30 or 2001:db8::2/125

                
              

              - **bgpPeerState** *(string) --* 

                The state of the BGP peer.

                 

                 
                * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.  
                 
                * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established. 
                 
                * **Available** : The BGP peer can be established. 
                 
                * **Deleting** : The BGP peer is in the process of being deleted. 
                 
                * **Deleted** : The BGP peer has been deleted and cannot be established. 
                 

                
              

              - **bgpStatus** *(string) --* 

                The Up/Down state of the BGP peer.

                 

                 
                * **Up** : The BGP peer is established. 
                 
                * **Down** : The BGP peer is down. 
                 

                
          
        
      
    

  .. py:method:: create_connection(**kwargs)

    

    Creates a new connection between the customer network and a specific AWS Direct Connect location.

     

    A connection links your internal network to an AWS Direct Connect location over a standard 1 gigabit or 10 gigabit Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. An AWS Direct Connect location provides access to Amazon Web Services in the region it is associated with. You can establish connections with AWS Direct Connect locations in multiple regions, but a connection in one region does not provide connectivity to other regions.

     

    To find the locations for your region, use  DescribeLocations .

     

    You can automatically add the new connection to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new connection is allocated on the same AWS Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no connection will be created.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreateConnection>`_    


    **Request Syntax** 
    ::

      response = client.create_connection(
          location='string',
          bandwidth='string',
          connectionName='string',
          lagId='string'
      )
    :type location: string
    :param location: **[REQUIRED]** 

      Where the connection is located.

       

      Example: EqSV5

       

      Default: None

      

    
    :type bandwidth: string
    :param bandwidth: **[REQUIRED]** 

      Bandwidth of the connection.

       

      Example: 1Gbps

       

      Default: None

      

    
    :type connectionName: string
    :param connectionName: **[REQUIRED]** 

      The name of the connection.

       

      Example: "*My Connection to AWS* "

       

      Default: None

      

    
    :type lagId: string
    :param lagId: 

      The ID of the LAG.

       

      Example: dxlag-fg5678gh

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A connection represents the physical network connection between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new connection.

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **connectionName** *(string) --* 

          The name of the connection.

           

          Example: "*My Connection to AWS* "

           

          Default: None

          
        

        - **connectionState** *(string) --* 

          State of the connection.

           

           
          * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
           
          * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The connection has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the connection is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The connection is in the process of being deleted. 
           
          * **Deleted** : The connection has been deleted. 
           
          * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
           

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **bandwidth** *(string) --* 

          Bandwidth of the connection.

           

          Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

           

          Default: None

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **partnerName** *(string) --* 

          The name of the AWS Direct Connect service provider associated with the connection.

          
        

        - **loaIssueTime** *(datetime) --* 

          The time of the most recent call to  DescribeLoa for this connection.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **awsDevice** *(string) --* 

          The Direct Connection endpoint which the physical connection terminates on.

          
    

  .. py:method:: create_direct_connect_gateway(**kwargs)

    

    Creates a new direct connect gateway. A direct connect gateway is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways. direct connect gateways are global and visible in any AWS region after they are created. The virtual interfaces and virtual private gateways that are connected through a direct connect gateway can be in different regions. This enables you to connect to a VPC in any region, regardless of the region in which the virtual interfaces are located, and pass traffic between them.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreateDirectConnectGateway>`_    


    **Request Syntax** 
    ::

      response = client.create_direct_connect_gateway(
          directConnectGatewayName='string',
          amazonSideAsn=123
      )
    :type directConnectGatewayName: string
    :param directConnectGatewayName: **[REQUIRED]** 

      The name of the direct connect gateway.

       

      Example: "My direct connect gateway"

       

      Default: None

      

    
    :type amazonSideAsn: integer
    :param amazonSideAsn: 

      The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294 

       

      Example: 65200

       

      Default: 64512

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'directConnectGateway': {
                'directConnectGatewayId': 'string',
                'directConnectGatewayName': 'string',
                'amazonSideAsn': 123,
                'ownerAccount': 'string',
                'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
                'stateChangeError': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the response from the CreateDirectConnectGateway API call

        
        

        - **directConnectGateway** *(dict) --* 

          The direct connect gateway to be created.

          
          

          - **directConnectGatewayId** *(string) --* 

            The ID of the direct connect gateway.

             

            Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

            
          

          - **directConnectGatewayName** *(string) --* 

            The name of the direct connect gateway.

             

            Example: "My direct connect gateway"

             

            Default: None

            
          

          - **amazonSideAsn** *(integer) --* 

            The autonomous system number (ASN) for the Amazon side of the connection.

            
          

          - **ownerAccount** *(string) --* 

            The AWS account ID of the owner of the direct connect gateway.

            
          

          - **directConnectGatewayState** *(string) --* 

            State of the direct connect gateway.

             

             
            * **Pending** : The initial state after calling  CreateDirectConnectGateway . 
             
            * **Available** : The direct connect gateway is ready for use. 
             
            * **Deleting** : The initial state after calling  DeleteDirectConnectGateway . 
             
            * **Deleted** : The direct connect gateway is deleted and cannot pass traffic. 
             

            
          

          - **stateChangeError** *(string) --* 

            Error message when the state of an object fails to advance.

            
      
    

  .. py:method:: create_direct_connect_gateway_association(**kwargs)

    

    Creates an association between a direct connect gateway and a virtual private gateway (VGW). The VGW must be attached to a VPC and must not be associated with another direct connect gateway.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation>`_    


    **Request Syntax** 
    ::

      response = client.create_direct_connect_gateway_association(
          directConnectGatewayId='string',
          virtualGatewayId='string'
      )
    :type directConnectGatewayId: string
    :param directConnectGatewayId: **[REQUIRED]** 

      The ID of the direct connect gateway.

       

      Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

       

      Default: None

      

    
    :type virtualGatewayId: string
    :param virtualGatewayId: **[REQUIRED]** 

      The ID of the virtual private gateway.

       

      Example: "vgw-abc123ef"

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'directConnectGatewayAssociation': {
                'directConnectGatewayId': 'string',
                'virtualGatewayId': 'string',
                'virtualGatewayRegion': 'string',
                'virtualGatewayOwnerAccount': 'string',
                'associationState': 'associating'|'associated'|'disassociating'|'disassociated',
                'stateChangeError': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the response from the CreateDirectConnectGatewayAssociation API call

        
        

        - **directConnectGatewayAssociation** *(dict) --* 

          The direct connect gateway association to be created.

          
          

          - **directConnectGatewayId** *(string) --* 

            The ID of the direct connect gateway.

             

            Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

            
          

          - **virtualGatewayId** *(string) --* 

            The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

             

            Example: vgw-123er56

            
          

          - **virtualGatewayRegion** *(string) --* 

            The region in which the virtual private gateway is located.

             

            Example: us-east-1

            
          

          - **virtualGatewayOwnerAccount** *(string) --* 

            The AWS account ID of the owner of the virtual private gateway.

            
          

          - **associationState** *(string) --* 

            State of the direct connect gateway association.

             

             
            * **Associating** : The initial state after calling  CreateDirectConnectGatewayAssociation . 
             
            * **Associated** : The direct connect gateway and virtual private gateway are successfully associated and ready to pass traffic. 
             
            * **Disassociating** : The initial state after calling  DeleteDirectConnectGatewayAssociation . 
             
            * **Disassociated** : The virtual private gateway is successfully disassociated from the direct connect gateway. Traffic flow between the direct connect gateway and virtual private gateway stops. 
             

            
          

          - **stateChangeError** *(string) --* 

            Error message when the state of an object fails to advance.

            
      
    

  .. py:method:: create_interconnect(**kwargs)

    

    Creates a new interconnect between a AWS Direct Connect partner's network and a specific AWS Direct Connect location.

     

    An interconnect is a connection which is capable of hosting other connections. The AWS Direct Connect partner can use an interconnect to provide sub-1Gbps AWS Direct Connect service to tier 2 customers who do not have their own connections. Like a standard connection, an interconnect links the AWS Direct Connect partner's network to an AWS Direct Connect location over a standard 1 Gbps or 10 Gbps Ethernet fiber-optic cable. One end is connected to the partner's router, the other to an AWS Direct Connect router.

     

    You can automatically add the new interconnect to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new interconnect is allocated on the same AWS Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no interconnect will be created.

     

    For each end customer, the AWS Direct Connect partner provisions a connection on their interconnect by calling AllocateConnectionOnInterconnect. The end customer can then connect to AWS resources by creating a virtual interface on their connection, using the VLAN assigned to them by the AWS Direct Connect partner.

     

    .. note::

       

      This is intended for use by AWS Direct Connect partners only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreateInterconnect>`_    


    **Request Syntax** 
    ::

      response = client.create_interconnect(
          interconnectName='string',
          bandwidth='string',
          location='string',
          lagId='string'
      )
    :type interconnectName: string
    :param interconnectName: **[REQUIRED]** 

      The name of the interconnect.

       

      Example: "*1G Interconnect to AWS* "

       

      Default: None

      

    
    :type bandwidth: string
    :param bandwidth: **[REQUIRED]** 

      The port bandwidth

       

      Example: 1Gbps

       

      Default: None

       

      Available values: 1Gbps,10Gbps

      

    
    :type location: string
    :param location: **[REQUIRED]** 

      Where the interconnect is located

       

      Example: EqSV5

       

      Default: None

      

    
    :type lagId: string
    :param lagId: 

      The ID of the LAG.

       

      Example: dxlag-fg5678gh

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'interconnectId': 'string',
            'interconnectName': 'string',
            'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        An interconnect is a connection that can host other connections.

         

        Like a standard AWS Direct Connect connection, an interconnect represents the physical connection between an AWS Direct Connect partner's network and a specific Direct Connect location. An AWS Direct Connect partner who owns an interconnect can provision hosted connections on the interconnect for their end customers, thereby providing the end customers with connectivity to AWS services.

         

        The resources of the interconnect, including bandwidth and VLAN numbers, are shared by all of the hosted connections on the interconnect, and the owner of the interconnect determines how these resources are assigned.

        
        

        - **interconnectId** *(string) --* 

          The ID of the interconnect.

           

          Example: dxcon-abc123

          
        

        - **interconnectName** *(string) --* 

          The name of the interconnect.

           

          Example: "*1G Interconnect to AWS* "

          
        

        - **interconnectState** *(string) --* 

          State of the interconnect.

           

           
          * **Requested** : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The interconnect has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the interconnect is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The interconnect is in the process of being deleted. 
           
          * **Deleted** : The interconnect has been deleted. 
           

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **bandwidth** *(string) --* 

          Bandwidth of the connection.

           

          Example: 1Gbps

           

          Default: None

          
        

        - **loaIssueTime** *(datetime) --* 

          The time of the most recent call to DescribeInterconnectLoa for this Interconnect.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **awsDevice** *(string) --* 

          The Direct Connection endpoint which the physical connection terminates on.

          
    

  .. py:method:: create_lag(**kwargs)

    

    Creates a new link aggregation group (LAG) with the specified number of bundled physical connections between the customer network and a specific AWS Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple 1 gigabit or 10 gigabit interfaces, allowing you to treat them as a single interface.

     

    All connections in a LAG must use the same bandwidth (for example, 10 Gbps), and must terminate at the same AWS Direct Connect endpoint.

     

    You can have up to 10 connections per LAG. Regardless of this limit, if you request more connections for the LAG than AWS Direct Connect can allocate on a single endpoint, no LAG is created.

     

    You can specify an existing physical connection or interconnect to include in the LAG (which counts towards the total number of connections). Doing so interrupts the current physical connection or hosted connections, and re-establishes them as a member of the LAG. The LAG will be created on the same AWS Direct Connect endpoint to which the connection terminates. Any virtual interfaces associated with the connection are automatically disassociated and re-associated with the LAG. The connection ID does not change.

     

    If the AWS account used to create a LAG is a registered AWS Direct Connect partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreateLag>`_    


    **Request Syntax** 
    ::

      response = client.create_lag(
          numberOfConnections=123,
          location='string',
          connectionsBandwidth='string',
          lagName='string',
          connectionId='string'
      )
    :type numberOfConnections: integer
    :param numberOfConnections: **[REQUIRED]** 

      The number of physical connections initially provisioned and bundled by the LAG.

       

      Default: None

      

    
    :type location: string
    :param location: **[REQUIRED]** 

      The AWS Direct Connect location in which the LAG should be allocated.

       

      Example: EqSV5

       

      Default: None

      

    
    :type connectionsBandwidth: string
    :param connectionsBandwidth: **[REQUIRED]** 

      The bandwidth of the individual physical connections bundled by the LAG.

       

      Default: None

       

      Available values: 1Gbps, 10Gbps

      

    
    :type lagName: string
    :param lagName: **[REQUIRED]** 

      The name of the LAG.

       

      Example: "``3x10G LAG to AWS`` "

       

      Default: None

      

    
    :type connectionId: string
    :param connectionId: 

      The ID of an existing connection to migrate to the LAG.

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'connectionsBandwidth': 'string',
            'numberOfConnections': 123,
            'lagId': 'string',
            'ownerAccount': 'string',
            'lagName': 'string',
            'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
            'location': 'string',
            'region': 'string',
            'minimumLinks': 123,
            'awsDevice': 'string',
            'connections': [
                {
                    'ownerAccount': 'string',
                    'connectionId': 'string',
                    'connectionName': 'string',
                    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                    'region': 'string',
                    'location': 'string',
                    'bandwidth': 'string',
                    'vlan': 123,
                    'partnerName': 'string',
                    'loaIssueTime': datetime(2015, 1, 1),
                    'lagId': 'string',
                    'awsDevice': 'string'
                },
            ],
            'allowsHostedConnections': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes a link aggregation group (LAG). A LAG is a connection that uses the Link Aggregation Control Protocol (LACP) to logically aggregate a bundle of physical connections. Like an interconnect, it can host other connections. All connections in a LAG must terminate on the same physical AWS Direct Connect endpoint, and must be the same bandwidth.

        
        

        - **connectionsBandwidth** *(string) --* 

          The individual bandwidth of the physical connections bundled by the LAG.

           

          Available values: 1Gbps, 10Gbps

          
        

        - **numberOfConnections** *(integer) --* 

          The number of physical connections bundled by the LAG, up to a maximum of 10.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **ownerAccount** *(string) --* 

          The owner of the LAG.

          
        

        - **lagName** *(string) --* 

          The name of the LAG.

          
        

        - **lagState** *(string) --* 

          The state of the LAG.

           

           
          * **Requested** : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available. 
           
          * **Pending** : The LAG has been approved, and is being initialized. 
           
          * **Available** : The network link is established, and the LAG is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The LAG is in the process of being deleted. 
           
          * **Deleted** : The LAG has been deleted. 
           

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **minimumLinks** *(integer) --* 

          The minimum number of physical connections that must be operational for the LAG itself to be operational. If the number of operational connections drops below this setting, the LAG state changes to ``down`` . This value can help to ensure that a LAG is not overutilized if a significant number of its bundled connections go down.

          
        

        - **awsDevice** *(string) --* 

          The AWS Direct Connection endpoint that hosts the LAG.

          
        

        - **connections** *(list) --* 

          A list of connections bundled by this LAG.

          
          

          - *(dict) --* 

            A connection represents the physical network connection between the AWS Direct Connect location and the customer.

            
            

            - **ownerAccount** *(string) --* 

              The AWS account that will own the new connection.

              
            

            - **connectionId** *(string) --* 

              The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

               

              Example: dxcon-fg5678gh

               

              Default: None

              
            

            - **connectionName** *(string) --* 

              The name of the connection.

               

              Example: "*My Connection to AWS* "

               

              Default: None

              
            

            - **connectionState** *(string) --* 

              State of the connection.

               

               
              * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
               
              * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
               
              * **Pending** : The connection has been approved, and is being initialized. 
               
              * **Available** : The network link is up, and the connection is ready for use. 
               
              * **Down** : The network link is down. 
               
              * **Deleting** : The connection is in the process of being deleted. 
               
              * **Deleted** : The connection has been deleted. 
               
              * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
               

              
            

            - **region** *(string) --* 

              The AWS region where the connection is located.

               

              Example: us-east-1

               

              Default: None

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **bandwidth** *(string) --* 

              Bandwidth of the connection.

               

              Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

               

              Default: None

              
            

            - **vlan** *(integer) --* 

              The VLAN ID.

               

              Example: 101

              
            

            - **partnerName** *(string) --* 

              The name of the AWS Direct Connect service provider associated with the connection.

              
            

            - **loaIssueTime** *(datetime) --* 

              The time of the most recent call to  DescribeLoa for this connection.

              
            

            - **lagId** *(string) --* 

              The ID of the LAG.

               

              Example: dxlag-fg5678gh

              
            

            - **awsDevice** *(string) --* 

              The Direct Connection endpoint which the physical connection terminates on.

              
        
      
        

        - **allowsHostedConnections** *(boolean) --* 

          Indicates whether the LAG can host other connections.

           

          .. note::

             

            This is intended for use by AWS Direct Connect partners only.

             

          
    

  .. py:method:: create_private_virtual_interface(**kwargs)

    

    Creates a new private virtual interface. A virtual interface is the VLAN that transports AWS Direct Connect traffic. A private virtual interface supports sending traffic to a single virtual private cloud (VPC).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreatePrivateVirtualInterface>`_    


    **Request Syntax** 
    ::

      response = client.create_private_virtual_interface(
          connectionId='string',
          newPrivateVirtualInterface={
              'virtualInterfaceName': 'string',
              'vlan': 123,
              'asn': 123,
              'authKey': 'string',
              'amazonAddress': 'string',
              'customerAddress': 'string',
              'addressFamily': 'ipv4'|'ipv6',
              'virtualGatewayId': 'string',
              'directConnectGatewayId': 'string'
          }
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

       

      Example: dxcon-fg5678gh

       

      Default: None

      

    
    :type newPrivateVirtualInterface: dict
    :param newPrivateVirtualInterface: **[REQUIRED]** 

      Detailed information for the private virtual interface to be created.

       

      Default: None

      

    
      - **virtualInterfaceName** *(string) --* **[REQUIRED]** 

        The name of the virtual interface assigned by the customer.

         

        Example: "My VPC"

        

      
      - **vlan** *(integer) --* **[REQUIRED]** 

        The VLAN ID.

         

        Example: 101

        

      
      - **asn** *(integer) --* **[REQUIRED]** 

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

         

        Example: 65000

        

      
      - **authKey** *(string) --* 

        The authentication key for BGP configuration.

         

        Example: asdf34example

        

      
      - **amazonAddress** *(string) --* 

        IP address assigned to the Amazon interface.

         

        Example: 192.168.1.1/30 or 2001:db8::1/125

        

      
      - **customerAddress** *(string) --* 

        IP address assigned to the customer interface.

         

        Example: 192.168.1.2/30 or 2001:db8::2/125

        

      
      - **addressFamily** *(string) --* 

        Indicates the address family for the BGP peer.

         

         
        * **ipv4** : IPv4 address family 
         
        * **ipv6** : IPv6 address family 
         

        

      
      - **virtualGatewayId** *(string) --* 

        The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

         

        Example: vgw-123er56

        

      
      - **directConnectGatewayId** *(string) --* 

        The ID of the direct connect gateway.

         

        Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new virtual interface.

          
        

        - **virtualInterfaceId** *(string) --* 

          The ID of the virtual interface.

           

          Example: dxvif-123dfg56

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **virtualInterfaceType** *(string) --* 

          The type of virtual interface.

           

          Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so on.)

          
        

        - **virtualInterfaceName** *(string) --* 

          The name of the virtual interface assigned by the customer.

           

          Example: "My VPC"

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **asn** *(integer) --* 

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

           

          Example: 65000

          
        

        - **amazonSideAsn** *(integer) --* 

          The autonomous system number (ASN) for the Amazon side of the connection.

          
        

        - **authKey** *(string) --* 

          The authentication key for BGP configuration.

           

          Example: asdf34example

          
        

        - **amazonAddress** *(string) --* 

          IP address assigned to the Amazon interface.

           

          Example: 192.168.1.1/30 or 2001:db8::1/125

          
        

        - **customerAddress** *(string) --* 

          IP address assigned to the customer interface.

           

          Example: 192.168.1.2/30 or 2001:db8::2/125

          
        

        - **addressFamily** *(string) --* 

          Indicates the address family for the BGP peer.

           

           
          * **ipv4** : IPv4 address family 
           
          * **ipv6** : IPv6 address family 
           

          
        

        - **virtualInterfaceState** *(string) --* 

          State of the virtual interface.

           

           
          * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
           
          * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
           
          * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
           
          * **Available** : A virtual interface that is able to forward traffic. 
           
          * **Down** : A virtual interface that is BGP down. 
           
          * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
           
          * **Deleted** : A virtual interface that cannot forward traffic. 
           
          * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
           

          
        

        - **customerRouterConfig** *(string) --* 

          Information for generating the customer router configuration.

          
        

        - **virtualGatewayId** *(string) --* 

          The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

           

          Example: vgw-123er56

          
        

        - **directConnectGatewayId** *(string) --* 

          The ID of the direct connect gateway.

           

          Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

          
        

        - **routeFilterPrefixes** *(list) --* 

          A list of routes to be advertised to the AWS network in this region (public virtual interface).

          
          

          - *(dict) --* 

            A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

            
            

            - **cidr** *(string) --* 

              CIDR notation for the advertised route. Multiple routes are separated by commas.

               

              IPv6 CIDRs must be at least a /64 or shorter

               

              Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

              
        
      
        

        - **bgpPeers** *(list) --* 

          A list of the BGP peers configured on this virtual interface.

          
          

          - *(dict) --* 

            A structure containing information about a BGP peer.

            
            

            - **asn** *(integer) --* 

              The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

               

              Example: 65000

              
            

            - **authKey** *(string) --* 

              The authentication key for BGP configuration.

               

              Example: asdf34example

              
            

            - **addressFamily** *(string) --* 

              Indicates the address family for the BGP peer.

               

               
              * **ipv4** : IPv4 address family 
               
              * **ipv6** : IPv6 address family 
               

              
            

            - **amazonAddress** *(string) --* 

              IP address assigned to the Amazon interface.

               

              Example: 192.168.1.1/30 or 2001:db8::1/125

              
            

            - **customerAddress** *(string) --* 

              IP address assigned to the customer interface.

               

              Example: 192.168.1.2/30 or 2001:db8::2/125

              
            

            - **bgpPeerState** *(string) --* 

              The state of the BGP peer.

               

               
              * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.  
               
              * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established. 
               
              * **Available** : The BGP peer can be established. 
               
              * **Deleting** : The BGP peer is in the process of being deleted. 
               
              * **Deleted** : The BGP peer has been deleted and cannot be established. 
               

              
            

            - **bgpStatus** *(string) --* 

              The Up/Down state of the BGP peer.

               

               
              * **Up** : The BGP peer is established. 
               
              * **Down** : The BGP peer is down. 
               

              
        
      
    

  .. py:method:: create_public_virtual_interface(**kwargs)

    

    Creates a new public virtual interface. A virtual interface is the VLAN that transports AWS Direct Connect traffic. A public virtual interface supports sending traffic to public services of AWS such as Amazon Simple Storage Service (Amazon S3).

     

    When creating an IPv6 public virtual interface (addressFamily is 'ipv6'), the customer and amazon address fields should be left blank to use auto-assigned IPv6 space. Custom IPv6 Addresses are currently not supported.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreatePublicVirtualInterface>`_    


    **Request Syntax** 
    ::

      response = client.create_public_virtual_interface(
          connectionId='string',
          newPublicVirtualInterface={
              'virtualInterfaceName': 'string',
              'vlan': 123,
              'asn': 123,
              'authKey': 'string',
              'amazonAddress': 'string',
              'customerAddress': 'string',
              'addressFamily': 'ipv4'|'ipv6',
              'routeFilterPrefixes': [
                  {
                      'cidr': 'string'
                  },
              ]
          }
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

       

      Example: dxcon-fg5678gh

       

      Default: None

      

    
    :type newPublicVirtualInterface: dict
    :param newPublicVirtualInterface: **[REQUIRED]** 

      Detailed information for the public virtual interface to be created.

       

      Default: None

      

    
      - **virtualInterfaceName** *(string) --* **[REQUIRED]** 

        The name of the virtual interface assigned by the customer.

         

        Example: "My VPC"

        

      
      - **vlan** *(integer) --* **[REQUIRED]** 

        The VLAN ID.

         

        Example: 101

        

      
      - **asn** *(integer) --* **[REQUIRED]** 

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

         

        Example: 65000

        

      
      - **authKey** *(string) --* 

        The authentication key for BGP configuration.

         

        Example: asdf34example

        

      
      - **amazonAddress** *(string) --* 

        IP address assigned to the Amazon interface.

         

        Example: 192.168.1.1/30 or 2001:db8::1/125

        

      
      - **customerAddress** *(string) --* 

        IP address assigned to the customer interface.

         

        Example: 192.168.1.2/30 or 2001:db8::2/125

        

      
      - **addressFamily** *(string) --* 

        Indicates the address family for the BGP peer.

         

         
        * **ipv4** : IPv4 address family 
         
        * **ipv6** : IPv6 address family 
         

        

      
      - **routeFilterPrefixes** *(list) --* 

        A list of routes to be advertised to the AWS network in this region (public virtual interface).

        

      
        - *(dict) --* 

          A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

          

        
          - **cidr** *(string) --* 

            CIDR notation for the advertised route. Multiple routes are separated by commas.

             

            IPv6 CIDRs must be at least a /64 or shorter

             

            Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

            

          
        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new virtual interface.

          
        

        - **virtualInterfaceId** *(string) --* 

          The ID of the virtual interface.

           

          Example: dxvif-123dfg56

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **virtualInterfaceType** *(string) --* 

          The type of virtual interface.

           

          Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so on.)

          
        

        - **virtualInterfaceName** *(string) --* 

          The name of the virtual interface assigned by the customer.

           

          Example: "My VPC"

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **asn** *(integer) --* 

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

           

          Example: 65000

          
        

        - **amazonSideAsn** *(integer) --* 

          The autonomous system number (ASN) for the Amazon side of the connection.

          
        

        - **authKey** *(string) --* 

          The authentication key for BGP configuration.

           

          Example: asdf34example

          
        

        - **amazonAddress** *(string) --* 

          IP address assigned to the Amazon interface.

           

          Example: 192.168.1.1/30 or 2001:db8::1/125

          
        

        - **customerAddress** *(string) --* 

          IP address assigned to the customer interface.

           

          Example: 192.168.1.2/30 or 2001:db8::2/125

          
        

        - **addressFamily** *(string) --* 

          Indicates the address family for the BGP peer.

           

           
          * **ipv4** : IPv4 address family 
           
          * **ipv6** : IPv6 address family 
           

          
        

        - **virtualInterfaceState** *(string) --* 

          State of the virtual interface.

           

           
          * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
           
          * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
           
          * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
           
          * **Available** : A virtual interface that is able to forward traffic. 
           
          * **Down** : A virtual interface that is BGP down. 
           
          * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
           
          * **Deleted** : A virtual interface that cannot forward traffic. 
           
          * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
           

          
        

        - **customerRouterConfig** *(string) --* 

          Information for generating the customer router configuration.

          
        

        - **virtualGatewayId** *(string) --* 

          The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

           

          Example: vgw-123er56

          
        

        - **directConnectGatewayId** *(string) --* 

          The ID of the direct connect gateway.

           

          Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

          
        

        - **routeFilterPrefixes** *(list) --* 

          A list of routes to be advertised to the AWS network in this region (public virtual interface).

          
          

          - *(dict) --* 

            A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

            
            

            - **cidr** *(string) --* 

              CIDR notation for the advertised route. Multiple routes are separated by commas.

               

              IPv6 CIDRs must be at least a /64 or shorter

               

              Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

              
        
      
        

        - **bgpPeers** *(list) --* 

          A list of the BGP peers configured on this virtual interface.

          
          

          - *(dict) --* 

            A structure containing information about a BGP peer.

            
            

            - **asn** *(integer) --* 

              The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

               

              Example: 65000

              
            

            - **authKey** *(string) --* 

              The authentication key for BGP configuration.

               

              Example: asdf34example

              
            

            - **addressFamily** *(string) --* 

              Indicates the address family for the BGP peer.

               

               
              * **ipv4** : IPv4 address family 
               
              * **ipv6** : IPv6 address family 
               

              
            

            - **amazonAddress** *(string) --* 

              IP address assigned to the Amazon interface.

               

              Example: 192.168.1.1/30 or 2001:db8::1/125

              
            

            - **customerAddress** *(string) --* 

              IP address assigned to the customer interface.

               

              Example: 192.168.1.2/30 or 2001:db8::2/125

              
            

            - **bgpPeerState** *(string) --* 

              The state of the BGP peer.

               

               
              * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.  
               
              * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established. 
               
              * **Available** : The BGP peer can be established. 
               
              * **Deleting** : The BGP peer is in the process of being deleted. 
               
              * **Deleted** : The BGP peer has been deleted and cannot be established. 
               

              
            

            - **bgpStatus** *(string) --* 

              The Up/Down state of the BGP peer.

               

               
              * **Up** : The BGP peer is established. 
               
              * **Down** : The BGP peer is down. 
               

              
        
      
    

  .. py:method:: delete_bgp_peer(**kwargs)

    

    Deletes a BGP peer on the specified virtual interface that matches the specified customer address and ASN. You cannot delete the last BGP peer from a virtual interface.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DeleteBGPPeer>`_    


    **Request Syntax** 
    ::

      response = client.delete_bgp_peer(
          virtualInterfaceId='string',
          asn=123,
          customerAddress='string'
      )
    :type virtualInterfaceId: string
    :param virtualInterfaceId: 

      The ID of the virtual interface from which the BGP peer will be deleted.

       

      Example: dxvif-456abc78

       

      Default: None

      

    
    :type asn: integer
    :param asn: 

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

       

      Example: 65000

      

    
    :type customerAddress: string
    :param customerAddress: 

      IP address assigned to the customer interface.

       

      Example: 192.168.1.2/30 or 2001:db8::2/125

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'virtualInterface': {
                'ownerAccount': 'string',
                'virtualInterfaceId': 'string',
                'location': 'string',
                'connectionId': 'string',
                'virtualInterfaceType': 'string',
                'virtualInterfaceName': 'string',
                'vlan': 123,
                'asn': 123,
                'amazonSideAsn': 123,
                'authKey': 'string',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'customerRouterConfig': 'string',
                'virtualGatewayId': 'string',
                'directConnectGatewayId': 'string',
                'routeFilterPrefixes': [
                    {
                        'cidr': 'string'
                    },
                ],
                'bgpPeers': [
                    {
                        'asn': 123,
                        'authKey': 'string',
                        'addressFamily': 'ipv4'|'ipv6',
                        'amazonAddress': 'string',
                        'customerAddress': 'string',
                        'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                        'bgpStatus': 'up'|'down'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when DeleteBGPPeer is called.

        
        

        - **virtualInterface** *(dict) --* 

          A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

          
          

          - **ownerAccount** *(string) --* 

            The AWS account that will own the new virtual interface.

            
          

          - **virtualInterfaceId** *(string) --* 

            The ID of the virtual interface.

             

            Example: dxvif-123dfg56

             

            Default: None

            
          

          - **location** *(string) --* 

            Where the connection is located.

             

            Example: EqSV5

             

            Default: None

            
          

          - **connectionId** *(string) --* 

            The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

             

            Example: dxcon-fg5678gh

             

            Default: None

            
          

          - **virtualInterfaceType** *(string) --* 

            The type of virtual interface.

             

            Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so on.)

            
          

          - **virtualInterfaceName** *(string) --* 

            The name of the virtual interface assigned by the customer.

             

            Example: "My VPC"

            
          

          - **vlan** *(integer) --* 

            The VLAN ID.

             

            Example: 101

            
          

          - **asn** *(integer) --* 

            The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

             

            Example: 65000

            
          

          - **amazonSideAsn** *(integer) --* 

            The autonomous system number (ASN) for the Amazon side of the connection.

            
          

          - **authKey** *(string) --* 

            The authentication key for BGP configuration.

             

            Example: asdf34example

            
          

          - **amazonAddress** *(string) --* 

            IP address assigned to the Amazon interface.

             

            Example: 192.168.1.1/30 or 2001:db8::1/125

            
          

          - **customerAddress** *(string) --* 

            IP address assigned to the customer interface.

             

            Example: 192.168.1.2/30 or 2001:db8::2/125

            
          

          - **addressFamily** *(string) --* 

            Indicates the address family for the BGP peer.

             

             
            * **ipv4** : IPv4 address family 
             
            * **ipv6** : IPv6 address family 
             

            
          

          - **virtualInterfaceState** *(string) --* 

            State of the virtual interface.

             

             
            * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
             
            * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
             
            * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
             
            * **Available** : A virtual interface that is able to forward traffic. 
             
            * **Down** : A virtual interface that is BGP down. 
             
            * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
             
            * **Deleted** : A virtual interface that cannot forward traffic. 
             
            * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
             

            
          

          - **customerRouterConfig** *(string) --* 

            Information for generating the customer router configuration.

            
          

          - **virtualGatewayId** *(string) --* 

            The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

             

            Example: vgw-123er56

            
          

          - **directConnectGatewayId** *(string) --* 

            The ID of the direct connect gateway.

             

            Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

            
          

          - **routeFilterPrefixes** *(list) --* 

            A list of routes to be advertised to the AWS network in this region (public virtual interface).

            
            

            - *(dict) --* 

              A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

              
              

              - **cidr** *(string) --* 

                CIDR notation for the advertised route. Multiple routes are separated by commas.

                 

                IPv6 CIDRs must be at least a /64 or shorter

                 

                Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

                
          
        
          

          - **bgpPeers** *(list) --* 

            A list of the BGP peers configured on this virtual interface.

            
            

            - *(dict) --* 

              A structure containing information about a BGP peer.

              
              

              - **asn** *(integer) --* 

                The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

                 

                Example: 65000

                
              

              - **authKey** *(string) --* 

                The authentication key for BGP configuration.

                 

                Example: asdf34example

                
              

              - **addressFamily** *(string) --* 

                Indicates the address family for the BGP peer.

                 

                 
                * **ipv4** : IPv4 address family 
                 
                * **ipv6** : IPv6 address family 
                 

                
              

              - **amazonAddress** *(string) --* 

                IP address assigned to the Amazon interface.

                 

                Example: 192.168.1.1/30 or 2001:db8::1/125

                
              

              - **customerAddress** *(string) --* 

                IP address assigned to the customer interface.

                 

                Example: 192.168.1.2/30 or 2001:db8::2/125

                
              

              - **bgpPeerState** *(string) --* 

                The state of the BGP peer.

                 

                 
                * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.  
                 
                * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established. 
                 
                * **Available** : The BGP peer can be established. 
                 
                * **Deleting** : The BGP peer is in the process of being deleted. 
                 
                * **Deleted** : The BGP peer has been deleted and cannot be established. 
                 

                
              

              - **bgpStatus** *(string) --* 

                The Up/Down state of the BGP peer.

                 

                 
                * **Up** : The BGP peer is established. 
                 
                * **Down** : The BGP peer is down. 
                 

                
          
        
      
    

  .. py:method:: delete_connection(**kwargs)

    

    Deletes the connection.

     

    Deleting a connection only stops the AWS Direct Connect port hour and data transfer charges. You need to cancel separately with the providers any services or charges for cross-connects or network circuits that connect you to the AWS Direct Connect location.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DeleteConnection>`_    


    **Request Syntax** 
    ::

      response = client.delete_connection(
          connectionId='string'
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

       

      Example: dxcon-fg5678gh

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A connection represents the physical network connection between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new connection.

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **connectionName** *(string) --* 

          The name of the connection.

           

          Example: "*My Connection to AWS* "

           

          Default: None

          
        

        - **connectionState** *(string) --* 

          State of the connection.

           

           
          * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
           
          * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The connection has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the connection is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The connection is in the process of being deleted. 
           
          * **Deleted** : The connection has been deleted. 
           
          * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
           

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **bandwidth** *(string) --* 

          Bandwidth of the connection.

           

          Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

           

          Default: None

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **partnerName** *(string) --* 

          The name of the AWS Direct Connect service provider associated with the connection.

          
        

        - **loaIssueTime** *(datetime) --* 

          The time of the most recent call to  DescribeLoa for this connection.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **awsDevice** *(string) --* 

          The Direct Connection endpoint which the physical connection terminates on.

          
    

  .. py:method:: delete_direct_connect_gateway(**kwargs)

    

    Deletes a direct connect gateway. You must first delete all virtual interfaces that are attached to the direct connect gateway and disassociate all virtual private gateways that are associated with the direct connect gateway.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DeleteDirectConnectGateway>`_    


    **Request Syntax** 
    ::

      response = client.delete_direct_connect_gateway(
          directConnectGatewayId='string'
      )
    :type directConnectGatewayId: string
    :param directConnectGatewayId: **[REQUIRED]** 

      The ID of the direct connect gateway.

       

      Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'directConnectGateway': {
                'directConnectGatewayId': 'string',
                'directConnectGatewayName': 'string',
                'amazonSideAsn': 123,
                'ownerAccount': 'string',
                'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
                'stateChangeError': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the response from the DeleteDirectConnectGateway API call

        
        

        - **directConnectGateway** *(dict) --* 

          The direct connect gateway to be deleted.

          
          

          - **directConnectGatewayId** *(string) --* 

            The ID of the direct connect gateway.

             

            Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

            
          

          - **directConnectGatewayName** *(string) --* 

            The name of the direct connect gateway.

             

            Example: "My direct connect gateway"

             

            Default: None

            
          

          - **amazonSideAsn** *(integer) --* 

            The autonomous system number (ASN) for the Amazon side of the connection.

            
          

          - **ownerAccount** *(string) --* 

            The AWS account ID of the owner of the direct connect gateway.

            
          

          - **directConnectGatewayState** *(string) --* 

            State of the direct connect gateway.

             

             
            * **Pending** : The initial state after calling  CreateDirectConnectGateway . 
             
            * **Available** : The direct connect gateway is ready for use. 
             
            * **Deleting** : The initial state after calling  DeleteDirectConnectGateway . 
             
            * **Deleted** : The direct connect gateway is deleted and cannot pass traffic. 
             

            
          

          - **stateChangeError** *(string) --* 

            Error message when the state of an object fails to advance.

            
      
    

  .. py:method:: delete_direct_connect_gateway_association(**kwargs)

    

    Deletes the association between a direct connect gateway and a virtual private gateway.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation>`_    


    **Request Syntax** 
    ::

      response = client.delete_direct_connect_gateway_association(
          directConnectGatewayId='string',
          virtualGatewayId='string'
      )
    :type directConnectGatewayId: string
    :param directConnectGatewayId: **[REQUIRED]** 

      The ID of the direct connect gateway.

       

      Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

       

      Default: None

      

    
    :type virtualGatewayId: string
    :param virtualGatewayId: **[REQUIRED]** 

      The ID of the virtual private gateway.

       

      Example: "vgw-abc123ef"

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'directConnectGatewayAssociation': {
                'directConnectGatewayId': 'string',
                'virtualGatewayId': 'string',
                'virtualGatewayRegion': 'string',
                'virtualGatewayOwnerAccount': 'string',
                'associationState': 'associating'|'associated'|'disassociating'|'disassociated',
                'stateChangeError': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the response from the DeleteDirectConnectGatewayAssociation API call

        
        

        - **directConnectGatewayAssociation** *(dict) --* 

          The direct connect gateway association to be deleted.

          
          

          - **directConnectGatewayId** *(string) --* 

            The ID of the direct connect gateway.

             

            Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

            
          

          - **virtualGatewayId** *(string) --* 

            The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

             

            Example: vgw-123er56

            
          

          - **virtualGatewayRegion** *(string) --* 

            The region in which the virtual private gateway is located.

             

            Example: us-east-1

            
          

          - **virtualGatewayOwnerAccount** *(string) --* 

            The AWS account ID of the owner of the virtual private gateway.

            
          

          - **associationState** *(string) --* 

            State of the direct connect gateway association.

             

             
            * **Associating** : The initial state after calling  CreateDirectConnectGatewayAssociation . 
             
            * **Associated** : The direct connect gateway and virtual private gateway are successfully associated and ready to pass traffic. 
             
            * **Disassociating** : The initial state after calling  DeleteDirectConnectGatewayAssociation . 
             
            * **Disassociated** : The virtual private gateway is successfully disassociated from the direct connect gateway. Traffic flow between the direct connect gateway and virtual private gateway stops. 
             

            
          

          - **stateChangeError** *(string) --* 

            Error message when the state of an object fails to advance.

            
      
    

  .. py:method:: delete_interconnect(**kwargs)

    

    Deletes the specified interconnect.

     

    .. note::

       

      This is intended for use by AWS Direct Connect partners only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DeleteInterconnect>`_    


    **Request Syntax** 
    ::

      response = client.delete_interconnect(
          interconnectId='string'
      )
    :type interconnectId: string
    :param interconnectId: **[REQUIRED]** 

      The ID of the interconnect.

       

      Example: dxcon-abc123

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when DeleteInterconnect is called.

        
        

        - **interconnectState** *(string) --* 

          State of the interconnect.

           

           
          * **Requested** : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The interconnect has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the interconnect is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The interconnect is in the process of being deleted. 
           
          * **Deleted** : The interconnect has been deleted. 
           

          
    

  .. py:method:: delete_lag(**kwargs)

    

    Deletes a link aggregation group (LAG). You cannot delete a LAG if it has active virtual interfaces or hosted connections.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DeleteLag>`_    


    **Request Syntax** 
    ::

      response = client.delete_lag(
          lagId='string'
      )
    :type lagId: string
    :param lagId: **[REQUIRED]** 

      The ID of the LAG to delete.

       

      Example: dxlag-abc123

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'connectionsBandwidth': 'string',
            'numberOfConnections': 123,
            'lagId': 'string',
            'ownerAccount': 'string',
            'lagName': 'string',
            'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
            'location': 'string',
            'region': 'string',
            'minimumLinks': 123,
            'awsDevice': 'string',
            'connections': [
                {
                    'ownerAccount': 'string',
                    'connectionId': 'string',
                    'connectionName': 'string',
                    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                    'region': 'string',
                    'location': 'string',
                    'bandwidth': 'string',
                    'vlan': 123,
                    'partnerName': 'string',
                    'loaIssueTime': datetime(2015, 1, 1),
                    'lagId': 'string',
                    'awsDevice': 'string'
                },
            ],
            'allowsHostedConnections': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes a link aggregation group (LAG). A LAG is a connection that uses the Link Aggregation Control Protocol (LACP) to logically aggregate a bundle of physical connections. Like an interconnect, it can host other connections. All connections in a LAG must terminate on the same physical AWS Direct Connect endpoint, and must be the same bandwidth.

        
        

        - **connectionsBandwidth** *(string) --* 

          The individual bandwidth of the physical connections bundled by the LAG.

           

          Available values: 1Gbps, 10Gbps

          
        

        - **numberOfConnections** *(integer) --* 

          The number of physical connections bundled by the LAG, up to a maximum of 10.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **ownerAccount** *(string) --* 

          The owner of the LAG.

          
        

        - **lagName** *(string) --* 

          The name of the LAG.

          
        

        - **lagState** *(string) --* 

          The state of the LAG.

           

           
          * **Requested** : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available. 
           
          * **Pending** : The LAG has been approved, and is being initialized. 
           
          * **Available** : The network link is established, and the LAG is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The LAG is in the process of being deleted. 
           
          * **Deleted** : The LAG has been deleted. 
           

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **minimumLinks** *(integer) --* 

          The minimum number of physical connections that must be operational for the LAG itself to be operational. If the number of operational connections drops below this setting, the LAG state changes to ``down`` . This value can help to ensure that a LAG is not overutilized if a significant number of its bundled connections go down.

          
        

        - **awsDevice** *(string) --* 

          The AWS Direct Connection endpoint that hosts the LAG.

          
        

        - **connections** *(list) --* 

          A list of connections bundled by this LAG.

          
          

          - *(dict) --* 

            A connection represents the physical network connection between the AWS Direct Connect location and the customer.

            
            

            - **ownerAccount** *(string) --* 

              The AWS account that will own the new connection.

              
            

            - **connectionId** *(string) --* 

              The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

               

              Example: dxcon-fg5678gh

               

              Default: None

              
            

            - **connectionName** *(string) --* 

              The name of the connection.

               

              Example: "*My Connection to AWS* "

               

              Default: None

              
            

            - **connectionState** *(string) --* 

              State of the connection.

               

               
              * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
               
              * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
               
              * **Pending** : The connection has been approved, and is being initialized. 
               
              * **Available** : The network link is up, and the connection is ready for use. 
               
              * **Down** : The network link is down. 
               
              * **Deleting** : The connection is in the process of being deleted. 
               
              * **Deleted** : The connection has been deleted. 
               
              * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
               

              
            

            - **region** *(string) --* 

              The AWS region where the connection is located.

               

              Example: us-east-1

               

              Default: None

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **bandwidth** *(string) --* 

              Bandwidth of the connection.

               

              Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

               

              Default: None

              
            

            - **vlan** *(integer) --* 

              The VLAN ID.

               

              Example: 101

              
            

            - **partnerName** *(string) --* 

              The name of the AWS Direct Connect service provider associated with the connection.

              
            

            - **loaIssueTime** *(datetime) --* 

              The time of the most recent call to  DescribeLoa for this connection.

              
            

            - **lagId** *(string) --* 

              The ID of the LAG.

               

              Example: dxlag-fg5678gh

              
            

            - **awsDevice** *(string) --* 

              The Direct Connection endpoint which the physical connection terminates on.

              
        
      
        

        - **allowsHostedConnections** *(boolean) --* 

          Indicates whether the LAG can host other connections.

           

          .. note::

             

            This is intended for use by AWS Direct Connect partners only.

             

          
    

  .. py:method:: delete_virtual_interface(**kwargs)

    

    Deletes a virtual interface.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DeleteVirtualInterface>`_    


    **Request Syntax** 
    ::

      response = client.delete_virtual_interface(
          virtualInterfaceId='string'
      )
    :type virtualInterfaceId: string
    :param virtualInterfaceId: **[REQUIRED]** 

      The ID of the virtual interface.

       

      Example: dxvif-123dfg56

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when DeleteVirtualInterface is called.

        
        

        - **virtualInterfaceState** *(string) --* 

          State of the virtual interface.

           

           
          * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
           
          * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
           
          * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
           
          * **Available** : A virtual interface that is able to forward traffic. 
           
          * **Down** : A virtual interface that is BGP down. 
           
          * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
           
          * **Deleted** : A virtual interface that cannot forward traffic. 
           
          * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
           

          
    

  .. py:method:: describe_connection_loa(**kwargs)

    

    Deprecated in favor of  DescribeLoa .

     

    Returns the LOA-CFA for a Connection.

     

    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that your APN partner or service provider uses when establishing your cross connect to AWS at the colocation facility. For more information, see `Requesting Cross Connects at AWS Direct Connect Locations <http://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html>`__ in the AWS Direct Connect user guide.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeConnectionLoa>`_    


    **Request Syntax** 
    ::

      response = client.describe_connection_loa(
          connectionId='string',
          providerName='string',
          loaContentType='application/pdf'
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

       

      Example: dxcon-fg5678gh

       

      Default: None

      

    
    :type providerName: string
    :param providerName: 

      The name of the APN partner or service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

       

      Default: None

      

    
    :type loaContentType: string
    :param loaContentType: 

      A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is "application/pdf".

       

      Default: application/pdf

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'loa': {
                'loaContent': b'bytes',
                'loaContentType': 'application/pdf'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when DescribeConnectionLoa is called.

        
        

        - **loa** *(dict) --* 

          A structure containing the Letter of Authorization - Connecting Facility Assignment (LOA-CFA) for a connection.

          
          

          - **loaContent** *(bytes) --* 

            The binary contents of the LOA-CFA document.

            
          

          - **loaContentType** *(string) --* 

            A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is "application/pdf".

             

            Default: application/pdf

            
      
    

  .. py:method:: describe_connections(**kwargs)

    

    Displays all connections in this region.

     

    If a connection ID is provided, the call returns only that particular connection.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeConnections>`_    


    **Request Syntax** 
    ::

      response = client.describe_connections(
          connectionId='string'
      )
    :type connectionId: string
    :param connectionId: 

      The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

       

      Example: dxcon-fg5678gh

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'connections': [
                {
                    'ownerAccount': 'string',
                    'connectionId': 'string',
                    'connectionName': 'string',
                    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                    'region': 'string',
                    'location': 'string',
                    'bandwidth': 'string',
                    'vlan': 123,
                    'partnerName': 'string',
                    'loaIssueTime': datetime(2015, 1, 1),
                    'lagId': 'string',
                    'awsDevice': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A structure containing a list of connections.

        
        

        - **connections** *(list) --* 

          A list of connections.

          
          

          - *(dict) --* 

            A connection represents the physical network connection between the AWS Direct Connect location and the customer.

            
            

            - **ownerAccount** *(string) --* 

              The AWS account that will own the new connection.

              
            

            - **connectionId** *(string) --* 

              The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

               

              Example: dxcon-fg5678gh

               

              Default: None

              
            

            - **connectionName** *(string) --* 

              The name of the connection.

               

              Example: "*My Connection to AWS* "

               

              Default: None

              
            

            - **connectionState** *(string) --* 

              State of the connection.

               

               
              * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
               
              * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
               
              * **Pending** : The connection has been approved, and is being initialized. 
               
              * **Available** : The network link is up, and the connection is ready for use. 
               
              * **Down** : The network link is down. 
               
              * **Deleting** : The connection is in the process of being deleted. 
               
              * **Deleted** : The connection has been deleted. 
               
              * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
               

              
            

            - **region** *(string) --* 

              The AWS region where the connection is located.

               

              Example: us-east-1

               

              Default: None

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **bandwidth** *(string) --* 

              Bandwidth of the connection.

               

              Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

               

              Default: None

              
            

            - **vlan** *(integer) --* 

              The VLAN ID.

               

              Example: 101

              
            

            - **partnerName** *(string) --* 

              The name of the AWS Direct Connect service provider associated with the connection.

              
            

            - **loaIssueTime** *(datetime) --* 

              The time of the most recent call to  DescribeLoa for this connection.

              
            

            - **lagId** *(string) --* 

              The ID of the LAG.

               

              Example: dxlag-fg5678gh

              
            

            - **awsDevice** *(string) --* 

              The Direct Connection endpoint which the physical connection terminates on.

              
        
      
    

  .. py:method:: describe_connections_on_interconnect(**kwargs)

    

    Deprecated in favor of  DescribeHostedConnections .

     

    Returns a list of connections that have been provisioned on the given interconnect.

     

    .. note::

       

      This is intended for use by AWS Direct Connect partners only.

       

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeConnectionsOnInterconnect>`_    


    **Request Syntax** 
    ::

      response = client.describe_connections_on_interconnect(
          interconnectId='string'
      )
    :type interconnectId: string
    :param interconnectId: **[REQUIRED]** 

      ID of the interconnect on which a list of connection is provisioned.

       

      Example: dxcon-abc123

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'connections': [
                {
                    'ownerAccount': 'string',
                    'connectionId': 'string',
                    'connectionName': 'string',
                    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                    'region': 'string',
                    'location': 'string',
                    'bandwidth': 'string',
                    'vlan': 123,
                    'partnerName': 'string',
                    'loaIssueTime': datetime(2015, 1, 1),
                    'lagId': 'string',
                    'awsDevice': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A structure containing a list of connections.

        
        

        - **connections** *(list) --* 

          A list of connections.

          
          

          - *(dict) --* 

            A connection represents the physical network connection between the AWS Direct Connect location and the customer.

            
            

            - **ownerAccount** *(string) --* 

              The AWS account that will own the new connection.

              
            

            - **connectionId** *(string) --* 

              The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

               

              Example: dxcon-fg5678gh

               

              Default: None

              
            

            - **connectionName** *(string) --* 

              The name of the connection.

               

              Example: "*My Connection to AWS* "

               

              Default: None

              
            

            - **connectionState** *(string) --* 

              State of the connection.

               

               
              * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
               
              * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
               
              * **Pending** : The connection has been approved, and is being initialized. 
               
              * **Available** : The network link is up, and the connection is ready for use. 
               
              * **Down** : The network link is down. 
               
              * **Deleting** : The connection is in the process of being deleted. 
               
              * **Deleted** : The connection has been deleted. 
               
              * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
               

              
            

            - **region** *(string) --* 

              The AWS region where the connection is located.

               

              Example: us-east-1

               

              Default: None

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **bandwidth** *(string) --* 

              Bandwidth of the connection.

               

              Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

               

              Default: None

              
            

            - **vlan** *(integer) --* 

              The VLAN ID.

               

              Example: 101

              
            

            - **partnerName** *(string) --* 

              The name of the AWS Direct Connect service provider associated with the connection.

              
            

            - **loaIssueTime** *(datetime) --* 

              The time of the most recent call to  DescribeLoa for this connection.

              
            

            - **lagId** *(string) --* 

              The ID of the LAG.

               

              Example: dxlag-fg5678gh

              
            

            - **awsDevice** *(string) --* 

              The Direct Connection endpoint which the physical connection terminates on.

              
        
      
    

  .. py:method:: describe_direct_connect_gateway_associations(**kwargs)

    

    Returns a list of all direct connect gateway and virtual private gateway (VGW) associations. Either a direct connect gateway ID or a VGW ID must be provided in the request. If a direct connect gateway ID is provided, the response returns all VGWs associated with the direct connect gateway. If a VGW ID is provided, the response returns all direct connect gateways associated with the VGW. If both are provided, the response only returns the association that matches both the direct connect gateway and the VGW.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations>`_    


    **Request Syntax** 
    ::

      response = client.describe_direct_connect_gateway_associations(
          directConnectGatewayId='string',
          virtualGatewayId='string',
          maxResults=123,
          nextToken='string'
      )
    :type directConnectGatewayId: string
    :param directConnectGatewayId: 

      The ID of the direct connect gateway.

       

      Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

       

      Default: None

      

    
    :type virtualGatewayId: string
    :param virtualGatewayId: 

      The ID of the virtual private gateway.

       

      Example: "vgw-abc123ef"

       

      Default: None

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of direct connect gateway associations to return per page.

       

      Example: 15

       

      Default: None

      

    
    :type nextToken: string
    :param nextToken: 

      The token provided in the previous describe result to retrieve the next page of the result.

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'directConnectGatewayAssociations': [
                {
                    'directConnectGatewayId': 'string',
                    'virtualGatewayId': 'string',
                    'virtualGatewayRegion': 'string',
                    'virtualGatewayOwnerAccount': 'string',
                    'associationState': 'associating'|'associated'|'disassociating'|'disassociated',
                    'stateChangeError': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the response from the DescribeDirectConnectGatewayAssociations API call

        
        

        - **directConnectGatewayAssociations** *(list) --* 

          Information about the direct connect gateway associations.

          
          

          - *(dict) --* 

            The association between a direct connect gateway and virtual private gateway.

            
            

            - **directConnectGatewayId** *(string) --* 

              The ID of the direct connect gateway.

               

              Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

              
            

            - **virtualGatewayId** *(string) --* 

              The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

               

              Example: vgw-123er56

              
            

            - **virtualGatewayRegion** *(string) --* 

              The region in which the virtual private gateway is located.

               

              Example: us-east-1

              
            

            - **virtualGatewayOwnerAccount** *(string) --* 

              The AWS account ID of the owner of the virtual private gateway.

              
            

            - **associationState** *(string) --* 

              State of the direct connect gateway association.

               

               
              * **Associating** : The initial state after calling  CreateDirectConnectGatewayAssociation . 
               
              * **Associated** : The direct connect gateway and virtual private gateway are successfully associated and ready to pass traffic. 
               
              * **Disassociating** : The initial state after calling  DeleteDirectConnectGatewayAssociation . 
               
              * **Disassociated** : The virtual private gateway is successfully disassociated from the direct connect gateway. Traffic flow between the direct connect gateway and virtual private gateway stops. 
               

              
            

            - **stateChangeError** *(string) --* 

              Error message when the state of an object fails to advance.

              
        
      
        

        - **nextToken** *(string) --* 

          Token to retrieve the next page of the result.

          
    

  .. py:method:: describe_direct_connect_gateway_attachments(**kwargs)

    

    Returns a list of all direct connect gateway and virtual interface (VIF) attachments. Either a direct connect gateway ID or a VIF ID must be provided in the request. If a direct connect gateway ID is provided, the response returns all VIFs attached to the direct connect gateway. If a VIF ID is provided, the response returns all direct connect gateways attached to the VIF. If both are provided, the response only returns the attachment that matches both the direct connect gateway and the VIF.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments>`_    


    **Request Syntax** 
    ::

      response = client.describe_direct_connect_gateway_attachments(
          directConnectGatewayId='string',
          virtualInterfaceId='string',
          maxResults=123,
          nextToken='string'
      )
    :type directConnectGatewayId: string
    :param directConnectGatewayId: 

      The ID of the direct connect gateway.

       

      Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

       

      Default: None

      

    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: 

      The ID of the virtual interface.

       

      Example: "dxvif-abc123ef"

       

      Default: None

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of direct connect gateway attachments to return per page.

       

      Example: 15

       

      Default: None

      

    
    :type nextToken: string
    :param nextToken: 

      The token provided in the previous describe result to retrieve the next page of the result.

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'directConnectGatewayAttachments': [
                {
                    'directConnectGatewayId': 'string',
                    'virtualInterfaceId': 'string',
                    'virtualInterfaceRegion': 'string',
                    'virtualInterfaceOwnerAccount': 'string',
                    'attachmentState': 'attaching'|'attached'|'detaching'|'detached',
                    'stateChangeError': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the response from the DescribeDirectConnectGatewayAttachments API call

        
        

        - **directConnectGatewayAttachments** *(list) --* 

          Information about the direct connect gateway attachments.

          
          

          - *(dict) --* 

            The association between a direct connect gateway and virtual interface.

            
            

            - **directConnectGatewayId** *(string) --* 

              The ID of the direct connect gateway.

               

              Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

              
            

            - **virtualInterfaceId** *(string) --* 

              The ID of the virtual interface.

               

              Example: dxvif-123dfg56

               

              Default: None

              
            

            - **virtualInterfaceRegion** *(string) --* 

              The region in which the virtual interface is located.

               

              Example: us-east-1

              
            

            - **virtualInterfaceOwnerAccount** *(string) --* 

              The AWS account ID of the owner of the virtual interface.

              
            

            - **attachmentState** *(string) --* 

              State of the direct connect gateway attachment.

               

               
              * **Attaching** : The initial state after a virtual interface is created using the direct connect gateway. 
               
              * **Attached** : The direct connect gateway and virtual interface are successfully attached and ready to pass traffic. 
               
              * **Detaching** : The initial state after calling  DeleteVirtualInterface on a virtual interface that is attached to a direct connect gateway. 
               
              * **Detached** : The virtual interface is successfully detached from the direct connect gateway. Traffic flow between the direct connect gateway and virtual interface stops. 
               

              
            

            - **stateChangeError** *(string) --* 

              Error message when the state of an object fails to advance.

              
        
      
        

        - **nextToken** *(string) --* 

          Token to retrieve the next page of the result.

          
    

  .. py:method:: describe_direct_connect_gateways(**kwargs)

    

    Returns a list of direct connect gateways in your account. Deleted direct connect gateways are not returned. You can provide a direct connect gateway ID in the request to return information about the specific direct connect gateway only. Otherwise, if a direct connect gateway ID is not provided, information about all of your direct connect gateways is returned. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeDirectConnectGateways>`_    


    **Request Syntax** 
    ::

      response = client.describe_direct_connect_gateways(
          directConnectGatewayId='string',
          maxResults=123,
          nextToken='string'
      )
    :type directConnectGatewayId: string
    :param directConnectGatewayId: 

      The ID of the direct connect gateway.

       

      Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

       

      Default: None

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of direct connect gateways to return per page.

       

      Example: 15

       

      Default: None

      

    
    :type nextToken: string
    :param nextToken: 

      The token provided in the previous describe result to retrieve the next page of the result.

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'directConnectGateways': [
                {
                    'directConnectGatewayId': 'string',
                    'directConnectGatewayName': 'string',
                    'amazonSideAsn': 123,
                    'ownerAccount': 'string',
                    'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
                    'stateChangeError': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the response from the DescribeDirectConnectGateways API call

        
        

        - **directConnectGateways** *(list) --* 

          Information about the direct connect gateways.

          
          

          - *(dict) --* 

            A direct connect gateway is an intermediate object that enables you to connect virtual interfaces and virtual private gateways.

            
            

            - **directConnectGatewayId** *(string) --* 

              The ID of the direct connect gateway.

               

              Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

              
            

            - **directConnectGatewayName** *(string) --* 

              The name of the direct connect gateway.

               

              Example: "My direct connect gateway"

               

              Default: None

              
            

            - **amazonSideAsn** *(integer) --* 

              The autonomous system number (ASN) for the Amazon side of the connection.

              
            

            - **ownerAccount** *(string) --* 

              The AWS account ID of the owner of the direct connect gateway.

              
            

            - **directConnectGatewayState** *(string) --* 

              State of the direct connect gateway.

               

               
              * **Pending** : The initial state after calling  CreateDirectConnectGateway . 
               
              * **Available** : The direct connect gateway is ready for use. 
               
              * **Deleting** : The initial state after calling  DeleteDirectConnectGateway . 
               
              * **Deleted** : The direct connect gateway is deleted and cannot pass traffic. 
               

              
            

            - **stateChangeError** *(string) --* 

              Error message when the state of an object fails to advance.

              
        
      
        

        - **nextToken** *(string) --* 

          Token to retrieve the next page of the result.

          
    

  .. py:method:: describe_hosted_connections(**kwargs)

    

    Returns a list of hosted connections that have been provisioned on the given interconnect or link aggregation group (LAG).

     

    .. note::

       

      This is intended for use by AWS Direct Connect partners only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeHostedConnections>`_    


    **Request Syntax** 
    ::

      response = client.describe_hosted_connections(
          connectionId='string'
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the interconnect or LAG on which the hosted connections are provisioned.

       

      Example: dxcon-abc123 or dxlag-abc123

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'connections': [
                {
                    'ownerAccount': 'string',
                    'connectionId': 'string',
                    'connectionName': 'string',
                    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                    'region': 'string',
                    'location': 'string',
                    'bandwidth': 'string',
                    'vlan': 123,
                    'partnerName': 'string',
                    'loaIssueTime': datetime(2015, 1, 1),
                    'lagId': 'string',
                    'awsDevice': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A structure containing a list of connections.

        
        

        - **connections** *(list) --* 

          A list of connections.

          
          

          - *(dict) --* 

            A connection represents the physical network connection between the AWS Direct Connect location and the customer.

            
            

            - **ownerAccount** *(string) --* 

              The AWS account that will own the new connection.

              
            

            - **connectionId** *(string) --* 

              The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

               

              Example: dxcon-fg5678gh

               

              Default: None

              
            

            - **connectionName** *(string) --* 

              The name of the connection.

               

              Example: "*My Connection to AWS* "

               

              Default: None

              
            

            - **connectionState** *(string) --* 

              State of the connection.

               

               
              * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
               
              * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
               
              * **Pending** : The connection has been approved, and is being initialized. 
               
              * **Available** : The network link is up, and the connection is ready for use. 
               
              * **Down** : The network link is down. 
               
              * **Deleting** : The connection is in the process of being deleted. 
               
              * **Deleted** : The connection has been deleted. 
               
              * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
               

              
            

            - **region** *(string) --* 

              The AWS region where the connection is located.

               

              Example: us-east-1

               

              Default: None

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **bandwidth** *(string) --* 

              Bandwidth of the connection.

               

              Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

               

              Default: None

              
            

            - **vlan** *(integer) --* 

              The VLAN ID.

               

              Example: 101

              
            

            - **partnerName** *(string) --* 

              The name of the AWS Direct Connect service provider associated with the connection.

              
            

            - **loaIssueTime** *(datetime) --* 

              The time of the most recent call to  DescribeLoa for this connection.

              
            

            - **lagId** *(string) --* 

              The ID of the LAG.

               

              Example: dxlag-fg5678gh

              
            

            - **awsDevice** *(string) --* 

              The Direct Connection endpoint which the physical connection terminates on.

              
        
      
    

  .. py:method:: describe_interconnect_loa(**kwargs)

    

    Deprecated in favor of  DescribeLoa .

     

    Returns the LOA-CFA for an Interconnect.

     

    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to AWS at the colocation facility. For more information, see `Requesting Cross Connects at AWS Direct Connect Locations <http://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html>`__ in the AWS Direct Connect user guide.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeInterconnectLoa>`_    


    **Request Syntax** 
    ::

      response = client.describe_interconnect_loa(
          interconnectId='string',
          providerName='string',
          loaContentType='application/pdf'
      )
    :type interconnectId: string
    :param interconnectId: **[REQUIRED]** 

      The ID of the interconnect.

       

      Example: dxcon-abc123

      

    
    :type providerName: string
    :param providerName: 

      The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

       

      Default: None

      

    
    :type loaContentType: string
    :param loaContentType: 

      A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is "application/pdf".

       

      Default: application/pdf

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'loa': {
                'loaContent': b'bytes',
                'loaContentType': 'application/pdf'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when DescribeInterconnectLoa is called.

        
        

        - **loa** *(dict) --* 

          A structure containing the Letter of Authorization - Connecting Facility Assignment (LOA-CFA) for a connection.

          
          

          - **loaContent** *(bytes) --* 

            The binary contents of the LOA-CFA document.

            
          

          - **loaContentType** *(string) --* 

            A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is "application/pdf".

             

            Default: application/pdf

            
      
    

  .. py:method:: describe_interconnects(**kwargs)

    

    Returns a list of interconnects owned by the AWS account.

     

    If an interconnect ID is provided, it will only return this particular interconnect.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeInterconnects>`_    


    **Request Syntax** 
    ::

      response = client.describe_interconnects(
          interconnectId='string'
      )
    :type interconnectId: string
    :param interconnectId: 

      The ID of the interconnect.

       

      Example: dxcon-abc123

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'interconnects': [
                {
                    'interconnectId': 'string',
                    'interconnectName': 'string',
                    'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
                    'region': 'string',
                    'location': 'string',
                    'bandwidth': 'string',
                    'loaIssueTime': datetime(2015, 1, 1),
                    'lagId': 'string',
                    'awsDevice': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A structure containing a list of interconnects.

        
        

        - **interconnects** *(list) --* 

          A list of interconnects.

          
          

          - *(dict) --* 

            An interconnect is a connection that can host other connections.

             

            Like a standard AWS Direct Connect connection, an interconnect represents the physical connection between an AWS Direct Connect partner's network and a specific Direct Connect location. An AWS Direct Connect partner who owns an interconnect can provision hosted connections on the interconnect for their end customers, thereby providing the end customers with connectivity to AWS services.

             

            The resources of the interconnect, including bandwidth and VLAN numbers, are shared by all of the hosted connections on the interconnect, and the owner of the interconnect determines how these resources are assigned.

            
            

            - **interconnectId** *(string) --* 

              The ID of the interconnect.

               

              Example: dxcon-abc123

              
            

            - **interconnectName** *(string) --* 

              The name of the interconnect.

               

              Example: "*1G Interconnect to AWS* "

              
            

            - **interconnectState** *(string) --* 

              State of the interconnect.

               

               
              * **Requested** : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
               
              * **Pending** : The interconnect has been approved, and is being initialized. 
               
              * **Available** : The network link is up, and the interconnect is ready for use. 
               
              * **Down** : The network link is down. 
               
              * **Deleting** : The interconnect is in the process of being deleted. 
               
              * **Deleted** : The interconnect has been deleted. 
               

              
            

            - **region** *(string) --* 

              The AWS region where the connection is located.

               

              Example: us-east-1

               

              Default: None

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **bandwidth** *(string) --* 

              Bandwidth of the connection.

               

              Example: 1Gbps

               

              Default: None

              
            

            - **loaIssueTime** *(datetime) --* 

              The time of the most recent call to DescribeInterconnectLoa for this Interconnect.

              
            

            - **lagId** *(string) --* 

              The ID of the LAG.

               

              Example: dxlag-fg5678gh

              
            

            - **awsDevice** *(string) --* 

              The Direct Connection endpoint which the physical connection terminates on.

              
        
      
    

  .. py:method:: describe_lags(**kwargs)

    

    Describes the link aggregation groups (LAGs) in your account. 

     

    If a LAG ID is provided, only information about the specified LAG is returned.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeLags>`_    


    **Request Syntax** 
    ::

      response = client.describe_lags(
          lagId='string'
      )
    :type lagId: string
    :param lagId: 

      The ID of the LAG.

       

      Example: dxlag-abc123

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'lags': [
                {
                    'connectionsBandwidth': 'string',
                    'numberOfConnections': 123,
                    'lagId': 'string',
                    'ownerAccount': 'string',
                    'lagName': 'string',
                    'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
                    'location': 'string',
                    'region': 'string',
                    'minimumLinks': 123,
                    'awsDevice': 'string',
                    'connections': [
                        {
                            'ownerAccount': 'string',
                            'connectionId': 'string',
                            'connectionName': 'string',
                            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                            'region': 'string',
                            'location': 'string',
                            'bandwidth': 'string',
                            'vlan': 123,
                            'partnerName': 'string',
                            'loaIssueTime': datetime(2015, 1, 1),
                            'lagId': 'string',
                            'awsDevice': 'string'
                        },
                    ],
                    'allowsHostedConnections': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A structure containing a list of LAGs.

        
        

        - **lags** *(list) --* 

          A list of LAGs.

          
          

          - *(dict) --* 

            Describes a link aggregation group (LAG). A LAG is a connection that uses the Link Aggregation Control Protocol (LACP) to logically aggregate a bundle of physical connections. Like an interconnect, it can host other connections. All connections in a LAG must terminate on the same physical AWS Direct Connect endpoint, and must be the same bandwidth.

            
            

            - **connectionsBandwidth** *(string) --* 

              The individual bandwidth of the physical connections bundled by the LAG.

               

              Available values: 1Gbps, 10Gbps

              
            

            - **numberOfConnections** *(integer) --* 

              The number of physical connections bundled by the LAG, up to a maximum of 10.

              
            

            - **lagId** *(string) --* 

              The ID of the LAG.

               

              Example: dxlag-fg5678gh

              
            

            - **ownerAccount** *(string) --* 

              The owner of the LAG.

              
            

            - **lagName** *(string) --* 

              The name of the LAG.

              
            

            - **lagState** *(string) --* 

              The state of the LAG.

               

               
              * **Requested** : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available. 
               
              * **Pending** : The LAG has been approved, and is being initialized. 
               
              * **Available** : The network link is established, and the LAG is ready for use. 
               
              * **Down** : The network link is down. 
               
              * **Deleting** : The LAG is in the process of being deleted. 
               
              * **Deleted** : The LAG has been deleted. 
               

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **region** *(string) --* 

              The AWS region where the connection is located.

               

              Example: us-east-1

               

              Default: None

              
            

            - **minimumLinks** *(integer) --* 

              The minimum number of physical connections that must be operational for the LAG itself to be operational. If the number of operational connections drops below this setting, the LAG state changes to ``down`` . This value can help to ensure that a LAG is not overutilized if a significant number of its bundled connections go down.

              
            

            - **awsDevice** *(string) --* 

              The AWS Direct Connection endpoint that hosts the LAG.

              
            

            - **connections** *(list) --* 

              A list of connections bundled by this LAG.

              
              

              - *(dict) --* 

                A connection represents the physical network connection between the AWS Direct Connect location and the customer.

                
                

                - **ownerAccount** *(string) --* 

                  The AWS account that will own the new connection.

                  
                

                - **connectionId** *(string) --* 

                  The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

                   

                  Example: dxcon-fg5678gh

                   

                  Default: None

                  
                

                - **connectionName** *(string) --* 

                  The name of the connection.

                   

                  Example: "*My Connection to AWS* "

                   

                  Default: None

                  
                

                - **connectionState** *(string) --* 

                  State of the connection.

                   

                   
                  * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
                   
                  * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
                   
                  * **Pending** : The connection has been approved, and is being initialized. 
                   
                  * **Available** : The network link is up, and the connection is ready for use. 
                   
                  * **Down** : The network link is down. 
                   
                  * **Deleting** : The connection is in the process of being deleted. 
                   
                  * **Deleted** : The connection has been deleted. 
                   
                  * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
                   

                  
                

                - **region** *(string) --* 

                  The AWS region where the connection is located.

                   

                  Example: us-east-1

                   

                  Default: None

                  
                

                - **location** *(string) --* 

                  Where the connection is located.

                   

                  Example: EqSV5

                   

                  Default: None

                  
                

                - **bandwidth** *(string) --* 

                  Bandwidth of the connection.

                   

                  Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

                   

                  Default: None

                  
                

                - **vlan** *(integer) --* 

                  The VLAN ID.

                   

                  Example: 101

                  
                

                - **partnerName** *(string) --* 

                  The name of the AWS Direct Connect service provider associated with the connection.

                  
                

                - **loaIssueTime** *(datetime) --* 

                  The time of the most recent call to  DescribeLoa for this connection.

                  
                

                - **lagId** *(string) --* 

                  The ID of the LAG.

                   

                  Example: dxlag-fg5678gh

                  
                

                - **awsDevice** *(string) --* 

                  The Direct Connection endpoint which the physical connection terminates on.

                  
            
          
            

            - **allowsHostedConnections** *(boolean) --* 

              Indicates whether the LAG can host other connections.

               

              .. note::

                 

                This is intended for use by AWS Direct Connect partners only.

                 

              
        
      
    

  .. py:method:: describe_loa(**kwargs)

    

    Returns the LOA-CFA for a connection, interconnect, or link aggregation group (LAG).

     

    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to AWS at the colocation facility. For more information, see `Requesting Cross Connects at AWS Direct Connect Locations <http://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html>`__ in the AWS Direct Connect user guide.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeLoa>`_    


    **Request Syntax** 
    ::

      response = client.describe_loa(
          connectionId='string',
          providerName='string',
          loaContentType='application/pdf'
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of a connection, LAG, or interconnect for which to get the LOA-CFA information.

       

      Example: dxcon-abc123 or dxlag-abc123

       

      Default: None

      

    
    :type providerName: string
    :param providerName: 

      The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

       

      Default: None

      

    
    :type loaContentType: string
    :param loaContentType: 

      A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is "application/pdf".

       

      Default: application/pdf

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'loaContent': b'bytes',
            'loaContentType': 'application/pdf'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A structure containing the Letter of Authorization - Connecting Facility Assignment (LOA-CFA) for a connection.

        
        

        - **loaContent** *(bytes) --* 

          The binary contents of the LOA-CFA document.

          
        

        - **loaContentType** *(string) --* 

          A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is "application/pdf".

           

          Default: application/pdf

          
    

  .. py:method:: describe_locations()

    

    Returns the list of AWS Direct Connect locations in the current AWS region. These are the locations that may be selected when calling  CreateConnection or  CreateInterconnect .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeLocations>`_    


    **Request Syntax** 

    ::

      response = client.describe_locations()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'locations': [
                {
                    'locationCode': 'string',
                    'locationName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A location is a network facility where AWS Direct Connect routers are available to be connected. Generally, these are colocation hubs where many network providers have equipment, and where cross connects can be delivered. Locations include a name and facility code, and must be provided when creating a connection.

        
        

        - **locations** *(list) --* 

          A list of colocation hubs where network providers have equipment. Most regions have multiple locations available.

          
          

          - *(dict) --* 

            An AWS Direct Connect location where connections and interconnects can be requested.

            
            

            - **locationCode** *(string) --* 

              The code used to indicate the AWS Direct Connect location.

              
            

            - **locationName** *(string) --* 

              The name of the AWS Direct Connect location. The name includes the colocation partner name and the physical site of the lit building.

              
        
      
    

  .. py:method:: describe_tags(**kwargs)

    

    Describes the tags associated with the specified Direct Connect resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeTags>`_    


    **Request Syntax** 
    ::

      response = client.describe_tags(
          resourceArns=[
              'string',
          ]
      )
    :type resourceArns: list
    :param resourceArns: **[REQUIRED]** 

      The Amazon Resource Names (ARNs) of the Direct Connect resources.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resourceTags': [
                {
                    'resourceArn': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when DescribeTags is called.

        
        

        - **resourceTags** *(list) --* 

          Information about the tags.

          
          

          - *(dict) --* 

            The tags associated with a Direct Connect resource.

            
            

            - **resourceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Direct Connect resource.

              
            

            - **tags** *(list) --* 

              The tags.

              
              

              - *(dict) --* 

                Information about a tag.

                
                

                - **key** *(string) --* 

                  The key of the tag.

                  
                

                - **value** *(string) --* 

                  The value of the tag.

                  
            
          
        
      
    

  .. py:method:: describe_virtual_gateways()

    

    Returns a list of virtual private gateways owned by the AWS account.

     

    You can create one or more AWS Direct Connect private virtual interfaces linking to a virtual private gateway. A virtual private gateway can be managed via Amazon Virtual Private Cloud (VPC) console or the `EC2 CreateVpnGateway <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-CreateVpnGateway.html>`__ action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeVirtualGateways>`_    


    **Request Syntax** 

    ::

      response = client.describe_virtual_gateways()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'virtualGateways': [
                {
                    'virtualGatewayId': 'string',
                    'virtualGatewayState': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A structure containing a list of virtual private gateways.

        
        

        - **virtualGateways** *(list) --* 

          A list of virtual private gateways.

          
          

          - *(dict) --* 

            You can create one or more AWS Direct Connect private virtual interfaces linking to your virtual private gateway.

             

            Virtual private gateways can be managed using the Amazon Virtual Private Cloud (Amazon VPC) console or the `Amazon EC2 CreateVpnGateway action <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-CreateVpnGateway.html>`__ .

            
            

            - **virtualGatewayId** *(string) --* 

              The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

               

              Example: vgw-123er56

              
            

            - **virtualGatewayState** *(string) --* 

              State of the virtual private gateway.

               

               
              * **Pending** : This is the initial state after calling *CreateVpnGateway* . 
               
              * **Available** : Ready for use by a private virtual interface. 
               
              * **Deleting** : This is the initial state after calling *DeleteVpnGateway* . 
               
              * **Deleted** : In this state, a private virtual interface is unable to send traffic over this gateway. 
               

              
        
      
    

  .. py:method:: describe_virtual_interfaces(**kwargs)

    

    Displays all virtual interfaces for an AWS account. Virtual interfaces deleted fewer than 15 minutes before you make the request are also returned. If you specify a connection ID, only the virtual interfaces associated with the connection are returned. If you specify a virtual interface ID, then only a single virtual interface is returned.

     

    A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeVirtualInterfaces>`_    


    **Request Syntax** 
    ::

      response = client.describe_virtual_interfaces(
          connectionId='string',
          virtualInterfaceId='string'
      )
    :type connectionId: string
    :param connectionId: 

      The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

       

      Example: dxcon-fg5678gh

       

      Default: None

      

    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: 

      The ID of the virtual interface.

       

      Example: dxvif-123dfg56

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'virtualInterfaces': [
                {
                    'ownerAccount': 'string',
                    'virtualInterfaceId': 'string',
                    'location': 'string',
                    'connectionId': 'string',
                    'virtualInterfaceType': 'string',
                    'virtualInterfaceName': 'string',
                    'vlan': 123,
                    'asn': 123,
                    'amazonSideAsn': 123,
                    'authKey': 'string',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                    'customerRouterConfig': 'string',
                    'virtualGatewayId': 'string',
                    'directConnectGatewayId': 'string',
                    'routeFilterPrefixes': [
                        {
                            'cidr': 'string'
                        },
                    ],
                    'bgpPeers': [
                        {
                            'asn': 123,
                            'authKey': 'string',
                            'addressFamily': 'ipv4'|'ipv6',
                            'amazonAddress': 'string',
                            'customerAddress': 'string',
                            'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                            'bgpStatus': 'up'|'down'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A structure containing a list of virtual interfaces.

        
        

        - **virtualInterfaces** *(list) --* 

          A list of virtual interfaces.

          
          

          - *(dict) --* 

            A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.

            
            

            - **ownerAccount** *(string) --* 

              The AWS account that will own the new virtual interface.

              
            

            - **virtualInterfaceId** *(string) --* 

              The ID of the virtual interface.

               

              Example: dxvif-123dfg56

               

              Default: None

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **connectionId** *(string) --* 

              The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

               

              Example: dxcon-fg5678gh

               

              Default: None

              
            

            - **virtualInterfaceType** *(string) --* 

              The type of virtual interface.

               

              Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so on.)

              
            

            - **virtualInterfaceName** *(string) --* 

              The name of the virtual interface assigned by the customer.

               

              Example: "My VPC"

              
            

            - **vlan** *(integer) --* 

              The VLAN ID.

               

              Example: 101

              
            

            - **asn** *(integer) --* 

              The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

               

              Example: 65000

              
            

            - **amazonSideAsn** *(integer) --* 

              The autonomous system number (ASN) for the Amazon side of the connection.

              
            

            - **authKey** *(string) --* 

              The authentication key for BGP configuration.

               

              Example: asdf34example

              
            

            - **amazonAddress** *(string) --* 

              IP address assigned to the Amazon interface.

               

              Example: 192.168.1.1/30 or 2001:db8::1/125

              
            

            - **customerAddress** *(string) --* 

              IP address assigned to the customer interface.

               

              Example: 192.168.1.2/30 or 2001:db8::2/125

              
            

            - **addressFamily** *(string) --* 

              Indicates the address family for the BGP peer.

               

               
              * **ipv4** : IPv4 address family 
               
              * **ipv6** : IPv6 address family 
               

              
            

            - **virtualInterfaceState** *(string) --* 

              State of the virtual interface.

               

               
              * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner. 
               
              * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created. 
               
              * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic. 
               
              * **Available** : A virtual interface that is able to forward traffic. 
               
              * **Down** : A virtual interface that is BGP down. 
               
              * **Deleting** : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic. 
               
              * **Deleted** : A virtual interface that cannot forward traffic. 
               
              * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state. 
               

              
            

            - **customerRouterConfig** *(string) --* 

              Information for generating the customer router configuration.

              
            

            - **virtualGatewayId** *(string) --* 

              The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.

               

              Example: vgw-123er56

              
            

            - **directConnectGatewayId** *(string) --* 

              The ID of the direct connect gateway.

               

              Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

              
            

            - **routeFilterPrefixes** *(list) --* 

              A list of routes to be advertised to the AWS network in this region (public virtual interface).

              
              

              - *(dict) --* 

                A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

                
                

                - **cidr** *(string) --* 

                  CIDR notation for the advertised route. Multiple routes are separated by commas.

                   

                  IPv6 CIDRs must be at least a /64 or shorter

                   

                  Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64

                  
            
          
            

            - **bgpPeers** *(list) --* 

              A list of the BGP peers configured on this virtual interface.

              
              

              - *(dict) --* 

                A structure containing information about a BGP peer.

                
                

                - **asn** *(integer) --* 

                  The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

                   

                  Example: 65000

                  
                

                - **authKey** *(string) --* 

                  The authentication key for BGP configuration.

                   

                  Example: asdf34example

                  
                

                - **addressFamily** *(string) --* 

                  Indicates the address family for the BGP peer.

                   

                   
                  * **ipv4** : IPv4 address family 
                   
                  * **ipv6** : IPv6 address family 
                   

                  
                

                - **amazonAddress** *(string) --* 

                  IP address assigned to the Amazon interface.

                   

                  Example: 192.168.1.1/30 or 2001:db8::1/125

                  
                

                - **customerAddress** *(string) --* 

                  IP address assigned to the customer interface.

                   

                  Example: 192.168.1.2/30 or 2001:db8::2/125

                  
                

                - **bgpPeerState** *(string) --* 

                  The state of the BGP peer.

                   

                   
                  * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.  
                   
                  * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established. 
                   
                  * **Available** : The BGP peer can be established. 
                   
                  * **Deleting** : The BGP peer is in the process of being deleted. 
                   
                  * **Deleted** : The BGP peer has been deleted and cannot be established. 
                   

                  
                

                - **bgpStatus** *(string) --* 

                  The Up/Down state of the BGP peer.

                   

                   
                  * **Up** : The BGP peer is established. 
                   
                  * **Down** : The BGP peer is down. 
                   

                  
            
          
        
      
    

  .. py:method:: disassociate_connection_from_lag(**kwargs)

    

    Disassociates a connection from a link aggregation group (LAG). The connection is interrupted and re-established as a standalone connection (the connection is not deleted; to delete the connection, use the  DeleteConnection request). If the LAG has associated virtual interfaces or hosted connections, they remain associated with the LAG. A disassociated connection owned by an AWS Direct Connect partner is automatically converted to an interconnect.

     

    If disassociating the connection will cause the LAG to fall below its setting for minimum number of operational connections, the request fails, except when it's the last member of the LAG. If all connections are disassociated, the LAG continues to exist as an empty LAG with no physical connections. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DisassociateConnectionFromLag>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_connection_from_lag(
          connectionId='string',
          lagId='string'
      )
    :type connectionId: string
    :param connectionId: **[REQUIRED]** 

      The ID of the connection to disassociate from the LAG.

       

      Example: dxcon-abc123

       

      Default: None

      

    
    :type lagId: string
    :param lagId: **[REQUIRED]** 

      The ID of the LAG.

       

      Example: dxlag-abc123

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A connection represents the physical network connection between the AWS Direct Connect location and the customer.

        
        

        - **ownerAccount** *(string) --* 

          The AWS account that will own the new connection.

          
        

        - **connectionId** *(string) --* 

          The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

           

          Example: dxcon-fg5678gh

           

          Default: None

          
        

        - **connectionName** *(string) --* 

          The name of the connection.

           

          Example: "*My Connection to AWS* "

           

          Default: None

          
        

        - **connectionState** *(string) --* 

          State of the connection.

           

           
          * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
           
          * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
           
          * **Pending** : The connection has been approved, and is being initialized. 
           
          * **Available** : The network link is up, and the connection is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The connection is in the process of being deleted. 
           
          * **Deleted** : The connection has been deleted. 
           
          * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
           

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **bandwidth** *(string) --* 

          Bandwidth of the connection.

           

          Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

           

          Default: None

          
        

        - **vlan** *(integer) --* 

          The VLAN ID.

           

          Example: 101

          
        

        - **partnerName** *(string) --* 

          The name of the AWS Direct Connect service provider associated with the connection.

          
        

        - **loaIssueTime** *(datetime) --* 

          The time of the most recent call to  DescribeLoa for this connection.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **awsDevice** *(string) --* 

          The Direct Connection endpoint which the physical connection terminates on.

          
    

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

        


  .. py:method:: tag_resource(**kwargs)

    

    Adds the specified tags to the specified Direct Connect resource. Each Direct Connect resource can have a maximum of 50 tags.

     

    Each tag consists of a key and an optional value. If a tag with the same key is already associated with the Direct Connect resource, this action updates its value.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/TagResource>`_    


    **Request Syntax** 
    ::

      response = client.tag_resource(
          resourceArn='string',
          tags=[
              {
                  'key': 'string',
                  'value': 'string'
              },
          ]
      )
    :type resourceArn: string
    :param resourceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the Direct Connect resource.

       

      Example: arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-fg5678gh

      

    
    :type tags: list
    :param tags: **[REQUIRED]** 

      The list of tags to add.

      

    
      - *(dict) --* 

        Information about a tag.

        

      
        - **key** *(string) --* **[REQUIRED]** 

          The key of the tag.

          

        
        - **value** *(string) --* 

          The value of the tag.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The response received when TagResource is called.

        
    

  .. py:method:: untag_resource(**kwargs)

    

    Removes one or more tags from the specified Direct Connect resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/UntagResource>`_    


    **Request Syntax** 
    ::

      response = client.untag_resource(
          resourceArn='string',
          tagKeys=[
              'string',
          ]
      )
    :type resourceArn: string
    :param resourceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the Direct Connect resource.

      

    
    :type tagKeys: list
    :param tagKeys: **[REQUIRED]** 

      The list of tag keys to remove.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The response received when UntagResource is called.

        
    

  .. py:method:: update_lag(**kwargs)

    

    Updates the attributes of a link aggregation group (LAG). 

     

    You can update the following attributes: 

     

     
    * The name of the LAG. 
     
    * The value for the minimum number of connections that must be operational for the LAG itself to be operational.  
     

     

    When you create a LAG, the default value for the minimum number of operational connections is zero (0). If you update this value, and the number of operational connections falls below the specified value, the LAG will automatically go down to avoid overutilization of the remaining connections. Adjusting this value should be done with care as it could force the LAG down if the value is set higher than the current number of operational connections.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/UpdateLag>`_    


    **Request Syntax** 
    ::

      response = client.update_lag(
          lagId='string',
          lagName='string',
          minimumLinks=123
      )
    :type lagId: string
    :param lagId: **[REQUIRED]** 

      The ID of the LAG to update.

       

      Example: dxlag-abc123

       

      Default: None

      

    
    :type lagName: string
    :param lagName: 

      The name for the LAG.

       

      Example: "``3x10G LAG to AWS`` "

       

      Default: None

      

    
    :type minimumLinks: integer
    :param minimumLinks: 

      The minimum number of physical connections that must be operational for the LAG itself to be operational.

       

      Default: None

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'connectionsBandwidth': 'string',
            'numberOfConnections': 123,
            'lagId': 'string',
            'ownerAccount': 'string',
            'lagName': 'string',
            'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
            'location': 'string',
            'region': 'string',
            'minimumLinks': 123,
            'awsDevice': 'string',
            'connections': [
                {
                    'ownerAccount': 'string',
                    'connectionId': 'string',
                    'connectionName': 'string',
                    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                    'region': 'string',
                    'location': 'string',
                    'bandwidth': 'string',
                    'vlan': 123,
                    'partnerName': 'string',
                    'loaIssueTime': datetime(2015, 1, 1),
                    'lagId': 'string',
                    'awsDevice': 'string'
                },
            ],
            'allowsHostedConnections': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Describes a link aggregation group (LAG). A LAG is a connection that uses the Link Aggregation Control Protocol (LACP) to logically aggregate a bundle of physical connections. Like an interconnect, it can host other connections. All connections in a LAG must terminate on the same physical AWS Direct Connect endpoint, and must be the same bandwidth.

        
        

        - **connectionsBandwidth** *(string) --* 

          The individual bandwidth of the physical connections bundled by the LAG.

           

          Available values: 1Gbps, 10Gbps

          
        

        - **numberOfConnections** *(integer) --* 

          The number of physical connections bundled by the LAG, up to a maximum of 10.

          
        

        - **lagId** *(string) --* 

          The ID of the LAG.

           

          Example: dxlag-fg5678gh

          
        

        - **ownerAccount** *(string) --* 

          The owner of the LAG.

          
        

        - **lagName** *(string) --* 

          The name of the LAG.

          
        

        - **lagState** *(string) --* 

          The state of the LAG.

           

           
          * **Requested** : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available. 
           
          * **Pending** : The LAG has been approved, and is being initialized. 
           
          * **Available** : The network link is established, and the LAG is ready for use. 
           
          * **Down** : The network link is down. 
           
          * **Deleting** : The LAG is in the process of being deleted. 
           
          * **Deleted** : The LAG has been deleted. 
           

          
        

        - **location** *(string) --* 

          Where the connection is located.

           

          Example: EqSV5

           

          Default: None

          
        

        - **region** *(string) --* 

          The AWS region where the connection is located.

           

          Example: us-east-1

           

          Default: None

          
        

        - **minimumLinks** *(integer) --* 

          The minimum number of physical connections that must be operational for the LAG itself to be operational. If the number of operational connections drops below this setting, the LAG state changes to ``down`` . This value can help to ensure that a LAG is not overutilized if a significant number of its bundled connections go down.

          
        

        - **awsDevice** *(string) --* 

          The AWS Direct Connection endpoint that hosts the LAG.

          
        

        - **connections** *(list) --* 

          A list of connections bundled by this LAG.

          
          

          - *(dict) --* 

            A connection represents the physical network connection between the AWS Direct Connect location and the customer.

            
            

            - **ownerAccount** *(string) --* 

              The AWS account that will own the new connection.

              
            

            - **connectionId** *(string) --* 

              The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).

               

              Example: dxcon-fg5678gh

               

              Default: None

              
            

            - **connectionName** *(string) --* 

              The name of the connection.

               

              Example: "*My Connection to AWS* "

               

              Default: None

              
            

            - **connectionState** *(string) --* 

              State of the connection.

               

               
              * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order. 
               
              * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer. 
               
              * **Pending** : The connection has been approved, and is being initialized. 
               
              * **Available** : The network link is up, and the connection is ready for use. 
               
              * **Down** : The network link is down. 
               
              * **Deleting** : The connection is in the process of being deleted. 
               
              * **Deleted** : The connection has been deleted. 
               
              * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer. 
               

              
            

            - **region** *(string) --* 

              The AWS region where the connection is located.

               

              Example: us-east-1

               

              Default: None

              
            

            - **location** *(string) --* 

              Where the connection is located.

               

              Example: EqSV5

               

              Default: None

              
            

            - **bandwidth** *(string) --* 

              Bandwidth of the connection.

               

              Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)

               

              Default: None

              
            

            - **vlan** *(integer) --* 

              The VLAN ID.

               

              Example: 101

              
            

            - **partnerName** *(string) --* 

              The name of the AWS Direct Connect service provider associated with the connection.

              
            

            - **loaIssueTime** *(datetime) --* 

              The time of the most recent call to  DescribeLoa for this connection.

              
            

            - **lagId** *(string) --* 

              The ID of the LAG.

               

              Example: dxlag-fg5678gh

              
            

            - **awsDevice** *(string) --* 

              The Direct Connection endpoint which the physical connection terminates on.

              
        
      
        

        - **allowsHostedConnections** *(boolean) --* 

          Indicates whether the LAG can host other connections.

           

          .. note::

             

            This is intended for use by AWS Direct Connect partners only.

             

          
    

==========
Paginators
==========


The available paginators are:
