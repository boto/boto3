

****************
ServiceDiscovery
****************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ServiceDiscovery.Client

  A low-level client representing Amazon Route 53 Auto Naming (ServiceDiscovery)::

    
    import boto3
    
    client = boto3.client('servicediscovery')

  
  These are the available methods:
  
  *   :py:meth:`~ServiceDiscovery.Client.can_paginate`

  
  *   :py:meth:`~ServiceDiscovery.Client.create_private_dns_namespace`

  
  *   :py:meth:`~ServiceDiscovery.Client.create_public_dns_namespace`

  
  *   :py:meth:`~ServiceDiscovery.Client.create_service`

  
  *   :py:meth:`~ServiceDiscovery.Client.delete_namespace`

  
  *   :py:meth:`~ServiceDiscovery.Client.delete_service`

  
  *   :py:meth:`~ServiceDiscovery.Client.deregister_instance`

  
  *   :py:meth:`~ServiceDiscovery.Client.generate_presigned_url`

  
  *   :py:meth:`~ServiceDiscovery.Client.get_instance`

  
  *   :py:meth:`~ServiceDiscovery.Client.get_instances_health_status`

  
  *   :py:meth:`~ServiceDiscovery.Client.get_namespace`

  
  *   :py:meth:`~ServiceDiscovery.Client.get_operation`

  
  *   :py:meth:`~ServiceDiscovery.Client.get_paginator`

  
  *   :py:meth:`~ServiceDiscovery.Client.get_service`

  
  *   :py:meth:`~ServiceDiscovery.Client.get_waiter`

  
  *   :py:meth:`~ServiceDiscovery.Client.list_instances`

  
  *   :py:meth:`~ServiceDiscovery.Client.list_namespaces`

  
  *   :py:meth:`~ServiceDiscovery.Client.list_operations`

  
  *   :py:meth:`~ServiceDiscovery.Client.list_services`

  
  *   :py:meth:`~ServiceDiscovery.Client.register_instance`

  
  *   :py:meth:`~ServiceDiscovery.Client.update_service`

  

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


  .. py:method:: create_private_dns_namespace(**kwargs)

    

    Creates a private namespace based on DNS, which will be visible only inside a specified Amazon VPC. The namespace defines your service naming scheme. For example, if you name your namespace ``example.com`` and name your service ``backend`` , the resulting DNS name for the service will be ``backend.example.com`` . You can associate more than one service with the same namespace.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/CreatePrivateDnsNamespace>`_    


    **Request Syntax** 
    ::

      response = client.create_private_dns_namespace(
          Name='string',
          CreatorRequestId='string',
          Description='string',
          Vpc='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name that you want to assign to this namespace. When you create a namespace, Amazon Route 53 automatically creates a hosted zone that has the same name as the namespace.

      

    
    :type CreatorRequestId: string
    :param CreatorRequestId: 

      An optional parameter that you can use to resolve concurrent creation requests. ``CreatorRequestId`` helps to determine if a specific client owns the namespace.

      This field is autopopulated if not provided.

    
    :type Description: string
    :param Description: 

      A description for the namespace.

      

    
    :type Vpc: string
    :param Vpc: **[REQUIRED]** 

      The ID of the Amazon VPC that you want to associate the namespace with.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OperationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OperationId** *(string) --* 

          A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .

          
    

  .. py:method:: create_public_dns_namespace(**kwargs)

    

    Creates a public namespace based on DNS, which will be visible on the internet. The namespace defines your service naming scheme. For example, if you name your namespace ``example.com`` and name your service ``backend`` , the resulting DNS name for the service will be ``backend.example.com`` . You can associate more than one service with the same namespace.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/CreatePublicDnsNamespace>`_    


    **Request Syntax** 
    ::

      response = client.create_public_dns_namespace(
          Name='string',
          CreatorRequestId='string',
          Description='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name that you want to assign to this namespace.

      

    
    :type CreatorRequestId: string
    :param CreatorRequestId: 

      An optional parameter that you can use to resolve concurrent creation requests. ``CreatorRequestId`` helps to determine if a specific client owns the namespace.

      This field is autopopulated if not provided.

    
    :type Description: string
    :param Description: 

      A description for the namespace.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OperationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OperationId** *(string) --* 

          A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .

          
    

  .. py:method:: create_service(**kwargs)

    

    Creates a service, which defines a template for the following entities:

     

     
    * One to five resource record sets 
     
    * Optionally, a health check 
     

     

    After you create the service, you can submit a  RegisterInstance request, and Amazon Route 53 uses the values in the template to create the specified entities. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/CreateService>`_    


    **Request Syntax** 
    ::

      response = client.create_service(
          Name='string',
          CreatorRequestId='string',
          Description='string',
          DnsConfig={
              'NamespaceId': 'string',
              'DnsRecords': [
                  {
                      'Type': 'SRV'|'A'|'AAAA',
                      'TTL': 123
                  },
              ]
          },
          HealthCheckConfig={
              'Type': 'HTTP'|'HTTPS'|'TCP',
              'ResourcePath': 'string',
              'FailureThreshold': 123
          }
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name that you want to assign to the service.

      

    
    :type CreatorRequestId: string
    :param CreatorRequestId: 

      An optional parameter that you can use to resolve concurrent creation requests. ``CreatorRequestId`` helps to determine if a specific client owns the namespace.

      This field is autopopulated if not provided.

    
    :type Description: string
    :param Description: 

      A description for the service.

      

    
    :type DnsConfig: dict
    :param DnsConfig: **[REQUIRED]** 

      A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance. 

      

    
      - **NamespaceId** *(string) --* **[REQUIRED]** 

        The ID of the namespace to use for DNS configuration.

        

      
      - **DnsRecords** *(list) --* **[REQUIRED]** 

        An array that contains one ``DnsRecord`` object for each resource record set that you want Amazon Route 53 to create when you register an instance.

        

      
        - *(dict) --* 

          A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

          

        
          - **Type** *(string) --* **[REQUIRED]** 

            The type of the resource, which indicates the value that Amazon Route 53 returns in response to DNS queries. The following values are supported:

             

             
            * **A** : Amazon Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44. 
             
            * **AAAA** : Amazon Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345. 
             
            * **SRV** : Amazon Route 53 returns the value for an SRV record. The value for an SRV record uses the following template, which can't be changed:  ``priority weight port resource-record-set-name``   The values of ``priority`` and ``weight`` are both set to 1. The value of port comes from the value that you specify for ``Port`` when you submit a  RegisterInstance request. 
             

            

          
          - **TTL** *(integer) --* **[REQUIRED]** 

            The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.

            

          
        
    
    
    :type HealthCheckConfig: dict
    :param HealthCheckConfig: 

       *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Amazon Route 53 associates the health check with all the resource record sets that you specify in ``DnsConfig`` .

       

      .. note::

         

        The health check uses 30 seconds as the request interval. This is the number of seconds between the time that each Amazon Route 53 health checker gets a response from your endpoint and the time that it sends the next health check request. A health checker in each data center around the world sends your endpoint a health check request every 30 seconds. On average, your endpoint receives a health check request about every two seconds. Health checkers in different data centers don't coordinate with one another, so you'll sometimes see several requests per second followed by a few seconds with no health checks at all.

         

       

      For information about the charges for health checks, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing>`__ .

      

    
      - **Type** *(string) --* 

        The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

         

        .. warning::

           

          You can't change the value of ``Type`` after you create a health check.

           

         

        You can create the following types of health checks:

         

         
        * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
         
        * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

        .. warning::

           If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

         
         
        * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
         

         

        For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

        

      
      - **ResourcePath** *(string) --* 

        The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Amazon Route 53 automatically adds the DNS name for the service and a leading forward slash (``/`` ) character. 

        

      
      - **FailureThreshold** *(integer) --* 

        The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Service': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'InstanceCount': 123,
                'DnsConfig': {
                    'NamespaceId': 'string',
                    'DnsRecords': [
                        {
                            'Type': 'SRV'|'A'|'AAAA',
                            'TTL': 123
                        },
                    ]
                },
                'HealthCheckConfig': {
                    'Type': 'HTTP'|'HTTPS'|'TCP',
                    'ResourcePath': 'string',
                    'FailureThreshold': 123
                },
                'CreateDate': datetime(2015, 1, 1),
                'CreatorRequestId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Service** *(dict) --* 

          A complex type that contains information about the new service.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to the service when you created it.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) that Amazon Route 53 assigns to the service when you create it.

            
          

          - **Name** *(string) --* 

            The name of the service.

            
          

          - **Description** *(string) --* 

            The description of the service.

            
          

          - **InstanceCount** *(integer) --* 

            The number of instances that are currently associated with the service. Instances that were previously associated with the service but that have been deleted are not included in the count.

            
          

          - **DnsConfig** *(dict) --* 

            A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

            
            

            - **NamespaceId** *(string) --* 

              The ID of the namespace to use for DNS configuration.

              
            

            - **DnsRecords** *(list) --* 

              An array that contains one ``DnsRecord`` object for each resource record set that you want Amazon Route 53 to create when you register an instance.

              
              

              - *(dict) --* 

                A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

                
                

                - **Type** *(string) --* 

                  The type of the resource, which indicates the value that Amazon Route 53 returns in response to DNS queries. The following values are supported:

                   

                   
                  * **A** : Amazon Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44. 
                   
                  * **AAAA** : Amazon Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345. 
                   
                  * **SRV** : Amazon Route 53 returns the value for an SRV record. The value for an SRV record uses the following template, which can't be changed:  ``priority weight port resource-record-set-name``   The values of ``priority`` and ``weight`` are both set to 1. The value of port comes from the value that you specify for ``Port`` when you submit a  RegisterInstance request. 
                   

                  
                

                - **TTL** *(integer) --* 

                  The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.

                  
            
          
        
          

          - **HealthCheckConfig** *(dict) --* 

             *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Amazon Route 53 associates the health check with all the resource record sets that you specify in ``DnsConfig`` .

             

            .. note::

               

              The health check uses 30 seconds as the request interval. This is the number of seconds between the time that each Amazon Route 53 health checker gets a response from your endpoint and the time that it sends the next health check request. A health checker in each data center around the world sends your endpoint a health check request every 30 seconds. On average, your endpoint receives a health check request about every two seconds. Health checkers in different data centers don't coordinate with one another, so you'll sometimes see several requests per second followed by a few seconds with no health checks at all.

               

             

            For information about the charges for health checks, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing>`__ .

            
            

            - **Type** *(string) --* 

              The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

               

              .. warning::

                 

                You can't change the value of ``Type`` after you create a health check.

                 

               

              You can create the following types of health checks:

               

               
              * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
               
              * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

              .. warning::

                 If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

               
               
              * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
               

               

              For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

              
            

            - **ResourcePath** *(string) --* 

              The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Amazon Route 53 automatically adds the DNS name for the service and a leading forward slash (``/`` ) character. 

              
            

            - **FailureThreshold** *(integer) --* 

              The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

              
        
          

          - **CreateDate** *(datetime) --* 

            The date and time that the service was created, in Unix format and Coordinated Universal Time (UTC).

            
          

          - **CreatorRequestId** *(string) --* 

            An optional parameter that you can use to resolve concurrent creation requests. ``CreatorRequestId`` helps to determine if a specific client owns the namespace.

            
      
    

  .. py:method:: delete_namespace(**kwargs)

    

    Deletes a namespace from the current account. If the namespace still contains one or more services, the request fails.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/DeleteNamespace>`_    


    **Request Syntax** 
    ::

      response = client.delete_namespace(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the namespace that you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OperationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OperationId** *(string) --* 

          A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .

          
    

  .. py:method:: delete_service(**kwargs)

    

    Deletes a specified service. If the service still contains one or more registered instances, the request fails.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/DeleteService>`_    


    **Request Syntax** 
    ::

      response = client.delete_service(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the service that you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: deregister_instance(**kwargs)

    

    Deletes the resource record sets and the health check, if any, that Amazon Route 53 created for the specified instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/DeregisterInstance>`_    


    **Request Syntax** 
    ::

      response = client.deregister_instance(
          ServiceId='string',
          InstanceId='string'
      )
    :type ServiceId: string
    :param ServiceId: **[REQUIRED]** 

      The ID of the service that the instance is associated with.

      

    
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The value that you specified for ``Id`` in the  RegisterInstance request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OperationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OperationId** *(string) --* 

          A value that you can use to determine whether the request completed successfully. For more information, see  GetOperation .

          
    

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


  .. py:method:: get_instance(**kwargs)

    

    Gets information about a specified instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetInstance>`_    


    **Request Syntax** 
    ::

      response = client.get_instance(
          ServiceId='string',
          InstanceId='string'
      )
    :type ServiceId: string
    :param ServiceId: **[REQUIRED]** 

      The ID of the service that the instance is associated with.

      

    
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The ID of the instance that you want to get information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Instance': {
                'Id': 'string',
                'CreatorRequestId': 'string',
                'Attributes': {
                    'string': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Instance** *(dict) --* 

          A complex type that contains information about a specified instance.

          
          

          - **Id** *(string) --* 

            An identifier that you want to associate with the instance. Note the following:

             

             
            * You can use this value to update an existing instance. 
             
            * To associate a new instance, you must specify a value that is unique among instances that you associate by using the same service. 
             

            
          

          - **CreatorRequestId** *(string) --* 

            An optional parameter that you can use to resolve concurrent creation requests. ``CreatorRequestId`` helps to determine if a specific client owns the namespace.

            
          

          - **Attributes** *(dict) --* 

            A string map that contains attribute keys and values. Supported attribute keys include the following:

             

             
            * ``AWS_INSTANCE_PORT`` : The port on the endpoint that you want Amazon Route 53 to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. For more information, see  CreateService . 
             
            * ``AWS_INSTANCE_IP`` : If the service that you specify contains a resource record set template for an A or AAAA record, the IP address that you want Amazon Route 53 to use for the value of the A record. 
             
            * ``AWS_INSTANCE_WEIGHT`` : The weight value in an SRV record if the service that you specify includes an SRV record. You can also specify a default weight that is applied to all instances in the ``Service`` configuration. For more information, see  CreateService . 
             
            * ``AWS_INSTANCE_PRIORITY`` : The priority value in an SRV record if the service that you specify includes an SRV record. 
             

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
    

  .. py:method:: get_instances_health_status(**kwargs)

    

    Gets the current health status (``Healthy`` , ``Unhealthy`` , or ``Unknown`` ) of one or more instances that are associated with a specified service.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetInstancesHealthStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_instances_health_status(
          ServiceId='string',
          Instances=[
              'string',
          ],
          MaxResults=123,
          NextToken='string'
      )
    :type ServiceId: string
    :param ServiceId: **[REQUIRED]** 

      The ID of the service that the instance is associated with.

      

    
    :type Instances: list
    :param Instances: 

      An array that contains the IDs of all the instances that you want to get the health status for. To get the IDs for the instances that you've created by using a specified service, submit a  ListInstances request.

       

      If you omit ``Instances`` , Amazon Route 53 returns the health status for all the instances that are associated with the specified service.

      

    
      - *(string) --* 

      
  
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of instances that you want Amazon Route 53 to return in the response to a ``GetInstancesHealthStatus`` request. If you don't specify a value for ``MaxResults`` , Amazon Route 53 returns up to 100 instances.

      

    
    :type NextToken: string
    :param NextToken: 

      For the first ``GetInstancesHealthStatus`` request, omit this value.

       

      If more than ``MaxResults`` instances match the specified criteria, you can submit another ``GetInstancesHealthStatus`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Status': {
                'string': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN'
            },
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Status** *(dict) --* 

          A complex type that contains the IDs and the health status of the instances that you specified in the ``GetInstancesHealthStatus`` request.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **NextToken** *(string) --* 

          If more than ``MaxResults`` instances match the specified criteria, you can submit another ``GetInstancesHealthStatus`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

          
    

  .. py:method:: get_namespace(**kwargs)

    

    Gets information about a namespace.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetNamespace>`_    


    **Request Syntax** 
    ::

      response = client.get_namespace(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the namespace that you want to get information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Namespace': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Type': 'DNS_PUBLIC'|'DNS_PRIVATE',
                'Description': 'string',
                'ServiceCount': 123,
                'Properties': {
                    'DnsProperties': {
                        'HostedZoneId': 'string'
                    }
                },
                'CreateDate': datetime(2015, 1, 1),
                'CreatorRequestId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Namespace** *(dict) --* 

          A complex type that contains information about the specified namespace.

          
          

          - **Id** *(string) --* 

            The ID of a namespace.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) that Amazon Route 53 assigns to the namespace when you create it.

            
          

          - **Name** *(string) --* 

            The name of the namespace, such as ``example.com`` .

            
          

          - **Type** *(string) --* 

            The type of the namespace. Valid values are ``DNS_PUBLIC`` and ``DNS_PRIVATE`` .

            
          

          - **Description** *(string) --* 

            The description that you specify for the namespace when you create it.

            
          

          - **ServiceCount** *(integer) --* 

            The number of services that are associated with the namespace.

            
          

          - **Properties** *(dict) --* 

            A complex type that contains information that's specific to the type of the namespace.

            
            

            - **DnsProperties** *(dict) --* 

              A complex type that contains the ID for the hosted zone that Amazon Route 53 creates when you create a namespace.

              
              

              - **HostedZoneId** *(string) --* 

                The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.

                
          
        
          

          - **CreateDate** *(datetime) --* 

            The date that the namespace was created, in Unix date/time format and Coordinated Universal Time (UTC).

            
          

          - **CreatorRequestId** *(string) --* 

            An optional parameter that you can use to resolve concurrent creation requests. ``CreatorRequestId`` helps to determine if a specific client owns the namespace.

            
      
    

  .. py:method:: get_operation(**kwargs)

    

    Gets information about any operation that returns an operation ID in the response, such as a ``CreateService`` request. To get a list of operations that match specified criteria, see  ListOperations .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetOperation>`_    


    **Request Syntax** 
    ::

      response = client.get_operation(
          OperationId='string'
      )
    :type OperationId: string
    :param OperationId: **[REQUIRED]** 

      The ID of the operation that you want to get more information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Operation': {
                'Id': 'string',
                'Type': 'CREATE_NAMESPACE'|'DELETE_NAMESPACE'|'UPDATE_SERVICE'|'REGISTER_INSTANCE'|'DEREGISTER_INSTANCE',
                'Status': 'SUBMITTED'|'PENDING'|'SUCCESS'|'FAIL',
                'ErrorMessage': 'string',
                'ErrorCode': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1),
                'Targets': {
                    'string': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Operation** *(dict) --* 

          A complex type that contains information about the operation.

          
          

          - **Id** *(string) --* 

            The ID of the operation that you want to get information about.

            
          

          - **Type** *(string) --* 

            The name of the operation that is associated with the specified ID.

            
          

          - **Status** *(string) --* 

            The status of the operation. Values include the following:

             

             
            * **SUBMITTED** : This is the initial state immediately after you submit a request. 
             
            * **PENDING** : Amazon Route 53 is performing the operation. 
             
            * **SUCCESS** : The operation succeeded. 
             
            * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` . 
             

            
          

          - **ErrorMessage** *(string) --* 

            If the value of ``Status`` is ``FAIL`` , the reason that the operation failed.

            
          

          - **ErrorCode** *(string) --* 

            The code associated with ``ErrorMessage`` .

            
          

          - **CreateDate** *(datetime) --* 

            The date and time that the request was submitted, in Unix date/time format and Coordinated Universal Time (UTC).

            
          

          - **UpdateDate** *(datetime) --* 

            The date and time that the value of ``Status`` changed to the current value, in Unix date/time format and Coordinated Universal Time (UTC).

            
          

          - **Targets** *(dict) --* 

            The name of the target entity that is associated with the operation:

             

             
            * **NAMESPACE** : The namespace ID is returned in the ``ResourceId`` property. 
             
            * **SERVICE** : The service ID is returned in the ``ResourceId`` property. 
             
            * **INSTANCE** : The instance ID is returned in the ``ResourceId`` property. 
             

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
    

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


  .. py:method:: get_service(**kwargs)

    

    Gets the settings for a specified service.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetService>`_    


    **Request Syntax** 
    ::

      response = client.get_service(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the service that you want to get settings for.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Service': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'InstanceCount': 123,
                'DnsConfig': {
                    'NamespaceId': 'string',
                    'DnsRecords': [
                        {
                            'Type': 'SRV'|'A'|'AAAA',
                            'TTL': 123
                        },
                    ]
                },
                'HealthCheckConfig': {
                    'Type': 'HTTP'|'HTTPS'|'TCP',
                    'ResourcePath': 'string',
                    'FailureThreshold': 123
                },
                'CreateDate': datetime(2015, 1, 1),
                'CreatorRequestId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Service** *(dict) --* 

          A complex type that contains information about the service.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to the service when you created it.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) that Amazon Route 53 assigns to the service when you create it.

            
          

          - **Name** *(string) --* 

            The name of the service.

            
          

          - **Description** *(string) --* 

            The description of the service.

            
          

          - **InstanceCount** *(integer) --* 

            The number of instances that are currently associated with the service. Instances that were previously associated with the service but that have been deleted are not included in the count.

            
          

          - **DnsConfig** *(dict) --* 

            A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

            
            

            - **NamespaceId** *(string) --* 

              The ID of the namespace to use for DNS configuration.

              
            

            - **DnsRecords** *(list) --* 

              An array that contains one ``DnsRecord`` object for each resource record set that you want Amazon Route 53 to create when you register an instance.

              
              

              - *(dict) --* 

                A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

                
                

                - **Type** *(string) --* 

                  The type of the resource, which indicates the value that Amazon Route 53 returns in response to DNS queries. The following values are supported:

                   

                   
                  * **A** : Amazon Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44. 
                   
                  * **AAAA** : Amazon Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345. 
                   
                  * **SRV** : Amazon Route 53 returns the value for an SRV record. The value for an SRV record uses the following template, which can't be changed:  ``priority weight port resource-record-set-name``   The values of ``priority`` and ``weight`` are both set to 1. The value of port comes from the value that you specify for ``Port`` when you submit a  RegisterInstance request. 
                   

                  
                

                - **TTL** *(integer) --* 

                  The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.

                  
            
          
        
          

          - **HealthCheckConfig** *(dict) --* 

             *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Amazon Route 53 associates the health check with all the resource record sets that you specify in ``DnsConfig`` .

             

            .. note::

               

              The health check uses 30 seconds as the request interval. This is the number of seconds between the time that each Amazon Route 53 health checker gets a response from your endpoint and the time that it sends the next health check request. A health checker in each data center around the world sends your endpoint a health check request every 30 seconds. On average, your endpoint receives a health check request about every two seconds. Health checkers in different data centers don't coordinate with one another, so you'll sometimes see several requests per second followed by a few seconds with no health checks at all.

               

             

            For information about the charges for health checks, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing>`__ .

            
            

            - **Type** *(string) --* 

              The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

               

              .. warning::

                 

                You can't change the value of ``Type`` after you create a health check.

                 

               

              You can create the following types of health checks:

               

               
              * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
               
              * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

              .. warning::

                 If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

               
               
              * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
               

               

              For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

              
            

            - **ResourcePath** *(string) --* 

              The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Amazon Route 53 automatically adds the DNS name for the service and a leading forward slash (``/`` ) character. 

              
            

            - **FailureThreshold** *(integer) --* 

              The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

              
        
          

          - **CreateDate** *(datetime) --* 

            The date and time that the service was created, in Unix format and Coordinated Universal Time (UTC).

            
          

          - **CreatorRequestId** *(string) --* 

            An optional parameter that you can use to resolve concurrent creation requests. ``CreatorRequestId`` helps to determine if a specific client owns the namespace.

            
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_instances(**kwargs)

    

    Gets summary information about the instances that you created by using a specified service.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListInstances>`_    


    **Request Syntax** 
    ::

      response = client.list_instances(
          ServiceId='string',
          NextToken='string',
          MaxResults=123
      )
    :type ServiceId: string
    :param ServiceId: **[REQUIRED]** 

      The ID of the service that you want to list instances for.

      

    
    :type NextToken: string
    :param NextToken: 

      For the first ``ListInstances`` request, omit this value.

       

      If more than ``MaxResults`` instances match the specified criteria, you can submit another ``ListInstances`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of instances that you want Amazon Route 53 to return in the response to a ``ListInstances`` request. If you don't specify a value for ``MaxResults`` , Amazon Route 53 returns up to 100 instances.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Instances': [
                {
                    'Id': 'string',
                    'Attributes': {
                        'string': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Instances** *(list) --* 

          Summary information about the instances that are associated with the specified service.

          
          

          - *(dict) --* 

            A complex type that contains information about the instances that you created by using a specified service.

            
            

            - **Id** *(string) --* 

              The ID for an instance that you created by using a specified service.

              
            

            - **Attributes** *(dict) --* 

              A string map that contain attribute keys and values for an instance. Supported attribute keys include the following:

               

               
              * ``AWS_INSTANCE_PORT`` : The port on the endpoint that you want Amazon Route 53 to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. For more information, see  CreateService . 
               
              * ``AWS_INSTANCE_IP`` : If the service that you specify contains a resource record set template for an A or AAAA record, the IP address that you want Amazon Route 53 to use for the value of the A record. 
               

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **NextToken** *(string) --* 

          If more than ``MaxResults`` instances match the specified criteria, you can submit another ``ListInstances`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

          
    

  .. py:method:: list_namespaces(**kwargs)

    

    Gets information about the namespaces that were created by the current AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListNamespaces>`_    


    **Request Syntax** 
    ::

      response = client.list_namespaces(
          NextToken='string',
          MaxResults=123,
          Filters=[
              {
                  'Name': 'TYPE',
                  'Values': [
                      'string',
                  ],
                  'Condition': 'EQ'|'IN'|'BETWEEN'
              },
          ]
      )
    :type NextToken: string
    :param NextToken: 

      For the first ``ListNamespaces`` request, omit this value.

       

      If more than ``MaxResults`` namespaces match the specified criteria, you can submit another ``ListNamespaces`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of namespaces that you want Amazon Route 53 to return in the response to a ``ListNamespaces`` request. If you don't specify a value for ``MaxResults`` , Amazon Route 53 returns up to 100 namespaces.

      

    
    :type Filters: list
    :param Filters: 

      A complex type that contains specifications for the namespaces that you want to list.

       

      If you specify more than one filter, an operation must match all filters to be returned by ListNamespaces.

      

    
      - *(dict) --* 

        A complex type that identifies the namespaces that you want to list. You can choose to list public or private namespaces.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          Specify ``TYPE`` .

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          If you specify ``EQ`` for ``Condition`` , specify either ``DNS_PUBLIC`` or ``DNS_PRIVATE`` .

           

          If you specify ``IN`` for ``Condition`` , you can specify ``DNS_PUBLIC`` , ``DNS_PRIVATE`` , or both.

          

        
          - *(string) --* 

          
      
        - **Condition** *(string) --* 

          The operator that you want to use to determine whether ``ListNamespaces`` returns a namespace. Valid values for ``condition`` include:

           

           
          * ``EQ`` : When you specify ``EQ`` for the condition, you can choose to list only public namespaces or private namespaces, but not both. ``EQ`` is the default condition and can be omitted. 
           
          * ``IN`` : When you specify ``IN`` for the condition, you can choose to list public namespaces, private namespaces, or both.  
           

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Namespaces': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Type': 'DNS_PUBLIC'|'DNS_PRIVATE'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Namespaces** *(list) --* 

          An array that contains one ``NamespaceSummary`` object for each namespace that matches the specified filter criteria.

          
          

          - *(dict) --* 

            A complex type that contains information about a namespace.

            
            

            - **Id** *(string) --* 

              The ID of the namespace.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) that Amazon Route 53 assigns to the namespace when you create it.

              
            

            - **Name** *(string) --* 

              The name of the namespace. When you create a namespace, Amazon Route 53 automatically creates a hosted zone that has the same name as the namespace.

              
            

            - **Type** *(string) --* 

              The type of the namespace, either public or private.

              
        
      
        

        - **NextToken** *(string) --* 

          If more than ``MaxResults`` namespaces match the specified criteria, you can submit another ``ListNamespaces`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

          
    

  .. py:method:: list_operations(**kwargs)

    

    Lists operations that match the criteria that you specify.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListOperations>`_    


    **Request Syntax** 
    ::

      response = client.list_operations(
          NextToken='string',
          MaxResults=123,
          Filters=[
              {
                  'Name': 'NAMESPACE_ID'|'SERVICE_ID'|'STATUS'|'TYPE'|'UPDATE_DATE',
                  'Values': [
                      'string',
                  ],
                  'Condition': 'EQ'|'IN'|'BETWEEN'
              },
          ]
      )
    :type NextToken: string
    :param NextToken: 

      For the first ``ListOperations`` request, omit this value.

       

      If more than ``MaxResults`` operations match the specified criteria, you can submit another ``ListOperations`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of items that you want Amazon Route 53 to return in the response to a ``ListOperations`` request. If you don't specify a value for ``MaxResults`` , Amazon Route 53 returns up to 100 operations.

      

    
    :type Filters: list
    :param Filters: 

      A complex type that contains specifications for the operations that you want to list, for example, operations that you started between a specified start date and end date.

       

      If you specify more than one filter, an operation must match all filters to be returned by ``ListOperations`` .

      

    
      - *(dict) --* 

        A complex type that lets you select the operations that you want to list.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          Specify the operations that you want to get:

           

           
          * **NAMESPACE_ID** : Gets operations related to specified namespaces. 
           
          * **SERVICE_ID** : Gets operations related to specified services. 
           
          * **STATUS** : Gets operations based on the status of the operations: ``SUBMITTED`` , ``PENDING`` , ``SUCCEED`` , or ``FAIL`` . 
           
          * **TYPE** : Gets specified types of operation. 
           
          * **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.  
           

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          Specify values that are applicable to the value that you specify for ``Name`` : 

           

           
          * **NAMESPACE_ID** : Specify one namespace ID. 
           
          * **SERVICE_ID** : Specify one service ID. 
           
          * **STATUS** : Specify one or more statuses: ``SUBMITTED`` , ``PENDING`` , ``SUCCEED`` , or ``FAIL`` . 
           
          * **TYPE** : Specify one or more of the following types: ``CREATE_NAMESPACE`` , ``DELETE_NAMESPACE`` , ``UPDATE_SERVICE`` , ``REGISTER_INSTANCE`` , or ``DEREGISTER_INSTANCE`` . 
           
          * **UPDATE_DATE** : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. 
           

          

        
          - *(string) --* 

          
      
        - **Condition** *(string) --* 

          The operator that you want to use to determine whether an operation matches the specified value. Valid values for condition include:

           

           
          * ``EQ`` : When you specify ``EQ`` for the condition, you can specify only one value. ``EQ`` is supported for ``NAMESPACE_ID`` , ``SERVICE_ID`` , ``STATUS`` , and ``TYPE`` . ``EQ`` is the default condition and can be omitted. 
           
          * ``IN`` : When you specify ``IN`` for the condition, you can specify a list of one or more values. ``IN`` is supported for ``STATUS`` and ``TYPE`` . An operation must match one of the specified values to be returned in the response. 
           
          * ``BETWEEN`` : Specify two values, a start date and an end date. The start date must be the first value. ``BETWEEN`` is supported for ``U`` .  
           

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Operations': [
                {
                    'Id': 'string',
                    'Status': 'SUBMITTED'|'PENDING'|'SUCCESS'|'FAIL'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Operations** *(list) --* 

          Summary information about the operations that match the specified criteria.

          
          

          - *(dict) --* 

            A complex type that contains information about an operation that matches the criteria that you specified in a  ListOperations request.

            
            

            - **Id** *(string) --* 

              The ID for an operation.

              
            

            - **Status** *(string) --* 

              The status of the operation. Values include the following:

               

               
              * **SUBMITTED** : This is the initial state immediately after you submit a request. 
               
              * **PENDING** : Amazon Route 53 is performing the operation. 
               
              * **SUCCESS** : The operation succeeded. 
               
              * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` . 
               

              
        
      
        

        - **NextToken** *(string) --* 

          If more than ``MaxResults`` operations match the specified criteria, you can submit another ``ListOperations`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

          
    

  .. py:method:: list_services(**kwargs)

    

    Gets settings for all the services that are associated with one or more specified namespaces.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListServices>`_    


    **Request Syntax** 
    ::

      response = client.list_services(
          NextToken='string',
          MaxResults=123,
          Filters=[
              {
                  'Name': 'NAMESPACE_ID',
                  'Values': [
                      'string',
                  ],
                  'Condition': 'EQ'|'IN'|'BETWEEN'
              },
          ]
      )
    :type NextToken: string
    :param NextToken: 

      For the first ``ListServices`` request, omit this value.

       

      If more than ``MaxResults`` services match the specified criteria, you can submit another ``ListServices`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of services that you want Amazon Route 53 to return in the response to a ``ListServices`` request. If you don't specify a value for ``MaxResults`` , Amazon Route 53 returns up to 100 services.

      

    
    :type Filters: list
    :param Filters: 

      A complex type that contains specifications for the namespaces that you want to list services for. 

       

      If you specify more than one filter, an operation must match all filters to be returned by ``ListServices`` .

      

    
      - *(dict) --* 

        A complex type that lets you specify the namespaces that you want to list services for.

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          Specify ``NAMESPACE_ID`` .

          

        
        - **Values** *(list) --* **[REQUIRED]** 

          The values that are applicable to the value that you specify for ``Condition`` to filter the list of services.

          

        
          - *(string) --* 

          
      
        - **Condition** *(string) --* 

          The operator that you want to use to determine whether a service is returned by ``ListServices`` . Valid values for ``Condition`` include the following:

           

           
          * ``EQ`` : When you specify ``EQ`` , specify one namespace ID for ``Values`` . ``EQ`` is the default condition and can be omitted. 
           
          * ``IN`` : When you specify ``IN`` , specify a list of the IDs for the namespaces that you want ``ListServices`` to return a list of services for. 
           

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Services': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'InstanceCount': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Services** *(list) --* 

          An array that contains one ``ServiceSummary`` object for each service that matches the specified filter criteria.

          
          

          - *(dict) --* 

            A complex type that contains information about a specified service.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to the service when you created it.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) that Amazon Route 53 assigns to the service when you create it.

              
            

            - **Name** *(string) --* 

              The name of the service.

              
            

            - **Description** *(string) --* 

              The description that you specify when you create the service.

              
            

            - **InstanceCount** *(integer) --* 

              The number of instances that are currently associated with the service. Instances that were previously associated with the service but that have been deleted are not included in the count.

              
        
      
        

        - **NextToken** *(string) --* 

          If more than ``MaxResults`` operations match the specified criteria, the value of ``NextToken`` is the first service in the next group of services that were created by the current AWS account. To get the next group, specify the value of ``NextToken`` from the previous response in the next request.

          
    

  .. py:method:: register_instance(**kwargs)

    

    Creates one or more resource record sets and optionally a health check based on the settings in a specified service. When you submit a ``RegisterInstance`` request, Amazon Route 53 does the following:

     

     
    * Creates a resource record set for each resource record set template in the service 
     
    * Creates a health check based on the settings in the health check template in the service, if any 
     
    * Associates the health check, if any, with each of the resource record sets 
     

     

    .. warning::

       

      One ``RegisterInstance`` request must complete before you can submit another request and specify the same service and instance ID.

       

     

    For more information, see  CreateService .

     

    When Amazon Route 53 receives a DNS query for the specified DNS name, it returns the applicable value:

     

     
    * **If the health check is healthy** : returns all the resource record sets 
     
    * **If the health check is unhealthy** : returns the IP address of the last healthy instance 
     
    * **If you didn't specify a health check template** : returns all the resource record sets 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/RegisterInstance>`_    


    **Request Syntax** 
    ::

      response = client.register_instance(
          ServiceId='string',
          InstanceId='string',
          CreatorRequestId='string',
          Attributes={
              'string': 'string'
          }
      )
    :type ServiceId: string
    :param ServiceId: **[REQUIRED]** 

      The ID of the service that you want to use for settings for the resource record sets and health check that Amazon Route 53 will create.

      

    
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      An identifier that you want to associate with the instance. Note the following:

       

       
      * You can use this value to update an existing instance. 
       
      * To register a new instance, you must specify a value that is unique among instances that you register by using the same service. 
       

      

    
    :type CreatorRequestId: string
    :param CreatorRequestId: 

      An optional parameter that you can use to resolve concurrent creation requests. ``CreatorRequestId`` helps to determine if a specific client owns the namespace.

      This field is autopopulated if not provided.

    
    :type Attributes: dict
    :param Attributes: **[REQUIRED]** 

      A string map that contain attribute keys and values. Supported attribute keys include the following:

       

       
      * ``AWS_INSTANCE_PORT`` : The port on the endpoint that you want Amazon Route 53 to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. For more information, see  CreateService . 
       
      * ``AWS_INSTANCE_IPV4`` : If the service that you specify contains a resource record set template for an A record, the IPv4 address that you want Amazon Route 53 to use for the value of the A record. 
       
      * ``AWS_INSTANCE_IPV6`` : If the service that you specify contains a resource record set template for an AAAA record, the IPv6 address that you want Amazon Route 53 to use for the value of the AAAA record. 
       

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OperationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OperationId** *(string) --* 

          A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .

          
    

  .. py:method:: update_service(**kwargs)

    

    Updates the TTL setting for a specified service. You must specify all the resource record set templates (and, optionally, a health check template) that you want to appear in the updated service. Any current resource record set templates (or health check template) that don't appear in an ``UpdateService`` request are deleted.

     

    When you update the TTL setting for a service, Amazon Route 53 also updates the corresponding settings in all the resource record sets and health checks that were created by using the specified service.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/UpdateService>`_    


    **Request Syntax** 
    ::

      response = client.update_service(
          Id='string',
          Service={
              'Description': 'string',
              'DnsConfig': {
                  'DnsRecords': [
                      {
                          'Type': 'SRV'|'A'|'AAAA',
                          'TTL': 123
                      },
                  ]
              },
              'HealthCheckConfig': {
                  'Type': 'HTTP'|'HTTPS'|'TCP',
                  'ResourcePath': 'string',
                  'FailureThreshold': 123
              }
          }
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the service that you want to update.

      

    
    :type Service: dict
    :param Service: **[REQUIRED]** 

      A complex type that contains the new settings for the service.

      

    
      - **Description** *(string) --* 

        A description for the service.

        

      
      - **DnsConfig** *(dict) --* **[REQUIRED]** 

        A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

        

      
        - **DnsRecords** *(list) --* **[REQUIRED]** 

          An array that contains one ``DnsRecord`` object for each resource record set that you want Amazon Route 53 to create when you register an instance.

          

        
          - *(dict) --* 

            A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

            

          
            - **Type** *(string) --* **[REQUIRED]** 

              The type of the resource, which indicates the value that Amazon Route 53 returns in response to DNS queries. The following values are supported:

               

               
              * **A** : Amazon Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44. 
               
              * **AAAA** : Amazon Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345. 
               
              * **SRV** : Amazon Route 53 returns the value for an SRV record. The value for an SRV record uses the following template, which can't be changed:  ``priority weight port resource-record-set-name``   The values of ``priority`` and ``weight`` are both set to 1. The value of port comes from the value that you specify for ``Port`` when you submit a  RegisterInstance request. 
               

              

            
            - **TTL** *(integer) --* **[REQUIRED]** 

              The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.

              

            
          
      
      
      - **HealthCheckConfig** *(dict) --* 

         *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Amazon Route 53 associates the health check with all the resource record sets that you specify in ``DnsConfig`` .

         

        .. note::

           

          The health check uses 30 seconds as the request interval. This is the number of seconds between the time that each Amazon Route 53 health checker gets a response from your endpoint and the time that it sends the next health check request. A health checker in each data center around the world sends your endpoint a health check request every 30 seconds. On average, your endpoint receives a health check request about every two seconds. Health checkers in different data centers don't coordinate with one another, so you'll sometimes see several requests per second followed by a few seconds with no health checks at all.

           

         

        For information about the charges for health checks, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing>`__ .

        

      
        - **Type** *(string) --* 

          The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

           

          .. warning::

             

            You can't change the value of ``Type`` after you create a health check.

             

           

          You can create the following types of health checks:

           

           
          * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
           
          * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

          .. warning::

             If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

           
           
          * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
           

           

          For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

          

        
        - **ResourcePath** *(string) --* 

          The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Amazon Route 53 automatically adds the DNS name for the service and a leading forward slash (``/`` ) character. 

          

        
        - **FailureThreshold** *(integer) --* 

          The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OperationId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OperationId** *(string) --* 

          A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .

          
    

==========
Paginators
==========


The available paginators are:
