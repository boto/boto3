

**********************
ElasticLoadBalancingv2
**********************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ElasticLoadBalancingv2.Client

  A low-level client representing Elastic Load Balancing (Elastic Load Balancing v2)::

    
    import boto3
    
    client = boto3.client('elbv2')

  
  These are the available methods:
  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.add_listener_certificates`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.add_tags`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.can_paginate`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.create_listener`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.create_load_balancer`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.create_rule`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.create_target_group`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.delete_listener`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.delete_load_balancer`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.delete_rule`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.delete_target_group`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.deregister_targets`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_account_limits`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_listener_certificates`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_listeners`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_load_balancer_attributes`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_load_balancers`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_rules`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_ssl_policies`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_tags`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_target_group_attributes`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_target_groups`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.describe_target_health`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.generate_presigned_url`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.get_paginator`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.get_waiter`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.modify_listener`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.modify_load_balancer_attributes`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.modify_rule`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.modify_target_group`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.modify_target_group_attributes`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.register_targets`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.remove_listener_certificates`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.remove_tags`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.set_ip_address_type`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.set_rule_priorities`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.set_security_groups`

  
  *   :py:meth:`~ElasticLoadBalancingv2.Client.set_subnets`

  

  .. py:method:: add_listener_certificates(**kwargs)

    

    Adds the specified certificate to the specified secure listener.

     

    If the certificate was already added, the call is successful but the certificate is not added again.

     

    To list the certificates for your listener, use  DescribeListenerCertificates . To remove certificates from your listener, use  RemoveListenerCertificates .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/AddListenerCertificates>`_    


    **Request Syntax** 
    ::

      response = client.add_listener_certificates(
          ListenerArn='string',
          Certificates=[
              {
                  'CertificateArn': 'string',
                  'IsDefault': True|False
              },
          ]
      )
    :type ListenerArn: string
    :param ListenerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the listener.

      

    
    :type Certificates: list
    :param Certificates: **[REQUIRED]** 

      The certificate to add. You can specify one certificate per call.

      

    
      - *(dict) --* 

        Information about an SSL server certificate.

        

      
        - **CertificateArn** *(string) --* 

          The Amazon Resource Name (ARN) of the certificate.

          

        
        - **IsDefault** *(boolean) --* 

          Indicates whether the certificate is the default certificate.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Certificates': [
                {
                    'CertificateArn': 'string',
                    'IsDefault': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Certificates** *(list) --* 

          Information about the certificates.

          
          

          - *(dict) --* 

            Information about an SSL server certificate.

            
            

            - **CertificateArn** *(string) --* 

              The Amazon Resource Name (ARN) of the certificate.

              
            

            - **IsDefault** *(boolean) --* 

              Indicates whether the certificate is the default certificate.

              
        
      
    

  .. py:method:: add_tags(**kwargs)

    

    Adds the specified tags to the specified Elastic Load Balancing resource. You can tag your Application Load Balancers, Network Load Balancers, and your target groups.

     

    Each tag consists of a key and an optional value. If a resource already has a tag with the same key, ``AddTags`` updates its value.

     

    To list the current tags for your resources, use  DescribeTags . To remove tags from your resources, use  RemoveTags .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/AddTags>`_    


    **Request Syntax** 
    ::

      response = client.add_tags(
          ResourceArns=[
              'string',
          ],
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ResourceArns: list
    :param ResourceArns: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resource.

      

    
      - *(string) --* 

      
  
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      The tags. Each resource can have a maximum of 10 tags.

      

    
      - *(dict) --* 

        Information about a tag.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of the tag.

          

        
        - **Value** *(string) --* 

          The value of the tag.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example adds the specified tags to the specified load balancer.
    ::

      response = client.add_tags(
          ResourceArns=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
          ],
          Tags=[
              {
                  'Key': 'project',
                  'Value': 'lima',
              },
              {
                  'Key': 'department',
                  'Value': 'digital-media',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

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


  .. py:method:: create_listener(**kwargs)

    

    Creates a listener for the specified Application Load Balancer or Network Load Balancer.

     

    To update a listener, use  ModifyListener . When you are finished with a listener, you can delete it using  DeleteListener . If you are finished with both the listener and the load balancer, you can delete them both using  DeleteLoadBalancer .

     

    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.

     

    For more information, see `Listeners for Your Application Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html>`__ in the *Application Load Balancers Guide* and `Listeners for Your Network Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html>`__ in the *Network Load Balancers Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateListener>`_    


    **Request Syntax** 
    ::

      response = client.create_listener(
          LoadBalancerArn='string',
          Protocol='HTTP'|'HTTPS'|'TCP',
          Port=123,
          SslPolicy='string',
          Certificates=[
              {
                  'CertificateArn': 'string',
                  'IsDefault': True|False
              },
          ],
          DefaultActions=[
              {
                  'Type': 'forward',
                  'TargetGroupArn': 'string'
              },
          ]
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type Protocol: string
    :param Protocol: **[REQUIRED]** 

      The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocol is TCP.

      

    
    :type Port: integer
    :param Port: **[REQUIRED]** 

      The port on which the load balancer is listening.

      

    
    :type SslPolicy: string
    :param SslPolicy: 

      [HTTPS listeners] The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.

      

    
    :type Certificates: list
    :param Certificates: 

      [HTTPS listeners] The SSL server certificate. You must provide exactly one certificate.

      

    
      - *(dict) --* 

        Information about an SSL server certificate.

        

      
        - **CertificateArn** *(string) --* 

          The Amazon Resource Name (ARN) of the certificate.

          

        
        - **IsDefault** *(boolean) --* 

          Indicates whether the certificate is the default certificate.

          

        
      
  
    :type DefaultActions: list
    :param DefaultActions: **[REQUIRED]** 

      The default action for the listener. For Application Load Balancers, the protocol of the specified target group must be HTTP or HTTPS. For Network Load Balancers, the protocol of the specified target group must be TCP.

      

    
      - *(dict) --* 

        Information about an action.

        

      
        - **Type** *(string) --* **[REQUIRED]** 

          The type of action.

          

        
        - **TargetGroupArn** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the target group.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Listeners': [
                {
                    'ListenerArn': 'string',
                    'LoadBalancerArn': 'string',
                    'Port': 123,
                    'Protocol': 'HTTP'|'HTTPS'|'TCP',
                    'Certificates': [
                        {
                            'CertificateArn': 'string',
                            'IsDefault': True|False
                        },
                    ],
                    'SslPolicy': 'string',
                    'DefaultActions': [
                        {
                            'Type': 'forward',
                            'TargetGroupArn': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Listeners** *(list) --* 

          Information about the listener.

          
          

          - *(dict) --* 

            Information about a listener.

            
            

            - **ListenerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the listener.

              
            

            - **LoadBalancerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the load balancer.

              
            

            - **Port** *(integer) --* 

              The port on which the load balancer is listening.

              
            

            - **Protocol** *(string) --* 

              The protocol for connections from clients to the load balancer.

              
            

            - **Certificates** *(list) --* 

              The SSL server certificate. You must provide a certificate if the protocol is HTTPS.

              
              

              - *(dict) --* 

                Information about an SSL server certificate.

                
                

                - **CertificateArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the certificate.

                  
                

                - **IsDefault** *(boolean) --* 

                  Indicates whether the certificate is the default certificate.

                  
            
          
            

            - **SslPolicy** *(string) --* 

              The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.

              
            

            - **DefaultActions** *(list) --* 

              The default actions for the listener.

              
              

              - *(dict) --* 

                Information about an action.

                
                

                - **Type** *(string) --* 

                  The type of action.

                  
                

                - **TargetGroupArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the target group.

                  
            
          
        
      
    

    **Examples** 

    This example creates an HTTP listener for the specified load balancer that forwards requests to the specified target group.
    ::

      response = client.create_listener(
          DefaultActions=[
              {
                  'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                  'Type': 'forward',
              },
          ],
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
          Port=80,
          Protocol='HTTP',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Listeners': [
              {
                  'DefaultActions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                          'Type': 'forward',
                      },
                  ],
                  'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
                  'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  'Port': 80,
                  'Protocol': 'HTTP',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example creates an HTTPS listener for the specified load balancer that forwards requests to the specified target group. Note that you must specify an SSL certificate for an HTTPS listener. You can create and manage certificates using AWS Certificate Manager (ACM). Alternatively, you can create a certificate using SSL/TLS tools, get the certificate signed by a certificate authority (CA), and upload the certificate to AWS Identity and Access Management (IAM).
    ::

      response = client.create_listener(
          Certificates=[
              {
                  'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-server-cert',
              },
          ],
          DefaultActions=[
              {
                  'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                  'Type': 'forward',
              },
          ],
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
          Port=443,
          Protocol='HTTPS',
          SslPolicy='ELBSecurityPolicy-2015-05',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Listeners': [
              {
                  'Certificates': [
                      {
                          'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-server-cert',
                      },
                  ],
                  'DefaultActions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                          'Type': 'forward',
                      },
                  ],
                  'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
                  'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  'Port': 443,
                  'Protocol': 'HTTPS',
                  'SslPolicy': 'ELBSecurityPolicy-2015-05',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_load_balancer(**kwargs)

    

    Creates an Application Load Balancer or a Network Load Balancer.

     

    When you create a load balancer, you can specify security groups, subnets, IP address type, and tags. Otherwise, you could do so later using  SetSecurityGroups ,  SetSubnets ,  SetIpAddressType , and  AddTags .

     

    To create listeners for your load balancer, use  CreateListener . To describe your current load balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete it using  DeleteLoadBalancer .

     

    For limit information, see `Limits for Your Application Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html>`__ in the *Application Load Balancers Guide* and `Limits for Your Network Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html>`__ in the *Network Load Balancers Guide* .

     

    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple load balancers with the same settings, each call succeeds.

     

    For more information, see `Application Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html>`__ in the *Application Load Balancers Guide* and `Network Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html>`__ in the *Network Load Balancers Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.create_load_balancer(
          Name='string',
          Subnets=[
              'string',
          ],
          SubnetMappings=[
              {
                  'SubnetId': 'string',
                  'AllocationId': 'string'
              },
          ],
          SecurityGroups=[
              'string',
          ],
          Scheme='internet-facing'|'internal',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          Type='application'|'network',
          IpAddressType='ipv4'|'dualstack'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the load balancer.

       

      This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.

      

    
    :type Subnets: list
    :param Subnets: 

      The IDs of the subnets to attach to the load balancer. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.

       

      [Application Load Balancers] You must specify subnets from at least two Availability Zones.

       

      [Network Load Balancers] You can specify subnets from one or more Availability Zones.

      

    
      - *(string) --* 

      
  
    :type SubnetMappings: list
    :param SubnetMappings: 

      The IDs of the subnets to attach to the load balancer. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.

       

      [Application Load Balancers] You must specify subnets from at least two Availability Zones. You cannot specify Elastic IP addresses for your subnets.

       

      [Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet.

      

    
      - *(dict) --* 

        Information about a subnet mapping.

        

      
        - **SubnetId** *(string) --* 

          The ID of the subnet.

          

        
        - **AllocationId** *(string) --* 

          [Network Load Balancers] The allocation ID of the Elastic IP address.

          

        
      
  
    :type SecurityGroups: list
    :param SecurityGroups: 

      [Application Load Balancers] The IDs of the security groups to assign to the load balancer.

      

    
      - *(string) --* 

      
  
    :type Scheme: string
    :param Scheme: 

      The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the Internet.

       

      The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.

       

      The default is an Internet-facing load balancer.

      

    
    :type Tags: list
    :param Tags: 

      One or more tags to assign to the load balancer.

      

    
      - *(dict) --* 

        Information about a tag.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of the tag.

          

        
        - **Value** *(string) --* 

          The value of the tag.

          

        
      
  
    :type Type: string
    :param Type: 

      The type of load balancer to create. The default is ``application`` .

      

    
    :type IpAddressType: string
    :param IpAddressType: 

      [Application Load Balancers] The type of IP addresses used by the subnets for your load balancer. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses). Internal load balancers must use ``ipv4`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LoadBalancers': [
                {
                    'LoadBalancerArn': 'string',
                    'DNSName': 'string',
                    'CanonicalHostedZoneId': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'LoadBalancerName': 'string',
                    'Scheme': 'internet-facing'|'internal',
                    'VpcId': 'string',
                    'State': {
                        'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                        'Reason': 'string'
                    },
                    'Type': 'application'|'network',
                    'AvailabilityZones': [
                        {
                            'ZoneName': 'string',
                            'SubnetId': 'string',
                            'LoadBalancerAddresses': [
                                {
                                    'IpAddress': 'string',
                                    'AllocationId': 'string'
                                },
                            ]
                        },
                    ],
                    'SecurityGroups': [
                        'string',
                    ],
                    'IpAddressType': 'ipv4'|'dualstack'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LoadBalancers** *(list) --* 

          Information about the load balancer.

          
          

          - *(dict) --* 

            Information about a load balancer.

            
            

            - **LoadBalancerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the load balancer.

              
            

            - **DNSName** *(string) --* 

              The public DNS name of the load balancer.

              
            

            - **CanonicalHostedZoneId** *(string) --* 

              The ID of the Amazon Route 53 hosted zone associated with the load balancer.

              
            

            - **CreatedTime** *(datetime) --* 

              The date and time the load balancer was created.

              
            

            - **LoadBalancerName** *(string) --* 

              The name of the load balancer.

              
            

            - **Scheme** *(string) --* 

              The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the Internet.

               

              The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.

              
            

            - **VpcId** *(string) --* 

              The ID of the VPC for the load balancer.

              
            

            - **State** *(dict) --* 

              The state of the load balancer.

              
              

              - **Code** *(string) --* 

                The state code. The initial state of the load balancer is ``provisioning`` . After the load balancer is fully set up and ready to route traffic, its state is ``active`` . If the load balancer could not be set up, its state is ``failed`` .

                
              

              - **Reason** *(string) --* 

                A description of the state.

                
          
            

            - **Type** *(string) --* 

              The type of load balancer.

              
            

            - **AvailabilityZones** *(list) --* 

              The Availability Zones for the load balancer.

              
              

              - *(dict) --* 

                Information about an Availability Zone.

                
                

                - **ZoneName** *(string) --* 

                  The name of the Availability Zone.

                  
                

                - **SubnetId** *(string) --* 

                  The ID of the subnet.

                  
                

                - **LoadBalancerAddresses** *(list) --* 

                  [Network Load Balancers] The static IP address.

                  
                  

                  - *(dict) --* 

                    Information about a static IP address for a load balancer.

                    
                    

                    - **IpAddress** *(string) --* 

                      The static IP address.

                      
                    

                    - **AllocationId** *(string) --* 

                      [Network Load Balancers] The allocation ID of the Elastic IP address.

                      
                
              
            
          
            

            - **SecurityGroups** *(list) --* 

              The IDs of the security groups for the load balancer.

              
              

              - *(string) --* 
          
            

            - **IpAddressType** *(string) --* 

              The type of IP addresses used by the subnets for your load balancer. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).

              
        
      
    

    **Examples** 

    This example creates an Internet-facing load balancer and enables the Availability Zones for the specified subnets.
    ::

      response = client.create_load_balancer(
          Name='my-load-balancer',
          Subnets=[
              'subnet-b7d581c0',
              'subnet-8360a9e7',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'LoadBalancers': [
              {
                  'AvailabilityZones': [
                      {
                          'SubnetId': 'subnet-8360a9e7',
                          'ZoneName': 'us-west-2a',
                      },
                      {
                          'SubnetId': 'subnet-b7d581c0',
                          'ZoneName': 'us-west-2b',
                      },
                  ],
                  'CanonicalHostedZoneId': 'Z2P70J7EXAMPLE',
                  'CreatedTime': datetime(2016, 3, 25, 21, 26, 12, 4, 85, 0),
                  'DNSName': 'my-load-balancer-424835706.us-west-2.elb.amazonaws.com',
                  'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  'LoadBalancerName': 'my-load-balancer',
                  'Scheme': 'internet-facing',
                  'SecurityGroups': [
                      'sg-5943793c',
                  ],
                  'State': {
                      'Code': 'provisioning',
                  },
                  'Type': 'application',
                  'VpcId': 'vpc-3ac0fb5f',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example creates an internal load balancer and enables the Availability Zones for the specified subnets.
    ::

      response = client.create_load_balancer(
          Name='my-internal-load-balancer',
          Scheme='internal',
          SecurityGroups=[
          ],
          Subnets=[
              'subnet-b7d581c0',
              'subnet-8360a9e7',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'LoadBalancers': [
              {
                  'AvailabilityZones': [
                      {
                          'SubnetId': 'subnet-8360a9e7',
                          'ZoneName': 'us-west-2a',
                      },
                      {
                          'SubnetId': 'subnet-b7d581c0',
                          'ZoneName': 'us-west-2b',
                      },
                  ],
                  'CanonicalHostedZoneId': 'Z2P70J7EXAMPLE',
                  'CreatedTime': datetime(2016, 3, 25, 21, 29, 48, 4, 85, 0),
                  'DNSName': 'internal-my-internal-load-balancer-1529930873.us-west-2.elb.amazonaws.com',
                  'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-internal-load-balancer/5b49b8d4303115c2',
                  'LoadBalancerName': 'my-internal-load-balancer',
                  'Scheme': 'internal',
                  'SecurityGroups': [
                      'sg-5943793c',
                  ],
                  'State': {
                      'Code': 'provisioning',
                  },
                  'Type': 'application',
                  'VpcId': 'vpc-3ac0fb5f',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_rule(**kwargs)

    

    Creates a rule for the specified listener. The listener must be associated with an Application Load Balancer.

     

    Rules are evaluated in priority order, from the lowest value to the highest value. When the condition for a rule is met, the specified action is taken. If no conditions are met, the action for the default rule is taken. For more information, see `Listener Rules <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules>`__ in the *Application Load Balancers Guide* .

     

    To view your current rules, use  DescribeRules . To update a rule, use  ModifyRule . To set the priorities of your rules, use  SetRulePriorities . To delete a rule, use  DeleteRule .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateRule>`_    


    **Request Syntax** 
    ::

      response = client.create_rule(
          ListenerArn='string',
          Conditions=[
              {
                  'Field': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          Priority=123,
          Actions=[
              {
                  'Type': 'forward',
                  'TargetGroupArn': 'string'
              },
          ]
      )
    :type ListenerArn: string
    :param ListenerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the listener.

      

    
    :type Conditions: list
    :param Conditions: **[REQUIRED]** 

      The conditions. Each condition specifies a field name and a single value.

       

      If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

       

       
      * A-Z, a-z, 0-9 
       
      * - . 
       
      * * (matches 0 or more characters) 
       
      * ? (matches exactly 1 character) 
       

       

      If the field name is ``path-pattern`` , you can specify a single path pattern. A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

       

       
      * A-Z, a-z, 0-9 
       
      * _ - . $ / ~ " ' @ : + 
       
      * & (using &amp;) 
       
      * * (matches 0 or more characters) 
       
      * ? (matches exactly 1 character) 
       

      

    
      - *(dict) --* 

        Information about a condition for a rule.

        

      
        - **Field** *(string) --* 

          The name of the field. The possible values are ``host-header`` and ``path-pattern`` .

          

        
        - **Values** *(list) --* 

          The condition value.

           

          If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

           

           
          * A-Z, a-z, 0-9 
           
          * - . 
           
          * * (matches 0 or more characters) 
           
          * ? (matches exactly 1 character) 
           

           

          If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

           

           
          * A-Z, a-z, 0-9 
           
          * _ - . $ / ~ " ' @ : + 
           
          * & (using &amp;) 
           
          * * (matches 0 or more characters) 
           
          * ? (matches exactly 1 character) 
           

          

        
          - *(string) --* 

          
      
      
  
    :type Priority: integer
    :param Priority: **[REQUIRED]** 

      The priority for the rule. A listener can't have multiple rules with the same priority.

      

    
    :type Actions: list
    :param Actions: **[REQUIRED]** 

      An action. Each action has the type ``forward`` and specifies a target group.

      

    
      - *(dict) --* 

        Information about an action.

        

      
        - **Type** *(string) --* **[REQUIRED]** 

          The type of action.

          

        
        - **TargetGroupArn** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the target group.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rules': [
                {
                    'RuleArn': 'string',
                    'Priority': 'string',
                    'Conditions': [
                        {
                            'Field': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'Actions': [
                        {
                            'Type': 'forward',
                            'TargetGroupArn': 'string'
                        },
                    ],
                    'IsDefault': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rules** *(list) --* 

          Information about the rule.

          
          

          - *(dict) --* 

            Information about a rule.

            
            

            - **RuleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the rule.

              
            

            - **Priority** *(string) --* 

              The priority.

              
            

            - **Conditions** *(list) --* 

              The conditions.

              
              

              - *(dict) --* 

                Information about a condition for a rule.

                
                

                - **Field** *(string) --* 

                  The name of the field. The possible values are ``host-header`` and ``path-pattern`` .

                  
                

                - **Values** *(list) --* 

                  The condition value.

                   

                  If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

                   

                   
                  * A-Z, a-z, 0-9 
                   
                  * - . 
                   
                  * * (matches 0 or more characters) 
                   
                  * ? (matches exactly 1 character) 
                   

                   

                  If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

                   

                   
                  * A-Z, a-z, 0-9 
                   
                  * _ - . $ / ~ " ' @ : + 
                   
                  * & (using &amp;) 
                   
                  * * (matches 0 or more characters) 
                   
                  * ? (matches exactly 1 character) 
                   

                  
                  

                  - *(string) --* 
              
            
          
            

            - **Actions** *(list) --* 

              The actions.

              
              

              - *(dict) --* 

                Information about an action.

                
                

                - **Type** *(string) --* 

                  The type of action.

                  
                

                - **TargetGroupArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the target group.

                  
            
          
            

            - **IsDefault** *(boolean) --* 

              Indicates whether this is the default rule.

              
        
      
    

    **Examples** 

    This example creates a rule that forwards requests to the specified target group if the URL contains the specified pattern (for example, /img/*).
    ::

      response = client.create_rule(
          Actions=[
              {
                  'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                  'Type': 'forward',
              },
          ],
          Conditions=[
              {
                  'Field': 'path-pattern',
                  'Values': [
                      '/img/*',
                  ],
              },
          ],
          ListenerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
          Priority=10,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Rules': [
              {
                  'Actions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                          'Type': 'forward',
                      },
                  ],
                  'Conditions': [
                      {
                          'Field': 'path-pattern',
                          'Values': [
                              '/img/*',
                          ],
                      },
                  ],
                  'IsDefault': False,
                  'Priority': '10',
                  'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_target_group(**kwargs)

    

    Creates a target group.

     

    To register targets with the target group, use  RegisterTargets . To update the health check settings for the target group, use  ModifyTargetGroup . To monitor the health of targets in the target group, use  DescribeTargetHealth .

     

    To route traffic to the targets in a target group, specify the target group in an action using  CreateListener or  CreateRule .

     

    To delete a target group, use  DeleteTargetGroup .

     

    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.

     

    For more information, see `Target Groups for Your Application Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html>`__ in the *Application Load Balancers Guide* or `Target Groups for Your Network Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html>`__ in the *Network Load Balancers Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateTargetGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_target_group(
          Name='string',
          Protocol='HTTP'|'HTTPS'|'TCP',
          Port=123,
          VpcId='string',
          HealthCheckProtocol='HTTP'|'HTTPS'|'TCP',
          HealthCheckPort='string',
          HealthCheckPath='string',
          HealthCheckIntervalSeconds=123,
          HealthCheckTimeoutSeconds=123,
          HealthyThresholdCount=123,
          UnhealthyThresholdCount=123,
          Matcher={
              'HttpCode': 'string'
          },
          TargetType='instance'|'ip'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the target group.

       

      This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.

      

    
    :type Protocol: string
    :param Protocol: **[REQUIRED]** 

      The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocol is TCP.

      

    
    :type Port: integer
    :param Port: **[REQUIRED]** 

      The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target.

      

    
    :type VpcId: string
    :param VpcId: **[REQUIRED]** 

      The identifier of the virtual private cloud (VPC).

      

    
    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: 

      The protocol the load balancer uses when performing health checks on targets. The TCP protocol is supported only if the protocol of the target group is TCP. For Application Load Balancers, the default is HTTP. For Network Load Balancers, the default is TCP.

      

    
    :type HealthCheckPort: string
    :param HealthCheckPort: 

      The port the load balancer uses when performing health checks on targets. The default is ``traffic-port`` , which is the port on which each target receives traffic from the load balancer.

      

    
    :type HealthCheckPath: string
    :param HealthCheckPath: 

      [HTTP/HTTPS health checks] The ping path that is the destination on the targets for health checks. The default is /.

      

    
    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: 

      The approximate amount of time, in seconds, between health checks of an individual target. For Application Load Balancers, the range is 5 to 300 seconds. For Network Load Balancers, the supported values are 10 or 30 seconds. The default is 30 seconds.

      

    
    :type HealthCheckTimeoutSeconds: integer
    :param HealthCheckTimeoutSeconds: 

      The amount of time, in seconds, during which no response from a target means a failed health check. For Application Load Balancers, the range is 2 to 60 seconds and the default is 5 seconds. For Network Load Balancers, this is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.

      

    
    :type HealthyThresholdCount: integer
    :param HealthyThresholdCount: 

      The number of consecutive health checks successes required before considering an unhealthy target healthy. For Application Load Balancers, the default is 5. For Network Load Balancers, the default is 3.

      

    
    :type UnhealthyThresholdCount: integer
    :param UnhealthyThresholdCount: 

      The number of consecutive health check failures required before considering a target unhealthy. For Application Load Balancers, the default is 2. For Network Load Balancers, this value must be the same as the healthy threshold count.

      

    
    :type Matcher: dict
    :param Matcher: 

      [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a target.

      

    
      - **HttpCode** *(string) --* **[REQUIRED]** 

        The HTTP codes.

         

        For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").

         

        For Network Load Balancers, this is 200 to 399.

        

      
    
    :type TargetType: string
    :param TargetType: 

      The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address). The default is ``instance`` . Note that you can't specify targets for a target group using both instance IDs and IP addresses.

       

      If the target type is ``ip`` , specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify publicly routable IP addresses.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TargetGroups': [
                {
                    'TargetGroupArn': 'string',
                    'TargetGroupName': 'string',
                    'Protocol': 'HTTP'|'HTTPS'|'TCP',
                    'Port': 123,
                    'VpcId': 'string',
                    'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP',
                    'HealthCheckPort': 'string',
                    'HealthCheckIntervalSeconds': 123,
                    'HealthCheckTimeoutSeconds': 123,
                    'HealthyThresholdCount': 123,
                    'UnhealthyThresholdCount': 123,
                    'HealthCheckPath': 'string',
                    'Matcher': {
                        'HttpCode': 'string'
                    },
                    'LoadBalancerArns': [
                        'string',
                    ],
                    'TargetType': 'instance'|'ip'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TargetGroups** *(list) --* 

          Information about the target group.

          
          

          - *(dict) --* 

            Information about a target group.

            
            

            - **TargetGroupArn** *(string) --* 

              The Amazon Resource Name (ARN) of the target group.

              
            

            - **TargetGroupName** *(string) --* 

              The name of the target group.

              
            

            - **Protocol** *(string) --* 

              The protocol to use for routing traffic to the targets.

              
            

            - **Port** *(integer) --* 

              The port on which the targets are listening.

              
            

            - **VpcId** *(string) --* 

              The ID of the VPC for the targets.

              
            

            - **HealthCheckProtocol** *(string) --* 

              The protocol to use to connect with the target.

              
            

            - **HealthCheckPort** *(string) --* 

              The port to use to connect with the target.

              
            

            - **HealthCheckIntervalSeconds** *(integer) --* 

              The approximate amount of time, in seconds, between health checks of an individual target.

              
            

            - **HealthCheckTimeoutSeconds** *(integer) --* 

              The amount of time, in seconds, during which no response means a failed health check.

              
            

            - **HealthyThresholdCount** *(integer) --* 

              The number of consecutive health checks successes required before considering an unhealthy target healthy.

              
            

            - **UnhealthyThresholdCount** *(integer) --* 

              The number of consecutive health check failures required before considering the target unhealthy.

              
            

            - **HealthCheckPath** *(string) --* 

              The destination for the health check request.

              
            

            - **Matcher** *(dict) --* 

              The HTTP codes to use when checking for a successful response from a target.

              
              

              - **HttpCode** *(string) --* 

                The HTTP codes.

                 

                For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").

                 

                For Network Load Balancers, this is 200 to 399.

                
          
            

            - **LoadBalancerArns** *(list) --* 

              The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.

              
              

              - *(string) --* 
          
            

            - **TargetType** *(string) --* 

              The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address).

              
        
      
    

    **Examples** 

    This example creates a target group that you can use to route traffic to targets using HTTP on port 80. This target group uses the default health check configuration.
    ::

      response = client.create_target_group(
          Name='my-targets',
          Port=80,
          Protocol='HTTP',
          VpcId='vpc-3ac0fb5f',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'TargetGroups': [
              {
                  'HealthCheckIntervalSeconds': 30,
                  'HealthCheckPath': '/',
                  'HealthCheckPort': 'traffic-port',
                  'HealthCheckProtocol': 'HTTP',
                  'HealthCheckTimeoutSeconds': 5,
                  'HealthyThresholdCount': 5,
                  'Matcher': {
                      'HttpCode': '200',
                  },
                  'Port': 80,
                  'Protocol': 'HTTP',
                  'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                  'TargetGroupName': 'my-targets',
                  'UnhealthyThresholdCount': 2,
                  'VpcId': 'vpc-3ac0fb5f',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_listener(**kwargs)

    

    Deletes the specified listener.

     

    Alternatively, your listener is deleted when you delete the load balancer it is attached to using  DeleteLoadBalancer .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteListener>`_    


    **Request Syntax** 
    ::

      response = client.delete_listener(
          ListenerArn='string'
      )
    :type ListenerArn: string
    :param ListenerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the listener.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deletes the specified listener.
    ::

      response = client.delete_listener(
          ListenerArn='arn:aws:elasticloadbalancing:ua-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_load_balancer(**kwargs)

    

    Deletes the specified Application Load Balancer or Network Load Balancer and its attached listeners.

     

    You can't delete a load balancer if deletion protection is enabled. If the load balancer does not exist or has already been deleted, the call succeeds.

     

    Deleting a load balancer does not affect its registered targets. For example, your EC2 instances continue to run and are still registered to their target groups. If you no longer need these EC2 instances, you can stop or terminate them.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.delete_load_balancer(
          LoadBalancerArn='string'
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deletes the specified load balancer.
    ::

      response = client.delete_load_balancer(
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_rule(**kwargs)

    

    Deletes the specified rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteRule>`_    


    **Request Syntax** 
    ::

      response = client.delete_rule(
          RuleArn='string'
      )
    :type RuleArn: string
    :param RuleArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the rule.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deletes the specified rule.
    ::

      response = client.delete_rule(
          RuleArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_target_group(**kwargs)

    

    Deletes the specified target group.

     

    You can delete a target group if it is not referenced by any actions. Deleting a target group also deletes any associated health checks.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteTargetGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_target_group(
          TargetGroupArn='string'
      )
    :type TargetGroupArn: string
    :param TargetGroupArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the target group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deletes the specified target group.
    ::

      response = client.delete_target_group(
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: deregister_targets(**kwargs)

    

    Deregisters the specified targets from the specified target group. After the targets are deregistered, they no longer receive traffic from the load balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeregisterTargets>`_    


    **Request Syntax** 
    ::

      response = client.deregister_targets(
          TargetGroupArn='string',
          Targets=[
              {
                  'Id': 'string',
                  'Port': 123,
                  'AvailabilityZone': 'string'
              },
          ]
      )
    :type TargetGroupArn: string
    :param TargetGroupArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the target group.

      

    
    :type Targets: list
    :param Targets: **[REQUIRED]** 

      The targets. If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.

      

    
      - *(dict) --* 

        Information about a target.

        

      
        - **Id** *(string) --* **[REQUIRED]** 

          The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.

          

        
        - **Port** *(integer) --* 

          The port on which the target is listening.

          

        
        - **AvailabilityZone** *(string) --* 

          An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.

           

          This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.

           

          With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example deregisters the specified instance from the specified target group.
    ::

      response = client.deregister_targets(
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
          Targets=[
              {
                  'Id': 'i-0f76fade',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_account_limits(**kwargs)

    

    Describes the current Elastic Load Balancing resource limits for your AWS account.

     

    For more information, see `Limits for Your Application Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html>`__ in the *Application Load Balancer Guide* or `Limits for Your Network Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html>`__ in the *Network Load Balancers Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits>`_    


    **Request Syntax** 
    ::

      response = client.describe_account_limits(
          Marker='string',
          PageSize=123
      )
    :type Marker: string
    :param Marker: 

      The marker for the next set of results. (You received this marker from a previous call.)

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of results to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Limits': [
                {
                    'Name': 'string',
                    'Max': 'string'
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Limits** *(list) --* 

          Information about the limits.

          
          

          - *(dict) --* 

            Information about an Elastic Load Balancing resource limit for your AWS account.

            
            

            - **Name** *(string) --* 

              The name of the limit. The possible values are:

               

               
              * application-load-balancers 
               
              * listeners-per-application-load-balancer 
               
              * listeners-per-network-load-balancer 
               
              * network-load-balancers 
               
              * rules-per-application-load-balancer 
               
              * target-groups 
               
              * targets-per-application-load-balancer 
               
              * targets-per-availability-zone-per-network-load-balancer 
               
              * targets-per-network-load-balancer 
               

              
            

            - **Max** *(string) --* 

              The maximum value of the limit.

              
        
      
        

        - **NextMarker** *(string) --* 

          The marker to use when requesting the next set of results. If there are no additional results, the string is empty.

          
    

  .. py:method:: describe_listener_certificates(**kwargs)

    

    Describes the certificates for the specified secure listener.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates>`_    


    **Request Syntax** 
    ::

      response = client.describe_listener_certificates(
          ListenerArn='string',
          Marker='string',
          PageSize=123
      )
    :type ListenerArn: string
    :param ListenerArn: **[REQUIRED]** 

      The Amazon Resource Names (ARN) of the listener.

      

    
    :type Marker: string
    :param Marker: 

      The marker for the next set of results. (You received this marker from a previous call.)

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of results to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Certificates': [
                {
                    'CertificateArn': 'string',
                    'IsDefault': True|False
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Certificates** *(list) --* 

          Information about the certificates.

          
          

          - *(dict) --* 

            Information about an SSL server certificate.

            
            

            - **CertificateArn** *(string) --* 

              The Amazon Resource Name (ARN) of the certificate.

              
            

            - **IsDefault** *(boolean) --* 

              Indicates whether the certificate is the default certificate.

              
        
      
        

        - **NextMarker** *(string) --* 

          The marker to use when requesting the next set of results. If there are no additional results, the string is empty.

          
    

  .. py:method:: describe_listeners(**kwargs)

    

    Describes the specified listeners or the listeners for the specified Application Load Balancer or Network Load Balancer. You must specify either a load balancer or one or more listeners.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListeners>`_    


    **Request Syntax** 
    ::

      response = client.describe_listeners(
          LoadBalancerArn='string',
          ListenerArns=[
              'string',
          ],
          Marker='string',
          PageSize=123
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type ListenerArns: list
    :param ListenerArns: 

      The Amazon Resource Names (ARN) of the listeners.

      

    
      - *(string) --* 

      
  
    :type Marker: string
    :param Marker: 

      The marker for the next set of results. (You received this marker from a previous call.)

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of results to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Listeners': [
                {
                    'ListenerArn': 'string',
                    'LoadBalancerArn': 'string',
                    'Port': 123,
                    'Protocol': 'HTTP'|'HTTPS'|'TCP',
                    'Certificates': [
                        {
                            'CertificateArn': 'string',
                            'IsDefault': True|False
                        },
                    ],
                    'SslPolicy': 'string',
                    'DefaultActions': [
                        {
                            'Type': 'forward',
                            'TargetGroupArn': 'string'
                        },
                    ]
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Listeners** *(list) --* 

          Information about the listeners.

          
          

          - *(dict) --* 

            Information about a listener.

            
            

            - **ListenerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the listener.

              
            

            - **LoadBalancerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the load balancer.

              
            

            - **Port** *(integer) --* 

              The port on which the load balancer is listening.

              
            

            - **Protocol** *(string) --* 

              The protocol for connections from clients to the load balancer.

              
            

            - **Certificates** *(list) --* 

              The SSL server certificate. You must provide a certificate if the protocol is HTTPS.

              
              

              - *(dict) --* 

                Information about an SSL server certificate.

                
                

                - **CertificateArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the certificate.

                  
                

                - **IsDefault** *(boolean) --* 

                  Indicates whether the certificate is the default certificate.

                  
            
          
            

            - **SslPolicy** *(string) --* 

              The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.

              
            

            - **DefaultActions** *(list) --* 

              The default actions for the listener.

              
              

              - *(dict) --* 

                Information about an action.

                
                

                - **Type** *(string) --* 

                  The type of action.

                  
                

                - **TargetGroupArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the target group.

                  
            
          
        
      
        

        - **NextMarker** *(string) --* 

          The marker to use when requesting the next set of results. If there are no additional results, the string is empty.

          
    

    **Examples** 

    This example describes the specified listener.
    ::

      response = client.describe_listeners(
          ListenerArns=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Listeners': [
              {
                  'DefaultActions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                          'Type': 'forward',
                      },
                  ],
                  'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
                  'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  'Port': 80,
                  'Protocol': 'HTTP',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_load_balancer_attributes(**kwargs)

    

    Describes the attributes for the specified Application Load Balancer or Network Load Balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes>`_    


    **Request Syntax** 
    ::

      response = client.describe_load_balancer_attributes(
          LoadBalancerArn='string'
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Attributes': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Attributes** *(list) --* 

          Information about the load balancer attributes.

          
          

          - *(dict) --* 

            Information about a load balancer attribute.

            
            

            - **Key** *(string) --* 

              The name of the attribute.

               

               
              * ``access_logs.s3.enabled`` - [Application Load Balancers] Indicates whether access logs stored in Amazon S3 are enabled. The value is ``true`` or ``false`` . 
               
              * ``access_logs.s3.bucket`` - [Application Load Balancers] The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket. 
               
              * ``access_logs.s3.prefix`` - [Application Load Balancers] The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket. 
               
              * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The value is ``true`` or ``false`` . 
               
              * ``idle_timeout.timeout_seconds`` - [Application Load Balancers] The idle timeout value, in seconds. The valid range is 1-4000. The default is 60 seconds. 
               

              
            

            - **Value** *(string) --* 

              The value of the attribute.

              
        
      
    

    **Examples** 

    This example describes the attributes of the specified load balancer.
    ::

      response = client.describe_load_balancer_attributes(
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Attributes': [
              {
                  'Key': 'access_logs.s3.enabled',
                  'Value': 'false',
              },
              {
                  'Key': 'idle_timeout.timeout_seconds',
                  'Value': '60',
              },
              {
                  'Key': 'access_logs.s3.prefix',
                  'Value': '',
              },
              {
                  'Key': 'deletion_protection.enabled',
                  'Value': 'false',
              },
              {
                  'Key': 'access_logs.s3.bucket',
                  'Value': '',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_load_balancers(**kwargs)

    

    Describes the specified load balancers or all of your load balancers.

     

    To describe the listeners for a load balancer, use  DescribeListeners . To describe the attributes for a load balancer, use  DescribeLoadBalancerAttributes .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_    


    **Request Syntax** 
    ::

      response = client.describe_load_balancers(
          LoadBalancerArns=[
              'string',
          ],
          Names=[
              'string',
          ],
          Marker='string',
          PageSize=123
      )
    :type LoadBalancerArns: list
    :param LoadBalancerArns: 

      The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.

      

    
      - *(string) --* 

      
  
    :type Names: list
    :param Names: 

      The names of the load balancers.

      

    
      - *(string) --* 

      
  
    :type Marker: string
    :param Marker: 

      The marker for the next set of results. (You received this marker from a previous call.)

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of results to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LoadBalancers': [
                {
                    'LoadBalancerArn': 'string',
                    'DNSName': 'string',
                    'CanonicalHostedZoneId': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'LoadBalancerName': 'string',
                    'Scheme': 'internet-facing'|'internal',
                    'VpcId': 'string',
                    'State': {
                        'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                        'Reason': 'string'
                    },
                    'Type': 'application'|'network',
                    'AvailabilityZones': [
                        {
                            'ZoneName': 'string',
                            'SubnetId': 'string',
                            'LoadBalancerAddresses': [
                                {
                                    'IpAddress': 'string',
                                    'AllocationId': 'string'
                                },
                            ]
                        },
                    ],
                    'SecurityGroups': [
                        'string',
                    ],
                    'IpAddressType': 'ipv4'|'dualstack'
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LoadBalancers** *(list) --* 

          Information about the load balancers.

          
          

          - *(dict) --* 

            Information about a load balancer.

            
            

            - **LoadBalancerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the load balancer.

              
            

            - **DNSName** *(string) --* 

              The public DNS name of the load balancer.

              
            

            - **CanonicalHostedZoneId** *(string) --* 

              The ID of the Amazon Route 53 hosted zone associated with the load balancer.

              
            

            - **CreatedTime** *(datetime) --* 

              The date and time the load balancer was created.

              
            

            - **LoadBalancerName** *(string) --* 

              The name of the load balancer.

              
            

            - **Scheme** *(string) --* 

              The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the Internet.

               

              The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.

              
            

            - **VpcId** *(string) --* 

              The ID of the VPC for the load balancer.

              
            

            - **State** *(dict) --* 

              The state of the load balancer.

              
              

              - **Code** *(string) --* 

                The state code. The initial state of the load balancer is ``provisioning`` . After the load balancer is fully set up and ready to route traffic, its state is ``active`` . If the load balancer could not be set up, its state is ``failed`` .

                
              

              - **Reason** *(string) --* 

                A description of the state.

                
          
            

            - **Type** *(string) --* 

              The type of load balancer.

              
            

            - **AvailabilityZones** *(list) --* 

              The Availability Zones for the load balancer.

              
              

              - *(dict) --* 

                Information about an Availability Zone.

                
                

                - **ZoneName** *(string) --* 

                  The name of the Availability Zone.

                  
                

                - **SubnetId** *(string) --* 

                  The ID of the subnet.

                  
                

                - **LoadBalancerAddresses** *(list) --* 

                  [Network Load Balancers] The static IP address.

                  
                  

                  - *(dict) --* 

                    Information about a static IP address for a load balancer.

                    
                    

                    - **IpAddress** *(string) --* 

                      The static IP address.

                      
                    

                    - **AllocationId** *(string) --* 

                      [Network Load Balancers] The allocation ID of the Elastic IP address.

                      
                
              
            
          
            

            - **SecurityGroups** *(list) --* 

              The IDs of the security groups for the load balancer.

              
              

              - *(string) --* 
          
            

            - **IpAddressType** *(string) --* 

              The type of IP addresses used by the subnets for your load balancer. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).

              
        
      
        

        - **NextMarker** *(string) --* 

          The marker to use when requesting the next set of results. If there are no additional results, the string is empty.

          
    

    **Examples** 

    This example describes the specified load balancer.
    ::

      response = client.describe_load_balancers(
          LoadBalancerArns=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'LoadBalancers': [
              {
                  'AvailabilityZones': [
                      {
                          'SubnetId': 'subnet-8360a9e7',
                          'ZoneName': 'us-west-2a',
                      },
                      {
                          'SubnetId': 'subnet-b7d581c0',
                          'ZoneName': 'us-west-2b',
                      },
                  ],
                  'CanonicalHostedZoneId': 'Z2P70J7EXAMPLE',
                  'CreatedTime': datetime(2016, 3, 25, 21, 26, 12, 4, 85, 0),
                  'DNSName': 'my-load-balancer-424835706.us-west-2.elb.amazonaws.com',
                  'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  'LoadBalancerName': 'my-load-balancer',
                  'Scheme': 'internet-facing',
                  'SecurityGroups': [
                      'sg-5943793c',
                  ],
                  'State': {
                      'Code': 'active',
                  },
                  'Type': 'application',
                  'VpcId': 'vpc-3ac0fb5f',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_rules(**kwargs)

    

    Describes the specified rules or the rules for the specified listener. You must specify either a listener or one or more rules.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeRules>`_    


    **Request Syntax** 
    ::

      response = client.describe_rules(
          ListenerArn='string',
          RuleArns=[
              'string',
          ],
          Marker='string',
          PageSize=123
      )
    :type ListenerArn: string
    :param ListenerArn: 

      The Amazon Resource Name (ARN) of the listener.

      

    
    :type RuleArns: list
    :param RuleArns: 

      The Amazon Resource Names (ARN) of the rules.

      

    
      - *(string) --* 

      
  
    :type Marker: string
    :param Marker: 

      The marker for the next set of results. (You received this marker from a previous call.)

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of results to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rules': [
                {
                    'RuleArn': 'string',
                    'Priority': 'string',
                    'Conditions': [
                        {
                            'Field': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'Actions': [
                        {
                            'Type': 'forward',
                            'TargetGroupArn': 'string'
                        },
                    ],
                    'IsDefault': True|False
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rules** *(list) --* 

          Information about the rules.

          
          

          - *(dict) --* 

            Information about a rule.

            
            

            - **RuleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the rule.

              
            

            - **Priority** *(string) --* 

              The priority.

              
            

            - **Conditions** *(list) --* 

              The conditions.

              
              

              - *(dict) --* 

                Information about a condition for a rule.

                
                

                - **Field** *(string) --* 

                  The name of the field. The possible values are ``host-header`` and ``path-pattern`` .

                  
                

                - **Values** *(list) --* 

                  The condition value.

                   

                  If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

                   

                   
                  * A-Z, a-z, 0-9 
                   
                  * - . 
                   
                  * * (matches 0 or more characters) 
                   
                  * ? (matches exactly 1 character) 
                   

                   

                  If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

                   

                   
                  * A-Z, a-z, 0-9 
                   
                  * _ - . $ / ~ " ' @ : + 
                   
                  * & (using &amp;) 
                   
                  * * (matches 0 or more characters) 
                   
                  * ? (matches exactly 1 character) 
                   

                  
                  

                  - *(string) --* 
              
            
          
            

            - **Actions** *(list) --* 

              The actions.

              
              

              - *(dict) --* 

                Information about an action.

                
                

                - **Type** *(string) --* 

                  The type of action.

                  
                

                - **TargetGroupArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the target group.

                  
            
          
            

            - **IsDefault** *(boolean) --* 

              Indicates whether this is the default rule.

              
        
      
        

        - **NextMarker** *(string) --* 

          The marker to use when requesting the next set of results. If there are no additional results, the string is empty.

          
    

    **Examples** 

    This example describes the specified rule.
    ::

      response = client.describe_rules(
          RuleArns=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Rules': [
              {
                  'Actions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                          'Type': 'forward',
                      },
                  ],
                  'Conditions': [
                      {
                          'Field': 'path-pattern',
                          'Values': [
                              '/img/*',
                          ],
                      },
                  ],
                  'IsDefault': False,
                  'Priority': '10',
                  'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_ssl_policies(**kwargs)

    

    Describes the specified policies or all policies used for SSL negotiation.

     

    For more information, see `Security Policies <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies>`__ in the *Application Load Balancers Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies>`_    


    **Request Syntax** 
    ::

      response = client.describe_ssl_policies(
          Names=[
              'string',
          ],
          Marker='string',
          PageSize=123
      )
    :type Names: list
    :param Names: 

      The names of the policies.

      

    
      - *(string) --* 

      
  
    :type Marker: string
    :param Marker: 

      The marker for the next set of results. (You received this marker from a previous call.)

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of results to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SslPolicies': [
                {
                    'SslProtocols': [
                        'string',
                    ],
                    'Ciphers': [
                        {
                            'Name': 'string',
                            'Priority': 123
                        },
                    ],
                    'Name': 'string'
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SslPolicies** *(list) --* 

          Information about the policies.

          
          

          - *(dict) --* 

            Information about a policy used for SSL negotiation.

            
            

            - **SslProtocols** *(list) --* 

              The protocols.

              
              

              - *(string) --* 
          
            

            - **Ciphers** *(list) --* 

              The ciphers.

              
              

              - *(dict) --* 

                Information about a cipher used in a policy.

                
                

                - **Name** *(string) --* 

                  The name of the cipher.

                  
                

                - **Priority** *(integer) --* 

                  The priority of the cipher.

                  
            
          
            

            - **Name** *(string) --* 

              The name of the policy.

              
        
      
        

        - **NextMarker** *(string) --* 

          The marker to use when requesting the next set of results. If there are no additional results, the string is empty.

          
    

    **Examples** 

    This example describes the specified policy used for SSL negotiation.
    ::

      response = client.describe_ssl_policies(
          Names=[
              'ELBSecurityPolicy-2015-05',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SslPolicies': [
              {
                  'Ciphers': [
                      {
                          'Name': 'ECDHE-ECDSA-AES128-GCM-SHA256',
                          'Priority': 1,
                      },
                      {
                          'Name': 'ECDHE-RSA-AES128-GCM-SHA256',
                          'Priority': 2,
                      },
                      {
                          'Name': 'ECDHE-ECDSA-AES128-SHA256',
                          'Priority': 3,
                      },
                      {
                          'Name': 'ECDHE-RSA-AES128-SHA256',
                          'Priority': 4,
                      },
                      {
                          'Name': 'ECDHE-ECDSA-AES128-SHA',
                          'Priority': 5,
                      },
                      {
                          'Name': 'ECDHE-RSA-AES128-SHA',
                          'Priority': 6,
                      },
                      {
                          'Name': 'DHE-RSA-AES128-SHA',
                          'Priority': 7,
                      },
                      {
                          'Name': 'ECDHE-ECDSA-AES256-GCM-SHA384',
                          'Priority': 8,
                      },
                      {
                          'Name': 'ECDHE-RSA-AES256-GCM-SHA384',
                          'Priority': 9,
                      },
                      {
                          'Name': 'ECDHE-ECDSA-AES256-SHA384',
                          'Priority': 10,
                      },
                      {
                          'Name': 'ECDHE-RSA-AES256-SHA384',
                          'Priority': 11,
                      },
                      {
                          'Name': 'ECDHE-RSA-AES256-SHA',
                          'Priority': 12,
                      },
                      {
                          'Name': 'ECDHE-ECDSA-AES256-SHA',
                          'Priority': 13,
                      },
                      {
                          'Name': 'AES128-GCM-SHA256',
                          'Priority': 14,
                      },
                      {
                          'Name': 'AES128-SHA256',
                          'Priority': 15,
                      },
                      {
                          'Name': 'AES128-SHA',
                          'Priority': 16,
                      },
                      {
                          'Name': 'AES256-GCM-SHA384',
                          'Priority': 17,
                      },
                      {
                          'Name': 'AES256-SHA256',
                          'Priority': 18,
                      },
                      {
                          'Name': 'AES256-SHA',
                          'Priority': 19,
                      },
                  ],
                  'Name': 'ELBSecurityPolicy-2015-05',
                  'SslProtocols': [
                      'TLSv1',
                      'TLSv1.1',
                      'TLSv1.2',
                  ],
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_tags(**kwargs)

    

    Describes the tags for the specified resources. You can describe the tags for one or more Application Load Balancers, Network Load Balancers, and target groups.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTags>`_    


    **Request Syntax** 
    ::

      response = client.describe_tags(
          ResourceArns=[
              'string',
          ]
      )
    :type ResourceArns: list
    :param ResourceArns: **[REQUIRED]** 

      The Amazon Resource Names (ARN) of the resources.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TagDescriptions': [
                {
                    'ResourceArn': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TagDescriptions** *(list) --* 

          Information about the tags.

          
          

          - *(dict) --* 

            The tags associated with a resource.

            
            

            - **ResourceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the resource.

              
            

            - **Tags** *(list) --* 

              Information about the tags.

              
              

              - *(dict) --* 

                Information about a tag.

                
                

                - **Key** *(string) --* 

                  The key of the tag.

                  
                

                - **Value** *(string) --* 

                  The value of the tag.

                  
            
          
        
      
    

    **Examples** 

    This example describes the tags assigned to the specified load balancer.
    ::

      response = client.describe_tags(
          ResourceArns=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'TagDescriptions': [
              {
                  'ResourceArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  'Tags': [
                      {
                          'Key': 'project',
                          'Value': 'lima',
                      },
                      {
                          'Key': 'department',
                          'Value': 'digital-media',
                      },
                  ],
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_target_group_attributes(**kwargs)

    

    Describes the attributes for the specified target group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroupAttributes>`_    


    **Request Syntax** 
    ::

      response = client.describe_target_group_attributes(
          TargetGroupArn='string'
      )
    :type TargetGroupArn: string
    :param TargetGroupArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the target group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Attributes': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Attributes** *(list) --* 

          Information about the target group attributes

          
          

          - *(dict) --* 

            Information about a target group attribute.

            
            

            - **Key** *(string) --* 

              The name of the attribute.

               

               
              * ``deregistration_delay.timeout_seconds`` - The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. 
               
              * ``proxy_protocol_v2.enabled`` - [Network Load Balancers] Indicates whether Proxy Protocol version 2 is enabled. 
               
              * ``stickiness.enabled`` - [Application Load Balancers] Indicates whether sticky sessions are enabled. The value is ``true`` or ``false`` . 
               
              * ``stickiness.type`` - [Application Load Balancers] The type of sticky sessions. The possible value is ``lb_cookie`` . 
               
              * ``stickiness.lb_cookie.duration_seconds`` - [Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds). 
               

              
            

            - **Value** *(string) --* 

              The value of the attribute.

              
        
      
    

    **Examples** 

    This example describes the attributes of the specified target group.
    ::

      response = client.describe_target_group_attributes(
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Attributes': [
              {
                  'Key': 'stickiness.enabled',
                  'Value': 'false',
              },
              {
                  'Key': 'deregistration_delay.timeout_seconds',
                  'Value': '300',
              },
              {
                  'Key': 'stickiness.type',
                  'Value': 'lb_cookie',
              },
              {
                  'Key': 'stickiness.lb_cookie.duration_seconds',
                  'Value': '86400',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_target_groups(**kwargs)

    

    Describes the specified target groups or all of your target groups. By default, all target groups are described. Alternatively, you can specify one of the following to filter the results: the ARN of the load balancer, the names of one or more target groups, or the ARNs of one or more target groups.

     

    To describe the targets for a target group, use  DescribeTargetHealth . To describe the attributes of a target group, use  DescribeTargetGroupAttributes .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_target_groups(
          LoadBalancerArn='string',
          TargetGroupArns=[
              'string',
          ],
          Names=[
              'string',
          ],
          Marker='string',
          PageSize=123
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type TargetGroupArns: list
    :param TargetGroupArns: 

      The Amazon Resource Names (ARN) of the target groups.

      

    
      - *(string) --* 

      
  
    :type Names: list
    :param Names: 

      The names of the target groups.

      

    
      - *(string) --* 

      
  
    :type Marker: string
    :param Marker: 

      The marker for the next set of results. (You received this marker from a previous call.)

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of results to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TargetGroups': [
                {
                    'TargetGroupArn': 'string',
                    'TargetGroupName': 'string',
                    'Protocol': 'HTTP'|'HTTPS'|'TCP',
                    'Port': 123,
                    'VpcId': 'string',
                    'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP',
                    'HealthCheckPort': 'string',
                    'HealthCheckIntervalSeconds': 123,
                    'HealthCheckTimeoutSeconds': 123,
                    'HealthyThresholdCount': 123,
                    'UnhealthyThresholdCount': 123,
                    'HealthCheckPath': 'string',
                    'Matcher': {
                        'HttpCode': 'string'
                    },
                    'LoadBalancerArns': [
                        'string',
                    ],
                    'TargetType': 'instance'|'ip'
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TargetGroups** *(list) --* 

          Information about the target groups.

          
          

          - *(dict) --* 

            Information about a target group.

            
            

            - **TargetGroupArn** *(string) --* 

              The Amazon Resource Name (ARN) of the target group.

              
            

            - **TargetGroupName** *(string) --* 

              The name of the target group.

              
            

            - **Protocol** *(string) --* 

              The protocol to use for routing traffic to the targets.

              
            

            - **Port** *(integer) --* 

              The port on which the targets are listening.

              
            

            - **VpcId** *(string) --* 

              The ID of the VPC for the targets.

              
            

            - **HealthCheckProtocol** *(string) --* 

              The protocol to use to connect with the target.

              
            

            - **HealthCheckPort** *(string) --* 

              The port to use to connect with the target.

              
            

            - **HealthCheckIntervalSeconds** *(integer) --* 

              The approximate amount of time, in seconds, between health checks of an individual target.

              
            

            - **HealthCheckTimeoutSeconds** *(integer) --* 

              The amount of time, in seconds, during which no response means a failed health check.

              
            

            - **HealthyThresholdCount** *(integer) --* 

              The number of consecutive health checks successes required before considering an unhealthy target healthy.

              
            

            - **UnhealthyThresholdCount** *(integer) --* 

              The number of consecutive health check failures required before considering the target unhealthy.

              
            

            - **HealthCheckPath** *(string) --* 

              The destination for the health check request.

              
            

            - **Matcher** *(dict) --* 

              The HTTP codes to use when checking for a successful response from a target.

              
              

              - **HttpCode** *(string) --* 

                The HTTP codes.

                 

                For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").

                 

                For Network Load Balancers, this is 200 to 399.

                
          
            

            - **LoadBalancerArns** *(list) --* 

              The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.

              
              

              - *(string) --* 
          
            

            - **TargetType** *(string) --* 

              The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address).

              
        
      
        

        - **NextMarker** *(string) --* 

          The marker to use when requesting the next set of results. If there are no additional results, the string is empty.

          
    

    **Examples** 

    This example describes the specified target group.
    ::

      response = client.describe_target_groups(
          TargetGroupArns=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'TargetGroups': [
              {
                  'HealthCheckIntervalSeconds': 30,
                  'HealthCheckPath': '/',
                  'HealthCheckPort': 'traffic-port',
                  'HealthCheckProtocol': 'HTTP',
                  'HealthCheckTimeoutSeconds': 5,
                  'HealthyThresholdCount': 5,
                  'LoadBalancerArns': [
                      'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  ],
                  'Matcher': {
                      'HttpCode': '200',
                  },
                  'Port': 80,
                  'Protocol': 'HTTP',
                  'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                  'TargetGroupName': 'my-targets',
                  'UnhealthyThresholdCount': 2,
                  'VpcId': 'vpc-3ac0fb5f',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_target_health(**kwargs)

    

    Describes the health of the specified targets or all of your targets.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth>`_    


    **Request Syntax** 
    ::

      response = client.describe_target_health(
          TargetGroupArn='string',
          Targets=[
              {
                  'Id': 'string',
                  'Port': 123,
                  'AvailabilityZone': 'string'
              },
          ]
      )
    :type TargetGroupArn: string
    :param TargetGroupArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the target group.

      

    
    :type Targets: list
    :param Targets: 

      The targets.

      

    
      - *(dict) --* 

        Information about a target.

        

      
        - **Id** *(string) --* **[REQUIRED]** 

          The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.

          

        
        - **Port** *(integer) --* 

          The port on which the target is listening.

          

        
        - **AvailabilityZone** *(string) --* 

          An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.

           

          This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.

           

          With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TargetHealthDescriptions': [
                {
                    'Target': {
                        'Id': 'string',
                        'Port': 123,
                        'AvailabilityZone': 'string'
                    },
                    'HealthCheckPort': 'string',
                    'TargetHealth': {
                        'State': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                        'Reason': 'Elb.RegistrationInProgress'|'Elb.InitialHealthChecking'|'Target.ResponseCodeMismatch'|'Target.Timeout'|'Target.FailedHealthChecks'|'Target.NotRegistered'|'Target.NotInUse'|'Target.DeregistrationInProgress'|'Target.InvalidState'|'Target.IpUnusable'|'Elb.InternalError',
                        'Description': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TargetHealthDescriptions** *(list) --* 

          Information about the health of the targets.

          
          

          - *(dict) --* 

            Information about the health of a target.

            
            

            - **Target** *(dict) --* 

              The description of the target.

              
              

              - **Id** *(string) --* 

                The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.

                
              

              - **Port** *(integer) --* 

                The port on which the target is listening.

                
              

              - **AvailabilityZone** *(string) --* 

                An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.

                 

                This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.

                 

                With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .

                
          
            

            - **HealthCheckPort** *(string) --* 

              The port to use to connect with the target.

              
            

            - **TargetHealth** *(dict) --* 

              The health information for the target.

              
              

              - **State** *(string) --* 

                The state of the target.

                
              

              - **Reason** *(string) --* 

                The reason code. If the target state is ``healthy`` , a reason code is not provided.

                 

                If the target state is ``initial`` , the reason code can be one of the following values:

                 

                 
                * ``Elb.RegistrationInProgress`` - The target is in the process of being registered with the load balancer. 
                 
                * ``Elb.InitialHealthChecking`` - The load balancer is still sending the target the minimum number of health checks required to determine its health status. 
                 

                 

                If the target state is ``unhealthy`` , the reason code can be one of the following values:

                 

                 
                * ``Target.ResponseCodeMismatch`` - The health checks did not return an expected HTTP code. 
                 
                * ``Target.Timeout`` - The health check requests timed out. 
                 
                * ``Target.FailedHealthChecks`` - The health checks failed because the connection to the target timed out, the target response was malformed, or the target failed the health check for an unknown reason. 
                 
                * ``Elb.InternalError`` - The health checks failed due to an internal error. 
                 

                 

                If the target state is ``unused`` , the reason code can be one of the following values:

                 

                 
                * ``Target.NotRegistered`` - The target is not registered with the target group. 
                 
                * ``Target.NotInUse`` - The target group is not used by any load balancer or the target is in an Availability Zone that is not enabled for its load balancer. 
                 
                * ``Target.IpUnusable`` - The target IP address is reserved for use by a load balancer. 
                 
                * ``Target.InvalidState`` - The target is in the stopped or terminated state. 
                 

                 

                If the target state is ``draining`` , the reason code can be the following value:

                 

                 
                * ``Target.DeregistrationInProgress`` - The target is in the process of being deregistered and the deregistration delay period has not expired. 
                 

                
              

              - **Description** *(string) --* 

                A description of the target health that provides additional details. If the state is ``healthy`` , a description is not provided.

                
          
        
      
    

    **Examples** 

    This example describes the health of the targets for the specified target group. One target is healthy but the other is not specified in an action, so it can't receive traffic from the load balancer.
    ::

      response = client.describe_target_health(
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'TargetHealthDescriptions': [
              {
                  'Target': {
                      'Id': 'i-0f76fade',
                      'Port': 80,
                  },
                  'TargetHealth': {
                      'Description': 'Given target group is not configured to receive traffic from ELB',
                      'Reason': 'Target.NotInUse',
                      'State': 'unused',
                  },
              },
              {
                  'HealthCheckPort': '80',
                  'Target': {
                      'Id': 'i-0f76fade',
                      'Port': 80,
                  },
                  'TargetHealth': {
                      'State': 'healthy',
                  },
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example describes the health of the specified target. This target is healthy.
    ::

      response = client.describe_target_health(
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
          Targets=[
              {
                  'Id': 'i-0f76fade',
                  'Port': 80,
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'TargetHealthDescriptions': [
              {
                  'HealthCheckPort': '80',
                  'Target': {
                      'Id': 'i-0f76fade',
                      'Port': 80,
                  },
                  'TargetHealth': {
                      'State': 'healthy',
                  },
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

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

        


  .. py:method:: modify_listener(**kwargs)

    

    Modifies the specified properties of the specified listener.

     

    Any properties that you do not specify retain their current values. However, changing the protocol from HTTPS to HTTP removes the security policy and SSL certificate properties. If you change the protocol from HTTP to HTTPS, you must add the security policy and server certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyListener>`_    


    **Request Syntax** 
    ::

      response = client.modify_listener(
          ListenerArn='string',
          Port=123,
          Protocol='HTTP'|'HTTPS'|'TCP',
          SslPolicy='string',
          Certificates=[
              {
                  'CertificateArn': 'string',
                  'IsDefault': True|False
              },
          ],
          DefaultActions=[
              {
                  'Type': 'forward',
                  'TargetGroupArn': 'string'
              },
          ]
      )
    :type ListenerArn: string
    :param ListenerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the listener.

      

    
    :type Port: integer
    :param Port: 

      The port for connections from clients to the load balancer.

      

    
    :type Protocol: string
    :param Protocol: 

      The protocol for connections from clients to the load balancer. Application Load Balancers support HTTP and HTTPS and Network Load Balancers support TCP.

      

    
    :type SslPolicy: string
    :param SslPolicy: 

      The security policy that defines which protocols and ciphers are supported. For more information, see `Security Policies <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies>`__ in the *Application Load Balancers Guide* .

      

    
    :type Certificates: list
    :param Certificates: 

      The default SSL server certificate.

      

    
      - *(dict) --* 

        Information about an SSL server certificate.

        

      
        - **CertificateArn** *(string) --* 

          The Amazon Resource Name (ARN) of the certificate.

          

        
        - **IsDefault** *(boolean) --* 

          Indicates whether the certificate is the default certificate.

          

        
      
  
    :type DefaultActions: list
    :param DefaultActions: 

      The default action. For Application Load Balancers, the protocol of the specified target group must be HTTP or HTTPS. For Network Load Balancers, the protocol of the specified target group must be TCP.

      

    
      - *(dict) --* 

        Information about an action.

        

      
        - **Type** *(string) --* **[REQUIRED]** 

          The type of action.

          

        
        - **TargetGroupArn** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the target group.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Listeners': [
                {
                    'ListenerArn': 'string',
                    'LoadBalancerArn': 'string',
                    'Port': 123,
                    'Protocol': 'HTTP'|'HTTPS'|'TCP',
                    'Certificates': [
                        {
                            'CertificateArn': 'string',
                            'IsDefault': True|False
                        },
                    ],
                    'SslPolicy': 'string',
                    'DefaultActions': [
                        {
                            'Type': 'forward',
                            'TargetGroupArn': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Listeners** *(list) --* 

          Information about the modified listeners.

          
          

          - *(dict) --* 

            Information about a listener.

            
            

            - **ListenerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the listener.

              
            

            - **LoadBalancerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the load balancer.

              
            

            - **Port** *(integer) --* 

              The port on which the load balancer is listening.

              
            

            - **Protocol** *(string) --* 

              The protocol for connections from clients to the load balancer.

              
            

            - **Certificates** *(list) --* 

              The SSL server certificate. You must provide a certificate if the protocol is HTTPS.

              
              

              - *(dict) --* 

                Information about an SSL server certificate.

                
                

                - **CertificateArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the certificate.

                  
                

                - **IsDefault** *(boolean) --* 

                  Indicates whether the certificate is the default certificate.

                  
            
          
            

            - **SslPolicy** *(string) --* 

              The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.

              
            

            - **DefaultActions** *(list) --* 

              The default actions for the listener.

              
              

              - *(dict) --* 

                Information about an action.

                
                

                - **Type** *(string) --* 

                  The type of action.

                  
                

                - **TargetGroupArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the target group.

                  
            
          
        
      
    

    **Examples** 

    This example changes the default action for the specified listener.
    ::

      response = client.modify_listener(
          DefaultActions=[
              {
                  'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f',
                  'Type': 'forward',
              },
          ],
          ListenerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Listeners': [
              {
                  'DefaultActions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f',
                          'Type': 'forward',
                      },
                  ],
                  'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2',
                  'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  'Port': 80,
                  'Protocol': 'HTTP',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example changes the server certificate for the specified HTTPS listener.
    ::

      response = client.modify_listener(
          Certificates=[
              {
                  'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-new-server-cert',
              },
          ],
          ListenerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Listeners': [
              {
                  'Certificates': [
                      {
                          'CertificateArn': 'arn:aws:iam::123456789012:server-certificate/my-new-server-cert',
                      },
                  ],
                  'DefaultActions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                          'Type': 'forward',
                      },
                  ],
                  'ListenerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65',
                  'LoadBalancerArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  'Port': 443,
                  'Protocol': 'HTTPS',
                  'SslPolicy': 'ELBSecurityPolicy-2015-05',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: modify_load_balancer_attributes(**kwargs)

    

    Modifies the specified attributes of the specified Application Load Balancer or Network Load Balancer.

     

    If any of the specified attributes can't be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes>`_    


    **Request Syntax** 
    ::

      response = client.modify_load_balancer_attributes(
          LoadBalancerArn='string',
          Attributes=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type Attributes: list
    :param Attributes: **[REQUIRED]** 

      The load balancer attributes.

      

    
      - *(dict) --* 

        Information about a load balancer attribute.

        

      
        - **Key** *(string) --* 

          The name of the attribute.

           

           
          * ``access_logs.s3.enabled`` - [Application Load Balancers] Indicates whether access logs stored in Amazon S3 are enabled. The value is ``true`` or ``false`` . 
           
          * ``access_logs.s3.bucket`` - [Application Load Balancers] The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket. 
           
          * ``access_logs.s3.prefix`` - [Application Load Balancers] The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket. 
           
          * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The value is ``true`` or ``false`` . 
           
          * ``idle_timeout.timeout_seconds`` - [Application Load Balancers] The idle timeout value, in seconds. The valid range is 1-4000. The default is 60 seconds. 
           

          

        
        - **Value** *(string) --* 

          The value of the attribute.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Attributes': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Attributes** *(list) --* 

          Information about the load balancer attributes.

          
          

          - *(dict) --* 

            Information about a load balancer attribute.

            
            

            - **Key** *(string) --* 

              The name of the attribute.

               

               
              * ``access_logs.s3.enabled`` - [Application Load Balancers] Indicates whether access logs stored in Amazon S3 are enabled. The value is ``true`` or ``false`` . 
               
              * ``access_logs.s3.bucket`` - [Application Load Balancers] The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket. 
               
              * ``access_logs.s3.prefix`` - [Application Load Balancers] The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket. 
               
              * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The value is ``true`` or ``false`` . 
               
              * ``idle_timeout.timeout_seconds`` - [Application Load Balancers] The idle timeout value, in seconds. The valid range is 1-4000. The default is 60 seconds. 
               

              
            

            - **Value** *(string) --* 

              The value of the attribute.

              
        
      
    

    **Examples** 

    This example enables deletion protection for the specified load balancer.
    ::

      response = client.modify_load_balancer_attributes(
          Attributes=[
              {
                  'Key': 'deletion_protection.enabled',
                  'Value': 'true',
              },
          ],
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Attributes': [
              {
                  'Key': 'deletion_protection.enabled',
                  'Value': 'true',
              },
              {
                  'Key': 'access_logs.s3.enabled',
                  'Value': 'false',
              },
              {
                  'Key': 'idle_timeout.timeout_seconds',
                  'Value': '60',
              },
              {
                  'Key': 'access_logs.s3.prefix',
                  'Value': '',
              },
              {
                  'Key': 'access_logs.s3.bucket',
                  'Value': '',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example changes the idle timeout value for the specified load balancer.
    ::

      response = client.modify_load_balancer_attributes(
          Attributes=[
              {
                  'Key': 'idle_timeout.timeout_seconds',
                  'Value': '30',
              },
          ],
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Attributes': [
              {
                  'Key': 'idle_timeout.timeout_seconds',
                  'Value': '30',
              },
              {
                  'Key': 'access_logs.s3.enabled',
                  'Value': 'false',
              },
              {
                  'Key': 'access_logs.s3.prefix',
                  'Value': '',
              },
              {
                  'Key': 'deletion_protection.enabled',
                  'Value': 'true',
              },
              {
                  'Key': 'access_logs.s3.bucket',
                  'Value': '',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example enables access logs for the specified load balancer. Note that the S3 bucket must exist in the same region as the load balancer and must have a policy attached that grants access to the Elastic Load Balancing service.
    ::

      response = client.modify_load_balancer_attributes(
          Attributes=[
              {
                  'Key': 'access_logs.s3.enabled',
                  'Value': 'true',
              },
              {
                  'Key': 'access_logs.s3.bucket',
                  'Value': 'my-loadbalancer-logs',
              },
              {
                  'Key': 'access_logs.s3.prefix',
                  'Value': 'myapp',
              },
          ],
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Attributes': [
              {
                  'Key': 'access_logs.s3.enabled',
                  'Value': 'true',
              },
              {
                  'Key': 'access_logs.s3.bucket',
                  'Value': 'my-load-balancer-logs',
              },
              {
                  'Key': 'access_logs.s3.prefix',
                  'Value': 'myapp',
              },
              {
                  'Key': 'idle_timeout.timeout_seconds',
                  'Value': '60',
              },
              {
                  'Key': 'deletion_protection.enabled',
                  'Value': 'false',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: modify_rule(**kwargs)

    

    Modifies the specified rule.

     

    Any existing properties that you do not modify retain their current values.

     

    To modify the default action, use  ModifyListener .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyRule>`_    


    **Request Syntax** 
    ::

      response = client.modify_rule(
          RuleArn='string',
          Conditions=[
              {
                  'Field': 'string',
                  'Values': [
                      'string',
                  ]
              },
          ],
          Actions=[
              {
                  'Type': 'forward',
                  'TargetGroupArn': 'string'
              },
          ]
      )
    :type RuleArn: string
    :param RuleArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the rule.

      

    
    :type Conditions: list
    :param Conditions: 

      The conditions.

      

    
      - *(dict) --* 

        Information about a condition for a rule.

        

      
        - **Field** *(string) --* 

          The name of the field. The possible values are ``host-header`` and ``path-pattern`` .

          

        
        - **Values** *(list) --* 

          The condition value.

           

          If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

           

           
          * A-Z, a-z, 0-9 
           
          * - . 
           
          * * (matches 0 or more characters) 
           
          * ? (matches exactly 1 character) 
           

           

          If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

           

           
          * A-Z, a-z, 0-9 
           
          * _ - . $ / ~ " ' @ : + 
           
          * & (using &amp;) 
           
          * * (matches 0 or more characters) 
           
          * ? (matches exactly 1 character) 
           

          

        
          - *(string) --* 

          
      
      
  
    :type Actions: list
    :param Actions: 

      The actions. The target group must use the HTTP or HTTPS protocol.

      

    
      - *(dict) --* 

        Information about an action.

        

      
        - **Type** *(string) --* **[REQUIRED]** 

          The type of action.

          

        
        - **TargetGroupArn** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the target group.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rules': [
                {
                    'RuleArn': 'string',
                    'Priority': 'string',
                    'Conditions': [
                        {
                            'Field': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'Actions': [
                        {
                            'Type': 'forward',
                            'TargetGroupArn': 'string'
                        },
                    ],
                    'IsDefault': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rules** *(list) --* 

          Information about the rule.

          
          

          - *(dict) --* 

            Information about a rule.

            
            

            - **RuleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the rule.

              
            

            - **Priority** *(string) --* 

              The priority.

              
            

            - **Conditions** *(list) --* 

              The conditions.

              
              

              - *(dict) --* 

                Information about a condition for a rule.

                
                

                - **Field** *(string) --* 

                  The name of the field. The possible values are ``host-header`` and ``path-pattern`` .

                  
                

                - **Values** *(list) --* 

                  The condition value.

                   

                  If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

                   

                   
                  * A-Z, a-z, 0-9 
                   
                  * - . 
                   
                  * * (matches 0 or more characters) 
                   
                  * ? (matches exactly 1 character) 
                   

                   

                  If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

                   

                   
                  * A-Z, a-z, 0-9 
                   
                  * _ - . $ / ~ " ' @ : + 
                   
                  * & (using &amp;) 
                   
                  * * (matches 0 or more characters) 
                   
                  * ? (matches exactly 1 character) 
                   

                  
                  

                  - *(string) --* 
              
            
          
            

            - **Actions** *(list) --* 

              The actions.

              
              

              - *(dict) --* 

                Information about an action.

                
                

                - **Type** *(string) --* 

                  The type of action.

                  
                

                - **TargetGroupArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the target group.

                  
            
          
            

            - **IsDefault** *(boolean) --* 

              Indicates whether this is the default rule.

              
        
      
    

    **Examples** 

    This example modifies the condition for the specified rule.
    ::

      response = client.modify_rule(
          Conditions=[
              {
                  'Field': 'path-pattern',
                  'Values': [
                      '/images/*',
                  ],
              },
          ],
          RuleArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Rules': [
              {
                  'Actions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                          'Type': 'forward',
                      },
                  ],
                  'Conditions': [
                      {
                          'Field': 'path-pattern',
                          'Values': [
                              '/images/*',
                          ],
                      },
                  ],
                  'IsDefault': False,
                  'Priority': '10',
                  'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: modify_target_group(**kwargs)

    

    Modifies the health checks used when evaluating the health state of the targets in the specified target group.

     

    To monitor the health of the targets, use  DescribeTargetHealth .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup>`_    


    **Request Syntax** 
    ::

      response = client.modify_target_group(
          TargetGroupArn='string',
          HealthCheckProtocol='HTTP'|'HTTPS'|'TCP',
          HealthCheckPort='string',
          HealthCheckPath='string',
          HealthCheckIntervalSeconds=123,
          HealthCheckTimeoutSeconds=123,
          HealthyThresholdCount=123,
          UnhealthyThresholdCount=123,
          Matcher={
              'HttpCode': 'string'
          }
      )
    :type TargetGroupArn: string
    :param TargetGroupArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the target group.

      

    
    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: 

      The protocol the load balancer uses when performing health checks on targets. The TCP protocol is supported only if the protocol of the target group is TCP.

      

    
    :type HealthCheckPort: string
    :param HealthCheckPort: 

      The port the load balancer uses when performing health checks on targets.

      

    
    :type HealthCheckPath: string
    :param HealthCheckPath: 

      [HTTP/HTTPS health checks] The ping path that is the destination for the health check request.

      

    
    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: 

      The approximate amount of time, in seconds, between health checks of an individual target. For Application Load Balancers, the range is 5 to 300 seconds. For Network Load Balancers, the supported values are 10 or 30 seconds.

      

    
    :type HealthCheckTimeoutSeconds: integer
    :param HealthCheckTimeoutSeconds: 

      [HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.

      

    
    :type HealthyThresholdCount: integer
    :param HealthyThresholdCount: 

      The number of consecutive health checks successes required before considering an unhealthy target healthy.

      

    
    :type UnhealthyThresholdCount: integer
    :param UnhealthyThresholdCount: 

      The number of consecutive health check failures required before considering the target unhealthy. For Network Load Balancers, this value must be the same as the healthy threshold count.

      

    
    :type Matcher: dict
    :param Matcher: 

      [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a target.

      

    
      - **HttpCode** *(string) --* **[REQUIRED]** 

        The HTTP codes.

         

        For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").

         

        For Network Load Balancers, this is 200 to 399.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TargetGroups': [
                {
                    'TargetGroupArn': 'string',
                    'TargetGroupName': 'string',
                    'Protocol': 'HTTP'|'HTTPS'|'TCP',
                    'Port': 123,
                    'VpcId': 'string',
                    'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP',
                    'HealthCheckPort': 'string',
                    'HealthCheckIntervalSeconds': 123,
                    'HealthCheckTimeoutSeconds': 123,
                    'HealthyThresholdCount': 123,
                    'UnhealthyThresholdCount': 123,
                    'HealthCheckPath': 'string',
                    'Matcher': {
                        'HttpCode': 'string'
                    },
                    'LoadBalancerArns': [
                        'string',
                    ],
                    'TargetType': 'instance'|'ip'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TargetGroups** *(list) --* 

          Information about the target group.

          
          

          - *(dict) --* 

            Information about a target group.

            
            

            - **TargetGroupArn** *(string) --* 

              The Amazon Resource Name (ARN) of the target group.

              
            

            - **TargetGroupName** *(string) --* 

              The name of the target group.

              
            

            - **Protocol** *(string) --* 

              The protocol to use for routing traffic to the targets.

              
            

            - **Port** *(integer) --* 

              The port on which the targets are listening.

              
            

            - **VpcId** *(string) --* 

              The ID of the VPC for the targets.

              
            

            - **HealthCheckProtocol** *(string) --* 

              The protocol to use to connect with the target.

              
            

            - **HealthCheckPort** *(string) --* 

              The port to use to connect with the target.

              
            

            - **HealthCheckIntervalSeconds** *(integer) --* 

              The approximate amount of time, in seconds, between health checks of an individual target.

              
            

            - **HealthCheckTimeoutSeconds** *(integer) --* 

              The amount of time, in seconds, during which no response means a failed health check.

              
            

            - **HealthyThresholdCount** *(integer) --* 

              The number of consecutive health checks successes required before considering an unhealthy target healthy.

              
            

            - **UnhealthyThresholdCount** *(integer) --* 

              The number of consecutive health check failures required before considering the target unhealthy.

              
            

            - **HealthCheckPath** *(string) --* 

              The destination for the health check request.

              
            

            - **Matcher** *(dict) --* 

              The HTTP codes to use when checking for a successful response from a target.

              
              

              - **HttpCode** *(string) --* 

                The HTTP codes.

                 

                For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").

                 

                For Network Load Balancers, this is 200 to 399.

                
          
            

            - **LoadBalancerArns** *(list) --* 

              The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.

              
              

              - *(string) --* 
          
            

            - **TargetType** *(string) --* 

              The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address).

              
        
      
    

    **Examples** 

    This example changes the configuration of the health checks used to evaluate the health of the targets for the specified target group.
    ::

      response = client.modify_target_group(
          HealthCheckPort='443',
          HealthCheckProtocol='HTTPS',
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'TargetGroups': [
              {
                  'HealthCheckIntervalSeconds': 30,
                  'HealthCheckPort': '443',
                  'HealthCheckProtocol': 'HTTPS',
                  'HealthCheckTimeoutSeconds': 5,
                  'HealthyThresholdCount': 5,
                  'LoadBalancerArns': [
                      'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
                  ],
                  'Matcher': {
                      'HttpCode': '200',
                  },
                  'Port': 443,
                  'Protocol': 'HTTPS',
                  'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f',
                  'TargetGroupName': 'my-https-targets',
                  'UnhealthyThresholdCount': 2,
                  'VpcId': 'vpc-3ac0fb5f',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: modify_target_group_attributes(**kwargs)

    

    Modifies the specified attributes of the specified target group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes>`_    


    **Request Syntax** 
    ::

      response = client.modify_target_group_attributes(
          TargetGroupArn='string',
          Attributes=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type TargetGroupArn: string
    :param TargetGroupArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the target group.

      

    
    :type Attributes: list
    :param Attributes: **[REQUIRED]** 

      The attributes.

      

    
      - *(dict) --* 

        Information about a target group attribute.

        

      
        - **Key** *(string) --* 

          The name of the attribute.

           

           
          * ``deregistration_delay.timeout_seconds`` - The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. 
           
          * ``proxy_protocol_v2.enabled`` - [Network Load Balancers] Indicates whether Proxy Protocol version 2 is enabled. 
           
          * ``stickiness.enabled`` - [Application Load Balancers] Indicates whether sticky sessions are enabled. The value is ``true`` or ``false`` . 
           
          * ``stickiness.type`` - [Application Load Balancers] The type of sticky sessions. The possible value is ``lb_cookie`` . 
           
          * ``stickiness.lb_cookie.duration_seconds`` - [Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds). 
           

          

        
        - **Value** *(string) --* 

          The value of the attribute.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Attributes': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Attributes** *(list) --* 

          Information about the attributes.

          
          

          - *(dict) --* 

            Information about a target group attribute.

            
            

            - **Key** *(string) --* 

              The name of the attribute.

               

               
              * ``deregistration_delay.timeout_seconds`` - The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. 
               
              * ``proxy_protocol_v2.enabled`` - [Network Load Balancers] Indicates whether Proxy Protocol version 2 is enabled. 
               
              * ``stickiness.enabled`` - [Application Load Balancers] Indicates whether sticky sessions are enabled. The value is ``true`` or ``false`` . 
               
              * ``stickiness.type`` - [Application Load Balancers] The type of sticky sessions. The possible value is ``lb_cookie`` . 
               
              * ``stickiness.lb_cookie.duration_seconds`` - [Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds). 
               

              
            

            - **Value** *(string) --* 

              The value of the attribute.

              
        
      
    

    **Examples** 

    This example sets the deregistration delay timeout to the specified value for the specified target group.
    ::

      response = client.modify_target_group_attributes(
          Attributes=[
              {
                  'Key': 'deregistration_delay.timeout_seconds',
                  'Value': '600',
              },
          ],
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Attributes': [
              {
                  'Key': 'stickiness.enabled',
                  'Value': 'false',
              },
              {
                  'Key': 'deregistration_delay.timeout_seconds',
                  'Value': '600',
              },
              {
                  'Key': 'stickiness.type',
                  'Value': 'lb_cookie',
              },
              {
                  'Key': 'stickiness.lb_cookie.duration_seconds',
                  'Value': '86400',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: register_targets(**kwargs)

    

    Registers the specified targets with the specified target group.

     

    You can register targets by instance ID or by IP address. If the target is an EC2 instance, it must be in the ``running`` state when you register it.

     

    By default, the load balancer routes requests to registered targets using the protocol and port for the target group. Alternatively, you can override the port for a target when you register it. You can register each EC2 instance or IP address with the same target group multiple times using different ports.

     

    With a Network Load Balancer, you cannot register instances by instance ID if they have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1. You can register instances of these types by IP address.

     

    To remove a target from a target group, use  DeregisterTargets .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RegisterTargets>`_    


    **Request Syntax** 
    ::

      response = client.register_targets(
          TargetGroupArn='string',
          Targets=[
              {
                  'Id': 'string',
                  'Port': 123,
                  'AvailabilityZone': 'string'
              },
          ]
      )
    :type TargetGroupArn: string
    :param TargetGroupArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the target group.

      

    
    :type Targets: list
    :param Targets: **[REQUIRED]** 

      The targets.

      

    
      - *(dict) --* 

        Information about a target.

        

      
        - **Id** *(string) --* **[REQUIRED]** 

          The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.

          

        
        - **Port** *(integer) --* 

          The port on which the target is listening.

          

        
        - **AvailabilityZone** *(string) --* 

          An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.

           

          This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.

           

          With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example registers the specified instances with the specified target group.
    ::

      response = client.register_targets(
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
          Targets=[
              {
                  'Id': 'i-80c8dd94',
              },
              {
                  'Id': 'i-ceddcd4d',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

    This example registers the specified instance with the specified target group using multiple ports. This enables you to register ECS containers on the same instance as targets in the target group.
    ::

      response = client.register_targets(
          TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/3bb63f11dfb0faf9',
          Targets=[
              {
                  'Id': 'i-80c8dd94',
                  'Port': 80,
              },
              {
                  'Id': 'i-80c8dd94',
                  'Port': 766,
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: remove_listener_certificates(**kwargs)

    

    Removes the specified certificate from the specified secure listener.

     

    You can't remove the default certificate for a listener. To replace the default certificate, call  ModifyListener .

     

    To list the certificates for your listener, use  DescribeListenerCertificates .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates>`_    


    **Request Syntax** 
    ::

      response = client.remove_listener_certificates(
          ListenerArn='string',
          Certificates=[
              {
                  'CertificateArn': 'string',
                  'IsDefault': True|False
              },
          ]
      )
    :type ListenerArn: string
    :param ListenerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the listener.

      

    
    :type Certificates: list
    :param Certificates: **[REQUIRED]** 

      The certificate to remove. You can specify one certificate per call.

      

    
      - *(dict) --* 

        Information about an SSL server certificate.

        

      
        - **CertificateArn** *(string) --* 

          The Amazon Resource Name (ARN) of the certificate.

          

        
        - **IsDefault** *(boolean) --* 

          Indicates whether the certificate is the default certificate.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: remove_tags(**kwargs)

    

    Removes the specified tags from the specified Elastic Load Balancing resource.

     

    To list the current tags for your resources, use  DescribeTags .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RemoveTags>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags(
          ResourceArns=[
              'string',
          ],
          TagKeys=[
              'string',
          ]
      )
    :type ResourceArns: list
    :param ResourceArns: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resource.

      

    
      - *(string) --* 

      
  
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      The tag keys for the tags to remove.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    This example removes the specified tags from the specified load balancer.
    ::

      response = client.remove_tags(
          ResourceArns=[
              'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
          ],
          TagKeys=[
              'project',
              'department',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_ip_address_type(**kwargs)

    

    Sets the type of IP addresses used by the subnets of the specified Application Load Balancer or Network Load Balancer.

     

    Note that Network Load Balancers must use ``ipv4`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetIpAddressType>`_    


    **Request Syntax** 
    ::

      response = client.set_ip_address_type(
          LoadBalancerArn='string',
          IpAddressType='ipv4'|'dualstack'
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type IpAddressType: string
    :param IpAddressType: **[REQUIRED]** 

      The IP address type. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses). Internal load balancers must use ``ipv4`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IpAddressType': 'ipv4'|'dualstack'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **IpAddressType** *(string) --* 

          The IP address type.

          
    

  .. py:method:: set_rule_priorities(**kwargs)

    

    Sets the priorities of the specified rules.

     

    You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetRulePriorities>`_    


    **Request Syntax** 
    ::

      response = client.set_rule_priorities(
          RulePriorities=[
              {
                  'RuleArn': 'string',
                  'Priority': 123
              },
          ]
      )
    :type RulePriorities: list
    :param RulePriorities: **[REQUIRED]** 

      The rule priorities.

      

    
      - *(dict) --* 

        Information about the priorities for the rules for a listener.

        

      
        - **RuleArn** *(string) --* 

          The Amazon Resource Name (ARN) of the rule.

          

        
        - **Priority** *(integer) --* 

          The rule priority.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rules': [
                {
                    'RuleArn': 'string',
                    'Priority': 'string',
                    'Conditions': [
                        {
                            'Field': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'Actions': [
                        {
                            'Type': 'forward',
                            'TargetGroupArn': 'string'
                        },
                    ],
                    'IsDefault': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rules** *(list) --* 

          Information about the rules.

          
          

          - *(dict) --* 

            Information about a rule.

            
            

            - **RuleArn** *(string) --* 

              The Amazon Resource Name (ARN) of the rule.

              
            

            - **Priority** *(string) --* 

              The priority.

              
            

            - **Conditions** *(list) --* 

              The conditions.

              
              

              - *(dict) --* 

                Information about a condition for a rule.

                
                

                - **Field** *(string) --* 

                  The name of the field. The possible values are ``host-header`` and ``path-pattern`` .

                  
                

                - **Values** *(list) --* 

                  The condition value.

                   

                  If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

                   

                   
                  * A-Z, a-z, 0-9 
                   
                  * - . 
                   
                  * * (matches 0 or more characters) 
                   
                  * ? (matches exactly 1 character) 
                   

                   

                  If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.

                   

                   
                  * A-Z, a-z, 0-9 
                   
                  * _ - . $ / ~ " ' @ : + 
                   
                  * & (using &amp;) 
                   
                  * * (matches 0 or more characters) 
                   
                  * ? (matches exactly 1 character) 
                   

                  
                  

                  - *(string) --* 
              
            
          
            

            - **Actions** *(list) --* 

              The actions.

              
              

              - *(dict) --* 

                Information about an action.

                
                

                - **Type** *(string) --* 

                  The type of action.

                  
                

                - **TargetGroupArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the target group.

                  
            
          
            

            - **IsDefault** *(boolean) --* 

              Indicates whether this is the default rule.

              
        
      
    

    **Examples** 

    This example sets the priority of the specified rule.
    ::

      response = client.set_rule_priorities(
          RulePriorities=[
              {
                  'Priority': 5,
                  'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3',
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Rules': [
              {
                  'Actions': [
                      {
                          'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                          'Type': 'forward',
                      },
                  ],
                  'Conditions': [
                      {
                          'Field': 'path-pattern',
                          'Values': [
                              '/img/*',
                          ],
                      },
                  ],
                  'IsDefault': False,
                  'Priority': '5',
                  'RuleArn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_security_groups(**kwargs)

    

    Associates the specified security groups with the specified Application Load Balancer. The specified security groups override the previously associated security groups.

     

    Note that you can't specify a security group for a Network Load Balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetSecurityGroups>`_    


    **Request Syntax** 
    ::

      response = client.set_security_groups(
          LoadBalancerArn='string',
          SecurityGroups=[
              'string',
          ]
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type SecurityGroups: list
    :param SecurityGroups: **[REQUIRED]** 

      The IDs of the security groups.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SecurityGroupIds': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SecurityGroupIds** *(list) --* 

          The IDs of the security groups associated with the load balancer.

          
          

          - *(string) --* 
      
    

    **Examples** 

    This example associates the specified security group with the specified load balancer.
    ::

      response = client.set_security_groups(
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
          SecurityGroups=[
              'sg-5943793c',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SecurityGroupIds': [
              'sg-5943793c',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_subnets(**kwargs)

    

    Enables the Availability Zone for the specified subnets for the specified Application Load Balancer. The specified subnets replace the previously enabled subnets.

     

    Note that you can't change the subnets for a Network Load Balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetSubnets>`_    


    **Request Syntax** 
    ::

      response = client.set_subnets(
          LoadBalancerArn='string',
          Subnets=[
              'string',
          ],
          SubnetMappings=[
              {
                  'SubnetId': 'string',
                  'AllocationId': 'string'
              },
          ]
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type Subnets: list
    :param Subnets: **[REQUIRED]** 

      The IDs of the subnets. You must specify subnets from at least two Availability Zones. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.

      

    
      - *(string) --* 

      
  
    :type SubnetMappings: list
    :param SubnetMappings: 

      The IDs of the subnets. You must specify subnets from at least two Availability Zones. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.

       

      You cannot specify Elastic IP addresses for your subnets.

      

    
      - *(dict) --* 

        Information about a subnet mapping.

        

      
        - **SubnetId** *(string) --* 

          The ID of the subnet.

          

        
        - **AllocationId** *(string) --* 

          [Network Load Balancers] The allocation ID of the Elastic IP address.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AvailabilityZones': [
                {
                    'ZoneName': 'string',
                    'SubnetId': 'string',
                    'LoadBalancerAddresses': [
                        {
                            'IpAddress': 'string',
                            'AllocationId': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AvailabilityZones** *(list) --* 

          Information about the subnet and Availability Zone.

          
          

          - *(dict) --* 

            Information about an Availability Zone.

            
            

            - **ZoneName** *(string) --* 

              The name of the Availability Zone.

              
            

            - **SubnetId** *(string) --* 

              The ID of the subnet.

              
            

            - **LoadBalancerAddresses** *(list) --* 

              [Network Load Balancers] The static IP address.

              
              

              - *(dict) --* 

                Information about a static IP address for a load balancer.

                
                

                - **IpAddress** *(string) --* 

                  The static IP address.

                  
                

                - **AllocationId** *(string) --* 

                  [Network Load Balancers] The allocation ID of the Elastic IP address.

                  
            
          
        
      
    

    **Examples** 

    This example enables the Availability Zones for the specified subnets for the specified load balancer.
    ::

      response = client.set_subnets(
          LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188',
          Subnets=[
              'subnet-8360a9e7',
              'subnet-b7d581c0',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AvailabilityZones': [
              {
                  'SubnetId': 'subnet-8360a9e7',
                  'ZoneName': 'us-west-2a',
              },
              {
                  'SubnetId': 'subnet-b7d581c0',
                  'ZoneName': 'us-west-2b',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:

* :py:class:`ElasticLoadBalancingv2.Paginator.DescribeListeners`


* :py:class:`ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers`


* :py:class:`ElasticLoadBalancingv2.Paginator.DescribeTargetGroups`



.. py:class:: ElasticLoadBalancingv2.Paginator.DescribeListeners

  ::

    
    paginator = client.get_paginator('describe_listeners')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElasticLoadBalancingv2.Client.describe_listeners`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListeners>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          LoadBalancerArn='string',
          ListenerArns=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type ListenerArns: list
    :param ListenerArns: 

      The Amazon Resource Names (ARN) of the listeners.

      

    
      - *(string) --* 

      
  
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
            'Listeners': [
                {
                    'ListenerArn': 'string',
                    'LoadBalancerArn': 'string',
                    'Port': 123,
                    'Protocol': 'HTTP'|'HTTPS'|'TCP',
                    'Certificates': [
                        {
                            'CertificateArn': 'string',
                            'IsDefault': True|False
                        },
                    ],
                    'SslPolicy': 'string',
                    'DefaultActions': [
                        {
                            'Type': 'forward',
                            'TargetGroupArn': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Listeners** *(list) --* 

          Information about the listeners.

          
          

          - *(dict) --* 

            Information about a listener.

            
            

            - **ListenerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the listener.

              
            

            - **LoadBalancerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the load balancer.

              
            

            - **Port** *(integer) --* 

              The port on which the load balancer is listening.

              
            

            - **Protocol** *(string) --* 

              The protocol for connections from clients to the load balancer.

              
            

            - **Certificates** *(list) --* 

              The SSL server certificate. You must provide a certificate if the protocol is HTTPS.

              
              

              - *(dict) --* 

                Information about an SSL server certificate.

                
                

                - **CertificateArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the certificate.

                  
                

                - **IsDefault** *(boolean) --* 

                  Indicates whether the certificate is the default certificate.

                  
            
          
            

            - **SslPolicy** *(string) --* 

              The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.

              
            

            - **DefaultActions** *(list) --* 

              The default actions for the listener.

              
              

              - *(dict) --* 

                Information about an action.

                
                

                - **Type** *(string) --* 

                  The type of action.

                  
                

                - **TargetGroupArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the target group.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers

  ::

    
    paginator = client.get_paginator('describe_load_balancers')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElasticLoadBalancingv2.Client.describe_load_balancers`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          LoadBalancerArns=[
              'string',
          ],
          Names=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type LoadBalancerArns: list
    :param LoadBalancerArns: 

      The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.

      

    
      - *(string) --* 

      
  
    :type Names: list
    :param Names: 

      The names of the load balancers.

      

    
      - *(string) --* 

      
  
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
            'LoadBalancers': [
                {
                    'LoadBalancerArn': 'string',
                    'DNSName': 'string',
                    'CanonicalHostedZoneId': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'LoadBalancerName': 'string',
                    'Scheme': 'internet-facing'|'internal',
                    'VpcId': 'string',
                    'State': {
                        'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                        'Reason': 'string'
                    },
                    'Type': 'application'|'network',
                    'AvailabilityZones': [
                        {
                            'ZoneName': 'string',
                            'SubnetId': 'string',
                            'LoadBalancerAddresses': [
                                {
                                    'IpAddress': 'string',
                                    'AllocationId': 'string'
                                },
                            ]
                        },
                    ],
                    'SecurityGroups': [
                        'string',
                    ],
                    'IpAddressType': 'ipv4'|'dualstack'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LoadBalancers** *(list) --* 

          Information about the load balancers.

          
          

          - *(dict) --* 

            Information about a load balancer.

            
            

            - **LoadBalancerArn** *(string) --* 

              The Amazon Resource Name (ARN) of the load balancer.

              
            

            - **DNSName** *(string) --* 

              The public DNS name of the load balancer.

              
            

            - **CanonicalHostedZoneId** *(string) --* 

              The ID of the Amazon Route 53 hosted zone associated with the load balancer.

              
            

            - **CreatedTime** *(datetime) --* 

              The date and time the load balancer was created.

              
            

            - **LoadBalancerName** *(string) --* 

              The name of the load balancer.

              
            

            - **Scheme** *(string) --* 

              The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the Internet.

               

              The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.

              
            

            - **VpcId** *(string) --* 

              The ID of the VPC for the load balancer.

              
            

            - **State** *(dict) --* 

              The state of the load balancer.

              
              

              - **Code** *(string) --* 

                The state code. The initial state of the load balancer is ``provisioning`` . After the load balancer is fully set up and ready to route traffic, its state is ``active`` . If the load balancer could not be set up, its state is ``failed`` .

                
              

              - **Reason** *(string) --* 

                A description of the state.

                
          
            

            - **Type** *(string) --* 

              The type of load balancer.

              
            

            - **AvailabilityZones** *(list) --* 

              The Availability Zones for the load balancer.

              
              

              - *(dict) --* 

                Information about an Availability Zone.

                
                

                - **ZoneName** *(string) --* 

                  The name of the Availability Zone.

                  
                

                - **SubnetId** *(string) --* 

                  The ID of the subnet.

                  
                

                - **LoadBalancerAddresses** *(list) --* 

                  [Network Load Balancers] The static IP address.

                  
                  

                  - *(dict) --* 

                    Information about a static IP address for a load balancer.

                    
                    

                    - **IpAddress** *(string) --* 

                      The static IP address.

                      
                    

                    - **AllocationId** *(string) --* 

                      [Network Load Balancers] The allocation ID of the Elastic IP address.

                      
                
              
            
          
            

            - **SecurityGroups** *(list) --* 

              The IDs of the security groups for the load balancer.

              
              

              - *(string) --* 
          
            

            - **IpAddressType** *(string) --* 

              The type of IP addresses used by the subnets for your load balancer. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElasticLoadBalancingv2.Paginator.DescribeTargetGroups

  ::

    
    paginator = client.get_paginator('describe_target_groups')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElasticLoadBalancingv2.Client.describe_target_groups`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          LoadBalancerArn='string',
          TargetGroupArns=[
              'string',
          ],
          Names=[
              'string',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type LoadBalancerArn: string
    :param LoadBalancerArn: 

      The Amazon Resource Name (ARN) of the load balancer.

      

    
    :type TargetGroupArns: list
    :param TargetGroupArns: 

      The Amazon Resource Names (ARN) of the target groups.

      

    
      - *(string) --* 

      
  
    :type Names: list
    :param Names: 

      The names of the target groups.

      

    
      - *(string) --* 

      
  
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
            'TargetGroups': [
                {
                    'TargetGroupArn': 'string',
                    'TargetGroupName': 'string',
                    'Protocol': 'HTTP'|'HTTPS'|'TCP',
                    'Port': 123,
                    'VpcId': 'string',
                    'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP',
                    'HealthCheckPort': 'string',
                    'HealthCheckIntervalSeconds': 123,
                    'HealthCheckTimeoutSeconds': 123,
                    'HealthyThresholdCount': 123,
                    'UnhealthyThresholdCount': 123,
                    'HealthCheckPath': 'string',
                    'Matcher': {
                        'HttpCode': 'string'
                    },
                    'LoadBalancerArns': [
                        'string',
                    ],
                    'TargetType': 'instance'|'ip'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TargetGroups** *(list) --* 

          Information about the target groups.

          
          

          - *(dict) --* 

            Information about a target group.

            
            

            - **TargetGroupArn** *(string) --* 

              The Amazon Resource Name (ARN) of the target group.

              
            

            - **TargetGroupName** *(string) --* 

              The name of the target group.

              
            

            - **Protocol** *(string) --* 

              The protocol to use for routing traffic to the targets.

              
            

            - **Port** *(integer) --* 

              The port on which the targets are listening.

              
            

            - **VpcId** *(string) --* 

              The ID of the VPC for the targets.

              
            

            - **HealthCheckProtocol** *(string) --* 

              The protocol to use to connect with the target.

              
            

            - **HealthCheckPort** *(string) --* 

              The port to use to connect with the target.

              
            

            - **HealthCheckIntervalSeconds** *(integer) --* 

              The approximate amount of time, in seconds, between health checks of an individual target.

              
            

            - **HealthCheckTimeoutSeconds** *(integer) --* 

              The amount of time, in seconds, during which no response means a failed health check.

              
            

            - **HealthyThresholdCount** *(integer) --* 

              The number of consecutive health checks successes required before considering an unhealthy target healthy.

              
            

            - **UnhealthyThresholdCount** *(integer) --* 

              The number of consecutive health check failures required before considering the target unhealthy.

              
            

            - **HealthCheckPath** *(string) --* 

              The destination for the health check request.

              
            

            - **Matcher** *(dict) --* 

              The HTTP codes to use when checking for a successful response from a target.

              
              

              - **HttpCode** *(string) --* 

                The HTTP codes.

                 

                For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").

                 

                For Network Load Balancers, this is 200 to 399.

                
          
            

            - **LoadBalancerArns** *(list) --* 

              The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.

              
              

              - *(string) --* 
          
            

            - **TargetType** *(string) --* 

              The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address).

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    